# Use Case: Search the Catalog

## Overview

**Use Case ID:** UC-001  
**Use Case Name:** Search the Catalog  
**Primary Actor:** Member, Librarian  
**Goal:** Find Books in the Catalog and determine which have an available Book Copy.  
**Trigger:** A Member or Librarian opens the Catalog to find a Book.  
**Status:** Draft  

**Requirements:** [FR-001, FR-010, NFR-001, NFR-006, C-001, C-002, C-010, C-011, C-012](../requirements.md)

## Preconditions

- The Member or Librarian is signed in with their User Account.

## Main Success Scenario

1. The Member or Librarian opens the Catalog.
2. The system displays the Books offered in the Catalog in ascending title order, with the title, author, ISBN when known, and available Book Copy count for each Book.
3. The Member or Librarian enters a search query.
4. The system displays the matching Books in the same order and with the same details.

## Alternative Flows

### A1: Empty Catalog

**Trigger:** The Catalog contains no Books (step 2)  
**Flow:**

1. The system indicates that the Catalog is empty.
2. Use case ends.

### A2: No Matching Books

**Trigger:** No Books in the Catalog match the query (step 4)  
**Flow:**

1. The system indicates that no Books match the query.
2. Use case continues at step 3.

### A3: Blank Query

**Trigger:** The Member or Librarian leaves the query blank or clears it (step 3)  
**Flow:**

1. Use case continues at step 2.

## Postconditions

### Success Postconditions

- The Member or Librarian can see the matching Books and determine which have at least one available Book Copy.

### Failure Postconditions

_None — the use case changes no data._

## Business Rules

### BR-001: Catalog Scope

Search considers Books offered in the Catalog, including Books whose available Book Copy count is zero. A withdrawn Book is excluded.

### BR-002: Available Book Copy Count

The count for each Book includes every Book Copy of that Book with no Active Loan.

### BR-003: Search Matching

A query matches a Book when its text appears in the title, author credit, or ISBN. Ignore letter case and surrounding whitespace in the query. A Book without an ISBN can still match by title or author credit. A query with no text after trimming shows all Books in the Catalog.

### BR-004: Result Order

Books are displayed in ascending title order.
