# API-EV-052 — Research evidence summary

**Finding (sanitized extract):** Client WebSocket keepalive uses distinct JSON application ping/pong and RFC 6455 transport PING/PONG channels; HA configures aiohttp transport heartbeat as well as JSON ping, while Go installs transport-frame handlers plus JSON ping

**Evidence classification:** THIRD-PARTY OBSERVED; server timing/deadline and actual emitted frames UNVERIFIED  
**Provenance:** EXPLICIT_CLAIM_FIELD / EXPLICIT_LEDGER_CLASS  
**Direct model operation references:** No direct operation mapping in the frozen machine-readable model.

**Boundaries:** Not established beyond the evidence and conditions described in the private research record.

## Revision-pinned third-party source references (independence not implied)

- [Pinned public source 1](https://github.com/sebr/bhyve-home-assistant/blob/43fd888a9ecb9e914f4f0b1d0d818c3218c48e95/custom_components/bhyve/pybhyve/websocket.py#L95-L150)
- [Pinned public source 2](https://github.com/gillcaleb/orbit-bhyve-go-client/blob/bc05a2aa8ef2e067e37b0bf14cffa02958162d63/pkg/websocket/websocket.go#L41-L79)
- [Pinned public source 3](https://github.com/sunnierseattle/bhyve/blob/d68f5c15a8a711c44a389864c41d51ccf311fac4/bhyve.py#L149-L168)

**Publication caveat:** This is a minimal public derivative of a private research ledger entry, not a copy of the underlying authenticated response, a complete reproduction of the original entry or a vendor certification. Classification transcribed from the private ledger.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
