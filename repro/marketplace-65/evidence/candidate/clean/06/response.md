Created and validated [docs/architecture/stack.md](docs/architecture/stack.md) for the Book Library checkout. All referenced layer skills are installed.

| Layer | Technology |
| --- | --- |
| Migration | Flyway with PostgreSQL |
| Persistence | jOOQ |
| Service | Spring Boot |
| UI | Vaadin Flow |
| E2E | Playwright for Java with Drama Finder |
| Client and API | Absent |

UI use cases integrate through Vaadin Flow Browserless tests. Use cases offered directly through the service integrate through Spring service tests. The stack records your E2E scope of **Use cases and test cases**.

Default AI Unified Process decision rights apply. Validation checked the Markdown structure, installed skills, integration rows, E2E scope, and marker. No application or browser workloads ran.