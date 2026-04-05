---
title: "OpenEduCat Admission Enterprise"
module: "openeducat_admission_enterprise"
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

# 🟢 OpenEduCat Admission Enterprise

> **Module:** `openeducat_admission_enterprise` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_admission]] [[openeducat_core_enterprise]]
[[openeducat_student_progress_enterprise]]

## 📖 Description

## OpenEduCat Admission Enterprise

### Admission Management

[![](/openeducat_admission_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module allows you to manage admission process efficiently. You can set fees details
& adds constrains to admission process through admission register.

[Contact Us](https://www.openeducat.org/contactus/)

## Create Admission Process

Create admission register to initiate admission process. You can set fees details, time
duration, maximum no. of application & other details.

![](/openeducat_admission_enterprise/static/description/admission_register.png)

## Create Application, Pay Fees & Be Student

![](/openeducat_admission_enterprise/static/description/admission.png)

Based on admission register applicant can apply for particular course and goes under
different stages. Make fees payment & proceed to create student.

## Fees Payment

Create invoice for admission fees, make payment & proceed for enrollment of student.

![](/openeducat_admission_enterprise/static/description/fees_payment.png)

## Time Period based Report

![](/openeducat_admission_enterprise/static/description/admission_analysis.png)

Admission analysis report gives brief details about admissions for particular period of
time.

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Admissions/Configuration/Admission Stages`
- `Admissions/Configuration/Admission Tags`
- `Admissions/Reporting/Admission Analysis`

### Views

- `* INHERIT op.admission.form.inherit (form)`
- `* INHERIT op.admission.register.inherit.form (form)`
- `* INHERIT op.admission.register.search.inherit (search)`
- `* INHERIT op.admission.tree.inherit (list)`
- `* INHERIT op.course.admission.dashboard.kanban (kanban)`
- `* INHERIT op.course.admission.program.kanban (kanban)`
- `* INHERIT op.course.plan.form (form)`
- `* INHERIT op.course.plan.form (form)`
- `admission.stage.form (form)`
- `admission.stage.list (list)`
- `admission.tag.view.form (form)`
- `admission.tag.view.list (list)`
- `op.admission.kanban (kanban)`
- `op.admission.register.form (form)`
- `view.admission.kanban (kanban)`

### Reports

_none_

## 🛠️ Technical Documentation

**11 model(s) defined by this module:**

### 🗃️ `op.admission` — Admission

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation              |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | --------------------- |
| `academic_plan_id`              | Academic Plan                 | `many2one`  |     | ✅    | op.academic.plan      |
| `active`                        | Active                        | `boolean`   |     | ✅    |                       |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event        |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                       |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                       |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                       |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity         |
| `activity_state`                | Activity State                | `selection` |     |       |                       |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                       |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                       |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type    |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users             |
| `admission_date`                | Admission Date                | `date`      |     | ✅    |                       |
| `application`                   | Application                   | `char`      |     | ✅    |                       |
| `application_date`              | Application Date              | `datetime`  | ✅  | ✅    |                       |
| `application_number`            | Application Number            | `char`      |     | ✅    |                       |
| `attachment_ids`                | Attachments                   | `many2many` |     | ✅    | ir.attachment         |
| `batch_id`                      | Batch                         | `many2one`  |     | ✅    | op.batch              |
| `birth_date`                    | Birth Date                    | `date`      |     | ✅    |                       |
| `campaign_id`                   | Marketing Campaign            | `many2one`  |     | ✅    | utm.campaign          |
| `city`                          | City                          | `char`      |     | ✅    |                       |
| `color`                         | Color Index                   | `integer`   |     | ✅    |                       |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company           |
| `country_id`                    | Country                       | `many2one`  |     | ✅    | res.country           |
| `course_id`                     | Course                        | `many2one`  | ✅  | ✅    | op.course             |
| `course_ids`                    | Courses                       | `many2many` |     |       | op.course             |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                       |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users             |
| `day_close`                     | Days to Close                 | `float`     |     | ✅    |                       |
| `day_open`                      | Days to Assign                | `float`     |     | ✅    |                       |
| `discount`                      | Discount (%)                  | `float`     |     | ✅    |                       |
| `display_name`                  | Display Name                  | `char`      |     |       |                       |
| `due_date`                      | Due Date                      | `date`      |     | ✅    |                       |
| `duration_tracking`             | Status time                   | `json`      |     |       |                       |
| `email`                         | Email                         | `char`      |     | ✅    |                       |
| `email2`                        | HEllo                         | `char`      |     | ✅    |                       |
| `e_sign_request_id`             | Esign Request                 | `many2one`  |     | ✅    | e.sign.request        |
| `e_sign_template_id`            | Esign Template                | `many2one`  |     | ✅    | e.sign.template       |
| `family_business`               | Family Business               | `char`      |     | ✅    |                       |
| `family_income`                 | Family Income                 | `float`     |     | ✅    |                       |
| `fees`                          | Fees                          | `float`     |     | ✅    |                       |
| `fees_start_date`               | Fees Start Date               | `date`      |     | ✅    |                       |
| `fees_term_id`                  | Fees Term                     | `many2one`  |     |       | op.fees.terms         |
| `first_name`                    | First Name                    | `char`      |     | ✅    |                       |
| `gender`                        | Gender                        | `selection` |     | ✅    |                       |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                       |
| `id`                            | ID                            | `integer`   |     | ✅    |                       |
| `image`                         | image                         | `binary`    |     | ✅    |                       |
| `intake_year_id`                | Intake Year                   | `many2one`  |     | ✅    | op.intake.year        |
| `is_rotting`                    | Rotting                       | `boolean`   |     |       |                       |
| `is_student`                    | Is Already Student            | `boolean`   |     | ✅    |                       |
| `last_name`                     | Last Name                     | `char`      |     | ✅    |                       |
| `medium_id`                     | Marketing Medium              | `many2one`  |     | ✅    | utm.medium            |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                       |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers        |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                       |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                       |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                       |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message          |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                       |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                       |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                       |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner           |
| `middle_name`                   | Middle Name                   | `char`      |     | ✅    |                       |
| `mobile`                        | Mobile                        | `char`      |     | ✅    |                       |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                       |
| `name`                          | Name                          | `char`      |     | ✅    |                       |
| `nbr`                           | No of Admission               | `integer`   |     | ✅    |                       |
| `order_id`                      | Registration Fees Ref         | `many2one`  |     | ✅    | sale.order            |
| `partner_id`                    | Partner                       | `many2one`  |     | ✅    | res.partner           |
| `phone`                         | Phone                         | `char`      |     | ✅    |                       |
| `prev_course_id`                | Previous Course               | `char`      |     | ✅    |                       |
| `prev_institute_id`             | Previous Institute            | `char`      |     | ✅    |                       |
| `prev_result`                   | Previous Result               | `char`      |     | ✅    |                       |
| `program_id`                    | Program                       | `many2one`  |     | ✅    | op.program            |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating         |
| `referred_by`                   | Referred By                   | `char`      |     | ✅    |                       |
| `register_id`                   | Admission Register            | `many2one`  | ✅  | ✅    | op.admission.register |
| `required_field`                | Required Field                | `boolean`   |     | ✅    |                       |
| `rotting_days`                  | Days Rotting                  | `integer`   |     |       |                       |
| `signed_document`               | Signed Document               | `binary`    |     | ✅    |                       |
| `similar_admission_count`       | Similar Admissions            | `integer`   |     |       |                       |
| `source_id`                     | Lead Source                   | `many2one`  |     | ✅    | utm.source            |
| `stage_id`                      | Stage                         | `many2one`  |     | ✅    | admission.stage       |
| `state`                         | State                         | `selection` |     | ✅    |                       |
| `state_id`                      | States                        | `many2one`  |     | ✅    | res.country.state     |
| `street`                        | Street                        | `char`      |     | ✅    |                       |
| `street2`                       | Street2                       | `char`      |     | ✅    |                       |
| `student_id`                    | Student                       | `many2one`  |     | ✅    | op.student            |
| `tag_ids`                       | Tags                          | `many2many` |     | ✅    | admission.tag         |
| `team_id`                       | Sales Team                    | `many2one`  |     | ✅    | crm.team              |
| `title`                         | Title                         | `many2one`  |     | ✅    | res.partner.title     |
| `user_id`                       | User ID                       | `many2one`  |     |       | res.users             |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message          |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                       |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users             |
| `zip`                           | Zip                           | `char`      |     | ✅    |                       |

**Access Rights:**

| Name                                | Group               | Perms     |
| ----------------------------------- | ------------------- | --------- |
| name_op_admission_back_office_admin | Admission / Manager | `R/W/C/D` |
| name_op_admission_faculty           | Admission / User    | `R/W/C`   |

**Record Rules:**

- **Admission multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.admission.register` — Admission Register

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                              | Label                            | Type        | Req | Store | Relation                    |
| ---------------------------------- | -------------------------------- | ----------- | --- | ----- | --------------------------- |
| `academic_term_id`                 | Terms                            | `many2one`  |     | ✅    | op.academic.term            |
| `academic_years_id`                | Academic Year                    | `many2one`  |     | ✅    | op.academic.year            |
| `active`                           | Active                           | `boolean`   |     | ✅    |                             |
| `admission_base`                   | Admission Base                   | `selection` |     | ✅    |                             |
| `admission_count`                  | Admission Count                  | `integer`   |     | ✅    |                             |
| `admission_fees_line_ids`          | Admission Fees Configuration     | `one2many`  |     | ✅    | op.admission.fees.line      |
| `admission_ids`                    | Admissions                       | `one2many`  |     | ✅    | op.admission                |
| `admission_template_id`            | Admission Template               | `many2one`  |     | ✅    | op.admission.customtemplate |
| `application_count`                | Total_record                     | `integer`   |     |       |                             |
| `color`                            | Color Index                      | `integer`   |     | ✅    |                             |
| `company_id`                       | Company                          | `many2one`  |     | ✅    | res.company                 |
| `confirm_count`                    | Confirm Count                    | `integer`   |     |       |                             |
| `course_id`                        | Course                           | `many2one`  |     | ✅    | op.course                   |
| `create_date`                      | Created on                       | `datetime`  |     | ✅    |                             |
| `create_uid`                       | Created by                       | `many2one`  |     | ✅    | res.users                   |
| `display_name`                     | Display Name                     | `char`      |     |       |                             |
| `done_count`                       | Done Count                       | `integer`   |     |       |                             |
| `draft_count`                      | Draft Count                      | `integer`   |     |       |                             |
| `end_date`                         | End Date                         | `date`      |     | ✅    |                             |
| `has_message`                      | Has Message                      | `boolean`   |     |       |                             |
| `id`                               | ID                               | `integer`   |     | ✅    |                             |
| `is_favorite`                      | Is Favorite                      | `boolean`   |     | ✅    |                             |
| `kanban_admission_dashboard_graph` | Kanban Admission Dashboard Graph | `text`      |     |       |                             |
| `max_count`                        | Maximum No. of Admission         | `integer`   |     | ✅    |                             |
| `message_attachment_count`         | Attachment Count                 | `integer`   |     |       |                             |
| `message_follower_ids`             | Followers                        | `one2many`  |     | ✅    | mail.followers              |
| `message_has_error`                | Message Delivery error           | `boolean`   |     |       |                             |
| `message_has_error_counter`        | Number of errors                 | `integer`   |     |       |                             |
| `message_has_sms_error`            | SMS Delivery error               | `boolean`   |     |       |                             |
| `message_ids`                      | Messages                         | `one2many`  |     | ✅    | mail.message                |
| `message_is_follower`              | Is Follower                      | `boolean`   |     |       |                             |
| `message_needaction`               | Action Needed                    | `boolean`   |     |       |                             |
| `message_needaction_counter`       | Number of Actions                | `integer`   |     |       |                             |
| `message_partner_ids`              | Followers (Partners)             | `many2many` |     |       | res.partner                 |
| `min_count`                        | Minimum No. of Admission         | `integer`   |     | ✅    |                             |
| `minimum_age_criteria`             | Minimum Required Age(Years)      | `integer`   |     | ✅    |                             |
| `name`                             | Name                             | `char`      | ✅  | ✅    |                             |
| `online_count`                     | Online Count                     | `integer`   |     |       |                             |
| `product_id`                       | Course Fees                      | `many2one`  |     | ✅    | product.product             |
| `program_fees`                     | Program Fees                     | `float`     |     | ✅    |                             |
| `program_id`                       | Program                          | `many2one`  |     | ✅    | op.program                  |
| `rating_ids`                       | Ratings                          | `one2many`  |     | ✅    | rating.rating               |
| `register_product_id`              | Fees                             | `many2one`  |     | ✅    | product.product             |
| `registration_fees`                | Registration Fees                | `boolean`   |     | ✅    |                             |
| `sign_in_required`                 | Registration Required ?          | `boolean`   |     | ✅    |                             |
| `start_date`                       | Start Date                       | `date`      | ✅  | ✅    |                             |
| `state`                            | Status                           | `selection` |     | ✅    |                             |
| `website_message_ids`              | Website Messages                 | `one2many`  |     | ✅    | mail.message                |
| `write_date`                       | Last Updated on                  | `datetime`  |     | ✅    |                             |
| `write_uid`                        | Last Updated by                  | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                                         | Group               | Perms     |
| -------------------------------------------- | ------------------- | --------- |
| name_op_admission_register_back_office_admin | Admission / Manager | `R/W/C/D` |
| name_op_admission_register_faculty           | Admission / User    | `R/W/C`   |
| name_op_admission_register_portal_user       | Role / Portal       | `R/W/C`   |
| name_op_admission_register_public_user       | Role / Public       | `R/W/C`   |

**Record Rules:**

- **Admission Register multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `admission.stage` — Admission Stages

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
| `view_boolean`               | Form View              | `boolean`   |     | ✅    |                |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                                     | Group               | Perms     |
| ---------------------------------------- | ------------------- | --------- |
| access_admission_stage_back_office_admin | Admission / Manager | `R/W/C/D` |
| access_admission_stage_faculty           | Admission / User    | `R/W/C`   |

**Record Rules:**

- **Admission Stage Multi Company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

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

### 🗃️ `admission.tag` — Admission Tag

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `color`        | Color           | `integer`  |     | ✅    |             |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Tag Name        | `char`     | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                                   | Group               | Perms     |
| -------------------------------------- | ------------------- | --------- |
| access_admission_tag_back_office_admin | Admission / Manager | `R/W/C/D` |
| access_admission_tag_faculty           | Admission / User    | `R/W/C`   |

**Record Rules:**

- **Admission Tag Multi Company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

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

### 🗃️ `op.student.fees.details` — Student Fees Details

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                   | Label                 | Type        | Req | Store | Relation           |
| ----------------------- | --------------------- | ----------- | --- | ----- | ------------------ |
| `after_discount_amount` | After Discount Amount | `monetary`  |     |       |                    |
| `amount`                | Fees Amount           | `monetary`  |     | ✅    |                    |
| `batch_id`              | Batch                 | `many2one`  |     | ✅    | op.batch           |
| `company_id`            | Company               | `many2one`  |     | ✅    | res.company        |
| `course_id`             | Course                | `many2one`  |     | ✅    | op.course          |
| `create_date`           | Created on            | `datetime`  |     | ✅    |                    |
| `create_uid`            | Created by            | `many2one`  |     | ✅    | res.users          |
| `currency_id`           | Currency              | `many2one`  |     |       | res.currency       |
| `date`                  | Submit Date           | `date`      |     | ✅    |                    |
| `discount`              | Discount (%)          | `float`     |     | ✅    |                    |
| `display_name`          | Display Name          | `char`      |     |       |                    |
| `fees_factor`           | Fees Factor           | `float`     |     | ✅    |                    |
| `fees_line_id`          | Fees Line             | `many2one`  |     | ✅    | op.fees.terms.line |
| `id`                    | ID                    | `integer`   |     | ✅    |                    |
| `invoice_id`            | Invoice ID            | `many2one`  |     | ✅    | account.move       |
| `invoice_state`         | Invoice Status        | `selection` |     |       |                    |
| `product_id`            | Product               | `many2one`  |     | ✅    | product.product    |
| `state`                 | Status                | `selection` |     | ✅    |                    |
| `student_id`            | Student               | `many2one`  | ✅  | ✅    | op.student         |
| `write_date`            | Last Updated on       | `datetime`  |     | ✅    |                    |
| `write_uid`             | Last Updated by       | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                           | Group               | Perms     |
| ---------------------------------------------- | ------------------- | --------- |
| name_op_student_fees_details_back_office_admin | Fees / Manager      | `R/W/C/D` |
| name_op_student_fees_details_faculty           | Fees / User         | `R/W/C`   |
| name_op_student_fees_details_back_office_admin | Admission / Manager | `R/W/C/D` |
| name_op_student_fees_details_student           | Admission / Manager | `R/W/C/D` |

### 🗃️ `ir.ui.view` — View

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                             | Type        | Req | Store | Relation                |
| ----------------------------- | --------------------------------- | ----------- | --- | ----- | ----------------------- |
| `active`                      | Active                            | `boolean`   |     | ✅    |                         |
| `arch`                        | View Architecture                 | `text`      |     |       |                         |
| `arch_base`                   | Base View Architecture            | `text`      |     |       |                         |
| `arch_db`                     | Arch Blob                         | `text`      |     | ✅    |                         |
| `arch_fs`                     | Arch Filename                     | `char`      |     | ✅    |                         |
| `arch_prev`                   | Previous View Architecture        | `text`      |     | ✅    |                         |
| `arch_updated`                | Modified Architecture             | `boolean`   |     | ✅    |                         |
| `controller_page_ids`         | Controller Page                   | `one2many`  |     | ✅    | website.controller.page |
| `create_date`                 | Created on                        | `datetime`  |     | ✅    |                         |
| `create_uid`                  | Created by                        | `many2one`  |     | ✅    | res.users               |
| `customize_show`              | Show As Optional Inherit          | `boolean`   |     | ✅    |                         |
| `display_name`                | Display Name                      | `char`      |     |       |                         |
| `first_page_id`               | Website Page                      | `many2one`  |     |       | website.page            |
| `group_ids`                   | Groups                            | `many2many` |     | ✅    | res.groups              |
| `id`                          | ID                                | `integer`   |     | ✅    |                         |
| `inherit_children_ids`        | Views which inherit from this one | `one2many`  |     | ✅    | ir.ui.view              |
| `inherit_id`                  | Inherited View                    | `many2one`  |     | ✅    | ir.ui.view              |
| `invalid_locators`            | Invalid Locators                  | `json`      |     |       |                         |
| `is_seo_optimized`            | SEO optimized                     | `boolean`   |     | ✅    |                         |
| `key`                         | Key                               | `char`      |     | ✅    |                         |
| `mode`                        | View inheritance mode             | `selection` | ✅  | ✅    |                         |
| `model`                       | Model                             | `char`      |     | ✅    |                         |
| `model_data_id`               | Model Data                        | `many2one`  |     |       | ir.model.data           |
| `model_id`                    | Model of the view                 | `many2one`  |     |       | ir.model                |
| `name`                        | View Name                         | `char`      | ✅  | ✅    |                         |
| `page_ids`                    | Page                              | `one2many`  |     | ✅    | website.page            |
| `priority`                    | Sequence                          | `integer`   | ✅  | ✅    |                         |
| `seo_name`                    | Seo name                          | `char`      |     | ✅    |                         |
| `theme_template_id`           | Theme Template                    | `many2one`  |     | ✅    | theme.ir.ui.view        |
| `track`                       | Track                             | `boolean`   |     | ✅    |                         |
| `type`                        | View Type                         | `selection` |     | ✅    |                         |
| `visibility`                  | Visibility                        | `selection` |     | ✅    |                         |
| `visibility_password`         | Visibility Password               | `char`      |     | ✅    |                         |
| `visibility_password_display` | Visibility Password Display       | `char`      |     |       |                         |
| `warning_info`                | Warning information               | `html`      |     |       |                         |
| `website_id`                  | Website                           | `many2one`  |     | ✅    | website                 |
| `website_meta_description`    | Website meta description          | `text`      |     | ✅    |                         |
| `website_meta_keywords`       | Website meta keywords             | `char`      |     | ✅    |                         |
| `website_meta_og_img`         | Website opengraph image           | `char`      |     | ✅    |                         |
| `website_meta_title`          | Website meta title                | `char`      |     | ✅    |                         |
| `write_date`                  | Last Updated on                   | `datetime`  |     | ✅    |                         |
| `write_uid`                   | Last Updated by                   | `many2one`  |     | ✅    | res.users               |
| `xml_id`                      | External ID                       | `char`      |     |       |                         |

**Access Rights:**

| Name                                        | Group                         | Perms     |
| ------------------------------------------- | ----------------------------- | --------- |
| access_website_ir_ui_view_restricted_editor | Website / Restricted Editor   | `R`       |
| access_website_ir_ui_view_designer          | Website / Editor and Designer | `R/W/C/D` |
| ir_ui_view group_system                     | Role / Administrator          | `R/W/C/D` |
| ir_ui_view group_user                       | Everyone                      | `-`       |

**Record Rules:**

- **website_designer: Manage Website and qWeb view** (72) `R/W/C/D`
  - Domain: `[('type', '=', 'qweb')]`
- **website_designer: global view** (72) `R`
  - Domain: `[('type', '!=', 'qweb')]`
- **Administration Settings: Manage all views** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Website View Visibility Public** (11) `R`
  - Domain: `['|', ('type', '!=', 'qweb'), ('visibility', 'in', ('public', False))]`
- **Website View Visibility Connected** (10) `R`
  - Domain:
    `['|', ('type', '!=', 'qweb'), ('visibility', 'in', ('public', 'connected', False))]`
