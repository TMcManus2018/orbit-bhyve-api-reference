# Contributing to the unofficial API reference

Contributors should distinguish experiment, source code, inference and unknown status. Every third-party code assertion should point to a pinned commit and relevant lines; copied/vendored/forked implementations must not be counted as independent confirmations.

Do not invent request schemas, elevate source-only claims to server verification, or submit real credentials, account identifiers, signed URLs, private histories or raw responses. Do not replace `example.invalid` with a real server in published specifications or introduce runnable control code.

Run `python scripts/validate_reference.py` from the generated reference root before proposing changes.
