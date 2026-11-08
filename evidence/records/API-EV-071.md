# API-EV-071 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE REST OBSERVATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** `REST-09`, `REST-11`, `REST-12`, `REST-13`, `REST-14`, `REST-16`

## Context and method

API-5E/E1 conducted six selected first-party GET observations for a single account/controller on November 2, 2026.

## Recorded result

One login and six GETs totalled seven physical requests: /v1/users/{user_id} returned 200 and matched the selected user ID; /v1/user_feedback?user_id= returned 200 with 11 object records; /v1/landscapes, /v1/weather_forecast/{device_id} and nested account-devices each returned 404; /v1/meshes/{mesh_id} returned 200, matching the selected mesh ID and exposing a one-object devices array.

## Scope, contradictions and unverified claims

The user-feedback content was not exported. The mesh array record included a device_id key but its value was not compared to the selected controller. Three 404s are account/profile-specific; no complete schema or global support claim is warranted.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
