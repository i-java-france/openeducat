---
title: "Openeducat Assignment Grading Bridge"
module: "openeducat_assignment_grading_bridge"
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

# 🟢 Openeducat Assignment Grading Bridge

> **Module:** `openeducat_assignment_grading_bridge` | **Version:** `19.0.1.0`
> **Category:** Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc
> **Website:** https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_assignment]] [[openeducat_grading]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `Assignments/Configuration/Late Submission`

### Views

- `* INHERIT gradebook.line.inherited.form (form)`
- `* INHERIT gradebook.line.inherited.list (list)`
- `* INHERIT op.assignment.inherited.form (form)`
- `* INHERIT op.assignment.inherited.list (list)`
- `* INHERIT op.assignment.sub.line.inherited.form (form)`
- `* INHERIT op.assignment.sub.line.inherited.list (list)`
- `* INHERIT portal_submited_assignment_score (qweb)`
- `late.submission.form (form)`
- `late.submission.line.form (form)`
- `late.submission.line.search (search)`
- `late.submission.list (list)`
- `late.submission.search (search)`
- `late.sunbmission.line.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**5 model(s) defined by this module:**

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

### 🗃️ `op.assignment.sub.line` — Assignment Submission

> 📧 Mail Thread

Model for managing assignment submission lines with rubric assessment.

    This model extends the base assignment submission line to include rubric-based
    assessment functionality. It handles the creation and management of rubric
    elements, assessment attempts, and final scoring.

**Fields:**

| Field                           | Label                    | Type        | Req | Store | Relation                      |
| ------------------------------- | ------------------------ | ----------- | --- | ----- | ----------------------------- |
| `active`                        | Active                   | `boolean`   |     | ✅    |                               |
| `assessment_attempt_line`       | Assessment Attempts Line | `one2many`  |     | ✅    | op.assessment.attempt         |
| `assessment_attempt_line_count` | Assessment Attempts      | `integer`   |     |       |                               |
| `assignment_id`                 | Assignment               | `many2one`  | ✅  | ✅    | op.assignment                 |
| `attachment_ids`                | Attachments              | `one2many`  |     | ✅    | ir.attachment                 |
| `company_id`                    | Company                  | `many2one`  |     | ✅    | res.company                   |
| `create_date`                   | Created on               | `datetime`  |     | ✅    |                               |
| `create_uid`                    | Created by               | `many2one`  |     | ✅    | res.users                     |
| `data`                          | Attachment Data          | `binary`    |     |       |                               |
| `data_filename`                 | Filename                 | `char`      |     |       |                               |
| `description`                   | Description              | `text`      |     | ✅    |                               |
| `display_name`                  | Display Name             | `char`      |     |       |                               |
| `evaluation_boolean`            | Evaluation Boolean       | `boolean`   |     |       |                               |
| `faculty_user_id`               | Faculty User             | `many2one`  |     |       | res.users                     |
| `feedback_data`                 | Feedback                 | `binary`    |     | ✅    |                               |
| `feedback_data_json`            | Feedback json            | `text`      |     | ✅    |                               |
| `final_assessment_id`           | Final Assessment         | `many2one`  |     | ✅    | final.assessment.selection    |
| `grades_id`                     | Grades                   | `many2one`  |     | ✅    | op.assign.grade.config        |
| `grade_table_id`                | Grade                    | `many2one`  |     | ✅    | op.grade.table                |
| `grade_table_line_id`           | Grade                    | `many2one`  |     | ✅    | op.grade.table.line           |
| `has_message`                   | Has Message              | `boolean`   |     |       |                               |
| `hide_grade`                    | Hide Grade               | `boolean`   |     |       |                               |
| `id`                            | ID                       | `integer`   |     | ✅    |                               |
| `ignore`                        | Ignore                   | `boolean`   |     | ✅    |                               |
| `ignore_attempt`                | Ignore Attempt           | `integer`   |     | ✅    |                               |
| `last_attempt_score`            | Last Attempt Score       | `char`      |     | ✅    |                               |
| `late_submit`                   | Late Submission          | `boolean`   |     |       |                               |
| `marks`                         | Given Marks              | `float`     |     | ✅    |                               |
| `message_attachment_count`      | Attachment Count         | `integer`   |     |       |                               |
| `message_follower_ids`          | Followers                | `one2many`  |     | ✅    | mail.followers                |
| `message_has_error`             | Message Delivery error   | `boolean`   |     |       |                               |
| `message_has_error_counter`     | Number of errors         | `integer`   |     |       |                               |
| `message_has_sms_error`         | SMS Delivery error       | `boolean`   |     |       |                               |
| `message_ids`                   | Messages                 | `one2many`  |     | ✅    | mail.message                  |
| `message_is_follower`           | Is Follower              | `boolean`   |     |       |                               |
| `message_needaction`            | Action Needed            | `boolean`   |     |       |                               |
| `message_needaction_counter`    | Number of Actions        | `integer`   |     |       |                               |
| `message_partner_ids`           | Followers (Partners)     | `many2many` |     |       | res.partner                   |
| `name`                          | Submission               | `char`      |     |       |                               |
| `note`                          | Note                     | `text`      |     | ✅    |                               |
| `obtained_mark`                 | Obtained Marks           | `float`     |     | ✅    |                               |
| `penalty`                       | Penalty %                | `float`     |     | ✅    |                               |
| `progression_id`                | Progression No           | `many2one`  |     | ✅    | op.student.progression        |
| `rating_ids`                    | Ratings                  | `one2many`  |     | ✅    | rating.rating                 |
| `rubric_element_line`           | Rubrics Elements         | `one2many`  | ✅  | ✅    | op.assignment.rubric.sub.line |
| `rubric_template_id`            | Rubric Template          | `many2one`  |     |       | op.rubric.template            |
| `rubric_type`                   | Rubrics Type             | `selection` |     |       |                               |
| `state`                         | Status                   | `selection` |     | ✅    |                               |
| `student_id`                    | Student                  | `many2one`  | ✅  | ✅    | op.student                    |
| `submission_date`               | Submission Date          | `datetime`  | ✅  | ✅    |                               |
| `user_boolean`                  | Check user               | `boolean`   |     |       |                               |
| `user_id`                       | User                     | `many2one`  |     |       | res.users                     |
| `website_message_ids`           | Website Messages         | `one2many`  |     | ✅    | mail.message                  |
| `write_date`                    | Last Updated on          | `datetime`  |     | ✅    |                               |
| `write_uid`                     | Last Updated by          | `many2one`  |     | ✅    | res.users                     |

**Access Rights:**

| Name                                 | Group                | Perms     |
| ------------------------------------ | -------------------- | --------- |
| op_assignment_sub_line_student       | Assignment / Manager | `R/W/C/D` |
| op_assignment_sub_line_user          | Assignment / User    | `R/W/C`   |
| access_op_assignment_sub_line_portal | Role / Portal        | `R/W/C`   |

**Record Rules:**

- **Student Assignment Submission Line Rule** (104) `R/W/C/D`
  - Domain:
    `['|', ('student_id.user_id','=',user.id), ('student_id.user_id','in',         user.child_ids.ids)]     `
- **User Assignment Submission Line Rule** (103) `R/W/C/D`
  - Domain: `[('assignment_id.faculty_id.user_id','=',user.id)]`
- **Manager Assignment Submission Line Rule** (104) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Assignment Sub Line multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `gradebook.line` — Grade Book Line

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation                |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ----------------------- |
| `academic_term_id`           | Term                   | `many2one`  | ✅  | ✅    | op.academic.term        |
| `academic_year_id`           | Academic Year          | `many2one`  | ✅  | ✅    | op.academic.year        |
| `assignment_archived`        | Assignment Archived    | `boolean`   |     | ✅    |                         |
| `assignment_type_id`         | Assignment Type        | `many2one`  | ✅  | ✅    | grading.assignment.type |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company             |
| `course_id`                  | Course                 | `many2one`  | ✅  | ✅    | op.course               |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                         |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users               |
| `display_name`               | Display Name           | `char`      |     |       |                         |
| `grade_assigment_id`         | Assignment             | `many2one`  | ✅  | ✅    | grading.assignment      |
| `gradebook_id`               | Student                | `many2one`  |     | ✅    | gradebook.gradebook     |
| `grade_table_id`             | Grade Table            | `many2one`  |     | ✅    | op.grade.table          |
| `grade_table_line_id`        | Grade Table Line       | `many2one`  |     | ✅    | op.grade.table.line     |
| `has_message`                | Has Message            | `boolean`   |     |       |                         |
| `hide`                       | Hide                   | `boolean`   |     |       |                         |
| `hide_sub`                   | Hide Sub               | `boolean`   |     |       |                         |
| `id`                         | ID                     | `integer`   |     | ✅    |                         |
| `marks`                      | Given Marks            | `float`     |     | ✅    |                         |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                         |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers          |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                         |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                         |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                         |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message            |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                         |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                         |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                         |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner             |
| `obtained_marks`             | Obtained Mark          | `float`     |     | ✅    |                         |
| `penalty`                    | Penalty %              | `float`     |     | ✅    |                         |
| `percentage`                 | Percentage             | `float`     |     | ✅    |                         |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating           |
| `state`                      | State                  | `selection` |     | ✅    |                         |
| `state_hide`                 | State Hide             | `boolean`   |     | ✅    |                         |
| `subject_id`                 | Subject                | `many2one`  |     | ✅    | op.subject              |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message            |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                         |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name                                    | Group             | Perms     |
| --------------------------------------- | ----------------- | --------- |
| access_gradebook_line_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_gradebook_line_faculty           | Grading / User    | `R/W/C`   |

**Record Rules:**

- **Gradebook Line multi company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `late.submission` — Late Submission

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label           | Type       | Req | Store | Relation             |
| --------------- | --------------- | ---------- | --- | ----- | -------------------- |
| `company_id`    | Company         | `many2one` |     | ✅    | res.company          |
| `create_date`   | Created on      | `datetime` |     | ✅    |                      |
| `create_uid`    | Created by      | `many2one` |     | ✅    | res.users            |
| `display_name`  | Display Name    | `char`     |     |       |                      |
| `id`            | ID              | `integer`  |     | ✅    |                      |
| `late_sub_line` | Late Submission | `one2many` |     | ✅    | late.submission.line |
| `name`          | Name            | `char`     | ✅  | ✅    |                      |
| `write_date`    | Last Updated on | `datetime` |     | ✅    |                      |
| `write_uid`     | Last Updated by | `many2one` |     | ✅    | res.users            |

**Access Rights:**

| Name                           | Group                | Perms     |
| ------------------------------ | -------------------- | --------- |
| access_late_submission_manager | Assignment / Manager | `R/W/C/D` |
| access_late_submission_user    | Assignment / User    | `R`       |

**Record Rules:**

- **Late Submission Multi Comp Rule** (Global) `R/W/C/D`
  - Domain:
    `['|','|',('company_id','=',False),('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids),('company_id','in', company_ids)]`

### 🗃️ `late.submission.line` — Late Submission Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label           | Type        | Req | Store | Relation        |
| -------------------- | --------------- | ----------- | --- | ----- | --------------- |
| `create_date`        | Created on      | `datetime`  |     | ✅    |                 |
| `create_uid`         | Created by      | `many2one`  |     | ✅    | res.users       |
| `display_name`       | Display Name    | `char`      |     |       |                 |
| `id`                 | ID              | `integer`   |     | ✅    |                 |
| `late_submission_id` | Late Submission | `many2one`  |     | ✅    | late.submission |
| `no_of_days`         | Days            | `float`     |     | ✅    |                 |
| `penalty`            | Penalty(%)      | `float`     |     | ✅    |                 |
| `penalty_type`       | Penalty Type    | `selection` |     | ✅    |                 |
| `write_date`         | Last Updated on | `datetime`  |     | ✅    |                 |
| `write_uid`          | Last Updated by | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                                | Group                | Perms     |
| ----------------------------------- | -------------------- | --------- |
| access_late_submission_line_manager | Assignment / Manager | `R/W/C/D` |
| access_late_submission_line_user    | Assignment / User    | `R`       |
