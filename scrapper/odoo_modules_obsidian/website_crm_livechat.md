---
title: "Lead Livechat Sessions"
module: "website_crm_livechat"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Website"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/w______]
---

# 🟢 Lead Livechat Sessions

> **Module:** `website_crm_livechat` | **Version:** `19.0.1.0` **Category:** Website |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[website_crm]] [[website_livechat]]

## 📖 Description

Adds a stat button on lead form view to access their livechat sessions.

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT crm.lead.view.form.inherit.website.crm.livechat (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

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

### 🗃️ `chatbot.script.step` — Chatbot Script Step

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                       | Label                     | Type        | Req | Store | Relation              |
| --------------------------- | ------------------------- | ----------- | --- | ----- | --------------------- |
| `answer_ids`                | Answers                   | `one2many`  |     | ✅    | chatbot.script.answer |
| `chatbot_script_id`         | Chatbot                   | `many2one`  | ✅  | ✅    | chatbot.script        |
| `create_date`               | Created on                | `datetime`  |     | ✅    |                       |
| `create_uid`                | Created by                | `many2one`  |     | ✅    | res.users             |
| `crm_team_id`               | Sales Team                | `many2one`  |     | ✅    | crm.team              |
| `display_name`              | Display Name              | `char`      |     |       |                       |
| `id`                        | ID                        | `integer`   |     | ✅    |                       |
| `is_forward_operator`       | Is Forward Operator       | `boolean`   |     |       |                       |
| `is_forward_operator_child` | Is Forward Operator Child | `boolean`   |     |       |                       |
| `message`                   | Message                   | `html`      |     | ✅    |                       |
| `name`                      | Name                      | `char`      |     |       |                       |
| `operator_expertise_ids`    | Operator Expertise        | `many2many` |     | ✅    | im_livechat.expertise |
| `sequence`                  | Sequence                  | `integer`   |     | ✅    |                       |
| `step_type`                 | Step Type                 | `selection` | ✅  | ✅    |                       |
| `triggering_answer_ids`     | Only If                   | `many2many` |     | ✅    | chatbot.script.answer |
| `write_date`                | Last Updated on           | `datetime`  |     | ✅    |                       |
| `write_uid`                 | Last Updated by           | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                     | Group                     | Perms     |
| ------------------------ | ------------------------- | --------- |
| chatbot.script.step.user | Live Chat / Administrator | `R/W/C/D` |
