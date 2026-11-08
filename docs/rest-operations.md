# REST interface — research inventory

**27 candidate operations** across **24 canonical path templates**. State-changing methods are recorded only as source-derived descriptions; they are **not approved for execution**. A response in one owner's account is not a general vendor contract.

| ID | Method | Candidate path | Research status | Risk | Evidence | Pinned upstream source |
| --- | --- | --- | --- | --- | --- | --- |
| REST-01 | `POST` | `/v1/session` | OPERATOR_200 | AUTH_EXCHANGE | A2-E01 | [source](https://github.com/sebr/pybhyve/blob/df8316f174bf3cf18db34d62c378b5da6af1c8fc/pybhyve/client.py#L127-L137) |
| REST-02 | `GET` | `/v1/devices` | OPERATOR_200 | READ | API-EV-062 | [source](https://github.com/billchurch/bhyve-api/blob/c1d6a58259e60a24dcb95732cbef4f5bbb489718/src/index.js#L98-L105) |
| REST-03 | `GET` | `/v1/devices/{device_id}` | OPERATOR_200 | READ | A2-E03 | [source](https://github.com/valiquette/homebridge-orbit-irrigation/blob/80a0731f633d8bedf941f14820975d58e4504e9d/src/orbitapi.ts#L108-L141) |
| REST-04 | `GET` | `/v1/watering_events/{device_id}` | OPERATOR_200 | READ | API-EV-063 | [source](https://github.com/markse123/yardrelay-for-bhyve/blob/5f0717a766d5848d816d36be542e6b93dcb5f12e/server/orbit-client.js#L166-L173) |
| REST-05 | `GET` | `/v1/sprinkler_timer_programs` | OPERATOR_200 | READ | API-EV-061 | [source](https://github.com/sunnierseattle/bhyve/blob/d68f5c15a8a711c44a389864c41d51ccf311fac4/bhyve.py#L189-L198) |
| REST-06 | `GET` | `/v1/landscape_descriptions/{device_id}` | OPERATOR_200 | READ | A2-E06 | [source](https://github.com/sebr/bhyve-home-assistant/blob/43fd888a9ecb9e914f4f0b1d0d818c3218c48e95/custom_components/bhyve/pybhyve/client.py#L169-L181) |
| REST-07 | `GET` | `/v1/zone_reports/{device_id}` | OPERATOR_302 | REDIRECT_SOURCE | A2-E07 | [source](https://github.com/jpage4500/hubitat-drivers/blob/8c0466dd57f331e7828ff40443b35ea43946a183/orbit-bhyve/orbit-bhyve-controller.groovy#L453-L458) |
| REST-08 | `GET` | `/v1/event_logs/{device_id}` | OPERATOR_200 | READ | API-EV-061 | [source](https://github.com/jpage4500/hubitat-drivers/blob/8c0466dd57f331e7828ff40443b35ea43946a183/orbit-bhyve/orbit-bhyve-controller.groovy#L453-L458) |
| REST-09 | `GET` | `/v1/meshes/{mesh_id}` | HTTP_200 | READ | API-EV-071 | [source](https://github.com/jpage4500/hubitat-drivers/blob/8c0466dd57f331e7828ff40443b35ea43946a183/orbit-bhyve/orbit-bhyve-controller.groovy#L459-L461) |
| REST-10 | `GET` | `/v1/network_topologies/{topology_id}` | NOT_TESTED_ID_MISSING | READ | A2-E09 | [source](https://github.com/jpage4500/hubitat-drivers/blob/8c0466dd57f331e7828ff40443b35ea43946a183/orbit-bhyve/orbit-bhyve-controller.groovy#L459-L461) |
| REST-11 | `GET` | `/v1/users/{user_id}` | HTTP_200 | READ_SENSITIVE | API-EV-071 | [source](https://github.com/jpage4500/hubitat-drivers/blob/8c0466dd57f331e7828ff40443b35ea43946a183/orbit-bhyve/orbit-bhyve-controller.groovy#L440-L448) |
| REST-12 | `GET` | `/v1/user_feedback?user_id={user_id}` | HTTP_200 | READ_SENSITIVE | API-EV-071 | [source](https://github.com/jpage4500/hubitat-drivers/blob/8c0466dd57f331e7828ff40443b35ea43946a183/orbit-bhyve/orbit-bhyve-controller.groovy#L440-L448) |
| REST-13 | `GET` | `/v1/landscapes` | OPERATOR_404 | READ | API-EV-071 | [source](https://github.com/jesimpsonjr-tech/bhyve-dashboard/blob/0df29724fe88bd509b0e5d87eca3f93f5359f117/bhyve_server.py#L185-L218) |
| REST-14 | `GET` | `/v1/weather_forecast/{device_id}` | OPERATOR_404 | READ | API-EV-071 | [source](https://github.com/jesimpsonjr-tech/bhyve-dashboard/blob/0df29724fe88bd509b0e5d87eca3f93f5359f117/bhyve_server.py#L185-L218) |
| REST-15 | `GET` | `/v1/bhyve_accounts/{account_id}` | OPERATOR_200 | READ_SENSITIVE | A2-E12 | — |
| REST-16 | `GET` | `/v1/bhyve_accounts/{account_id}/devices` | OPERATOR_404 | READ_SENSITIVE | API-EV-071 | — |
| REST-17 | `GET` | `/v1/device_assets/{device_id}` | OPERATOR_200 | SIGNED_ASSET_INDEX | API-EV-063 | — |
| REST-18 | `GET` | `/v1/device_assets/{device_id}/{yyyymmdd}` | OPERATOR_302_TO_VERIFIED_S3 | SIGNED_DAILY_ASSET | API-EV-063 | — |
| REST-19 | `POST` | `/v1/graph2` | SOURCE_ONLY | MUTATION_UNKNOWN | A2-E14 | [source](https://github.com/valiquette/homebridge-orbit-irrigation/blob/80a0731f633d8bedf941f14820975d58e4504e9d/src/orbitapi.ts#L225-L257) |
| REST-20 | `POST` | `/v1/sprinkler_timer_programs` | SOURCE_ONLY | STATE_CHANGE | A2-E15 | [source](https://github.com/sunnierseattle/bhyve/blob/d68f5c15a8a711c44a389864c41d51ccf311fac4/bhyve.py#L200-L244) |
| REST-21 | `PUT` | `/v1/sprinkler_timer_programs/{program_id}` | SOURCE_ONLY | STATE_CHANGE | A2-E15 | [source](https://github.com/sunnierseattle/bhyve/blob/d68f5c15a8a711c44a389864c41d51ccf311fac4/bhyve.py#L200-L244) |
| REST-22 | `DELETE` | `/v1/sprinkler_timer_programs/{program_id}` | SOURCE_ONLY | STATE_CHANGE | A2-E15 | [source](https://github.com/sunnierseattle/bhyve/blob/d68f5c15a8a711c44a389864c41d51ccf311fac4/bhyve.py#L200-L244) |
| REST-23 | `PUT` | `/v1/devices/{device_id}` | SOURCE_ONLY | STATE_CHANGE | A2-E16 | [source](https://github.com/waitbutY/bhyve-swift/blob/eec9bd2b414953e7d9ad7c096901bea2aea7ebb1/Sources/BHyve/REST/Endpoints.swift#L43-L46) |
| REST-24 | `POST` | `/v1/devices/{device_id}/rain_delay` | SOURCE_ONLY | STATE_CHANGE | A2-E17 | [source](https://github.com/jesimpsonjr-tech/bhyve-dashboard/blob/0df29724fe88bd509b0e5d87eca3f93f5359f117/bhyve_server.py#L292-L355) |
| REST-25 | `POST` | `/v1/devices/{device_id}/manual_watering` | SOURCE_ONLY | STATE_CHANGE | A2-E18 | [source](https://github.com/jesimpsonjr-tech/bhyve-dashboard/blob/0df29724fe88bd509b0e5d87eca3f93f5359f117/bhyve_server.py#L218-L292) |
| REST-26 | `POST` | `/v1/devices/{device_id}/stop` | SOURCE_ONLY | STATE_CHANGE | A2-E18 | [source](https://github.com/jesimpsonjr-tech/bhyve-dashboard/blob/0df29724fe88bd509b0e5d87eca3f93f5359f117/bhyve_server.py#L218-L292) |
| REST-27 | `PUT` | `/v1/landscape_descriptions/{landscape_id}` | SOURCE_ONLY | STATE_CHANGE | API-EV-017 | — |

Consult the [evidence method](methodology.md), [bounded observations](first-party-observations.md) and [inert OpenAPI JSON](../specifications/orbit-bhyve-full-openapi.json) before interpreting a row.

## Evidence traceability

Consult the [operation-by-operation source/observation crosswalk](../evidence/operation-evidence-crosswalk.md) and [complete 73-record evidence index](../evidence/research-index.md). Some source-analysis IDs (A2/A3) are **not** operator-observed network transactions.
