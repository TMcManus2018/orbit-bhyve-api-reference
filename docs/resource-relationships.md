# Resource relationships — conceptual research map

These **13 relationships** are evidence-qualified client-derived hypotheses, not a complete vendor-confirmed resource graph.

| ID | Relationship | Classification | Not established |
| --- | --- | --- | --- |
| A3-R01 | Session credential → REST device requests | SOURCE_INFERRED_NOT_LIVE_VERIFIED | Single universal token/header profile. |
| A3-R02 | REST login token → WS `app_connection` | SOURCE_INFERRED_NOT_LIVE_VERIFIED | A valid WS handshake for API-key-only sessions. |
| A3-R03 | Account/user ↔ devices | SOURCE_INFERRED_NOT_LIVE_VERIFIED | Nested `/bhyve_accounts/{id}/devices` works; it returned 404 in observed profile. |
| A3-R04 | Device → zone / landscape descriptions | SOURCE_INFERRED_NOT_LIVE_VERIFIED | Every zone property/relationship is present or typed. |
| A3-R05 | Device → programs | SOURCE_INFERRED_NOT_LIVE_VERIFIED | `program_list` WS sender implies a supported program response. |
| A3-R06 | Device → watering-history containers | SOURCE_INFERRED_NOT_LIVE_VERIFIED | Global retention/completeness or single event per container. |
| A3-R07 | Device → event logs | SOURCE_INFERRED_NOT_LIVE_VERIFIED | Same pagination as watering history. |
| A3-R08 | Device → asset index | SOURCE_INFERRED_NOT_LIVE_VERIFIED | WS asset events or full archive coverage. |
| A3-R09 | Asset index → daily asset links | SOURCE_INFERRED_NOT_LIVE_VERIFIED | Every historical day available; signed URLs safe to publish. |
| A3-R10 | Device → zone-report redirect | SOURCE_INFERRED_NOT_LIVE_VERIFIED | Payload shape, safe redirect following or successful target retrieval. |
| A3-R11 | Device → WS subscription | SOURCE_INFERRED_NOT_LIVE_VERIFIED | One subscription per socket, accepted filter, or successful resubscription. |
| A3-R12 | WS messages → device / zone / program status | SOURCE_INFERRED_NOT_LIVE_VERIFIED | Real-time source-of-truth, ordered delivery or persistent event history. |
| A3-R13 | Daily asset contains history, zone, zone-report structures | SOURCE_INFERRED_NOT_LIVE_VERIFIED | Generic REST response is an asset-shaped object or immutable record; prior asset `watering_events: null` remains unexplained. |

The [full evidence model](../specifications/orbit-bhyve-full-model.json) retains historical provenance notes, some of which refer to private research filenames not republished here.
