# Open Questions

Questions about the specification that the specification does not answer yet. A question is `Resolved` only when
the answer is in the specification itself; **Resolved in** names where. Resolved and withdrawn questions stay as
history.

## OQ-001: How may the Librarian remove a Book with Loan History?

**Element:** FR-007  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The tutorial requires Loan History to survive Catalog changes. The alternatives are to withdraw the Book while preserving Loan History, or to permit removal only for Books that have never been borrowed.

**Assumed:** The Librarian can withdraw the Book while preserving its Loan History.  

## OQ-002: What response-time targets apply to Catalog search and lending actions?

**Element:** FR-001  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The vision calls for fast Catalog search and quick borrowing and returns. The product owner left numerical performance targets undecided for this draft. Define the measured actions, load conditions, and acceptable response times before specifying performance acceptance criteria.

## OQ-003: How current must the Active Loans view be?

**Element:** FR-004  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The vision calls for a real-time view of Active Loans. The product owner left numerical performance targets undecided for this draft. Define the acceptable delay between a committed Loan change and its appearance in the view.

## OQ-004: What service availability is required?

**Element:** C-001  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The product owner left numerical availability targets undecided for this draft. Define service hours, the measurement window, and the required uptime before specifying an availability acceptance criterion.

## OQ-005: How is a Book represented after withdrawal?

**Element:** Entity: BOOK.withdrawn_at  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  
**Assumed:** A withdrawal sets a Book-level date and time and excludes all its copies from new borrowing. The Book, copies, and Loans remain linked. This applies the draft reading in OQ-001.  

## OQ-006: How is an ISBN used to identify a Book?

**Element:** Entity: BOOK.isbn  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  
**Assumed:** ISBN is optional and unique when supplied. It has a 50-character limit.  

## OQ-007: What author credit does a Book require?

**Element:** Entity: BOOK.author  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  
**Assumed:** Each Book has one required author credit field that can contain multiple names, with a 255-character limit. The required title also has a 255-character limit.  

## OQ-008: How are individual Book Copies identified?

**Element:** Entity: BOOK_COPY  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  
**Assumed:** Each copy has an internal identifier. The number of copies and the number available are derived from copy and Loan records.  

## OQ-009: What contact information is required for a Member?

**Element:** Entity: MEMBER.email  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  
**Assumed:** A Member has a required name and an optional email address. Both fields are limited to 255 characters, and email addresses may be shared.  

## OQ-010: How is Member Account creation attributed?

**Element:** Entity: MEMBER.created_by_user_id  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  
**Assumed:** Each Member retains a reference to the Librarian User Account that created the Member Account.  

## OQ-011: How is historical attribution retained for borrowing and returns?

**Element:** Entity: LOAN  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  
**Assumed:** Both actions are attributed through the borrowing Member’s durable User Account link. Loan History uses the linked Book and Member records as they are currently described.  

## OQ-012: How is attribution for Catalog changes recorded?

**Element:** Entity: CATALOG_CHANGE  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  
**Assumed:** Keep one dated record per Book addition, edit, or withdrawal, linked to the Book and responsible Librarian User Account. Retain attribution and action type without storing earlier bibliographic values.  

## OQ-013: Which Book details does Catalog search match?

**Element:** UC-001 BR-003  
**Raised by:** /use-case-spec, 2026-11-18  
**Blocking:** No  
**Status:** Resolved  

The requirements specify Catalog search and the tutorial names the displayed Book details. They leave the search fields, match behavior, and handling of blank queries open.

**Assumed:** Search matches part of the title, author credit, or ISBN, ignoring letter case and surrounding query whitespace. Opening the Catalog or clearing the query shows all Books offered in the Catalog.  

**Answer:** Confirm the existing replay-fixture behavior: partial matches in title, author or ISBN; case-insensitive; trim surrounding whitespace; blank query lists all offered Books.  
**Answered by:** User (explicit product-owner answer in this conversation), 2026-11-18  
**Resolved in:** UC-001 BR-003, UC-001 A3  
