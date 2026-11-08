# PUB-2 verification and publication boundaries

A. **Traceability:** 73 IDs, one individual page per ID, an index JSON and a 55-operation crosswalk. If a source-only operation has no direct Git code pin, this is explicitly reported as a gap, not claimed as independently verified.

B. **Fidelity:** operator-reported and source-derived observations are distinct; the frozen full model and separate later WebSocket diagnostic remain separate. These are summaries, not a complete raw evidence export.

C. **Privacy:** original account payloads, local archives, controller/user/mesh values, full original private ledger, signed links and working repository history must remain excluded. Automated pattern scans do not substitute for manual inspection.

D. **Document hygiene:** known encoding defects repaired. Embedded relative references to unpublished working documents are de-linked or redirected to released evidence summaries; historical source filenames in the standalone request-map JSON are explicitly nonlinking provenance.

E. **Packaging:** one directory layout at ZIP root with no Git history, no duplicate nested folder tree. Publication only after human review and successful public-hosted CI.

## PUB-2.1 fixes and release gates

- Evidence summaries previously truncated by the generator (and three title-only
  API-5E summaries) have been replaced by dated, privacy-safe editorial results.
- API-EV-061 through API-EV-073 are now assigned explicit categories based on
  the original ledger, not guessed from a prose phrase. The classifications
  distinguish new live requests, offline checks and third-party source claims.
- REST-15 retains its frozen model identifier and adds direct operator evidence
  [API-EV-038](../evidence/records/API-EV-038.md); no new upstream source is invented.
- The public validator **allows** a new `.git` directory from GitHub checkout;
  only the **archive inspector** refuses Git metadata and unsafe entry paths.
- All evidence source citations avoid asserting that forked/vendored code is
  independently developed or independently server-verified.

Publication remains a **separate owner decision**. Before a public release,
confirm that the owner approves publication of the chosen historical activity
dates and aggregate counts; perform a final editorial/privacy review; verify
upstream public links and licensing obligations; and run CI on the new public
repository's exact initial commit. Automated success is not vendor approval.
