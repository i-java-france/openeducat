---
title: "Dashboards"
module: "board"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Productivity"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/____________]
---

# 🟢 Dashboards

> **Module:** `board` | **Version:** `19.0.1.0` **Category:** Productivity |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[spreadsheet_dashboard]]

## 📖 Description

# Lets the user create a custom dashboard.

Allows users to create custom dashboard.

## 🖥️ UI Components

### Menus

- `Dashboards/My Dashboard`

### Views

- `My Dashboard (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

### 🗃️ `board.board` — Board

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

**Access Rights:**

| Name        | Group       | Perms |
| ----------- | ----------- | ----- |
| board.board | Role / User | `R`   |
