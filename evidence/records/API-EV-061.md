# API-EV-061 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE REST OBSERVATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** `REST-05`, `REST-08`

## Context and method

API-5C/C1 conducted a single authorized selected-device comparison of event-log pages and sprinkler programs.

## Recorded result

Six GETs plus one session POST used seven physical HTTP requests. Event-log page 1 with per-page=10 and =50 returned the same 100-element JSON array; page 2 for both sizes returned identical empty arrays. Programs with and without a device_id filter returned the same canonicalized five-element JSON array.

## Scope, contradictions and unverified claims

Event-log retention/cap and server paging rules remain unknown. Identical program arrays do not show whether the device_id filter was ignored or every program belonged to that device. No redirect target was followed or controller state modified.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
