# Open Questions

Questions about the specification that the specification does not answer yet. A question is Resolved only when
the answer is in the specification itself; resolved and withdrawn questions stay as history.

## OQ-001: What latency target applies to the active-loan view?

**Element:** FR-007  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** No  
**Status:** Open  

The vision says the Librarian has a real time view, but supplies no numerical latency target.
The user explicitly chose to leave numerical quality targets undecided for this navigator reproduction.
A future performance requirement needs a measurable threshold; the fixture makes no such guarantee.

## OQ-002: Who may inspect completed lending history?

**Element:** FR-008  
**Raised by:** /requirements, 2026-11-18  
**Blocking:** No  
**Status:** Open  
**Assumed:** The Librarian inspects completed loans across Members.  

The vision requires history but does not specify every role's history access.
The default follows the Librarian's oversight responsibility; Member history access remains unspecified.

## OQ-003: Which Book description fields and limits are required?

**Element:** Entity: BOOK  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  
**Assumed:** A required title of at most 255 characters is sufficient for the draft model.  

The sources require catalog search but do not provide an exhaustive Book field list or text limits.
This model does not add author, ISBN or other fields without a stated requirement.

## OQ-004: Which member profile fields are mandatory?

**Element:** Entity: MEMBER  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  
**Assumed:** Name is required, email is optional, and both have a 255-character limit.  

The architecture separates the member profile from the user account and names name/email as profile data.
The draft uses ordinary field defaults; no uniqueness rule for display names or email was specified.

## OQ-005: How is a book copy identified for the business?

**Element:** Entity: BOOK_COPY  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  
**Assumed:** Each book copy has a required unique inventory_code of at most 50 characters.  

The sources distinguish individual lendable copies without fixing their human-readable identifier.
An internal id still identifies the row; the inventory code is a draft business-label choice.

## OQ-006: How does the Loan record distinguish an active loan?

**Element:** Entity: LOAN  
**Raised by:** /entity-model, 2026-11-18  
**Blocking:** No  
**Status:** Open  
**Assumed:** returned_at is absent for an Active loan and present for a Completed loan.  

The vision requires active loans and history. A nullable return time represents that distinction without
introducing a separate status field. Borrowing and return times preserve the requested history.

