---
title: "Spreadsheet Base"
module: "spreadsheet_base"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org/"
license: "Other proprietary"
category: "Uncategorized"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_____________]
---

# 🟢 Spreadsheet Base

> **Module:** `spreadsheet_base` | **Version:** `19.0.1.0` **Category:** Uncategorized |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org/

## 🔗 Dependencies

[[spreadsheet]] [[base_sparse_field]] [[bus]]

## 📖 Description

[![Odoo Community Association](https://odoo-community.org/readme-banner-image)](https://odoo-community.org/get-involved?utm_source=readme)

# Spreadsheet Oca

[![Beta](https://img.shields.io/badge/maturity-Beta-yellow.png)](https://odoo-community.org/page/development-status)
[![License: AGPL-3](https://img.shields.io/badge/license-AGPL--3-blue.png)](http://www.gnu.org/licenses/agpl-3.0-standalone.html)
[![OCA/spreadsheet](https://img.shields.io/badge/github-OCA%2Fspreadsheet-lightgray.png?logo=github)](https://github.com/OCA/spreadsheet/tree/18.0/spreadsheet_base)
[![Translate me on Weblate](https://img.shields.io/badge/weblate-Translate%20me-F47D42.png)](https://translation.odoo-community.org/projects/spreadsheet-18-0/spreadsheet-18-0-spreadsheet_base)
[![Try me on Runboat](https://img.shields.io/badge/runboat-Try%20me-875A7B.png)](https://runboat.odoo-community.org/builds?repo=OCA/spreadsheet&target_branch=18.0)

This module adds a functionality for adding and editing Spreadsheets using Odoo CE.

It is an alternative to the proprietary module spreadsheet_edition of Odoo Enterprise
Edition.

**Table of contents**

- [Usage](#usage)
  - [**Create a new spreadsheet**](#create-a-new-spreadsheet)
  - [**Create a new dynamic spreadsheet from pivot**](#create-a-new-dynamic-spreadsheet-from-pivot)
- [Development](#development)
- [Known issues / Roadmap](#known-issues-roadmap)
  - [Adding new lines on pivot tables](#adding-new-lines-on-pivot-tables)
- [Bug Tracker](#bug-tracker)
- [Credits](#credits)
  - [Authors](#authors)
  - [Contributors](#contributors)
  - [Maintainers](#maintainers)

## [Usage](#toc-entry-1)

### [**Create a new spreadsheet**](#toc-entry-2)

- Go to ‘Spreadsheet’ menu
- Click on ‘Create’
- Put a name, then click on the “Edit” button

![image1](https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/static/description/spreadsheet_create.png)

- At this point you switch to spreadsheet editing mode. The editor is named
  o-spreadsheet and looks like another common spreadsheet web editors. (OnlyOffice,
  Ethercalc, Google Sheets (non-free)).

![image2](https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/static/description/spreadsheet_edit.png)

- You can use common functions SUM(), AVERAGE(), etc. in the cells. For a complete list
  of functions and their syntax, Refer to the documentation
  <https://github.com/odoo/o-spreadsheet/> or go to
  <https://odoo.github.io/o-spreadsheet/> and click on “Insert > Function”.

![image3](https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/static/description/o-spreadsheet.png)

- Note: Business Odoo module can add “business functions”. This is currently the case
  for the accounting module, which adds the following features:

  > - ODOO.CREDIT(account_codes, date_range): Get the total credit for the specified
  >   account(s) and period.
  > - ODOO.DEBIT(account_codes, date_range): Get the total debit for the specified
  >   account(s) and period.
  > - ODOO.BALANCE(account_codes, date_range): Get the total balance for the specified
  >   account(s) and period.
  > - ODOO.FISCALYEAR.START(day): Returns the starting date of the fiscal year
  >   encompassing the provided date.
  > - ODOO.FISCALYEAR.END(day): Returns the ending date of the fiscal year encompassing
  >   the provided date.
  > - ODOO.ACCOUNT.GROUP(type): Returns the account ids of a given group where type
  >   should be a value of the account_type field of account.account model. (income,
  >   asset_receivable, etc.)

### [**Create a new dynamic spreadsheet from pivot**](#toc-entry-3)

- Go to any pivot
- Press on insert button
- Select the dynamic rows or dynamic columns option and set a number of rows/columns

A new table that will be updated with the actual or filtered values will be added.

- Note: When a pivot has multiple levels of aggrupations in the rows or the columns, the
  number of rows/columns selected will be transfered to each level.

  Example: number of groups -> 2 number of rows -> 3
  - val1
    - subval1.1
    - subval1.2
    - subval1.3
  - val2
    - subval2.1
    - subval2.2
    - subval2.3
  - val3
    - subval3.1
    - subval3.2
    - subval3.3

<https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/Hhttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ehttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/rhttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ehttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/>
<https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ihttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/shttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/>
<https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ahttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/>
<https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/vhttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ihttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/shttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/uhttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ahttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/lhttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/>
<https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ehttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/xhttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ahttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/phttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/lhttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ehttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/>
<https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ohttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/fhttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/>
<https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/uhttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/shttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ehttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/:https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/>
<https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/.https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/.https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/>
<https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/fhttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ihttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ghttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/uhttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/rhttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/ehttps://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/:https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/:https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/>
<https://raw.githubusercontent.com/OCA/spreadsheet/18.0/spreadsheet_base/../static/description/spreadsheetdynamic_table.gif>

## [Development](#toc-entry-4)

If you want to develop custom business functions, you can add others, based on the file
<https://github.com/odoo/odoo/blob/16.0/addons/spreadsheet_account/static/src/accounting_functions.js>

## [Known issues / Roadmap](#toc-entry-5)

### [Adding new lines on pivot tables](#toc-entry-6)

When we add a pivot table, the number of rows is predefined according to the current
data.

In order to add new rows, we need to reinsert the pivot table.

## [Bug Tracker](#toc-entry-7)

Bugs are tracked on [GitHub Issues](https://github.com/OCA/spreadsheet/issues). In case
of trouble, please check there if your issue has already been reported. If you spotted
it first, help us to smash it by providing a detailed and welcomed
[feedback](https://github.com/OCA/spreadsheet/issues/new?body=module:%20spreadsheet_base%0Aversion:%2018.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

Do not contact contributors directly about support or help with technical issues.

## [Credits](#toc-entry-8)

### [Authors](#toc-entry-9)

- CreuBlanca

### [Contributors](#toc-entry-10)

- Enric Tobella
- [Tecnativa](https://www.tecnativa.com):
  - Carlos Roca
- [Open User Systems](https://www.openusersystems.com):
  - Chris Mann

### [Maintainers](#toc-entry-11)

This module is maintained by the OCA.

[![Odoo Community Association](https://odoo-community.org/logo.png)](https://odoo-community.org)

OCA, or the Odoo Community Association, is a nonprofit organization whose mission is to
support the collaborative development of Odoo features and promote its widespread use.

This module is part of the
[OCA/spreadsheet](https://github.com/OCA/spreadsheet/tree/18.0/spreadsheet_base) project
on GitHub.

You are welcome to contribute. To learn how please visit
<https://odoo-community.org/page/Contribute>.

## 🖥️ UI Components

### Menus

- `Spreadsheets`

### Views

- `spreadsheet.select.row.number.form (form)`
- `spreadsheet.spreadsheet.import.form (in spreadsheet_base) (form)`
- `spreadsheet.spreadsheet.search (in spreadsheet_base) (search)`
- `spreadsheet.spreadsheet.tree (in spreadsheet_base) (form)`
- `spreadsheet.spreadsheet.tree (in spreadsheet_base) (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**7 model(s) defined by this module:**

### 🗃️ `spreadsheet.spreadsheet.import` — Import data to spreadsheet

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                   | Label                 | Type         | Req | Store | Relation                            |
| ----------------------- | --------------------- | ------------ | --- | ----- | ----------------------------------- |
| `can_be_dynamic`        | Can Be Dynamic        | `boolean`    |     | ✅    |                                     |
| `can_have_dynamic_cols` | Can Have Dynamic Cols | `boolean`    |     | ✅    |                                     |
| `create_date`           | Created on            | `datetime`   |     | ✅    |                                     |
| `create_uid`            | Created by            | `many2one`   |     | ✅    | res.users                           |
| `datasource_name`       | Datasource Name       | `char`       |     | ✅    |                                     |
| `display_name`          | Display Name          | `char`       |     |       |                                     |
| `dynamic`               | Dynamic Rows          | `boolean`    |     | ✅    |                                     |
| `dynamic_cols`          | Dynamic Columns       | `boolean`    |     | ✅    |                                     |
| `id`                    | ID                    | `integer`    |     | ✅    |                                     |
| `import_data`           | Import Data           | `serialized` |     | ✅    |                                     |
| `is_tree`               | Is Tree               | `boolean`    |     | ✅    |                                     |
| `mode`                  | Code                  | `char`       |     |       |                                     |
| `mode_id`               | Mode                  | `many2one`   | ✅  | ✅    | spreadsheet.spreadsheet.import.mode |
| `name`                  | Name                  | `char`       |     | ✅    |                                     |
| `number_of_cols`        | Number of Columns     | `integer`    |     | ✅    |                                     |
| `number_of_rows`        | Number Of Rows        | `integer`    |     | ✅    |                                     |
| `spreadsheet_id`        | Spreadsheet           | `many2one`   |     | ✅    | spreadsheet.spreadsheet             |
| `write_date`            | Last Updated on       | `datetime`   |     | ✅    |                                     |
| `write_uid`             | Last Updated by       | `many2one`   |     | ✅    | res.users                           |

**Access Rights:**

| Name                                  | Group       | Perms     |
| ------------------------------------- | ----------- | --------- |
| access_spreadsheet_spreadsheet_import | Role / User | `R/W/C/D` |

### 🗃️ `spreadsheet.spreadsheet.import.mode` — Import Mode

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation   |
| -------------- | --------------- | ----------- | --- | ----- | ---------- |
| `code`         | Code            | `char`      | ✅  | ✅    |            |
| `create_date`  | Created on      | `datetime`  |     | ✅    |            |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users  |
| `display_name` | Display Name    | `char`      |     |       |            |
| `group_ids`    | Group           | `many2many` |     | ✅    | res.groups |
| `id`           | ID              | `integer`   |     | ✅    |            |
| `name`         | Name            | `char`      | ✅  | ✅    |            |
| `sequence`     | Sequence        | `integer`   |     | ✅    |            |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |            |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users  |

**Access Rights:**

| Name                             | Group       | Perms |
| -------------------------------- | ----------- | ----- |
| access_spreadsheet_base_revision | Role / User | `R`   |

**Record Rules:**

- **Spreadsheet Import mode** (Global) `R/W/C/D`
  - Domain: `[('group_ids','in', user.group_ids.ids)]`

### 🗃️ `spreadsheet.select.row.number` — Select number of rows to duplicate row

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                   | Label                 | Type       | Req | Store | Relation  |
| ----------------------- | --------------------- | ---------- | --- | ----- | --------- |
| `can_have_dynamic_cols` | Can Have Dynamic Cols | `boolean`  |     | ✅    |           |
| `create_date`           | Created on            | `datetime` |     | ✅    |           |
| `create_uid`            | Created by            | `many2one` |     | ✅    | res.users |
| `display_name`          | Display Name          | `char`     |     |       |           |
| `dynamic_cols`          | Dynamic Cols          | `boolean`  |     | ✅    |           |
| `dynamic_rows`          | Dynamic Rows          | `boolean`  |     | ✅    |           |
| `id`                    | ID                    | `integer`  |     | ✅    |           |
| `number_of_cols`        | Number Of Cols        | `integer`  |     | ✅    |           |
| `number_of_rows`        | Number Of Rows        | `integer`  |     | ✅    |           |
| `write_date`            | Last Updated on       | `datetime` |     | ✅    |           |
| `write_uid`             | Last Updated by       | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                                 | Group       | Perms     |
| ------------------------------------ | ----------- | --------- |
| access_spreadsheet_select_row_number | Role / User | `R/W/C/D` |

### 🗃️ `spreadsheet.spreadsheet` — Spreadsheet

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label                | Type         | Req | Store | Relation                  |
| -------------------------- | -------------------- | ------------ | --- | ----- | ------------------------- |
| `company_id`               | Company              | `many2one`   |     | ✅    | res.company               |
| `contributor_group_ids`    | Contributors Groups  | `many2many`  |     | ✅    | res.groups                |
| `contributor_ids`          | Contributors         | `many2many`  |     | ✅    | res.users                 |
| `create_date`              | Created on           | `datetime`   |     | ✅    |                           |
| `create_uid`               | Created by           | `many2one`   |     | ✅    | res.users                 |
| `display_name`             | Display Name         | `char`       |     |       |                           |
| `filename`                 | Filename             | `char`       |     |       |                           |
| `id`                       | ID                   | `integer`    |     | ✅    |                           |
| `name`                     | Name                 | `char`       | ✅  | ✅    |                           |
| `owner_id`                 | Owner                | `many2one`   | ✅  | ✅    | res.users                 |
| `reader_group_ids`         | Readers Groups       | `many2many`  |     | ✅    | res.groups                |
| `reader_ids`               | Readers              | `many2many`  |     | ✅    | res.users                 |
| `spreadsheet_binary_data`  | Spreadsheet file     | `binary`     |     | ✅    |                           |
| `spreadsheet_raw`          | Spreadsheet Raw      | `serialized` |     |       |                           |
| `spreadsheet_revision_ids` | Spreadsheet Revision | `one2many`   |     | ✅    | spreadsheet.base.revision |
| `write_date`               | Last Updated on      | `datetime`   |     | ✅    |                           |
| `write_uid`                | Last Updated by      | `many2one`   |     | ✅    | res.users                 |

**Access Rights:**

| Name                           | Group              | Perms     |
| ------------------------------ | ------------------ | --------- |
| access_spreadsheet_spreadsheet | Spreadsheet / User | `R/W/C/D` |

**Record Rules:**

- **Spreadsheet Company Rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Spreadsheet Owner** (55) `R/W/C/D`
  - Domain: `[('owner_id','=', user.id)]`
- **Spreadsheet Contributor** (55) `R/W`
  - Domain: `[('contributor_ids','=', user.id)]`
- **Spreadsheet Reader** (55) `R`
  - Domain: `[('reader_ids','=', user.id)]`
- **Spreadsheet Manager** (56) `R/W/C/D`
  - Domain: `[(1,'=', 1)]`

### 🗃️ `spreadsheet.abstract` — Spreadsheet abstract for inheritance

Allow sending messages related to the current model via as a bus.bus channel.

    The model needs to be allowed as a valid channel for the bus in `_build_bus_channel_list`.

**Fields:**

| Field                      | Label                | Type         | Req | Store | Relation                  |
| -------------------------- | -------------------- | ------------ | --- | ----- | ------------------------- |
| `display_name`             | Display Name         | `char`       |     |       |                           |
| `id`                       | ID                   | `integer`    |     | ✅    |                           |
| `name`                     | Name                 | `char`       | ✅  | ✅    |                           |
| `spreadsheet_binary_data`  | Spreadsheet file     | `binary`     |     | ✅    |                           |
| `spreadsheet_raw`          | Spreadsheet Raw      | `serialized` |     |       |                           |
| `spreadsheet_revision_ids` | Spreadsheet Revision | `one2many`   |     | ✅    | spreadsheet.base.revision |

### 🗃️ `spreadsheet.base.revision` — Spreadsheet Oca Revision

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label           | Type       | Req | Store | Relation  |
| -------------------- | --------------- | ---------- | --- | ----- | --------- |
| `client_id`          | Client          | `char`     |     | ✅    |           |
| `commands`           | Commands        | `char`     |     | ✅    |           |
| `create_date`        | Created on      | `datetime` |     | ✅    |           |
| `create_uid`         | Created by      | `many2one` |     | ✅    | res.users |
| `display_name`       | Display Name    | `char`     |     |       |           |
| `id`                 | ID              | `integer`  |     | ✅    |           |
| `model`              | Model           | `char`     | ✅  | ✅    |           |
| `next_revision_id`   | Next Revision   | `char`     |     | ✅    |           |
| `res_id`             | Res             | `integer`  | ✅  | ✅    |           |
| `server_revision_id` | Server Revision | `char`     |     | ✅    |           |
| `type`               | Type            | `char`     |     | ✅    |           |
| `write_date`         | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`          | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                             | Group       | Perms     |
| -------------------------------- | ----------- | --------- |
| access_spreadsheet_base_revision | Role / User | `R/W/C/D` |

### 🗃️ `ir.websocket` — websocket message handling

Override to handle discuss specific features (channel in particular).

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |
