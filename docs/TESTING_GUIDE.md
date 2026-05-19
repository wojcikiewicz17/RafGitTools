# Testing Guide — RafGitTools

## Scope and source of truth
This guide defines the executable test/build matrix used locally and in GitHub Actions.
It matches the current Android flavors (`dev`, `production`), build types (`debug`, `release`) and ABIs (`armeabi-v7a`, `arm64-v8a`).

## Environment baseline
- JDK: 17
- Android SDK: platform 34 + build-tools 34.0.0
- NDK: 26.3.11579264
- CMake: 3.22.1

Bootstrap helpers:
- `./scripts/prepare_local_properties.sh`
- `./scripts/gradlew_with_java17.sh`

## Test taxonomy

### 1) Unit tests (JVM)
Run deterministic JVM tests without device/emulator.

```bash
./scripts/gradlew_with_java17.sh testDevDebugUnitTest testProductionDebugUnitTest --stacktrace
```

### 2) Integration tests (module-level integration)
Run use case/service integration in JVM layer (same task bucket as unit in current project layout).

```bash
./scripts/gradlew_with_java17.sh testDevDebugUnitTest --tests '*JGit*' --stacktrace
./scripts/gradlew_with_java17.sh testDevDebugUnitTest --tests '*Github*' --stacktrace
```

### 3) UI tests (instrumented)
Requires connected device/emulator.

```bash
./scripts/gradlew_with_java17.sh connectedDevDebugAndroidTest --stacktrace
```

### 4) E2E (workflow-level)
Current E2E definition is CI pipeline orchestration:
- build variants,
- unit tests,
- lint,
- artifact upload,
- APK ABI/signature validation.

Workflows:
- `.github/workflows/ci.yml`
- `.github/workflows/android-ci.yml`
- `.github/workflows/internal-validation.yml`
- `.github/workflows/release.yml`

## Build matrix commands

### Debug builds (local and CI)
```bash
./scripts/gradlew_with_java17.sh assembleDevDebug assembleProductionDebug --stacktrace
```

### Release validation build (unsigned lane, internal only)
```bash
ALLOW_UNSIGNED_RELEASE=true ./scripts/gradlew_with_java17.sh assembleProductionRelease --stacktrace
./scripts/native/verify_apks.sh
```

### Official release build (signed, mandatory)
Do not set `ALLOW_UNSIGNED_RELEASE=true`.

Required secrets/props:
- `RELEASE_STORE_FILE`
- `RELEASE_STORE_PASSWORD`
- `RELEASE_KEY_ALIAS`
- `RELEASE_KEY_PASSWORD`

```bash
./scripts/gradlew_with_java17.sh assembleProductionRelease --stacktrace --info
./scripts/native/verify_apks.sh
```

## Coverage targets (progressive)
Coverage targets are gated by real report artifacts (`app/build/reports/tests/` and tooling output).

- Stage 1: 15%
- Stage 2: 25%
- Stage 3: 40%
- Stage 4: 80%

Rule: never claim target progression without attached report files in CI artifacts.

## Artifact validation
Always validate produced APKs after release builds:

```bash
./scripts/native/verify_apks.sh
```

Validation checks:
- APK inventory and size report.
- Required ABIs present in each APK: `armeabi-v7a` and `arm64-v8a`.
- Signature state (signed vs unsigned) according to lane.
- Signed/unsigned size delta report when both artifacts exist.
