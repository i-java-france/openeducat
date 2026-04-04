#!/usr/bin/env python3
"""
Odoo → Obsidian Technical Documentation Scraper
================================================
Fetches installed modules + full technical docs:
  - Module metadata (version, author, license…)
  - Menus, Views, Reports added by the module
  - Dependencies (with names)
  - All Models/Tables the module defines
  - All Fields per Model (name, type, description)
  - Access Rights per Model
  - Record Rules per Model

Usage:
    pip install requests markdownify
    python main.py
"""

import re
import time
from pathlib import Path

import requests

try:
    from markdownify import markdownify as to_md
except ImportError:
    raise SystemExit("Run:  pip install markdownify")

# ─────────────────────────────────────────────────────────
#  CONFIG
# ─────────────────────────────────────────────────────────
CONFIG = {
    "url": "https://abdelhadieddiraa46080.o19.oeducat.org",
    "session_id": "eIjYQvr_ab6JXIUaRS3BT5x-VuJNDsy-c6hEXRX0-pD6a-0Vx3H-XQYFTqU2LXb382A_w8cBUd2dpgGw8CxY",
    "output_dir": "./odoo_modules_obsidian",
    "vault_tag": "odoo/module",
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
    payload = {
        "jsonrpc": "2.0",
        "method": "call",
        "id": _rpc_id,
        "params": {
            "model": model,
            "method": method,
            "args": args or [],
            "kwargs": kwargs or {},
        },
    }
    r = SESSION.post(f"{CONFIG['url']}/web/dataset/call_kw", json=payload, timeout=60)
    r.raise_for_status()
    data = r.json()
    if "error" in data:
        msg = data["error"].get("data", {}).get("message", str(data["error"]))
        raise RuntimeError(f"RPC [{model}.{method}]: {msg}")
    return data["result"]


# ─────────────────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────────────────


def state_emoji(state):
    return {
        "installed": "🟢",
        "uninstalled": "⚪",
        "to install": "🔵",
        "to upgrade": "🟡",
        "to remove": "🔴",
    }.get(state, "❓")


def html2md(html):
    if not html or str(html).strip() in ("", "false", "False"):
        return "_No description._"
    result = to_md(
        html, heading_style="ATX", bullets="-", strip=["script", "style", "button"]
    )
    return re.sub(r"\n{3,}", "\n\n", result).strip()


def slugify(name):
    return re.sub(r"[^\w\-]", "_", name).lower()


def cat_name(cat):
    if isinstance(cat, list) and len(cat) == 2:
        return str(cat[1])
    return str(cat) if cat else "Uncategorized"


def bullets(text, prefix="- "):
    """Turn a newline-separated string into a markdown bullet list."""
    if not text or str(text).strip() in ("", "False", "false"):
        return "_none_"
    lines = [l.strip() for l in str(text).splitlines() if l.strip()]
    return "\n".join(f"{prefix}`{l}`" for l in lines)


# ─────────────────────────────────────────────────────────
#  FETCH MODULES
# ─────────────────────────────────────────────────────────


def fetch_installed_modules():
    print("📦 Fetching installed modules …")
    fields = [
        "name",
        "shortdesc",
        "summary",
        "description_html",
        "author",
        "maintainer",
        "contributors",
        "website",
        "installed_version",
        "latest_version",
        "license",
        "state",
        "category_id",
        "auto_install",
        "application",
        "menus_by_module",
        "views_by_module",
        "reports_by_module",
        "dependencies_id",
        "module_type",
    ]
    modules = rpc(
        "ir.module.module",
        "search_read",
        args=[[["state", "=", "installed"]]],
        kwargs={"fields": fields, "order": "name asc"},
    )
    print(f"   ✅ {len(modules)} installed modules found")
    return modules


# ─────────────────────────────────────────────────────────
#  FETCH DEPENDENCY NAMES
# ─────────────────────────────────────────────────────────


def fetch_dep_names(dep_ids):
    """Resolve dependency IDs → technical names."""
    if not dep_ids:
        return []
    # dependencies_id points to ir.module.module.dependency records
    deps = rpc(
        "ir.module.module.dependency",
        "search_read",
        args=[[["id", "in", dep_ids]]],
        kwargs={"fields": ["name"], "limit": 0},
    )
    return [d["name"] for d in deps]


# ─────────────────────────────────────────────────────────
#  FETCH TECHNICAL DOCS: Models + Fields + ACL + Rules
# ─────────────────────────────────────────────────────────


def fetch_models_for_module(module_name):
    """
    Get all ir.model records that belong to this module.
    Strategy: search ir.model.data for records of type ir.model
    belonging to this module, then read the model details.
    """
    # Find model xmlids belonging to this module
    imd_records = rpc(
        "ir.model.data",
        "search_read",
        args=[
            [
                ["module", "=", module_name],
                ["model", "=", "ir.model"],
            ]
        ],
        kwargs={"fields": ["res_id", "name"], "limit": 0},
    )

    if not imd_records:
        return []

    model_ids = [r["res_id"] for r in imd_records]

    models = rpc(
        "ir.model",
        "search_read",
        args=[[["id", "in", model_ids]]],
        kwargs={
            "fields": [
                "name",
                "model",
                "info",
                "state",
                "transient",
                "is_mail_thread",
                "field_id",
                "access_ids",
                "rule_ids",
            ],
            "limit": 0,
        },
    )
    return models


def fetch_fields_for_model(field_ids):
    """Fetch field metadata for a list of field IDs."""
    if not field_ids:
        return []
    return rpc(
        "ir.model.fields",
        "search_read",
        args=[[["id", "in", field_ids]]],
        kwargs={
            "fields": [
                "name",
                "field_description",
                "ttype",
                "required",
                "readonly",
                "store",
                "relation",
                "help",
            ],
            "order": "name asc",
            "limit": 0,
        },
    )


def fetch_access_for_model(access_ids):
    if not access_ids:
        return []
    return rpc(
        "ir.model.access",
        "search_read",
        args=[[["id", "in", access_ids]]],
        kwargs={
            "fields": [
                "name",
                "group_id",
                "perm_read",
                "perm_write",
                "perm_create",
                "perm_unlink",
            ],
            "limit": 0,
        },
    )


def fetch_rules_for_model(rule_ids):
    if not rule_ids:
        return []
    return rpc(
        "ir.rule",
        "search_read",
        args=[[["id", "in", rule_ids]]],
        kwargs={
            "fields": [
                "name",
                "domain_force",
                "groups",
                "perm_read",
                "perm_write",
                "perm_create",
                "perm_unlink",
            ],
            "limit": 0,
        },
    )


# ─────────────────────────────────────────────────────────
#  BUILD OBSIDIAN NOTE
# ─────────────────────────────────────────────────────────


def perm_str(rec):
    p = []
    if rec.get("perm_read"):
        p.append("R")
    if rec.get("perm_write"):
        p.append("W")
    if rec.get("perm_create"):
        p.append("C")
    if rec.get("perm_unlink"):
        p.append("D")
    return "/".join(p) if p else "-"


def render_model_section(model, fields, accesses, rules):
    lines = []
    transient = "✳️ Transient (Wizard)" if model.get("transient") else ""
    mail = "📧 Mail Thread" if model.get("is_mail_thread") else ""
    badges = "  ".join(filter(None, [transient, mail]))

    lines.append(f"\n### 🗃️ `{model['model']}` — {model['name']}")
    if badges:
        lines.append(f"> {badges}")
    if model.get("info"):
        lines.append(f"\n{model['info']}\n")

    # Fields table
    if fields:
        lines.append("\n**Fields:**\n")
        lines.append("| Field | Label | Type | Req | Store | Relation |")
        lines.append("|-------|-------|------|-----|-------|----------|")
        for f in fields:
            req = "✅" if f.get("required") else ""
            store = "✅" if f.get("store") else ""
            rel = f.get("relation") or ""
            label = f.get("field_description") or ""
            lines.append(
                f"| `{f['name']}` | {label} | `{f['ttype']}` "
                f"| {req} | {store} | {rel} |"
            )

    # Access rights table
    if accesses:
        lines.append("\n**Access Rights:**\n")
        lines.append("| Name | Group | Perms |")
        lines.append("|------|-------|-------|")
        for a in accesses:
            grp = (
                a["group_id"][1] if isinstance(a.get("group_id"), list) else "Everyone"
            )
            lines.append(f"| {a['name']} | {grp} | `{perm_str(a)}` |")

    # Record rules
    if rules:
        lines.append("\n**Record Rules:**\n")
        for r in rules:
            grps = (
                ", ".join(
                    g[1] if isinstance(g, list) else str(g)
                    for g in (r.get("groups") or [])
                )
                or "Global"
            )
            lines.append(f"- **{r['name']}** ({grps}) `{perm_str(r)}`")
            if r.get("domain_force"):
                lines.append(f"  - Domain: `{r['domain_force']}`")

    return "\n".join(lines)


def build_note(mod, dep_names, models_data):
    cat = cat_name(mod.get("category_id"))
    state = mod.get("state", "unknown")

    tags = [
        CONFIG["vault_tag"],
        f"odoo/state/{state.replace(' ', '_')}",
        f"odoo/category/{re.sub(r'[^\\w]', '_', cat.lower())}",
    ]
    if mod.get("application"):
        tags.append("odoo/app")

    # ── Frontmatter ──────────────────────────────────────
    fm = f"""---
title: "{mod.get("shortdesc") or mod["name"]}"
module: "{mod["name"]}"
state: "{state}"
version: "{mod.get("installed_version") or "N/A"}"
author: "{mod.get("author") or "N/A"}"
maintainer: "{mod.get("maintainer") or "N/A"}"
website: "{mod.get("website") or ""}"
license: "{mod.get("license") or "N/A"}"
category: "{cat}"
application: {str(bool(mod.get("application"))).lower()}
auto_install: {str(bool(mod.get("auto_install"))).lower()}
tags: [{", ".join(tags)}]
---"""

    # ── Header ───────────────────────────────────────────
    header = f"""
# {state_emoji(state)} {mod.get("shortdesc") or mod["name"]}

> **Module:** `{mod["name"]}`  |  **Version:** `{mod.get("installed_version") or "N/A"}`
> **Category:** {cat}  |  **License:** `{mod.get("license") or "N/A"}`
> **Author:** {mod.get("author") or "N/A"}
> **Website:** {mod.get("website") or "_N/A_"}
"""

    # ── Dependencies ─────────────────────────────────────
    dep_section = "## 🔗 Dependencies\n\n"
    if dep_names:
        dep_section += " ".join(f"[[{d}]]" for d in dep_names)
    else:
        dep_section += "_none_"

    # ── Description ──────────────────────────────────────
    desc_section = f"""
## 📖 Description

{html2md(mod.get("description_html") or mod.get("summary") or "")}
"""

    # ── Menus / Views / Reports ───────────────────────────
    ui_section = f"""
## 🖥️ UI Components

### Menus
{bullets(mod.get("menus_by_module"))}

### Views
{bullets(mod.get("views_by_module"))}

### Reports
{bullets(mod.get("reports_by_module"))}
"""

    # ── Technical: Models ─────────────────────────────────
    tech_section = "\n## 🛠️ Technical Documentation\n"

    if models_data:
        tech_section += f"\n**{len(models_data)} model(s) defined by this module:**\n"
        for entry in models_data:
            tech_section += render_model_section(
                entry["model"],
                entry["fields"],
                entry["accesses"],
                entry["rules"],
            )
    else:
        tech_section += "\n_No models defined by this module._\n"

    return fm + header + dep_section + desc_section + ui_section + tech_section


# ─────────────────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────────────────


def run():
    out_dir = Path(CONFIG["output_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)

    modules = fetch_installed_modules()

    index_lines = [
        "# 🗂️ Odoo Installed Modules Index\n",
        f"_{len(modules)} installed modules_\n",
        "",
        "| Module | Name | Category | Version |",
        "|--------|------|----------|---------|",
    ]

    print("\n🔬 Building technical docs & writing notes …\n")

    for i, mod in enumerate(modules, 1):
        name = mod["name"]
        print(f"  [{i:>3}/{len(modules)}] {name} …", end=" ", flush=True)

        # 1. Dependency names
        dep_ids = mod.get("dependencies_id") or []
        try:
            dep_names = fetch_dep_names(dep_ids)
        except Exception:
            dep_names = []

        # 2. Models defined by this module
        models_data = []
        try:
            models = fetch_models_for_module(name)
            for model in models:
                field_ids = model.get("field_id") or []
                access_ids = model.get("access_ids") or []
                rule_ids = model.get("rule_ids") or []

                fields = fetch_fields_for_model(field_ids)
                accesses = fetch_access_for_model(access_ids)
                rules = fetch_rules_for_model(rule_ids)

                models_data.append(
                    {
                        "model": model,
                        "fields": fields,
                        "accesses": accesses,
                        "rules": rules,
                    }
                )
        except Exception as e:
            print(f"⚠️  models error: {e}", end=" ")

        # 3. Build & save note
        content = build_note(mod, dep_names, models_data)
        filename = slugify(name) + ".md"
        (out_dir / filename).write_text(content, encoding="utf-8")

        model_count = len(models_data)
        print(f"✅ ({model_count} models, {len(dep_names)} deps)")

        # Index row
        cat = cat_name(mod.get("category_id"))
        ver = mod.get("installed_version") or "N/A"
        disp = mod.get("shortdesc") or name
        index_lines.append(f"| [[{name}]] | {disp} | {cat} | {ver} |")

        time.sleep(0.1)  # be polite

    # Write index
    index_path = out_dir / "_INDEX.md"
    index_path.write_text("\n".join(index_lines), encoding="utf-8")

    print(f"\n✅ Done! {len(modules)} notes → {out_dir.resolve()}")
    print(f"   📋 Index → {index_path.resolve()}")
    print("   Drop the folder into your Obsidian vault!")


if __name__ == "__main__":
    run()
