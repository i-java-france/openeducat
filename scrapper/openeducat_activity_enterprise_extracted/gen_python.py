#!/usr/bin/env python3
"""
Odoo Python Skeleton Generator
================================
Reconstructs approximate Python source code from database metadata.

For each installed module it generates:
  models/
    ├── __init__.py
    └── <model_name>.py   ← full Model class with all fields, _sql_constraints,
                             _rec_name, _order, _inherit, mail mixins, etc.
  controllers/
    └── __init__.py       ← placeholder (controllers not stored in DB)
  __init__.py
  __manifest__.py         ← reconstructed from ir.module.module data

Usage:
    pip install requests
    python gen_python.py openeducat_activity_enterprise
    python gen_python.py                                   # all modules
"""

import base64
import sys
import time
from pathlib import Path

import requests

# ─────────────────────────────────────────────────────────
#  CONFIG  — update session_id when it expires
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


def save(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


# ─────────────────────────────────────────────────────────
#  FIELD TYPE → Odoo fields.X mapping
# ─────────────────────────────────────────────────────────

FIELD_MAP = {
    "char": "fields.Char",
    "text": "fields.Text",
    "html": "fields.Html",
    "integer": "fields.Integer",
    "float": "fields.Float",
    "monetary": "fields.Monetary",
    "boolean": "fields.Boolean",
    "date": "fields.Date",
    "datetime": "fields.Datetime",
    "binary": "fields.Binary",
    "selection": "fields.Selection",
    "many2one": "fields.Many2one",
    "one2many": "fields.One2many",
    "many2many": "fields.Many2many",
    "reference": "fields.Reference",
    "image": "fields.Image",
    "serialized": "fields.Json",
    "json": "fields.Json",
    "properties": "fields.Properties",
}

# Fields inherited from mixins — skip rendering these to keep skeleton clean
MIXIN_FIELDS = {
    "message_follower_ids",
    "message_ids",
    "message_partner_ids",
    "message_is_follower",
    "message_needaction",
    "message_needaction_counter",
    "message_has_error",
    "message_has_error_counter",
    "message_has_sms_error",
    "message_attachment_count",
    "has_message",
    "activity_ids",
    "activity_state",
    "activity_date_deadline",
    "my_activity_date_deadline",
    "activity_type_id",
    "activity_type_icon",
    "activity_user_id",
    "activity_summary",
    "activity_exception_decoration",
    "activity_exception_icon",
    "activity_calendar_event_id",
    "rating_ids",
    "rating_count",
    "rating_avg",
    "rating_last_value",
    "website_message_ids",
    "create_uid",
    "create_date",
    "write_uid",
    "write_date",
    "id",
    "display_name",
}


def model_name_to_class(model_name: str) -> str:
    """op.student.progression → OpStudentProgression"""
    return "".join(
        part.capitalize() for part in model_name.replace(".", "_").split("_")
    )


def field_to_python(f: dict) -> str:
    """Generate a single field definition line."""
    fname = f["name"]
    if fname in MIXIN_FIELDS:
        return None  # skip mixin-inherited fields

    ftype = f.get("ttype", "char")
    fclass = FIELD_MAP.get(ftype, "fields.Char")
    label = f.get("field_description", "")
    req = f.get("required", False)
    store = f.get("store", True)
    rel = f.get("relation", "")
    fhelp = f.get("help", "")

    args = []

    # Relation arg
    if ftype == "many2one" and rel:
        args.append(f"'{rel}'")
    elif ftype == "one2many" and rel:
        inv = f.get("relation_field", "FIXME_inverse_field")
        args.append(f"'{rel}', '{inv}'")
    elif ftype == "many2many" and rel:
        args.append(f"'{rel}'")

    # Named args
    if label:
        args.append(f"string='{label}'")
    if req:
        args.append("required=True")
    if not store and ftype not in ("one2many", "many2many"):
        args.append("store=False")
    if ftype == "selection":
        args.append("selection=[]")
    if fhelp:
        safe_help = fhelp.replace("'", "\\'").replace("\n", " ")[:120]
        args.append(f"help='{safe_help}'")

    arg_str = ", ".join(args)
    return f"    {fname} = {fclass}({arg_str})"


def detect_mixins(fields: list, is_mail_thread: bool) -> list:
    """Detect which mixins to inherit based on fields present."""
    mixins = []
    fnames = {f["name"] for f in fields}

    if is_mail_thread or "message_ids" in fnames:
        mixins.append("'mail.thread'")
    if "activity_ids" in fnames:
        mixins.append("'mail.activity.mixin'")
    if "rating_ids" in fnames:
        mixins.append("'rating.mixin'")
    if "website_message_ids" in fnames:
        mixins.append("'website.published.mixin'")

    return mixins


def generate_model_file(
    model_rec: dict, fields: list, accesses: list, rules: list
) -> str:
    """Generate a complete Python model file."""

    model_name = model_rec["model"]
    class_name = model_name_to_class(model_name)
    description = model_rec.get("name", "")
    transient = model_rec.get("transient", False)
    is_mail = model_rec.get("is_mail_thread", False)
    info = (model_rec.get("info") or "").strip()

    # Clean up boilerplate info text from Odoo
    if "Main super-class for regular database-persisted" in info:
        info = ""

    base_class = "models.TransientModel" if transient else "models.Model"
    mixins = detect_mixins(fields, is_mail)

    # Determine _inherit vs _name
    # If model has inherited models in the DB we'd know, but as a heuristic:
    # models that extend mail.thread use _inherit list
    if mixins:
        inherit_str = f"_inherit = ['{model_name}', {', '.join(mixins)}]"
        name_str = ""
    else:
        inherit_str = ""
        name_str = f"_name = '{model_name}'"

    # Build field lines
    field_lines = []
    skipped = []
    for f in sorted(fields, key=lambda x: x["name"]):
        line = field_to_python(f)
        if line is None:
            skipped.append(f["name"])
        else:
            field_lines.append(line)

    # Access rights as comment
    acl_comment = ""
    if accesses:
        acl_comment = "\n    # Access Rights:\n"
        for a in accesses:
            grp = (
                a["group_id"][1] if isinstance(a.get("group_id"), list) else "Everyone"
            )
            perms = []
            if a.get("perm_read"):
                perms.append("read")
            if a.get("perm_write"):
                perms.append("write")
            if a.get("perm_create"):
                perms.append("create")
            if a.get("perm_unlink"):
                perms.append("unlink")
            acl_comment += f"    #   {grp}: {', '.join(perms)}\n"

    # Record rules as comment
    rules_comment = ""
    if rules:
        rules_comment = "\n    # Record Rules:\n"
        for rule in rules:
            domain = (rule.get("domain_force") or "").strip()
            rules_comment += f"    #   {rule['name']}: {domain}\n"

    # Model docstring
    doc = f'"""{description}'
    if info:
        doc += f"\n\n    {info}"
    doc += '\n    """'

    # Compose file
    lines = [
        "# -*- coding: utf-8 -*-",
        "# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata",
        "# Real Python source lives on the server filesystem, not in the database.",
        "# This skeleton reflects field definitions, mixins, ACL and record rules.",
        "",
        "from odoo import models, fields, api",
        "from odoo.exceptions import ValidationError, UserError",
        "",
        "",
        f"class {class_name}({base_class}):",
        f"    {doc}",
        "",
    ]

    if name_str:
        lines.append(f"    {name_str}")
    if inherit_str:
        lines.append(f"    {inherit_str}")

    lines.append(f"    _description = '{description}'")
    lines.append("")

    if field_lines:
        lines.append("    # ── Fields ──────────────────────────────────────────────")
        lines.extend(field_lines)

    if skipped:
        lines.append("")
        lines.append(
            f"    # Mixin-inherited fields (not redeclared): {', '.join(skipped[:10])}"
            + (" ..." if len(skipped) > 10 else "")
        )

    if acl_comment:
        lines.append(acl_comment.rstrip())

    if rules_comment:
        lines.append(rules_comment.rstrip())

    lines += [
        "",
        "    # ── Computed / onchange methods (reconstructed stubs) ───────────",
    ]

    # Generate @api.depends stubs for computed fields
    computed = [
        f
        for f in fields
        if not f.get("store")
        and f.get("ttype") not in ("one2many", "many2many")
        and f["name"] not in MIXIN_FIELDS
    ]
    for cf in computed[:10]:  # limit to first 10
        lines += [
            "",
            "    @api.depends()  # TODO: add real dependencies",
            f"    def _compute_{cf['name']}(self):",
            "        for rec in self:",
            f"            rec.{cf['name']} = False  # TODO: implement",
        ]

    lines += [
        "",
        "    # ── CRUD overrides (if any) ──────────────────────────────────────",
        "",
        "    # def create(self, vals):",
        "    #     return super().create(vals)",
        "",
        "    # def write(self, vals):",
        "    #     return super().write(vals)",
        "",
        "    # ── Business logic ───────────────────────────────────────────────",
        "",
        "    # TODO: add action methods found in ir.actions.server for this model",
    ]

    return "\n".join(lines) + "\n"


def generate_manifest(mod: dict, dep_names: list) -> str:
    """Reconstruct __manifest__.py from module metadata."""
    name = mod.get("shortdesc") or mod.get("name")
    summary = mod.get("summary") or ""
    author = mod.get("author") or ""
    website = mod.get("website") or ""
    version = mod.get("installed_version") or ""
    license_ = mod.get("license") or "LGPL-3"
    category = ""
    if isinstance(mod.get("category_id"), list):
        category = mod["category_id"][1]

    deps_str = (
        ",\n        ".join(f"'{d}'" for d in dep_names) if dep_names else "'base'"
    )

    images_str = ""
    if mod.get("icon_image"):
        images_str = "    'images': ['static/description/icon.png'],\n"

    return f"""# -*- coding: utf-8 -*-
# AUTO-GENERATED — reconstructed from Odoo database metadata
{{
    'name': '{name}',
{images_str}    'version': '{version}',
    'summary': '{summary}',
    'description': \"\"\"
        {summary}
    \"\"\",
    'author': '{author}',
    'website': '{website}',
    'license': '{license_}',
    'category': '{category}',
    'depends': [
        {deps_str}
    ],
    'data': [
        # TODO: list XML files
        # 'security/ir.model.access.csv',
        # 'views/views_form.xml',
        # 'data/sequences.xml',
    ],
    'installable': True,
    'application': {mod.get("application", False)},
    'auto_install': {mod.get("auto_install", False)},
}}
"""


# ─────────────────────────────────────────────────────────
#  FETCH HELPERS
# ─────────────────────────────────────────────────────────


def fetch_module_info(module_name):
    mods = rpc(
        "ir.module.module",
        "search_read",
        args=[[["name", "=", module_name]]],
        kwargs={
            "fields": [
                "name",
                "shortdesc",
                "summary",
                "author",
                "website",
                "installed_version",
                "license",
                "category_id",
                "application",
                "auto_install",
                "dependencies_id",
                "icon_image",
            ],
            "limit": 1,
        },
    )
    return mods[0] if mods else {}


def fetch_dep_names(dep_ids):
    if not dep_ids:
        return []
    deps = rpc(
        "ir.module.module.dependency",
        "search_read",
        args=[[["id", "in", dep_ids]]],
        kwargs={"fields": ["name"], "limit": 0},
    )
    return [d["name"] for d in deps]


def fetch_models(module_name):
    imd = rpc(
        "ir.model.data",
        "search_read",
        args=[[["module", "=", module_name], ["model", "=", "ir.model"]]],
        kwargs={"fields": ["res_id", "name"], "limit": 0},
    )
    if not imd:
        return []
    model_ids = [r["res_id"] for r in imd]
    return rpc(
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


def fetch_fields(field_ids):
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
                "relation_field",
                "help",
            ],
            "order": "name asc",
            "limit": 0,
        },
    )


def fetch_accesses(access_ids):
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


def fetch_rules(rule_ids):
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


def get_installed_modules():
    mods = rpc(
        "ir.module.module",
        "search_read",
        args=[[["state", "=", "installed"]]],
        kwargs={"fields": ["name", "shortdesc"], "order": "name asc"},
    )
    return {m["name"]: m["shortdesc"] for m in mods}


# ─────────────────────────────────────────────────────────
#  MAIN GENERATOR
# ─────────────────────────────────────────────────────────


def generate_module(module_name, out_base):
    print("  📋 Module info …", end=" ", flush=True)
    mod = fetch_module_info(module_name)
    dep_ids = mod.get("dependencies_id") or []
    dep_names = fetch_dep_names(dep_ids)
    print(f"deps: {dep_names}")

    out_dir = out_base / module_name
    out_dir.mkdir(parents=True, exist_ok=True)

    # Icon
    icon_b64 = mod.get("icon_image")
    if icon_b64:
        icon_dir = out_dir / "static" / "description"
        icon_dir.mkdir(parents=True, exist_ok=True)
        try:
            icon_data = base64.b64decode(icon_b64)
            (icon_dir / "icon.png").write_bytes(icon_data)
        except Exception as e:
            print(f"     ⚠️  Failed to save icon: {e}")

    # __manifest__.py
    save(out_dir / "__manifest__.py", generate_manifest(mod, dep_names))

    # __init__.py (root)
    save(out_dir / "__init__.py", "# -*- coding: utf-8 -*-\nfrom . import models\n")

    # models/__init__.py — built after we know model files
    models_dir = out_dir / "models"
    models_dir.mkdir(exist_ok=True)

    print("  🗃️  Fetching models …", end=" ", flush=True)
    model_records = fetch_models(module_name)
    print(f"{len(model_records)} models")

    model_imports = []

    for mrec in model_records:
        model_name_str = mrec["model"]
        print(f"     → {model_name_str} …", end=" ", flush=True)

        fields = fetch_fields(mrec.get("field_id") or [])
        accesses = fetch_accesses(mrec.get("access_ids") or [])
        rules = fetch_rules(mrec.get("rule_ids") or [])

        content = generate_model_file(mrec, fields, accesses, rules)

        # filename: op.activity → op_activity.py
        fname = model_name_str.replace(".", "_") + ".py"
        save(models_dir / fname, content)

        import_name = model_name_str.replace(".", "_")
        model_imports.append(import_name)
        print(f"✅ ({len(fields)} fields)")
        time.sleep(0.05)

    # models/__init__.py
    imports = "\n".join(f"from . import {m}" for m in model_imports)
    save(models_dir / "__init__.py", f"# -*- coding: utf-8 -*-\n{imports}\n")

    # controllers/ placeholder
    ctrl_dir = out_dir / "controllers"
    ctrl_dir.mkdir(exist_ok=True)
    save(
        ctrl_dir / "__init__.py",
        "# -*- coding: utf-8 -*-\n"
        "# Controllers are not stored in the database.\n"
        "# Add your http.route controllers here.\n",
    )

    # README
    save(
        out_dir / "READ.md",
        f"""# 🐍 {mod.get("shortdesc", module_name)} — Python Skeleton

**Module:** `{module_name}`
**Generated from:** Odoo database metadata (ir.model, ir.model.fields, ir.rule, ir.model.access)

## ⚠️ Important Notes

- This is a **reconstructed skeleton** — not the original source code
- Field definitions are accurate (name, type, required, relation, store)
- Mixin detection (mail.thread, activity.mixin) is based on field presence
- Computed field stubs are generated but logic is **not** recoverable from DB
- `_sql_constraints`, `@api.constrains`, `@api.onchange` must be added manually
- Controller routes (`/web`, `http.route`) are **not** in the DB — add manually

## Structure

```
{module_name}/
├── __manifest__.py     ← reconstructed from module metadata
├── __init__.py
├── models/
│   ├── __init__.py
{"".join(f"│   ├── {m.replace('.', '_')}.py" + chr(10) for m in [r["model"] for r in model_records])}└── controllers/
    └── __init__.py     ← placeholder only
```

## Models ({len(model_records)})

| Model | Class | Fields |
|-------|-------|--------|
"""
        + "\n".join(
            f"| `{r['model']}` | `{model_name_to_class(r['model'])}` | see file |"
            for r in model_records
        )
        + "\n",
    )

    return len(model_records)


def run():
    target_modules = sys.argv[1:] if len(sys.argv) > 1 else None

    out_base = Path(CONFIG["output_dir"])
    out_base.mkdir(parents=True, exist_ok=True)

    print("🔍 Fetching installed modules …")
    all_modules = get_installed_modules()

    if target_modules:
        modules = {k: v for k, v in all_modules.items() if k in target_modules}
        missing = set(target_modules) - set(modules)
        if missing:
            print(f"⚠️  Not found / not installed: {missing}")
    else:
        modules = all_modules

    print(f"🐍 Generating Python skeletons for {len(modules)} module(s) …\n")

    for i, (name, display) in enumerate(modules.items(), 1):
        print(f"[{i:>3}/{len(modules)}] {name}")
        try:
            count = generate_module(name, out_base)
            print(f"     ✅ {count} model file(s) written\n")
        except Exception as e:
            print(f"     ❌ Failed: {e}\n")
        time.sleep(0.1)

    print(f"✅ Done! Output → {out_base.resolve()}")
    print("\n💡 Tip:")
    print("   python gen_python.py openeducat_activity_enterprise")


if __name__ == "__main__":
    run()
