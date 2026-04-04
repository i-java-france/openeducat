---
title: "OpenEducat Thesis Management"
module: "openeducat_thesis"
state: "installed"
version: "19.0.1.0.0"
author: "OpenEducat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "LGPL-3"
category: "Education"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________, odoo/app]
---

# 🟢 OpenEducat Thesis Management

> **Module:** `openeducat_thesis` | **Version:** `19.0.1.0.0` **Category:** Education |
> **License:** `LGPL-3` **Author:** OpenEducat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_core]] [[openeducat_core_enterprise]] [[mail]] [[portal]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `Thesis`
- `Thesis/Configuration`
- `Thesis/Configuration/Committee Members`
- `Thesis/Configuration/Evaluation Templates`
- `Thesis/Configuration/Extension Reasons`
- `Thesis/Configuration/Report Types`
- `Thesis/Thesis Management`
- `Thesis/Thesis Management/Extension Requests`
- `Thesis/Thesis Management/Progress Reports`
- `Thesis/Thesis Management/Registrations`
- `Thesis/Thesis Management/Submissions`

### Views

- `* INHERIT Portal layout : Thesis Detail (qweb)`
- `* INHERIT Portal layout : Thesis Home (qweb)`
- `* INHERIT Portal layout : Thesis Registration Form (qweb)`
- `* INHERIT Show Thesis (qweb)`
- `* INHERIT op.program.form.thesis (form)`
- `My Thesis (qweb)`
- `My Thesis Details (qweb)`
- `op.thesis.committee.assign.form (form)`
- `op.thesis.committee.form (form)`
- `op.thesis.committee.list (list)`
- `op.thesis.committee.search (search)`
- `op.thesis.evaluation.form (form)`
- `op.thesis.evaluation.list (list)`
- `op.thesis.evaluation.parameter.form (form)`
- `op.thesis.evaluation.parameter.list (list)`
- `op.thesis.examiner.invite.form (form)`
- `op.thesis.extension.form (form)`
- `op.thesis.extension.graph (graph)`
- `op.thesis.extension.list (list)`
- `op.thesis.extension.pivot (pivot)`
- `op.thesis.extension.reason.form (form)`
- `op.thesis.extension.reason.list (list)`
- `op.thesis.extension.search (search)`
- `op.thesis.progress.feedback.form (form)`
- `op.thesis.progress.form (form)`
- `op.thesis.progress.graph (graph)`
- `op.thesis.progress.list (list)`
- `op.thesis.progress.pivot (pivot)`
- `op.thesis.progress.search (search)`
- `op.thesis.registration.form (form)`
- `op.thesis.registration.graph (graph)`
- `op.thesis.registration.kanban (kanban)`
- `op.thesis.registration.list (list)`
- `op.thesis.registration.pivot (pivot)`
- `op.thesis.registration.search (search)`
- `op.thesis.report.type.form (form)`
- `op.thesis.report.type.list (list)`
- `op.thesis.submission.form (form)`
- `op.thesis.submission.graph (graph)`
- `op.thesis.submission.list (list)`
- `op.thesis.submission.pivot (pivot)`
- `op.thesis.submission.search (search)`
- `openeducat_thesis_registration (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**14 model(s) defined by this module:**

### 🗃️ `op.thesis.evaluation.template` — Thesis Evaluation

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                       |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------------ |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event                 |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                                |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                                |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                                |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity                  |
| `activity_state`                | Activity State                | `selection` |     |       |                                |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                                |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                                |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type             |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users                      |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                                |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users                      |
| `display_name`                  | Display Name                  | `char`      |     |       |                                |
| `has_grading_history`           | Has Grading History           | `boolean`   |     |       |                                |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                                |
| `id`                            | ID                            | `integer`   |     | ✅    |                                |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                                |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers                 |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                                |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                                |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                                |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message                   |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                                |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                                |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                                |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner                    |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                                |
| `name`                          | Name                          | `char`      | ✅  | ✅    |                                |
| `parameter_line`                | Parameters                    | `one2many`  | ✅  | ✅    | op.thesis.evaluation.parameter |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating                  |
| `state`                         | Status                        | `selection` |     | ✅    |                                |
| `total_marks`                   | Total Marks                   | `integer`   |     | ✅    |                                |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message                   |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                                |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users                      |

**Access Rights:**

| Name                                 | Group       | Perms     |
| ------------------------------------ | ----------- | --------- |
| access_op_thesis_evaluation_template | Role / User | `R/W/C/D` |

### 🗃️ `op.thesis.extension` — Thesis Extension Request

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                   |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | -------------------------- |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event             |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                            |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                            |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                            |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity              |
| `activity_state`                | Activity State                | `selection` |     |       |                            |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                            |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                            |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type         |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users                  |
| `attachment_ids`                | Supporting Documents          | `many2many` |     | ✅    | ir.attachment              |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                            |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users                  |
| `current_deadline`              | Current Deadline              | `date`      |     | ✅    |                            |
| `display_name`                  | Display Name                  | `char`      |     |       |                            |
| `extension_duration`            | Extension Days                | `integer`   |     | ✅    |                            |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                            |
| `hod_approval`                  | HoD Approved                  | `boolean`   |     | ✅    |                            |
| `hod_comment`                   | HoD Comment                   | `text`      |     | ✅    |                            |
| `hod_id`                        | Head of Department            | `many2one`  |     | ✅    | op.faculty                 |
| `id`                            | ID                            | `integer`   |     | ✅    |                            |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                            |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers             |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                            |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                            |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                            |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message               |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                            |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                            |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                            |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner                |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                            |
| `name`                          | Reference                     | `char`      |     | ✅    |                            |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating              |
| `reason_details`                | Detailed Reason               | `text`      | ✅  | ✅    |                            |
| `reason_id`                     | Reason                        | `many2one`  | ✅  | ✅    | op.thesis.extension.reason |
| `registration_id`               | Thesis Registration           | `many2one`  | ✅  | ✅    | op.thesis.registration     |
| `request_date`                  | Request Date                  | `date`      | ✅  | ✅    |                            |
| `requested_deadline`            | Requested Deadline            | `date`      | ✅  | ✅    |                            |
| `state`                         | Status                        | `selection` |     | ✅    |                            |
| `student_id`                    | Student                       | `many2one`  |     | ✅    | op.student                 |
| `supervisor_approval`           | Supervisor Approved           | `boolean`   |     | ✅    |                            |
| `supervisor_comment`            | Supervisor Comment            | `text`      |     | ✅    |                            |
| `supervisor_id`                 | Supervisor                    | `many2one`  |     | ✅    | op.faculty                 |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message               |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                            |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users                  |

**Access Rights:**

| Name                           | Group                         | Perms     |
| ------------------------------ | ----------------------------- | --------- |
| op.thesis.extension.admin      | Thesis / Thesis Administrator | `R/W/C/D` |
| op.thesis.extension.hod        | Thesis / Thesis HoD           | `R/W/C`   |
| op.thesis.extension.supervisor | Thesis / Thesis Supervisor    | `R/W`     |
| op.thesis.extension.student    | Role / Portal                 | `R/W/C`   |

### 🗃️ `op.program` — Thesis Program

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                    | Type        | Req | Store | Relation                      |
| ---------------------------- | ------------------------ | ----------- | --- | ----- | ----------------------------- |
| `active`                     | Active                   | `boolean`   |     | ✅    |                               |
| `admission_count`            | Admission Count          | `integer`   |     |       |                               |
| `area_id`                    | Area                     | `many2one`  |     | ✅    | op.area                       |
| `batch_count`                | Batch Count              | `integer`   |     |       |                               |
| `code`                       | Code                     | `char`      | ✅  | ✅    |                               |
| `color`                      | Color Index              | `integer`   |     | ✅    |                               |
| `company_id`                 | Company                  | `many2one`  |     | ✅    | res.company                   |
| `course_count`               | Course Count             | `integer`   |     |       |                               |
| `create_date`                | Created on               | `datetime`  |     | ✅    |                               |
| `create_uid`                 | Created by               | `many2one`  |     | ✅    | res.users                     |
| `department_id`              | Department               | `many2one`  |     | ✅    | op.department                 |
| `display_name`               | Display Name             | `char`      |     |       |                               |
| `evaluation_template_id`     | Evaluation Template      | `many2one`  |     | ✅    | op.thesis.evaluation.template |
| `full_description`           | Full Description         | `html`      |     | ✅    |                               |
| `has_message`                | Has Message              | `boolean`   |     |       |                               |
| `id`                         | ID                       | `integer`   |     | ✅    |                               |
| `image_1920`                 | Image                    | `binary`    |     | ✅    |                               |
| `max_unit_load`              | Maximum Unit Load        | `float`     |     | ✅    |                               |
| `message_attachment_count`   | Attachment Count         | `integer`   |     |       |                               |
| `message_follower_ids`       | Followers                | `one2many`  |     | ✅    | mail.followers                |
| `message_has_error`          | Message Delivery error   | `boolean`   |     |       |                               |
| `message_has_error_counter`  | Number of errors         | `integer`   |     |       |                               |
| `message_has_sms_error`      | SMS Delivery error       | `boolean`   |     |       |                               |
| `message_ids`                | Messages                 | `one2many`  |     | ✅    | mail.message                  |
| `message_is_follower`        | Is Follower              | `boolean`   |     |       |                               |
| `message_needaction`         | Action Needed            | `boolean`   |     |       |                               |
| `message_needaction_counter` | Number of Actions        | `integer`   |     |       |                               |
| `message_partner_ids`        | Followers (Partners)     | `many2many` |     |       | res.partner                   |
| `min_unit_load`              | Minimum Unit Load        | `float`     |     | ✅    |                               |
| `name`                       | Name                     | `char`      | ✅  | ✅    |                               |
| `program_level_id`           | Program Level            | `many2one`  | ✅  | ✅    | op.program.level              |
| `program_sessions_count`     | Session Count            | `integer`   |     |       |                               |
| `rating_ids`                 | Ratings                  | `one2many`  |     | ✅    | rating.rating                 |
| `required_thesis`            | Required Thesis          | `boolean`   |     | ✅    |                               |
| `short_desc`                 | Short Description        | `text`      |     | ✅    |                               |
| `student_count`              | Student Count            | `integer`   |     |       |                               |
| `subject_count`              | Subject Count            | `integer`   |     |       |                               |
| `thesis_duration`            | Thesis Duration (months) | `integer`   |     | ✅    |                               |
| `thesis_guidelines`          | Thesis Guidelines        | `html`      |     | ✅    |                               |
| `user_id`                    | User                     | `many2one`  |     | ✅    | res.users                     |
| `website_message_ids`        | Website Messages         | `one2many`  |     | ✅    | mail.message                  |
| `write_date`                 | Last Updated on          | `datetime`  |     | ✅    |                               |
| `write_uid`                  | Last Updated by          | `many2one`  |     | ✅    | res.users                     |

**Access Rights:**

| Name                                | Group                | Perms     |
| ----------------------------------- | -------------------- | --------- |
| access_op_program_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_op_program_faculty           | OpenEduCat / User    | `R`       |

**Record Rules:**

- **Program multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `op.thesis.progress` — Thesis Progress Report

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation               |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ---------------------- |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event         |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                        |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                        |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                        |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity          |
| `activity_state`                | Activity State                | `selection` |     |       |                        |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                        |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                        |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type     |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users              |
| `attachment_ids`                | Attachments                   | `many2many` |     | ✅    | ir.attachment          |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                        |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users              |
| `display_name`                  | Display Name                  | `char`      |     |       |                        |
| `feedback_date`                 | Feedback Date                 | `date`      |     | ✅    |                        |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                        |
| `id`                            | ID                            | `integer`   |     | ✅    |                        |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                        |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers         |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                        |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                        |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                        |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message           |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                        |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                        |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                        |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner            |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                        |
| `name`                          | Report Title                  | `char`      | ✅  | ✅    |                        |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating          |
| `registration_id`               | Thesis Registration           | `many2one`  | ✅  | ✅    | op.thesis.registration |
| `report_content`                | Report Content                | `html`      | ✅  | ✅    |                        |
| `report_date`                   | Report Date                   | `date`      | ✅  | ✅    |                        |
| `report_id`                     | Report Type                   | `many2one`  | ✅  | ✅    | op.thesis.report.type  |
| `reviewer_ids`                  | Additional Reviewers          | `many2many` |     | ✅    | op.thesis.committee    |
| `state`                         | Status                        | `selection` |     | ✅    |                        |
| `student_id`                    | Student                       | `many2one`  |     | ✅    | op.student             |
| `supervisor_feedback`           | Supervisor Feedback           | `html`      |     | ✅    |                        |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message           |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                        |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                          | Group                         | Perms     |
| ----------------------------- | ----------------------------- | --------- |
| op.thesis.progress.admin      | Thesis / Thesis Administrator | `R/W/C/D` |
| op.thesis.progress.hod        | Thesis / Thesis HoD           | `R/W/C`   |
| op.thesis.progress.supervisor | Thesis / Thesis Supervisor    | `R/W/C`   |
| op.thesis.progress.student    | Role / Portal                 | `R/W/C`   |

### 🗃️ `op.thesis.registration` — Thesis Registration

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation             |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | -------------------- |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event       |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                      |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                      |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                      |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity        |
| `activity_state`                | Activity State                | `selection` |     |       |                      |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                      |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                      |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type   |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users            |
| `available_program_ids`         | Available Program             | `many2many` |     |       | op.program           |
| `code`                          | Code                          | `char`      |     | ✅    |                      |
| `color`                         | Color Index                   | `integer`   |     | ✅    |                      |
| `committee_ids`                 | Committee Members             | `one2many`  |     | ✅    | op.thesis.committee  |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                      |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users            |
| `default_submission_deadline`   | Default Deadline              | `date`      |     | ✅    |                      |
| `department_id`                 | Department                    | `many2one`  |     |       | op.department        |
| `display_name`                  | Display Name                  | `char`      |     |       |                      |
| `extension_count`               | Extensions                    | `integer`   |     |       |                      |
| `extension_ids`                 | Extension Requests            | `one2many`  |     | ✅    | op.thesis.extension  |
| `final_submission_deadline`     | Approved Deadline             | `date`      |     | ✅    |                      |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                      |
| `has_supervisor`                | Has Supervisor and Examiner   | `boolean`   |     | ✅    |                      |
| `id`                            | ID                            | `integer`   |     | ✅    |                      |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                      |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers       |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                      |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                      |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                      |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message         |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                      |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                      |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                      |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner          |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                      |
| `name`                          | Title                         | `char`      | ✅  | ✅    |                      |
| `program_duration_months`       | Thesis Duration (months)      | `integer`   |     |       |                      |
| `program_id`                    | Program                       | `many2one`  | ✅  | ✅    | op.program           |
| `progress_count`                | Progress Report               | `integer`   |     |       |                      |
| `progress_report_count`         | Progress Report Count         | `integer`   |     | ✅    |                      |
| `progress_report_ids`           | Progress Reports              | `one2many`  |     | ✅    | op.thesis.progress   |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating        |
| `registration_date`             | Registration Date             | `date`      |     | ✅    |                      |
| `research_area`                 | Research Area                 | `many2one`  | ✅  | ✅    | op.area              |
| `state`                         | Status                        | `selection` |     | ✅    |                      |
| `student_id`                    | Student                       | `many2one`  | ✅  | ✅    | op.student           |
| `submission_id`                 | Thesis Submission             | `many2one`  |     | ✅    | op.thesis.submission |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message         |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                      |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                              | Group                         | Perms     |
| --------------------------------- | ----------------------------- | --------- |
| op.thesis.registration.admin      | Thesis / Thesis Administrator | `R/W/C/D` |
| op.thesis.registration.hod        | Thesis / Thesis HoD           | `R/W/C`   |
| op.thesis.registration.supervisor | Thesis / Thesis Supervisor    | `R/W/C`   |
| op.thesis.registration.student    | Role / Portal                 | `R/W/C`   |

### 🗃️ `op.thesis.submission` — Thesis Submission

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                             |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------------------ |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event                       |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                                      |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                                      |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                                      |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity                        |
| `activity_state`                | Activity State                | `selection` |     |       |                                      |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                                      |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                                      |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type                   |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users                            |
| `additonal_file`                | Additonal Document            | `binary`    |     | ✅    |                                      |
| `additonal_filename`            | Document Name                 | `char`      |     | ✅    |                                      |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                                      |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users                            |
| `display_name`                  | Display Name                  | `char`      |     |       |                                      |
| `evaluation_date`               | Evaluation Date               | `date`      |     | ✅    |                                      |
| `evaluation_lines`              | Evaluation Lines              | `one2many`  |     | ✅    | op.thesis.submission.evaluation.line |
| `evaluation_template_id`        | Evaluation Template           | `many2one`  |     | ✅    | op.thesis.evaluation.template        |
| `examiner_id`                   | Examiner                      | `many2one`  |     | ✅    | op.thesis.committee                  |
| `has_examiner_assigned`         | Examiner Assigned             | `boolean`   |     | ✅    |                                      |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                                      |
| `id`                            | ID                            | `integer`   |     | ✅    |                                      |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                                      |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers                       |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                                      |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                                      |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                                      |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message                         |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                                      |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                                      |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                                      |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner                          |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                                      |
| `name`                          | Reference                     | `char`      |     | ✅    |                                      |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating                        |
| `registration_id`               | Thesis Registration           | `many2one`  | ✅  | ✅    | op.thesis.registration               |
| `revision_comments`             | Revision Comments             | `text`      |     | ✅    |                                      |
| `state`                         | Status                        | `selection` |     | ✅    |                                      |
| `student_id`                    | Student                       | `many2one`  |     | ✅    | op.student                           |
| `submission_date`               | Submission Date               | `date`      |     | ✅    |                                      |
| `thesis_file`                   | Thesis Document               | `binary`    | ✅  | ✅    |                                      |
| `thesis_filename`               | Filename                      | `char`      |     | ✅    |                                      |
| `title`                         | Final Title                   | `char`      | ✅  | ✅    |                                      |
| `total_score`                   | Total Score                   | `float`     |     | ✅    |                                      |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message                         |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                                      |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users                            |

**Access Rights:**

| Name                            | Group                         | Perms     |
| ------------------------------- | ----------------------------- | --------- |
| op.thesis.submission.admin      | Thesis / Thesis Administrator | `R/W/C/D` |
| op.thesis.submission.hod        | Thesis / Thesis HoD           | `R/W/C`   |
| op.thesis.submission.supervisor | Thesis / Thesis Supervisor    | `R/W/C`   |
| op.thesis.submission.student    | Role / Portal                 | `R/W/C`   |

### 🗃️ `op.thesis.committee.assign.wizard` — Assign Committee Members Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field             | Label               | Type        | Req | Store | Relation               |
| ----------------- | ------------------- | ----------- | --- | ----- | ---------------------- |
| `create_date`     | Created on          | `datetime`  |     | ✅    |                        |
| `create_uid`      | Created by          | `many2one`  |     | ✅    | res.users              |
| `display_name`    | Display Name        | `char`      |     |       |                        |
| `email`           | Email               | `char`      |     | ✅    |                        |
| `faculty_id`      | Faculty Member      | `many2one`  | ✅  | ✅    | op.faculty             |
| `id`              | ID                  | `integer`   |     | ✅    |                        |
| `phone`           | Phone               | `char`      |     | ✅    |                        |
| `registration_id` | Thesis Registration | `many2one`  | ✅  | ✅    | op.thesis.registration |
| `role`            | Role                | `selection` | ✅  | ✅    |                        |
| `write_date`      | Last Updated on     | `datetime`  |     | ✅    |                        |
| `write_uid`       | Last Updated by     | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                                     | Group                         | Perms     |
| ---------------------------------------- | ----------------------------- | --------- |
| access_op_thesis_committee_assign_wizard | Thesis / Thesis Administrator | `R/W/C/D` |

### 🗃️ `op.thesis.examiner.invite.wizard` — Invite Thesis Examiner Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field           | Label             | Type        | Req | Store | Relation             |
| --------------- | ----------------- | ----------- | --- | ----- | -------------------- |
| `create_date`   | Created on        | `datetime`  |     | ✅    |                      |
| `create_uid`    | Created by        | `many2one`  |     | ✅    | res.users            |
| `display_name`  | Display Name      | `char`      |     |       |                      |
| `email`         | Email             | `char`      | ✅  | ✅    |                      |
| `faculty_id`    | Faculty Member    | `many2one`  |     | ✅    | op.faculty           |
| `id`            | ID                | `integer`   |     | ✅    |                      |
| `name`          | Name              | `char`      |     | ✅    |                      |
| `phone`         | Phone             | `char`      |     | ✅    |                      |
| `role`          | Role              | `selection` | ✅  | ✅    |                      |
| `submission_id` | Thesis Submission | `many2one`  | ✅  | ✅    | op.thesis.submission |
| `write_date`    | Last Updated on   | `datetime`  |     | ✅    |                      |
| `write_uid`     | Last Updated by   | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                                    | Group                         | Perms     |
| --------------------------------------- | ----------------------------- | --------- |
| access_op_thesis_examiner_invite_wizard | Thesis / Thesis Administrator | `R/W/C/D` |

### 🗃️ `op.thesis.committee` — Thesis Committee Member

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label               | Type        | Req | Store | Relation               |
| ----------------- | ------------------- | ----------- | --- | ----- | ---------------------- |
| `create_date`     | Created on          | `datetime`  |     | ✅    |                        |
| `create_uid`      | Created by          | `many2one`  |     | ✅    | res.users              |
| `display_name`    | Display Name        | `char`      |     |       |                        |
| `email`           | Email               | `char`      |     | ✅    |                        |
| `faculty_id`      | Faculty Member      | `many2one`  | ✅  | ✅    | op.faculty             |
| `id`              | ID                  | `integer`   |     | ✅    |                        |
| `phone`           | Phone               | `char`      |     | ✅    |                        |
| `registration_id` | Thesis Registration | `many2one`  | ✅  | ✅    | op.thesis.registration |
| `role`            | Role                | `selection` | ✅  | ✅    |                        |
| `write_date`      | Last Updated on     | `datetime`  |     | ✅    |                        |
| `write_uid`       | Last Updated by     | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                           | Group                         | Perms     |
| ------------------------------ | ----------------------------- | --------- |
| op.thesis.committee.admin      | Thesis / Thesis Administrator | `R/W/C/D` |
| op.thesis.committee.hod        | Thesis / Thesis HoD           | `R/W/C/D` |
| op.thesis.committee.supervisor | Thesis / Thesis Supervisor    | `R/W/C`   |
| op.thesis.committee.student    | Role / Portal                 | `R`       |

### 🗃️ `op.thesis.evaluation.parameter` — Thesis Evaluation Parameter

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label           | Type       | Req | Store | Relation                      |
| --------------- | --------------- | ---------- | --- | ----- | ----------------------------- |
| `create_date`   | Created on      | `datetime` |     | ✅    |                               |
| `create_uid`    | Created by      | `many2one` |     | ✅    | res.users                     |
| `display_name`  | Display Name    | `char`     |     |       |                               |
| `evaluation_id` | Evaluation      | `many2one` |     | ✅    | op.thesis.evaluation.template |
| `id`            | ID              | `integer`  |     | ✅    |                               |
| `max_marks`     | Max Marks       | `integer`  |     | ✅    |                               |
| `name`          | Parameter Name  | `char`     | ✅  | ✅    |                               |
| `write_date`    | Last Updated on | `datetime` |     | ✅    |                               |
| `write_uid`     | Last Updated by | `many2one` |     | ✅    | res.users                     |

**Access Rights:**

| Name                                  | Group       | Perms     |
| ------------------------------------- | ----------- | --------- |
| access_op_thesis_evaluation_parameter | Role / User | `R/W/C/D` |

### 🗃️ `op.thesis.extension.reason` — Thesis Extension Reason

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `code`         | Code            | `char`     | ✅  | ✅    |           |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Reason Name     | `char`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                              | Group       | Perms     |
| --------------------------------- | ----------- | --------- |
| access_op_thesis_extension_reason | Role / User | `R/W/C/D` |

### 🗃️ `op.thesis.progress.feedback.wizard` — Thesis Progress Feedback Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field            | Label           | Type        | Req | Store | Relation           |
| ---------------- | --------------- | ----------- | --- | ----- | ------------------ |
| `create_date`    | Created on      | `datetime`  |     | ✅    |                    |
| `create_uid`     | Created by      | `many2one`  |     | ✅    | res.users          |
| `display_name`   | Display Name    | `char`      |     |       |                    |
| `feedback`       | Feedback        | `html`      | ✅  | ✅    |                    |
| `id`             | ID              | `integer`   |     | ✅    |                    |
| `progress_id`    | Progress Report | `many2one`  | ✅  | ✅    | op.thesis.progress |
| `recommendation` | Recommendation  | `selection` | ✅  | ✅    |                    |
| `write_date`     | Last Updated on | `datetime`  |     | ✅    |                    |
| `write_uid`      | Last Updated by | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                      | Group                         | Perms     |
| ----------------------------------------- | ----------------------------- | --------- |
| access_op_thesis_progress_feedback_wizard | Thesis / Thesis Administrator | `R/W/C/D` |

### 🗃️ `op.thesis.report.type` — Thesis Report Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `code`         | Code            | `char`     | ✅  | ✅    |           |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Report Type     | `char`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                         | Group       | Perms     |
| ---------------------------- | ----------- | --------- |
| access_op_thesis_report_type | Role / User | `R/W/C/D` |

### 🗃️ `op.thesis.submission.evaluation.line` — Thesis Submission Evaluation Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label           | Type       | Req | Store | Relation                       |
| --------------- | --------------- | ---------- | --- | ----- | ------------------------------ |
| `create_date`   | Created on      | `datetime` |     | ✅    |                                |
| `create_uid`    | Created by      | `many2one` |     | ✅    | res.users                      |
| `display_name`  | Display Name    | `char`     |     |       |                                |
| `id`            | ID              | `integer`  |     | ✅    |                                |
| `max_marks`     | Max Score       | `integer`  |     |       |                                |
| `parameter_id`  | Parameter       | `many2one` | ✅  | ✅    | op.thesis.evaluation.parameter |
| `score`         | Score           | `integer`  |     | ✅    |                                |
| `submission_id` | Submission      | `many2one` | ✅  | ✅    | op.thesis.submission           |
| `write_date`    | Last Updated on | `datetime` |     | ✅    |                                |
| `write_uid`     | Last Updated by | `many2one` |     | ✅    | res.users                      |

**Access Rights:**

| Name                                        | Group       | Perms     |
| ------------------------------------------- | ----------- | --------- |
| access_op_thesis_submission_evaluation_line | Role / User | `R/W/C/D` |
