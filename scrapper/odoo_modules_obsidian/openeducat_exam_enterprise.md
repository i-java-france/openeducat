---
title: "OpenEduCat Exam Enterprise"
module: "openeducat_exam_enterprise"
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

# 🟢 OpenEduCat Exam Enterprise

> **Module:** `openeducat_exam_enterprise` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_exam]] [[openeducat_core_enterprise]]
[[openeducat_student_progress_enterprise]] [[openeducat_onboarding]]

## 📖 Description

## OpenEduCat Exam Enterprise

### Exam Management

[![](/openeducat_exam_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

Exam is very important part of any educational institute. Exam module from OpenEduCat
helps you managing most of the exam details very easily using Exam module.

[Contact Us](https://www.openeducat.org/contactus/)

## Exam Session

Exam is managed under Exam Sessions. Where one session refers to one particular exam,
for example for the students of graduation exam session may be 1st monthly exam. Exam
session records details like start date, end date, type of the exam etc...

![](/openeducat_exam_enterprise/static/description/exam_session.png)

## Exam

![](/openeducat_exam_enterprise/static/description/exam.png)

Exam records details of exam-subject, duration of exam, total marks, passing marks, and
list of attendees of course.

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Exams/Exam Dashboard`

### Views

- `* INHERIT Portal layout : invoice menu entries (qweb)`
- `* INHERIT Show Exam (qweb)`
- `* INHERIT Student Progression Marksheet Line Form (form)`
- `* INHERIT Student Progression Marksheet Line list (list)`
- `* INHERIT exam_notification_inherit (qweb)`
- `* INHERIT op.exam.attendees.inherited.list (list)`
- `* INHERIT op.exam.attendees.inherited.search (search)`
- `* INHERIT op.exam.inherited.form (form)`
- `* INHERIT op.exam.inherited.list (list)`
- `* INHERIT op.exam.inherited.search (search)`
- `* INHERIT op.exam.room.inherited.form (form)`
- `* INHERIT op.exam.room.inherited_list (list)`
- `* INHERIT op.exam.session.inherit.form (form)`
- `* INHERIT op.exam.session.inherit.search (search)`
- `* INHERIT op.exam.session.tree.inherit (list)`
- `* INHERIT op.exam.type.inherited.form (form)`
- `* INHERIT op.exam.type.inherited.list (list)`
- `* INHERIT op.grade.configuration.list (list)`
- `* INHERIT op.marksheet.line.form (form)`
- `* INHERIT op.marksheet.line.inherited.form (form)`
- `* INHERIT op.marksheet.line.inherited.list (list)`
- `* INHERIT op.marksheet.register.inherited.form (form)`
- `* INHERIT op.marksheet.register.inherited.list (list)`
- `* INHERIT op.result.line.form (form)`
- `* INHERIT op.result.line.inherited.list (list)`
- `* INHERIT op.result.line.inherited.search (search)`
- `* INHERIT op.result.template.inherited.form (form)`
- `* INHERIT op.result.template.inherited.list (list)`
- `* INHERIT op.result.template.inherited.search (search)`
- `* INHERIT student_exam_progression_report (qweb)`
- `* INHERIT student_progression_exam_portal_inherit (qweb)`
- `Activity Progress Wizard (form)`
- `op.exam.room.form (form)`
- `op.exam.type.form (form)`
- `op.exam.view.kanban (kanban)`
- `op.grade.configuration.form (form)`
- `openeducat_exam_portal (qweb)`
- `openeducat_exam_portal_data (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**14 model(s) defined by this module:**

### 🗃️ `op.exam` — Exam

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
| `attendees_count`            | Attendees Count        | `integer`   |     |       |                    |
| `attendees_line`             | Attendees              | `one2many`  |     | ✅    | op.exam.attendees  |
| `batch_id`                   | Batch                  | `many2one`  |     | ✅    | op.batch           |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company        |
| `course_id`                  | Course                 | `many2one`  |     | ✅    | op.course          |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                    |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users          |
| `display_name`               | Display Name           | `char`      |     |       |                    |
| `end_time`                   | End Time               | `datetime`  | ✅  | ✅    |                    |
| `exam_code`                  | Exam Code              | `char`      | ✅  | ✅    |                    |
| `faculty_id`                 | Faculty                | `many2one`  | ✅  | ✅    | op.faculty         |
| `grading_assignment_id`      | Grading Assignment     | `many2one`  |     | ✅    | grading.assignment |
| `has_message`                | Has Message            | `boolean`   |     |       |                    |
| `id`                         | ID                     | `integer`   |     | ✅    |                    |
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
| `min_marks`                  | Passing Marks          | `integer`   | ✅  | ✅    |                    |
| `name`                       | Exam                   | `char`      | ✅  | ✅    |                    |
| `note`                       | Note                   | `text`      |     | ✅    |                    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating      |
| `responsible_id`             | Responsible            | `many2many` |     | ✅    | op.faculty         |
| `results_entered`            | Results Entered        | `boolean`   |     | ✅    |                    |
| `session_id`                 | Exam Session           | `many2one`  |     | ✅    | op.exam.session    |
| `start_time`                 | Start Time             | `datetime`  | ✅  | ✅    |                    |
| `state`                      | Status                 | `selection` |     | ✅    |                    |
| `subject_id`                 | Subject                | `many2one`  | ✅  | ✅    | op.subject         |
| `total_marks`                | Total Marks            | `integer`   | ✅  | ✅    |                    |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message       |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                    |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                      | Group          | Perms     |
| ------------------------- | -------------- | --------- |
| op_exam_back_office_admin | Exam / Manager | `R/W/C/D` |
| op_exam_faculty           | Exam / User    | `R/W/C`   |

**Record Rules:**

- **Exam multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.exam.session` — Exam Session

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
| `active`                     | Active                 | `boolean`   |     | ✅    |                  |
| `batch_id`                   | Batch                  | `many2one`  | ✅  | ✅    | op.batch         |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company      |
| `complete_exam_count`        | Complete Exam Count    | `integer`   |     |       |                  |
| `course_id`                  | Course                 | `many2one`  | ✅  | ✅    | op.course        |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                  |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users        |
| `display_name`               | Display Name           | `char`      |     |       |                  |
| `end_date`                   | End Date               | `date`      | ✅  | ✅    |                  |
| `evaluation_type`            | Evolution Type         | `selection` | ✅  | ✅    |                  |
| `exam_code`                  | Exam Session Code      | `char`      | ✅  | ✅    |                  |
| `exam_count`                 | Exam Count             | `integer`   |     |       |                  |
| `exam_ids`                   | Exam(s)                | `one2many`  |     | ✅    | op.exam          |
| `exams_count`                | Exams                  | `integer`   |     |       |                  |
| `exam_type`                  | Exam Type              | `many2one`  | ✅  | ✅    | op.exam.type     |
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
| `name`                       | Exam Session           | `char`      | ✅  | ✅    |                  |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating    |
| `start_date`                 | Start Date             | `date`      | ✅  | ✅    |                  |
| `state`                      | Status                 | `selection` |     | ✅    |                  |
| `term_id`                    | Term                   | `many2one`  | ✅  | ✅    | op.academic.term |
| `venue`                      | Venue                  | `many2one`  |     | ✅    | res.partner      |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message     |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                  |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users        |
| `year_id`                    | Academic Year          | `many2one`  | ✅  | ✅    | op.academic.year |

**Access Rights:**

| Name                              | Group          | Perms     |
| --------------------------------- | -------------- | --------- |
| op_exam_session_back_office_admin | Exam / Manager | `R/W/C/D` |
| op_exam_session_faculty           | Exam / User    | `R/W/C`   |

**Record Rules:**

- **Exam Session multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.marksheet.register` — Marksheet Register

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
| `exam_session_id`            | Exam Session           | `many2one`  | ✅  | ✅    | op.exam.session    |
| `generated_by`               | Generated By           | `many2one`  | ✅  | ✅    | res.users          |
| `generated_date`             | Generated Date         | `date`      | ✅  | ✅    |                    |
| `has_message`                | Has Message            | `boolean`   |     |       |                    |
| `id`                         | ID                     | `integer`   |     | ✅    |                    |
| `marksheet_line`             | Marksheets             | `one2many`  |     | ✅    | op.marksheet.line  |
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
| `name`                       | Marksheet Register     | `char`      | ✅  | ✅    |                    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating      |
| `result_template_id`         | Result Template        | `many2one`  | ✅  | ✅    | op.result.template |
| `state`                      | Status                 | `selection` | ✅  | ✅    |                    |
| `total_failed`               | Total Fail             | `integer`   |     | ✅    |                    |
| `total_pass`                 | Total Pass             | `integer`   |     | ✅    |                    |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message       |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                    |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                    | Group          | Perms     |
| --------------------------------------- | -------------- | --------- |
| op_marksheet_register_back_office_admin | Exam / Manager | `R/W/C/D` |
| op_marksheet_register_faculty           | Exam / User    | `R/W/C`   |

**Record Rules:**

- **Marksheet Register multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.result.template` — Result Template

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
| `active`                     | Active                 | `boolean`   |     | ✅    |                        |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company            |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                        |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users              |
| `display_name`               | Display Name           | `char`      |     |       |                        |
| `evaluation_type`            | Evolution Type         | `selection` |     | ✅    |                        |
| `exam_session_id`            | Exam Session           | `many2one`  | ✅  | ✅    | op.exam.session        |
| `grade_ids`                  | Grade Configuration    | `many2many` |     | ✅    | op.grade.configuration |
| `grade_scale_id`             | Grade Scale            | `many2one`  |     | ✅    | op.grade.scale         |
| `has_message`                | Has Message            | `boolean`   |     |       |                        |
| `id`                         | ID                     | `integer`   |     | ✅    |                        |
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
| `name`                       | Name                   | `char`      | ✅  | ✅    |                        |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating          |
| `result_date`                | Result Date            | `date`      | ✅  | ✅    |                        |
| `state`                      | Status                 | `selection` |     | ✅    |                        |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message           |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                        |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                                      | Group          | Perms     |
| ----------------------------------------- | -------------- | --------- |
| name_op_result_template_back_office_admin | Exam / Manager | `R/W/C/D` |
| name_op_result_template_faculty           | Exam / User    | `R/W/C`   |

**Record Rules:**

- **Result Template multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

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

### 🗃️ `op.exam.attendees` — Exam Attendees

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation     |
| -------------- | --------------- | ----------- | --- | ----- | ------------ |
| `batch_id`     | Batch           | `many2one`  |     | ✅    | op.batch     |
| `company_id`   | Company         | `many2one`  |     | ✅    | res.company  |
| `course_id`    | Course          | `many2one`  |     | ✅    | op.course    |
| `create_date`  | Created on      | `datetime`  |     | ✅    |              |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users    |
| `display_name` | Display Name    | `char`      |     |       |              |
| `exam_id`      | Exam            | `many2one`  | ✅  | ✅    | op.exam      |
| `grade`        | Grade           | `char`      |     |       |              |
| `id`           | ID              | `integer`   |     | ✅    |              |
| `marks`        | Marks           | `integer`   |     | ✅    |              |
| `note`         | Note            | `text`      |     | ✅    |              |
| `room_id`      | Room            | `many2one`  |     | ✅    | op.exam.room |
| `status`       | Status          | `selection` | ✅  | ✅    |              |
| `student_id`   | Student         | `many2one`  | ✅  | ✅    | op.student   |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |              |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users    |

**Access Rights:**

| Name                      | Group       | Perms     |
| ------------------------- | ----------- | --------- |
| op_exam_attendees_faculty | Exam / User | `R/W/C/D` |

**Record Rules:**

- **Exam Attendees multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.exam.room` — Exam Room

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation     |
| -------------- | --------------- | ---------- | --- | ----- | ------------ |
| `capacity`     | No of Seats     | `integer`  |     | ✅    |              |
| `classroom_id` | Classroom       | `many2one` | ✅  | ✅    | op.classroom |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company  |
| `create_date`  | Created on      | `datetime` |     | ✅    |              |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users    |
| `display_name` | Display Name    | `char`     |     |       |              |
| `id`           | ID              | `integer`  |     | ✅    |              |
| `name`         | Name            | `char`     | ✅  | ✅    |              |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |              |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users    |

**Access Rights:**

| Name                           | Group          | Perms     |
| ------------------------------ | -------------- | --------- |
| op_exam_room_back_office_admin | Exam / Manager | `R/W/C/D` |
| op_exam_room_faculty           | Exam / User    | `R`       |

**Record Rules:**

- **Exam Room multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.exam.type` — Exam Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
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

| Name                           | Group          | Perms     |
| ------------------------------ | -------------- | --------- |
| op_exam_type_back_office_admin | Exam / Manager | `R/W/C/D` |
| op_exam_type_faculty           | Exam / User    | `R`       |

**Record Rules:**

- **Exam Type multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.grade.configuration` — Grade Configuration

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label              | Type       | Req | Store | Relation    |
| -------------- | ------------------ | ---------- | --- | ----- | ----------- |
| `company_id`   | Company            | `many2one` |     | ✅    | res.company |
| `create_date`  | Created on         | `datetime` |     | ✅    |             |
| `create_uid`   | Created by         | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name       | `char`     |     |       |             |
| `grade_point`  | Grade Point        | `float`    |     | ✅    |             |
| `id`           | ID                 | `integer`  |     | ✅    |             |
| `max_per`      | Maximum Percentage | `integer`  | ✅  | ✅    |             |
| `min_per`      | Minimum Percentage | `integer`  | ✅  | ✅    |             |
| `result`       | Result to Display  | `char`     | ✅  | ✅    |             |
| `write_date`   | Last Updated on    | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by    | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                                      | Group          | Perms     |
| ----------------------------------------- | -------------- | --------- |
| access_op_grade_configuration_back_office | Exam / Manager | `R/W/C/D` |
| access_op_grade_configuration_faculty     | Exam / User    | `R`       |

**Record Rules:**

- **Grade Configuration multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.marksheet.line` — Marksheet Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field              | Label              | Type        | Req | Store | Relation               |
| ------------------ | ------------------ | ----------- | --- | ----- | ---------------------- |
| `active`           | Active             | `boolean`   |     | ✅    |                        |
| `company_id`       | Company            | `many2one`  |     | ✅    | res.company            |
| `create_date`      | Created on         | `datetime`  |     | ✅    |                        |
| `create_uid`       | Created by         | `many2one`  |     | ✅    | res.users              |
| `display_name`     | Display Name       | `char`      |     |       |                        |
| `evaluation_type`  | Evolution Type     | `selection` |     | ✅    |                        |
| `exam_name`        | Exam Session       | `many2one`  |     |       | op.exam.session        |
| `exam_type`        | Exam Type          | `many2one`  |     |       | op.exam.type           |
| `generated_date`   | Generated Date     | `date`      | ✅  | ✅    |                        |
| `gpa_count`        | GPA                | `float`     |     |       |                        |
| `grade`            | Grade              | `char`      |     |       |                        |
| `grand_total`      | Grand Total        | `integer`   |     |       |                        |
| `id`               | ID                 | `integer`   |     | ✅    |                        |
| `is_read`          | Read?              | `boolean`   |     | ✅    |                        |
| `marksheet_reg_id` | Marksheet Register | `many2one`  |     | ✅    | op.marksheet.register  |
| `percentage`       | Percentage         | `float`     |     | ✅    |                        |
| `progression_id`   | Progression No     | `many2one`  |     | ✅    | op.student.progression |
| `result_line`      | Results            | `one2many`  |     | ✅    | op.result.line         |
| `status`           | Status             | `selection` |     | ✅    |                        |
| `student_id`       | Student            | `many2one`  | ✅  | ✅    | op.student             |
| `total_marks`      | Total Marks        | `integer`   |     | ✅    |                        |
| `total_points`     | total_points       | `float`     |     | ✅    |                        |
| `write_date`       | Last Updated on    | `datetime`  |     | ✅    |                        |
| `write_uid`        | Last Updated by    | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                                | Group          | Perms     |
| ----------------------------------- | -------------- | --------- |
| op_marksheet_line_back_office_admin | Exam / Manager | `R/W/C/D` |
| op_marksheet_line_student           | Exam / Manager | `R/W/C/D` |
| op_marksheet_line_faculty           | Exam / User    | `R/W/C`   |

**Record Rules:**

- **Student Marksheet** (141) `R/W/C/D`
  - Domain:
    `['|', ('student_id.user_id','=',user.id),             ('student_id.user_id','in',user.child_ids.ids)]         `
- **Admin Marksheet** (141) `R/W/C/D`
  - Domain: `[(1,"=",1)]`
- **Marksheet Line multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `marksheet.line.progress.wizard` — Marksheet line Progress Wizard

> ✳️ Transient (Wizard)

Progression Marksheet

**Fields:**

| Field           | Label           | Type        | Req | Store | Relation          |
| --------------- | --------------- | ----------- | --- | ----- | ----------------- |
| `create_date`   | Created on      | `datetime`  |     | ✅    |                   |
| `create_uid`    | Created by      | `many2one`  |     | ✅    | res.users         |
| `display_name`  | Display Name    | `char`      |     |       |                   |
| `id`            | ID              | `integer`   |     | ✅    |                   |
| `marksheet_ids` | Marksheet       | `many2many` |     | ✅    | op.marksheet.line |
| `student_id`    | Student Name    | `many2one`  |     | ✅    | op.student        |
| `write_date`    | Last Updated on | `datetime`  |     | ✅    |                   |
| `write_uid`     | Last Updated by | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                                          | Group          | Perms     |
| --------------------------------------------- | -------------- | --------- |
| access_marksheet_line_progress_wizard         | Exam / Manager | `R/W/C/D` |
| access_marksheet_line_progress_wizard_faculty | Exam / User    | `R/W/C`   |

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

### 🗃️ `op.result.line` — Result Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label           | Type        | Req | Store | Relation          |
| ------------------- | --------------- | ----------- | --- | ----- | ----------------- |
| `company_id`        | Company         | `many2one`  |     | ✅    | res.company       |
| `create_date`       | Created on      | `datetime`  |     | ✅    |                   |
| `create_uid`        | Created by      | `many2one`  |     | ✅    | res.users         |
| `credit`            | Subject Credit  | `float`     |     |       |                   |
| `display_name`      | Display Name    | `char`      |     |       |                   |
| `evaluation_type`   | Evolution Type  | `selection` |     | ✅    |                   |
| `exam_id`           | Exam            | `many2one`  | ✅  | ✅    | op.exam           |
| `grade`             | Grade           | `char`      |     |       |                   |
| `grade_point`       | Grade Point     | `float`     |     | ✅    |                   |
| `id`                | ID              | `integer`   |     | ✅    |                   |
| `marks`             | Marks           | `integer`   | ✅  | ✅    |                   |
| `marksheet_line_id` | Marksheet Line  | `many2one`  |     | ✅    | op.marksheet.line |
| `qp`                | Quality Points  | `float`     |     |       |                   |
| `session_id`        | Exam Session    | `many2one`  |     | ✅    | op.exam.session   |
| `status`            | Status          | `selection` |     | ✅    |                   |
| `student_id`        | Student         | `many2one`  | ✅  | ✅    | op.student        |
| `write_date`        | Last Updated on | `datetime`  |     | ✅    |                   |
| `write_uid`         | Last Updated by | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                             | Group          | Perms     |
| -------------------------------- | -------------- | --------- |
| op_result_line_back_office_admin | Exam / Manager | `R/W/C/D` |
| op_result_line_student           | Exam / Manager | `R/W/C/D` |
| op_result_line_faculty           | Exam / User    | `R/W/C`   |

**Record Rules:**

- **Student Result Line** (141) `R/W/C/D`
  - Domain:
    `['|', ('student_id.user_id','=',user.id),             ('student_id.user_id','in',user.child_ids.ids)]         `
- **Admin Result Line** (141) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Result Line multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `
