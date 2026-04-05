---
title: "Mass mailing on lead / opportunities"
module: "mass_mailing_crm"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Email Marketing"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_______________]
---

# 🟢 Mass mailing on lead / opportunities

> **Module:** `mass_mailing_crm` | **Version:** `19.0.1.0` **Category:** Email Marketing
> | **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[crm]] [[mass_mailing]]

## 📖 Description

UTM and mass mailing on lead / opportunities

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT mailing.mailing.view.form.inherit.crm (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

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

### 🗃️ `mailing.mailing` — Mass Mailing

> 📧 Mail Thread

Mass Mailing models the sending of emails to a list of recipients for a mass mailing
campaign.

**Fields:**

| Field                           | Label                                       | Type        | Req | Store | Relation           |
| ------------------------------- | ------------------------------------------- | ----------- | --- | ----- | ------------------ |
| `ab_testing_completed`          | A/B Testing Campaign Finished               | `boolean`   |     |       |                    |
| `ab_testing_description`        | A/B Testing Description                     | `html`      |     |       |                    |
| `ab_testing_enabled`            | Allow A/B Testing                           | `boolean`   |     | ✅    |                    |
| `ab_testing_is_winner_mailing`  | Is the Winner of its Campaign               | `boolean`   |     |       |                    |
| `ab_testing_mailings_count`     | A/B Test Mailings #                         | `integer`   |     |       |                    |
| `ab_testing_pc`                 | A/B Testing percentage                      | `integer`   |     | ✅    |                    |
| `ab_testing_schedule_datetime`  | Send Final On                               | `datetime`  |     |       |                    |
| `ab_testing_winner_selection`   | Winner Selection                            | `selection` |     |       |                    |
| `active`                        | Active                                      | `boolean`   |     | ✅    |                    |
| `activity_calendar_event_id`    | Next Activity Calendar Event                | `many2one`  |     |       | calendar.event     |
| `activity_date_deadline`        | Next Activity Deadline                      | `date`      |     |       |                    |
| `activity_exception_decoration` | Activity Exception Decoration               | `selection` |     |       |                    |
| `activity_exception_icon`       | Icon                                        | `char`      |     |       |                    |
| `activity_ids`                  | Activities                                  | `one2many`  |     | ✅    | mail.activity      |
| `activity_state`                | Activity State                              | `selection` |     |       |                    |
| `activity_summary`              | Next Activity Summary                       | `char`      |     |       |                    |
| `activity_type_icon`            | Activity Type Icon                          | `char`      |     |       |                    |
| `activity_type_id`              | Next Activity Type                          | `many2one`  |     |       | mail.activity.type |
| `activity_user_id`              | Responsible User                            | `many2one`  |     |       | res.users          |
| `attachment_ids`                | Attachments                                 | `many2many` |     | ✅    | ir.attachment      |
| `automated_marketing`           | Specific mailing used in marketing campaign | `boolean`   |     | ✅    |                    |
| `body_arch`                     | Body                                        | `html`      |     | ✅    |                    |
| `body_html`                     | Body converted to be sent by mail           | `html`      |     | ✅    |                    |
| `bounced`                       | Bounced                                     | `integer`   |     |       |                    |
| `bounced_ratio`                 | Bounced Ratio                               | `float`     |     |       |                    |
| `calendar_date`                 | Calendar Date                               | `datetime`  |     | ✅    |                    |
| `campaign_id`                   | UTM Campaign                                | `many2one`  |     | ✅    | utm.campaign       |
| `canceled`                      | Canceled                                    | `integer`   |     |       |                    |
| `clicked`                       | Clicked                                     | `integer`   |     |       |                    |
| `clicks_ratio`                  | Number of Clicks                            | `float`     |     |       |                    |
| `color`                         | Color Index                                 | `integer`   |     | ✅    |                    |
| `contact_list_ids`              | Mailing Lists                               | `many2many` |     | ✅    | mailing.list       |
| `create_date`                   | Created on                                  | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                                  | `many2one`  |     | ✅    | res.users          |
| `crm_lead_count`                | Leads/Opportunities Count                   | `integer`   |     |       |                    |
| `delivered`                     | Delivered                                   | `integer`   |     |       |                    |
| `display_name`                  | Display Name                                | `char`      |     |       |                    |
| `email_from`                    | Send From                                   | `char`      |     | ✅    |                    |
| `expected`                      | Expected                                    | `integer`   |     |       |                    |
| `failed`                        | Failed                                      | `integer`   |     |       |                    |
| `favorite`                      | Favorite                                    | `boolean`   |     | ✅    |                    |
| `favorite_date`                 | Favorite Date                               | `datetime`  |     | ✅    |                    |
| `has_message`                   | Has Message                                 | `boolean`   |     |       |                    |
| `id`                            | ID                                          | `integer`   |     | ✅    |                    |
| `is_ab_test_sent`               | Is Ab Test Sent                             | `boolean`   |     |       |                    |
| `is_body_empty`                 | Is Body Empty                               | `boolean`   |     |       |                    |
| `keep_archives`                 | Keep Archives                               | `boolean`   |     | ✅    |                    |
| `kpi_mail_required`             | KPI mail required                           | `boolean`   |     | ✅    |                    |
| `lang`                          | Language                                    | `char`      |     | ✅    |                    |
| `link_trackers_count`           | Link Trackers Count                         | `integer`   |     |       |                    |
| `mailing_domain`                | Domain                                      | `char`      |     | ✅    |                    |
| `mailing_filter_count`          | # Favorite Filters                          | `integer`   |     |       |                    |
| `mailing_filter_domain`         | Favorite filter domain                      | `char`      |     |       |                    |
| `mailing_filter_id`             | Favorite Filter                             | `many2one`  |     | ✅    | mailing.filter     |
| `mailing_model_id`              | Recipients Model                            | `many2one`  | ✅  | ✅    | ir.model           |
| `mailing_model_name`            | Recipients Model Name                       | `char`      |     |       |                    |
| `mailing_model_real`            | Recipients Real Model                       | `char`      |     |       |                    |
| `mailing_on_mailing_list`       | Based on Mailing Lists                      | `boolean`   |     |       |                    |
| `mailing_trace_ids`             | Emails Statistics                           | `one2many`  |     | ✅    | mailing.trace      |
| `mailing_type`                  | Mailing Type                                | `selection` | ✅  | ✅    |                    |
| `mailing_type_description`      | Mailing Type Description                    | `char`      |     |       |                    |
| `mail_server_available`         | Mail Server Available                       | `boolean`   |     |       |                    |
| `mail_server_id`                | Mail Server                                 | `many2one`  |     | ✅    | ir.mail_server     |
| `marketing_activity_ids`        | Marketing Activities                        | `one2many`  |     | ✅    | marketing.activity |
| `medium_id`                     | Medium                                      | `many2one`  |     | ✅    | utm.medium         |
| `message_attachment_count`      | Attachment Count                            | `integer`   |     |       |                    |
| `message_follower_ids`          | Followers                                   | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`             | Message Delivery error                      | `boolean`   |     |       |                    |
| `message_has_error_counter`     | Number of errors                            | `integer`   |     |       |                    |
| `message_has_sms_error`         | SMS Delivery error                          | `boolean`   |     |       |                    |
| `message_ids`                   | Messages                                    | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`           | Is Follower                                 | `boolean`   |     |       |                    |
| `message_needaction`            | Action Needed                               | `boolean`   |     |       |                    |
| `message_needaction_counter`    | Number of Actions                           | `integer`   |     |       |                    |
| `message_partner_ids`           | Followers (Partners)                        | `many2many` |     |       | res.partner        |
| `my_activity_date_deadline`     | My Activity Deadline                        | `date`      |     |       |                    |
| `name`                          | Name                                        | `char`      |     |       |                    |
| `next_departure`                | Scheduled date                              | `datetime`  |     |       |                    |
| `next_departure_is_past`        | Next Departure Is Past                      | `boolean`   |     |       |                    |
| `opened`                        | Opened                                      | `integer`   |     |       |                    |
| `opened_ratio`                  | Opened Ratio                                | `float`     |     |       |                    |
| `pending`                       | Pending                                     | `integer`   |     |       |                    |
| `preview`                       | Preview                                     | `char`      |     | ✅    |                    |
| `process`                       | Process                                     | `integer`   |     |       |                    |
| `rating_ids`                    | Ratings                                     | `one2many`  |     | ✅    | rating.rating      |
| `received_ratio`                | Received Ratio                              | `float`     |     |       |                    |
| `render_model`                  | Rendering Model                             | `char`      |     |       |                    |
| `replied`                       | Replied                                     | `integer`   |     |       |                    |
| `replied_ratio`                 | Replied Ratio                               | `float`     |     |       |                    |
| `reply_to`                      | Reply To                                    | `char`      |     | ✅    |                    |
| `reply_to_mode`                 | Reply-To Mode                               | `selection` |     | ✅    |                    |
| `sale_invoiced_amount`          | Invoiced Amount                             | `integer`   |     |       |                    |
| `sale_quotation_count`          | Quotation Count                             | `integer`   |     |       |                    |
| `scheduled`                     | Scheduled                                   | `integer`   |     |       |                    |
| `schedule_date`                 | Scheduled for                               | `datetime`  |     | ✅    |                    |
| `schedule_type`                 | Schedule                                    | `selection` | ✅  | ✅    |                    |
| `sent`                          | Sent                                        | `integer`   |     |       |                    |
| `sent_date`                     | Sent Date                                   | `datetime`  |     | ✅    |                    |
| `source_id`                     | Source                                      | `many2one`  | ✅  | ✅    | utm.source         |
| `state`                         | Status                                      | `selection` | ✅  | ✅    |                    |
| `subject`                       | Subject                                     | `char`      | ✅  | ✅    |                    |
| `total`                         | Total                                       | `integer`   |     |       |                    |
| `use_exclusion_list`            | Use Exclusion List                          | `boolean`   |     | ✅    |                    |
| `use_leads`                     | Use Leads                                   | `boolean`   |     |       |                    |
| `user_id`                       | Responsible                                 | `many2one`  |     | ✅    | res.users          |
| `warning_message`               | Warning Message                             | `char`      |     |       |                    |
| `website_message_ids`           | Website Messages                            | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on                             | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by                             | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                           | Group                  | Perms     |
| ------------------------------ | ---------------------- | --------- |
| access.mailing.mailing.mm.user | Email Marketing / User | `R/W/C/D` |
| access.mailing.mailing.system  | Role / Administrator   | `R/W/C/D` |

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
