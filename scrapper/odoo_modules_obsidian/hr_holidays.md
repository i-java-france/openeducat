---
title: "Time Off"
module: "hr_holidays"
state: "installed"
version: "19.0.1.6"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/app/time-off"
license: "LGPL-3"
category: "Time Off"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/________, odoo/app]
---

# 🟢 Time Off

> **Module:** `hr_holidays` | **Version:** `19.0.1.6` **Category:** Time Off |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:**
> https://www.odoo.com/app/time-off

## 🔗 Dependencies

[[hr]] [[calendar]] [[resource]]

## 📖 Description

# Manage time off requests and allocations

This application controls the time off schedule of your company. It allows employees to
request time off. Then, managers can review requests for time off and approve or reject
them. This way you can control the overall time off planning for the company or
department.

You can configure several kinds of time off (sickness, paid days, ...) and allocate time
off to an employee or department quickly using time off allocation. An employee can also
make a request for more days off by making a new time off allocation. It will increase
the total of available days for that time off type (if the request is accepted).

You can keep track of time off in different ways by following reports:

- Time Off Summary
- Time Off by Department
- Time Off Analysis

A synchronization with an internal agenda (Meetings of the CRM module) is also possible
in order to automatically create a meeting when a time off request is accepted by
setting up a type of meeting in time off Type.

## 🖥️ UI Components

### Menus

- `Time Off`
- `Time Off/Configuration`
- `Time Off/Configuration/Accrual Plans`
- `Time Off/Configuration/Activity Types`
- `Time Off/Configuration/Mandatory Days`
- `Time Off/Configuration/Public Holidays`
- `Time Off/Configuration/Time Off Types`
- `Time Off/Management`
- `Time Off/Management/Allocations`
- `Time Off/Management/Time Off`
- `Time Off/My Time`
- `Time Off/My Time/Dashboard`
- `Time Off/My Time/My Allocations`
- `Time Off/My Time/My Time Off`
- `Time Off/Overview`
- `Time Off/Reporting`
- `Time Off/Reporting/Balance`
- `Time Off/Reporting/by Employee`
- `Time Off/Reporting/by Type`

### Views

- `* INHERIT hr.department.kanban.inherit (kanban)`
- `* INHERIT hr.employee.kanban.leaves.status (kanban)`
- `* INHERIT hr.employee.leave.form.inherit (form)`
- `* INHERIT hr.employee.list.leave (list)`
- `* INHERIT hr.employee.public.kanban.leaves.status (kanban)`
- `* INHERIT hr.employee.public.leave.form.inherit (form)`
- `* INHERIT hr.employee.search.view.inherit (search)`
- `* INHERIT hr.holidays.view.list (list)`
- `* INHERIT hr.holidays.view.search.manager (search)`
- `* INHERIT hr.holidays.view.search.my (search)`
- `* INHERIT hr.holidays.view.search.report (search)`
- `* INHERIT hr.leave.allocation.view.form.manager (form)`
- `* INHERIT hr.leave.allocation.view.form.manager.dashboard (form)`
- `* INHERIT hr.leave.allocation.view.list.my (list)`
- `* INHERIT hr.leave.allocation.view.search.my (search)`
- `* INHERIT hr.leave.allocation.view.search.my (search)`
- `* INHERIT hr.leave.view.form.dashboard (form)`
- `* INHERIT hr.leave.view.form.dashboard (form)`
- `* INHERIT hr.leave.view.form.dashboard.new.time.off (form)`
- `* INHERIT hr.leave.view.form.dashboard.new.time.off (form)`
- `* INHERIT hr.leave.view.form.manager (form)`
- `* INHERIT hr.leave.view.kanban.my (kanban)`
- `* INHERIT resource.calendar.form.inherit (form)`
- `* INHERIT resource.calendar.leaves.form.inherit (form)`
- `* INHERIT resource.calendar.leaves.list.inherit (list)`
- `* INHERIT resource.calendar.leaves.search.inherit (search)`
- `* INHERIT resource.calendar.view.list.inherit.hr.holidays (list)`
- `* INHERIT view.calendar.event.form.inherit (form)`
- `hr.holidays.cancel.leave form (form)`
- `hr.holidays.filter (search)`
- `hr.holidays.filter (search)`
- `hr.holidays.filter (search)`
- `hr.holidays.filter_allocations (search)`
- `hr.holidays.graph (graph)`
- `hr.holidays.report_graph (graph)`
- `hr.holidays.report_list (list)`
- `hr.holidays.report_pivot (pivot)`
- `hr.holidays.summary.employee.form (form)`
- `hr.holidays.view.list (list)`
- `hr.leave.accrual.level.form (form)`
- `hr.leave.accrual.plan.form (form)`
- `hr.leave.accrual.plan.list (list)`
- `hr.leave.accrual.plan.search (search)`
- `hr.leave.allocation.generate.multi.wizard form (form)`
- `hr.leave.allocation.view.activity (activity)`
- `hr.leave.allocation.view.form (form)`
- `hr.leave.allocation.view.kanban (kanban)`
- `hr.leave.allocation.view.list (list)`
- `hr.leave.employee.type.report.view.pivot (pivot)`
- `hr.leave.generate.multi.wizard form (form)`
- `hr.leave.mandatory.day form (form)`
- `hr.leave.mandatory.day list (list)`
- `hr.leave.mandatory.day search (search)`
- `hr.leave.report.calendar.view (calendar)`
- `hr.leave.report.calendar.view.form (form)`
- `hr.leave.report.calendar.view.search (search)`
- `hr.leave.report.calendar.year.view (calendar)`
- `hr.leave.type.filter (search)`
- `hr.leave.type.form (form)`
- `hr.leave.type.kanban (kanban)`
- `hr.leave.type.normal.list (list)`
- `hr.leave.view.activity (activity)`
- `hr.leave.view.calendar (calendar)`
- `hr.leave.view.dashboard (calendar)`
- `hr.leave.view.dashboard (calendar)`
- `hr.leave.view.form (form)`
- `hr.leave.view.kanban (kanban)`
- `report.hr.holidays.report.leave_all.graph (graph)`
- `report.hr.holidays.report.leave_all.list (list)`
- `report.hr.holidays.report.leave_all.pivot (pivot)`
- `report_holidayssummary (qweb)`

### Reports

- `Time Off Summary`

## 🛠️ Technical Documentation

**27 model(s) defined by this module:**

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

### 🗃️ `hr.department` — Department

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
| `absence_of_today`              | Absence by Today              | `integer`   |     |       |                    |
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
| `allocation_to_approve_count`   | Allocation to Approve         | `integer`   |     |       |                    |
| `child_ids`                     | Child Departments             | `one2many`  |     | ✅    | hr.department      |
| `color`                         | Color Index                   | `integer`   |     | ✅    |                    |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company        |
| `complete_name`                 | Complete Name                 | `char`      |     |       |                    |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `expected_employee`             | Expected Employee             | `integer`   |     |       |                    |
| `expenses_to_approve_count`     | Expenses to Approve           | `integer`   |     |       |                    |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `has_read_access`               | Has Read Access               | `boolean`   |     |       |                    |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
| `jobs_ids`                      | Jobs                          | `one2many`  |     | ✅    | hr.job             |
| `leave_to_approve_count`        | Time Off to Approve           | `integer`   |     |       |                    |
| `manager_id`                    | Manager                       | `many2one`  |     | ✅    | hr.employee        |
| `master_department_id`          | Master Department             | `many2one`  |     | ✅    | hr.department      |
| `member_ids`                    | Members                       | `one2many`  |     | ✅    | hr.employee        |
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
| `name`                          | Department Name               | `char`      | ✅  | ✅    |                    |
| `new_applicant_count`           | New Applicant                 | `integer`   |     |       |                    |
| `new_hired_employee`            | New Hired Employee            | `integer`   |     |       |                    |
| `note`                          | Note                          | `text`      |     | ✅    |                    |
| `parent_id`                     | Parent Department             | `many2one`  |     | ✅    | hr.department      |
| `parent_path`                   | Parent Path                   | `char`      |     | ✅    |                    |
| `plan_ids`                      | Plan                          | `one2many`  |     | ✅    | mail.activity.plan |
| `plans_count`                   | Plans Count                   | `integer`   |     |       |                    |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `total_employee`                | Total Employee                | `integer`   |     |       |                    |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                   | Group                                     | Perms     |
| ---------------------- | ----------------------------------------- | --------- |
| hr.department.user     | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.department.public   | Role / Public                             | `R`       |
| hr.department.employee | Role / User                               | `R`       |

**Record Rules:**

- **Department multi company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Job department: Public** (11) `R`
  - Domain:
    `['|', ('jobs_ids.website_published', '=', True), ('child_ids', 'not in', [])]`

### 🗃️ `hr.employee` — Employee

> 📧 Mail Thread

    NB: Any field only available on the model hr.employee (i.e. not on the
    hr.employee.public model) should have `groups="hr.group_hr_user"` on its
    definition to avoid being prefetched when the user hasn't access to the
    hr.employee model. Indeed, the prefetch loads the data for all the fields
    that are available according to the group defined on them.

**Fields:**

| Field                            | Label                           | Type         | Req | Store | Relation                  |
| -------------------------------- | ------------------------------- | ------------ | --- | ----- | ------------------------- |
| `active`                         | Active                          | `boolean`    |     | ✅    |                           |
| `active_employee`                | Active Employee                 | `boolean`    |     |       |                           |
| `activity_calendar_event_id`     | Next Activity Calendar Event    | `many2one`   |     |       | calendar.event            |
| `activity_date_deadline`         | Next Activity Deadline          | `date`       |     |       |                           |
| `activity_exception_decoration`  | Activity Exception Decoration   | `selection`  |     |       |                           |
| `activity_exception_icon`        | Icon                            | `char`       |     |       |                           |
| `activity_ids`                   | Activities                      | `one2many`   |     | ✅    | mail.activity             |
| `activity_state`                 | Activity State                  | `selection`  |     |       |                           |
| `activity_summary`               | Next Activity Summary           | `char`       |     |       |                           |
| `activity_type_icon`             | Activity Type Icon              | `char`       |     |       |                           |
| `activity_type_id`               | Next Activity Type              | `many2one`   |     |       | mail.activity.type        |
| `activity_user_id`               | Responsible User                | `many2one`   |     |       | res.users                 |
| `additional_note`                | Additional Note                 | `text`       |     |       |                           |
| `address_id`                     | Work Address                    | `many2one`   |     |       | res.partner               |
| `allocation_count`               | Total number of days allocated. | `float`      |     |       |                           |
| `allocation_display`             | Allocation Display              | `char`       |     |       |                           |
| `allocation_remaining_display`   | Allocation Remaining Display    | `char`       |     |       |                           |
| `allocations_count`              | Total number of allocations     | `integer`    |     |       |                           |
| `allowed_country_state_ids`      | Allowed Country State           | `many2many`  |     |       | res.country.state         |
| `applicant_ids`                  | Applicants                      | `one2many`   |     | ✅    | hr.applicant              |
| `avatar_1024`                    | Avatar 1024                     | `binary`     |     |       |                           |
| `avatar_128`                     | Avatar 128                      | `binary`     |     |       |                           |
| `avatar_1920`                    | Avatar                          | `binary`     |     |       |                           |
| `avatar_256`                     | Avatar 256                      | `binary`     |     |       |                           |
| `avatar_512`                     | Avatar 512                      | `binary`     |     |       |                           |
| `badge_ids`                      | Employee Badges                 | `one2many`   |     |       | gamification.badge.user   |
| `bank_account_ids`               | Bank Accounts                   | `many2many`  |     | ✅    | res.partner.bank          |
| `barcode`                        | Badge ID                        | `char`       |     | ✅    |                           |
| `birthday`                       | Birthday                        | `date`       |     | ✅    |                           |
| `birthday_public_display`        | Show to all employees           | `boolean`    |     | ✅    |                           |
| `birthday_public_display_string` | Public Date of Birth            | `char`       |     |       |                           |
| `car_ids`                        | Vehicles (private)              | `one2many`   |     | ✅    | fleet.vehicle             |
| `category_ids`                   | Tags                            | `many2many`  |     | ✅    | hr.employee.category      |
| `certificate`                    | Certificate Level               | `selection`  |     | ✅    |                           |
| `certification_ids`              | Certification                   | `one2many`   |     |       | hr.employee.skill         |
| `child_all_count`                | Indirect Subordinates Count     | `integer`    |     |       |                           |
| `child_count`                    | Direct Subordinates Count       | `integer`    |     |       |                           |
| `child_ids`                      | Direct subordinates             | `one2many`   |     | ✅    | hr.employee               |
| `children`                       | Dependent Children              | `integer`    |     |       |                           |
| `coach_id`                       | Coach                           | `many2one`   |     | ✅    | hr.employee               |
| `color`                          | Color Index                     | `integer`    |     | ✅    |                           |
| `company_country_code`           | Company Country Code            | `char`       |     |       |                           |
| `company_country_id`             | Company Country                 | `many2one`   |     |       | res.country               |
| `company_id`                     | Company                         | `many2one`   | ✅  | ✅    | res.company               |
| `contract_date_end`              | Contract End Date               | `date`       |     |       |                           |
| `contract_date_start`            | Contract Start Date             | `date`       |     |       |                           |
| `contract_template_id`           | Contract Template               | `many2one`   |     |       | hr.version                |
| `contract_type_id`               | Contract Type                   | `many2one`   |     |       | hr.contract.type          |
| `contract_wage`                  | Contract Wage                   | `monetary`   |     |       |                           |
| `country_code`                   | Country Code                    | `char`       |     |       |                           |
| `country_id`                     | Nationality (Country)           | `many2one`   |     |       | res.country               |
| `country_of_birth`               | Country of Birth                | `many2one`   |     | ✅    | res.country               |
| `create_date`                    | Created on                      | `datetime`   |     | ✅    |                           |
| `create_uid`                     | Created by                      | `many2one`   |     | ✅    | res.users                 |
| `currency_id`                    | Currency                        | `many2one`   |     |       | res.currency              |
| `current_date_version`           | Current Date Version            | `date`       |     |       |                           |
| `current_employee_skill_ids`     | Current Employee Skill          | `one2many`   |     |       | hr.employee.skill         |
| `current_leave_id`               | Current Time Off Type           | `many2one`   |     |       | hr.leave.type             |
| `current_leave_state`            | Current Time Off Status         | `selection`  |     |       |                           |
| `current_version_id`             | Current Version                 | `many2one`   |     | ✅    | hr.version                |
| `date_end`                       | Date End                        | `date`       |     |       |                           |
| `date_start`                     | Date Start                      | `date`       |     |       |                           |
| `date_version`                   | Date Version                    | `date`       | ✅  |       |                           |
| `department_color`               | Department Color                | `integer`    |     |       |                           |
| `department_id`                  | Department                      | `many2one`   |     |       | hr.department             |
| `departure_date`                 | Departure Date                  | `date`       |     |       |                           |
| `departure_description`          | Additional Information          | `html`       |     |       |                           |
| `departure_reason_id`            | Departure Reason                | `many2one`   |     |       | hr.departure.reason       |
| `direct_badge_ids`               | Direct Badge                    | `one2many`   |     | ✅    | gamification.badge.user   |
| `display_certification_page`     | Display Certification Page      | `boolean`    |     |       |                           |
| `display_name`                   | Display Name                    | `char`       |     |       |                           |
| `distance_home_work`             | Home-Work Distance              | `integer`    |     |       |                           |
| `distance_home_work_unit`        | Home-Work Distance unit         | `selection`  | ✅  |       |                           |
| `driving_license`                | Driving License                 | `binary`     |     | ✅    |                           |
| `email`                          | Email                           | `char`       |     |       |                           |
| `emergency_contact`              | Emergency Contact               | `char`       |     | ✅    |                           |
| `emergency_phone`                | Emergency Phone                 | `char`       |     | ✅    |                           |
| `employee_cars_count`            | Cars                            | `integer`    |     |       |                           |
| `employee_id`                    | Employee                        | `many2one`   |     |       | hr.employee               |
| `employee_properties`            | Properties                      | `properties` |     | ✅    |                           |
| `employee_skill_ids`             | Skills                          | `one2many`   |     | ✅    | hr.employee.skill         |
| `employee_type`                  | Employee Type                   | `selection`  | ✅  |       |                           |
| `exceptional_location_id`        | Current                         | `many2one`   |     |       | hr.work.location          |
| `expense_manager_id`             | Expense Approver                | `many2one`   |     | ✅    | res.users                 |
| `filter_for_expense`             | Filter For Expense              | `boolean`    |     |       |                           |
| `friday_location_id`             | Friday                          | `many2one`   |     | ✅    | hr.work.location          |
| `goal_ids`                       | Employee HR Goals               | `one2many`   |     |       | gamification.goal         |
| `has_badges`                     | Has Badges                      | `boolean`    |     |       |                           |
| `has_message`                    | Has Message                     | `boolean`    |     |       |                           |
| `has_multiple_bank_accounts`     | Has Multiple Bank Accounts      | `boolean`    |     |       |                           |
| `has_work_permit`                | Work Permit                     | `binary`     |     | ✅    |                           |
| `hr_icon_display`                | Hr Icon Display                 | `selection`  |     |       |                           |
| `hr_presence_state`              | Hr Presence State               | `selection`  |     |       |                           |
| `hr_responsible_id`              | HR Responsible                  | `many2one`   | ✅  |       | res.users                 |
| `id`                             | ID                              | `integer`    |     | ✅    |                           |
| `id_card`                        | ID Card Copy                    | `binary`     |     | ✅    |                           |
| `identification_id`              | Identification No               | `char`       |     |       |                           |
| `image_1024`                     | Image 1024                      | `binary`     |     | ✅    |                           |
| `image_128`                      | Image 128                       | `binary`     |     | ✅    |                           |
| `image_1920`                     | Image                           | `binary`     |     | ✅    |                           |
| `image_256`                      | Image 256                       | `binary`     |     | ✅    |                           |
| `image_512`                      | Image 512                       | `binary`     |     | ✅    |                           |
| `im_status`                      | IM Status                       | `char`       |     |       |                           |
| `is_absent`                      | Absent Today                    | `boolean`    |     |       |                           |
| `is_current`                     | Is Current                      | `boolean`    |     |       |                           |
| `is_custom_job_title`            | Is Custom Job Title             | `boolean`    |     |       |                           |
| `is_flexible`                    | Is Flexible                     | `boolean`    |     |       |                           |
| `is_fully_flexible`              | Is Fully Flexible               | `boolean`    |     |       |                           |
| `is_future`                      | Is Future                       | `boolean`    |     |       |                           |
| `is_in_contract`                 | Is In Contract                  | `boolean`    |     |       |                           |
| `is_past`                        | Is Past                         | `boolean`    |     |       |                           |
| `is_subordinate`                 | Is Subordinate                  | `boolean`    |     |       |                           |
| `is_trusted_bank_account`        | Is Trusted Bank Account         | `boolean`    |     |       |                           |
| `is_user_active`                 | User's active                   | `boolean`    |     |       |                           |
| `job_id`                         | Job                             | `many2one`   |     |       | hr.job                    |
| `job_title`                      | Job Title                       | `char`       |     |       |                           |
| `km_home_work`                   | Home-Work Distance in Km        | `integer`    |     |       |                           |
| `lang`                           | Lang                            | `selection`  |     | ✅    |                           |
| `last_activity`                  | Last Activity                   | `date`       |     |       |                           |
| `last_activity_time`             | Last Activity Time              | `char`       |     |       |                           |
| `last_modified_date`             | Last Modified on                | `datetime`   | ✅  |       |                           |
| `last_modified_uid`              | Last Modified by                | `many2one`   | ✅  |       | res.users                 |
| `leave_date_from`                | From Date                       | `date`       |     |       |                           |
| `leave_date_to`                  | To Date                         | `date`       |     |       |                           |
| `leave_manager_id`               | Time Off Approver               | `many2one`   |     | ✅    | res.users                 |
| `legal_name`                     | Legal Name                      | `char`       |     | ✅    |                           |
| `license_plate`                  | License Plate                   | `char`       |     |       |                           |
| `marital`                        | Marital Status                  | `selection`  | ✅  |       |                           |
| `member_of_department`           | Member of department            | `boolean`    |     |       |                           |
| `message_attachment_count`       | Attachment Count                | `integer`    |     |       |                           |
| `message_follower_ids`           | Followers                       | `one2many`   |     | ✅    | mail.followers            |
| `message_has_error`              | Message Delivery error          | `boolean`    |     |       |                           |
| `message_has_error_counter`      | Number of errors                | `integer`    |     |       |                           |
| `message_has_sms_error`          | SMS Delivery error              | `boolean`    |     |       |                           |
| `message_ids`                    | Messages                        | `one2many`   |     | ✅    | mail.message              |
| `message_is_follower`            | Is Follower                     | `boolean`    |     |       |                           |
| `message_main_attachment_id`     | Main Attachment                 | `many2one`   |     | ✅    | ir.attachment             |
| `message_needaction`             | Action Needed                   | `boolean`    |     |       |                           |
| `message_needaction_counter`     | Number of Actions               | `integer`    |     |       |                           |
| `message_partner_ids`            | Followers (Partners)            | `many2many`  |     |       | res.partner               |
| `mobile_phone`                   | Work Mobile                     | `char`       |     | ✅    |                           |
| `mobility_card`                  | Mobility Card                   | `char`       |     | ✅    |                           |
| `monday_location_id`             | Monday                          | `many2one`   |     | ✅    | hr.work.location          |
| `my_activity_date_deadline`      | My Activity Deadline            | `date`       |     |       |                           |
| `name`                           | Employee Name                   | `char`       |     | ✅    |                           |
| `newly_hired`                    | Newly Hired                     | `boolean`    |     |       |                           |
| `parent_id`                      | Manager                         | `many2one`   |     | ✅    | hr.employee               |
| `passport_expiration_date`       | Passport Expiration Date        | `date`       |     |       |                           |
| `passport_id`                    | Passport No                     | `char`       |     |       |                           |
| `permit_no`                      | Work Permit No                  | `char`       |     | ✅    |                           |
| `phone`                          | Phone                           | `char`       |     |       |                           |
| `pin`                            | PIN                             | `char`       |     | ✅    |                           |
| `place_of_birth`                 | Place of Birth                  | `char`       |     | ✅    |                           |
| `primary_bank_account_id`        | Primary Bank Account            | `many2one`   |     |       | res.partner.bank          |
| `private_car_plate`              | Private Car Plate               | `char`       |     | ✅    |                           |
| `private_city`                   | Private City                    | `char`       |     |       |                           |
| `private_country_id`             | Private Country                 | `many2one`   |     |       | res.country               |
| `private_email`                  | Private Email                   | `char`       |     | ✅    |                           |
| `private_phone`                  | Private Phone                   | `char`       |     | ✅    |                           |
| `private_state_id`               | Private State                   | `many2one`   |     |       | res.country.state         |
| `private_street`                 | Private Street                  | `char`       |     |       |                           |
| `private_street2`                | Private Street2                 | `char`       |     |       |                           |
| `private_zip`                    | Private Zip                     | `char`       |     |       |                           |
| `rating_ids`                     | Ratings                         | `one2many`   |     | ✅    | rating.rating             |
| `related_partners_count`         | Related Partners Count          | `integer`    |     |       |                           |
| `resource_calendar_id`           | Default Working Hours           | `many2one`   |     |       | resource.calendar         |
| `resource_id`                    | Resource                        | `many2one`   | ✅  | ✅    | resource.resource         |
| `resume_line_ids`                | Resume lines                    | `one2many`   |     | ✅    | hr.resume.line            |
| `salary_distribution`            | Salary Distribution             | `json`       |     | ✅    |                           |
| `saturday_location_id`           | Saturday                        | `many2one`   |     | ✅    | hr.work.location          |
| `sex`                            | Gender                          | `selection`  |     |       |                           |
| `share`                          | Share User                      | `boolean`    |     |       |                           |
| `show_hr_icon_display`           | Show Hr Icon Display            | `boolean`    |     |       |                           |
| `show_leaves`                    | Able to see Remaining Time Off  | `boolean`    |     |       |                           |
| `skill_ids`                      | Skill                           | `many2many`  |     | ✅    | hr.skill                  |
| `spouse_birthdate`               | Spouse Birthdate                | `date`       |     |       |                           |
| `spouse_complete_name`           | Spouse Legal Name               | `char`       |     |       |                           |
| `ssnid`                          | SSN No                          | `char`       |     |       |                           |
| `structure_type_id`              | Salary Structure Type           | `many2one`   |     |       | hr.payroll.structure.type |
| `study_field`                    | Field of Study                  | `char`       |     | ✅    |                           |
| `study_school`                   | School                          | `char`       |     | ✅    |                           |
| `subordinate_ids`                | Subordinates                    | `one2many`   |     |       | hr.employee               |
| `sunday_location_id`             | Sunday                          | `many2one`   |     | ✅    | hr.work.location          |
| `thursday_location_id`           | Thursday                        | `many2one`   |     | ✅    | hr.work.location          |
| `today_location_name`            | Today Location Name             | `char`       |     | ✅    |                           |
| `trial_date_end`                 | End of Trial Period             | `date`       |     |       |                           |
| `tuesday_location_id`            | Tuesday                         | `many2one`   |     | ✅    | hr.work.location          |
| `tz`                             | Timezone                        | `selection`  |     |       |                           |
| `user_id`                        | User                            | `many2one`   |     | ✅    | res.users                 |
| `user_partner_id`                | User's partner                  | `many2one`   |     |       | res.partner               |
| `version_id`                     | Version                         | `many2one`   | ✅  |       | hr.version                |
| `version_ids`                    | Employee Versions               | `one2many`   | ✅  | ✅    | hr.version                |
| `versions_count`                 | Versions Count                  | `integer`    |     |       |                           |
| `visa_expire`                    | Visa Expiration Date            | `date`       |     | ✅    |                           |
| `visa_no`                        | Visa No                         | `char`       |     | ✅    |                           |
| `wage`                           | Wage                            | `monetary`   |     |       |                           |
| `website_message_ids`            | Website Messages                | `one2many`   |     | ✅    | mail.message              |
| `wednesday_location_id`          | Wednesday                       | `many2one`   |     | ✅    | hr.work.location          |
| `work_contact_id`                | Work Contact                    | `many2one`   |     | ✅    | res.partner               |
| `work_email`                     | Work Email                      | `char`       |     | ✅    |                           |
| `work_location_id`               | Work Location                   | `many2one`   |     |       | hr.work.location          |
| `work_location_name`             | Work Location Name              | `char`       |     |       |                           |
| `work_location_type`             | Work Location Type              | `selection`  |     |       |                           |
| `work_permit_expiration_date`    | Work Permit Expiration Date     | `date`       |     | ✅    |                           |
| `work_permit_name`               | work_permit_name                | `char`       |     |       |                           |
| `work_permit_scheduled_activity` | Work Permit Scheduled Activity  | `boolean`    |     | ✅    |                           |
| `work_phone`                     | Work Phone                      | `char`       |     | ✅    |                           |
| `write_date`                     | Last Updated on                 | `datetime`   |     | ✅    |                           |
| `write_uid`                      | Last Updated by                 | `many2one`   |     | ✅    | res.users                 |

**Access Rights:**

| Name                         | Group                                     | Perms     |
| ---------------------------- | ----------------------------------------- | --------- |
| hr.employee user             | Employees / Officer: Manage all employees | `R/W/C/D` |
| name_hr_employee_back_office | OpenEduCat / Manager                      | `R/W/C`   |
| name_hr_employee_student     | OpenEduCat / Manager                      | `R`       |
| hr.employee system user      | Role / Administrator                      | `R`       |

**Record Rules:**

- **Employee multi company rule** (Global) `R/W/C/D`
  - Domain:
    `['|', '|', '|',         ('company_id', 'in', company_ids + [False]),         ('parent_id.user_id', '=', user.id),         ('id', '=', user.employee_id.parent_id.id),         ('user_id', '=', user.id)     ]`
- **HR multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `hr.version` — Employee Contract

> 📧 Mail Thread

Write and Create: Special case when setting a contract as running: If there is already a
validated time off over another contract with a different schedule, split the time off,
before the \_check_contracts raises an issue. If there are existing leaves that are
spanned by this new contract, update their resource calendar to the current one.

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                  |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------- |
| `active`                        | Active                        | `boolean`   |     | ✅    |                           |
| `active_employee`               | Active Employee               | `boolean`   |     |       |                           |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event            |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                           |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                           |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                           |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity             |
| `activity_state`                | Activity State                | `selection` |     |       |                           |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                           |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                           |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type        |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users                 |
| `additional_note`               | Additional Note               | `text`      |     | ✅    |                           |
| `address_id`                    | Work Address                  | `many2one`  |     | ✅    | res.partner               |
| `allowed_country_state_ids`     | Allowed Country State         | `many2many` |     |       | res.country.state         |
| `children`                      | Dependent Children            | `integer`   |     | ✅    |                           |
| `company_country_id`            | Company country               | `many2one`  |     |       | res.country               |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company               |
| `contract_date_end`             | Contract End Date             | `date`      |     | ✅    |                           |
| `contract_date_start`           | Contract Start Date           | `date`      |     | ✅    |                           |
| `contract_template_id`          | Contract Template             | `many2one`  |     | ✅    | hr.version                |
| `contract_type_id`              | Contract Type                 | `many2one`  |     | ✅    | hr.contract.type          |
| `contract_wage`                 | Contract Wage                 | `monetary`  |     |       |                           |
| `country_code`                  | Country Code                  | `char`      |     |       |                           |
| `country_id`                    | Nationality (Country)         | `many2one`  |     | ✅    | res.country               |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                           |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users                 |
| `currency_id`                   | Currency                      | `many2one`  |     |       | res.currency              |
| `date_end`                      | Date End                      | `date`      |     |       |                           |
| `date_start`                    | Date Start                    | `date`      |     |       |                           |
| `date_version`                  | Date Version                  | `date`      | ✅  | ✅    |                           |
| `department_id`                 | Department                    | `many2one`  |     | ✅    | hr.department             |
| `departure_date`                | Departure Date                | `date`      |     | ✅    |                           |
| `departure_description`         | Additional Information        | `html`      |     | ✅    |                           |
| `departure_reason_id`           | Departure Reason              | `many2one`  |     | ✅    | hr.departure.reason       |
| `display_name`                  | Display Name                  | `char`      |     |       |                           |
| `distance_home_work`            | Home-Work Distance            | `integer`   |     | ✅    |                           |
| `distance_home_work_unit`       | Home-Work Distance unit       | `selection` | ✅  | ✅    |                           |
| `employee_id`                   | Employee                      | `many2one`  |     | ✅    | hr.employee               |
| `employee_type`                 | Employee Type                 | `selection` | ✅  | ✅    |                           |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                           |
| `hr_responsible_id`             | HR Responsible                | `many2one`  | ✅  | ✅    | res.users                 |
| `id`                            | ID                            | `integer`   |     | ✅    |                           |
| `identification_id`             | Identification No             | `char`      |     | ✅    |                           |
| `is_current`                    | Is Current                    | `boolean`   |     |       |                           |
| `is_custom_job_title`           | Is Custom Job Title           | `boolean`   |     | ✅    |                           |
| `is_flexible`                   | Is Flexible                   | `boolean`   |     | ✅    |                           |
| `is_fully_flexible`             | Is Fully Flexible             | `boolean`   |     | ✅    |                           |
| `is_future`                     | Is Future                     | `boolean`   |     |       |                           |
| `is_in_contract`                | Is In Contract                | `boolean`   |     |       |                           |
| `is_past`                       | Is Past                       | `boolean`   |     |       |                           |
| `job_id`                        | Job                           | `many2one`  |     | ✅    | hr.job                    |
| `job_title`                     | Job Title                     | `char`      |     | ✅    |                           |
| `km_home_work`                  | Home-Work Distance in Km      | `integer`   |     | ✅    |                           |
| `last_modified_date`            | Last Modified on              | `datetime`  | ✅  | ✅    |                           |
| `last_modified_uid`             | Last Modified by              | `many2one`  | ✅  | ✅    | res.users                 |
| `marital`                       | Marital Status                | `selection` | ✅  | ✅    |                           |
| `member_of_department`          | Member of department          | `boolean`   |     |       |                           |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                           |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers            |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                           |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                           |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                           |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message              |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                           |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                           |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                           |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner               |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                           |
| `name`                          | Name                          | `char`      |     | ✅    |                           |
| `passport_expiration_date`      | Passport Expiration Date      | `date`      |     | ✅    |                           |
| `passport_id`                   | Passport No                   | `char`      |     | ✅    |                           |
| `private_city`                  | Private City                  | `char`      |     | ✅    |                           |
| `private_country_id`            | Private Country               | `many2one`  |     | ✅    | res.country               |
| `private_state_id`              | Private State                 | `many2one`  |     | ✅    | res.country.state         |
| `private_street`                | Private Street                | `char`      |     | ✅    |                           |
| `private_street2`               | Private Street2               | `char`      |     | ✅    |                           |
| `private_zip`                   | Private Zip                   | `char`      |     | ✅    |                           |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating             |
| `resource_calendar_id`          | Working Hours                 | `many2one`  |     | ✅    | resource.calendar         |
| `sex`                           | Gender                        | `selection` |     | ✅    |                           |
| `spouse_birthdate`              | Spouse Birthdate              | `date`      |     | ✅    |                           |
| `spouse_complete_name`          | Spouse Legal Name             | `char`      |     | ✅    |                           |
| `ssnid`                         | SSN No                        | `char`      |     | ✅    |                           |
| `structure_type_id`             | Salary Structure Type         | `many2one`  |     | ✅    | hr.payroll.structure.type |
| `trial_date_end`                | End of Trial Period           | `date`      |     | ✅    |                           |
| `tz`                            | Timezone                      | `selection` |     |       |                           |
| `wage`                          | Wage                          | `monetary`  |     | ✅    |                           |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message              |
| `work_location_id`              | Work Location                 | `many2one`  |     | ✅    | hr.work.location          |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                           |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name               | Group                                     | Perms     |
| ------------------ | ----------------------------------------- | --------- |
| hr.version.user    | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.version.manager | Employees / Administrator                 | `R/W/C/D` |

**Record Rules:**

- **HR Contract: Contract Manager** (50) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **HR Contract: Multi Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`

### 🗃️ `hr.leave` — Time Off

> 📧 Mail Thread

Time Off Requests Access specifications

     - a regular employee / user
      - can see all leaves;
      - cannot see name field of leaves belonging to other user as it may contain
        private information that we don't want to share to other people than
        HR people;
      - can modify only its own not validated leaves (except writing on state to
        bypass approval);
      - can discuss on its leave requests;
      - can reset only its own leaves;
      - cannot validate any leaves;
     - an Officer
      - can see all leaves;
      - can validate "HR" single validation leaves from people if
       - he is the employee manager;
       - he is the department manager;
       - he is member of the same department;
       - target employee has no manager and no department manager;
      - can validate "Manager" single validation leaves from people if
       - he is the employee manager;
       - he is the department manager;
       - target employee has no manager and no department manager;
      - can first validate "Both" double validation leaves from people like "HR"
        single validation, moving the leaves to validate1 state;
      - cannot validate its own leaves;
      - can reset only its own leaves;
      - can refuse all leaves;
     - a Manager
      - can do everything he wants

    On top of that multicompany rules apply based on company defined on the
    leave request leave type.

**Fields:**

| Field                                | Label                          | Type        | Req | Store | Relation           |
| ------------------------------------ | ------------------------------ | ----------- | --- | ----- | ------------------ |
| `active_employee`                    | Employee Active                | `boolean`   |     |       |                    |
| `activity_calendar_event_id`         | Next Activity Calendar Event   | `many2one`  |     |       | calendar.event     |
| `activity_date_deadline`             | Next Activity Deadline         | `date`      |     |       |                    |
| `activity_exception_decoration`      | Activity Exception Decoration  | `selection` |     |       |                    |
| `activity_exception_icon`            | Icon                           | `char`      |     |       |                    |
| `activity_ids`                       | Activities                     | `one2many`  |     | ✅    | mail.activity      |
| `activity_state`                     | Activity State                 | `selection` |     |       |                    |
| `activity_summary`                   | Next Activity Summary          | `char`      |     |       |                    |
| `activity_type_icon`                 | Activity Type Icon             | `char`      |     |       |                    |
| `activity_type_id`                   | Next Activity Type             | `many2one`  |     |       | mail.activity.type |
| `activity_user_id`                   | Responsible User               | `many2one`  |     |       | res.users          |
| `attachment_ids`                     | Attachments                    | `one2many`  |     | ✅    | ir.attachment      |
| `can_approve`                        | Can Approve                    | `boolean`   |     |       |                    |
| `can_back_to_approve`                | Can Back To Approve            | `boolean`   |     |       |                    |
| `can_cancel`                         | Can Cancel                     | `boolean`   |     |       |                    |
| `can_refuse`                         | Can Refuse                     | `boolean`   |     |       |                    |
| `can_validate`                       | Can Validate                   | `boolean`   |     |       |                    |
| `color`                              | Color                          | `integer`   |     |       |                    |
| `company_id`                         | Company                        | `many2one`  |     | ✅    | res.company        |
| `create_date`                        | Created on                     | `datetime`  |     | ✅    |                    |
| `create_uid`                         | Created by                     | `many2one`  |     | ✅    | res.users          |
| `dashboard_warning_message`          | Dashboard Warning Message      | `char`      |     |       |                    |
| `date_from`                          | Start Date                     | `datetime`  |     | ✅    |                    |
| `date_to`                            | End Date                       | `datetime`  |     | ✅    |                    |
| `department_id`                      | Department                     | `many2one`  |     | ✅    | hr.department      |
| `display_name`                       | Display Name                   | `char`      |     |       |                    |
| `duration_display`                   | Requested                      | `char`      |     | ✅    |                    |
| `employee_company_id`                | Employee Company               | `many2one`  |     | ✅    | res.company        |
| `employee_id`                        | Employee                       | `many2one`  | ✅  | ✅    | hr.employee        |
| `first_approver_id`                  | First Approval                 | `many2one`  |     | ✅    | hr.employee        |
| `has_mandatory_day`                  | Has Mandatory Day              | `boolean`   |     |       |                    |
| `has_message`                        | Has Message                    | `boolean`   |     |       |                    |
| `holiday_status_id`                  | Time Off Type                  | `many2one`  | ✅  | ✅    | hr.leave.type      |
| `holiday_status_requires_allocation` | Requires allocation            | `boolean`   |     |       |                    |
| `id`                                 | ID                             | `integer`   |     | ✅    |                    |
| `is_hatched`                         | Hatched                        | `boolean`   |     |       |                    |
| `is_striked`                         | Striked                        | `boolean`   |     |       |                    |
| `last_several_days`                  | All day                        | `boolean`   |     |       |                    |
| `leave_type_increases_duration`      | Leave Type Increases Duration  | `char`      |     |       |                    |
| `leave_type_request_unit`            | Duration Type                  | `selection` |     |       |                    |
| `leave_type_support_document`        | Supporting Document            | `boolean`   |     |       |                    |
| `max_leaves`                         | Max Leaves                     | `float`     |     |       |                    |
| `meeting_id`                         | Meeting                        | `many2one`  |     | ✅    | calendar.event     |
| `message_attachment_count`           | Attachment Count               | `integer`   |     |       |                    |
| `message_follower_ids`               | Followers                      | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`                  | Message Delivery error         | `boolean`   |     |       |                    |
| `message_has_error_counter`          | Number of errors               | `integer`   |     |       |                    |
| `message_has_sms_error`              | SMS Delivery error             | `boolean`   |     |       |                    |
| `message_ids`                        | Messages                       | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`                | Is Follower                    | `boolean`   |     |       |                    |
| `message_main_attachment_id`         | Main Attachment                | `many2one`  |     | ✅    | ir.attachment      |
| `message_needaction`                 | Action Needed                  | `boolean`   |     |       |                    |
| `message_needaction_counter`         | Number of Actions              | `integer`   |     |       |                    |
| `message_partner_ids`                | Followers (Partners)           | `many2many` |     |       | res.partner        |
| `my_activity_date_deadline`          | My Activity Deadline           | `date`      |     |       |                    |
| `name`                               | Description                    | `char`      |     |       |                    |
| `notes`                              | Reasons                        | `text`      |     | ✅    |                    |
| `number_of_days`                     | Duration (Days)                | `float`     |     | ✅    |                    |
| `number_of_hours`                    | Duration (Hours)               | `float`     |     | ✅    |                    |
| `private_name`                       | Time Off Description           | `char`      |     | ✅    |                    |
| `rating_ids`                         | Ratings                        | `one2many`  |     | ✅    | rating.rating      |
| `request_date_from`                  | Request Start Date             | `date`      |     | ✅    |                    |
| `request_date_from_period`           | Date Period Start              | `selection` |     | ✅    |                    |
| `request_date_to`                    | Request End Date               | `date`      |     | ✅    |                    |
| `request_date_to_period`             | Date Period End                | `selection` |     | ✅    |                    |
| `request_hour_from`                  | Hour from                      | `float`     |     | ✅    |                    |
| `request_hour_to`                    | Hour to                        | `float`     |     | ✅    |                    |
| `request_unit_half`                  | Half-Day                       | `boolean`   |     | ✅    |                    |
| `request_unit_hours`                 | Specific Time                  | `boolean`   |     | ✅    |                    |
| `resource_calendar_id`               | Resource Calendar              | `many2one`  |     | ✅    | resource.calendar  |
| `second_approver_id`                 | Second Approval                | `many2one`  |     | ✅    | hr.employee        |
| `state`                              | Status                         | `selection` |     | ✅    |                    |
| `supported_attachment_ids`           | Attach File                    | `many2many` |     |       | ir.attachment      |
| `supported_attachment_ids_count`     | Supported Attachment Ids Count | `integer`   |     |       |                    |
| `tz`                                 | Tz                             | `selection` |     |       |                    |
| `tz_mismatch`                        | Tz Mismatch                    | `boolean`   |     |       |                    |
| `user_id`                            | User                           | `many2one`  |     | ✅    | res.users          |
| `validation_type`                    | Validation Type                | `selection` |     |       |                    |
| `virtual_remaining_leaves`           | Available Time Off             | `float`     |     |       |                    |
| `website_message_ids`                | Website Messages               | `one2many`  |     | ✅    | mail.message       |
| `write_date`                         | Last Updated on                | `datetime`  |     | ✅    |                    |
| `write_uid`                          | Last Updated by                | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                         | Group                                   | Perms     |
| ---------------------------- | --------------------------------------- | --------- |
| hr.holidays.user.request     | Time Off / Officer: Manage all requests | `R/W/C/D` |
| hr.holidays.manager.request  | Time Off / Administrator                | `R/W/C/D` |
| hr.holidays.employee.request | Role / User                             | `R/W/C/D` |

**Record Rules:**

- **Time Off base.group_user read** (1) `R`
  - Domain: `[('employee_id.user_id', '=', user.id)]`
- **Time Off base.group_user create/write** (1) `W/C`
  - Domain:
    `[         '|',             '&',                 ('employee_id.user_id', '=', user.id),                 ('state', 'not in', ['validate', 'validate1']),             '&',                 ('validation_type', 'in', ['manager', 'both', 'no_validation']),                 ('employee_id.leave_manager_id', '=', user.id),     ]`
- **Time Off base.group_user unlink** (1) `D`
  - Domain:
    `[('employee_id.user_id', '=', user.id), ('state', 'in', ['confirm', 'validate1'])]`
- **Time Off Responsible read** (79) `R`
  - Domain: `[             ('employee_id.leave_manager_id', '=', user.id),     ]`
- **Time Off Responsible create/write** (79) `W/C`
  - Domain:
    `[         '|',             '&',                 ('employee_id.user_id', '=', user.id),                 ('state', '!=', 'validate'),             ('employee_id.leave_manager_id', '=', user.id),     ]`
- **Time Off All Approver read** (80) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Time Off All Approver create/write** (80) `W/C`
  - Domain:
    `[         '|',             '&',                 ('employee_id.user_id', '=', user.id),                 ('state', '!=', 'validate'),             '|',                 ('employee_id.user_id', '!=', user.id),                 ('employee_id.user_id', '=', False)     ]`
- **Time Off Administrator** (81) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Time Off: multi company global rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`

### 🗃️ `hr.leave.allocation` — Time Off Allocation

> 📧 Mail Thread

Allocation Requests Access specifications: similar to leave requests

**Fields:**

| Field                               | Label                                                                                 | Type        | Req | Store | Relation              |
| ----------------------------------- | ------------------------------------------------------------------------------------- | ----------- | --- | ----- | --------------------- |
| `accrual_plan_id`                   | Accrual Plan                                                                          | `many2one`  |     | ✅    | hr.leave.accrual.plan |
| `active_employee`                   | Active Employee                                                                       | `boolean`   |     |       |                       |
| `activity_calendar_event_id`        | Next Activity Calendar Event                                                          | `many2one`  |     |       | calendar.event        |
| `activity_date_deadline`            | Next Activity Deadline                                                                | `date`      |     |       |                       |
| `activity_exception_decoration`     | Activity Exception Decoration                                                         | `selection` |     |       |                       |
| `activity_exception_icon`           | Icon                                                                                  | `char`      |     |       |                       |
| `activity_ids`                      | Activities                                                                            | `one2many`  |     | ✅    | mail.activity         |
| `activity_state`                    | Activity State                                                                        | `selection` |     |       |                       |
| `activity_summary`                  | Next Activity Summary                                                                 | `char`      |     |       |                       |
| `activity_type_icon`                | Activity Type Icon                                                                    | `char`      |     |       |                       |
| `activity_type_id`                  | Next Activity Type                                                                    | `many2one`  |     |       | mail.activity.type    |
| `activity_user_id`                  | Responsible User                                                                      | `many2one`  |     |       | res.users             |
| `actual_lastcall`                   | Actual Lastcall                                                                       | `date`      |     | ✅    |                       |
| `allocation_type`                   | Allocation Type                                                                       | `selection` | ✅  | ✅    |                       |
| `already_accrued`                   | Already Accrued                                                                       | `boolean`   |     | ✅    |                       |
| `approver_id`                       | First Approval                                                                        | `many2one`  |     | ✅    | hr.employee           |
| `can_approve`                       | Can Approve                                                                           | `boolean`   |     |       |                       |
| `can_refuse`                        | Can Refuse                                                                            | `boolean`   |     |       |                       |
| `can_validate`                      | Can Validate                                                                          | `boolean`   |     |       |                       |
| `carried_over_days_expiration_date` | Carried over days expiration date                                                     | `date`      |     | ✅    |                       |
| `create_date`                       | Created on                                                                            | `datetime`  |     | ✅    |                       |
| `create_uid`                        | Created by                                                                            | `many2one`  |     | ✅    | res.users             |
| `date_from`                         | Start Date                                                                            | `date`      | ✅  | ✅    |                       |
| `date_to`                           | End Date                                                                              | `date`      |     | ✅    |                       |
| `department_id`                     | Department                                                                            | `many2one`  |     | ✅    | hr.department         |
| `display_name`                      | Display Name                                                                          | `char`      |     |       |                       |
| `duration_display`                  | Allocated (Days/Hours)                                                                | `char`      |     |       |                       |
| `employee_company_id`               | Company                                                                               | `many2one`  |     | ✅    | res.company           |
| `employee_id`                       | Employee                                                                              | `many2one`  | ✅  | ✅    | hr.employee           |
| `expiring_carryover_days`           | The number of carried over days that will expire on carried_over_days_expiration_date | `float`     |     | ✅    |                       |
| `has_message`                       | Has Message                                                                           | `boolean`   |     |       |                       |
| `holiday_status_id`                 | Time Off Type                                                                         | `many2one`  | ✅  | ✅    | hr.leave.type         |
| `id`                                | ID                                                                                    | `integer`   |     | ✅    |                       |
| `is_name_custom`                    | Is Name Custom                                                                        | `boolean`   |     |       |                       |
| `is_officer`                        | Is Officer                                                                            | `boolean`   |     |       |                       |
| `lastcall`                          | Date of the last accrual allocation                                                   | `date`      |     | ✅    |                       |
| `last_executed_carryover_date`      | Last Executed Carryover Date                                                          | `date`      |     | ✅    |                       |
| `leaves_taken`                      | Time off Taken                                                                        | `float`     |     |       |                       |
| `manager_id`                        | Manager                                                                               | `many2one`  |     | ✅    | hr.employee           |
| `max_leaves`                        | Max Leaves                                                                            | `float`     |     |       |                       |
| `message_attachment_count`          | Attachment Count                                                                      | `integer`   |     |       |                       |
| `message_follower_ids`              | Followers                                                                             | `one2many`  |     | ✅    | mail.followers        |
| `message_has_error`                 | Message Delivery error                                                                | `boolean`   |     |       |                       |
| `message_has_error_counter`         | Number of errors                                                                      | `integer`   |     |       |                       |
| `message_has_sms_error`             | SMS Delivery error                                                                    | `boolean`   |     |       |                       |
| `message_ids`                       | Messages                                                                              | `one2many`  |     | ✅    | mail.message          |
| `message_is_follower`               | Is Follower                                                                           | `boolean`   |     |       |                       |
| `message_needaction`                | Action Needed                                                                         | `boolean`   |     |       |                       |
| `message_needaction_counter`        | Number of Actions                                                                     | `integer`   |     |       |                       |
| `message_partner_ids`               | Followers (Partners)                                                                  | `many2many` |     |       | res.partner           |
| `my_activity_date_deadline`         | My Activity Deadline                                                                  | `date`      |     |       |                       |
| `name`                              | Description                                                                           | `char`      |     | ✅    |                       |
| `name_validity`                     | Description with validity                                                             | `char`      |     |       |                       |
| `nextcall`                          | Date of the next accrual allocation                                                   | `date`      |     | ✅    |                       |
| `notes`                             | Reasons                                                                               | `text`      |     | ✅    |                       |
| `number_of_days`                    | Number of Days                                                                        | `float`     |     | ✅    |                       |
| `number_of_days_display`            | Duration (days)                                                                       | `float`     |     |       |                       |
| `number_of_hours_display`           | Duration (hours)                                                                      | `float`     |     | ✅    |                       |
| `rating_ids`                        | Ratings                                                                               | `one2many`  |     | ✅    | rating.rating         |
| `second_approver_id`                | Second Approval                                                                       | `many2one`  |     | ✅    | hr.employee           |
| `state`                             | Status                                                                                | `selection` |     | ✅    |                       |
| `type_request_unit`                 | Type Request Unit                                                                     | `selection` |     |       |                       |
| `validation_type`                   | Validation Type                                                                       | `selection` |     |       |                       |
| `virtual_remaining_leaves`          | Available Time Off                                                                    | `float`     |     |       |                       |
| `website_message_ids`               | Website Messages                                                                      | `one2many`  |     | ✅    | mail.message          |
| `write_date`                        | Last Updated on                                                                       | `datetime`  |     | ✅    |                       |
| `write_uid`                         | Last Updated by                                                                       | `many2one`  |     | ✅    | res.users             |
| `yearly_accrued_amount`             | Yearly Accrued Amount                                                                 | `float`     |     | ✅    |                       |

**Access Rights:**

| Name                            | Group                                   | Perms     |
| ------------------------------- | --------------------------------------- | --------- |
| hr.holidays.user.allocation     | Time Off / Officer: Manage all requests | `R/W/C/D` |
| hr.holidays.manager.allocation  | Time Off / Administrator                | `R/W/C/D` |
| hr.holidays.employee.allocation | Role / User                             | `R/W/C/D` |

**Record Rules:**

- **Time Off: multi company global rule** (Global) `R/W/C/D`
  - Domain:
    `[         '|',             ('employee_id', '=', False),             ('employee_id.company_id', 'in', company_ids),         ('holiday_status_id.company_id', 'in', company_ids + [False])     ]`
- **Allocations: employee: read own** (1) `R`
  - Domain:
    `[         '|',             ('employee_id.leave_manager_id', '=', user.id),             ('employee_id.user_id', '=', user.id),     ]`
- **Allocations: base.group_user create/write** (1) `W/C`
  - Domain:
    `[         '|',             '&',                 ('employee_id.user_id', '=', user.id),                 ('state', '=', 'confirm'),             '&',                 ('validation_type', 'in', ['manager', 'both', 'no_validation']),                 ('employee_id.leave_manager_id', '=', user.id),     ]`
- **Allocations: Responsible: create/write** (79) `W/C`
  - Domain:
    `[         '|',             '&',                 ('employee_id.user_id', '=', user.id),                 ('state', '!=', 'validate'),             ('employee_id.leave_manager_id', '=', user.id),     ]`
- **Allocations: see all time off: read all** (80) `R`
  - Domain: `[(1, '=', 1)]`
- **Allocations base.group_user unlink** (1) `D`
  - Domain: `[('employee_id.user_id', '=', user.id), ('state', '=', 'draft')]`
- **Allocations: holiday user: create/write** (80) `R/W/C/D`
  - Domain:
    `[         '|',             '&',                 ('employee_id.user_id', '=', user.id),                 ('state', '!=', 'validate'),             '|',                 ('employee_id.user_id', '!=', user.id),                 ('employee_id.user_id', '=', False)     ]`
- **Allocations: administrator: no limit** (81) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `hr.leave.accrual.plan` — Accrual Plan

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label                   | Type        | Req | Store | Relation               |
| ------------------------- | ----------------------- | ----------- | --- | ----- | ---------------------- |
| `accrued_gain_time`       | Accrued Gain Time       | `selection` | ✅  | ✅    |                        |
| `active`                  | Active                  | `boolean`   |     | ✅    |                        |
| `added_value_type`        | Added Value Type        | `selection` |     | ✅    |                        |
| `allocation_ids`          | Allocation              | `one2many`  |     | ✅    | hr.leave.allocation    |
| `can_be_carryover`        | Can Be Carryover        | `boolean`   |     | ✅    |                        |
| `carryover_date`          | Carry-Over Time         | `selection` | ✅  | ✅    |                        |
| `carryover_day`           | Carryover Day           | `selection` |     | ✅    |                        |
| `carryover_month`         | Carryover Month         | `selection` |     | ✅    |                        |
| `company_id`              | Company                 | `many2one`  |     | ✅    | res.company            |
| `create_date`             | Created on              | `datetime`  |     | ✅    |                        |
| `create_uid`              | Created by              | `many2one`  |     | ✅    | res.users              |
| `display_name`            | Display Name            | `char`      |     |       |                        |
| `employees_count`         | Employees               | `integer`   |     |       |                        |
| `id`                      | ID                      | `integer`   |     | ✅    |                        |
| `is_based_on_worked_time` | Is Based On Worked Time | `boolean`   |     | ✅    |                        |
| `level_count`             | Levels                  | `integer`   |     |       |                        |
| `level_ids`               | Milestones              | `one2many`  |     | ✅    | hr.leave.accrual.level |
| `name`                    | Name                    | `char`      | ✅  | ✅    |                        |
| `show_transition_mode`    | Show Transition Mode    | `boolean`   |     |       |                        |
| `time_off_type_id`        | Time Off Type           | `many2one`  |     | ✅    | hr.leave.type          |
| `transition_mode`         | Transition Mode         | `selection` | ✅  | ✅    |                        |
| `write_date`              | Last Updated on         | `datetime`  |     | ✅    |                        |
| `write_uid`               | Last Updated by         | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                          | Group                                   | Perms     |
| ----------------------------- | --------------------------------------- | --------- |
| hr.leave.accrual.plan.user    | Time Off / Officer: Manage all requests | `R`       |
| hr.leave.accrual.plan.manager | Time Off / Administrator                | `R/W/C/D` |

**Record Rules:**

- **Accrual plan multi company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `hr.leave.accrual.level` — Accrual Plan Level

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                       | Type        | Req | Store | Relation              |
| ----------------------------- | --------------------------- | ----------- | --- | ----- | --------------------- |
| `accrual_plan_id`             | Accrual Plan                | `many2one`  | ✅  | ✅    | hr.leave.accrual.plan |
| `accrual_validity`            | Accrual Validity            | `boolean`   |     | ✅    |                       |
| `accrual_validity_count`      | Accrual Validity Count      | `integer`   |     | ✅    |                       |
| `accrual_validity_type`       | Accrual Validity Type       | `selection` | ✅  | ✅    |                       |
| `accrued_gain_time`           | Accrued Gain Time           | `selection` |     |       |                       |
| `action_with_unused_accruals` | Action With Unused Accruals | `selection` | ✅  | ✅    |                       |
| `added_value`                 | Added Value                 | `float`     | ✅  | ✅    |                       |
| `added_value_type`            | Added Value Type            | `selection` | ✅  | ✅    |                       |
| `can_be_carryover`            | Can Be Carryover            | `boolean`   |     |       |                       |
| `can_modify_value_type`       | Can Modify Value Type       | `boolean`   |     |       |                       |
| `cap_accrued_time`            | Cap Accrued Time            | `boolean`   |     | ✅    |                       |
| `cap_accrued_time_yearly`     | Cap Accrued Time Yearly     | `boolean`   |     | ✅    |                       |
| `carryover_options`           | Carryover Options           | `selection` | ✅  | ✅    |                       |
| `create_date`                 | Created on                  | `datetime`  |     | ✅    |                       |
| `create_uid`                  | Created by                  | `many2one`  |     | ✅    | res.users             |
| `display_name`                | Display Name                | `char`      |     |       |                       |
| `first_day`                   | First Day                   | `selection` |     | ✅    |                       |
| `first_month`                 | First Month                 | `selection` |     | ✅    |                       |
| `first_month_day`             | First Month Day             | `selection` |     | ✅    |                       |
| `frequency`                   | Frequency                   | `selection` | ✅  | ✅    |                       |
| `id`                          | ID                          | `integer`   |     | ✅    |                       |
| `maximum_leave`               | Maximum Leave               | `float`     |     | ✅    |                       |
| `maximum_leave_yearly`        | Maximum Leave Yearly        | `float`     |     | ✅    |                       |
| `milestone_date`              | Milestone Date              | `selection` | ✅  | ✅    |                       |
| `postpone_max_days`           | Postpone Max Days           | `integer`   |     | ✅    |                       |
| `second_day`                  | Second Day                  | `selection` |     | ✅    |                       |
| `second_month`                | Second Month                | `selection` |     | ✅    |                       |
| `second_month_day`            | Second Month Day            | `selection` |     | ✅    |                       |
| `sequence`                    | sequence                    | `integer`   |     | ✅    |                       |
| `start_count`                 | Start Count                 | `integer`   |     | ✅    |                       |
| `start_type`                  | Start Type                  | `selection` | ✅  | ✅    |                       |
| `week_day`                    | Allocation on               | `selection` | ✅  | ✅    |                       |
| `write_date`                  | Last Updated on             | `datetime`  |     | ✅    |                       |
| `write_uid`                   | Last Updated by             | `many2one`  |     | ✅    | res.users             |
| `yearly_day`                  | Yearly Day                  | `selection` |     | ✅    |                       |
| `yearly_month`                | Yearly Month                | `selection` |     | ✅    |                       |

**Access Rights:**

| Name                           | Group                                   | Perms     |
| ------------------------------ | --------------------------------------- | --------- |
| hr.leave.accrual.level.user    | Time Off / Officer: Manage all requests | `R`       |
| hr.leave.accrual.level.manager | Time Off / Administrator                | `R/W/C/D` |

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

### 🗃️ `hr.holidays.cancel.leave` — Cancel Time Off Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label            | Type       | Req | Store | Relation  |
| -------------- | ---------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on       | `datetime` |     | ✅    |           |
| `create_uid`   | Created by       | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name     | `char`     |     |       |           |
| `id`           | ID               | `integer`  |     | ✅    |           |
| `leave_id`     | Time Off Request | `many2one` | ✅  | ✅    | hr.leave  |
| `reason`       | Reason           | `text`     |     | ✅    |           |
| `write_date`   | Last Updated on  | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by  | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                            | Group       | Perms     |
| ------------------------------- | ----------- | --------- |
| access_hr_holidays_cancel_leave | Role / User | `R/W/C/D` |

### 🗃️ `hr.departure.wizard` — Departure Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                   | Label                  | Type        | Req | Store | Relation            |
| ----------------------- | ---------------------- | ----------- | --- | ----- | ------------------- |
| `create_date`           | Created on             | `datetime`  |     | ✅    |                     |
| `create_uid`            | Created by             | `many2one`  |     | ✅    | res.users           |
| `departure_date`        | Contract End Date      | `date`      | ✅  | ✅    |                     |
| `departure_description` | Additional Information | `html`      |     | ✅    |                     |
| `departure_reason_id`   | Departure Reason       | `many2one`  | ✅  | ✅    | hr.departure.reason |
| `display_name`          | Display Name           | `char`      |     |       |                     |
| `employee_ids`          | Employees              | `many2many` | ✅  | ✅    | hr.employee         |
| `id`                    | ID                     | `integer`   |     | ✅    |                     |
| `is_user_employee`      | User Employee          | `boolean`   |     |       |                     |
| `release_campany_car`   | Release Company Car    | `boolean`   |     | ✅    |                     |
| `remove_related_user`   | Related User           | `boolean`   |     | ✅    |                     |
| `set_date_end`          | Set Contract End Date  | `boolean`   |     | ✅    |                     |
| `write_date`            | Last Updated on        | `datetime`  |     | ✅    |                     |
| `write_uid`             | Last Updated by        | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                       | Group                                     | Perms   |
| -------------------------- | ----------------------------------------- | ------- |
| access.hr.departure.wizard | Employees / Officer: Manage all employees | `R/W/C` |

### 🗃️ `hr.leave.allocation.generate.multi.wizard` — Generate time off allocations for multiple employees

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field               | Label           | Type        | Req | Store | Relation              |
| ------------------- | --------------- | ----------- | --- | ----- | --------------------- |
| `accrual_plan_id`   | Accrual Plan    | `many2one`  |     | ✅    | hr.leave.accrual.plan |
| `allocation_mode`   | Allocation Mode | `selection` | ✅  | ✅    |                       |
| `allocation_type`   | Allocation Type | `selection` | ✅  | ✅    |                       |
| `category_id`       | Employee Tag    | `many2one`  |     | ✅    | hr.employee.category  |
| `company_id`        | Company         | `many2one`  | ✅  | ✅    | res.company           |
| `create_date`       | Created on      | `datetime`  |     | ✅    |                       |
| `create_uid`        | Created by      | `many2one`  |     | ✅    | res.users             |
| `date_from`         | Start Date      | `date`      | ✅  | ✅    |                       |
| `date_to`           | End Date        | `date`      |     | ✅    |                       |
| `department_id`     | Department      | `many2one`  |     | ✅    | hr.department         |
| `display_name`      | Display Name    | `char`      |     |       |                       |
| `duration`          | Allocation      | `float`     |     | ✅    |                       |
| `employee_ids`      | Employees       | `many2many` |     | ✅    | hr.employee           |
| `holiday_status_id` | Time Off Type   | `many2one`  | ✅  | ✅    | hr.leave.type         |
| `id`                | ID              | `integer`   |     | ✅    |                       |
| `name`              | Description     | `char`      |     | ✅    |                       |
| `notes`             | Reasons         | `text`      |     | ✅    |                       |
| `request_unit`      | Duration Type   | `selection` |     |       |                       |
| `write_date`        | Last Updated on | `datetime`  |     | ✅    |                       |
| `write_uid`         | Last Updated by | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                                             | Group                | Perms     |
| ------------------------------------------------ | -------------------- | --------- |
| access_hr_leave_allocation_generate_multi_wizard | Time Off Responsible | `R/W/C/D` |

### 🗃️ `hr.leave.generate.multi.wizard` — Generate time off for multiple employees

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field               | Label           | Type        | Req | Store | Relation             |
| ------------------- | --------------- | ----------- | --- | ----- | -------------------- |
| `allocation_mode`   | Allocation Mode | `selection` | ✅  | ✅    |                      |
| `category_id`       | Employee Tag    | `many2one`  |     | ✅    | hr.employee.category |
| `company_id`        | Company         | `many2one`  | ✅  | ✅    | res.company          |
| `create_date`       | Created on      | `datetime`  |     | ✅    |                      |
| `create_uid`        | Created by      | `many2one`  |     | ✅    | res.users            |
| `date_from`         | Start Date      | `date`      | ✅  | ✅    |                      |
| `date_to`           | End Date        | `date`      | ✅  | ✅    |                      |
| `department_id`     | Department      | `many2one`  |     | ✅    | hr.department        |
| `display_name`      | Display Name    | `char`      |     |       |                      |
| `employee_ids`      | Employees       | `many2many` |     | ✅    | hr.employee          |
| `holiday_status_id` | Time Off Type   | `many2one`  | ✅  | ✅    | hr.leave.type        |
| `id`                | ID              | `integer`   |     | ✅    |                      |
| `name`              | Description     | `char`      |     | ✅    |                      |
| `write_date`        | Last Updated on | `datetime`  |     | ✅    |                      |
| `write_uid`         | Last Updated by | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                                  | Group                | Perms     |
| ------------------------------------- | -------------------- | --------- |
| access_hr_leave_generate_multi_wizard | Time Off Responsible | `R/W/C/D` |

### 🗃️ `report.hr_holidays.report_holidayssummary` — Holidays Summary Report

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `hr.holidays.summary.employee` — HR Time Off Summary Report By Employee

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label                | Type        | Req | Store | Relation    |
| -------------- | -------------------- | ----------- | --- | ----- | ----------- |
| `create_date`  | Created on           | `datetime`  |     | ✅    |             |
| `create_uid`   | Created by           | `many2one`  |     | ✅    | res.users   |
| `date_from`    | From                 | `date`      | ✅  | ✅    |             |
| `display_name` | Display Name         | `char`      |     |       |             |
| `emp`          | Employee(s)          | `many2many` |     | ✅    | hr.employee |
| `holiday_type` | Select Time Off Type | `selection` | ✅  | ✅    |             |
| `id`           | ID                   | `integer`   |     | ✅    |             |
| `write_date`   | Last Updated on      | `datetime`  |     | ✅    |             |
| `write_uid`    | Last Updated by      | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                                | Group                                   | Perms   |
| ----------------------------------- | --------------------------------------- | ------- |
| access.hr.holidays.summary.employee | Time Off / Officer: Manage all requests | `R/W/C` |

### 🗃️ `hr.leave.mandatory.day` — Mandatory Day

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label           | Type        | Req | Store | Relation          |
| ---------------------- | --------------- | ----------- | --- | ----- | ----------------- |
| `color`                | Color           | `integer`   |     | ✅    |                   |
| `company_id`           | Company         | `many2one`  | ✅  | ✅    | res.company       |
| `create_date`          | Created on      | `datetime`  |     | ✅    |                   |
| `create_uid`           | Created by      | `many2one`  |     | ✅    | res.users         |
| `department_ids`       | Departments     | `many2many` |     | ✅    | hr.department     |
| `display_name`         | Display Name    | `char`      |     |       |                   |
| `end_date`             | End Date        | `date`      | ✅  | ✅    |                   |
| `id`                   | ID              | `integer`   |     | ✅    |                   |
| `job_ids`              | Job Position    | `many2many` |     | ✅    | hr.job            |
| `name`                 | Name            | `char`      | ✅  | ✅    |                   |
| `resource_calendar_id` | Working Hours   | `many2one`  |     | ✅    | resource.calendar |
| `start_date`           | Start Date      | `date`      | ✅  | ✅    |                   |
| `write_date`           | Last Updated on | `datetime`  |     | ✅    |                   |
| `write_uid`            | Last Updated by | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                                     | Group                    | Perms     |
| ---------------------------------------- | ------------------------ | --------- |
| access_hr_holidays_mandatory_day_manager | Time Off / Administrator | `R/W/C/D` |
| access_hr_holidays_mandatory_day_user    | Role / User              | `R`       |

**Record Rules:**

- **Mandatory Day: multi company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `mail.message.subtype` — Message subtypes

Class holding subtype definition for messages. Subtypes allow to tune the follower
subscription, allowing only some subtypes to be pushed on the Wall.

**Fields:**

| Field              | Label            | Type       | Req | Store | Relation             |
| ------------------ | ---------------- | ---------- | --- | ----- | -------------------- |
| `create_date`      | Created on       | `datetime` |     | ✅    |                      |
| `create_uid`       | Created by       | `many2one` |     | ✅    | res.users            |
| `default`          | Default          | `boolean`  |     | ✅    |                      |
| `description`      | Description      | `text`     |     | ✅    |                      |
| `display_name`     | Display Name     | `char`     |     |       |                      |
| `hidden`           | Hidden           | `boolean`  |     | ✅    |                      |
| `id`               | ID               | `integer`  |     | ✅    |                      |
| `internal`         | Internal Only    | `boolean`  |     | ✅    |                      |
| `name`             | Message Type     | `char`     | ✅  | ✅    |                      |
| `parent_id`        | Parent           | `many2one` |     | ✅    | mail.message.subtype |
| `relation_field`   | Relation field   | `char`     |     | ✅    |                      |
| `res_model`        | Model            | `char`     |     | ✅    |                      |
| `sequence`         | Sequence         | `integer`  |     | ✅    |                      |
| `track_recipients` | Track Recipients | `boolean`  |     | ✅    |                      |
| `write_date`       | Last Updated on  | `datetime` |     | ✅    |                      |
| `write_uid`        | Last Updated by  | `many2one` |     | ✅    | res.users            |

**Access Rights:**

| Name                        | Group                | Perms     |
| --------------------------- | -------------------- | --------- |
| mail.message.subtype.system | Role / Administrator | `R/W/C/D` |
| mail.message.subtype.all    | Role / Portal        | `R`       |
| mail.message.subtype.all    | Role / Public        | `R`       |
| mail.message.subtype.user   | Role / User          | `R`       |

**Record Rules:**

- **mail.message.subtype: portal/public: read public subtypes** (10, 11) `R/W/C/D`
  - Domain: `[('internal', '=', False)]`

### 🗃️ `hr.employee.public` — Public Employee

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                          | Type        | Req | Store | Relation                |
| -------------------------------- | ------------------------------ | ----------- | --- | ----- | ----------------------- |
| `active`                         | Active                         | `boolean`   |     | ✅    |                         |
| `address_id`                     | Address                        | `many2one`  |     | ✅    | res.partner             |
| `allocation_display`             | Allocation Display             | `char`      |     |       |                         |
| `allocation_remaining_display`   | Allocation Remaining Display   | `char`      |     |       |                         |
| `avatar_1024`                    | Avatar 1024                    | `binary`    |     |       |                         |
| `avatar_128`                     | Avatar 128                     | `binary`    |     |       |                         |
| `avatar_1920`                    | Avatar                         | `binary`    |     |       |                         |
| `avatar_256`                     | Avatar 256                     | `binary`    |     |       |                         |
| `avatar_512`                     | Avatar 512                     | `binary`    |     |       |                         |
| `badge_ids`                      | Badge                          | `one2many`  |     |       | gamification.badge.user |
| `birthday_public_display_string` | Public Date of Birth           | `char`      |     |       |                         |
| `certification_ids`              | Certification                  | `one2many`  |     |       | hr.employee.skill       |
| `child_all_count`                | Child All Count                | `integer`   |     |       |                         |
| `child_count`                    | Child Count                    | `integer`   |     |       |                         |
| `child_ids`                      | Direct subordinates            | `one2many`  |     | ✅    | hr.employee.public      |
| `coach_id`                       | Coach                          | `many2one`  |     | ✅    | hr.employee.public      |
| `color`                          | Color                          | `integer`   |     | ✅    |                         |
| `company_id`                     | Company                        | `many2one`  |     | ✅    | res.company             |
| `country_code`                   | Country Code                   | `char`      |     |       |                         |
| `create_date`                    | Create Date                    | `datetime`  |     | ✅    |                         |
| `create_uid`                     | Created by                     | `many2one`  |     | ✅    | res.users               |
| `current_employee_skill_ids`     | Current Employee Skill         | `one2many`  |     |       | hr.employee.skill       |
| `department_color`               | Department Color               | `integer`   |     |       |                         |
| `department_id`                  | Department                     | `many2one`  |     | ✅    | hr.department           |
| `display_certification_page`     | Display Certification Page     | `boolean`   |     |       |                         |
| `display_name`                   | Display Name                   | `char`      |     |       |                         |
| `email`                          | Email                          | `char`      |     |       |                         |
| `employee_id`                    | Employee                       | `many2one`  |     | ✅    | hr.employee             |
| `employee_skill_ids`             | Skills                         | `one2many`  |     | ✅    | hr.employee.skill       |
| `expense_manager_id`             | Expense Manager                | `many2one`  |     | ✅    | res.users               |
| `filter_for_expense`             | Filter For Expense             | `boolean`   |     |       |                         |
| `friday_location_id`             | Friday                         | `many2one`  |     | ✅    | hr.work.location        |
| `has_badges`                     | Has Badges                     | `boolean`   |     |       |                         |
| `hr_icon_display`                | Hr Icon Display                | `selection` |     |       |                         |
| `hr_presence_state`              | Hr Presence State              | `selection` |     |       |                         |
| `id`                             | ID                             | `integer`   |     | ✅    |                         |
| `image_1024`                     | Image 1024                     | `binary`    |     |       |                         |
| `image_128`                      | Image 128                      | `binary`    |     |       |                         |
| `image_1920`                     | Image                          | `binary`    |     |       |                         |
| `image_256`                      | Image 256                      | `binary`    |     |       |                         |
| `image_512`                      | Image 512                      | `binary`    |     |       |                         |
| `im_status`                      | IM Status                      | `char`      |     |       |                         |
| `is_absent`                      | Absent Today                   | `boolean`   |     |       |                         |
| `is_manager`                     | Is Manager                     | `boolean`   |     |       |                         |
| `is_subordinate`                 | Is Subordinate                 | `boolean`   |     |       |                         |
| `is_user`                        | Is User                        | `boolean`   |     |       |                         |
| `job_id`                         | Job                            | `many2one`  |     | ✅    | hr.job                  |
| `job_title`                      | Job Title                      | `char`      |     |       |                         |
| `last_activity`                  | Last Activity                  | `date`      |     |       |                         |
| `last_activity_time`             | Last Activity Time             | `char`      |     |       |                         |
| `leave_date_to`                  | To Date                        | `date`      |     |       |                         |
| `leave_manager_id`               | Time Off Approver              | `many2one`  |     | ✅    | res.users               |
| `member_of_department`           | Member Of Department           | `boolean`   |     |       |                         |
| `mobile_phone`                   | Mobile Phone                   | `char`      |     | ✅    |                         |
| `mobility_card`                  | Mobility Card                  | `char`      |     | ✅    |                         |
| `monday_location_id`             | Monday                         | `many2one`  |     | ✅    | hr.work.location        |
| `name`                           | Name                           | `char`      |     | ✅    |                         |
| `newly_hired`                    | Newly Hired                    | `boolean`   |     |       |                         |
| `parent_id`                      | Manager                        | `many2one`  |     | ✅    | hr.employee.public      |
| `phone`                          | Phone                          | `char`      |     |       |                         |
| `resource_calendar_id`           | Resource Calendar              | `many2one`  |     | ✅    | resource.calendar       |
| `resource_id`                    | Resource                       | `many2one`  |     | ✅    | resource.resource       |
| `resume_line_ids`                | Resume lines                   | `one2many`  |     | ✅    | hr.resume.line          |
| `saturday_location_id`           | Saturday                       | `many2one`  |     | ✅    | hr.work.location        |
| `share`                          | Share User                     | `boolean`   |     |       |                         |
| `show_hr_icon_display`           | Show Hr Icon Display           | `boolean`   |     |       |                         |
| `show_leaves`                    | Able to see Remaining Time Off | `boolean`   |     |       |                         |
| `subordinate_ids`                | Subordinates                   | `one2many`  |     |       | hr.employee             |
| `sunday_location_id`             | Sunday                         | `many2one`  |     | ✅    | hr.work.location        |
| `thursday_location_id`           | Thursday                       | `many2one`  |     | ✅    | hr.work.location        |
| `today_location_name`            | Today Location Name            | `char`      |     | ✅    |                         |
| `tuesday_location_id`            | Tuesday                        | `many2one`  |     | ✅    | hr.work.location        |
| `tz`                             | Timezone                       | `selection` |     |       |                         |
| `user_id`                        | User                           | `many2one`  |     | ✅    | res.users               |
| `user_partner_id`                | User's partner                 | `many2one`  |     |       | res.partner             |
| `wednesday_location_id`          | Wednesday                      | `many2one`  |     | ✅    | hr.work.location        |
| `work_contact_id`                | Work Contact                   | `many2one`  |     | ✅    | res.partner             |
| `work_email`                     | Work Email                     | `char`      |     | ✅    |                         |
| `work_location_id`               | Work Location                  | `many2one`  |     | ✅    | hr.work.location        |
| `work_location_name`             | Work Location Name             | `char`      |     |       |                         |
| `work_location_type`             | Work Location Type             | `selection` |     |       |                         |
| `work_phone`                     | Work Phone                     | `char`      |     | ✅    |                         |
| `write_date`                     | Last Updated on                | `datetime`  |     | ✅    |                         |
| `write_uid`                      | Last Updated by                | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name               | Group       | Perms |
| ------------------ | ----------- | ----- |
| hr.employee_public | Role / User | `R`   |

**Record Rules:**

- **Employee multi company rule** (Global) `R/W/C/D`
  - Domain:
    `['|', '|', '|',         ('company_id', 'in', company_ids + [False]),         ('parent_id.user_id', '=', user.id),         ('id', '=', user.employee_id.parent_id.id),         ('user_id', '=', user.id)     ]`

### 🗃️ `resource.resource` — Resources

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label                | Type        | Req | Store | Relation          |
| ---------------------- | -------------------- | ----------- | --- | ----- | ----------------- |
| `active`               | Active               | `boolean`   |     | ✅    |                   |
| `avatar_128`           | Avatar 128           | `binary`    |     |       |                   |
| `calendar_id`          | Working Time         | `many2one`  |     | ✅    | resource.calendar |
| `color`                | Color                | `integer`   |     | ✅    |                   |
| `company_id`           | Company              | `many2one`  |     | ✅    | res.company       |
| `create_date`          | Created on           | `datetime`  |     | ✅    |                   |
| `create_uid`           | Created by           | `many2one`  |     | ✅    | res.users         |
| `department_id`        | Department           | `many2one`  |     |       | hr.department     |
| `display_name`         | Display Name         | `char`      |     |       |                   |
| `email`                | Email                | `char`      |     |       |                   |
| `employee_id`          | Employee             | `one2many`  |     | ✅    | hr.employee       |
| `employee_skill_ids`   | Skills               | `one2many`  |     |       | hr.employee.skill |
| `hr_icon_display`      | Hr Icon Display      | `selection` |     |       |                   |
| `id`                   | ID                   | `integer`   |     | ✅    |                   |
| `im_status`            | IM Status            | `char`      |     |       |                   |
| `job_title`            | Job Title            | `char`      |     |       |                   |
| `leave_date_to`        | To Date              | `date`      |     |       |                   |
| `name`                 | Name                 | `char`      | ✅  | ✅    |                   |
| `phone`                | Phone                | `char`      |     |       |                   |
| `resource_type`        | Type                 | `selection` | ✅  | ✅    |                   |
| `share`                | Share User           | `boolean`   |     |       |                   |
| `show_hr_icon_display` | Show Hr Icon Display | `boolean`   |     |       |                   |
| `time_efficiency`      | Efficiency Factor    | `float`     | ✅  | ✅    |                   |
| `tz`                   | Timezone             | `selection` | ✅  | ✅    |                   |
| `user_id`              | User                 | `many2one`  |     | ✅    | res.users         |
| `work_email`           | Work Email           | `char`      |     |       |                   |
| `work_location_id`     | Work Location        | `many2one`  |     |       | hr.work.location  |
| `work_phone`           | Work Phone           | `char`      |     |       |                   |
| `write_date`           | Last Updated on      | `datetime`  |     | ✅    |                   |
| `write_uid`            | Last Updated by      | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                                     | Group                                     | Perms     |
| ---------------------------------------- | ----------------------------------------- | --------- |
| resource.resource.user                   | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.employee.resource.manager             | Employees / Administrator                 | `R/W/C/D` |
| name_resource_resource_back_office_admin | OpenEduCat / Manager                      | `R/W/C`   |
| resource.resource                        | Role / Administrator                      | `R`       |
| resource.resource all                    | Role / User                               | `R`       |

**Record Rules:**

- **resource.resource multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `resource.calendar.leaves` — Resource Time Off Detail

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                     | Type        | Req | Store | Relation          |
| ---------------------------- | ------------------------- | ----------- | --- | ----- | ----------------- |
| `calendar_id`                | Working Hours             | `many2one`  |     | ✅    | resource.calendar |
| `company_id`                 | Company                   | `many2one`  |     | ✅    | res.company       |
| `create_date`                | Created on                | `datetime`  |     | ✅    |                   |
| `create_uid`                 | Created by                | `many2one`  |     | ✅    | res.users         |
| `date_from`                  | Start Date                | `datetime`  | ✅  | ✅    |                   |
| `date_to`                    | End Date                  | `datetime`  | ✅  | ✅    |                   |
| `display_name`               | Display Name              | `char`      |     |       |                   |
| `elligible_for_accrual_rate` | Eligible for Accrual Rate | `boolean`   |     | ✅    |                   |
| `holiday_id`                 | Time Off Request          | `many2one`  |     | ✅    | hr.leave          |
| `id`                         | ID                        | `integer`   |     | ✅    |                   |
| `name`                       | Reason                    | `char`      |     | ✅    |                   |
| `resource_id`                | Resource                  | `many2one`  |     | ✅    | resource.resource |
| `time_type`                  | Time Type                 | `selection` |     | ✅    |                   |
| `write_date`                 | Last Updated on           | `datetime`  |     | ✅    |                   |
| `write_uid`                  | Last Updated by           | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                          | Group                                   | Perms     |
| ----------------------------- | --------------------------------------- | --------- |
| resource_calendar_leaves_user | Time Off / Officer: Manage all requests | `R/W/C/D` |
| resource.calendar.leaves      | Role / Administrator                    | `R/W/C/D` |
| resource.calendar.leaves      | Role / User                             | `R/W/C/D` |

**Record Rules:**

- **resource.calendar.leaves: employee reads own or global** (1) `R`
  - Domain:
    `['|', ('resource_id', '=', False), ('resource_id.user_id', 'in', [False, user.id])]`
- **resource.calendar.leaves: employee modifies own** (1) `W/C/D`
  - Domain:
    `[('resource_id', '!=', False), ('resource_id.user_id', 'in', [False, user.id])]`
- **resource.calendar.leaves: admin modifies global** (2) `W/C/D`
  - Domain: `[('resource_id', '=', False)]`
- **resource.calendar.leaves: multi-company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Time Off Resources: Approver** (1) `R`
  - Domain: `[(1,'=',1)]`
- **Time Off Resources: All Approver** (80) `R/W/C/D`
  - Domain: `[(1,'=',1)]`

### 🗃️ `resource.calendar` — Resource Working Time

Calendar model for a resource. It has

    - attendance_ids: list of resource.calendar.attendance that are a working
                    interval in a given weekday.
    - leave_ids: list of leaves linked to this calendar. A leave can be general
                or linked to a specific resource, depending on its resource_id.

    All methods in this class use intervals. An interval is a tuple holding
    (begin_datetime, end_datetime). A list of intervals is therefore a list of
    tuples, holding several intervals of work or leaves.

**Fields:**

| Field                      | Label                        | Type        | Req | Store | Relation                     |
| -------------------------- | ---------------------------- | ----------- | --- | ----- | ---------------------------- |
| `active`                   | Active                       | `boolean`   |     | ✅    |                              |
| `associated_leaves_count`  | Time Off Count               | `integer`   |     |       |                              |
| `attendance_ids`           | Working Time                 | `one2many`  |     | ✅    | resource.calendar.attendance |
| `attendance_ids_1st_week`  | Working Time 1st Week        | `one2many`  |     |       | resource.calendar.attendance |
| `attendance_ids_2nd_week`  | Working Time 2nd Week        | `one2many`  |     |       | resource.calendar.attendance |
| `company_id`               | Company                      | `many2one`  |     | ✅    | res.company                  |
| `create_date`              | Created on                   | `datetime`  |     | ✅    |                              |
| `create_uid`               | Created by                   | `many2one`  |     | ✅    | res.users                    |
| `display_name`             | Display Name                 | `char`      |     |       |                              |
| `duration_based`           | Attendance based on duration | `boolean`   |     | ✅    |                              |
| `flexible_hours`           | Flexible Hours               | `boolean`   |     | ✅    |                              |
| `full_time_required_hours` | Full Time Equivalent         | `float`     |     | ✅    |                              |
| `global_leave_ids`         | Global Time Off              | `one2many`  |     | ✅    | resource.calendar.leaves     |
| `hours_per_day`            | Average Hour per Day         | `float`     |     | ✅    |                              |
| `hours_per_week`           | Hours per Week               | `float`     |     | ✅    |                              |
| `id`                       | ID                           | `integer`   |     | ✅    |                              |
| `is_fulltime`              | Is Full Time                 | `boolean`   |     |       |                              |
| `leave_ids`                | Time Off                     | `one2many`  |     | ✅    | resource.calendar.leaves     |
| `name`                     | Name                         | `char`      | ✅  | ✅    |                              |
| `schedule_type`            | Schedule Type                | `selection` | ✅  | ✅    |                              |
| `two_weeks_calendar`       | Calendar in 2 weeks mode     | `boolean`   |     | ✅    |                              |
| `two_weeks_explanation`    | Explanation                  | `char`      |     |       |                              |
| `tz`                       | Timezone                     | `selection` | ✅  | ✅    |                              |
| `tz_offset`                | Timezone offset              | `char`      |     |       |                              |
| `work_resources_count`     | Work Resources count         | `integer`   |     |       |                              |
| `work_time_rate`           | Work Time Rate               | `float`     |     |       |                              |
| `write_date`               | Last Updated on              | `datetime`  |     | ✅    |                              |
| `write_uid`                | Last Updated by              | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                               | Group                                     | Perms     |
| ---------------------------------- | ----------------------------------------- | --------- |
| hr.employee.resource.calendar.user | Employees / Officer: Manage all employees | `R/W/C/D` |
| resource.calendar.system           | Role / Administrator                      | `R/W/C/D` |
| resource.calendar.user             | Role / User                               | `R`       |

### 🗃️ `hr.leave.report.calendar` — Time Off Calendar

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label                | Type        | Req | Store | Relation      |
| ---------------------- | -------------------- | ----------- | --- | ----- | ------------- |
| `company_id`           | Company              | `many2one`  |     | ✅    | res.company   |
| `department_id`        | Department           | `many2one`  |     | ✅    | hr.department |
| `description`          | Description          | `char`      |     | ✅    |               |
| `display_name`         | Display Name         | `char`      |     |       |               |
| `duration`             | Duration             | `float`     |     | ✅    |               |
| `duration_display`     | Requested            | `char`      |     |       |               |
| `employee_id`          | Employee             | `many2one`  |     | ✅    | hr.employee   |
| `holiday_status_id`    | Time Off Type        | `many2one`  |     | ✅    | hr.leave.type |
| `id`                   | ID                   | `integer`   |     | ✅    |               |
| `is_absent`            | Absent Today         | `boolean`   |     |       |               |
| `is_hatched`           | Hatched              | `boolean`   |     | ✅    |               |
| `is_manager`           | Manager              | `boolean`   |     |       |               |
| `is_striked`           | Striked              | `boolean`   |     | ✅    |               |
| `job_id`               | Job                  | `many2one`  |     | ✅    | hr.job        |
| `leave_id`             | Leave                | `many2one`  |     | ✅    | hr.leave      |
| `leave_manager_id`     | Time Off Approver    | `many2one`  |     |       | res.users     |
| `member_of_department` | Member of department | `boolean`   |     |       |               |
| `name`                 | Name                 | `char`      |     |       |               |
| `start_datetime`       | From                 | `datetime`  |     | ✅    |               |
| `state`                | State                | `selection` |     | ✅    |               |
| `stop_datetime`        | To                   | `datetime`  |     | ✅    |               |
| `tz`                   | Timezone             | `selection` |     | ✅    |               |
| `user_id`              | User                 | `many2one`  |     | ✅    | res.users     |

**Access Rights:**

| Name                            | Group       | Perms |
| ------------------------------- | ----------- | ----- |
| access_hr_leave_report_calendar | Role / User | `R`   |

**Record Rules:**

- **Time Off Report Calendar: multi company global rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `hr.leave.report` — Time Off Summary / Report

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation            |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------- |
| `allocation_id`                 | Allocation Request            | `many2one`  |     | ✅    | hr.leave.allocation |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company         |
| `date_from`                     | Start Date                    | `datetime`  |     | ✅    |                     |
| `date_to`                       | End Date                      | `datetime`  |     | ✅    |                     |
| `department_id`                 | Department                    | `many2one`  |     | ✅    | hr.department       |
| `display_name`                  | Display Name                  | `char`      |     |       |                     |
| `employee_id`                   | Employee                      | `many2one`  |     | ✅    | hr.employee         |
| `has_department_manager_access` | Has Department Manager Access | `boolean`   |     |       |                     |
| `holiday_status_id`             | Time Off Type                 | `many2one`  |     | ✅    | hr.leave.type       |
| `id`                            | ID                            | `integer`   |     | ✅    |                     |
| `leave_id`                      | Time Off Request              | `many2one`  |     | ✅    | hr.leave            |
| `leave_type`                    | Request Type                  | `selection` |     | ✅    |                     |
| `name`                          | Description                   | `char`      |     | ✅    |                     |
| `number_of_days`                | Number of Days                | `float`     |     | ✅    |                     |
| `number_of_hours`               | Number of Hours               | `float`     |     | ✅    |                     |
| `state`                         | Status                        | `selection` |     | ✅    |                     |

**Access Rights:**

| Name                   | Group       | Perms |
| ---------------------- | ----------- | ----- |
| access_hr_leave_report | Role / User | `R`   |

**Record Rules:**

- **Time Off Report: multi company global rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Time Off Summary / Report: Internal User** (1) `R`
  - Domain: `[('has_department_manager_access', '=', True)]`
- **Time Off Summary / Report: All Approver** (80) `R`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `hr.leave.employee.type.report` — Time Off Summary / Report

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label           | Type        | Req | Store | Relation      |
| ----------------- | --------------- | ----------- | --- | ----- | ------------- |
| `active_employee` | Active Employee | `boolean`   |     | ✅    |               |
| `company_id`      | Company         | `many2one`  |     | ✅    | res.company   |
| `date_from`       | Start Date      | `datetime`  |     | ✅    |               |
| `date_to`         | End Date        | `datetime`  |     | ✅    |               |
| `department_id`   | Department      | `many2one`  |     | ✅    | hr.department |
| `display_name`    | Display Name    | `char`      |     |       |               |
| `employee_id`     | Employee        | `many2one`  |     | ✅    | hr.employee   |
| `holiday_status`  | Holiday Status  | `selection` |     | ✅    |               |
| `id`              | ID              | `integer`   |     | ✅    |               |
| `leave_type`      | Time Off Type   | `many2one`  |     | ✅    | hr.leave.type |
| `number_of_days`  | Number of Days  | `float`     |     | ✅    |               |
| `number_of_hours` | Number of Hours | `float`     |     | ✅    |               |
| `state`           | Status          | `selection` |     | ✅    |               |

**Access Rights:**

| Name                                         | Group                    | Perms |
| -------------------------------------------- | ------------------------ | ----- |
| access_hr_leave_employee_type_report_manager | Time Off / Administrator | `R/W` |

### 🗃️ `hr.leave.type` — Time Off Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                 | Label                           | Type        | Req | Store | Relation              |
| ------------------------------------- | ------------------------------- | ----------- | --- | ----- | --------------------- |
| `accrual_count`                       | Accruals count                  | `float`     |     |       |                       |
| `accruals_ids`                        | Accruals                        | `one2many`  |     | ✅    | hr.leave.accrual.plan |
| `active`                              | Active                          | `boolean`   |     | ✅    |                       |
| `allocation_count`                    | Allocations                     | `integer`   |     |       |                       |
| `allocation_notif_subtype_id`         | Allocation Notification Subtype | `many2one`  |     | ✅    | mail.message.subtype  |
| `allocation_validation_type`          | Approval                        | `selection` |     | ✅    |                       |
| `allow_request_on_top`                | Allow Request on Top            | `boolean`   |     | ✅    |                       |
| `allows_negative`                     | Allow Negative Cap              | `boolean`   |     | ✅    |                       |
| `color`                               | Color                           | `integer`   |     | ✅    |                       |
| `company_id`                          | Company                         | `many2one`  |     | ✅    | res.company           |
| `country_code`                        | Country Code                    | `char`      |     |       |                       |
| `country_id`                          | Country                         | `many2one`  |     | ✅    | res.country           |
| `create_calendar_meeting`             | Display Time Off in Calendar    | `boolean`   |     | ✅    |                       |
| `create_date`                         | Created on                      | `datetime`  |     | ✅    |                       |
| `create_uid`                          | Created by                      | `many2one`  |     | ✅    | res.users             |
| `display_name`                        | Display Name                    | `char`      |     |       |                       |
| `elligible_for_accrual_rate`          | Eligible for Accrual Rate       | `boolean`   |     | ✅    |                       |
| `employee_requests`                   | Allow Employee Requests         | `boolean`   | ✅  | ✅    |                       |
| `group_days_leave`                    | Group Time Off                  | `float`     |     |       |                       |
| `has_valid_allocation`                | Has Valid Allocation            | `boolean`   |     |       |                       |
| `hide_on_dashboard`                   | Hide On Dashboard               | `boolean`   |     | ✅    |                       |
| `icon_id`                             | Cover Image                     | `many2one`  |     | ✅    | ir.attachment         |
| `id`                                  | ID                              | `integer`   |     | ✅    |                       |
| `include_public_holidays_in_duration` | Ignore Public Holidays          | `boolean`   |     | ✅    |                       |
| `is_used`                             | Is Used                         | `boolean`   |     |       |                       |
| `leave_notif_subtype_id`              | Time Off Notification Subtype   | `many2one`  |     | ✅    | mail.message.subtype  |
| `leaves_taken`                        | Time off Already Taken          | `float`     |     |       |                       |
| `leave_validation_type`               | Time Off Validation             | `selection` |     | ✅    |                       |
| `max_allowed_negative`                | Maximum Excess Amount           | `integer`   |     | ✅    |                       |
| `max_leaves`                          | Maximum Allowed                 | `float`     |     |       |                       |
| `name`                                | Time Off Type                   | `char`      | ✅  | ✅    |                       |
| `request_unit`                        | Duration Type                   | `selection` | ✅  | ✅    |                       |
| `requires_allocation`                 | Requires allocation             | `boolean`   | ✅  | ✅    |                       |
| `responsible_ids`                     | Notify HR                       | `many2many` |     | ✅    | res.users             |
| `sequence`                            | Sequence                        | `integer`   |     | ✅    |                       |
| `support_document`                    | Supporting Document             | `boolean`   |     | ✅    |                       |
| `time_type`                           | Kind of Time Off                | `selection` |     | ✅    |                       |
| `unpaid`                              | Is Unpaid                       | `boolean`   |     | ✅    |                       |
| `virtual_remaining_leaves`            | Virtual Remaining Time Off      | `float`     |     |       |                       |
| `write_date`                          | Last Updated on                 | `datetime`  |     | ✅    |                       |
| `write_uid`                           | Last Updated by                 | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                        | Group                                   | Perms     |
| --------------------------- | --------------------------------------- | --------- |
| hr.holidays.status user     | Time Off / Officer: Manage all requests | `R`       |
| hr.holidays.status manager  | Time Off / Administrator                | `R/W/C/D` |
| hr.holidays.status employee | Role / User                             | `R`       |

**Record Rules:**

- **Time Off multi company rule** (Global) `R/W/C/D`
  - Domain:
    `[         '|',              ('company_id', 'in', company_ids),             '&',                 ('company_id', '=', False),                 ('country_id', 'in', user.env.companies.country_id.ids + [False])     ]     `

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
