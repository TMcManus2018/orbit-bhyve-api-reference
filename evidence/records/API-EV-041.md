# API-EV-041 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE REDIRECT CLASSIFICATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** None recorded in the frozen machine model.

## Context and method

The October 26, 2026 API-4B zone-report GET was classified without following the server redirect.

## Recorded result

GET /v1/zone_reports/{device_id} returned HTTP 302. The Location was HTTPS to a recognized Orbit-associated S3 host family, with an OTHER_PATH not matching the existing validated daily-asset allowlist; the target was NOT_FOLLOWED_UNVERIFIED_DESTINATION.

## Scope, contradictions and unverified claims

Host-family recognition does not authenticate or authorize an arbitrary signed object path. The target resource, payload, exact URL, signed query and content type were not verified.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
