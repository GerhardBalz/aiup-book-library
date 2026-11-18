# Open Questions

Questions about the specification that the specification does not answer yet. A question is `Resolved` only when
the answer is in the specification itself; **Resolved in** names where. Resolved and withdrawn questions stay as
history.

## OQ-001: What happens when a Librarian removes a Book that has Loan History?

**Element:** FR-013  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** Yes  
**Status:** Open  

The tutorial identifies two options. Block removal after any Loan, or withdraw the Book from the Catalog while retaining its record. Both options must preserve Loan History.

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
