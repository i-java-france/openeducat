---
title: "OpenEduCat Classroom Enterprise"
module: "openeducat_classroom_enterprise"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Education"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________, odoo/app]
---

# 🟢 OpenEduCat Classroom Enterprise

> **Module:** `openeducat_classroom_enterprise` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_classroom]] [[openeducat_core_enterprise]] [[openeducat_onboarding]]
[[sale_management]]

## 📖 Description

## OpenEduCat Classroom Enterprise

### Manage Classrooms & it's Assets

[![](/openeducat_classroom_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module allows you to manage classroom details.

[Contact Us](https://www.openeducat.org/contactus/)

## Classroom

Manage classrooms for exams and resource allocation. You can manage facility and asset
details for the classroom.

![](/openeducat_classroom_enterprise/static/description/classroom.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT op.classroom.inherited.form.view (form)`
- `* INHERIT op.classroom.inherited.search.view (search)`
- `* INHERIT op.classroom.inherited.tree.view (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**2 model(s) defined by this module:**

### 🗃️ `op.classroom` — Classroom

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation         |
| -------------- | --------------- | ---------- | --- | ----- | ---------------- |
| `active`       | Active          | `boolean`  |     | ✅    |                  |
| `asset_line`   | Asset           | `one2many` |     | ✅    | op.asset         |
| `batch_id`     | Batch           | `many2one` |     | ✅    | op.batch         |
| `capacity`     | No of Seats     | `integer`  | ✅  | ✅    |                  |
| `code`         | Code            | `char`     | ✅  | ✅    |                  |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company      |
| `course_id`    | Course          | `many2one` |     | ✅    | op.course        |
| `create_date`  | Created on      | `datetime` |     | ✅    |                  |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users        |
| `display_name` | Display Name    | `char`     |     |       |                  |
| `facilities`   | Facility Lines  | `one2many` |     | ✅    | op.facility.line |
| `id`           | ID              | `integer`  |     | ✅    |                  |
| `name`         | Name            | `char`     | ✅  | ✅    |                  |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                  |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users        |

**Access Rights:**

| Name                                | Group               | Perms     |
| ----------------------------------- | ------------------- | --------- |
| name_op_classroom_back_office_admin | Classroom / Manager | `R/W/C/D` |
| name_op_classroom_faculty           | Classroom / User    | `R/W`     |

**Record Rules:**

- **Classroom multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.asset` — Classroom Assets

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label           | Type       | Req | Store | Relation        |
| ----------------- | --------------- | ---------- | --- | ----- | --------------- |
| `asset_id`        | Asset           | `many2one` |     | ✅    | op.classroom    |
| `code`            | Code            | `char`     |     | ✅    |                 |
| `company_id`      | Company         | `many2one` |     | ✅    | res.company     |
| `create_date`     | Created on      | `datetime` |     | ✅    |                 |
| `create_uid`      | Created by      | `many2one` |     | ✅    | res.users       |
| `display_name`    | Display Name    | `char`     |     |       |                 |
| `id`              | ID              | `integer`  |     | ✅    |                 |
| `product_id`      | Product         | `many2one` | ✅  | ✅    | product.product |
| `product_uom_qty` | Quantity        | `float`    | ✅  | ✅    |                 |
| `write_date`      | Last Updated on | `datetime` |     | ✅    |                 |
| `write_uid`       | Last Updated by | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                            | Group               | Perms     |
| ------------------------------- | ------------------- | --------- |
| name_op_asset_back_office_admin | Classroom / Manager | `R/W/C/D` |
| name_op_asset_faculty           | Classroom / User    | `R`       |

**Record Rules:**

- **Asset multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`
