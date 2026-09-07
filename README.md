# Software Engineering & Business Process Analysis

A software engineering and business-process analysis case study demonstrating how business requirements can be translated into **BPMN process maps, Agile user stories, acceptance criteria, Jira-ready backlog items, Scrum delivery artifacts, and test scenarios**.

The project also applies foundational **Lean Six Sigma principles** to compare current and future workflows, identify process waste, clarify stakeholder responsibilities, and design process-improvement guidance.

---

## Project Overview

This project analyzes a software change request and delivery workflow from initial business request through engineering review, development, testing, business acceptance, and release readiness.

The objective was to model the current-state process, identify gaps and inefficiencies, and design a more structured future-state workflow.

The analysis demonstrates how business requirements can be carried through the software development lifecycle using:

- Business and functional requirements
- BPMN-style process mapping
- Agile user stories
- Acceptance criteria
- Jira-ready backlog design
- Scrum planning
- Requirements traceability
- Test scenarios
- Lean Six Sigma process analysis
- Roles and responsibilities mapping

---

## Business Problem

The current-state workflow relies heavily on manual communication, email-based clarification, spreadsheet/backlog tracking, and repeated handoffs between stakeholders.

Key process challenges include:

- Incomplete or inconsistent requirements
- Repeated clarification loops
- Limited visibility into request status
- Unclear ownership during handoffs
- Manual backlog and prioritization activities
- Testing expectations defined relatively late
- Disconnected requirements and testing artifacts
- Informal release confirmation

The future-state workflow introduces standardized intake, requirement validation, defined ownership, Jira-based tracking, acceptance criteria, structured testing, Scrum planning, and formal release-readiness controls.

---

## Current-State BPMN Process

The current-state model represents a more manual software change-request workflow.

Key characteristics include:

- Email-based request submission
- Manual requirements review
- Clarification loops between business and engineering
- Spreadsheet or manual backlog tracking
- Manual prioritization
- Testing expectations confirmed after development begins
- Email-based release confirmation

![Current-State Software Change Request Workflow](process-maps/current-state-bpmn.png)

---

## Future-State BPMN Process

The future-state model introduces a more structured workflow with defined controls and traceability.

Key improvements include:

- Standardized change-request intake
- Required-information validation
- Earlier documentation of requirements and acceptance needs
- Structured engineering feasibility review
- Jira-based backlog management
- Backlog prioritization
- Sprint planning
- Testing against documented acceptance criteria
- Formal business acceptance
- Explicit release-readiness status

![Future-State Software Change Request Workflow](process-maps/future-state-bpmn.png)

---

## Business & Functional Requirements

The project includes structured business and functional requirements using requirement IDs for traceability.

Examples include:

- **BR-01:** Standardized request intake
- **BR-02:** Requirement completeness
- **BR-03:** Clear ownership
- **BR-05:** Requirements traceability
- **BR-08:** Defined acceptance criteria
- **BR-09:** Testing alignment
- **BR-10:** Approval before release

Functional requirements translate these needs into specific workflow capabilities such as validation rules, status tracking, engineering-review documentation, backlog creation, test-result recording, and invalid-transition controls.

View the full requirements:

- [`business-requirements.md`](requirements/business-requirements.md)
- [`functional-requirements.md`](requirements/functional-requirements.md)

---

## Agile User Stories & Acceptance Criteria

Business requirements were translated into Agile user stories using the standard format:

> **As a [user], I want [capability], so that [business value].**

Examples include:

- Submit a standardized change request
- Validate request completeness
- Track request status and ownership
- Record engineering feasibility
- Prioritize approved work
- Define acceptance criteria
- Trace requirements to testing
- Record test results
- Capture business acceptance

Acceptance criteria were written using **Given / When / Then** format to define measurable conditions for completion.

View:

- [`user-stories.md`](agile/user-stories.md)
- [`acceptance-criteria.md`](agile/acceptance-criteria.md)

---

## Jira-Ready Backlog & Scrum Planning

The project includes a Jira-ready backlog containing:

- Issue keys
- Story summaries
- User stories
- Priorities
- Story points
- Sprint assignments
- Requirement references
- Status

The illustrative Scrum plan organizes backlog items across four delivery sprints:

### Sprint 1
Request intake and workflow visibility

### Sprint 2
Engineering review and delivery readiness

### Sprint 3
Testing, traceability, and business acceptance

### Sprint 4
Workflow controls and governance

The Scrum plan also defines:

- Product goal
- Backlog prioritization approach
- Sprint goals
- Scrum roles
- Scrum ceremonies
- Definition of Ready
- Definition of Done

View:

- [`jira-backlog.csv`](agile/jira-backlog.csv)
- [`scrum-plan.md`](agile/scrum-plan.md)

---

## Current-State vs Future-State Analysis

The two workflows were compared across key process areas.

| Process Area | Current State | Future State |
|---|---|---|
| Request Intake | Email-based submission | Standardized request intake |
| Requirement Review | Manual review and clarification | Required-information validation |
| Requirement Definition | Clarified throughout delivery | Requirements and acceptance needs documented earlier |
| Engineering Review | Informal clarification loops | Structured feasibility review |
| Work Tracking | Spreadsheet / manual backlog | Jira backlog |
| Prioritization | Manual prioritization | Structured backlog prioritization |
| Delivery Planning | No explicit planning stage | Sprint planning |
| Testing Definition | Defined after development begins | Acceptance needs defined before development |
| Testing | Generic test activity | Testing against acceptance criteria |
| Business Approval | Review after testing | Formal business acceptance |
| Release | Email confirmation | Explicit release-readiness status |

The full comparison is available here:

[`current-vs-future-analysis.md`](analysis/current-vs-future-analysis.md)

---

## Lean Six Sigma Process Analysis

Foundational Lean Six Sigma concepts were applied to identify process waste and design improvements.

### Lean Waste Identified

The current-state workflow contains examples of:

- **Waiting** — clarification through manual email exchanges
- **Defects / Rework** — incomplete requirements causing repeated clarification or redevelopment
- **Overprocessing** — information repeated across email, meetings, and tracking tools
- **Handoffs** — manual transfers between business, engineering, QA, and approvers
- **Work in Progress** — items sitting in manually managed backlogs
- **Underutilized Knowledge** — engineering or QA input introduced too late

### Root Causes Analyzed

Key root causes included:

- Unstructured request intake
- Late definition of acceptance expectations
- Fragmented tracking
- Unclear process ownership

### Designed Improvements

The future-state workflow introduces:

- Standardized intake
- Early requirement validation
- Earlier acceptance definition
- Jira-based centralized tracking
- Structured backlog prioritization
- Sprint planning
- Requirements-to-testing traceability
- Formal release-readiness controls

The complete Lean Six Sigma analysis is available here:

[`lean-six-sigma-analysis.md`](analysis/lean-six-sigma-analysis.md)

> The Lean Six Sigma work in this project is applied at a foundational process-analysis level and does not represent formal Lean Six Sigma certification.

---

## Roles & Responsibilities

The future-state workflow clarifies responsibility across:

- Business Requester
- Business Analyst
- Product Owner
- Engineering
- Development
- QA
- Business Approver

A simplified RACI-style matrix is used to clarify ownership across major process stages.

View:

[`roles-responsibilities.md`](analysis/roles-responsibilities.md)

---

## Requirements Traceability & Testing

The project demonstrates traceability across:

**Business Requirement → Functional Requirement → User Story → Acceptance Criteria → Test Scenario**

Example:

```text
BR-08
Defined Acceptance Criteria
        ↓
FR-08
System supports acceptance criteria
        ↓
US-06
Define Acceptance Criteria
        ↓
AC-06.1 / AC-06.2
Readiness conditions
        ↓
TS-05
Prevent Development Without Acceptance Criteria

Test scenarios cover:

- Successful request submission
- Missing required information
- Requirement clarification
- Engineering feasibility review
- Development-readiness controls
- Successful testing
- Failed-test rework
- Business acceptance
- Release-readiness controls

View:

[`test-scenarios.md`](testing/test-scenarios.md)

---

## Key Deliverables

This repository contains:

- Business requirements
- Functional requirements
- Current-state BPMN process map
- Future-state BPMN process map
- Agile user stories
- Acceptance criteria
- Jira-ready backlog
- Scrum delivery plan
- Current vs future workflow analysis
- Lean Six Sigma process analysis
- Roles and responsibilities matrix
- Requirements-based test scenarios

---

## Skills & Concepts Demonstrated

- Business Requirements Analysis
- Functional Requirements
- BPMN Process Mapping
- Current-State / Future-State Analysis
- Agile / Scrum
- Jira Backlog Design
- User Stories
- Acceptance Criteria
- Requirements Traceability
- Gap Analysis
- Lean Six Sigma
- Root Cause Analysis
- Process Improvement
- Software Testing
- RACI / Role Clarification
- SDLC Analysis

---

## Repository Structure

```text
Software-Engineering-Process-Analysis/
│
├── requirements/
│   ├── business-requirements.md
│   └── functional-requirements.md
│
├── process-maps/
│   ├── README.md
│   ├── current-state-bpmn.png
│   └── future-state-bpmn.png
│
├── agile/
│   ├── user-stories.md
│   ├── acceptance-criteria.md
│   ├── jira-backlog.csv
│   └── scrum-plan.md
│
├── analysis/
│   ├── current-vs-future-analysis.md
│   ├── lean-six-sigma-analysis.md
│   └── roles-responsibilities.md
│
├── testing/
│   └── test-scenarios.md
│
└── README.md
Project Scope & Limitations

This repository is a software engineering and business-process analysis case study designed to demonstrate requirements analysis, BPMN modelling, Agile delivery artifacts, testing traceability, and process-improvement methods.

The proposed future-state improvements represent designed process recommendations, not measured production outcomes.

No claims are made regarding production implementation, measured cycle-time reduction, cost savings, or operational performance improvements.
