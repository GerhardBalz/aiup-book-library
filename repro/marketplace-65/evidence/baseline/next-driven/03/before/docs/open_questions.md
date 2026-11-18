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
