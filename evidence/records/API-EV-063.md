# API-EV-063 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE REST/DAILY-ASSET COMPARISON  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** `REST-04`, `REST-17`, `REST-18`

## Context and method

API-5C/C3 compared selected August 6–8, 2026 watering histories under a validated daily-asset-only follow policy.

## Recorded result

The run reported 16 physical requests, 68 REST history containers and 21 REST events in the selected window. August 7 had 21 REST events and 21 asset events matching on selected identity/field checks (AGREEMENT). August 6 and 8 had zero REST events but retrieved daily assets whose watering_events fields were explicit null, so both comparisons were INCONCLUSIVE.

## Scope, contradictions and unverified claims

A retrieved daily asset with watering_events:null is not a verified zero-event array. The three-day comparison does not establish general completeness; the unresolved zone-report S3 target was not requested.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
