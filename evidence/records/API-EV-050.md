# API-EV-050 — Research evidence summary

**Finding (sanitized extract):** Third-party clients construct distinct query forms user, user_id or t for GET devices, device_id/t for programs, and page/per-page/t for watering history; dashboard's local Flask input per_page is emitted upstream as per-page

**Evidence classification:** THIRD-PARTY OBSERVED construction; query equivalence, filter effects and universal paging UNVERIFIED  
**Provenance:** EXPLICIT_CLAIM_FIELD / EXPLICIT_LEDGER_CLASS  
**Direct model operation references:** No direct operation mapping in the frozen machine-readable model.

**Boundaries:** Not established beyond the evidence and conditions described in the private research record.

## Revision-pinned third-party source references (independence not implied)

- [Pinned public source 1](https://github.com/valiquette/homebridge-orbit-irrigation/blob/80a0731f633d8bedf941f14820975d58e4504e9d/src/orbitapi.ts#L69-L83)
- [Pinned public source 2](https://github.com/billchurch/bhyve-api/blob/c1d6a58259e60a24dcb95732cbef4f5bbb489718/src/index.js#L98-L105)
- [Pinned public source 3](https://github.com/markse123/yardrelay-for-bhyve/blob/5f0717a766d5848d816d36be542e6b93dcb5f12e/server/orbit-client.js#L156-L173)
- [Pinned public source 4](https://github.com/jesimpsonjr-tech/bhyve-dashboard/blob/0df29724fe88bd509b0e5d87eca3f93f5359f117/bhyve_server.py#L145-L162)

**Publication caveat:** This is a minimal public derivative of a private research ledger entry, not a copy of the underlying authenticated response, a complete reproduction of the original entry or a vendor certification. Classification transcribed from the private ledger.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
