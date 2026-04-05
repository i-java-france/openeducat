---
title: "United States - Localizations"
module: "l10n_us"
state: "installed"
version: "19.0.1.1"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/documentation/latest/applications/finance/fiscal_localizations.html"
license: "LGPL-3"
category: "Account Charts"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/______________]
---

# 🟢 United States - Localizations

> **Module:** `l10n_us` | **Version:** `19.0.1.1` **Category:** Account Charts |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:**
> https://www.odoo.com/documentation/latest/applications/finance/fiscal_localizations.html

## 🔗 Dependencies

[[base]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT res.partner.bank.form.inherit (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

### 🗃️ `res.partner.bank` — Bank Accounts

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                  | Label                                | Type        | Req | Store | Relation           |
| -------------------------------------- | ------------------------------------ | ----------- | --- | ----- | ------------------ |
| `acc_holder_name`                      | Account Holder Name                  | `char`      |     | ✅    |                    |
| `acc_number`                           | Account Number                       | `char`      | ✅  | ✅    |                    |
| `acc_type`                             | Type                                 | `selection` |     |       |                    |
| `active`                               | Active                               | `boolean`   |     | ✅    |                    |
| `activity_calendar_event_id`           | Next Activity Calendar Event         | `many2one`  |     |       | calendar.event     |
| `activity_date_deadline`               | Next Activity Deadline               | `date`      |     |       |                    |
| `activity_exception_decoration`        | Activity Exception Decoration        | `selection` |     |       |                    |
| `activity_exception_icon`              | Icon                                 | `char`      |     |       |                    |
| `activity_ids`                         | Activities                           | `one2many`  |     | ✅    | mail.activity      |
| `activity_state`                       | Activity State                       | `selection` |     |       |                    |
| `activity_summary`                     | Next Activity Summary                | `char`      |     |       |                    |
| `activity_type_icon`                   | Activity Type Icon                   | `char`      |     |       |                    |
| `activity_type_id`                     | Next Activity Type                   | `many2one`  |     |       | mail.activity.type |
| `activity_user_id`                     | Responsible User                     | `many2one`  |     |       | res.users          |
| `allow_out_payment`                    | Send Money                           | `boolean`   |     | ✅    |                    |
| `bank_bic`                             | Bank Identifier Code                 | `char`      |     |       |                    |
| `bank_city`                            | City                                 | `char`      |     |       |                    |
| `bank_country`                         | Country                              | `many2one`  |     |       | res.country        |
| `bank_email`                           | Email                                | `char`      |     |       |                    |
| `bank_id`                              | Bank                                 | `many2one`  |     | ✅    | res.bank           |
| `bank_name`                            | Name                                 | `char`      |     |       |                    |
| `bank_phone`                           | Phone                                | `char`      |     |       |                    |
| `bank_state`                           | Fed. State                           | `many2one`  |     |       | res.country.state  |
| `bank_street`                          | Street                               | `char`      |     |       |                    |
| `bank_street2`                         | Street2                              | `char`      |     |       |                    |
| `bank_zip`                             | Zip                                  | `char`      |     |       |                    |
| `clearing_number`                      | Clearing Number                      | `char`      |     | ✅    |                    |
| `color`                                | Color                                | `integer`   |     |       |                    |
| `company_id`                           | Company                              | `many2one`  |     | ✅    | res.company        |
| `country_code`                         | Country Code                         | `char`      |     |       |                    |
| `create_date`                          | Created on                           | `datetime`  |     | ✅    |                    |
| `create_uid`                           | Created by                           | `many2one`  |     | ✅    | res.users          |
| `currency_id`                          | Currency                             | `many2one`  |     | ✅    | res.currency       |
| `currency_symbol`                      | Symbol                               | `char`      |     |       |                    |
| `display_name`                         | Display Name                         | `char`      |     |       |                    |
| `duplicate_bank_partner_ids`           | Duplicate Bank Partner               | `many2many` |     |       | res.partner        |
| `employee_has_multiple_bank_accounts`  | Has Multiple Bank Accounts           | `boolean`   |     |       |                    |
| `employee_id`                          | Employee                             | `many2many` |     |       | hr.employee        |
| `employee_salary_amount`               | Salary Allocation                    | `float`     |     |       |                    |
| `employee_salary_amount_is_percentage` | Employee Salary Amount Is Percentage | `boolean`   |     |       |                    |
| `has_iban_warning`                     | Has Iban Warning                     | `boolean`   |     | ✅    |                    |
| `has_message`                          | Has Message                          | `boolean`   |     |       |                    |
| `has_money_transfer_warning`           | Has Money Transfer Warning           | `boolean`   |     | ✅    |                    |
| `id`                                   | ID                                   | `integer`   |     | ✅    |                    |
| `journal_id`                           | Account Journal                      | `one2many`  |     | ✅    | account.journal    |
| `l10n_us_bank_account_type`            | Bank Account Type                    | `selection` | ✅  | ✅    |                    |
| `lock_trust_fields`                    | Lock Trust Fields                    | `boolean`   |     |       |                    |
| `message_attachment_count`             | Attachment Count                     | `integer`   |     |       |                    |
| `message_follower_ids`                 | Followers                            | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`                    | Message Delivery error               | `boolean`   |     |       |                    |
| `message_has_error_counter`            | Number of errors                     | `integer`   |     |       |                    |
| `message_has_sms_error`                | SMS Delivery error                   | `boolean`   |     |       |                    |
| `message_ids`                          | Messages                             | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`                  | Is Follower                          | `boolean`   |     |       |                    |
| `message_needaction`                   | Action Needed                        | `boolean`   |     |       |                    |
| `message_needaction_counter`           | Number of Actions                    | `integer`   |     |       |                    |
| `message_partner_ids`                  | Followers (Partners)                 | `many2many` |     |       | res.partner        |
| `money_transfer_service`               | Money Transfer Service               | `char`      |     |       |                    |
| `my_activity_date_deadline`            | My Activity Deadline                 | `date`      |     |       |                    |
| `note`                                 | Notes                                | `text`      |     | ✅    |                    |
| `partner_country_name`                 | Country Name                         | `char`      |     |       |                    |
| `partner_customer_rank`                | Customer Rank                        | `integer`   |     |       |                    |
| `partner_id`                           | Account Holder                       | `many2one`  | ✅  | ✅    | res.partner        |
| `partner_supplier_rank`                | Supplier Rank                        | `integer`   |     |       |                    |
| `rating_ids`                           | Ratings                              | `one2many`  |     | ✅    | rating.rating      |
| `related_moves`                        | Related Moves                        | `one2many`  |     | ✅    | account.move       |
| `sanitized_acc_number`                 | Sanitized Account Number             | `char`      |     | ✅    |                    |
| `sequence`                             | Sequence                             | `integer`   |     | ✅    |                    |
| `show_aba_routing`                     | Show Aba Routing                     | `boolean`   |     |       |                    |
| `user_has_group_validate_bank_account` | User Has Group Validate Bank Account | `boolean`   |     |       |                    |
| `website_message_ids`                  | Website Messages                     | `one2many`  |     | ✅    | mail.message       |
| `write_date`                           | Last Updated on                      | `datetime`  |     | ✅    |                    |
| `write_uid`                            | Last Updated by                      | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                   | Group              | Perms     |
| -------------------------------------- | ------------------ | --------- |
| res_partner_bank group_partner_manager | Contact / Creation | `R/W/C/D` |
| res_partner_bank group_user            | Role / User        | `R`       |

**Record Rules:**

- **Partner bank company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Billing: Allow accessing employee bank accounts** (37) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **HR: Prevent non HR officers from accessing employee bank accounts** (1) `R/W/C/D`
  - Domain: `[('partner_id.employee_ids', '=', False)]`
- **HR: Allow HR officers from accessing employee bank accounts** (49) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
