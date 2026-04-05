---
title: "OpenEduCat Attendance Enterprise"
module: "openeducat_attendance_enterprise"
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

# 🟢 OpenEduCat Attendance Enterprise

> **Module:** `openeducat_attendance_enterprise` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_attendance_report_xlsx]] [[openeducat_attendance]]
[[openeducat_core_enterprise]] [[openeducat_student_progress_enterprise]] [[website]]
[[openeducat_onboarding]]

## 📖 Description

## OpenEduCat Attendance Enterprise

### Manage Student Attendance

[![](/openeducat_attendance_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module allows you to manage the student attendance. You can print absent report for
student.

[Contact Us](https://www.openeducat.org/contactus/)

## Attendance Register

Create attendance register for course and relevant batch. Faculties can then manage
attendance sheet date wise.

![](/openeducat_attendance_enterprise/static/description/attendance_register.png)

## Take Attendance

![](/openeducat_attendance_enterprise/static/description/take_attendance.png)

Record attendance of all students from a simple wizard. Select only absent students and
that students are added as absent and others as present default.

## Attendance Sheet

Attendance sheet shows the list of students with present status. You can find details
for number of present and absent students.

![](/openeducat_attendance_enterprise/static/description/attendance_sheet.png)

## Attendace Report

![](/openeducat_attendance_enterprise/static/description/attendance_report.png)

You can print attendance report for students between specific days.

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Class Attendances/Reporting`
- `Class Attendances/Reporting/Attendance Line Analysis`
- `Class Attendances/Reporting/Attendance Sheet Analysis`

### Views

- `* INHERIT Portal layout : invoice menu entries (qweb)`
- `* INHERIT Show Attendance (qweb)`
- `* INHERIT Student Progression Attendance Form (form)`
- `* INHERIT Student Progression Attendance list (list)`
- `* INHERIT op.academic.plan.form.attendance (form)`
- `* INHERIT op.attendance.line.form (form)`
- `* INHERIT op.attendance.line.list (list)`
- `* INHERIT op.attendance.onboard (list)`
- `* INHERIT op.attendance.register.inherited.form (form)`
- `* INHERIT op.attendance.register.inherited.list (list)`
- `* INHERIT op.attendance.sheet.inherited.form (form)`
- `* INHERIT op.attendance.sheet.inherited.list (list)`
- `* INHERIT op.batch.attendance.dashboard.kanban (kanban)`
- `* INHERIT student_attendance_progression_report (qweb)`
- `* INHERIT student_progression_attendance_portal_inherit (qweb)`
- `Attendance Progress Wizard (form)`
- `op.attendance.line.form (form)`
- `op.attendance.line.kanban (kanban)`
- `op.attendance.register.form (form)`
- `op.attendance.register.kanban (kanban)`
- `op.attendance.sheet.form (form)`
- `op.attendance.sheet.kanban (kanban)`
- `openeducat_attendance_portal (qweb)`

### Reports

- `Print Attendance Report`
- `Print Attendance Report By Week`

## 🛠️ Technical Documentation

**11 model(s) defined by this module:**

### 🗃️ `op.attendance.line` — Attendance Lines

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
| `absent`                     | Absent Unexcused       | `boolean`   |     | ✅    |                        |
| `active`                     | Active                 | `boolean`   |     | ✅    |                        |
| `attendance_date`            | Date                   | `date`      |     | ✅    |                        |
| `attendance_id`              | Attendance Sheet       | `many2one`  |     | ✅    | op.attendance.sheet    |
| `attendance_type_id`         | Attendance Type        | `many2one`  |     | ✅    | op.attendance.type     |
| `batch_id`                   | Batch                  | `many2one`  |     | ✅    | op.batch               |
| `check_in`                   | Attendance Time        | `datetime`  | ✅  | ✅    |                        |
| `color`                      | Color Index            | `integer`   |     | ✅    |                        |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company            |
| `course_id`                  | Course                 | `many2one`  |     | ✅    | op.course              |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                        |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users              |
| `display_name`               | Display Name           | `char`      |     |       |                        |
| `excused`                    | Absent Excused         | `boolean`   |     | ✅    |                        |
| `has_message`                | Has Message            | `boolean`   |     |       |                        |
| `id`                         | ID                     | `integer`   |     | ✅    |                        |
| `late`                       | Late                   | `boolean`   |     | ✅    |                        |
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
| `present`                    | Present                | `boolean`   |     | ✅    |                        |
| `progression_id`             | Progression No         | `many2one`  |     | ✅    | op.student.progression |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating          |
| `register_id`                | Register               | `many2one`  |     | ✅    | op.attendance.register |
| `remark`                     | Remark                 | `char`      |     | ✅    |                        |
| `session_id`                 | Session                | `many2one`  |     |       | op.session             |
| `state`                      | Status                 | `selection` |     |       |                        |
| `student_id`                 | Student                | `many2one`  | ✅  | ✅    | op.student             |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message           |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                        |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                       | Group                | Perms     |
| -------------------------- | -------------------- | --------- |
| op_attendance_line_student | Attendance / Manager | `R/W/C/D` |
| op_attendance_line_faculty | Attendance / User    | `R/W/C`   |

**Record Rules:**

- **Student Attendance** (169) `R/W/C/D`
  - Domain:
    `['|', ('student_id.user_id','=',user.id),             ('student_id.user_id','in',user.child_ids.ids)]         `
- **User Attendance** (168) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Attendance line multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.attendance.register` — Attendance Register

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation         |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ---------------- |
| `academic_plan_id`           | Academic Plan          | `many2one`  |     | ✅    | op.academic.plan |
| `active`                     | Active                 | `boolean`   |     | ✅    |                  |
| `attendance_option`          | Attendance Option      | `selection` |     | ✅    |                  |
| `auto_create`                | Auto Create            | `boolean`   |     | ✅    |                  |
| `auto_create_if_session`     | Create On Session      | `boolean`   |     | ✅    |                  |
| `auto_create_type`           | Duration               | `selection` |     | ✅    |                  |
| `batch_id`                   | Batch                  | `many2one`  |     | ✅    | op.batch         |
| `code`                       | Code                   | `char`      | ✅  | ✅    |                  |
| `color`                      | Color Index            | `integer`   |     | ✅    |                  |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company      |
| `course_id`                  | Course                 | `many2one`  |     | ✅    | op.course        |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                  |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users        |
| `display_name`               | Display Name           | `char`      |     |       |                  |
| `has_message`                | Has Message            | `boolean`   |     |       |                  |
| `id`                         | ID                     | `integer`   |     | ✅    |                  |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                  |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers   |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                  |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                  |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                  |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message     |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                  |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                  |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                  |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner      |
| `name`                       | Name                   | `char`      | ✅  | ✅    |                  |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating    |
| `required_field`             | Required Field         | `boolean`   |     | ✅    |                  |
| `section_id`                 | Section                | `many2one`  |     | ✅    | op.section       |
| `sheet_count`                | Sheet Count            | `integer`   |     |       |                  |
| `subject_id`                 | Subject                | `many2one`  |     | ✅    | op.subject       |
| `user_id`                    | User                   | `many2one`  |     | ✅    | res.users        |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message     |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                  |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                           | Group                | Perms     |
| ------------------------------ | -------------------- | --------- |
| op_attendance_register_student | Attendance / Manager | `R/W/C/D` |
| op_attendance_register_faculty | Attendance / User    | `R`       |

**Record Rules:**

- **Attendance Register multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.attendance.sheet` — Attendance Sheet

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
| `academic_plan_id`           | Academic Plan          | `many2one`  |     |       | op.academic.plan       |
| `active`                     | Active                 | `boolean`   |     | ✅    |                        |
| `attendance_date`            | Date                   | `date`      | ✅  | ✅    |                        |
| `attendance_line`            | Attendance Line        | `one2many`  |     | ✅    | op.attendance.line     |
| `attendance_option`          | Attendance Option      | `selection` |     | ✅    |                        |
| `batch_id`                   | Batch                  | `many2one`  |     | ✅    | op.batch               |
| `color`                      | Color Index            | `integer`   |     | ✅    |                        |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company            |
| `course_id`                  | Course                 | `many2one`  |     | ✅    | op.course              |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                        |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users              |
| `display_name`               | Display Name           | `char`      |     |       |                        |
| `excused_count`              | Total Absent Excused   | `integer`   |     |       |                        |
| `faculty_id`                 | Faculty                | `many2one`  |     | ✅    | op.faculty             |
| `has_message`                | Has Message            | `boolean`   |     |       |                        |
| `id`                         | ID                     | `integer`   |     | ✅    |                        |
| `late_count`                 | Total Late             | `integer`   |     |       |                        |
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
| `name`                       | Name                   | `char`      |     | ✅    |                        |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating          |
| `register_id`                | Register               | `many2one`  | ✅  | ✅    | op.attendance.register |
| `section_id`                 | Section                | `many2one`  |     | ✅    | op.section             |
| `session_id`                 | Session                | `many2one`  |     | ✅    | op.session             |
| `state`                      | Status                 | `selection` |     | ✅    |                        |
| `subject_id`                 | Subject                | `many2one`  |     | ✅    | op.subject             |
| `total_absent`               | Total Absent           | `integer`   |     |       |                        |
| `total_present`              | Total Present          | `integer`   |     |       |                        |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message           |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                        |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                        | Group                | Perms     |
| --------------------------- | -------------------- | --------- |
| op_attendance_sheet_student | Attendance / Manager | `R/W/C/D` |
| op_attendance_sheet_faculty | Attendance / User    | `R/W/C`   |

**Record Rules:**

- **Attendance Sheet multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.academic.plan` — OpenEduCat Academic Plan

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
| `academic_session_count`        | Academic Session count        | `integer`   |     |       |                         |
| `academic_year_id`              | Academic Year                 | `many2one`  | ✅  | ✅    | op.academic.year        |
| `active`                        | Active                        | `boolean`   |     | ✅    |                         |
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
| `attendance_sheet_count`        | Attendance Sheet              | `integer`   |     |       |                         |
| `code`                          | Code                          | `char`      | ✅  | ✅    |                         |
| `color`                         | Color Index                   | `integer`   |     | ✅    |                         |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company             |
| `course_configure_count`        | Course Configure Count        | `integer`   |     |       |                         |
| `course_id`                     | Course                        | `many2one`  |     | ✅    | op.course               |
| `course_plan_line`              | Configure Course              | `one2many`  |     | ✅    | op.course.plan          |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                         |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users               |
| `display_name`                  | Display Name                  | `char`      |     |       |                         |
| `duration_tracking`             | Status time                   | `json`      |     |       |                         |
| `end_date`                      | End Date                      | `date`      |     |       |                         |
| `fees_plan_count`               | Student Fees Plan count       | `integer`   |     |       |                         |
| `final_approve_user_id`         | Final Approve User            | `many2one`  |     | ✅    | res.users               |
| `first_approve_user_id`         | First Approve User            | `many2one`  |     | ✅    | res.users               |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                         |
| `id`                            | ID                            | `integer`   |     | ✅    |                         |
| `intake_year_ids`               | Intake Year                   | `many2many` |     | ✅    | op.intake.year          |
| `is_rotting`                    | Rotting                       | `boolean`   |     |       |                         |
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
| `name`                          | Name                          | `char`      |     |       |                         |
| `program_id`                    | Program                       | `many2one`  | ✅  | ✅    | op.program              |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating           |
| `rotting_days`                  | Days Rotting                  | `integer`   |     |       |                         |
| `sequence`                      | Sequence                      | `char`      |     | ✅    |                         |
| `stages_id`                     | Stage                         | `many2one`  |     | ✅    | op.academic.plan.stages |
| `start_date`                    | Start Date                    | `date`      |     |       |                         |
| `state`                         | State                         | `selection` |     | ✅    |                         |
| `student_count`                 | Student Count                 | `integer`   |     |       |                         |
| `student_course_ids`            | Students                      | `one2many`  |     | ✅    | op.student.course       |
| `subject_count`                 | Subject Count                 | `integer`   |     |       |                         |
| `topics_line`                   | Topics Line                   | `one2many`  |     | ✅    | op.topics               |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message            |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                         |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name                                      | Group                | Perms     |
| ----------------------------------------- | -------------------- | --------- |
| access_op_academic_plan_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_op_academic_plan_faculty           | OpenEduCat / User    | `R`       |
| access_op_academic_plan_portal_user       | Role / Portal        | `R/W`     |

**Record Rules:**

- **Academic Plan multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `op.batch` — OpenEduCat Batch

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation        |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | --------------- |
| `active`                     | Active                 | `boolean`   |     | ✅    |                 |
| `code`                       | Code                   | `char`      | ✅  | ✅    |                 |
| `color`                      | Color Index            | `integer`   |     | ✅    |                 |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company     |
| `course_id`                  | Course                 | `many2one`  | ✅  | ✅    | op.course       |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                 |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users       |
| `display_name`               | Display Name           | `char`      |     |       |                 |
| `end_date`                   | End Date               | `date`      | ✅  | ✅    |                 |
| `has_message`                | Has Message            | `boolean`   |     |       |                 |
| `id`                         | ID                     | `integer`   |     | ✅    |                 |
| `kanban_dashboard_graph`     | Kanban Dashboard Graph | `text`      |     |       |                 |
| `lectures_count`             | Lectures Count         | `integer`   |     |       |                 |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                 |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers  |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                 |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                 |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                 |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message    |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                 |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                 |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                 |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner     |
| `name`                       | Name                   | `char`      | ✅  | ✅    |                 |
| `notice_group_id`            | Notice Group           | `many2one`  |     | ✅    | op.notice.group |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating   |
| `start_date`                 | Start Date             | `date`      | ✅  | ✅    |                 |
| `student_count`              | Student Count          | `integer`   |     |       |                 |
| `total_absent_student`       | Total Absent           | `integer`   |     |       |                 |
| `total_present_student`      | Total Present          | `integer`   |     |       |                 |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message    |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                 |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                            | Group                | Perms     |
| ------------------------------- | -------------------- | --------- |
| name_op_batch_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| name_op_batch_faculty           | OpenEduCat / User    | `R/W/C`   |
| name_op_batch_parent            | Role / Portal        | `R`       |

**Record Rules:**

- **Batch multi-company** (Global) `R/W/C/D`
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

### 🗃️ `attendance.progress.wizard` — Attendance Progress Wizard

> ✳️ Transient (Wizard)

Progression Attendance

**Fields:**

| Field            | Label           | Type        | Req | Store | Relation           |
| ---------------- | --------------- | ----------- | --- | ----- | ------------------ |
| `attendance_ids` | Attendance      | `many2many` |     | ✅    | op.attendance.line |
| `create_date`    | Created on      | `datetime`  |     | ✅    |                    |
| `create_uid`     | Created by      | `many2one`  |     | ✅    | res.users          |
| `display_name`   | Display Name    | `char`      |     |       |                    |
| `id`             | ID              | `integer`   |     | ✅    |                    |
| `student_id`     | Student Name    | `many2one`  |     | ✅    | op.student         |
| `write_date`     | Last Updated on | `datetime`  |     | ✅    |                    |
| `write_uid`      | Last Updated by | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                 | Group                | Perms     |
| ------------------------------------ | -------------------- | --------- |
| name_attendance_progress_wizard      | Attendance / Manager | `R/W/C/D` |
| name_attendance_progress_wizard_user | Attendance / User    | `R/W/C`   |

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

### 🗃️ `report.op.attendance_xlsx` — Openeducat Attendance Report

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `report.op.attendance_xlsx_by_week` — Openeducat Attendance Report By Week

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |
