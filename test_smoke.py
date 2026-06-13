"""Minimal structural smoke test for the shipped single-file dashboard.

Run: python test_smoke.py   (exits non-zero on any failure)
or:  python -m pytest -q

This is a single-file HTML app whose stat engine is inline JavaScript, so the
smoke test validates the shipped-asset invariants that matter for a fully
offline GitHub-Pages app: the file loads, markup is balanced, script tags are
paired, no unfilled template placeholders survive, no BOM, and no hardcoded
local developer paths leaked into the shipped HTML.
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
HTML = HERE / "OBESITY_NMA_REVIEW.html"
INDEX = HERE / "index.html"


def _read(p):
    return p.read_text(encoding="utf-8")


def test_dashboard_exists_and_nonempty():
    assert HTML.exists(), f"missing {HTML.name}"
    assert HTML.stat().st_size > 100_000, "dashboard unexpectedly small"


def test_no_bom():
    for p in (HTML, INDEX):
        raw = p.read_bytes()
        assert not raw.startswith(b"\xef\xbb\xbf"), f"BOM in {p.name}"


def test_script_tags_paired():
    src = _read(HTML)
    opens = len(re.findall(r"<script\b", src))
    closes = src.count("</script>")
    assert opens == closes, f"<script> {opens} vs </script> {closes}"


def test_div_balance_in_markup():
    # Strip inline scripts: <div> appearing inside JS template literals is legal
    # and would otherwise create a false imbalance.
    src = re.sub(r"<script\b.*?</script>", "", _read(HTML), flags=re.S)
    opens = len(re.findall(r"<div[\s>]", src))
    closes = len(re.findall(r"</div>", src))
    assert opens == closes, f"div markup imbalance: {opens} open / {closes} close"


def test_no_unfilled_placeholders():
    src = _read(HTML)
    # Tokens are assembled from fragments so this scanner file does not itself
    # trip placeholder-detection lint while still checking the shipped HTML.
    tokens = ["REPLACE" + "_ME", "__PLACE" + "HOLDER__", "{{" + "REPLACE", "TODO" + "_FILL"]
    for tok in tokens:
        assert tok not in src, f"unfilled placeholder token {tok!r} in shipped HTML"


def test_no_hardcoded_local_paths():
    src = _read(HTML)
    assert "C:\\Users" not in src and "C:/Users" not in src, "hardcoded Windows user path"
    assert not re.search(r"/home/[a-z]+/", src), "hardcoded /home path"


def test_index_redirects_to_dashboard():
    assert INDEX.exists(), "missing index.html"
    assert "OBESITY_NMA_REVIEW.html" in _read(INDEX), "index does not point to dashboard"


def _run():
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for fn in fns:
        try:
            fn()
            print(f"PASS {fn.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL {fn.__name__}: {e}")
    print(f"\n{len(fns) - failed} passed, {failed} failed")
    return failed


if __name__ == "__main__":
    import sys
    sys.exit(1 if _run() else 0)
