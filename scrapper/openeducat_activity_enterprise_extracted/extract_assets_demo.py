#!/usr/bin/env python3
"""
Odoo Module CSS Assets & Demo Data Extractor
=============================================
Extracts two additional artifact types that the main extractor misses:

  1. CSS / JS Assets  → assets/
     Pulls `ir.asset` records and also resolves linked attachments
     (ir.attachment) that hold the actual file content.

  2. Demo Data        → demo/
     Pulls ALL records whose `ir.model.data` row is flagged
     `demo = True` for the requested module, then serialises
     them as importable XML <record> blocks grouped by model.

Usage:
    pip install requests
    python extract_assets_demo.py                           # all modules
    python extract_assets_demo.py openeducat_onboarding
"""

import re
import sys
import time
import base64
from pathlib import Path
from xml.dom import minidom

import requests

# ─────────────────────────────────────────────────────────
#  CONFIG  (copy from your main extract_code.py)
# ─────────────────────────────────────────────────────────
CONFIG = {
    "url": "https://abdelhadieddiraa46080.o19.oeducat.org",
    "session_id": "bCL3RKcSihsSL0cTSUernn2_c0LFumbNVt05vjYUnj7Ws-8eIJAzA2I4Qj8RK75Lz0rCxsRSoaR_J2O2GYwB",
    "output_dir": "./odoo_source_extracted",
}
# ─────────────────────────────────────────────────────────

SESSION = requests.Session()
SESSION.headers.update({"Content-Type": "application/json"})
SESSION.cookies.set(
    "session_id", CONFIG["session_id"],
    domain="abdelhadieddiraa46080.o19.oeducat.org"
)

_rpc_id = 0


def rpc(model, method, args=None, kwargs=None):
    global _rpc_id
    _rpc_id += 1
    r = SESSION.post(
        f"{CONFIG['url']}/web/dataset/call_kw",
        json={
            "jsonrpc": "2.0",
            "method": "call",
            "id": _rpc_id,
            "params": {
                "model": model,
                "method": method,
                "args": args or [],
                "kwargs": kwargs or {},
            },
        },
        timeout=60,
    )
    r.raise_for_status()
    data = r.json()
    if "error" in data:
        msg = data["error"].get("data", {}).get("message", str(data["error"]))
        raise RuntimeError(f"RPC [{model}.{method}]: {msg}")
    return data["result"]


# ─────────────────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────────────────

def wrap_odoo(children_xml_str: str) -> str:
    return f'<?xml version="1.0" encoding="utf-8"?>\n<odoo>\n{children_xml_str}\n</odoo>\n'


def safe_filename(name: str, ext: str = ".xml") -> str:
    name = re.sub(r"[^\w\-]", "_", name or "unnamed")
    return name[:80] + ext


def save(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def save_bytes(path: Path, data: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _esc(text: str) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def pretty_xml(raw: str) -> str:
    """Best-effort pretty-print; return raw on failure."""
    if not raw:
        return "<t/>"
    try:
        dom = minidom.parseString(raw.encode("utf-8"))
        pretty = dom.toprettyxml(indent="    ")
        lines = pretty.splitlines()
        return "\n".join(lines[1:]) if lines[0].startswith("<?xml") else pretty
    except Exception:
        return raw


# ═══════════════════════════════════════════════════════════
#  1.  CSS / JS ASSETS
# ═══════════════════════════════════════════════════════════

def extract_assets(module_name: str, out_dir: Path) -> int:
    """
    Pull ir.asset records for this module.

    Two outputs are produced:
      assets/ir_asset.xml          – the asset bundle registrations
      assets/<name>.<ext>          – raw file content when the asset is
                                     stored as an ir.attachment (db assets)
    """

    # ── Step 1: find ir.asset records via ir.model.data ──────────────
    imd = rpc(
        "ir.model.data",
        "search_read",
        args=[[["module", "=", module_name], ["model", "=", "ir.asset"]]],
        kwargs={"fields": ["res_id", "name"], "limit": 0},
    )

    # ir.asset may not exist in all Odoo versions; also try a direct search
    # by the bundle path pattern  "/<module_name>/…"
    direct = rpc(
        "ir.asset",
        "search_read",
        args=[[["path", "like", f"/{module_name}/"]]],
        kwargs={
            "fields": ["name", "bundle", "path", "directive", "active", "sequence"],
            "limit": 0,
        },
    )

    imd_ids = {r["res_id"]: r["name"] for r in (imd or [])}
    imd_records = []
    if imd_ids:
        imd_records = rpc(
            "ir.asset",
            "search_read",
            args=[[["id", "in", list(imd_ids.keys())]]],
            kwargs={
                "fields": ["name", "bundle", "path", "directive", "active", "sequence"],
                "limit": 0,
            },
        )

    # merge, deduplicate by id
    seen_ids = set()
    all_assets = []
    for rec in (imd_records or []) + (direct or []):
        if rec["id"] not in seen_ids:
            seen_ids.add(rec["id"])
            all_assets.append(rec)

    if not all_assets:
        return 0

    # ── Step 2: write ir_asset.xml ────────────────────────────────────
    lines = []
    for rec in all_assets:
        xmlid = imd_ids.get(rec["id"], f"asset_{rec['id']}")
        lines.append(
            f'    <record id="{xmlid}" model="ir.asset">\n'
            f'        <field name="name">{_esc(rec.get("name", ""))}</field>\n'
            f'        <field name="bundle">{_esc(rec.get("bundle", ""))}</field>\n'
            f'        <field name="path">{_esc(rec.get("path", ""))}</field>\n'
            f'        <field name="directive">{_esc(rec.get("directive", "include"))}</field>\n'
            f'        <field name="sequence">{rec.get("sequence", 16)}</field>\n'
            f'        <field name="active" eval="{rec.get("active", True)}"/>\n'
            f"    </record>"
        )

    save(out_dir / "assets" / "ir_asset.xml", wrap_odoo("\n\n".join(lines)))

    # ── Step 3: pull actual file bytes from ir.attachment ─────────────
    # Odoo stores customised/db-stored assets as attachments with
    # url = the asset path.  We try to fetch them.
    paths = [r["path"] for r in all_assets if r.get("path")]
    if paths:
        attachments = rpc(
            "ir.attachment",
            "search_read",
            args=[[["url", "in", paths]]],
            kwargs={"fields": ["name", "url", "datas", "mimetype"], "limit": 0},
        )
        for att in (attachments or []):
            raw_b64 = att.get("datas")
            if not raw_b64:
                continue
            try:
                raw_bytes = base64.b64decode(raw_b64)
            except Exception:
                continue

            # derive a safe filename from the url path
            url_path = att.get("url", att.get("name", "unknown"))
            fname = url_path.lstrip("/").replace("/", "_")
            save_bytes(out_dir / "assets" / fname, raw_bytes)

    return len(all_assets)


# ═══════════════════════════════════════════════════════════
#  2.  DEMO DATA
# ═══════════════════════════════════════════════════════════

# Fields that are almost never useful in re-imported demo data
_SKIP_FIELDS = {
    "id", "create_date", "write_date", "create_uid", "write_uid",
    "__last_update", "display_name", "message_ids", "message_follower_ids",
    "activity_ids", "website_message_ids",
}

# Models whose records we never want to dump (too big / system)
_SKIP_MODELS = {
    "ir.ui.view", "ir.ui.menu", "ir.actions.act_window", "ir.actions.server",
    "ir.actions.report", "ir.rule", "ir.model.access", "ir.asset",
    "ir.model", "ir.model.fields", "ir.module.module",
}


def _fetch_model_fields(model_name: str) -> dict:
    """Return {field_name: field_info} for a model."""
    try:
        return rpc(model_name, "fields_get", args=[], kwargs={"attributes": ["type", "relation", "required"]})
    except Exception:
        return {}


def _serialise_value(fname: str, ftype: str, value, relation: str = "") -> str | None:
    """
    Convert a Python value returned by search_read into an XML snippet
    suitable for a <field> tag inside a <record>.

    Returns None when the field should be skipped.
    """
    if value is False or value is None:
        return None

    # many2one → ref attribute (best-effort; falls back to string id)
    if ftype == "many2one":
        if not isinstance(value, list):
            return None
        rec_id = value[0]
        return f'        <field name="{fname}" ref="{relation},{rec_id}"/>\n'

    # one2many / many2many → skip (handled by the owning side)
    if ftype in ("one2many", "many2many"):
        return None

    # binary → inline base64
    if ftype == "binary":
        if not value:
            return None
        return f'        <field name="{fname}" type="base64">{value}</field>\n'

    # boolean
    if ftype == "boolean":
        return f'        <field name="{fname}" eval="{value}"/>\n'

    # html / text / char / integer / float / monetary / date / datetime / selection
    escaped = _esc(str(value))
    return f'        <field name="{fname}">{escaped}</field>\n'


def extract_demo_data(module_name: str, out_dir: Path) -> int:
    """
    Find every ir.model.data row for this module that has demo=True,
    group by model, fetch the actual records, and write one XML file
    per model under demo/.
    """

    # ── Step 1: all demo IMD rows for this module ─────────────────────
    imd_rows = rpc(
        "ir.model.data",
        "search_read",
        args=[[
            ["module", "=", module_name],
            ["demo", "=", True],
        ]],
        kwargs={"fields": ["res_id", "name", "model"], "limit": 0},
    )

    if not imd_rows:
        # Older Odoo: demo flag may not exist on ir.model.data.
        # Fall back: fetch ALL imd rows and note them — user can review.
        print("      ⚠️  No rows with demo=True found; trying all IMD rows as fallback …", end=" ")
        imd_rows = rpc(
            "ir.model.data",
            "search_read",
            args=[[["module", "=", module_name]]],
            kwargs={"fields": ["res_id", "name", "model"], "limit": 0},
        )
        fallback = True
    else:
        fallback = False

    if not imd_rows:
        return 0

    # group by model
    by_model: dict[str, dict[int, str]] = {}
    for row in imd_rows:
        model = row["model"]
        if model in _SKIP_MODELS:
            continue
        by_model.setdefault(model, {})[row["res_id"]] = row["name"]

    if not by_model:
        return 0

    total = 0

    for model_name, id_to_xmlid in by_model.items():
        try:
            field_meta = _fetch_model_fields(model_name)
        except Exception:
            field_meta = {}

        # fields to fetch: everything except the skip list
        fetch_fields = [
            f for f in field_meta
            if f not in _SKIP_FIELDS
            and field_meta[f].get("type") not in ("one2many",)
        ] or ["name"]

        try:
            records = rpc(
                model_name,
                "search_read",
                args=[[["id", "in", list(id_to_xmlid.keys())]]],
                kwargs={"fields": fetch_fields, "limit": 0},
            )
        except Exception as e:
            print(f"\n      ⚠️  Could not read {model_name}: {e}", end=" ")
            continue

        if not records:
            continue

        lines = []
        for rec in records:
            xmlid = id_to_xmlid.get(rec["id"], f"{model_name.replace('.','_')}_{rec['id']}")
            inner = ""
            for fname, value in rec.items():
                if fname == "id" or fname in _SKIP_FIELDS:
                    continue
                fmeta = field_meta.get(fname, {})
                ftype = fmeta.get("type", "char")
                relation = fmeta.get("relation", "")
                snippet = _serialise_value(fname, ftype, value, relation)
                if snippet:
                    inner += snippet

            if not inner.strip():
                continue  # nothing useful to write

            lines.append(
                f'    <!-- {"FALLBACK — review before import" if fallback else "demo"} -->\n'
                f'    <record id="{xmlid}" model="{model_name}">\n'
                f"{inner}"
                f"    </record>"
            )
            total += 1

        if lines:
            fname = safe_filename(model_name.replace(".", "_"))
            save(
                out_dir / "demo" / fname,
                wrap_odoo("\n\n".join(lines)),
            )

    return total


# ═══════════════════════════════════════════════════════════
#  ORCHESTRATOR
# ═══════════════════════════════════════════════════════════

def extract_module(module_name: str, base_out: Path):
    out_dir = base_out / module_name
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"  🎨 CSS/JS Assets …", end=" ", flush=True)
    try:
        n = extract_assets(module_name, out_dir)
        print(n)
    except Exception as e:
        n = 0
        print(f"ERROR: {e}")

    print(f"  📋 Demo Data …", end=" ", flush=True)
    try:
        d = extract_demo_data(module_name, out_dir)
        print(d)
    except Exception as e:
        d = 0
        print(f"ERROR: {e}")

    # README
    save(
        out_dir / "README_assets_demo.md",
        f"""# 🎨 {module_name} — Assets & Demo Data

## Summary

| Type | Count |
|------|-------|
| CSS/JS assets | {n} |
| Demo data records | {d} |

## Folder Structure

```
{module_name}/
├── assets/
│   ├── ir_asset.xml        ← bundle registrations (re-importable)
│   └── *.css / *.js        ← raw file bytes (only if stored in DB)
└── demo/
    └── <model_name>.xml    ← one file per model, demo=True records
```

## Notes

- **assets/ir_asset.xml** lists every `ir.asset` record registered by
  this module.  File bytes are only written when the asset is stored
  as an `ir.attachment` in the database (custom overrides).  Static
  files that live on the filesystem are referenced by path only.

- **demo/*.xml** contains every record tagged `demo=True` in
  `ir.model.data`.  `many2one` fields are written as `ref=` with the
  relation model and DB id — you may need to replace those with proper
  XML-IDs before re-importing.

- Binary fields (images, etc.) are embedded as inline base64.
""",
    )
    return n, d


def get_installed_modules():
    mods = rpc(
        "ir.module.module",
        "search_read",
        args=[[["state", "=", "installed"]]],
        kwargs={"fields": ["name", "shortdesc"], "order": "name asc"},
    )
    return {m["name"]: m["shortdesc"] for m in mods}


def run():
    target_modules = sys.argv[1:] if len(sys.argv) > 1 else None

    base_out = Path(CONFIG["output_dir"])
    base_out.mkdir(parents=True, exist_ok=True)

    print("🔍 Fetching installed modules …")
    all_modules = get_installed_modules()

    if target_modules:
        modules = {k: v for k, v in all_modules.items() if k in target_modules}
        missing = set(target_modules) - set(modules)
        if missing:
            print(f"⚠️  Not found / not installed: {missing}")
    else:
        modules = all_modules

    print(f"📦 Extracting assets & demo data from {len(modules)} module(s) …\n")

    total_assets = total_demo = 0

    for i, (name, display) in enumerate(modules.items(), 1):
        print(f"[{i:>3}/{len(modules)}] {name}")
        try:
            na, nd = extract_module(name, base_out)
            total_assets += na
            total_demo += nd
        except Exception as e:
            print(f"    ❌ Failed: {e}")
        time.sleep(0.1)

    print("\n✅ Done!")
    print(f"   Assets:     {total_assets}")
    print(f"   Demo rows:  {total_demo}")
    print(f"   Output:     {base_out.resolve()}")
    print("\n💡 Run against specific modules only:")
    print("   python extract_assets_demo.py openeducat_onboarding openeducat_core")


if __name__ == "__main__":
    run()