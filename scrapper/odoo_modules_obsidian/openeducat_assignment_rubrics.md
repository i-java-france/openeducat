---
title: "OpenEduCat Assignment Rubrics Enterprise"
module: "openeducat_assignment_rubrics"
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

# 🟢 OpenEduCat Assignment Rubrics Enterprise

> **Module:** `openeducat_assignment_rubrics` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_assignment_enterprise]] [[mail]]

## 📖 Description

## OpenEduCat Assignment Rubrics

### Advanced Rubric-Based Assignment Assessment

[![](/openeducat_assignment_rubrics/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module provides a comprehensive rubric-based assessment system for assignments.
Faculty can create detailed rubrics templates with point-based or percentage-based
scoring, ensuring consistent and fair evaluation of student submissions.

[Contact Us](https://www.openeducat.org/contactus/)

## Smart Rubrics Template Creation

- Create detailed rubric templates with multiple assessment criteria
- Choose between point-based or percentage-based scoring
- Real-time validation of percentage distribution
- Visual feedback on rubric completeness
- Template state management (Draft, In Use, Cancelled)

![](/openeducat_assignment_rubrics/static/description/template_creation.png)

## Intelligent Element Management

![](/openeducat_assignment_rubrics/static/description/element_creation.png)

- Create detailed assessment elements with clear criteria
- Automatic validation of percentage distribution
- Visual indicators for valid/invalid distributions
- Multiple levels of assessment for each element
- Detailed feedback options for each level

## Smart Validation System

- Real-time validation of rubric completeness
- Color-coded status indicators for easy monitoring
- Automatic percentage validation for percentage-based rubrics
- Prevents template activation if validation fails
- Clear error messages for quick resolution

![](/openeducat_assignment_rubrics/static/description/in_use_template.png)

## Streamlined Assignment Management

![](/openeducat_assignment_rubrics/static/description/assignment_creation.png)

- Easy assignment creation with rubric templates
- Automatic rubric element assignment
- Multiple submission attempts tracking
- Best attempt selection for final grading
- Comprehensive submission management

## Advanced Grading System

- Structured grading based on rubric criteria
- Automatic total calculation
- Detailed feedback for each criterion
- Multiple attempt management
- Final grade selection based on best attempt

![](/openeducat_assignment_rubrics/static/description/assignment_submission.png)

## Key Features

### Smart Validation

Real-time validation of rubric completeness with visual feedback

### Flexible Scoring

Support for both point-based and percentage-based assessment

### Multiple Attempts

Track and manage multiple submission attempts with best attempt selection

### Detailed Feedback

Provide comprehensive feedback at multiple levels

### State Management

Complete lifecycle management of rubric templates

### Easy Integration

Seamless integration with existing assignment system

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Assignments/Configuration/Rubrics Level`
- `Assignments/Configuration/Rubrics Template`

### Views

- `* INHERIT Assignment Rubrics (qweb)`
- `* INHERIT op.assignment.inherit.form (form)`
- `* INHERIT op.assignment.sub.line.inherit.form (form)`
- `* INHERIT portal_student_submit_assignment_data_inherit (qweb)`
- `* INHERIT rubrics.op.assignment.sub.line.inherited.tree.view (list)`
- `* INHERIT student_progression_assignment_status_patch (qweb)`
- `op.assessment.attempt.form (form)`
- `op.assessment.attempt.list (list)`
- `op.assignment.rubric.level.sub.line.form (form)`
- `op.assignment.rubric.level.sub.line.list (list)`
- `op.assignment.rubric.sub.line.form (form)`
- `op.assignment.rubric.sub.line.list (list)`
- `op.assignment.sub.line.pdf.view (form)`
- `op.rubric.element.assessment.line.form (form)`
- `op.rubric.element.assessment.line.list (list)`
- `op.rubric.element.form (form)`
- `op.rubric.element.level.form (form)`
- `op.rubric.element.level.list (list)`
- `op.rubric.element.list (list)`
- `op.rubric.level.form (form)`
- `op.rubric.level.list (list)`
- `op.rubric.template.form (form)`
- `op.rubric.template.list (list)`

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

### 🗃️ `op.rubric.template` — Rubrics Template Configuration

> 📧 Mail Thread

Model for managing rubric templates.

    This model handles the configuration of rubric templates, including:
    - Template elements and their scoring
    - Template state management
    - Company-specific templates

    The template can be in different states:
    - Draft: Initial state, can be edited
    - In Use: Active and being used
    - Cancelled: No longer in use
    - Re-open: Reopened for editing
    - Expired: No longer valid for new assessments

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation           |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------ |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event     |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                    |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                    |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                    |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity      |
| `activity_state`                | Activity State                | `selection` |     |       |                    |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                    |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                    |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users          |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company        |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `email_cc`                      | Email cc                      | `char`      |     | ✅    |                    |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                    |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                    |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                    |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                    |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                    |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                    |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                    |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner        |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                    |
| `name`                          | Name                          | `char`      | ✅  | ✅    |                    |
| `points_validation_status`      | Validation Status             | `selection` |     | ✅    |                    |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `rubric_element_line`           | Rubrics Elements              | `one2many`  |     | ✅    | op.rubric.element  |
| `rubrics_type`                  | Rubrics Type                  | `selection` | ✅  | ✅    |                    |
| `state`                         | Status                        | `selection` |     | ✅    |                    |
| `template_expired`              | Template Expired              | `boolean`   |     | ✅    |                    |
| `template_expired_by`           | Expired By                    | `many2one`  |     | ✅    | res.users          |
| `template_expired_date`         | Expired Date                  | `datetime`  |     | ✅    |                    |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                      | Group             | Perms     |
| ------------------------- | ----------------- | --------- |
| op_rubric_template_user   | Assignment / User | `R/W/C/D` |
| access_op_rubric_template | Role / User       | `R`       |

**Record Rules:**

- **Op Rubric Template Multi Comp Rule** (Global) `R/W/C/D`
  - Domain:
    `['|','|',('company_id','=',False),('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids),('company_id','in', company_ids)]`

### 🗃️ `op.assessment.attempt` — Assessment Attempt

    Assessment Attempt Model

    This model represents an attempt to assess a student's assignment submission.
    It tracks the assessment process, scores, and feedback for each attempt.

    Fields:
        name: Computed field that generates a unique name for each attempt
        assignment_sub_line_id: Reference to the assignment submission being assessed
        assessment_by: The user who performed the assessment
        assessment_date: When the assessment was performed
        assessment_score: Score calculated based on rubrics
        final_score: Final score after review
        feedback: Overall feedback for the attempt
        rubric_template_id: The rubric template used for assessment
        rubric_element_assessment_line: Detailed assessment of each rubric element

**Fields:**

| Field                            | Label                            | Type       | Req | Store | Relation                          |
| -------------------------------- | -------------------------------- | ---------- | --- | ----- | --------------------------------- |
| `assessment_by`                  | Assessment By                    | `many2one` |     | ✅    | res.users                         |
| `assessment_date`                | Assessment Date                  | `datetime` |     | ✅    |                                   |
| `assessment_score`               | Assessment Score                 | `float`    |     | ✅    |                                   |
| `assignment_sub_line_id`         | Assignment                       | `many2one` | ✅  | ✅    | op.assignment.sub.line            |
| `create_date`                    | Created on                       | `datetime` |     | ✅    |                                   |
| `create_uid`                     | Created by                       | `many2one` |     | ✅    | res.users                         |
| `display_name`                   | Display Name                     | `char`     |     |       |                                   |
| `feedback`                       | Overall Feedback                 | `text`     |     | ✅    |                                   |
| `final_score`                    | Final Score                      | `float`    |     | ✅    |                                   |
| `id`                             | ID                               | `integer`  |     | ✅    |                                   |
| `name`                           | Name                             | `char`     |     | ✅    |                                   |
| `rubric_element_assessment_line` | Rubrics Elements Assessment Line | `one2many` |     | ✅    | op.rubric.element.assessment.line |
| `rubric_template_id`             | Rubrics Template                 | `many2one` |     | ✅    | op.rubric.template                |
| `write_date`                     | Last Updated on                  | `datetime` |     | ✅    |                                   |
| `write_uid`                      | Last Updated by                  | `many2one` |     | ✅    | res.users                         |

**Access Rights:**

| Name                         | Group       | Perms     |
| ---------------------------- | ----------- | --------- |
| access_op_assessment_attempt | Role / User | `R/W/C/D` |

### 🗃️ `final.assessment.selection` — Final Assessment Selection

    Final Assessment Selection Model

    This model manages the selection of the final assessment attempt for a submission.
    It allows choosing between different attempts (best, worst, first, last) and
    maintains the final assessment details.

    Fields:
        submission_id: Reference to the assignment submission
        assessement_selection: Method used to select the final attempt
        final_attempt_id: The selected assessment attempt
        reviewer_id: User who made the final selection
        final_assessment_date: When the final assessment was made
        final_score: Final score from the selected attempt
        feedback: Final feedback from the selected attempt

**Fields:**

| Field                   | Label                 | Type        | Req | Store | Relation               |
| ----------------------- | --------------------- | ----------- | --- | ----- | ---------------------- |
| `assessement_selection` | Selected Attempt      | `selection` | ✅  | ✅    |                        |
| `create_date`           | Created on            | `datetime`  |     | ✅    |                        |
| `create_uid`            | Created by            | `many2one`  |     | ✅    | res.users              |
| `display_name`          | Display Name          | `char`      |     |       |                        |
| `feedback`              | Final Feedback        | `text`      |     | ✅    |                        |
| `final_assessment_date` | Final Assessment Date | `datetime`  |     | ✅    |                        |
| `final_attempt_id`      | Final Attempt         | `many2one`  |     | ✅    | op.assessment.attempt  |
| `final_score`           | Final Score           | `float`     |     | ✅    |                        |
| `id`                    | ID                    | `integer`   |     | ✅    |                        |
| `reviewer_id`           | Reviewer              | `many2one`  |     | ✅    | res.users              |
| `submission_id`         | Submission            | `many2one`  | ✅  | ✅    | op.assignment.sub.line |
| `write_date`            | Last Updated on       | `datetime`  |     | ✅    |                        |
| `write_uid`             | Last Updated by       | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                              | Group       | Perms     |
| --------------------------------- | ----------- | --------- |
| access_final_assessment_selection | Role / User | `R/W/C/D` |

### 🗃️ `op.rubric.element.assessment.line` — Rubric Element Assessment Line

    Rubric Element Assessment Line Model

    This model represents the assessment of individual rubric elements for an attempt.
    It stores the scores and feedback for each element of the rubric.

    Fields:
        name: Computed field that generates a unique name for each assessment line
        assessment_attempt_id: Reference to the parent assessment attempt
        rubric_template_id: The rubric template being used
        rubric_type: Type of rubric (from template)
        rubric_element_id: The specific element being assessed
        rubric_level_id: The level achieved for this element
        rubric_level_description: Description of the achieved level
        rubric_element_feedback: Specific feedback for this element
        rubric_level_point: Points awarded for this element
        rubric_level_percentage: Percentage score for this element

**Fields:**

| Field                      | Label              | Type        | Req | Store | Relation              |
| -------------------------- | ------------------ | ----------- | --- | ----- | --------------------- |
| `assessment_attempt_id`    | Assessment Attempt | `many2one`  | ✅  | ✅    | op.assessment.attempt |
| `create_date`              | Created on         | `datetime`  |     | ✅    |                       |
| `create_uid`               | Created by         | `many2one`  |     | ✅    | res.users             |
| `display_name`             | Display Name       | `char`      |     |       |                       |
| `id`                       | ID                 | `integer`   |     | ✅    |                       |
| `name`                     | Name               | `char`      |     | ✅    |                       |
| `out_of`                   | Out Of             | `float`     |     | ✅    |                       |
| `rubric_element_feedback`  | Element Feedback   | `text`      |     | ✅    |                       |
| `rubric_element_id`        | Element            | `many2one`  | ✅  | ✅    | op.rubric.element     |
| `rubric_level_description` | Level Description  | `text`      |     | ✅    |                       |
| `rubric_level_id`          | Level              | `many2one`  | ✅  | ✅    | op.rubric.level       |
| `rubric_level_percentage`  | Level Percentage   | `float`     |     | ✅    |                       |
| `rubric_level_point`       | Level Point        | `float`     |     | ✅    |                       |
| `rubric_template_id`       | Rubrics Template   | `many2one`  |     | ✅    | op.rubric.template    |
| `rubric_type`              | Rubrics Type       | `selection` |     | ✅    |                       |
| `write_date`               | Last Updated on    | `datetime`  |     | ✅    |                       |
| `write_uid`                | Last Updated by    | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                                     | Group       | Perms     |
| ---------------------------------------- | ----------- | --------- |
| access_op_rubric_element_assessment_line | Role / User | `R/W/C/D` |

### 🗃️ `op.rubric.level` — Rubric Level

Model for managing rubric levels.

    This model handles the configuration of rubric levels, including
    their names, sequences, and percentage weights for scoring.

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `is_active`    | Active          | `boolean`  |     | ✅    |           |
| `name`         | Level Name      | `char`     | ✅  | ✅    |           |
| `percentage`   | Percentage      | `float`    |     | ✅    |           |
| `sequence`     | Sequence        | `integer`  | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                   | Group       | Perms     |
| ---------------------- | ----------- | --------- |
| access_op_rubric_level | Role / User | `R/W/C/D` |

### 🗃️ `op.assignment.rubric.level.sub.line` — Rubric Level Sub Line

Model for managing rubric level sublines in assignment submissions.

    This model handles the individual rubric levels and their scoring
    for each rubric element in an assignment submission.

**Fields:**

| Field                          | Label             | Type       | Req | Store | Relation                      |
| ------------------------------ | ----------------- | ---------- | --- | ----- | ----------------------------- |
| `assignment_rubric_subline_id` | Rubric Sub Line   | `many2one` |     | ✅    | op.assignment.rubric.sub.line |
| `create_date`                  | Created on        | `datetime` |     | ✅    |                               |
| `create_uid`                   | Created by        | `many2one` |     | ✅    | res.users                     |
| `display_name`                 | Display Name      | `char`     |     |       |                               |
| `id`                           | ID                | `integer`  |     | ✅    |                               |
| `level_description`            | Level Description | `text`     |     | ✅    |                               |
| `level_id`                     | Level             | `many2one` | ✅  | ✅    | op.rubric.level               |
| `level_percentage`             | Percentage        | `integer`  |     | ✅    |                               |
| `level_points`                 | Points            | `integer`  |     | ✅    |                               |
| `rubric_element_id`            | Element           | `many2one` |     |       | op.rubric.element             |
| `rubric_template_id`           | Rubric Template   | `many2one` |     |       | op.rubric.template            |
| `write_date`                   | Last Updated on   | `datetime` |     | ✅    |                               |
| `write_uid`                    | Last Updated by   | `many2one` |     | ✅    | res.users                     |

**Access Rights:**

| Name                                       | Group       | Perms     |
| ------------------------------------------ | ----------- | --------- |
| access_op_assignment_rubric_level_sub_line | Role / User | `R/W/C/D` |

### 🗃️ `op.rubric.element` — Rubrics Elements Configuration

Model for managing rubric elements configuration.

    This model handles the configuration of individual rubric elements,
    including their scoring type (points or percentage), descriptions,
    and associated levels.

**Fields:**

| Field                       | Label                  | Type        | Req | Store | Relation                |
| --------------------------- | ---------------------- | ----------- | --- | ----- | ----------------------- |
| `create_date`               | Created on             | `datetime`  |     | ✅    |                         |
| `create_uid`                | Created by             | `many2one`  |     | ✅    | res.users               |
| `description`               | FeedBack               | `text`      |     | ✅    |                         |
| `display_name`              | Display Name           | `char`      |     |       |                         |
| `id`                        | ID                     | `integer`   |     | ✅    |                         |
| `name`                      | Name                   | `char`      | ✅  | ✅    |                         |
| `percentage`                | Percentage             | `float`     |     | ✅    |                         |
| `point`                     | Point                  | `float`     |     | ✅    |                         |
| `rubrics_element_level_ids` | Rubrics Elements Level | `one2many`  |     | ✅    | op.rubric.element.level |
| `rubrics_template_id`       | Rubric Template        | `many2one`  |     | ✅    | op.rubric.template      |
| `rubrics_type`              | Rubrics Type           | `selection` |     |       |                         |
| `write_date`                | Last Updated on        | `datetime`  |     | ✅    |                         |
| `write_uid`                 | Last Updated by        | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name                     | Group             | Perms     |
| ------------------------ | ----------------- | --------- |
| op_rubric_element_user   | Assignment / User | `R/W/C/D` |
| access_op_rubric_element | Role / User       | `R`       |

### 🗃️ `op.rubric.element.level` — Rubrics Elements Level Configuration

Model for managing rubric element levels configuration.

    This model handles the configuration of individual levels within
    a rubric element, including their descriptions and sequences.

**Fields:**

| Field          | Label                                      | Type       | Req | Store | Relation          |
| -------------- | ------------------------------------------ | ---------- | --- | ----- | ----------------- |
| `create_date`  | Created on                                 | `datetime` |     | ✅    |                   |
| `create_uid`   | Created by                                 | `many2one` |     | ✅    | res.users         |
| `description`  | Description for this Level in this Element | `text`     |     | ✅    |                   |
| `display_name` | Display Name                               | `char`     |     |       |                   |
| `element_id`   | Rubric Element                             | `many2one` |     | ✅    | op.rubric.element |
| `id`           | ID                                         | `integer`  |     | ✅    |                   |
| `level_id`     | Level                                      | `many2one` | ✅  | ✅    | op.rubric.level   |
| `sequence`     | Sequence                                   | `integer`  |     | ✅    |                   |
| `write_date`   | Last Updated on                            | `datetime` |     | ✅    |                   |
| `write_uid`    | Last Updated by                            | `many2one` |     | ✅    | res.users         |

**Access Rights:**

| Name                           | Group       | Perms     |
| ------------------------------ | ----------- | --------- |
| access_op_rubric_element_level | Role / User | `R/W/C/D` |

### 🗃️ `op.assignment.rubric.sub.line` — Rubric Sub Line

Model for managing rubric sublines in assignment submissions.

    This model handles the individual rubric elements and their scoring
    for each assignment submission.

**Fields:**

| Field                      | Label                  | Type        | Req | Store | Relation                            |
| -------------------------- | ---------------------- | ----------- | --- | ----- | ----------------------------------- |
| `assignment_sub_id`        | Assignment Sub         | `many2one`  |     | ✅    | op.assignment.sub.line              |
| `create_date`              | Created on             | `datetime`  |     | ✅    |                                     |
| `create_uid`               | Created by             | `many2one`  |     | ✅    | res.users                           |
| `display_name`             | Display Name           | `char`      |     |       |                                     |
| `id`                       | ID                     | `integer`   |     | ✅    |                                     |
| `maximum`                  | Out of                 | `float`     |     | ✅    |                                     |
| `rubric_element_id`        | Element                | `many2one`  |     | ✅    | op.rubric.element                   |
| `rubric_level_subline_ids` | Rubrics Elements Level | `one2many`  |     | ✅    | op.assignment.rubric.level.sub.line |
| `rubrics_type`             | Rubrics type           | `selection` | ✅  | ✅    |                                     |
| `rubric_template_id`       | Rubric Template        | `many2one`  |     |       | op.rubric.template                  |
| `write_date`               | Last Updated on        | `datetime`  |     | ✅    |                                     |
| `write_uid`                | Last Updated by        | `many2one`  |     | ✅    | res.users                           |

**Access Rights:**

| Name                                 | Group             | Perms     |
| ------------------------------------ | ----------------- | --------- |
| op_assignment_rubric_sub_line_user   | Assignment / User | `R/W/C/D` |
| access_op_assignment_rubric_sub_line | Role / User       | `R`       |
