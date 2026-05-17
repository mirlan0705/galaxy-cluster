# API Design

## POST /jobs

This endpoint should not run the simulation directly; it only creates a queued job.

Creates a new simulation job.

Called by: frontend.

Input:
- simulation_type
- parameters

