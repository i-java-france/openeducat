---
title: "Base - Module Install Request"
module: "base_install_request"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Technical"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 Base - Module Install Request

> **Module:** `base_install_request` | **Version:** `19.0.1.0` **Category:** Technical |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[mail]]

## 📖 Description

# Allow internal users requesting a module installation

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT ir.module.module.view.kanban.inherit.mail (kanban)`
- `base.module.install.request.view.form (form)`
- `base.module.install.review.view.form (form)`
- `base_install_request.base_module_install_review_description (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

### 🗃️ `ir.module.module` — Module

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                             | Label                           | Type        | Req | Store | Relation                    |
| --------------------------------- | ------------------------------- | ----------- | --- | ----- | --------------------------- |
| `account_templates`               | Account Templates               | `binary`    |     |       |                             |
| `application`                     | Application                     | `boolean`   |     | ✅    |                             |
| `author`                          | Author                          | `char`      |     | ✅    |                             |
| `auto_install`                    | Automatic Installation          | `boolean`   |     | ✅    |                             |
| `category_id`                     | Category                        | `many2one`  |     | ✅    | ir.module.category          |
| `contributors`                    | Contributors                    | `text`      |     | ✅    |                             |
| `country_ids`                     | Country                         | `many2many` |     | ✅    | res.country                 |
| `create_date`                     | Created on                      | `datetime`  |     | ✅    |                             |
| `create_uid`                      | Created by                      | `many2one`  |     | ✅    | res.users                   |
| `demo`                            | Demo Data                       | `boolean`   |     | ✅    |                             |
| `dependencies_id`                 | Dependencies                    | `one2many`  |     | ✅    | ir.module.module.dependency |
| `description`                     | Description                     | `text`      |     | ✅    |                             |
| `description_html`                | Description HTML                | `html`      |     |       |                             |
| `display_name`                    | Display Name                    | `char`      |     |       |                             |
| `exclusion_ids`                   | Exclusions                      | `one2many`  |     | ✅    | ir.module.module.exclusion  |
| `has_iap`                         | Has Iap                         | `boolean`   |     |       |                             |
| `icon`                            | Icon URL                        | `char`      |     | ✅    |                             |
| `icon_flag`                       | Flag                            | `char`      |     |       |                             |
| `icon_image`                      | Icon                            | `binary`    |     |       |                             |
| `id`                              | ID                              | `integer`   |     | ✅    |                             |
| `image_ids`                       | Screenshots                     | `one2many`  |     | ✅    | ir.attachment               |
| `imported`                        | Imported Module                 | `boolean`   |     | ✅    |                             |
| `installed_version`               | Latest Version                  | `char`      |     |       |                             |
| `is_installed_on_current_website` | Is Installed On Current Website | `boolean`   |     |       |                             |
| `latest_version`                  | Installed Version               | `char`      |     | ✅    |                             |
| `license`                         | License                         | `selection` |     | ✅    |                             |
| `maintainer`                      | Maintainer                      | `char`      |     | ✅    |                             |
| `menus_by_module`                 | Menus                           | `text`      |     | ✅    |                             |
| `module_type`                     | Module Type                     | `selection` |     | ✅    |                             |
| `name`                            | Technical Name                  | `char`      | ✅  | ✅    |                             |
| `published_version`               | Published Version               | `char`      |     | ✅    |                             |
| `reports_by_module`               | Reports                         | `text`      |     | ✅    |                             |
| `sequence`                        | Sequence                        | `integer`   |     | ✅    |                             |
| `shortdesc`                       | Module Name                     | `char`      |     | ✅    |                             |
| `state`                           | Status                          | `selection` |     | ✅    |                             |
| `summary`                         | Summary                         | `char`      |     | ✅    |                             |
| `to_buy`                          | Odoo Enterprise Module          | `boolean`   |     | ✅    |                             |
| `url`                             | URL                             | `char`      |     | ✅    |                             |
| `views_by_module`                 | Views                           | `text`      |     | ✅    |                             |
| `website`                         | Website                         | `char`      |     | ✅    |                             |
| `write_date`                      | Last Updated on                 | `datetime`  |     | ✅    |                             |
| `write_uid`                       | Last Updated by                 | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                        | Group                | Perms     |
| --------------------------- | -------------------- | --------- |
| ir_module_module group_user | Role / Administrator | `R/W/C/D` |
| ir_module_module group_user | Role / User          | `R`       |

### 🗃️ `base.module.install.request` — Module Activation Request

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation         |
| -------------- | --------------- | ----------- | --- | ----- | ---------------- |
| `body_html`    | Body            | `html`      |     | ✅    |                  |
| `create_date`  | Created on      | `datetime`  |     | ✅    |                  |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users        |
| `display_name` | Display Name    | `char`      |     |       |                  |
| `id`           | ID              | `integer`   |     | ✅    |                  |
| `module_id`    | Module          | `many2one`  | ✅  | ✅    | ir.module.module |
| `user_id`      | User            | `many2one`  | ✅  | ✅    | res.users        |
| `user_ids`     | Send to:        | `many2many` |     |       | res.users        |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |                  |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                               | Group       | Perms   |
| ---------------------------------- | ----------- | ------- |
| access_base_module_install_request | Role / User | `R/W/C` |

### 🗃️ `base.module.install.review` — Module Activation Review

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                 | Label               | Type        | Req | Store | Relation         |
| --------------------- | ------------------- | ----------- | --- | ----- | ---------------- |
| `create_date`         | Created on          | `datetime`  |     | ✅    |                  |
| `create_uid`          | Created by          | `many2one`  |     | ✅    | res.users        |
| `display_name`        | Display Name        | `char`      |     |       |                  |
| `id`                  | ID                  | `integer`   |     | ✅    |                  |
| `module_id`           | Module              | `many2one`  | ✅  | ✅    | ir.module.module |
| `module_ids`          | Depending Apps      | `many2many` |     |       | ir.module.module |
| `modules_description` | Modules Description | `html`      |     |       |                  |
| `write_date`          | Last Updated on     | `datetime`  |     | ✅    |                  |
| `write_uid`           | Last Updated by     | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                              | Group                | Perms   |
| --------------------------------- | -------------------- | ------- |
| access_base_module_install_review | Role / Administrator | `R/W/C` |
