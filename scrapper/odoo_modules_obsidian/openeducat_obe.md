---
title: "OpenEduCat OBE"
module: "openeducat_obe"
state: "installed"
version: "19.0.1.0.2"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "LGPL-3"
category: "Education"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________, odoo/app]
---

# 🟢 OpenEduCat OBE

> **Module:** `openeducat_obe` | **Version:** `19.0.1.0.2` **Category:** Education |
> **License:** `LGPL-3` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_core_enterprise]] [[openeducat_assignment_enterprise]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `SIS/Configuration/OBE`
- `SIS/Configuration/OBE/Course outcome`
- `SIS/Configuration/OBE/Program outcome`
- `SIS/Reporting/Attainment`

### Views

- `* INHERIT op.academic.plan.form (form)`
- `* INHERIT op.assignment.form (form)`
- `* INHERIT op.course.plan.form (form)`
- `attainment.dashboard.record.pivot (pivot)`
- `copo.lines.form (form)`
- `copo.lines.tree (list)`
- `copo.map.form (form)`
- `copo.map.tree (list)`
- `course.outcome.form (form)`
- `course.outcome.tree (list)`
- `program.outcome.form (form)`
- `program.outcome.tree (list)`
- `student.attainment.form (form)`
- `student.attainment.tree (list)`
- `student.co.attainment.form (form)`
- `student.co.attainment.tree (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**11 model(s) defined by this module:**

### 🗃️ `op.assignment` — Assignment

> 📧 Mail Thread

Model for managing assignments with rubric-based assessment.

    This model extends the base assignment model to include rubric-based
    assessment functionality. It handles rubric templates and final assessment
    criteria for assignments.

**Fields:**

| Field                               | Label                         | Type        | Req | Store | Relation                   |
| ----------------------------------- | ----------------------------- | ----------- | --- | ----- | -------------------------- |
| `active`                            | Active                        | `boolean`   |     | ✅    |                            |
| `activity_calendar_event_id`        | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event             |
| `activity_date_deadline`            | Next Activity Deadline        | `date`      |     |       |                            |
| `activity_exception_decoration`     | Activity Exception Decoration | `selection` |     |       |                            |
| `activity_exception_icon`           | Icon                          | `char`      |     |       |                            |
| `activity_ids`                      | Activities                    | `one2many`  |     |       | mail.activity              |
| `activity_state`                    | Activity State                | `selection` |     |       |                            |
| `activity_summary`                  | Next Activity Summary         | `char`      |     |       |                            |
| `activity_type_icon`                | Activity Type Icon            | `char`      |     |       |                            |
| `activity_type_id`                  | Next Activity Type            | `many2one`  |     |       | mail.activity.type         |
| `activity_user_id`                  | Responsible User              | `many2one`  |     |       | res.users                  |
| `additional_attempt`                | Student Additonal Attempt     | `one2many`  |     | ✅    | student.additional.attempt |
| `allocation_ids`                    | Allocated To                  | `many2many` |     | ✅    | op.student                 |
| `assignment_sub_line`               | Submission                    | `one2many`  |     | ✅    | op.assignment.sub.line     |
| `assignment_sub_line_count`         | Submissions                   | `integer`   |     |       |                            |
| `assignment_type`                   | Assignment Type               | `many2one`  | ✅  |       | grading.assignment.type    |
| `attachment_ids`                    | Attachments                   | `one2many`  |     | ✅    | ir.attachment              |
| `attempt`                           | Score Attempt Using           | `selection` |     | ✅    |                            |
| `attempt_type`                      | Number of Attempt             | `selection` | ✅  | ✅    |                            |
| `batch_id`                          | Batch                         | `many2one`  | ✅  | ✅    | op.batch                   |
| `color`                             | Color Index                   | `integer`   |     |       |                            |
| `co_map_ids`                        | CO                            | `one2many`  |     | ✅    | assignment.co              |
| `company_id`                        | Company                       | `many2one`  |     | ✅    | res.company                |
| `course_id`                         | Course                        | `many2one`  | ✅  |       | op.course                  |
| `courses_subjects`                  | Courses Subjects              | `many2many` |     | ✅    | op.subject                 |
| `create_date`                       | Created on                    | `datetime`  |     | ✅    |                            |
| `create_uid`                        | Created by                    | `many2one`  |     | ✅    | res.users                  |
| `description`                       | Description                   | `text`      | ✅  | ✅    |                            |
| `display_name`                      | Display Name                  | `char`      |     |       |                            |
| `evaluation_type`                   | Evolution Type                | `selection` | ✅  | ✅    |                            |
| `faculty_id`                        | Faculty                       | `many2one`  | ✅  |       | op.faculty                 |
| `final_assessment_attempt_criteria` | Final Attempt Criteria        | `selection` | ✅  | ✅    |                            |
| `grade`                             | Grade                         | `many2one`  |     |       | op.grade.table             |
| `gradebook_line_id`                 | Gradebook Line                | `one2many`  |     |       | gradebook.line             |
| `grading_assignment_id`             | Grading Assignment            | `many2one`  | ✅  | ✅    | grading.assignment         |
| `has_message`                       | Has Message                   | `boolean`   |     |       |                            |
| `hide`                              | Hide                          | `boolean`   |     |       |                            |
| `hide_subject`                      | Hide Subject                  | `boolean`   |     |       |                            |
| `id`                                | ID                            | `integer`   |     | ✅    |                            |
| `issued_date`                       | Issued Date                   | `datetime`  | ✅  |       |                            |
| `late_submission_id`                | Late Submission Criteria      | `many2one`  |     | ✅    | late.submission            |
| `lock_change`                       | Lock Change                   | `boolean`   |     |       |                            |
| `marks`                             | Marks                         | `float`     |     | ✅    |                            |
| `mark_update`                       | Mark Update                   | `boolean`   |     | ✅    |                            |
| `max_attempt`                       | Max Attempt                   | `integer`   |     | ✅    |                            |
| `message_attachment_count`          | Attachment Count              | `integer`   |     |       |                            |
| `message_follower_ids`              | Followers                     | `one2many`  |     | ✅    | mail.followers             |
| `message_has_error`                 | Message Delivery error        | `boolean`   |     |       |                            |
| `message_has_error_counter`         | Number of errors              | `integer`   |     |       |                            |
| `message_has_sms_error`             | SMS Delivery error            | `boolean`   |     |       |                            |
| `message_ids`                       | Messages                      | `one2many`  |     | ✅    | mail.message               |
| `message_is_follower`               | Is Follower                   | `boolean`   |     |       |                            |
| `message_needaction`                | Action Needed                 | `boolean`   |     |       |                            |
| `message_needaction_counter`        | Number of Actions             | `integer`   |     |       |                            |
| `message_partner_ids`               | Followers (Partners)          | `many2many` |     |       | res.partner                |
| `my_activity_date_deadline`         | My Activity Deadline          | `date`      |     |       |                            |
| `name`                              | Name                          | `char`      | ✅  |       |                            |
| `point`                             | Points                        | `float`     |     |       |                            |
| `points_validation_status`          | Points Validation Status      | `selection` |     | ✅    |                            |
| `rating_ids`                        | Ratings                       | `one2many`  |     | ✅    | rating.rating              |
| `reviewer`                          | Reviewer                      | `many2one`  |     | ✅    | op.faculty                 |
| `rubric_template_id`                | Rubrics Template              | `many2one`  |     | ✅    | op.rubric.template         |
| `sequence`                          | Index                         | `char`      | ✅  |       |                            |
| `stage_id`                          | Stage                         | `many2one`  |     |       | assignment.stage           |
| `state`                             | Status                        | `selection` | ✅  | ✅    |                            |
| `subject_id`                        | Subject                       | `many2one`  |     |       | op.subject                 |
| `submission_date`                   | Submission Date               | `datetime`  | ✅  | ✅    |                            |
| `term_id`                           | Term                          | `many2one`  |     |       | op.academic.term           |
| `user_id`                           | User                          | `many2one`  | ✅  |       | res.users                  |
| `website_message_ids`               | Website Messages              | `one2many`  |     | ✅    | mail.message               |
| `write_date`                        | Last Updated on               | `datetime`  |     | ✅    |                            |
| `write_uid`                         | Last Updated by               | `many2one`  |     | ✅    | res.users                  |
| `year_id`                           | Academic Year                 | `many2one`  |     |       | op.academic.year           |

**Access Rights:**

| Name                  | Group                | Perms     |
| --------------------- | -------------------- | --------- |
| op_assignment_student | Assignment / Manager | `R/W/C/D` |
| op_assignment_user    | Assignment / User    | `R/W/C/D` |
| op_assignment_portal  | Role / Portal        | `R/W/C`   |

**Record Rules:**

- **User Assignment rule** (103) `R/W/C/D`
  - Domain: `[('faculty_id.user_id','=',user.id)]`
- **Manager Assignment rule** (104) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Assignment multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `copo.lines` — CO-PO Lines

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
| `academic_term_id`           | Academic Term          | `many2one`  |     | ✅    | op.academic.term |
| `academic_year_id`           | Academic Year          | `many2one`  |     | ✅    | op.academic.year |
| `co_id`                      | Course Outcome         | `many2one`  | ✅  | ✅    | course.outcome   |
| `copo_map_id`                | COPO Map               | `many2one`  |     | ✅    | copo.map         |
| `course_plan_id`             | Course Plan            | `many2one`  |     | ✅    | op.course.plan   |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                  |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users        |
| `display_name`               | Display Name           | `char`      |     |       |                  |
| `has_message`                | Has Message            | `boolean`   |     |       |                  |
| `id`                         | ID                     | `integer`   |     | ✅    |                  |
| `mapping_weight`             | Mapping Weight         | `selection` | ✅  | ✅    |                  |
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
| `po_ids`                     | Program Outcomes       | `many2many` | ✅  | ✅    | program.outcome  |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating    |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message     |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                  |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                                | Group                | Perms     |
| ----------------------------------- | -------------------- | --------- |
| access_copo_lines_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_copo_lines_faculty           | OpenEduCat / User    | `R/W/C`   |

### 🗃️ `copo.map` — CO-PO Mapping

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
| `academic_year_id`           | Academic Year          | `many2one`  |     | ✅    | op.academic.year |
| `copo_line_ids`              | CO PO Lines            | `one2many`  |     | ✅    | copo.lines       |
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
| `program_id`                 | Program                | `many2one`  |     | ✅    | op.program       |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating    |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message     |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                  |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                              | Group                | Perms     |
| --------------------------------- | -------------------- | --------- |
| access_copo_map_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_copo_map_faculty           | OpenEduCat / User    | `R/W/C`   |

### 🗃️ `course.outcome` — Course Outcome

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
| `academic_term_id`           | Academic Term          | `many2one`  |     | ✅    | op.academic.term |
| `academic_year_id`           | Academic Year          | `many2one`  |     | ✅    | op.academic.year |
| `co_code`                    | CO Code                | `char`      | ✅  | ✅    |                  |
| `course_id`                  | Course                 | `many2one`  |     | ✅    | op.course        |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                  |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users        |
| `description`                | Description            | `text`      |     | ✅    |                  |
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
| `subject_id`                 | Subject                | `many2one`  |     | ✅    | op.subject       |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message     |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                  |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                                    | Group                | Perms     |
| --------------------------------------- | -------------------- | --------- |
| access_course_outcome_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_course_outcome_faculty           | OpenEduCat / User    | `R/W/C`   |

### 🗃️ `op.course.plan` — Course Plan

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                   | Type        | Req | Store | Relation           |
| ---------------------------- | ----------------------- | ----------- | --- | ----- | ------------------ |
| `academic_plan_id`           | Academic Plan           | `many2one`  |     | ✅    | op.academic.plan   |
| `academic_term_id`           | Academic Term           | `many2one`  | ✅  | ✅    | op.academic.term   |
| `copo_line_ids`              | CO PO Lines             | `one2many`  |     | ✅    | copo.lines         |
| `copo_lines_count`           | CO PO Lines Count       | `integer`   |     |       |                    |
| `course_credit`              | Course Credit           | `one2many`  |     | ✅    | course.credit      |
| `course_id`                  | Course                  | `many2one`  | ✅  | ✅    | op.course          |
| `course_ids`                 | Courses                 | `many2many` |     | ✅    | op.course          |
| `create_date`                | Created on              | `datetime`  |     | ✅    |                    |
| `create_uid`                 | Created by              | `many2one`  |     | ✅    | res.users          |
| `display_name`               | Display Name            | `char`      |     |       |                    |
| `fees_term_id`               | Fees Term               | `many2one`  |     | ✅    | op.fees.terms      |
| `has_message`                | Has Message             | `boolean`   |     |       |                    |
| `id`                         | ID                      | `integer`   |     | ✅    |                    |
| `message_attachment_count`   | Attachment Count        | `integer`   |     |       |                    |
| `message_follower_ids`       | Followers               | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`          | Message Delivery error  | `boolean`   |     |       |                    |
| `message_has_error_counter`  | Number of errors        | `integer`   |     |       |                    |
| `message_has_sms_error`      | SMS Delivery error      | `boolean`   |     |       |                    |
| `message_ids`                | Messages                | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`        | Is Follower             | `boolean`   |     |       |                    |
| `message_needaction`         | Action Needed           | `boolean`   |     |       |                    |
| `message_needaction_counter` | Number of Actions       | `integer`   |     |       |                    |
| `message_partner_ids`        | Followers (Partners)    | `many2many` |     |       | res.partner        |
| `name`                       | Name                    | `char`      |     |       |                    |
| `rating_ids`                 | Ratings                 | `one2many`  |     | ✅    | rating.rating      |
| `subject_configure_count`    | Subject Configure Count | `integer`   |     |       |                    |
| `subject_faculty_line`       | Configure Subjects      | `one2many`  |     | ✅    | op.subject.faculty |
| `website_message_ids`        | Website Messages        | `one2many`  |     | ✅    | mail.message       |
| `write_date`                 | Last Updated on         | `datetime`  |     | ✅    |                    |
| `write_uid`                  | Last Updated by         | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                    | Group                | Perms     |
| --------------------------------------- | -------------------- | --------- |
| access_op_course_plan_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_op_course_plan_faculty           | OpenEduCat / User    | `R/W`     |

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

### 🗃️ `program.outcome` — Program Outcome

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
| `academic_term_id`           | Academic Term          | `many2one`  |     | ✅    | op.academic.term |
| `academic_year_id`           | Academic Year          | `many2one`  |     | ✅    | op.academic.year |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                  |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users        |
| `description`                | Description            | `text`      |     | ✅    |                  |
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
| `name`                       | PO Name                | `char`      | ✅  | ✅    |                  |
| `po_code`                    | PO Code                | `char`      | ✅  | ✅    |                  |
| `program_id`                 | Program                | `many2one`  |     | ✅    | op.program       |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating    |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message     |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                  |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                                     | Group                | Perms     |
| ---------------------------------------- | -------------------- | --------- |
| access_program_outcome_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_program_outcome_faculty           | OpenEduCat / User    | `R/W/C`   |

### 🗃️ `student.attainment` — Student Attainment

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                  | Type        | Req | Store | Relation              |
| ----------------------------- | ---------------------- | ----------- | --- | ----- | --------------------- |
| `academic_year_id`            | Academic Year          | `many2one`  |     | ✅    | op.academic.year      |
| `co_attainment_ids`           | CO Attainments         | `one2many`  |     | ✅    | student.co.attainment |
| `course_id`                   | Course                 | `many2one`  |     | ✅    | op.course             |
| `create_date`                 | Created on             | `datetime`  |     | ✅    |                       |
| `create_uid`                  | Created by             | `many2one`  |     | ✅    | res.users             |
| `display_name`                | Display Name           | `char`      |     |       |                       |
| `has_message`                 | Has Message            | `boolean`   |     |       |                       |
| `id`                          | ID                     | `integer`   |     | ✅    |                       |
| `message_attachment_count`    | Attachment Count       | `integer`   |     |       |                       |
| `message_follower_ids`        | Followers              | `one2many`  |     | ✅    | mail.followers        |
| `message_has_error`           | Message Delivery error | `boolean`   |     |       |                       |
| `message_has_error_counter`   | Number of errors       | `integer`   |     |       |                       |
| `message_has_sms_error`       | SMS Delivery error     | `boolean`   |     |       |                       |
| `message_ids`                 | Messages               | `one2many`  |     | ✅    | mail.message          |
| `message_is_follower`         | Is Follower            | `boolean`   |     |       |                       |
| `message_needaction`          | Action Needed          | `boolean`   |     |       |                       |
| `message_needaction_counter`  | Number of Actions      | `integer`   |     |       |                       |
| `message_partner_ids`         | Followers (Partners)   | `many2many` |     |       | res.partner           |
| `overall_attainment`          | Overall Attainment     | `float`     |     | ✅    |                       |
| `po_attainment`               | PO Attainment          | `float`     |     | ✅    |                       |
| `program_id`                  | Program                | `many2one`  | ✅  | ✅    | op.program            |
| `rating_ids`                  | Ratings                | `one2many`  |     | ✅    | rating.rating         |
| `student_id`                  | Student                | `many2one`  | ✅  | ✅    | op.student            |
| `_virtual_co_attainment_data` | Virtual CO Data        | `char`      |     | ✅    |                       |
| `website_message_ids`         | Website Messages       | `one2many`  |     | ✅    | mail.message          |
| `write_date`                  | Last Updated on        | `datetime`  |     | ✅    |                       |
| `write_uid`                   | Last Updated by        | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                                        | Group                | Perms     |
| ------------------------------------------- | -------------------- | --------- |
| access_student_attainment_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_student_attainment_faculty           | OpenEduCat / User    | `R/W/C`   |

### 🗃️ `assignment.co` — Assignment CO

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label            | Type       | Req | Store | Relation       |
| --------------- | ---------------- | ---------- | --- | ----- | -------------- |
| `assignment_id` | Assignment       | `many2one` |     | ✅    | op.assignment  |
| `co_id`         | CO               | `many2one` |     | ✅    | course.outcome |
| `create_date`   | Created on       | `datetime` |     | ✅    |                |
| `create_uid`    | Created by       | `many2one` |     | ✅    | res.users      |
| `display_name`  | Display Name     | `char`     |     |       |                |
| `id`            | ID               | `integer`  |     | ✅    |                |
| `weightage`     | CO Weightage (%) | `float`    |     | ✅    |                |
| `write_date`    | Last Updated on  | `datetime` |     | ✅    |                |
| `write_uid`     | Last Updated by  | `many2one` |     | ✅    | res.users      |

**Access Rights:**

| Name                                   | Group                | Perms     |
| -------------------------------------- | -------------------- | --------- |
| access_assignment_co_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_assignment_co_faculty           | OpenEduCat / User    | `R/W/C`   |

### 🗃️ `attainment.dashboard.record` — Attainment Dashboard Record

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label              | Type       | Req | Store | Relation   |
| -------------------- | ------------------ | ---------- | --- | ----- | ---------- |
| `co_attainment`      | CO Attainment      | `float`    |     | ✅    |            |
| `course_id`          | Course             | `many2one` |     | ✅    | op.course  |
| `create_date`        | Created on         | `datetime` |     | ✅    |            |
| `create_uid`         | Created by         | `many2one` |     | ✅    | res.users  |
| `display_name`       | Display Name       | `char`     |     |       |            |
| `id`                 | ID                 | `integer`  |     | ✅    |            |
| `overall_attainment` | Overall Attainment | `float`    |     | ✅    |            |
| `po_attainment`      | PO Attainment      | `float`    |     | ✅    |            |
| `program_id`         | Program            | `many2one` |     | ✅    | op.program |
| `student_id`         | Student            | `many2one` |     | ✅    | op.student |
| `write_date`         | Last Updated on    | `datetime` |     | ✅    |            |
| `write_uid`          | Last Updated by    | `many2one` |     | ✅    | res.users  |

**Access Rights:**

| Name                                                 | Group                | Perms     |
| ---------------------------------------------------- | -------------------- | --------- |
| access_attainment_dashboard_record_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_attainment_dashboard_record_faculty           | OpenEduCat / User    | `R/W/C`   |

### 🗃️ `student.co.attainment` — Student CO Attainment

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                   | Label               | Type       | Req | Store | Relation           |
| ----------------------- | ------------------- | ---------- | --- | ----- | ------------------ |
| `attainment_score`      | CO Attainment Score | `float`    |     | ✅    |                    |
| `co_id`                 | Course Outcome      | `many2one` | ✅  | ✅    | course.outcome     |
| `create_date`           | Created on          | `datetime` |     | ✅    |                    |
| `create_uid`            | Created by          | `many2one` |     | ✅    | res.users          |
| `display_name`          | Display Name        | `char`     |     |       |                    |
| `id`                    | ID                  | `integer`  |     | ✅    |                    |
| `student_attainment_id` | Student Attainment  | `many2one` |     | ✅    | student.attainment |
| `term_ids`              | Academic Terms      | `many2one` |     |       | op.academic.term   |
| `write_date`            | Last Updated on     | `datetime` |     | ✅    |                    |
| `write_uid`             | Last Updated by     | `many2one` |     | ✅    | res.users          |

**Access Rights:**

| Name                                           | Group                | Perms     |
| ---------------------------------------------- | -------------------- | --------- |
| access_student_co_attainment_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_student_co_attainment_faculty           | OpenEduCat / User    | `R/W/C`   |
