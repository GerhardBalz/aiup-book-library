Created the draft [Book Library entity model](docs/entity_model.md). It models individual Book Copies, retains Loan History after Catalog withdrawal, and links actions to User Accounts. The model’s structure and foreign keys passed validation. The open-questions lint reported zero errors or warnings.

**Clarified** — The requirements and glossary establish that each Loan references an individual Book Copy. No new product-owner decisions were made.

**Assumed** — Recorded in the [open-questions log](docs/open_questions.md).

| ID | Draft assumption |
|---|---|
| OQ-005 | Record withdrawal on the Book and preserve its copies and Loans. |
| OQ-006 | ISBN is optional and unique when supplied. |
| OQ-007 | Require a title and a single author-credit field, each capped at 255 characters. |
| OQ-008 | Identify each copy internally and derive availability from Catalog and Loan records. |
| OQ-009 | Require a Member name and allow an optional, shared email address. |
| OQ-010 | Store the Librarian account that created each Member Account. |
| OQ-011 | Attribute borrowing and returns through the Member’s User Account and use current Book and Member details in Loan History. |
| OQ-012 | Keep a dated attribution record for each Catalog change. |

**Open** — OQ-001 remains open on the withdrawal policy used by the draft. OQ-002–OQ-004 remain open on search and lending response times, Active Loans freshness, and service availability. No lifecycle status was advanced.