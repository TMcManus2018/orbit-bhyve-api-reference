# API-EV-058 — Research evidence summary

**Finding (sanitized extract):** Hubitat's active orbit-bhyve-controller.groovy contains REST dispatch; its separate orbit-bhyve-sprinkler-timer.groovy actually connects WS, parses inbound device_disconnected, device_connected, flow_sensor_state_changed and other event labels, and sends app_connection and control commands

**Evidence classification:** THIRD-PARTY OBSERVED pinned Groovy code; server event delivery UNVERIFIED; fork family lineage dependent  
**Provenance:** EXPLICIT_CLAIM_FIELD / EXPLICIT_LEDGER_CLASS  
**Direct model operation references:** WS-26, WS-27

**Boundaries:** Not established beyond the evidence and conditions described in the private research record.

## Revision-pinned third-party source references (independence not implied)

- [Pinned public source 1](https://github.com/jpage4500/hubitat-drivers/blob/8c0466dd57f331e7828ff40443b35ea43946a183/orbit-bhyve/orbit-bhyve-controller.groovy#L432-L485)
- [Pinned public source 2](https://github.com/jpage4500/hubitat-drivers/blob/8c0466dd57f331e7828ff40443b35ea43946a183/orbit-bhyve/orbit-bhyve-sprinkler-timer.groovy#L138-L285)
- [Pinned public source 3](https://github.com/jpage4500/hubitat-drivers/blob/8c0466dd57f331e7828ff40443b35ea43946a183/orbit-bhyve/orbit-bhyve-sprinkler-timer.groovy#L288-L309)

**Publication caveat:** This is a minimal public derivative of a private research ledger entry, not a copy of the underlying authenticated response, a complete reproduction of the original entry or a vendor certification. Classification transcribed from the private ledger.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
