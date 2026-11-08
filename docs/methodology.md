# Research methodology and evidence qualification

The inventory combines **owner-reported bounded first-party observations** with independent **inspection of client implementations at pinned Git revisions**. It does not reproduce or reveal the owner's private account payloads.

- `OPERATOR_200`, `OPERATOR_404` etc.: a selected request outcome, **not** universal endpoint support or absence.
- `SOURCE_ONLY`, `SOURCE_ONLY_NOT_WIRE_VERIFIED`: a client constructs a method or WebSocket event; successful server execution is **not** shown.
- `SOURCE_INFERRED_NOT_LIVE_VERIFIED`: a conceptual relationship not directly tested.
- `UNKNOWN`, `NOT_TESTED`: no supported result; do not invent one.

Forks, vendored code and wrappers must not be double-counted as independent server evidence. See the [source matrix](../evidence/source-coverage.md), which identifies original Git commits and code lineage.

Inclusion in a JSON OpenAPI/AsyncAPI file does **not** raise confidence or authorize execution. Partial schemas remain partial. The historical request-surface JSON retains source filenames from an internal research checkpoint; those filenames do not imply public links.

## Record scope

The [73-entry evidence index](../evidence/research-index.md) includes implementation proof, source-only inference, offline processing and bounded observed API outcomes. The evidence phrases "VERIFIED (project implementation)" or "VERIFIED (client source)" do **not** establish vendor server success. Individual record classes extracted from narrative headings may require editorial review.
