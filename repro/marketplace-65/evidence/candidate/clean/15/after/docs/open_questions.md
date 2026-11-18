# Open Questions

Questions about the specification that the specification does not answer yet. A question is `Resolved` only when
the answer is in the specification itself; **Resolved in** names where. Resolved and withdrawn questions stay as
history.

## OQ-001: What happens when a Librarian removes a Book that has Loan History?

**Element:** FR-013  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** Yes  
**Status:** Resolved  

The tutorial identifies two options. Block removal after any Loan, or withdraw the Book from the Catalog while retaining its record. Both options must preserve Loan History.

**Answer:** Withdraw it from the Catalog and retain its record. Preserve Loan History.  
**Answered by:** Product owner (explicit user answer in this conversation), 2026-11-18  
**Resolved in:** FR-013, Glossary: Book  

## OQ-002: What response-time target should apply to Catalog search?

**Element:** FR-003  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The vision asks for fast discovery. The product owner left numerical performance targets undecided for this draft.

## OQ-003: What response-time target should apply to borrowing?

**Element:** FR-006  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The vision asks for quick borrowing. The product owner left numerical performance targets undecided for this draft.

## OQ-004: What response-time target should apply to returning?

**Element:** FR-007  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The vision asks for quick returns. The product owner left numerical performance targets undecided for this draft.

## OQ-005: What latency target should apply to the Active Loans view?

**Element:** NFR-004  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The vision calls for a real-time view. The draft specifies what the next retrieval must show. The product owner left numerical performance targets undecided.

## OQ-006: What service hours and uptime target should apply to Book Library?

**Element:** C-001  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The product owner left numerical availability targets undecided for this draft.

## OQ-007: Who needs to review Loan History across Members?

**Element:** FR-010  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The vision calls for a history of who borrowed what and when. The architecture limits Members to their own Loans.

**Assumed:** The Librarian can view Loan History across Members.  

## OQ-008: How should the first release prioritize Catalog maintenance and Loan History?

**Element:** FR-011  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The vision names Catalog management and Loan History without assigning priorities.

**Assumed:** Adding Books is High so the Catalog can be populated. Updating and removing Books and reviewing Loan History are Medium. The remaining requirements and constraints are High.

## OQ-009: Should each Loan identify an individual Copy?

**Element:** Entity: COPY  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  

FR-006 and FR-007 refer to lending and returning a Copy. The tutorial sketches a Book-level quantity and a Loan that identifies the Book.

**Assumed:** Track each Copy with its own identifier and require each Loan to identify one Copy. A Book can have zero or more Copies, and availability is derived from Copies without an Active Loan.  

## OQ-010: What lengths should the Catalog allow for Book titles and author credits?

**Element:** Entity: BOOK.title  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The glossary names both fields, and the sources give no storage limits.

**Assumed:** Store a required title and author credit with up to 255 characters each.  

## OQ-011: How should the Catalog record an ISBN?

**Element:** Entity: BOOK.isbn  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The glossary identifies ISBN as part of a Book description. It gives no rules for missing ISBNs, duplicate editions, or ISBN formatting.

**Assumed:** Allow a missing ISBN. When supplied, store a unique valid canonical ISBN-13, converting a valid ISBN-10 to ISBN-13.  

## OQ-012: What lengths and requirements should apply to Member Profile contact fields?

**Element:** Entity: MEMBER.name  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The tutorial names name and email. Sign-in uses the separate User Account.

**Assumed:** Require a name of up to 255 characters and allow an optional email of up to 254 characters.  

## OQ-013: Can borrow and return have the same recorded time?

**Element:** Entity: LOAN.returned_at  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  

A Loan begins on borrow and ends on return. The sources give no minimum Loan duration.

**Assumed:** Allow equal timestamps and require a return timestamp to be at or after the borrow timestamp.  


## OQ-014: What should the actor see when opening the Catalog or searching with a blank term?

**Element:** UC-001 step 2  
**Raised by:** /use-case-spec, 2026-11-18  
**Blocking:** No  
**Status:** Open  

**Assumed:** Show the full Catalog on opening it and when the search term is blank or cleared.  

## OQ-015: Which Book details should a search match, and how should it compare the search term?

**Element:** UC-001 BR-002  
**Raised by:** /use-case-spec, 2026-11-18  
**Blocking:** No  
**Status:** Open  

**Assumed:** Match a substring of title, author, or ISBN, ignoring letter case and surrounding whitespace in the search term.  

## OQ-016: What should happen when no Books match the search?

**Element:** UC-001 A2  
**Raised by:** /use-case-spec, 2026-11-18  
**Blocking:** No  
**Status:** Open  

**Assumed:** Show a no-matches message and allow the actor to search again.  
