---
title: "OpenEduCat Fees Parent Bridge"
module: "openeducat_fees_parent_bridge"
state: "installed"
version: "19.0.0.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Education"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 OpenEduCat Fees Parent Bridge

> **Module:** `openeducat_fees_parent_bridge` | **Version:** `19.0.0.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_fees_plan]] [[openeducat_parent_enterprise]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT op.fees.plan.inherit.form (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

### 🗃️ `op.fees.plan` — Fees Plan for Student Fees

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation          |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ----------------- |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company       |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                   |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users         |
| `display_name`               | Display Name           | `char`      |     |       |                   |
| `fees_plan_line_ids`         | Lines                  | `one2many`  |     | ✅    | op.fees.plan.line |
| `fees_term_id`               | Fees Terms             | `many2one`  |     | ✅    | op.fees.terms     |
| `has_message`                | Has Message            | `boolean`   |     |       |                   |
| `id`                         | ID                     | `integer`   |     | ✅    |                   |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                   |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers    |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                   |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                   |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                   |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message      |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                   |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                   |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                   |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner       |
| `name`                       | Fees Plan              | `char`      |     | ✅    |                   |
| `paid_amount`                | Paid Amount            | `float`     |     |       |                   |
| `product_id`                 | Course Fees            | `many2one`  | ✅  | ✅    | product.product   |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating     |
| `remaining_amount`           | Remaining Amount       | `float`     |     | ✅    |                   |
| `state`                      | Status                 | `selection` |     | ✅    |                   |
| `student_id`                 | Student                | `many2one`  |     | ✅    | op.student        |
| `total_amount`               | Total Amount           | `float`     |     | ✅    |                   |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message      |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                   |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                                     | Group                | Perms     |
| ---------------------------------------- | -------------------- | --------- |
| access_op_fees_plan_op_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_op_fees_plan_user                 | OpenEduCat / User    | `R`       |
| access_op_fees_plan_portal               | Role / Portal        | `R`       |

**Record Rules:**

- **Fees Plan multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `
