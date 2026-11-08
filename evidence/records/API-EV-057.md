# API-EV-057 — Curated research evidence summary

**Evidence classification:** THIRD-PARTY SOURCE-ONLY SECURITY OBSERVATION  
**Editorial review:** compared with the original research ledger; this is still a **sanitized derivative**, not the full private source record.  
**Associated operation IDs:** None recorded in the frozen machine model.

## Context and method

Comparative source inspection highlighted practices relevant to credential and WebSocket-frame handling.

## Recorded result

The YardRelay implementation explicitly avoids automatic REST redirect following, while inspected Go, openHAB and blacksmithlabs code contained candidate token logging or WebSocket frame/logging behaviours.

## Scope, contradictions and unverified claims

Code-level risk indicators are not proof of runtime data disclosure, exploitation or a vendor security flaw. Do not reproduce potentially sensitive logging or unsafe redirect handling.

## Revision-pinned third-party source references (independence not implied)

- [Pinned client source 1](https://github.com/markse123/yardrelay-for-bhyve/blob/5f0717a766d5848d816d36be542e6b93dcb5f12e/server/orbit-client.js#L393-L430)
- [Pinned client source 2](https://github.com/gillcaleb/orbit-bhyve-go-client/blob/bc05a2aa8ef2e067e37b0bf14cffa02958162d63/pkg/client/client.go#L37-L62)
- [Pinned client source 3](https://github.com/openhab/openhab-addons/blob/e3eeb3e9a918d1abe9b2b351a5958b0c1f9df0d5/bundles/org.openhab.binding.orbitbhyve/src/main/java/org/openhab/binding/orbitbhyve/internal/handler/OrbitBhyveBridgeHandler.java#L427-L437)
- [Pinned client source 4](https://github.com/blacksmithlabs/orbit-bhyve-remote/blob/29ca8d4a37c477b33ad9b60ae6128eca6242d5db/src/lib/api.js#L35-L76)

No raw Orbit response, personal identifier, session credential or signed URL is reproduced in this summary. Third-party client code alone is not live vendor verification.

[All evidence records](../research-index.md) · [REST/WS mapping](../operation-evidence-crosswalk.md)
