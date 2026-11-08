# API-EV-054 — Research evidence summary

**Finding (sanitized extract):** Swift decoder handles incoming watering_in_progress_notification, watering_complete, device_idle, battery_status, rain_delay, program_changed, device_status, and fault, often defaulting missing fields

**Evidence classification:** THIRD-PARTY OBSERVED INBOUND-HANDLED parser; server emission and field requiredness UNVERIFIED  
**Provenance:** EXPLICIT_CLAIM_FIELD / EXPLICIT_LEDGER_CLASS  
**Direct model operation references:** No direct operation mapping in the frozen machine-readable model.

**Boundaries:** Not established beyond the evidence and conditions described in the private research record.

## Revision-pinned third-party source references (independence not implied)

- [Pinned public source 1](https://github.com/waitbutY/bhyve-swift/blob/eec9bd2b414953e7d9ad7c096901bea2aea7ebb1/Sources/BHyve/WebSocket/BHyveEvent.swift#L14-L55)

**Publication caveat:** This is a minimal public derivative of a private research ledger entry, not a copy of the underlying authenticated response, a complete reproduction of the original entry or a vendor certification. Classification transcribed from the private ledger.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
