---
title: "Portal Rating"
module: "portal_rating"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Services"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/________]
---

# 🟢 Portal Rating

> **Module:** `portal_rating` | **Version:** `19.0.1.0` **Category:** Services |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[portal]] [[rating]]

## 📖 Description

Bridge module adding rating capabilities on portal. It includes notably inclusion of
rating directly within the customer portal discuss widget.

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT message_thread (qweb)`
- `* INHERIT rating.rating.view.form (form)`
- `Rating: rating composer in popup (qweb)`
- `Rating: static star widget (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

### 🗃️ `ir.http` — HTTP Routing

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `mail.message` — Message

Override MailMessage class in order to add a new type: SMS messages. Those messages
comes with their own notification method, using SMS gateway.

**Fields:**

| Field                             | Label                              | Type                 | Req | Store | Relation                  |
| --------------------------------- | ---------------------------------- | -------------------- | --- | ----- | ------------------------- |
| `account_audit_log_account_id`    | Account                            | `many2one`           |     |       | account.account           |
| `account_audit_log_company_id`    | Company                            | `many2one`           |     |       | res.company               |
| `account_audit_log_move_id`       | Journal Entry                      | `many2one`           |     |       | account.move              |
| `account_audit_log_partner_id`    | Partner                            | `many2one`           |     |       | res.partner               |
| `account_audit_log_preview`       | Description                        | `text`               |     |       |                           |
| `account_audit_log_restricted`    | Protected by restricted Audit Logs | `boolean`            |     |       |                           |
| `account_audit_log_tax_id`        | Tax                                | `many2one`           |     |       | account.tax               |
| `attachment_ids`                  | Attachments                        | `many2many`          |     | ✅    | ir.attachment             |
| `author_avatar`                   | Author's avatar                    | `binary`             |     |       |                           |
| `author_guest_id`                 | Guest                              | `many2one`           |     | ✅    | mail.guest                |
| `author_id`                       | Author                             | `many2one`           |     | ✅    | res.partner               |
| `body`                            | Contents                           | `html`               |     | ✅    |                           |
| `call_history_ids`                | Call History                       | `one2many`           |     | ✅    | discuss.call.history      |
| `channel_id`                      | Channel                            | `many2one`           |     |       | discuss.channel           |
| `child_ids`                       | Child Messages                     | `one2many`           |     | ✅    | mail.message              |
| `create_date`                     | Created on                         | `datetime`           |     | ✅    |                           |
| `create_uid`                      | Created by                         | `many2one`           |     | ✅    | res.users                 |
| `date`                            | Date                               | `datetime`           |     | ✅    |                           |
| `display_name`                    | Display Name                       | `char`               |     |       |                           |
| `email_add_signature`             | Email Add Signature                | `boolean`            |     | ✅    |                           |
| `email_from`                      | From                               | `char`               |     | ✅    |                           |
| `email_layout_xmlid`              | Layout                             | `char`               |     | ✅    |                           |
| `has_error`                       | Has error                          | `boolean`            |     |       |                           |
| `has_sms_error`                   | Has SMS error                      | `boolean`            |     |       |                           |
| `id`                              | ID                                 | `integer`            |     | ✅    |                           |
| `incoming_email_cc`               | Emails Cc                          | `char`               |     | ✅    |                           |
| `incoming_email_to`               | Emails To                          | `text`               |     | ✅    |                           |
| `is_current_user_or_guest_author` | Is Current User Or Guest Author    | `boolean`            |     |       |                           |
| `is_internal`                     | Employee Only                      | `boolean`            |     | ✅    |                           |
| `letter_ids`                      | Letter                             | `one2many`           |     | ✅    | snailmail.letter          |
| `linked_message_ids`              | Linked Message                     | `many2many`          |     |       | mail.message              |
| `mail_activity_type_id`           | Mail Activity Type                 | `many2one`           |     | ✅    | mail.activity.type        |
| `mail_ids`                        | Mails                              | `one2many`           |     | ✅    | mail.mail                 |
| `mail_server_id`                  | Outgoing mail server               | `many2one`           |     | ✅    | ir.mail_server            |
| `message_id`                      | Message-Id                         | `char`               |     | ✅    |                           |
| `message_link_preview_ids`        | Message Link Preview               | `one2many`           |     | ✅    | mail.message.link.preview |
| `message_type`                    | Type                               | `selection`          | ✅  | ✅    |                           |
| `model`                           | Related Document Model             | `char`               |     | ✅    |                           |
| `needaction`                      | Need Action                        | `boolean`            |     |       |                           |
| `notification_ids`                | Notifications                      | `one2many`           |     | ✅    | mail.notification         |
| `notified_partner_ids`            | Partners with Need Action          | `many2many`          |     | ✅    | res.partner               |
| `outgoing_email_to`               | emails To                          | `char`               |     | ✅    |                           |
| `parent_id`                       | Parent Message                     | `many2one`           |     | ✅    | mail.message              |
| `partner_ids`                     | Recipients                         | `many2many`          |     | ✅    | res.partner               |
| `pinned_at`                       | Pinned                             | `datetime`           |     | ✅    |                           |
| `preview`                         | Preview                            | `char`               |     |       |                           |
| `rating_id`                       | Rating                             | `many2one`           |     |       | rating.rating             |
| `rating_ids`                      | Related ratings                    | `one2many`           |     | ✅    | rating.rating             |
| `rating_value`                    | Rating Value                       | `float`              |     |       |                           |
| `reaction_ids`                    | Reactions                          | `one2many`           |     | ✅    | mail.message.reaction     |
| `record_alias_domain_id`          | Alias Domain                       | `many2one`           |     | ✅    | mail.alias.domain         |
| `record_company_id`               | Company                            | `many2one`           |     | ✅    | res.company               |
| `record_name`                     | Message Record Name                | `char`               |     |       |                           |
| `reply_to`                        | Reply-To                           | `char`               |     | ✅    |                           |
| `reply_to_force_new`              | No threading for answers           | `boolean`            |     | ✅    |                           |
| `res_id`                          | Related Document ID                | `many2one_reference` |     | ✅    |                           |
| `snailmail_error`                 | Snailmail message in error         | `boolean`            |     |       |                           |
| `starred`                         | Starred                            | `boolean`            |     |       |                           |
| `starred_partner_ids`             | Favorited By                       | `many2many`          |     | ✅    | res.partner               |
| `subject`                         | Subject                            | `char`               |     | ✅    |                           |
| `subtype_id`                      | Subtype                            | `many2one`           |     | ✅    | mail.message.subtype      |
| `tracking_value_ids`              | Tracking values                    | `one2many`           |     | ✅    | mail.tracking.value       |
| `write_date`                      | Last Updated on                    | `datetime`           |     | ✅    |                           |
| `write_uid`                       | Last Updated by                    | `many2one`           |     | ✅    | res.users                 |

**Access Rights:**

| Name                | Group         | Perms     |
| ------------------- | ------------- | --------- |
| mail.message.portal | Role / Portal | `R/W/C/D` |
| mail.message.all    | Role / Public | `R`       |
| mail.message.user   | Role / User   | `R/W/C/D` |

**Record Rules:**

- **User: All Chatter** (83) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `rating.rating` — Rating

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                 | Label                         | Type                 | Req | Store | Relation     |
| --------------------- | ----------------------------- | -------------------- | --- | ----- | ------------ |
| `access_token`        | Security Token                | `char`               |     | ✅    |              |
| `consumed`            | Filled Rating                 | `boolean`            |     | ✅    |              |
| `create_date`         | Submitted on                  | `datetime`           |     | ✅    |              |
| `create_uid`          | Created by                    | `many2one`           |     | ✅    | res.users    |
| `display_name`        | Display Name                  | `char`               |     |       |              |
| `feedback`            | Comment                       | `text`               |     | ✅    |              |
| `id`                  | ID                            | `integer`            |     | ✅    |              |
| `is_internal`         | Visible Internally Only       | `boolean`            |     | ✅    |              |
| `message_id`          | Message                       | `many2one`           |     | ✅    | mail.message |
| `parent_ref`          | Parent Ref                    | `reference`          |     |       |              |
| `parent_res_id`       | Parent Document               | `integer`            |     | ✅    |              |
| `parent_res_model`    | Parent Document Model         | `char`               |     | ✅    |              |
| `parent_res_model_id` | Parent Related Document Model | `many2one`           |     | ✅    | ir.model     |
| `parent_res_name`     | Parent Document Name          | `char`               |     | ✅    |              |
| `partner_id`          | Customer                      | `many2one`           |     | ✅    | res.partner  |
| `publisher_comment`   | Publisher comment             | `text`               |     | ✅    |              |
| `publisher_datetime`  | Commented on                  | `datetime`           |     | ✅    |              |
| `publisher_id`        | Commented by                  | `many2one`           |     | ✅    | res.partner  |
| `rated_on`            | Rated On                      | `datetime`           |     | ✅    |              |
| `rated_partner_id`    | Rated Operator                | `many2one`           |     | ✅    | res.partner  |
| `rated_partner_name`  | Name                          | `char`               |     |       |              |
| `rating`              | Rating Value                  | `float`              |     | ✅    |              |
| `rating_image`        | Image                         | `binary`             |     |       |              |
| `rating_image_url`    | Image URL                     | `char`               |     |       |              |
| `rating_text`         | Rating                        | `selection`          |     | ✅    |              |
| `res_id`              | Document                      | `many2one_reference` | ✅  | ✅    |              |
| `res_model`           | Document Model                | `char`               |     | ✅    |              |
| `res_model_id`        | Related Document Model        | `many2one`           |     | ✅    | ir.model     |
| `res_name`            | Resource name                 | `char`               |     | ✅    |              |
| `resource_ref`        | Resource Ref                  | `reference`          |     |       |              |
| `write_date`          | Last Updated on               | `datetime`           |     | ✅    |              |
| `write_uid`           | Last Updated by               | `many2one`           |     | ✅    | res.users    |

**Access Rights:**

| Name                        | Group                | Perms     |
| --------------------------- | -------------------- | --------- |
| rating.rating.access.system | Role / Administrator | `R/W/C/D` |
| rating.rating.portal        | Role / Portal        | `-`       |
| rating.rating.public        | Role / Public        | `-`       |
| rating.rating.user          | Role / User          | `R/W/C`   |
