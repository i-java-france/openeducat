---
title: "Website Mail"
module: "website_mail"
state: "installed"
version: "19.0.0.1"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Website"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/w______]
---

# 🟢 Website Mail

> **Module:** `website_mail` | **Version:** `19.0.0.1` **Category:** Website |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[website]] [[mail]]

## 📖 Description

Module holding mail improvements for website. It holds the follow widget.

## 🖥️ UI Components

### Menus

_none_

### Views

- `follow (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**2 model(s) defined by this module:**

### 🗃️ `ir.http` — HTTP Routing

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `publisher_warranty.contract` — Publisher Warranty Contract

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

**Access Rights:**

| Name                            | Group                | Perms     |
| ------------------------------- | -------------------- | --------- |
| publisher.warranty.contract.all | Role / Administrator | `R/W/C/D` |
