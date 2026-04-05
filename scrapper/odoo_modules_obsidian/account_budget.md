---
title: "Budget Management"
module: "account_budget"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc "
maintainer: "OpenEduCat Inc"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Accounting"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/__________]
---

# 🟢 Budget Management

> **Module:** `account_budget` | **Version:** `19.0.1.0` **Category:** Accounting |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[account]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `Invoicing/Accounting/Budgets`
- `Invoicing/Configuration/Budgetary Positions`
- `Invoicing/Reporting/Management/Budgets Analysis`

### Views

- `* INHERIT account.analytic.account.form.inherit.budget (form)`
- `account.budget.line.search (search)`
- `account.budget.post.form (form)`
- `account.budget.post.list (list)`
- `account.budget.post.search (search)`
- `crossovered.budget.kanban (kanban)`
- `crossovered.budget.line.form (form)`
- `crossovered.budget.line.graph (graph)`
- `crossovered.budget.line.pivot (pivot)`
- `crossovered.budget.line.tree (list)`
- `crossovered.budget.search (search)`
- `crossovered.budget.view.form (form)`
- `crossovered.budget.view.tree (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**4 model(s) defined by this module:**

### 🗃️ `account.analytic.account` — Analytic Account

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation                 |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ------------------------ |
| `active`                     | Active                 | `boolean`   |     | ✅    |                          |
| `balance`                    | Balance                | `monetary`  |     |       |                          |
| `code`                       | Reference              | `char`      |     | ✅    |                          |
| `color`                      | Color Index            | `integer`   |     |       |                          |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company              |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                          |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users                |
| `credit`                     | Credit                 | `monetary`  |     |       |                          |
| `crossovered_budget_line`    | Budget Lines           | `one2many`  |     | ✅    | crossovered.budget.lines |
| `currency_id`                | Currency               | `many2one`  |     |       | res.currency             |
| `debit`                      | Debit                  | `monetary`  |     |       |                          |
| `display_name`               | Display Name           | `char`      |     |       |                          |
| `has_message`                | Has Message            | `boolean`   |     |       |                          |
| `id`                         | ID                     | `integer`   |     | ✅    |                          |
| `invoice_count`              | Invoice Count          | `integer`   |     |       |                          |
| `line_ids`                   | Analytic Lines         | `one2many`  |     | ✅    | account.analytic.line    |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                          |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers           |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                          |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                          |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                          |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message             |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                          |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                          |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                          |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner              |
| `name`                       | Analytic Account       | `char`      | ✅  | ✅    |                          |
| `partner_id`                 | Customer               | `many2one`  |     | ✅    | res.partner              |
| `plan_id`                    | Plan                   | `many2one`  | ✅  | ✅    | account.analytic.plan    |
| `purchase_order_count`       | Purchase Order Count   | `integer`   |     |       |                          |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating            |
| `root_plan_id`               | Root Plan              | `many2one`  |     | ✅    | account.analytic.plan    |
| `vendor_bill_count`          | Vendor Bill Count      | `integer`   |     |       |                          |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message             |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                          |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                                | Group                            | Perms     |
| ----------------------------------- | -------------------------------- | --------- |
| account_analytic_account salesman   | Sales / User: Own Documents Only | `R/W/C`   |
| account.analytic.account accountant | Contact / Accountant             | `R/W/C/D` |
| access_account_analytic_account     | Analytic Accounting              | `R/W/C/D` |
| account.analytic.account            | Role / User                      | `R`       |

**Record Rules:**

- **Analytic multi company rule** (Global) `R/W/C/D`
  - Domain: `['|',('company_id','=',False),('company_id', 'parent_of', company_ids)]`

### 🗃️ `crossovered.budget` — Budget

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation                 |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ------------------------ |
| `company_id`                 | Company                | `many2one`  | ✅  | ✅    | res.company              |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                          |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users                |
| `crossovered_budget_line`    | Budget Lines           | `one2many`  |     | ✅    | crossovered.budget.lines |
| `date_from`                  | Start Date             | `date`      | ✅  | ✅    |                          |
| `date_to`                    | End Date               | `date`      | ✅  | ✅    |                          |
| `display_name`               | Display Name           | `char`      |     |       |                          |
| `has_message`                | Has Message            | `boolean`   |     |       |                          |
| `id`                         | ID                     | `integer`   |     | ✅    |                          |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                          |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers           |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                          |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                          |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                          |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message             |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                          |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                          |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                          |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner              |
| `name`                       | Budget Name            | `char`      | ✅  | ✅    |                          |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating            |
| `state`                      | Status                 | `selection` | ✅  | ✅    |                          |
| `user_id`                    | Responsible            | `many2one`  |     | ✅    | res.users                |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message             |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                          |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                          | Group                | Perms     |
| ----------------------------- | -------------------- | --------- |
| crossovered.budget            | Accounting / Advisor | `R`       |
| crossovered.budget accountant | Contact / Accountant | `R/W/C/D` |

**Record Rules:**

- **Budget multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),('company_id','child_of',[user.company_id.id])]`

### 🗃️ `account.budget.post` — Budgetary Position

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation        |
| -------------- | --------------- | ----------- | --- | ----- | --------------- |
| `account_ids`  | Accounts        | `many2many` |     | ✅    | account.account |
| `company_id`   | Company         | `many2one`  | ✅  | ✅    | res.company     |
| `create_date`  | Created on      | `datetime`  |     | ✅    |                 |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users       |
| `display_name` | Display Name    | `char`      |     |       |                 |
| `id`           | ID              | `integer`   |     | ✅    |                 |
| `name`         | Name            | `char`      | ✅  | ✅    |                 |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |                 |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                           | Group                | Perms     |
| ------------------------------ | -------------------- | --------- |
| account.budget.post            | Accounting / Advisor | `R`       |
| account.budget.post accountant | Contact / Accountant | `R/W/C/D` |

**Record Rules:**

- **Budget post multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),('company_id','child_of',[user.company_id.id])]`

### 🗃️ `crossovered.budget.lines` — Budget Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label              | Type        | Req | Store | Relation                 |
| -------------------------- | ------------------ | ----------- | --- | ----- | ------------------------ |
| `analytic_account_id`      | Analytic Account   | `many2one`  |     | ✅    | account.analytic.account |
| `analytic_plan_id`         | Analytic Plan      | `many2one`  |     |       | account.analytic.plan    |
| `company_id`               | Company            | `many2one`  |     | ✅    | res.company              |
| `create_date`              | Created on         | `datetime`  |     | ✅    |                          |
| `create_uid`               | Created by         | `many2one`  |     | ✅    | res.users                |
| `crossovered_budget_id`    | Budget             | `many2one`  | ✅  | ✅    | crossovered.budget       |
| `crossovered_budget_state` | Budget State       | `selection` |     | ✅    |                          |
| `currency_id`              | Currency           | `many2one`  |     |       | res.currency             |
| `date_from`                | Start Date         | `date`      | ✅  | ✅    |                          |
| `date_to`                  | End Date           | `date`      | ✅  | ✅    |                          |
| `display_name`             | Display Name       | `char`      |     |       |                          |
| `general_budget_id`        | Budgetary Position | `many2one`  |     | ✅    | account.budget.post      |
| `id`                       | ID                 | `integer`   |     | ✅    |                          |
| `is_above_budget`          | Is Above Budget    | `boolean`   |     |       |                          |
| `name`                     | Name               | `char`      |     |       |                          |
| `paid_date`                | Paid Date          | `date`      |     | ✅    |                          |
| `percentage`               | Achievement        | `float`     |     |       |                          |
| `planned_amount`           | Planned Amount     | `monetary`  | ✅  | ✅    |                          |
| `practical_amount`         | Practical Amount   | `monetary`  |     |       |                          |
| `theoritical_amount`       | Theoretical Amount | `monetary`  |     |       |                          |
| `write_date`               | Last Updated on    | `datetime`  |     | ✅    |                          |
| `write_uid`                | Last Updated by    | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                                | Group                | Perms     |
| ----------------------------------- | -------------------- | --------- |
| crossovered.budget.lines accountant | Contact / Accountant | `R/W/C/D` |
| crossovered.budget.lines manager    | Role / User          | `R/W/C`   |

**Record Rules:**

- **Budget lines multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),('company_id','child_of',[user.company_id.id])]`
