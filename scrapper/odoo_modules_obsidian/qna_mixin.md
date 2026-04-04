---
title: "QNA Mixin"
module: "qna_mixin"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "QNA"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/___]
---

# 🟢 QNA Mixin

> **Module:** `qna_mixin` | **Version:** `19.0.1.0` **Category:** QNA | **License:**
> `Other proprietary` **Author:** OpenEduCat Inc **Website:** https://www.openeducat.org

## 🔗 Dependencies

[[web]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `question.answer.form (form)`
- `question.answer.tree (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

### 🗃️ `qna.mixin` — QNA Mixin

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type       | Req | Store | Relation        |
| -------------- | ------------ | ---------- | --- | ----- | --------------- |
| `display_name` | Display Name | `char`     |     |       |                 |
| `id`           | ID           | `integer`  |     | ✅    |                 |
| `question_ids` | Questions    | `one2many` |     | ✅    | question.single |

### 🗃️ `question.answer` — Question Answer

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Answer          | `char`     |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                   | Group       | Perms     |
| ---------------------- | ----------- | --------- |
| access_question_answer | Role / User | `R/W/C/D` |

### 🗃️ `question.single` — Question Single

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label                  | Type        | Req | Store | Relation        |
| ----------------- | ---------------------- | ----------- | --- | ----- | --------------- |
| `answer_ids`      | Answer                 | `many2many` |     | ✅    | question.answer |
| `create_date`     | Created on             | `datetime`  |     | ✅    |                 |
| `create_uid`      | Created by             | `many2one`  |     | ✅    | res.users       |
| `display_name`    | Display Name           | `char`      |     |       |                 |
| `id`              | ID                     | `integer`   |     | ✅    |                 |
| `name`            | Question               | `char`      | ✅  | ✅    |                 |
| `placeholder`     | Placeholder            | `char`      |     | ✅    |                 |
| `qna_id`          | Document               | `integer`   | ✅  | ✅    |                 |
| `question_type`   | Question Type          | `selection` |     | ✅    |                 |
| `required_answer` | Answer Required        | `boolean`   |     | ✅    |                 |
| `res_model`       | Document Model         | `char`      |     | ✅    |                 |
| `res_model_id`    | Related Document Model | `many2one`  |     | ✅    | ir.model        |
| `write_date`      | Last Updated on        | `datetime`  |     | ✅    |                 |
| `write_uid`       | Last Updated by        | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                   | Group       | Perms     |
| ---------------------- | ----------- | --------- |
| access_question_single | Role / User | `R/W/C/D` |
