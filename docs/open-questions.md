# Unresolved questions and limitations

- **Authentication:** Universal API-key/session token/header/app-ID combinations and WebSocket credential acceptance are not verified.
- **Watering history:** Long-term REST retention, pagination and all-date asset equivalence remain unproven; an earlier `watering_events: null` discrepancy is unresolved.
- **Event logs:** Selected page-size behaviour differed from expected parameter semantics.
- **Zone reports:** One 302 redirect was classified but its destination was not retrieved; payload and authorization boundary are unknown.
- **Accounts, users and topology:** Some candidate selectors were missing; selected routes returned 404; one successful mesh GET did not verify contents or general availability.
- **WebSocket:** App authentication, accepted subscription, incoming event schemas/order and CLOSE cause remain unknown.
- **Mutations:** Source-derived REST and WebSocket control operations have not been experimentally validated, including their persistent or physical effects.
- **Currency/completeness:** Pinned clients can become stale, and undiscovered vendor endpoints may exist.

Documenting an unknown is preferable to assuming a server contract. Publication is **not** authorization for new live experiments.
