---
title: "Web PWA"
module: "web_pwa"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: ""
license: "Other proprietary"
category: "Web"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/w__]
---

# 🟢 Web PWA

> **Module:** `web_pwa` | **Version:** `19.0.1.0` **Category:** Web | **License:**
> `Other proprietary` **Author:** OpenEduCat Inc **Website:** _N/A_

## 🔗 Dependencies

[[web]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT Scoped App (qweb)`
- `* INHERIT Web Bootstrap (qweb)`
- `* INHERIT Web layout PWA (qweb)`
- `* INHERIT res.config.settings.view.form.inherit.pwa (form)`
- `PWA service worker (qweb)`
- `PWA service worker activate (qweb)`
- `PWA service worker fetch (qweb)`
- `PWA service worker install (qweb)`
- `PWA service worker settings (qweb)`
- `pwa.config.form (form)`
- `pwa.config.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

### 🗃️ `pwa.config` — Progressive Web App Configuration

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label            | Type        | Req | Store | Relation    |
| ---------------------- | ---------------- | ----------- | --- | ----- | ----------- |
| `active`               | Active           | `boolean`   |     | ✅    |             |
| `create_date`          | Created on       | `datetime`  |     | ✅    |             |
| `create_uid`           | Created by       | `many2one`  |     | ✅    | res.users   |
| `display_name`         | Display Name     | `char`      |     |       |             |
| `id`                   | ID               | `integer`   |     | ✅    |             |
| `pwa_background_color` | Background Color | `char`      |     | ✅    |             |
| `pwa_company_id`       | Company          | `many2one`  |     | ✅    | res.company |
| `pwa_display`          | Display          | `selection` |     | ✅    |             |
| `pwa_icon_128`         | Icon (128x128)   | `binary`    |     | ✅    |             |
| `pwa_icon_192`         | Icon (192x192)   | `binary`    |     | ✅    |             |
| `pwa_icon_512`         | Icon (512x512)   | `binary`    |     | ✅    |             |
| `pwa_name`             | Name             | `char`      |     | ✅    |             |
| `pwa_scope`            | Scope            | `char`      |     | ✅    |             |
| `pwa_short_name`       | Short Name       | `char`      |     | ✅    |             |
| `pwa_theme_color`      | Theme Color      | `char`      |     | ✅    |             |
| `write_date`           | Last Updated on  | `datetime`  |     | ✅    |             |
| `write_uid`            | Last Updated by  | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name              | Group       | Perms     |
| ----------------- | ----------- | --------- |
| access_pwa_config | Role / User | `R/W/C/D` |
