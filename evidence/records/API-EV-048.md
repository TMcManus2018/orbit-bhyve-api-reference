# API-EV-048 — Research evidence summary

**Finding (sanitized extract):** Two newer REST clients disagree on token preference: JP selects orbit_session_token before orbit_api_key and sends both REST token-header names; YardRelay selects API-key first and uses a session-token header only as fallback

**Evidence classification:** THIRD-PARTY OBSERVED client source; cross-token acceptance UNVERIFIED  
**Provenance:** EXPLICIT_CLAIM_FIELD / EXPLICIT_LEDGER_CLASS  
**Direct model operation references:** No direct operation mapping in the frozen machine-readable model.

**Boundaries:** Not established beyond the evidence and conditions described in the private research record.

## Revision-pinned third-party source references (independence not implied)

- [Pinned public source 1](https://github.com/jordanpwalsh/bhyve-api/blob/3f6f7e90a53db98f8bcb4dcac682034b5c31cf3c/src/login.ts#L71-L79)
- [Pinned public source 2](https://github.com/jordanpwalsh/bhyve-api/blob/3f6f7e90a53db98f8bcb4dcac682034b5c31cf3c/src/bhyve-api.ts#L11-L27)
- [Pinned public source 3](https://github.com/markse123/yardrelay-for-bhyve/blob/5f0717a766d5848d816d36be542e6b93dcb5f12e/server/orbit-client.js#L120-L143)
- [Pinned public source 4](https://github.com/markse123/yardrelay-for-bhyve/blob/5f0717a766d5848d816d36be542e6b93dcb5f12e/server/orbit-client.js#L489-L505)

**Publication caveat:** This is a minimal public derivative of a private research ledger entry, not a copy of the underlying authenticated response, a complete reproduction of the original entry or a vendor certification. Classification transcribed from the private ledger.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
