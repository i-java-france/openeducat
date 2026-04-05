---
title: "OpenEduCat Exam GPA Enterprise"
module: "openeducat_exam_gpa_enterprise"
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

# 🟢 OpenEduCat Exam GPA Enterprise

> **Module:** `openeducat_exam_gpa_enterprise` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_exam_enterprise]] [[openeducat_student_progress_enterprise]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT op.grade.point.inherited.form (form)`
- `* INHERIT op.grade.point.inherited.list (list)`
- `* INHERIT op.marksheet.line.inherited.form (form)`
- `* INHERIT op.marksheet.line.inherited.list (list)`
- `* INHERIT op.result.line.inherited.form (form)`
- `* INHERIT op.result.line.inherited.list (list)`
- `* INHERIT op.student.progression.inherited.form (form)`
- `* INHERIT op.subject.inherited.form (form)`
- `* INHERIT op.subject.inherited.list (list)`
- `student_transcript_report (qweb)`

### Reports

- `Transcript`

## 🛠️ Technical Documentation

**5 model(s) defined by this module:**

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

### 🗃️ `op.subject` — Subject Material Allocation

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                       | Type        | Req | Store | Relation          |
| ---------------------------- | --------------------------- | ----------- | --- | ----- | ----------------- |
| `active`                     | Active                      | `boolean`   |     | ✅    |                   |
| `assignment_count`           | Assignment Count            | `integer`   |     |       |                   |
| `attachment_ids`             | Attachments                 | `one2many`  |     | ✅    | ir.attachment     |
| `attempted_units`            | Attempted Units             | `selection` |     | ✅    |                   |
| `code`                       | Code                        | `char`      | ✅  | ✅    |                   |
| `company_id`                 | Company                     | `many2one`  |     | ✅    | res.company       |
| `course_id`                  | Course                      | `many2one`  |     | ✅    | op.course         |
| `create_date`                | Created on                  | `datetime`  |     | ✅    |                   |
| `create_uid`                 | Created by                  | `many2one`  |     | ✅    | res.users         |
| `credit_point`               | Credit                      | `float`     |     | ✅    |                   |
| `default_template`           | Use Default Course Template | `boolean`   |     | ✅    |                   |
| `department_id`              | Department                  | `many2one`  |     | ✅    | op.department     |
| `display_name`               | Display Name                | `char`      |     |       |                   |
| `grade_template_ids`         | Grade Template              | `many2many` | ✅  | ✅    | op.grade.template |
| `grade_weightage`            | Grade Weightage             | `float`     |     | ✅    |                   |
| `has_message`                | Has Message                 | `boolean`   |     |       |                   |
| `id`                         | ID                          | `integer`   |     | ✅    |                   |
| `message_attachment_count`   | Attachment Count            | `integer`   |     |       |                   |
| `message_follower_ids`       | Followers                   | `one2many`  |     | ✅    | mail.followers    |
| `message_has_error`          | Message Delivery error      | `boolean`   |     |       |                   |
| `message_has_error_counter`  | Number of errors            | `integer`   |     |       |                   |
| `message_has_sms_error`      | SMS Delivery error          | `boolean`   |     |       |                   |
| `message_ids`                | Messages                    | `one2many`  |     | ✅    | mail.message      |
| `message_is_follower`        | Is Follower                 | `boolean`   |     |       |                   |
| `message_needaction`         | Action Needed               | `boolean`   |     |       |                   |
| `message_needaction_counter` | Number of Actions           | `integer`   |     |       |                   |
| `message_partner_ids`        | Followers (Partners)        | `many2many` |     |       | res.partner       |
| `name`                       | Name                        | `char`      | ✅  | ✅    |                   |
| `parent_sub_id`              | Parent Subject              | `many2one`  |     | ✅    | op.subject        |
| `rating_ids`                 | Ratings                     | `one2many`  |     | ✅    | rating.rating     |
| `subject_credit`             | Credit Hours                | `float`     |     | ✅    |                   |
| `subject_type`               | Subject Type                | `selection` | ✅  | ✅    |                   |
| `timetable_count`            | Timetable Count             | `integer`   |     |       |                   |
| `type`                       | Type                        | `selection` | ✅  | ✅    |                   |
| `website_message_ids`        | Website Messages            | `one2many`  |     | ✅    | mail.message      |
| `write_date`                 | Last Updated on             | `datetime`  |     | ✅    |                   |
| `write_uid`                  | Last Updated by             | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                              | Group                | Perms     |
| --------------------------------- | -------------------- | --------- |
| name_op_subject_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| name_op_subject_faculty           | OpenEduCat / User    | `R`       |
| name_op_subject_library           | Library / Manager    | `R`       |
| name_op_subject_parent            | Role / Portal        | `R`       |

**Record Rules:**

- **Subject multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`
- **Subject multi-department** (Global) `R/W/C/D`
  - Domain:
    `['|','|',('department_id','=',False),('department_id','child_of',[user.dept_id.id]),('department_id','in',user.department_ids.ids)]`

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
