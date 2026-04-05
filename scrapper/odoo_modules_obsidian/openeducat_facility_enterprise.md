---
title: "OpenEduCat Facility Enterprise"
module: "openeducat_facility_enterprise"
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

# 🟢 OpenEduCat Facility Enterprise

> **Module:** `openeducat_facility_enterprise` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_facility]] [[openeducat_core_enterprise]] [[openeducat_onboarding]]

## 📖 Description

## OpenEduCat Facility Enterprise

### Facility Management

[![](/openeducat_facility_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module adds the feature to manage facilities to OpenEduCat.

[Contact Us](https://www.openeducat.org/contactus/)

## Facilities

You can define facilities like TV, AC and allocate to classrooms and hostel rooms.

![](/openeducat_facility_enterprise/static/description/facility.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT op.facility.inherited.form (form)`
- `* INHERIT op.facility.inherited.list (list)`
- `* INHERIT op.facility.line.inherited.form (form)`
- `* INHERIT op.facility.line.inherited.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**2 model(s) defined by this module:**

### 🗃️ `op.facility` — Manage Facility

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `active`       | Active          | `boolean`  |     | ✅    |             |
| `code`         | Code            | `char`     | ✅  | ✅    |             |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Name            | `char`     | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                     | Group              | Perms     |
| ------------------------ | ------------------ | --------- |
| name_op_facility_manager | Facility / Manager | `R/W/C/D` |
| name_op_facility_user    | Facility / User    | `R`       |

**Record Rules:**

- **Facility multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.facility.line` — Manage Facility Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation     |
| -------------- | --------------- | ---------- | --- | ----- | ------------ |
| `classroom_id` | Classroom       | `many2one` |     | ✅    | op.classroom |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company  |
| `create_date`  | Created on      | `datetime` |     | ✅    |              |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users    |
| `display_name` | Display Name    | `char`     |     |       |              |
| `facility_id`  | Facility        | `many2one` | ✅  | ✅    | op.facility  |
| `id`           | ID              | `integer`  |     | ✅    |              |
| `quantity`     | Quantity        | `float`    | ✅  | ✅    |              |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |              |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users    |

**Access Rights:**

| Name                          | Group              | Perms     |
| ----------------------------- | ------------------ | --------- |
| name_op_facility_line_manager | Facility / Manager | `R/W/C/D` |
| name_op_facility_line_user    | Facility / User    | `R`       |

**Record Rules:**

- **Facility Line multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`
