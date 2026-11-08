# API-EV-038 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE REST OBSERVATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** None recorded in the frozen machine model.

## Context and method

A read-only API-2 endpoints experiment on October 25, 2026 inspected five fixed first-party REST routes.

## Recorded result

GET /v1/devices returned HTTP 200 with one device; GET /v1/zone_reports/{device_id} returned HTTP 302 without following the redirect; GET /v1/event_logs/{device_id} returned HTTP 200 with 100 elements; GET /v1/bhyve_accounts/{account_id} returned HTTP 200 with an object containing recognized top-level keys created_at, id and name; GET /v1/bhyve_accounts/{account_id}/devices returned HTTP 404. The selected run used 11 physical requests.

## Scope, contradictions and unverified claims

The 100-item event-log array is not proven to be the full history; the 404 is account/profile-specific. No redirected zone-report body was read. Response keys were from a limited recognition set, not complete universal schemas.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
