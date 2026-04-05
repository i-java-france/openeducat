# 🐍 OpenEduCat Onboarding — Python Skeleton

**Module:** `openeducat_onboarding`
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
openeducat_onboarding/
├── __manifest__.py     ← reconstructed from module metadata
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── oe_onboarding_plan.py
│   ├── oe_onboarding_steps.py
└── controllers/
    └── __init__.py     ← placeholder only
```

## Models (2)

| Model | Class | Fields |
|-------|-------|--------|
| `oe.onboarding.plan` | `OeOnboardingPlan` | see file |
| `oe.onboarding.steps` | `OeOnboardingSteps` | see file |
