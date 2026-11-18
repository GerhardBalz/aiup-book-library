Created [docs/use_cases.puml](<{LOCAL_REPLAY}/issue37-book-library-replay-01/docs/use_cases.puml>) as a draft with nine use cases covering all 13 functional requirements.

Member and Librarian share **Search the Catalog** and **Sign In**. Adding and editing a Book share **Maintain Book Details**. Withdrawal remains a separate goal because it must preserve Loan History. History retention also traces to **Return a Book**, which completes the Loan record.

Static checks passed for PlantUML structure, IDs, actor links, requirement traces, and draft styling. No PlantUML renderer was available on PATH. Spec-review reported nine `SPEC_MISSING` errors for the draft use cases, which have no individual specifications yet.