---
title: "Base import module"
module: "base_import_module"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Tools"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_____]
---

# 🟢 Base import module

> **Module:** `base_import_module` | **Version:** `19.0.1.0` **Category:** Tools |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[web]]

## 📖 Description

# Import a custom data module

This module allows authorized users to import a custom data module (.xml files and
static assests) for customization purpose.

## 🖥️ UI Components

### Menus

- `Apps/Import Module`

### Views

- `* INHERIT Apps (form)`
- `* INHERIT Apps Kanban Data Modules (kanban)`
- `* INHERIT Apps List Data Modules (list)`
- `* INHERIT Search Data Modules (search)`
- `base.import.module.form (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**5 model(s) defined by this module:**

### 🗃️ `ir.http` — HTTP Routing

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `base.import.module` — Import Module

> ✳️ Transient (Wizard)

Import Module

**Fields:**

| Field                  | Label                      | Type        | Req | Store | Relation  |
| ---------------------- | -------------------------- | ----------- | --- | ----- | --------- |
| `create_date`          | Created on                 | `datetime`  |     | ✅    |           |
| `create_uid`           | Created by                 | `many2one`  |     | ✅    | res.users |
| `display_name`         | Display Name               | `char`      |     |       |           |
| `force`                | Force init                 | `boolean`   |     | ✅    |           |
| `id`                   | ID                         | `integer`   |     | ✅    |           |
| `import_message`       | Import Message             | `text`      |     | ✅    |           |
| `module_file`          | Module .ZIP file           | `binary`    | ✅  | ✅    |           |
| `modules_dependencies` | Modules Dependencies       | `text`      |     | ✅    |           |
| `state`                | Status                     | `selection` |     | ✅    |           |
| `with_demo`            | Import demo data of module | `boolean`   |     | ✅    |           |
| `write_date`           | Last Updated on            | `datetime`  |     | ✅    |           |
| `write_uid`            | Last Updated by            | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                      | Group                | Perms   |
| ------------------------- | -------------------- | ------- |
| access.base.import.module | Role / Administrator | `R/W/C` |

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

### 🗃️ `base.module.uninstall` — Module Uninstall

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                 | Label                | Type        | Req | Store | Relation         |
| --------------------- | -------------------- | ----------- | --- | ----- | ---------------- |
| `create_date`         | Created on           | `datetime`  |     | ✅    |                  |
| `create_uid`          | Created by           | `many2one`  |     | ✅    | res.users        |
| `display_name`        | Display Name         | `char`      |     |       |                  |
| `id`                  | ID                   | `integer`   |     | ✅    |                  |
| `impacted_module_ids` | Impacted modules     | `many2many` |     |       | ir.module.module |
| `model_ids`           | Impacted data models | `many2many` |     |       | ir.model         |
| `module_ids`          | Module(s)            | `many2many` | ✅  | ✅    | ir.module.module |
| `show_all`            | Show All             | `boolean`   |     | ✅    |                  |
| `write_date`          | Last Updated on      | `datetime`  |     | ✅    |                  |
| `write_uid`           | Last Updated by      | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                         | Group                | Perms   |
| ---------------------------- | -------------------- | ------- |
| access.base.module.uninstall | Role / Administrator | `R/W/C` |

### 🗃️ `ir.ui.view` — View

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                             | Type        | Req | Store | Relation                |
| ----------------------------- | --------------------------------- | ----------- | --- | ----- | ----------------------- |
| `active`                      | Active                            | `boolean`   |     | ✅    |                         |
| `arch`                        | View Architecture                 | `text`      |     |       |                         |
| `arch_base`                   | Base View Architecture            | `text`      |     |       |                         |
| `arch_db`                     | Arch Blob                         | `text`      |     | ✅    |                         |
| `arch_fs`                     | Arch Filename                     | `char`      |     | ✅    |                         |
| `arch_prev`                   | Previous View Architecture        | `text`      |     | ✅    |                         |
| `arch_updated`                | Modified Architecture             | `boolean`   |     | ✅    |                         |
| `controller_page_ids`         | Controller Page                   | `one2many`  |     | ✅    | website.controller.page |
| `create_date`                 | Created on                        | `datetime`  |     | ✅    |                         |
| `create_uid`                  | Created by                        | `many2one`  |     | ✅    | res.users               |
| `customize_show`              | Show As Optional Inherit          | `boolean`   |     | ✅    |                         |
| `display_name`                | Display Name                      | `char`      |     |       |                         |
| `first_page_id`               | Website Page                      | `many2one`  |     |       | website.page            |
| `group_ids`                   | Groups                            | `many2many` |     | ✅    | res.groups              |
| `id`                          | ID                                | `integer`   |     | ✅    |                         |
| `inherit_children_ids`        | Views which inherit from this one | `one2many`  |     | ✅    | ir.ui.view              |
| `inherit_id`                  | Inherited View                    | `many2one`  |     | ✅    | ir.ui.view              |
| `invalid_locators`            | Invalid Locators                  | `json`      |     |       |                         |
| `is_seo_optimized`            | SEO optimized                     | `boolean`   |     | ✅    |                         |
| `key`                         | Key                               | `char`      |     | ✅    |                         |
| `mode`                        | View inheritance mode             | `selection` | ✅  | ✅    |                         |
| `model`                       | Model                             | `char`      |     | ✅    |                         |
| `model_data_id`               | Model Data                        | `many2one`  |     |       | ir.model.data           |
| `model_id`                    | Model of the view                 | `many2one`  |     |       | ir.model                |
| `name`                        | View Name                         | `char`      | ✅  | ✅    |                         |
| `page_ids`                    | Page                              | `one2many`  |     | ✅    | website.page            |
| `priority`                    | Sequence                          | `integer`   | ✅  | ✅    |                         |
| `seo_name`                    | Seo name                          | `char`      |     | ✅    |                         |
| `theme_template_id`           | Theme Template                    | `many2one`  |     | ✅    | theme.ir.ui.view        |
| `track`                       | Track                             | `boolean`   |     | ✅    |                         |
| `type`                        | View Type                         | `selection` |     | ✅    |                         |
| `visibility`                  | Visibility                        | `selection` |     | ✅    |                         |
| `visibility_password`         | Visibility Password               | `char`      |     | ✅    |                         |
| `visibility_password_display` | Visibility Password Display       | `char`      |     |       |                         |
| `warning_info`                | Warning information               | `html`      |     |       |                         |
| `website_id`                  | Website                           | `many2one`  |     | ✅    | website                 |
| `website_meta_description`    | Website meta description          | `text`      |     | ✅    |                         |
| `website_meta_keywords`       | Website meta keywords             | `char`      |     | ✅    |                         |
| `website_meta_og_img`         | Website opengraph image           | `char`      |     | ✅    |                         |
| `website_meta_title`          | Website meta title                | `char`      |     | ✅    |                         |
| `write_date`                  | Last Updated on                   | `datetime`  |     | ✅    |                         |
| `write_uid`                   | Last Updated by                   | `many2one`  |     | ✅    | res.users               |
| `xml_id`                      | External ID                       | `char`      |     |       |                         |

**Access Rights:**

| Name                                        | Group                         | Perms     |
| ------------------------------------------- | ----------------------------- | --------- |
| access_website_ir_ui_view_restricted_editor | Website / Restricted Editor   | `R`       |
| access_website_ir_ui_view_designer          | Website / Editor and Designer | `R/W/C/D` |
| ir_ui_view group_system                     | Role / Administrator          | `R/W/C/D` |
| ir_ui_view group_user                       | Everyone                      | `-`       |

**Record Rules:**

- **website_designer: Manage Website and qWeb view** (72) `R/W/C/D`
  - Domain: `[('type', '=', 'qweb')]`
- **website_designer: global view** (72) `R`
  - Domain: `[('type', '!=', 'qweb')]`
- **Administration Settings: Manage all views** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Website View Visibility Public** (11) `R`
  - Domain: `['|', ('type', '!=', 'qweb'), ('visibility', 'in', ('public', False))]`
- **Website View Visibility Connected** (10) `R`
  - Domain:
    `['|', ('type', '!=', 'qweb'), ('visibility', 'in', ('public', 'connected', False))]`
