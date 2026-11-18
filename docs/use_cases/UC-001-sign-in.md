# Use Case: Sign in

## Overview

**Use Case ID:** UC-001  
**Use Case Name:** Sign in  
**Primary Actor:** Member, Librarian  
**Goal:** The actor signs in with their own user account so that subsequent actions are tied to their identity.  
**Trigger:** The actor requests to sign in.  
**Status:** Draft  

**Requirements:** [FR-001](../requirements.md)  
**Layers:** UI  

## Preconditions

- The library is configured with local user accounts and their roles.
- The actor is not signed in.

## Main Success Scenario

1. The actor requests to sign in.
2. Book Library asks for the user account's username and password.
3. The actor supplies the credentials.
4. Book Library verifies the credentials and signs the actor in under that user account and its role.

## Alternative Flows

### A1: Credentials are not accepted

**Trigger:** Book Library cannot verify the supplied credentials (step 4).  
**Flow:**

1. Book Library informs the actor that the credentials were not accepted.
2. Use case continues at step 3.

### A2: Actor abandons sign-in

**Trigger:** The actor abandons the request before supplying credentials (step 3).  
**Flow:**

1. The actor leaves the sign-in interaction.
2. Use case ends.

## Postconditions

### Success Postconditions

- The actor is signed in under their user account and its role.

### Failure Postconditions

- The actor remains not signed in.
- Stored user accounts and member profiles are unchanged.

## Business Rules

### BR-001: Valid credentials

A successful sign-in requires valid credentials for the user account.
