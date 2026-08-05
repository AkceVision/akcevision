# ADR-0001: Main Application Structure

## Status

Accepted

## Date

L19 Sprint-01

## Context

The Gateway module is the first executable service of the AkceVision platform.

At the current stage, the application contains only two endpoints:

- GET /
- GET /health

A modular router architecture is planned for future development.

## Decision

The `main.py` file will remain intentionally simple during the Foundation phase.

Although a router structure (`routers/health.py`) has been introduced, the application bootstrap will not be refactored until the number of endpoints justifies the additional architectural complexity.

## Consequences

### Advantages

- Simple startup process
- Easy debugging
- Minimal complexity
- Fast onboarding for new contributors

### Future Work

When additional API modules are introduced (authentication, metrics, portfolio, risk, market intelligence), the application will transition to a fully modular router-based architecture using `app.include_router()`.

## Approval

- Architecture Review: Accepted
- Engineering Review: Accepted
