# API-EV-042 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE REST OBSERVATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** None recorded in the frozen machine model.

## Context and method

The October 26, 2026 API-4C experiment tested three candidate routes previously known principally from public client source.

## Recorded result

GET /v1/devices/{device_id} returned HTTP 200 with a JSON object; GET /v1/landscape_descriptions/{device_id} returned HTTP 200 with an eight-element array; GET /v1/sprinkler_timer_programs returned HTTP 200 with a five-element array. Recognized device fields included id, name, status, num_stations and zones; recognized landscape/program rows included id, device_id and created_at.

## Scope, contradictions and unverified claims

Allowlisted field names and array counts do not determine all keys, field types, requiredness, nested structure or cross-account behaviour.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
