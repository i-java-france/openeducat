---
title: "OpenEduCat Health Enterprise"
module: "openeducat_health_enterprise"
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

# 🟢 OpenEduCat Health Enterprise

> **Module:** `openeducat_health_enterprise` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_core_enterprise]] [[uom]]

## 📖 Description

## OpenEduCat Health

### Manage Health Details

[![Logo](/openeducat_health_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module allows you to manage health details for students and faculties.

[Contact Us](https://www.openeducat.org/contactus/)

## Health

You can maintain health related details like eye glasses and any regular check up for
students and faculties.

![Health](/openeducat_health_enterprise/static/description/health.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `SIS/General/Health`

### Views

- `* INHERIT op.faculty.form (form)`
- `* INHERIT op.student.form (form)`
- `* INHERIT student_portal_health (qweb)`
- `op.health.form (form)`
- `op.health.list (list)`
- `op.health.search (search)`

### Reports

_none_

## 🛠️ Technical Documentation

**4 model(s) defined by this module:**

### 🗃️ `op.health` — Health Detail for Students and Faculties

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
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company        |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `eyeglasses`                    | Eye Glasses                   | `boolean`   |     | ✅    |                    |
| `eyeglasses_no`                 | Eye Glasses                   | `char`      |     | ✅    |                    |
| `eye_status`                    | Eye Vision Type               | `selection` |     | ✅    |                    |
| `eye_with_number`               | Which Eye Has Glasses?        | `selection` |     | ✅    |                    |
| `faculty_id`                    | Faculty                       | `many2one`  |     | ✅    | op.faculty         |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `health_line`                   | Checkup Lines                 | `one2many`  |     | ✅    | op.health.line     |
| `height`                        | Height                        | `float`     | ✅  | ✅    |                    |
| `height_uom_id`                 | Height Unit                   | `many2one`  |     | ✅    | uom.uom            |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
| `left_eye_hyperopia`            | Left Eye Hyperopia            | `float`     |     | ✅    |                    |
| `left_eye_myopia`               | Left Eye Myopia               | `float`     |     | ✅    |                    |
| `major_diseases`                | Major Diseases                | `boolean`   |     | ✅    |                    |
| `major_diseases_note`           | Major Diseases                | `text`      |     | ✅    |                    |
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
| `name`                          | Name                          | `char`      |     | ✅    |                    |
| `physical_challenges`           | Physical Challenge            | `boolean`   |     | ✅    |                    |
| `physical_challenges_note`      | Physical Challenge            | `text`      |     | ✅    |                    |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `regular_checkup`               | Any Regular Checkup Required  | `boolean`   |     | ✅    |                    |
| `right_eye_hyperopia`           | Right Eye Hyperopia           | `float`     |     | ✅    |                    |
| `right_eye_myopia`              | Right Eye Myopia              | `float`     |     | ✅    |                    |
| `state`                         | Status                        | `selection` |     | ✅    |                    |
| `student_id`                    | Student                       | `many2one`  |     | ✅    | op.student         |
| `type`                          | Type                          | `selection` | ✅  | ✅    |                    |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `weight`                        | Weight                        | `float`     | ✅  | ✅    |                    |
| `weight_uom_id`                 | Weight Unit                   | `many2one`  |     | ✅    | uom.uom            |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                   | Group            | Perms     |
| ---------------------- | ---------------- | --------- |
| name_op_health_student | Health / Manager | `R/W/C/D` |
| name_op_health_faculty | Health / User    | `R/W`     |

**Record Rules:**

- **Health multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

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

### 🗃️ `op.health.line` — Health Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label                  | Type       | Req | Store | Relation    |
| ---------------- | ---------------------- | ---------- | --- | ----- | ----------- |
| `company_id`     | Company                | `many2one` |     | ✅    | res.company |
| `create_date`    | Created on             | `datetime` |     | ✅    |             |
| `create_uid`     | Created by             | `many2one` |     | ✅    | res.users   |
| `date`           | Date                   | `date`     |     | ✅    |             |
| `display_name`   | Display Name           | `char`     |     |       |             |
| `health_id`      | Health                 | `many2one` |     | ✅    | op.health   |
| `id`             | ID                     | `integer`  |     | ✅    |             |
| `name`           | Checkup Detail         | `text`     | ✅  | ✅    |             |
| `recommendation` | Checkup Recommendation | `text`     |     | ✅    |             |
| `write_date`     | Last Updated on        | `datetime` |     | ✅    |             |
| `write_uid`      | Last Updated by        | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                        | Group            | Perms     |
| --------------------------- | ---------------- | --------- |
| name_op_health_line_student | Health / Manager | `R/W/C/D` |
| name_op_health_line_faculty | Health / User    | `R/W`     |

**Record Rules:**

- **Health Line multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`
