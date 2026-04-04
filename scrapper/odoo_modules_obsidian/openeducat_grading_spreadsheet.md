---
title: "OpenEduCat Grading spreadsheet"
module: "openeducat_grading_spreadsheet"
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

# 🟢 OpenEduCat Grading spreadsheet

> **Module:** `openeducat_grading_spreadsheet` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_grading]] [[spreadsheet_base]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

_none_

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

### 🗃️ `gradebook.gradebook` — Grade Book

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ----------------------- |
| `academic_year_id`              | Year                          | `many2many` | ✅  | ✅    | op.academic.year        |
| `academic_year_ids`             | Academic Year                 | `many2one`  |     | ✅    | op.academic.year        |
| `access_token`                  | Security Token                | `char`      |     | ✅    |                         |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event          |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                         |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                         |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                         |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity           |
| `activity_state`                | Activity State                | `selection` |     |       |                         |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                         |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                         |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type      |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users               |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company             |
| `course_id`                     | Course                        | `many2one`  | ✅  | ✅    | op.course               |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                         |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users               |
| `display_name`                  | Display Name                  | `char`      |     |       |                         |
| `grade`                         | Grade                         | `char`      |     | ✅    |                         |
| `gradebook`                     | Gradebook                     | `char`      |     | ✅    |                         |
| `gradebook_line_id`             | Gradebook Line                | `one2many`  |     | ✅    | gradebook.line          |
| `grade_override`                | Final Grades                  | `one2many`  |     | ✅    | op.grade.override.line  |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                         |
| `id`                            | ID                            | `integer`   |     | ✅    |                         |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                         |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers          |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                         |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                         |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                         |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message            |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                         |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                         |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                         |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner             |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                         |
| `name`                          | Name                          | `char`      | ✅  | ✅    |                         |
| `override_hide`                 | Override Hide                 | `boolean`   |     | ✅    |                         |
| `percentage`                    | Percentage                    | `float`     |     | ✅    |                         |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating           |
| `report_access_url`             | Portal Access URL Report      | `char`      |     |       |                         |
| `report_type`                   | Report Type                   | `selection` |     | ✅    |                         |
| `spreadsheet_id`                | Spreadsheet                   | `many2one`  |     | ✅    | spreadsheet.spreadsheet |
| `state`                         | State                         | `selection` |     | ✅    |                         |
| `student_id`                    | Student                       | `many2one`  | ✅  | ✅    | op.student              |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message            |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                         |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name                                         | Group             | Perms     |
| -------------------------------------------- | ----------------- | --------- |
| access_gradebook_gradebook_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_gradebook_gradebook_faculty           | Grading / User    | `R/W/C`   |
| access_gradebook_gradebook                   | Role / Portal     | `R`       |

**Record Rules:**

- **Gradebook Gradebook multi company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `
