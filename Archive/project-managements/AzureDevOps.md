# Azure DevOps

 In Azure DevOps project planning, distinguishing between Epics and Features is essential for organizing work at different levels of abstraction. Here's a clear breakdown with criteria to help you decide:


## Epic and Feature

| **Criteria**       | **Epic**                                                                 | **Feature**                                                             |
|--------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Scope**          | Broad, strategic goal                                                    | Specific capability or service                                          |
| **Duration**       | Weeks to months                                                          | Days to weeks                                                           |
| **Granularity**    | High-level                                                               | Mid-level                                                               |
| **Ownership**      | Often cross-team or cross-project                                        | Typically owned by a single team                                       |
| **Breakdown**      | Composed of multiple Features                                            | Composed of multiple User Stories                                       |
| **Example**        | “Implement Employee Evaluation System”                                   | “Enable Supervisor to CRUD Evaluations”                                 |


### How to Decide if Something is an Epic

Ask yourself:

- Does this represent a major business objective?
- Will it require multiple teams or sprints to complete?
- Can it be broken down into distinct Features?
If yes → it's likely an Epic.

### How to Decide if Something is a Feature

Ask yourself:

- Is this a specific functionality or service?
- Can it be delivered by a single team?
- Can it be broken down into User Stories?
If yes → it's likely a Feature.

### Tip for Your Project

In your case:

- Epic: E01_Employee_Performance_Evaluation_System
Represents the entire goal of building the evaluation system.
- Feature: E01_F02_Evaluation_Management
A specific capability within the system, like managing evaluations.


## Feature vs User Story

Distinguishing between Features and User Stories is key to effective project planning in Azure DevOps. Here's a clear breakdown to help you decide:

| **Criteria**     | **Feature**                                                                 | **User Story**                                                                 |
|------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Scope**        | A complete functionality or service                                          | A specific user need or interaction                                            |
| **Granularity**  | Medium-level: can be broken into multiple user stories                       | Fine-grained: focused on a single user goal                                   |
| **Duration**     | Typically takes several days to a sprint                                     | Usually completed within a few days                                           |
| **Ownership**    | Owned by a team or product owner                                             | Owned by a developer or small team                                            |
| **Purpose**      | Describes *what* the system should do                                        | Describes *why* and *how* a user interacts with the system                    |
| **Example**      | “Enable Evaluation Management for Supervisors”                               | “As a supervisor, I want to update an employee’s evaluation”                 |

### How to Identify a Feature

Ask:

- Does this describe a capability or service the system provides?
- Can it be broken down into multiple user stories?
If yes → it's a Feature.

### How to Identify a User Story

Ask:

- Does this describe a specific user goal or interaction?
- Is it written from the user's perspective (e.g., As a [role], I want [goal])?
If yes → it's a User Story.



## User Story vs Task


## When to Deploy to Test Server

In a CI/CD pipeline for Azure DevOps, the decision to deploy to a test server after finishing a User Story or a Feature depends on your team's workflow and release strategy. Here's a practical guideline to help you decide:


### After Completing a User Story

- Recommended for Agile teams practicing continuous testing.
- Ensures early feedback on small, incremental changes.
- Ideal when:
  - The story is independent and testable.
  - You want to validate functionality quickly.
  - You have automated tests in place.

### After Completing a Feature

- Suitable for larger, integrated changes.
- Ensures the entire feature works as expected before testing.
- Ideal when:
  - The feature includes multiple user stories.
  - You want to avoid partial deployments.
  - You need integration testing across components.

### Best Practice

Use a branching strategy like:

- main: production
- develop: integration
- feature/*: per feature
- story/*: per user story

And configure your CI/CD pipeline to:

- Build and test on every commit.
- Deploy to test server:
  - Automatically after merging a User Story branch (for fast feedback).
  - Or after merging a Feature branch (for integrated testing).

### Milestone

In project management, a milestone is a significant point or event in the project timeline that marks the completion of a major deliverable or phase.

- What Is a Milestone?
  - It’s not a task, but a checkpoint.
  - It helps track progress, alignment, and readiness.
  - It often signals a decision point, review, or release.

####  Why Use Milestones?

Helps teams focus on goals.
Makes it easier to report progress to stakeholders.
Useful for planning sprints, releases, and reviews.

#### Examples of Milestones in Software Projects

| **Milestone Name**           | **Description**                                                  |
|-----------------------------|------------------------------------------------------------------|
| ✅ Feature Complete          | All planned features for a release are implemented.              |
| 🧪 Test Environment Ready    | CI/CD pipeline is set up and test server is live.                |
| 🚀 First Internal Demo       | A working version is ready for internal stakeholders.            |
| 📦 Beta Release              | A version is released to selected users for feedback.            |
| 🏁 Final Release             | The product is deployed to production.                           |


### User Story and Task

Summary

- User Story = What the user wants and why
- Task = How the team will build it

### 🧩 User Story vs Task: Key Differences

| **Criteria**     | **User Story**                                                                 | **Task**                                                                 |
|------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Purpose**      | Describes a **user goal** or **need**                                          | Describes a **technical step** to implement part of a user story         |
| **Perspective**  | Written from the **user’s point of view**                                      | Written from the **developer’s or team’s point of view**                 |
| **Format**       | Often follows: *As a [role], I want [goal], so that [benefit]*                 | Describes what needs to be done (e.g., “Create API endpoint”)            |
| **Scope**        | Represents a **complete unit of value**                                        | Represents a **subtask** or **implementation detail**                    |
| **Deliverable**  | Results in a **feature or functionality** visible to the user                  | Results in **code, config, or setup** that supports the user story       |
| **Example**      | “As a supervisor, I want to update an employee’s evaluation.”                  | “Create UpdateEvaluationCommandHandler”                                  |

