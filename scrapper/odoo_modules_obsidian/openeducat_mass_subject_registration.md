---
title: "OpenEduCat Mass Subject Registration"
module: "openeducat_mass_subject_registration"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Education"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 OpenEduCat Mass Subject Registration

> **Module:** `openeducat_mass_subject_registration` | **Version:** `19.0.1.0`
> **Category:** Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc
> **Website:** https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_core_enterprise]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `wizard.op.student.subject.registration.form (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

### 🗃️ `wizard.op.student.subject.registration` — Create Subject Registration

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation   |
| -------------- | --------------- | ----------- | --- | ----- | ---------- |
| `batch_id`     | Batch           | `many2one`  |     | ✅    | op.batch   |
| `course_id`    | Course          | `many2one`  |     | ✅    | op.course  |
| `create_date`  | Created on      | `datetime`  |     | ✅    |            |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users  |
| `display_name` | Display Name    | `char`      |     |       |            |
| `id`           | ID              | `integer`   |     | ✅    |            |
| `student_ids`  | Students        | `many2many` |     | ✅    | op.student |
| `subjects_ids` | Subjects        | `many2many` |     | ✅    | op.subject |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |            |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users  |

**Access Rights:**

| Name                                          | Group       | Perms   |
| --------------------------------------------- | ----------- | ------- |
| access_wizard_op_student_subject_registration | Role / User | `R/W/C` |
