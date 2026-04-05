---
title: "Sparse Fields"
module: "base_sparse_field"
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

# 🟢 Sparse Fields

> **Module:** `base_sparse_field` | **Version:** `19.0.1.0` **Category:** Technical |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[base]]

## 📖 Description

The purpose of this module is to implement "sparse" fields, i.e., fields that are mostly
null. This implementation circumvents the PostgreSQL limitation on the number of columns
in a table. The values of all sparse fields are stored in a "serialized" field in the
form of a JSON mapping.

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT ir.model form (form)`
- `* INHERIT ir.model.fields form (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

### 🗃️ `base` — Base

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.model.fields` — Fields

fields configuration for form builder

**Fields:**

| Field                      | Label                          | Type        | Req | Store | Relation                  |
| -------------------------- | ------------------------------ | ----------- | --- | ----- | ------------------------- |
| `column1`                  | Column 1                       | `char`      |     | ✅    |                           |
| `column2`                  | Column 2                       | `char`      |     | ✅    |                           |
| `company_dependent`        | Company Dependent              | `boolean`   |     | ✅    |                           |
| `compute`                  | Compute                        | `text`      |     | ✅    |                           |
| `copied`                   | Copied                         | `boolean`   |     | ✅    |                           |
| `create_date`              | Created on                     | `datetime`  |     | ✅    |                           |
| `create_uid`               | Created by                     | `many2one`  |     | ✅    | res.users                 |
| `currency_field`           | Currency field                 | `char`      |     | ✅    |                           |
| `depends`                  | Dependencies                   | `char`      |     | ✅    |                           |
| `display_name`             | Display Name                   | `char`      |     |       |                           |
| `domain`                   | Domain                         | `char`      |     | ✅    |                           |
| `field_description`        | Field Label                    | `char`      | ✅  | ✅    |                           |
| `group_expand`             | Expand Groups                  | `boolean`   |     | ✅    |                           |
| `groups`                   | Groups                         | `many2many` |     | ✅    | res.groups                |
| `help`                     | Field Help                     | `text`      |     | ✅    |                           |
| `id`                       | ID                             | `integer`   |     | ✅    |                           |
| `index`                    | Indexed                        | `boolean`   |     | ✅    |                           |
| `model`                    | Model Name                     | `char`      | ✅  | ✅    |                           |
| `model_id`                 | Model                          | `many2one`  | ✅  | ✅    | ir.model                  |
| `modules`                  | In Apps                        | `char`      |     |       |                           |
| `name`                     | Field Name                     | `char`      | ✅  | ✅    |                           |
| `on_delete`                | On Delete                      | `selection` |     | ✅    |                           |
| `readonly`                 | Readonly                       | `boolean`   |     | ✅    |                           |
| `related`                  | Related Field Definition       | `char`      |     | ✅    |                           |
| `related_field_id`         | Related Field                  | `many2one`  |     | ✅    | ir.model.fields           |
| `relation`                 | Related Model                  | `char`      |     | ✅    |                           |
| `relation_field`           | Relation Field                 | `char`      |     | ✅    |                           |
| `relation_field_id`        | Relation field                 | `many2one`  |     | ✅    | ir.model.fields           |
| `relation_table`           | Relation Table                 | `char`      |     | ✅    |                           |
| `required`                 | Required                       | `boolean`   |     | ✅    |                           |
| `sanitize`                 | Sanitize HTML                  | `boolean`   |     | ✅    |                           |
| `sanitize_attributes`      | Sanitize HTML Attributes       | `boolean`   |     | ✅    |                           |
| `sanitize_form`            | Sanitize HTML Form             | `boolean`   |     | ✅    |                           |
| `sanitize_overridable`     | Sanitize HTML overridable      | `boolean`   |     | ✅    |                           |
| `sanitize_style`           | Sanitize HTML Style            | `boolean`   |     | ✅    |                           |
| `sanitize_tags`            | Sanitize HTML Tags             | `boolean`   |     | ✅    |                           |
| `secure`                   | Secure                         | `boolean`   |     | ✅    |                           |
| `selectable`               | Selectable                     | `boolean`   |     | ✅    |                           |
| `selection`                | Selection Options (Deprecated) | `char`      |     |       |                           |
| `selection_ids`            | Selection Options              | `one2many`  |     | ✅    | ir.model.fields.selection |
| `serialization_field_id`   | Serialization Field            | `many2one`  |     | ✅    | ir.model.fields           |
| `size`                     | Size                           | `integer`   |     | ✅    |                           |
| `state`                    | Type                           | `selection` | ✅  | ✅    |                           |
| `store`                    | Stored                         | `boolean`   |     | ✅    |                           |
| `strip_classes`            | Strip Class Attribute          | `boolean`   |     | ✅    |                           |
| `strip_style`              | Strip Style Attribute          | `boolean`   |     | ✅    |                           |
| `tracking`                 | Enable Ordered Tracking        | `integer`   |     | ✅    |                           |
| `translate`                | Translatable                   | `selection` |     | ✅    |                           |
| `ttype`                    | Field Type                     | `selection` | ✅  | ✅    |                           |
| `website_form_blacklisted` | Blacklisted in web forms       | `boolean`   |     | ✅    |                           |
| `write_date`               | Last Updated on                | `datetime`  |     | ✅    |                           |
| `write_uid`                | Last Updated by                | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name                              | Group         | Perms     |
| --------------------------------- | ------------- | --------- |
| ir_model_fields group_erp_manager | Access Rights | `R/W/C/D` |
| ir_model_fields all               | Role / User   | `-`       |

### 🗃️ `sparse_fields.test` — Sparse fields Test

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type         | Req | Store | Relation    |
| -------------- | --------------- | ------------ | --- | ----- | ----------- |
| `boolean`      | Boolean         | `boolean`    |     |       |             |
| `char`         | Char            | `char`       |     |       |             |
| `create_date`  | Created on      | `datetime`   |     | ✅    |             |
| `create_uid`   | Created by      | `many2one`   |     | ✅    | res.users   |
| `data`         | Data            | `serialized` |     | ✅    |             |
| `display_name` | Display Name    | `char`       |     |       |             |
| `float`        | Float           | `float`      |     |       |             |
| `id`           | ID              | `integer`    |     | ✅    |             |
| `integer`      | Integer         | `integer`    |     |       |             |
| `partner`      | Partner         | `many2one`   |     |       | res.partner |
| `selection`    | Selection       | `selection`  |     |       |             |
| `write_date`   | Last Updated on | `datetime`   |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one`   |     | ✅    | res.users   |

**Access Rights:**

| Name                      | Group                | Perms   |
| ------------------------- | -------------------- | ------- |
| access.sparse_fields.test | Role / Administrator | `R/W/C` |
