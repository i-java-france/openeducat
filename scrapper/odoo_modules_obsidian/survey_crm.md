---
title: "Survey CRM"
module: "survey_crm"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Surveys"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_______]
---

# 🟢 Survey CRM

> **Module:** `survey_crm` | **Version:** `19.0.1.0` **Category:** Surveys |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[survey]] [[crm]]

## 📖 Description

Bridge module between Survey and CRM. Enables the creation of a lead from a survey when
the participant selects lead-generating answers. An option on the suggested answers can
be activated to make them lead-generating.

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT survey.question.form.inherit.survey.crm (form)`
- `* INHERIT survey.survey.view.form.inherit.survey.crm (form)`
- `* INHERIT survey.survey.view.kanban.inherit.survey.crm (kanban)`
- `* INHERIT survey.user_input.view.form.inherit.survey.crm (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**6 model(s) defined by this module:**

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

### 🗃️ `survey.survey` — Survey

> 📧 Mail Thread

Add the new 'Lead Qualification' survey template to the templates that can be selected
in the helper screen.

**Fields:**

| Field                             | Label                          | Type        | Req | Store | Relation           |
| --------------------------------- | ------------------------------ | ----------- | --- | ----- | ------------------ |
| `access_mode`                     | Access Mode                    | `selection` | ✅  | ✅    |                    |
| `access_token`                    | Access Token                   | `char`      |     | ✅    |                    |
| `active`                          | Active                         | `boolean`   |     | ✅    |                    |
| `activity_calendar_event_id`      | Next Activity Calendar Event   | `many2one`  |     |       | calendar.event     |
| `activity_date_deadline`          | Next Activity Deadline         | `date`      |     |       |                    |
| `activity_exception_decoration`   | Activity Exception Decoration  | `selection` |     |       |                    |
| `activity_exception_icon`         | Icon                           | `char`      |     |       |                    |
| `activity_ids`                    | Activities                     | `one2many`  |     | ✅    | mail.activity      |
| `activity_state`                  | Activity State                 | `selection` |     |       |                    |
| `activity_summary`                | Next Activity Summary          | `char`      |     |       |                    |
| `activity_type_icon`              | Activity Type Icon             | `char`      |     |       |                    |
| `activity_type_id`                | Next Activity Type             | `many2one`  |     |       | mail.activity.type |
| `activity_user_id`                | Responsible User               | `many2one`  |     |       | res.users          |
| `allowed_survey_types`            | Allowed survey types           | `json`      |     |       |                    |
| `answer_count`                    | Registered                     | `integer`   |     |       |                    |
| `answer_done_count`               | Attempts                       | `integer`   |     |       |                    |
| `answer_duration_avg`             | Average Duration               | `float`     |     |       |                    |
| `answer_score_avg`                | Avg Score (%)                  | `float`     |     |       |                    |
| `attempts_limit`                  | Number of attempts             | `integer`   |     | ✅    |                    |
| `background_image`                | Background Image               | `binary`    |     | ✅    |                    |
| `background_image_url`            | Background Url                 | `char`      |     |       |                    |
| `certification`                   | Is a Certification             | `boolean`   |     | ✅    |                    |
| `certification_badge_id`          | Certification Badge            | `many2one`  |     | ✅    | gamification.badge |
| `certification_badge_id_dummy`    | Certification Badge            | `many2one`  |     |       | gamification.badge |
| `certification_give_badge`        | Give Badge                     | `boolean`   |     | ✅    |                    |
| `certification_mail_template_id`  | Certified Email Template       | `many2one`  |     | ✅    | mail.template      |
| `certification_report_layout`     | Certification template         | `selection` |     | ✅    |                    |
| `certification_validity_months`   | Validity                       | `integer`   |     | ✅    |                    |
| `color`                           | Color Index                    | `integer`   |     | ✅    |                    |
| `course_id`                       | Course                         | `many2one`  |     | ✅    | op.course          |
| `create_date`                     | Created on                     | `datetime`  |     | ✅    |                    |
| `create_uid`                      | Created by                     | `many2one`  |     | ✅    | res.users          |
| `description`                     | Description                    | `html`      |     | ✅    |                    |
| `description_done`                | End Message                    | `html`      |     | ✅    |                    |
| `display_name`                    | Display Name                   | `char`      |     |       |                    |
| `generate_lead`                   | Lead Generating                | `boolean`   |     | ✅    |                    |
| `has_conditional_questions`       | Contains conditional questions | `boolean`   |     |       |                    |
| `has_message`                     | Has Message                    | `boolean`   |     |       |                    |
| `id`                              | ID                             | `integer`   |     | ✅    |                    |
| `is_attempts_limited`             | Limited number of attempts     | `boolean`   |     | ✅    |                    |
| `is_time_limited`                 | The survey is limited in time  | `boolean`   |     | ✅    |                    |
| `lang_ids`                        | Languages                      | `many2many` |     | ✅    | res.lang           |
| `lead_count`                      | Leads                          | `integer`   |     |       |                    |
| `lead_ids`                        | Lead                           | `one2many`  |     | ✅    | crm.lead           |
| `message_attachment_count`        | Attachment Count               | `integer`   |     |       |                    |
| `message_follower_ids`            | Followers                      | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`               | Message Delivery error         | `boolean`   |     |       |                    |
| `message_has_error_counter`       | Number of errors               | `integer`   |     |       |                    |
| `message_has_sms_error`           | SMS Delivery error             | `boolean`   |     |       |                    |
| `message_ids`                     | Messages                       | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`             | Is Follower                    | `boolean`   |     |       |                    |
| `message_needaction`              | Action Needed                  | `boolean`   |     |       |                    |
| `message_needaction_counter`      | Number of Actions              | `integer`   |     |       |                    |
| `message_partner_ids`             | Followers (Partners)           | `many2many` |     |       | res.partner        |
| `my_activity_date_deadline`       | My Activity Deadline           | `date`      |     |       |                    |
| `page_ids`                        | Pages                          | `one2many`  |     |       | survey.question    |
| `progression_mode`                | Display Progress as            | `selection` |     | ✅    |                    |
| `question_and_page_ids`           | Sections and Questions         | `one2many`  |     | ✅    | survey.question    |
| `question_count`                  | # Questions                    | `integer`   |     |       |                    |
| `question_ids`                    | Questions                      | `one2many`  |     |       | survey.question    |
| `questions_layout`                | Pagination                     | `selection` | ✅  | ✅    |                    |
| `questions_selection`             | Question Selection             | `selection` | ✅  | ✅    |                    |
| `rating_ids`                      | Ratings                        | `one2many`  |     | ✅    | rating.rating      |
| `restrict_user_ids`               | Restricted to                  | `many2many` |     | ✅    | res.users          |
| `scoring_max_obtainable`          | Maximum obtainable score       | `float`     |     |       |                    |
| `scoring_success_min`             | Required Score (%)             | `float`     |     | ✅    |                    |
| `scoring_type`                    | Scoring                        | `selection` | ✅  | ✅    |                    |
| `session_answer_count`            | Answers Count                  | `integer`   |     |       |                    |
| `session_available`               | Live session available         | `boolean`   |     |       |                    |
| `session_code`                    | Session Code                   | `char`      |     | ✅    |                    |
| `session_link`                    | Session Link                   | `char`      |     |       |                    |
| `session_question_answer_count`   | Question Answers Count         | `integer`   |     |       |                    |
| `session_question_id`             | Current Question               | `many2one`  |     | ✅    | survey.question    |
| `session_question_start_time`     | Current Question Start Time    | `datetime`  |     | ✅    |                    |
| `session_show_leaderboard`        | Show Session Leaderboard       | `boolean`   |     |       |                    |
| `session_speed_rating`            | Reward quick answers           | `boolean`   |     | ✅    |                    |
| `session_speed_rating_time_limit` | Time limit (seconds)           | `integer`   |     | ✅    |                    |
| `session_start_time`              | Current Session Start Time     | `datetime`  |     | ✅    |                    |
| `session_state`                   | Session State                  | `selection` |     | ✅    |                    |
| `success_count`                   | Success                        | `integer`   |     |       |                    |
| `success_ratio`                   | Success Ratio (%)              | `integer`   |     |       |                    |
| `survey_type`                     | Survey Type                    | `selection` | ✅  | ✅    |                    |
| `team_id`                         | Assign Leads to                | `many2one`  |     | ✅    | crm.team           |
| `time_limit`                      | Time limit (minutes)           | `float`     |     | ✅    |                    |
| `title`                           | Survey Title                   | `char`      | ✅  | ✅    |                    |
| `user_id`                         | Responsible                    | `many2one`  |     | ✅    | res.users          |
| `user_input_ids`                  | User responses                 | `one2many`  |     | ✅    | survey.user_input  |
| `users_can_go_back`               | Users can go back              | `boolean`   |     | ✅    |                    |
| `users_can_signup`                | Users can signup               | `boolean`   |     |       |                    |
| `users_login_required`            | Require Login                  | `boolean`   |     | ✅    |                    |
| `website_message_ids`             | Website Messages               | `one2many`  |     | ✅    | mail.message       |
| `write_date`                      | Last Updated on                | `datetime`  |     | ✅    |                    |
| `write_uid`                       | Last Updated by                | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                         | Group                   | Perms     |
| ---------------------------- | ----------------------- | --------- |
| survey.survey.survey.user    | Surveys / User          | `R/W/C/D` |
| survey.survey.survey.manager | Surveys / Administrator | `R/W/C/D` |
| survey.survey.user           | Role / User             | `-`       |
| survey.survey.all            | Everyone                | `-`       |

**Record Rules:**

- **Survey: manager: all** (29) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Survey: officer: unrestricted survey or in restricted users** (28) `R/W/C/D`
  - Domain:
    `[             '|', ('restrict_user_ids', 'in', user.id), ('restrict_user_ids', '=', False)]`

### 🗃️ `survey.user_input` — Survey User Input

> 📧 Mail Thread

Metadata for a set of one user's answers to a particular survey

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation               |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ---------------------- |
| `access_token`                  | Identification token          | `char`      | ✅  | ✅    |                        |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event         |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                        |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                        |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                        |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity          |
| `activity_state`                | Activity State                | `selection` |     |       |                        |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                        |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                        |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type     |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users              |
| `attempts_count`                | Attempts Count                | `integer`   |     |       |                        |
| `attempts_limit`                | Number of attempts            | `integer`   |     |       |                        |
| `attempts_number`               | Attempt n°                    | `integer`   |     |       |                        |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                        |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users              |
| `deadline`                      | Deadline                      | `datetime`  |     | ✅    |                        |
| `display_name`                  | Display Name                  | `char`      |     |       |                        |
| `email`                         | Email                         | `char`      |     | ✅    |                        |
| `end_datetime`                  | End date and time             | `datetime`  |     | ✅    |                        |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                        |
| `id`                            | ID                            | `integer`   |     | ✅    |                        |
| `invite_token`                  | Invite token                  | `char`      |     | ✅    |                        |
| `is_attempts_limited`           | Limited number of attempts    | `boolean`   |     |       |                        |
| `is_session_answer`             | Is in a Session               | `boolean`   |     | ✅    |                        |
| `lang_id`                       | Language                      | `many2one`  |     | ✅    | res.lang               |
| `last_displayed_page_id`        | Last displayed question/page  | `many2one`  |     | ✅    | survey.question        |
| `lead_id`                       | Lead                          | `many2one`  |     | ✅    | crm.lead               |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                        |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers         |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                        |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                        |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                        |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message           |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                        |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                        |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                        |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner            |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                        |
| `nickname`                      | Nickname                      | `char`      |     | ✅    |                        |
| `partner_id`                    | Contact                       | `many2one`  |     | ✅    | res.partner            |
| `predefined_question_ids`       | Predefined Questions          | `many2many` |     | ✅    | survey.question        |
| `question_time_limit_reached`   | Question Time Limit Reached   | `boolean`   |     |       |                        |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating          |
| `scoring_percentage`            | Score (%)                     | `float`     |     | ✅    |                        |
| `scoring_success`               | Quiz Passed                   | `boolean`   |     | ✅    |                        |
| `scoring_total`                 | Total Score                   | `float`     |     | ✅    |                        |
| `scoring_type`                  | Scoring                       | `selection` |     |       |                        |
| `start_datetime`                | Start date and time           | `datetime`  |     | ✅    |                        |
| `state`                         | Status                        | `selection` |     | ✅    |                        |
| `survey_first_submitted`        | Survey First Submitted        | `boolean`   |     | ✅    |                        |
| `survey_id`                     | Survey                        | `many2one`  | ✅  | ✅    | survey.survey          |
| `survey_time_limit_reached`     | Survey Time Limit Reached     | `boolean`   |     |       |                        |
| `test_entry`                    | Test Entry                    | `boolean`   |     | ✅    |                        |
| `user_input_line_ids`           | Answers                       | `one2many`  |     | ✅    | survey.user_input.line |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message           |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                        |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                             | Group                   | Perms     |
| -------------------------------- | ----------------------- | --------- |
| survey.user_input.survey.user    | Surveys / User          | `R/W/C/D` |
| survey.user_input.survey.manager | Surveys / Administrator | `R/W/C/D` |
| survey.user_input.user           | Role / User             | `-`       |
| survey.user_input.all            | Everyone                | `-`       |

**Record Rules:**

- **Survey user input: manager: all non specialized surveys** (29) `R/W/C/D`
  - Domain:
    `[('survey_id.survey_type', 'in', ('assessment', 'custom', 'live_session', 'survey'))]`
- **Survey user input: officer: unrestricted survey or in restricted users** (28)
  `R/W/C/D`
  - Domain:
    `[             '&', ('survey_id.survey_type', 'in', ('assessment', 'custom', 'live_session', 'survey')),             '|', ('survey_id.restrict_user_ids', 'in', user.id),                  ('survey_id.restrict_user_ids', '=', False)]`

### 🗃️ `survey.question.answer` — Survey Label

A preconfigured answer for a question. This model stores values used for

      * simple choice, multiple choice: proposed values for the selection /
        radio;
      * matrix: row and column values;

**Fields:**

| Field                  | Label                    | Type        | Req | Store | Relation        |
| ---------------------- | ------------------------ | ----------- | --- | ----- | --------------- |
| `answer_score`         | Score                    | `float`     |     | ✅    |                 |
| `create_date`          | Created on               | `datetime`  |     | ✅    |                 |
| `create_uid`           | Created by               | `many2one`  |     | ✅    | res.users       |
| `display_name`         | Display Name             | `char`      |     |       |                 |
| `generate_lead`        | Lead creation            | `boolean`   |     | ✅    |                 |
| `id`                   | ID                       | `integer`   |     | ✅    |                 |
| `is_correct`           | Correct                  | `boolean`   |     | ✅    |                 |
| `matrix_question_id`   | Question (as matrix row) | `many2one`  |     | ✅    | survey.question |
| `question_id`          | Question                 | `many2one`  |     | ✅    | survey.question |
| `question_type`        | Question Type            | `selection` |     |       |                 |
| `scoring_type`         | Scoring Type             | `selection` |     |       |                 |
| `sequence`             | Label Sequence order     | `integer`   |     | ✅    |                 |
| `value`                | Suggested value          | `char`      |     | ✅    |                 |
| `value_image`          | Image                    | `binary`    |     | ✅    |                 |
| `value_image_filename` | Image Filename           | `char`      |     | ✅    |                 |
| `value_label`          | Value Label              | `char`      |     |       |                 |
| `write_date`           | Last Updated on          | `datetime`  |     | ✅    |                 |
| `write_uid`            | Last Updated by          | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                                  | Group                   | Perms     |
| ------------------------------------- | ----------------------- | --------- |
| survey.question.answer.survey.user    | Surveys / User          | `R/W/C/D` |
| survey.question.answer.survey.manager | Surveys / Administrator | `R/W/C/D` |
| survey.question.answer.user           | Role / User             | `-`       |
| survey.question.answer.all            | Everyone                | `-`       |

**Record Rules:**

- **Survey question answer: manager: all** (29) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Survey question answer: officer: unrestricted survey or in restricted users** (28)
  `R/W/C/D`
  - Domain:
    `[             '|',                 '|', ('question_id.survey_id.restrict_user_ids', 'in', user.id), ('matrix_question_id.survey_id.restrict_user_ids', 'in', user.id),                 '|', ('question_id.survey_id.restrict_user_ids', '=', False), ('matrix_question_id.survey_id.restrict_user_ids', '=', False)]         `

### 🗃️ `survey.question` — Survey Question

Questions that will be asked in a survey.

        Each question can have one of more suggested answers (eg. in case of
        multi-answer checkboxes, radio buttons...).

        Technical note:

        survey.question is also the model used for the survey's pages (with the "is_page" field set to True).

        A page corresponds to a "section" in the interface, and the fact that it separates the survey in
        actual pages in the interface depends on the "questions_layout" parameter on the survey.survey model.
        Pages are also used when randomizing questions. The randomization can happen within a "page".

        Using the same model for questions and pages allows to put all the pages and questions together in a o2m field
        (see survey.survey.question_and_page_ids) on the view side and easily reorganize your survey by dragging the
        items around.

        It also removes on level of encoding by directly having 'Add a page' and 'Add a question'
        links on the list view of questions, enabling a faster encoding.

        However, this has the downside of making the code reading a little bit more complicated.
        Efforts were made at the model level to create computed fields so that the use of these models
        still seems somewhat logical. That means:
        - A survey still has "page_ids" (question_and_page_ids filtered on is_page = True)
        - These "page_ids" still have question_ids (questions located between this page and the next)
        - These "question_ids" still have a "page_id"

        That makes the use and display of these information at view and controller levels easier to understand.

**Fields:**

| Field                                    | Label                           | Type        | Req | Store | Relation               |
| ---------------------------------------- | ------------------------------- | ----------- | --- | ----- | ---------------------- |
| `allowed_triggering_question_ids`        | Allowed Triggering Questions    | `many2many` |     |       | survey.question        |
| `answer_date`                            | Correct date answer             | `date`      |     | ✅    |                        |
| `answer_datetime`                        | Correct datetime answer         | `datetime`  |     | ✅    |                        |
| `answer_numerical_box`                   | Correct numerical answer        | `float`     |     | ✅    |                        |
| `answer_score`                           | Score                           | `float`     |     | ✅    |                        |
| `background_image`                       | Background Image                | `binary`    |     | ✅    |                        |
| `background_image_url`                   | Background Url                  | `char`      |     |       |                        |
| `comment_count_as_answer`                | Comment is an answer            | `boolean`   |     | ✅    |                        |
| `comments_allowed`                       | Show Comments Field             | `boolean`   |     | ✅    |                        |
| `comments_message`                       | Comment Message                 | `char`      |     | ✅    |                        |
| `constr_error_msg`                       | Error message                   | `char`      |     | ✅    |                        |
| `constr_mandatory`                       | Mandatory Answer                | `boolean`   |     | ✅    |                        |
| `create_date`                            | Created on                      | `datetime`  |     | ✅    |                        |
| `create_uid`                             | Created by                      | `many2one`  |     | ✅    | res.users              |
| `description`                            | Description                     | `html`      |     | ✅    |                        |
| `display_name`                           | Display Name                    | `char`      |     |       |                        |
| `generate_lead`                          | Lead Generating                 | `boolean`   |     |       |                        |
| `has_image_only_suggested_answer`        | Has image only suggested answer | `boolean`   |     |       |                        |
| `id`                                     | ID                              | `integer`   |     | ✅    |                        |
| `is_page`                                | Is a page?                      | `boolean`   |     | ✅    |                        |
| `is_placed_before_trigger`               | Is misplaced?                   | `boolean`   |     |       |                        |
| `is_scored_question`                     | Scored                          | `boolean`   |     | ✅    |                        |
| `is_time_customized`                     | Customized speed rewards        | `boolean`   |     | ✅    |                        |
| `is_time_limited`                        | The question is limited in time | `boolean`   |     | ✅    |                        |
| `matrix_row_ids`                         | Matrix Rows                     | `one2many`  |     | ✅    | survey.question.answer |
| `matrix_subtype`                         | Matrix Type                     | `selection` |     | ✅    |                        |
| `page_id`                                | Page                            | `many2one`  |     | ✅    | survey.question        |
| `question_ids`                           | Questions                       | `one2many`  |     |       | survey.question        |
| `question_placeholder`                   | Placeholder                     | `char`      |     | ✅    |                        |
| `questions_selection`                    | Question Selection              | `selection` |     |       |                        |
| `question_type`                          | Question Type                   | `selection` |     | ✅    |                        |
| `random_questions_count`                 | # Questions Randomly Picked     | `integer`   |     | ✅    |                        |
| `save_as_email`                          | Save as user email              | `boolean`   |     | ✅    |                        |
| `save_as_nickname`                       | Save as user nickname           | `boolean`   |     | ✅    |                        |
| `scale_max`                              | Scale Maximum Value             | `integer`   |     | ✅    |                        |
| `scale_max_label`                        | Scale Maximum Label             | `char`      |     | ✅    |                        |
| `scale_mid_label`                        | Scale Middle Label              | `char`      |     | ✅    |                        |
| `scale_min`                              | Scale Minimum Value             | `integer`   |     | ✅    |                        |
| `scale_min_label`                        | Scale Minimum Label             | `char`      |     | ✅    |                        |
| `scoring_type`                           | Scoring Type                    | `selection` |     |       |                        |
| `sequence`                               | Sequence                        | `integer`   |     | ✅    |                        |
| `session_available`                      | Live Session available          | `boolean`   |     |       |                        |
| `suggested_answer_ids`                   | Types of answers                | `one2many`  |     | ✅    | survey.question.answer |
| `survey_id`                              | Survey                          | `many2one`  |     | ✅    | survey.survey          |
| `survey_session_speed_rating`            | Reward quick answers            | `boolean`   |     |       |                        |
| `survey_session_speed_rating_time_limit` | General Time limit (seconds)    | `integer`   |     |       |                        |
| `survey_type`                            | Survey Type                     | `selection` |     |       |                        |
| `time_limit`                             | Time limit (seconds)            | `integer`   |     | ✅    |                        |
| `title`                                  | Title                           | `char`      | ✅  | ✅    |                        |
| `triggering_answer_ids`                  | Triggering Answers              | `many2many` |     | ✅    | survey.question.answer |
| `triggering_question_ids`                | Triggering Questions            | `many2many` |     |       | survey.question        |
| `user_input_line_ids`                    | Answers                         | `one2many`  |     | ✅    | survey.user_input.line |
| `validation_email`                       | Input must be an email          | `boolean`   |     | ✅    |                        |
| `validation_error_msg`                   | Validation Error                | `char`      |     | ✅    |                        |
| `validation_length_max`                  | Maximum Text Length             | `integer`   |     | ✅    |                        |
| `validation_length_min`                  | Minimum Text Length             | `integer`   |     | ✅    |                        |
| `validation_max_date`                    | Maximum Date                    | `date`      |     | ✅    |                        |
| `validation_max_datetime`                | Maximum Datetime                | `datetime`  |     | ✅    |                        |
| `validation_max_float_value`             | Maximum value                   | `float`     |     | ✅    |                        |
| `validation_min_date`                    | Minimum Date                    | `date`      |     | ✅    |                        |
| `validation_min_datetime`                | Minimum Datetime                | `datetime`  |     | ✅    |                        |
| `validation_min_float_value`             | Minimum value                   | `float`     |     | ✅    |                        |
| `validation_required`                    | Validate entry                  | `boolean`   |     | ✅    |                        |
| `write_date`                             | Last Updated on                 | `datetime`  |     | ✅    |                        |
| `write_uid`                              | Last Updated by                 | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                           | Group                   | Perms     |
| ------------------------------ | ----------------------- | --------- |
| survey.question.survey.user    | Surveys / User          | `R/W/C/D` |
| survey.question.survey.manager | Surveys / Administrator | `R/W/C/D` |
| survey.question.user           | Role / User             | `-`       |
| survey.question.all            | Everyone                | `-`       |

**Record Rules:**

- **Survey question: manager: all** (29) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Survey question: officer: unrestricted survey or in restricted users** (28)
  `R/W/C/D`
  - Domain:
    `[             '|', ('survey_id.restrict_user_ids', 'in', user.id), ('survey_id.restrict_user_ids', '=', False)]`
