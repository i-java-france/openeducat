---
title: "Approval All in One"
module: "multi_approval"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Tool"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/____, odoo/app]
---

# 🟢 Approval All in One

> **Module:** `multi_approval` | **Version:** `19.0.1.0` **Category:** Tool |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[base]] [[product]] [[mail]] [[base_automation]] [[sale]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `Approvals`
- `Approvals/Activity Types`
- `Approvals/Approval Types`
- `Approvals/Approvals`
- `Approvals/Approvals/All Approval`
- `Approvals/Approvals/My Request`
- `Approvals/Approvals/To Review`

### Views

- `Approval Product Line (list)`
- `Approval Request (form)`
- `Approval Request (list)`
- `Approval Request search (search)`
- `Approval Types (form)`
- `Approval Types (kanban)`
- `Approval Types (list)`
- `New Approval Request (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**6 model(s) defined by this module:**

### 🗃️ `multi.request` — Approval Request

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation            |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------- |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event      |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                     |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                     |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                     |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity       |
| `activity_state`                | Activity State                | `selection` |     |       |                     |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                     |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                     |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type  |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users           |
| `amount`                        | Amount                        | `float`     |     | ✅    |                     |
| `amount_opt`                    | Amount Opt                    | `selection` |     | ✅    |                     |
| `approval_type_id`              | Approval Type                 | `many2one`  |     | ✅    | multi.approval.type |
| `attachment_number`             | Number of Attachments         | `integer`   |     |       |                     |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company         |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                     |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users           |
| `date`                          | Request Date                  | `datetime`  |     | ✅    |                     |
| `date_confirmed`                | Date Confirm                  | `datetime`  |     | ✅    |                     |
| `date_end`                      | Date Start                    | `datetime`  |     | ✅    |                     |
| `date_opt`                      | Date Opt                      | `selection` |     | ✅    |                     |
| `date_start`                    | Date End                      | `datetime`  |     | ✅    |                     |
| `display_name`                  | Display Name                  | `char`      |     |       |                     |
| `document_opt`                  | Document Opt                  | `selection` |     | ✅    |                     |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                     |
| `id`                            | ID                            | `integer`   |     | ✅    |                     |
| `line_ids`                      | Approvers                     | `one2many`  |     | ✅    | multi.request.line  |
| `location`                      | Location                      | `char`      |     | ✅    |                     |
| `location_opt`                  | Location Opt                  | `selection` |     | ✅    |                     |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                     |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers      |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                     |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                     |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                     |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message        |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                     |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                     |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                     |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner         |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                     |
| `name`                          | Name                          | `char`      | ✅  | ✅    |                     |
| `partner_id`                    | Contact                       | `many2one`  |     | ✅    | res.partner         |
| `partner_opt`                   | Partner Opt                   | `selection` |     | ✅    |                     |
| `payment_opt`                   | Payment Opt                   | `selection` |     | ✅    |                     |
| `period_opt`                    | Period Opt                    | `selection` |     | ✅    |                     |
| `product_line_ids`              | Products                      | `one2many`  |     | ✅    | multi.product.line  |
| `product_opt`                   | Product Opt                   | `selection` |     | ✅    |                     |
| `quantity`                      | Quantity                      | `integer`   |     | ✅    |                     |
| `quantity_opt`                  | Quantity Opt                  | `selection` |     | ✅    |                     |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating       |
| `reason`                        | Description                   | `html`      |     | ✅    |                     |
| `reference`                     | Reference                     | `char`      |     | ✅    |                     |
| `reference_opt`                 | Reference Opt                 | `selection` |     | ✅    |                     |
| `request_status`                | Request Status                | `selection` |     | ✅    |                     |
| `source_document`               | Source Document               | `reference` |     | ✅    |                     |
| `user_id`                       | Request by                    | `many2one`  |     | ✅    | res.users           |
| `user_status`                   | User Status                   | `selection` |     | ✅    |                     |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message        |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                     |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                 | Group         | Perms     |
| -------------------- | ------------- | --------- |
| access_multi_request | Access Rights | `R/W/C/D` |
| access_multi_request | Role / User   | `R/W/C`   |

### 🗃️ `multi.model.request` — ApprovalModelRequest

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field              | Label           | Type        | Req | Store | Relation            |
| ------------------ | --------------- | ----------- | --- | ----- | ------------------- |
| `approval_type_id` | Approval Type   | `many2one`  |     | ✅    | multi.approval.type |
| `create_date`      | Created on      | `datetime`  |     | ✅    |                     |
| `create_uid`       | Created by      | `many2one`  |     | ✅    | res.users           |
| `description`      | Description     | `html`      |     | ✅    |                     |
| `display_name`     | Display Name    | `char`      |     |       |                     |
| `id`               | ID              | `integer`   |     | ✅    |                     |
| `name`             | Name            | `char`      |     | ✅    |                     |
| `priority`         | Priority        | `integer`   |     | ✅    |                     |
| `request_date`     | Requested Date  | `datetime`  |     | ✅    |                     |
| `source_document`  | Source Document | `reference` |     | ✅    |                     |
| `user_id`          | User            | `many2one`  |     | ✅    | res.users           |
| `write_date`       | Last Updated on | `datetime`  |     | ✅    |                     |
| `write_uid`        | Last Updated by | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                       | Group         | Perms     |
| -------------------------- | ------------- | --------- |
| access_multi_model_request | Access Rights | `R/W/C/D` |
| access_multi_model_request | Role / User   | `R/W/C`   |

### 🗃️ `multi.product.line` — ApprovalProductLine

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label               | Type       | Req | Store | Relation        |
| ---------------- | ------------------- | ---------- | --- | ----- | --------------- |
| `create_date`    | Created on          | `datetime` |     | ✅    |                 |
| `create_uid`     | Created by          | `many2one` |     | ✅    | res.users       |
| `display_name`   | Display Name        | `char`     |     |       |                 |
| `id`             | ID                  | `integer`  |     | ✅    |                 |
| `line_product`   | ApprovalProductLine | `many2one` |     | ✅    | multi.request   |
| `product_id`     | Product             | `many2one` |     | ✅    | product.product |
| `product_uom_id` | Unit Of Measure     | `many2one` |     |       | uom.uom         |
| `quantity`       | Quantity            | `integer`  |     | ✅    |                 |
| `write_date`     | Last Updated on     | `datetime` |     | ✅    |                 |
| `write_uid`      | Last Updated by     | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                      | Group         | Perms     |
| ------------------------- | ------------- | --------- |
| access_multi_product_line | Access Rights | `R/W/C/D` |
| access_multi_product_line | Role / User   | `R/W/C`   |

### 🗃️ `multi.request.line` — ApprovalRequestLine

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field              | Label               | Type        | Req | Store | Relation      |
| ------------------ | ------------------- | ----------- | --- | ----- | ------------- |
| `approval_minimum` | Approval Minimum    | `integer`   |     | ✅    |               |
| `approve_tmpl_id`  | Approve Template    | `many2one`  |     | ✅    | mail.template |
| `create_date`      | Created on          | `datetime`  |     | ✅    |               |
| `create_uid`       | Created by          | `many2one`  |     | ✅    | res.users     |
| `display_name`     | Display Name        | `char`      |     |       |               |
| `id`               | ID                  | `integer`   |     | ✅    |               |
| `line`             | ApprovalRequestLine | `many2one`  |     | ✅    | multi.request |
| `reject_tmpl_id`   | Reject Template     | `many2one`  |     | ✅    | mail.template |
| `require_opt`      | Type of Approval    | `selection` |     | ✅    |               |
| `status`           | Status              | `selection` |     | ✅    |               |
| `user_id`          | User                | `many2one`  |     | ✅    | res.users     |
| `write_date`       | Last Updated on     | `datetime`  |     | ✅    |               |
| `write_uid`        | Last Updated by     | `many2one`  |     | ✅    | res.users     |

**Access Rights:**

| Name                      | Group         | Perms     |
| ------------------------- | ------------- | --------- |
| access_multi_request_line | Access Rights | `R/W/C/D` |
| access_multi_request_line | Role / User   | `R/W/C`   |

### 🗃️ `multi.approval.type` — MultiApproval

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                       | Label                         | Type        | Req | Store | Relation                 |
| --------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------ |
| `active`                    | Active                        | `boolean`   |     | ✅    |                          |
| `amount_opt`                | Amount                        | `selection` |     | ✅    |                          |
| `apply_for_model`           | Apply For Model ?             | `boolean`   |     | ✅    |                          |
| `approval_minimum`          | Minimum Approvers             | `integer`   |     |       |                          |
| `approve_python_code`       | Approved Action               | `text`      |     | ✅    |                          |
| `create_date`               | Created on                    | `datetime`  |     | ✅    |                          |
| `create_uid`                | Created by                    | `many2one`  |     | ✅    | res.users                |
| `date_opt`                  | Date                          | `selection` |     | ✅    |                          |
| `description`               | Description                   | `char`      |     | ✅    |                          |
| `display_name`              | Display Name                  | `char`      |     |       |                          |
| `document_opt`              | Document                      | `selection` |     | ✅    |                          |
| `domain`                    | Domain                        | `text`      |     | ✅    |                          |
| `hide_button`               | Hide Buttons from Model View? | `boolean`   |     | ✅    |                          |
| `id`                        | ID                            | `integer`   |     | ✅    |                          |
| `image`                     | Image                         | `binary`    |     | ✅    |                          |
| `is_configured`             | Configured                    | `boolean`   |     | ✅    |                          |
| `is_request`                | Request                       | `boolean`   |     | ✅    |                          |
| `line_ids`                  | Approvers                     | `one2many`  |     | ✅    | multi.approval.type.line |
| `location_opt`              | Location                      | `selection` |     | ✅    |                          |
| `model_id`                  | Model                         | `many2one`  |     | ✅    | ir.model                 |
| `model_name`                | Model Name                    | `char`      |     | ✅    |                          |
| `name`                      | Name                          | `char`      |     | ✅    |                          |
| `partner_opt`               | Contact                       | `selection` |     | ✅    |                          |
| `payment_opt`               | Payment                       | `selection` |     | ✅    |                          |
| `period_opt`                | Period                        | `selection` |     | ✅    |                          |
| `priority`                  | Priority                      | `integer`   |     | ✅    |                          |
| `product_opt`               | Product                       | `selection` |     | ✅    |                          |
| `quantity_opt`              | Quantity                      | `selection` |     | ✅    |                          |
| `reference_opt`             | Reference                     | `selection` |     | ✅    |                          |
| `refuse_python_code`        | Refused Action                | `text`      |     | ✅    |                          |
| `request_to_validate_count` | record count                  | `integer`   |     |       |                          |
| `write_date`                | Last Updated on               | `datetime`  |     | ✅    |                          |
| `write_uid`                 | Last Updated by               | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                              | Group                    | Perms     |
| --------------------------------- | ------------------------ | --------- |
| access_multi_approval_type_manger | Approval / Administrator | `R/W/C/D` |
| access_multi_approval_type_user   | Approval / User          | `R`       |

### 🗃️ `multi.approval.type.line` — MultiApprovalLine

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label             | Type        | Req | Store | Relation            |
| ----------------- | ----------------- | ----------- | --- | ----- | ------------------- |
| `approve_tmpl_id` | Approve Template  | `many2one`  |     | ✅    | mail.template       |
| `create_date`     | Created on        | `datetime`  |     | ✅    |                     |
| `create_uid`      | Created by        | `many2one`  |     | ✅    | res.users           |
| `display_name`    | Display Name      | `char`      |     |       |                     |
| `id`              | ID                | `integer`   |     | ✅    |                     |
| `line`            | MultiApprovalLine | `many2one`  |     | ✅    | multi.approval.type |
| `reject_tmpl_id`  | Reject Template   | `many2one`  |     | ✅    | mail.template       |
| `require_opt`     | Type of Approval  | `selection` |     | ✅    |                     |
| `user_id`         | User              | `many2one`  |     | ✅    | res.users           |
| `write_date`      | Last Updated on   | `datetime`  |     | ✅    |                     |
| `write_uid`       | Last Updated by   | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                            | Group         | Perms     |
| ------------------------------- | ------------- | --------- |
| access_multi_approval_type_line | Access Rights | `R/W/C/D` |
| access_multi_approval_type_line | Role / User   | `R/W/C`   |
