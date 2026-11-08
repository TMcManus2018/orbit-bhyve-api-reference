# API-EV-062 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE AUTHENTICATION OBSERVATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** `REST-02`

## Context and method

API-5C/C2 tested fixed API-key REST header variants for a single session and device-list endpoint.

## Recorded result

One session POST and five GET requests used six physical requests. GET /v1/devices baseline, OMIT_ORIGIN, OMIT_REFERER and OMIT_USER_AGENT each returned HTTP 200 with identical one-device canonical JSON arrays. Omitting Orbit-App-Id returned HTTP 401. A session-token-only case was skipped because the login did not issue that field.

## Scope, contradictions and unverified claims

The apparent User-Agent omission may not remove a lower-level library default. These results do not establish global required headers, session-token invalidity or WebSocket authentication semantics.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
