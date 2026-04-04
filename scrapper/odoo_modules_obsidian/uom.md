---
title: "Units of measure"
module: "uom"
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

# 🟢 Units of measure

> **Module:** `uom` | **Version:** `19.0.1.0` **Category:** Sales | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[base]]

## 📖 Description

# This is the base module for managing Units of measure.

## 🖥️ UI Components

### Menus

_none_

### Views

- `uom.uom.form (form)`
- `uom.uom.list (list)`
- `uom.uom.view.search (search)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

### 🗃️ `uom.uom` — Product Unit of Measure

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label                | Type        | Req | Store | Relation           |
| ---------------------- | -------------------- | ----------- | --- | ----- | ------------------ |
| `active`               | Active               | `boolean`   |     | ✅    |                    |
| `create_date`          | Created on           | `datetime`  |     | ✅    |                    |
| `create_uid`           | Created by           | `many2one`  |     | ✅    | res.users          |
| `display_name`         | Display Name         | `char`      |     |       |                    |
| `factor`               | Absolute Quantity    | `float`     |     | ✅    |                    |
| `fiscal_country_codes` | Fiscal Country Codes | `char`      |     |       |                    |
| `id`                   | ID                   | `integer`   |     | ✅    |                    |
| `name`                 | Unit Name            | `char`      | ✅  | ✅    |                    |
| `package_type_id`      | Package Type         | `many2one`  |     | ✅    | stock.package.type |
| `parent_path`          | Parent Path          | `char`      |     | ✅    |                    |
| `product_uom_ids`      | Barcodes             | `one2many`  |     | ✅    | product.uom        |
| `related_uom_ids`      | Related UoMs         | `one2many`  |     | ✅    | uom.uom            |
| `relative_factor`      | Contains             | `float`     | ✅  | ✅    |                    |
| `relative_uom_id`      | Reference Unit       | `many2one`  |     | ✅    | uom.uom            |
| `rounding`             | Rounding Precision   | `float`     |     |       |                    |
| `route_ids`            | Routes               | `many2many` |     |       | stock.route        |
| `sequence`             | Sequence             | `integer`   |     | ✅    |                    |
| `write_date`           | Last Updated on      | `datetime`  |     | ✅    |                    |
| `write_uid`            | Last Updated by      | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                    | Group                            | Perms     |
| ----------------------- | -------------------------------- | --------- |
| uom.uom.user            | Sales / User: Own Documents Only | `R`       |
| uom.uom.product.manager | Products / Create                | `R/W/C/D` |
| uom.uom.manager         | Role / Administrator             | `R/W/C/D` |
| uom.uom portal          | Role / Portal                    | `R`       |
| uom.uom public          | Role / Public                    | `R`       |
| uom.uom.user            | Role / User                      | `R`       |
