# API-EV-045 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE REST/ASSET AUDIT  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** None recorded in the frozen machine model.

## Context and method

A follow-up October 27, 2026 audit narrowed the reason the prior July 25 comparison failed.

## Recorded result

Across 67 returned history containers, the strict parser classified noncanonical_or_invalid_date=67 and timestamp_like_date=67 while accepting zero containers. Counts for malformed/missing/null irrigation categories were zero. REST traversal still ended with EMPTY_PAGE and rest_structure_valid=false.

## Scope, contradictions and unverified claims

The aggregates suggest full timestamp-like labels rather than expected date-only strings but do not prove exact syntax/time zones. The parser failure cannot be interpreted as absence of watering.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
