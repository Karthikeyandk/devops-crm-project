# syntax=docker/dockerfile:1

# Build stage
FROM node:24-alpine AS builder

WORKDIR /app

# Enable Corepack so Yarn 4 can be used
RUN corepack enable

# Copy dependency metadata first for better layer caching
COPY package.json yarn.lock .yarnrc.yml ./

# The project uses a patched Twenty SDK
COPY .yarn/patches .yarn/patches

# Install dependencies
RUN yarn install

# Copy application source
COPY src ./src
COPY public ./public
COPY tsconfig.json tsconfig.spec.json vitest.config.ts vitest.unit.config.ts .oxlintrc.json ./

# Build the Twenty application
RUN yarn twenty dev:build


# Runtime stage
FROM node:24-alpine AS runtime

WORKDIR /app

RUN corepack enable

# Create a non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copy the project files and installed dependencies from the builder
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/yarn.lock ./yarn.lock
COPY --from=builder /app/.yarnrc.yml ./.yarnrc.yml
COPY --from=builder /app/.yarn ./.yarn
COPY --chown=appuser:appgroup --from=builder /app/node_modules ./node_modules
COPY --chown=appuser:appgroup --from=builder /app/.twenty/output ./.twenty/output

COPY --from=builder /app/src ./src
COPY --from=builder /app/public ./public
COPY --from=builder /app/tsconfig.json ./tsconfig.json
COPY --from=builder /app/tsconfig.spec.json ./tsconfig.spec.json
COPY --from=builder /app/.oxlintrc.json ./.oxlintrc.json
COPY --from=builder /app/vitest.config.ts ./vitest.config.ts
COPY --from=builder /app/vitest.unit.config.ts ./vitest.unit.config.ts

# Run as non-root
USER appuser

# The Twenty app does not expose its own HTTP server.
# The container performs a one-shot application sync.
CMD ["yarn", "twenty", "apply"]
