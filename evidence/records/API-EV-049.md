# API-EV-049 — Research evidence summary

**Finding (sanitized extract):** Maintained Home Assistant Python derivative obtains orbit_api_key, sends both token-named REST headers and populates a WS app_connection.orbit_session_token property using its stored token

**Evidence classification:** THIRD-PARTY OBSERVED dependent/vendored source; REST-to-WS credential compatibility UNVERIFIED  
**Provenance:** EXPLICIT_CLAIM_FIELD / EXPLICIT_LEDGER_CLASS  
**Direct model operation references:** No direct operation mapping in the frozen machine-readable model.

**Boundaries:** Not established beyond the evidence and conditions described in the private research record.

## Revision-pinned third-party source references (independence not implied)

- [Pinned public source 1](https://github.com/sebr/bhyve-home-assistant/blob/43fd888a9ecb9e914f4f0b1d0d818c3218c48e95/custom_components/bhyve/pybhyve/client.py#L75-L85)
- [Pinned public source 2](https://github.com/sebr/bhyve-home-assistant/blob/43fd888a9ecb9e914f4f0b1d0d818c3218c48e95/custom_components/bhyve/pybhyve/client.py#L188-L210)
- [Pinned public source 3](https://github.com/sebr/bhyve-home-assistant/blob/43fd888a9ecb9e914f4f0b1d0d818c3218c48e95/custom_components/bhyve/pybhyve/websocket.py#L130-L148)

**Publication caveat:** This is a minimal public derivative of a private research ledger entry, not a copy of the underlying authenticated response, a complete reproduction of the original entry or a vendor certification. Classification transcribed from the private ledger.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
