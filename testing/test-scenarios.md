# Test Scenarios

## Overview

The following test scenarios demonstrate how documented business requirements, functional requirements, user stories, and acceptance criteria can be traced into testing activities.

## TS-01 — Successful Change Request Submission

**Related Requirements:** BR-01, FR-01  
**Related User Story:** US-01  
**Related Acceptance Criterion:** AC-01.1

**Precondition:** User has access to the change-request form.

**Steps:**
1. Open the change-request form.
2. Complete all required fields.
3. Submit the request.

**Expected Result:**
- A unique request is created.
- Request status is set to `Submitted`.
- Submitted information is stored successfully.

---

## TS-02 — Missing Required Information

**Related Requirements:** BR-02, FR-02  
**Related User Stories:** US-01, US-02  
**Related Acceptance Criteria:** AC-01.2, AC-02.2

**Steps:**
1. Open the request form.
2. Leave one required field blank.
3. Attempt to submit.

**Expected Result:**
- Submission is prevented.
- Missing required information is identified.

---

## TS-03 — Requirement Clarification

**Related Requirements:** BR-02, FR-02  
**Related User Story:** US-02  
**Related Acceptance Criterion:** AC-02.2

**Steps:**
1. Review a submitted request.
2. Identify unclear business information.
3. Request clarification.

**Expected Result:**
- Status changes to `Awaiting Clarification`.
- Request does not proceed to engineering review.

---

## TS-04 — Engineering Feasibility Review

**Related Requirements:** BR-06, FR-06  
**Related User Story:** US-04  
**Related Acceptance Criterion:** AC-04.1

**Steps:**
1. Open a complete request in engineering review.
2. Record feasibility, dependencies, risks, and implementation considerations.
3. Complete the assessment.

**Expected Result:**
- Engineering-review information is stored.
- Request can proceed when sufficiently defined.

---

## TS-05 — Prevent Development Without Acceptance Criteria

**Related Requirements:** BR-08, FR-08  
**Related User Story:** US-06  
**Related Acceptance Criterion:** AC-06.1

**Steps:**
1. Open a backlog item without acceptance criteria.
2. Attempt to mark it `Ready for Development`.

**Expected Result:**
- Workflow prevents the transition.
- Missing acceptance criteria are identified.

---

## TS-06 — Successful Test Execution

**Related Requirements:** BR-09, FR-09  
**Related User Stories:** US-07, US-08  
**Related Acceptance Criterion:** AC-08.1

**Steps:**
1. Open a test scenario.
2. Execute the required test.
3. Record expected and actual results.
4. Mark the test as passed.

**Expected Result:**
- Test result is saved.
- Requirement and acceptance-criterion references remain linked.

---

## TS-07 — Failed Test Creates Rework

**Related Requirements:** BR-09, FR-09  
**Related User Story:** US-08  
**Related Acceptance Criterion:** AC-08.2

**Steps:**
1. Execute a test that does not meet expected behaviour.
2. Record the test as failed.
3. Associate a defect reference.

**Expected Result:**
- Failure is recorded.
- Defect reference is linked.
- Change cannot progress directly to business acceptance.

---

## TS-08 — Business Acceptance

**Related Requirements:** BR-10, FR-10  
**Related User Story:** US-09  
**Related Acceptance Criterion:** AC-09.1

**Steps:**
1. Complete all required testing successfully.
2. Submit the change for business acceptance.
3. Approve the delivered functionality.

**Expected Result:**
- Business acceptance is recorded.
- Change may progress to `Ready for Release`.

---

## TS-09 — Prevent Release Without Business Approval

**Related Requirements:** BR-10, BR-12, FR-12  
**Related User Story:** US-11  
**Related Acceptance Criterion:** AC-11.2

**Steps:**
1. Open a change that has not received business acceptance.
2. Attempt to mark it `Ready for Release`.

**Expected Result:**
- Workflow prevents the status change.
- Business acceptance is required before release readiness.
