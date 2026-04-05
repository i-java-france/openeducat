---
title: "OpenEduCat Campus Enterprise"
module: "openeducat_campus_enterprise"
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

# 🟢 OpenEduCat Campus Enterprise

> **Module:** `openeducat_campus_enterprise` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[account]] [[openeducat_core_enterprise]]

## 📖 Description

## OpenEduCat Campus Enterprise

### Manage Campus

[![](/openeducat_campus_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module allows you to manage campus. You can define the facility capacity.

[Contact Us](https://www.openeducat.org/contactus/)

## Campus Facility

Create facilities of the campus and child facility as sub facilit. Set capacity of
capacity.

![](/openeducat_campus_enterprise/static/description/campus.png)

## Campus Facility Allocation

![](/openeducat_campus_enterprise/static/description/campus_allocation.png)

You can allocate that facility for period of date range and can create invoice for that
also.

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Campus`
- `Campus/Configuration`
- `Campus/Configuration/Facility Type`
- `Campus/Configuration/Settings`
- `Campus/Facilities`
- `Campus/Facilities/Facility`
- `Campus/Facilities/Facility Allocations`

### Views

- `Facility Allocations (calendar)`
- `Facility Invoice Form (form)`
- `op.campus.facility.form (form)`
- `op.campus.facility.form (form)`
- `op.campus.facility.graph (graph)`
- `op.campus.facility.list (list)`
- `op.campus.facility.pivot (pivot)`
- `op.campus.facility.search (search)`
- `op.facility.allocation.form (form)`
- `op.facility.allocation.list (list)`
- `op.facility.allocation.pivot (pivot)`
- `op.facility.allocation.search (search)`
- `op.facility.type.form (form)`
- `op.facility.type.form (form)`
- `op.facility.type.list (list)`
- `op.facility.type.search (search)`

### Reports

_none_

## 🛠️ Technical Documentation

**6 model(s) defined by this module:**

### 🗃️ `op.campus.facility` — Campus Facility

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation               |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ---------------------- |
| `active`                        | Active                        | `boolean`   |     | ✅    |                        |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event         |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                        |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                        |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                        |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity          |
| `activity_state`                | Activity State                | `selection` |     |       |                        |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                        |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                        |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type     |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users              |
| `capacity`                      | Capacity                      | `integer`   |     | ✅    |                        |
| `child_ids`                     | Child Facility                | `one2many`  |     | ✅    | op.campus.facility     |
| `code`                          | Code                          | `char`      | ✅  | ✅    |                        |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company            |
| `complete_name`                 | Complete Name                 | `char`      |     | ✅    |                        |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                        |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users              |
| `display_name`                  | Display Name                  | `char`      |     |       |                        |
| `facility_allocation_lines`     | Allocations                   | `one2many`  |     | ✅    | op.facility.allocation |
| `facility_type_id`              | Facility Type                 | `many2one`  | ✅  | ✅    | op.facility.type       |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                        |
| `id`                            | ID                            | `integer`   |     | ✅    |                        |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                        |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers         |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                        |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                        |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                        |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message           |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                        |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                        |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                        |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner            |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                        |
| `name`                          | Name                          | `char`      | ✅  | ✅    |                        |
| `parent_id`                     | Parent Facility               | `many2one`  |     | ✅    | op.campus.facility     |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating          |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message           |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                        |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                                           | Group            | Perms     |
| ---------------------------------------------- | ---------------- | --------- |
| name_op_campus_facility_back_office_admin      | Campus / Manager | `R/W/C/D` |
| name_op_campus_facility_back_office_admin_user | Campus / User    | `R/W/C`   |

**Record Rules:**

- **Campus Facility multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.facility.allocation` — Facility Allocation

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation           |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ------------------ |
| `active`                     | Active                 | `boolean`   |     | ✅    |                    |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company        |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                    |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users          |
| `display_name`               | Display Name           | `char`      |     |       |                    |
| `facility_id`                | Facility               | `many2one`  | ✅  | ✅    | op.campus.facility |
| `from_date`                  | From Date              | `datetime`  |     | ✅    |                    |
| `has_message`                | Has Message            | `boolean`   |     |       |                    |
| `id`                         | ID                     | `integer`   |     | ✅    |                    |
| `invoice_id`                 | Invoice                | `many2one`  |     | ✅    | account.move       |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                    |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                    |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                    |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                    |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                    |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                    |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                    |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner        |
| `partner_id`                 | Person                 | `many2one`  | ✅  | ✅    | res.partner        |
| `product_id`                 | Product                | `many2one`  |     | ✅    | product.product    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating      |
| `to_date`                    | To Date                | `datetime`  |     | ✅    |                    |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message       |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                    |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                               | Group            | Perms     |
| -------------------------------------------------- | ---------------- | --------- |
| name_op_facility_allocation_back_office_admin      | Campus / Manager | `R/W/C/D` |
| name_op_facility_allocation_back_office_admin_user | Campus / User    | `R/W/C`   |

**Record Rules:**

- **Facility Allocation multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `facility.invoice` — facility Invoice

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation        |
| -------------- | --------------- | ---------- | --- | ----- | --------------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |                 |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users       |
| `display_name` | Display Name    | `char`     |     |       |                 |
| `from_date`    | From Date       | `date`     | ✅  | ✅    |                 |
| `id`           | ID              | `integer`  |     | ✅    |                 |
| `partner_id`   | Customer        | `many2one` | ✅  | ✅    | res.partner     |
| `product_id`   | Product         | `many2one` | ✅  | ✅    | product.product |
| `to_date`      | To Date         | `date`     | ✅  | ✅    |                 |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                 |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                       | Group            | Perms     |
| -------------------------- | ---------------- | --------- |
| name_facility_invoice      | Campus / Manager | `R/W/C/D` |
| name_facility_invoice_user | Campus / User    | `R`       |

### 🗃️ `op.facility.type` — Facility Type

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

| Name                                         | Group            | Perms     |
| -------------------------------------------- | ---------------- | --------- |
| name_op_facility_type_back_office_admin      | Campus / Manager | `R/W/C/D` |
| name_op_facility_type_back_office_admin_user | Campus / User    | `R`       |

**Record Rules:**

- **Facility Type multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `onboarding.onboarding` — Onboarding

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label                       | Type        | Req | Store | Relation                   |
| -------------------------- | --------------------------- | ----------- | --- | ----- | -------------------------- |
| `create_date`              | Created on                  | `datetime`  |     | ✅    |                            |
| `create_uid`               | Created by                  | `many2one`  |     | ✅    | res.users                  |
| `current_onboarding_state` | Completion State            | `selection` |     |       |                            |
| `current_progress_id`      | Onboarding Progress         | `many2one`  |     |       | onboarding.progress        |
| `display_name`             | Display Name                | `char`      |     |       |                            |
| `id`                       | ID                          | `integer`   |     | ✅    |                            |
| `is_onboarding_closed`     | Was panel closed?           | `boolean`   |     |       |                            |
| `is_per_company`           | Should be done per company? | `boolean`   |     |       |                            |
| `name`                     | Name of the onboarding      | `char`      |     | ✅    |                            |
| `panel_close_action_name`  | Closing action              | `char`      |     | ✅    |                            |
| `progress_ids`             | Onboarding Progress Records | `one2many`  |     | ✅    | onboarding.progress        |
| `route_name`               | One word name               | `char`      | ✅  | ✅    |                            |
| `sequence`                 | Sequence                    | `integer`   |     | ✅    |                            |
| `step_ids`                 | Onboarding steps            | `many2many` |     | ✅    | onboarding.onboarding.step |
| `text_completed`           | Message at completion       | `char`      |     | ✅    |                            |
| `write_date`               | Last Updated on             | `datetime`  |     | ✅    |                            |
| `write_uid`                | Last Updated by             | `many2one`  |     | ✅    | res.users                  |

**Access Rights:**

| Name                          | Group                | Perms     |
| ----------------------------- | -------------------- | --------- |
| onboarding.onboarding.manager | Role / Administrator | `R/W/C/D` |
| onboarding.onboarding.user    | Role / User          | `-`       |
| onboarding.onboarding.all     | Everyone             | `-`       |

### 🗃️ `onboarding.onboarding.step` — Onboarding Step

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                               | Type        | Req | Store | Relation                 |
| ----------------------------- | ----------------------------------- | ----------- | --- | ----- | ------------------------ |
| `button_text`                 | Button text                         | `char`      | ✅  | ✅    |                          |
| `create_date`                 | Created on                          | `datetime`  |     | ✅    |                          |
| `create_uid`                  | Created by                          | `many2one`  |     | ✅    | res.users                |
| `current_progress_step_id`    | Step Progress                       | `many2one`  |     |       | onboarding.progress.step |
| `current_step_state`          | Completion State                    | `selection` |     |       |                          |
| `description`                 | Description                         | `char`      |     | ✅    |                          |
| `display_name`                | Display Name                        | `char`      |     |       |                          |
| `done_icon`                   | Font Awesome Icon when completed    | `char`      |     | ✅    |                          |
| `done_text`                   | Text to show when step is completed | `char`      |     | ✅    |                          |
| `id`                          | ID                                  | `integer`   |     | ✅    |                          |
| `is_per_company`              | Is per company                      | `boolean`   |     | ✅    |                          |
| `onboarding_ids`              | Onboardings                         | `many2many` |     | ✅    | onboarding.onboarding    |
| `panel_step_open_action_name` | Opening action                      | `char`      |     | ✅    |                          |
| `progress_ids`                | Onboarding Progress Step Records    | `one2many`  |     | ✅    | onboarding.progress.step |
| `sequence`                    | Sequence                            | `integer`   |     | ✅    |                          |
| `step_image`                  | Step Image                          | `binary`    |     | ✅    |                          |
| `step_image_alt`              | Alt Text for the Step Image         | `char`      |     | ✅    |                          |
| `step_image_filename`         | Step Image Filename                 | `char`      |     | ✅    |                          |
| `title`                       | Title                               | `char`      |     | ✅    |                          |
| `write_date`                  | Last Updated on                     | `datetime`  |     | ✅    |                          |
| `write_uid`                   | Last Updated by                     | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                               | Group                | Perms     |
| ---------------------------------- | -------------------- | --------- |
| onboarding.onboarding.step.manager | Role / Administrator | `R/W/C/D` |
| onboarding.onboarding.step.user    | Role / User          | `-`       |
| onboarding.onboarding.step.all     | Everyone             | `-`       |
