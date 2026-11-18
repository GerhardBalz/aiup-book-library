# Book Library Requirements

Draft catalog based on the Book Library vision, architecture, and tutorial.

## Functional Requirements

| ID | Title | User Story | Priority | Status |
| --- | --- | --- | --- | --- |
| FR-001 | Search the Catalog as a Member | As a Member, I want to search the Catalog and see which Books have an available Book Copy so that I can find a Book to borrow on my own. | High | Open |
| FR-002 | Borrow a Book | As a Member, I want to borrow an available Book Copy so that the library records that I have it. | High | Open |
| FR-003 | Return a Book | As a Member, I want to return a Book Copy on one of my Active Loans so that it becomes available to other Members. | High | Open |
| FR-004 | View Active Loans | As a Librarian, I want to see all Active Loans and their Members, Books, and borrowing dates so that I know who has each borrowed Book. | High | Open |
| FR-005 | Add a Book | As a Librarian, I want to add a Book to the Catalog so that Members can find it. | High | Open |
| FR-006 | Edit a Book | As a Librarian, I want to edit a Book in the Catalog so that Members can rely on its details. | Medium | Open |
| FR-007 | Remove a Book from the Catalog | As a Librarian, I want to withdraw a Book from the Catalog while preserving its Loan History so that Members see the current collection and past borrowing remains traceable. | Medium | Open |
| FR-008 | Create a Member Account | As a Librarian, I want to create a User Account for a Member manually so that the Member can sign in and borrow Books. | High | Open |
| FR-009 | View My Loans | As a Member, I want to see my own Active Loans and completed Loans so that I know what to return and can check what I borrowed before. | High | Open |
| FR-010 | Search the Catalog as a Librarian | As a Librarian, I want to search the Catalog and see which Books have an available Book Copy so that I can answer Members' availability questions. | Medium | Open |
| FR-011 | Sign In as a Member | As a Member, I want to sign in with my User Account so that the library can identify me when I borrow or return a Book Copy. | High | Open |
| FR-012 | Sign In as a Librarian | As a Librarian, I want to sign in with my User Account so that I can access my library management functions. | High | Open |
| FR-013 | Retain Loan History | As a Librarian, I want the Loan History to retain the Member, Book, borrowing date and time, and return date and time for each completed Loan so that I can trace who borrowed what and when. | High | Open |

## Non-Functional Requirements

| ID | Title | Requirement | Category | Priority | Status |
| --- | --- | --- | --- | --- | --- |
| NFR-001 | Require Authentication | Zero application routes other than sign-in permit unauthenticated access. | Security | High | Open |
| NFR-002 | Protect Librarian Functions | Zero Librarian-only routes permit access to a Member User Account. | Security | High | Open |
| NFR-003 | Protect Member Functions | Zero Member-only routes permit access to a Librarian User Account. | Security | High | Open |
| NFR-004 | Isolate Member Loans | A Member can retrieve zero Loans belonging to another Member through My Loans. | Security | High | Open |
| NFR-005 | Attribute Actions | Every Catalog change, Member Account creation, borrowing action, and return action is attributable to exactly one authenticated User Account. | Security | High | Open |
| NFR-006 | Keep Views Independent of Repositories | Zero feature views call a repository directly. | Maintainability | High | Open |

## Constraints

| ID | Title | Constraint | Category | Priority | Status |
| --- | --- | --- | --- | --- | --- |
| C-001 | Web Application | Deliver Book Library as a web application. | Technical | High | Open |
| C-002 | Single Library Branch | Support one library branch per catalog. | Business | High | Open |
| C-003 | Payments | Payment processing is outside the first release. | Business | High | Open |
| C-004 | Fines | Fines handling is outside the first release. | Business | High | Open |
| C-005 | Reservations | Reservations are outside the first release. | Business | High | Open |
| C-006 | Waiting Lists | Waiting lists are outside the first release. | Business | High | Open |
| C-007 | Self-Service Sign-Up | Self-service sign-up is outside the first release. | Business | High | Open |
| C-008 | Password Reset | Self-service password reset is outside the first release. | Business | High | Open |
| C-009 | Social Login | Social login is outside the first release. | Business | High | Open |
| C-010 | Web UI Stack | Use Vaadin for the web UI. | Technical | High | Open |
| C-011 | Data Access Stack | Use jOOQ for database access. | Technical | High | Open |
| C-012 | Security Stack | Use Spring Security for authentication and authorization. | Technical | High | Open |
