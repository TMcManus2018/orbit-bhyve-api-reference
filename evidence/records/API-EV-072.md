# API-EV-072 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE WEBSOCKET TRANSPORT OBSERVATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** None recorded in the frozen machine model.

## Context and method

API-5E/E2 inspected a single selected WebSocket connection after one owner-account login.

## Recorded result

The owner reported one WSS attempt, one app_connection using the REST API key under orbit_session_token, one JSON application ping and a single receive item classified INVALID_OR_OVERSIZED, followed by CONNECTION_CLOSED_OR_ERROR. No recognized server JSON application event was captured or controller command sent.

## Scope, contradictions and unverified claims

The diagnostic combined several invalid-frame and closing causes; it did not establish an accepted application authentication, subscription, credential rejection, valid pong or server close code.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
