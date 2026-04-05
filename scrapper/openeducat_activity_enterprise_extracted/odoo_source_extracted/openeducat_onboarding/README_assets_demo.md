# 🎨 openeducat_onboarding — Assets & Demo Data

## Summary

| Type | Count |
|------|-------|
| CSS/JS assets | 0 |
| Demo data records | 0 |

## Folder Structure

```
openeducat_onboarding/
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
