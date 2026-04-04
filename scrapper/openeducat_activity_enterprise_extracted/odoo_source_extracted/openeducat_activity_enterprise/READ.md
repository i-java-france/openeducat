# 🐍 OpenEduCat Activity Enterprise — Python Skeleton

**Module:** `openeducat_activity_enterprise` **Generated from:** Odoo database metadata
(ir.model, ir.model.fields, ir.rule, ir.model.access)

## ⚠️ Important Notes

- This is a **reconstructed skeleton** — not the original source code
- Field definitions are accurate (name, type, required, relation, store)
- Mixin detection (mail.thread, activity.mixin) is based on field presence
- Computed field stubs are generated but logic is **not** recoverable from DB
- `_sql_constraints`, `@api.constrains`, `@api.onchange` must be added manually
- Controller routes (`/web`, `http.route`) are **not** in the DB — add manually

## Structure

```
openeducat_activity_enterprise/
├── __manifest__.py     ← reconstructed from module metadata
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── op_activity.py
│   ├── op_student_progression.py
│   ├── activity_progress_wizard.py
│   ├── op_activity_type.py
│   ├── migration_report.py
└── controllers/
    └── __init__.py     ← placeholder only
```

## Models (5)

| Model                      | Class                    | Fields   |
| -------------------------- | ------------------------ | -------- |
| `op.activity`              | `OpActivity`             | see file |
| `op.student.progression`   | `OpStudentProgression`   | see file |
| `activity.progress.wizard` | `ActivityProgressWizard` | see file |
| `op.activity.type`         | `OpActivityType`         | see file |
| `migration.report`         | `MigrationReport`        | see file |
