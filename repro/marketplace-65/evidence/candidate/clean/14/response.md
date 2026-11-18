Drafted [UC-001 — Search the Catalog](docs/use_cases/UC-001-search-the-catalog.md). Strict use-case validation and open-question lint both passed with zero errors and warnings.

Recorded three defaults in the [open-questions log](docs/open_questions.md).

- **OQ-014** — Opening the Catalog or clearing the search shows the full Catalog.
- **OQ-015** — Search matches part of a title, author, or ISBN, ignoring case and surrounding whitespace.
- **OQ-016** — When a search finds no matches, the actor can try again.

The checkout already records your OQ-001 answer for Book removal. The Catalog search response-time target remains open under OQ-002, which is marked non-blocking for this draft.

UC-001 is **Draft**. Its semantic review is available via `/spec-review UC-001`.