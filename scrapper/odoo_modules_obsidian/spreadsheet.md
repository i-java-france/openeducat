---
title: "Spreadsheet"
module: "spreadsheet"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Dashboard"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 Spreadsheet

> **Module:** `spreadsheet` | **Version:** `19.0.1.0` **Category:** Dashboard |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[bus]] [[web]] [[portal]]

## 📖 Description

Spreadsheet

## 🖥️ UI Components

### Menus

_none_

### Views

- `Public spreadsheet layout (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**6 model(s) defined by this module:**

### 🗃️ `res.currency` — Currency

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                       | Type        | Req | Store | Relation          |
| ----------------------------- | --------------------------- | ----------- | --- | ----- | ----------------- |
| `active`                      | Active                      | `boolean`   |     | ✅    |                   |
| `create_date`                 | Created on                  | `datetime`  |     | ✅    |                   |
| `create_uid`                  | Created by                  | `many2one`  |     | ✅    | res.users         |
| `currency_subunit_label`      | Currency Subunit            | `char`      |     | ✅    |                   |
| `currency_unit_label`         | Currency Unit               | `char`      |     | ✅    |                   |
| `date`                        | Date                        | `date`      |     |       |                   |
| `decimal_places`              | Decimal Places              | `integer`   |     | ✅    |                   |
| `display_name`                | Display Name                | `char`      |     |       |                   |
| `display_rounding_warning`    | Display Rounding Warning    | `boolean`   |     |       |                   |
| `fiscal_country_codes`        | Fiscal Country Codes        | `char`      |     |       |                   |
| `full_name`                   | Name                        | `char`      |     | ✅    |                   |
| `id`                          | ID                          | `integer`   |     | ✅    |                   |
| `inverse_rate`                | Inverse Rate                | `float`     |     |       |                   |
| `is_current_company_currency` | Is Current Company Currency | `boolean`   |     |       |                   |
| `iso_numeric`                 | Currency numeric code.      | `integer`   |     | ✅    |                   |
| `name`                        | Currency                    | `char`      | ✅  | ✅    |                   |
| `position`                    | Symbol Position             | `selection` |     | ✅    |                   |
| `rate`                        | Current Rate                | `float`     |     |       |                   |
| `rate_ids`                    | Rates                       | `one2many`  |     | ✅    | res.currency.rate |
| `rate_string`                 | Rate String                 | `char`      |     |       |                   |
| `rounding`                    | Rounding Factor             | `float`     |     | ✅    |                   |
| `symbol`                      | Symbol                      | `char`      | ✅  | ✅    |                   |
| `write_date`                  | Last Updated on             | `datetime`  |     | ✅    |                   |
| `write_uid`                   | Last Updated by             | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                         | Group                | Perms     |
| ---------------------------- | -------------------- | --------- |
| res.currency account manager | Accounting / Advisor | `R/W/C/D` |
| res_currency group_system    | Role / Administrator | `R/W/C/D` |
| res_currency group_all       | Role / Portal        | `R`       |
| res_currency group_all       | Role / Public        | `R`       |
| res_currency group_all       | Role / User          | `R`       |

### 🗃️ `res.currency.rate` — Currency Rate

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label                | Type       | Req | Store | Relation     |
| ---------------------- | -------------------- | ---------- | --- | ----- | ------------ |
| `company_id`           | Company              | `many2one` |     | ✅    | res.company  |
| `company_rate`         | Company Rate         | `float`    |     |       |              |
| `create_date`          | Created on           | `datetime` |     | ✅    |              |
| `create_uid`           | Created by           | `many2one` |     | ✅    | res.users    |
| `currency_id`          | Currency             | `many2one` | ✅  | ✅    | res.currency |
| `display_name`         | Display Name         | `char`     |     |       |              |
| `id`                   | ID                   | `integer`  |     | ✅    |              |
| `inverse_company_rate` | Inverse Company Rate | `float`    |     |       |              |
| `name`                 | Date                 | `date`     | ✅  | ✅    |              |
| `rate`                 | Technical Rate       | `float`    |     | ✅    |              |
| `write_date`           | Last Updated on      | `datetime` |     | ✅    |              |
| `write_uid`            | Last Updated by      | `many2one` |     | ✅    | res.users    |

**Access Rights:**

| Name                              | Group                | Perms     |
| --------------------------------- | -------------------- | --------- |
| res.currency.rate account manager | Accounting / Advisor | `R/W/C/D` |
| res_currency_rate group_system    | Role / Administrator | `R/W/C/D` |
| res_currency_rate group_all       | Role / Portal        | `R`       |
| res_currency_rate group_all       | Role / Public        | `R`       |
| res_currency_rate group_all       | Role / User          | `R`       |

**Record Rules:**

- **multi-company currency rate rule** (Global) `R/W/C/D`
  - Domain:
    `['|', ('company_id', 'parent_of', company_ids), ('company_id', '=', False)]`

### 🗃️ `ir.http` — HTTP Routing

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `res.lang` — Languages

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label               | Type        | Req | Store | Relation  |
| ---------------- | ------------------- | ----------- | --- | ----- | --------- |
| `active`         | Active              | `boolean`   |     | ✅    |           |
| `code`           | Locale Code         | `char`      | ✅  | ✅    |           |
| `create_date`    | Created on          | `datetime`  |     | ✅    |           |
| `create_uid`     | Created by          | `many2one`  |     | ✅    | res.users |
| `date_format`    | Date Format         | `selection` | ✅  | ✅    |           |
| `decimal_point`  | Decimal Separator   | `char`      | ✅  | ✅    |           |
| `direction`      | Direction           | `selection` | ✅  | ✅    |           |
| `display_name`   | Display Name        | `char`      |     |       |           |
| `flag_image`     | Image               | `binary`    |     | ✅    |           |
| `flag_image_url` | Flag Image Url      | `char`      |     |       |           |
| `grouping`       | Separator Format    | `selection` | ✅  | ✅    |           |
| `id`             | ID                  | `integer`   |     | ✅    |           |
| `iso_code`       | ISO code            | `char`      |     | ✅    |           |
| `name`           | Name                | `char`      | ✅  | ✅    |           |
| `thousands_sep`  | Thousands Separator | `char`      |     | ✅    |           |
| `time_format`    | Time Format         | `selection` | ✅  | ✅    |           |
| `url_code`       | URL Code            | `char`      | ✅  | ✅    |           |
| `week_start`     | First Day of Week   | `selection` | ✅  | ✅    |           |
| `write_date`     | Last Updated on     | `datetime`  |     | ✅    |           |
| `write_uid`      | Last Updated by     | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                | Group                | Perms     |
| ------------------- | -------------------- | --------- |
| res_lang group_user | Role / Administrator | `R/W/C/D` |
| res_lang group_all  | Role / Portal        | `R`       |
| res_lang group_all  | Role / Public        | `R`       |
| res_lang group_all  | Role / User          | `R`       |

### 🗃️ `ir.model` — Models

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                      | Type        | Req | Store | Relation        |
| ------------------------------- | -------------------------- | ----------- | --- | ----- | --------------- |
| `abstract`                      | Abstract Model             | `boolean`   |     | ✅    |                 |
| `access_ids`                    | Access                     | `one2many`  |     | ✅    | ir.model.access |
| `count`                         | Count (Incl. Archived)     | `integer`   |     |       |                 |
| `create_date`                   | Created on                 | `datetime`  |     | ✅    |                 |
| `create_uid`                    | Created by                 | `many2one`  |     | ✅    | res.users       |
| `display_name`                  | Display Name               | `char`      |     |       |                 |
| `field_id`                      | Fields                     | `one2many`  | ✅  | ✅    | ir.model.fields |
| `fold_name`                     | Fold Field                 | `char`      |     | ✅    |                 |
| `id`                            | ID                         | `integer`   |     | ✅    |                 |
| `info`                          | Information                | `text`      |     | ✅    |                 |
| `inherited_model_ids`           | Inherited models           | `many2many` |     |       | ir.model        |
| `is_mail_activity`              | Has Mail Activity          | `boolean`   |     | ✅    |                 |
| `is_mail_blacklist`             | Has Mail Blacklist         | `boolean`   |     | ✅    |                 |
| `is_mailing_enabled`            | Mailing Enabled            | `boolean`   |     |       |                 |
| `is_mail_thread`                | Has Mail Thread            | `boolean`   |     | ✅    |                 |
| `is_mail_thread_sms`            | Mail Thread SMS            | `boolean`   |     |       |                 |
| `is_phone_whatsapp`             | Whatsapp Contact           | `boolean`   |     |       |                 |
| `model`                         | Model                      | `char`      | ✅  | ✅    |                 |
| `modules`                       | In Apps                    | `char`      |     |       |                 |
| `name`                          | Model Description          | `char`      | ✅  | ✅    |                 |
| `order`                         | Order                      | `char`      | ✅  | ✅    |                 |
| `rule_ids`                      | Record Rules               | `one2many`  |     | ✅    | ir.rule         |
| `state`                         | Type                       | `selection` |     | ✅    |                 |
| `transient`                     | Transient Model            | `boolean`   |     | ✅    |                 |
| `view_ids`                      | Views                      | `one2many`  |     |       | ir.ui.view      |
| `website_form_access`           | Allowed to use in forms    | `boolean`   |     | ✅    |                 |
| `website_form_default_field_id` | Field for custom form data | `many2one`  |     | ✅    | ir.model.fields |
| `website_form_key`              | Website Form Key           | `char`      |     | ✅    |                 |
| `website_form_label`            | Label for form action      | `char`      |     | ✅    |                 |
| `write_date`                    | Last Updated on            | `datetime`  |     | ✅    |                 |
| `write_uid`                     | Last Updated by            | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                       | Group                  | Perms     |
| -------------------------- | ---------------------- | --------- |
| access_ir_model            | Email Marketing / User | `R`       |
| ir_model group_erp_manager | Access Rights          | `R/W/C/D` |
| ir_model_all               | Role / User            | `-`       |

### 🗃️ `spreadsheet.mixin` — Spreadsheet mixin

The base model, which is implicitly inherited by all models.

**Fields:**

| Field                     | Label                 | Type      | Req | Store | Relation |
| ------------------------- | --------------------- | --------- | --- | ----- | -------- |
| `display_name`            | Display Name          | `char`    |     |       |          |
| `id`                      | ID                    | `integer` |     | ✅    |          |
| `spreadsheet_binary_data` | Spreadsheet file      | `binary`  |     | ✅    |          |
| `spreadsheet_data`        | Spreadsheet Data      | `text`    |     |       |          |
| `spreadsheet_file_name`   | Spreadsheet File Name | `char`    |     |       |          |
| `thumbnail`               | Thumbnail             | `binary`  |     | ✅    |          |
