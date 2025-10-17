# Using Jira for software project management

Using Jira for software project management involves a series of steps and actions, from initial setup to day-to-day use. The process generally follows the Agile project lifecycle, with Jira providing tools to manage each phase.

## Initial Setup and Project Creation

The first step is to create a new project in Jira.

- Choose a project template: Jira offers several templates, such as Scrum, Kanban, and Bug Tracking. For software development, Scrum is a popular choice as it's designed for iterative development with sprints.

- Define project details: Give your project a clear name and a unique key. This key is used to create issue identifiers (e.g., "SWP-123").

- Configure the workflow: Jira comes with default workflows (e.g., To Do, In Progress, Done), but you can customize them to match your team's process. For example, you might add steps like "In Review" or "Testing."

## Backlog Creation and Management

Once your project is set up, you need to populate the backlog, which is the prioritized list of all work.

- Create issue types: The backlog is filled with various issue types.
  - Epics: Use these for large, high-level goals.
  - Stories: These are the user stories that describe features from the user's perspective.
  - Bugs: Use this for defects or errors.
  - Tasks: These are for small, technical work items.
- Write detailed descriptions: For each issue, write a clear and concise summary. Use the description field to add details, acceptance criteria, and any other relevant information.
- Prioritize the backlog: The Product Owner (or a similar role) prioritizes the backlog by dragging and dropping issues. The most important items should be at the top.

## Sprint Planning and Execution

For Scrum projects, the work is organized into sprints.

- Plan a sprint: At the start of a sprint, the team selects a set of high-priority issues from the backlog to work on. These issues are moved from the backlog into a new sprint.

- Break down work: Larger user stories can be broken down into smaller, actionable tasks. This helps the team understand the steps required to complete the story.

- Use the board: The Jira board (e.g., the Scrum board) provides a visual representation of the work in progress. Team members move issues from one column to another (e.g., "To Do" to "In Progress") as they work on them.

- Conduct daily stand-ups: During daily stand-ups, the team reviews the Jira board to discuss progress, roadblocks, and what they will work on next.

## Monitoring and Reporting

Jira provides several tools to track progress and identify trends.

- Dashboards: Create custom dashboards with gadgets to visualize key metrics like the sprint burndown chart, which shows the remaining work in a sprint.
- Reports: Use Jira's built-in reports to get insights into your team's performance. The Velocity Report can show how much work a team can complete in a sprint, which helps with future sprint planning.
- Track progress: Use the issue status and assignee to monitor who is working on what and the overall progress of the project.
  
## Review and Retrospective

At the end of a sprint, the team uses Jira to review their work and improve.

- Sprint Review: The team presents the completed work to stakeholders. Jira can be used to show the finished stories and demonstrate the new functionality.
- Sprint Retrospective: The team discusses what went well, what could be improved, and creates action items for the next sprint. These action items can be logged as tasks in Jira.
- Close the sprint: Once the review and retrospective are complete, the sprint is closed. Any unfinished issues are automatically moved back to the backlog to be prioritized for a future sprint.

## Acceptance Criteria 

Acceptance criteria are a set of predefined conditions that a product, feature, or work item must satisfy to be considered complete and acceptable to stakeholders. They act as a "definition of done" for a specific piece of work, providing a clear, testable list of requirements.

### At What Level Is It Applied?

Acceptance criteria are most commonly and effectively applied at the level of a User Story.

While you can technically create acceptance criteria for Epics, Features, or even Tasks, their primary purpose is to define the boundaries and success of a single, deliverable piece of value, which is exactly what a user story represents.

- User Story: This is where acceptance criteria are essential. They translate the high-level, user-centric description ("As a user, I want to...") into a concrete, testable checklist that developers can build against and testers can use to verify.

- Epic/Feature: These are often too large and abstract for detailed acceptance criteria. Instead, an Epic is considered "done" when all of its constituent features are complete. A Feature is "done" when its user stories are complete. The acceptance criteria for the user stories are what ultimately define the success of the feature.

- Task: Tasks are typically too small and technical for their own acceptance criteria. They are the individual steps a developer takes to complete a user story. The user story's acceptance criteria are what the developer is ultimately trying to satisfy through the completion of their tasks.

- Bug: Acceptance criteria for a bug are a bit different. They describe the conditions for a bug to be considered "fixed" and ensure the fix hasn't introduced new problems.

### Examples of Acceptance Criteria

Acceptance criteria are often written in a Given/When/Then format, also known as Gherkin syntax, to make them clear and testable.

### Example for a User Story

- User Story: As a registered user, I want to log in to the website using my email and password so that I can access my account.
- Acceptance Criteria:
  - Given I am on the login page, when I enter a valid email and a valid password, then I should be redirected to my account dashboard.
  - Given I am on the login page, when I enter an invalid email and/or password, then I should see an error message that says "Invalid email or password."
  - Given I am on the login page, when I click the "Forgot Password" link, then I should be taken to a password recovery page.
  - Given a user has been locked out for 3 failed login attempts, when they try to log in again, then they should see a message that their account is locked and a timer for the lockout period.

### Example for a Bug

- Bug Title: Shopping cart subtotal is incorrect when applying a discount code.
- Acceptance Criteria:
  - Given a user adds items to the cart, when they apply a valid discount code, then the subtotal should accurately reflect the discounted price.
  - Given the discount code is invalid, when the user applies it, then the subtotal should remain unchanged and an error message should be displayed.
  - The fix should not affect the functionality of the "Remove Item" button in the cart.

