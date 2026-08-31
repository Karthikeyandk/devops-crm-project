# Docker Containerization

## 1. Overview

This project is a Twenty CRM application developed using the Twenty SDK.

The Docker setup containerizes the application workflow and runs the required Twenty CRM services using Docker Compose.

The setup includes:

- PostgreSQL for persistent database storage
- Redis for caching and background-job support
- Twenty CRM server
- Twenty worker
- Custom application container for building and syncing the Twenty app

Docker Compose is used to define and run the multi-container application stack.

## 2. Application Structure

The project is a Twenty application rather than a standalone Node.js web server.

Important project files include:

- `src/application-config.ts`
- `src/front-components/`
- `src/navigation-menu-items/`
- `src/page-layouts/`
- `src/__tests__/`
- `package.json`
- `yarn.lock`
- `.yarnrc.yml`

The application uses:

- Node.js 24
- Yarn 4.13.0
- Twenty SDK 2.35.1
- React 19
- TypeScript
- Vitest
- Oxlint

## 3. Docker Architecture

```text
                    Docker Compose
                         |
        +----------------+----------------+
        |                |                |
      Server           Worker            App
        |                                 |
        |                                 |
     PostgreSQL                         Twenty CLI
        |                              build + sync
        |
      Redis
```

## 4. Dockerfile

The Dockerfile uses a multi-stage build.

### Build stage

The builder stage:

- Uses Node.js 24 Alpine.
- Enables Corepack.
- Installs Yarn 4 dependencies.
- Preserves the local Twenty SDK patch.
- Copies application source.
- Runs:

```bash
yarn twenty dev:build
```

### Runtime stage

.env
## 6. Environment Variables

The application uses a local `.env` file.

Example:

```env
TWENTY_API_URL=http://server:3000


```text
.env*
API keys should never be committed to the repository.

```text
http://server:3000
```
The service name `server` is used instead of `localhost` because Compose services communicate using their service names on the Docker network.

## 7. Ports

The Twenty server maps:

```text
Container: 3000
```

Therefore the application is available from the host at:

```text
http://localhost:2020
```

## 8. Networking

Docker Compose creates a default project network.

All services are attached to the same network.

The application container can reach the Twenty server using:

```text
server:3000
```

PostgreSQL is reached using:

```text
db:5432
```

Redis is reached using:

```text
redis:6379
```

## 9. Volumes

Two named volumes are used.

### PostgreSQL volume

`db-data`

Mounted at:

```text
/var/lib/postgresql/data
```

### Twenty server storage

`server-local-data`

Mounted at:

```text
/app/packages/twenty-server/.local-storage
```

Named volumes provide persistent data storage for Compose services.

## 10. Healthchecks and Startup Order
Host:      2020


Inside the Docker Compose network, the Twenty server is reached using:
```


The `.env` file is excluded from Git using:
TWENTY_API_KEY=<local-api-key>
```
The PostgreSQL service uses `pg_isready` to verify database availability.


The `.yarn/patches` directory is intentionally not ignored because the project uses a patched Twenty SDK dependency.
```

Redis uses:

.env.*
dist
*.log
The runtime stage:
```bash
coverage

.github
- Uses Node.js 24 Alpine.
redis-cli ping
```
- Copies the required application files and dependencies.
.git
node_modules
.twenty

The Twenty server uses:

```text
- Creates a non-root `appuser`.
- Uses `appuser` instead of root.
```text
- Uses `COPY --chown` for writable application files.
/healthz
```



The runtime command is:

The server waits for PostgreSQL and Redis to become healthy.
The `.dockerignore` excludes unnecessary files from the Docker build context, including:



## 11. .dockerignore
```bash
```

The worker and application wait for the Twenty server to become healthy.


Compose supports `service_healthy` dependencies so a dependent service waits for the dependency healthcheck to pass.


## 12. Loom Demonstration

A Loom video demonstrating the Docker containerization setup, application build, Docker Compose services, Twenty application sync, and verification steps is available below.

**Loom Video:**
https://www.loom.com/share/4a13b9de003245f3b6e9e858c73f4321

