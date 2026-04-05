---
title: "OpenEduCat Alumni Job Enterprise"
module: "openeducat_alumni_job_enterprise"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "http://www.openeducat.org"
license: "Other proprietary"
category: "Education"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________, odoo/app]
---

# 🟢 OpenEduCat Alumni Job Enterprise

> **Module:** `openeducat_alumni_job_enterprise` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> http://www.openeducat.org

## 🔗 Dependencies

[[openeducat_alumni_enterprise]] [[openeducat_job_enterprise]]
[[openeducat_job_skill_bridge]]

## 📖 Description

## OpenEduCat Alumni job

### Can Create Job post

[![](/openeducat_alumni_job_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module allows alumni to create job post.

[Contact Us](https://www.openeducat.org/contactus/)

Alumni can create job post.

![](/openeducat_alumni_job_enterprise/static/description/post_job.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Alumni/Alumni Job`

### Views

- `* INHERIT Portal layout : Alumni Job (qweb)`
- `* INHERIT Show Alumni Job (qweb)`
- `Alumni Job (qweb)`
- `Alumni Job Details (qweb)`
- `Alumni Job List (qweb)`
- `Alumni Job List (qweb)`
- `Alumni Job List (qweb)`
- `Edit Job Post (qweb)`
- `Job Created (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

### 🗃️ `website.menu` — Website Menu

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                 | Label                | Type        | Req | Store | Relation                |
| --------------------- | -------------------- | ----------- | --- | ----- | ----------------------- |
| `child_id`            | Child Menus          | `one2many`  |     | ✅    | website.menu            |
| `controller_page_id`  | Related Model Page   | `many2one`  |     | ✅    | website.controller.page |
| `create_date`         | Created on           | `datetime`  |     | ✅    |                         |
| `create_uid`          | Created by           | `many2one`  |     | ✅    | res.users               |
| `display_name`        | Display Name         | `char`      |     |       |                         |
| `group_ids`           | Visible Groups       | `many2many` |     | ✅    | res.groups              |
| `id`                  | ID                   | `integer`   |     | ✅    |                         |
| `is_admission_parent` | Is admission Parent  | `boolean`   |     | ✅    |                         |
| `is_alumni_parent`    | Is alumni job Parent | `boolean`   |     | ✅    |                         |
| `is_mega_menu`        | Is Mega Menu         | `boolean`   |     |       |                         |
| `is_visible`          | Is Visible           | `boolean`   |     |       |                         |
| `mega_menu_classes`   | Mega Menu Classes    | `char`      |     | ✅    |                         |
| `mega_menu_content`   | Mega Menu Content    | `html`      |     | ✅    |                         |
| `name`                | Menu                 | `char`      | ✅  | ✅    |                         |
| `new_window`          | New Window           | `boolean`   |     | ✅    |                         |
| `page_id`             | Related Page         | `many2one`  |     | ✅    | website.page            |
| `parent_id`           | Parent Menu          | `many2one`  |     | ✅    | website.menu            |
| `parent_path`         | Parent Path          | `char`      |     | ✅    |                         |
| `sequence`            | Sequence             | `integer`   |     | ✅    |                         |
| `theme_template_id`   | Theme Template       | `many2one`  |     | ✅    | theme.website.menu      |
| `url`                 | Url                  | `char`      | ✅  | ✅    |                         |
| `website_id`          | Website              | `many2one`  |     | ✅    | website                 |
| `write_date`          | Last Updated on      | `datetime`  |     | ✅    |                         |
| `write_uid`           | Last Updated by      | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name                | Group                         | Perms     |
| ------------------- | ----------------------------- | --------- |
| Web Menu Manager    | Website / Editor and Designer | `R/W/C/D` |
| access_website_menu | Role / Portal                 | `R`       |
| access_website_menu | Role / Public                 | `R`       |
| access_website_menu | Role / User                   | `R`       |

**Record Rules:**

- **Website menu: group_ids** (Global) `R/W/C/D`
  - Domain:
    `['|', ('group_ids', '=', False), ('group_ids', 'in', user.all_group_ids.ids)]`
