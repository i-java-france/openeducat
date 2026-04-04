---
title: "Openeducat Lesson Enterprise"
module: "openeducat_lesson"
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

# 🟢 Openeducat Lesson Enterprise

> **Module:** `openeducat_lesson` | **Version:** `19.0.1.0` **Category:** Education |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_timetable]] [[openeducat_parent]]

## 📖 Description

## OpenEduCat Lesson Planning

### Manage Lesson Planning

[![](/openeducat_lesson/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module allows you to manage the lesson planning. This module adds feature to manage
the session to OpenEduCat.

[Contact Us](https://www.openeducat.org/contactus/)

## Lesson Planning

Lesson Planning contains all details of course, batch, subject, time, day, faculty.

![](/openeducat_lesson/static/description/lesson_form.png)

![](/openeducat_lesson/static/description/lesson_calendar.png)

Calendar view gives you better look to check lesson planning.

You can define list of lecture name with their respective course, subject and faculty.

![](/openeducat_lesson/static/description/lesson_list1.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Time Table/Lesson Planning`
- `Time Table/Lesson Planning/Lesson Planning`

### Views

- `* INHERIT form view inherited lesson (form)`
- `* INHERIT list view inherited lesson (list)`
- `lesson calendar view (calendar)`
- `lesson form view (form)`
- `lesson list view (list)`
- `lesson search view (search)`
- `op.lesson.graph (graph)`
- `op.lesson.pivot (pivot)`
- `report_lesson_planning (qweb)`

### Reports

- `Lesson planning`

## 🛠️ Technical Documentation

**2 model(s) defined by this module:**

### 🗃️ `op.lesson` — Lesson

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `active`                     | Active                 | `boolean`   |     | ✅    |                |
| `batch_id`                   | Batch                  | `many2one`  | ✅  | ✅    | op.batch       |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company    |
| `course_id`                  | Course                 | `many2one`  | ✅  | ✅    | op.course      |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users      |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `end_datetime`               | End Time               | `datetime`  |     | ✅    |                |
| `faculty_id`                 | Faculty                | `many2one`  |     | ✅    | op.faculty     |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `lesson_topic`               | Lecture Topic          | `text`      | ✅  | ✅    |                |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `name`                       | Lecture Name           | `char`      | ✅  | ✅    |                |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `session_ids`                | Session                | `many2many` |     | ✅    | op.session     |
| `start_datetime`             | Start Time             | `datetime`  |     | ✅    |                |
| `state`                      | Status                 | `selection` |     | ✅    |                |
| `subject_id`                 | Subject                | `many2one`  | ✅  | ✅    | op.subject     |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                            | Group               | Perms     |
| ------------------------------- | ------------------- | --------- |
| access_op_lesson_student        | Timetable / Manager | `R/W/C/D` |
| access_op_lesson_timetable_user | Timetable / User    | `R/W/C`   |

**Record Rules:**

- **Backoffice Lesson Rule** (161) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Faculty Lesson Rule** (160) `R/W/C/D`
  - Domain: `[('faculty_id.user_id', '=', user.id)]`
- **Student Lesson Rule** (161) `R/W/C/D`
  - Domain:
    `['|', ('session_ids.user_ids', 'in', user.ids), ('session_ids.user_ids', 'in',             user.child_ids.ids)]         `
- **Lesson multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.session` — Sessions

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
| `academic_plan_id`           | Academic Plan          | `many2one`  |     | ✅    | op.academic.plan    |
| `active`                     | Active                 | `boolean`   |     | ✅    |                     |
| `attendance_sheet`           | Session                | `one2many`  |     | ✅    | op.attendance.sheet |
| `batch_id`                   | Batch                  | `many2one`  |     | ✅    | op.batch            |
| `classroom_id`               | Classroom              | `many2one`  |     | ✅    | op.classroom        |
| `color`                      | Color Index            | `integer`   |     | ✅    |                     |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company         |
| `course_id`                  | Course                 | `many2one`  |     | ✅    | op.course           |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                     |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users           |
| `days`                       | Days                   | `selection` |     | ✅    |                     |
| `display_name`               | Display Name           | `char`      |     |       |                     |
| `end_datetime`               | End Time               | `datetime`  | ✅  | ✅    |                     |
| `faculty_id`                 | Faculty                | `many2one`  | ✅  | ✅    | op.faculty          |
| `has_message`                | Has Message            | `boolean`   |     |       |                     |
| `id`                         | ID                     | `integer`   |     | ✅    |                     |
| `lesson_ids`                 | Lesson                 | `many2many` |     | ✅    | op.lesson           |
| `meeting_count`              | Meeting Count          | `integer`   |     |       |                     |
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
| `name`                       | Name                   | `char`      |     | ✅    |                     |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating       |
| `required_field`             | Required Field         | `boolean`   |     | ✅    |                     |
| `section_ids`                | Section                | `many2many` |     | ✅    | op.section          |
| `start_datetime`             | Start Time             | `datetime`  | ✅  | ✅    |                     |
| `state`                      | Status                 | `selection` |     | ✅    |                     |
| `student_count`              | Student Count          | `integer`   |     |       |                     |
| `subject_id`                 | Subject                | `many2one`  | ✅  | ✅    | op.subject          |
| `timing`                     | Session timing         | `char`      |     |       |                     |
| `timing_id`                  | Timing                 | `many2one`  |     | ✅    | op.timing           |
| `type`                       | Day                    | `char`      |     | ✅    |                     |
| `user_id`                    | User                   | `many2one`  |     | ✅    | res.users           |
| `user_ids`                   | Users                  | `many2many` |     | ✅    | res.users           |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message        |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                     |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                           | Group               | Perms     |
| ------------------------------ | ------------------- | --------- |
| name_op_session_student        | Timetable / Manager | `R/W/C/D` |
| name_op_session_timetable_user | Timetable / User    | `R/W/C`   |

**Record Rules:**

- **Student Session rule** (160) `R/W/C/D`
  - Domain: `['|', ('user_ids','in',user.id), ('user_ids','in',user.child_ids.ids)]`
- **Manager Session Rule** (161) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **User Session Rule** (160) `R/W/C/D`
  - Domain: `[('faculty_id.user_id','=',user.id)]`
- **Timetable multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`
