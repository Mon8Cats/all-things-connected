# Project management

## Terms

Epic, Feature, User Story, Task, Bug, Baglog

### Epic

An epic is a large body of work that can be broken down into smaller, more manageable pieces. It's a high-level goal, often spanning multiple teams and iterations. Epics are a way to organize related user stories and features under a single strategic objective. They typically don't fit within a single sprint. For example, "Implement a new user authentication system" could be an epic.

### Feature

A feature is a specific piece of functionality that provides value to the user. It's a component of a product that's often a part of an epic. Features are typically larger than a single user story but smaller than an epic. For instance, within the "New user authentication system" epic, "Implement social media login" would be a feature.


### Task

A user story is a short, simple description of a feature told from the perspective of the end-user. It describes what the user wants to achieve and why, following a common format: "As a [type of user], I want to [goal] so that I can [reason]." User stories are the core of Agile development and are small enough to be completed within a single sprint. For example, "As a new user, I want to log in with my Google account so I don't have to create a new password."

### Bug

A bug is a defect or error in the software that causes it to behave unexpectedly. It's an issue that needs to be fixed to ensure the product functions as intended. Bugs are often logged as a separate work item but can sometimes be treated like a high-priority task or user story.


### Backlog

The backlog is a prioritized list of all work that needs to be done on a product. It serves as a single source of truth for the development team. The backlog contains a mix of all the items above: epics, features, user stories, tasks, and bugs. The product owner is responsible for grooming and prioritizing the backlog to ensure the team is always working on the most valuable items.

## Time Spans

Epics and features are long-term goals that align with a release. User stories, tasks, and bugs are short-term, actionable items that are completed within a sprint.

### Epic & Feature

Epics and Features are large-scale items that generally take longer than a single sprint to complete. They are typically worked on across multiple sprints and are often aligned with a release. For example, a "new user authentication system" epic may be broken down into features, and those features will be developed and released over several months, with each sprint completing a small part of the work.

### User Story, Task & Bug

User stories, tasks, and bugs are all designed to be completed within a single sprint.

- A user story is the core work item for a sprint. The goal of a sprint is to deliver a set of user stories that create a potentially shippable product increment.

- Tasks are the technical sub-components of a user story, so they must be completed within the same sprint as the story they belong to.

- A bug can be thought of as a high-priority task. If it's critical, it will be added to the current sprint; otherwise, it will be prioritized in the backlog for a future sprint.

### Sprint & Release

- A sprint is a short, time-boxed period (usually 1-4 weeks) during which a team works to complete a set of work. At the end of each sprint, the team should have a working, incremental piece of the product.

- A release is when a finished product or an updated version is made available to users. A release can contain the work from several sprints, or sometimes just one. Releasing frequently is a key principle of Agile, but the frequency depends on the project and company.

## Deployment and Release

The traditional model where a deployment and a release were the same thing is now often separated, especially with Agile and DevOps.

- Deployment is the technical act of putting the code on the servers.

- Release is the business decision to make that deployed code available to customers.

- A deployment can happen after a sprint, or even multiple times within a sprint.

- A release can happen at the end of a sprint, or after several sprints, depending on business needs.

- "Available to customer" means the software is live and usable by end-users. This is the moment of the release.

When to Deploy? After a Sprint, or a Release?
In a true Agile or DevOps environment, deployment can happen at any time, even multiple times a day. The key is separating deployment from release.

- Continuous Deployment: The most advanced form of this is Continuous Deployment, where every code change that passes automated tests is automatically deployed to production. This is often the ideal for teams that are mature with their CI/CD (Continuous Integration/Continuous Delivery) pipelines.

- Deployment after a sprint: Many teams, especially those still maturing, will deploy a new increment of work to a staging or production environment at the end of each sprint. This allows them to have a "potentially shippable" product increment, as required by Scrum.

- Deployment is a technical action, not a business one. The engineering team can deploy code to production, but keep the new features hidden from users. This is often done using feature flags (also known as feature toggles).

### What are the differences between release and deployment?

This is a critical distinction in modern software development.

- Deployment: This is the technical process of installing software in a specific environment. It's an engineering task. The goal is to get the code running on the servers. It can happen in a test environment, a staging environment, or production.

  - Analogy: It's like a chef preparing a new dish and placing it on a serving tray in the kitchen. The dish is ready, but the customer can't see or eat it yet.

- Release: This is a business decision to make a deployed feature or version of software available to users. This is where the product owner or business stakeholders are heavily involved. A release might involve marketing announcements, user documentation, and turning on feature flags.

  -Analogy: It's when the waiter brings the dish out of the kitchen and serves it to the customer. The customer can now use and enjoy the new feature.

The separation of these two concepts allows for greater flexibility. For example, a team can deploy an unfinished feature to production and hide it with a feature flag. This reduces the risk of a "big bang" release and allows the team to work on a feature over multiple sprints without blocking other, unrelated deployments.

### Which means "available to customer"?

A release means the software is available to the customer.

- Deployment to production does not automatically mean the customer can see or use the new features. The features become available when they are released.

- For example, a team might deploy new code to production every day. However, they may only have a "release" once a month where they turn on a set of feature flags and announce the new functionality to their users. This gives the team the agility of frequent deployments while giving the business the control to launch features strategically.
  
