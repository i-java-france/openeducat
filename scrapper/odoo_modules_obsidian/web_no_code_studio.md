---
title: "Web No Code Studio"
module: "web_no_code_studio"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org/"
license: "Other proprietary"
category: "Tools"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_____, odoo/app]
---

# 🟢 Web No Code Studio

> **Module:** `web_no_code_studio` | **Version:** `19.0.1.0` **Category:** Tools |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org/

## 🔗 Dependencies

[[mail]] [[base_automation]] [[web]] [[html_editor]] [[backend_theme]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT web_no_code_studio.report_iframe_layout (qweb)`
- `* INHERIT web_no_code_studio.report_layout (qweb)`
- `Report Assets (qweb)`
- `ir.actions.report.kanban (kanban)`

### Reports

_none_

## 🛠️ Technical Documentation

**10 model(s) defined by this module:**

### 🗃️ `no.code.approval.rule` — Approval Rule

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation                       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ------------------------------ |
| `action_id`                  | Action                 | `many2one`  |     | ✅    | ir.actions.actions             |
| `action_xmlid`               | External ID            | `char`      |     |       |                                |
| `active`                     | Active                 | `boolean`   |     | ✅    |                                |
| `approval_group_id`          | Approval Group         | `many2one`  |     | ✅    | res.groups                     |
| `approver_ids`               | Approvers              | `many2many` |     |       | res.users                      |
| `approver_log_ids`           | Approver Log           | `one2many`  |     | ✅    | no.code.approval.rule.approver |
| `can_validate`               | Can be approved        | `boolean`   |     |       |                                |
| `conditional`                | Conditional Rule       | `boolean`   |     |       |                                |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                                |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users                      |
| `display_name`               | Display Name           | `char`      |     |       |                                |
| `domain`                     | Domain                 | `char`      |     | ✅    |                                |
| `entries_count`              | Number of Entries      | `integer`   |     |       |                                |
| `entry_ids`                  | Entries                | `one2many`  |     | ✅    | no.code.approval.entry         |
| `exclusive_user`             | Exclusive Approval     | `boolean`   |     | ✅    |                                |
| `has_message`                | Has Message            | `boolean`   |     |       |                                |
| `id`                         | ID                     | `integer`   |     | ✅    |                                |
| `kanban_color`               | Kanban Color           | `integer`   |     |       |                                |
| `message`                    | Description            | `char`      |     | ✅    |                                |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers                 |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message                   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner                    |
| `method`                     | Method                 | `char`      |     | ✅    |                                |
| `model_id`                   | Model                  | `many2one`  | ✅  | ✅    | ir.model                       |
| `model_name`                 | Model Name             | `char`      |     | ✅    |                                |
| `name`                       | Name                   | `char`      |     | ✅    |                                |
| `notification_order`         | Step                   | `selection` |     | ✅    |                                |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating                  |
| `users_to_notify`            | Users to Notify        | `many2many` |     | ✅    | res.users                      |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message                   |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                                |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users                      |

**Access Rights:**

| Name                         | Group       | Perms     |
| ---------------------------- | ----------- | --------- |
| access_no_code_approval_rule | Role / User | `R/W/C/D` |

### 🗃️ `no.code.approval.entry` — Approval Entry

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label                | Type                 | Req | Store | Relation              |
| -------------- | -------------------- | -------------------- | --- | ----- | --------------------- |
| `action_id`    | Action               | `many2one`           |     | ✅    | ir.actions.actions    |
| `approved`     | Approved             | `boolean`            |     | ✅    |                       |
| `create_date`  | Created on           | `datetime`           |     | ✅    |                       |
| `create_uid`   | Created by           | `many2one`           |     | ✅    | res.users             |
| `display_name` | Display Name         | `char`               |     |       |                       |
| `id`           | ID                   | `integer`            |     | ✅    |                       |
| `method`       | Method               | `char`               |     | ✅    |                       |
| `model`        | Model Name           | `char`               |     | ✅    |                       |
| `name`         | Name                 | `char`               |     | ✅    |                       |
| `reference`    | Reference            | `char`               |     |       |                       |
| `res_id`       | Record ID            | `many2one_reference` | ✅  | ✅    |                       |
| `rule_id`      | Approval Rule        | `many2one`           | ✅  | ✅    | no.code.approval.rule |
| `user_id`      | Approved/rejected by | `many2one`           | ✅  | ✅    | res.users             |
| `write_date`   | Last Updated on      | `datetime`           |     | ✅    |                       |
| `write_uid`    | Last Updated by      | `many2one`           |     | ✅    | res.users             |

**Access Rights:**

| Name                          | Group       | Perms     |
| ----------------------------- | ----------- | --------- |
| access_no_code_approval_entry | Role / User | `R/W/C/D` |

### 🗃️ `no.code.approval.request` — Approval Request

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field              | Label           | Type                 | Req | Store | Relation              |
| ------------------ | --------------- | -------------------- | --- | ----- | --------------------- |
| `create_date`      | Created on      | `datetime`           |     | ✅    |                       |
| `create_uid`       | Created by      | `many2one`           |     | ✅    | res.users             |
| `display_name`     | Display Name    | `char`               |     |       |                       |
| `id`               | ID              | `integer`            |     | ✅    |                       |
| `mail_activity_id` | Linked Activity | `many2one`           | ✅  | ✅    | mail.activity         |
| `res_id`           | Record ID       | `many2one_reference` | ✅  | ✅    |                       |
| `rule_id`          | Approval Rule   | `many2one`           | ✅  | ✅    | no.code.approval.rule |
| `write_date`       | Last Updated on | `datetime`           |     | ✅    |                       |
| `write_uid`        | Last Updated by | `many2one`           |     | ✅    | res.users             |

**Access Rights:**

| Name                            | Group       | Perms     |
| ------------------------------- | ----------- | --------- |
| access_no_code_approval_request | Role / User | `R/W/C/D` |

### 🗃️ `no.code.approval.rule.approver` — Approval Rule Approvers Enriched

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label           | Type       | Req | Store | Relation              |
| --------------- | --------------- | ---------- | --- | ----- | --------------------- |
| `create_date`   | Created on      | `datetime` |     | ✅    |                       |
| `create_uid`    | Created by      | `many2one` |     | ✅    | res.users             |
| `date_to`       | Date To         | `date`     |     | ✅    |                       |
| `display_name`  | Display Name    | `char`     |     |       |                       |
| `id`            | ID              | `integer`  |     | ✅    |                       |
| `is_delegation` | Is Delegation   | `boolean`  |     | ✅    |                       |
| `rule_id`       | Rule            | `many2one` | ✅  | ✅    | no.code.approval.rule |
| `user_id`       | User            | `many2one` | ✅  | ✅    | res.users             |
| `write_date`    | Last Updated on | `datetime` |     | ✅    |                       |
| `write_uid`     | Last Updated by | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                                  | Group       | Perms     |
| ------------------------------------- | ----------- | --------- |
| access_no_code_approval_rule_approver | Role / User | `R/W/C/D` |

### 🗃️ `base` — Base

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.model.fields` — Fields

fields configuration for form builder

**Fields:**

| Field                      | Label                          | Type        | Req | Store | Relation                  |
| -------------------------- | ------------------------------ | ----------- | --- | ----- | ------------------------- |
| `column1`                  | Column 1                       | `char`      |     | ✅    |                           |
| `column2`                  | Column 2                       | `char`      |     | ✅    |                           |
| `company_dependent`        | Company Dependent              | `boolean`   |     | ✅    |                           |
| `compute`                  | Compute                        | `text`      |     | ✅    |                           |
| `copied`                   | Copied                         | `boolean`   |     | ✅    |                           |
| `create_date`              | Created on                     | `datetime`  |     | ✅    |                           |
| `create_uid`               | Created by                     | `many2one`  |     | ✅    | res.users                 |
| `currency_field`           | Currency field                 | `char`      |     | ✅    |                           |
| `depends`                  | Dependencies                   | `char`      |     | ✅    |                           |
| `display_name`             | Display Name                   | `char`      |     |       |                           |
| `domain`                   | Domain                         | `char`      |     | ✅    |                           |
| `field_description`        | Field Label                    | `char`      | ✅  | ✅    |                           |
| `group_expand`             | Expand Groups                  | `boolean`   |     | ✅    |                           |
| `groups`                   | Groups                         | `many2many` |     | ✅    | res.groups                |
| `help`                     | Field Help                     | `text`      |     | ✅    |                           |
| `id`                       | ID                             | `integer`   |     | ✅    |                           |
| `index`                    | Indexed                        | `boolean`   |     | ✅    |                           |
| `model`                    | Model Name                     | `char`      | ✅  | ✅    |                           |
| `model_id`                 | Model                          | `many2one`  | ✅  | ✅    | ir.model                  |
| `modules`                  | In Apps                        | `char`      |     |       |                           |
| `name`                     | Field Name                     | `char`      | ✅  | ✅    |                           |
| `on_delete`                | On Delete                      | `selection` |     | ✅    |                           |
| `readonly`                 | Readonly                       | `boolean`   |     | ✅    |                           |
| `related`                  | Related Field Definition       | `char`      |     | ✅    |                           |
| `related_field_id`         | Related Field                  | `many2one`  |     | ✅    | ir.model.fields           |
| `relation`                 | Related Model                  | `char`      |     | ✅    |                           |
| `relation_field`           | Relation Field                 | `char`      |     | ✅    |                           |
| `relation_field_id`        | Relation field                 | `many2one`  |     | ✅    | ir.model.fields           |
| `relation_table`           | Relation Table                 | `char`      |     | ✅    |                           |
| `required`                 | Required                       | `boolean`   |     | ✅    |                           |
| `sanitize`                 | Sanitize HTML                  | `boolean`   |     | ✅    |                           |
| `sanitize_attributes`      | Sanitize HTML Attributes       | `boolean`   |     | ✅    |                           |
| `sanitize_form`            | Sanitize HTML Form             | `boolean`   |     | ✅    |                           |
| `sanitize_overridable`     | Sanitize HTML overridable      | `boolean`   |     | ✅    |                           |
| `sanitize_style`           | Sanitize HTML Style            | `boolean`   |     | ✅    |                           |
| `sanitize_tags`            | Sanitize HTML Tags             | `boolean`   |     | ✅    |                           |
| `secure`                   | Secure                         | `boolean`   |     | ✅    |                           |
| `selectable`               | Selectable                     | `boolean`   |     | ✅    |                           |
| `selection`                | Selection Options (Deprecated) | `char`      |     |       |                           |
| `selection_ids`            | Selection Options              | `one2many`  |     | ✅    | ir.model.fields.selection |
| `serialization_field_id`   | Serialization Field            | `many2one`  |     | ✅    | ir.model.fields           |
| `size`                     | Size                           | `integer`   |     | ✅    |                           |
| `state`                    | Type                           | `selection` | ✅  | ✅    |                           |
| `store`                    | Stored                         | `boolean`   |     | ✅    |                           |
| `strip_classes`            | Strip Class Attribute          | `boolean`   |     | ✅    |                           |
| `strip_style`              | Strip Style Attribute          | `boolean`   |     | ✅    |                           |
| `tracking`                 | Enable Ordered Tracking        | `integer`   |     | ✅    |                           |
| `translate`                | Translatable                   | `selection` |     | ✅    |                           |
| `ttype`                    | Field Type                     | `selection` | ✅  | ✅    |                           |
| `website_form_blacklisted` | Blacklisted in web forms       | `boolean`   |     | ✅    |                           |
| `write_date`               | Last Updated on                | `datetime`  |     | ✅    |                           |
| `write_uid`                | Last Updated by                | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name                              | Group         | Perms     |
| --------------------------------- | ------------- | --------- |
| ir_model_fields group_erp_manager | Access Rights | `R/W/C/D` |
| ir_model_fields all               | Role / User   | `-`       |

### 🗃️ `ir.ui.menu` — Menu

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label           | Type        | Req | Store | Relation   |
| --------------- | --------------- | ----------- | --- | ----- | ---------- |
| `action`        | Action          | `reference` |     | ✅    |            |
| `active`        | Active          | `boolean`   |     | ✅    |            |
| `child_id`      | Child IDs       | `one2many`  |     | ✅    | ir.ui.menu |
| `complete_name` | Full Path       | `char`      |     |       |            |
| `create_date`   | Created on      | `datetime`  |     | ✅    |            |
| `create_uid`    | Created by      | `many2one`  |     | ✅    | res.users  |
| `display_name`  | Display Name    | `char`      |     |       |            |
| `group_ids`     | Groups          | `many2many` |     | ✅    | res.groups |
| `id`            | ID              | `integer`   |     | ✅    |            |
| `name`          | Menu            | `char`      | ✅  | ✅    |            |
| `parent_id`     | Parent Menu     | `many2one`  |     | ✅    | ir.ui.menu |
| `parent_path`   | Parent Path     | `char`      |     | ✅    |            |
| `sequence`      | Sequence        | `integer`   |     | ✅    |            |
| `web_icon`      | Web Icon File   | `char`      |     | ✅    |            |
| `web_icon_data` | Web Icon Image  | `binary`    |     | ✅    |            |
| `write_date`    | Last Updated on | `datetime`  |     | ✅    |            |
| `write_uid`     | Last Updated by | `many2one`  |     | ✅    | res.users  |

**Access Rights:**

| Name                    | Group                | Perms     |
| ----------------------- | -------------------- | --------- |
| ir_ui_menu group_system | Role / Administrator | `R/W/C/D` |
| ir_ui_menu group_user   | Role / User          | `R`       |

### 🗃️ `ir.qweb` — Qweb

IrQweb object for rendering stuff in the website context

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.actions.report` — Report Action

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label                     | Type        | Req | Store | Relation           |
| -------------------- | ------------------------- | ----------- | --- | ----- | ------------------ |
| `attachment`         | Save as Attachment Prefix | `char`      |     | ✅    |                    |
| `attachment_use`     | Reload from Attachment    | `boolean`   |     | ✅    |                    |
| `binding_model_id`   | Binding Model             | `many2one`  |     | ✅    | ir.model           |
| `binding_type`       | Binding Type              | `selection` | ✅  | ✅    |                    |
| `binding_view_types` | Binding View Types        | `char`      |     | ✅    |                    |
| `create_date`        | Created on                | `datetime`  |     | ✅    |                    |
| `create_uid`         | Created by                | `many2one`  |     | ✅    | res.users          |
| `display_name`       | Display Name              | `char`      |     |       |                    |
| `domain`             | Filter domain             | `char`      |     | ✅    |                    |
| `group_ids`          | Groups                    | `many2many` |     | ✅    | res.groups         |
| `help`               | Action Description        | `html`      |     | ✅    |                    |
| `id`                 | ID                        | `integer`   |     | ✅    |                    |
| `is_invoice_report`  | Invoice report            | `boolean`   |     | ✅    |                    |
| `model`              | Model Name                | `char`      | ✅  | ✅    |                    |
| `model_id`           | Model                     | `many2one`  |     |       | ir.model           |
| `multi`              | On Multiple Doc.          | `boolean`   |     | ✅    |                    |
| `name`               | Action Name               | `char`      | ✅  | ✅    |                    |
| `paperformat_id`     | Paper Format              | `many2one`  |     | ✅    | report.paperformat |
| `path`               | Path to show in the URL   | `char`      |     | ✅    |                    |
| `print_report_name`  | Printed Report Name       | `char`      |     | ✅    |                    |
| `report_file`        | Report File               | `char`      |     | ✅    |                    |
| `report_name`        | Template Name             | `char`      | ✅  | ✅    |                    |
| `report_type`        | Report Type               | `selection` | ✅  | ✅    |                    |
| `type`               | Action Type               | `char`      | ✅  | ✅    |                    |
| `write_date`         | Last Updated on           | `datetime`  |     | ✅    |                    |
| `write_uid`          | Last Updated by           | `many2one`  |     | ✅    | res.users          |
| `xml_id`             | External ID               | `char`      |     |       |                    |

**Access Rights:**

| Name                           | Group                | Perms     |
| ------------------------------ | -------------------- | --------- |
| ir_actions_report_group_system | Role / Administrator | `R/W/C/D` |
| ir.actions.report.access.user  | Role / User          | `R`       |

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
