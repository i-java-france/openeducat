#!/usr/bin/env python3
"""
Quick script to discover the real Odoo database name.
Run this before the main scraper.
"""

import requests

BASE_URL = "https://abdelhadieddiraa46080.o19.oeducat.org"
session = requests.Session()

print("=" * 50)
print("  Odoo DB Name Finder")
print("=" * 50)

# Method 1: /web/database/list
print("\n[1] Trying /web/database/list ...")
try:
    r = session.post(
        f"{BASE_URL}/web/database/list",
        json={"jsonrpc": "2.0", "method": "call", "id": 1, "params": {}},
        timeout=10,
    )
    data = r.json()
    if "result" in data:
        print(f"    ✅ Found: {data['result']}")
    else:
        print(
            f"    ❌ {data.get('error', {}).get('data', {}).get('message', 'blocked')}"
        )
except Exception as e:
    print(f"    ❌ {e}")

# Method 2: /web/webclient/version_info (sometimes leaks db)
print("\n[2] Trying /web/webclient/version_info ...")
try:
    r = session.post(
        f"{BASE_URL}/web/webclient/version_info",
        json={"jsonrpc": "2.0", "method": "call", "id": 2, "params": {}},
        timeout=10,
    )
    print(f"    → {r.text[:300]}")
except Exception as e:
    print(f"    ❌ {e}")

# Method 3: Try common DB name patterns
print("\n[3] Brute-forcing common DB name patterns ...")
candidates = [
    "abdelhadieddiraa46080",
    "abdelhadieddiraa",
    "oeducat",
    "openeducat",
    "o19",
    "odoo",
    "prod",
    "main",
    "abdelhadieddiraa46080-main",
    "abdelhadieddiraa46080-prod",
    "edu",
]

for db in candidates:
    try:
        r = session.post(
            f"{BASE_URL}/web/session/authenticate",
            json={
                "jsonrpc": "2.0",
                "method": "call",
                "id": 3,
                "params": {"db": db, "login": "admin", "password": "admin"},
            },
            timeout=10,
        )
        data = r.json()
        if "error" not in data and data.get("result", {}).get("uid"):
            print(f"    ✅ SUCCESS! DB name is: '{db}' (uid={data['result']['uid']})")
            break
        else:
            msg = data.get("error", {}).get("data", {}).get("message", "failed")
            print(f"    ✗ '{db}' → {msg}")
    except Exception as e:
        print(f"    ✗ '{db}' → {e}")

print("\nDone.")
