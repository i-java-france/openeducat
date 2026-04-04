---
title: "Web Routing"
module: "http_routing"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Technical"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 Web Routing

> **Module:** `http_routing` | **Version:** `19.0.1.0` **Category:** Technical |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[web]]

## 📖 Description

Proposes advanced routing options not available in web or base to keep base modules
simple.

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT res.lang.form.http_routing.inherit (form)`
- `* INHERIT res.lang.list.model.inherit (list)`
- `400 (qweb)`
- `403 (qweb)`
- `415 (qweb)`
- `422 (qweb)`
- `4xx (qweb)`
- `500 (qweb)`
- `HTTP Error (qweb)`
- `Page Not Found (qweb)`
- `error_message (qweb)`
- `http_error_debug (qweb)`

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

### 🗃️ `ir.qweb` — Qweb

IrQweb object for rendering stuff in the website context

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |
