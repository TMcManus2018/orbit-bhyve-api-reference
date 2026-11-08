# API-EV-053 — Curated research evidence summary

**Evidence classification:** THIRD-PARTY SOURCE-ONLY WEBSOCKET CANDIDATES  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** None recorded in the frozen machine model.

## Context and method

Source inspection of the willioz Python client identified program-related WebSocket send constructs.

## Recorded result

Client code constructs program_list, program_save, program_delete, program_enable and program_disable. The list method returns an empty placeholder list after sending instead of a verified vendor response.

## Scope, contradictions and unverified claims

Source code does not prove WebSocket server receipt, acknowledgement, accepted payload shape or program mutations. These are potentially state-changing candidates, not instructions to send them.

## Revision-pinned third-party source references (independence not implied)

- [Pinned client source 1](https://github.com/willioz/Obit-bhyve-python-package/blob/3cb75ca86e4124851b93d178b7dcb1611e742a31/orbit_bhyve/client.py#L349-L390)
- [Pinned client source 2](https://github.com/willioz/Obit-bhyve-python-package/blob/3cb75ca86e4124851b93d178b7dcb1611e742a31/orbit_bhyve/client.py#L392-L489)

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
