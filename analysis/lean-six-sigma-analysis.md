# Lean Six Sigma Process Improvement Analysis

## Overview

This analysis applies foundational Lean Six Sigma concepts to compare the current-state and future-state software change request workflows.

The objective is to identify process waste, clarify likely root causes of inefficiency, and document improvement controls that support a more consistent and traceable delivery process.

This project applies Lean Six Sigma concepts at a foundational process-analysis level and does not represent formal Lean Six Sigma certification.

---

## 1. Define

### Problem Statement

The current-state workflow relies on email communication, manual review, spreadsheet or backlog tracking, and repeated clarification between business and engineering stakeholders.

These characteristics create opportunities for:

- Rework
- Waiting
- Repeated handoffs
- Inconsistent information
- Limited status visibility
- Late testing alignment
- Unclear ownership

### Improvement Goal

Design a future-state workflow that:

- Improves requirement completeness
- Reduces avoidable clarification loops
- Establishes clear ownership
- Improves process visibility
- Strengthens requirement-to-testing traceability
- Creates structured backlog and sprint planning
- Introduces formal release-readiness controls

---

## 2. Measure

The process comparison uses observable workflow characteristics rather than production timing or cost data.

### Current-State Observations

The current-state BPMN model includes:

- Email-based request submission
- Manual requirement review
- Email-based clarification
- Additional engineering clarification loops
- Spreadsheet or manual backlog recording
- Manual prioritization
- Testing expectations defined after development begins
- Email-based release confirmation

### Future-State Observations

The redesigned process introduces:

- Standardized request intake
- Required-information validation
- Earlier documentation of requirements and acceptance needs
- Structured engineering review
- Jira-based backlog management
- Backlog prioritization
- Sprint planning
- Testing against documented acceptance criteria
- Formal business acceptance
- Explicit release-readiness status

---

## 3. Analyze

### Lean Waste Identification

The current-state process was reviewed using common Lean waste categories.

| Waste Type | Current-State Example | Future-State Response |
|---|---|---|
| Waiting | Requests may wait for clarification through email exchanges | Upfront validation identifies missing information before engineering review |
| Defects / Rework | Incomplete requirements can cause repeated clarification or redevelopment | Requirements and acceptance needs are defined earlier |
| Overprocessing | Information may be repeated across emails, meetings, and tracking files | Centralized workflow and Jira backlog reduce duplicate tracking |
| Motion / Handoffs | Requests move manually between business, analyst, engineering, QA, and approver | Ownership and workflow stages are explicitly defined |
| Inventory / Work in Progress | Approved work may sit in manually managed backlogs without clear prioritization | Structured prioritization and sprint planning improve work visibility |
| Underutilized Knowledge | QA or engineering feedback may occur after key decisions have already been made | Engineering feasibility and acceptance needs are considered earlier |

---

## 4. Root Cause Analysis

### Root Cause 1 — Unstructured Intake

**Observed Issue:**  
Requests may enter the process with incomplete or inconsistent information.

**Likely Root Cause:**  
No standardized intake structure or required-field validation.

**Designed Improvement:**  
Introduce standardized submission and requirement-completeness validation before engineering review.

---

### Root Cause 2 — Late Definition of Acceptance Expectations

**Observed Issue:**  
Testing expectations are defined or confirmed after development has started.

**Likely Root Cause:**  
Acceptance requirements are not treated as a readiness condition for development.

**Designed Improvement:**  
Document requirements and acceptance needs before development planning.

---

### Root Cause 3 — Fragmented Tracking

**Observed Issue:**  
Request information may be distributed across email, spreadsheets, and separate backlog records.

**Likely Root Cause:**  
No centralized workflow or single delivery-tracking mechanism.

**Designed Improvement:**  
Create or update Jira backlog items and maintain structured workflow status.

---

### Root Cause 4 — Unclear Handoff Responsibility

**Observed Issue:**  
Stakeholders may rely on follow-up communication to determine who owns the next action.

**Likely Root Cause:**  
Responsibilities are not consistently assigned by workflow stage.

**Designed Improvement:**  
Define role ownership for requirement review, engineering assessment, development, testing, acceptance, and release readiness.

---

## 5. Improve

The future-state workflow introduces the following process improvements:

### Standardized Intake

A structured request form improves consistency in the information available at the start of the process.

### Early Validation

Requests are checked for completeness before engineering assessment, reducing avoidable downstream clarification.

### Earlier Acceptance Definition

Acceptance needs are documented before development, improving alignment between business requirements, development, and testing.

### Centralized Backlog Management

Jira-based backlog tracking replaces disconnected spreadsheet or manual tracking.

### Structured Prioritization

Backlog prioritization and sprint planning provide a clearer connection between approved requirements and development capacity.

### Requirements Traceability

Requirements, user stories, acceptance criteria, and test scenarios are linked throughout the delivery lifecycle.

### Formal Release Readiness

A defined release-readiness stage replaces informal email confirmation.

---

## 6. Control

To sustain the future-state design, the following process controls are recommended:

- Require mandatory intake fields before submission
- Prevent engineering review when requirements are incomplete
- Require acceptance criteria before a story is marked ready for development
- Maintain clear owner and status fields throughout the workflow
- Link test scenarios to requirements or acceptance criteria
- Require successful testing before business acceptance
- Require business approval before release readiness
- Maintain change and approval history for traceability
- Review backlog readiness during refinement
- Review recurring clarification or failed-test patterns during retrospectives

---

## Roles and Process Ownership

| Process Stage | Primary Owner |
|---|---|
| Request Submission | Business Requester |
| Requirement Validation | Business Analyst |
| Requirement Clarification | Business Analyst / Requester |
| Engineering Feasibility Review | Engineering / Product |
| Backlog Prioritization | Product Owner |
| Sprint Planning | Scrum Team |
| Development | Development Team |
| Testing | QA |
| Business Acceptance | Business Approver |
| Release Readiness | Product / Release Owner |

Clear ownership reduces ambiguity at handoff points and makes outstanding actions easier to identify.

---

## Summary

Using foundational Lean Six Sigma principles, the workflow redesign addresses process waste associated with waiting, rework, duplicate tracking, unclear handoffs, and late validation.

The future-state process improves structure by shifting validation earlier, centralizing backlog management, clarifying responsibilities, and linking requirements more directly to testing and release readiness.

The improvements described here are design recommendations based on process analysis and are not presented as measured production outcomes.
