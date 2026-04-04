---
title: "OpenEduCat Dynamic Admission"
module: "openeducat_dynamic_admission"
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

# 🟢 OpenEduCat Dynamic Admission

> **Module:** `openeducat_dynamic_admission` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[website]] [[website_sale]] [[website_payment]] [[openeducat_admission]]
[[openeducat_core_enterprise]] [[website_mail]] [[openeducat_admission_enterprise]]

## 📖 Description

## OpenEduCat Dynamic Admission

### To Create Dynamic Admission Form and Online Admission

[![](/openeducat_dynamic_admission/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module allows you to create dynamic admission form and get online application using
that web form.

[Contact Us](https://www.openeducat.org/contactus/)

## Create Application Form

This module allows you to create dynamic Admission Form.

[![](/openeducat_dynamic_admission/static/description/admission_template.png)](https://www.openeducat.org/demo)

Online Demo

## Edit Application Form

[![](/openeducat_dynamic_admission/static/description/edit_admission_template.png)](https://www.openeducat.org/demo)

This module also allow to create your custom fields, edit form and design for your
Admission Form.

## Select Admission Form

This module allows you to Select dynamic Admission Forms for register. This module also
allow to user has registration required or not.

[![](/openeducat_dynamic_admission/static/description/select_template.png)](https://www.openeducat.org/demo)

## Online Application Form

[![](/openeducat_dynamic_admission/static/description/admission_form.png)](https://www.openeducat.org/demo)

This module allows you to manage online admission process.

## Online Payment for Registration

Select the payment method for online payment.

![](/openeducat_dynamic_admission/static/description/payment.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Admissions/Configuration/Admission Templates`

### Views

- `* INHERIT Course Category (qweb)`
- `* INHERIT Course Description (qweb)`
- `* INHERIT Portal layout : Admission New Registration (qweb)`
- `* INHERIT Program Admission (qweb)`
- `* INHERIT Program Category (qweb)`
- `* INHERIT Program Category (qweb)`
- `* INHERIT Program Category (qweb)`
- `* INHERIT Program Description (qweb)`
- `* INHERIT Program Fees (qweb)`
- `* INHERIT Show New Registration (qweb)`
- `* INHERIT Show Online Admission (qweb)`
- `* INHERIT op.admission.form (form)`
- `* INHERIT op.admission.new.register.inherit.form (form)`
- `* INHERIT op.admission.new.register.inherit.kanban (kanban)`
- `* INHERIT op.course.form (form)`
- `* INHERIT op.program.form (form)`
- `* INHERIT s_website_form_admission (qweb)`
- `* INHERIT snippets_inherit_dynamic (qweb)`
- `Admission Web Page (qweb)`
- `Application Received - Thank You (qweb)`
- `Course Detail (qweb)`
- `Courses-Offered (qweb)`
- `Dynamic Text Snippet (qweb)`
- `Dynamic line Snippet (qweb)`
- `Edit Admission Web Page (qweb)`
- `Enable Search (qweb)`
- `Enable Search (qweb)`
- `Program Detail (qweb)`
- `Program-Offered (qweb)`
- `Sort-by Template (qweb)`
- `Sort-by Template (qweb)`
- `admission_checkout (qweb)`
- `admission_customtemplate_form_view (form)`
- `admission_customtemplate_list_view (list)`
- `apply (qweb)`
- `openeducat_dynamic_admission.course_attributes (qweb)`
- `openeducat_dynamic_admission.course_side_attributes (qweb)`
- `openeducat_dynamic_admission.program_attributes (qweb)`
- `openeducat_dynamic_admission.program_side_attributes (qweb)`
- `openeducat_student_newregistration_list_data (qweb)`
- `program_apply (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**9 model(s) defined by this module:**

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

### 🗃️ `op.admission.customtemplate` — Admission Template

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                   | Type        | Req | Store | Relation              |
| ---------------------------- | ----------------------- | ----------- | --- | ----- | --------------------- |
| `admission_register_line`    | Admission Register Line | `one2many`  |     | ✅    | op.admission.register |
| `admission_url`              | Admission URL           | `char`      |     | ✅    |                       |
| `admission_webpage`          | WebPage Content         | `html`      |     | ✅    |                       |
| `company_id`                 | Company                 | `many2one`  |     | ✅    | res.company           |
| `create_date`                | Created on              | `datetime`  |     | ✅    |                       |
| `create_uid`                 | Created by              | `many2one`  |     | ✅    | res.users             |
| `display_name`               | Display Name            | `char`      |     |       |                       |
| `has_message`                | Has Message             | `boolean`   |     |       |                       |
| `id`                         | ID                      | `integer`   |     | ✅    |                       |
| `message_attachment_count`   | Attachment Count        | `integer`   |     |       |                       |
| `message_follower_ids`       | Followers               | `one2many`  |     | ✅    | mail.followers        |
| `message_has_error`          | Message Delivery error  | `boolean`   |     |       |                       |
| `message_has_error_counter`  | Number of errors        | `integer`   |     |       |                       |
| `message_has_sms_error`      | SMS Delivery error      | `boolean`   |     |       |                       |
| `message_ids`                | Messages                | `one2many`  |     | ✅    | mail.message          |
| `message_is_follower`        | Is Follower             | `boolean`   |     |       |                       |
| `message_needaction`         | Action Needed           | `boolean`   |     |       |                       |
| `message_needaction_counter` | Number of Actions       | `integer`   |     |       |                       |
| `message_partner_ids`        | Followers (Partners)    | `many2many` |     |       | res.partner           |
| `name`                       | Name                    | `char`      | ✅  | ✅    |                       |
| `program_admission_webpage`  | Program WebPage Content | `html`      |     | ✅    |                       |
| `program_base_template`      | Program Base Template   | `boolean`   |     | ✅    |                       |
| `rating_ids`                 | Ratings                 | `one2many`  |     | ✅    | rating.rating         |
| `website_message_ids`        | Website Messages        | `one2many`  |     | ✅    | mail.message          |
| `write_date`                 | Last Updated on         | `datetime`  |     | ✅    |                       |
| `write_uid`                  | Last Updated by         | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                                     | Group                | Perms     |
| ---------------------------------------- | -------------------- | --------- |
| access_op_admission_customtemplate_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_op_admission_customtemplate_user  | OpenEduCat / User    | `R`       |

**Record Rules:**

- **Admission Customtemplate Multi Company** (Global) `R/W/C/D`
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

### 🗃️ `product.product` — Product Variant

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                       | Label                                    | Type                    | Req | Store | Relation                         |
| ------------------------------------------- | ---------------------------------------- | ----------------------- | --- | ----- | -------------------------------- |
| `accessory_product_ids`                     | Accessory Products                       | `many2many`             |     |       | product.product                  |
| `account_tag_ids`                           | Account Tags                             | `many2many`             |     |       | account.account.tag              |
| `active`                                    | Active                                   | `boolean`               |     | ✅    |                                  |
| `activity_calendar_event_id`                | Next Activity Calendar Event             | `many2one`              |     |       | calendar.event                   |
| `activity_date_deadline`                    | Next Activity Deadline                   | `date`                  |     |       |                                  |
| `activity_exception_decoration`             | Activity Exception Decoration            | `selection`             |     |       |                                  |
| `activity_exception_icon`                   | Icon                                     | `char`                  |     |       |                                  |
| `activity_ids`                              | Activities                               | `one2many`              |     | ✅    | mail.activity                    |
| `activity_state`                            | Activity State                           | `selection`             |     |       |                                  |
| `activity_summary`                          | Next Activity Summary                    | `char`                  |     |       |                                  |
| `activity_type_icon`                        | Activity Type Icon                       | `char`                  |     |       |                                  |
| `activity_type_id`                          | Next Activity Type                       | `many2one`              |     |       | mail.activity.type               |
| `activity_user_id`                          | Responsible User                         | `many2one`              |     |       | res.users                        |
| `additional_product_tag_ids`                | Variant Tags                             | `many2many`             |     | ✅    | product.tag                      |
| `allow_out_of_stock_order`                  | Sell when Out-of-Stock                   | `boolean`               |     |       |                                  |
| `all_product_tag_ids`                       | All Product Tag                          | `many2many`             |     |       | product.tag                      |
| `alternative_product_ids`                   | Alternative Products                     | `many2many`             |     |       | product.template                 |
| `asset_category_id`                         | Asset Type                               | `many2one`              |     |       | account.asset.category           |
| `attribute_line_ids`                        | Product Attributes                       | `one2many`              |     |       | product.template.attribute.line  |
| `available_threshold`                       | Show Threshold                           | `float`                 |     |       |                                  |
| `avg_cost`                                  | Average Cost                             | `monetary`              |     |       |                                  |
| `barcode`                                   | Barcode                                  | `char`                  |     | ✅    |                                  |
| `base_unit_count`                           | Base Unit Count                          | `float`                 | ✅  | ✅    |                                  |
| `base_unit_id`                              | Custom Unit of Measure                   | `many2one`              |     | ✅    | website.base.unit                |
| `base_unit_name`                            | Base Unit Name                           | `char`                  |     |       |                                  |
| `base_unit_price`                           | Price Per Unit                           | `monetary`              |     |       |                                  |
| `can_be_expensed`                           | Expenses                                 | `boolean`               |     |       |                                  |
| `can_image_1024_be_zoomed`                  | Can Image 1024 be zoomed                 | `boolean`               |     |       |                                  |
| `can_image_variant_1024_be_zoomed`          | Can Variant Image 1024 be zoomed         | `boolean`               |     | ✅    |                                  |
| `can_publish`                               | Can Publish                              | `boolean`               |     |       |                                  |
| `categ_id`                                  | Product Category                         | `many2one`              |     |       | product.category                 |
| `code`                                      | Reference                                | `char`                  |     |       |                                  |
| `color`                                     | Color Index                              | `integer`               |     |       |                                  |
| `combination_indices`                       | Combination Indices                      | `char`                  |     | ✅    |                                  |
| `combo_ids`                                 | Combo Choices                            | `many2many`             |     |       | product.combo                    |
| `company_currency_id`                       | Valuation Currency                       | `many2one`              |     |       | res.currency                     |
| `company_id`                                | Company                                  | `many2one`              |     |       | res.company                      |
| `compare_list_price`                        | Compare to Price                         | `monetary`              |     |       |                                  |
| `cost_currency_id`                          | Cost Currency                            | `many2one`              |     |       | res.currency                     |
| `cost_method`                               | Cost Method                              | `selection`             |     |       |                                  |
| `country_of_origin`                         | Origin of Goods                          | `many2one`              |     |       | res.country                      |
| `create_date`                               | Created on                               | `datetime`              |     | ✅    |                                  |
| `create_uid`                                | Created by                               | `many2one`              |     | ✅    | res.users                        |
| `currency_id`                               | Currency                                 | `many2one`              |     |       | res.currency                     |
| `default_code`                              | Internal Reference                       | `char`                  |     | ✅    |                                  |
| `deferred_revenue_category_id`              | Deferred Revenue Type                    | `many2one`              |     |       | account.asset.category           |
| `description`                               | Description                              | `html`                  |     |       |                                  |
| `description_ecommerce`                     | eCommerce Description                    | `html`                  |     |       |                                  |
| `description_picking`                       | Description on Picking                   | `text`                  |     |       |                                  |
| `description_pickingin`                     | Description on Receptions                | `text`                  |     |       |                                  |
| `description_pickingout`                    | Description on Delivery Orders           | `text`                  |     |       |                                  |
| `description_purchase`                      | Purchase Description                     | `text`                  |     |       |                                  |
| `description_sale`                          | Sales Description                        | `text`                  |     |       |                                  |
| `display_name`                              | Display Name                             | `char`                  |     |       |                                  |
| `event_ticket_ids`                          | Event Tickets                            | `one2many`              |     | ✅    | event.event.ticket               |
| `expense_policy`                            | Re-Invoice Costs                         | `selection`             |     |       |                                  |
| `expense_policy_tooltip`                    | Expense Policy Tooltip                   | `char`                  |     |       |                                  |
| `fiscal_country_codes`                      | Fiscal Country Codes                     | `char`                  |     |       |                                  |
| `free_qty`                                  | Free To Use Quantity                     | `float`                 |     |       |                                  |
| `has_available_route_ids`                   | Routes can be selected on this product   | `boolean`               |     |       |                                  |
| `has_configurable_attributes`               | Is a configurable product                | `boolean`               |     |       |                                  |
| `has_message`                               | Has Message                              | `boolean`               |     |       |                                  |
| `hs_code`                                   | HS Code                                  | `char`                  |     |       |                                  |
| `id`                                        | ID                                       | `integer`               |     | ✅    |                                  |
| `image_1024`                                | Image 1024                               | `binary`                |     |       |                                  |
| `image_128`                                 | Image 128                                | `binary`                |     |       |                                  |
| `image_1920`                                | Image                                    | `binary`                |     |       |                                  |
| `image_256`                                 | Image 256                                | `binary`                |     |       |                                  |
| `image_512`                                 | Image 512                                | `binary`                |     |       |                                  |
| `image_variant_1024`                        | Variant Image 1024                       | `binary`                |     | ✅    |                                  |
| `image_variant_128`                         | Variant Image 128                        | `binary`                |     | ✅    |                                  |
| `image_variant_1920`                        | Variant Image                            | `binary`                |     | ✅    |                                  |
| `image_variant_256`                         | Variant Image 256                        | `binary`                |     | ✅    |                                  |
| `image_variant_512`                         | Variant Image 512                        | `binary`                |     | ✅    |                                  |
| `incoming_qty`                              | Incoming                                 | `float`                 |     |       |                                  |
| `invoice_policy`                            | Invoicing Policy                         | `selection`             |     |       |                                  |
| `is_dynamically_created`                    | Is Dynamically Created                   | `boolean`               |     |       |                                  |
| `is_favorite`                               | Favorite                                 | `boolean`               |     | ✅    |                                  |
| `is_in_purchase_order`                      | Is In Purchase Order                     | `boolean`               |     |       |                                  |
| `is_in_selected_section_of_order`           | Is In Selected Section Of Order          | `boolean`               |     | ✅    |                                  |
| `is_product_variant`                        | Is Product Variant                       | `boolean`               |     |       |                                  |
| `is_published`                              | Is Published                             | `boolean`               |     |       |                                  |
| `is_seo_optimized`                          | SEO optimized                            | `boolean`               |     |       |                                  |
| `is_storable`                               | Track Inventory                          | `boolean`               |     |       |                                  |
| `list_price`                                | Sales Price                              | `float`                 |     |       |                                  |
| `location_id`                               | Location                                 | `many2one`              |     |       | stock.location                   |
| `lot_properties_definition`                 | Lot Properties                           | `properties_definition` |     | ✅    |                                  |
| `lot_sequence_id`                           | Serial/Lot Numbers Sequence              | `many2one`              |     |       | ir.sequence                      |
| `lot_valuated`                              | Valuation by Lot/Serial                  | `boolean`               |     |       |                                  |
| `lst_price`                                 | Sales Price                              | `float`                 |     |       |                                  |
| `message_attachment_count`                  | Attachment Count                         | `integer`               |     |       |                                  |
| `message_follower_ids`                      | Followers                                | `one2many`              |     | ✅    | mail.followers                   |
| `message_has_error`                         | Message Delivery error                   | `boolean`               |     |       |                                  |
| `message_has_error_counter`                 | Number of errors                         | `integer`               |     |       |                                  |
| `message_has_sms_error`                     | SMS Delivery error                       | `boolean`               |     |       |                                  |
| `message_ids`                               | Messages                                 | `one2many`              |     | ✅    | mail.message                     |
| `message_is_follower`                       | Is Follower                              | `boolean`               |     |       |                                  |
| `message_needaction`                        | Action Needed                            | `boolean`               |     |       |                                  |
| `message_needaction_counter`                | Number of Actions                        | `integer`               |     |       |                                  |
| `message_partner_ids`                       | Followers (Partners)                     | `many2many`             |     |       | res.partner                      |
| `monthly_demand`                            | Monthly Demand                           | `float`                 |     |       |                                  |
| `my_activity_date_deadline`                 | My Activity Deadline                     | `date`                  |     |       |                                  |
| `name`                                      | Name                                     | `char`                  | ✅  |       |                                  |
| `nbr_moves_in`                              | Nbr Moves In                             | `integer`               |     |       |                                  |
| `nbr_moves_out`                             | Nbr Moves Out                            | `integer`               |     |       |                                  |
| `nbr_reordering_rules`                      | Reordering Rules                         | `integer`               |     |       |                                  |
| `next_serial`                               | Next Serial                              | `char`                  |     |       |                                  |
| `optional_product_ids`                      | Optional Products                        | `many2many`             |     |       | product.template                 |
| `orderpoint_ids`                            | Minimum Stock Rules                      | `one2many`              |     | ✅    | stock.warehouse.orderpoint       |
| `outgoing_qty`                              | Outgoing                                 | `float`                 |     |       |                                  |
| `out_of_stock_message`                      | Out-of-Stock Message                     | `html`                  |     |       |                                  |
| `partner_ref`                               | Customer Ref                             | `char`                  |     |       |                                  |
| `price_extra`                               | Variant Price Extra                      | `float`                 |     |       |                                  |
| `pricelist_rule_ids`                        | Pricelist Rules                          | `one2many`              |     |       | product.pricelist.item           |
| `product_catalog_product_is_in_sale_order`  | Product Catalog Product Is In Sale Order | `boolean`               |     |       |                                  |
| `product_document_count`                    | Documents Count                          | `integer`               |     |       |                                  |
| `product_document_ids`                      | Documents                                | `one2many`              |     | ✅    | product.document                 |
| `product_properties`                        | Properties                               | `properties`            |     |       |                                  |
| `product_tag_ids`                           | Tags                                     | `many2many`             |     |       | product.tag                      |
| `product_template_attribute_value_ids`      | Attribute Values                         | `many2many`             |     | ✅    | product.template.attribute.value |
| `product_template_image_ids`                | Extra Product Media                      | `one2many`              |     |       | product.image                    |
| `product_template_variant_value_ids`        | Variant Values                           | `many2many`             |     | ✅    | product.template.attribute.value |
| `product_tmpl_id`                           | Product Template                         | `many2one`              | ✅  | ✅    | product.template                 |
| `product_tooltip`                           | Product Tooltip                          | `char`                  |     |       |                                  |
| `product_uom_ids`                           | Unit Barcode                             | `one2many`              |     | ✅    | product.uom                      |
| `product_variant_count`                     | # Product Variants                       | `integer`               |     |       |                                  |
| `product_variant_id`                        | Product                                  | `many2one`              |     |       | product.product                  |
| `product_variant_ids`                       | Products                                 | `one2many`              | ✅  |       | product.product                  |
| `product_variant_image_ids`                 | Extra Variant Images                     | `one2many`              |     | ✅    | product.image                    |
| `property_account_expense_id`               | Expense Account                          | `many2one`              |     |       | account.account                  |
| `property_account_income_id`                | Income Account                           | `many2one`              |     |       | account.account                  |
| `property_price_difference_account_id`      | Price Difference Account                 | `many2one`              |     |       | account.account                  |
| `property_stock_inventory`                  | Inventory Location                       | `many2one`              |     |       | stock.location                   |
| `property_stock_production`                 | Production Location                      | `many2one`              |     |       | stock.location                   |
| `public_categ_ids`                          | Website Product Category                 | `many2many`             |     |       | product.public.category          |
| `publish_date`                              | Publish Date                             | `datetime`              | ✅  |       |                                  |
| `purchased_product_qty`                     | Purchased                                | `float`                 |     |       |                                  |
| `purchase_line_warn_msg`                    | Message for Purchase Order Line          | `text`                  |     |       |                                  |
| `purchase_method`                           | Control Policy                           | `selection`             |     |       |                                  |
| `purchase_ok`                               | Purchase                                 | `boolean`               |     |       |                                  |
| `purchase_order_line_ids`                   | PO Lines                                 | `one2many`              |     | ✅    | purchase.order.line              |
| `putaway_rule_ids`                          | Putaway Rules                            | `one2many`              |     | ✅    | stock.putaway.rule               |
| `qty_available`                             | Quantity On Hand                         | `float`                 |     |       |                                  |
| `rating_avg`                                | Average Rating                           | `float`                 |     |       |                                  |
| `rating_avg_text`                           | Rating Avg Text                          | `selection`             |     |       |                                  |
| `rating_count`                              | Rating count                             | `integer`               |     |       |                                  |
| `rating_ids`                                | Ratings                                  | `one2many`              |     | ✅    | rating.rating                    |
| `rating_last_feedback`                      | Rating Last Feedback                     | `text`                  |     |       |                                  |
| `rating_last_image`                         | Rating Last Image                        | `binary`                |     |       |                                  |
| `rating_last_text`                          | Rating Text                              | `selection`             |     |       |                                  |
| `rating_last_value`                         | Rating Last Value                        | `float`                 |     |       |                                  |
| `rating_percentage_satisfaction`            | Rating Satisfaction                      | `float`                 |     |       |                                  |
| `reordering_max_qty`                        | Reordering Max Qty                       | `float`                 |     |       |                                  |
| `reordering_min_qty`                        | Reordering Min Qty                       | `float`                 |     |       |                                  |
| `responsible_id`                            | Responsible                              | `many2one`              |     |       | res.users                        |
| `route_from_categ_ids`                      | Category Routes                          | `many2many`             |     |       | stock.route                      |
| `route_ids`                                 | Routes                                   | `many2many`             |     |       | stock.route                      |
| `sale_delay`                                | Customer Lead Time                       | `integer`               |     |       |                                  |
| `sale_line_warn_msg`                        | Sales Order Line Warning                 | `text`                  |     |       |                                  |
| `sale_ok`                                   | Sales                                    | `boolean`               |     |       |                                  |
| `sales_count`                               | Sold                                     | `float`                 |     |       |                                  |
| `seller_ids`                                | Vendors                                  | `one2many`              |     |       | product.supplierinfo             |
| `seo_name`                                  | Seo name                                 | `char`                  |     |       |                                  |
| `sequence`                                  | Sequence                                 | `integer`               |     |       |                                  |
| `serial_prefix_format`                      | Custom Lot/Serial                        | `char`                  |     |       |                                  |
| `service_to_purchase`                       | Subcontract Service                      | `boolean`               |     |       |                                  |
| `service_tracking`                          | Create on Order                          | `selection`             | ✅  |       |                                  |
| `service_type`                              | Track Service                            | `selection`             |     |       |                                  |
| `show_availability`                         | Show availability Qty                    | `boolean`               |     |       |                                  |
| `show_forecasted_qty_status_button`         | Show Forecasted Qty Status Button        | `boolean`               |     |       |                                  |
| `show_on_hand_qty_status_button`            | Show On Hand Qty Status Button           | `boolean`               |     |       |                                  |
| `show_qty_update_button`                    | Show Qty Update Button                   | `boolean`               |     |       |                                  |
| `standard_price`                            | Cost                                     | `float`                 |     | ✅    |                                  |
| `standard_price_update_warning`             | Standard Price Update Warning            | `char`                  |     |       |                                  |
| `stock_move_ids`                            | Stock Move                               | `one2many`              |     | ✅    | stock.move                       |
| `stock_notification_partner_ids`            | Back in stock Notifications              | `many2many`             |     | ✅    | res.partner                      |
| `stock_quant_ids`                           | Stock Quant                              | `one2many`              |     | ✅    | stock.quant                      |
| `storage_category_capacity_ids`             | Storage Category Capacity                | `one2many`              |     | ✅    | stock.storage.category.capacity  |
| `suggested_qty`                             | Suggested Qty                            | `integer`               |     |       |                                  |
| `suggest_estimated_price`                   | Suggest Estimated Price                  | `float`                 |     |       |                                  |
| `supplier_taxes_id`                         | Purchase Taxes                           | `many2many`             |     |       | account.tax                      |
| `taxes_id`                                  | Sales Taxes                              | `many2many`             |     |       | account.tax                      |
| `tax_string`                                | Tax String                               | `char`                  |     |       |                                  |
| `total_value`                               | Total Value                              | `monetary`              |     |       |                                  |
| `tracking`                                  | Tracking                                 | `selection`             | ✅  |       |                                  |
| `type`                                      | Product Type                             | `selection`             | ✅  |       |                                  |
| `uom_id`                                    | Unit                                     | `many2one`              | ✅  |       | uom.uom                          |
| `uom_ids`                                   | Packagings                               | `many2many`             |     |       | uom.uom                          |
| `uom_name`                                  | Unit Name                                | `char`                  |     |       |                                  |
| `valid_ean`                                 | Barcode is valid EAN                     | `boolean`               |     |       |                                  |
| `valid_product_template_attribute_line_ids` | Valid Product Attribute Lines            | `many2many`             |     |       | product.template.attribute.line  |
| `valuation`                                 | Valuation                                | `selection`             |     |       |                                  |
| `variant_ribbon_id`                         | Variant Ribbon                           | `many2one`              |     | ✅    | product.ribbon                   |
| `variants_default_code`                     | Variants Default Code                    | `char`                  |     |       |                                  |
| `variant_seller_ids`                        | Variant Seller                           | `one2many`              |     |       | product.supplierinfo             |
| `virtual_available`                         | Forecasted Quantity                      | `float`                 |     |       |                                  |
| `visible_expense_policy`                    | Re-Invoice Policy visible                | `boolean`               |     |       |                                  |
| `volume`                                    | Volume                                   | `float`                 |     | ✅    |                                  |
| `volume_uom_name`                           | Volume unit of measure label             | `char`                  |     |       |                                  |
| `warehouse_id`                              | Warehouse                                | `many2one`              |     |       | stock.warehouse                  |
| `website_absolute_url`                      | Website Absolute URL                     | `char`                  |     |       |                                  |
| `website_description`                       | Description for the website              | `html`                  |     |       |                                  |
| `website_id`                                | Website                                  | `many2one`              |     |       | website                          |
| `website_message_ids`                       | Website Messages                         | `one2many`              |     | ✅    | mail.message                     |
| `website_meta_description`                  | Website meta description                 | `text`                  |     |       |                                  |
| `website_meta_keywords`                     | Website meta keywords                    | `char`                  |     |       |                                  |
| `website_meta_og_img`                       | Website opengraph image                  | `char`                  |     |       |                                  |
| `website_meta_title`                        | Website meta title                       | `char`                  |     |       |                                  |
| `website_published`                         | Visible on current website               | `boolean`               |     |       |                                  |
| `website_ribbon_id`                         | Ribbon                                   | `many2one`              |     |       | product.ribbon                   |
| `website_sequence`                          | Website Sequence                         | `integer`               |     |       |                                  |
| `website_size_x`                            | Size X                                   | `integer`               |     |       |                                  |
| `website_size_y`                            | Size Y                                   | `integer`               |     |       |                                  |
| `website_url`                               | Website URL                              | `char`                  |     |       |                                  |
| `weight`                                    | Weight                                   | `float`                 |     | ✅    |                                  |
| `weight_uom_name`                           | Weight unit of measure label             | `char`                  |     |       |                                  |
| `write_date`                                | Write Date                               | `datetime`              |     | ✅    |                                  |
| `write_uid`                                 | Last Updated by                          | `many2one`              |     | ✅    | res.users                        |

**Access Rights:**

| Name                          | Group             | Perms     |
| ----------------------------- | ----------------- | --------- |
| product.product.purchase.user | Purchase / User   | `R`       |
| product.product manager       | Products / Create | `R/W/C/D` |
| product_product_stock_user    | Inventory / User  | `R`       |
| product.product.account.user  | Auditor           | `R`       |
| product.product.public        | Role / Portal     | `R`       |
| product.product.public        | Role / Public     | `R`       |
| product.product employee      | Role / User       | `R`       |
| product.product.public        | Role / User       | `R`       |

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

### 🗃️ `op.admission.fees.line` — Admission Fees Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                    | Label              | Type       | Req | Store | Relation              |
| ------------------------ | ------------------ | ---------- | --- | ----- | --------------------- |
| `course_fees_product_id` | Course Fees        | `many2one` |     | ✅    | product.product       |
| `course_id`              | Course             | `many2one` | ✅  | ✅    | op.course             |
| `create_date`            | Created on         | `datetime` |     | ✅    |                       |
| `create_uid`             | Created by         | `many2one` |     | ✅    | res.users             |
| `display_name`           | Display Name       | `char`     |     |       |                       |
| `id`                     | ID                 | `integer`  |     | ✅    |                       |
| `register_id`            | Admission Register | `many2one` |     | ✅    | op.admission.register |
| `register_product_id`    | Fees               | `many2one` |     | ✅    | product.product       |
| `registration_fees`      | Registration Fees  | `boolean`  |     | ✅    |                       |
| `write_date`             | Last Updated on    | `datetime` |     | ✅    |                       |
| `write_uid`              | Last Updated by    | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                                        | Group                | Perms     |
| ------------------------------------------- | -------------------- | --------- |
| access_op_admission_fees_line_admin         | OpenEduCat / Manager | `R/W/C/D` |
| access_op_admission_fees_line_portal        | Role / Portal        | `R/W/C`   |
| access_op_admission_fees_line_portal_public | Role / Public        | `R/W/C`   |

### 🗃️ `website.menu` — Website Menu

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                 | Label                | Type        | Req | Store | Relation                |
| --------------------- | -------------------- | ----------- | --- | ----- | ----------------------- |
| `child_id`            | Child Menus          | `one2many`  |     | ✅    | website.menu            |
| `controller_page_id`  | Related Model Page   | `many2one`  |     | ✅    | website.controller.page |
| `create_date`         | Created on           | `datetime`  |     | ✅    |                         |
| `create_uid`          | Created by           | `many2one`  |     | ✅    | res.users               |
| `display_name`        | Display Name         | `char`      |     |       |                         |
| `group_ids`           | Visible Groups       | `many2many` |     | ✅    | res.groups              |
| `id`                  | ID                   | `integer`   |     | ✅    |                         |
| `is_admission_parent` | Is admission Parent  | `boolean`   |     | ✅    |                         |
| `is_alumni_parent`    | Is alumni job Parent | `boolean`   |     | ✅    |                         |
| `is_mega_menu`        | Is Mega Menu         | `boolean`   |     |       |                         |
| `is_visible`          | Is Visible           | `boolean`   |     |       |                         |
| `mega_menu_classes`   | Mega Menu Classes    | `char`      |     | ✅    |                         |
| `mega_menu_content`   | Mega Menu Content    | `html`      |     | ✅    |                         |
| `name`                | Menu                 | `char`      | ✅  | ✅    |                         |
| `new_window`          | New Window           | `boolean`   |     | ✅    |                         |
| `page_id`             | Related Page         | `many2one`  |     | ✅    | website.page            |
| `parent_id`           | Parent Menu          | `many2one`  |     | ✅    | website.menu            |
| `parent_path`         | Parent Path          | `char`      |     | ✅    |                         |
| `sequence`            | Sequence             | `integer`   |     | ✅    |                         |
| `theme_template_id`   | Theme Template       | `many2one`  |     | ✅    | theme.website.menu      |
| `url`                 | Url                  | `char`      | ✅  | ✅    |                         |
| `website_id`          | Website              | `many2one`  |     | ✅    | website                 |
| `write_date`          | Last Updated on      | `datetime`  |     | ✅    |                         |
| `write_uid`           | Last Updated by      | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name                | Group                         | Perms     |
| ------------------- | ----------------------------- | --------- |
| Web Menu Manager    | Website / Editor and Designer | `R/W/C/D` |
| access_website_menu | Role / Portal                 | `R`       |
| access_website_menu | Role / Public                 | `R`       |
| access_website_menu | Role / User                   | `R`       |

**Record Rules:**

- **Website menu: group_ids** (Global) `R/W/C/D`
  - Domain:
    `['|', ('group_ids', '=', False), ('group_ids', 'in', user.all_group_ids.ids)]`
