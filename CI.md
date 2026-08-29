# Continuous Integration (CI) - GitHub Actions

## 1. Overview

Continuous Integration (CI) was implemented for the DevOps CRM project using GitHub Actions.

The CI workflow is automatically triggered when a Pull Request is opened or updated. It also runs when changes are pushed to the main branch.

The workflow validates the project by:

- Installing dependencies
- Running lint checks
- Running TypeScript type checks
- Running unit tests
- Running integration tests
- Building the application

If any required step fails, the CI job fails.

---

## 2. Workflow File

The workflow is defined in:

`.github/workflows/ci.yml`

Workflow name:

`CI`

---

## 3. Workflow Trigger

The workflow uses:

```yaml
on:
  push:
    branches:
      - main
  pull_request: {}
```
---

## 4. Runner

The CI workflow runs on a GitHub-hosted Ubuntu runner.

The runner is configured as:

```yaml
runs-on: ubuntu-latest
```
---

## 5. Permissions

The workflow uses read-only access to repository contents:

```yaml
permissions:
  contents: read
```
---

## 6. Concurrency

The workflow uses concurrency control:

```yaml
concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true
```
---

## 7. CI Workflow Steps

The CI workflow performs the following steps in order.

### 7.1 Checkout

```yaml
- name: Checkout
  uses: actions/checkout@v4
```

### 7.2 Spawn Twenty Test Instance

```yaml
- name: Spawn Twenty test instance
  id: twenty
  uses: twentyhq/twenty/.github/actions/spawn-twenty-app-dev-test@main
  with:
    twenty-version: ${{ env.TWENTY_VERSION }}
```
---

### 7.3 Enable Corepack

```yaml
- name: Enable Corepack
  run: corepack enable
```
---

### 7.4 Setup Node.js

```yaml
- name: Setup Node.js
  uses: actions/setup-node@v4
  with:
    node-version-file: '.nvmrc'
    cache: yarn
```
---

### 7.5 Install Dependencies

```yaml
- name: Install dependencies
  run: yarn install --immutable
```
---

### 7.6 Lint

```yaml
- name: Lint
  run: yarn lint
```
---

### 7.7 Typecheck

```yaml
- name: Typecheck
  run: yarn typecheck
```
---

### 7.8 Unit Tests

```yaml
- name: Unit tests
  run: yarn test:unit
```
---

### 7.9 Integration Tests

```yaml
- name: Run integration tests
  run: yarn test
  env:
    TWENTY_API_URL: ${{ steps.twenty.outputs.server-url }}
    TWENTY_API_KEY: ${{ steps.twenty.outputs.api-key }}
```
---

### 7.10 Build Application

```yaml
- name: Build application
  run: yarn twenty dev:build
```
---

## 8. Failure Handling

The CI workflow is designed to fail when any required validation step fails.

The workflow does not use `continue-on-error` for the required steps.

Therefore, if any of the following commands fails, the CI job fails:

- Dependency installation
- Linting
- Type checking
- Unit tests
- Integration tests
- Application build

This ensures that a Pull Request receives a successful CI result only when all required validation stages complete successfully.

---

## 9. Existing CI Workflow

The repository already contained a GitHub Actions CI workflow before this task.

The existing workflow already included:

- Checkout
- Twenty test instance setup
- Corepack enablement
- Node.js setup
- Dependency installation
- Linting
- Type checking
- Unit tests
- Integration tests

However, the application build step was not included in the existing workflow.

Therefore, the main change made for this task was to add an application build step.

---

## 10. Change Made for This Task

The following application build step was added to the existing CI workflow:

```yaml
- name: Build application
  run: yarn twenty dev:build
```
---

### 11. Local CI Commands

```bash
yarn install --immutable
yarn lint
yarn typecheck
yarn test:unit
yarn test
yarn twenty dev:build
```
This command sequence represents the main validation stages performed by the CI workflow.

---

## 12. CI Branch

The CI implementation was created on the following branch:

`Karthikeyan-ci`

The branch was created from the `main` branch.

---

## 13. Pull Request Verification

After the CI changes are committed and pushed to GitHub, a Pull Request will trigger the CI workflow automatically.

The Pull Request should display the GitHub Actions `CI` check.

The expected workflow stages are:

```text
Checkout
    ↓
Spawn Twenty test instance
    ↓
Enable Corepack
    ↓
Setup Node.js
    ↓
Install dependencies
    ↓
Lint
    ↓
Typecheck
    ↓
Unit tests
    ↓
Integration tests
    ↓
Build application
```
---

## 14. Issues Faced

The repository already contained a GitHub Actions CI workflow.

However, the existing workflow did not include an application build step.

The project also does not define a separate `build` script in `package.json`.

Therefore, using:

```bash
yarn build
```

---

## 15. Solution

```yaml
- name: Build application
  run: yarn twenty dev:build
```
This command was selected because the project does not define a separate `build` script in `package.json`.

The same command was successfully tested during the local application setup.

The build step was added as the final validation stage of the CI workflow.

---

## 16. CI Verification

After the CI workflow changes are pushed to GitHub, the Pull Request should automatically trigger the `CI` workflow.

The GitHub Actions run should show the following stages:

```text
Checkout
↓
Spawn Twenty test instance
↓
Enable Corepack
↓
Setup Node.js
↓
Install dependencies
↓
Lint
↓
Typecheck
↓
Unit tests
↓
Integration tests
↓
Build application
```
---

## 17. Loom Video

The Loom video will demonstrate the CI workflow running on the Pull Request.

The video will cover:

- The GitHub Actions workflow file.
- The Pull Request.
- The CI workflow triggering automatically.
- Dependency installation.
- Lint checks.
- Type checking.
- Unit tests.
- Integration tests.
- Application build.
- Successful CI result.

Loom Video:

https://www.loom.com/share/d51143ead8b141adbc306b74a9682513

---

## 18. Final Outcome

The GitHub Actions CI workflow now covers all the required Continuous Integration stages.

The final workflow validates:

- Pull Request trigger
- Dependency installation
- Linting
- Type checking
- Unit tests
- Integration tests
- Application build
- Failure handling

The CI workflow file is:

```text
.github/workflows/ci.yml
```
---
