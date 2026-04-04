---
title: "OpenEduCat Parent Enterprise"
module: "openeducat_parent_enterprise"
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

# 🟢 OpenEduCat Parent Enterprise

> **Module:** `openeducat_parent_enterprise` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_core_enterprise]] [[openeducat_parent]]

## 📖 Description

## OpenEduCat Parent Enterprise

### Manage Parent Login

[![](/openeducat_parent_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module allows you to manage parent login. You can have parent details of students.

[Contact Us](https://www.openeducat.org/contactus/)

## Parent

Parent can see his child's activity & other details.

![](/openeducat_parent_enterprise/static/description/parent.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT Link to frontend portal (qweb)`
- `* INHERIT Portal layout : Child Info (qweb)`
- `* INHERIT op.parent.view.form.inherit (form)`
- `* INHERIT op.parent.view.tree.inherit (list)`
- `* INHERIT student_portal_library (qweb)`
- `Portal My Parent : Core Details (qweb)`
- `op.parent.form (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

### 🗃️ `op.parent` — Parent

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
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company            |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                        |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users              |
| `display_name`                  | Display Name                  | `char`      |     |       |                        |
| `email`                         | Email                         | `char`      |     | ✅    |                        |
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
| `mobile`                        | Mobile                        | `char`      |     | ✅    |                        |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                        |
| `name`                          | Name                          | `many2one`  | ✅  | ✅    | res.partner            |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating          |
| `relationship_id`               | Relation with Student         | `many2one`  | ✅  | ✅    | op.parent.relationship |
| `student_ids`                   | Student(s)                    | `many2many` | ✅  | ✅    | op.student             |
| `tag_ids`                       | Tags                          | `many2many` |     | ✅    | res.partner.category   |
| `user_id`                       | User                          | `many2one`  |     | ✅    | res.users              |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message           |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                        |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                           | Group            | Perms     |
| ------------------------------ | ---------------- | --------- |
| name_op_parent_op_parent_admin | Parent / Manager | `R/W/C/D` |
| name_op_parent_op_parent       | Role / Portal    | `R`       |

**Record Rules:**

- **Parent Login rule** (10) `R/W/C/D`
  - Domain: `['|', ('user_id','=',user.id), ('user_id','in',user.child_ids.ids)]`
- **Backoffice Login rule** (109) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Parent multi-company** (Global) `R/W/C/D`
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
