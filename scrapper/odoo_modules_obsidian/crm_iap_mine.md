---
title: "Lead Generation"
module: "crm_iap_mine"
state: "installed"
version: "19.0.1.2"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "CRM"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/___]
---

# 🟢 Lead Generation

> **Module:** `crm_iap_mine` | **Version:** `19.0.1.2` **Category:** CRM | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[iap_crm]] [[iap_mail]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `CRM/Configuration/Lead Generation`
- `CRM/Configuration/Lead Generation/Lead Mining Requests`

### Views

- `* INHERIT crm.lead.kanban.inherit.iap.mine (kanban)`
- `* INHERIT crm.lead.kanban.lead.inherit.iap.mine (kanban)`
- `* INHERIT crm.lead.view.list.lead.inherit.iap.mine (list)`
- `* INHERIT crm.lead.view.list.opportunity.inherit.iap.mine (list)`
- `* INHERIT enrich_company (qweb)`
- `* INHERIT res.config.settings.view.form.inherit.crm.iap.lead (form)`
- `crm.iap.lead.mining.request.view.form (form)`
- `crm.iap.lead.mining.request.view.list (list)`
- `crm.iap.lead.mining.request.view.search (search)`

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

### 🗃️ `crm.iap.lead.industry` — CRM IAP Lead Industry

Industry Tags of Acquisition Rules

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `color`        | Color Index     | `integer`  |     | ✅    |           |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Industry        | `char`     | ✅  | ✅    |           |
| `reveal_ids`   | Reveal          | `char`     | ✅  | ✅    |           |
| `sequence`     | Sequence        | `integer`  |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                         | Group                 | Perms     |
| ---------------------------- | --------------------- | --------- |
| access_crm_iap_lead_industry | Sales / Administrator | `R/W/C/D` |

### 🗃️ `crm.iap.lead.mining.request` — CRM Lead Mining Request

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                   | Label                        | Type        | Req | Store | Relation               |
| ----------------------- | ---------------------------- | ----------- | --- | ----- | ---------------------- |
| `available_state_ids`   | Available State              | `one2many`  |     |       | res.country.state      |
| `company_size_max`      | Company Size Max             | `integer`   |     | ✅    |                        |
| `company_size_min`      | Size                         | `integer`   |     | ✅    |                        |
| `contact_filter_type`   | Filter on                    | `selection` |     | ✅    |                        |
| `contact_number`        | Number of Contacts           | `integer`   |     | ✅    |                        |
| `country_ids`           | Countries                    | `many2many` |     | ✅    | res.country            |
| `create_date`           | Created on                   | `datetime`  |     | ✅    |                        |
| `create_uid`            | Created by                   | `many2one`  |     | ✅    | res.users              |
| `display_name`          | Display Name                 | `char`      |     |       |                        |
| `error_type`            | Error Type                   | `selection` |     | ✅    |                        |
| `filter_on_size`        | Filter on Size               | `boolean`   |     | ✅    |                        |
| `id`                    | ID                           | `integer`   |     | ✅    |                        |
| `industry_ids`          | Industries                   | `many2many` |     | ✅    | crm.iap.lead.industry  |
| `lead_contacts_credits` | Lead Contacts Credits        | `char`      |     |       |                        |
| `lead_count`            | Number of Generated Leads    | `integer`   |     |       |                        |
| `lead_credits`          | Lead Credits                 | `char`      |     |       |                        |
| `lead_ids`              | Generated Lead / Opportunity | `one2many`  |     | ✅    | crm.lead               |
| `lead_number`           | Number of Leads              | `integer`   | ✅  | ✅    |                        |
| `lead_total_credits`    | Lead Total Credits           | `char`      |     |       |                        |
| `lead_type`             | Type                         | `selection` | ✅  | ✅    |                        |
| `name`                  | Request Number               | `char`      | ✅  | ✅    |                        |
| `preferred_role_id`     | Preferred Role               | `many2one`  |     | ✅    | crm.iap.lead.role      |
| `role_ids`              | Other Roles                  | `many2many` |     | ✅    | crm.iap.lead.role      |
| `search_type`           | Target                       | `selection` | ✅  | ✅    |                        |
| `seniority_id`          | Seniority                    | `many2one`  |     | ✅    | crm.iap.lead.seniority |
| `state`                 | Status                       | `selection` | ✅  | ✅    |                        |
| `state_ids`             | States                       | `many2many` |     | ✅    | res.country.state      |
| `tag_ids`               | Tags                         | `many2many` |     | ✅    | crm.tag                |
| `team_id`               | Sales Team                   | `many2one`  |     | ✅    | crm.team               |
| `user_id`               | Salesperson                  | `many2one`  |     | ✅    | res.users              |
| `write_date`            | Last Updated on              | `datetime`  |     | ✅    |                        |
| `write_uid`             | Last Updated by              | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                               | Group                 | Perms     |
| ---------------------------------- | --------------------- | --------- |
| access_crm_iap_lead_mining_request | Sales / Administrator | `R/W/C/D` |

### 🗃️ `crm.iap.lead.helpers` — Helper methods for crm_iap_mine modules

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
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                        | Group    | Perms |
| --------------------------- | -------- | ----- |
| access_crm_iap_lead_helpers | Everyone | `-`   |

### 🗃️ `crm.iap.lead.role` — People Role

CRM Reveal People Roles for People

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `color`        | Color Index     | `integer`  |     | ✅    |           |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Role Name       | `char`     | ✅  | ✅    |           |
| `reveal_id`    | Reveal          | `char`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                     | Group                 | Perms     |
| ------------------------ | --------------------- | --------- |
| access_crm_iap_lead_role | Sales / Administrator | `R/W/C/D` |

### 🗃️ `crm.iap.lead.seniority` — People Seniority

Seniority for People Rules

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Name            | `char`     | ✅  | ✅    |           |
| `reveal_id`    | Reveal          | `char`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                          | Group                 | Perms     |
| ----------------------------- | --------------------- | --------- |
| access_crm_iap_lead_seniority | Sales / Administrator | `R/W/C/D` |
