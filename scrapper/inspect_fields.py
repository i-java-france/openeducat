#!/usr/bin/env python3
"""
Inspect what fields & technical data are available
on ir.module.module in Odoo 19.
"""

import requests

CONFIG = {
    "url": "https://abdelhadieddiraa46080.o19.oeducat.org",
    "session_id": "eIjYQvr_ab6JXIUaRS3BT5x-VuJNDsy-c6hEXRX0-pD6a-0Vx3H-XQYFTqU2LXb382A_w8cBUd2dpgGw8CxY",
}

SESSION = requests.Session()
SESSION.headers.update({"Content-Type": "application/json"})
SESSION.cookies.set(
    "session_id", CONFIG["session_id"], domain="abdelhadieddiraa46080.o19.oeducat.org"
)


def rpc(endpoint, params):
    resp = SESSION.post(
        f"{CONFIG['url']}{endpoint}",
        json={"jsonrpc": "2.0", "method": "call", "id": 1, "params": params},
        timeout=30,
    )
    data = resp.json()
    if "error" in data:
        raise RuntimeError(data["error"]["data"]["message"])
    return data["result"]


# ── 1. Get ALL available fields on ir.module.module ──────────────────────────
print("\n" + "=" * 60)
print("  ALL FIELDS on ir.module.module")
print("=" * 60)

fields_meta = rpc(
    "/web/dataset/call_kw",
    {
        "model": "ir.module.module",
        "method": "fields_get",
        "args": [],
        "kwargs": {"attributes": ["string", "type", "help"]},
    },
)

for fname, finfo in sorted(fields_meta.items()):
    print(f"  {fname:<40} [{finfo['type']:<12}] {finfo.get('string', '')}")


# ── 2. Fetch one installed module to see actual data ─────────────────────────
print("\n" + "=" * 60)
print("  SAMPLE: first installed module (all fields)")
print("=" * 60)

sample = rpc(
    "/web/dataset/call_kw",
    {
        "model": "ir.module.module",
        "method": "search_read",
        "args": [[["state", "=", "installed"]]],
        "kwargs": {
            "fields": list(fields_meta.keys()),
            "limit": 1,
        },
    },
)

if sample:
    for k, v in sample[0].items():
        # truncate long values
        display = str(v)[:120] + "..." if len(str(v)) > 120 else str(v)
        print(f"  {k:<40} = {display}")


# ── 3. Check ir.model (models defined by modules) ────────────────────────────
print("\n" + "=" * 60)
print("  ir.model fields available")
print("=" * 60)

model_fields = rpc(
    "/web/dataset/call_kw",
    {
        "model": "ir.model",
        "method": "fields_get",
        "args": [],
        "kwargs": {"attributes": ["string", "type"]},
    },
)

for fname, finfo in sorted(model_fields.items()):
    print(f"  {fname:<40} [{finfo['type']:<12}] {finfo.get('string', '')}")


# ── 4. Sample one model record ────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  SAMPLE: ir.model record (one module's models)")
print("=" * 60)

model_sample = rpc(
    "/web/dataset/call_kw",
    {
        "model": "ir.model",
        "method": "search_read",
        "args": [[["modules", "ilike", "openeducat"]]],
        "kwargs": {
            "fields": ["name", "model", "info", "modules", "field_id"],
            "limit": 3,
        },
    },
)

for m in model_sample:
    print(f"\n  Model: {m.get('model')} ({m.get('name')})")
    print(f"  Modules: {m.get('modules')}")
    print(f"  Info: {str(m.get('info', ''))[:200]}")
    print(f"  Fields count: {len(m.get('field_id', []))}")
