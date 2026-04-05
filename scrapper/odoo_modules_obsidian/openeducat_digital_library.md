---
title: "OpenEduCat Digital Library"
module: "openeducat_digital_library"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Education"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________, odoo/app]
---

# 🟢 OpenEduCat Digital Library

> **Module:** `openeducat_digital_library` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[base]] [[website]] [[portal]] [[openeducat_core_enterprise]]

## 📖 Description

## OpenEduCat Digital Library

[![](/openeducat_digital_library/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This Module Adds The Feature Of Digital Library To Read Books In OpenEduCat. You Can
Upload Books & Audiobooks And Publish It.

[Contact Us](https://www.openeducat.org/contactus/)

## Category

### Create Different Categories And Add Material To Category.Add Parent Category To Category

![](/openeducat_digital_library/static/description/category_view.png)

## Material

### Upload Material For Library And Publish It Online. Set Your Publish Policy For Your Material When You Want To Publish. Add Different Types Of Material.Add Publisher, Author, Edition, Source, ISBN Code, Description

![](/openeducat_digital_library/static/description/material_view.png)

## Material Types

![](/openeducat_digital_library/static/description/pdf_material.png)

#### **PDF**

Upload Book As PDF. User Can Read A PDF As User Reading A Book.

![](/openeducat_digital_library/static/description/audio_material.png)

#### **Audiobook**

Upload Material of Audiobook And You Can Publish It On Website.User Can Listen To
Audiobook From Website.

## Enrollment

### Get Details Of Users Who Enrolled To Read Book Or Listen AudioBooks.Enrollment Date, Last Access Date.

![](/openeducat_digital_library/static/description/enrollment_view.png)

## Home Page

### Home Page That Display Material Which Are Published Online. Navigate By Categories, Search For The Particular Material By Search.

![](/openeducat_digital_library/static/description/home_page.png)

## Material Detail Page

### Material Detail Page That Display All The Details Of Material Like Publisher, Author, Category, Edition, Reviews.

![](/openeducat_digital_library/static/description/material_detail_view.png)

## PDF Flip-Book

### Digital Library Provides Feature To Read Book As Real Time Flip Book.

![](/openeducat_digital_library/static/description/pdf-flipbook.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Digital Library`
- `Digital Library/Category`
- `Digital Library/Enrollment`
- `Digital Library/Material`

### Views

- `* INHERIT Shoe Digital Library (qweb)`
- `Digital Library (qweb)`
- `Library (qweb)`
- `Library Category (qweb)`
- `My Library (qweb)`
- `iframe_html_div (qweb)`
- `op.digital.library.category.form (form)`
- `op.digital.library.category.list (list)`
- `op.digital.library.enrollment.form (form)`
- `op.digital.library.enrollment.list (list)`
- `op.digital.library.material.form (form)`
- `op.digital.library.material.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**7 model(s) defined by this module:**

### 🗃️ `op.digital.library.author` — Author Of Material

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
| `name`         | Name            | `char`     |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                                               | Group                     | Perms     |
| -------------------------------------------------- | ------------------------- | --------- |
| access_op_digital_library_author_back_office_admin | Digital Library / Manager | `R/W/C/D` |
| access_op_digital_library_author_faculty           | Digital Library / User    | `R/W/C`   |
| access_op_digital_library_author_portal            | Role / Portal             | `R`       |
| access_op_digital_library_author_public            | Role / Public             | `R`       |
| access_op_digital_library_author_user              | Role / User               | `R`       |

### 🗃️ `op.digital.library.publisher` — Author Of Material

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
| `name`         | Name            | `char`     |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                                                  | Group                     | Perms     |
| ----------------------------------------------------- | ------------------------- | --------- |
| access_op_digital_library_publisher_back_office_admin | Digital Library / Manager | `R/W/C/D` |
| access_op_digital_library_publisher_faculty           | Digital Library / User    | `R/W/C`   |
| access_op_digital_library_publisher_portal            | Role / Portal             | `R`       |
| access_op_digital_library_publisher_public            | Role / Public             | `R`       |
| access_op_digital_library_publisher_user              | Role / User               | `R`       |

### 🗃️ `op.digital.library.category` — Category Of Material

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label           | Type        | Req | Store | Relation                    |
| ---------------- | --------------- | ----------- | --- | ----- | --------------------------- |
| `company_id`     | Company         | `many2one`  |     | ✅    | res.company                 |
| `create_date`    | Created on      | `datetime`  |     | ✅    |                             |
| `create_uid`     | Created by      | `many2one`  |     | ✅    | res.users                   |
| `display_name`   | Display Name    | `char`      |     | ✅    |                             |
| `id`             | ID              | `integer`   |     | ✅    |                             |
| `material_count` | Total Material  | `integer`   |     |       |                             |
| `material_ids`   | Material        | `many2many` |     | ✅    | op.digital.library.material |
| `name`           | Name            | `char`      | ✅  | ✅    |                             |
| `parent_id`      | Parent Category | `many2one`  |     | ✅    | op.digital.library.category |
| `write_date`     | Last Updated on | `datetime`  |     | ✅    |                             |
| `write_uid`      | Last Updated by | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                                               | Group                     | Perms     |
| -------------------------------------------------- | ------------------------- | --------- |
| name_op_digital_library_category_back_office_admin | Digital Library / Manager | `R/W/C/D` |
| name_op_digital_library_category_faculty           | Digital Library / User    | `R/W/C`   |
| name_op_digital_library_category_portal            | Role / Portal             | `R`       |
| name_op_digital_library_category_public            | Role / Public             | `R`       |
| name_op_digital_library_category_user              | Role / User               | `R`       |

**Record Rules:**

- **Library Category multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|','|',('company_id','=',False),('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids),('company_id',         'in', company_ids)]     `

### 🗃️ `op.digital.library.enrollment` — Digital Library Enrollment

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label           | Type        | Req | Store | Relation                    |
| ----------------- | --------------- | ----------- | --- | ----- | --------------------------- |
| `active`          | Active          | `boolean`   |     | ✅    |                             |
| `category_ids`    | Categories      | `many2many` |     |       | op.digital.library.category |
| `company_id`      | Company         | `many2one`  |     | ✅    | res.company                 |
| `create_date`     | Created on      | `datetime`  |     | ✅    |                             |
| `create_uid`      | Created by      | `many2one`  |     | ✅    | res.users                   |
| `display_name`    | Display Name    | `char`      |     |       |                             |
| `enrollment_date` | Enrollment Date | `datetime`  | ✅  | ✅    |                             |
| `id`              | ID              | `integer`   |     | ✅    |                             |
| `last_access`     | Last Access     | `datetime`  |     | ✅    |                             |
| `material_id`     | Material        | `many2one`  |     | ✅    | op.digital.library.material |
| `state`           | State           | `selection` |     | ✅    |                             |
| `user_id`         | User            | `many2one`  | ✅  | ✅    | res.users                   |
| `write_date`      | Last Updated on | `datetime`  |     | ✅    |                             |
| `write_uid`       | Last Updated by | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                                                   | Group                     | Perms |
| ------------------------------------------------------ | ------------------------- | ----- |
| access_op_digital_library_enrollment_back_office_admin | Digital Library / Manager | `R`   |
| access_op_digital_library_enrollment_faculty           | Digital Library / User    | `R`   |
| access_op_digital_library_enrollment_portal            | Role / Portal             | `R`   |
| access_op_digital_library_enrollment_public            | Role / Public             | `R`   |
| access_op_digital_library_enrollment_user              | Role / User               | `R`   |

**Record Rules:**

- **Digital Library Enrollment multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|','|',('company_id','=',False),('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids),('company_id',         'in', company_ids)]     `

### 🗃️ `op.digital.library.material.review` — Digital Library Material Review

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation                    |
| -------------- | --------------- | ---------- | --- | ----- | --------------------------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |                             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users                   |
| `display_name` | Display Name    | `char`     |     |       |                             |
| `email`        | Email           | `char`     |     | ✅    |                             |
| `id`           | ID              | `integer`  |     | ✅    |                             |
| `material_id`  | Material        | `many2one` |     | ✅    | op.digital.library.material |
| `name`         | Name            | `char`     |     | ✅    |                             |
| `rating`       | Rating          | `float`    |     | ✅    |                             |
| `review`       | Review          | `char`     |     | ✅    |                             |
| `user_id`      | User            | `many2one` |     | ✅    | res.users                   |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users                   |

**Access Rights:**

| Name                                                        | Group                     | Perms     |
| ----------------------------------------------------------- | ------------------------- | --------- |
| access_op_digital_library_material_review_back_office_admin | Digital Library / Manager | `R/W/C/D` |
| access_op_digital_library_material_review_faculty           | Digital Library / User    | `R/W/C`   |
| access_op_digital_library_material_review_portal            | Role / Portal             | `R`       |
| access_op_digital_library_material_review_public            | Role / Public             | `R`       |
| access_op_digital_library_material_review_user              | Role / User               | `R`       |

### 🗃️ `op.digital.library.material` — Material For Digital Library

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label           | Type        | Req | Store | Relation                           |
| -------------------------- | --------------- | ----------- | --- | ----- | ---------------------------------- |
| `author_ids`               | Author(s)       | `many2many` | ✅  | ✅    | op.digital.library.author          |
| `company_id`               | Company         | `many2one`  |     | ✅    | res.company                        |
| `create_date`              | Created on      | `datetime`  |     | ✅    |                                    |
| `create_uid`               | Created by      | `many2one`  |     | ✅    | res.users                          |
| `display_name`             | Display Name    | `char`      |     |       |                                    |
| `id`                       | ID              | `integer`   |     | ✅    |                                    |
| `isbn_code`                | ISBN Code       | `char`      |     | ✅    |                                    |
| `language_id`              | Language        | `many2one`  |     | ✅    | res.lang                           |
| `material_cover`           | Cover Image     | `binary`    |     | ✅    |                                    |
| `material_data`            | Upload Here     | `binary`    | ✅  | ✅    |                                    |
| `material_description`     | Description     | `html`      |     | ✅    |                                    |
| `material_edition`         | Edition         | `char`      | ✅  | ✅    |                                    |
| `material_enrollment_line` | Enrollments     | `one2many`  |     | ✅    | op.digital.library.enrollment      |
| `material_review_line`     | Reviews         | `one2many`  |     | ✅    | op.digital.library.material.review |
| `material_source`          | Source          | `char`      | ✅  | ✅    |                                    |
| `material_tags`            | Tag(s)          | `many2many` |     | ✅    | op.digital.library.material.tag    |
| `material_type`            | Material Type   | `selection` | ✅  | ✅    |                                    |
| `name`                     | Name            | `char`      | ✅  | ✅    |                                    |
| `publisher_ids`            | Publisher(s)    | `many2many` | ✅  | ✅    | op.digital.library.publisher       |
| `publish_online`           | Publish Online  | `boolean`   |     | ✅    |                                    |
| `rating`                   | Rating          | `float`     |     |       |                                    |
| `total_reviews`            | Total Review    | `integer`   |     |       |                                    |
| `write_date`               | Last Updated on | `datetime`  |     | ✅    |                                    |
| `write_uid`                | Last Updated by | `many2one`  |     | ✅    | res.users                          |

**Access Rights:**

| Name                                               | Group                     | Perms     |
| -------------------------------------------------- | ------------------------- | --------- |
| name_op_digital_library_material_back_office_admin | Digital Library / Manager | `R/W/C/D` |
| name_op_digital_library_material_faculty           | Digital Library / User    | `R/W/C`   |
| name_op_digital_library_material_portal            | Role / Portal             | `R`       |
| name_op_digital_library_material_public            | Role / Public             | `R`       |
| name_op_digital_library_material_user              | Role / User               | `R`       |

**Record Rules:**

- **Library Material multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|','|',('company_id','=',False),('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids),('company_id',         'in', company_ids)]     `

### 🗃️ `op.digital.library.material.tag` — Tags For Material

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
| `name`         | Name            | `char`     |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                                                     | Group                     | Perms     |
| -------------------------------------------------------- | ------------------------- | --------- |
| access_op_digital_library_material_tag_back_office_admin | Digital Library / Manager | `R/W/C/D` |
| access_op_digital_library_material_tag_faculty           | Digital Library / User    | `R/W/C`   |
| access_op_digital_library_material_tag_portal            | Role / Portal             | `R`       |
| access_op_digital_library_material_tag_public            | Role / Public             | `R`       |
| access_op_digital_library_material_tag_user              | Role / User               | `R`       |
