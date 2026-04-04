---
title: "OpenEduCat Scholarship Enterprise"
module: "openeducat_scholarship_enterprise"
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

# 🟢 OpenEduCat Scholarship Enterprise

> **Module:** `openeducat_scholarship_enterprise` | **Version:** `19.0.1.0`
> **Category:** Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc
> **Website:** https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_core_enterprise]] [[account]]

## 📖 Description

## OpenEduCat Scholarship Enterprise

### Manage Scholarships

[![](/openeducat_scholarship_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module allows you to have details for scholarship of students.

[Contact Us](https://www.openeducat.org/contactus/)

## Scholarship

You can keep record of scholarships of the student and set for approved or rejected.

![](/openeducat_scholarship_enterprise/static/description/scholarship.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `SIS/Configuration/General Management/Scholarship Stages`
- `SIS/Configuration/General Management/Scholarship Types`
- `SIS/General/Scholarship`
- `SIS/General/Scholarship/Scholarships`

### Views

- `Scholarship form view (form)`
- `op.scholarship.form (form)`
- `op.scholarship.kanban (kanban)`
- `op.scholarship.list (list)`
- `op.scholarship.search (search)`
- `op.scholarship.type.form (form)`
- `op.scholarship.type.list (list)`
- `op.scholarship.type.search (search)`
- `scholarship list view (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

### 🗃️ `op.scholarship` — Scholarship

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation            |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ------------------- |
| `active`                     | Active                 | `boolean`   |     | ✅    |                     |
| `amount`                     | Amount                 | `integer`   |     | ✅    |                     |
| `batch_id`                   | Batch                  | `many2one`  |     | ✅    | op.batch            |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company         |
| `course_id`                  | Course                 | `many2one`  |     | ✅    | op.course           |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                     |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users           |
| `display_name`               | Display Name           | `char`      |     |       |                     |
| `has_message`                | Has Message            | `boolean`   |     |       |                     |
| `id`                         | ID                     | `integer`   |     | ✅    |                     |
| `invoice_id`                 | Invoice                | `many2one`  |     | ✅    | account.move        |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                     |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers      |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                     |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                     |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                     |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message        |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                     |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                     |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                     |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner         |
| `name`                       | Name                   | `char`      | ✅  | ✅    |                     |
| `product_id`                 | Product                | `many2one`  |     | ✅    | product.product     |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating       |
| `scholarship_stages_id`      | Scholarship Stages     | `many2one`  |     | ✅    | scholarship.stages  |
| `sponsor_id`                 | Sponsor                | `many2one`  |     | ✅    | res.partner         |
| `student_courses`            | Student Courses        | `many2many` |     | ✅    | op.course           |
| `student_id`                 | Student                | `many2one`  | ✅  | ✅    | op.student          |
| `type_id`                    | Type                   | `many2one`  | ✅  | ✅    | op.scholarship.type |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message        |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                     |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                                  | Group                 | Perms     |
| ------------------------------------- | --------------------- | --------- |
| name_op_scholarship_back_office_admin | Scholarship / Manager | `R/W/C/D` |
| access_op_scholarship_student_user    | Scholarship / User    | `R/W`     |

**Record Rules:**

- **Scholarship multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `scholarship.stages` — Scholarship Stages

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `company_id`   | Company         | `many2one` | ✅  | ✅    | res.company |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Name            | `char`     | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                           | Group                 | Perms     |
| ------------------------------ | --------------------- | --------- |
| access_scholarship_stages      | Scholarship / Manager | `R/W/C/D` |
| access_scholarship_stages_user | Scholarship / User    | `R/W`     |

**Record Rules:**

- **Scholarship Type multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.scholarship.type` — Scholarship Type

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
| `amount`       | Amount          | `integer`  |     | ✅    |             |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Name            | `char`     | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                                       | Group                 | Perms     |
| ------------------------------------------ | --------------------- | --------- |
| name_op_scholarship_type_back_office_admin | Scholarship / Manager | `R/W/C/D` |
| access_op_scholarship_user                 | Scholarship / User    | `R`       |

**Record Rules:**

- **Scholarship Type multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`
