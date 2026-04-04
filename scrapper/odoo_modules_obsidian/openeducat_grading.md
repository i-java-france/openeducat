---
title: "OpenEduCat Grading"
module: "openeducat_grading"
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

# 🟢 OpenEduCat Grading

> **Module:** `openeducat_grading` | **Version:** `19.0.1.0` **Category:** Education |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_core_enterprise]] [[openeducat_student_progress_enterprise]]
[[openeducat_assignment_enterprise]] [[openeducat_attendance_enterprise]]

## 📖 Description

## OpenEduCat Grading

### OpenEduCat Grading module provides facility to Manage Student's Gradebook.

[![](/openeducat_grading/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

Based on best of class enterprise level architecture, OpenEduCat is ready to be used
from local infrastructure to a highly scalable cloud environment.

[Contact Us](https://www.openeducat.org/contactus/)

## Grade Scale

User can add Customized Grade Scale.

![](/openeducat_grading/static/description/grade_scale.png)

## Grade Template

![](/openeducat_grading/static/description/grade_template.png)

Here you can custom create different grade template, GPA value that corresponds with
each letter grade based on percentage.

## Gradebook

User can Create and Manage student's Gradebook.

![](/openeducat_grading/static/description/gradebook.png)

## Grading Assignment

![](/openeducat_grading/static/description/grading_assignment.png)

User can create Grading assignments and assign grades.

## Grade View

Can view Student's gradebook overview.

![](/openeducat_grading/static/description/grade_overview.png)

## Reports

![](/openeducat_grading/static/description/result_overview.png)

Can view gradebook by Student, Course, Subject and can download student Report Card and
Transcript.

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Grade Book`
- `Grade Book/Configuration`
- `Grade Book/Configuration/Assignment`
- `Grade Book/Configuration/Assignment/Assignment Stages`
- `Grade Book/Configuration/Assignment/Assignment Types`
- `Grade Book/Configuration/Assignment/Grade Table`
- `Grade Book/Configuration/Course`
- `Grade Book/Configuration/Course/Grade Scale`
- `Grade Book/Configuration/Course/Grade Template`
- `Grade Book/Configuration/Settings`
- `Grade Book/Grade Book`
- `Grade Book/Grading Assignment`
- `Grade Book/Reporting`
- `Grade Book/Reporting/Grade By Batch`
- `Grade Book/Reporting/Grade By Course`
- `Grade Book/Reporting/Grade By Report`
- `Grade Book/Reporting/Grade By Subject`
- `Grade Book/Reporting/Gradebook Excel Report`
- `Grade Book/Reporting/Grades Analysis`
- `Grade Book/Reporting/Honor Roll`

### Views

- `* INHERIT Portal layout: Grade Book (qweb)`
- `* INHERIT Show Gradebook (qweb)`
- `* INHERIT op.assignment.form (form)`
- `* INHERIT op.batch.list (list)`
- `* INHERIT op.course.form (form)`
- `* INHERIT op.course.list (list)`
- `* INHERIT op.student.grading.smart.buttons (form)`
- `* INHERIT op.student.progression.form.inherit.grading (form)`
- `* INHERIT op.subject.form (form)`
- `* INHERIT op.subject.list (list)`
- `Grade Book (qweb)`
- `assignment.stage.form (form)`
- `assignment.stage.list (list)`
- `assignment.type.weight.line.form (form)`
- `assignment.type.weight.line.list (list)`
- `assignment.type.weight.line.search (search)`
- `assignment.wizard.form (form)`
- `attendance.type.weight.line.form (form)`
- `attendance.type.weight.line.list (list)`
- `attendance.type.weight.line.search (search)`
- `double_col_report (qweb)`
- `double_col_trans (qweb)`
- `gradebook.gradebook.form (form)`
- `gradebook.gradebook.list (list)`
- `gradebook.gradebook.search (search)`
- `gradebook.line.form (form)`
- `gradebook.line.list (list)`
- `gradebook.line.pivot (pivot)`
- `gradebook.line.search (search)`
- `grading.assignment.form (form)`
- `grading.assignment.kanban (kanban)`
- `grading.assignment.list (list)`
- `grading.assignment.search (search)`
- `grading.wizard.form (form)`
- `honor_certi_data (qweb)`
- `honor_roll_list (qweb)`
- `honour_certification (qweb)`
- `op.grade.override.line.form (form)`
- `op.grade.override.line.list (list)`
- `op.grade.override.line.search (search)`
- `op.grade.scale.form (form)`
- `op.grade.scale.list (list)`
- `op.grade.scale.search (search)`
- `op.grade.table.form (form)`
- `op.grade.table.line.form (form)`
- `op.grade.table.line.list (list)`
- `op.grade.table.line.search (search)`
- `op.grade.table.list (list)`
- `op.grade.table.search (search)`
- `op.grade.template.form (form)`
- `op.grade.template.line.form (form)`
- `op.grade.template.line.list (list)`
- `op.grade.template.line.search (search)`
- `op.grade.template.list (list)`
- `op.grade.template.search (search)`
- `op.grade.type.form (form)`
- `op.grade.type.list (list)`
- `op.grade.type.search (search)`
- `op.honorroll (list)`
- `op.honorroll.form (form)`
- `op.honorroll.line (list)`
- `op.honorroll.line.form (form)`
- `op.honorroll.line.search (search)`
- `op.honorroll.search (search)`
- `report_comment (qweb)`
- `single_col_report (qweb)`
- `single_col_trans (qweb)`
- `student.transcript.wizard.form (form)`
- `student_grade_report (qweb)`
- `student_transcript (qweb)`
- `subterm.weight.line.form (form)`
- `subterm.weight.line.list (list)`
- `subterm.weight.line.search (search)`

### Reports

- `Grade Report`
- `Honor Roll Certificate`
- `Honor Roll List`
- `Transcript`

## 🛠️ Technical Documentation

**27 model(s) defined by this module:**

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

### 🗃️ `assignment.stage` — Assignment Stages

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
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company    |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users      |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `fold`                       | Folded In Kanban       | `boolean`   |     | ✅    |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
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
| `name`                       | Stage Name             | `char`      | ✅  | ✅    |                |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `sequence`                   | Sequence               | `integer`   |     | ✅    |                |
| `state`                      | State                  | `selection` |     | ✅    |                |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                                      | Group             | Perms     |
| ----------------------------------------- | ----------------- | --------- |
| access_assignment_stage_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_assignment_stage_faculty           | Grading / User    | `R/W/C`   |

**Record Rules:**

- **Assignment Stage Multi Comp Rule** (Global) `R/W/C/D`
  - Domain:
    `['|','|',('company_id','=',False),('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids),('company_id','in', company_ids)]`

### 🗃️ `op.course` — Course

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                         | Type        | Req | Store | Relation               |
| -------------------------------- | ----------------------------- | ----------- | --- | ----- | ---------------------- |
| `active`                         | Active                        | `boolean`   |     | ✅    |                        |
| `activity_calendar_event_id`     | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event         |
| `activity_date_deadline`         | Next Activity Deadline        | `date`      |     |       |                        |
| `activity_exception_decoration`  | Activity Exception Decoration | `selection` |     |       |                        |
| `activity_exception_icon`        | Icon                          | `char`      |     |       |                        |
| `activity_ids`                   | Activities                    | `one2many`  |     | ✅    | mail.activity          |
| `activity_state`                 | Activity State                | `selection` |     |       |                        |
| `activity_summary`               | Next Activity Summary         | `char`      |     |       |                        |
| `activity_type_icon`             | Activity Type Icon            | `char`      |     |       |                        |
| `activity_type_id`               | Next Activity Type            | `many2one`  |     |       | mail.activity.type     |
| `activity_user_id`               | Responsible User              | `many2one`  |     |       | res.users              |
| `admission_count`                | Admission Count               | `integer`   |     |       |                        |
| `allow_reviews`                  | Allow Reviews                 | `boolean`   |     | ✅    |                        |
| `announcement_line`              | Announcements                 | `one2many`  |     | ✅    | op.course.announcement |
| `area_id`                        | Area                          | `many2one`  |     |       | op.area                |
| `assignment_count`               | Assignment Count              | `integer`   |     |       |                        |
| `avg_progress`                   | Avg. Progress (%)             | `float`     |     | ✅    |                        |
| `background`                     | Background Image              | `binary`    |     | ✅    |                        |
| `batch_count`                    | Batch Count                   | `integer`   |     |       |                        |
| `can_publish`                    | Can Publish                   | `boolean`   |     |       |                        |
| `category_ids`                   | Categories                    | `many2many` |     | ✅    | op.course.category     |
| `certi_date`                     | Certificate Date              | `boolean`   |     | ✅    |                        |
| `certi_title`                    | Certificate Title             | `char`      |     | ✅    |                        |
| `child_course_count`             | Child Course Count            | `integer`   |     |       |                        |
| `code`                           | Code                          | `char`      | ✅  | ✅    |                        |
| `color`                          | Color Index                   | `integer`   |     | ✅    |                        |
| `company_id`                     | Company                       | `many2one`  |     | ✅    | res.company            |
| `completion_count`               | Completions                   | `integer`   |     | ✅    |                        |
| `content_category_ids`           | Content Modules               | `one2many`  |     |       | op.course.module       |
| `content_content_ids`            | Content                       | `one2many`  |     |       | op.course.module       |
| `course_change_fees`             | Course Change Fees            | `boolean`   |     | ✅    |                        |
| `course_image`                   | Course Image                  | `binary`    |     | ✅    |                        |
| `cover_properties`               | Cover Properties              | `text`      |     | ✅    |                        |
| `create_date`                    | Created on                    | `datetime`  |     | ✅    |                        |
| `create_uid`                     | Created by                    | `many2one`  |     | ✅    | res.users              |
| `credit`                         | Course Credit                 | `float`     |     | ✅    |                        |
| `department_id`                  | Department                    | `many2one`  |     | ✅    | op.department          |
| `description`                    | Description                   | `html`      |     | ✅    |                        |
| `display_name`                   | Display Name                  | `char`      |     |       |                        |
| `display_style`                  | Display Style                 | `selection` |     | ✅    |                        |
| `enrollment_line`                | Enrollment                    | `one2many`  |     | ✅    | op.course.enrollment   |
| `evaluation_type`                | Evaluation Type               | `selection` | ✅  | ✅    |                        |
| `faculty_count`                  | Faculty Count                 | `integer`   |     |       |                        |
| `faculty_ids`                    | Instructor                    | `many2many` |     | ✅    | op.faculty             |
| `fees_term_id`                   | Fees Term                     | `many2one`  |     | ✅    | op.fees.terms          |
| `forum_count`                    | Forum Count                   | `integer`   |     | ✅    |                        |
| `forum_id`                       | Forum                         | `many2one`  |     | ✅    | forum.forum            |
| `forum_post_count`               | Forum Post Count              | `integer`   |     | ✅    |                        |
| `forum_post_ids`                 | Forum Post                    | `one2many`  |     | ✅    | forum.post             |
| `forum_reply_count`              | Forum Reply Count             | `integer`   |     | ✅    |                        |
| `full_description`               | Full Description              | `html`      |     | ✅    |                        |
| `grade_scale_id`                 | Final Grade                   | `many2one`  |     | ✅    | op.grade.scale         |
| `grade_template_ids`             | Grade Template                | `many2many` | ✅  | ✅    | op.grade.template      |
| `has_message`                    | Has Message                   | `boolean`   |     |       |                        |
| `id`                             | ID                            | `integer`   |     | ✅    |                        |
| `image_1024`                     | Image 1024                    | `binary`    |     | ✅    |                        |
| `image_128`                      | Image 128                     | `binary`    |     | ✅    |                        |
| `image_1920`                     | Image                         | `binary`    |     | ✅    |                        |
| `image_256`                      | Image 256                     | `binary`    |     | ✅    |                        |
| `image_512`                      | Image 512                     | `binary`    |     | ✅    |                        |
| `invited_users_ids`              | Invited Users                 | `many2many` |     | ✅    | res.users              |
| `is_certificate`                 | Certificate Of Completion?    | `boolean`   |     | ✅    |                        |
| `is_enroll_user`                 | Enroll User                   | `boolean`   |     | ✅    |                        |
| `is_paid`                        | Paid Course?                  | `boolean`   |     | ✅    |                        |
| `is_published`                   | Is Published                  | `boolean`   |     | ✅    |                        |
| `list_price`                     | Price                         | `float`     |     |       |                        |
| `lms_course_count`               | LMS course count              | `char`      |     | ✅    |                        |
| `lms_course_type`                | Course type                   | `selection` | ✅  | ✅    |                        |
| `max_unit_load`                  | Maximum Unit Load             | `float`     |     | ✅    |                        |
| `message_attachment_count`       | Attachment Count              | `integer`   |     |       |                        |
| `message_follower_ids`           | Followers                     | `one2many`  |     | ✅    | mail.followers         |
| `message_has_error`              | Message Delivery error        | `boolean`   |     |       |                        |
| `message_has_error_counter`      | Number of errors              | `integer`   |     |       |                        |
| `message_has_sms_error`          | SMS Delivery error            | `boolean`   |     |       |                        |
| `message_ids`                    | Messages                      | `one2many`  |     | ✅    | mail.message           |
| `message_is_follower`            | Is Follower                   | `boolean`   |     |       |                        |
| `message_needaction`             | Action Needed                 | `boolean`   |     |       |                        |
| `message_needaction_counter`     | Number of Actions             | `integer`   |     |       |                        |
| `message_partner_ids`            | Followers (Partners)          | `many2many` |     |       | res.partner            |
| `min_unit_load`                  | Minimum Unit Load             | `float`     |     | ✅    |                        |
| `module_lines`                   | Module                        | `one2many`  |     | ✅    | op.course.module       |
| `my_activity_date_deadline`      | My Activity Deadline          | `date`      |     |       |                        |
| `name`                           | Name                          | `char`      | ✅  | ✅    |                        |
| `navigation_policy`              | Navigation Policy             | `selection` | ✅  | ✅    |                        |
| `notice_group_id`                | Notice Group                  | `many2one`  |     | ✅    | op.notice.group        |
| `online_course`                  | Online Course                 | `boolean`   |     | ✅    |                        |
| `online_course_created`          | Online Course Created         | `boolean`   |     | ✅    |                        |
| `parent_id`                      | Parent Course                 | `many2one`  |     | ✅    | op.course              |
| `price`                          | Computed Price                | `float`     |     |       |                        |
| `product_id`                     | Product                       | `many2one`  |     | ✅    | product.product        |
| `program_id`                     | Program                       | `many2one`  |     | ✅    | op.program             |
| `rating_avg`                     | Average Rating                | `float`     |     |       |                        |
| `rating_avg_stars`               | Rating Average (Stars)        | `float`     |     |       |                        |
| `rating_avg_text`                | Rating Avg Text               | `selection` |     |       |                        |
| `rating_count`                   | Rating count                  | `integer`   |     |       |                        |
| `rating_ids`                     | Ratings                       | `one2many`  |     | ✅    | rating.rating          |
| `rating_last_feedback`           | Rating Last Feedback          | `text`      |     |       |                        |
| `rating_last_image`              | Rating Last Image             | `binary`    |     |       |                        |
| `rating_last_text`               | Rating Text                   | `selection` |     |       |                        |
| `rating_last_value`              | Rating Last Value             | `float`     |     | ✅    |                        |
| `rating_percentage_satisfaction` | Rating Satisfaction           | `float`     |     |       |                        |
| `reg_fees`                       | Registration Fees             | `boolean`   |     | ✅    |                        |
| `sequence`                       | Sequence                      | `integer`   |     | ✅    |                        |
| `short_desc`                     | Short Description             | `text`      |     | ✅    |                        |
| `specialization_id`              | Specialization                | `many2one`  |     | ✅    | op.specialization      |
| `state`                          | State                         | `selection` |     | ✅    |                        |
| `student_count`                  | Student Count                 | `integer`   |     |       |                        |
| `subject_count`                  | Subject Count                 | `integer`   |     |       |                        |
| `subject_counts`                 | Subject Counts                | `integer`   |     |       |                        |
| `subject_ids`                    | Subject(s)                    | `many2many` |     | ✅    | op.subject             |
| `subject_selection_option`       | Subject Selection             | `selection` |     | ✅    |                        |
| `suggested_course_ids`           | Suggested Course              | `many2many` |     | ✅    | op.course              |
| `survey_ids`                     | Survey                        | `one2many`  |     | ✅    | survey.survey          |
| `tag_ids`                        | Tags                          | `many2many` |     | ✅    | op.course.tag          |
| `timetable_count`                | Timetable Count               | `integer`   |     |       |                        |
| `timing_course_count`            | Timing Course Count           | `integer`   |     |       |                        |
| `total_enrollment`               | Total Enrollment              | `integer`   |     | ✅    |                        |
| `total_modules`                  | Number of Contents            | `integer`   |     | ✅    |                        |
| `total_time`                     | Duration                      | `float`     |     | ✅    |                        |
| `user_id`                        | Responsible                   | `many2one`  |     | ✅    | res.users              |
| `visibility`                     | Visibility Policy             | `selection` | ✅  | ✅    |                        |
| `website_absolute_url`           | Website Absolute URL          | `char`      |     |       |                        |
| `website_id`                     | Website                       | `many2one`  |     | ✅    | website                |
| `website_message_ids`            | Website Messages              | `one2many`  |     | ✅    | mail.message           |
| `website_published`              | Visible on current website    | `boolean`   |     |       |                        |
| `website_url`                    | Website URL                   | `char`      |     |       |                        |
| `write_date`                     | Last Updated on               | `datetime`  |     | ✅    |                        |
| `write_uid`                      | Last Updated by               | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                             | Group                | Perms     |
| -------------------------------- | -------------------- | --------- |
| name_op_course_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| name_op_course_faculty           | OpenEduCat / User    | `R/W/C`   |
| name_op_course_library           | Library / Manager    | `R`       |
| access_op_course                 | LMS / Manager        | `R/W/C/D` |
| access_op_course_user            | LMS / User           | `R/W/C`   |
| access_op_course_portal          | Role / Portal        | `R/W`     |
| name_op_course_parent            | Role / Portal        | `R`       |
| access_op_course_public          | Role / Public        | `R`       |
| name_op_dynamic_admission_course | Role / Public        | `R`       |

**Record Rules:**

- **Course multi-company** (1) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `
- **Course multi-department** (1) `R/W/C/D`
  - Domain:
    `         ['|','|',('department_id','=',False),('department_id','child_of',[user.dept_id.id]),('department_id','in',user.department_ids.ids)]     `
- **course multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

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

### 🗃️ `op.grade.template` — Grade Template

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
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company            |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                        |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users              |
| `display_name`               | Display Name           | `char`      |     |       |                        |
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
| `state`                      | State                  | `selection` |     | ✅    |                        |
| `template_line_ids`          | Template Line          | `one2many`  | ✅  | ✅    | op.grade.template.line |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message           |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                        |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                                       | Group             | Perms     |
| ------------------------------------------ | ----------------- | --------- |
| access_op_grade_template_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_op_grade_template_faculty           | Grading / User    | `R/W/C`   |

**Record Rules:**

- **Grade Template multi company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `grading.assignment` — Grading Assigment

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
| `assignment_type`               | Assignment Type               | `many2one`  | ✅  | ✅    | grading.assignment.type |
| `color`                         | Color Index                   | `integer`   |     | ✅    |                         |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company             |
| `course_id`                     | Course                        | `many2one`  | ✅  | ✅    | op.course               |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                         |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users               |
| `display_name`                  | Display Name                  | `char`      |     |       |                         |
| `faculty_id`                    | Faculty                       | `many2one`  | ✅  | ✅    | op.faculty              |
| `grade`                         | Grade                         | `many2one`  |     | ✅    | op.grade.table          |
| `gradebook_line_id`             | Gradebook Line                | `one2many`  |     | ✅    | gradebook.line          |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                         |
| `hide`                          | Hide                          | `boolean`   |     |       |                         |
| `hide_subject`                  | Hide Subject                  | `boolean`   |     |       |                         |
| `id`                            | ID                            | `integer`   |     | ✅    |                         |
| `issued_date`                   | Issued Date                   | `datetime`  | ✅  | ✅    |                         |
| `lock_change`                   | Lock Change                   | `boolean`   |     |       |                         |
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
| `point`                         | Points                        | `float`     |     | ✅    |                         |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating           |
| `sequence`                      | Index                         | `char`      | ✅  | ✅    |                         |
| `stage_id`                      | Stage                         | `many2one`  |     | ✅    | assignment.stage        |
| `state`                         | State                         | `selection` |     | ✅    |                         |
| `subject_id`                    | Subject                       | `many2one`  |     | ✅    | op.subject              |
| `term_id`                       | Term                          | `many2one`  |     | ✅    | op.academic.term        |
| `user_id`                       | User                          | `many2one`  | ✅  | ✅    | res.users               |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message            |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                         |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users               |
| `year_id`                       | Academic Year                 | `many2one`  |     | ✅    | op.academic.year        |

**Access Rights:**

| Name                                        | Group                | Perms     |
| ------------------------------------------- | -------------------- | --------- |
| grading_assignment_manager                  | Assignment / Manager | `R/W/C/D` |
| grading_assignment_user                     | Assignment / User    | `R/W/C`   |
| access_grading_assignment_back_office_admin | Grading / Manager    | `R/W/C/D` |
| access_grading_assignment_faculty           | Grading / User       | `R/W/C`   |
| grading_assignment_portal                   | Role / Portal        | `R/W/C`   |

**Record Rules:**

- **Faculty Grading Assignment rule** (181) `R/W/C/D`
  - Domain: `[('faculty_id.user_id','=',user.id)]`
- **Admin Grading Assignment rule** (182) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Backoffice Grading Assignment rule** (182) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Grading Assignment multi company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `op.grade.scale` — Grading Scale

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
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company    |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users      |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
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
| `name`                       | Name                   | `char`      | ✅  | ✅    |                |
| `op_grade_type_ids`          | Grade Type             | `one2many`  |     | ✅    | op.grade.type  |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `state`                      | State                  | `selection` |     | ✅    |                |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                                    | Group             | Perms     |
| --------------------------------------- | ----------------- | --------- |
| access_op_grade_scale_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_op_grade_scale_faculty           | Grading / User    | `R/W/C`   |

**Record Rules:**

- **Grade Scale multi company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `op.honorroll` — Honor Roll

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation           |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------ |
| `active`                        | Active                        | `boolean`   |     | ✅    |                    |
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
| `background`                    | Background Image              | `binary`    |     | ✅    |                    |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company        |
| `course_id`                     | Course                        | `many2one`  | ✅  | ✅    | op.course          |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `description`                   | Description                   | `text`      | ✅  | ✅    |                    |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `from_per`                      | From Percentage               | `float`     | ✅  | ✅    |                    |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `honor_line_id`                 | Honor Line                    | `one2many`  |     | ✅    | op.honorroll.line  |
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
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `state`                         | State                         | `selection` |     | ✅    |                    |
| `subject_id`                    | Subject                       | `many2one`  |     | ✅    | op.subject         |
| `to_per`                        | To Percentage                 | `float`     | ✅  | ✅    |                    |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |
| `year_id`                       | Academic Year                 | `many2one`  | ✅  | ✅    | op.academic.year   |

**Access Rights:**

| Name                                  | Group             | Perms     |
| ------------------------------------- | ----------------- | --------- |
| access_op_honorroll_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_op_honorroll_faculty           | Grading / User    | `R/W/C`   |

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

### 🗃️ `op.student` — Student

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                       | Label                                               | Type         | Req | Store | Relation                    |
| ------------------------------------------- | --------------------------------------------------- | ------------ | --- | ----- | --------------------------- |
| `account_move_count`                        | Account Move Count                                  | `integer`    |     |       |                             |
| `achievement_line_ids`                      | Achievement Details                                 | `one2many`   |     | ✅    | op.achievement              |
| `active`                                    | Active                                              | `boolean`    |     | ✅    |                             |
| `active_lang_count`                         | Active Lang Count                                   | `integer`    |     |       |                             |
| `activity_calendar_event_id`                | Next Activity Calendar Event                        | `many2one`   |     |       | calendar.event              |
| `activity_count`                            | Activity Count                                      | `integer`    |     |       |                             |
| `activity_date_deadline`                    | Next Activity Deadline                              | `date`       |     |       |                             |
| `activity_exception_decoration`             | Activity Exception Decoration                       | `selection`  |     |       |                             |
| `activity_exception_icon`                   | Icon                                                | `char`       |     |       |                             |
| `activity_ids`                              | Activities                                          | `one2many`   |     | ✅    | mail.activity               |
| `activity_log`                              | Activity Log                                        | `one2many`   |     | ✅    | op.activity                 |
| `activity_state`                            | Activity State                                      | `selection`  |     |       |                             |
| `activity_summary`                          | Next Activity Summary                               | `char`       |     |       |                             |
| `activity_type_icon`                        | Activity Type Icon                                  | `char`       |     |       |                             |
| `activity_type_id`                          | Next Activity Type                                  | `many2one`   |     |       | mail.activity.type          |
| `activity_user_id`                          | Responsible User                                    | `many2one`   |     |       | res.users                   |
| `allocation_ids`                            | Assignment(s)                                       | `many2many`  |     | ✅    | op.assignment               |
| `alumni_boolean`                            | Is An Alumni?                                       | `boolean`    |     | ✅    |                             |
| `alumni_id`                                 | Group                                               | `many2one`   |     | ✅    | op.alumni.group             |
| `applicant_ids`                             | Applicants                                          | `one2many`   |     |       | hr.applicant                |
| `application_count`                         | Applications                                        | `integer`    |     |       |                             |
| `application_statistics`                    | Stats                                               | `json`       |     |       |                             |
| `assignment_count`                          | Assignment Count                                    | `integer`    |     |       |                             |
| `attendance_ids`                            | Attendance                                          | `one2many`   |     | ✅    | op.attendance.line          |
| `autopost_bills`                            | Auto-post bills                                     | `selection`  | ✅  |       |                             |
| `available_invoice_template_pdf_report_ids` | Available Invoice Template Pdf Report               | `one2many`   |     |       | ir.actions.report           |
| `available_peppol_eas`                      | Available Peppol Eas                                | `json`       |     |       |                             |
| `avatar_1024`                               | Avatar 1024                                         | `binary`     |     |       |                             |
| `avatar_128`                                | Avatar 128                                          | `binary`     |     |       |                             |
| `avatar_1920`                               | Avatar                                              | `binary`     |     |       |                             |
| `avatar_256`                                | Avatar 256                                          | `binary`     |     |       |                             |
| `avatar_512`                                | Avatar 512                                          | `binary`     |     |       |                             |
| `bank_account_count`                        | Bank                                                | `integer`    |     |       |                             |
| `bank_ids`                                  | Banks                                               | `one2many`   |     |       | res.partner.bank            |
| `barcode`                                   | Badge ID                                            | `char`       |     | ✅    |                             |
| `birth_date`                                | Birth Date                                          | `date`       |     | ✅    |                             |
| `blood_group`                               | Blood Group                                         | `selection`  |     | ✅    |                             |
| `buyer_id`                                  | Buyer                                               | `many2one`   |     |       | res.users                   |
| `calendar_last_notif_ack`                   | Last notification marked as read from base Calendar | `datetime`   |     |       |                             |
| `can_publish`                               | Can Publish                                         | `boolean`    |     |       |                             |
| `category_id`                               | Category                                            | `many2one`   |     | ✅    | op.category                 |
| `certificate_number`                        | Certificate No.                                     | `char`       |     | ✅    |                             |
| `certifications_company_count`              | Company Certifications Count                        | `integer`    |     |       |                             |
| `certifications_count`                      | Certifications Count                                | `integer`    |     |       |                             |
| `channel_ids`                               | Channels                                            | `many2many`  |     |       | discuss.channel             |
| `channel_member_ids`                        | Channel Member                                      | `one2many`   |     |       | discuss.channel.member      |
| `chatbot_script_ids`                        | Chatbot Script                                      | `one2many`   |     |       | chatbot.script              |
| `child_ids`                                 | Contact                                             | `one2many`   |     |       | res.partner                 |
| `city`                                      | City                                                | `char`       |     |       |                             |
| `code`                                      | Company Code                                        | `char`       |     |       |                             |
| `color`                                     | Color Index                                         | `integer`    |     |       |                             |
| `comment`                                   | Notes                                               | `html`       |     |       |                             |
| `commercial_company_name`                   | Company Name Entity                                 | `char`       |     |       |                             |
| `commercial_partner_id`                     | Commercial Entity                                   | `many2one`   |     |       | res.partner                 |
| `company_id`                                | Company                                             | `many2one`   |     | ✅    | res.company                 |
| `company_name`                              | Company Name                                        | `char`       |     |       |                             |
| `company_registry`                          | Company ID                                          | `char`       |     |       |                             |
| `company_registry_label`                    | Company ID Label                                    | `char`       |     |       |                             |
| `company_registry_placeholder`              | Company Registry Placeholder                        | `char`       |     |       |                             |
| `company_type`                              | Company Type                                        | `selection`  |     |       |                             |
| `complete_name`                             | Complete Name                                       | `char`       |     |       |                             |
| `contact_address`                           | Complete Address                                    | `char`       |     |       |                             |
| `contact_address_inline`                    | Inlined Complete Address                            | `char`       |     |       |                             |
| `contract_ids`                              | Partner Contracts                                   | `one2many`   |     |       | account.analytic.account    |
| `country_code`                              | Country Code                                        | `char`       |     |       |                             |
| `country_id`                                | Country                                             | `many2one`   |     |       | res.country                 |
| `course_detail_ids`                         | Course Details                                      | `one2many`   |     | ✅    | op.student.course           |
| `create_date`                               | Created on                                          | `datetime`   |     | ✅    |                             |
| `create_uid`                                | Created by                                          | `many2one`   |     | ✅    | res.users                   |
| `credit`                                    | Total Receivable                                    | `monetary`   |     |       |                             |
| `credit_limit`                              | Credit Limit                                        | `float`      |     |       |                             |
| `credit_to_invoice`                         | Credit To Invoice                                   | `monetary`   |     |       |                             |
| `crm_lead_count`                            | Crm Lead Count                                      | `integer`    |     |       |                             |
| `crm_lead_ids`                              | CRM Leads                                           | `one2many`   |     | ✅    | crm.lead                    |
| `currency_id`                               | Currency                                            | `many2one`   |     |       | res.currency                |
| `current_job`                               | Current Job                                         | `char`       |     | ✅    |                             |
| `current_position`                          | Current Position                                    | `char`       |     | ✅    |                             |
| `customer_rank`                             | Customer Rank                                       | `integer`    |     |       |                             |
| `days_sales_outstanding`                    | Days Sales Outstanding (DSO)                        | `float`      |     |       |                             |
| `debit`                                     | Total Payable                                       | `monetary`   |     |       |                             |
| `descriptor`                                | Descriptor                                          | `char`       |     | ✅    |                             |
| `discipline_count`                          | Discipline Count                                    | `integer`    |     |       |                             |
| `discipline_ids`                            | Discipline Details                                  | `one2many`   |     | ✅    | op.discipline               |
| `display_invoice_edi_format`                | Display Invoice Edi Format                          | `boolean`    |     |       |                             |
| `display_invoice_template_pdf_report_id`    | Display Invoice Template Pdf Report                 | `boolean`    |     |       |                             |
| `display_name`                              | Display Name                                        | `char`       |     |       |                             |
| `duplicate_bank_partner_ids`                | Duplicate Bank Partner                              | `many2many`  |     |       | res.partner                 |
| `email`                                     | Email                                               | `char`       |     |       |                             |
| `email_formatted`                           | Formatted Email                                     | `char`       |     |       |                             |
| `email_normalized`                          | Normalized Email                                    | `char`       |     |       |                             |
| `emergency_contact`                         | Emergency Contact                                   | `many2one`   |     | ✅    | res.partner                 |
| `employee`                                  | Employee                                            | `boolean`    |     |       |                             |
| `employee_ids`                              | Employees                                           | `one2many`   |     |       | hr.employee                 |
| `employees_count`                           | Employees Count                                     | `integer`    |     |       |                             |
| `event_count`                               | # Events                                            | `integer`    |     |       |                             |
| `fees_detail_ids`                           | Fees Collection Details                             | `one2many`   |     | ✅    | op.student.fees.details     |
| `fees_details_count`                        | Fees Details Count                                  | `integer`    |     |       |                             |
| `fees_plan_details_count`                   | Fees Plan Details Count                             | `integer`    |     |       |                             |
| `fees_plan_ids`                             | Fees Plan Details                                   | `one2many`   |     | ✅    | op.fees.plan                |
| `first_name`                                | First Name                                          | `char`       |     | ✅    |                             |
| `fiscal_country_codes`                      | Fiscal Country Codes                                | `char`       |     |       |                             |
| `fiscal_country_group_codes`                | Fiscal Country Group Codes                          | `json`       |     |       |                             |
| `function`                                  | Job Position                                        | `char`       |     |       |                             |
| `gender`                                    | Gender                                              | `selection`  | ✅  | ✅    |                             |
| `global_location_number`                    | GLN                                                 | `char`       |     |       |                             |
| `gr_no`                                     | Registration Number                                 | `char`       |     | ✅    |                             |
| `group_on`                                  | Week Day                                            | `selection`  | ✅  |       |                             |
| `group_rfq`                                 | Group RFQ                                           | `selection`  | ✅  |       |                             |
| `has_message`                               | Has Message                                         | `boolean`    |     |       |                             |
| `head_office`                               | Head Office                                         | `char`       |     |       |                             |
| `health_count`                              | Health Count                                        | `integer`    |     |       |                             |
| `health_lines`                              | Health Detail                                       | `one2many`   |     | ✅    | op.health                   |
| `hr_contact`                                | HR Contact                                          | `char`       |     |       |                             |
| `hr_email`                                  | HR Email                                            | `char`       |     |       |                             |
| `hr_name`                                   | HR Name                                             | `char`       |     |       |                             |
| `id`                                        | ID                                                  | `integer`    |     | ✅    |                             |
| `id_number`                                 | ID Card Number                                      | `char`       |     | ✅    |                             |
| `ignore_abnormal_invoice_amount`            | Ignore Abnormal Invoice Amount                      | `boolean`    |     |       |                             |
| `ignore_abnormal_invoice_date`              | Ignore Abnormal Invoice Date                        | `boolean`    |     |       |                             |
| `image_1024`                                | Image 1024                                          | `binary`     |     |       |                             |
| `image_128`                                 | Image 128                                           | `binary`     |     |       |                             |
| `image_1920`                                | Image                                               | `binary`     |     |       |                             |
| `image_256`                                 | Image 256                                           | `binary`     |     |       |                             |
| `image_512`                                 | Image 512                                           | `binary`     |     |       |                             |
| `image_detect`                              | Image Detect                                        | `binary`     |     | ✅    |                             |
| `im_status`                                 | IM Status                                           | `char`       |     |       |                             |
| `industry_id`                               | Industry                                            | `many2one`   |     |       | res.partner.industry        |
| `invoice_edi_format`                        | eInvoice format                                     | `selection`  |     |       |                             |
| `invoice_edi_format_store`                  | Invoice Edi Format Store                            | `char`       |     |       |                             |
| `invoice_id`                                | Invoice ID                                          | `many2one`   |     | ✅    | account.move                |
| `invoice_ids`                               | Invoices                                            | `one2many`   |     |       | account.move                |
| `invoice_sending_method`                    | Invoice sending                                     | `selection`  |     |       |                             |
| `invoice_template_pdf_report_id`            | Invoice report                                      | `many2one`   |     |       | ir.actions.report           |
| `is_blacklisted`                            | Blacklist                                           | `boolean`    |     |       |                             |
| `is_company`                                | Is a Company                                        | `boolean`    |     |       |                             |
| `is_finished`                               | Finished or Withdrawn                               | `boolean`    |     | ✅    |                             |
| `is_in_call`                                | Is In Call                                          | `boolean`    |     |       |                             |
| `is_parent`                                 | Is a Parent                                         | `boolean`    |     |       |                             |
| `is_peppol_edi_format`                      | Is Peppol Edi Format                                | `boolean`    |     |       |                             |
| `is_pickup_location`                        | Is Pickup Location                                  | `boolean`    |     |       |                             |
| `is_public`                                 | Is Public                                           | `boolean`    |     |       |                             |
| `is_published`                              | Is Published                                        | `boolean`    |     |       |                             |
| `is_seo_optimized`                          | SEO optimized                                       | `boolean`    |     |       |                             |
| `is_student`                                | Is a Student                                        | `boolean`    |     |       |                             |
| `is_ubl_format`                             | Is Ubl Format                                       | `boolean`    |     |       |                             |
| `is_venue`                                  | Venue                                               | `boolean`    |     |       |                             |
| `Job_post_count`                            | Job Post Count                                      | `integer`    |     |       |                             |
| `job_post_ids`                              | Job Post Details                                    | `one2many`   |     | ✅    | op.job.applicant            |
| `join_date`                                 | Join Date                                           | `date`       |     |       |                             |
| `lang`                                      | Language                                            | `selection`  |     |       |                             |
| `last_attendance_id`                        | Last Attendance                                     | `many2one`   |     | ✅    | op.attendance.line          |
| `last_name`                                 | Last Name                                           | `char`       |     | ✅    |                             |
| `leave_date_to`                             | Leave Date To                                       | `date`       |     |       |                             |
| `library_card_id`                           | Library Card                                        | `many2one`   |     | ✅    | op.library.card             |
| `livechat_channel_count`                    | Livechat Channel Count                              | `integer`    |     |       |                             |
| `main_user_id`                              | Main User                                           | `many2one`   |     |       | res.users                   |
| `media_movement_lines`                      | Movements                                           | `one2many`   |     | ✅    | op.media.movement           |
| `media_movement_lines_count`                | Media Movement Lines Count                          | `integer`    |     |       |                             |
| `meeting_count`                             | # Meetings                                          | `integer`    |     |       |                             |
| `meeting_ids`                               | Meetings                                            | `many2many`  |     |       | calendar.event              |
| `message_attachment_count`                  | Attachment Count                                    | `integer`    |     |       |                             |
| `message_bounce`                            | Bounce                                              | `integer`    |     |       |                             |
| `message_follower_ids`                      | Followers                                           | `one2many`   |     | ✅    | mail.followers              |
| `message_has_error`                         | Message Delivery error                              | `boolean`    |     |       |                             |
| `message_has_error_counter`                 | Number of errors                                    | `integer`    |     |       |                             |
| `message_has_sms_error`                     | SMS Delivery error                                  | `boolean`    |     |       |                             |
| `message_ids`                               | Messages                                            | `one2many`   |     | ✅    | mail.message                |
| `message_is_follower`                       | Is Follower                                         | `boolean`    |     |       |                             |
| `message_needaction`                        | Action Needed                                       | `boolean`    |     |       |                             |
| `message_needaction_counter`                | Number of Actions                                   | `integer`    |     |       |                             |
| `message_partner_ids`                       | Followers (Partners)                                | `many2many`  |     |       | res.partner                 |
| `middle_name`                               | Middle Name                                         | `char`       |     | ✅    |                             |
| `my_activity_date_deadline`                 | My Activity Deadline                                | `date`       |     |       |                             |
| `name`                                      | Name                                                | `char`       |     |       |                             |
| `nationality`                               | Nationality                                         | `many2one`   |     | ✅    | res.country                 |
| `number`                                    | Invoice Number                                      | `char`       |     |       |                             |
| `offline_since`                             | Offline since                                       | `datetime`   |     |       |                             |
| `on_time_rate`                              | On-Time Delivery Rate                               | `float`      |     |       |                             |
| `opportunity_count`                         | Opportunity Count                                   | `integer`    |     |       |                             |
| `opportunity_ids`                           | Opportunities                                       | `one2many`   |     |       | crm.lead                    |
| `parent_id`                                 | Related Company                                     | `many2one`   |     |       | res.partner                 |
| `parent_ids`                                | Parent                                              | `many2many`  |     | ✅    | op.parent                   |
| `parent_name`                               | Parent name                                         | `char`       |     |       |                             |
| `partner_company_registry_placeholder`      | Partner Company Registry Placeholder                | `char`       |     |       |                             |
| `partner_id`                                | Partner                                             | `many2one`   | ✅  | ✅    | res.partner                 |
| `partner_latitude`                          | Geo Latitude                                        | `float`      |     |       |                             |
| `partner_longitude`                         | Geo Longitude                                       | `float`      |     |       |                             |
| `partner_share`                             | Share Partner                                       | `boolean`    |     |       |                             |
| `partner_vat_placeholder`                   | Partner Vat Placeholder                             | `char`       |     |       |                             |
| `passing_year_id`                           | Passing Year                                        | `many2one`   |     | ✅    | op.batch                    |
| `payment_token_count`                       | Payment Token Count                                 | `integer`    |     |       |                             |
| `payment_token_ids`                         | Payment Tokens                                      | `one2many`   |     |       | payment.token               |
| `peppol_eas`                                | Peppol e-address (EAS)                              | `selection`  |     |       |                             |
| `peppol_endpoint`                           | Peppol Endpoint                                     | `char`       |     |       |                             |
| `phone`                                     | Phone                                               | `char`       |     |       |                             |
| `phone_blacklisted`                         | Blacklisted Phone is Phone                          | `boolean`    |     |       |                             |
| `phone_mobile_search`                       | Phone Number                                        | `char`       |     |       |                             |
| `phone_sanitized`                           | Sanitized Number                                    | `char`       |     |       |                             |
| `phone_sanitized_blacklisted`               | Phone Blacklisted                                   | `boolean`    |     |       |                             |
| `picking_warn_msg`                          | Message for Stock Picking                           | `text`       |     |       |                             |
| `pin`                                       | PIN                                                 | `char`       |     | ✅    |                             |
| `placement_count`                           | Placement Count                                     | `integer`    |     |       |                             |
| `placement_line`                            | Placement Details                                   | `one2many`   |     | ✅    | op.placement.offer          |
| `properties`                                | Properties                                          | `properties` |     |       |                             |
| `properties_base_definition_id`             | Properties Base Definition                          | `many2one`   |     |       | properties.base.definition  |
| `property_account_payable_id`               | Account Payable                                     | `many2one`   |     |       | account.account             |
| `property_account_position_id`              | Fiscal Position                                     | `many2one`   |     |       | account.fiscal.position     |
| `property_account_receivable_id`            | Account Receivable                                  | `many2one`   |     |       | account.account             |
| `property_delivery_carrier_id`              | Delivery Method                                     | `many2one`   |     |       | delivery.carrier            |
| `property_inbound_payment_method_line_id`   | Property Inbound Payment Method Line                | `many2one`   |     |       | account.payment.method.line |
| `property_outbound_payment_method_line_id`  | Property Outbound Payment Method Line               | `many2one`   |     |       | account.payment.method.line |
| `property_payment_term_id`                  | Customer Payment Terms                              | `many2one`   |     |       | account.payment.term        |
| `property_product_pricelist`                | Pricelist                                           | `many2one`   |     |       | product.pricelist           |
| `property_purchase_currency_id`             | Supplier Currency                                   | `many2one`   |     |       | res.currency                |
| `property_stock_customer`                   | Customer Location                                   | `many2one`   |     |       | stock.location              |
| `property_stock_supplier`                   | Vendor Location                                     | `many2one`   |     |       | stock.location              |
| `property_supplier_payment_term_id`         | Vendor Payment Terms                                | `many2one`   |     |       | account.payment.term        |
| `purchase_line_ids`                         | Purchase Lines                                      | `one2many`   |     |       | purchase.order.line         |
| `purchase_order_count`                      | Purchase Order Count                                | `integer`    |     |       |                             |
| `purchase_warn_msg`                         | Message for Purchase Order                          | `text`       |     |       |                             |
| `rating_ids`                                | Ratings                                             | `one2many`   |     | ✅    | rating.rating               |
| `receipt_reminder_email`                    | Receipt Reminder                                    | `boolean`    |     |       |                             |
| `ref`                                       | Reference                                           | `char`       |     |       |                             |
| `ref_company_ids`                           | Companies that refers to partner                    | `one2many`   |     |       | res.company                 |
| `reminder_date_before_receipt`              | Days Before Receipt                                 | `integer`    |     |       |                             |
| `rtc_session_ids`                           | Rtc Session                                         | `one2many`   |     |       | discuss.channel.rtc.session |
| `sale_order_count`                          | Sale Order Count                                    | `integer`    |     |       |                             |
| `sale_order_ids`                            | Sales Order                                         | `one2many`   |     |       | sale.order                  |
| `sale_warn_msg`                             | Message for Sales Order                             | `text`       |     |       |                             |
| `same_company_registry_partner_id`          | Partner with same Company Registry                  | `many2one`   |     |       | res.partner                 |
| `same_vat_partner_id`                       | Partner with same Tax ID                            | `many2one`   |     |       | res.partner                 |
| `self`                                      | Self                                                | `many2one`   |     |       | res.partner                 |
| `seo_name`                                  | Seo name                                            | `char`       |     |       |                             |
| `show_credit_limit`                         | Show Credit Limit                                   | `boolean`    |     |       |                             |
| `signup_type`                               | Signup Token Type                                   | `char`       |     |       |                             |
| `skill_line`                                | Skills Details                                      | `one2many`   |     | ✅    | op.skill.line               |
| `specific_property_product_pricelist`       | Specific Property Product Pricelist                 | `many2one`   |     |       | product.pricelist           |
| `state`                                     | Status                                              | `selection`  |     | ✅    |                             |
| `state_id`                                  | State                                               | `many2one`   |     |       | res.country.state           |
| `static_map_url`                            | Static Map Url                                      | `char`       |     |       |                             |
| `static_map_url_is_valid`                   | Static Map Url Is Valid                             | `boolean`    |     |       |                             |
| `street`                                    | Street                                              | `char`       |     |       |                             |
| `street2`                                   | Street2                                             | `char`       |     |       |                             |
| `student_badge_ids`                         | Badges                                              | `one2many`   |     | ✅    | op.badge.student            |
| `student_count`                             | Student Count                                       | `integer`    |     | ✅    |                             |
| `student_skill_line`                        | Student Skills                                      | `one2many`   |     | ✅    | op.student.skill.line       |
| `suggest_based_on`                          | Suggest Based On                                    | `char`       |     |       |                             |
| `suggest_days`                              | Suggest Days                                        | `integer`    |     |       |                             |
| `suggest_percent`                           | Suggest Percent                                     | `integer`    |     |       |                             |
| `supplier_invoice_count`                    | # Vendor Bills                                      | `integer`    |     |       |                             |
| `supplier_rank`                             | Supplier Rank                                       | `integer`    |     |       |                             |
| `ticket_count`                              | Ticket Count                                        | `integer`    |     |       |                             |
| `title`                                     | Title                                               | `many2one`   |     |       | res.partner.title           |
| `total_invoiced`                            | Total Invoiced                                      | `monetary`   |     |       |                             |
| `trust`                                     | Degree of trust you have in this debtor             | `selection`  |     |       |                             |
| `type`                                      | Address Type                                        | `selection`  |     |       |                             |
| `type_address_label`                        | Address Type Description                            | `char`       |     |       |                             |
| `tz`                                        | Timezone                                            | `selection`  |     |       |                             |
| `tz_offset`                                 | Timezone offset                                     | `char`       |     |       |                             |
| `use_partner_credit_limit`                  | Partner Limit                                       | `boolean`    |     |       |                             |
| `user_id`                                   | User                                                | `many2one`   |     | ✅    | res.users                   |
| `user_ids`                                  | Users                                               | `one2many`   |     |       | res.users                   |
| `user_livechat_username`                    | User Livechat Username                              | `char`       |     |       |                             |
| `vat`                                       | Tax ID                                              | `char`       |     |       |                             |
| `vat_label`                                 | Tax ID Label                                        | `char`       |     |       |                             |
| `visa_info`                                 | Visa Info                                           | `char`       |     | ✅    |                             |
| `visitor_ids`                               | Visitors                                            | `one2many`   |     |       | website.visitor             |
| `website`                                   | Website Link                                        | `char`       |     |       |                             |
| `website_absolute_url`                      | Website Absolute URL                                | `char`       |     |       |                             |
| `website_description`                       | Website Partner Full Description                    | `html`       |     |       |                             |
| `website_id`                                | Website                                             | `many2one`   |     |       | website                     |
| `website_message_ids`                       | Website Messages                                    | `one2many`   |     | ✅    | mail.message                |
| `website_meta_description`                  | Website meta description                            | `text`       |     |       |                             |
| `website_meta_keywords`                     | Website meta keywords                               | `char`       |     |       |                             |
| `website_meta_og_img`                       | Website opengraph image                             | `char`       |     |       |                             |
| `website_meta_title`                        | Website meta title                                  | `char`       |     |       |                             |
| `website_published`                         | Visible on current website                          | `boolean`    |     |       |                             |
| `website_short_description`                 | Website Partner Short Description                   | `text`       |     |       |                             |
| `website_url`                               | Website URL                                         | `char`       |     |       |                             |
| `wishlist_ids`                              | Wishlist                                            | `one2many`   |     |       | product.wishlist            |
| `write_date`                                | Last Updated on                                     | `datetime`   |     | ✅    |                             |
| `write_uid`                                 | Last Updated by                                     | `many2one`   |     | ✅    | res.users                   |
| `zip`                                       | Zip                                                 | `char`       |     |       |                             |

**Access Rights:**

| Name                    | Group                | Perms     |
| ----------------------- | -------------------- | --------- |
| access_op_student       | Alumni / Manager     | `R/W/C/D` |
| access_op_student_user  | Alumni / User        | `R/W/C`   |
| op_student_student      | OpenEduCat / Manager | `R/W/C/D` |
| op_student_faculty      | OpenEduCat / User    | `R/W`     |
| name_op_student_library | Library / Manager    | `R`       |
| op_student              | Role / Portal        | `R`       |
| op_student_parent       | Role / Portal        | `R`       |
| access_op_student       | Role / Public        | `R/W/C/D` |

**Record Rules:**

- **Student Login rule** (93) `R/W/C/D`
  - Domain: `[('user_id','=',user.id)]`
- **View Students** (92) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Student Parent Login rule** (10) `R/W/C/D`
  - Domain: `['|', ('user_id','=',user.id), ('user_id','in',user.child_ids.ids)]`
- **Student multi-company** (Global) `R/W/C/D`
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

### 🗃️ `assignment.statistics` — Assignment Statistics

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                              | Group             | Perms     |
| --------------------------------- | ----------------- | --------- |
| access_assignment_statistics      | Grading / Manager | `R/W/C/D` |
| access_assignment_statistics_user | Grading / User    | `R/W/C`   |

### 🗃️ `assignment.type.weight.line` — Assignment Type Weight Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label           | Type       | Req | Store | Relation                |
| -------------------- | --------------- | ---------- | --- | ----- | ----------------------- |
| `assignment_type_id` | Assignment Type | `many2one` |     | ✅    | grading.assignment.type |
| `company_id`         | Company         | `many2one` |     | ✅    | res.company             |
| `create_date`        | Created on      | `datetime` |     | ✅    |                         |
| `create_uid`         | Created by      | `many2one` |     | ✅    | res.users               |
| `display_name`       | Display Name    | `char`     |     |       |                         |
| `grade_templates_id` | Grade Template  | `many2one` |     | ✅    | op.grade.template.line  |
| `id`                 | ID              | `integer`  |     | ✅    |                         |
| `weightage`          | Weightage       | `float`    |     | ✅    |                         |
| `write_date`         | Last Updated on | `datetime` |     | ✅    |                         |
| `write_uid`          | Last Updated by | `many2one` |     | ✅    | res.users               |

**Access Rights:**

| Name                                                 | Group             | Perms     |
| ---------------------------------------------------- | ----------------- | --------- |
| access_assignment_type_weight_line_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_assignment_type_weight_line_faculty           | Grading / User    | `R/W/C`   |

**Record Rules:**

- **Assignment Type Weightage Line multi company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `assignment.wizard` — Assignment Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field            | Label           | Type        | Req | Store | Relation           |
| ---------------- | --------------- | ----------- | --- | ----- | ------------------ |
| `assignment_ids` | Assignment      | `many2many` |     | ✅    | grading.assignment |
| `create_date`    | Created on      | `datetime`  |     | ✅    |                    |
| `create_uid`     | Created by      | `many2one`  |     | ✅    | res.users          |
| `display_name`   | Display Name    | `char`      |     |       |                    |
| `id`             | ID              | `integer`   |     | ✅    |                    |
| `write_date`     | Last Updated on | `datetime`  |     | ✅    |                    |
| `write_uid`      | Last Updated by | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                          | Group             | Perms     |
| ----------------------------- | ----------------- | --------- |
| access_assignment_wizard      | Grading / Manager | `R/W/C/D` |
| access_assignment_wizard_user | Grading / User    | `R/W/C`   |

### 🗃️ `attendance.weight.line` — Attendance Weight Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label           | Type        | Req | Store | Relation               |
| -------------------- | --------------- | ----------- | --- | ----- | ---------------------- |
| `attendance_type`    | Attendance Type | `selection` | ✅  | ✅    |                        |
| `company_id`         | Company         | `many2one`  |     | ✅    | res.company            |
| `create_date`        | Created on      | `datetime`  |     | ✅    |                        |
| `create_uid`         | Created by      | `many2one`  |     | ✅    | res.users              |
| `display_name`       | Display Name    | `char`      |     |       |                        |
| `grade_templates_id` | Grade Template  | `many2one`  |     | ✅    | op.grade.template.line |
| `id`                 | ID              | `integer`   |     | ✅    |                        |
| `weightage`          | Weightage       | `float`     | ✅  | ✅    |                        |
| `write_date`         | Last Updated on | `datetime`  |     | ✅    |                        |
| `write_uid`          | Last Updated by | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                                            | Group             | Perms     |
| ----------------------------------------------- | ----------------- | --------- |
| access_attendance_weight_line_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_attendance_weight_line_faculty           | Grading / User    | `R/W/C`   |

**Record Rules:**

- **Attendance Weightage Line multi company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `op.grade.table` — Grade Table

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label           | Type       | Req | Store | Relation            |
| ----------------- | --------------- | ---------- | --- | ----- | ------------------- |
| `active`          | Active          | `boolean`  |     | ✅    |                     |
| `company_id`      | Company         | `many2one` |     | ✅    | res.company         |
| `create_date`     | Created on      | `datetime` |     | ✅    |                     |
| `create_uid`      | Created by      | `many2one` |     | ✅    | res.users           |
| `display_name`    | Display Name    | `char`     |     |       |                     |
| `grade_table_ids` | Grade Lines     | `one2many` | ✅  | ✅    | op.grade.table.line |
| `id`              | ID              | `integer`  |     | ✅    |                     |
| `name`            | Name            | `char`     | ✅  | ✅    |                     |
| `write_date`      | Last Updated on | `datetime` |     | ✅    |                     |
| `write_uid`       | Last Updated by | `many2one` |     | ✅    | res.users           |

**Access Rights:**

| Name                                    | Group             | Perms     |
| --------------------------------------- | ----------------- | --------- |
| access_op_grade_table_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_op_grade_table_faculty           | Grading / User    | `R/W/C`   |

**Record Rules:**

- **Grade Table multi company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `op.grade.table.line` — Grade Table Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label           | Type       | Req | Store | Relation       |
| ---------------- | --------------- | ---------- | --- | ----- | -------------- |
| `company_id`     | Company         | `many2one` |     | ✅    | res.company    |
| `create_date`    | Created on      | `datetime` |     | ✅    |                |
| `create_uid`     | Created by      | `many2one` |     | ✅    | res.users      |
| `display_name`   | Display Name    | `char`     |     |       |                |
| `grade_table_id` | Grade Table     | `many2one` |     | ✅    | op.grade.table |
| `id`             | ID              | `integer`  |     | ✅    |                |
| `name`           | Name            | `char`     | ✅  | ✅    |                |
| `percentage`     | Percentage      | `float`    | ✅  | ✅    |                |
| `write_date`     | Last Updated on | `datetime` |     | ✅    |                |
| `write_uid`      | Last Updated by | `many2one` |     | ✅    | res.users      |

**Access Rights:**

| Name                                         | Group             | Perms     |
| -------------------------------------------- | ----------------- | --------- |
| access_op_grade_table_line_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_op_grade_table_line_faculty           | Grading / User    | `R/W/C`   |

**Record Rules:**

- **Grade Table Line multi company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `op.grade.template.line` — Grade Template Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label             | Type        | Req | Store | Relation                    |
| ---------------------------- | ----------------- | ----------- | --- | ----- | --------------------------- |
| `academic_term_id`           | Terms             | `many2one`  |     | ✅    | op.academic.term            |
| `academic_years_id`          | Academic Year     | `many2one`  | ✅  | ✅    | op.academic.year            |
| `assignment_type_id`         | Assignment Type   | `many2one`  |     | ✅    | grading.assignment.type     |
| `assignment_type_weight_ids` | Assignment Weight | `one2many`  |     | ✅    | assignment.type.weight.line |
| `attendance_type_weight_ids` | Attendance Weight | `one2many`  |     | ✅    | attendance.weight.line      |
| `company_id`                 | Company           | `many2one`  |     | ✅    | res.company                 |
| `create_date`                | Created on        | `datetime`  |     | ✅    |                             |
| `create_uid`                 | Created by        | `many2one`  |     | ✅    | res.users                   |
| `display_name`               | Display Name      | `char`      |     |       |                             |
| `grade_template_id`          | Grade Template    | `many2one`  |     | ✅    | op.grade.template           |
| `id`                         | ID                | `integer`   |     | ✅    |                             |
| `percentage`                 | Percentage        | `float`     |     | ✅    |                             |
| `subterm_weight_ids`         | Subterm Weight    | `one2many`  |     | ✅    | subterm.weight.line         |
| `weightage`                  | Weightage Type    | `selection` | ✅  | ✅    |                             |
| `write_date`                 | Last Updated on   | `datetime`  |     | ✅    |                             |
| `write_uid`                  | Last Updated by   | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                                            | Group             | Perms     |
| ----------------------------------------------- | ----------------- | --------- |
| access_op_grade_template_line_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_op_grade_template_line_faculty           | Grading / User    | `R/W/C`   |

**Record Rules:**

- **Grade Template Line multi company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `op.grade.override.line` — Grading Override Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label           | Type       | Req | Store | Relation            |
| ---------------- | --------------- | ---------- | --- | ----- | ------------------- |
| `assignment_id`  | Assignment      | `many2one` |     | ✅    | grading.assignment  |
| `calculated`     | Calculated      | `char`     |     | ✅    |                     |
| `comment`        | Comment         | `char`     |     | ✅    |                     |
| `company_id`     | Company         | `many2one` |     | ✅    | res.company         |
| `create_date`    | Created on      | `datetime` |     | ✅    |                     |
| `create_uid`     | Created by      | `many2one` |     | ✅    | res.users           |
| `display_name`   | Display Name    | `char`     |     |       |                     |
| `final`          | Final           | `char`     |     | ✅    |                     |
| `grade`          | Grade           | `char`     |     | ✅    |                     |
| `grade_grade_id` | Student         | `many2one` |     | ✅    | gradebook.gradebook |
| `id`             | ID              | `integer`  |     | ✅    |                     |
| `override`       | Override        | `float`    |     | ✅    |                     |
| `subject`        | Subject         | `many2one` |     | ✅    | op.subject          |
| `term`           | Terms           | `many2one` |     | ✅    | op.academic.term    |
| `write_date`     | Last Updated on | `datetime` |     | ✅    |                     |
| `write_uid`      | Last Updated by | `many2one` |     | ✅    | res.users           |
| `year`           | Year            | `many2one` |     | ✅    | op.academic.year    |
| `year_hidden`    | Hidden Year     | `many2one` |     | ✅    | op.academic.year    |

**Access Rights:**

| Name                                            | Group             | Perms     |
| ----------------------------------------------- | ----------------- | --------- |
| access_op_grade_override_line_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_op_grade_override_line_faculty           | Grading / User    | `R/W/C`   |

**Record Rules:**

- **Grade Override Line multi company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `op.grade.type` — Grading Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label              | Type       | Req | Store | Relation       |
| ------------------- | ------------------ | ---------- | --- | ----- | -------------- |
| `company_id`        | Company            | `many2one` |     | ✅    | res.company    |
| `create_date`       | Created on         | `datetime` |     | ✅    |                |
| `create_uid`        | Created by         | `many2one` |     | ✅    | res.users      |
| `display_name`      | Display Name       | `char`     |     |       |                |
| `earn_credits`      | Earn Credits       | `boolean`  |     | ✅    |                |
| `factor`            | Factor             | `float`    |     | ✅    |                |
| `form_factor`       | Form Factor        | `boolean`  |     | ✅    |                |
| `gpa_value`         | GPA                | `float`    |     | ✅    |                |
| `id`                | ID                 | `integer`  |     | ✅    |                |
| `include_gpa`       | Include GPA        | `boolean`  |     | ✅    |                |
| `max_percentage`    | Maximum Percentage | `float`    |     | ✅    |                |
| `min_percentage`    | Minimum Percentage | `float`    |     | ✅    |                |
| `name`              | Name               | `char`     | ✅  | ✅    |                |
| `op_grade_scale_id` | Grade scale        | `many2one` |     | ✅    | op.grade.scale |
| `write_date`        | Last Updated on    | `datetime` |     | ✅    |                |
| `write_uid`         | Last Updated by    | `many2one` |     | ✅    | res.users      |

**Access Rights:**

| Name                                   | Group             | Perms     |
| -------------------------------------- | ----------------- | --------- |
| access_op_grade_type_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_op_grade_type_faculty           | Grading / User    | `R/W/C`   |

**Record Rules:**

- **Grade Type multi company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `grading.wizard` — Grading Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field              | Label           | Type       | Req | Store | Relation         |
| ------------------ | --------------- | ---------- | --- | ----- | ---------------- |
| `academic_year_id` | Academic Year   | `many2one` | ✅  | ✅    | op.academic.year |
| `course_id`        | Course          | `many2one` | ✅  | ✅    | op.course        |
| `create_date`      | Created on      | `datetime` |     | ✅    |                  |
| `create_uid`       | Created by      | `many2one` |     | ✅    | res.users        |
| `display_name`     | Display Name    | `char`     |     |       |                  |
| `id`               | ID              | `integer`  |     | ✅    |                  |
| `write_date`       | Last Updated on | `datetime` |     | ✅    |                  |
| `write_uid`        | Last Updated by | `many2one` |     | ✅    | res.users        |

**Access Rights:**

| Name                       | Group             | Perms     |
| -------------------------- | ----------------- | --------- |
| access_grading_wizard      | Grading / Manager | `R/W/C/D` |
| access_grading_wizard_user | Grading / User    | `R/W/C`   |

### 🗃️ `op.honorroll.line` — Honor Roll Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation         |
| -------------- | --------------- | ---------- | --- | ----- | ---------------- |
| `course_id`    | Course          | `many2one` |     | ✅    | op.course        |
| `create_date`  | Created on      | `datetime` |     | ✅    |                  |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users        |
| `display_name` | Display Name    | `char`     |     |       |                  |
| `honor_id`     | Honor           | `many2one` |     | ✅    | op.honorroll     |
| `id`           | ID              | `integer`  |     | ✅    |                  |
| `percentage`   | Percentage      | `float`    |     | ✅    |                  |
| `student_id`   | Student         | `many2one` |     | ✅    | op.student       |
| `subject_id`   | Subject         | `many2one` |     | ✅    | op.subject       |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                  |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users        |
| `year_id`      | Academic Year   | `many2one` |     | ✅    | op.academic.year |

**Access Rights:**

| Name                                       | Group             | Perms     |
| ------------------------------------------ | ----------------- | --------- |
| access_op_honorroll_line_back_office_admin | Grading / Manager | `R/W/C/D` |
| model_op_honorroll_line_faculty            | Grading / User    | `R/W/C`   |

### 🗃️ `student.statistics` — Student Statistics

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                           | Group             | Perms     |
| ------------------------------ | ----------------- | --------- |
| access_student_statistics      | Grading / Manager | `R/W/C/D` |
| access_student_statistics_user | Grading / User    | `R/W/C`   |

### 🗃️ `student.transcript.wizard` — Student Transcript Generation Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                        | Label                    | Type        | Req | Store | Relation   |
| ---------------------------- | ------------------------ | ----------- | --- | ----- | ---------- |
| `allowed_course_ids`         | Allowed Course           | `many2many` |     |       | op.course  |
| `allowed_program_ids`        | Allowed Program          | `many2many` |     |       | op.program |
| `course_id`                  | Course                   | `many2one`  |     | ✅    | op.course  |
| `create_date`                | Created on               | `datetime`  |     | ✅    |            |
| `create_uid`                 | Created by               | `many2one`  |     | ✅    | res.users  |
| `display_name`               | Display Name             | `char`      |     |       |            |
| `id`                         | ID                       | `integer`   |     | ✅    |            |
| `is_program_base_transcript` | Program Based Transcript | `boolean`   |     | ✅    |            |
| `program_id`                 | Program                  | `many2one`  |     | ✅    | op.program |
| `student_id`                 | Student                  | `many2one`  | ✅  | ✅    | op.student |
| `write_date`                 | Last Updated on          | `datetime`  |     | ✅    |            |
| `write_uid`                  | Last Updated by          | `many2one`  |     | ✅    | res.users  |

**Access Rights:**

| Name                             | Group             | Perms     |
| -------------------------------- | ----------------- | --------- |
| access_student_transcript_wizard | Grading / Manager | `R/W/C/D` |

### 🗃️ `subterm.weight.line` — Sub Term Weight Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label           | Type       | Req | Store | Relation               |
| ---------------------- | --------------- | ---------- | --- | ----- | ---------------------- |
| `academic_sub_term_id` | Sub Terms       | `many2one` | ✅  | ✅    | op.academic.term       |
| `company_id`           | Company         | `many2one` |     | ✅    | res.company            |
| `create_date`          | Created on      | `datetime` |     | ✅    |                        |
| `create_uid`           | Created by      | `many2one` |     | ✅    | res.users              |
| `display_name`         | Display Name    | `char`     |     |       |                        |
| `grade_template_id`    | Grade Template  | `many2one` |     | ✅    | op.grade.template.line |
| `id`                   | ID              | `integer`  |     | ✅    |                        |
| `weightage`            | Weightage       | `float`    |     | ✅    |                        |
| `write_date`           | Last Updated on | `datetime` |     | ✅    |                        |
| `write_uid`            | Last Updated by | `many2one` |     | ✅    | res.users              |

**Access Rights:**

| Name                                         | Group             | Perms     |
| -------------------------------------------- | ----------------- | --------- |
| access_subterm_weight_line_back_office_admin | Grading / Manager | `R/W/C/D` |
| access_subterm_weight_line_faculty           | Grading / User    | `R/W/C`   |

**Record Rules:**

- **Subterm Weightage Line multi company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `
