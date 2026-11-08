# API-EV-040 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE REST OBSERVATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** None recorded in the frozen machine model.

## Context and method

The October 26, 2026 API-4C experiment tested event-log pagination separately from watering-history pagination.

## Recorded result

An unparameterized event-logs GET returned an HTTP 200 array of 100. Explicit page=1&per-page=10 returned HTTP 200 with 100 entries; page=2&per-page=10 returned HTTP 200 with an empty array. The selected page-one and page-two payloads were unequal.

## Scope, contradictions and unverified claims

These results do not establish a 100-item total, universal cap, reliable pagination or global ignoring of per-page. The watering-history route has different observed paging behaviour.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
