# Book Library requirements

Draft reproduction artifacts for [Marketplace #65](https://github.com/AI-Unified-Process/marketplace/issues/65),
derived from [the vision](vision.md), [architecture](architecture.md) and [starter README](../README.md).
These documents exercise specification navigation; they do not approve production implementation.

## Functional Requirements

| ID | Title | User Story | Priority | Status |
| --- | --- | --- | --- | --- |
| FR-001 | Sign in | As a Member or Librarian, I want to sign in with my own user account so that actions are tied to my identity. | High | Open |
| FR-002 | Search catalog | As a Member or Librarian, I want to search the catalog so that I can find a book. | High | Open |
| FR-003 | See copy availability | As a Member, I want to see which book copies are available so that I can choose a book copy to borrow. | High | Open |
| FR-004 | Borrow book copy | As a Member, I want to borrow an available book copy so that I can use it outside the library. | High | Open |
| FR-005 | Return book copy | As a Member, I want to return a borrowed book copy so that the loan is completed and the book copy becomes available. | High | Open |
| FR-006 | View own active loans | As a Member, I want to see my active loans so that I know which book copies I currently hold. | High | Open |
| FR-007 | View active loans | As a Librarian, I want to see all active loans so that I can tell which Member holds each book copy. | High | Open |
| FR-008 | View lending history | As a Librarian, I want to see completed loans so that I can trace who borrowed each book copy and when. | High | Open |
| FR-009 | Manage catalog | As a Librarian, I want to maintain books and book copies in the catalog so that the catalog represents the library's collection. | High | Open |
| FR-010 | Create member account | As a Librarian, I want to create a Member's user account and member profile so that the Member can sign in and borrow book copies. | High | Open |

## Non-Functional Requirements

| ID | Title | Requirement | Category | Priority | Status |
| --- | --- | --- | --- | --- | --- |

Numerical performance and availability targets remain undecided by the user's explicit choice for this
reproduction. No numerical target is introduced or qualified. The active-loan refresh target is recorded
in [OQ-001](open_questions.md#oq-001-what-latency-target-applies-to-the-active-loan-view).

## Constraints

| ID | Title | Constraint | Category | Priority | Status |
| --- | --- | --- | --- | --- | --- |
| C-001 | Runtime | Retain Java 25 from the starter build. | Technical | High | Open |
| C-002 | UI | Retain the starter's Vaadin Flow UI. | Technical | High | Open |
| C-003 | Database access | Retain jOOQ for database access. | Technical | High | Open |
| C-004 | Database | Retain PostgreSQL as the database. | Technical | High | Open |
| C-005 | Migrations | Retain Flyway for schema migrations. | Technical | High | Open |
| C-006 | Feature layout | Retain the architecture's package-by-feature layout with ui and domain subpackages. | Technical | High | Open |
| C-007 | Member provisioning | A Librarian creates member accounts; self service sign-up, password reset and social login are outside this version. | Business | High | Open |
| C-008 | Payment scope | Payments and fines are outside this version. | Business | High | Open |
| C-009 | Reservation scope | Reservations and waiting lists are outside this version. | Business | High | Open |
| C-010 | Library scope | This version serves one library branch. | Business | High | Open |
| C-011 | Role boundary | Librarian-only views require the Librarian role; a Librarian does not borrow book copies. | Business | High | Open |
