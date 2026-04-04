---
title: "OpenEduCat Admission Esign"
module: "openeducat_admission_esign"
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

# 🟢 OpenEduCat Admission Esign

> **Module:** `openeducat_admission_esign` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_admission_enterprise]] [[esign_intg]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT E-sign Request Form Inherit (form)`
- `* INHERIT inherit.op.admission.form (form)`
- `Admission Letter (qweb)`
- `admission_letter_header_footer (qweb)`
- `report_admission_letter_request (qweb)`

### Reports

- `Student Admission Letter`

## 🛠️ Technical Documentation

**4 model(s) defined by this module:**

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

### 🗃️ `e.sign.template.lines` — E-sign Template Lines

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
| `alignment`                     | Alignment                     | `char`      | ✅  | ✅    |                    |
| `company_custom`                | Company Custom                | `selection` |     | ✅    |                    |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `find_text`                     | Text                          | `char`      |     | ✅    |                    |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `height`                        | Height                        | `float`     |     | ✅    |                    |
| `height_pix`                    | Height Pix                    | `float`     |     | ✅    |                    |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
| `is_position`                   | Is Position?                  | `boolean`   |     | ✅    |                    |
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
| `option_ids`                    | Selection options             | `many2many` |     | ✅    | e.sign.item.option |
| `page_height`                   | Page Height                   | `float`     |     | ✅    |                    |
| `page_number`                   | Page Number                   | `integer`   |     | ✅    |                    |
| `page_width`                    | Page Width                    | `float`     |     | ✅    |                    |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `required`                      | Required                      | `boolean`   |     | ✅    |                    |
| `responsible_id`                | Responsible                   | `many2one`  |     | ✅    | e.sign.item.role   |
| `responsible_key`               | Responsible Key               | `char`      |     | ✅    |                    |
| `template_id`                   | Template                      | `many2one`  |     | ✅    | e.sign.template    |
| `type_id`                       | Type                          | `many2one`  | ✅  | ✅    | e.sign.items       |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `width`                         | Width                         | `float`     |     | ✅    |                    |
| `width_pix`                     | Width Pix                     | `float`     |     | ✅    |                    |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |
| `x_offset`                      | X Offset                      | `float`     |     | ✅    |                    |
| `x_position`                    | X Position                    | `float`     |     | ✅    |                    |
| `x_position_percentage`         | X Position Percentage         | `float`     |     | ✅    |                    |
| `y_offset`                      | Y Offset                      | `float`     |     | ✅    |                    |
| `y_position`                    | Y Position                    | `float`     |     | ✅    |                    |
| `y_position_percentage`         | Y Position Percentage         | `float`     |     | ✅    |                    |

**Access Rights:**

| Name                                | Group         | Perms     |
| ----------------------------------- | ------------- | --------- |
| access_e_sign_template_lines_portal | Role / Portal | `R/W/C/D` |
| access_e_sign_template_lines        | Role / User   | `R/W/C/D` |

### 🗃️ `e.sign.request` — Signature Request

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation            |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------- |
| `access_token`                  | Security Token                | `char`      |     | ✅    |                     |
| `access_token_expired`          | Access Token Expired          | `boolean`   |     | ✅    |                     |
| `access_url`                    | Portal Access URL             | `char`      |     |       |                     |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event      |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                     |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                     |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                     |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity       |
| `activity_state`                | Activity State                | `selection` |     |       |                     |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                     |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                     |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type  |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users           |
| `color`                         | Color                         | `integer`   |     | ✅    |                     |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company         |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                     |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users           |
| `display_name`                  | Display Name                  | `char`      |     |       |                     |
| `doc_name`                      | Document Name                 | `char`      |     |       |                     |
| `favorited_ids`                 | Favorite of                   | `many2many` |     | ✅    | res.users           |
| `final_pdf`                     | Final Pdf                     | `binary`    |     | ✅    |                     |
| `group_ids`                     | Template Access Group         | `many2many` |     | ✅    | res.groups          |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                     |
| `id`                            | ID                            | `integer`   |     | ✅    |                     |
| `is_sign_order`                 | Sign Order                    | `boolean`   |     | ✅    |                     |
| `item_info`                     | Item Info                     | `binary`    |     |       |                     |
| `last_action_date`              | Last Action Date              | `datetime`  |     |       |                     |
| `message`                       | sign.message                  | `html`      |     | ✅    |                     |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                     |
| `message_cc`                    | sign.message_cc               | `html`      |     | ✅    |                     |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers      |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                     |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                     |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                     |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message        |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                     |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                     |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                     |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner         |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                     |
| `privacy`                       | Who can Sign                  | `selection` |     | ✅    |                     |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating       |
| `request_item_ids`              | Signers                       | `one2many`  |     | ✅    | e.sign.request.item |
| `sign_closed`                   | Completed Signatures          | `integer`   |     |       |                     |
| `sign_log_ids`                  | Logs                          | `one2many`  |     | ✅    | e.sign.logs         |
| `sign_total`                    | Requested Signatures          | `integer`   |     |       |                     |
| `sign_wait`                     | Sent Requests                 | `integer`   |     |       |                     |
| `sign_with_key`                 | Sign With Key                 | `boolean`   |     | ✅    |                     |
| `state`                         | State                         | `selection` |     | ✅    |                     |
| `status_url`                    | Status URL                    | `char`      |     | ✅    |                     |
| `subject`                       | Email Subject                 | `char`      |     | ✅    |                     |
| `tag_ids`                       | Tags                          | `many2many` |     |       | esign.tag           |
| `template_id`                   | Template                      | `many2one`  |     | ✅    | e.sign.template     |
| `url`                           | URL                           | `char`      |     | ✅    |                     |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message        |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                     |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                         | Group         | Perms     |
| ---------------------------- | ------------- | --------- |
| access_e_sign_request_portal | Role / Portal | `R/W/C/D` |
| access_e_sign_request_public | Role / Public | `R/W/C/D` |
| access_e_sign_request        | Role / User   | `R/W/C/D` |
