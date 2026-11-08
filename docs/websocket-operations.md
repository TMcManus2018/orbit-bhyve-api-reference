# WebSocket interface — source-derived operation inventory

**28 source operations** represent **26 named JSON events** from public clients. Client sends and receive handlers are *not* proof of vendor acceptance, reply events or effect. A JSON `ping` event is distinct from a WebSocket protocol PING frame.

| ID | Candidate event | Direction | Research status | Evidence | Pinned upstream source |
| --- | --- | --- | --- | --- | --- |
| WS-01 | `app_connection` | OUTBOUND_AUTH | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E01 | [source](https://github.com/markse123/yardrelay-for-bhyve/blob/5f0717a766d5848d816d36be542e6b93dcb5f12e/server/orbit-client.js#L242-L250) |
| WS-02 | `ping` | OUTBOUND_KEEPALIVE | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E02 | [source](https://github.com/sebr/bhyve-home-assistant/blob/43fd888a9ecb9e914f4f0b1d0d818c3218c48e95/custom_components/bhyve/pybhyve/websocket.py#L95-L105) |
| WS-03 | `pong` | INBOUND_HANDLED | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E03 | [source](https://github.com/sunnierseattle/bhyve/blob/d68f5c15a8a711c44a389864c41d51ccf311fac4/bhyve.py#L149-L168) |
| WS-04 | `change_mode` | OUTBOUND_CONTROL | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E04 | [source](https://github.com/valiquette/homebridge-orbit-irrigation/blob/80a0731f633d8bedf941f14820975d58e4504e9d/src/orbitapi.ts#L324-L360) |
| WS-05 | `change_mode` | INBOUND_HANDLED | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E05 | [source](https://github.com/openhab/openhab-addons/blob/e3eeb3e9a918d1abe9b2b351a5958b0c1f9df0d5/bundles/org.openhab.binding.orbitbhyve/src/main/java/org/openhab/binding/orbitbhyve/internal/handler/OrbitBhyveBridgeHandler.java#L285-L296) |
| WS-06 | `rain_delay` | OUTBOUND_CONTROL | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E06 | [source](https://github.com/markse123/yardrelay-for-bhyve/blob/5f0717a766d5848d816d36be542e6b93dcb5f12e/server/orbit-client.js#L231-L240) |
| WS-07 | `rain_delay` | INBOUND_HANDLED | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E07 | [source](https://github.com/openhab/openhab-addons/blob/e3eeb3e9a918d1abe9b2b351a5958b0c1f9df0d5/bundles/org.openhab.binding.orbitbhyve/src/main/java/org/openhab/binding/orbitbhyve/internal/handler/OrbitBhyveBridgeHandler.java#L297-L299) |
| WS-08 | `watering_in_progress_notification` | INBOUND_HANDLED | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E08 | [source](https://github.com/openhab/openhab-addons/blob/e3eeb3e9a918d1abe9b2b351a5958b0c1f9df0d5/bundles/org.openhab.binding.orbitbhyve/src/main/java/org/openhab/binding/orbitbhyve/internal/handler/OrbitBhyveBridgeHandler.java#L264-L278) |
| WS-09 | `watering_complete` | INBOUND_HANDLED | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E09 | [source](https://github.com/openhab/openhab-addons/blob/e3eeb3e9a918d1abe9b2b351a5958b0c1f9df0d5/bundles/org.openhab.binding.orbitbhyve/src/main/java/org/openhab/binding/orbitbhyve/internal/handler/OrbitBhyveBridgeHandler.java#L279-L284) |
| WS-10 | `skip_active_station` | INBOUND_HANDLED | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E10 | [source](https://github.com/openhab/openhab-addons/blob/e3eeb3e9a918d1abe9b2b351a5958b0c1f9df0d5/bundles/org.openhab.binding.orbitbhyve/src/main/java/org/openhab/binding/orbitbhyve/internal/handler/OrbitBhyveBridgeHandler.java#L300-L302) |
| WS-11 | `program_changed` | INBOUND_HANDLED | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E11 | [source](https://github.com/openhab/openhab-addons/blob/e3eeb3e9a918d1abe9b2b351a5958b0c1f9df0d5/bundles/org.openhab.binding.orbitbhyve/src/main/java/org/openhab/binding/orbitbhyve/internal/handler/OrbitBhyveBridgeHandler.java#L303-L309) |
| WS-12 | `device_idle` | INBOUND_HANDLED | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E12 | [source](https://github.com/willioz/Obit-bhyve-python-package/blob/3cb75ca86e4124851b93d178b7dcb1611e742a31/orbit_bhyve/device.py#L64-L90) |
| WS-13 | `device_connected` | INBOUND_HANDLED | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E13 | [source](https://github.com/willioz/Obit-bhyve-python-package/blob/3cb75ca86e4124851b93d178b7dcb1611e742a31/orbit_bhyve/device.py#L87-L102) |
| WS-14 | `battery_status/device_status/fault` | INBOUND_HANDLED_GROUP | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E14 | [source](https://github.com/waitbutY/bhyve-swift/blob/eec9bd2b414953e7d9ad7c096901bea2aea7ebb1/Sources/BHyve/WebSocket/BHyveEvent.swift#L30-L52) |
| WS-15 | `clear_low_battery` | INBOUND_HANDLED | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E15 | [source](https://github.com/codyc1515/homebridge-orbit-bhyve/blob/a0429db5890b6f407f1db5e5df77ed03b4ce1dcf/index.js#L614-L619) |
| WS-16 | `sync` | OUTBOUND_CONTROL | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E16 | [source](https://github.com/valiquette/homebridge-orbit-irrigation/blob/80a0731f633d8bedf941f14820975d58e4504e9d/src/orbitapi.ts#L511-L521) |
| WS-17 | `fs_identify` | OUTBOUND_CONTROL | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E17 | [source](https://github.com/valiquette/homebridge-orbit-irrigation/blob/80a0731f633d8bedf941f14820975d58e4504e9d/src/orbitapi.ts#L530-L541) |
| WS-18 | `set_manual_preset_runtime` | OUTBOUND_CONTROL | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E18 | [source](https://github.com/norman2112/bhyve-mcp/blob/ec3a312d7020e51784a36b5e5fe03f97f6106d94/src/bhyve_mcp/pybhyve/client.py#L347-L355) |
| WS-19 | `program_list` | OUTBOUND_UNPROVEN_READ | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E19 | [source](https://github.com/willioz/Obit-bhyve-python-package/blob/3cb75ca86e4124851b93d178b7dcb1611e742a31/orbit_bhyve/client.py#L349-L390) |
| WS-20 | `program_save` | OUTBOUND_CONTROL | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E20 | [source](https://github.com/willioz/Obit-bhyve-python-package/blob/3cb75ca86e4124851b93d178b7dcb1611e742a31/orbit_bhyve/client.py#L392-L432) |
| WS-21 | `program_delete` | OUTBOUND_CONTROL | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E21 | [source](https://github.com/willioz/Obit-bhyve-python-package/blob/3cb75ca86e4124851b93d178b7dcb1611e742a31/orbit_bhyve/client.py#L434-L451) |
| WS-22 | `program_enable` | OUTBOUND_CONTROL | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E22 | [source](https://github.com/willioz/Obit-bhyve-python-package/blob/3cb75ca86e4124851b93d178b7dcb1611e742a31/orbit_bhyve/client.py#L453-L470) |
| WS-23 | `program_disable` | OUTBOUND_CONTROL | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E23 | [source](https://github.com/willioz/Obit-bhyve-python-package/blob/3cb75ca86e4124851b93d178b7dcb1611e742a31/orbit_bhyve/client.py#L472-L489) |
| WS-24 | `RFC6455 PING/PONG` | TRANSPORT_CONTROL | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E24 | [source](https://github.com/gillcaleb/orbit-bhyve-go-client/blob/bc05a2aa8ef2e067e37b0bf14cffa02958162d63/pkg/websocket/websocket.go#L61-L70) |
| WS-25 | `generic event handler` | INBOUND_GENERIC | SOURCE_ONLY_NOT_WIRE_VERIFIED | A3-E25 | [source](https://github.com/willioz/Obit-bhyve-python-package/blob/3cb75ca86e4124851b93d178b7dcb1611e742a31/orbit_bhyve/client.py#L166-L206) |
| WS-26 | `device_disconnected` | INBOUND_HANDLED | SOURCE_ONLY_NOT_WIRE_VERIFIED | API-EV-058 | — |
| WS-27 | `flow_sensor_state_changed` | INBOUND_HANDLED | SOURCE_ONLY_NOT_WIRE_VERIFIED | API-EV-058 | — |
| WS-28 | `set_manual_preset_time` | INBOUND_HANDLED | SOURCE_ONLY_NOT_WIRE_VERIFIED | API-EV-024 | — |

Selected first-party transport research did **not** establish accepted application authentication, subscription, recognized event delivery or controller effects. See [sanitized observations](first-party-observations.md) and the [inert AsyncAPI model](../specifications/orbit-bhyve-full-asyncapi.json).

## Evidence traceability

The [crosswalk](../evidence/operation-evidence-crosswalk.md) and [73-record index](../evidence/research-index.md) distinguish public client message definitions from actually observed WebSocket transport.
