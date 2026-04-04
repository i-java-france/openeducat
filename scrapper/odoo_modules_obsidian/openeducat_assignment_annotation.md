---
title: "OpenEduCat Assignment Annotation"
module: "openeducat_assignment_annotation"
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

# 🟢 OpenEduCat Assignment Annotation

> **Module:** `openeducat_assignment_annotation` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_assignment_enterprise]]

## 📖 Description

## OpenEduCat Assignment Annotation

### Create Annotations on submitted assignments of students

[![](/openeducat_assignment_annotation/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

You can use this module to annotate student assignments that have been turned in so you
can point out errors and ask them to submit revised versions.

[Contact Us](https://www.openeducat.org/contactus/)

## Assignment Submission

![](/openeducat_assignment_annotation/static/description/assign-1.png)

Students can submit the answers of assignment allocated to them. Once assignment is
submitted, faculty will have option to accept, reject or annotate the submitted
assignment from students. Faculty can also ask student to improve the answers and
resubmit the assignment.

## Annotation Creation

An annotation might look like highlighting information information or vocabulary in a
text, marking a text with symbols to represent different ideas, creating notes in the
margins of a text to keep track of thoughts and questions, or writing summaries at the
end of a chapter or section for easy review..

![](/openeducat_assignment_annotation/static/description/assign-2.png)

## Feedback

![](/openeducat_assignment_annotation/static/description/assign-3.png)

From the student menu, students can view the annotated assignment and resubmit it after
making the necessary changes.

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT assignment_data_feeedback_inherit (qweb)`
- `* INHERIT op.assignment.sub.line.inherited.form.view (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

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
