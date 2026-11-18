# Stack

**For the agent:** read before writing code. This file is the AI Unified Process record of the technical layers,
independent of how the team documents its architecture. The Layers table says which layer skill builds and tests
each technical layer: `/use-case-implement` runs the Skill column bottom-up, `/use-case-test` runs the Test skill
column from the integration layer up, and `/use-case-coverage` searches for the markers in the last table.

**Last updated:** 2026-11-18

## Layers

| Layer | Technology | Skill | Test skill | Location |
| --- | --- | --- | --- | --- |
| Migration | Flyway (PostgreSQL) | `flyway-schema` | – | `src/main/resources/db/migration` |
| Persistence | jOOQ (PostgreSQL) | `jooq-persistence` | `jooq-persistence-test` | `<feature>.domain` |
| Client | – | – | – | – |
| Service | Spring Boot | `spring-service` | `spring-service-test` | `<feature>.domain` |
| API | – | – | – | – |
| UI | Vaadin Flow | `vaadin-flow-ui` | `vaadin-flow-ui-test` | `<feature>.ui`, `core.ui` |
| E2E | Playwright for Java with Drama Finder | – | `vaadin-e2e-test` | `src/test/java` |

**Integration layer:**

| Use case offered through | Tested in | Test skill |
| --- | --- | --- |
| UI | UI | `vaadin-flow-ui-test` |
| Service | Service | `spring-service-test` |

Both integration test skills run in process against PostgreSQL. Vaadin Flow Browserless tests exercise the
UI and the layers it calls. Service integration tests cover use cases offered directly through the service.
A use case uses the first row named in its `**Layers:**` line, or the UI row when it has no such line.

**E2E scope:** Use cases and test cases

The product owner confirmed this scope on 2026-11-18 at 14:40:28 UTC for the Book Library #65 pilot.
It covers UI use cases and test-case journeys.

Constraints C-002 through C-006 record Java 25, Spring Boot with Vaadin Flow, PostgreSQL, jOOQ, and Flyway.
The [package architecture](../architecture.md) places the service between the Vaadin view and the repository
and gives the service the transaction boundary.

## Module layout

The checkout is a single Maven module with root Java package `ai.unified.process.demo.book.library`.
Each feature has a `ui` package for views and a `domain` package for services, repositories, and records.
Shared UI, configuration, and security live under `core`. jOOQ generates schema classes into
`ai.unified.process.demo.book.library.db`.

Java sources and tests live under `src/main/java` and `src/test/java`. Flyway migrations live in
`src/main/resources/db/migration`. Browserless tests run with the Maven test phase, and Failsafe
runs browser integration tests named `*IT`.

## Commands

| Purpose | Command |
| --- | --- |
| Build | `./mvnw clean package -Pproduction` |
| Unit tests | `./mvnw test` |
| Integration tests (Browserless UI) | `./mvnw test` |
| End-to-end tests | `./mvnw verify` |

On Windows the wrapper is `.\mvnw.cmd`.

## Markers

Each layer skill keeps its own rows here. It checks the rows against its marker reference and corrects them
when it runs.

| Layer | Skill | Kind | Marker to grep for |
| --- | --- | --- | --- |
| All | – | Code | `// UC-XXX BR-YYY:` directly above the method, query condition, or validator that enforces the rule |
