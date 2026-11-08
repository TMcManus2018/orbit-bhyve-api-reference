# API-EV-036 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED BOUNDED LIVE REST OBSERVATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** None recorded in the frozen machine model.

## Context and method

The October 24, 2026 API-2 direct-HTTP matrix compared selected watering-history pagination sizes.

## Recorded result

Requested per-page values 10, 14, 28, 50 and 100 yielded first/second-page counts 10/10, 14/14, 28/28, 50/17 and 67/0 respectively (HTTP 200). The run used 32 physical requests. Full 10- and 14-item traversals each found 67 containers and 831 nested irrigation records, no observed duplicate containers, and empty-page termination.

## Scope, contradictions and unverified claims

Direct HTTP paging behaviour differed from an earlier browser report. These are bounded observations of one collection, not a stable pagination specification or proof of a fixed history-retention period.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
