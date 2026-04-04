---
title: "OpenEduCat Onboarding"
module: "openeducat_onboarding"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Tool"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/____]
---

# 🟢 OpenEduCat Onboarding

> **Module:** `openeducat_onboarding` | **Version:** `19.0.1.0` **Category:** Tool |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[base]] [[openeducat_core]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `OnBoarding`

### Views

- `oe.onboarding.plan (list)`
- `oe.onboarding.steps (kanban)`

### Reports

_none_

## 🛠️ Technical Documentation

**2 model(s) defined by this module:**

### 🗃️ `oe.onboarding.plan` — Onboarding Plan

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation            |
| -------------- | --------------- | ---------- | --- | ----- | ------------------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |                     |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users           |
| `display_name` | Display Name    | `char`     |     |       |                     |
| `id`           | ID              | `integer`  |     | ✅    |                     |
| `name`         | Plan Name       | `char`     |     | ✅    |                     |
| `step_id`      | Steps           | `one2many` |     | ✅    | oe.onboarding.steps |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                     |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users           |

**Access Rights:**

| Name                 | Group                | Perms     |
| -------------------- | -------------------- | --------- |
| access_op_onboarding | OpenEduCat / Manager | `R/W/C/D` |

### 🗃️ `oe.onboarding.steps` — Onboarding Steps

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation              |
| -------------- | --------------- | ---------- | --- | ----- | --------------------- |
| `action_id`    | Action          | `many2one` |     | ✅    | ir.actions.act_window |
| `create_date`  | Created on      | `datetime` |     | ✅    |                       |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users             |
| `display_name` | Display Name    | `char`     |     |       |                       |
| `doc_link`     | Doc Link        | `text`     |     | ✅    |                       |
| `id`           | ID              | `integer`  |     | ✅    |                       |
| `image`        | Image           | `binary`   |     | ✅    |                       |
| `is_done`      | Done ?          | `boolean`  |     | ✅    |                       |
| `is_start`     | Is Start        | `boolean`  |     | ✅    |                       |
| `name`         | Sequence        | `char`     |     | ✅    |                       |
| `plan_id`      | Plan            | `many2one` |     | ✅    | oe.onboarding.plan    |
| `step_name`    | Steps Name      | `char`     |     | ✅    |                       |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                       |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users             |
| `youtube_link` | Youtube Link    | `text`     |     | ✅    |                       |

**Access Rights:**

| Name                       | Group                | Perms     |
| -------------------------- | -------------------- | --------- |
| access_op_onboarding_steps | OpenEduCat / Manager | `R/W/C/D` |
