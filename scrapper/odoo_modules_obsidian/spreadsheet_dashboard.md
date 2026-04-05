---
title: "Spreadsheet dashboard"
module: "spreadsheet_dashboard"
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

# 🟢 Spreadsheet dashboard

> **Module:** `spreadsheet_dashboard` | **Version:** `19.0.1.0` **Category:** Dashboard
> | **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[spreadsheet]]

## 📖 Description

Spreadsheet

## 🖥️ UI Components

### Menus

- `Dashboards`
- `Dashboards/Configuration`
- `Dashboards/Configuration/Dashboards`
- `Dashboards/Dashboards`

### Views

- `spreadsheet.dashboard.group.view.form (form)`
- `spreadsheet.dashboard.group.view.list (list)`
- `spreadsheet.dashboard.kanban (kanban)`
- `spreadsheet.dashboard.view.form (form)`
- `spreadsheet.dashboard.view.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

### 🗃️ `spreadsheet.dashboard.share` — Copy of a shared dashboard

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label                 | Type       | Req | Store | Relation              |
| ------------------------- | --------------------- | ---------- | --- | ----- | --------------------- |
| `access_token`            | Access Token          | `char`     | ✅  | ✅    |                       |
| `create_date`             | Created on            | `datetime` |     | ✅    |                       |
| `create_uid`              | Created by            | `many2one` |     | ✅    | res.users             |
| `dashboard_id`            | Dashboard             | `many2one` | ✅  | ✅    | spreadsheet.dashboard |
| `display_name`            | Display Name          | `char`     |     |       |                       |
| `excel_export`            | Excel Export          | `binary`   |     | ✅    |                       |
| `full_url`                | URL                   | `char`     |     |       |                       |
| `id`                      | ID                    | `integer`  |     | ✅    |                       |
| `name`                    | Name                  | `char`     |     |       |                       |
| `spreadsheet_binary_data` | Spreadsheet file      | `binary`   |     | ✅    |                       |
| `spreadsheet_data`        | Spreadsheet Data      | `text`     |     |       |                       |
| `spreadsheet_file_name`   | Spreadsheet File Name | `char`     |     |       |                       |
| `thumbnail`               | Thumbnail             | `binary`   |     | ✅    |                       |
| `write_date`              | Last Updated on       | `datetime` |     | ✅    |                       |
| `write_uid`               | Last Updated by       | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                               | Group       | Perms     |
| ---------------------------------- | ----------- | --------- |
| access_spreadsheet_dashboard_share | Role / User | `R/W/C/D` |

**Record Rules:**

- **spreadsheet.dashboard.share: create uid** (1) `R/W/C/D`
  - Domain: `[('create_uid', '=', user.id)]`

### 🗃️ `spreadsheet.dashboard.group` — Group of dashboards

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label               | Type       | Req | Store | Relation              |
| ------------------------- | ------------------- | ---------- | --- | ----- | --------------------- |
| `create_date`             | Created on          | `datetime` |     | ✅    |                       |
| `create_uid`              | Created by          | `many2one` |     | ✅    | res.users             |
| `dashboard_ids`           | Dashboard           | `one2many` |     | ✅    | spreadsheet.dashboard |
| `display_name`            | Display Name        | `char`     |     |       |                       |
| `id`                      | ID                  | `integer`  |     | ✅    |                       |
| `name`                    | Name                | `char`     | ✅  | ✅    |                       |
| `published_dashboard_ids` | Published Dashboard | `one2many` |     | ✅    | spreadsheet.dashboard |
| `sequence`                | Sequence            | `integer`  |     | ✅    |                       |
| `write_date`              | Last Updated on     | `datetime` |     | ✅    |                       |
| `write_uid`               | Last Updated by     | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                                    | Group             | Perms     |
| --------------------------------------- | ----------------- | --------- |
| access_spreadsheet_dashboard_group      | Dashboard / Admin | `R/W/C/D` |
| access_spreadsheet_dashboard_group_user | Role / User       | `R`       |

### 🗃️ `spreadsheet.dashboard` — Spreadsheet Dashboard

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                      | Type        | Req | Store | Relation                    |
| ---------------------------- | -------------------------- | ----------- | --- | ----- | --------------------------- |
| `company_ids`                | Companies                  | `many2many` |     | ✅    | res.company                 |
| `create_date`                | Created on                 | `datetime`  |     | ✅    |                             |
| `create_uid`                 | Created by                 | `many2one`  |     | ✅    | res.users                   |
| `dashboard_group_id`         | Dashboard Group            | `many2one`  | ✅  | ✅    | spreadsheet.dashboard.group |
| `display_name`               | Display Name               | `char`      |     |       |                             |
| `favorite_user_ids`          | Favorite Users             | `many2many` |     | ✅    | res.users                   |
| `group_ids`                  | Group                      | `many2many` |     | ✅    | res.groups                  |
| `id`                         | ID                         | `integer`   |     | ✅    |                             |
| `is_favorite`                | Is Favorite                | `boolean`   |     |       |                             |
| `is_published`               | Is Published               | `boolean`   |     | ✅    |                             |
| `main_data_model_ids`        | Main Data Model            | `many2many` |     | ✅    | ir.model                    |
| `name`                       | Name                       | `char`      | ✅  | ✅    |                             |
| `sample_dashboard_file_path` | Sample Dashboard File Path | `char`      |     | ✅    |                             |
| `sequence`                   | Sequence                   | `integer`   |     | ✅    |                             |
| `spreadsheet_binary_data`    | Spreadsheet file           | `binary`    |     | ✅    |                             |
| `spreadsheet_data`           | Spreadsheet Data           | `text`      |     |       |                             |
| `spreadsheet_file_name`      | Spreadsheet File Name      | `char`      |     |       |                             |
| `thumbnail`                  | Thumbnail                  | `binary`    |     | ✅    |                             |
| `write_date`                 | Last Updated on            | `datetime`  |     | ✅    |                             |
| `write_uid`                  | Last Updated by            | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                       | Group             | Perms     |
| -------------------------- | ----------------- | --------- |
| spreadsheet_dashboard      | Dashboard / Admin | `R/W/C/D` |
| spreadsheet_dashboard_user | Role / User       | `R`       |

**Record Rules:**

- **Spreadsheet dashboard: groups** (1) `R/W/C/D`
  - Domain: `[('group_ids', 'in', user.all_group_ids.ids)]`
- **Dashboard multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_ids', 'in', company_ids + [False])]`
- **Spreadsheet dashboard: manager** (57) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
