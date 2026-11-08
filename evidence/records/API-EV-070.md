# API-EV-070 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE REST OBSERVATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** None recorded in the frozen machine model.

## Context and method

API-5C/C4-E performed one independently authorized first-party GET of an owner-selected historical mesh reference.

## Recorded result

One login and one mesh GET used two physical requests. GET /v1/meshes/{mesh_id} returned HTTP 200, application/json and a JSON object with top-level id, devices (array) and created_at keys. The request used a reference validated against eight local archived device snapshots.

## Scope, contradictions and unverified claims

This experiment did not compare returned id with requested mesh_id or inspect device array members, length or selected-controller membership. It does not establish full response schema or universal endpoint availability.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
