# API-EV-060 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE REDIRECT CLASSIFICATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** None recorded in the frozen machine model.

## Context and method

The owner separately authorized one API-5B/B3 first-party zone-report no-follow experiment.

## Recorded result

The operator reported one login and one fixed zone-report GET (two physical HTTP requests). The GET returned HTTP 302; execution state FIRST_PARTY_302_CLASSIFIED, and DENY_NOT_AUTHORIZED prevented the signed-target request. The target used an Orbit-associated S3 variant with an unpinned path and unrecognized query-key profile.

## Scope, contradictions and unverified claims

Neither the object body nor its origin/authenticity was verified. The one-run authorization was consumed, and no broader allowlist or production access was approved.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
