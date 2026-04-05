---
title: "Payment Provider: Custom Payment Modes"
module: "payment_custom"
state: "installed"
version: "19.0.2.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Payment Providers"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________________]
---

# 🟢 Payment Provider: Custom Payment Modes

> **Module:** `payment_custom` | **Version:** `19.0.2.0` **Category:** Payment Providers
> | **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[payment]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT Custom Provider Form (form)`
- `* INHERIT custom_state_header (qweb)`
- `* INHERIT payment_custom.payment_method_form (qweb)`
- `* INHERIT payment_custom.token_form (qweb)`
- `redirect_form (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**2 model(s) defined by this module:**

### 🗃️ `payment.provider` — Payment Provider

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                          | Type        | Req | Store | Relation         |
| ------------------------------- | ------------------------------ | ----------- | --- | ----- | ---------------- |
| `allow_express_checkout`        | Allow Express Checkout         | `boolean`   |     | ✅    |                  |
| `allow_tokenization`            | Allow Saving Payment Methods   | `boolean`   |     | ✅    |                  |
| `auth_msg`                      | Authorize Message              | `html`      |     | ✅    |                  |
| `available_country_ids`         | Countries                      | `many2many` |     | ✅    | res.country      |
| `available_currency_ids`        | Currencies                     | `many2many` |     | ✅    | res.currency     |
| `cancel_msg`                    | Cancelled Message              | `html`      |     | ✅    |                  |
| `capture_manually`              | Capture Amount Manually        | `boolean`   |     | ✅    |                  |
| `code`                          | Code                           | `selection` | ✅  | ✅    |                  |
| `color`                         | Color                          | `integer`   |     | ✅    |                  |
| `company_id`                    | Company                        | `many2one`  | ✅  | ✅    | res.company      |
| `create_date`                   | Created on                     | `datetime`  |     | ✅    |                  |
| `create_uid`                    | Created by                     | `many2one`  |     | ✅    | res.users        |
| `custom_mode`                   | Custom Mode                    | `selection` |     | ✅    |                  |
| `display_name`                  | Display Name                   | `char`      |     |       |                  |
| `done_msg`                      | Done Message                   | `html`      |     | ✅    |                  |
| `express_checkout_form_view_id` | Express Checkout Form Template | `many2one`  |     | ✅    | ir.ui.view       |
| `id`                            | ID                             | `integer`   |     | ✅    |                  |
| `image_128`                     | Image                          | `binary`    |     | ✅    |                  |
| `inline_form_view_id`           | Inline Form Template           | `many2one`  |     | ✅    | ir.ui.view       |
| `is_published`                  | Published                      | `boolean`   |     | ✅    |                  |
| `journal_id`                    | Payment Journal                | `many2one`  |     |       | account.journal  |
| `main_currency_id`              | Currency                       | `many2one`  |     |       | res.currency     |
| `maximum_amount`                | Maximum Amount                 | `monetary`  |     | ✅    |                  |
| `module_id`                     | Corresponding Module           | `many2one`  |     | ✅    | ir.module.module |
| `module_state`                  | Installation State             | `selection` |     |       |                  |
| `module_to_buy`                 | Odoo Enterprise Module         | `boolean`   |     |       |                  |
| `name`                          | Name                           | `char`      | ✅  | ✅    |                  |
| `payment_method_ids`            | Supported Payment Methods      | `many2many` |     | ✅    | payment.method   |
| `pending_msg`                   | Pending Message                | `html`      |     | ✅    |                  |
| `pre_msg`                       | Help Message                   | `html`      |     | ✅    |                  |
| `qr_code`                       | Enable QR Codes                | `boolean`   |     | ✅    |                  |
| `redirect_form_view_id`         | Redirect Form Template         | `many2one`  |     | ✅    | ir.ui.view       |
| `sequence`                      | Sequence                       | `integer`   |     | ✅    |                  |
| `so_reference_type`             | Communication                  | `selection` |     | ✅    |                  |
| `state`                         | State                          | `selection` | ✅  | ✅    |                  |
| `support_express_checkout`      | Express Checkout               | `boolean`   |     |       |                  |
| `support_manual_capture`        | Manual Capture Supported       | `selection` |     |       |                  |
| `support_refund`                | Refund                         | `selection` |     |       |                  |
| `support_tokenization`          | Tokenization                   | `boolean`   |     |       |                  |
| `token_inline_form_view_id`     | Token Inline Form Template     | `many2one`  |     | ✅    | ir.ui.view       |
| `website_id`                    | Website                        | `many2one`  |     | ✅    | website          |
| `write_date`                    | Last Updated on                | `datetime`  |     | ✅    |                  |
| `write_uid`                     | Last Updated by                | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                    | Group                | Perms     |
| ----------------------- | -------------------- | --------- |
| payment.provider.system | Role / Administrator | `R/W/C/D` |

**Record Rules:**

- **Access providers in own companies only** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'parent_of', company_ids)]`

### 🗃️ `payment.transaction` — Payment Transaction

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                       | Label                   | Type        | Req | Store | Relation            |
| --------------------------- | ----------------------- | ----------- | --- | ----- | ------------------- |
| `amount`                    | Amount                  | `monetary`  | ✅  | ✅    |                     |
| `capture_manually`          | Capture Amount Manually | `boolean`   |     |       |                     |
| `child_transaction_ids`     | Child Transactions      | `one2many`  |     | ✅    | payment.transaction |
| `company_id`                | Company                 | `many2one`  |     | ✅    | res.company         |
| `create_date`               | Created on              | `datetime`  |     | ✅    |                     |
| `create_uid`                | Created by              | `many2one`  |     | ✅    | res.users           |
| `currency_id`               | Currency                | `many2one`  | ✅  | ✅    | res.currency        |
| `display_name`              | Display Name            | `char`      |     |       |                     |
| `id`                        | ID                      | `integer`   |     | ✅    |                     |
| `invoice_ids`               | Invoices                | `many2many` |     | ✅    | account.move        |
| `invoices_count`            | Invoices Count          | `integer`   |     |       |                     |
| `is_donation`               | Is donation             | `boolean`   |     | ✅    |                     |
| `is_live`                   | Production Environment  | `boolean`   |     | ✅    |                     |
| `is_post_processed`         | Is Post-processed       | `boolean`   |     | ✅    |                     |
| `landing_route`             | Landing Route           | `char`      |     | ✅    |                     |
| `last_state_change`         | Last State Change Date  | `datetime`  |     | ✅    |                     |
| `operation`                 | Operation               | `selection` |     | ✅    |                     |
| `partner_address`           | Address                 | `char`      |     | ✅    |                     |
| `partner_city`              | City                    | `char`      |     | ✅    |                     |
| `partner_country_id`        | Country                 | `many2one`  |     | ✅    | res.country         |
| `partner_email`             | Email                   | `char`      |     | ✅    |                     |
| `partner_id`                | Customer                | `many2one`  | ✅  | ✅    | res.partner         |
| `partner_lang`              | Language                | `selection` |     | ✅    |                     |
| `partner_name`              | Partner Name            | `char`      |     | ✅    |                     |
| `partner_phone`             | Phone                   | `char`      |     | ✅    |                     |
| `partner_state_id`          | State                   | `many2one`  |     | ✅    | res.country.state   |
| `partner_zip`               | Zip                     | `char`      |     | ✅    |                     |
| `payment_id`                | Payment                 | `many2one`  |     | ✅    | account.payment     |
| `payment_method_code`       | Payment Method Code     | `char`      |     |       |                     |
| `payment_method_id`         | Payment Method          | `many2one`  | ✅  | ✅    | payment.method      |
| `primary_payment_method_id` | Primary Payment Method  | `many2one`  |     |       | payment.method      |
| `provider_code`             | Provider Code           | `selection` |     |       |                     |
| `provider_id`               | Provider                | `many2one`  | ✅  | ✅    | payment.provider    |
| `provider_reference`        | Provider Reference      | `char`      |     | ✅    |                     |
| `reference`                 | Reference               | `char`      | ✅  | ✅    |                     |
| `refunds_count`             | Refunds Count           | `integer`   |     |       |                     |
| `sale_order_ids`            | Sales Orders            | `many2many` |     | ✅    | sale.order          |
| `sale_order_ids_nbr`        | # of Sales Orders       | `integer`   |     |       |                     |
| `source_transaction_id`     | Source Transaction      | `many2one`  |     | ✅    | payment.transaction |
| `state`                     | Status                  | `selection` | ✅  | ✅    |                     |
| `state_message`             | Message                 | `text`      |     | ✅    |                     |
| `token_id`                  | Payment Token           | `many2one`  |     | ✅    | payment.token       |
| `tokenize`                  | Create Token            | `boolean`   |     | ✅    |                     |
| `write_date`                | Last Updated on         | `datetime`  |     | ✅    |                     |
| `write_uid`                 | Last Updated by         | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                       | Group                  | Perms     |
| -------------------------- | ---------------------- | --------- |
| payment.transaction.user   | Accounting / Invoicing | `R/W/C`   |
| payment.transaction.system | Role / Administrator   | `R/W/C/D` |

**Record Rules:**

- **Access transactions in own companies only** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`
- **Access every payment transaction** (25) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
