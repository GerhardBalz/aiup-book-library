Created the draft entity model for Books, Copies, Member Profiles, and Loans. Each Loan identifies an individual Copy, and each Member Profile links to the starter project’s `APP_USER` table. [Entity model](docs/entity_model.md)

**Clarified**  
No user decisions were recorded.

**Assumed**

| ID | Draft decision |
| --- | --- |
| OQ-009 | Track individual Copies. A Book may have zero or more Copies, and each Copy may have at most one Active Loan. |
| OQ-010 | Require Book titles and author credits, with up to 255 characters each. |
| OQ-011 | Allow missing ISBNs. Store supplied ISBNs as unique, canonical ISBN-13 values. |
| OQ-012 | Require a Member name of up to 255 characters and allow an optional email of up to 254 characters. |
| OQ-013 | Allow borrow and return timestamps to be equal. |

**Open**  
OQ-001 remains a product decision about how to remove Books with Loan History. The draft requires preserving Loan History in either case. [Open questions](docs/open_questions.md)

The model passed the structural checks, and the question-log lint reported zero findings. I used a working checklist because TodoWrite was unavailable.