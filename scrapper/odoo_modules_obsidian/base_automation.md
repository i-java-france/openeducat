---
title: "Automation Rules"
module: "base_automation"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Sales"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_____]
---

# 🟢 Automation Rules

> **Module:** `base_automation` | **Version:** `19.0.1.0` **Category:** Sales |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[base]] [[digest]] [[resource]] [[mail]] [[sms]]

## 📖 Description

# This module allows to implement automation rules for any object.

Use automation rules to automatically trigger actions for various screens.

**Example:** A lead created by a specific user may be automatically set to a specific
Sales Team, or an opportunity which still has status pending after 14 days might trigger
an automatic reminder email.

## 🖥️ UI Components

### Menus

- `Settings/Technical/Automation/Automation Rules`

### Views

- `* INHERIT Server Actions (form)`
- `Automations (form)`
- `base.automation.kanban (kanban)`
- `base.automation.list (list)`
- `base.automation.search (search)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

### 🗃️ `base.automation` — Automation Rule

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type                 | Req | Store | Relation                  |
| ------------------------------- | ----------------------------- | -------------------- | --- | ----- | ------------------------- |
| `action_server_ids`             | Actions                       | `one2many`           |     | ✅    | ir.actions.server         |
| `active`                        | Active                        | `boolean`            |     | ✅    |                           |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`           |     |       | calendar.event            |
| `activity_date_deadline`        | Next Activity Deadline        | `date`               |     |       |                           |
| `activity_exception_decoration` | Activity Exception Decoration | `selection`          |     |       |                           |
| `activity_exception_icon`       | Icon                          | `char`               |     |       |                           |
| `activity_ids`                  | Activities                    | `one2many`           |     | ✅    | mail.activity             |
| `activity_state`                | Activity State                | `selection`          |     |       |                           |
| `activity_summary`              | Next Activity Summary         | `char`               |     |       |                           |
| `activity_type_icon`            | Activity Type Icon            | `char`               |     |       |                           |
| `activity_type_id`              | Next Activity Type            | `many2one`           |     |       | mail.activity.type        |
| `activity_user_id`              | Responsible User              | `many2one`           |     |       | res.users                 |
| `create_date`                   | Created on                    | `datetime`           |     | ✅    |                           |
| `create_uid`                    | Created by                    | `many2one`           |     | ✅    | res.users                 |
| `description`                   | Description                   | `html`               |     | ✅    |                           |
| `display_name`                  | Display Name                  | `char`               |     |       |                           |
| `filter_domain`                 | Apply on                      | `char`               |     | ✅    |                           |
| `filter_pre_domain`             | Before Update Domain          | `char`               |     | ✅    |                           |
| `has_message`                   | Has Message                   | `boolean`            |     |       |                           |
| `id`                            | ID                            | `integer`            |     | ✅    |                           |
| `last_run`                      | Last Run                      | `datetime`           |     | ✅    |                           |
| `log_webhook_calls`             | Log Calls                     | `boolean`            |     | ✅    |                           |
| `message_attachment_count`      | Attachment Count              | `integer`            |     |       |                           |
| `message_follower_ids`          | Followers                     | `one2many`           |     | ✅    | mail.followers            |
| `message_has_error`             | Message Delivery error        | `boolean`            |     |       |                           |
| `message_has_error_counter`     | Number of errors              | `integer`            |     |       |                           |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`            |     |       |                           |
| `message_ids`                   | Messages                      | `one2many`           |     | ✅    | mail.message              |
| `message_is_follower`           | Is Follower                   | `boolean`            |     |       |                           |
| `message_needaction`            | Action Needed                 | `boolean`            |     |       |                           |
| `message_needaction_counter`    | Number of Actions             | `integer`            |     |       |                           |
| `message_partner_ids`           | Followers (Partners)          | `many2many`          |     |       | res.partner               |
| `model_id`                      | Model                         | `many2one`           | ✅  | ✅    | ir.model                  |
| `model_is_mail_thread`          | Has Mail Thread               | `boolean`            |     |       |                           |
| `model_name`                    | Model Name                    | `char`               |     |       |                           |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`               |     |       |                           |
| `name`                          | Automation Rule Name          | `char`               | ✅  | ✅    |                           |
| `on_change_field_ids`           | On Change Fields Trigger      | `many2many`          |     | ✅    | ir.model.fields           |
| `previous_domain`               | Previous Domain               | `char`               |     |       |                           |
| `rating_ids`                    | Ratings                       | `one2many`           |     | ✅    | rating.rating             |
| `record_getter`                 | Record Getter                 | `char`               |     | ✅    |                           |
| `trg_date_calendar_id`          | Use Calendar                  | `many2one`           |     | ✅    | resource.calendar         |
| `trg_date_id`                   | Trigger Date                  | `many2one`           |     | ✅    | ir.model.fields           |
| `trg_date_range`                | Delay                         | `integer`            |     | ✅    |                           |
| `trg_date_range_mode`           | Delay mode                    | `selection`          |     | ✅    |                           |
| `trg_date_range_type`           | Delay unit                    | `selection`          |     | ✅    |                           |
| `trg_field_ref`                 | Trigger Reference             | `many2one_reference` |     | ✅    |                           |
| `trg_field_ref_model_name`      | Trigger Field Model           | `char`               |     |       |                           |
| `trg_selection_field_id`        | Trigger Field                 | `many2one`           |     | ✅    | ir.model.fields.selection |
| `trigger`                       | Trigger                       | `selection`          | ✅  | ✅    |                           |
| `trigger_field_ids`             | Trigger Fields                | `many2many`          |     | ✅    | ir.model.fields           |
| `url`                           | Url                           | `char`               |     |       |                           |
| `webhook_uuid`                  | Webhook UUID                  | `char`               |     | ✅    |                           |
| `website_message_ids`           | Website Messages              | `one2many`           |     | ✅    | mail.message              |
| `write_date`                    | Last Updated on               | `datetime`           |     | ✅    |                           |
| `write_uid`                     | Last Updated by               | `many2one`           |     | ✅    | res.users                 |

**Access Rights:**

| Name                   | Group                | Perms     |
| ---------------------- | -------------------- | --------- |
| base.automation config | Role / Administrator | `R/W/C/D` |

### 🗃️ `ir.cron` — Scheduled Actions

> 📧 Mail Thread

Model describing cron jobs (also called actions or tasks).

**Fields:**

| Field                               | Label                         | Type        | Req | Store | Relation                  |
| ----------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------- |
| `action_class`                      | Action Class                  | `char`      |     |       |                           |
| `active`                            | Active                        | `boolean`   |     | ✅    |                           |
| `activity_calendar_event_id`        | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event            |
| `activity_date_deadline`            | Next Activity Deadline        | `date`      |     |       |                           |
| `activity_date_deadline_range`      | Due Date In                   | `integer`   |     |       |                           |
| `activity_date_deadline_range_type` | Due type                      | `selection` |     |       |                           |
| `activity_exception_decoration`     | Activity Exception Decoration | `selection` |     |       |                           |
| `activity_exception_icon`           | Icon                          | `char`      |     |       |                           |
| `activity_ids`                      | Activities                    | `one2many`  |     | ✅    | mail.activity             |
| `activity_note`                     | Note                          | `html`      |     |       |                           |
| `activity_state`                    | Activity State                | `selection` |     |       |                           |
| `activity_summary`                  | Next Activity Summary         | `char`      |     |       |                           |
| `activity_type_icon`                | Activity Type Icon            | `char`      |     |       |                           |
| `activity_type_id`                  | Next Activity Type            | `many2one`  |     |       | mail.activity.type        |
| `activity_user_field_name`          | User Field                    | `char`      |     |       |                           |
| `activity_user_id`                  | Responsible User              | `many2one`  |     |       | res.users                 |
| `activity_user_type`                | User Type                     | `selection` |     |       |                           |
| `allowed_states`                    | Allowed states                | `json`      |     |       |                           |
| `automated_name`                    | Automated Name                | `char`      |     |       |                           |
| `available_model_ids`               | Available Models              | `many2many` |     |       | ir.model                  |
| `base_automation_id`                | Automation Rule               | `many2one`  |     |       | base.automation           |
| `binding_model_id`                  | Binding Model                 | `many2one`  |     |       | ir.model                  |
| `binding_type`                      | Binding Type                  | `selection` | ✅  |       |                           |
| `binding_view_types`                | Binding View Types            | `char`      |     |       |                           |
| `child_ids`                         | Child Actions                 | `one2many`  |     |       | ir.actions.server         |
| `code`                              | Python Code                   | `text`      |     |       |                           |
| `create_date`                       | Created on                    | `datetime`  |     | ✅    |                           |
| `create_uid`                        | Created by                    | `many2one`  |     | ✅    | res.users                 |
| `cron_name`                         | Name                          | `char`      |     | ✅    |                           |
| `crud_model_id`                     | Record to Create              | `many2one`  |     |       | ir.model                  |
| `crud_model_name`                   | Target Model Name             | `char`      |     |       |                           |
| `display_name`                      | Display Name                  | `char`      |     |       |                           |
| `evaluation_type`                   | Value Type                    | `selection` |     |       |                           |
| `failure_count`                     | Failure Count                 | `integer`   |     | ✅    |                           |
| `first_failure_date`                | First Failure Date            | `datetime`  |     | ✅    |                           |
| `followers_partner_field_name`      | Followers Field               | `char`      |     |       |                           |
| `followers_type`                    | Followers Type                | `selection` |     |       |                           |
| `group_ids`                         | Allowed Groups                | `many2many` |     |       | res.groups                |
| `has_message`                       | Has Message                   | `boolean`   |     |       |                           |
| `help`                              | Action Description            | `html`      |     |       |                           |
| `html_value`                        | Html Value                    | `html`      |     |       |                           |
| `icon`                              | Icon                          | `char`      |     |       |                           |
| `id`                                | ID                            | `integer`   |     | ✅    |                           |
| `interval_number`                   | Interval Number               | `integer`   | ✅  | ✅    |                           |
| `interval_type`                     | Interval Unit                 | `selection` | ✅  | ✅    |                           |
| `ir_actions_server_id`              | Server action                 | `many2one`  | ✅  | ✅    | ir.actions.server         |
| `ir_cron_ids`                       | Scheduled Action              | `one2many`  |     |       | ir.cron                   |
| `lastcall`                          | Last Execution Date           | `datetime`  |     | ✅    |                           |
| `link_field_id`                     | Link Field                    | `many2one`  |     |       | ir.model.fields           |
| `mail_post_autofollow`              | Subscribe Recipients          | `boolean`   |     |       |                           |
| `mail_post_method`                  | Send Email As                 | `selection` |     |       |                           |
| `message_attachment_count`          | Attachment Count              | `integer`   |     |       |                           |
| `message_follower_ids`              | Followers                     | `one2many`  |     | ✅    | mail.followers            |
| `message_has_error`                 | Message Delivery error        | `boolean`   |     |       |                           |
| `message_has_error_counter`         | Number of errors              | `integer`   |     |       |                           |
| `message_has_sms_error`             | SMS Delivery error            | `boolean`   |     |       |                           |
| `message_ids`                       | Messages                      | `one2many`  |     | ✅    | mail.message              |
| `message_is_follower`               | Is Follower                   | `boolean`   |     |       |                           |
| `message_needaction`                | Action Needed                 | `boolean`   |     |       |                           |
| `message_needaction_counter`        | Number of Actions             | `integer`   |     |       |                           |
| `message_partner_ids`               | Followers (Partners)          | `many2many` |     |       | res.partner               |
| `model_id`                          | Model                         | `many2one`  | ✅  |       | ir.model                  |
| `model_name`                        | Model Name                    | `char`      |     |       |                           |
| `my_activity_date_deadline`         | My Activity Deadline          | `date`      |     |       |                           |
| `name`                              | Action Name                   | `char`      | ✅  |       |                           |
| `nextcall`                          | Next Execution Date           | `datetime`  | ✅  | ✅    |                           |
| `parent_id`                         | Parent Action                 | `many2one`  |     |       | ir.actions.server         |
| `partner_ids`                       | Partner                       | `many2many` |     |       | res.partner               |
| `path`                              | Path to show in the URL       | `char`      |     |       |                           |
| `priority`                          | Priority                      | `integer`   |     | ✅    |                           |
| `rating_ids`                        | Ratings                       | `one2many`  |     | ✅    | rating.rating             |
| `resource_ref`                      | Record                        | `reference` |     |       |                           |
| `selection_value`                   | Custom Value                  | `many2one`  |     |       | ir.model.fields.selection |
| `sequence`                          | Sequence                      | `integer`   |     |       |                           |
| `sequence_id`                       | Sequence to use               | `many2one`  |     |       | ir.sequence               |
| `show_code_history`                 | Show Code History             | `boolean`   |     |       |                           |
| `sms_method`                        | Send SMS As                   | `selection` |     |       |                           |
| `sms_template_id`                   | SMS Template                  | `many2one`  |     |       | sms.template              |
| `state`                             | Type                          | `selection` | ✅  |       |                           |
| `template_id`                       | Email Template                | `many2one`  |     |       | mail.template             |
| `type`                              | Action Type                   | `char`      | ✅  |       |                           |
| `update_boolean_value`              | Boolean Value                 | `selection` |     |       |                           |
| `update_field_id`                   | Field to Update               | `many2one`  |     |       | ir.model.fields           |
| `update_field_type`                 | Field Type                    | `selection` |     |       |                           |
| `update_m2m_operation`              | Many2many Operations          | `selection` |     |       |                           |
| `update_path`                       | Field to Update Path          | `char`      |     |       |                           |
| `update_related_model_id`           | Update Related Model          | `many2one`  |     |       | ir.model                  |
| `usage`                             | Usage                         | `selection` | ✅  |       |                           |
| `user_id`                           | Scheduler User                | `many2one`  | ✅  | ✅    | res.users                 |
| `value`                             | Value                         | `text`      |     |       |                           |
| `value_field_to_show`               | Value Field To Show           | `selection` |     |       |                           |
| `warning`                           | Warning                       | `text`      |     |       |                           |
| `webhook_field_ids`                 | Webhook Fields                | `many2many` |     |       | ir.model.fields           |
| `webhook_sample_payload`            | Sample Payload                | `text`      |     |       |                           |
| `webhook_url`                       | Webhook URL                   | `char`      |     |       |                           |
| `website_message_ids`               | Website Messages              | `one2many`  |     | ✅    | mail.message              |
| `website_path`                      | Website Path                  | `char`      |     |       |                           |
| `website_published`                 | Available on the Website      | `boolean`   |     |       |                           |
| `website_url`                       | Website Url                   | `char`      |     |       |                           |
| `write_date`                        | Last Updated on               | `datetime`  |     | ✅    |                           |
| `write_uid`                         | Last Updated by               | `many2one`  |     | ✅    | res.users                 |
| `xml_id`                            | External ID                   | `char`      |     |       |                           |

**Access Rights:**

| Name               | Group                | Perms     |
| ------------------ | -------------------- | --------- |
| ir_cron group_cron | Role / Administrator | `R/W/C/D` |

### 🗃️ `ir.actions.server` — Server Action

> 📧 Mail Thread

Add website option in server actions.

**Fields:**

| Field                               | Label                         | Type        | Req | Store | Relation                  |
| ----------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------- |
| `action_class`                      | Action Class                  | `char`      |     | ✅    |                           |
| `activity_calendar_event_id`        | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event            |
| `activity_date_deadline`            | Next Activity Deadline        | `date`      |     |       |                           |
| `activity_date_deadline_range`      | Due Date In                   | `integer`   |     | ✅    |                           |
| `activity_date_deadline_range_type` | Due type                      | `selection` |     | ✅    |                           |
| `activity_exception_decoration`     | Activity Exception Decoration | `selection` |     |       |                           |
| `activity_exception_icon`           | Icon                          | `char`      |     |       |                           |
| `activity_ids`                      | Activities                    | `one2many`  |     | ✅    | mail.activity             |
| `activity_note`                     | Note                          | `html`      |     | ✅    |                           |
| `activity_state`                    | Activity State                | `selection` |     |       |                           |
| `activity_summary`                  | Title                         | `char`      |     | ✅    |                           |
| `activity_type_icon`                | Activity Type Icon            | `char`      |     |       |                           |
| `activity_type_id`                  | Activity Type                 | `many2one`  |     | ✅    | mail.activity.type        |
| `activity_user_field_name`          | User Field                    | `char`      |     | ✅    |                           |
| `activity_user_id`                  | Responsible                   | `many2one`  |     | ✅    | res.users                 |
| `activity_user_type`                | User Type                     | `selection` |     | ✅    |                           |
| `allowed_states`                    | Allowed states                | `json`      |     |       |                           |
| `automated_name`                    | Automated Name                | `char`      |     | ✅    |                           |
| `available_model_ids`               | Available Models              | `many2many` |     |       | ir.model                  |
| `base_automation_id`                | Automation Rule               | `many2one`  |     | ✅    | base.automation           |
| `binding_model_id`                  | Binding Model                 | `many2one`  |     | ✅    | ir.model                  |
| `binding_type`                      | Binding Type                  | `selection` | ✅  | ✅    |                           |
| `binding_view_types`                | Binding View Types            | `char`      |     | ✅    |                           |
| `child_ids`                         | Child Actions                 | `one2many`  |     | ✅    | ir.actions.server         |
| `code`                              | Python Code                   | `text`      |     | ✅    |                           |
| `create_date`                       | Created on                    | `datetime`  |     | ✅    |                           |
| `create_uid`                        | Created by                    | `many2one`  |     | ✅    | res.users                 |
| `crud_model_id`                     | Record to Create              | `many2one`  |     | ✅    | ir.model                  |
| `crud_model_name`                   | Target Model Name             | `char`      |     |       |                           |
| `display_name`                      | Display Name                  | `char`      |     |       |                           |
| `evaluation_type`                   | Value Type                    | `selection` |     | ✅    |                           |
| `followers_partner_field_name`      | Followers Field               | `char`      |     | ✅    |                           |
| `followers_type`                    | Followers Type                | `selection` |     | ✅    |                           |
| `group_ids`                         | Allowed Groups                | `many2many` |     | ✅    | res.groups                |
| `has_message`                       | Has Message                   | `boolean`   |     |       |                           |
| `help`                              | Action Description            | `html`      |     | ✅    |                           |
| `html_value`                        | Html Value                    | `html`      |     | ✅    |                           |
| `icon`                              | Icon                          | `char`      |     | ✅    |                           |
| `id`                                | ID                            | `integer`   |     | ✅    |                           |
| `ir_cron_ids`                       | Scheduled Action              | `one2many`  |     | ✅    | ir.cron                   |
| `link_field_id`                     | Link Field                    | `many2one`  |     | ✅    | ir.model.fields           |
| `mail_post_autofollow`              | Subscribe Recipients          | `boolean`   |     | ✅    |                           |
| `mail_post_method`                  | Send Email As                 | `selection` |     | ✅    |                           |
| `message_attachment_count`          | Attachment Count              | `integer`   |     |       |                           |
| `message_follower_ids`              | Followers                     | `one2many`  |     | ✅    | mail.followers            |
| `message_has_error`                 | Message Delivery error        | `boolean`   |     |       |                           |
| `message_has_error_counter`         | Number of errors              | `integer`   |     |       |                           |
| `message_has_sms_error`             | SMS Delivery error            | `boolean`   |     |       |                           |
| `message_ids`                       | Messages                      | `one2many`  |     | ✅    | mail.message              |
| `message_is_follower`               | Is Follower                   | `boolean`   |     |       |                           |
| `message_needaction`                | Action Needed                 | `boolean`   |     |       |                           |
| `message_needaction_counter`        | Number of Actions             | `integer`   |     |       |                           |
| `message_partner_ids`               | Followers (Partners)          | `many2many` |     |       | res.partner               |
| `model_id`                          | Model                         | `many2one`  | ✅  | ✅    | ir.model                  |
| `model_name`                        | Model Name                    | `char`      |     |       |                           |
| `my_activity_date_deadline`         | My Activity Deadline          | `date`      |     |       |                           |
| `name`                              | Action Name                   | `char`      | ✅  | ✅    |                           |
| `parent_id`                         | Parent Action                 | `many2one`  |     | ✅    | ir.actions.server         |
| `partner_ids`                       | Partner                       | `many2many` |     | ✅    | res.partner               |
| `path`                              | Path to show in the URL       | `char`      |     | ✅    |                           |
| `rating_ids`                        | Ratings                       | `one2many`  |     | ✅    | rating.rating             |
| `resource_ref`                      | Record                        | `reference` |     | ✅    |                           |
| `selection_value`                   | Custom Value                  | `many2one`  |     | ✅    | ir.model.fields.selection |
| `sequence`                          | Sequence                      | `integer`   |     | ✅    |                           |
| `sequence_id`                       | Sequence to use               | `many2one`  |     | ✅    | ir.sequence               |
| `show_code_history`                 | Show Code History             | `boolean`   |     |       |                           |
| `sms_method`                        | Send SMS As                   | `selection` |     | ✅    |                           |
| `sms_template_id`                   | SMS Template                  | `many2one`  |     | ✅    | sms.template              |
| `state`                             | Type                          | `selection` | ✅  | ✅    |                           |
| `template_id`                       | Email Template                | `many2one`  |     | ✅    | mail.template             |
| `type`                              | Action Type                   | `char`      | ✅  | ✅    |                           |
| `update_boolean_value`              | Boolean Value                 | `selection` |     | ✅    |                           |
| `update_field_id`                   | Field to Update               | `many2one`  |     | ✅    | ir.model.fields           |
| `update_field_type`                 | Field Type                    | `selection` |     |       |                           |
| `update_m2m_operation`              | Many2many Operations          | `selection` |     | ✅    |                           |
| `update_path`                       | Field to Update Path          | `char`      |     | ✅    |                           |
| `update_related_model_id`           | Update Related Model          | `many2one`  |     | ✅    | ir.model                  |
| `usage`                             | Usage                         | `selection` | ✅  | ✅    |                           |
| `value`                             | Value                         | `text`      |     | ✅    |                           |
| `value_field_to_show`               | Value Field To Show           | `selection` |     |       |                           |
| `warning`                           | Warning                       | `text`      |     |       |                           |
| `webhook_field_ids`                 | Webhook Fields                | `many2many` |     | ✅    | ir.model.fields           |
| `webhook_sample_payload`            | Sample Payload                | `text`      |     |       |                           |
| `webhook_url`                       | Webhook URL                   | `char`      |     | ✅    |                           |
| `website_message_ids`               | Website Messages              | `one2many`  |     | ✅    | mail.message              |
| `website_path`                      | Website Path                  | `char`      |     | ✅    |                           |
| `website_published`                 | Available on the Website      | `boolean`   |     | ✅    |                           |
| `website_url`                       | Website Url                   | `char`      |     |       |                           |
| `write_date`                        | Last Updated on               | `datetime`  |     | ✅    |                           |
| `write_uid`                         | Last Updated by               | `many2one`  |     | ✅    | res.users                 |
| `xml_id`                            | External ID                   | `char`      |     |       |                           |

**Access Rights:**

| Name                           | Group                | Perms     |
| ------------------------------ | -------------------- | --------- |
| ir_actions_server_group_system | Role / Administrator | `R/W/C/D` |
