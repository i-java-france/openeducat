---
title: "OpenEduCat Fees Plan"
module: "openeducat_fees_plan"
state: "installed"
version: "19.0.0.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Education"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 OpenEduCat Fees Plan

> **Module:** `openeducat_fees_plan` | **Version:** `19.0.0.0` **Category:** Education |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_fees]] [[openeducat_core_enterprise]] [[openeducat_attendance_enterprise]]
[[openeducat_admission_enterprise]] [[openeducat_onboarding]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `SIS/General/Fees`
- `SIS/General/Fees/Fees Plan`
- `SIS/General/Fees/Fees Plan Lines`

### Views

- `* INHERIT kanban.view.inherit (kanban)`
- `* INHERIT op.academic.plan.form.fees (form)`
- `* INHERIT op.faculty.form (form)`
- `* INHERIT op.fees.terms.form.inherited (form)`
- `* INHERIT op.fees.terms.tree.view (list)`
- `* INHERIT op.student.course.form.inherit (form)`
- `* INHERIT op.student.form.fees.plan.inherit (form)`
- `* INHERIT student_portal_fees_collection_details (qweb)`
- `advance_report_fees_analysis (qweb)`
- `advance_report_fees_analysis_document (qweb)`
- `op.fees.element.plan.form (form)`
- `op.fees.element.plan.list (list)`
- `op.fees.plan.form (form)`
- `op.fees.plan.line.form (form)`
- `op.fees.plan.line.list (list)`
- `op.fees.plan.list (list)`
- `op.fees.plan.search (search)`

### Reports

- `Fees Report`

## 🛠️ Technical Documentation

**14 model(s) defined by this module:**

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

### 🗃️ `op.fees.plan` — Fees Plan for Student Fees

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation          |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ----------------- |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company       |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                   |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users         |
| `display_name`               | Display Name           | `char`      |     |       |                   |
| `fees_plan_line_ids`         | Lines                  | `one2many`  |     | ✅    | op.fees.plan.line |
| `fees_term_id`               | Fees Terms             | `many2one`  |     | ✅    | op.fees.terms     |
| `has_message`                | Has Message            | `boolean`   |     |       |                   |
| `id`                         | ID                     | `integer`   |     | ✅    |                   |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                   |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers    |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                   |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                   |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                   |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message      |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                   |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                   |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                   |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner       |
| `name`                       | Fees Plan              | `char`      |     | ✅    |                   |
| `paid_amount`                | Paid Amount            | `float`     |     |       |                   |
| `product_id`                 | Course Fees            | `many2one`  | ✅  | ✅    | product.product   |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating     |
| `remaining_amount`           | Remaining Amount       | `float`     |     | ✅    |                   |
| `state`                      | Status                 | `selection` |     | ✅    |                   |
| `student_id`                 | Student                | `many2one`  |     | ✅    | op.student        |
| `total_amount`               | Total Amount           | `float`     |     | ✅    |                   |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message      |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                   |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                                     | Group                | Perms     |
| ---------------------------------------- | -------------------- | --------- |
| access_op_fees_plan_op_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_op_fees_plan_user                 | OpenEduCat / User    | `R`       |
| access_op_fees_plan_portal               | Role / Portal        | `R`       |

**Record Rules:**

- **Fees Plan multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.fees.terms` — Fees Terms For Course

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
| `bill_selection`             | Bill Every             | `selection` |     | ✅    |                    |
| `code`                       | Code                   | `char`      | ✅  | ✅    |                    |
| `company_id`                 | Company                | `many2one`  | ✅  | ✅    | res.company        |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                    |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users          |
| `day_type`                   | Type                   | `selection` |     | ✅    |                    |
| `discount`                   | Discount (%)           | `float`     |     | ✅    |                    |
| `display_name`               | Display Name           | `char`      |     |       |                    |
| `expires_after`              | Invoice Cycles         | `integer`   |     | ✅    |                    |
| `fees_terms`                 | Term Type              | `selection` |     | ✅    |                    |
| `has_message`                | Has Message            | `boolean`   |     |       |                    |
| `id`                         | ID                     | `integer`   |     | ✅    |                    |
| `line_ids`                   | Terms                  | `one2many`  |     | ✅    | op.fees.terms.line |
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
| `name`                       | Name                   | `char`      | ✅  | ✅    |                    |
| `no_days`                    | No of Days             | `integer`   |     | ✅    |                    |
| `note`                       | Description            | `text`      |     | ✅    |                    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating      |
| `term_duration`              | Term Duration          | `integer`   |     | ✅    |                    |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message       |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                    |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                | Group          | Perms     |
| ----------------------------------- | -------------- | --------- |
| name_op_fees_terms_backoffice_admin | Fees / Manager | `R/W/C/D` |
| name_op_fees_terms_faculty          | Fees / User    | `R/W/C`   |

**Record Rules:**

- **Fees Terms multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

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

### 🗃️ `op.faculty` — OpenEduCat Faculty

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
| `active`                                    | Active                                              | `boolean`    |     | ✅    |                             |
| `active_lang_count`                         | Active Lang Count                                   | `integer`    |     |       |                             |
| `activity_calendar_event_id`                | Next Activity Calendar Event                        | `many2one`   |     |       | calendar.event              |
| `activity_date_deadline`                    | Next Activity Deadline                              | `date`       |     |       |                             |
| `activity_exception_decoration`             | Activity Exception Decoration                       | `selection`  |     |       |                             |
| `activity_exception_icon`                   | Icon                                                | `char`       |     |       |                             |
| `activity_ids`                              | Activities                                          | `one2many`   |     | ✅    | mail.activity               |
| `activity_state`                            | Activity State                                      | `selection`  |     |       |                             |
| `activity_summary`                          | Next Activity Summary                               | `char`       |     |       |                             |
| `activity_type_icon`                        | Activity Type Icon                                  | `char`       |     |       |                             |
| `activity_type_id`                          | Next Activity Type                                  | `many2one`   |     |       | mail.activity.type          |
| `activity_user_id`                          | Responsible User                                    | `many2one`   |     |       | res.users                   |
| `allowed_department_ids`                    | Allowed Department                                  | `many2many`  |     | ✅    | op.department               |
| `applicant_ids`                             | Applicants                                          | `one2many`   |     |       | hr.applicant                |
| `application_count`                         | Applications                                        | `integer`    |     |       |                             |
| `application_statistics`                    | Stats                                               | `json`       |     |       |                             |
| `assignment_count`                          | Assignment Count                                    | `integer`    |     |       |                             |
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
| `barcode`                                   | Barcode                                             | `char`       |     |       |                             |
| `bio_data`                                  | Bio Data                                            | `html`       |     | ✅    |                             |
| `birth_date`                                | Birth Date                                          | `date`       | ✅  | ✅    |                             |
| `blood_group`                               | Blood Group                                         | `selection`  |     | ✅    |                             |
| `buyer_id`                                  | Buyer                                               | `many2one`   |     |       | res.users                   |
| `calendar_last_notif_ack`                   | Last notification marked as read from base Calendar | `datetime`   |     |       |                             |
| `can_publish`                               | Can Publish                                         | `boolean`    |     |       |                             |
| `category_id`                               | Tags                                                | `many2many`  |     |       | res.partner.category        |
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
| `course_count`                              | Course Count                                        | `integer`    |     |       |                             |
| `create_date`                               | Created on                                          | `datetime`   |     | ✅    |                             |
| `create_uid`                                | Created by                                          | `many2one`   |     | ✅    | res.users                   |
| `credit`                                    | Total Receivable                                    | `monetary`   |     |       |                             |
| `credit_limit`                              | Credit Limit                                        | `float`      |     |       |                             |
| `credit_to_invoice`                         | Credit To Invoice                                   | `monetary`   |     |       |                             |
| `currency_id`                               | Currency                                            | `many2one`   |     |       | res.currency                |
| `customer_rank`                             | Customer Rank                                       | `integer`    |     |       |                             |
| `days_sales_outstanding`                    | Days Sales Outstanding (DSO)                        | `float`      |     |       |                             |
| `debit`                                     | Total Payable                                       | `monetary`   |     |       |                             |
| `designation`                               | Designation                                         | `char`       |     | ✅    |                             |
| `display_invoice_edi_format`                | Display Invoice Edi Format                          | `boolean`    |     |       |                             |
| `display_invoice_template_pdf_report_id`    | Display Invoice Template Pdf Report                 | `boolean`    |     |       |                             |
| `display_name`                              | Display Name                                        | `char`       |     |       |                             |
| `duplicate_bank_partner_ids`                | Duplicate Bank Partner                              | `many2many`  |     |       | res.partner                 |
| `email`                                     | Email                                               | `char`       |     |       |                             |
| `email_formatted`                           | Formatted Email                                     | `char`       |     |       |                             |
| `email_normalized`                          | Normalized Email                                    | `char`       |     |       |                             |
| `emergency_contact`                         | Emergency Contact                                   | `many2one`   |     | ✅    | res.partner                 |
| `emp_id`                                    | HR Employee                                         | `many2one`   |     | ✅    | hr.employee                 |
| `employee`                                  | Employee                                            | `boolean`    |     |       |                             |
| `employee_ids`                              | Employees                                           | `one2many`   |     |       | hr.employee                 |
| `employees_count`                           | Employees Count                                     | `integer`    |     |       |                             |
| `event_count`                               | # Events                                            | `integer`    |     |       |                             |
| `faculty_subject_ids`                       | Subject(s)                                          | `many2many`  |     | ✅    | op.subject                  |
| `first_name`                                | First Name                                          | `char`       | ✅  | ✅    |                             |
| `fiscal_country_codes`                      | Fiscal Country Codes                                | `char`       |     |       |                             |
| `fiscal_country_group_codes`                | Fiscal Country Group Codes                          | `json`       |     |       |                             |
| `function`                                  | Job Position                                        | `char`       |     |       |                             |
| `gender`                                    | Gender                                              | `selection`  | ✅  | ✅    |                             |
| `global_location_number`                    | GLN                                                 | `char`       |     |       |                             |
| `group_on`                                  | Week Day                                            | `selection`  | ✅  |       |                             |
| `group_rfq`                                 | Group RFQ                                           | `selection`  | ✅  |       |                             |
| `has_message`                               | Has Message                                         | `boolean`    |     |       |                             |
| `head_office`                               | Head Office                                         | `char`       |     |       |                             |
| `health_faculty_count`                      | Health Faculty Count                                | `integer`    |     |       |                             |
| `health_faculty_lines`                      | Health Detail                                       | `one2many`   |     | ✅    | op.health                   |
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
| `im_status`                                 | IM Status                                           | `char`       |     |       |                             |
| `industry_id`                               | Industry                                            | `many2one`   |     |       | res.partner.industry        |
| `invoice_edi_format`                        | eInvoice format                                     | `selection`  |     |       |                             |
| `invoice_edi_format_store`                  | Invoice Edi Format Store                            | `char`       |     |       |                             |
| `invoice_ids`                               | Invoices                                            | `one2many`   |     |       | account.move                |
| `invoice_sending_method`                    | Invoice sending                                     | `selection`  |     |       |                             |
| `invoice_template_pdf_report_id`            | Invoice report                                      | `many2one`   |     |       | ir.actions.report           |
| `is_blacklisted`                            | Blacklist                                           | `boolean`    |     |       |                             |
| `is_company`                                | Is a Company                                        | `boolean`    |     |       |                             |
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
| `lang`                                      | Language                                            | `selection`  |     |       |                             |
| `last_login`                                | Latest Connection                                   | `datetime`   |     |       |                             |
| `last_name`                                 | Last Name                                           | `char`       | ✅  | ✅    |                             |
| `leave_date_to`                             | Leave Date To                                       | `date`       |     |       |                             |
| `library_card_id`                           | Library Card                                        | `many2one`   |     | ✅    | op.library.card             |
| `livechat_channel_count`                    | Livechat Channel Count                              | `integer`    |     |       |                             |
| `login`                                     | Login                                               | `char`       |     |       |                             |
| `main_department_id`                        | Main Department                                     | `many2one`   |     | ✅    | op.department               |
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
| `offline_since`                             | Offline since                                       | `datetime`   |     |       |                             |
| `on_time_rate`                              | On-Time Delivery Rate                               | `float`      |     |       |                             |
| `opportunity_count`                         | Opportunity Count                                   | `integer`    |     |       |                             |
| `opportunity_ids`                           | Opportunities                                       | `one2many`   |     |       | crm.lead                    |
| `parent_id`                                 | Related Company                                     | `many2one`   |     |       | res.partner                 |
| `parent_name`                               | Parent name                                         | `char`       |     |       |                             |
| `partner_company_registry_placeholder`      | Partner Company Registry Placeholder                | `char`       |     |       |                             |
| `partner_id`                                | Partner                                             | `many2one`   | ✅  | ✅    | res.partner                 |
| `partner_latitude`                          | Geo Latitude                                        | `float`      |     |       |                             |
| `partner_longitude`                         | Geo Longitude                                       | `float`      |     |       |                             |
| `partner_share`                             | Share Partner                                       | `boolean`    |     |       |                             |
| `partner_vat_placeholder`                   | Partner Vat Placeholder                             | `char`       |     |       |                             |
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
| `session_count`                             | Session Count                                       | `integer`    |     |       |                             |
| `session_ids`                               | Sessions                                            | `one2many`   |     | ✅    | op.session                  |
| `show_credit_limit`                         | Show Credit Limit                                   | `boolean`    |     |       |                             |
| `signup_type`                               | Signup Token Type                                   | `char`       |     |       |                             |
| `specific_property_product_pricelist`       | Specific Property Product Pricelist                 | `many2one`   |     |       | product.pricelist           |
| `state_id`                                  | State                                               | `many2one`   |     |       | res.country.state           |
| `static_map_url`                            | Static Map Url                                      | `char`       |     |       |                             |
| `static_map_url_is_valid`                   | Static Map Url Is Valid                             | `boolean`    |     |       |                             |
| `street`                                    | Street                                              | `char`       |     |       |                             |
| `street2`                                   | Street2                                             | `char`       |     |       |                             |
| `subject_cost_ids`                          | Subject Cost                                        | `one2many`   |     | ✅    | op.subject.cost             |
| `subject_count`                             | Subject Count                                       | `integer`    |     |       |                             |
| `suggest_based_on`                          | Suggest Based On                                    | `char`       |     |       |                             |
| `suggest_days`                              | Suggest Days                                        | `integer`    |     |       |                             |
| `suggest_percent`                           | Suggest Percent                                     | `integer`    |     |       |                             |
| `supplier_invoice_count`                    | # Vendor Bills                                      | `integer`    |     |       |                             |
| `supplier_rank`                             | Supplier Rank                                       | `integer`    |     |       |                             |
| `ticket_count`                              | Ticket Count                                        | `integer`    |     |       |                             |
| `timetable_count`                           | Timetable Count                                     | `integer`    |     |       |                             |
| `title`                                     | Title                                               | `many2one`   |     |       | res.partner.title           |
| `total_invoiced`                            | Total Invoiced                                      | `monetary`   |     |       |                             |
| `trust`                                     | Degree of trust you have in this debtor             | `selection`  |     |       |                             |
| `type`                                      | Address Type                                        | `selection`  |     |       |                             |
| `type_address_label`                        | Address Type Description                            | `char`       |     |       |                             |
| `tz`                                        | Timezone                                            | `selection`  |     |       |                             |
| `tz_offset`                                 | Timezone offset                                     | `char`       |     |       |                             |
| `use_partner_credit_limit`                  | Partner Limit                                       | `boolean`    |     |       |                             |
| `user_id`                                   | Salesperson                                         | `many2one`   |     |       | res.users                   |
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

| Name                              | Group                | Perms     |
| --------------------------------- | -------------------- | --------- |
| name_op_faculty_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| op_faculty_faculty                | OpenEduCat / User    | `R`       |
| name_op_faculty_library           | Library / Manager    | `R`       |
| op_faculty_parent                 | Role / Portal        | `R`       |

**Record Rules:**

- **Faculty Login rule** (92) `R/W/C/D`
  - Domain: `['|',('user_id','=',user.id),('emp_id.user_id','=',user.id)]`
- **View Faculties** (93) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Faculty multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`
- **Faculty multi-department** (Global) `R/W/C/D`
  - Domain:
    `['|','|','|','|',('user_id','=',user.id),('emp_id.user_id','=',user.id),('main_department_id','=',False),('main_department_id','child_of',[user.dept_id.id]),('main_department_id','in',user.department_ids.ids)]`
- **Gradebook Faculty Login rule** (182) `R/W/C/D`
  - Domain: `[(1,'=',1)]`

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

### 🗃️ `op.student.course` — Student Course Details

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation              |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | --------------------- |
| `academic_plan_id`           | Academic Plan          | `many2one`  |     | ✅    | op.academic.plan      |
| `academic_term_id`           | Terms                  | `many2one`  |     | ✅    | op.academic.term      |
| `academic_years_id`          | Academic Year          | `many2one`  |     | ✅    | op.academic.year      |
| `batch_id`                   | Batch                  | `many2one`  |     | ✅    | op.batch              |
| `course_id`                  | Course                 | `many2one`  | ✅  | ✅    | op.course             |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                       |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users             |
| `display_name`               | Display Name           | `char`      |     |       |                       |
| `expires_after`              | Invoice Cycles         | `integer`   |     | ✅    |                       |
| `faculty_advisor_id`         | Faculty Advisor        | `many2one`  |     | ✅    | op.faculty            |
| `fees_plan_id`               | Fees Term Plan         | `many2one`  |     | ✅    | op.fees.plan          |
| `fees_start_date`            | Fees Start Date        | `date`      |     | ✅    |                       |
| `fees_term_id`               | Fees Term              | `many2one`  |     | ✅    | op.fees.terms         |
| `generated_invoices`         | Generated Invoices     | `integer`   |     | ✅    |                       |
| `has_message`                | Has Message            | `boolean`   |     |       |                       |
| `id`                         | ID                     | `integer`   |     | ✅    |                       |
| `intake_year_id`             | Intake Year            | `many2one`  |     | ✅    | op.intake.year        |
| `is_withdrawal`              | Withdrawal             | `boolean`   |     | ✅    |                       |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                       |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers        |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                       |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                       |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                       |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message          |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                       |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                       |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                       |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner           |
| `next_invoice_date`          | Next Invoice Date      | `date`      |     | ✅    |                       |
| `prev_invoice_date`          | Previous Invoice Date  | `date`      |     | ✅    |                       |
| `product_id`                 | Course Fees            | `many2one`  |     | ✅    | product.product       |
| `program_id`                 | Program                | `many2one`  |     |       | op.program            |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating         |
| `required_field`             | Required Field         | `boolean`   |     | ✅    |                       |
| `roll_number`                | Roll Number            | `char`      |     | ✅    |                       |
| `session_count`              | Session Count          | `integer`   |     |       |                       |
| `state`                      | Status                 | `selection` |     | ✅    |                       |
| `student_id`                 | Student                | `many2one`  |     | ✅    | op.student            |
| `subject_ids`                | Subjects               | `many2many` |     | ✅    | op.subject            |
| `user_id`                    | User                   | `many2one`  |     | ✅    | res.users             |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message          |
| `withdrawal_id`              | Withdrawal Details     | `many2one`  |     | ✅    | op.student.withdrawal |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                       |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                                     | Group                | Perms     |
| ---------------------------------------- | -------------------- | --------- |
| name_op_student_course_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| name_op_student_course_faculty           | OpenEduCat / User    | `R/W/C`   |
| op_student_course_parent                 | Library / Manager    | `R`       |
| op_student_course_parent                 | Role / Portal        | `R`       |

**Record Rules:**

- **Student Course multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|','|',('student_id.company_id','=',False),('student_id.company_id','child_of',[user.company_id.id]),('student_id.company_id','in',user.company_ids.ids),('student_id.company_id','in', company_ids)]`

### 🗃️ `op.fees.plan.line` — Fees Details Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                    | Label               | Type        | Req | Store | Relation              |
| ------------------------ | ------------------- | ----------- | --- | ----- | --------------------- |
| `amount`                 | Amount              | `float`     | ✅  | ✅    |                       |
| `batch_id`               | Batch               | `many2one`  |     | ✅    | op.batch              |
| `company_id`             | Company             | `many2one`  |     | ✅    | res.company           |
| `course_id`              | Course              | `many2one`  |     | ✅    | op.course             |
| `create_date`            | Created on          | `datetime`  |     | ✅    |                       |
| `create_uid`             | Created by          | `many2one`  |     | ✅    | res.users             |
| `display_name`           | Display Name        | `char`      |     |       |                       |
| `due_date`               | Due Date            | `date`      |     | ✅    |                       |
| `due_days`               | Due Days            | `integer`   |     | ✅    |                       |
| `fees_element_line_ids`  | Lines               | `one2many`  |     | ✅    | op.fees.element.plan  |
| `fees_factor`            | Value (%)           | `float`     |     | ✅    |                       |
| `fees_plan_id`           | Fees                | `many2one`  |     | ✅    | op.fees.plan          |
| `fees_reminder_line_ids` | Fees Reminder Lines | `many2many` |     | ✅    | op.fees.template.line |
| `fees_term_id`           | Fees Term           | `many2one`  |     |       | op.fees.terms         |
| `id`                     | ID                  | `integer`   |     | ✅    |                       |
| `invoice_date`           | Date                | `date`      |     | ✅    |                       |
| `invoice_id`             | Invoice             | `many2one`  |     | ✅    | account.move          |
| `invoice_state`          | Invoice Status      | `selection` |     |       |                       |
| `op_fees_terms_line_id`  | Invoice ID          | `many2one`  |     | ✅    | op.fees.terms.line    |
| `paid_amount`            | Paid Amount         | `float`     |     | ✅    |                       |
| `product_id`             | Product             | `many2one`  |     | ✅    | product.product       |
| `state`                  | Status              | `selection` |     | ✅    |                       |
| `student_id`             | Student             | `many2one`  |     | ✅    | op.student            |
| `write_date`             | Last Updated on     | `datetime`  |     | ✅    |                       |
| `write_uid`              | Last Updated by     | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                                          | Group                | Perms     |
| --------------------------------------------- | -------------------- | --------- |
| access_op_fees_plan_line_op_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_op_fees_plan_line_user                 | OpenEduCat / User    | `R`       |

**Record Rules:**

- **Fees Plan Line multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('fees_plan_id.company_id','=',False),'&',('fees_plan_id.company_id','in',company_ids),'|',('fees_plan_id.company_id','child_of',[user.company_id.id]),('fees_plan_id.company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.fees.terms.line` — Fees Details Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label           | Type       | Req | Store | Relation              |
| ------------------- | --------------- | ---------- | --- | ----- | --------------------- |
| `company_id`        | Company         | `many2one` |     | ✅    | res.company           |
| `create_date`       | Created on      | `datetime` |     | ✅    |                       |
| `create_uid`        | Created by      | `many2one` |     | ✅    | res.users             |
| `display_name`      | Display Name    | `char`     |     |       |                       |
| `due_date`          | Due Date        | `date`     |     | ✅    |                       |
| `due_days`          | Due Days        | `integer`  |     | ✅    |                       |
| `fees_element_line` | Fees Elements   | `one2many` |     | ✅    | op.fees.element       |
| `fees_id`           | Fees            | `many2one` |     | ✅    | op.fees.terms         |
| `id`                | ID              | `integer`  |     | ✅    |                       |
| `line_ids`          | Lines           | `one2many` |     | ✅    | op.fees.template.line |
| `value`             | Value (%)       | `float`    |     | ✅    |                       |
| `write_date`        | Last Updated on | `datetime` |     | ✅    |                       |
| `write_uid`         | Last Updated by | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                                     | Group          | Perms     |
| ---------------------------------------- | -------------- | --------- |
| name_op_fees_terms_line_backoffice_admin | Fees / Manager | `R/W/C/D` |
| name_op_fees_terms_line_backoffice_admin | Fees / User    | `R/W/C`   |

**Record Rules:**

- **Fees Terms line multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.fees.element` — Fees Element for course

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label           | Type       | Req | Store | Relation           |
| -------------------- | --------------- | ---------- | --- | ----- | ------------------ |
| `company_id`         | Company         | `many2one` |     | ✅    | res.company        |
| `create_date`        | Created on      | `datetime` |     | ✅    |                    |
| `create_uid`         | Created by      | `many2one` |     | ✅    | res.users          |
| `display_name`       | Display Name    | `char`     |     |       |                    |
| `fees_terms_line_id` | Fees Terms      | `many2one` |     | ✅    | op.fees.terms.line |
| `id`                 | ID              | `integer`  |     | ✅    |                    |
| `product_id`         | Product(s)      | `many2one` | ✅  | ✅    | product.product    |
| `sequence`           | Sequence        | `integer`  |     | ✅    |                    |
| `value`              | Value (%)       | `float`    |     | ✅    |                    |
| `write_date`         | Last Updated on | `datetime` |     | ✅    |                    |
| `write_uid`          | Last Updated by | `many2one` |     | ✅    | res.users          |

**Access Rights:**

| Name                   | Group          | Perms     |
| ---------------------- | -------------- | --------- |
| access_op_fees_element | Fees / Manager | `R/W/C/D` |

**Record Rules:**

- **Fees Element multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.fees.element.plan` — Fees Element Plan

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label           | Type       | Req | Store | Relation          |
| ------------------- | --------------- | ---------- | --- | ----- | ----------------- |
| `create_date`       | Created on      | `datetime` |     | ✅    |                   |
| `create_uid`        | Created by      | `many2one` |     | ✅    | res.users         |
| `display_name`      | Display Name    | `char`     |     |       |                   |
| `fees_plan_line_id` | Fees Plan Line  | `many2one` |     | ✅    | op.fees.plan.line |
| `id`                | ID              | `integer`  |     | ✅    |                   |
| `product_id`        | Product(s)      | `many2one` | ✅  | ✅    | product.product   |
| `sequence`          | Sequence        | `integer`  |     | ✅    |                   |
| `value`             | Value (%)       | `float`    |     | ✅    |                   |
| `write_date`        | Last Updated on | `datetime` |     | ✅    |                   |
| `write_uid`         | Last Updated by | `many2one` |     | ✅    | res.users         |

**Access Rights:**

| Name                                          | Group                | Perms     |
| --------------------------------------------- | -------------------- | --------- |
| access_op_fees_element_plan_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_op_fees_element_plan_user              | OpenEduCat / User    | `R`       |

### 🗃️ `op.fees.template.line` — Fees Template Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label           | Type        | Req | Store | Relation           |
| --------------- | --------------- | ----------- | --- | ----- | ------------------ |
| `company_id`    | Company         | `many2one`  |     | ✅    | res.company        |
| `create_date`   | Created on      | `datetime`  |     | ✅    |                    |
| `create_uid`    | Created by      | `many2one`  |     | ✅    | res.users          |
| `days`          | Days            | `integer`   |     | ✅    |                    |
| `display_name`  | Display Name    | `char`      |     |       |                    |
| `duration_type` | Duration Type   | `selection` |     | ✅    |                    |
| `id`            | ID              | `integer`   |     | ✅    |                    |
| `line_id`       | Fees Line       | `many2one`  |     | ✅    | op.fees.terms.line |
| `template_id`   | Template        | `many2one`  |     | ✅    | mail.template      |
| `write_date`    | Last Updated on | `datetime`  |     | ✅    |                    |
| `write_uid`     | Last Updated by | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                           | Group                | Perms     |
| ---------------------------------------------- | -------------------- | --------- |
| access_op_fees_template_line_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_op_fees_template_line_user              | OpenEduCat / User    | `R`       |

**Record Rules:**

- **Fees Template line multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.subject.cost` — Subject Cost

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation        |
| -------------- | --------------- | ---------- | --- | ----- | --------------- |
| `cost`         | Cost            | `float`    |     |       |                 |
| `create_date`  | Created on      | `datetime` |     | ✅    |                 |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users       |
| `display_name` | Display Name    | `char`     |     |       |                 |
| `faculty_id`   | Faculty         | `many2one` |     | ✅    | op.faculty      |
| `id`           | ID              | `integer`  |     | ✅    |                 |
| `product_id`   | Product         | `many2one` |     | ✅    | product.product |
| `subject_id`   | Subject         | `many2one` |     | ✅    | op.subject      |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                 |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                                     | Group                | Perms     |
| ---------------------------------------- | -------------------- | --------- |
| access_op_subject_cost_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |

### 🗃️ `select.fees.term.type.wizard` — Wizard For Fees Term Type

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation  |
| -------------- | --------------- | ----------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime`  |     | ✅    |           |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users |
| `display_name` | Display Name    | `char`      |     |       |           |
| `fees_terms`   | Fees Terms      | `selection` |     | ✅    |           |
| `id`           | ID              | `integer`   |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                                | Group          | Perms     |
| ----------------------------------- | -------------- | --------- |
| access_select_fees_term_type_wizard | Fees / Manager | `R/W/C/D` |
