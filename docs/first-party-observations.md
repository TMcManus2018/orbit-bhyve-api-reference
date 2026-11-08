# Selected sanitized owner-reported experimental observations

The original private API responses and account identifiers are **not** published. Results represent specific owner-reported tests, not independently reproduced or globally verified Orbit server behaviour.

| Evidence | Observation | Limitation |
| --- | --- | --- |
| API-EV-043 | Zone-report GET produced a 302 to an Orbit-associated object storage host. | Target path was outside the validated daily-asset allowlist; **not followed**. |
| API-EV-046 | July 25, 2026: 1 REST history record matched 1 daily-asset record using selected fields. | Only one date/event. |
| API-EV-047 | August 7, 2026: 21 REST events matched 21 daily-asset events. | A prior contradictory `watering_events: null` observation remains unexplained. |
| API-EV-063 | Selected August 6–8 REST/asset comparison. | `null` in an asset cannot universally be interpreted as no irrigation. |
| API-EV-065 | Eight saved and checksum-verified daily assets: six populated irrigation arrays totalling 72 entries, and two explicit-null structures. | Files were retained privately; dates were selected, not a coverage survey. |
| API-EV-070 | One mesh GET returned HTTP 200 and a JSON object containing `id`, `created_at` and `devices` (array). | No returned-ID equality, array membership or universal schema established. |
| API-EV-071 | Later six-GET structural probe: one selected mesh GET returned HTTP 200 and matched the private mesh ID; own-user and feedback GETs returned 200, while three other candidate routes returned 404. | Mesh device-array membership and complete schemas remain unverified. The earlier API-EV-070 did not compare the returned mesh ID; no retroactive change to that evidence. |
| API-EV-072 | WebSocket observation did not establish any valid recognized application message. | Accepted app authentication, subscription and close reason not proven. |
| API-EV-073 | Separate frame diagnostic saw an empty CLOSE frame after JSON application ping. | Transport observation; not incorporated into the earlier frozen full-model application evidence. |

Authentication was observed with selected header profiles on owner-controlled requests, not as a universal token/header contract. Existing one-shot research authorizations were consumed and are **not** renewed by publishing these notes.

## Complete supporting ledger index

The nine selected rows above are **not** the full experiment/research ledger. See the [73-record privacy-minimized index](../evidence/research-index.md), which also covers third-party source analysis, private implementation evidence and offline consistency studies. Original private API payloads are not published.
