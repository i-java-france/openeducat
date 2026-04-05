---
title: "OpenEduCat Activity Enterprise"
module: "openeducat_activity_enterprise"
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

# 🟢 OpenEduCat Activity Enterprise

> **Module:** `openeducat_activity_enterprise` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_activity]] [[openeducat_core_enterprise]]
[[openeducat_student_progress_enterprise]] [[openeducat_onboarding]]

## 📖 Description

## OpenEduCat Activity Enterprise

### Manage student activities

[![](/openeducat_activity_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module adds feature to maintain details of student's activity.

[Contact Us](https://www.openeducat.org/contactus/)

## Student Activity

Keep track of student's activities. Categorize activity by type, date & other details.

![](/openeducat_activity_enterprise/static/description/activity.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `SIS/Reporting/Migration Report`
- `Students/Reporting/Activity Analysis`

### Views

- `* INHERIT Enterprise_student_activity_portal (qweb)`
- `* INHERIT Student Progression Activity Form (form)`
- `* INHERIT Student Progression list (list)`
- `* INHERIT op.activity.form (form)`
- `* INHERIT op.activity.inherited.form.view (form)`
- `* INHERIT op.activity.inherited.tree.view (list)`
- `* INHERIT op.activity.list (list)`
- `* INHERIT student_activity_progression_report (qweb)`
- `* INHERIT student_progression_activity_portal_inherit (qweb)`
- `Activity Progress Wizard (form)`
- `migration.pivot (pivot)`

### Reports

_none_

## 🛠️ Technical Documentation

**5 model(s) defined by this module:**

### 🗃️ `op.activity` — Student Activity

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
| `date`                          | Date                          | `date`      |     | ✅    |                        |
| `description`                   | Description                   | `text`      |     | ✅    |                        |
| `display_name`                  | Display Name                  | `char`      |     |       |                        |
| `faculty_id`                    | Faculty                       | `many2one`  |     | ✅    | op.faculty             |
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
| `progression_id`                | Progression No                | `many2one`  |     | ✅    | op.student.progression |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating          |
| `student_id`                    | Student                       | `many2one`  | ✅  | ✅    | op.student             |
| `type_id`                       | Activity Type                 | `many2one`  |     | ✅    | op.activity.type       |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message           |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                        |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                        | Group                                   | Perms     |
| --------------------------- | --------------------------------------- | --------- |
| name_op_activity_student    | Openeducat Activity Privilege / Manager | `R/W/C/D` |
| name_op_activity_op_faculty | Openeducat Activity Privilege / User    | `R/W`     |

**Record Rules:**

- **Student Activity Logs** (102) `R/W/C/D`
  - Domain:
    `['|', ('student_id.user_id','=',user.id), ('student_id.user_id','in',user.child_ids.ids)]         `
- **Faculty Activity Logs** (101) `R/W/C/D`
  - Domain:
    `['|', ('faculty_id.user_id','=',user.id), ('faculty_id.user_id','in',user.child_ids.ids)]         `
- **Back Office Activity Logs** (102) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Activity multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.student.progression` — Student progression

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation               |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ---------------------- |
| `achievement_lines`          | Progression Achivement | `one2many`  |     | ✅    | op.achievement         |
| `active`                     | Active                 | `boolean`   |     | ✅    |                        |
| `activity_lines`             | Progression Activities | `one2many`  |     | ✅    | op.activity            |
| `assignment_lines`           | Progression Assignment | `one2many`  |     | ✅    | op.assignment.sub.line |
| `attendance_lines`           | Progression Attendance | `one2many`  |     | ✅    | op.attendance.line     |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company            |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                        |
| `created_by`                 | Created By             | `many2one`  |     | ✅    | res.users              |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users              |
| `date`                       | Date                   | `date`      | ✅  | ✅    |                        |
| `discipline_lines`           | Progression Discipline | `one2many`  |     | ✅    | op.discipline          |
| `display_name`               | Display Name           | `char`      |     |       |                        |
| `grade_book`                 | GradeBook              | `char`      |     | ✅    |                        |
| `has_message`                | Has Message            | `boolean`   |     |       |                        |
| `id`                         | ID                     | `integer`   |     | ✅    |                        |
| `marksheet_lines`            | Progression Marksheet  | `one2many`  |     | ✅    | op.marksheet.line      |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                        |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers         |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                        |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                        |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                        |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message           |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                        |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                        |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                        |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner            |
| `name`                       | Sequence               | `char`      | ✅  | ✅    |                        |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating          |
| `state`                      | Status                 | `selection` |     | ✅    |                        |
| `student_id`                 | Student                | `many2one`  | ✅  | ✅    | op.student             |
| `total_achievement`          | Total Achievement      | `integer`   |     | ✅    |                        |
| `total_activity`             | Total Activity         | `integer`   |     | ✅    |                        |
| `total_assignment`           | Total Assignment       | `integer`   |     | ✅    |                        |
| `total_attendance`           | Total Attendance       | `integer`   |     | ✅    |                        |
| `total_discipline`           | Total Discipline       | `integer`   |     | ✅    |                        |
| `total_marksheet_line`       | Total Marksheet        | `integer`   |     | ✅    |                        |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message           |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                        |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                          | Group                | Perms     |
| ----------------------------- | -------------------- | --------- |
| access_op_student_progression | OpenEduCat / Manager | `R/W/C/D` |
| access_op_student_progression | OpenEduCat / User    | `R/W/C`   |

**Record Rules:**

- **Student progression multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `activity.progress.wizard` — Activity Progress Wizard

> ✳️ Transient (Wizard)

Progression Activity

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation    |
| -------------- | --------------- | ----------- | --- | ----- | ----------- |
| `activity_ids` | Activity        | `many2many` |     | ✅    | op.activity |
| `create_date`  | Created on      | `datetime`  |     | ✅    |             |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`      |     |       |             |
| `id`           | ID              | `integer`   |     | ✅    |             |
| `student_id`   | Student Name    | `many2one`  |     | ✅    | op.student  |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                                  | Group                                   | Perms     |
| ------------------------------------- | --------------------------------------- | --------- |
| name_activity_progress_wizard         | Openeducat Activity Privilege / Manager | `R/W/C/D` |
| name_activity_progress_wizard_faculty | Openeducat Activity Privilege / User    | `R/W/C`   |

### 🗃️ `op.activity.type` — Activity Type

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
| `company_id`   | Company         | `many2one` |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Name            | `char`     | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                                    | Group                                   | Perms     |
| --------------------------------------- | --------------------------------------- | --------- |
| name_op_activity_type_back_office_admin | Openeducat Activity Privilege / Manager | `R/W/C/D` |
| name_op_activity_type_op_faculty        | Openeducat Activity Privilege / User    | `R`       |

**Record Rules:**

- **Activity Type multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `migration.report` — Migration Report

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label         | Type       | Req | Store | Relation   |
| -------------- | ------------- | ---------- | --- | ----- | ---------- |
| `create_date`  | Creation Date | `datetime` |     | ✅    |            |
| `create_uid`   | Created By    | `many2one` |     | ✅    | res.users  |
| `date`         | Date          | `date`     |     | ✅    |            |
| `display_name` | Display Name  | `char`     |     |       |            |
| `faculty_id`   | Faculty       | `many2one` |     | ✅    | op.faculty |
| `id`           | ID            | `integer`  |     | ✅    |            |
| `student_id`   | Student       | `many2one` |     | ✅    | op.student |
| `write_date`   | Updated Date  | `datetime` |     | ✅    |            |
| `write_uid`    | Updated By    | `many2one` |     | ✅    | res.users  |

**Access Rights:**

| Name                    | Group       | Perms |
| ----------------------- | ----------- | ----- |
| access_migration_report | Role / User | `R`   |
