---
title: "In-App Purchases"
module: "iap"
state: "installed"
version: "19.0.1.1"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Tools"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_____]
---

# 🟢 In-App Purchases

> **Module:** `iap` | **Version:** `19.0.1.1` **Category:** Tools | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[web]] [[base_setup]]

## 📖 Description

This module provides standard tools (account model, context manager and helpers) to
support In-App purchases inside Odoo.

## 🖥️ UI Components

### Menus

- `Settings/Technical/IAP`
- `Settings/Technical/IAP/IAP Accounts`

### Views

- `* INHERIT res.config.settings.view.form.inherit.base.setup.iap (form)`
- `iap.account.form (form)`
- `iap.account.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

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

### 🗃️ `iap.enrich.api` — IAP Lead Enrichment API

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `iap.service` — IAP Service

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label           | Type       | Req | Store | Relation  |
| ----------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`     | Created on      | `datetime` |     | ✅    |           |
| `create_uid`      | Created by      | `many2one` |     | ✅    | res.users |
| `description`     | Description     | `char`     | ✅  | ✅    |           |
| `display_name`    | Display Name    | `char`     |     |       |           |
| `id`              | ID              | `integer`  |     | ✅    |           |
| `integer_balance` | Integer Balance | `boolean`  | ✅  | ✅    |           |
| `name`            | Name            | `char`     | ✅  | ✅    |           |
| `technical_name`  | Technical Name  | `char`     | ✅  | ✅    |           |
| `unit_name`       | Unit Name       | `char`     | ✅  | ✅    |           |
| `write_date`      | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`       | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                | Group                | Perms     |
| ------------------- | -------------------- | --------- |
| iap.service.manager | Role / Administrator | `R/W/C/D` |
| iap.service.user    | Role / User          | `R`       |
