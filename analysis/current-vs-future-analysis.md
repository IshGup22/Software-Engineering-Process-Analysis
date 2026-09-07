# Current-State vs Future-State Process Analysis

## Overview

The current-state and future-state BPMN models were compared to identify process gaps and design improvements across the software change request lifecycle.

The analysis focuses on requirement quality, communication, ownership, traceability, backlog management, testing alignment, and release readiness.

## Process Comparison

| Process Area | Current State | Future State | Designed Improvement |
|---|---|---|---|
| Request Intake | Change requests submitted by email | Standardized change-request submission | Improves consistency and completeness of intake information |
| Requirement Review | Manual review followed by clarification emails | Required information validated before progression | Moves quality checks earlier in the process |
| Requirement Definition | Requirements clarified throughout multiple handoffs | Requirements and acceptance needs documented before engineering review | Improves requirement readiness |
| Engineering Review | Technical review may trigger additional clarification | Structured feasibility review with defined decision point | Clarifies engineering-review expectations |
| Work Tracking | Backlog/spreadsheet entry | Jira backlog item | Centralizes delivery tracking |
| Prioritization | Work prioritized manually | Structured backlog prioritization | Supports transparent prioritization |
| Delivery Planning | No explicit planning stage represented | Sprint planning incorporated into workflow | Connects approved work to Scrum delivery |
| Testing Definition | Testing expectations confirmed after development begins | Acceptance needs defined before development | Shifts validation criteria earlier |
| Testing | Generic testing activity | Tests executed against documented acceptance criteria | Improves requirements-to-testing traceability |
| Business Approval | Delivered change reviewed after testing | Formal business acceptance checkpoint | Clarifies approval responsibility |
| Release | Release confirmed through email | Change marked ready for release | Creates a defined workflow status |
| Traceability | Information distributed across emails and tracking tools | Requirements, backlog, testing, and approval stages connected | Improves lifecycle visibility |

## Key Process Changes

### 1. Earlier Requirement Validation

The future-state workflow introduces a validation checkpoint immediately after request submission.

Requests that do not contain required information are returned for clarification before reaching engineering review.

### 2. Acceptance Criteria Shifted Upstream

In the current state, testing expectations are defined or confirmed after development begins.

The future-state process documents requirements and acceptance needs before engineering review and development.

This supports clearer development expectations and stronger testing alignment.

### 3. Centralized Work Tracking

The current-state workflow includes manual backlog or spreadsheet tracking.

The future state creates or updates a Jira backlog item, allowing delivery work to be managed through a centralized Agile workflow.

### 4. Structured Agile Planning

Backlog prioritization and sprint planning are explicitly included in the future-state workflow.

This connects business and engineering review decisions to the Scrum delivery process.

### 5. Requirements-to-Testing Traceability

Future-state testing is performed against documented acceptance criteria rather than relying on testing expectations defined later in the process.

### 6. Clearer Release Readiness

The current state uses email confirmation for release.

The future-state workflow introduces a formal `Ready for Release` stage following testing and business acceptance.

## Observable Design Changes

Based on the two process models, the redesign:

- Replaces **three explicitly email-based/manual communication steps** with structured workflow activities
- Replaces spreadsheet/backlog recording with **Jira-based tracking**
- Introduces an explicit **Sprint Planning** stage
- Moves acceptance-definition activity from after development to **before development**
- Adds explicit requirement-validation and release-readiness controls
- Maintains feedback loops for incomplete requirements, failed testing, and rejected business acceptance

These are process-design observations from the BPMN models and are not presented as measured production performance improvements.
