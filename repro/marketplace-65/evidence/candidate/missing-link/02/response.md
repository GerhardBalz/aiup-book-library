I stopped at the `use-case-spec` clarification step with the UC-001 draft untouched and validation pending.

**OQ-013 · UC-001 BR-003** — How should Catalog search match Books?

- **Confirm the draft behavior (Recommended).** Match partial text in the title, author credit, or ISBN, ignoring letter case and surrounding whitespace. A blank or cleared query shows all Books offered in the Catalog. This lets both Members and Librarians search using whichever Book detail they have.
- **Revise the behavior.** Specify which fields to search, how to match them, and what a blank query should show.

The diagram and requirements catalog already establish that UC-001 covers both FR-001 and FR-010. The draft is missing the FR-010 link. OQ-002 remains open for numerical search performance targets, which the product owner deferred for this draft.