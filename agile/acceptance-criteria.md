# Acceptance Criteria

Acceptance criteria define the conditions that must be satisfied for selected user stories to be considered complete.

---

## US-01 — Submit Change Request

### AC-01.1
**Given** a requester opens the change-request form  
**When** all required fields are completed and the request is submitted  
**Then** the system creates a new request with a unique identifier and status of `Submitted`.

### AC-01.2
**Given** a required field is missing  
**When** the requester attempts to submit the request  
**Then** submission is prevented and the missing information is identified.

---

## US-02 — Validate Request Completeness

### AC-02.1
**Given** a submitted request contains all required business information  
**When** the Business Analyst completes the review  
**Then** the request can progress to `Engineering Review`.

### AC-02.2
**Given** the Business Analyst identifies missing or unclear information  
**When** clarification is requested  
**Then** the request status changes to `Awaiting Clarification`.

---

## US-03 — Track Request Status

### AC-03.1
**Given** a stakeholder has access to a request  
**When** the request is opened  
**Then** the current status, owner, priority, and outstanding action are displayed.

### AC-03.2
**Given** the request moves to another workflow stage  
**When** the status is updated  
**Then** the new status and responsible owner are recorded.

---

## US-04 — Review Technical Feasibility

### AC-04.1
**Given** a complete request reaches engineering review  
**When** an engineer completes the assessment  
**Then** feasibility, dependencies, risks, and implementation considerations can be recorded.

### AC-04.2
**Given** engineering requires additional business information  
**When** clarification is requested  
**Then** the request cannot progress to backlog prioritization until clarification is resolved.

---

## US-05 — Prioritize Approved Work

### AC-05.1
**Given** a request has completed requirements and engineering review  
**When** the Product Owner approves it for delivery  
**Then** a backlog item can be created with priority and requirement references.

### AC-05.2
**Given** a backlog item exists  
**When** sprint planning occurs  
**Then** the item can be selected based on priority, dependencies, and available capacity.

---

## US-06 — Define Acceptance Criteria

### AC-06.1
**Given** a user story is being prepared for development  
**When** no acceptance criteria are documented  
**Then** the item cannot be marked `Ready for Development`.

### AC-06.2
**Given** measurable acceptance criteria have been defined  
**When** the team reviews the story  
**Then** the item may progress to development planning.

---

## US-07 — Trace Requirements to Testing

### AC-07.1
**Given** a test scenario is created  
**When** it is saved  
**Then** it must reference at least one related requirement or acceptance criterion.

### AC-07.2
**Given** a requirement is selected  
**When** its traceability information is reviewed  
**Then** associated user stories and test scenarios can be identified.

---

## US-08 — Record Test Results

### AC-08.1
**Given** a test scenario is executed  
**When** the tester records the result  
**Then** the expected result, actual result, and pass/fail status are stored.

### AC-08.2
**Given** a test fails  
**When** the tester records the failure  
**Then** a defect or issue reference can be associated with the test result.

---

## US-09 — Approve Delivered Change

### AC-09.1
**Given** all required testing has passed  
**When** the business approver completes acceptance review  
**Then** the change may be approved for release readiness.

### AC-09.2
**Given** business acceptance is rejected  
**When** the approver records the decision  
**Then** the request cannot progress to `Ready for Release`.

---

## US-11 — Prevent Premature Progression

### AC-11.1
**Given** required testing is incomplete  
**When** a user attempts to move the request to business acceptance  
**Then** the workflow prevents the status change.

### AC-11.2
**Given** business acceptance has not been completed  
**When** a user attempts to mark the request ready for release  
**Then** the workflow prevents the transition.
