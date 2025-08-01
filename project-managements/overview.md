# Project Managements Overview

## Clean Architecture

- Purpose: business logic, domain model, free of any framework-specific dependencies
- Contents
  - Entities: Project, Task, User, Resource, comment, Notification
  - Value objects (no identity): Money, DateRange, TaskStatus
  - Domain Services: complex business rules not fit into an entity
  - Interfaces: contracts for infrastructure services
  - Domain events: TaskCompeltedEvent, ProjectCreatedEvent

## Application Layer

- Purpose: orchestrates the domain layer to fulfill user cases. application-specific business rules, coordinates interactions between UI and domain
- Contents
  - Commands, CommandHandlers
  - Queries, QueryHandlers
  - DTOs
  - Interfaces: defines application services and orchestrators
  - Behaviors/Pipelines: Used for cross-cutting concerns like validation, logging, and transaction management

## Infrastructure Layer

- Purpose: implements the interfaces defined in the Domain and Application layers. It deals with external concerns like databases, file systems, and external APIs
- Contents:
  - Persistence: EF Core: DbConext, Configurations, implements Repositories
  - Identity & Security: implement user authentication and authorization
  - External Services: integrations with email, notifications
  - Caching: caching mechanisms
  - Logging: logging implementation

## Presentation Layer

- Purpose: user interface, responsible for displaying data and handling user input
- Contents:
  - Controllers:
  - Views:
  - View Models:
  - Client-Side Assets: JavaScript, CSS, images
  - Dependency Injection Configuration:

## Cross-Cutting Concerns

- Logging:
- Validation:
- Authentication & Authorization:
- Error Handling:
- Testing:

## Things to Consider:

- MediatR
- FluentValidation
- Asynchronous Programming
- Repository Pattern: generic and specific repositories.
- Aggregates: identify logical clusters fo entities that are treated as a single unit for data changes. The root fo an aggregate is the only entity that can be directly accessed from outside the aggregate. This helps maintain data consistency.
- Domain events: use them to decouple domain logic and handle side effects. Task, Completed, TaskCompletedEvent, trigger notification or update to project progress
- Read Models/Projections: create denormalized read models optimized for retrieval.
- Error Handling: custom exceptions for business rule violations and global exception handling middleware.
- Authentication and Authorization: define roles and policies for different user types: Project Manager, Team Member, Administrator
- Notifications: how will users be notified of updates, assigned tasks or deadlines?
- File Uploads: attach files to tasks or projects (where to store and managed?)
- Real-time Updates: progress tracking or chant? (SignalR)
- Deployment
- Logging and Monitoring: Application Insights)
- Testing Strategy: Unit tests, Integration tests, end-to-end tests
