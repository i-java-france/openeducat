---
title: "OpenEduCat Exam Grading Bridge"
module: "openeducat_exam_grading_bridge"
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

# 🟢 OpenEduCat Exam Grading Bridge

> **Module:** `openeducat_exam_grading_bridge` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_exam_enterprise]] [[openeducat_grading]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT op.exam.attendees.inheritedlist (list)`
- `* INHERIT op.exam.inherited.grading.form (form)`
- `* INHERIT op.exam.session.grading.form (form)`
- `* INHERIT op.result.template.inherited.form (form)`
- `* INHERIT op.result.template.inherited.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**8 model(s) defined by this module:**

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

### 🗃️ `grading.assignment.type` — Assignment Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation    |
| -------------- | --------------- | ----------- | --- | ----- | ----------- |
| `assign_type`  | Type            | `selection` |     | ✅    |             |
| `code`         | Code            | `char`      | ✅  | ✅    |             |
| `company_id`   | Company         | `many2one`  |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime`  |     | ✅    |             |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`      |     |       |             |
| `id`           | ID              | `integer`   |     | ✅    |             |
| `name`         | Name            | `char`      | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                                       | Group                | Perms     |
| ------------------------------------------ | -------------------- | --------- |
| grading_assignment_type_assignment_manager | Assignment / Manager | `R/W/C/D` |
| grading_assignment_type_user               | Assignment / User    | `R/W/C`   |

**Record Rules:**

- **Assignment Type multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

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
