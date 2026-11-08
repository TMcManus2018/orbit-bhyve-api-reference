"""Offline PUB-2 validation of a research-only publication candidate.

Standard library only. Does not contact Orbit or any other network host.
"""

import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
IDS = [f"API-EV-{i:03d}" for i in range(1, 74)]
LINK = re.compile(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)")
SENSITIVE = re.compile(
    r"(?i)(X-Amz-(?:Signature|Credential|Security-Token)\s*=|"
    r"AWSAccessKeyId\s*=|Hatley Lane|Chaucer Court|VIS6109|"
    r"https://github\.com/TMcManus2018/orbit-bhyve-history-export/(?:blob|tree)/|"
    r"(?:[A-Z]:\\(?:Users|Documents|Program Files)\\)|"
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)"
)


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def main():
    # A new, independent public repository is expected to have .git during
    # checkout. Archive creation separately prohibits Git metadata.
    model = load("specifications/orbit-bhyve-full-model.json")
    oa = load("specifications/orbit-bhyve-full-openapi.json")
    ws = load("specifications/orbit-bhyve-full-asyncapi.json")
    req = load("evidence/api5c-request-surface.json")
    ix = load("evidence/research-index.json")
    assert [len(model[x]) for x in ("http", "websocket", "resource_edges")] == [27, 28, 13]
    assert [len(req[x]) for x in ("http", "websocket")] == [27, 28]
    assert model["source_map"] == "evidence/api5c-request-surface.json"
    assert ix["schema"] == "orbit-bhyve-public-evidence-index-v1"
    assert [r["id"] for r in ix["records"]] == IDS
    assert not any(r.get("editorial_review_required", True) for r in ix["records"]), (
        "Unresolved editorial evidence classification"
    )
    assert all(r.get("classification_method") != "INFERRED_FROM_PHRASE"
               for r in ix["records"])
    assert ix["public_summaries_are_full_records"] is False
    assert [s["url"] for s in oa["servers"]] == ["https://example.invalid"]
    assert oa["openapi"] == "3.1.0"
    ops = [val[k] for val in oa["paths"].values()
           for k in ("get", "post", "put", "patch", "delete") if k in val]
    assert len(ops) == 27 and all(op["x-execution-policy"] == "DO_NOT_EXECUTE" for op in ops)
    assert ws["asyncapi"] == "3.0.0"
    assert all(s["host"] == "example.invalid" for s in ws["servers"].values())
    assert len(ws["operations"]) == 28
    assert all(op["x-execution-policy"] == "DO_NOT_EXECUTE" for op in ws["operations"].values())
    for id_ in IDS:
        assert (ROOT / "evidence" / "records" / f"{id_}.md").is_file(), id_
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        assert not path.is_symlink(), path
        if path.suffix not in (".md", ".json", ".yaml", ".yml"):
            continue
        text = path.read_text(encoding="utf-8")
        assert not SENSITIVE.search(text), f"Sensitive text pattern: {path}"
        assert not any(x in text for x in ("â†’", "â†”", "â€“", "â€”", "â€™")), path
        assert "[longer source entry withheld]" not in text, path
        assert "Pinned, independent third-party code references" not in text, path
        if path.suffix == ".json":
            json.loads(text)
        for match in LINK.finditer(text):
            href = match.group(2)
            if urlparse(href).scheme or href.startswith(("#", "mailto:")):
                continue
            rel = unquote(href.split("#", 1)[0])
            if rel:
                dest = (path.parent / rel).resolve()
                assert dest.is_relative_to(ROOT) and dest.is_file(), (path, href)
    crosswalk = (ROOT / "evidence/operation-evidence-crosswalk.md").read_text(encoding="utf-8")
    assert "[API-EV-038](records/API-EV-038.md)" in next(
        line for line in crosswalk.splitlines() if line.startswith("| REST-15 |")
    )
    assert (ROOT / "evidence/records/API-EV-038.md").read_text(encoding="utf-8").find(
        "GET /v1/bhyve_accounts/{account_id}") >= 0
    assert (ROOT / "evidence/records/API-EV-071.md").read_text(encoding="utf-8").find(
        "11 object records") >= 0
    print("PUB-2.1 reference verification passed: 73 records; 27 REST; 28 WS; 13 relationships")


if __name__ == "__main__":
    main()
