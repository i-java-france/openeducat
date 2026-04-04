---
title: "Barcode - GS1 Nomenclature"
module: "barcodes_gs1_nomenclature"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Inventory"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 Barcode - GS1 Nomenclature

> **Module:** `barcodes_gs1_nomenclature` | **Version:** `19.0.1.0` **Category:**
> Inventory | **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[barcodes]] [[uom]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT Barcode Nomenclatures (form)`
- `* INHERIT Barcode Nomenclatures (list)`
- `* INHERIT Barcode Rule (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

### 🗃️ `barcode.nomenclature` — Barcode Nomenclature

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                 | Label                | Type        | Req | Store | Relation     |
| --------------------- | -------------------- | ----------- | --- | ----- | ------------ |
| `create_date`         | Created on           | `datetime`  |     | ✅    |              |
| `create_uid`          | Created by           | `many2one`  |     | ✅    | res.users    |
| `display_name`        | Display Name         | `char`      |     |       |              |
| `gs1_separator_fnc1`  | FNC1 Separator       | `char`      |     | ✅    |              |
| `id`                  | ID                   | `integer`   |     | ✅    |              |
| `is_gs1_nomenclature` | Is GS1 Nomenclature  | `boolean`   |     | ✅    |              |
| `name`                | Barcode Nomenclature | `char`      | ✅  | ✅    |              |
| `rule_ids`            | Rules                | `one2many`  |     | ✅    | barcode.rule |
| `upc_ean_conv`        | UPC/EAN Conversion   | `selection` | ✅  | ✅    |              |
| `write_date`          | Last Updated on      | `datetime`  |     | ✅    |              |
| `write_uid`           | Last Updated by      | `many2one`  |     | ✅    | res.users    |

**Access Rights:**

| Name                               | Group                     | Perms     |
| ---------------------------------- | ------------------------- | --------- |
| barcode.nomenclature.stock.user    | Inventory / User          | `R`       |
| barcode.nomenclature.stock.manager | Inventory / Administrator | `R/W/C/D` |
| barcode.nomenclature.manager       | Access Rights             | `R/W/C/D` |
| barcode.nomenclature.user          | Role / User               | `R`       |

### 🗃️ `barcode.rule` — Barcode Rule

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label                | Type        | Req | Store | Relation             |
| ------------------------- | -------------------- | ----------- | --- | ----- | -------------------- |
| `alias`                   | Alias                | `char`      | ✅  | ✅    |                      |
| `associated_uom_id`       | Associated Uom       | `many2one`  |     | ✅    | uom.uom              |
| `barcode_nomenclature_id` | Barcode Nomenclature | `many2one`  |     | ✅    | barcode.nomenclature |
| `create_date`             | Created on           | `datetime`  |     | ✅    |                      |
| `create_uid`              | Created by           | `many2one`  |     | ✅    | res.users            |
| `display_name`            | Display Name         | `char`      |     |       |                      |
| `encoding`                | Encoding             | `selection` | ✅  | ✅    |                      |
| `gs1_content_type`        | GS1 Content Type     | `selection` |     | ✅    |                      |
| `gs1_decimal_usage`       | Decimal              | `boolean`   |     | ✅    |                      |
| `id`                      | ID                   | `integer`   |     | ✅    |                      |
| `is_gs1_nomenclature`     | Is GS1 Nomenclature  | `boolean`   |     |       |                      |
| `name`                    | Rule Name            | `char`      | ✅  | ✅    |                      |
| `pattern`                 | Barcode Pattern      | `char`      | ✅  | ✅    |                      |
| `sequence`                | Sequence             | `integer`   |     | ✅    |                      |
| `type`                    | Type                 | `selection` | ✅  | ✅    |                      |
| `write_date`              | Last Updated on      | `datetime`  |     | ✅    |                      |
| `write_uid`               | Last Updated by      | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                       | Group                     | Perms     |
| -------------------------- | ------------------------- | --------- |
| barcode.rule.stock.user    | Inventory / User          | `R`       |
| barcode.rule.stock.manager | Inventory / Administrator | `R/W/C/D` |
| barcode.rule.manager       | Access Rights             | `R/W/C/D` |
| barcode.rule.user          | Role / User               | `R`       |

### 🗃️ `ir.http` — HTTP Routing

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |
