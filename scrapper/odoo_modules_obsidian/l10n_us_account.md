---
title: "United States - Accounting"
module: "l10n_us_account"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/documentation/latest/applications/finance/fiscal_localizations.html"
license: "LGPL-3"
category: "Account Charts"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/______________]
---

# 🟢 United States - Accounting

> **Module:** `l10n_us_account` | **Version:** `19.0.1.0` **Category:** Account Charts |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:**
> https://www.odoo.com/documentation/latest/applications/finance/fiscal_localizations.html

## 🔗 Dependencies

[[l10n_us]] [[account]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT res.bank.view.form.inherit.intermediary (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**2 model(s) defined by this module:**

### 🗃️ `account.chart.template` — Account Chart Template

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `res.bank` — Bank

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label                | Type       | Req | Store | Relation          |
| ---------------------- | -------------------- | ---------- | --- | ----- | ----------------- |
| `active`               | Active               | `boolean`  |     | ✅    |                   |
| `bic`                  | Bank Identifier Code | `char`     |     | ✅    |                   |
| `city`                 | City                 | `char`     |     | ✅    |                   |
| `country`              | Country              | `many2one` |     | ✅    | res.country       |
| `country_code`         | Country Code         | `char`     |     |       |                   |
| `create_date`          | Created on           | `datetime` |     | ✅    |                   |
| `create_uid`           | Created by           | `many2one` |     | ✅    | res.users         |
| `display_name`         | Display Name         | `char`     |     |       |                   |
| `email`                | Email                | `char`     |     | ✅    |                   |
| `id`                   | ID                   | `integer`  |     | ✅    |                   |
| `intermediary_bank_id` | Intermediary Bank    | `many2one` |     | ✅    | res.bank          |
| `name`                 | Name                 | `char`     | ✅  | ✅    |                   |
| `phone`                | Phone                | `char`     |     | ✅    |                   |
| `state`                | Fed. State           | `many2one` |     | ✅    | res.country.state |
| `street`               | Street               | `char`     |     | ✅    |                   |
| `street2`              | Street2              | `char`     |     | ✅    |                   |
| `write_date`           | Last Updated on      | `datetime` |     | ✅    |                   |
| `write_uid`            | Last Updated by      | `many2one` |     | ✅    | res.users         |
| `zip`                  | Zip                  | `char`     |     | ✅    |                   |

**Access Rights:**

| Name                           | Group                | Perms     |
| ------------------------------ | -------------------- | --------- |
| res_bank_group_partner_manager | Contact / Creation   | `R/W/C/D` |
| res_bank_group_system          | Role / Administrator | `R/W/C/D` |
| res_bank user                  | Role / User          | `R`       |
