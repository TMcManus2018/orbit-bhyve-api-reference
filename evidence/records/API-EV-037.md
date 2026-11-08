# API-EV-037 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE AUTHENTICATION OBSERVATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** None recorded in the frozen machine model.

## Context and method

The October 24, 2026 authenticated API-2 matrix tested specific login fields and header omissions.

## Recorded result

The selected session response contained orbit_api_key and user/account identifier fields but no orbit_session_token. An API-key GET /v1/devices returned HTTP 200. Omitting Orbit-App-Id yielded HTTP 401; omitting Origin, Referer or User-Agent individually yielded HTTP 200 in the tested profile.

## Scope, contradictions and unverified claims

Field presence and HTTP statuses apply to one session, account and endpoint. No universal credential/header contract, session-token non-support or downstream forwarding rule was established.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
