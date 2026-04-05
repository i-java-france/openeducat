---
title: "IAP / Mail"
module: "iap_mail"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Tools"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_____]
---

# 🟢 IAP / Mail

> **Module:** `iap_mail` | **Version:** `19.0.1.0` **Category:** Tools | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[iap]] [[mail]]

## 📖 Description

Bridge between IAP and mail

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT iap.account.view.form (form)`
- `enrich_company (qweb)`
- `enrich_company_by_dnb (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

### 🗃️ `iap.account` — IAP Account

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `account_token`              | Account Token          | `char`      |     | ✅    |                |
| `balance`                    | Balance                | `char`      |     | ✅    |                |
| `company_ids`                | Company                | `many2many` |     | ✅    | res.company    |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users      |
| `description`                | Description            | `char`      |     |       |                |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `name`                       | Name                   | `char`      |     | ✅    |                |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `sender_name`                | Sender Name            | `char`      |     | ✅    |                |
| `service_id`                 | Service                | `many2one`  | ✅  | ✅    | iap.service    |
| `service_locked`             | Service Locked         | `boolean`   |     | ✅    |                |
| `service_name`               | Technical Name         | `char`      |     |       |                |
| `state`                      | State                  | `selection` |     | ✅    |                |
| `warning_threshold`          | Email Alert Threshold  | `float`     |     | ✅    |                |
| `warning_user_ids`           | Email Alert Recipients | `many2many` |     | ✅    | res.users      |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                | Group                | Perms     |
| ------------------- | -------------------- | --------- |
| iap.account.manager | Role / Administrator | `R/W/C/D` |
| iap.account.user    | Role / User          | `R/C`     |

**Record Rules:**

- **User IAP Account** (1) `R/W/C/D`
  - Domain: `['|', ('company_ids', '=', False), ('company_ids', 'in', company_ids)]`
