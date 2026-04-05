---
title: "Automated Marketing"
module: "automated_marketing"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Marketing"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________, odoo/app]
---

# 🟢 Automated Marketing

> **Module:** `automated_marketing` | **Version:** `19.0.1.0` **Category:** Marketing |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[mass_mailing]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `Automated Marketing`
- `Automated Marketing/Campaigns`
- `Automated Marketing/Reporting`
- `Automated Marketing/Reporting/Link Tracker`
- `Automated Marketing/Reporting/Participants`
- `Automated Marketing/Reporting/Traces`

### Views

- `* INHERIT Server Action (form)`
- `* INHERIT mailing.mailing.view.form.promotion.hive (form)`
- `* INHERIT mailing.mailing.view.tree.promotion.hive (list)`
- `* INHERIT mailing.trace.view.form.inherit.promotion.hive (form)`
- `mailing.mailing.view.form.marketing.activity (form)`
- `marketing.activity.view.form (form)`
- `marketing.campaign.test.view.form (form)`
- `marketing.campaign.view.form (form)`
- `marketing.campaign.view.kanban (kanban)`
- `marketing.campaign.view.tree (list)`
- `marketing.participant.view.form (form)`
- `marketing.participant.view.graph (graph)`
- `marketing.participant.view.pivot (pivot)`
- `marketing.participant.view.tree (list)`
- `marketing.trace.view.form (form)`
- `marketing.trace.view.graph (graph)`
- `marketing.trace.view.pivot (pivot)`
- `marketing.trace.view.search (search)`
- `marketing.trace.view.tree (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**8 model(s) defined by this module:**

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

### 🗃️ `mail.compose.message` — Email composition wizard

> ✳️ Transient (Wizard)

Generic message composition wizard. You may inherit from this wizard at model and view
levels to provide specific features.

        The behavior of the wizard depends on the composition_mode field:
        - 'comment': post on a record.
        - 'mass_mail': wizard in mass mailing mode where the mail details can
            contain template placeholders that will be merged with actual data
            before being sent to each recipient.

**Fields:**

| Field                         | Label                                            | Type        | Req | Store | Relation             |
| ----------------------------- | ------------------------------------------------ | ----------- | --- | ----- | -------------------- |
| `attachment_ids`              | Attachments                                      | `many2many` |     | ✅    | ir.attachment        |
| `author_id`                   | Author                                           | `many2one`  |     | ✅    | res.partner          |
| `auto_delete`                 | Delete Emails                                    | `boolean`   |     | ✅    |                      |
| `auto_delete_keep_log`        | Keep Message Copy                                | `boolean`   |     | ✅    |                      |
| `body`                        | Contents                                         | `html`      |     | ✅    |                      |
| `body_has_template_value`     | Body content is the same as the template         | `boolean`   |     |       |                      |
| `campaign_id`                 | Mass Mailing Campaign                            | `many2one`  |     | ✅    | utm.campaign         |
| `can_edit_body`               | Can Edit Body                                    | `boolean`   |     |       |                      |
| `composition_batch`           | Batch composition                                | `boolean`   |     |       |                      |
| `composition_comment_option`  | Comment Options                                  | `selection` |     | ✅    |                      |
| `composition_mode`            | Composition mode                                 | `selection` |     | ✅    |                      |
| `create_date`                 | Created on                                       | `datetime`  |     | ✅    |                      |
| `create_uid`                  | Created by                                       | `many2one`  |     | ✅    | res.users            |
| `display_name`                | Display Name                                     | `char`      |     |       |                      |
| `email_add_signature`         | Add signature                                    | `boolean`   |     | ✅    |                      |
| `email_from`                  | From                                             | `char`      |     | ✅    |                      |
| `email_layout_xmlid`          | Email Notification Layout                        | `char`      |     | ✅    |                      |
| `force_send`                  | Send mailing or notifications directly           | `boolean`   |     | ✅    |                      |
| `id`                          | ID                                               | `integer`   |     | ✅    |                      |
| `is_mail_template_editor`     | Is Editor                                        | `boolean`   |     |       |                      |
| `lang`                        | Language                                         | `char`      |     | ✅    |                      |
| `mail_activity_type_id`       | Mail Activity Type                               | `many2one`  |     | ✅    | mail.activity.type   |
| `mailing_list_ids`            | Mailing List                                     | `many2many` |     | ✅    | mailing.list         |
| `mail_server_id`              | Outgoing mail server                             | `many2one`  |     | ✅    | ir.mail_server       |
| `marketing_activity_id`       | Marketing Activity                               | `many2one`  |     | ✅    | marketing.activity   |
| `mass_mailing_id`             | Mass Mailing                                     | `many2one`  |     | ✅    | mailing.mailing      |
| `mass_mailing_name`           | Mass Mailing Name                                | `char`      |     | ✅    |                      |
| `message_type`                | Type                                             | `selection` | ✅  | ✅    |                      |
| `model`                       | Related Document Model                           | `char`      |     | ✅    |                      |
| `model_is_thread`             | Thread-Enabled                                   | `boolean`   |     |       |                      |
| `notified_bcc_contains_share` | Is an external partner follower of the document? | `boolean`   |     |       |                      |
| `notify_author`               | Notify Author                                    | `boolean`   |     | ✅    |                      |
| `notify_author_mention`       | Notify Author Mention                            | `boolean`   |     | ✅    |                      |
| `notify_skip_followers`       | Notify Skip Followers                            | `boolean`   |     | ✅    |                      |
| `parent_id`                   | Parent Message                                   | `many2one`  |     | ✅    | mail.message         |
| `partner_ids`                 | Additional Contacts                              | `many2many` |     | ✅    | res.partner          |
| `partner_ids_all_have_email`  | Partner Ids All Have Email                       | `boolean`   |     |       |                      |
| `record_alias_domain_id`      | Alias Domain                                     | `many2one`  |     | ✅    | mail.alias.domain    |
| `record_company_id`           | Company                                          | `many2one`  |     | ✅    | res.company          |
| `render_model`                | Rendering Model                                  | `char`      |     |       |                      |
| `reply_to`                    | Reply To                                         | `char`      |     | ✅    |                      |
| `reply_to_force_new`          | Considers answers as new thread                  | `boolean`   |     | ✅    |                      |
| `reply_to_mode`               | Replies                                          | `selection` |     |       |                      |
| `res_domain`                  | Active domain                                    | `text`      |     | ✅    |                      |
| `res_domain_user_id`          | Responsible                                      | `many2one`  |     | ✅    | res.users            |
| `res_ids`                     | Related Document IDs                             | `text`      |     | ✅    |                      |
| `scheduled_date`              | Scheduled Date                                   | `char`      |     | ✅    |                      |
| `subject`                     | Subject                                          | `char`      |     | ✅    |                      |
| `subtype_id`                  | Subtype                                          | `many2one`  |     | ✅    | mail.message.subtype |
| `subtype_is_log`              | Is a log                                         | `boolean`   |     |       |                      |
| `template_id`                 | Use template                                     | `many2one`  |     | ✅    | mail.template        |
| `template_name`               | Template Name                                    | `char`      |     | ✅    |                      |
| `use_exclusion_list`          | Use Exclusion List                               | `boolean`   |     | ✅    |                      |
| `write_date`                  | Last Updated on                                  | `datetime`  |     | ✅    |                      |
| `write_uid`                   | Last Updated by                                  | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                        | Group       | Perms   |
| --------------------------- | ----------- | ------- |
| access.mail.compose.message | Role / User | `R/W/C` |

**Record Rules:**

- **Mail Compose Message Rule** (Global) `R/W`
  - Domain: `[('create_uid', '=', user.id)]`

### 🗃️ `mailing.trace` — Mailing Statistics

MailingTrace models the statistics collected about emails. Those statistics are stored
in a separated model and table to avoid bloating the mail_mail table with statistics
values. This also allows to delete emails send with mass mailing without loosing the
statistics about them.

    Note:: State management / Error codes / Failure types summary

      * trace_status
        'outgoing', 'process', 'pending', 'sent', 'opened', 'replied',
        'error', 'bounce', 'cancel'
      * failure_type
        # generic
        'unknown',
        # mass_mailing
        "mail_email_invalid", "mail_smtp", "mail_email_missing",
        "mail_from_invalid", "mail_from_missing",
        # mass mailing mass mode specific codes
        "mail_bl", "mail_optout", "mail_dup"
        # mass_mailing_sms
        'sms_number_missing', 'sms_number_format', 'sms_credit', 'sms_server',
        'sms_acc', 'sms_country_not_supported', 'sms_registration_needed',
        # mass_mailing_sms mass mode specific codes
        'sms_blacklist', 'sms_duplicate', 'sms_optout',
      * cancel:
        * mail: set in _prepare_mail_values in composer, if email is blacklisted
          (mail) or in opt_out / seen list (mass_mailing) or email_to is void
          or incorrectly formatted (mass_mailing) - based on mail cancel state
        * sms: set in _prepare_mass_sms_trace_values in composer if sms is
          in cancel state; either blacklisted (sms) or in opt_out / seen list
          (sms);
        * void mail / void sms number -> error (mail_missing, sms_number_missing)
        * invalid mail / invalid sms number -> error (RECIPIENT, sms_number_format)
      * exception: set in  _postprocess_sent_message (_postprocess_iap_sent_sms)
        if mail (sms) not sent with failure type, reset if sent;
      * process: (used in sms): set in SmsTracker._update_sms_traces when held back
        (at IAP) before actual sending to the sms_service.
      * pending: (used in sms): default value for sent sms.
      * sent: set in
        * _postprocess_sent_message if mail
        * SmsTracker._update_sms_traces if sms, when delivery report is received.
      * clicked: triggered by add_click
      * opened: triggered by add_click + blank gif (mail) + gateway reply (mail)
      * replied: triggered by gateway reply (mail)
      * bounced: triggered by gateway bounce (mail) or in _prepare_mass_sms_trace_values
        if sms_number_format error when sending sms (sms)

**Fields:**

| Field                  | Label                 | Type                 | Req | Store | Relation           |
| ---------------------- | --------------------- | -------------------- | --- | ----- | ------------------ |
| `campaign_id`          | Campaign              | `many2one`           |     | ✅    | utm.campaign       |
| `create_date`          | Created on            | `datetime`           |     | ✅    |                    |
| `create_uid`           | Created by            | `many2one`           |     | ✅    | res.users          |
| `display_name`         | Display Name          | `char`               |     |       |                    |
| `email`                | Email                 | `char`               |     | ✅    |                    |
| `failure_reason`       | Failure reason        | `text`               |     | ✅    |                    |
| `failure_type`         | Failure type          | `selection`          |     | ✅    |                    |
| `id`                   | ID                    | `integer`            |     | ✅    |                    |
| `is_test_trace`        | Generated for testing | `boolean`            |     | ✅    |                    |
| `links_click_datetime` | Clicked On            | `datetime`           |     | ✅    |                    |
| `links_click_ids`      | Links click           | `one2many`           |     | ✅    | link.tracker.click |
| `mail_mail_id`         | Mail                  | `many2one`           |     | ✅    | mail.mail          |
| `mail_mail_id_int`     | Mail ID (tech)        | `integer`            |     | ✅    |                    |
| `marketing_trace_id`   | Marketing Trace       | `many2one`           |     | ✅    | marketing.trace    |
| `mass_mailing_id`      | Mailing               | `many2one`           |     | ✅    | mailing.mailing    |
| `medium_id`            | Medium                | `many2one`           |     |       | utm.medium         |
| `message_id`           | Message-ID            | `char`               |     | ✅    |                    |
| `model`                | Document model        | `char`               | ✅  | ✅    |                    |
| `open_datetime`        | Opened On             | `datetime`           |     | ✅    |                    |
| `reply_datetime`       | Replied On            | `datetime`           |     | ✅    |                    |
| `res_id`               | Document ID           | `many2one_reference` |     | ✅    |                    |
| `sent_datetime`        | Sent On               | `datetime`           |     | ✅    |                    |
| `source_id`            | Source                | `many2one`           |     |       | utm.source         |
| `trace_status`         | Status                | `selection`          |     | ✅    |                    |
| `trace_type`           | Type                  | `selection`          | ✅  | ✅    |                    |
| `write_date`           | Last Updated on       | `datetime`           |     | ✅    |                    |
| `write_uid`            | Last Updated by       | `many2one`           |     | ✅    | res.users          |

**Access Rights:**

| Name                         | Group                  | Perms     |
| ---------------------------- | ---------------------- | --------- |
| access.mailing.trace.mm.user | Email Marketing / User | `R/W/C/D` |

### 🗃️ `marketing.activity` — Marketing Activity

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label                  | Type        | Req | Store | Relation           |
| -------------------------- | ---------------------- | ----------- | --- | ----- | ------------------ |
| `activity_domain`          | Activity Filter        | `char`      |     | ✅    |                    |
| `activity_type`            | Activity Type          | `selection` | ✅  | ✅    |                    |
| `allowed_parent_ids`       | Allowed parents        | `many2many` |     |       | marketing.activity |
| `campaign_id`              | Campaign               | `many2one`  | ✅  | ✅    | marketing.campaign |
| `child_ids`                | Child Activities       | `one2many`  |     | ✅    | marketing.activity |
| `childreen_graph_data`     | Childreen Graph Data   | `char`      |     | ✅    |                    |
| `create_date`              | Created on             | `datetime`  |     | ✅    |                    |
| `create_uid`               | Created by             | `many2one`  |     | ✅    | res.users          |
| `display_name`             | Display Name           | `char`      |     |       |                    |
| `domain`                   | Applied Filter         | `char`      |     | ✅    |                    |
| `id`                       | ID                     | `integer`   |     | ✅    |                    |
| `interval_number`          | Send after             | `integer`   |     | ✅    |                    |
| `interval_standardized`    | Send after (in hours)  | `integer`   |     | ✅    |                    |
| `interval_type`            | Delay Type             | `selection` | ✅  | ✅    |                    |
| `mailing_type`             | Mailing Type           | `selection` |     | ✅    |                    |
| `mass_mailing_id`          | Marketing Template     | `many2one`  |     | ✅    | mailing.mailing    |
| `model_id`                 | Model                  | `many2one`  |     |       | ir.model           |
| `model_name`               | Model Name             | `char`      |     |       |                    |
| `name`                     | Source Name            | `char`      | ✅  |       |                    |
| `parent_id`                | Activity               | `many2one`  |     | ✅    | marketing.activity |
| `processed`                | Processed              | `integer`   |     |       |                    |
| `rejected`                 | Rejected               | `integer`   |     |       |                    |
| `require_sync`             | Require trace sync     | `boolean`   |     | ✅    |                    |
| `server_action_id`         | Server Action          | `many2one`  |     | ✅    | ir.actions.server  |
| `statistics_graph_data`    | Statistics Graph Data  | `char`      |     |       |                    |
| `total_bounce`             | Total Bounce           | `integer`   |     |       |                    |
| `total_click`              | Total Click            | `integer`   |     |       |                    |
| `total_open`               | Total Open             | `integer`   |     |       |                    |
| `total_reply`              | Total Reply            | `integer`   |     |       |                    |
| `total_sent`               | Total Sent             | `integer`   |     |       |                    |
| `trace_ids`                | Traces                 | `one2many`  |     | ✅    | marketing.trace    |
| `trigger_category`         | Trigger Category       | `selection` |     | ✅    |                    |
| `trigger_type`             | Trigger Type           | `selection` | ✅  | ✅    |                    |
| `utm_campaign_id`          | UTM Campaign           | `many2one`  |     |       | utm.campaign       |
| `utm_source_id`            | Source                 | `many2one`  | ✅  | ✅    | utm.source         |
| `validity_duration`        | Validity Duration      | `boolean`   |     | ✅    |                    |
| `validity_duration_number` | Valid during           | `integer`   |     | ✅    |                    |
| `validity_duration_type`   | Validity Duration Type | `selection` | ✅  | ✅    |                    |
| `write_date`               | Last Updated on        | `datetime`  |     | ✅    |                    |
| `write_uid`                | Last Updated by        | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                      | Group                                           | Perms     |
| ------------------------- | ----------------------------------------------- | --------- |
| access_marketing_activity | Automated Marketing / Automated Marketing Users | `R/W/C/D` |

### 🗃️ `marketing.campaign` — Marketing Campaign

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                                      | Type        | Req | Store | Relation              |
| ------------------------------- | ------------------------------------------ | ----------- | --- | ----- | --------------------- |
| `ab_testing_completed`          | A/B Testing Campaign Finished              | `boolean`   |     |       |                       |
| `ab_testing_mailings_count`     | A/B Test Mailings #                        | `integer`   |     |       |                       |
| `ab_testing_schedule_datetime`  | Send Final On                              | `datetime`  |     |       |                       |
| `ab_testing_winner_mailing_id`  | A/B Campaign Winner Mailing                | `many2one`  |     |       | mailing.mailing       |
| `ab_testing_winner_selection`   | Winner Selection                           | `selection` |     |       |                       |
| `active`                        | Active                                     | `boolean`   |     | ✅    |                       |
| `activity_type`                 | Activity Type                              | `selection` | ✅  | ✅    |                       |
| `bounced_ratio`                 | Bounced Ratio                              | `float`     |     |       |                       |
| `click_count`                   | Number of clicks generated by the campaign | `integer`   |     |       |                       |
| `color`                         | Color Index                                | `integer`   |     |       |                       |
| `company_id`                    | Company                                    | `many2one`  |     |       | res.company           |
| `completed_participant_count`   | # of completed participants                | `integer`   |     |       |                       |
| `create_date`                   | Created on                                 | `datetime`  |     | ✅    |                       |
| `create_uid`                    | Created by                                 | `many2one`  |     | ✅    | res.users             |
| `crm_lead_count`                | Leads/Opportunities count                  | `integer`   |     |       |                       |
| `currency_id`                   | Currency                                   | `many2one`  |     |       | res.currency          |
| `display_name`                  | Display Name                               | `char`      |     |       |                       |
| `domain`                        | Filter                                     | `char`      |     | ✅    |                       |
| `id`                            | ID                                         | `integer`   |     | ✅    |                       |
| `invoiced_amount`               | Revenues generated by the campaign         | `integer`   |     |       |                       |
| `is_auto_campaign`              | Automatically Generated Campaign           | `boolean`   |     |       |                       |
| `is_mailing_campaign_activated` | Is Mailing Campaign Activated              | `boolean`   |     |       |                       |
| `last_sync_date`                | Last activities synchronization            | `datetime`  |     | ✅    |                       |
| `link_tracker_click_count`      | # Clicks                                   | `integer`   |     |       |                       |
| `mailing_mail_count`            | Number of Mass Mailing                     | `integer`   |     |       |                       |
| `mailing_mail_ids`              | Mass Mailings                              | `one2many`  |     |       | mailing.mailing       |
| `marketing_activity_ids`        | Activities                                 | `one2many`  |     | ✅    | marketing.activity    |
| `mass_mailing_count`            | # Mailings                                 | `integer`   |     |       |                       |
| `model_id`                      | Model                                      | `many2one`  | ✅  | ✅    | ir.model              |
| `model_name`                    | Model Name                                 | `char`      |     | ✅    |                       |
| `name`                          | Campaign Identifier                        | `char`      | ✅  |       |                       |
| `opened_ratio`                  | Opened Ratio                               | `float`     |     |       |                       |
| `participant_ids`               | Participants                               | `one2many`  |     | ✅    | marketing.participant |
| `quotation_count`               | Quotation Count                            | `integer`   |     |       |                       |
| `received_ratio`                | Received Ratio                             | `float`     |     |       |                       |
| `replied_ratio`                 | Replied Ratio                              | `float`     |     |       |                       |
| `require_sync`                  | Sync of participants is required           | `boolean`   |     |       |                       |
| `running_participant_count`     | # of active participants                   | `integer`   |     |       |                       |
| `stage_id`                      | Stage                                      | `many2one`  | ✅  |       | utm.stage             |
| `state`                         | State                                      | `selection` |     | ✅    |                       |
| `tag_ids`                       | Tags                                       | `many2many` |     |       | utm.tag               |
| `test_participant_count`        | # of test participants                     | `integer`   |     |       |                       |
| `title`                         | Campaign Name                              | `char`      | ✅  |       |                       |
| `total_participant_count`       | # of active and completed participants     | `integer`   |     |       |                       |
| `unique_field_id`               | Unique Field                               | `many2one`  |     | ✅    | ir.model.fields       |
| `use_leads`                     | Use Leads                                  | `boolean`   |     |       |                       |
| `user_id`                       | Responsible                                | `many2one`  | ✅  |       | res.users             |
| `utm_campaign_id`               | UTM Campaign                               | `many2one`  | ✅  | ✅    | utm.campaign          |
| `write_date`                    | Last Updated on                            | `datetime`  |     | ✅    |                       |
| `write_uid`                     | Last Updated by                            | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                      | Group                                           | Perms     |
| ------------------------- | ----------------------------------------------- | --------- |
| access_marketing_campaign | Automated Marketing / Automated Marketing Users | `R/W/C/D` |

### 🗃️ `marketing.campaign.test` — Marketing Campaign Test

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation           |
| -------------- | --------------- | ----------- | --- | ----- | ------------------ |
| `campaign_id`  | Campaign        | `many2one`  | ✅  | ✅    | marketing.campaign |
| `create_date`  | Created on      | `datetime`  |     | ✅    |                    |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users          |
| `display_name` | Display Name    | `char`      |     |       |                    |
| `id`           | ID              | `integer`   |     | ✅    |                    |
| `model_id`     | Model           | `many2one`  |     |       | ir.model           |
| `model_name`   | Record model    | `char`      |     |       |                    |
| `res_id`       | Record ID       | `integer`   |     | ✅    |                    |
| `resource_ref` | Record          | `reference` |     |       |                    |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |                    |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                           | Group                                           | Perms   |
| ------------------------------ | ----------------------------------------------- | ------- |
| access_marketing_campaign_test | Automated Marketing / Automated Marketing Users | `R/W/C` |

### 🗃️ `marketing.participant` — Marketing Participant

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation           |
| -------------- | --------------- | ----------- | --- | ----- | ------------------ |
| `campaign_id`  | Campaign        | `many2one`  | ✅  | ✅    | marketing.campaign |
| `create_date`  | Created on      | `datetime`  |     | ✅    |                    |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users          |
| `display_name` | Display Name    | `char`      |     |       |                    |
| `id`           | ID              | `integer`   |     | ✅    |                    |
| `is_test`      | Test Record     | `boolean`   |     | ✅    |                    |
| `model_id`     | Model           | `many2one`  |     | ✅    | ir.model           |
| `model_name`   | Record model    | `char`      |     | ✅    |                    |
| `res_id`       | Record ID       | `integer`   |     | ✅    |                    |
| `resource_ref` | Record          | `reference` |     |       |                    |
| `state`        | State           | `selection` | ✅  | ✅    |                    |
| `trace_ids`    | Actions         | `one2many`  |     | ✅    | marketing.trace    |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |                    |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                         | Group                                           | Perms     |
| ---------------------------- | ----------------------------------------------- | --------- |
| access_marketing_participant | Automated Marketing / Automated Marketing Users | `R/W/C/D` |

### 🗃️ `marketing.trace` — Marketing Trace

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label                   | Type        | Req | Store | Relation              |
| ------------------- | ----------------------- | ----------- | --- | ----- | --------------------- |
| `activity_id`       | Activity                | `many2one`  | ✅  | ✅    | marketing.activity    |
| `activity_type`     | Activity Type           | `selection` |     |       |                       |
| `child_ids`         | Direct child traces     | `one2many`  |     | ✅    | marketing.trace       |
| `clicked`           | Clicked On              | `datetime`  |     |       |                       |
| `create_date`       | Created on              | `datetime`  |     | ✅    |                       |
| `create_uid`        | Created by              | `many2one`  |     | ✅    | res.users             |
| `display_name`      | Display Name            | `char`      |     |       |                       |
| `id`                | ID                      | `integer`   |     | ✅    |                       |
| `is_test`           | Test Trace              | `boolean`   |     | ✅    |                       |
| `mailing_trace_ids` | Mass mailing statistics | `one2many`  |     | ✅    | mailing.trace         |
| `opened`            | Opened On               | `datetime`  |     |       |                       |
| `parent_id`         | Parent                  | `many2one`  |     | ✅    | marketing.trace       |
| `participant_id`    | Participant             | `many2one`  | ✅  | ✅    | marketing.participant |
| `replied`           | Replied On              | `datetime`  |     |       |                       |
| `res_id`            | Document ID             | `integer`   |     | ✅    |                       |
| `schedule_date`     | Schedule Date           | `datetime`  |     | ✅    |                       |
| `sent`              | Sent On                 | `datetime`  |     |       |                       |
| `state`             | State                   | `selection` | ✅  | ✅    |                       |
| `state_msg`         | Error message           | `char`      |     | ✅    |                       |
| `trigger_type`      | Trigger Type            | `selection` |     |       |                       |
| `write_date`        | Last Updated on         | `datetime`  |     | ✅    |                       |
| `write_uid`         | Last Updated by         | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                   | Group                                           | Perms     |
| ---------------------- | ----------------------------------------------- | --------- |
| access_marketing_trace | Automated Marketing / Automated Marketing Users | `R/W/C/D` |
