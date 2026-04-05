---
title: "Calendar"
module: "calendar"
state: "installed"
version: "19.0.1.1"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Calendar"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/________, odoo/app]
---

# 🟢 Calendar

> **Module:** `calendar` | **Version:** `19.0.1.1` **Category:** Calendar | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[base]] [[mail]]

## 📖 Description

# This is a full-featured calendar system.

## It supports:

> - Calendar of events
> - Recurring events

If you need to manage your meetings, you should install the CRM module.

## 🖥️ UI Components

### Menus

- `Calendar`
- `Calendar/Calendar`
- `Calendar/Configuration`
- `Calendar/Configuration/Reminders`
- `Calendar/Configuration/Settings`
- `Settings/Technical/Calendar`
- `Settings/Technical/Calendar/Calendar Alarm`
- `Settings/Technical/Calendar/Meeting Types`

### Views

- `* INHERIT mail.activity.form.inherit.calendar (form)`
- `* INHERIT mail.activity.schedule.inherit.calendar (form)`
- `* INHERIT res.config.settings.view.form.inherit.calendar (form)`
- `* INHERIT res.users.form.calendar (form)`
- `* INHERIT res.users.preferences.form.inherit (form)`
- `* INHERIT res.users.view.form.inherit.calendar (form)`
- `* INHERIT res_partner.view.form.calendar (form)`
- `Calendar Invitation Page for anonymous users (qweb)`
- `calendar.alarm.form (form)`
- `calendar.alarm.list (list)`
- `calendar.event.calendar (calendar)`
- `calendar.event.form (form)`
- `calendar.event.form.quick_create (form)`
- `calendar.event.list (list)`
- `calendar.event.search (search)`
- `calendar.event.type (list)`
- `calendar.popover.delete.wizard.form (form)`
- `calendar.popover.delete.wizard.view.form (form)`
- `calendar.provider.config.view.form (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**18 model(s) defined by this module:**

### 🗃️ `calendar.event` — Calendar Event

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                             | Label                        | Type                 | Req | Store | Relation                      |
| --------------------------------- | ---------------------------- | -------------------- | --- | ----- | ----------------------------- |
| `academic_calendar`               | Academic Calendar?           | `boolean`            |     | ✅    |                               |
| `accepted_count`                  | Accepted Count               | `integer`            |     |       |                               |
| `access_token`                    | Invitation Token             | `char`               |     | ✅    |                               |
| `active`                          | Active                       | `boolean`            |     | ✅    |                               |
| `activity_ids`                    | Activities                   | `one2many`           |     | ✅    | mail.activity                 |
| `alarm_ids`                       | Reminders                    | `many2many`          |     | ✅    | calendar.alarm                |
| `allday`                          | All Day                      | `boolean`            |     | ✅    |                               |
| `applicant_id`                    | Applicant                    | `many2one`           |     | ✅    | hr.applicant                  |
| `appointment_id`                  | Online Appointment           | `many2one`           |     | ✅    | calendar.online.appointment   |
| `attendee_ids`                    | Participant                  | `one2many`           |     | ✅    | calendar.attendee             |
| `attendees_count`                 | Attendees Count              | `integer`            |     |       |                               |
| `automatic_email`                 | Automatic Email              | `boolean`            |     | ✅    |                               |
| `awaiting_count`                  | Awaiting Count               | `integer`            |     |       |                               |
| `batch_ids`                       | Batches                      | `many2many`          |     | ✅    | op.batch                      |
| `booking_status`                  | Booking Status               | `selection`          |     | ✅    |                               |
| `byday`                           | By day                       | `selection`          |     |       |                               |
| `categ_ids`                       | Tags                         | `many2many`          |     | ✅    | calendar.event.type           |
| `count`                           | Number of Repetitions        | `integer`            |     |       |                               |
| `course_ids`                      | Courses                      | `many2many`          |     | ✅    | op.course                     |
| `create_date`                     | Created on                   | `datetime`           |     | ✅    |                               |
| `create_uid`                      | Created by                   | `many2one`           |     | ✅    | res.users                     |
| `current_attendee`                | Current Attendee             | `many2one`           |     |       | calendar.attendee             |
| `current_status`                  | Attending?                   | `selection`          |     |       |                               |
| `day`                             | Date of month                | `integer`            |     |       |                               |
| `declined_count`                  | Declined Count               | `integer`            |     |       |                               |
| `description`                     | Description                  | `html`               |     | ✅    |                               |
| `display_description`             | Display Description          | `boolean`            |     |       |                               |
| `display_name`                    | Display Name                 | `char`               |     |       |                               |
| `display_time`                    | Event Time                   | `char`               |     |       |                               |
| `duration`                        | Duration                     | `float`              |     | ✅    |                               |
| `effective_privacy`               | Effective Privacy            | `selection`          |     |       |                               |
| `end_type`                        | Recurrence Termination       | `selection`          |     |       |                               |
| `event_tz`                        | Timezone                     | `selection`          |     |       |                               |
| `follow_recurrence`               | Follow Recurrence            | `boolean`            |     | ✅    |                               |
| `fri`                             | Fri                          | `boolean`            |     |       |                               |
| `has_message`                     | Has Message                  | `boolean`            |     |       |                               |
| `id`                              | ID                           | `integer`            |     | ✅    |                               |
| `interval`                        | Repeat On                    | `integer`            |     |       |                               |
| `invalid_email_partner_ids`       | Invalid Email Partner        | `many2many`          |     |       | res.partner                   |
| `is_highlighted`                  | Is the Event Highlighted     | `boolean`            |     |       |                               |
| `is_organizer_alone`              | Is the Organizer Alone       | `boolean`            |     |       |                               |
| `location`                        | Location                     | `char`               |     | ✅    |                               |
| `meeting_url`                     | URL                          | `char`               |     | ✅    |                               |
| `meet_url`                        | Google Meet URL              | `char`               |     | ✅    |                               |
| `message_attachment_count`        | Attachment Count             | `integer`            |     |       |                               |
| `message_follower_ids`            | Followers                    | `one2many`           |     | ✅    | mail.followers                |
| `message_has_error`               | Message Delivery error       | `boolean`            |     |       |                               |
| `message_has_error_counter`       | Number of errors             | `integer`            |     |       |                               |
| `message_has_sms_error`           | SMS Delivery error           | `boolean`            |     |       |                               |
| `message_ids`                     | Messages                     | `one2many`           |     | ✅    | mail.message                  |
| `message_is_follower`             | Is Follower                  | `boolean`            |     |       |                               |
| `message_needaction`              | Action Needed                | `boolean`            |     |       |                               |
| `message_needaction_counter`      | Number of Actions            | `integer`            |     |       |                               |
| `message_partner_ids`             | Followers (Partners)         | `many2many`          |     |       | res.partner                   |
| `mon`                             | Mon                          | `boolean`            |     |       |                               |
| `month_by`                        | Option                       | `selection`          |     |       |                               |
| `mpw`                             | Moderator Password           | `char`               |     | ✅    |                               |
| `name`                            | Meeting Subject              | `char`               | ✅  | ✅    |                               |
| `notes`                           | Notes                        | `html`               |     | ✅    |                               |
| `online_appointment_resource_ids` | Online Appointment Resources | `many2one`           |     | ✅    | calendar.appointment.resource |
| `online_meeting`                  | Online Meeting               | `boolean`            |     | ✅    |                               |
| `opportunity_id`                  | Crm Opportunity              | `many2one`           |     | ✅    | crm.lead                      |
| `op_session_id`                   | Session                      | `many2one`           |     | ✅    | op.session                    |
| `partner_id`                      | Scheduled by                 | `many2one`           |     |       | res.partner                   |
| `partner_ids`                     | Attendees                    | `many2many`          |     | ✅    | res.partner                   |
| `privacy`                         | Privacy                      | `selection`          |     | ✅    |                               |
| `rating_ids`                      | Ratings                      | `one2many`           |     | ✅    | rating.rating                 |
| `recurrence_id`                   | Recurrence Rule              | `many2one`           |     | ✅    | calendar.recurrence           |
| `recurrence_update`               | Recurrence Update            | `selection`          |     |       |                               |
| `recurrency`                      | Recurrent                    | `boolean`            |     | ✅    |                               |
| `res_id`                          | Document ID                  | `many2one_reference` |     | ✅    |                               |
| `res_model`                       | Document Model Name          | `char`               |     | ✅    |                               |
| `res_model_id`                    | Document Model               | `many2one`           |     | ✅    | ir.model                      |
| `res_model_name`                  | Model Description            | `char`               |     |       |                               |
| `rrule`                           | Recurrent Rule               | `char`               |     |       |                               |
| `rrule_type`                      | Recurrence                   | `selection`          |     |       |                               |
| `rrule_type_ui`                   | Repeat                       | `selection`          |     |       |                               |
| `sat`                             | Sat                          | `boolean`            |     |       |                               |
| `should_show_status`              | Should Show Status           | `boolean`            |     |       |                               |
| `show_as`                         | Show as                      | `selection`          | ✅  | ✅    |                               |
| `start`                           | Start                        | `datetime`           | ✅  | ✅    |                               |
| `start_date`                      | Start Date                   | `date`               |     | ✅    |                               |
| `stop`                            | Stop                         | `datetime`           | ✅  | ✅    |                               |
| `stop_date`                       | End Date                     | `date`               |     | ✅    |                               |
| `sun`                             | Sun                          | `boolean`            |     |       |                               |
| `tentative_count`                 | Tentative Count              | `integer`            |     |       |                               |
| `thu`                             | Thu                          | `boolean`            |     |       |                               |
| `tue`                             | Tue                          | `boolean`            |     |       |                               |
| `unavailable_partner_ids`         | Unavailable Attendees        | `many2many`          |     |       | res.partner                   |
| `until`                           | Until                        | `date`               |     |       |                               |
| `user_can_edit`                   | User Can Edit                | `boolean`            |     |       |                               |
| `user_id`                         | Organizer                    | `many2one`           |     | ✅    | res.users                     |
| `videocall_channel_id`            | Discuss Channel              | `many2one`           |     | ✅    | discuss.channel               |
| `videocall_location`              | Meeting URL                  | `char`               |     | ✅    |                               |
| `videocall_source`                | Videocall Source             | `selection`          |     |       |                               |
| `website_message_ids`             | Website Messages             | `one2many`           |     | ✅    | mail.message                  |
| `wed`                             | Wed                          | `boolean`            |     |       |                               |
| `weekday`                         | Weekday                      | `selection`          |     |       |                               |
| `write_date`                      | Last Updated on              | `datetime`           |     | ✅    |                               |
| `write_uid`                       | Last Updated by              | `many2one`           |     | ✅    | res.users                     |

**Access Rights:**

| Name                           | Group                                        | Perms     |
| ------------------------------ | -------------------------------------------- | --------- |
| calendar.event                 | Sales / User: Own Documents Only             | `R/W/C`   |
| calendar.event.manager         | Sales / Administrator                        | `R/W/C/D` |
| calendar.event.hr.user         | Time Off / Officer: Manage all requests      | `R/W/C/D` |
| calendar.event.hruser          | Recruitment / Officer: Manage all applicants | `R/W/C/D` |
| calendar.event.partner.manager | Contact / Creation                           | `R/W/C/D` |
| calendar.event_all_user        | Role / Portal                                | `R`       |
| calendar.event_all_employee    | Role / User                                  | `R/W/C/D` |

**Record Rules:**

- **Own events** (10) `R/W/C/D`
  - Domain: `[('partner_ids', 'in', user.partner_id.id)]`
- **All Calendar Event for employees** (1) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Private events** (Global) `W/C/D`
  - Domain:
    `['|', ('privacy', '!=', 'private'), '&', ('privacy', '=', 'private'), '|', ('user_id', '=', user.id), ('partner_ids', 'in', user.partner_id.id)]`

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

### 🗃️ `discuss.channel` — Discussion Channel

> 📧 Mail Thread

Chat Session Reprensenting a conversation between users. It extends the base method for
anonymous usage.

**Fields:**

| Field                                    | Label                                                                                       | Type        | Req | Store | Relation                           |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- | ----------- | --- | ----- | ---------------------------------- |
| `active`                                 | Active                                                                                      | `boolean`   |     | ✅    |                                    |
| `avatar_128`                             | Avatar                                                                                      | `binary`    |     |       |                                    |
| `avatar_cache_key`                       | Avatar Cache Key                                                                            | `char`      |     |       |                                    |
| `calendar_event_ids`                     | Calendar Event                                                                              | `one2many`  |     | ✅    | calendar.event                     |
| `call_history_ids`                       | Call History                                                                                | `one2many`  |     | ✅    | discuss.call.history               |
| `channel_member_ids`                     | Members                                                                                     | `one2many`  |     | ✅    | discuss.channel.member             |
| `channel_name_member_ids`                | Channel Name Member                                                                         | `one2many`  |     |       | discuss.channel.member             |
| `channel_partner_ids`                    | Partners                                                                                    | `many2many` |     |       | res.partner                        |
| `channel_type`                           | Channel Type                                                                                | `selection` | ✅  | ✅    |                                    |
| `chatbot_current_step_id`                | Chatbot Current Step                                                                        | `many2one`  |     | ✅    | chatbot.script.step                |
| `chatbot_message_ids`                    | Chatbot Messages                                                                            | `one2many`  |     | ✅    | chatbot.message                    |
| `country_id`                             | Country                                                                                     | `many2one`  |     | ✅    | res.country                        |
| `create_date`                            | Created on                                                                                  | `datetime`  |     | ✅    |                                    |
| `create_uid`                             | Created by                                                                                  | `many2one`  |     | ✅    | res.users                          |
| `default_display_mode`                   | Default Display Mode                                                                        | `selection` |     | ✅    |                                    |
| `description`                            | Description                                                                                 | `text`      |     | ✅    |                                    |
| `display_name`                           | Display Name                                                                                | `char`      |     |       |                                    |
| `duration`                               | Duration                                                                                    | `float`     |     |       |                                    |
| `faculty_id`                             | Faculty                                                                                     | `many2one`  |     | ✅    | op.faculty                         |
| `from_message_id`                        | From Message                                                                                | `many2one`  |     | ✅    | mail.message                       |
| `group_ids`                              | Auto Subscription                                                                           | `many2many` |     | ✅    | res.groups                         |
| `group_public_id`                        | Authorized Group                                                                            | `many2one`  |     | ✅    | res.groups                         |
| `has_crm_lead`                           | Has Crm Lead                                                                                | `boolean`   |     | ✅    |                                    |
| `has_message`                            | Has Message                                                                                 | `boolean`   |     |       |                                    |
| `id`                                     | ID                                                                                          | `integer`   |     | ✅    |                                    |
| `image_128`                              | Image                                                                                       | `binary`    |     | ✅    |                                    |
| `invitation_url`                         | Invitation URL                                                                              | `char`      |     |       |                                    |
| `invited_member_ids`                     | Invited Member                                                                              | `one2many`  |     |       | discuss.channel.member             |
| `is_created_student`                     | Is Created Student                                                                          | `boolean`   |     | ✅    |                                    |
| `is_editable`                            | Is Editable                                                                                 | `boolean`   |     |       |                                    |
| `is_member`                              | Is Member                                                                                   | `boolean`   |     |       |                                    |
| `is_pending_chat_request`                | When created from an operator, whether the channel is yet to be opened on the visitor side. | `boolean`   |     | ✅    |                                    |
| `last_interest_dt`                       | Last Interest                                                                               | `datetime`  |     | ✅    |                                    |
| `lead_ids`                               | Leads                                                                                       | `one2many`  |     | ✅    | crm.lead                           |
| `livechat_agent_history_ids`             | Agents (History)                                                                            | `one2many`  |     |       | im_livechat.channel.member.history |
| `livechat_agent_partner_ids`             | Agents                                                                                      | `many2many` |     | ✅    | res.partner                        |
| `livechat_agent_providing_help_history`  | Help Provided (Agent)                                                                       | `many2one`  |     | ✅    | im_livechat.channel.member.history |
| `livechat_agent_requesting_help_history` | Help Requested (Agent)                                                                      | `many2one`  |     | ✅    | im_livechat.channel.member.history |
| `livechat_bot_history_ids`               | Bots (History)                                                                              | `one2many`  |     |       | im_livechat.channel.member.history |
| `livechat_bot_partner_ids`               | Bots                                                                                        | `many2many` |     | ✅    | res.partner                        |
| `livechat_channel_id`                    | Channel                                                                                     | `many2one`  |     | ✅    | im_livechat.channel                |
| `livechat_channel_member_history_ids`    | Livechat Channel Member History                                                             | `one2many`  |     | ✅    | im_livechat.channel.member.history |
| `livechat_conversation_tag_ids`          | Live Chat Conversation Tags                                                                 | `many2many` |     | ✅    | im_livechat.conversation.tag       |
| `livechat_customer_guest_ids`            | Customers (Guests)                                                                          | `many2many` |     |       | mail.guest                         |
| `livechat_customer_history_ids`          | Customers (History)                                                                         | `one2many`  |     |       | im_livechat.channel.member.history |
| `livechat_customer_partner_ids`          | Customers (Partners)                                                                        | `many2many` |     | ✅    | res.partner                        |
| `livechat_end_dt`                        | Session end date                                                                            | `datetime`  |     | ✅    |                                    |
| `livechat_expertise_ids`                 | Livechat Expertise                                                                          | `many2many` |     | ✅    | im_livechat.expertise              |
| `livechat_failure`                       | Live Chat Session Failure                                                                   | `selection` |     | ✅    |                                    |
| `livechat_is_escalated`                  | Is session escalated                                                                        | `boolean`   |     | ✅    |                                    |
| `livechat_lang_id`                       | Language                                                                                    | `many2one`  |     | ✅    | res.lang                           |
| `livechat_matches_self_expertise`        | Livechat Matches Self Expertise                                                             | `boolean`   |     |       |                                    |
| `livechat_matches_self_lang`             | Livechat Matches Self Lang                                                                  | `boolean`   |     |       |                                    |
| `livechat_note`                          | Live Chat Note                                                                              | `html`      |     | ✅    |                                    |
| `livechat_operator_id`                   | Operator                                                                                    | `many2one`  |     | ✅    | res.partner                        |
| `livechat_outcome`                       | Livechat Outcome                                                                            | `selection` |     | ✅    |                                    |
| `livechat_start_hour`                    | Session Start Hour                                                                          | `float`     |     | ✅    |                                    |
| `livechat_state`                         | Livechat State                                                                              | `selection` |     | ✅    |                                    |
| `livechat_status`                        | Livechat Status                                                                             | `selection` |     | ✅    |                                    |
| `livechat_visitor_id`                    | Visitor                                                                                     | `many2one`  |     | ✅    | website.visitor                    |
| `livechat_week_day`                      | Day of the Week                                                                             | `selection` |     | ✅    |                                    |
| `member_count`                           | Member Count                                                                                | `integer`   |     |       |                                    |
| `message_attachment_count`               | Attachment Count                                                                            | `integer`   |     |       |                                    |
| `message_count`                          | # Messages                                                                                  | `integer`   |     |       |                                    |
| `message_follower_ids`                   | Followers                                                                                   | `one2many`  |     | ✅    | mail.followers                     |
| `message_has_error`                      | Message Delivery error                                                                      | `boolean`   |     |       |                                    |
| `message_has_error_counter`              | Number of errors                                                                            | `integer`   |     |       |                                    |
| `message_has_sms_error`                  | SMS Delivery error                                                                          | `boolean`   |     |       |                                    |
| `message_ids`                            | Messages                                                                                    | `one2many`  |     | ✅    | mail.message                       |
| `message_is_follower`                    | Is Follower                                                                                 | `boolean`   |     |       |                                    |
| `message_needaction`                     | Action Needed                                                                               | `boolean`   |     |       |                                    |
| `message_needaction_counter`             | Number of Actions                                                                           | `integer`   |     |       |                                    |
| `message_partner_ids`                    | Followers (Partners)                                                                        | `many2many` |     |       | res.partner                        |
| `name`                                   | Name                                                                                        | `char`      | ✅  | ✅    |                                    |
| `parent_channel_id`                      | Parent Channel                                                                              | `many2one`  |     | ✅    | discuss.channel                    |
| `pinned_message_ids`                     | Pinned Messages                                                                             | `one2many`  |     | ✅    | mail.message                       |
| `rating_avg`                             | Average Rating                                                                              | `float`     |     |       |                                    |
| `rating_avg_text`                        | Rating Avg Text                                                                             | `selection` |     |       |                                    |
| `rating_count`                           | Rating count                                                                                | `integer`   |     |       |                                    |
| `rating_ids`                             | Ratings                                                                                     | `one2many`  |     | ✅    | rating.rating                      |
| `rating_last_feedback`                   | Rating Last Feedback                                                                        | `text`      |     |       |                                    |
| `rating_last_image`                      | Rating Last Image                                                                           | `binary`    |     |       |                                    |
| `rating_last_text`                       | Rating Text                                                                                 | `selection` |     | ✅    |                                    |
| `rating_last_value`                      | Rating Last Value                                                                           | `float`     |     | ✅    |                                    |
| `rating_percentage_satisfaction`         | Rating Satisfaction                                                                         | `float`     |     |       |                                    |
| `rtc_session_ids`                        | Rtc Session                                                                                 | `one2many`  |     | ✅    | discuss.channel.rtc.session        |
| `self_member_id`                         | Self Member                                                                                 | `many2one`  |     |       | discuss.channel.member             |
| `sfu_channel_uuid`                       | Sfu Channel Uuid                                                                            | `char`      |     | ✅    |                                    |
| `sfu_server_url`                         | Sfu Server Url                                                                              | `char`      |     | ✅    |                                    |
| `student_id`                             | Student                                                                                     | `many2one`  |     | ✅    | op.student                         |
| `sub_channel_ids`                        | Sub Channels                                                                                | `one2many`  |     | ✅    | discuss.channel                    |
| `subscription_department_ids`            | HR Departments                                                                              | `many2many` |     | ✅    | hr.department                      |
| `uuid`                                   | UUID                                                                                        | `char`      |     | ✅    |                                    |
| `website_message_ids`                    | Website Messages                                                                            | `one2many`  |     | ✅    | mail.message                       |
| `whatsapp_contact`                       | Whatsapp Contact                                                                            | `many2one`  |     | ✅    | whatsapp.contact                   |
| `write_date`                             | Last Updated on                                                                             | `datetime`  |     | ✅    |                                    |
| `write_uid`                              | Last Updated by                                                                             | `many2one`  |     | ✅    | res.users                          |

**Access Rights:**

| Name                   | Group                | Perms     |
| ---------------------- | -------------------- | --------- |
| discuss.channel.system | Role / Administrator | `R/W/C/D` |
| discuss.channel.portal | Role / Portal        | `R`       |
| discuss.channel.portal | Role / Portal        | `R/W/C/D` |
| discuss.channel.public | Role / Public        | `R`       |
| discuss.channel.user   | Role / User          | `R/W/C`   |

**Record Rules:**

- **discuss.channel: can access channels (as member or as group allowed)** (10, 11, 1)
  `R/W/C/D`
  - Domain:
    `             [                 "|",                     "&",                         ("channel_type", "!=", "channel"),                         "|",                             ("is_member", "=", True),                             ("parent_channel_id.is_member", "=", True),                     "&",                         ("channel_type", "=", "channel"),                         "|",                             ("group_public_id", "=", False),                             ("group_public_id", "in", user.all_group_ids.ids),             ]         `
- **discuss.channel: admin full access** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **discuss.channel: livechat users can read all livechat channels** (51) `R`
  - Domain: `[('channel_type', '=', 'livechat')]`
- **discuss.channel: sales users can read lead's origin channel** (25) `R`
  - Domain: `[("has_crm_lead", "=", True)]`

### 🗃️ `mail.activity` — Activity

An actual activity to perform. Activities are linked to documents using res_id and
res_model_id fields. Activities have a deadline that can be used in kanban view to
display a status. Once done activities are unlinked and a message is posted. This
message has a new activity_type_id field that indicates the activity linked to the
message.

**Fields:**

| Field                          | Label                     | Type                 | Req | Store | Relation           |
| ------------------------------ | ------------------------- | -------------------- | --- | ----- | ------------------ |
| `active`                       | Active                    | `boolean`            |     | ✅    |                    |
| `activity_category`            | Action                    | `selection`          |     |       |                    |
| `activity_decoration`          | Decoration Type           | `selection`          |     |       |                    |
| `activity_type_id`             | Activity Type             | `many2one`           |     | ✅    | mail.activity.type |
| `attachment_ids`               | Attachments               | `many2many`          |     | ✅    | ir.attachment      |
| `automated`                    | Automated activity        | `boolean`            |     | ✅    |                    |
| `calendar_event_id`            | Calendar Meeting          | `many2one`           |     | ✅    | calendar.event     |
| `can_write`                    | Can Write                 | `boolean`            |     |       |                    |
| `chaining_type`                | Chaining Type             | `selection`          |     |       |                    |
| `create_date`                  | Created on                | `datetime`           |     | ✅    |                    |
| `create_uid`                   | Created by                | `many2one`           |     | ✅    | res.users          |
| `date_deadline`                | Due Date                  | `date`               | ✅  | ✅    |                    |
| `date_done`                    | Done Date                 | `date`               |     | ✅    |                    |
| `display_name`                 | Display Name              | `char`               |     |       |                    |
| `feedback`                     | Feedback                  | `text`               |     | ✅    |                    |
| `has_recommended_activities`   | Next activities available | `boolean`            |     |       |                    |
| `icon`                         | Icon                      | `char`               |     |       |                    |
| `id`                           | ID                        | `integer`            |     | ✅    |                    |
| `mail_template_ids`            | Email templates           | `many2many`          |     |       | mail.template      |
| `note`                         | Note                      | `html`               |     | ✅    |                    |
| `previous_activity_type_id`    | Previous Activity Type    | `many2one`           |     | ✅    | mail.activity.type |
| `recommended_activity_type_id` | Recommended Activity Type | `many2one`           |     | ✅    | mail.activity.type |
| `res_id`                       | Related Document ID       | `many2one_reference` |     | ✅    |                    |
| `res_model`                    | Related Document Model    | `char`               |     | ✅    |                    |
| `res_model_id`                 | Document Model            | `many2one`           |     | ✅    | ir.model           |
| `res_name`                     | Document Name             | `char`               |     | ✅    |                    |
| `state`                        | State                     | `selection`          |     |       |                    |
| `summary`                      | Summary                   | `char`               |     | ✅    |                    |
| `user_id`                      | Assigned to               | `many2one`           |     | ✅    | res.users          |
| `user_tz`                      | Timezone                  | `selection`          |     | ✅    |                    |
| `write_date`                   | Last Updated on           | `datetime`           |     | ✅    |                    |
| `write_uid`                    | Last Updated by           | `many2one`           |     | ✅    | res.users          |

**Access Rights:**

| Name               | Group       | Perms     |
| ------------------ | ----------- | --------- |
| mail.activity.user | Role / User | `R/W/C/D` |

**Record Rules:**

- **mail.activity: user: write/unlink only (created or assigned)** (1) `W/D`
  - Domain: `['|', ('user_id', '=', user.id), ('create_uid', '=', user.id)]`

### 🗃️ `mail.activity.mixin` — Activity Mixin

Mail Activity Mixin is a mixin class to use if you want to add activities management on
a model. It works like the mail.thread mixin. It defines an activity_ids one2many field
toward activities using res_id and res_model_id. Various related / computed fields are
also added to have a global status of activities on documents.

    Activities come with a new JS widget for the form view. It is integrated in the
    Chatter widget although it is a separate widget. It displays activities linked
    to the current record and allow to schedule, edit and mark done activities.

    There is also a kanban widget defined. It defines a small widget to integrate
    in kanban vignettes. It allow to manage activities directly from the kanban
    view. Use widget="kanban_activity" on activitiy_ids field in kanban view to
    use it.

    Some context keys allow to control the mixin behavior. Use those in some
    specific cases like import

     * ``mail_activity_automation_skip``: skip activities automation; it means
       no automated activities will be generated, updated or unlinked, allowing
       to save computation and avoid generating unwanted activities;

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
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                    |

### 🗃️ `mail.activity.schedule` — Activity schedule plan Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                        | Label                      | Type        | Req | Store | Relation                    |
| ---------------------------- | -------------------------- | ----------- | --- | ----- | --------------------------- |
| `activity_category`          | Action                     | `selection` |     |       |                             |
| `activity_type_id`           | Activity Type              | `many2one`  |     | ✅    | mail.activity.type          |
| `activity_user_id`           | Assigned to                | `many2one`  |     | ✅    | res.users                   |
| `chaining_type`              | Chaining Type              | `selection` |     |       |                             |
| `company_id`                 | Company                    | `many2one`  |     |       | res.company                 |
| `create_date`                | Created on                 | `datetime`  |     | ✅    |                             |
| `create_uid`                 | Created by                 | `many2one`  |     | ✅    | res.users                   |
| `date_deadline`              | Due Date                   | `date`      |     | ✅    |                             |
| `department_id`              | Department                 | `many2one`  |     |       | hr.department               |
| `display_name`               | Display Name               | `char`      |     |       |                             |
| `error`                      | Error                      | `html`      |     |       |                             |
| `has_error`                  | Has Error                  | `boolean`   |     |       |                             |
| `has_warning`                | Has Warning                | `boolean`   |     |       |                             |
| `id`                         | ID                         | `integer`   |     | ✅    |                             |
| `is_batch_mode`              | Use in batch               | `boolean`   |     |       |                             |
| `note`                       | Note                       | `html`      |     | ✅    |                             |
| `plan_available_ids`         | Plan Available             | `many2many` |     | ✅    | mail.activity.plan          |
| `plan_date`                  | Plan Date                  | `date`      |     | ✅    |                             |
| `plan_department_filterable` | Plan Department Filterable | `boolean`   |     |       |                             |
| `plan_has_user_on_demand`    | Has on demand responsible  | `boolean`   |     |       |                             |
| `plan_id`                    | Plan                       | `many2one`  |     | ✅    | mail.activity.plan          |
| `plan_on_demand_user_id`     | Assigned To                | `many2one`  |     | ✅    | res.users                   |
| `plan_schedule_line_ids`     | Schedule Lines             | `one2many`  |     |       | mail.activity.schedule.line |
| `res_ids`                    | Document IDs               | `text`      |     | ✅    |                             |
| `res_model`                  | Model                      | `char`      |     | ✅    |                             |
| `res_model_id`               | Applies to                 | `many2one`  |     | ✅    | ir.model                    |
| `summary`                    | Summary                    | `char`      |     | ✅    |                             |
| `warning`                    | Warning                    | `html`      |     |       |                             |
| `write_date`                 | Last Updated on            | `datetime`  |     | ✅    |                             |
| `write_uid`                  | Last Updated by            | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                        | Group       | Perms   |
| --------------------------- | ----------- | ------- |
| mail.activity.schedule.user | Role / User | `R/W/C` |

### 🗃️ `mail.activity.type` — Activity Type

Activity Types are used to categorize activities. Each type is a different kind of
activity e.g. call, mail, meeting. An activity can be generic i.e. available for all
models using activities; or specific to a model in which case res_model field should be
used.

**Fields:**

| Field                     | Label                | Type        | Req | Store | Relation           |
| ------------------------- | -------------------- | ----------- | --- | ----- | ------------------ |
| `active`                  | Active               | `boolean`   |     | ✅    |                    |
| `category`                | Action               | `selection` |     | ✅    |                    |
| `chaining_type`           | Chaining Type        | `selection` | ✅  | ✅    |                    |
| `create_date`             | Created on           | `datetime`  |     | ✅    |                    |
| `create_uid`              | Create Uid           | `many2one`  |     | ✅    | res.users          |
| `decoration_type`         | Decoration Type      | `selection` |     | ✅    |                    |
| `default_note`            | Default Note         | `html`      |     | ✅    |                    |
| `default_user_id`         | Default User         | `many2one`  |     | ✅    | res.users          |
| `delay_count`             | Schedule             | `integer`   |     | ✅    |                    |
| `delay_from`              | Delay Type           | `selection` | ✅  | ✅    |                    |
| `delay_label`             | Delay Label          | `char`      |     |       |                    |
| `delay_unit`              | Delay units          | `selection` | ✅  | ✅    |                    |
| `display_name`            | Display Name         | `char`      |     |       |                    |
| `icon`                    | Icon                 | `char`      |     | ✅    |                    |
| `id`                      | ID                   | `integer`   |     | ✅    |                    |
| `initial_res_model`       | Initial model        | `selection` |     |       |                    |
| `mail_template_ids`       | Email templates      | `many2many` |     | ✅    | mail.template      |
| `name`                    | Name                 | `char`      | ✅  | ✅    |                    |
| `previous_type_ids`       | Preceding Activities | `many2many` |     | ✅    | mail.activity.type |
| `res_model`               | Model                | `selection` |     | ✅    |                    |
| `res_model_change`        | Model has change     | `boolean`   |     |       |                    |
| `sequence`                | Sequence             | `integer`   |     | ✅    |                    |
| `suggested_next_type_ids` | Suggest              | `many2many` |     | ✅    | mail.activity.type |
| `summary`                 | Default Summary      | `char`      |     | ✅    |                    |
| `triggered_next_type_id`  | Trigger              | `many2one`  |     | ✅    | mail.activity.type |
| `write_date`              | Last Updated on      | `datetime`  |     | ✅    |                    |
| `write_uid`               | Last Updated by      | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                | Group                    | Perms     |
| ----------------------------------- | ------------------------ | --------- |
| mail.activity.type.sale.manager     | Sales / Administrator    | `R/W/C/D` |
| mail.activity.type.sale.manager     | Sales / Administrator    | `R/W/C/D` |
| mail.activity.type.holidays.manager | Time Off / Administrator | `R/W/C/D` |
| mail.activity.type.expense.user     | Expenses / Administrator | `R/W/C/D` |
| mail.activity.type.fleet.manager    | Fleet / Administrator    | `R/W/C/D` |
| mail.activity.type.system           | Role / Administrator     | `R/W/C/D` |
| mail.activity.type.user             | Role / User              | `R`       |

### 🗃️ `calendar.attendee` — Calendar Attendee Information

Calendar Attendee Information

**Fields:**

| Field                  | Label             | Type        | Req | Store | Relation            |
| ---------------------- | ----------------- | ----------- | --- | ----- | ------------------- |
| `access_token`         | Invitation Token  | `char`      |     | ✅    |                     |
| `apw`                  | Attendee Password | `char`      |     | ✅    |                     |
| `attendee_meeting_url` | URL               | `char`      |     | ✅    |                     |
| `availability`         | Available/Busy    | `selection` |     | ✅    |                     |
| `common_name`          | Common name       | `char`      |     | ✅    |                     |
| `create_date`          | Created on        | `datetime`  |     | ✅    |                     |
| `create_uid`           | Created by        | `many2one`  |     | ✅    | res.users           |
| `display_name`         | Display Name      | `char`      |     |       |                     |
| `email`                | Email             | `char`      |     |       |                     |
| `event_id`             | Meeting linked    | `many2one`  | ✅  | ✅    | calendar.event      |
| `id`                   | ID                | `integer`   |     | ✅    |                     |
| `mail_tz`              | Mail Tz           | `selection` |     |       |                     |
| `partner_id`           | Attendee          | `many2one`  | ✅  | ✅    | res.partner         |
| `phone`                | Phone             | `char`      |     |       |                     |
| `recurrence_id`        | Recurrence Rule   | `many2one`  |     |       | calendar.recurrence |
| `state`                | Status            | `selection` |     | ✅    |                     |
| `write_date`           | Last Updated on   | `datetime`  |     | ✅    |                     |
| `write_uid`            | Last Updated by   | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                       | Group                                   | Perms     |
| -------------------------- | --------------------------------------- | --------- |
| calendar.attendee.hr.user  | Time Off / Officer: Manage all requests | `R/W/C/D` |
| calendar.attendee_portal   | Role / Portal                           | `-`       |
| calendar.attendee_employee | Role / User                             | `R/W/C/D` |

**Record Rules:**

- **Own attendees** (10) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `calendar.filters` — Calendar Filters

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label           | Type       | Req | Store | Relation    |
| ----------------- | --------------- | ---------- | --- | ----- | ----------- |
| `active`          | Active          | `boolean`  |     | ✅    |             |
| `create_date`     | Created on      | `datetime` |     | ✅    |             |
| `create_uid`      | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name`    | Display Name    | `char`     |     |       |             |
| `id`              | ID              | `integer`  |     | ✅    |             |
| `partner_checked` | Checked         | `boolean`  |     | ✅    |             |
| `partner_id`      | Employee        | `many2one` | ✅  | ✅    | res.partner |
| `user_id`         | Me              | `many2one` | ✅  | ✅    | res.users   |
| `write_date`      | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`       | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                         | Group                | Perms     |
| ---------------------------- | -------------------- | --------- |
| access_calendar_contacts     | Role / Administrator | `R/W/C/D` |
| access_calendar_contacts_all | Role / User          | `R/W/C/D` |

### 🗃️ `calendar.popover.delete.wizard` — Calendar Popover Delete Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                     | Label                                    | Type        | Req | Store | Relation       |
| ------------------------- | ---------------------------------------- | ----------- | --- | ----- | -------------- |
| `body`                    | Contents                                 | `html`      |     | ✅    |                |
| `body_has_template_value` | Body content is the same as the template | `boolean`   |     |       |                |
| `calendar_event_id`       | Calendar Event                           | `many2one`  |     | ✅    | calendar.event |
| `can_edit_body`           | Can Edit Body                            | `boolean`   |     |       |                |
| `create_date`             | Created on                               | `datetime`  |     | ✅    |                |
| `create_uid`              | Created by                               | `many2one`  |     | ✅    | res.users      |
| `delete`                  | Delete                                   | `selection` |     | ✅    |                |
| `display_name`            | Display Name                             | `char`      |     |       |                |
| `id`                      | ID                                       | `integer`   |     | ✅    |                |
| `is_mail_template_editor` | Is Editor                                | `boolean`   |     |       |                |
| `lang`                    | Language                                 | `char`      |     | ✅    |                |
| `recipient_ids`           | Recipients                               | `many2many` |     |       | res.partner    |
| `render_model`            | Rendering Model                          | `char`      |     |       |                |
| `subject`                 | Subject                                  | `char`      |     | ✅    |                |
| `template_id`             | Mail Template                            | `many2one`  |     | ✅    | mail.template  |
| `write_date`              | Last Updated on                          | `datetime`  |     | ✅    |                |
| `write_uid`               | Last Updated by                          | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                                     | Group       | Perms     |
| ---------------------------------------- | ----------- | --------- |
| calendar.attendee_employee_delete_wizard | Role / User | `R/W/C/D` |

### 🗃️ `calendar.provider.config` — Calendar Provider Configuration Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                                 | Label                                    | Type        | Req | Store | Relation  |
| ------------------------------------- | ---------------------------------------- | ----------- | --- | ----- | --------- |
| `cal_client_id`                       | Google Client_id                         | `char`      |     | ✅    |           |
| `cal_client_secret`                   | Google Client_key                        | `char`      |     | ✅    |           |
| `cal_sync_paused`                     | Google Synchronization Paused            | `boolean`   |     | ✅    |           |
| `create_date`                         | Created on                               | `datetime`  |     | ✅    |           |
| `create_uid`                          | Created by                               | `many2one`  |     | ✅    | res.users |
| `display_name`                        | Display Name                             | `char`      |     |       |           |
| `external_calendar_provider`          | Choose an external calendar to configure | `selection` |     | ✅    |           |
| `id`                                  | ID                                       | `integer`   |     | ✅    |           |
| `microsoft_outlook_client_identifier` | Outlook Client Id                        | `char`      |     | ✅    |           |
| `microsoft_outlook_client_secret`     | Outlook Client Secret                    | `char`      |     | ✅    |           |
| `microsoft_outlook_sync_paused`       | Outlook Synchronization Paused           | `boolean`   |     | ✅    |           |
| `write_date`                          | Last Updated on                          | `datetime`  |     | ✅    |           |
| `write_uid`                           | Last Updated by                          | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                             | Group                | Perms     |
| -------------------------------- | -------------------- | --------- |
| calendar.provider.config.manager | Role / Administrator | `R/W/C/D` |
| calendar.provider.config.all     | Everyone             | `-`       |

### 🗃️ `calendar.alarm` — Event Alarm

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label               | Type        | Req | Store | Relation      |
| -------------------- | ------------------- | ----------- | --- | ----- | ------------- |
| `alarm_type`         | Type                | `selection` | ✅  | ✅    |               |
| `body`               | Additional Message  | `text`      |     | ✅    |               |
| `create_date`        | Created on          | `datetime`  |     | ✅    |               |
| `create_uid`         | Created by          | `many2one`  |     | ✅    | res.users     |
| `display_name`       | Display Name        | `char`      |     |       |               |
| `duration`           | Remind Before       | `integer`   | ✅  | ✅    |               |
| `duration_minutes`   | Duration in minutes | `integer`   |     | ✅    |               |
| `id`                 | ID                  | `integer`   |     | ✅    |               |
| `interval`           | Unit                | `selection` | ✅  | ✅    |               |
| `mail_template_id`   | Email Template      | `many2one`  |     | ✅    | mail.template |
| `name`               | Name                | `char`      | ✅  | ✅    |               |
| `notify_responsible` | Notify Responsible  | `boolean`   |     | ✅    |               |
| `sms_template_id`    | SMS Template        | `many2one`  |     | ✅    | sms.template  |
| `write_date`         | Last Updated on     | `datetime`  |     | ✅    |               |
| `write_uid`          | Last Updated by     | `many2one`  |     | ✅    | res.users     |

**Access Rights:**

| Name           | Group       | Perms     |
| -------------- | ----------- | --------- |
| calendar.alarm | Role / User | `R/W/C/D` |

### 🗃️ `calendar.alarm_manager` — Event Alarm Manager

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

**Access Rights:**

| Name                          | Group       | Perms     |
| ----------------------------- | ----------- | --------- |
| access_calendar_alarm_manager | Role / User | `R/W/C/D` |

### 🗃️ `calendar.event.type` — Event Meeting Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `color`        | Color           | `integer`  |     | ✅    |           |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Name            | `char`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                         | Group                                        | Perms     |
| ---------------------------- | -------------------------------------------- | --------- |
| calendar.event.type.salesman | Sales / User: Own Documents Only             | `R`       |
| calendar.event.type.manager  | Sales / Administrator                        | `R/W/C`   |
| calendar.event.type.manager  | Time Off / Administrator                     | `R/W/C/D` |
| calendar.event.type.officer  | Recruitment / Officer: Manage all applicants | `R/W/C`   |
| calendar.event.type.manager  | Role / Administrator                         | `R/W/C/D` |
| calendar.event.type.all      | Role / User                                  | `R`       |
| calendar.event.type.user     | Role / User                                  | `R`       |

### 🗃️ `calendar.recurrence` — Event Recurrence Rule

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label           | Type        | Req | Store | Relation        |
| -------------------- | --------------- | ----------- | --- | ----- | --------------- |
| `base_event_id`      | Base Event      | `many2one`  |     | ✅    | calendar.event  |
| `byday`              | By day          | `selection` |     | ✅    |                 |
| `calendar_event_ids` | Calendar Event  | `one2many`  |     | ✅    | calendar.event  |
| `count`              | Count           | `integer`   |     | ✅    |                 |
| `create_date`        | Created on      | `datetime`  |     | ✅    |                 |
| `create_uid`         | Created by      | `many2one`  |     | ✅    | res.users       |
| `day`                | Day             | `integer`   |     | ✅    |                 |
| `display_name`       | Display Name    | `char`      |     |       |                 |
| `dtstart`            | Dtstart         | `datetime`  |     |       |                 |
| `end_type`           | End Type        | `selection` |     | ✅    |                 |
| `event_tz`           | Timezone        | `selection` |     | ✅    |                 |
| `fri`                | Fri             | `boolean`   |     | ✅    |                 |
| `id`                 | ID              | `integer`   |     | ✅    |                 |
| `interval`           | Interval        | `integer`   |     | ✅    |                 |
| `mon`                | Mon             | `boolean`   |     | ✅    |                 |
| `month_by`           | Month By        | `selection` |     | ✅    |                 |
| `name`               | Name            | `char`      |     | ✅    |                 |
| `rrule`              | Rrule           | `char`      |     | ✅    |                 |
| `rrule_type`         | Rrule Type      | `selection` |     | ✅    |                 |
| `sat`                | Sat             | `boolean`   |     | ✅    |                 |
| `sun`                | Sun             | `boolean`   |     | ✅    |                 |
| `thu`                | Thu             | `boolean`   |     | ✅    |                 |
| `trigger_id`         | Trigger         | `many2one`  |     | ✅    | ir.cron.trigger |
| `tue`                | Tue             | `boolean`   |     | ✅    |                 |
| `until`              | Repeat Until    | `date`      |     | ✅    |                 |
| `wed`                | Wed             | `boolean`   |     | ✅    |                 |
| `weekday`            | Weekday         | `selection` |     | ✅    |                 |
| `write_date`         | Last Updated on | `datetime`  |     | ✅    |                 |
| `write_uid`          | Last Updated by | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                       | Group       | Perms     |
| -------------------------- | ----------- | --------- |
| access_calendar_recurrence | Role / User | `R/W/C/D` |

### 🗃️ `ir.http` — HTTP Routing

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `res.users` — User

Update of res.users class - add a preference about username for livechat purpose

**Fields:**

| Field                                       | Label                                                 | Type         | Req | Store | Relation                    |
| ------------------------------------------- | ----------------------------------------------------- | ------------ | --- | ----- | --------------------------- |
| `accesses_count`                            | # Access Rights                                       | `integer`    |     |       |                             |
| `access_token`                              | Access Token                                          | `char`       |     | ✅    |                             |
| `account_move_count`                        | Account Move Count                                    | `integer`    |     |       |                             |
| `action_id`                                 | Home Action                                           | `many2one`   |     | ✅    | ir.actions.actions          |
| `active`                                    | Active                                                | `boolean`    |     | ✅    |                             |
| `active_lang_count`                         | Active Lang Count                                     | `integer`    |     |       |                             |
| `active_partner`                            | Partner is Active                                     | `boolean`    |     |       |                             |
| `activity_calendar_event_id`                | Next Activity Calendar Event                          | `many2one`   |     |       | calendar.event              |
| `activity_date_deadline`                    | Next Activity Deadline                                | `date`       |     |       |                             |
| `activity_exception_decoration`             | Activity Exception Decoration                         | `selection`  |     |       |                             |
| `activity_exception_icon`                   | Icon                                                  | `char`       |     |       |                             |
| `activity_ids`                              | Activities                                            | `one2many`   |     |       | mail.activity               |
| `activity_state`                            | Activity State                                        | `selection`  |     |       |                             |
| `activity_summary`                          | Next Activity Summary                                 | `char`       |     |       |                             |
| `activity_type_icon`                        | Activity Type Icon                                    | `char`       |     |       |                             |
| `activity_type_id`                          | Next Activity Type                                    | `many2one`   |     |       | mail.activity.type          |
| `activity_user_id`                          | Responsible User                                      | `many2one`   |     |       | res.users                   |
| `additional_note`                           | Additional Note                                       | `text`       |     |       |                             |
| `all_group_ids`                             | Groups and implied groups                             | `many2many`  |     |       | res.groups                  |
| `api_key_ids`                               | API Keys                                              | `one2many`   |     | ✅    | res.users.apikeys           |
| `applicant_ids`                             | Applicants                                            | `one2many`   |     |       | hr.applicant                |
| `application_count`                         | Applications                                          | `integer`    |     |       |                             |
| `application_statistics`                    | Stats                                                 | `json`       |     |       |                             |
| `auth_passkey_key_ids`                      | Auth Passkey Key                                      | `one2many`   |     | ✅    | auth.passkey.key            |
| `autopost_bills`                            | Auto-post bills                                       | `selection`  | ✅  |       |                             |
| `available_invoice_template_pdf_report_ids` | Available Invoice Template Pdf Report                 | `one2many`   |     |       | ir.actions.report           |
| `available_peppol_eas`                      | Available Peppol Eas                                  | `json`       |     |       |                             |
| `avatar_1024`                               | Avatar 1024                                           | `binary`     |     |       |                             |
| `avatar_128`                                | Avatar 128                                            | `binary`     |     |       |                             |
| `avatar_1920`                               | Avatar                                                | `binary`     |     |       |                             |
| `avatar_256`                                | Avatar 256                                            | `binary`     |     |       |                             |
| `avatar_512`                                | Avatar 512                                            | `binary`     |     |       |                             |
| `badge_ids`                                 | Badges                                                | `one2many`   |     | ✅    | gamification.badge.user     |
| `bank_account_count`                        | Bank                                                  | `integer`    |     |       |                             |
| `bank_account_ids`                          | Bank Accounts                                         | `many2many`  |     |       | res.partner.bank            |
| `bank_ids`                                  | Banks                                                 | `one2many`   |     |       | res.partner.bank            |
| `barcode`                                   | Badge ID                                              | `char`       |     |       |                             |
| `bronze_badge`                              | Bronze badges count                                   | `integer`    |     |       |                             |
| `buyer_id`                                  | Buyer                                                 | `many2one`   |     |       | res.users                   |
| `calendar_default_privacy`                  | Calendar Default Privacy                              | `selection`  |     |       |                             |
| `calendar_last_notif_ack`                   | Last notification marked as read from base Calendar   | `datetime`   |     |       |                             |
| `can_edit_role`                             | Can Edit Role                                         | `boolean`    |     |       |                             |
| `can_publish`                               | Can Publish                                           | `boolean`    |     |       |                             |
| `category_id`                               | Tags                                                  | `many2many`  |     |       | res.partner.category        |
| `category_ids`                              | Employee Tags                                         | `many2many`  |     |       | hr.employee.category        |
| `certifications_company_count`              | Company Certifications Count                          | `integer`    |     |       |                             |
| `certifications_count`                      | Certifications Count                                  | `integer`    |     |       |                             |
| `channel_ids`                               | Channels                                              | `many2many`  |     |       | discuss.channel             |
| `channel_member_ids`                        | Channel Member                                        | `one2many`   |     |       | discuss.channel.member      |
| `chatbot_script_ids`                        | Chatbot Script                                        | `one2many`   |     |       | chatbot.script              |
| `chatter_position`                          | Chatter Position                                      | `selection`  |     | ✅    |                             |
| `child_ids`                                 | Childs                                                | `many2many`  |     | ✅    | res.users                   |
| `city`                                      | City                                                  | `char`       |     |       |                             |
| `client_id`                                 | Client ID                                             | `char`       |     | ✅    |                             |
| `client_secret`                             | Client Secret                                         | `char`       |     | ✅    |                             |
| `code`                                      | Company Code                                          | `char`       |     |       |                             |
| `color`                                     | Color Index                                           | `integer`    |     |       |                             |
| `comment`                                   | Notes                                                 | `html`       |     |       |                             |
| `commercial_company_name`                   | Company Name Entity                                   | `char`       |     |       |                             |
| `commercial_partner_id`                     | Commercial Entity                                     | `many2one`   |     |       | res.partner                 |
| `companies_count`                           | Number of Companies                                   | `integer`    |     |       |                             |
| `company_id`                                | Company                                               | `many2one`   | ✅  | ✅    | res.company                 |
| `company_ids`                               | Companies                                             | `many2many`  |     | ✅    | res.company                 |
| `company_name`                              | Company Name                                          | `char`       |     |       |                             |
| `company_registry`                          | Company ID                                            | `char`       |     |       |                             |
| `company_registry_label`                    | Company ID Label                                      | `char`       |     |       |                             |
| `company_registry_placeholder`              | Company Registry Placeholder                          | `char`       |     |       |                             |
| `company_type`                              | Company Type                                          | `selection`  |     |       |                             |
| `complete_name`                             | Complete Name                                         | `char`       |     |       |                             |
| `contact_address`                           | Complete Address                                      | `char`       |     |       |                             |
| `contact_address_inline`                    | Inlined Complete Address                              | `char`       |     |       |                             |
| `contract_ids`                              | Partner Contracts                                     | `one2many`   |     |       | account.analytic.account    |
| `country_code`                              | Country Code                                          | `char`       |     |       |                             |
| `country_id`                                | Country                                               | `many2one`   |     |       | res.country                 |
| `create_date`                               | Create Date                                           | `datetime`   |     | ✅    |                             |
| `create_employee`                           | Technical field, whether to create an employee        | `boolean`    |     |       |                             |
| `create_employee_id`                        | Technical field, bind user to this employee on create | `many2one`   |     |       | hr.employee                 |
| `create_uid`                                | Created by                                            | `many2one`   |     | ✅    | res.users                   |
| `credit`                                    | Total Receivable                                      | `monetary`   |     |       |                             |
| `credit_limit`                              | Credit Limit                                          | `float`      |     |       |                             |
| `credit_to_invoice`                         | Credit To Invoice                                     | `monetary`   |     |       |                             |
| `crm_team_ids`                              | Sales Teams                                           | `many2many`  |     |       | crm.team                    |
| `crm_team_member_ids`                       | Sales Team Members                                    | `one2many`   |     | ✅    | crm.team.member             |
| `currency_id`                               | Currency                                              | `many2one`   |     |       | res.currency                |
| `customer_rank`                             | Customer Rank                                         | `integer`    |     |       |                             |
| `dark_mode`                                 | Dark Mode                                             | `boolean`    |     | ✅    |                             |
| `days_sales_outstanding`                    | Days Sales Outstanding (DSO)                          | `float`      |     |       |                             |
| `debit`                                     | Total Payable                                         | `monetary`   |     |       |                             |
| `department_count`                          | Number of Departments                                 | `integer`    |     |       |                             |
| `department_ids`                            | Allowed Department                                    | `many2many`  |     | ✅    | op.department               |
| `dept_id`                                   | Department Name                                       | `many2one`   |     | ✅    | op.department               |
| `device_ids`                                | User devices                                          | `one2many`   |     | ✅    | res.device                  |
| `display_invoice_edi_format`                | Display Invoice Edi Format                            | `boolean`    |     |       |                             |
| `display_invoice_template_pdf_report_id`    | Display Invoice Template Pdf Report                   | `boolean`    |     |       |                             |
| `display_name`                              | Display Name                                          | `char`       |     |       |                             |
| `duplicate_bank_partner_ids`                | Duplicate Bank Partner                                | `many2many`  |     |       | res.partner                 |
| `email`                                     | Email                                                 | `char`       |     |       |                             |
| `email_domain_placeholder`                  | Email Domain Placeholder                              | `char`       |     |       |                             |
| `email_formatted`                           | Formatted Email                                       | `char`       |     |       |                             |
| `email_normalized`                          | Normalized Email                                      | `char`       |     |       |                             |
| `emergency_contact`                         | Emergency Contact                                     | `char`       |     |       |                             |
| `emergency_phone`                           | Emergency Phone                                       | `char`       |     |       |                             |
| `employee`                                  | Employee                                              | `boolean`    |     |       |                             |
| `employee_bank_account_ids`                 | Employee's Bank Accounts                              | `many2many`  |     |       | res.partner.bank            |
| `employee_count`                            | Employee Count                                        | `integer`    |     |       |                             |
| `employee_id`                               | Company employee                                      | `many2one`   |     |       | hr.employee                 |
| `employee_ids`                              | Related employee                                      | `one2many`   |     | ✅    | hr.employee                 |
| `employee_resource_calendar_id`             | Employee's Working Hours                              | `many2one`   |     |       | resource.calendar           |
| `employees_count`                           | Employees Count                                       | `integer`    |     |       |                             |
| `esign_initials`                            | Digitial Initials                                     | `binary`     |     | ✅    |                             |
| `esign_signature`                           | Digital Signature                                     | `binary`     |     | ✅    |                             |
| `event_count`                               | # Events                                              | `integer`    |     |       |                             |
| `fiscal_country_codes`                      | Fiscal Country Codes                                  | `char`       |     |       |                             |
| `fiscal_country_group_codes`                | Fiscal Country Group Codes                            | `json`       |     |       |                             |
| `friday_location_id`                        | Fridays                                               | `many2one`   |     |       | hr.work.location            |
| `function`                                  | Job Position                                          | `char`       |     |       |                             |
| `global_location_number`                    | GLN                                                   | `char`       |     |       |                             |
| `goal_ids`                                  | Goal                                                  | `one2many`   |     | ✅    | gamification.goal           |
| `gold_badge`                                | Gold badges count                                     | `integer`    |     |       |                             |
| `grievance_team_id`                         | Grievance Team                                        | `many2one`   |     | ✅    | grievance.team              |
| `group_ids`                                 | Groups                                                | `many2many`  |     | ✅    | res.groups                  |
| `group_on`                                  | Week Day                                              | `selection`  | ✅  |       |                             |
| `group_rfq`                                 | Group RFQ                                             | `selection`  | ✅  |       |                             |
| `groups_count`                              | # Groups                                              | `integer`    |     |       |                             |
| `has_access_livechat`                       | Has access to Livechat                                | `boolean`    |     |       |                             |
| `has_external_mail_server`                  | Has External Mail Server                              | `boolean`    |     |       |                             |
| `has_message`                               | Has Message                                           | `boolean`    |     |       |                             |
| `head_office`                               | Head Office                                           | `char`       |     |       |                             |
| `hr_contact`                                | HR Contact                                            | `char`       |     |       |                             |
| `hr_email`                                  | HR Email                                              | `char`       |     |       |                             |
| `hr_name`                                   | HR Name                                               | `char`       |     |       |                             |
| `id`                                        | ID                                                    | `integer`    |     | ✅    |                             |
| `ignore_abnormal_invoice_amount`            | Ignore Abnormal Invoice Amount                        | `boolean`    |     |       |                             |
| `ignore_abnormal_invoice_date`              | Ignore Abnormal Invoice Date                          | `boolean`    |     |       |                             |
| `image_1024`                                | Image 1024                                            | `binary`     |     |       |                             |
| `image_128`                                 | Image 128                                             | `binary`     |     |       |                             |
| `image_1920`                                | Image                                                 | `binary`     |     |       |                             |
| `image_256`                                 | Image 256                                             | `binary`     |     |       |                             |
| `image_512`                                 | Image 512                                             | `binary`     |     |       |                             |
| `im_status`                                 | IM Status                                             | `char`       |     |       |                             |
| `industry_id`                               | Industry                                              | `many2one`   |     |       | res.partner.industry        |
| `invoice_edi_format`                        | eInvoice format                                       | `selection`  |     |       |                             |
| `invoice_edi_format_store`                  | Invoice Edi Format Store                              | `char`       |     |       |                             |
| `invoice_ids`                               | Invoices                                              | `one2many`   |     |       | account.move                |
| `invoice_sending_method`                    | Invoice sending                                       | `selection`  |     |       |                             |
| `invoice_template_pdf_report_id`            | Invoice report                                        | `many2one`   |     |       | ir.actions.report           |
| `is_blacklisted`                            | Blacklist                                             | `boolean`    |     |       |                             |
| `is_company`                                | Is a Company                                          | `boolean`    |     |       |                             |
| `is_hr_user`                                | Is Hr User                                            | `boolean`    |     |       |                             |
| `is_in_call`                                | Is in call                                            | `boolean`    |     |       |                             |
| `is_out_of_office`                          | Out of Office                                         | `boolean`    |     |       |                             |
| `is_parent`                                 | Is a Parent                                           | `boolean`    |     |       |                             |
| `is_peppol_edi_format`                      | Is Peppol Edi Format                                  | `boolean`    |     |       |                             |
| `is_pickup_location`                        | Is Pickup Location                                    | `boolean`    |     |       |                             |
| `is_public`                                 | Is Public                                             | `boolean`    |     |       |                             |
| `is_published`                              | Is Published                                          | `boolean`    |     |       |                             |
| `is_seo_optimized`                          | SEO optimized                                         | `boolean`    |     |       |                             |
| `is_student`                                | Is a Student                                          | `boolean`    |     |       |                             |
| `is_system`                                 | Is System                                             | `boolean`    |     |       |                             |
| `is_ubl_format`                             | Is Ubl Format                                         | `boolean`    |     |       |                             |
| `is_venue`                                  | Venue                                                 | `boolean`    |     |       |                             |
| `job_title`                                 | Job Title                                             | `char`       |     |       |                             |
| `karma`                                     | Karma                                                 | `integer`    |     | ✅    |                             |
| `karma_tracking_ids`                        | Karma Changes                                         | `one2many`   |     | ✅    | gamification.karma.tracking |
| `km_home_work`                              | Home-Work Distance in Km                              | `integer`    |     |       |                             |
| `lang`                                      | Language                                              | `selection`  |     |       |                             |
| `leave_date_to`                             | To Date                                               | `date`       |     |       |                             |
| `livechat_channel_count`                    | Livechat Channel Count                                | `integer`    |     |       |                             |
| `livechat_channel_ids`                      | Livechat Channel                                      | `many2many`  |     | ✅    | im_livechat.channel         |
| `livechat_expertise_ids`                    | Live Chat Expertise                                   | `many2many`  |     |       | im_livechat.expertise       |
| `livechat_is_in_call`                       | Livechat Is In Call                                   | `boolean`    |     |       |                             |
| `livechat_lang_ids`                         | Livechat Languages                                    | `many2many`  |     |       | res.lang                    |
| `livechat_ongoing_session_count`            | Number of Ongoing sessions                            | `integer`    |     |       |                             |
| `livechat_username`                         | Livechat Username                                     | `char`       |     |       |                             |
| `log_ids`                                   | User log entries                                      | `one2many`   |     | ✅    | res.users.log               |
| `login`                                     | Login                                                 | `char`       | ✅  | ✅    |                             |
| `login_date`                                | Latest Login                                          | `datetime`   |     |       |                             |
| `logo_visible`                              | Show Company Logo in Sidebar                          | `boolean`    |     | ✅    |                             |
| `main_user_id`                              | Main User                                             | `many2one`   |     |       | res.users                   |
| `manual_im_status`                          | IM status manually set by the user                    | `selection`  |     | ✅    |                             |
| `meeting_count`                             | # Meetings                                            | `integer`    |     |       |                             |
| `meeting_ids`                               | Meetings                                              | `many2many`  |     |       | calendar.event              |
| `message_attachment_count`                  | Attachment Count                                      | `integer`    |     |       |                             |
| `message_bounce`                            | Bounce                                                | `integer`    |     |       |                             |
| `message_follower_ids`                      | Followers                                             | `one2many`   |     |       | mail.followers              |
| `message_has_error`                         | Message Delivery error                                | `boolean`    |     |       |                             |
| `message_has_error_counter`                 | Number of errors                                      | `integer`    |     |       |                             |
| `message_has_sms_error`                     | SMS Delivery error                                    | `boolean`    |     |       |                             |
| `message_ids`                               | Messages                                              | `one2many`   |     |       | mail.message                |
| `message_is_follower`                       | Is Follower                                           | `boolean`    |     |       |                             |
| `message_needaction`                        | Action Needed                                         | `boolean`    |     |       |                             |
| `message_needaction_counter`                | Number of Actions                                     | `integer`    |     |       |                             |
| `message_partner_ids`                       | Followers (Partners)                                  | `many2many`  |     |       | res.partner                 |
| `mobile_phone`                              | Work Mobile                                           | `char`       |     |       |                             |
| `monday_location_id`                        | Mondays                                               | `many2one`   |     |       | hr.work.location            |
| `my_activity_date_deadline`                 | My Activity Deadline                                  | `date`       |     |       |                             |
| `name`                                      | Name                                                  | `char`       |     |       |                             |
| `new_password`                              | Set Password                                          | `char`       |     |       |                             |
| `next_rank_id`                              | Next Rank                                             | `many2one`   |     | ✅    | gamification.karma.rank     |
| `notification_type`                         | Notification                                          | `selection`  | ✅  | ✅    |                             |
| `odoobot_failed`                            | Odoobot Failed                                        | `boolean`    |     | ✅    |                             |
| `odoobot_state`                             | OdooBot Status                                        | `selection`  |     | ✅    |                             |
| `offline_since`                             | Offline since                                         | `datetime`   |     |       |                             |
| `onesignal_device_id`                       | One Signal Device ID                                  | `char`       |     | ✅    |                             |
| `on_time_rate`                              | On-Time Delivery Rate                                 | `float`      |     |       |                             |
| `opportunity_count`                         | Opportunity Count                                     | `integer`    |     |       |                             |
| `opportunity_ids`                           | Opportunities                                         | `one2many`   |     |       | crm.lead                    |
| `outgoing_mail_server_id`                   | Outgoing Mail Server                                  | `many2one`   |     |       | ir.mail_server              |
| `outgoing_mail_server_type`                 | Outgoing Mail Server Type                             | `selection`  | ✅  |       |                             |
| `out_of_office_from`                        | Out Of Office From                                    | `datetime`   |     | ✅    |                             |
| `out_of_office_message`                     | Vacation Responder                                    | `html`       |     | ✅    |                             |
| `out_of_office_to`                          | Out Of Office To                                      | `datetime`   |     | ✅    |                             |
| `parent_id`                                 | Related Company                                       | `many2one`   |     |       | res.partner                 |
| `parent_name`                               | Parent name                                           | `char`       |     |       |                             |
| `partner_company_registry_placeholder`      | Partner Company Registry Placeholder                  | `char`       |     |       |                             |
| `partner_id`                                | Related Partner                                       | `many2one`   | ✅  | ✅    | res.partner                 |
| `partner_latitude`                          | Geo Latitude                                          | `float`      |     |       |                             |
| `partner_longitude`                         | Geo Longitude                                         | `float`      |     |       |                             |
| `partner_share`                             | Share Partner                                         | `boolean`    |     |       |                             |
| `partner_vat_placeholder`                   | Partner Vat Placeholder                               | `char`       |     |       |                             |
| `password`                                  | Password                                              | `char`       |     |       |                             |
| `payment_token_count`                       | Payment Token Count                                   | `integer`    |     |       |                             |
| `payment_token_ids`                         | Payment Tokens                                        | `one2many`   |     |       | payment.token               |
| `peppol_eas`                                | Peppol e-address (EAS)                                | `selection`  |     |       |                             |
| `peppol_endpoint`                           | Peppol Endpoint                                       | `char`       |     |       |                             |
| `phone`                                     | Phone                                                 | `char`       |     |       |                             |
| `phone_blacklisted`                         | Blacklisted Phone is Phone                            | `boolean`    |     |       |                             |
| `phone_mobile_search`                       | Phone Number                                          | `char`       |     |       |                             |
| `phone_sanitized`                           | Sanitized Number                                      | `char`       |     |       |                             |
| `phone_sanitized_blacklisted`               | Phone Blacklisted                                     | `boolean`    |     |       |                             |
| `picking_warn_msg`                          | Message for Stock Picking                             | `text`       |     |       |                             |
| `pin`                                       | PIN                                                   | `char`       |     |       |                             |
| `pin_whatsapp_contact_id`                   | Pin Whatsapp Contact                                  | `char`       |     | ✅    |                             |
| `placement_team_id`                         | Placement Team Members                                | `many2one`   |     | ✅    | op.placement.cell           |
| `presence_ids`                              | Presence                                              | `one2many`   |     | ✅    | mail.presence               |
| `private_city`                              | Private City                                          | `char`       |     |       |                             |
| `private_country_id`                        | Private Country                                       | `many2one`   |     |       | res.country                 |
| `private_email`                             | Private Email                                         | `char`       |     |       |                             |
| `private_phone`                             | Private Phone                                         | `char`       |     |       |                             |
| `private_state_id`                          | Private State                                         | `many2one`   |     |       | res.country.state           |
| `private_street`                            | Private Street                                        | `char`       |     |       |                             |
| `private_street2`                           | Private Street2                                       | `char`       |     |       |                             |
| `private_zip`                               | Private Zip                                           | `char`       |     |       |                             |
| `properties`                                | Properties                                            | `properties` |     |       |                             |
| `properties_base_definition_id`             | Properties Base Definition                            | `many2one`   |     |       | properties.base.definition  |
| `property_account_payable_id`               | Account Payable                                       | `many2one`   |     |       | account.account             |
| `property_account_position_id`              | Fiscal Position                                       | `many2one`   |     |       | account.fiscal.position     |
| `property_account_receivable_id`            | Account Receivable                                    | `many2one`   |     |       | account.account             |
| `property_delivery_carrier_id`              | Delivery Method                                       | `many2one`   |     |       | delivery.carrier            |
| `property_inbound_payment_method_line_id`   | Property Inbound Payment Method Line                  | `many2one`   |     |       | account.payment.method.line |
| `property_outbound_payment_method_line_id`  | Property Outbound Payment Method Line                 | `many2one`   |     |       | account.payment.method.line |
| `property_payment_term_id`                  | Customer Payment Terms                                | `many2one`   |     |       | account.payment.term        |
| `property_product_pricelist`                | Pricelist                                             | `many2one`   |     |       | product.pricelist           |
| `property_purchase_currency_id`             | Supplier Currency                                     | `many2one`   |     |       | res.currency                |
| `property_stock_customer`                   | Customer Location                                     | `many2one`   |     |       | stock.location              |
| `property_stock_supplier`                   | Vendor Location                                       | `many2one`   |     |       | stock.location              |
| `property_supplier_payment_term_id`         | Vendor Payment Terms                                  | `many2one`   |     |       | account.payment.term        |
| `property_warehouse_id`                     | Default Warehouse                                     | `many2one`   |     | ✅    | stock.warehouse             |
| `purchase_line_ids`                         | Purchase Lines                                        | `one2many`   |     |       | purchase.order.line         |
| `purchase_order_count`                      | Purchase Order Count                                  | `integer`    |     |       |                             |
| `purchase_warn_msg`                         | Message for Purchase Order                            | `text`       |     |       |                             |
| `rank_id`                                   | Rank                                                  | `many2one`   |     | ✅    | gamification.karma.rank     |
| `rating_ids`                                | Ratings                                               | `one2many`   |     |       | rating.rating               |
| `receipt_reminder_email`                    | Receipt Reminder                                      | `boolean`    |     |       |                             |
| `ref`                                       | Reference                                             | `char`       |     |       |                             |
| `ref_company_ids`                           | Companies that refers to partner                      | `one2many`   |     |       | res.company                 |
| `refresh_token`                             | Refresh Token                                         | `char`       |     | ✅    |                             |
| `reminder_date_before_receipt`              | Days Before Receipt                                   | `integer`    |     |       |                             |
| `resource_calendar_id`                      | Default Working Hours                                 | `many2one`   |     |       | resource.calendar           |
| `resource_ids`                              | Resources                                             | `one2many`   |     | ✅    | resource.resource           |
| `res_users_settings_id`                     | Settings                                              | `many2one`   |     |       | res.users.settings          |
| `res_users_settings_ids`                    | Res Users Settings                                    | `one2many`   |     | ✅    | res.users.settings          |
| `role`                                      | Role                                                  | `selection`  |     |       |                             |
| `role_ids`                                  | User Roles                                            | `many2many`  |     | ✅    | res.role                    |
| `role_line_ids`                             | Role lines                                            | `one2many`   |     | ✅    | res.users.role.line         |
| `rtc_session_ids`                           | Rtc Session                                           | `one2many`   |     |       | discuss.channel.rtc.session |
| `rules_count`                               | # Record Rules                                        | `integer`    |     |       |                             |
| `sale_order_count`                          | Sale Order Count                                      | `integer`    |     |       |                             |
| `sale_order_ids`                            | Sales Order                                           | `one2many`   |     |       | sale.order                  |
| `sale_team_id`                              | User Sales Team                                       | `many2one`   |     | ✅    | crm.team                    |
| `sale_warn_msg`                             | Message for Sales Order                               | `text`       |     |       |                             |
| `same_company_registry_partner_id`          | Partner with same Company Registry                    | `many2one`   |     |       | res.partner                 |
| `same_vat_partner_id`                       | Partner with same Tax ID                              | `many2one`   |     |       | res.partner                 |
| `saturday_location_id`                      | Saturdays                                             | `many2one`   |     |       | hr.work.location            |
| `self`                                      | Self                                                  | `many2one`   |     |       | res.partner                 |
| `seo_name`                                  | Seo name                                              | `char`       |     |       |                             |
| `share`                                     | Share User                                            | `boolean`    |     | ✅    |                             |
| `show_alert`                                | Show Alert                                            | `boolean`    |     |       |                             |
| `show_credit_limit`                         | Show Credit Limit                                     | `boolean`    |     |       |                             |
| `signature`                                 | Email Signature                                       | `html`       |     | ✅    |                             |
| `signup_type`                               | Signup Token Type                                     | `char`       |     |       |                             |
| `silver_badge`                              | Silver badges count                                   | `integer`    |     |       |                             |
| `specific_property_product_pricelist`       | Specific Property Product Pricelist                   | `many2one`   |     |       | product.pricelist           |
| `state`                                     | Status                                                | `selection`  |     |       |                             |
| `state_id`                                  | State                                                 | `many2one`   |     |       | res.country.state           |
| `static_map_url`                            | Static Map Url                                        | `char`       |     |       |                             |
| `static_map_url_is_valid`                   | Static Map Url Is Valid                               | `boolean`    |     |       |                             |
| `street`                                    | Street                                                | `char`       |     |       |                             |
| `street2`                                   | Street2                                               | `char`       |     |       |                             |
| `student_line`                              | Line                                                  | `many2one`   |     | ✅    | op.student                  |
| `suggest_based_on`                          | Suggest Based On                                      | `char`       |     |       |                             |
| `suggest_days`                              | Suggest Days                                          | `integer`    |     |       |                             |
| `suggest_percent`                           | Suggest Percent                                       | `integer`    |     |       |                             |
| `sunday_location_id`                        | Sundays                                               | `many2one`   |     |       | hr.work.location            |
| `supplier_invoice_count`                    | # Vendor Bills                                        | `integer`    |     |       |                             |
| `supplier_rank`                             | Supplier Rank                                         | `integer`    |     |       |                             |
| `thursday_location_id`                      | Thursdays                                             | `many2one`   |     |       | hr.work.location            |
| `ticket_count`                              | Ticket Count                                          | `integer`    |     |       |                             |
| `title`                                     | Title                                                 | `many2one`   |     |       | res.partner.title           |
| `total_invoiced`                            | Total Invoiced                                        | `monetary`   |     |       |                             |
| `totp_enabled`                              | Two-factor authentication                             | `boolean`    |     |       |                             |
| `totp_last_counter`                         | Totp Last Counter                                     | `integer`    |     | ✅    |                             |
| `totp_secret`                               | Totp Secret                                           | `char`       |     |       |                             |
| `totp_trusted_device_ids`                   | Trusted Devices                                       | `one2many`   |     | ✅    | auth_totp.device            |
| `tour_enabled`                              | Onboarding                                            | `boolean`    |     | ✅    |                             |
| `trust`                                     | Degree of trust you have in this debtor               | `selection`  |     |       |                             |
| `tuesday_location_id`                       | Tuesdays                                              | `many2one`   |     |       | hr.work.location            |
| `type`                                      | Address Type                                          | `selection`  |     |       |                             |
| `type_address_label`                        | Address Type Description                              | `char`       |     |       |                             |
| `tz`                                        | Timezone                                              | `selection`  |     |       |                             |
| `tz_offset`                                 | Timezone offset                                       | `char`       |     |       |                             |
| `use_partner_credit_limit`                  | Partner Limit                                         | `boolean`    |     |       |                             |
| `user_id`                                   | Salesperson                                           | `many2one`   |     |       | res.users                   |
| `user_ids`                                  | Users                                                 | `one2many`   |     |       | res.users                   |
| `user_line`                                 | User Line                                             | `one2many`   |     | ✅    | op.student                  |
| `user_livechat_username`                    | User Livechat Username                                | `char`       |     |       |                             |
| `vat`                                       | Tax ID                                                | `char`       |     |       |                             |
| `vat_label`                                 | Tax ID Label                                          | `char`       |     |       |                             |
| `view_group_hierarchy`                      | Technical field for user group setting                | `json`       |     |       |                             |
| `visa_expire`                               | Visa Expiration Date                                  | `date`       |     |       |                             |
| `visitor_ids`                               | Visitors                                              | `one2many`   |     |       | website.visitor             |
| `website`                                   | Website Link                                          | `char`       |     |       |                             |
| `website_absolute_url`                      | Website Absolute URL                                  | `char`       |     |       |                             |
| `website_description`                       | Website Partner Full Description                      | `html`       |     |       |                             |
| `website_id`                                | Website                                               | `many2one`   |     | ✅    | website                     |
| `website_message_ids`                       | Website Messages                                      | `one2many`   |     |       | mail.message                |
| `website_meta_description`                  | Website meta description                              | `text`       |     |       |                             |
| `website_meta_keywords`                     | Website meta keywords                                 | `char`       |     |       |                             |
| `website_meta_og_img`                       | Website opengraph image                               | `char`       |     |       |                             |
| `website_meta_title`                        | Website meta title                                    | `char`       |     |       |                             |
| `website_published`                         | Visible on current website                            | `boolean`    |     |       |                             |
| `website_short_description`                 | Website Partner Short Description                     | `text`       |     |       |                             |
| `website_url`                               | Website URL                                           | `char`       |     |       |                             |
| `wednesday_location_id`                     | Wednesdays                                            | `many2one`   |     |       | hr.work.location            |
| `wishlist_ids`                              | Wishlist                                              | `one2many`   |     |       | product.wishlist            |
| `work_contact_id`                           | Work Contact                                          | `many2one`   |     |       | res.partner                 |
| `work_email`                                | Work Email                                            | `char`       |     |       |                             |
| `work_location_id`                          | Work Location                                         | `many2one`   |     |       | hr.work.location            |
| `work_location_name`                        | Work Location Name                                    | `char`       |     |       |                             |
| `work_location_type`                        | Work Location Type                                    | `selection`  |     |       |                             |
| `work_phone`                                | Work Phone                                            | `char`       |     |       |                             |
| `write_date`                                | Last Updated on                                       | `datetime`   |     | ✅    |                             |
| `write_uid`                                 | Last Updated by                                       | `many2one`   |     | ✅    | res.users                   |
| `zip`                                       | Zip                                                   | `char`       |     |       |                             |

**Access Rights:**

| Name                             | Group            | Perms     |
| -------------------------------- | ---------------- | --------- |
| access_op_placement_cell_res     | Placement / User | `R/W/C`   |
| name_res_users_back_office_admin | Parent / Manager | `R/W/C/D` |
| res_users group_erp_manager      | Access Rights    | `R/W/C/D` |
| res_users all                    | Role / Portal    | `R`       |
| res_users all                    | Role / Public    | `R`       |
| res_users all                    | Role / User      | `R`       |

**Record Rules:**

- **user rule** (Global) `R/W/C/D`
  - Domain: `['|', ('share', '=', False), ('company_ids', 'in', company_ids)]`
- **portal user access** (10) `R/W/C/D`
  - Domain: `[('commercial_partner_id', '=', user.commercial_partner_id.id)]`

### 🗃️ `res.users.settings` — User Settings

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                      | Label                                     | Type        | Req | Store | Relation                           |
| ------------------------------------------ | ----------------------------------------- | ----------- | --- | ----- | ---------------------------------- |
| `calendar_default_privacy`                 | Calendar Default Privacy                  | `selection` | ✅  | ✅    |                                    |
| `channel_notifications`                    | Channel Notifications                     | `selection` |     | ✅    |                                    |
| `create_date`                              | Created on                                | `datetime`  |     | ✅    |                                    |
| `create_uid`                               | Created by                                | `many2one`  |     | ✅    | res.users                          |
| `display_name`                             | Display Name                              | `char`      |     |       |                                    |
| `embedded_actions_config_ids`              | Embedded Actions Config                   | `one2many`  |     | ✅    | res.users.settings.embedded.action |
| `id`                                       | ID                                        | `integer`   |     | ✅    |                                    |
| `is_discuss_sidebar_category_channel_open` | Is discuss sidebar category channel open? | `boolean`   |     | ✅    |                                    |
| `is_discuss_sidebar_category_chat_open`    | Is discuss sidebar category chat open?    | `boolean`   |     | ✅    |                                    |
| `livechat_expertise_ids`                   | Live Chat Expertise                       | `many2many` |     | ✅    | im_livechat.expertise              |
| `livechat_lang_ids`                        | Livechat languages                        | `many2many` |     | ✅    | res.lang                           |
| `livechat_username`                        | Livechat Username                         | `char`      |     | ✅    |                                    |
| `push_to_talk_key`                         | Push-To-Talk shortcut                     | `char`      |     | ✅    |                                    |
| `use_push_to_talk`                         | Use the push to talk feature              | `boolean`   |     | ✅    |                                    |
| `user_id`                                  | User                                      | `many2one`  | ✅  | ✅    | res.users                          |
| `voice_active_duration`                    | Duration of voice activity in ms          | `integer`   |     | ✅    |                                    |
| `volume_settings_ids`                      | Volumes of other partners                 | `one2many`  |     | ✅    | res.users.settings.volumes         |
| `write_date`                               | Last Updated on                           | `datetime`  |     | ✅    |                                    |
| `write_uid`                                | Last Updated by                           | `many2one`  |     | ✅    | res.users                          |

**Access Rights:**

| Name               | Group       | Perms     |
| ------------------ | ----------- | --------- |
| res.users.settings | Role / User | `R/W/C/D` |
| res.users.settings | Everyone    | `-`       |

**Record Rules:**

- **Administrators can access all User Settings.** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **res.users.settings: access their own entries** (1) `R/W/C/D`
  - Domain: `[('user_id', '=', user.id)]`
