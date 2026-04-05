---
title: "Esign"
module: "esign_intg"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "http://www.openeducat.org"
license: "Other proprietary"
category: "Uncategorized"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_____________]
---

# 🟢 Esign

> **Module:** `esign_intg` | **Version:** `19.0.1.0` **Category:** Uncategorized |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> http://www.openeducat.org

## 🔗 Dependencies

[[base]] [[website]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `E-sign`
- `E-sign/Configuration`
- `E-sign/Configuration/Field Types`
- `E-sign/Configuration/Roles`
- `E-sign/Documents`
- `E-sign/E-sign`

### Views

- `* INHERIT res.users.esign.form.inherit (form)`
- `Document Template (form)`
- `Document Template (list)`
- `E-sign Request (form)`
- `E-sign Request (list)`
- `E-sign Template (form)`
- `E-sign Tree (list)`
- `Item types input info (qweb)`
- `Template To Sign (qweb)`
- `e.sign.item.role.form (form)`
- `e.sign.item.role.tree (list)`
- `e.sign.items.form (form)`
- `e.sign.items.tree (list)`
- `e.sign.logs.tree (list)`
- `e.sign.request.item.form (form)`
- `e.sign.request.item.tree (list)`
- `e.sign.request.kanban (kanban)`
- `e.sign.request.search (search)`
- `e.sign.template.kanban (kanban)`
- `e.sign.template.lines.form (form)`
- `e.sign.template.lines.tree (list)`
- `e.sign.template.search (search)`
- `esign.send.form.view (form)`
- `esign_request_logs (qweb)`
- `send.copy.view.form (form)`
- `share.document.view.form (form)`

### Reports

- `Logs`

## 🛠️ Technical Documentation

**16 model(s) defined by this module:**

### 🗃️ `document.template` — Document Template

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
| `code`                          | Code                          | `char`      |     | ✅    |                    |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `data`                          | Pdf                           | `binary`    | ✅  | ✅    |                    |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `font_color`                    | Font Color                    | `char`      |     | ✅    |                    |
| `fonts_size`                    | Font Size                     | `integer`   |     | ✅    |                    |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
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
| `model_id`                      | Data Model                    | `many2one`  |     | ✅    | ir.model           |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                    |
| `name`                          | Name                          | `char`      | ✅  | ✅    |                    |
| `page_size`                     | Page Size                     | `selection` |     | ✅    |                    |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                            | Group         | Perms     |
| ------------------------------- | ------------- | --------- |
| access_document_template_portal | Role / Portal | `R/W/C/D` |
| access_document_template        | Role / User   | `R/W/C/D` |

### 🗃️ `e.sign.template.lines` — E-sign Template Lines

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
| `alignment`                     | Alignment                     | `char`      | ✅  | ✅    |                    |
| `company_custom`                | Company Custom                | `selection` |     | ✅    |                    |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `find_text`                     | Text                          | `char`      |     | ✅    |                    |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `height`                        | Height                        | `float`     |     | ✅    |                    |
| `height_pix`                    | Height Pix                    | `float`     |     | ✅    |                    |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
| `is_position`                   | Is Position?                  | `boolean`   |     | ✅    |                    |
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
| `option_ids`                    | Selection options             | `many2many` |     | ✅    | e.sign.item.option |
| `page_height`                   | Page Height                   | `float`     |     | ✅    |                    |
| `page_number`                   | Page Number                   | `integer`   |     | ✅    |                    |
| `page_width`                    | Page Width                    | `float`     |     | ✅    |                    |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `required`                      | Required                      | `boolean`   |     | ✅    |                    |
| `responsible_id`                | Responsible                   | `many2one`  |     | ✅    | e.sign.item.role   |
| `responsible_key`               | Responsible Key               | `char`      |     | ✅    |                    |
| `template_id`                   | Template                      | `many2one`  |     | ✅    | e.sign.template    |
| `type_id`                       | Type                          | `many2one`  | ✅  | ✅    | e.sign.items       |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `width`                         | Width                         | `float`     |     | ✅    |                    |
| `width_pix`                     | Width Pix                     | `float`     |     | ✅    |                    |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |
| `x_offset`                      | X Offset                      | `float`     |     | ✅    |                    |
| `x_position`                    | X Position                    | `float`     |     | ✅    |                    |
| `x_position_percentage`         | X Position Percentage         | `float`     |     | ✅    |                    |
| `y_offset`                      | Y Offset                      | `float`     |     | ✅    |                    |
| `y_position`                    | Y Position                    | `float`     |     | ✅    |                    |
| `y_position_percentage`         | Y Position Percentage         | `float`     |     | ✅    |                    |

**Access Rights:**

| Name                                | Group         | Perms     |
| ----------------------------------- | ------------- | --------- |
| access_e_sign_template_lines_portal | Role / Portal | `R/W/C/D` |
| access_e_sign_template_lines        | Role / User   | `R/W/C/D` |

### 🗃️ `e.sign.request` — Signature Request

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation            |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------- |
| `access_token`                  | Security Token                | `char`      |     | ✅    |                     |
| `access_token_expired`          | Access Token Expired          | `boolean`   |     | ✅    |                     |
| `access_url`                    | Portal Access URL             | `char`      |     |       |                     |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event      |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                     |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                     |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                     |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity       |
| `activity_state`                | Activity State                | `selection` |     |       |                     |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                     |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                     |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type  |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users           |
| `color`                         | Color                         | `integer`   |     | ✅    |                     |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company         |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                     |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users           |
| `display_name`                  | Display Name                  | `char`      |     |       |                     |
| `doc_name`                      | Document Name                 | `char`      |     |       |                     |
| `favorited_ids`                 | Favorite of                   | `many2many` |     | ✅    | res.users           |
| `final_pdf`                     | Final Pdf                     | `binary`    |     | ✅    |                     |
| `group_ids`                     | Template Access Group         | `many2many` |     | ✅    | res.groups          |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                     |
| `id`                            | ID                            | `integer`   |     | ✅    |                     |
| `is_sign_order`                 | Sign Order                    | `boolean`   |     | ✅    |                     |
| `item_info`                     | Item Info                     | `binary`    |     |       |                     |
| `last_action_date`              | Last Action Date              | `datetime`  |     |       |                     |
| `message`                       | sign.message                  | `html`      |     | ✅    |                     |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                     |
| `message_cc`                    | sign.message_cc               | `html`      |     | ✅    |                     |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers      |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                     |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                     |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                     |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message        |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                     |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                     |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                     |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner         |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                     |
| `privacy`                       | Who can Sign                  | `selection` |     | ✅    |                     |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating       |
| `request_item_ids`              | Signers                       | `one2many`  |     | ✅    | e.sign.request.item |
| `sign_closed`                   | Completed Signatures          | `integer`   |     |       |                     |
| `sign_log_ids`                  | Logs                          | `one2many`  |     | ✅    | e.sign.logs         |
| `sign_total`                    | Requested Signatures          | `integer`   |     |       |                     |
| `sign_wait`                     | Sent Requests                 | `integer`   |     |       |                     |
| `sign_with_key`                 | Sign With Key                 | `boolean`   |     | ✅    |                     |
| `state`                         | State                         | `selection` |     | ✅    |                     |
| `status_url`                    | Status URL                    | `char`      |     | ✅    |                     |
| `subject`                       | Email Subject                 | `char`      |     | ✅    |                     |
| `tag_ids`                       | Tags                          | `many2many` |     |       | esign.tag           |
| `template_id`                   | Template                      | `many2one`  |     | ✅    | e.sign.template     |
| `url`                           | URL                           | `char`      |     | ✅    |                     |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message        |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                     |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                         | Group         | Perms     |
| ---------------------------- | ------------- | --------- |
| access_e_sign_request_portal | Role / Portal | `R/W/C/D` |
| access_e_sign_request_public | Role / Public | `R/W/C/D` |
| access_e_sign_request        | Role / User   | `R/W/C/D` |

### 🗃️ `e.sign.template` — Template for Document

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation              |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | --------------------- |
| `active`                        | Active                        | `boolean`   |     | ✅    |                       |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event        |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                       |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                       |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                       |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity         |
| `activity_state`                | Activity State                | `selection` |     |       |                       |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                       |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                       |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type    |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users             |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                       |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users             |
| `data`                          | Pdf                           | `binary`    |     |       |                       |
| `display_name`                  | Display Name                  | `char`      |     |       |                       |
| `favorited_ids`                 | Invited Users                 | `many2many` |     | ✅    | res.users             |
| `group_ids`                     | Template Access Group         | `many2many` |     | ✅    | res.groups            |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                       |
| `id`                            | ID                            | `integer`   |     | ✅    |                       |
| `in_progress_count`             | In Progress Count             | `integer`   |     |       |                       |
| `is_favorite`                   | Is Favorite                   | `boolean`   |     | ✅    |                       |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                       |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers        |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                       |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                       |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                       |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message          |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                       |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                       |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                       |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner           |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                       |
| `name`                          | Template name                 | `char`      |     | ✅    |                       |
| `privacy`                       | Who can Sign                  | `selection` |     | ✅    |                       |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating         |
| `redirect_url`                  | Redirect Link                 | `char`      |     | ✅    |                       |
| `share_link`                    | Share Link                    | `char`      |     | ✅    |                       |
| `show_open_requests`            | Show Open Requests            | `boolean`   |     |       |                       |
| `signed_count`                  | Signed Count                  | `integer`   |     |       |                       |
| `tag_ids`                       | Tags                          | `many2many` |     | ✅    | esign.tag             |
| `template_id`                   | Template                      | `many2one`  | ✅  | ✅    | document.template     |
| `template_lines`                | Template Lines                | `one2many`  | ✅  | ✅    | e.sign.template.lines |
| `user_id`                       | Responsible                   | `many2one`  |     | ✅    | res.users             |
| `username`                      | User Name                     | `char`      |     | ✅    |                       |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message          |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                       |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                   | Group    | Perms     |
| ---------------------- | -------- | --------- |
| access_e_sign_template | Everyone | `R/W/C/D` |

**Record Rules:**

- **e.sign.template: Manage by Invited Users** (Global) `R/W/C/D`
  - Domain:
    `['|', ('privacy', '=', 'invite'), '&' , ('privacy', '=', 'employee'), ('favorited_ids', 'in', [user.id])]`
- **e.sign.template: Manage by All Users** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `e.sign.request.signer` — E-Sign request signer

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                    | Label               | Type       | Req | Store | Relation         |
| ------------------------ | ------------------- | ---------- | --- | ----- | ---------------- |
| `create_date`            | Created on          | `datetime` |     | ✅    |                  |
| `create_uid`             | Created by          | `many2one` |     | ✅    | res.users        |
| `display_name`           | Display Name        | `char`     |     |       |                  |
| `e_sign_send_request_id` | E Sign Send Request | `many2one` |     | ✅    | esign.send       |
| `id`                     | ID                  | `integer`  |     | ✅    |                  |
| `partner_id`             | Contact             | `many2one` | ✅  | ✅    | res.partner      |
| `role_id`                | Role                | `many2one` | ✅  | ✅    | e.sign.item.role |
| `sent_order`             | Sign Order          | `integer`  |     | ✅    |                  |
| `write_date`             | Last Updated on     | `datetime` |     | ✅    |                  |
| `write_uid`              | Last Updated by     | `many2one` |     | ✅    | res.users        |

**Access Rights:**

| Name                         | Group       | Perms     |
| ---------------------------- | ----------- | --------- |
| access_e_sign_request_signer | Role / User | `R/W/C/D` |

### 🗃️ `esign.tag` — ESign Tag

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `color`        | Color Index     | `integer`  |     | ✅    |           |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Tag Name        | `char`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name             | Group       | Perms     |
| ---------------- | ----------- | --------- |
| access_esign_tag | Role / User | `R/W/C/D` |

### 🗃️ `e.sign.item.option` — Item Option

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
| `value`        | Option          | `text`     |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                             | Group         | Perms     |
| -------------------------------- | ------------- | --------- |
| access_e_sign_item_option_portal | Role / Portal | `R/W/C/D` |
| access_e_sign_item_option        | Role / User   | `R/W/C/D` |

### 🗃️ `e.sign.item.role` — Item Role

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
| `default`      | Default         | `boolean`  | ✅  | ✅    |           |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Name            | `char`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                    | Group       | Perms     |
| ----------------------- | ----------- | --------- |
| access_e_sign_item_role | Role / User | `R/W/C/D` |

### 🗃️ `send.copy` — Send copy

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation       |
| -------------- | --------------- | ----------- | --- | ----- | -------------- |
| `create_date`  | Created on      | `datetime`  |     | ✅    |                |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users      |
| `display_name` | Display Name    | `char`      |     |       |                |
| `id`           | ID              | `integer`   |     | ✅    |                |
| `partner_ids`  | Contact         | `many2many` |     | ✅    | res.partner    |
| `request_id`   | Request         | `many2one`  |     | ✅    | e.sign.request |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |                |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name             | Group       | Perms     |
| ---------------- | ----------- | --------- |
| access_send_copy | Role / User | `R/W/C/D` |

### 🗃️ `esign.send` — Send sign request

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field            | Label           | Type        | Req | Store | Relation              |
| ---------------- | --------------- | ----------- | --- | ----- | --------------------- |
| `activity_id`    | Linked Activity | `many2one`  |     | ✅    | mail.activity         |
| `attachment_ids` | Attachments     | `many2many` |     | ✅    | ir.attachment         |
| `create_date`    | Created on      | `datetime`  |     | ✅    |                       |
| `create_uid`     | Created by      | `many2one`  |     | ✅    | res.users             |
| `display_name`   | Display Name    | `char`      |     |       |                       |
| `filename`       | File Name       | `char`      |     | ✅    |                       |
| `follower_ids`   | Copy to         | `many2many` |     | ✅    | res.partner           |
| `id`             | ID              | `integer`   |     | ✅    |                       |
| `is_sign_order`  | Sign Order      | `boolean`   |     | ✅    |                       |
| `is_template`    | Is Template     | `boolean`   |     | ✅    |                       |
| `message`        | Message         | `html`      |     | ✅    |                       |
| `message_cc`     | CC Message      | `html`      |     | ✅    |                       |
| `partner_id`     | Contact         | `many2one`  |     | ✅    | res.partner           |
| `signer_ids`     | Signers         | `one2many`  |     | ✅    | e.sign.request.signer |
| `signers_count`  | Signers Count   | `integer`   |     | ✅    |                       |
| `subject`        | Subject         | `char`      | ✅  | ✅    |                       |
| `template_id`    | Template        | `many2one`  |     | ✅    | e.sign.template       |
| `write_date`     | Last Updated on | `datetime`  |     | ✅    |                       |
| `write_uid`      | Last Updated by | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name              | Group       | Perms     |
| ----------------- | ----------- | --------- |
| access_esign_send | Role / User | `R/W/C/D` |

### 🗃️ `share.document` — Share Document

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                | Label              | Type       | Req | Store | Relation        |
| -------------------- | ------------------ | ---------- | --- | ----- | --------------- |
| `create_date`        | Created on         | `datetime` |     | ✅    |                 |
| `create_uid`         | Created by         | `many2one` |     | ✅    | res.users       |
| `display_name`       | Display Name       | `char`     |     |       |                 |
| `id`                 | ID                 | `integer`  |     | ✅    |                 |
| `is_one_responsible` | Is One Responsible | `boolean`  |     | ✅    |                 |
| `template_id`        | Template           | `many2one` | ✅  | ✅    | e.sign.template |
| `url`                | Link to Share      | `char`     |     | ✅    |                 |
| `user_id`            | Responsible        | `many2one` |     |       | res.users       |
| `write_date`         | Last Updated on    | `datetime` |     | ✅    |                 |
| `write_uid`          | Last Updated by    | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                  | Group       | Perms     |
| --------------------- | ----------- | --------- |
| access_share_document | Role / User | `R/W/C/D` |

### 🗃️ `e.sign.items` — Sign Items

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label                   | Type        | Req | Store | Relation           |
| ---------------- | ----------------------- | ----------- | --- | ----- | ------------------ |
| `auto_field`     | Auto-fill Partner Field | `char`      |     | ✅    |                    |
| `create_date`    | Created on              | `datetime`  |     | ✅    |                    |
| `create_uid`     | Created by              | `many2one`  |     | ✅    | res.users          |
| `default_height` | Default Height          | `float`     | ✅  | ✅    |                    |
| `default_width`  | Default Width           | `float`     | ✅  | ✅    |                    |
| `display_name`   | Display Name            | `char`      |     |       |                    |
| `id`             | ID                      | `integer`   |     | ✅    |                    |
| `item_type`      | Type                    | `selection` | ✅  | ✅    |                    |
| `name`           | Field Name              | `char`      | ✅  | ✅    |                    |
| `option_ids`     | Selection options       | `many2many` |     | ✅    | e.sign.item.option |
| `placeholder`    | Placeholder             | `char`      |     | ✅    |                    |
| `responsible_id` | Responsible             | `many2one`  |     | ✅    | e.sign.item.role   |
| `tip`            | Tip                     | `char`      | ✅  | ✅    |                    |
| `write_date`     | Last Updated on         | `datetime`  |     | ✅    |                    |
| `write_uid`      | Last Updated by         | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                       | Group         | Perms     |
| -------------------------- | ------------- | --------- |
| access_e_sign_items_portal | Role / Portal | `R/W/C/D` |
| access_e_sign_items        | Role / User   | `R/W/C/D` |

### 🗃️ `e.sign.request.item` — Sign request item

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label           | Type        | Req | Store | Relation                  |
| ----------------- | --------------- | ----------- | --- | ----- | ------------------------- |
| `access_token`    | Access Token    | `char`      | ✅  | ✅    |                           |
| `create_date`     | Created on      | `datetime`  |     | ✅    |                           |
| `create_uid`      | Created by      | `many2one`  |     | ✅    | res.users                 |
| `display_name`    | Display Name    | `char`      |     |       |                           |
| `id`              | ID              | `integer`   |     | ✅    |                           |
| `is_mail_sent`    | Is Mail Sent    | `boolean`   |     | ✅    |                           |
| `item_value_ids`  | Value           | `one2many`  |     | ✅    | e.sign.request.item.value |
| `latitude`        | Latitude        | `float`     |     | ✅    |                           |
| `longitude`       | Longitude       | `float`     |     | ✅    |                           |
| `partner_id`      | Contact         | `many2one`  |     | ✅    | res.partner               |
| `request_id`      | Sign Request    | `many2one`  | ✅  | ✅    | e.sign.request            |
| `responsible_id`  | Responsible     | `many2one`  |     | ✅    | e.sign.item.role          |
| `responsible_key` | Responsible Key | `char`      |     | ✅    |                           |
| `role_id`         | Role            | `many2one`  |     | ✅    | e.sign.item.role          |
| `sent_order`      | Sign Order      | `integer`   |     | ✅    |                           |
| `signature`       | Signature       | `binary`    |     | ✅    |                           |
| `signer_email`    | Signer Email    | `char`      |     | ✅    |                           |
| `signing_date`    | Signed on       | `date`      |     | ✅    |                           |
| `state`           | State           | `selection` |     | ✅    |                           |
| `url`             | url             | `char`      |     | ✅    |                           |
| `write_date`      | Last Updated on | `datetime`  |     | ✅    |                           |
| `write_uid`       | Last Updated by | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name                              | Group         | Perms     |
| --------------------------------- | ------------- | --------- |
| access_e_sign_request_item_portal | Role / Portal | `R/W/C/D` |
| access_e_sign_request_item        | Role / User   | `R/W/C/D` |

### 🗃️ `e.sign.request.item.value` — Sign request item Value

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label             | Type       | Req | Store | Relation              |
| ----------------- | ----------------- | ---------- | --- | ----- | --------------------- |
| `alignment`       | Alignment         | `char`     |     | ✅    |                       |
| `create_date`     | Created on        | `datetime` |     | ✅    |                       |
| `create_uid`      | Created by        | `many2one` |     | ✅    | res.users             |
| `display_name`    | Display Name      | `char`     |     |       |                       |
| `id`              | ID                | `integer`  |     | ✅    |                       |
| `item_id`         | Sign Item         | `many2one` |     | ✅    | e.sign.template.lines |
| `request_id`      | Sign Request      | `many2one` |     |       | e.sign.request        |
| `request_item_id` | Sign Request item | `many2one` |     | ✅    | e.sign.request.item   |
| `value_data`      | Value Data        | `text`     |     | ✅    |                       |
| `write_date`      | Last Updated on   | `datetime` |     | ✅    |                       |
| `write_uid`       | Last Updated by   | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                                    | Group         | Perms     |
| --------------------------------------- | ------------- | --------- |
| access_e_sign_request_item_value_portal | Role / Portal | `R/W/C/D` |
| access_e_sign_request_item_value        | Role / User   | `R/W/C/D` |

### 🗃️ `e.sign.logs` — Sign requests access history

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field              | Label                              | Type        | Req | Store | Relation            |
| ------------------ | ---------------------------------- | ----------- | --- | ----- | ------------------- |
| `action`           | Action Performed                   | `selection` | ✅  | ✅    |                     |
| `create_date`      | Created on                         | `datetime`  |     | ✅    |                     |
| `create_uid`       | Created by                         | `many2one`  |     | ✅    | res.users           |
| `display_name`     | Display Name                       | `char`      |     |       |                     |
| `id`               | ID                                 | `integer`   |     | ✅    |                     |
| `ip`               | IP address of the visitor          | `char`      |     | ✅    |                     |
| `latitude`         | Latitude                           | `float`     |     | ✅    |                     |
| `log_date`         | Log Date                           | `datetime`  | ✅  | ✅    |                     |
| `longitude`        | Longitude                          | `float`     |     | ✅    |                     |
| `partner_id`       | Partner                            | `many2one`  |     | ✅    | res.partner         |
| `request_item_ids` | Request Item                       | `many2one`  |     | ✅    | e.sign.request.item |
| `request_state`    | State of the request on action log | `selection` | ✅  | ✅    |                     |
| `sign_request_id`  | Sign Request                       | `many2one`  | ✅  | ✅    | e.sign.request      |
| `token`            | User token                         | `char`      |     | ✅    |                     |
| `user_id`          | User                               | `many2one`  |     | ✅    | res.users           |
| `write_date`       | Last Updated on                    | `datetime`  |     | ✅    |                     |
| `write_uid`        | Last Updated by                    | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name               | Group       | Perms     |
| ------------------ | ----------- | --------- |
| access_e_sign_logs | Role / User | `R/W/C/D` |

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
