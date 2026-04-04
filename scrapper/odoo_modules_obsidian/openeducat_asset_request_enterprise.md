---
title: "OpenEduCat Asset Requests"
module: "openeducat_asset_request_enterprise"
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

# 🟢 OpenEduCat Asset Requests

> **Module:** `openeducat_asset_request_enterprise` | **Version:** `19.0.1.0`
> **Category:** Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc
> **Website:** https://www.openeducat.org

## 🔗 Dependencies

[[account_asset_mgmt]] [[openeducat_core_enterprise]] [[openeducat_parent_enterprise]]

## 📖 Description

## OpenEduCat Online Asset Management

[![](/openeducat_asset_request_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module allows you to manage the asset requests easily. Admin can allocate assets to
students and faculties.

[Contact Us](https://www.openeducat.org/contactus/)

## Asset Request

Online Asset Management manages the asset requests of students and faculties. Admin can
Approve or Reject the request from students and faculties.

![](/openeducat_asset_request_enterprise/static/description/RequestAsset.png)

## Allocate Asset

![](/openeducat_asset_request_enterprise/static/description/Allocatasset.png)

Once request has been approved, admin can Allocate the assets as per the request.

## Return Asset

At last, the allocated assets must be returned.

![](/openeducat_asset_request_enterprise/static/description/ReturnAsset.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Accounting/Assets`
- `Accounting/Assets/Request Assets`
- `Accounting/Assets/Request Reasons`

### Views

- `* INHERIT Account Assets Form View (form)`
- `* INHERIT Account Assets List View (list)`
- `* INHERIT Portal layout : Request Assets (qweb)`
- `* INHERIT Show request assets (qweb)`
- `* INHERIT portal_home_inherit_asset (qweb)`
- `Asset Requests (qweb)`
- `Asset Requests (qweb)`
- `Assets (qweb)`
- `My asset (qweb)`
- `Request Asset List View (list)`
- `Request Asset List View (list)`
- `Request Asset Pivot View (pivot)`
- `Request Asset search View (search)`
- `Request Assets Form View (form)`
- `Request Reason Form View (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

### 🗃️ `account.asset.request` — Asset Requests

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation             |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------------- |
| `allocate_date`              | Allocate Date          | `date`      |     | ✅    |                      |
| `approve_date`               | Approve Date           | `date`      |     | ✅    |                      |
| `asset_id`                   | Assets                 | `many2one`  |     | ✅    | account.asset.asset  |
| `color`                      | Color Index            | `integer`   |     | ✅    |                      |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company          |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                      |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users            |
| `display_name`               | Display Name           | `char`      |     |       |                      |
| `faculty_id`                 | Faculty                | `many2one`  |     | ✅    | op.faculty           |
| `has_message`                | Has Message            | `boolean`   |     |       |                      |
| `id`                         | ID                     | `integer`   |     | ✅    |                      |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                      |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers       |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                      |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                      |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                      |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message         |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                      |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                      |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                      |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner          |
| `name`                       | Name                   | `char`      |     | ✅    |                      |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating        |
| `reject_date`                | Reject Date            | `date`      |     | ✅    |                      |
| `request_date`               | Request Date           | `date`      |     | ✅    |                      |
| `requested_asset`            | Requested Asset        | `char`      | ✅  | ✅    |                      |
| `request_for`                | Request By             | `selection` | ✅  | ✅    |                      |
| `request_reason_id`          | Reason                 | `many2one`  | ✅  | ✅    | asset.request.reason |
| `return_date`                | Return Date            | `date`      |     | ✅    |                      |
| `state`                      | Status                 | `selection` |     | ✅    |                      |
| `student_id`                 | Student                | `many2one`  |     | ✅    | op.student           |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message         |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                      |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                                 | Group           | Perms     |
| ------------------------------------ | --------------- | --------- |
| access_account_asset_request_manager | Asset / Manager | `R/W/C/D` |
| access_account_asset_request_faculty | Asset / User    | `R/W/C`   |

**Record Rules:**

- **Request Assets multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `account.asset.asset` — Asset/Revenue Recognition

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                        | Type        | Req | Store | Relation                        |
| -------------------------------- | ---------------------------- | ----------- | --- | ----- | ------------------------------- |
| `account_analytic_id`            | Analytic Account             | `many2one`  |     | ✅    | account.analytic.account        |
| `active`                         | Active                       | `boolean`   |     | ✅    |                                 |
| `assign_state`                   | Assigned                     | `boolean`   |     | ✅    |                                 |
| `category_id`                    | Category                     | `many2one`  | ✅  | ✅    | account.asset.category          |
| `code`                           | Reference                    | `char`      |     | ✅    |                                 |
| `company_id`                     | Company                      | `many2one`  | ✅  | ✅    | res.company                     |
| `create_date`                    | Created on                   | `datetime`  |     | ✅    |                                 |
| `create_uid`                     | Created by                   | `many2one`  |     | ✅    | res.users                       |
| `currency_id`                    | Currency                     | `many2one`  | ✅  | ✅    | res.currency                    |
| `date`                           | Date                         | `date`      | ✅  | ✅    |                                 |
| `date_first_depreciation`        | Depreciation Dates           | `selection` | ✅  | ✅    |                                 |
| `depreciation_line_ids`          | Depreciation Lines           | `one2many`  |     | ✅    | account.asset.depreciation.line |
| `display_name`                   | Display Name                 | `char`      |     |       |                                 |
| `entry_count`                    | # Asset Entries              | `integer`   |     |       |                                 |
| `first_depreciation_manual_date` | First Depreciation Date      | `date`      |     | ✅    |                                 |
| `has_message`                    | Has Message                  | `boolean`   |     |       |                                 |
| `id`                             | ID                           | `integer`   |     | ✅    |                                 |
| `invoice_id`                     | Invoice                      | `many2one`  |     | ✅    | account.move                    |
| `message_attachment_count`       | Attachment Count             | `integer`   |     |       |                                 |
| `message_follower_ids`           | Followers                    | `one2many`  |     | ✅    | mail.followers                  |
| `message_has_error`              | Message Delivery error       | `boolean`   |     |       |                                 |
| `message_has_error_counter`      | Number of errors             | `integer`   |     |       |                                 |
| `message_has_sms_error`          | SMS Delivery error           | `boolean`   |     |       |                                 |
| `message_ids`                    | Messages                     | `one2many`  |     | ✅    | mail.message                    |
| `message_is_follower`            | Is Follower                  | `boolean`   |     |       |                                 |
| `message_needaction`             | Action Needed                | `boolean`   |     |       |                                 |
| `message_needaction_counter`     | Number of Actions            | `integer`   |     |       |                                 |
| `message_partner_ids`            | Followers (Partners)         | `many2many` |     |       | res.partner                     |
| `method`                         | Computation Method           | `selection` | ✅  | ✅    |                                 |
| `method_end`                     | Ending Date                  | `date`      |     | ✅    |                                 |
| `method_number`                  | Number of Depreciations      | `integer`   |     | ✅    |                                 |
| `method_period`                  | Number of Months in a Period | `integer`   | ✅  | ✅    |                                 |
| `method_progress_factor`         | Degressive Factor            | `float`     |     | ✅    |                                 |
| `method_time`                    | Time Method                  | `selection` | ✅  | ✅    |                                 |
| `name`                           | Asset Name                   | `char`      | ✅  | ✅    |                                 |
| `note`                           | Note                         | `text`      |     | ✅    |                                 |
| `partner_id`                     | Partner                      | `many2one`  |     | ✅    | res.partner                     |
| `prorata`                        | Prorata Temporis             | `boolean`   |     | ✅    |                                 |
| `rating_ids`                     | Ratings                      | `one2many`  |     | ✅    | rating.rating                   |
| `salvage_value`                  | Salvage Value                | `float`     |     | ✅    |                                 |
| `state`                          | Status                       | `selection` | ✅  | ✅    |                                 |
| `type`                           | Type                         | `selection` | ✅  |       |                                 |
| `value`                          | Gross Value                  | `float`     | ✅  | ✅    |                                 |
| `value_residual`                 | Residual Value               | `float`     |     |       |                                 |
| `website_message_ids`            | Website Messages             | `one2many`  |     | ✅    | mail.message                    |
| `write_date`                     | Last Updated on              | `datetime`  |     | ✅    |                                 |
| `write_uid`                      | Last Updated by              | `many2one`  |     | ✅    | res.users                       |

**Access Rights:**

| Name                | Group                  | Perms     |
| ------------------- | ---------------------- | --------- |
| account.asset.asset | Accounting / Invoicing | `R/C`     |
| account.asset.asset | Accounting / Advisor   | `R/W/C/D` |
| account.asset.asset | Contact / Accountant   | `R`       |

**Record Rules:**

- **Account Asset multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),('company_id','child_of',[user.company_id.id])]         `

### 🗃️ `asset.request.reason` — Request Reason

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
| `name`         | Reason          | `char`     |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                                | Group           | Perms     |
| ----------------------------------- | --------------- | --------- |
| access_asset_request_reason_manager | Asset / Manager | `R/W/C/D` |
| access_asset_request_reason_user    | Asset / User    | `R/W/C`   |
