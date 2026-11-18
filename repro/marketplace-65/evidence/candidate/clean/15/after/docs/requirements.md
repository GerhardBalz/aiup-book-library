# Book Library Requirements

This draft covers the first release described in [the vision](vision.md). [The architecture](architecture.md), [the README](../README.md), and [the tutorial](../TUTORIAL.md) supply checkout-specific details.

## Functional Requirements

| ID | Title | User Story | Priority | Status |
| --- | --- | --- | --- | --- |
| FR-001 | Sign in as a Member | As a Member, I want to sign in with my User Account so that I can access my Loans. | High | Open |
| FR-002 | Sign in as a Librarian | As a Librarian, I want to sign in with my User Account so that I can access librarian functions. | High | Open |
| FR-003 | Search the Catalog as a Member | As a Member, I want to search the Catalog so that I can find Books without asking a Librarian. | High | Open |
| FR-004 | Search the Catalog as a Librarian | As a Librarian, I want to search the Catalog so that I can help Members find Books. | High | Open |
| FR-005 | Check Book availability | As a Member, I want to see how many Copies of a Book are available so that I can choose a Book to borrow. | High | Open |
| FR-006 | Borrow a Book | As a Member, I want to borrow an available Copy of a Book so that I can take it out on Loan. | High | Open |
| FR-007 | Return a Book | As a Member, I want to record the return of a Book I borrowed so that my Active Loan closes and another Member can borrow the Copy. | High | Open |
| FR-008 | View my Loans | As a Member, I want to view my own Loans so that I can see what I have borrowed. | High | Open |
| FR-009 | View all Active Loans | As a Librarian, I want to view all Active Loans so that I can see which Member has each borrowed Book. | High | Open |
| FR-010 | View Loan History | As a Librarian, I want to view Loan History so that I can trace who borrowed each Book and when. | Medium | Open |
| FR-011 | Add Books | As a Librarian, I want to add Books to the Catalog so that Members can find newly acquired Books. | High | Open |
| FR-012 | Update Books | As a Librarian, I want to update Book details in the Catalog so that Members can find Books using accurate information. | Medium | Open |
| FR-013 | Remove Books from the Catalog | As a Librarian, I want to remove Books from the Catalog, withdrawing any Book with Loan History while retaining its record and Loan History so that Members see the current collection and I can trace past Loans. | Medium | Open |
| FR-014 | Create Member accounts | As a Librarian, I want to manually create a User Account for a Member so that the Member can sign in without self-service registration. | High | Open |

## Non-Functional Requirements

| ID | Title | Requirement | Category | Priority | Status |
| --- | --- | --- | --- | --- | --- |
| NFR-001 | Authenticated library actions | Every library action after sign-in requires an authenticated User Account and is attributable to exactly one User Account. | Security | High | Open |
| NFR-002 | Librarian-only access | Zero librarian-only views are accessible to Members. | Security | High | Open |
| NFR-003 | Member Loan privacy | A Member can retrieve zero Loans belonging to another Member. | Security | High | Open |
| NFR-004 | Current Active Loans | A committed borrow or return must be reflected by the first subsequent retrieval of the Active Loans view. | Performance | High | Open |
| NFR-005 | Feature package structure | Each feature package has exactly two subpackages, `ui` and `domain`. | Maintainability | High | Open |

## Constraints

| ID | Title | Constraint | Category | Priority | Status |
| --- | --- | --- | --- | --- | --- |
| C-001 | Web application | Book Library is delivered as a web application. | Technical | High | Open |
| C-002 | Runtime | The backend runs on Java 25. | Technical | High | Open |
| C-003 | Web framework | The web application uses Spring Boot and Vaadin Flow. | Technical | High | Open |
| C-004 | Database | Book Library stores persistent data in PostgreSQL. | Technical | High | Open |
| C-005 | Database access | Persistence uses jOOQ. | Technical | High | Open |
| C-006 | Schema migrations | Database schema changes use Flyway. | Technical | High | Open |
| C-007 | Single branch | The release supports one library branch. | Business | High | Open |
| C-008 | No payments | Payment handling is outside release scope. | Business | High | Open |
| C-009 | No fines | Fine handling is outside release scope. | Business | High | Open |
| C-010 | No reservations | Book reservations are outside release scope. | Business | High | Open |
| C-011 | No waiting lists | Book waiting lists are outside release scope. | Business | High | Open |
| C-012 | Manual registration | Self-service sign-up is outside release scope. | Business | High | Open |
| C-013 | No password reset | Self-service password reset is outside release scope. | Business | High | Open |
| C-014 | No social login | Social login is outside release scope. | Business | High | Open |
