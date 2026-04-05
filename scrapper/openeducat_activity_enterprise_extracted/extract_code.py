#!/usr/bin/env python3
"""
Odoo Module Source Code Extractor
===================================
Extracts all database-stored "source code" for installed modules:
  - XML Views (ir.ui.view)        → views/
  - Actions (ir.actions.*)        → actions/
  - Menus (ir.ui.menu)            → menus/
  - Security ACL (ir.model.access)→ security/
  - Record Rules (ir.rule)        → security/
  - Sequences (ir.sequence)       → data/
  - Cron Jobs (ir.cron)           → data/
  - Email Templates               → data/

Usage:
    pip install requests
    python extract_code.py                          # all modules
    python extract_code.py openeducat_activity_enterprise openeducat_core
"""

import re
import sys
import time
from pathlib import Path
from xml.dom import minidom

import requests

# ─────────────────────────────────────────────────────────
#  CONFIG
# ─────────────────────────────────────────────────────────
CONFIG = {
    "url": "https://abdelhadieddiraa46080.o19.oeducat.org",
    "session_id": "mbngZtbqkBkb9dfGlvlNCUJjazlxMg1j3xawMFuvP82GV2oN25l6Z6EFwQ0mYdVrvFRL-F5frOGHaIvpzNS5",
    "output_dir": "./odoo_source_extracted",
}
# ─────────────────────────────────────────────────────────

SESSION = requests.Session()
SESSION.headers.update({"Content-Type": "application/json"})
SESSION.cookies.set(
    "session_id", CONFIG["session_id"], domain="abdelhadieddiraa46080.o19.oeducat.org"
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


def get_installed_modules():
    mods = rpc(
        "ir.module.module",
        "search_read",
        args=[[["state", "=", "installed"]]],
        kwargs={"fields": ["name", "shortdesc"], "order": "name asc"},
    )
    return {m["name"]: m["shortdesc"] for m in mods}


def wrap_odoo(children_xml_str):
    return (
        f'<?xml version="1.0" encoding="utf-8"?>\n<odoo>\n{children_xml_str}\n</odoo>\n'
    )


def safe_filename(name, ext=".xml"):
    name = re.sub(r"[^\w\-]", "_", name or "unnamed")
    return name[:80] + ext


def save(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _esc(text):
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def pretty_arch(arch):
    """Try to pretty-print XML arch, return as-is if it fails."""
    if not arch:
        return "<t/>"
    try:
        dom = minidom.parseString(arch.encode("utf-8"))
        pretty = dom.toprettyxml(indent="    ")
        lines = pretty.splitlines()
        return "\n".join(lines[1:]) if lines[0].startswith("<?xml") else pretty
    except Exception:
        return arch


# ═══════════════════════════════════════════════════════════
#  EXTRACTORS
# ═══════════════════════════════════════════════════════════


def extract_views(module_name, out_dir):
    """Extract ir.ui.view → views/"""

    # Step 1: find view IDs belonging to this module via ir.model.data
    imd = rpc(
        "ir.model.data",
        "search_read",
        args=[[["module", "=", module_name], ["model", "=", "ir.ui.view"]]],
        kwargs={"fields": ["res_id", "name"], "limit": 0},
    )

    if not imd:
        return 0  # FIX: always return int

    view_ids = {r["res_id"]: r["name"] for r in imd}

    # Step 2: fetch full view data
    views = rpc(
        "ir.ui.view",
        "search_read",
        args=[[["id", "in", list(view_ids.keys())]]],
        kwargs={
            "fields": [
                "name",
                "type",
                "model",
                "arch_db",
                "inherit_id",
                "priority",
                "active",
                "key",
            ],
            "limit": 0,
        },
    )

    if not views:
        return 0  # FIX: always return int

    # Step 3: group by view type, write one file per type
    by_type = {}
    for v in views:
        t = v.get("type") or "other"
        by_type.setdefault(t, []).append(v)

    count = 0
    for vtype, vlist in by_type.items():
        lines = []
        for v in vlist:
            xmlid = view_ids.get(v["id"], v["name"])
            arch = pretty_arch(v.get("arch_db") or "<t/>")
            inherit = ""
            if v.get("inherit_id"):
                inherit = (
                    f'\n        <field name="inherit_id" '
                    f'ref="{_esc(str(v["inherit_id"][1]))}"/>'
                )
            lines.append(
                f'    <record id="{xmlid}" model="ir.ui.view">\n'
                f'        <field name="name">{_esc(v["name"])}</field>\n'
                f'        <field name="model">{_esc(v.get("model") or "")}</field>\n'
                f'        <field name="type">{vtype}</field>\n'
                f'        <field name="priority">{v.get("priority", 16)}</field>'
                f"{inherit}\n"
                f'        <field name="arch" type="xml">\n'
                f"{arch}\n"
                f"        </field>\n"
                f"    </record>"
            )
            count += 1

        save(
            out_dir / "views" / safe_filename(f"views_{vtype}"),
            wrap_odoo("\n\n".join(lines)),
        )

    return count  # FIX: always return int


def extract_actions(module_name, out_dir):
    """Extract all action types."""
    action_models = [
        (
            "ir.actions.act_window",
            [
                "name",
                "res_model",
                "view_mode",
                "domain",
                "context",
                "target",
                "binding_model_id",
            ],
        ),
        (
            "ir.actions.server",
            ["name", "model_id", "state", "code", "child_ids", "crud_model_id"],
        ),
        (
            "ir.actions.report",
            [
                "name",
                "model",
                "report_type",
                "report_name",
                "print_report_name",
                "binding_model_id",
            ],
        ),
        ("ir.actions.client", ["name", "tag", "context"]),
    ]

    total = 0
    for action_model, fields in action_models:
        imd = rpc(
            "ir.model.data",
            "search_read",
            args=[[["module", "=", module_name], ["model", "=", action_model]]],
            kwargs={"fields": ["res_id", "name"], "limit": 0},
        )
        if not imd:
            continue

        ids = {r["res_id"]: r["name"] for r in imd}
        records = rpc(
            action_model,
            "search_read",
            args=[[["id", "in", list(ids.keys())]]],
            kwargs={"fields": fields, "limit": 0},
        )
        if not records:
            continue

        lines = []
        short = action_model.split(".")[-1]
        for rec in records:
            xmlid = ids.get(rec["id"], rec.get("name", str(rec["id"])))
            inner = f'        <field name="name">{_esc(rec.get("name", ""))}</field>\n'
            for f in fields:
                if f == "name" or not rec.get(f):
                    continue
                val = rec[f]
                if isinstance(val, list):
                    val = val[1] if len(val) > 1 else val[0]
                inner += f'        <field name="{f}">{_esc(str(val))}</field>\n'
            lines.append(
                f'    <record id="{xmlid}" model="{action_model}">\n'
                f"{inner}"
                f"    </record>"
            )
            total += 1

        if lines:
            save(
                out_dir / "actions" / safe_filename(short),
                wrap_odoo("\n\n".join(lines)),
            )

    return total


def extract_menus(module_name, out_dir):
    """Extract ir.ui.menu."""
    imd = rpc(
        "ir.model.data",
        "search_read",
        args=[[["module", "=", module_name], ["model", "=", "ir.ui.menu"]]],
        kwargs={"fields": ["res_id", "name"], "limit": 0},
    )
    if not imd:
        return 0

    ids = {r["res_id"]: r["name"] for r in imd}
    records = rpc(
        "ir.ui.menu",
        "search_read",
        args=[[["id", "in", list(ids.keys())]]],
        kwargs={
            "fields": [
                "name",
                "parent_id",
                "action",
                "sequence",
                "active",
            ],  # FIX: removed groups_id
            "limit": 0,
        },
    )

    lines = []
    for rec in records:
        xmlid = ids.get(rec["id"], rec.get("name", str(rec["id"])))
        parent = (
            f' parent="{_esc(str(rec["parent_id"][1]))}"'
            if rec.get("parent_id")
            else ""
        )
        action = f' action="{_esc(str(rec["action"]))}"' if rec.get("action") else ""
        sequence = rec.get("sequence", 10)
        lines.append(
            f'    <menuitem id="{xmlid}"\n'
            f'              name="{_esc(rec["name"])}"\n'
            f'              sequence="{sequence}"{parent}{action}/>'
        )

    if lines:
        save(out_dir / "menus" / "menus.xml", wrap_odoo("\n".join(lines)))

    return len(lines)


def extract_security(module_name, out_dir):
    """Extract ACL (CSV) and record rules (XML)."""

    # Access rights → CSV
    imd_acl = rpc(
        "ir.model.data",
        "search_read",
        args=[[["module", "=", module_name], ["model", "=", "ir.model.access"]]],
        kwargs={"fields": ["res_id", "name"], "limit": 0},
    )

    acl_lines = [
        "id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink"
    ]
    if imd_acl:
        ids = {r["res_id"]: r["name"] for r in imd_acl}
        records = rpc(
            "ir.model.access",
            "search_read",
            args=[[["id", "in", list(ids.keys())]]],
            kwargs={
                "fields": [
                    "name",
                    "model_id",
                    "group_id",
                    "perm_read",
                    "perm_write",
                    "perm_create",
                    "perm_unlink",
                ],
                "limit": 0,
            },
        )
        for rec in records:
            xmlid = ids.get(rec["id"], rec["name"])
            model = rec["model_id"][1] if isinstance(rec.get("model_id"), list) else ""
            group = rec["group_id"][1] if isinstance(rec.get("group_id"), list) else ""
            acl_lines.append(
                f"{xmlid},{rec['name']},{model},{group},"
                f"{int(rec['perm_read'])},{int(rec['perm_write'])},"
                f"{int(rec['perm_create'])},{int(rec['perm_unlink'])}"
            )

    if len(acl_lines) > 1:
        save(out_dir / "security" / "ir.model.access.csv", "\n".join(acl_lines))

    # Record rules → XML
    imd_rules = rpc(
        "ir.model.data",
        "search_read",
        args=[[["module", "=", module_name], ["model", "=", "ir.rule"]]],
        kwargs={"fields": ["res_id", "name"], "limit": 0},
    )

    rule_lines = []
    if imd_rules:
        ids = {r["res_id"]: r["name"] for r in imd_rules}
        records = rpc(
            "ir.rule",
            "search_read",
            args=[[["id", "in", list(ids.keys())]]],
            kwargs={
                "fields": [
                    "name",
                    "model_id",
                    "domain_force",
                    "perm_read",
                    "perm_write",
                    "perm_create",
                    "perm_unlink",
                    "groups",
                ],
                "limit": 0,
            },
        )
        for rec in records:
            xmlid = ids.get(rec["id"], rec["name"])
            model = rec["model_id"][1] if isinstance(rec.get("model_id"), list) else ""
            domain = _esc(rec.get("domain_force") or "[(1,'=',1)]")
            rule_lines.append(
                f'    <record id="{xmlid}" model="ir.rule">\n'
                f'        <field name="name">{_esc(rec["name"])}</field>\n'
                f'        <field name="model_id" ref="{_esc(model)}"/>\n'
                f'        <field name="domain_force">{domain}</field>\n'
                f'        <field name="perm_read"   eval="{rec["perm_read"]}"/>\n'
                f'        <field name="perm_write"  eval="{rec["perm_write"]}"/>\n'
                f'        <field name="perm_create" eval="{rec["perm_create"]}"/>\n'
                f'        <field name="perm_unlink" eval="{rec["perm_unlink"]}"/>\n'
                f"    </record>"
            )

    if rule_lines:
        save(
            out_dir / "security" / "record_rules.xml",
            wrap_odoo("\n\n".join(rule_lines)),
        )

    return len(acl_lines) - 1, len(rule_lines)


def extract_data(module_name, out_dir):
    """Extract sequences, cron jobs, email templates."""
    extractors = [
        (
            "ir.sequence",
            [
                "name",
                "code",
                "prefix",
                "suffix",
                "padding",
                "number_increment",
                "number_next_actual",
            ],
        ),
        (
            "ir.cron",
            [
                "name",
                "model_id",
                "code",
                "interval_number",
                "interval_type",
                "numbercall",
                "active",
                "priority",
            ],
        ),
        (
            "mail.template",
            [
                "name",
                "model_id",
                "subject",
                "body_html",
                "email_from",
                "email_to",
                "lang",
            ],
        ),
    ]

    total = 0
    for model, fields in extractors:
        try:
            imd = rpc(
                "ir.model.data",
                "search_read",
                args=[[["module", "=", module_name], ["model", "=", model]]],
                kwargs={"fields": ["res_id", "name"], "limit": 0},
            )
            if not imd:
                continue

            ids = {r["res_id"]: r["name"] for r in imd}
            records = rpc(
                model,
                "search_read",
                args=[[["id", "in", list(ids.keys())]]],
                kwargs={"fields": fields, "limit": 0},
            )
            if not records:
                continue

            lines = []
            for rec in records:
                xmlid = ids.get(rec["id"], str(rec["id"]))
                inner = ""
                for f in fields:
                    val = rec.get(f)
                    if not val:
                        continue
                    if isinstance(val, list):
                        val = val[1] if len(val) > 1 else val[0]
                    inner += f'        <field name="{f}">{_esc(str(val))}</field>\n'
                lines.append(
                    f'    <record id="{xmlid}" model="{model}">\n{inner}    </record>'
                )
                total += 1

            short = model.replace(".", "_")
            save(out_dir / "data" / safe_filename(short), wrap_odoo("\n\n".join(lines)))

        except Exception as e:
            print(f"\n      ⚠️  {model}: {e}", end=" ")

    return total


# ═══════════════════════════════════════════════════════════
#  ORCHESTRATOR
# ═══════════════════════════════════════════════════════════


def extract_module(module_name, display_name, base_out):
    out_dir = base_out / module_name
    out_dir.mkdir(parents=True, exist_ok=True)

    results = {}

    print("    📄 Views …", end=" ", flush=True)
    results["views"] = extract_views(module_name, out_dir)
    print(results["views"])

    print("    ⚡ Actions …", end=" ", flush=True)
    results["actions"] = extract_actions(module_name, out_dir)
    print(results["actions"])

    print("    📂 Menus …", end=" ", flush=True)
    results["menus"] = extract_menus(module_name, out_dir)
    print(results["menus"])

    print("    🔒 Security …", end=" ", flush=True)
    acl, rules = extract_security(module_name, out_dir)
    results["acl"] = acl
    results["rules"] = rules
    print(f"{acl} ACL rows, {rules} rules")

    print("    📅 Data …", end=" ", flush=True)
    results["data"] = extract_data(module_name, out_dir)
    print(results["data"])

    save(
        out_dir / "README.md",
        f"""# 📦 {display_name} — Extracted Source

**Module:** `{module_name}`

## Summary

| Type | Count |
|------|-------|
| Views | {results["views"]} |
| Actions | {results["actions"]} |
| Menus | {results["menus"]} |
| ACL rows | {results["acl"]} |
| Record Rules | {results["rules"]} |
| Data records | {results["data"]} |

## Folder Structure

```
{module_name}/
├── views/          ← XML view definitions (grouped by type)
├── actions/        ← Window, server, report, client actions
├── menus/          ← Menu items
├── security/       ← ir.model.access.csv + record_rules.xml
└── data/           ← Sequences, cron jobs, email templates
```
""",
    )
    return results


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

    print(f"📦 Extracting {len(modules)} module(s) …\n")

    total_views = total_actions = total_menus = 0

    for i, (name, display) in enumerate(modules.items(), 1):
        print(f"[{i:>3}/{len(modules)}] {name}")
        try:
            r = extract_module(name, display, base_out)
            total_views += r.get("views", 0) or 0
            total_actions += r.get("actions", 0) or 0
            total_menus += r.get("menus", 0) or 0
        except Exception as e:
            print(f"    ❌ Failed: {e}")
        time.sleep(0.1)

    print("\n✅ Done!")
    print(f"   Views:   {total_views}")
    print(f"   Actions: {total_actions}")
    print(f"   Menus:   {total_menus}")
    print(f"   Output:  {base_out.resolve()}")
    print("\n💡 Tip: extract specific modules only:")
    print("   python extract_code.py openeducat_activity_enterprise openeducat_core")


if __name__ == "__main__":
    run()
