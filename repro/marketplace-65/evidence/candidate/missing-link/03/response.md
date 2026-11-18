Updated the [UC-001 Search the Catalog draft](docs/use_cases/UC-001-search-the-catalog.md) to link FR-010 alongside FR-001, covering Catalog search for both Librarians and Members.

- **Clarified:** Marked [OQ-013](docs/open_questions.md#oq-013-which-book-details-does-catalog-search-match) resolved for this fixture. Search matches partial title, author credit, or ISBN without regard to case. It trims surrounding whitespace and shows all offered Books when the trimmed query is blank.
- **Assumed:** No new defaults.
- **Open:** OQ-002 remains a non-blocking requirements question about response-time targets.

Strict use-case validation and open-question lint both passed with zero errors and warnings. UC-001 remains **Draft**. `/spec-review UC-001` is available for a separate semantic review before any status change.