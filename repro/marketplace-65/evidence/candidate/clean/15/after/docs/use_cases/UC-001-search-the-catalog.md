# Use Case: Search the Catalog

## Overview

**Use Case ID:** UC-001  
**Use Case Name:** Search the Catalog  
**Primary Actor:** Member, Librarian  
**Goal:** Find Books in the Catalog and see how many Copies are available to borrow.  
**Trigger:** The actor requests to search the Catalog.  
**Status:** Draft  

**Requirements:** [FR-003, FR-004, FR-005, NFR-001](../requirements.md)  

## Preconditions

- The actor is signed in with a Member or Librarian User Account.

## Main Success Scenario

1. The actor opens the Catalog.
2. The system shows the Books in the Catalog with their title, author, ISBN when available, and number of available Copies, sorted by title in ascending order.
3. The actor enters a search term and requests a search.
4. The system shows matching Books with the same details and ordering as in step 2.

## Alternative Flows

### A1: Empty Catalog

**Trigger:** The Catalog contains no Books (step 2).  
**Flow:**

1. The system indicates that the Catalog is empty.
2. Use case ends.

### A2: No Matching Books

**Trigger:** No Books in the Catalog match the search term (step 4).  
**Flow:**

1. The system indicates that no Books match the search term.
2. Use case continues at step 3.

### A3: Browse the Catalog

**Trigger:** The actor leaves the search term blank or clears it (step 3).  
**Flow:**

1. The system shows the full Catalog as in step 2.
2. Use case ends.

## Postconditions

### Success Postconditions

- The actor has seen the matching Books or the full Catalog, including the available Copy count for each Book shown.

### Failure Postconditions

_None — the use case changes no data._

## Business Rules

### BR-001: Catalog Visibility

Search and browsing include only Books listed in the Catalog.

### BR-002: Search Matching

A nonblank search term matches when it occurs in the title, author, or ISBN of a Book. Matching ignores letter case and surrounding whitespace in the search term.

### BR-003: Available Copies

The number of available Copies is the number of Copies of the Book that have no Active Loan. The system shows zero when no Copies are available.
