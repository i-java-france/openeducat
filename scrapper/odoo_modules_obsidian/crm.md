---
title: "CRM"
module: "crm"
state: "installed"
version: "19.0.1.9"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/app/crm"
license: "LGPL-3"
category: "CRM"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/___, odoo/app]
---

# 🟢 CRM

> **Module:** `crm` | **Version:** `19.0.1.9` **Category:** CRM | **License:** `LGPL-3`
> **Author:** Odoo S.A. **Website:** https://www.odoo.com/app/crm

## 🔗 Dependencies

[[base_setup]] [[sales_team]] [[mail]] [[calendar]] [[resource]] [[utm]] [[web_tour]]
[[contacts]] [[digest]] [[phone_validation]]

## 📖 Description

# Odoo CRM

Boost sales productivity, improve win rates, grow revenue with the Odoo
<a href="<https://www.odoo.com/app/crm>">Open Source CRM</a>.

Manage your sales funnel with no effort. Attract leads, follow-up on phone calls and
meetings. Analyse the quality of your leads to make informed decisions and save time by
integrating emails directly into the application.

# Your Sales Funnel, The Way You Like It

Track your opportunities pipeline with the revolutionary kanban view. Work inside your
sales funnel and get instant visual information about next actions, new messages, top
opportunities and expected revenues.

# Lead Management Made Easy

Create leads automatically from incoming emails. Analyse leads efficiency and compare
performance by campaigns, channels or Sales Team.

Find duplicates, merge leads and assign them to the right salesperson in one operation.
Spend less time on administration and more time on qualifying leads.

# Organize Your Opportunities

Get your opportunities organized to stay focused on the best deals. Manage all your
customer interactions from the opportunity like emails, phone calls, internal notes,
meetings and quotations.

Follow opportunities that interest you to get notified upon specific events: deal won or
lost, stage changed, new customer demand, etc.

# Email Integration and Automation

Work with the email applications you already use every day. Whether your company uses
Microsoft Outlook or Gmail, no one needs to change the way they work, so everyone stays
productive.

Route, sort and filter incoming emails automatically. Odoo CRM handles incoming emails
and route them to the right opportunities or Sales Team. New leads are created on the
fly and interested salespersons are notified automatically.

# Collaborative Agenda

Schedule your meetings and phone calls using the integrated calendar. You can see your
agenda and your colleagues' in one view. As a manager, it's easy to see what your team
is busy with.

# Lead Automation and Marketing Campaigns

Drive performance by automating tasks with Odoo
<a href="<https://www.odoo.com/app/crm>">CRM</a>.

Use our marketing campaigns to automate lead acquisition, follow ups and promotions.
Define automation rules (e.g. ask a salesperson to call, send an email, ...) based on
triggers (no activity since 20 days, answered a promotional email, etc.)

Optimize campaigns from lead to close, on every channel. Make smarter decisions about
where to invest and show the impact of your marketing activities on your company's
bottom line.

# Customize Your Sales Cycle

Customize your sales cycle by configuring sales stages that perfectly fit your sales
approach. Control statistics to get accurate forecasts to improve your sales performance
at every stage of your customer relationship.

# Drive Engagement with Gamification

### Leverage your team's natural desire for competition

Reinforce good habits and improve win rates with real-time recognition and rewards
inspired by [game mechanics](http://en.wikipedia.org/wiki/Gamification). Align Sales
Teams around clear business objectives with challenges, personal objectives and team
leader boards.

### Leaderboards

Promote leaders and competition amongst Sales Team with performance ratios.

### Personal Objectives

Assign clear goals to users to align them with the company objectives.

### Team Targets

Compare revenues with forecasts and budgets in real time.

## 🖥️ UI Components

### Menus

- `CRM`
- `CRM/Configuration`
- `CRM/Configuration/Activities`
- `CRM/Configuration/Activities/Activity Plans`
- `CRM/Configuration/Activities/Activity Types`
- `CRM/Configuration/Opportunities`
- `CRM/Configuration/Pipeline`
- `CRM/Configuration/Pipeline/Lost Reasons`
- `CRM/Configuration/Pipeline/Stages`
- `CRM/Configuration/Pipeline/Tags`
- `CRM/Configuration/Recurring Plans`
- `CRM/Configuration/Sales Teams`
- `CRM/Configuration/Settings`
- `CRM/Configuration/Teams Members`
- `CRM/Import & Synchronize`
- `CRM/Leads`
- `CRM/Reporting`
- `CRM/Reporting/Activities`
- `CRM/Reporting/Forecast`
- `CRM/Reporting/Leads`
- `CRM/Reporting/Pipeline`
- `CRM/Sales`
- `CRM/Sales/Customers`
- `CRM/Sales/My Activities`
- `CRM/Sales/My Pipeline`
- `CRM/Sales/Teams`

### Views

- `* INHERIT calendar.event.form.inherit (search)`
- `* INHERIT crm.lead.list.activities (list)`
- `* INHERIT crm.lead.list.lead.reporting (list)`
- `* INHERIT crm.lead.list.opportunity.reporting (list)`
- `* INHERIT crm.lead.search.myactivities (search)`
- `* INHERIT crm.lead.view.kanban.forecast (kanban)`
- `* INHERIT crm.lead.view.list.forecast (list)`
- `* INHERIT crm.lead.view.search.forecast (search)`
- `* INHERIT crm.team.form.inherit (form)`
- `* INHERIT crm.team.list.inherit.crm (list)`
- `* INHERIT crm.team.member.view.form.inherit.crm (form)`
- `* INHERIT crm.team.member.view.kanban.inherit.crm (kanban)`
- `* INHERIT crm.team.member.view.list (list)`
- `* INHERIT crm.team.view.kanban.dashboard.inherit.crm (kanban)`
- `* INHERIT digest.digest.view.form.inherit.crm.lead (form)`
- `* INHERIT res.config.settings.view.form.inherit.crm (form)`
- `* INHERIT utm.campaign.view.form (form)`
- `* INHERIT utm.campaign.view.kanban (kanban)`
- `* INHERIT view.res.partner.form.crm.inherited1 (form)`
- `Stage - Search (search)`
- `crm action helper (qweb)`
- `crm.activity.report.graph (graph)`
- `crm.activity.report.list (list)`
- `crm.activity.report.pivot (pivot)`
- `crm.activity.report.search (search)`
- `crm.lead.calendar.lead (calendar)`
- `crm.lead.form (form)`
- `crm.lead.form.quick_create (form)`
- `crm.lead.kanban (kanban)`
- `crm.lead.kanban.lead (kanban)`
- `crm.lead.list.lead (list)`
- `crm.lead.list.opportunity (list)`
- `crm.lead.lost.form (form)`
- `crm.lead.pls.update.view.form (form)`
- `crm.lead.search (search)`
- `crm.lead.search.lead (search)`
- `crm.lead.search.opportunity (search)`
- `crm.lead.view.activity (activity)`
- `crm.lead.view.graph (graph)`
- `crm.lead.view.graph.forecast (graph)`
- `crm.lead.view.pivot (pivot)`
- `crm.lead.view.pivot.forecast (pivot)`
- `crm.lead2opportunity.partner.form (form)`
- `crm.lead2opportunity.partner.mass.form (form)`
- `crm.lost.reason.form (form)`
- `crm.lost.reason.list (list)`
- `crm.lost.reason.view.search (search)`
- `crm.merge.opportunity.form (form)`
- `crm.opportunity.report.graph (graph)`
- `crm.opportunity.report.graph.lead (graph)`
- `crm.opportunity.report.pivot (pivot)`
- `crm.opportunity.report.view.pivot.lead (pivot)`
- `crm.recurring.plan.view.list (list)`
- `crm.recurring.plan.view.search (search)`
- `crm.stage.form (form)`
- `crm.stage.list (list)`
- `crm_lead_merge_summary (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**22 model(s) defined by this module:**

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

### 🗃️ `crm.lead` — Lead

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                | Label                                     | Type         | Req | Store | Relation                    |
| ------------------------------------ | ----------------------------------------- | ------------ | --- | ----- | --------------------------- |
| `active`                             | Active                                    | `boolean`    |     | ✅    |                             |
| `activity_calendar_event_id`         | Next Activity Calendar Event              | `many2one`   |     |       | calendar.event              |
| `activity_date_deadline`             | Next Activity Deadline                    | `date`       |     |       |                             |
| `activity_exception_decoration`      | Activity Exception Decoration             | `selection`  |     |       |                             |
| `activity_exception_icon`            | Icon                                      | `char`       |     |       |                             |
| `activity_ids`                       | Activities                                | `one2many`   |     | ✅    | mail.activity               |
| `activity_state`                     | Activity State                            | `selection`  |     |       |                             |
| `activity_summary`                   | Next Activity Summary                     | `char`       |     |       |                             |
| `activity_type_icon`                 | Activity Type Icon                        | `char`       |     |       |                             |
| `activity_type_id`                   | Next Activity Type                        | `many2one`   |     |       | mail.activity.type          |
| `activity_user_id`                   | Responsible User                          | `many2one`   |     |       | res.users                   |
| `automated_probability`              | Automated Probability                     | `float`      |     | ✅    |                             |
| `calendar_event_ids`                 | Meetings                                  | `one2many`   |     | ✅    | calendar.event              |
| `campaign_id`                        | Campaign                                  | `many2one`   |     | ✅    | utm.campaign                |
| `city`                               | City                                      | `char`       |     | ✅    |                             |
| `color`                              | Color Index                               | `integer`    |     | ✅    |                             |
| `commercial_partner_id`              | Customer Company                          | `many2one`   |     |       | res.partner                 |
| `company_currency`                   | Currency                                  | `many2one`   |     |       | res.currency                |
| `company_id`                         | Company                                   | `many2one`   |     | ✅    | res.company                 |
| `contact_name`                       | Contact Name                              | `char`       |     | ✅    |                             |
| `country_id`                         | Country                                   | `many2one`   |     | ✅    | res.country                 |
| `create_date`                        | Created on                                | `datetime`   |     | ✅    |                             |
| `create_uid`                         | Created by                                | `many2one`   |     | ✅    | res.users                   |
| `date_automation_last`               | Last Action                               | `datetime`   |     | ✅    |                             |
| `date_closed`                        | Closed Date                               | `datetime`   |     | ✅    |                             |
| `date_conversion`                    | Conversion Date                           | `datetime`   |     | ✅    |                             |
| `date_deadline`                      | Expected Closing                          | `date`       |     | ✅    |                             |
| `date_last_stage_update`             | Last Stage Update                         | `datetime`   |     | ✅    |                             |
| `date_open`                          | Assignment Date                           | `datetime`   |     | ✅    |                             |
| `day_close`                          | Days to Close                             | `float`      |     | ✅    |                             |
| `day_open`                           | Days to Assign                            | `float`      |     | ✅    |                             |
| `description`                        | Notes                                     | `html`       |     | ✅    |                             |
| `display_name`                       | Display Name                              | `char`       |     |       |                             |
| `duplicate_lead_count`               | Potential Duplicate Lead Count            | `integer`    |     |       |                             |
| `duplicate_lead_ids`                 | Potential Duplicate Lead                  | `many2many`  |     |       | crm.lead                    |
| `duration_tracking`                  | Status time                               | `json`       |     |       |                             |
| `email_cc`                           | Email cc                                  | `char`       |     | ✅    |                             |
| `email_domain_criterion`             | Email Domain Criterion                    | `char`       |     | ✅    |                             |
| `email_from`                         | Email                                     | `char`       |     | ✅    |                             |
| `email_normalized`                   | Normalized Email                          | `char`       |     | ✅    |                             |
| `email_state`                        | Email Quality                             | `selection`  |     | ✅    |                             |
| `event_id`                           | Source Event                              | `many2one`   |     | ✅    | event.event                 |
| `event_lead_rule_id`                 | Registration Rule                         | `many2one`   |     | ✅    | event.lead.rule             |
| `expected_revenue`                   | Expected Revenue                          | `monetary`   |     | ✅    |                             |
| `function`                           | Job Position                              | `char`       |     | ✅    |                             |
| `has_message`                        | Has Message                               | `boolean`    |     |       |                             |
| `iap_enrich_done`                    | Enrichment done                           | `boolean`    |     | ✅    |                             |
| `id`                                 | ID                                        | `integer`    |     | ✅    |                             |
| `is_automated_probability`           | Is automated probability?                 | `boolean`    |     |       |                             |
| `is_blacklisted`                     | Blacklist                                 | `boolean`    |     |       |                             |
| `is_partner_visible`                 | Is Partner Visible                        | `boolean`    |     |       |                             |
| `is_rotting`                         | Rotting                                   | `boolean`    |     |       |                             |
| `lang_active_count`                  | Lang Active Count                         | `integer`    |     |       |                             |
| `lang_code`                          | Locale Code                               | `char`       |     |       |                             |
| `lang_id`                            | Language                                  | `many2one`   |     | ✅    | res.lang                    |
| `lead_mining_request_id`             | Lead Mining Request                       | `many2one`   |     | ✅    | crm.iap.lead.mining.request |
| `lead_properties`                    | Properties                                | `properties` |     | ✅    |                             |
| `lost_reason_id`                     | Lost Reason                               | `many2one`   |     | ✅    | crm.lost.reason             |
| `medium_id`                          | Medium                                    | `many2one`   |     | ✅    | utm.medium                  |
| `meeting_display_date`               | Meeting Display Date                      | `date`       |     |       |                             |
| `meeting_display_label`              | Meeting Display Label                     | `char`       |     |       |                             |
| `message_attachment_count`           | Attachment Count                          | `integer`    |     |       |                             |
| `message_bounce`                     | Bounce                                    | `integer`    |     | ✅    |                             |
| `message_follower_ids`               | Followers                                 | `one2many`   |     | ✅    | mail.followers              |
| `message_has_error`                  | Message Delivery error                    | `boolean`    |     |       |                             |
| `message_has_error_counter`          | Number of errors                          | `integer`    |     |       |                             |
| `message_has_sms_error`              | SMS Delivery error                        | `boolean`    |     |       |                             |
| `message_ids`                        | Messages                                  | `one2many`   |     | ✅    | mail.message                |
| `message_is_follower`                | Is Follower                               | `boolean`    |     |       |                             |
| `message_needaction`                 | Action Needed                             | `boolean`    |     |       |                             |
| `message_needaction_counter`         | Number of Actions                         | `integer`    |     |       |                             |
| `message_partner_ids`                | Followers (Partners)                      | `many2many`  |     |       | res.partner                 |
| `my_activity_date_deadline`          | My Activity Deadline                      | `date`       |     |       |                             |
| `name`                               | Opportunity                               | `char`       | ✅  | ✅    |                             |
| `order_ids`                          | Orders                                    | `one2many`   |     | ✅    | sale.order                  |
| `origin_channel_id`                  | Live chat from which the lead was created | `many2one`   |     | ✅    | discuss.channel             |
| `origin_survey_id`                   | Survey                                    | `many2one`   |     | ✅    | survey.survey               |
| `partner_email_update`               | Partner Email will Update                 | `boolean`    |     |       |                             |
| `partner_id`                         | Contact                                   | `many2one`   |     | ✅    | res.partner                 |
| `partner_is_blacklisted`             | Partner is blacklisted                    | `boolean`    |     |       |                             |
| `partner_name`                       | Company Name                              | `char`       |     | ✅    |                             |
| `partner_phone_update`               | Partner Phone will Update                 | `boolean`    |     |       |                             |
| `phone`                              | Phone                                     | `char`       |     | ✅    |                             |
| `phone_blacklisted`                  | Blacklisted Phone is Phone                | `boolean`    |     |       |                             |
| `phone_mobile_search`                | Phone Number                              | `char`       |     |       |                             |
| `phone_sanitized`                    | Sanitized Number                          | `char`       |     | ✅    |                             |
| `phone_sanitized_blacklisted`        | Phone Blacklisted                         | `boolean`    |     |       |                             |
| `phone_state`                        | Phone Quality                             | `selection`  |     | ✅    |                             |
| `priority`                           | Priority                                  | `selection`  |     | ✅    |                             |
| `probability`                        | Probability                               | `float`      |     | ✅    |                             |
| `prorated_revenue`                   | Prorated Revenue                          | `monetary`   |     | ✅    |                             |
| `quotation_count`                    | Number of Quotations                      | `integer`    |     |       |                             |
| `rating_ids`                         | Ratings                                   | `one2many`   |     | ✅    | rating.rating               |
| `recurring_plan`                     | Recurring Plan                            | `many2one`   |     | ✅    | crm.recurring.plan          |
| `recurring_revenue`                  | Recurring Revenues                        | `monetary`   |     | ✅    |                             |
| `recurring_revenue_monthly`          | Expected MRR                              | `monetary`   |     | ✅    |                             |
| `recurring_revenue_monthly_prorated` | Prorated MRR                              | `monetary`   |     | ✅    |                             |
| `recurring_revenue_prorated`         | Prorated Recurring Revenues               | `monetary`   |     | ✅    |                             |
| `referred`                           | Referred By                               | `char`       |     | ✅    |                             |
| `registration_count`                 | # Registrations                           | `integer`    |     |       |                             |
| `registration_ids`                   | Source Registrations                      | `many2many`  |     | ✅    | event.registration          |
| `reveal_id`                          | Reveal ID                                 | `char`       |     | ✅    |                             |
| `rotting_days`                       | Days Rotting                              | `integer`    |     |       |                             |
| `sale_amount_total`                  | Sum of Orders                             | `monetary`   |     |       |                             |
| `sale_order_count`                   | Number of Sale Orders                     | `integer`    |     |       |                             |
| `show_enrich_button`                 | Allow manual enrich                       | `boolean`    |     |       |                             |
| `source_id`                          | Source                                    | `many2one`   |     | ✅    | utm.source                  |
| `stage_id`                           | Stage                                     | `many2one`   |     | ✅    | crm.stage                   |
| `stage_id_color`                     | Stage Color                               | `integer`    |     |       |                             |
| `state_id`                           | State                                     | `many2one`   |     | ✅    | res.country.state           |
| `street`                             | Street                                    | `char`       |     | ✅    |                             |
| `street2`                            | Street2                                   | `char`       |     | ✅    |                             |
| `student_id`                         | Student                                   | `many2one`   |     | ✅    | op.student                  |
| `tag_ids`                            | Tags                                      | `many2many`  |     | ✅    | crm.tag                     |
| `team_id`                            | Sales Team                                | `many2one`   |     | ✅    | crm.team                    |
| `type`                               | Type                                      | `selection`  | ✅  | ✅    |                             |
| `user_company_ids`                   | User Company                              | `many2many`  |     |       | res.company                 |
| `user_id`                            | Salesperson                               | `many2one`   |     | ✅    | res.users                   |
| `visitor_ids`                        | Web Visitors                              | `many2many`  |     | ✅    | website.visitor             |
| `visitor_page_count`                 | # Page Views                              | `integer`    |     |       |                             |
| `visitor_sessions_count`             | # Sessions                                | `integer`    |     |       |                             |
| `website`                            | Website                                   | `char`       |     | ✅    |                             |
| `website_message_ids`                | Website Messages                          | `one2many`   |     | ✅    | mail.message                |
| `won_status`                         | Won/Lost                                  | `selection`  |     | ✅    |                             |
| `write_date`                         | Last Updated on                           | `datetime`   |     | ✅    |                             |
| `write_uid`                          | Last Updated by                           | `many2one`   |     | ✅    | res.users                   |
| `zip`                                | Zip                                       | `char`       |     | ✅    |                             |

**Access Rights:**

| Name             | Group                            | Perms     |
| ---------------- | -------------------------------- | --------- |
| crm.lead         | Sales / User: Own Documents Only | `R/W/C`   |
| crm.lead.manager | Sales / Administrator            | `R/W/C/D` |

**Record Rules:**

- **Personal Leads** (25) `R/W/C/D`
  - Domain: `['|',('user_id','=',user.id),('user_id','=',False)]`
- **CRM Lead Multi-Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **All Leads** (26) `R/W/C/D`
  - Domain: `[(1,'=',1)]`

### 🗃️ `crm.team` — Sales Team

> 📧 Mail Thread

A mixin for models that inherits mail.alias to have a one-to-one relation between the
model and its alias.

**Fields:**

| Field                              | Label                                          | Type                    | Req | Store | Relation          |
| ---------------------------------- | ---------------------------------------------- | ----------------------- | --- | ----- | ----------------- |
| `abandoned_carts_amount`           | Amount of Abandoned Carts                      | `integer`               |     |       |                   |
| `abandoned_carts_count`            | Number of Abandoned Carts                      | `integer`               |     |       |                   |
| `active`                           | Active                                         | `boolean`               |     | ✅    |                   |
| `alias_bounced_content`            | Custom Bounced Message                         | `html`                  |     |       |                   |
| `alias_contact`                    | Alias Contact Security                         | `selection`             | ✅  |       |                   |
| `alias_defaults`                   | Default Values                                 | `text`                  | ✅  |       |                   |
| `alias_domain`                     | Alias Domain Name                              | `char`                  |     |       |                   |
| `alias_domain_id`                  | Alias Domain                                   | `many2one`              |     |       | mail.alias.domain |
| `alias_email`                      | Email Alias                                    | `char`                  |     |       |                   |
| `alias_force_thread_id`            | Record Thread ID                               | `integer`               |     |       |                   |
| `alias_full_name`                  | Alias Email                                    | `char`                  |     |       |                   |
| `alias_id`                         | Alias                                          | `many2one`              | ✅  | ✅    | mail.alias        |
| `alias_incoming_local`             | Local-part based incoming detection            | `boolean`               |     |       |                   |
| `alias_model_id`                   | Aliased Model                                  | `many2one`              | ✅  |       | ir.model          |
| `alias_name`                       | Alias Name                                     | `char`                  |     |       |                   |
| `alias_parent_model_id`            | Parent Model                                   | `many2one`              |     |       | ir.model          |
| `alias_parent_thread_id`           | Parent Record Thread ID                        | `integer`               |     |       |                   |
| `alias_status`                     | Alias Status                                   | `selection`             |     |       |                   |
| `assignment_auto_enabled`          | Auto Assignment                                | `boolean`               |     |       |                   |
| `assignment_domain`                | Assignment Domain                              | `char`                  |     | ✅    |                   |
| `assignment_enabled`               | Lead Assign                                    | `boolean`               |     |       |                   |
| `assignment_max`                   | Lead Average Capacity                          | `integer`               |     |       |                   |
| `assignment_optout`                | Skip auto assignment                           | `boolean`               |     | ✅    |                   |
| `color`                            | Color Index                                    | `integer`               |     | ✅    |                   |
| `company_id`                       | Company                                        | `many2one`              |     | ✅    | res.company       |
| `create_date`                      | Created on                                     | `datetime`              |     | ✅    |                   |
| `create_uid`                       | Created by                                     | `many2one`              |     | ✅    | res.users         |
| `crm_team_member_all_ids`          | Sales Team Members (incl. inactive)            | `one2many`              |     | ✅    | crm.team.member   |
| `crm_team_member_ids`              | Sales Team Members                             | `one2many`              |     | ✅    | crm.team.member   |
| `currency_id`                      | Currency                                       | `many2one`              |     |       | res.currency      |
| `dashboard_button_name`            | Dashboard Button                               | `char`                  |     |       |                   |
| `display_name`                     | Display Name                                   | `char`                  |     |       |                   |
| `favorite_user_ids`                | Favorite Members                               | `many2many`             |     | ✅    | res.users         |
| `has_message`                      | Has Message                                    | `boolean`               |     |       |                   |
| `id`                               | ID                                             | `integer`               |     | ✅    |                   |
| `invoiced`                         | Invoiced This Month                            | `float`                 |     |       |                   |
| `invoiced_target`                  | Invoicing Target                               | `float`                 |     | ✅    |                   |
| `is_favorite`                      | Show on dashboard                              | `boolean`               |     |       |                   |
| `is_membership_multi`              | Multiple Memberships Allowed                   | `boolean`               |     |       |                   |
| `lead_all_assigned_month_count`    | # Leads/Opps assigned this month               | `integer`               |     |       |                   |
| `lead_all_assigned_month_exceeded` | Exceed monthly lead assignement                | `boolean`               |     |       |                   |
| `lead_properties_definition`       | Lead Properties                                | `properties_definition` |     | ✅    |                   |
| `lead_unassigned_count`            | # Unassigned Leads                             | `integer`               |     |       |                   |
| `member_company_ids`               | Member Company                                 | `many2many`             |     |       | res.company       |
| `member_ids`                       | Salespersons                                   | `many2many`             |     |       | res.users         |
| `member_warning`                   | Membership Issue Warning                       | `text`                  |     |       |                   |
| `message_attachment_count`         | Attachment Count                               | `integer`               |     |       |                   |
| `message_follower_ids`             | Followers                                      | `one2many`              |     | ✅    | mail.followers    |
| `message_has_error`                | Message Delivery error                         | `boolean`               |     |       |                   |
| `message_has_error_counter`        | Number of errors                               | `integer`               |     |       |                   |
| `message_has_sms_error`            | SMS Delivery error                             | `boolean`               |     |       |                   |
| `message_ids`                      | Messages                                       | `one2many`              |     | ✅    | mail.message      |
| `message_is_follower`              | Is Follower                                    | `boolean`               |     |       |                   |
| `message_needaction`               | Action Needed                                  | `boolean`               |     |       |                   |
| `message_needaction_counter`       | Number of Actions                              | `integer`               |     |       |                   |
| `message_partner_ids`              | Followers (Partners)                           | `many2many`             |     |       | res.partner       |
| `name`                             | Sales Team                                     | `char`                  | ✅  | ✅    |                   |
| `origin_survey_ids`                | Survey opportunities related to the sales team | `one2many`              |     | ✅    | survey.survey     |
| `rating_ids`                       | Ratings                                        | `one2many`              |     | ✅    | rating.rating     |
| `sale_order_count`                 | # Sale Orders                                  | `integer`               |     |       |                   |
| `sequence`                         | Sequence                                       | `integer`               |     | ✅    |                   |
| `use_leads`                        | Leads                                          | `boolean`               |     | ✅    |                   |
| `use_opportunities`                | Pipeline                                       | `boolean`               |     | ✅    |                   |
| `user_id`                          | Team Leader                                    | `many2one`              |     | ✅    | res.users         |
| `website_ids`                      | Websites                                       | `one2many`              |     | ✅    | website           |
| `website_message_ids`              | Website Messages                               | `one2many`              |     | ✅    | mail.message      |
| `write_date`                       | Last Updated on                                | `datetime`              |     | ✅    |                   |
| `write_uid`                        | Last Updated by                                | `many2one`              |     | ✅    | res.users         |

**Access Rights:**

| Name             | Group                            | Perms     |
| ---------------- | -------------------------------- | --------- |
| crm.team.user    | Sales / User: Own Documents Only | `R`       |
| crm.team.manager | Sales / Administrator            | `R/W/C/D` |
| crm.team         | Role / User                      | `R`       |

**Record Rules:**

- **All Salesteam** (26) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Sales Team multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `crm.team.member` — Sales Team Member

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                               | Type        | Req | Store | Relation       |
| ----------------------------- | ----------------------------------- | ----------- | --- | ----- | -------------- |
| `active`                      | Active                              | `boolean`   |     | ✅    |                |
| `assignment_domain`           | Assignment Domain                   | `char`      |     | ✅    |                |
| `assignment_domain_preferred` | Preference assignment Domain        | `char`      |     | ✅    |                |
| `assignment_enabled`          | Lead Assign                         | `boolean`   |     |       |                |
| `assignment_max`              | Average Leads Capacity (on 30 days) | `integer`   |     | ✅    |                |
| `assignment_optout`           | Pause assignment                    | `boolean`   |     | ✅    |                |
| `company_id`                  | Company                             | `many2one`  |     |       | res.company    |
| `create_date`                 | Created on                          | `datetime`  |     | ✅    |                |
| `create_uid`                  | Created by                          | `many2one`  |     | ✅    | res.users      |
| `crm_team_id`                 | Sales Team                          | `many2one`  | ✅  | ✅    | crm.team       |
| `display_name`                | Display Name                        | `char`      |     |       |                |
| `email`                       | Email                               | `char`      |     |       |                |
| `has_message`                 | Has Message                         | `boolean`   |     |       |                |
| `id`                          | ID                                  | `integer`   |     | ✅    |                |
| `image_128`                   | Image (128)                         | `binary`    |     |       |                |
| `image_1920`                  | Image                               | `binary`    |     |       |                |
| `is_membership_multi`         | Multiple Memberships Allowed        | `boolean`   |     |       |                |
| `lead_day_count`              | Leads (last 24h)                    | `integer`   |     |       |                |
| `lead_month_count`            | Leads (30 days)                     | `integer`   |     |       |                |
| `member_warning`              | Member Warning                      | `text`      |     |       |                |
| `message_attachment_count`    | Attachment Count                    | `integer`   |     |       |                |
| `message_follower_ids`        | Followers                           | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`           | Message Delivery error              | `boolean`   |     |       |                |
| `message_has_error_counter`   | Number of errors                    | `integer`   |     |       |                |
| `message_has_sms_error`       | SMS Delivery error                  | `boolean`   |     |       |                |
| `message_ids`                 | Messages                            | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`         | Is Follower                         | `boolean`   |     |       |                |
| `message_needaction`          | Action Needed                       | `boolean`   |     |       |                |
| `message_needaction_counter`  | Number of Actions                   | `integer`   |     |       |                |
| `message_partner_ids`         | Followers (Partners)                | `many2many` |     |       | res.partner    |
| `name`                        | Name                                | `char`      |     |       |                |
| `phone`                       | Phone                               | `char`      |     |       |                |
| `rating_ids`                  | Ratings                             | `one2many`  |     | ✅    | rating.rating  |
| `user_company_ids`            | User Company                        | `many2many` |     |       | res.company    |
| `user_id`                     | Salesperson                         | `many2one`  | ✅  | ✅    | res.users      |
| `user_in_teams_ids`           | User In Teams                       | `many2many` |     |       | res.users      |
| `website_message_ids`         | Website Messages                    | `one2many`  |     | ✅    | mail.message   |
| `write_date`                  | Last Updated on                     | `datetime`  |     | ✅    |                |
| `write_uid`                   | Last Updated by                     | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                           | Group                 | Perms     |
| ------------------------------ | --------------------- | --------- |
| access.crm.team.member.manager | Sales / Administrator | `R/W/C/D` |
| access.crm.team.member.user    | Role / User           | `R`       |
| access.crm.team.member.all     | Everyone              | `-`       |

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

### 🗃️ `res.config.settings` — Config Settings

> ✳️ Transient (Wizard)

Enhanced configuration interface for exchange rate management

**Fields:**

| Field                                                | Label                                                                                           | Type        | Req | Store | Relation                         |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------- | --- | ----- | -------------------------------- |
| `access_token`                                       | Access Token                                                                                    | `char`      |     | ✅    |                                  |
| `account_cash_basis_base_account_id`                 | Base Tax Received Account                                                                       | `many2one`  |     |       | account.account                  |
| `account_default_credit_limit`                       | Default Credit Limit                                                                            | `monetary`  |     |       |                                  |
| `account_discount_expense_allocation_id`             | Customer Invoices Discounts Account                                                             | `many2one`  |     |       | account.account                  |
| `account_discount_income_allocation_id`              | Vendor Bills Discounts Account                                                                  | `many2one`  |     |       | account.account                  |
| `account_fiscal_country_id`                          | Fiscal Country Code                                                                             | `many2one`  |     |       | res.country                      |
| `account_journal_early_pay_discount_gain_account_id` | Early Discount Gain                                                                             | `many2one`  |     |       | account.account                  |
| `account_journal_early_pay_discount_loss_account_id` | Early Discount Loss                                                                             | `many2one`  |     |       | account.account                  |
| `account_journal_suspense_account_id`                | Bank Suspense                                                                                   | `many2one`  |     |       | account.account                  |
| `account_on_checkout`                                | Customer Accounts                                                                               | `selection` | ✅  |       |                                  |
| `account_price_include`                              | Default Sales Price Include                                                                     | `selection` | ✅  |       |                                  |
| `account_storno`                                     | Storno accounting                                                                               | `boolean`   |     |       |                                  |
| `account_use_credit_limit`                           | Sales Credit Limit                                                                              | `boolean`   |     |       |                                  |
| `active_provider_id`                                 | Active Provider                                                                                 | `many2one`  |     |       | payment.provider                 |
| `active_user_count`                                  | Number of Active Users                                                                          | `integer`   |     |       |                                  |
| `add_to_cart_action`                                 | Add To Cart Action                                                                              | `selection` |     |       |                                  |
| `alias_domain_id`                                    | Alias Domain                                                                                    | `many2one`  |     |       | mail.alias.domain                |
| `anglo_saxon_accounting`                             | Use anglo-saxon accounting                                                                      | `boolean`   |     |       |                                  |
| `annual_inventory_day`                               | Day of the month                                                                                | `integer`   |     |       |                                  |
| `annual_inventory_month`                             | Annual Inventory Month                                                                          | `selection` |     |       |                                  |
| `app_login_details_show`                             | Replace Login URL                                                                               | `boolean`   |     | ✅    |                                  |
| `app_login_name`                                     | Login Page Name                                                                                 | `char`      |     | ✅    |                                  |
| `app_login_url`                                      | Login Page URL                                                                                  | `char`      |     | ✅    |                                  |
| `app_ribbon_name`                                    | Show Demo Ribbon                                                                                | `char`      |     | ✅    |                                  |
| `app_ribbon_name_show`                               | Show Ribbon                                                                                     | `boolean`   |     | ✅    |                                  |
| `app_show_lang`                                      | Show Quick Language Switcher                                                                    | `boolean`   |     | ✅    |                                  |
| `app_system_name`                                    | System Name                                                                                     | `char`      |     | ✅    |                                  |
| `attendance_subject_generic`                         | Attendance Subject Generic                                                                      | `selection` |     | ✅    |                                  |
| `auth_signup_reset_password`                         | Enable password reset from Login page                                                           | `boolean`   |     | ✅    |                                  |
| `auth_signup_template_user_id`                       | Template user for new users created through signup                                              | `many2one`  |     | ✅    | res.users                        |
| `auth_signup_uninvited`                              | Customer Account                                                                                | `selection` |     |       |                                  |
| `auth_totp_enforce`                                  | Enforce two-factor authentication                                                               | `boolean`   |     | ✅    |                                  |
| `auth_totp_policy`                                   | Two-factor authentication enforcing policy                                                      | `selection` |     | ✅    |                                  |
| `automatic_email`                                    | Automatic Email                                                                                 | `boolean`   |     | ✅    |                                  |
| `automatic_invoice`                                  | Automatic Invoice                                                                               | `boolean`   |     | ✅    |                                  |
| `autopost_bills`                                     | Auto-validate bills                                                                             | `boolean`   |     |       |                                  |
| `barcode_nomenclature_id`                            | Nomenclature                                                                                    | `many2one`  |     |       | barcode.nomenclature             |
| `barcode_separator`                                  | Separator                                                                                       | `char`      |     | ✅    |                                  |
| `cart_abandoned_delay`                               | Abandoned Delay                                                                                 | `float`     |     |       |                                  |
| `cart_recovery_mail_template`                        | Cart Recovery Email                                                                             | `many2one`  |     |       | mail.template                    |
| `cdn_activated`                                      | Content Delivery Network (CDN)                                                                  | `boolean`   |     |       |                                  |
| `cdn_filters`                                        | CDN Filters                                                                                     | `text`      |     |       |                                  |
| `cdn_url`                                            | CDN Base URL                                                                                    | `char`      |     |       |                                  |
| `channel_id`                                         | Website Live Channel                                                                            | `many2one`  |     |       | im_livechat.channel              |
| `chart_template`                                     | Chart Template                                                                                  | `selection` |     | ✅    |                                  |
| `client_id`                                          | Client ID                                                                                       | `char`      |     | ✅    |                                  |
| `client_secret`                                      | Client Secret                                                                                   | `char`      |     | ✅    |                                  |
| `company_count`                                      | Number of Companies                                                                             | `integer`   |     |       |                                  |
| `company_country_code`                               | Company Country Code                                                                            | `char`      |     |       |                                  |
| `company_country_group_codes`                        | Country Group Codes                                                                             | `json`      |     |       |                                  |
| `company_currency_id`                                | Company Currency                                                                                | `many2one`  |     |       | res.currency                     |
| `company_expense_allowed_payment_method_line_ids`    | Payment methods available for expenses paid by company                                          | `many2many` |     |       | account.payment.method.line      |
| `company_id`                                         | Company                                                                                         | `many2one`  | ✅  | ✅    | res.company                      |
| `company_informations`                               | Company Informations                                                                            | `text`      |     |       |                                  |
| `company_name`                                       | Company Name                                                                                    | `char`      |     |       |                                  |
| `company_so_template_id`                             | Default Template                                                                                | `many2one`  |     |       | sale.order.template              |
| `confirmation_email_template_id`                     | Confirmation Email Template                                                                     | `many2one`  |     |       | mail.template                    |
| `contract_expiration_notice_period`                  | Contract Expiry Notice Period                                                                   | `integer`   |     |       |                                  |
| `country_code`                                       | Country Code                                                                                    | `char`      |     |       |                                  |
| `create_date`                                        | Created on                                                                                      | `datetime`  |     | ✅    |                                  |
| `create_uid`                                         | Created by                                                                                      | `many2one`  |     | ✅    | res.users                        |
| `crm_auto_assignment_action`                         | Auto Assignment Action                                                                          | `selection` |     | ✅    |                                  |
| `crm_auto_assignment_interval_number`                | Repeat every                                                                                    | `integer`   |     | ✅    |                                  |
| `crm_auto_assignment_interval_type`                  | Auto Assignment Interval Unit                                                                   | `selection` |     | ✅    |                                  |
| `crm_auto_assignment_run_datetime`                   | Auto Assignment Next Execution Date                                                             | `datetime`  |     | ✅    |                                  |
| `crm_use_auto_assignment`                            | Rule-Based Assignment                                                                           | `boolean`   |     | ✅    |                                  |
| `currency_exchange_journal_id`                       | Currency Exchange Journal                                                                       | `many2one`  |     |       | account.journal                  |
| `currency_id`                                        | Currency                                                                                        | `many2one`  | ✅  |       | res.currency                     |
| `days_to_purchase`                                   | Days to Purchase                                                                                | `float`     |     |       |                                  |
| `default_allow_out_of_stock_order`                   | Continue selling when out-of-stock                                                              | `boolean`   |     | ✅    |                                  |
| `default_available_threshold`                        | Show Threshold                                                                                  | `float`     |     | ✅    |                                  |
| `default_invoice_policy`                             | Invoicing Policy                                                                                | `selection` |     | ✅    |                                  |
| `default_picking_policy`                             | Picking Policy                                                                                  | `selection` | ✅  | ✅    |                                  |
| `default_show_availability`                          | Show availability Qty                                                                           | `boolean`   |     | ✅    |                                  |
| `delay_alert_contract`                               | Delay alert contract outdated                                                                   | `integer`   |     | ✅    |                                  |
| `digest_emails`                                      | Digest Emails                                                                                   | `boolean`   |     | ✅    |                                  |
| `digest_id`                                          | Digest Email                                                                                    | `many2one`  |     | ✅    | digest.digest                    |
| `display_account_storno`                             | Display Account Storno                                                                          | `boolean`   |     |       |                                  |
| `display_invoice_amount_total_words`                 | Total amount of invoice in letters                                                              | `boolean`   |     |       |                                  |
| `display_invoice_tax_company_currency`               | Taxes in company currency                                                                       | `boolean`   |     |       |                                  |
| `display_name`                                       | Display Name                                                                                    | `char`      |     |       |                                  |
| `documents_binary_max_size`                          | Size                                                                                            | `integer`   |     | ✅    |                                  |
| `documents_forbidden_extensions`                     | Extensions                                                                                      | `char`      |     | ✅    |                                  |
| `downpayment_account_id`                             | Downpayment Account                                                                             | `many2one`  |     |       | account.account                  |
| `ecommerce_access`                                   | Ecommerce Access                                                                                | `selection` |     |       |                                  |
| `email_primary_color`                                | Email Button Text                                                                               | `char`      |     |       |                                  |
| `email_secondary_color`                              | Email Button Color                                                                              | `char`      |     |       |                                  |
| `enable_academic_plan`                               | Academic Plan                                                                                   | `boolean`   |     | ✅    |                                  |
| `enable_create_student_user`                         | Create Student User                                                                             | `boolean`   |     | ✅    |                                  |
| `enable_exchange_rate_module`                        | Enable Exchange Rate Synchronization                                                            | `boolean`   |     | ✅    |                                  |
| `enable_recaptcha`                                   | Enable reCAPTCHA                                                                                | `boolean`   |     | ✅    |                                  |
| `expense_account_id`                                 | Expense Account                                                                                 | `many2one`  |     |       | account.account                  |
| `expense_currency_exchange_account_id`               | Loss Exchange Rate Account                                                                      | `many2one`  |     |       | account.account                  |
| `expense_journal_id`                                 | Default Expense Journal                                                                         | `many2one`  |     |       | account.journal                  |
| `external_email_server_default`                      | Use Custom Email Servers                                                                        | `boolean`   |     | ✅    |                                  |
| `external_report_layout_id`                          | Document Template                                                                               | `many2one`  |     |       | ir.ui.view                       |
| `fail_counter`                                       | Fail Mail                                                                                       | `integer`   |     |       |                                  |
| `favicon`                                            | Favicon                                                                                         | `binary`    |     |       |                                  |
| `fiscalyear_last_day`                                | Fiscalyear Last Day                                                                             | `integer`   |     |       |                                  |
| `fiscalyear_last_month`                              | Fiscalyear Last Month                                                                           | `selection` |     |       |                                  |
| `fiscalyear_lock_date`                               | Global Lock Date                                                                                | `date`      |     |       |                                  |
| `force_restrictive_audit_trail`                      | Forced Audit Trail                                                                              | `boolean`   |     |       |                                  |
| `global_calendar_user_id`                            | Calendar User                                                                                   | `many2one`  |     | ✅    | res.users                        |
| `google_analytics_key`                               | Google Analytics Key                                                                            | `char`      |     |       |                                  |
| `google_gmail_client_identifier`                     | Gmail Client Id                                                                                 | `char`      |     | ✅    |                                  |
| `google_gmail_client_secret`                         | Gmail Client Secret                                                                             | `char`      |     | ✅    |                                  |
| `google_maps_static_api_key`                         | Google Maps API key                                                                             | `char`      |     | ✅    |                                  |
| `google_maps_static_api_secret`                      | Google Maps API secret                                                                          | `char`      |     | ✅    |                                  |
| `google_search_console`                              | Google Search Console Key                                                                       | `char`      |     |       |                                  |
| `google_translate_api_key`                           | Message Translation API Key                                                                     | `char`      |     | ✅    |                                  |
| `group_analytic_accounting`                          | Analytic Accounting                                                                             | `boolean`   |     | ✅    |                                  |
| `group_auto_done_setting`                            | Lock Confirmed Sales                                                                            | `boolean`   |     | ✅    |                                  |
| `group_cash_rounding`                                | Cash Rounding                                                                                   | `boolean`   |     | ✅    |                                  |
| `group_discount_per_so_line`                         | Discounts                                                                                       | `boolean`   |     | ✅    |                                  |
| `group_fiscal_year`                                  | Fiscal Years                                                                                    | `boolean`   |     | ✅    |                                  |
| `group_gmc_feed`                                     | Google Merchant Center                                                                          | `boolean`   |     |       |                                  |
| `group_lot_on_delivery_slip`                         | Display Lots & Serial Numbers on Delivery Slips                                                 | `boolean`   |     | ✅    |                                  |
| `group_lot_on_invoice`                               | Display Lots & Serial Numbers on Invoices                                                       | `boolean`   |     | ✅    |                                  |
| `group_mass_mailing_campaign`                        | Mailing Campaigns                                                                               | `boolean`   |     | ✅    |                                  |
| `group_multi_currency`                               | Multi-Currencies                                                                                | `boolean`   |     | ✅    |                                  |
| `group_multi_website`                                | Multi-website                                                                                   | `boolean`   |     | ✅    |                                  |
| `group_product_price_comparison`                     | Comparison Price                                                                                | `boolean`   |     | ✅    |                                  |
| `group_product_pricelist`                            | Pricelists                                                                                      | `boolean`   |     | ✅    |                                  |
| `group_product_variant`                              | Variants                                                                                        | `boolean`   |     | ✅    |                                  |
| `group_proforma_sales`                               | Pro-Forma Invoice                                                                               | `boolean`   |     | ✅    |                                  |
| `group_sale_delivery_address`                        | Customer Addresses                                                                              | `boolean`   |     | ✅    |                                  |
| `group_sale_order_template`                          | Quotation Templates                                                                             | `boolean`   |     | ✅    |                                  |
| `group_send_reminder`                                | Receipt Reminder                                                                                | `boolean`   |     | ✅    |                                  |
| `group_show_uom_price`                               | Base Unit Price                                                                                 | `boolean`   |     | ✅    |                                  |
| `group_stock_adv_location`                           | Multi-Step Routes                                                                               | `boolean`   |     | ✅    |                                  |
| `group_stock_lot_print_gs1`                          | Print GS1 Barcodes for Lots & Serial Numbers                                                    | `boolean`   |     | ✅    |                                  |
| `group_stock_multi_locations`                        | Storage Locations                                                                               | `boolean`   |     | ✅    |                                  |
| `group_stock_production_lot`                         | Lots & Serial Numbers                                                                           | `boolean`   |     | ✅    |                                  |
| `group_stock_reception_report`                       | Reception Report                                                                                | `boolean`   |     | ✅    |                                  |
| `group_stock_sign_delivery`                          | Signature                                                                                       | `boolean`   |     | ✅    |                                  |
| `group_stock_tracking_lot`                           | Packages                                                                                        | `boolean`   |     | ✅    |                                  |
| `group_stock_tracking_owner`                         | Consignment                                                                                     | `boolean`   |     | ✅    |                                  |
| `group_uom`                                          | Units of Measure & Packagings                                                                   | `boolean`   |     | ✅    |                                  |
| `group_use_lead`                                     | Leads                                                                                           | `boolean`   |     | ✅    |                                  |
| `group_use_recurring_revenues`                       | Recurring Revenues                                                                              | `boolean`   |     | ✅    |                                  |
| `group_warning_purchase`                             | Purchase Warnings                                                                               | `boolean`   |     | ✅    |                                  |
| `group_warning_sale`                                 | Sale Order Warnings                                                                             | `boolean`   |     | ✅    |                                  |
| `group_warning_stock`                                | Warnings for Stock                                                                              | `boolean`   |     | ✅    |                                  |
| `hard_lock_date`                                     | Hard Lock Date                                                                                  | `date`      |     |       |                                  |
| `has_accounting_entries`                             | Has Accounting Entries                                                                          | `boolean`   |     |       |                                  |
| `has_chart_of_accounts`                              | Company has a chart of accounts                                                                 | `boolean`   |     |       |                                  |
| `has_default_share_image`                            | Use a image by default for sharing                                                              | `boolean`   |     |       |                                  |
| `has_enabled_provider`                               | Has Enabled Provider                                                                            | `boolean`   |     |       |                                  |
| `has_google_analytics`                               | Google Analytics                                                                                | `boolean`   |     |       |                                  |
| `has_google_search_console`                          | Google Search Console                                                                           | `boolean`   |     |       |                                  |
| `has_plausible_shared_key`                           | Plausible Analytics                                                                             | `boolean`   |     |       |                                  |
| `horizon_days`                                       | Replenishment Horizon                                                                           | `float`     |     |       |                                  |
| `hr_expense_alias_domain_id`                         | Hr Expense Alias Domain                                                                         | `many2one`  |     |       | mail.alias.domain                |
| `hr_expense_alias_prefix`                            | Default Alias Name for Expenses                                                                 | `char`      |     | ✅    |                                  |
| `hr_expense_use_mailgateway`                         | Let your employees record expenses by email                                                     | `boolean`   |     | ✅    |                                  |
| `hr_presence_control_email`                          | Based on number of emails sent                                                                  | `boolean`   |     |       |                                  |
| `hr_presence_control_email_amount`                   | # emails to send                                                                                | `integer`   |     |       |                                  |
| `hr_presence_control_ip`                             | Based on IP Address                                                                             | `boolean`   |     |       |                                  |
| `hr_presence_control_ip_list`                        | Valid IP addresses                                                                              | `char`      |     |       |                                  |
| `hr_presence_control_login`                          | Based on user status in system                                                                  | `boolean`   |     |       |                                  |
| `id`                                                 | ID                                                                                              | `integer`   |     | ✅    |                                  |
| `income_account_id`                                  | Income Account                                                                                  | `many2one`  |     |       | account.account                  |
| `income_currency_exchange_account_id`                | Gain Exchange Rate Account                                                                      | `many2one`  |     |       | account.account                  |
| `incoterm_id`                                        | Default incoterm                                                                                | `many2one`  |     |       | account.incoterms                |
| `invoice_mail_template_id`                           | Email Template                                                                                  | `many2one`  |     | ✅    | mail.template                    |
| `invoice_terms`                                      | Terms & Conditions                                                                              | `html`      |     |       |                                  |
| `invoice_terms_html`                                 | Terms & Conditions as a Web page                                                                | `html`      |     |       |                                  |
| `is_account_peppol_eligible`                         | PEPPOL eligible                                                                                 | `boolean`   |     |       |                                  |
| `is_batch_and_subject_constraint`                    | Batch and Subject Constraint                                                                    | `boolean`   |     | ✅    |                                  |
| `is_batch_constraint`                                | Batch Constraint                                                                                | `boolean`   |     | ✅    |                                  |
| `is_classroom_constraint`                            | Classroom Constraint                                                                            | `boolean`   |     | ✅    |                                  |
| `is_faculty_constraint`                              | Faculty Constraint                                                                              | `boolean`   |     | ✅    |                                  |
| `is_hash_verified`                                   | Is Hash Verified                                                                                | `boolean`   |     |       |                                  |
| `is_installed_sale`                                  | Is the Sale Module Installed                                                                    | `boolean`   |     | ✅    |                                  |
| `is_mail_sent`                                       | Is Mail Sent                                                                                    | `boolean`   |     |       |                                  |
| `is_membership_multi`                                | Multi Teams                                                                                     | `boolean`   |     | ✅    |                                  |
| `is_newsletter_enabled`                              | Is Newsletter Enabled                                                                           | `boolean`   |     | ✅    |                                  |
| `is_root_company`                                    | Is Root Company                                                                                 | `boolean`   |     |       |                                  |
| `language_count`                                     | Number of Languages                                                                             | `integer`   |     |       |                                  |
| `language_ids`                                       | Languages                                                                                       | `many2many` |     |       | res.lang                         |
| `lead_enrich_auto`                                   | Enrich lead automatically                                                                       | `selection` |     | ✅    |                                  |
| `lead_mining_in_pipeline`                            | Create a lead mining request directly from the opportunity pipeline.                            | `boolean`   |     | ✅    |                                  |
| `link_qr_code`                                       | Display Link QR-code                                                                            | `boolean`   |     |       |                                  |
| `lock_confirmed_po`                                  | Lock Confirmed Orders                                                                           | `boolean`   |     | ✅    |                                  |
| `mass_mailing_mail_server_id`                        | Mail Server                                                                                     | `many2one`  |     | ✅    | ir.mail_server                   |
| `mass_mailing_outgoing_mail_server`                  | Dedicated Server                                                                                | `boolean`   |     | ✅    |                                  |
| `mass_mailing_reports`                               | 24H Stat Mailing Reports                                                                        | `boolean`   |     | ✅    |                                  |
| `mass_mailing_split_contact_name`                    | Split First and Last Name                                                                       | `boolean`   |     | ✅    |                                  |
| `menu_bg_image`                                      | Apps Menu Footer Image                                                                          | `binary`    |     |       |                                  |
| `microsoft_outlook_client_identifier`                | Outlook Client Id                                                                               | `char`      |     | ✅    |                                  |
| `microsoft_outlook_client_secret`                    | Outlook Client Secret                                                                           | `char`      |     | ✅    |                                  |
| `module_account_3way_match`                          | 3-way matching: purchases, receptions and bills                                                 | `boolean`   |     | ✅    |                                  |
| `module_account_accountant`                          | Accounting                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_account_bank_statement_extract`              | Bank Statement Digitization                                                                     | `boolean`   |     | ✅    |                                  |
| `module_account_bank_statement_import_qif`           | Import .qif files                                                                               | `boolean`   |     | ✅    |                                  |
| `module_account_batch_payment`                       | Use batch payments                                                                              | `boolean`   |     | ✅    |                                  |
| `module_account_budget`                              | Budget Management                                                                               | `boolean`   |     | ✅    |                                  |
| `module_account_check_printing`                      | Allow check printing and deposits                                                               | `boolean`   |     | ✅    |                                  |
| `module_account_extract`                             | Document Digitization                                                                           | `boolean`   |     | ✅    |                                  |
| `module_account_inter_company_rules`                 | Manage Inter Company                                                                            | `boolean`   |     | ✅    |                                  |
| `module_account_intrastat`                           | Intrastat                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_account_invoice_extract`                     | Invoice Digitization                                                                            | `boolean`   |     | ✅    |                                  |
| `module_account_iso20022`                            | SEPA Credit Transfer / ISO20022                                                                 | `boolean`   |     | ✅    |                                  |
| `module_account_payment`                             | Invoice Online Payment                                                                          | `boolean`   |     | ✅    |                                  |
| `module_account_peppol`                              | PEPPOL Invoicing                                                                                | `boolean`   |     | ✅    |                                  |
| `module_account_reports`                             | Dynamic Reports                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_account_sepa_direct_debit`                   | Use SEPA Direct Debit                                                                           | `boolean`   |     | ✅    |                                  |
| `module_auth_ldap`                                   | LDAP Authentication                                                                             | `boolean`   |     | ✅    |                                  |
| `module_auth_oauth`                                  | Use external authentication providers (OAuth)                                                   | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup`                        | Database Backup to Local Server                                                                 | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_dropbox`                | Database Backup to Dropbox                                                                      | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_ftp`                    | Database Backup to Remote FTP Server                                                            | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_google_drive`           | Database Backup to Google Drive                                                                 | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_onedrive`               | Database Backup to Onedrive                                                                     | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_sftp`                   | Database Backup to Remote SFTP Server                                                           | `boolean`   |     | ✅    |                                  |
| `module_backend_theme`                               | Backend Theme                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_base_geolocalize`                            | GeoLocalize                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_base_import`                                 | Allow users to import data from CSV/XLS/XLSX/ODS files                                          | `boolean`   |     | ✅    |                                  |
| `module_bigbluebutton`                               | Bigbluebutton Enterprise                                                                        | `boolean`   |     | ✅    |                                  |
| `module_crm_iap_enrich`                              | Enrich your leads automatically with company data based on their email address.                 | `boolean`   |     | ✅    |                                  |
| `module_crm_iap_mine`                                | Generate new leads based on their country, industries, size, etc.                               | `boolean`   |     | ✅    |                                  |
| `module_currency_rate_live`                          | Automatic Currency Rates                                                                        | `boolean`   |     | ✅    |                                  |
| `module_delivery`                                    | Delivery Methods                                                                                | `boolean`   |     | ✅    |                                  |
| `module_delivery_bpost`                              | bpost Connector                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_delivery_dhl`                                | DHL Express Connector                                                                           | `boolean`   |     | ✅    |                                  |
| `module_delivery_easypost`                           | Easypost Connector                                                                              | `boolean`   |     | ✅    |                                  |
| `module_delivery_envia`                              | Envia.com Connector                                                                             | `boolean`   |     | ✅    |                                  |
| `module_delivery_fedex_rest`                         | FedEx Connector                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_delivery_sendcloud`                          | Sendcloud Connector                                                                             | `boolean`   |     | ✅    |                                  |
| `module_delivery_shiprocket`                         | Shiprocket Connector                                                                            | `boolean`   |     | ✅    |                                  |
| `module_delivery_starshipit`                         | Starshipit Connector                                                                            | `boolean`   |     | ✅    |                                  |
| `module_delivery_ups_rest`                           | UPS Connector                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_delivery_usps_rest`                          | USPS Connector                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_event_booth`                                 | Booth Management                                                                                | `boolean`   |     | ✅    |                                  |
| `module_event_sale`                                  | Tickets with Sale                                                                               | `boolean`   |     | ✅    |                                  |
| `module_google_address_autocomplete`                 | Google Address Autocomplete                                                                     | `boolean`   |     | ✅    |                                  |
| `module_google_calendar`                             | Allow the users to synchronize their calendar with Google Calendar                              | `boolean`   |     | ✅    |                                  |
| `module_google_gmail`                                | Support Gmail Authentication                                                                    | `boolean`   |     | ✅    |                                  |
| `module_googlemeet`                                  | Google Meet                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_google_recaptcha`                            | reCAPTCHA                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_helpdesk_elearning`                          | E-Learning                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_helpdesk_forum`                              | Helpdesk Forum                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_helpdesk_project_ext`                        | Helpdesk project                                                                                | `boolean`   |     | ✅    |                                  |
| `module_hr_attendance`                               | Based on attendances                                                                            | `boolean`   |     |       |                                  |
| `module_hr_expense_extract`                          | Send bills to OCR to generate expenses                                                          | `boolean`   |     | ✅    |                                  |
| `module_hr_expense_stripe`                           | Link your stripe issuing account to manage company credit cards for your employees through Odoo | `boolean`   |     | ✅    |                                  |
| `module_hr_payroll_expense`                          | Reimburse Expenses in Payslip                                                                   | `boolean`   |     | ✅    |                                  |
| `module_hr_presence`                                 | Advanced Presence Control                                                                       | `boolean`   |     | ✅    |                                  |
| `module_hr_recruitment_extract`                      | Send CV to OCR to fill applications                                                             | `boolean`   |     | ✅    |                                  |
| `module_hr_recruitment_survey`                       | Interview Forms                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_hr_skills`                                   | Skills Management                                                                               | `boolean`   |     | ✅    |                                  |
| `module_loyalty`                                     | Promotions, Coupons, Gift Card & Loyalty Program                                                | `boolean`   |     | ✅    |                                  |
| `module_mail_plugin`                                 | Allow integration with the mail plugins                                                         | `boolean`   |     | ✅    |                                  |
| `module_microsoft_calendar`                          | Allow the users to synchronize their calendar with Outlook Calendar                             | `boolean`   |     | ✅    |                                  |
| `module_microsoft_outlook`                           | Support Outlook Authentication                                                                  | `boolean`   |     | ✅    |                                  |
| `module_online_appointment`                          | Online Appointment Enterprise                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_achievement_enterprise`           | Achievement Enterprise                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_activity`                         | Activity                                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_activity_enterprise`              | Activity Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_admission`                        | Admission                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_admission_enterprise`             | Admission Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_admission_grading_bridge`         | Admission Grading Bridge                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_blog_enterprise`           | Alumni Blog Enterprise                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_enterprise`                | Alumni Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_event_enterprise`          | Alumni Event Enterprise                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_job_enterprise`            | Alumni Job Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_asset_request_enterprise`         | Asset Request Enterprise                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment`                       | Assignment                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_enterprise`            | Assignment Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_grading_bridge`        | Assignment Gradebook Bridge                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_grading_enterprise`    | Assignment Grading Enterprise                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_rubrics`               | Assignment Rubrics                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance`                       | Attendance                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance_enterprise`            | Attendance Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance_face_recognition`      | Attendance Face Recognition                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance_report_xlsx`           | Attendance Xlsx Report                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_campus_enterprise`                | Campus Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_classroom`                        | Classroom                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_classroom_enterprise`             | Classroom Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_convocation`                      | Convocation                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_crm_enterprise`                   | CRM Enterprise                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_dashboard_kpi`                    | Dashboard KPI                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_digital_library`                  | Digital Library                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_openeducat_discipline`                       | Discipline Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_dynamic_admission`                | Dynamic Admission                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_event_enterprise`                 | Event Enterprise                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam`                             | Exam                                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_enterprise`                  | Exam Enterprise                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_gpa_enterprise`              | Exam GPA Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_grading_bridge`              | Exam Grading Bridge                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_migration_bridge`            | Student Migration Exam Bridge                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_facility`                         | Facility                                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_facility_enterprise`              | Facility Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_fees`                             | Fees                                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_fees_parent_bridge`               | Fees Parent Bridge                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_fees_plan`                        | Fees Plan                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_grading`                          | Grading                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_grading_migration_bridge`         | Student Migration Grading Bridge                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_grievance_enterprise`             | Grievance                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_health_enterprise`                | Health Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_jitsi_enterprise`                 | Jitsi Enterprise                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_job_enterprise`                   | Job Enterprise                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lesson`                           | Lesson Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_library`                          | Library                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_library_barcode`                  | Library Barcode Enterprise                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_library_enterprise`               | Library Enterprise                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live`                             | Live Meeting                                                                                    | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live_assignment`                  | Live Meeting Assignment                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live_attendance`                  | Live Meeting Attendance                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live_attentiveness`               | Live Meeting Attentiveness                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms`                              | LMS Enterprise                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_admission`                    | LMS Admission                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_blog`                         | LMS Blog Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_forum`                        | LMS Forum Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_gamification`                 | LMS Gamification Enterprise                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_h5p`                          | LMS H5P Enterprise                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_sale`                         | LMS Sale Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_survey`                       | LMS Survey Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_mass_subject_registration`        | Mass Subject Registration                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_meeting_enterprise`               | Meeting Enterprise                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_notice_board_enterprise`          | Notice Board Enterprise                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_omr`                              | OMR                                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_parent`                           | Parent                                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_parent_enterprise`                | Parent Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_placement_enterprise`             | Placement Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_placement_job_enterprise`         | Placement Job Enterprise                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_quiz`                             | Quiz Enterprise                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_openeducat_quiz_anti_cheating`               | Quiz Anti Cheating                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_scholarship_enterprise`           | Scholarship Enterprise                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_secure`                           | Secure QR                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_skill_enterprise`                 | Skill Enterprise                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_skypemeet`                        | Skype Meet                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_attendance_enterprise`    | Student Attendance Kiosk                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_feedback_management`      | Student Feedback                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_leave_enterprise`         | Student Leave                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_mentor`                   | Student Mentor                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_progress_enterprise`      | Student Progress Enterprise                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_skill_assessment`         | Skill Assessment Enterprise                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_withdrawal_mgmt`          | Student Withdrawal Management                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_subject_material_allocation`      | Subject Material Allocation                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_thesis`                           | Thesis                                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_timetable`                        | Timetable                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_timetable_enterprise`             | Timetable Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_transportation_enterprise`        | Transportation Enterprise                                                                       | `boolean`   |     | ✅    |                                  |
| `module_partner_autocomplete`                        | Partner Autocomplete                                                                            | `boolean`   |     | ✅    |                                  |
| `module_partnership`                                 | Membership / Partnership                                                                        | `boolean`   |     | ✅    |                                  |
| `module_pos_event`                                   | Tickets with PoS                                                                                | `boolean`   |     | ✅    |                                  |
| `module_product_email_template`                      | Specific Email                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_product_expiry`                              | Expiration Dates                                                                                | `boolean`   |     | ✅    |                                  |
| `module_product_margin`                              | Allow Product Margin                                                                            | `boolean`   |     | ✅    |                                  |
| `module_purchase_product_matrix`                     | Purchase Grid Entry                                                                             | `boolean`   |     | ✅    |                                  |
| `module_purchase_requisition`                        | Purchase Agreements                                                                             | `boolean`   |     | ✅    |                                  |
| `module_quality_control`                             | Quality                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_quality_control_worksheet`                   | Quality Worksheet                                                                               | `boolean`   |     | ✅    |                                  |
| `module_sale_amazon`                                 | Amazon Sync                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_sale_commission`                             | Commissions                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_sale_gelato`                                 | Gelato                                                                                          | `boolean`   |     | ✅    |                                  |
| `module_sale_loyalty`                                | Coupons & Loyalty                                                                               | `boolean`   |     | ✅    |                                  |
| `module_sale_margin`                                 | Margins                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_sale_pdf_quote_builder`                      | PDF Quote builder                                                                               | `boolean`   |     | ✅    |                                  |
| `module_sale_product_matrix`                         | Sales Grid Entry                                                                                | `boolean`   |     | ✅    |                                  |
| `module_sale_shopee`                                 | Shopee Sync                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_sms`                                         | SMS                                                                                             | `boolean`   |     | ✅    |                                  |
| `module_snailmail_account`                           | Snailmail                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_stock_barcode`                               | Barcode Scanner                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_stock_barcode_barcodelookup`                 | Stock Barcode Database                                                                          | `boolean`   |     | ✅    |                                  |
| `module_stock_dropshipping`                          | Dropshipping                                                                                    | `boolean`   |     | ✅    |                                  |
| `module_stock_fleet`                                 | Dispatch Management System                                                                      | `boolean`   |     | ✅    |                                  |
| `module_stock_landed_costs`                          | Landed Costs                                                                                    | `boolean`   |     | ✅    |                                  |
| `module_stock_picking_batch`                         | Batch, Wave & Cluster Transfers                                                                 | `boolean`   |     | ✅    |                                  |
| `module_stock_sms`                                   | SMS Confirmation                                                                                | `boolean`   |     | ✅    |                                  |
| `module_teams`                                       | Teams                                                                                           | `boolean`   |     | ✅    |                                  |
| `module_voip`                                        | Phone                                                                                           | `boolean`   |     | ✅    |                                  |
| `module_website_cf_turnstile`                        | Cloudflare Turnstile                                                                            | `boolean`   |     | ✅    |                                  |
| `module_website_crm_iap_reveal`                      | Create Leads/Opportunities from your website's traffic                                          | `boolean`   |     | ✅    |                                  |
| `module_website_event_exhibitor`                     | Advanced Sponsors                                                                               | `boolean`   |     | ✅    |                                  |
| `module_website_event_sale`                          | Online Ticketing                                                                                | `boolean`   |     | ✅    |                                  |
| `module_website_event_track`                         | Tracks and Agenda                                                                               | `boolean`   |     | ✅    |                                  |
| `module_website_event_track_live`                    | Live Mode                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_website_event_track_quiz`                    | Quiz on Tracks                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_website_helpdesk_mgmt`                       | Helpdesk Website                                                                                | `boolean`   |     | ✅    |                                  |
| `module_website_hr_recruitment`                      | Online Posting                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_website_livechat`                            | Module Website Livechat                                                                         | `boolean`   |     | ✅    |                                  |
| `module_website_sale_autocomplete`                   | Address Autocomplete                                                                            | `boolean`   |     | ✅    |                                  |
| `module_website_sale_collect`                        | Click & Collect                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_web_unsplash`                                | Unsplash Image Library                                                                          | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_account_templates`                  | Account Templates                                                                               | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_ecommerce_templates`                | Whatsapp Ecommerce Templates                                                                    | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_education_templates`                | Education Templates                                                                             | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_other_templates`                    | Other Templates                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_services_templates`                 | Services Templates                                                                              | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_special_occasions_template`         | Special Occasions Templates                                                                     | `boolean`   |     | ✅    |                                  |
| `module_zoom`                                        | Zoom                                                                                            | `boolean`   |     | ✅    |                                  |
| `newsletter_id`                                      | Newsletter List                                                                                 | `many2one`  |     |       | mailing.list                     |
| `next_execution_timestamp`                           | Next Execution Time                                                                             | `datetime`  |     |       |                                  |
| `onboarding_payment_module`                          | Onboarding Payment Module                                                                       | `selection` |     |       |                                  |
| `openeducat_instance_hash_key`                       | OpenEducat Instance Hash Key                                                                    | `char`      |     |       |                                  |
| `openeducat_instance_hash_msg`                       | Instance Hash Key Message                                                                       | `char`      |     |       |                                  |
| `openeducat_instance_key`                            | OpenEducat Instance Key                                                                         | `char`      |     |       |                                  |
| `parent_qrcode`                                      | QR Code                                                                                         | `boolean`   |     | ✅    |                                  |
| `partner_autocomplete_insufficient_credit`           | Insufficient credit                                                                             | `boolean`   |     |       |                                  |
| `pay_invoices_online`                                | Pay Invoices Online                                                                             | `boolean`   |     | ✅    |                                  |
| `plausible_shared_key`                               | Plausible auth Key                                                                              | `char`      |     |       |                                  |
| `plausible_site`                                     | Plausible Site (e.g. domain.com)                                                                | `char`      |     |       |                                  |
| `po_double_validation`                               | Levels of Approvals \*                                                                          | `selection` |     |       |                                  |
| `po_double_validation_amount`                        | Minimum Amount                                                                                  | `monetary`  |     |       |                                  |
| `po_lock`                                            | Purchase Order Modification \*                                                                  | `selection` |     |       |                                  |
| `po_order_approval`                                  | Purchase Order Approval                                                                         | `boolean`   |     | ✅    |                                  |
| `portal_allow_api_keys`                              | Customer API Keys                                                                               | `boolean`   |     |       |                                  |
| `portal_confirmation_pay`                            | Online Payment                                                                                  | `boolean`   |     |       |                                  |
| `portal_confirmation_sign`                           | Online Signature                                                                                | `boolean`   |     |       |                                  |
| `predictive_lead_scoring_field_labels`               | Predictive Lead Scoring Field Labels                                                            | `char`      |     |       |                                  |
| `predictive_lead_scoring_fields`                     | Lead Scoring Frequency Fields                                                                   | `many2many` |     |       | crm.lead.scoring.frequency.field |
| `predictive_lead_scoring_fields_str`                 | Lead Scoring Frequency Fields in String                                                         | `char`      |     | ✅    |                                  |
| `predictive_lead_scoring_start_date`                 | Lead Scoring Starting Date                                                                      | `date`      |     |       |                                  |
| `predictive_lead_scoring_start_date_str`             | Lead Scoring Starting Date in String                                                            | `char`      |     | ✅    |                                  |
| `prepayment_percent`                                 | Prepayment percentage                                                                           | `float`     |     |       |                                  |
| `preview_ready`                                      | Display preview button                                                                          | `boolean`   |     |       |                                  |
| `product_volume_volume_in_cubic_feet`                | Volume unit of measure                                                                          | `selection` |     | ✅    |                                  |
| `product_weight_in_lbs`                              | Weight unit of measure                                                                          | `selection` |     | ✅    |                                  |
| `profiling_enabled_until`                            | Profiling enabled until                                                                         | `datetime`  |     | ✅    |                                  |
| `purchase_lock_date`                                 | Purchases Lock Date                                                                             | `date`      |     |       |                                  |
| `purchase_tax_id`                                    | Default Purchase Tax                                                                            | `many2one`  |     |       | account.tax                      |
| `qr_code`                                            | Display SEPA QR-code                                                                            | `boolean`   |     |       |                                  |
| `quick_edit_mode`                                    | Quick encoding                                                                                  | `selection` |     |       |                                  |
| `quotation_validity_days`                            | Default Quotation Validity                                                                      | `integer`   |     |       |                                  |
| `rate_provider_selection`                            | Exchange Rate Provider                                                                          | `selection` |     |       |                                  |
| `recaptcha_min_score`                                | Minimum score                                                                                   | `float`     |     | ✅    |                                  |
| `recaptcha_private_key`                              | Secret Key                                                                                      | `char`      |     | ✅    |                                  |
| `recaptcha_public_key`                               | Site Key                                                                                        | `char`      |     | ✅    |                                  |
| `refresh_token`                                      | Refresh Token                                                                                   | `char`      |     | ✅    |                                  |
| `replenish_on_order`                                 | Replenish on Order (MTO)                                                                        | `boolean`   |     |       |                                  |
| `report_footer`                                      | Custom Report Footer                                                                            | `html`      |     |       |                                  |
| `resource_calendar_id`                               | Company Working Hours                                                                           | `many2one`  |     |       | resource.calendar                |
| `restrictive_audit_trail`                            | Restricted Audit Trail                                                                          | `boolean`   |     |       |                                  |
| `restrict_template_rendering`                        | Restrict Template Rendering                                                                     | `boolean`   |     | ✅    |                                  |
| `sale_lock_date`                                     | Sales Lock Date                                                                                 | `date`      |     |       |                                  |
| `salesperson_id`                                     | Salesperson                                                                                     | `many2one`  |     |       | res.users                        |
| `salesteam_id`                                       | Sales Team                                                                                      | `many2one`  |     |       | crm.team                         |
| `sale_tax_id`                                        | Default Sale Tax                                                                                | `many2one`  |     |       | account.tax                      |
| `secure_qr_code`                                     | Secure Qr Code                                                                                  | `selection` |     | ✅    |                                  |
| `security_lead`                                      | Security Lead Time                                                                              | `float`     |     |       |                                  |
| `send_abandoned_cart_email`                          | Abandoned Email                                                                                 | `boolean`   |     |       |                                  |
| `sfu_server_key`                                     | SFU Server key                                                                                  | `char`      |     | ✅    |                                  |
| `sfu_server_url`                                     | SFU Server URL                                                                                  | `char`      |     | ✅    |                                  |
| `shared_user_account`                                | Shared Customer Accounts                                                                        | `boolean`   |     |       |                                  |
| `show_blacklist_buttons`                             | Blacklist Option when Unsubscribing                                                             | `boolean`   |     | ✅    |                                  |
| `show_branding_in_footer`                            | Show Branding In Footer                                                                         | `boolean`   |     | ✅    |                                  |
| `show_effect`                                        | Show Effect                                                                                     | `boolean`   |     | ✅    |                                  |
| `show_line_subtotals_tax_selection`                  | Line Subtotals Tax Display                                                                      | `selection` |     |       |                                  |
| `show_sale_receipts`                                 | Sale Receipt                                                                                    | `boolean`   |     | ✅    |                                  |
| `snailmail_color`                                    | Print In Color                                                                                  | `boolean`   |     |       |                                  |
| `snailmail_cover`                                    | Add a Cover Page                                                                                | `boolean`   |     |       |                                  |
| `snailmail_cover_readonly`                           | Snailmail Cover Readonly                                                                        | `boolean`   |     |       |                                  |
| `snailmail_duplex`                                   | Print Both sides                                                                                | `boolean`   |     |       |                                  |
| `social_default_image`                               | Default Social Share Image                                                                      | `binary`    |     |       |                                  |
| `stock_confirmation_type`                            | Stock Text Validation type                                                                      | `selection` |     |       |                                  |
| `stock_move_email_validation`                        | Email Confirmation picking                                                                      | `boolean`   |     |       |                                  |
| `stock_sms_confirmation_template_id`                 | SMS Template                                                                                    | `many2one`  |     |       | sms.template                     |
| `stock_text_confirmation`                            | Stock Text Validation with stock move                                                           | `boolean`   |     |       |                                  |
| `synchronization_batch_size`                         | Batch Size                                                                                      | `integer`   |     |       |                                  |
| `synchronization_frequency`                          | Synchronization Frequency                                                                       | `selection` |     |       |                                  |
| `tax_calculation_rounding_method`                    | Tax calculation rounding method                                                                 | `selection` |     |       |                                  |
| `tax_cash_basis_journal_id`                          | Tax Cash Basis Journal                                                                          | `many2one`  |     |       | account.journal                  |
| `tax_exigibility`                                    | Cash Basis                                                                                      | `boolean`   |     |       |                                  |
| `tax_lock_date`                                      | Tax Lock Date                                                                                   | `date`      |     |       |                                  |
| `tenor_api_key`                                      | Tenor API key                                                                                   | `char`      |     | ✅    |                                  |
| `terms_type`                                         | Terms & Conditions format                                                                       | `selection` |     |       |                                  |
| `transfer_account_id`                                | Internal Transfer                                                                               | `many2one`  |     |       | account.account                  |
| `twilio_account_sid`                                 | Account SID                                                                                     | `char`      |     | ✅    |                                  |
| `twilio_account_token`                               | Account Auth Token                                                                              | `char`      |     | ✅    |                                  |
| `unsplash_access_key`                                | Access Key                                                                                      | `char`      |     | ✅    |                                  |
| `unsplash_app_id`                                    | Application ID                                                                                  | `char`      |     | ✅    |                                  |
| `use_event_barcode`                                  | Use Event Barcode                                                                               | `boolean`   |     | ✅    |                                  |
| `use_google_maps_static_api`                         | Google Maps static API                                                                          | `boolean`   |     | ✅    |                                  |
| `use_invoice_terms`                                  | Default Terms & Conditions                                                                      | `boolean`   |     | ✅    |                                  |
| `use_project`                                        | Use Projects                                                                                    | `boolean`   |     | ✅    |                                  |
| `use_security_lead`                                  | Security Lead Time for Sales                                                                    | `boolean`   |     | ✅    |                                  |
| `use_sfu_server`                                     | Use SFU server                                                                                  | `boolean`   |     | ✅    |                                  |
| `use_twilio_rtc_servers`                             | Use Twilio ICE servers                                                                          | `boolean`   |     | ✅    |                                  |
| `use_website_form`                                   | Website Form                                                                                    | `boolean`   |     | ✅    |                                  |
| `verify_date`                                        | Verify Date                                                                                     | `char`      |     |       |                                  |
| `web_app_name`                                       | Web App Name                                                                                    | `char`      |     | ✅    |                                  |
| `website_block_third_party_domains`                  | Block 3rd-party domains                                                                         | `boolean`   |     |       |                                  |
| `website_company_id`                                 | Website Company                                                                                 | `many2one`  |     |       | res.company                      |
| `website_cookies_bar`                                | Cookies Bar                                                                                     | `boolean`   |     |       |                                  |
| `website_default_lang_code`                          | Default language code                                                                           | `char`      |     |       |                                  |
| `website_default_lang_id`                            | Default language                                                                                | `many2one`  |     |       | res.lang                         |
| `website_domain`                                     | Website Domain                                                                                  | `char`      |     |       |                                  |
| `website_homepage_url`                               | Homepage Url                                                                                    | `char`      |     |       |                                  |
| `website_id`                                         | website                                                                                         | `many2one`  |     | ✅    | website                          |
| `website_language_count`                             | Number of languages                                                                             | `integer`   |     |       |                                  |
| `website_logo`                                       | Website Logo                                                                                    | `binary`    |     |       |                                  |
| `website_name`                                       | Website Name                                                                                    | `char`      |     |       |                                  |
| `website_sale_contact_us_button_url`                 | Button Url                                                                                      | `char`      |     |       |                                  |
| `website_sale_prevent_zero_price_sale`               | Prevent Sale of Zero Priced Product                                                             | `boolean`   |     |       |                                  |
| `website_warehouse_id`                               | Warehouse                                                                                       | `many2one`  |     |       | stock.warehouse                  |
| `whatsapp_business_id`                               | Business Account                                                                                | `many2one`  |     | ✅    | whatsapp.business                |
| `work_permit_expiration_notice_period`               | Work Permit Expiry Notice Period                                                                | `integer`   |     |       |                                  |
| `write_date`                                         | Last Updated on                                                                                 | `datetime`  |     | ✅    |                                  |
| `write_uid`                                          | Last Updated by                                                                                 | `many2one`  |     | ✅    | res.users                        |

**Access Rights:**

| Name                       | Group                | Perms   |
| -------------------------- | -------------------- | ------- |
| access.res.config.settings | Role / Administrator | `R/W/C` |

### 🗃️ `crm.lead2opportunity.partner.mass` — Convert Lead to Opportunity (in mass)

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                   | Label               | Type        | Req | Store | Relation    |
| ----------------------- | ------------------- | ----------- | --- | ----- | ----------- |
| `action`                | Related Customer    | `selection` | ✅  | ✅    |             |
| `commercial_partner_id` | Company             | `many2one`  |     | ✅    | res.partner |
| `create_date`           | Created on          | `datetime`  |     | ✅    |             |
| `create_uid`            | Created by          | `many2one`  |     | ✅    | res.users   |
| `deduplicate`           | Apply deduplication | `boolean`   |     | ✅    |             |
| `display_name`          | Display Name        | `char`      |     |       |             |
| `duplicated_lead_ids`   | Opportunities       | `many2many` |     | ✅    | crm.lead    |
| `force_assignment`      | Force assignment    | `boolean`   |     | ✅    |             |
| `id`                    | ID                  | `integer`   |     | ✅    |             |
| `lead_contact_name`     | Contact Name        | `char`      |     |       |             |
| `lead_id`               | Associated Lead     | `many2one`  |     | ✅    | crm.lead    |
| `lead_partner_name`     | Company Name        | `char`      |     |       |             |
| `lead_tomerge_ids`      | Active Leads        | `many2many` |     | ✅    | crm.lead    |
| `name`                  | Conversion Action   | `selection` |     | ✅    |             |
| `partner_id`            | Customer            | `many2one`  |     | ✅    | res.partner |
| `team_id`               | Sales Team          | `many2one`  |     | ✅    | crm.team    |
| `user_id`               | Salesperson         | `many2one`  |     | ✅    | res.users   |
| `user_ids`              | Salespersons        | `many2many` |     | ✅    | res.users   |
| `write_date`            | Last Updated on     | `datetime`  |     | ✅    |             |
| `write_uid`             | Last Updated by     | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                                     | Group                            | Perms   |
| ---------------------------------------- | -------------------------------- | ------- |
| access.crm.lead2opportunity.partner.mass | Sales / User: Own Documents Only | `R/W/C` |

### 🗃️ `crm.lead2opportunity.partner` — Convert Lead to Opportunity (not in mass)

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                   | Label             | Type        | Req | Store | Relation    |
| ----------------------- | ----------------- | ----------- | --- | ----- | ----------- |
| `action`                | Related Customer  | `selection` | ✅  | ✅    |             |
| `commercial_partner_id` | Company           | `many2one`  |     | ✅    | res.partner |
| `create_date`           | Created on        | `datetime`  |     | ✅    |             |
| `create_uid`            | Created by        | `many2one`  |     | ✅    | res.users   |
| `display_name`          | Display Name      | `char`      |     |       |             |
| `duplicated_lead_ids`   | Opportunities     | `many2many` |     | ✅    | crm.lead    |
| `force_assignment`      | Force assignment  | `boolean`   |     | ✅    |             |
| `id`                    | ID                | `integer`   |     | ✅    |             |
| `lead_contact_name`     | Contact Name      | `char`      |     |       |             |
| `lead_id`               | Associated Lead   | `many2one`  | ✅  | ✅    | crm.lead    |
| `lead_partner_name`     | Company Name      | `char`      |     |       |             |
| `name`                  | Conversion Action | `selection` |     | ✅    |             |
| `partner_id`            | Customer          | `many2one`  |     | ✅    | res.partner |
| `team_id`               | Sales Team        | `many2one`  |     | ✅    | crm.team    |
| `user_id`               | Salesperson       | `many2one`  |     | ✅    | res.users   |
| `write_date`            | Last Updated on   | `datetime`  |     | ✅    |             |
| `write_uid`             | Last Updated by   | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                                | Group                            | Perms   |
| ----------------------------------- | -------------------------------- | ------- |
| access.crm.lead2opportunity.partner | Sales / User: Own Documents Only | `R/W/C` |

### 🗃️ `crm.activity.report` — CRM Activity Analysis

CRM Lead Analysis

**Fields:**

| Field                   | Label                | Type        | Req | Store | Relation             |
| ----------------------- | -------------------- | ----------- | --- | ----- | -------------------- |
| `active`                | Active               | `boolean`   |     | ✅    |                      |
| `author_id`             | Assigned To          | `many2one`  |     | ✅    | res.partner          |
| `body`                  | Activity Description | `html`      |     | ✅    |                      |
| `company_id`            | Company              | `many2one`  |     | ✅    | res.company          |
| `country_id`            | Country              | `many2one`  |     | ✅    | res.country          |
| `date`                  | Completion Date      | `datetime`  |     | ✅    |                      |
| `date_closed`           | Closed Date          | `datetime`  |     | ✅    |                      |
| `date_conversion`       | Conversion Date      | `datetime`  |     | ✅    |                      |
| `date_deadline`         | Expected Closing     | `date`      |     | ✅    |                      |
| `display_name`          | Display Name         | `char`      |     |       |                      |
| `id`                    | ID                   | `integer`   |     | ✅    |                      |
| `lead_create_date`      | Creation Date        | `datetime`  |     | ✅    |                      |
| `lead_id`               | Opportunity          | `many2one`  |     | ✅    | crm.lead             |
| `lead_type`             | Type                 | `selection` |     | ✅    |                      |
| `mail_activity_type_id` | Activity Type        | `many2one`  |     | ✅    | mail.activity.type   |
| `partner_id`            | Customer             | `many2one`  |     | ✅    | res.partner          |
| `stage_id`              | Stage                | `many2one`  |     | ✅    | crm.stage            |
| `subtype_id`            | Subtype              | `many2one`  |     | ✅    | mail.message.subtype |
| `tag_ids`               | Tags                 | `many2many` |     |       | crm.tag              |
| `team_id`               | Sales Team           | `many2one`  |     | ✅    | crm.team             |
| `user_id`               | Salesperson          | `many2one`  |     | ✅    | res.users            |
| `won_status`            | Is Won               | `selection` |     | ✅    |                      |

**Access Rights:**

| Name                         | Group                            | Perms |
| ---------------------------- | -------------------------------- | ----- |
| crm.activity.report.salesman | Sales / User: Own Documents Only | `R`   |
| crm.activity.report.user     | Role / User                      | `-`   |

**Record Rules:**

- **All Activities** (26) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Personal Activities** (25) `R/W/C/D`
  - Domain: `['|',('user_id','=',user.id),('user_id','=',False)]`
- **CRM Lead Multi-Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `crm.recurring.plan` — CRM Recurring revenue plans

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field              | Label           | Type       | Req | Store | Relation  |
| ------------------ | --------------- | ---------- | --- | ----- | --------- |
| `active`           | Active          | `boolean`  |     | ✅    |           |
| `create_date`      | Created on      | `datetime` |     | ✅    |           |
| `create_uid`       | Created by      | `many2one` |     | ✅    | res.users |
| `display_name`     | Display Name    | `char`     |     |       |           |
| `id`               | ID              | `integer`  |     | ✅    |           |
| `name`             | Plan Name       | `char`     | ✅  | ✅    |           |
| `number_of_months` | # Months        | `integer`  | ✅  | ✅    |           |
| `sequence`         | Sequence        | `integer`  |     | ✅    |           |
| `write_date`       | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`        | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                               | Group                            | Perms     |
| ---------------------------------- | -------------------------------- | --------- |
| crm.recurring.plan.access.salesman | Sales / User: Own Documents Only | `R`       |
| crm.recurring.plan.access.manager  | Sales / Administrator            | `R/W/C/D` |

### 🗃️ `crm.stage` — CRM Stages

Model for case stages. This models the main stages of a document management flow. Main
CRM objects (leads, opportunities, project issues, ...) will now use only stages,
instead of state and stages. Stages are for example used to display the kanban view of
records.

**Fields:**

| Field                    | Label              | Type        | Req | Store | Relation  |
| ------------------------ | ------------------ | ----------- | --- | ----- | --------- |
| `color`                  | Color              | `integer`   |     | ✅    |           |
| `create_date`            | Created on         | `datetime`  |     | ✅    |           |
| `create_uid`             | Created by         | `many2one`  |     | ✅    | res.users |
| `display_name`           | Display Name       | `char`      |     |       |           |
| `fold`                   | Folded in Pipeline | `boolean`   |     | ✅    |           |
| `id`                     | ID                 | `integer`   |     | ✅    |           |
| `is_won`                 | Is Won Stage?      | `boolean`   |     | ✅    |           |
| `name`                   | Stage Name         | `char`      | ✅  | ✅    |           |
| `requirements`           | Requirements       | `text`      |     | ✅    |           |
| `rotting_threshold_days` | Days to rot        | `integer`   |     | ✅    |           |
| `sequence`               | Sequence           | `integer`   |     | ✅    |           |
| `team_count`             | team_count         | `integer`   |     |       |           |
| `team_ids`               | Sales Teams        | `many2many` |     | ✅    | crm.team  |
| `write_date`             | Last Updated on    | `datetime`  |     | ✅    |           |
| `write_uid`              | Last Updated by    | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name      | Group                 | Perms     |
| --------- | --------------------- | --------- |
| crm.stage | Sales / Administrator | `R/W/C/D` |
| crm.stage | Role / User           | `R`       |

### 🗃️ `digest.digest` — Digest

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                     | Label                                   | Type        | Req | Store | Relation     |
| ----------------------------------------- | --------------------------------------- | ----------- | --- | ----- | ------------ |
| `available_fields`                        | Available Fields                        | `char`      |     |       |              |
| `company_id`                              | Company                                 | `many2one`  |     | ✅    | res.company  |
| `create_date`                             | Created on                              | `datetime`  |     | ✅    |              |
| `create_uid`                              | Created by                              | `many2one`  |     | ✅    | res.users    |
| `currency_id`                             | Currency                                | `many2one`  |     |       | res.currency |
| `display_name`                            | Display Name                            | `char`      |     |       |              |
| `id`                                      | ID                                      | `integer`   |     | ✅    |              |
| `is_subscribed`                           | Is user subscribed                      | `boolean`   |     |       |              |
| `kpi_account_total_revenue`               | Revenue                                 | `boolean`   |     | ✅    |              |
| `kpi_account_total_revenue_value`         | Kpi Account Total Revenue Value         | `monetary`  |     |       |              |
| `kpi_all_sale_total`                      | All Sales                               | `boolean`   |     | ✅    |              |
| `kpi_all_sale_total_value`                | Kpi All Sale Total Value                | `monetary`  |     |       |              |
| `kpi_crm_lead_created`                    | New Leads                               | `boolean`   |     | ✅    |              |
| `kpi_crm_lead_created_value`              | Kpi Crm Lead Created Value              | `integer`   |     |       |              |
| `kpi_crm_opportunities_won`               | Opportunities Won                       | `boolean`   |     | ✅    |              |
| `kpi_crm_opportunities_won_value`         | Kpi Crm Opportunities Won Value         | `integer`   |     |       |              |
| `kpi_hr_recruitment_new_colleagues`       | New Employees                           | `boolean`   |     | ✅    |              |
| `kpi_hr_recruitment_new_colleagues_value` | Kpi Hr Recruitment New Colleagues Value | `integer`   |     |       |              |
| `kpi_livechat_conversations`              | Conversations handled                   | `boolean`   |     | ✅    |              |
| `kpi_livechat_conversations_value`        | Kpi Livechat Conversations Value        | `integer`   |     |       |              |
| `kpi_livechat_rating`                     | % of Happiness                          | `boolean`   |     | ✅    |              |
| `kpi_livechat_rating_value`               | Kpi Livechat Rating Value               | `float`     |     |       |              |
| `kpi_livechat_response`                   | Time to answer (sec)                    | `boolean`   |     | ✅    |              |
| `kpi_livechat_response_value`             | Kpi Livechat Response Value             | `float`     |     |       |              |
| `kpi_mail_message_total`                  | Messages Sent                           | `boolean`   |     | ✅    |              |
| `kpi_mail_message_total_value`            | Kpi Mail Message Total Value            | `integer`   |     |       |              |
| `kpi_res_users_connected`                 | Connected Users                         | `boolean`   |     | ✅    |              |
| `kpi_res_users_connected_value`           | Kpi Res Users Connected Value           | `integer`   |     |       |              |
| `kpi_website_sale_total`                  | eCommerce Sales                         | `boolean`   |     | ✅    |              |
| `kpi_website_sale_total_value`            | Kpi Website Sale Total Value            | `monetary`  |     |       |              |
| `name`                                    | Name                                    | `char`      | ✅  | ✅    |              |
| `next_run_date`                           | Next Mailing Date                       | `date`      |     | ✅    |              |
| `periodicity`                             | Periodicity                             | `selection` | ✅  | ✅    |              |
| `state`                                   | Status                                  | `selection` |     | ✅    |              |
| `user_ids`                                | Recipients                              | `many2many` |     | ✅    | res.users    |
| `write_date`                              | Last Updated on                         | `datetime`  |     | ✅    |              |
| `write_uid`                               | Last Updated by                         | `many2one`  |     | ✅    | res.users    |

**Access Rights:**

| Name                         | Group         | Perms     |
| ---------------------------- | ------------- | --------- |
| digest.digest.administration | Access Rights | `R/W/C/D` |
| digest.digest.user           | Role / User   | `R`       |

### 🗃️ `crm.lead.scoring.frequency.field` — Fields that can be used for predictive lead scoring computation

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation        |
| -------------- | --------------- | ---------- | --- | ----- | --------------- |
| `color`        | Color           | `integer`  |     | ✅    |                 |
| `create_date`  | Created on      | `datetime` |     | ✅    |                 |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users       |
| `display_name` | Display Name    | `char`     |     |       |                 |
| `field_id`     | Field           | `many2one` | ✅  | ✅    | ir.model.fields |
| `id`           | ID              | `integer`  |     | ✅    |                 |
| `name`         | Field Label     | `char`     |     |       |                 |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                 |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                                           | Group                            | Perms |
| ---------------------------------------------- | -------------------------------- | ----- |
| access_crm_lead_scoring_frequency_field        | Sales / User: Own Documents Only | `R`   |
| access_crm_lead_scoring_frequency_field_system | Role / Administrator             | `R`   |

### 🗃️ `crm.lead.lost` — Get Lost Reason

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field            | Label           | Type        | Req | Store | Relation        |
| ---------------- | --------------- | ----------- | --- | ----- | --------------- |
| `create_date`    | Created on      | `datetime`  |     | ✅    |                 |
| `create_uid`     | Created by      | `many2one`  |     | ✅    | res.users       |
| `display_name`   | Display Name    | `char`      |     |       |                 |
| `id`             | ID              | `integer`   |     | ✅    |                 |
| `lead_ids`       | Leads           | `many2many` |     | ✅    | crm.lead        |
| `lost_feedback`  | Closing Note    | `html`      |     | ✅    |                 |
| `lost_reason_id` | Lost Reason     | `many2one`  |     | ✅    | crm.lost.reason |
| `write_date`     | Last Updated on | `datetime`  |     | ✅    |                 |
| `write_uid`      | Last Updated by | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                 | Group                            | Perms   |
| -------------------- | -------------------------------- | ------- |
| access.crm.lead.lost | Sales / User: Own Documents Only | `R/W/C` |

### 🗃️ `crm.lead.scoring.frequency` — Lead Scoring Frequency

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
| `lost_count`   | Lost Count      | `float`    |     | ✅    |           |
| `team_id`      | Sales Team      | `many2one` |     | ✅    | crm.team  |
| `value`        | Value           | `char`     |     | ✅    |           |
| `variable`     | Variable        | `char`     |     | ✅    |           |
| `won_count`    | Won Count       | `float`    |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                                     | Group                            | Perms |
| ---------------------------------------- | -------------------------------- | ----- |
| access_crm_lead_scoring_frequency        | Sales / User: Own Documents Only | `R`   |
| access_crm_lead_scoring_frequency_system | Role / Administrator             | `R`   |

### 🗃️ `crm.merge.opportunity` — Merge Opportunities

> ✳️ Transient (Wizard)

        Merge opportunities together.
        If we're talking about opportunities, it's just because it makes more sense
        to merge opps than leads, because the leads are more ephemeral objects.
        But since opportunities are leads, it's also possible to merge leads
        together (resulting in a new lead), or leads and opps together (resulting
        in a new opp).

**Fields:**

| Field             | Label               | Type        | Req | Store | Relation  |
| ----------------- | ------------------- | ----------- | --- | ----- | --------- |
| `create_date`     | Created on          | `datetime`  |     | ✅    |           |
| `create_uid`      | Created by          | `many2one`  |     | ✅    | res.users |
| `display_name`    | Display Name        | `char`      |     |       |           |
| `id`              | ID                  | `integer`   |     | ✅    |           |
| `opportunity_ids` | Leads/Opportunities | `many2many` |     | ✅    | crm.lead  |
| `team_id`         | Sales Team          | `many2one`  |     | ✅    | crm.team  |
| `user_id`         | Salesperson         | `many2one`  |     | ✅    | res.users |
| `write_date`      | Last Updated on     | `datetime`  |     | ✅    |           |
| `write_uid`       | Last Updated by     | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                         | Group                            | Perms   |
| ---------------------------- | -------------------------------- | ------- |
| access.crm.merge.opportunity | Sales / User: Own Documents Only | `R/W/C` |

### 🗃️ `crm.lost.reason` — Opp. Lost Reason

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `active`       | Active          | `boolean`  |     | ✅    |           |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `leads_count`  | Leads Count     | `integer`  |     |       |           |
| `name`         | Description     | `char`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                     | Group                            | Perms     |
| ------------------------ | -------------------------------- | --------- |
| crm.lost.reason.salesman | Sales / User: Own Documents Only | `R`       |
| crm.lost.reason.manager  | Sales / Administrator            | `R/W/C/D` |
| crm.lost.reason.user     | Role / User                      | `R`       |

### 🗃️ `ir.config_parameter` — System Parameter

Per-database storage of configuration key-value pairs.

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `key`          | Key             | `char`     | ✅  | ✅    |           |
| `value`        | Value           | `text`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                       | Group                | Perms     |
| -------------------------- | -------------------- | --------- |
| access_ir_config_parameter | Category / Manager   | `R`       |
| ir_config_parameter_system | Role / Administrator | `R/W/C/D` |

### 🗃️ `crm.lead.pls.update` — Update the probabilities

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field            | Label           | Type        | Req | Store | Relation                         |
| ---------------- | --------------- | ----------- | --- | ----- | -------------------------------- |
| `create_date`    | Created on      | `datetime`  |     | ✅    |                                  |
| `create_uid`     | Created by      | `many2one`  |     | ✅    | res.users                        |
| `display_name`   | Display Name    | `char`      |     |       |                                  |
| `id`             | ID              | `integer`   |     | ✅    |                                  |
| `pls_fields`     | Pls Fields      | `many2many` |     | ✅    | crm.lead.scoring.frequency.field |
| `pls_start_date` | Pls Start Date  | `date`      | ✅  | ✅    |                                  |
| `write_date`     | Last Updated on | `datetime`  |     | ✅    |                                  |
| `write_uid`      | Last Updated by | `many2one`  |     | ✅    | res.users                        |

**Access Rights:**

| Name                              | Group         | Perms     |
| --------------------------------- | ------------- | --------- |
| crm.lead.pls.update.access.system | Access Rights | `R/W/C/D` |

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

### 🗃️ `utm.campaign` — UTM Campaign

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                                      | Type        | Req | Store | Relation        |
| ------------------------------- | ------------------------------------------ | ----------- | --- | ----- | --------------- |
| `ab_testing_completed`          | A/B Testing Campaign Finished              | `boolean`   |     | ✅    |                 |
| `ab_testing_mailings_count`     | A/B Test Mailings #                        | `integer`   |     |       |                 |
| `ab_testing_schedule_datetime`  | Send Final On                              | `datetime`  |     | ✅    |                 |
| `ab_testing_winner_mailing_id`  | A/B Campaign Winner Mailing                | `many2one`  |     | ✅    | mailing.mailing |
| `ab_testing_winner_selection`   | Winner Selection                           | `selection` |     | ✅    |                 |
| `active`                        | Active                                     | `boolean`   |     | ✅    |                 |
| `bounced_ratio`                 | Bounced Ratio                              | `float`     |     |       |                 |
| `click_count`                   | Number of clicks generated by the campaign | `integer`   |     |       |                 |
| `color`                         | Color Index                                | `integer`   |     | ✅    |                 |
| `company_id`                    | Company                                    | `many2one`  |     | ✅    | res.company     |
| `create_date`                   | Created on                                 | `datetime`  |     | ✅    |                 |
| `create_uid`                    | Created by                                 | `many2one`  |     | ✅    | res.users       |
| `crm_lead_count`                | Leads/Opportunities count                  | `integer`   |     |       |                 |
| `currency_id`                   | Currency                                   | `many2one`  |     |       | res.currency    |
| `display_name`                  | Display Name                               | `char`      |     |       |                 |
| `id`                            | ID                                         | `integer`   |     | ✅    |                 |
| `invoiced_amount`               | Revenues generated by the campaign         | `integer`   |     |       |                 |
| `is_auto_campaign`              | Automatically Generated Campaign           | `boolean`   |     | ✅    |                 |
| `is_mailing_campaign_activated` | Is Mailing Campaign Activated              | `boolean`   |     |       |                 |
| `mailing_mail_count`            | Number of Mass Mailing                     | `integer`   |     |       |                 |
| `mailing_mail_ids`              | Mass Mailings                              | `one2many`  |     | ✅    | mailing.mailing |
| `name`                          | Campaign Identifier                        | `char`      | ✅  | ✅    |                 |
| `opened_ratio`                  | Opened Ratio                               | `float`     |     |       |                 |
| `quotation_count`               | Quotation Count                            | `integer`   |     |       |                 |
| `received_ratio`                | Received Ratio                             | `float`     |     |       |                 |
| `replied_ratio`                 | Replied Ratio                              | `float`     |     |       |                 |
| `stage_id`                      | Stage                                      | `many2one`  | ✅  | ✅    | utm.stage       |
| `tag_ids`                       | Tags                                       | `many2many` |     | ✅    | utm.tag         |
| `title`                         | Campaign Name                              | `char`      | ✅  | ✅    |                 |
| `use_leads`                     | Use Leads                                  | `boolean`   |     |       |                 |
| `user_id`                       | Responsible                                | `many2one`  | ✅  | ✅    | res.users       |
| `write_date`                    | Last Updated on                            | `datetime`  |     | ✅    |                 |
| `write_uid`                     | Last Updated by                            | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                     | Group                  | Perms     |
| ------------------------ | ---------------------- | --------- |
| utm.campaign             | Email Marketing / User | `R/W/C/D` |
| utm.campaign.system      | Role / Administrator   | `R/W/C/D` |
| access_utm_campaign_user | Role / User            | `R/W/C`   |
