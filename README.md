# Orbit B-hyve Cloud API — Unofficial Research Reference

> **Independent, documentation-only research.** This project is not affiliated with, supported by or endorsed by Orbit Irrigation. The cloud API is undocumented and can change without notice.

This reference combines **bounded first-party experiments** with code inspection of existing publicly available B-hyve repositories. It exists for developers researching the unofficial REST and WebSocket interfaces; it is **not a live API client or a verified vendor specification**.

## Scope (November 2026 research checkpoint)

| Inventoried source | Count |
| --- | ---: |
| REST method/path combinations | **27** over **24** path templates |
| WebSocket client-perspective operations | **28** (26 event labels) |
| Conceptual resource relationships | **13** |

These are **research inventory counts, not verified endpoint support or evidence of completeness**.

## Documentation

- [REST operations](docs/rest-operations.md): 27 candidate method/path pairs, risk and source evidence.
- [WebSocket operations](docs/websocket-operations.md): 28 client-side event constructs, without invented server acceptance.
- [Resource relationships](docs/resource-relationships.md): 13 conceptual edges and their uncertainties.
- [All 73 original research evidence IDs, sanitized and indexed](evidence/research-index.md) and [REST/WS evidence crosswalk](evidence/operation-evidence-crosswalk.md).
- [First-party experimental evidence](docs/first-party-observations.md): scoped, sanitized operator-reported findings.
- [Pinned third-party source matrix](evidence/source-coverage.md): repository lineage, forks and exact Git revisions.
- [Methodology](docs/methodology.md) and [open questions](docs/open-questions.md).
- [Inert OpenAPI 3.1 research JSON](specifications/orbit-bhyve-full-openapi.json), [inert AsyncAPI 3.0 research JSON](specifications/orbit-bhyve-full-asyncapi.json), [evidence model](specifications/orbit-bhyve-full-model.json) and [historical request-surface map](evidence/api5c-request-surface.json).
- [Synthetic examples](examples/README.md).

## Evidence classes

**Owner-observed** means one account owner reported a bounded HTTP/transport result. The original private API responses are not included and the observations are **not independently reproduced**. **Source-only** means a pinned public client constructs a request or event; this is not proof of vendor acceptance. **Inferred** means a hypothesized relationship without direct verification. **Unknown** is an explicitly unresolved claim.

The OpenAPI/AsyncAPI JSON files intentionally use `example.invalid` and `DO_NOT_EXECUTE` annotations. Do not replace those hosts to issue commands, infer safe controller effects, or follow the unverified zone-report redirect. See [security and responsible research](SECURITY.md).

## Provenance and publication boundary

This is a curated export of evidence-qualified research from a **private development repository** at snapshot commit `c00383815e9386fb25a3c6583251d75d3852729c`. It excludes private archives, source-code implementation, raw operator logs and local credentials. Some historical JSON provenance fields refer to private working-document filenames; they are *not* links to publicly available files.

Contributions must preserve the evidence distinctions in [CONTRIBUTING.md](CONTRIBUTING.md). [MIT license](LICENSE).

## PUB-2 editorial qualification

The 73-record index consists of **privacy-minimized extracts**, not a reproduction of the full private evidence ledger. The source-confirmation and claimed behaviour must be judged against the dated evidence classes. The full-model snapshot predates the separate API-EV-073 WebSocket CLOSE diagnostic; do not silently upgrade it. No private-authenticated responses, raw data or implementer credentials were added.

## PUB-2.1 publication verification

The current package includes curated, nontruncated summaries for the records
flagged in PUB-2 and a direct REST-15 evidence mapping. Run
`python scripts/validate_reference.py` in the fresh public Git checkout;
use `python scripts/validate_archive.py path/to/release.zip` to validate
that the distribution ZIP has no private Git metadata or duplicate paths.
Human content, privacy and upstream-link review remain mandatory.
