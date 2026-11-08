# API-EV-068 — Curated research evidence summary

**Evidence classification:** OPERATOR-REPORTED OFFLINE LOCAL METADATA CONSISTENCY OBSERVATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** None recorded in the frozen machine model.

## Context and method

API-5C/C4-C compared identifier locations and equality across eight local, checksum-verified assets.

## Recorded result

mesh_id and user_id were both present in the immediate nested device metadata of all eight assets, with equal values respectively across the eight snapshots and no conflicting sampled positions. No root-level device_id was present in these files. The scanner made zero network requests and exported no ID values or hashes.

## Scope, contradictions and unverified claims

Correlated snapshots from one controller are not independent owner-identity proof. Missing root device_id does not imply nested device identity mismatch. A later offline step was required to compare nested device.id.

## Revision-pinned third-party source references (independence not implied)

No direct public source-code pin is attached to this evidence record. This can be appropriate for operator-reported or offline evidence; do not imply external corroboration.

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
