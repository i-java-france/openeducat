---
title: "OpenEduCat Placement Job Enterprise"
module: "openeducat_placement_job_enterprise"
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

# 🟢 OpenEduCat Placement Job Enterprise

> **Module:** `openeducat_placement_job_enterprise` | **Version:** `19.0.1.0`
> **Category:** Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc
> **Website:** https://www.openeducat.org

## 🔗 Dependencies

[[base]] [[openeducat_core_enterprise]] [[openeducat_skill_enterprise]]
[[openeducat_placement_enterprise]] [[openeducat_job_enterprise]] [[website_event]]
[[contacts]] [[mail]]

## 📖 Description

## OpenEduCat Placement Job Enterprise

### Manage creating Activity Announcement and to see and manage the applicants for the particular job post

[![](/openeducat_placement_job_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

Based on best of class enterprise level architecture, OpenEduCat is ready to be used
from local infrastructure to a highly scalable cloud environment.

[Contact Us](https://www.openeducat.org/contactus/)

## Activity Announcement Management

User can create a Activity Announcement with different configurations.

![](/openeducat_placement_job_enterprise/static/description/activity_announcement_view.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Placements/Campus Events`
- `Placements/Configuration/Event Stages`
- `Placements/Configuration/Event Tages`
- `Placements/Configuration/Event Templates`
- `Placements/Configuration/Partner Companies`
- `Placements/Configuration/Recruitment Sessions`
- `Placements/Opportunities/Job Opportunities`
- `Placements/Opportunities/Student Applications`

### Views

- `* INHERIT Job Post Apply (qweb)`
- `* INHERIT event.event.form (form)`
- `* INHERIT jobpost_description_new (qweb)`
- `* INHERIT op.job.applicant.form (form)`
- `* INHERIT op.job.applicant.list (list)`
- `* INHERIT op.placement.cell.inherit.kanban (kanban)`
- `* INHERIT res.partner.form (form)`
- `Activity Apply (qweb)`
- `Activity Detail (qweb)`
- `Activity Detail (qweb)`
- `op.activity.announcement.activity (activity)`
- `op.activity.announcement.calendar (calendar)`
- `op.activity.announcement.form (form)`
- `op.activity.announcement.kanban (kanban)`
- `op.activity.announcement.list (list)`
- `op.activity.announcement.pivot (pivot)`
- `op.activity.announcement.search (search)`
- `placement.officer.create.wizard.form (form)`
- `training.season.form (form)`
- `training.season.list (list)`
- `training.season.search (search)`

### Reports

_none_

## 🛠️ Technical Documentation

**6 model(s) defined by this module:**

### 🗃️ `op.activity.announcement` — Activity Announcement

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
| `application_count`             | Application Count             | `integer`   |     |       |                       |
| `application_line_ids`          | Application Lines             | `one2many`  |     | ✅    | op.job.applicant      |
| `can_publish`                   | Can Publish                   | `boolean`   |     |       |                       |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company           |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                       |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users             |
| `description`                   | Description                   | `text`      |     | ✅    |                       |
| `display_name`                  | Display Name                  | `char`      |     |       |                       |
| `end_date`                      | End Date                      | `date`      | ✅  | ✅    |                       |
| `experience`                    | Experience                    | `selection` |     | ✅    |                       |
| `group_discussion`              | Group Discussion              | `boolean`   |     | ✅    |                       |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                       |
| `id`                            | ID                            | `integer`   |     | ✅    |                       |
| `is_favorite`                   | Favorite                      | `boolean`   |     | ✅    |                       |
| `is_published`                  | Is Published                  | `boolean`   |     | ✅    |                       |
| `is_read`                       | Is Read                       | `boolean`   |     | ✅    |                       |
| `is_seo_optimized`              | SEO optimized                 | `boolean`   |     | ✅    |                       |
| `job_post_id`                   | Job Post                      | `many2many` |     | ✅    | op.job.post           |
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
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                       |
| `name`                          | Name                          | `char`      | ✅  | ✅    |                       |
| `opportunity_type`              | Opportunity Type              | `selection` |     | ✅    |                       |
| `partner_id`                    | Partner Company               | `many2one`  |     | ✅    | res.partner           |
| `process`                       | Process                       | `selection` |     | ✅    |                       |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating         |
| `salary`                        | Salary                        | `float`     |     | ✅    |                       |
| `season_id`                     | Session                       | `many2one`  | ✅  | ✅    | training.season       |
| `seo_name`                      | Seo name                      | `char`      |     | ✅    |                       |
| `seq`                           | Sequence                      | `char`      |     | ✅    |                       |
| `skill_id`                      | Required Skills               | `many2many` |     | ✅    | op.student.skill.name |
| `start_date`                    | Start Date                    | `date`      | ✅  | ✅    |                       |
| `state`                         | State                         | `selection` |     | ✅    |                       |
| `team_id`                       | Handled By                    | `many2one`  |     | ✅    | op.placement.cell     |
| `vacancies`                     | Vacancies                     | `integer`   |     | ✅    |                       |
| `website_absolute_url`          | Website Absolute URL          | `char`      |     |       |                       |
| `website_id`                    | Website                       | `many2one`  |     | ✅    | website               |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message          |
| `website_meta_description`      | Website meta description      | `text`      |     | ✅    |                       |
| `website_meta_keywords`         | Website meta keywords         | `char`      |     | ✅    |                       |
| `website_meta_og_img`           | Website opengraph image       | `char`      |     | ✅    |                       |
| `website_meta_title`            | Website meta title            | `char`      |     | ✅    |                       |
| `website_published`             | Visible on current website    | `boolean`   |     |       |                       |
| `website_url`                   | Website URL                   | `char`      |     |       |                       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                       |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users             |
| `written_test`                  | Written Test                  | `boolean`   |     | ✅    |                       |

**Access Rights:**

| Name                                   | Group                | Perms     |
| -------------------------------------- | -------------------- | --------- |
| access_op_activity_announcement        | OpenEduCat / Manager | `R/W/C/D` |
| access_op_activity_announcement_user   | OpenEduCat / User    | `R/W`     |
| access_op_activity_announcement_portal | Role / Portal        | `R/W`     |

**Record Rules:**

- **Activity Announcement multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `res.partner` — Contact

> 📧 Mail Thread

Update of res.partner class to take into account the livechat username.

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
| `applicant_ids`                             | Applicants                                          | `one2many`   |     | ✅    | hr.applicant                |
| `application_count`                         | Applications                                        | `integer`    |     |       |                             |
| `application_statistics`                    | Stats                                               | `json`       |     |       |                             |
| `autopost_bills`                            | Auto-post bills                                     | `selection`  | ✅  | ✅    |                             |
| `available_invoice_template_pdf_report_ids` | Available Invoice Template Pdf Report               | `one2many`   |     |       | ir.actions.report           |
| `available_peppol_eas`                      | Available Peppol Eas                                | `json`       |     |       |                             |
| `avatar_1024`                               | Avatar 1024                                         | `binary`     |     |       |                             |
| `avatar_128`                                | Avatar 128                                          | `binary`     |     |       |                             |
| `avatar_1920`                               | Avatar                                              | `binary`     |     |       |                             |
| `avatar_256`                                | Avatar 256                                          | `binary`     |     |       |                             |
| `avatar_512`                                | Avatar 512                                          | `binary`     |     |       |                             |
| `bank_account_count`                        | Bank                                                | `integer`    |     |       |                             |
| `bank_ids`                                  | Banks                                               | `one2many`   |     | ✅    | res.partner.bank            |
| `barcode`                                   | Barcode                                             | `char`       |     | ✅    |                             |
| `buyer_id`                                  | Buyer                                               | `many2one`   |     | ✅    | res.users                   |
| `calendar_last_notif_ack`                   | Last notification marked as read from base Calendar | `datetime`   |     | ✅    |                             |
| `can_publish`                               | Can Publish                                         | `boolean`    |     |       |                             |
| `category_id`                               | Tags                                                | `many2many`  |     | ✅    | res.partner.category        |
| `certifications_company_count`              | Company Certifications Count                        | `integer`    |     |       |                             |
| `certifications_count`                      | Certifications Count                                | `integer`    |     |       |                             |
| `channel_ids`                               | Channels                                            | `many2many`  |     | ✅    | discuss.channel             |
| `channel_member_ids`                        | Channel Member                                      | `one2many`   |     | ✅    | discuss.channel.member      |
| `chatbot_script_ids`                        | Chatbot Script                                      | `one2many`   |     | ✅    | chatbot.script              |
| `child_ids`                                 | Contact                                             | `one2many`   |     | ✅    | res.partner                 |
| `city`                                      | City                                                | `char`       |     | ✅    |                             |
| `code`                                      | Company Code                                        | `char`       |     | ✅    |                             |
| `color`                                     | Color Index                                         | `integer`    |     | ✅    |                             |
| `comment`                                   | Notes                                               | `html`       |     | ✅    |                             |
| `commercial_company_name`                   | Company Name Entity                                 | `char`       |     | ✅    |                             |
| `commercial_partner_id`                     | Commercial Entity                                   | `many2one`   |     | ✅    | res.partner                 |
| `company_id`                                | Company                                             | `many2one`   |     | ✅    | res.company                 |
| `company_name`                              | Company Name                                        | `char`       |     | ✅    |                             |
| `company_registry`                          | Company ID                                          | `char`       |     | ✅    |                             |
| `company_registry_label`                    | Company ID Label                                    | `char`       |     |       |                             |
| `company_registry_placeholder`              | Company Registry Placeholder                        | `char`       |     |       |                             |
| `company_type`                              | Company Type                                        | `selection`  |     |       |                             |
| `complete_name`                             | Complete Name                                       | `char`       |     | ✅    |                             |
| `contact_address`                           | Complete Address                                    | `char`       |     |       |                             |
| `contact_address_inline`                    | Inlined Complete Address                            | `char`       |     |       |                             |
| `contract_ids`                              | Partner Contracts                                   | `one2many`   |     | ✅    | account.analytic.account    |
| `country_code`                              | Country Code                                        | `char`       |     |       |                             |
| `country_id`                                | Country                                             | `many2one`   |     | ✅    | res.country                 |
| `create_date`                               | Created on                                          | `datetime`   |     | ✅    |                             |
| `create_uid`                                | Created by                                          | `many2one`   |     | ✅    | res.users                   |
| `credit`                                    | Total Receivable                                    | `monetary`   |     |       |                             |
| `credit_limit`                              | Credit Limit                                        | `float`      |     | ✅    |                             |
| `credit_to_invoice`                         | Credit To Invoice                                   | `monetary`   |     |       |                             |
| `currency_id`                               | Currency                                            | `many2one`   |     |       | res.currency                |
| `customer_rank`                             | Customer Rank                                       | `integer`    |     | ✅    |                             |
| `days_sales_outstanding`                    | Days Sales Outstanding (DSO)                        | `float`      |     |       |                             |
| `debit`                                     | Total Payable                                       | `monetary`   |     |       |                             |
| `display_invoice_edi_format`                | Display Invoice Edi Format                          | `boolean`    |     |       |                             |
| `display_invoice_template_pdf_report_id`    | Display Invoice Template Pdf Report                 | `boolean`    |     |       |                             |
| `display_name`                              | Display Name                                        | `char`       |     |       |                             |
| `duplicate_bank_partner_ids`                | Duplicate Bank Partner                              | `many2many`  |     |       | res.partner                 |
| `email`                                     | Email                                               | `char`       |     | ✅    |                             |
| `email_formatted`                           | Formatted Email                                     | `char`       |     |       |                             |
| `email_normalized`                          | Normalized Email                                    | `char`       |     | ✅    |                             |
| `employee`                                  | Employee                                            | `boolean`    |     | ✅    |                             |
| `employee_ids`                              | Employees                                           | `one2many`   |     | ✅    | hr.employee                 |
| `employees_count`                           | Employees Count                                     | `integer`    |     |       |                             |
| `event_count`                               | # Events                                            | `integer`    |     |       |                             |
| `fiscal_country_codes`                      | Fiscal Country Codes                                | `char`       |     |       |                             |
| `fiscal_country_group_codes`                | Fiscal Country Group Codes                          | `json`       |     |       |                             |
| `function`                                  | Job Position                                        | `char`       |     | ✅    |                             |
| `global_location_number`                    | GLN                                                 | `char`       |     | ✅    |                             |
| `group_on`                                  | Week Day                                            | `selection`  | ✅  | ✅    |                             |
| `group_rfq`                                 | Group RFQ                                           | `selection`  | ✅  | ✅    |                             |
| `has_message`                               | Has Message                                         | `boolean`    |     |       |                             |
| `head_office`                               | Head Office                                         | `char`       |     | ✅    |                             |
| `hr_contact`                                | HR Contact                                          | `char`       |     | ✅    |                             |
| `hr_email`                                  | HR Email                                            | `char`       |     | ✅    |                             |
| `hr_name`                                   | HR Name                                             | `char`       |     | ✅    |                             |
| `id`                                        | ID                                                  | `integer`    |     | ✅    |                             |
| `ignore_abnormal_invoice_amount`            | Ignore Abnormal Invoice Amount                      | `boolean`    |     | ✅    |                             |
| `ignore_abnormal_invoice_date`              | Ignore Abnormal Invoice Date                        | `boolean`    |     | ✅    |                             |
| `image_1024`                                | Image 1024                                          | `binary`     |     | ✅    |                             |
| `image_128`                                 | Image 128                                           | `binary`     |     | ✅    |                             |
| `image_1920`                                | Image                                               | `binary`     |     | ✅    |                             |
| `image_256`                                 | Image 256                                           | `binary`     |     | ✅    |                             |
| `image_512`                                 | Image 512                                           | `binary`     |     | ✅    |                             |
| `im_status`                                 | IM Status                                           | `char`       |     |       |                             |
| `industry_id`                               | Industry                                            | `many2one`   |     | ✅    | res.partner.industry        |
| `invoice_edi_format`                        | eInvoice format                                     | `selection`  |     |       |                             |
| `invoice_edi_format_store`                  | Invoice Edi Format Store                            | `char`       |     | ✅    |                             |
| `invoice_ids`                               | Invoices                                            | `one2many`   |     | ✅    | account.move                |
| `invoice_sending_method`                    | Invoice sending                                     | `selection`  |     | ✅    |                             |
| `invoice_template_pdf_report_id`            | Invoice report                                      | `many2one`   |     | ✅    | ir.actions.report           |
| `is_blacklisted`                            | Blacklist                                           | `boolean`    |     |       |                             |
| `is_company`                                | Is a Company                                        | `boolean`    |     | ✅    |                             |
| `is_in_call`                                | Is In Call                                          | `boolean`    |     |       |                             |
| `is_parent`                                 | Is a Parent                                         | `boolean`    |     | ✅    |                             |
| `is_peppol_edi_format`                      | Is Peppol Edi Format                                | `boolean`    |     |       |                             |
| `is_pickup_location`                        | Is Pickup Location                                  | `boolean`    |     | ✅    |                             |
| `is_public`                                 | Is Public                                           | `boolean`    |     |       |                             |
| `is_published`                              | Is Published                                        | `boolean`    |     | ✅    |                             |
| `is_seo_optimized`                          | SEO optimized                                       | `boolean`    |     | ✅    |                             |
| `is_student`                                | Is a Student                                        | `boolean`    |     | ✅    |                             |
| `is_ubl_format`                             | Is Ubl Format                                       | `boolean`    |     |       |                             |
| `is_venue`                                  | Venue                                               | `boolean`    |     | ✅    |                             |
| `lang`                                      | Language                                            | `selection`  |     | ✅    |                             |
| `leave_date_to`                             | Leave Date To                                       | `date`       |     |       |                             |
| `livechat_channel_count`                    | Livechat Channel Count                              | `integer`    |     |       |                             |
| `main_user_id`                              | Main User                                           | `many2one`   |     |       | res.users                   |
| `meeting_count`                             | # Meetings                                          | `integer`    |     |       |                             |
| `meeting_ids`                               | Meetings                                            | `many2many`  |     | ✅    | calendar.event              |
| `message_attachment_count`                  | Attachment Count                                    | `integer`    |     |       |                             |
| `message_bounce`                            | Bounce                                              | `integer`    |     | ✅    |                             |
| `message_follower_ids`                      | Followers                                           | `one2many`   |     | ✅    | mail.followers              |
| `message_has_error`                         | Message Delivery error                              | `boolean`    |     |       |                             |
| `message_has_error_counter`                 | Number of errors                                    | `integer`    |     |       |                             |
| `message_has_sms_error`                     | SMS Delivery error                                  | `boolean`    |     |       |                             |
| `message_ids`                               | Messages                                            | `one2many`   |     | ✅    | mail.message                |
| `message_is_follower`                       | Is Follower                                         | `boolean`    |     |       |                             |
| `message_needaction`                        | Action Needed                                       | `boolean`    |     |       |                             |
| `message_needaction_counter`                | Number of Actions                                   | `integer`    |     |       |                             |
| `message_partner_ids`                       | Followers (Partners)                                | `many2many`  |     |       | res.partner                 |
| `my_activity_date_deadline`                 | My Activity Deadline                                | `date`       |     |       |                             |
| `name`                                      | Name                                                | `char`       |     | ✅    |                             |
| `offline_since`                             | Offline since                                       | `datetime`   |     |       |                             |
| `on_time_rate`                              | On-Time Delivery Rate                               | `float`      |     |       |                             |
| `opportunity_count`                         | Opportunity Count                                   | `integer`    |     |       |                             |
| `opportunity_ids`                           | Opportunities                                       | `one2many`   |     | ✅    | crm.lead                    |
| `parent_id`                                 | Related Company                                     | `many2one`   |     | ✅    | res.partner                 |
| `parent_name`                               | Parent name                                         | `char`       |     |       |                             |
| `partner_company_registry_placeholder`      | Partner Company Registry Placeholder                | `char`       |     |       |                             |
| `partner_latitude`                          | Geo Latitude                                        | `float`      |     | ✅    |                             |
| `partner_longitude`                         | Geo Longitude                                       | `float`      |     | ✅    |                             |
| `partner_share`                             | Share Partner                                       | `boolean`    |     | ✅    |                             |
| `partner_vat_placeholder`                   | Partner Vat Placeholder                             | `char`       |     |       |                             |
| `payment_token_count`                       | Payment Token Count                                 | `integer`    |     |       |                             |
| `payment_token_ids`                         | Payment Tokens                                      | `one2many`   |     | ✅    | payment.token               |
| `peppol_eas`                                | Peppol e-address (EAS)                              | `selection`  |     | ✅    |                             |
| `peppol_endpoint`                           | Peppol Endpoint                                     | `char`       |     | ✅    |                             |
| `phone`                                     | Phone                                               | `char`       |     | ✅    |                             |
| `phone_blacklisted`                         | Blacklisted Phone is Phone                          | `boolean`    |     |       |                             |
| `phone_mobile_search`                       | Phone Number                                        | `char`       |     |       |                             |
| `phone_sanitized`                           | Sanitized Number                                    | `char`       |     | ✅    |                             |
| `phone_sanitized_blacklisted`               | Phone Blacklisted                                   | `boolean`    |     |       |                             |
| `picking_warn_msg`                          | Message for Stock Picking                           | `text`       |     | ✅    |                             |
| `properties`                                | Properties                                          | `properties` |     | ✅    |                             |
| `properties_base_definition_id`             | Properties Base Definition                          | `many2one`   |     |       | properties.base.definition  |
| `property_account_payable_id`               | Account Payable                                     | `many2one`   |     | ✅    | account.account             |
| `property_account_position_id`              | Fiscal Position                                     | `many2one`   |     | ✅    | account.fiscal.position     |
| `property_account_receivable_id`            | Account Receivable                                  | `many2one`   |     | ✅    | account.account             |
| `property_delivery_carrier_id`              | Delivery Method                                     | `many2one`   |     | ✅    | delivery.carrier            |
| `property_inbound_payment_method_line_id`   | Property Inbound Payment Method Line                | `many2one`   |     | ✅    | account.payment.method.line |
| `property_outbound_payment_method_line_id`  | Property Outbound Payment Method Line               | `many2one`   |     | ✅    | account.payment.method.line |
| `property_payment_term_id`                  | Customer Payment Terms                              | `many2one`   |     | ✅    | account.payment.term        |
| `property_product_pricelist`                | Pricelist                                           | `many2one`   |     |       | product.pricelist           |
| `property_purchase_currency_id`             | Supplier Currency                                   | `many2one`   |     | ✅    | res.currency                |
| `property_stock_customer`                   | Customer Location                                   | `many2one`   |     | ✅    | stock.location              |
| `property_stock_supplier`                   | Vendor Location                                     | `many2one`   |     | ✅    | stock.location              |
| `property_supplier_payment_term_id`         | Vendor Payment Terms                                | `many2one`   |     | ✅    | account.payment.term        |
| `purchase_line_ids`                         | Purchase Lines                                      | `one2many`   |     | ✅    | purchase.order.line         |
| `purchase_order_count`                      | Purchase Order Count                                | `integer`    |     |       |                             |
| `purchase_warn_msg`                         | Message for Purchase Order                          | `text`       |     | ✅    |                             |
| `rating_ids`                                | Ratings                                             | `one2many`   |     | ✅    | rating.rating               |
| `receipt_reminder_email`                    | Receipt Reminder                                    | `boolean`    |     | ✅    |                             |
| `ref`                                       | Reference                                           | `char`       |     | ✅    |                             |
| `ref_company_ids`                           | Companies that refers to partner                    | `one2many`   |     | ✅    | res.company                 |
| `reminder_date_before_receipt`              | Days Before Receipt                                 | `integer`    |     | ✅    |                             |
| `rtc_session_ids`                           | Rtc Session                                         | `one2many`   |     | ✅    | discuss.channel.rtc.session |
| `sale_order_count`                          | Sale Order Count                                    | `integer`    |     |       |                             |
| `sale_order_ids`                            | Sales Order                                         | `one2many`   |     | ✅    | sale.order                  |
| `sale_warn_msg`                             | Message for Sales Order                             | `text`       |     | ✅    |                             |
| `same_company_registry_partner_id`          | Partner with same Company Registry                  | `many2one`   |     |       | res.partner                 |
| `same_vat_partner_id`                       | Partner with same Tax ID                            | `many2one`   |     |       | res.partner                 |
| `self`                                      | Self                                                | `many2one`   |     |       | res.partner                 |
| `seo_name`                                  | Seo name                                            | `char`       |     | ✅    |                             |
| `show_credit_limit`                         | Show Credit Limit                                   | `boolean`    |     |       |                             |
| `signup_type`                               | Signup Token Type                                   | `char`       |     | ✅    |                             |
| `specific_property_product_pricelist`       | Specific Property Product Pricelist                 | `many2one`   |     | ✅    | product.pricelist           |
| `state_id`                                  | State                                               | `many2one`   |     | ✅    | res.country.state           |
| `static_map_url`                            | Static Map Url                                      | `char`       |     |       |                             |
| `static_map_url_is_valid`                   | Static Map Url Is Valid                             | `boolean`    |     |       |                             |
| `street`                                    | Street                                              | `char`       |     | ✅    |                             |
| `street2`                                   | Street2                                             | `char`       |     | ✅    |                             |
| `suggest_based_on`                          | Suggest Based On                                    | `char`       |     | ✅    |                             |
| `suggest_days`                              | Suggest Days                                        | `integer`    |     | ✅    |                             |
| `suggest_percent`                           | Suggest Percent                                     | `integer`    |     | ✅    |                             |
| `supplier_invoice_count`                    | # Vendor Bills                                      | `integer`    |     |       |                             |
| `supplier_rank`                             | Supplier Rank                                       | `integer`    |     | ✅    |                             |
| `ticket_count`                              | Ticket Count                                        | `integer`    |     |       |                             |
| `title`                                     | Title                                               | `many2one`   |     | ✅    | res.partner.title           |
| `total_invoiced`                            | Total Invoiced                                      | `monetary`   |     |       |                             |
| `trust`                                     | Degree of trust you have in this debtor             | `selection`  |     | ✅    |                             |
| `type`                                      | Address Type                                        | `selection`  |     | ✅    |                             |
| `type_address_label`                        | Address Type Description                            | `char`       |     |       |                             |
| `tz`                                        | Timezone                                            | `selection`  |     | ✅    |                             |
| `tz_offset`                                 | Timezone offset                                     | `char`       |     |       |                             |
| `use_partner_credit_limit`                  | Partner Limit                                       | `boolean`    |     |       |                             |
| `user_id`                                   | Salesperson                                         | `many2one`   |     | ✅    | res.users                   |
| `user_ids`                                  | Users                                               | `one2many`   |     | ✅    | res.users                   |
| `user_livechat_username`                    | User Livechat Username                              | `char`       |     |       |                             |
| `vat`                                       | Tax ID                                              | `char`       |     | ✅    |                             |
| `vat_label`                                 | Tax ID Label                                        | `char`       |     |       |                             |
| `visitor_ids`                               | Visitors                                            | `one2many`   |     | ✅    | website.visitor             |
| `website`                                   | Website Link                                        | `char`       |     | ✅    |                             |
| `website_absolute_url`                      | Website Absolute URL                                | `char`       |     |       |                             |
| `website_description`                       | Website Partner Full Description                    | `html`       |     | ✅    |                             |
| `website_id`                                | Website                                             | `many2one`   |     | ✅    | website                     |
| `website_message_ids`                       | Website Messages                                    | `one2many`   |     | ✅    | mail.message                |
| `website_meta_description`                  | Website meta description                            | `text`       |     | ✅    |                             |
| `website_meta_keywords`                     | Website meta keywords                               | `char`       |     | ✅    |                             |
| `website_meta_og_img`                       | Website opengraph image                             | `char`       |     | ✅    |                             |
| `website_meta_title`                        | Website meta title                                  | `char`       |     | ✅    |                             |
| `website_published`                         | Visible on current website                          | `boolean`    |     |       |                             |
| `website_short_description`                 | Website Partner Short Description                   | `text`       |     | ✅    |                             |
| `website_url`                               | Website URL                                         | `char`       |     |       |                             |
| `wishlist_ids`                              | Wishlist                                            | `one2many`   |     | ✅    | product.wishlist            |
| `write_date`                                | Last Updated on                                     | `datetime`   |     | ✅    |                             |
| `write_uid`                                 | Last Updated by                                     | `many2one`   |     | ✅    | res.users                   |
| `zip`                                       | Zip                                                 | `char`       |     | ✅    |                             |

**Access Rights:**

| Name                              | Group                                        | Perms     |
| --------------------------------- | -------------------------------------------- | --------- |
| res.partner.crm.user              | Sales / User: Own Documents Only             | `R/W/C`   |
| res.partner.sale.user             | Sales / User: Own Documents Only             | `R`       |
| res.partner.crm.manager           | Sales / Administrator                        | `R`       |
| res.partner.sale.manager          | Sales / Administrator                        | `R/W/C`   |
| res_partner group_account_manager | Accounting / Advisor                         | `R`       |
| res.partner purchase              | Purchase / User                              | `R`       |
| res.partner.purchase.manager      | Purchase / Administrator                     | `R/W/C`   |
| res.partner.user                  | Recruitment / Officer: Manage all applicants | `R/W/C/D` |
| name_op_res_partner_student       | OpenEduCat / Manager                         | `R/W/C/D` |
| name_op_res_partner_faculty       | OpenEduCat / User                            | `R/W/C`   |
| name_op_res_partner_library       | Library / Manager                            | `R`       |
| res_partner group_partner_manager | Contact / Creation                           | `R/W/C/D` |
| res_partner group_stock_manager   | Inventory / Administrator                    | `R/W/C`   |
| res_partner group_portal          | Role / Portal                                | `R`       |
| res_partner group_public          | Role / Public                                | `R`       |
| res_partner group_user            | Role / User                                  | `R`       |

**Record Rules:**

- **res.partner company** (Global) `R/W/C/D`
  - Domain:
    `['|', '|', ('partner_share', '=', False), ('company_id', 'parent_of', company_ids), ('company_id', '=', False)]`
- **res_partner: portal/public: read access on my commercial partner** (10, 11) `R`
  - Domain: `[('id', 'child_of', user.commercial_partner_id.id)]`

### 🗃️ `event.event` — Event

> 📧 Mail Thread

Event Model for Training and Placement.

**Fields:**

| Field                                | Label                                       | Type                    | Req | Store | Relation                |
| ------------------------------------ | ------------------------------------------- | ----------------------- | --- | ----- | ----------------------- |
| `active`                             | Active                                      | `boolean`               |     | ✅    |                         |
| `activity_calendar_event_id`         | Next Activity Calendar Event                | `many2one`              |     |       | calendar.event          |
| `activity_date_deadline`             | Next Activity Deadline                      | `date`                  |     |       |                         |
| `activity_exception_decoration`      | Activity Exception Decoration               | `selection`             |     |       |                         |
| `activity_exception_icon`            | Icon                                        | `char`                  |     |       |                         |
| `activity_ids`                       | Activities                                  | `one2many`              |     | ✅    | mail.activity           |
| `activity_state`                     | Activity State                              | `selection`             |     |       |                         |
| `activity_summary`                   | Next Activity Summary                       | `char`                  |     |       |                         |
| `activity_type_icon`                 | Activity Type Icon                          | `char`                  |     |       |                         |
| `activity_type_id`                   | Next Activity Type                          | `many2one`              |     |       | mail.activity.type      |
| `activity_user_id`                   | Responsible User                            | `many2one`              |     |       | res.users               |
| `address_id`                         | Venue                                       | `many2one`              |     | ✅    | res.partner             |
| `address_inline`                     | Venue (formatted for one line uses)         | `char`                  |     |       |                         |
| `address_name`                       | Name                                        | `char`                  |     |       |                         |
| `address_search`                     | Address                                     | `many2one`              |     |       | res.partner             |
| `alumni_event_id`                    | Alumni Group                                | `many2one`              |     | ✅    | op.alumni.group         |
| `badge_format`                       | Badge Dimension                             | `selection`             | ✅  | ✅    |                         |
| `badge_image`                        | Badge Background                            | `binary`                |     | ✅    |                         |
| `can_publish`                        | Can Publish                                 | `boolean`               |     |       |                         |
| `ceremony_id`                        | Convocation Ceremony                        | `many2one`              |     | ✅    | op.convocation.ceremony |
| `community_menu`                     | Community Menu                              | `boolean`               |     | ✅    |                         |
| `community_menu_ids`                 | Event Community Menus                       | `one2many`              |     | ✅    | website.event.menu      |
| `company_id`                         | Company                                     | `many2one`              |     | ✅    | res.company             |
| `country_id`                         | Country                                     | `many2one`              |     | ✅    | res.country             |
| `cover_properties`                   | Cover Properties                            | `text`                  |     | ✅    |                         |
| `create_date`                        | Created on                                  | `datetime`              |     | ✅    |                         |
| `create_uid`                         | Created by                                  | `many2one`              |     | ✅    | res.users               |
| `currency_id`                        | Currency                                    | `many2one`              |     |       | res.currency            |
| `date_begin`                         | Start Date                                  | `datetime`              | ✅  | ✅    |                         |
| `date_end`                           | End Date                                    | `datetime`              | ✅  | ✅    |                         |
| `date_tz`                            | Display Timezone                            | `selection`             | ✅  | ✅    |                         |
| `description`                        | Description                                 | `html`                  |     | ✅    |                         |
| `display_name`                       | Display Name                                | `char`                  |     |       |                         |
| `event_mail_ids`                     | Mail Schedule                               | `one2many`              |     | ✅    | event.mail              |
| `event_register_url`                 | Event Registration Link                     | `char`                  |     |       |                         |
| `event_registrations_open`           | Registration open                           | `boolean`               |     |       |                         |
| `event_registrations_sold_out`       | Sold Out                                    | `boolean`               |     |       |                         |
| `event_registrations_started`        | Registrations started                       | `boolean`               |     |       |                         |
| `event_share_url`                    | Event Share URL                             | `char`                  |     |       |                         |
| `event_slot_count`                   | Slots Count                                 | `integer`               |     |       |                         |
| `event_slot_ids`                     | Slots                                       | `one2many`              |     | ✅    | event.slot              |
| `event_ticket_ids`                   | Event Ticket                                | `one2many`              |     | ✅    | event.event.ticket      |
| `event_type_id`                      | Template                                    | `many2one`              |     | ✅    | event.type              |
| `event_url`                          | Online Event URL                            | `char`                  |     | ✅    |                         |
| `footer_visible`                     | Footer Visible                              | `boolean`               |     | ✅    |                         |
| `general_question_ids`               | General Questions                           | `many2many`             |     | ✅    | event.question          |
| `has_message`                        | Has Message                                 | `boolean`               |     |       |                         |
| `header_visible`                     | Header Visible                              | `boolean`               |     | ✅    |                         |
| `id`                                 | ID                                          | `integer`               |     | ✅    |                         |
| `introduction_menu`                  | Introduction Menu                           | `boolean`               |     | ✅    |                         |
| `introduction_menu_ids`              | Introduction Menus                          | `one2many`              |     | ✅    | website.event.menu      |
| `is_convocation`                     | Is Convocation                              | `boolean`               |     | ✅    |                         |
| `is_done`                            | Is Done                                     | `boolean`               |     |       |                         |
| `is_finished`                        | Is Finished                                 | `boolean`               |     |       |                         |
| `is_multi_slots`                     | Is Multi Slots                              | `boolean`               |     | ✅    |                         |
| `is_one_day`                         | Is One Day                                  | `boolean`               |     |       |                         |
| `is_ongoing`                         | Is Ongoing                                  | `boolean`               |     |       |                         |
| `is_participating`                   | Is Participating                            | `boolean`               |     |       |                         |
| `is_published`                       | Is Published                                | `boolean`               |     | ✅    |                         |
| `is_seo_optimized`                   | SEO optimized                               | `boolean`               |     | ✅    |                         |
| `is_visible_on_website`              | Visible On Website                          | `boolean`               |     |       |                         |
| `kanban_state`                       | Kanban State                                | `selection`             |     | ✅    |                         |
| `lang`                               | Language                                    | `selection`             |     | ✅    |                         |
| `lead_count`                         | # Leads                                     | `integer`               |     |       |                         |
| `lead_ids`                           | Leads                                       | `one2many`              |     | ✅    | crm.lead                |
| `menu_id`                            | Event Menu                                  | `many2one`              |     | ✅    | website.menu            |
| `message_attachment_count`           | Attachment Count                            | `integer`               |     |       |                         |
| `message_follower_ids`               | Followers                                   | `one2many`              |     | ✅    | mail.followers          |
| `message_has_error`                  | Message Delivery error                      | `boolean`               |     |       |                         |
| `message_has_error_counter`          | Number of errors                            | `integer`               |     |       |                         |
| `message_has_sms_error`              | SMS Delivery error                          | `boolean`               |     |       |                         |
| `message_ids`                        | Messages                                    | `one2many`              |     | ✅    | mail.message            |
| `message_is_follower`                | Is Follower                                 | `boolean`               |     |       |                         |
| `message_needaction`                 | Action Needed                               | `boolean`               |     |       |                         |
| `message_needaction_counter`         | Number of Actions                           | `integer`               |     |       |                         |
| `message_partner_ids`                | Followers (Partners)                        | `many2many`             |     |       | res.partner             |
| `my_activity_date_deadline`          | My Activity Deadline                        | `date`                  |     |       |                         |
| `name`                               | Event                                       | `char`                  | ✅  | ✅    |                         |
| `note`                               | Note                                        | `html`                  |     | ✅    |                         |
| `organizer_id`                       | Organizer                                   | `many2one`              |     | ✅    | res.partner             |
| `other_menu_ids`                     | Other Menus                                 | `one2many`              |     | ✅    | website.event.menu      |
| `question_ids`                       | Questions                                   | `many2many`             |     | ✅    | event.question          |
| `rating_ids`                         | Ratings                                     | `one2many`              |     | ✅    | rating.rating           |
| `register_menu`                      | Register Menu                               | `boolean`               |     | ✅    |                         |
| `register_menu_ids`                  | Register Menus                              | `one2many`              |     | ✅    | website.event.menu      |
| `registration_ids`                   | Attendees                                   | `one2many`              |     | ✅    | event.registration      |
| `registration_properties_definition` | Registration Properties                     | `properties_definition` |     | ✅    |                         |
| `sale_order_lines_ids`               | All sale order lines pointing to this event | `one2many`              |     | ✅    | sale.order.line         |
| `sale_price_total`                   | Sales (Tax Included)                        | `monetary`              |     |       |                         |
| `seats_available`                    | Available Seats                             | `integer`               |     |       |                         |
| `seats_limited`                      | Limit Attendees                             | `boolean`               | ✅  | ✅    |                         |
| `seats_max`                          | Maximum Attendees                           | `integer`               |     | ✅    |                         |
| `seats_reserved`                     | Number of Registrations                     | `integer`               |     |       |                         |
| `seats_taken`                        | Number of Taken Seats                       | `integer`               |     |       |                         |
| `seats_used`                         | Number of Attendees                         | `integer`               |     |       |                         |
| `seo_name`                           | Seo name                                    | `char`                  |     | ✅    |                         |
| `specific_question_ids`              | Specific Questions                          | `many2many`             |     | ✅    | event.question          |
| `stage_id`                           | Stage                                       | `many2one`              |     | ✅    | event.stage             |
| `start_remaining`                    | Remaining before start                      | `integer`               |     |       |                         |
| `start_sale_datetime`                | Start sale date                             | `datetime`              |     |       |                         |
| `start_today`                        | Start Today                                 | `boolean`               |     |       |                         |
| `subtitle`                           | Event Subtitle                              | `char`                  |     | ✅    |                         |
| `tag_ids`                            | Tags                                        | `many2many`             |     | ✅    | event.tag               |
| `ticket_instructions`                | Ticket Instructions                         | `html`                  |     | ✅    |                         |
| `training_event`                     | Training Event                              | `boolean`               |     | ✅    |                         |
| `use_barcode`                        | Use Barcode                                 | `boolean`               |     |       |                         |
| `user_id`                            | Responsible                                 | `many2one`              |     | ✅    | res.users               |
| `website_absolute_url`               | Website Absolute URL                        | `char`                  |     |       |                         |
| `website_id`                         | Website                                     | `many2one`              |     | ✅    | website                 |
| `website_menu`                       | Website Menu                                | `boolean`               |     | ✅    |                         |
| `website_message_ids`                | Website Messages                            | `one2many`              |     | ✅    | mail.message            |
| `website_meta_description`           | Website meta description                    | `text`                  |     | ✅    |                         |
| `website_meta_keywords`              | Website meta keywords                       | `char`                  |     | ✅    |                         |
| `website_meta_og_img`                | Website opengraph image                     | `char`                  |     | ✅    |                         |
| `website_meta_title`                 | Website meta title                          | `char`                  |     | ✅    |                         |
| `website_published`                  | Visible on current website                  | `boolean`               |     |       |                         |
| `website_url`                        | Website URL                                 | `char`                  |     |       |                         |
| `website_visibility`                 | Website Visibility                          | `selection`             | ✅  | ✅    |                         |
| `write_date`                         | Last Updated on                             | `datetime`              |     | ✅    |                         |
| `write_uid`                          | Last Updated by                             | `many2one`              |     | ✅    | res.users               |

**Access Rights:**

| Name                     | Group                      | Perms     |
| ------------------------ | -------------------------- | --------- |
| event.event.registration | Events / Registration Desk | `R`       |
| event.event.user         | Events / User              | `R/W/C`   |
| event.event.manager      | Events / Administrator     | `R/W/C/D` |
| event.event              | Role / Portal              | `R`       |
| event.event              | Role / Public              | `R`       |
| event.event              | Role / User                | `R`       |

**Record Rules:**

- **Event: multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Event: public/portal: published read** (10, 11) `R`
  - Domain: `[('website_published', '=', True)]`

### 🗃️ `op.job.applicant` — Job Applicant

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                 |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------ |
| `active`                        | Active                        | `boolean`   |     | ✅    |                          |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event           |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                          |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                          |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                          |
| `activity_id`                   | Job Opportunity               | `many2one`  |     | ✅    | op.activity.announcement |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity            |
| `activity_state`                | Activity State                | `selection` |     |       |                          |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                          |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                          |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type       |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users                |
| `attachment_ids`                | Attachments                   | `one2many`  |     | ✅    | ir.attachment            |
| `attachment_number`             | Number of Attachments         | `integer`   |     |       |                          |
| `availability`                  | Availability                  | `date`      |     | ✅    |                          |
| `can_publish`                   | Can Publish                   | `boolean`   |     |       |                          |
| `color`                         | Color Index                   | `integer`   |     | ✅    |                          |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company              |
| `cover_letter`                  | Cover Letter                  | `text`      |     | ✅    |                          |
| `create_date`                   | Creation Date                 | `datetime`  |     | ✅    |                          |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users                |
| `currency_id`                   | Currency                      | `many2one`  |     |       | res.currency             |
| `date`                          | Date                          | `date`      |     | ✅    |                          |
| `date_closed`                   | Closed                        | `datetime`  |     | ✅    |                          |
| `date_last_stage_update`        | Last Stage Update             | `datetime`  |     | ✅    |                          |
| `date_open`                     | Assigned                      | `datetime`  |     | ✅    |                          |
| `day_close`                     | Days to Close                 | `float`     |     |       |                          |
| `day_open`                      | Days to Open                  | `float`     |     |       |                          |
| `display_name`                  | Display Name                  | `char`      |     |       |                          |
| `final_score`                   | Final Score                   | `float`     |     |       |                          |
| `gd_score`                      | Group Discussion              | `float`     |     | ✅    |                          |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                          |
| `id`                            | ID                            | `integer`   |     | ✅    |                          |
| `interview_score`               | Interview Score               | `float`     |     | ✅    |                          |
| `is_offer`                      | Is offer                      | `boolean`   |     | ✅    |                          |
| `is_published`                  | Is Published                  | `boolean`   |     | ✅    |                          |
| `is_seo_optimized`              | SEO optimized                 | `boolean`   |     | ✅    |                          |
| `join_date`                     | Joining Date                  | `date`      |     | ✅    |                          |
| `kanban_state`                  | Kanban State                  | `selection` | ✅  | ✅    |                          |
| `last_stage_id`                 | Last Stage                    | `many2one`  |     | ✅    | job.post.stage           |
| `legend_blocked`                | Kanban Blocked                | `char`      |     |       |                          |
| `legend_done`                   | Kanban Valid                  | `char`      |     |       |                          |
| `legend_normal`                 | Kanban Ongoing                | `char`      |     |       |                          |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                          |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers           |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                          |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                          |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                          |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message             |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                          |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                          |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                          |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner              |
| `mobile`                        | Phone                         | `char`      |     |       |                          |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                          |
| `name`                          | Application Number            | `char`      | ✅  | ✅    |                          |
| `notes`                         | Notes                         | `text`      |     | ✅    |                          |
| `offer_package`                 | Offer Package                 | `monetary`  |     | ✅    |                          |
| `post_id`                       | Job Post                      | `many2one`  |     | ✅    | op.job.post              |
| `priority`                      | Appreciation                  | `selection` |     | ✅    |                          |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating            |
| `salary_expected`               | Expected Salary               | `monetary`  |     | ✅    |                          |
| `salary_proposed`               | Proposed Salary               | `monetary`  |     | ✅    |                          |
| `seo_name`                      | Seo name                      | `char`      |     | ✅    |                          |
| `stage_id`                      | Stage                         | `many2one`  |     | ✅    | job.post.stage           |
| `state`                         | State                         | `selection` |     | ✅    |                          |
| `training_period`               | Training Period               | `char`      |     | ✅    |                          |
| `training_type`                 | Training Type                 | `selection` |     | ✅    |                          |
| `user_id`                       | Name                          | `many2one`  |     | ✅    | op.student               |
| `website_absolute_url`          | Website Absolute URL          | `char`      |     |       |                          |
| `website_id`                    | Website                       | `many2one`  |     | ✅    | website                  |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message             |
| `website_meta_description`      | Website meta description      | `text`      |     | ✅    |                          |
| `website_meta_keywords`         | Website meta keywords         | `char`      |     | ✅    |                          |
| `website_meta_og_img`           | Website opengraph image       | `char`      |     | ✅    |                          |
| `website_meta_title`            | Website meta title            | `char`      |     | ✅    |                          |
| `website_published`             | Visible on current website    | `boolean`   |     |       |                          |
| `website_url`                   | Website URL                   | `char`      |     |       |                          |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                          |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users                |
| `written_score`                 | Written Test Score            | `float`     |     | ✅    |                          |

**Access Rights:**

| Name                            | Group                | Perms     |
| ------------------------------- | -------------------- | --------- |
| access_op_job_applicant_manager | OpenEduCat / Manager | `R/W/C/D` |
| access_op_job_applicant_user    | OpenEduCat / User    | `R/W`     |

**Record Rules:**

- **Job Applicant multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `training.season` — Training Season

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                 |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------ |
| `active`                        | Active                        | `boolean`   |     | ✅    |                          |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event           |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                          |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                          |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                          |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity            |
| `activity_state`                | Activity State                | `selection` |     |       |                          |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                          |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                          |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type       |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users                |
| `application_count`             | Applications                  | `integer`   |     |       |                          |
| `avg_attendance`                | Average Attendance %          | `float`     |     |       |                          |
| `code`                          | Code                          | `char`      |     | ✅    |                          |
| `company_fee_applicable`        | Fee Applicable for Company    | `boolean`   |     | ✅    |                          |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                          |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users                |
| `display_name`                  | Display Name                  | `char`      |     |       |                          |
| `end_date`                      | End Date                      | `date`      | ✅  | ✅    |                          |
| `group_discussion`              | Group Discussions             | `boolean`   |     | ✅    |                          |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                          |
| `id`                            | ID                            | `integer`   |     | ✅    |                          |
| `internship`                    | Internship Program            | `boolean`   |     | ✅    |                          |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                          |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers           |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                          |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                          |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                          |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message             |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                          |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                          |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                          |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner              |
| `mock_interview`                | Mock Interviews               | `boolean`   |     | ✅    |                          |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                          |
| `name`                          | Session Name                  | `char`      | ✅  | ✅    |                          |
| `opportunity_ids`               | Job Opportunities             | `one2many`  |     | ✅    | op.activity.announcement |
| `partner_companies_ids`         | Partner Companies             | `many2many` |     | ✅    | res.partner              |
| `personality_dev`               | Personality Development       | `boolean`   |     | ✅    |                          |
| `placement_impact`              | Placement Impact %            | `float`     |     |       |                          |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating            |
| `resume_workshop`               | Resume Writing Workshop       | `boolean`   |     | ✅    |                          |
| `session_count`                 | Number of Training Sessions   | `integer`   |     |       |                          |
| `start_date`                    | Start Date                    | `date`      | ✅  | ✅    |                          |
| `state`                         | Status                        | `selection` |     | ✅    |                          |
| `student_fee_applicable`        | Fee Applicable for Student    | `boolean`   |     | ✅    |                          |
| `technical_skills`              | Technical Skills              | `boolean`   |     | ✅    |                          |
| `total_participants`            | Total Participants            | `integer`   |     |       |                          |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message             |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                          |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                                              | Group                | Perms     |
| ------------------------------------------------- | -------------------- | --------- |
| access_training_season_group_op_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_training_season_group_op_faculty           | OpenEduCat / User    | `R/W`     |

### 🗃️ `placement.officer.create.wizard` — Placement Officer Wizard

> ✳️ Transient (Wizard)

    Wizard to create Placement Officer from Job Applicant.

**Fields:**

| Field                | Label           | Type        | Req | Store | Relation         |
| -------------------- | --------------- | ----------- | --- | ----- | ---------------- |
| `applicant_id`       | Applicant       | `many2one`  | ✅  | ✅    | op.job.applicant |
| `company_id`         | Company         | `many2one`  |     | ✅    | res.company      |
| `create_date`        | Created on      | `datetime`  |     | ✅    |                  |
| `create_uid`         | Created by      | `many2one`  |     | ✅    | res.users        |
| `currency_id`        | Currency        | `many2one`  |     |       | res.currency     |
| `display_name`       | Display Name    | `char`      |     |       |                  |
| `id`                 | ID              | `integer`   |     | ✅    |                  |
| `join_date`          | Joining Date    | `date`      | ✅  | ✅    |                  |
| `offer_package`      | Offer Package   | `monetary`  |     | ✅    |                  |
| `partner_company_id` | Partner Company | `many2one`  | ✅  | ✅    | res.partner      |
| `student_id`         | Student         | `many2one`  | ✅  | ✅    | res.partner      |
| `training_period`    | Training Period | `float`     | ✅  | ✅    |                  |
| `training_type`      | Training Type   | `selection` |     | ✅    |                  |
| `write_date`         | Last Updated on | `datetime`  |     | ✅    |                  |
| `write_uid`          | Last Updated by | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                                                              | Group                | Perms     |
| ----------------------------------------------------------------- | -------------------- | --------- |
| access_placement_officer_create_wizard_group_op_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_placement_officer_create_wizard_group_op_faculty           | OpenEduCat / User    | `R/W`     |
