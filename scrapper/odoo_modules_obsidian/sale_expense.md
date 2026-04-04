---
title: "Sales Expense"
module: "sale_expense"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Sales"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_____]
---

# 🟢 Sales Expense

> **Module:** `sale_expense` | **Version:** `19.0.1.0` **Category:** Sales |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[sale_management]] [[hr_expense]]

## 📖 Description

# Reinvoice Employee Expense

Create some products for which you can re-invoice the costs. This module allow to
reinvoice employee expense, by setting the SO directly on the expense.

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT hr.expense.form.inherit.sale.expense (form)`
- `* INHERIT hr.expense.list.inherit.sale.expense (list)`
- `* INHERIT hr.expense.split.view.inherit.sale.expense (form)`
- `* INHERIT product.product.view.list.inherit.sale.expense (list)`
- `* INHERIT product.template.expense (form)`
- `* INHERIT sale.order.form.inherit.sale.expense (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**7 model(s) defined by this module:**

### 🗃️ `hr.expense` — Expense

> 📧 Mail Thread

        Here are the rights associated with the expense flow

        Action       Group                   Restriction
        =================================================================================
        Submit      Employee                Only his own
                    Officer                 If he is expense manager of the employee, manager of the employee
                                              or the employee is in the department managed by the officer
                    Manager                 Always
        Approve     Officer                 Not his own and he is expense manager of the employee, manager of the employee
                                              or the employee is in the department managed by the officer
                    Manager                 Always
        Post        Billing accountant      State == approved
        Cancel      Officer                 Not his own and he is expense manager of the employee, manager of the employee
                                              or the employee is in the department managed by the officer
                    Manager                 Always
        =================================================================================

**Fields:**

| Field                                | Label                                                 | Type        | Req | Store | Relation                    |
| ------------------------------------ | ----------------------------------------------------- | ----------- | --- | ----- | --------------------------- |
| `account_id`                         | Account                                               | `many2one`  |     | ✅    | account.account             |
| `account_move_id`                    | Journal Entry                                         | `many2one`  |     | ✅    | account.move                |
| `activity_calendar_event_id`         | Next Activity Calendar Event                          | `many2one`  |     |       | calendar.event              |
| `activity_date_deadline`             | Next Activity Deadline                                | `date`      |     |       |                             |
| `activity_exception_decoration`      | Activity Exception Decoration                         | `selection` |     |       |                             |
| `activity_exception_icon`            | Icon                                                  | `char`      |     |       |                             |
| `activity_ids`                       | Activities                                            | `one2many`  |     | ✅    | mail.activity               |
| `activity_state`                     | Activity State                                        | `selection` |     |       |                             |
| `activity_summary`                   | Next Activity Summary                                 | `char`      |     |       |                             |
| `activity_type_icon`                 | Activity Type Icon                                    | `char`      |     |       |                             |
| `activity_type_id`                   | Next Activity Type                                    | `many2one`  |     |       | mail.activity.type          |
| `activity_user_id`                   | Responsible User                                      | `many2one`  |     |       | res.users                   |
| `amount_residual`                    | Amount Due                                            | `monetary`  |     |       |                             |
| `analytic_distribution`              | Analytic Distribution                                 | `json`      |     | ✅    |                             |
| `analytic_precision`                 | Analytic Precision                                    | `integer`   |     |       |                             |
| `approval_date`                      | Approval Date                                         | `datetime`  |     | ✅    |                             |
| `approval_state`                     | Approval State                                        | `selection` |     | ✅    |                             |
| `attachment_ids`                     | Attachments                                           | `one2many`  |     | ✅    | ir.attachment               |
| `can_approve`                        | Can Approve                                           | `boolean`   |     |       |                             |
| `can_be_reinvoiced`                  | Can be reinvoiced                                     | `boolean`   |     |       |                             |
| `can_reset`                          | Can Reset                                             | `boolean`   |     |       |                             |
| `company_currency_id`                | Report Company Currency                               | `many2one`  |     |       | res.currency                |
| `company_id`                         | Company                                               | `many2one`  | ✅  | ✅    | res.company                 |
| `create_date`                        | Created on                                            | `datetime`  |     | ✅    |                             |
| `create_uid`                         | Created by                                            | `many2one`  |     | ✅    | res.users                   |
| `currency_id`                        | Currency                                              | `many2one`  | ✅  | ✅    | res.currency                |
| `currency_rate`                      | Currency Rate                                         | `float`     |     |       |                             |
| `date`                               | Expense Date                                          | `date`      |     | ✅    |                             |
| `department_id`                      | Department                                            | `many2one`  |     | ✅    | hr.department               |
| `description`                        | Internal Notes                                        | `text`      |     | ✅    |                             |
| `display_name`                       | Display Name                                          | `char`      |     |       |                             |
| `distribution_analytic_account_ids`  | Distribution Analytic Account                         | `many2many` |     |       | account.analytic.account    |
| `duplicate_expense_ids`              | Duplicate Expense                                     | `many2many` |     |       | hr.expense                  |
| `employee_id`                        | Employee                                              | `many2one`  | ✅  | ✅    | hr.employee                 |
| `former_sheet_id`                    | Former Report                                         | `integer`   |     | ✅    |                             |
| `has_message`                        | Has Message                                           | `boolean`   |     |       |                             |
| `id`                                 | ID                                                    | `integer`   |     | ✅    |                             |
| `is_editable`                        | Is Editable By Current User                           | `boolean`   |     |       |                             |
| `is_multiple_currency`               | Is currency_id different from the company_currency_id | `boolean`   |     |       |                             |
| `journal_id`                         | Journal                                               | `many2one`  |     |       | account.journal             |
| `label_currency_rate`                | Label Currency Rate                                   | `char`      |     |       |                             |
| `manager_id`                         | Manager                                               | `many2one`  |     | ✅    | res.users                   |
| `message_attachment_count`           | Attachment Count                                      | `integer`   |     |       |                             |
| `message_follower_ids`               | Followers                                             | `one2many`  |     | ✅    | mail.followers              |
| `message_has_error`                  | Message Delivery error                                | `boolean`   |     |       |                             |
| `message_has_error_counter`          | Number of errors                                      | `integer`   |     |       |                             |
| `message_has_sms_error`              | SMS Delivery error                                    | `boolean`   |     |       |                             |
| `message_ids`                        | Messages                                              | `one2many`  |     | ✅    | mail.message                |
| `message_is_follower`                | Is Follower                                           | `boolean`   |     |       |                             |
| `message_main_attachment_checksum`   | Checksum/SHA1                                         | `char`      |     |       |                             |
| `message_main_attachment_id`         | Main Attachment                                       | `many2one`  |     | ✅    | ir.attachment               |
| `message_needaction`                 | Action Needed                                         | `boolean`   |     |       |                             |
| `message_needaction_counter`         | Number of Actions                                     | `integer`   |     |       |                             |
| `message_partner_ids`                | Followers (Partners)                                  | `many2many` |     |       | res.partner                 |
| `my_activity_date_deadline`          | My Activity Deadline                                  | `date`      |     |       |                             |
| `name`                               | Description                                           | `char`      | ✅  | ✅    |                             |
| `nb_attachment`                      | Number of Attachments                                 | `integer`   |     |       |                             |
| `payment_method_line_id`             | Payment Method                                        | `many2one`  |     | ✅    | account.payment.method.line |
| `payment_mode`                       | Paid By                                               | `selection` | ✅  | ✅    |                             |
| `price_unit`                         | Unit Price                                            | `float`     | ✅  | ✅    |                             |
| `product_description`                | Product Description                                   | `html`      |     |       |                             |
| `product_has_cost`                   | Product Has Cost                                      | `boolean`   |     |       |                             |
| `product_has_tax`                    | Whether tax is defined on a selected product          | `boolean`   |     |       |                             |
| `product_id`                         | Category                                              | `many2one`  |     | ✅    | product.product             |
| `product_uom_id`                     | Unit                                                  | `many2one`  |     | ✅    | uom.uom                     |
| `quantity`                           | Quantity                                              | `float`     | ✅  | ✅    |                             |
| `rating_ids`                         | Ratings                                               | `one2many`  |     | ✅    | rating.rating               |
| `sale_order_id`                      | Customer to Reinvoice                                 | `many2one`  |     | ✅    | sale.order                  |
| `sale_order_line_id`                 | Sale Order Line                                       | `many2one`  |     | ✅    | sale.order.line             |
| `same_receipt_expense_ids`           | Same Receipt Expense                                  | `many2many` |     |       | hr.expense                  |
| `selectable_payment_method_line_ids` | Selectable Payment Method Line                        | `many2many` |     |       | account.payment.method.line |
| `split_expense_origin_id`            | Origin Split Expense                                  | `many2one`  |     | ✅    | hr.expense                  |
| `state`                              | Status                                                | `selection` |     | ✅    |                             |
| `tax_amount`                         | Tax amount                                            | `monetary`  |     | ✅    |                             |
| `tax_amount_currency`                | Tax amount in Currency                                | `monetary`  |     | ✅    |                             |
| `tax_ids`                            | Included taxes                                        | `many2many` |     | ✅    | account.tax                 |
| `total_amount`                       | Total                                                 | `monetary`  |     | ✅    |                             |
| `total_amount_currency`              | Total In Currency                                     | `monetary`  |     | ✅    |                             |
| `untaxed_amount`                     | Total Untaxed Amount                                  | `monetary`  |     | ✅    |                             |
| `untaxed_amount_currency`            | Total Untaxed Amount In Currency                      | `monetary`  |     | ✅    |                             |
| `vendor_id`                          | Vendor                                                | `many2one`  |     | ✅    | res.partner                 |
| `website_message_ids`                | Website Messages                                      | `one2many`  |     | ✅    | mail.message                |
| `write_date`                         | Last Updated on                                       | `datetime`  |     | ✅    |                             |
| `write_uid`                          | Last Updated by                                       | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                  | Group                    | Perms     |
| --------------------- | ------------------------ | --------- |
| hr.expense.accountant | Accounting / Invoicing   | `R/W/C`   |
| hr.expense.user       | Expenses / Team Approver | `R/W/C/D` |
| hr.expense.manager    | Expenses / Administrator | `R/W/C/D` |
| hr.expense.employee   | Role / User              | `R/W/C/D` |

**Record Rules:**

- **Manager Expense** (77, 39) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Team Approver Expense** (76) `R/W/C/D`
  - Domain:
    `['|', '|', '|', '|',             ('employee_id.user_id', '=', user.id),             ('employee_id.department_id.manager_id.user_id', '=', user.id),             ('employee_id', 'child_of', user.employee_ids.ids),             ('employee_id.expense_manager_id', '=', user.id),             ('manager_id', '=', user.id)]`
- **Employee Expense** (1) `R/W/C/D`
  - Domain:
    `[             '|', '&', ('employee_id.expense_manager_id', '=', user.id), ('state', 'in', ['draft', 'submitted', 'approved', 'refused']),                  '&', ('employee_id.user_id', '=', user.id), ('state', '=', 'draft')         ]`
- **Employees can't modify an expense that is not in draft state** (1) `R`
  - Domain:
    `[             '|', '&', ('employee_id.user_id', '=', user.id), ('state', '!=', 'draft'),                  '&', ('employee_id.expense_manager_id', '=', user.id), ('state', 'in', ['submitted', 'approved', 'refused'])         ]`
- **Expense multi company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`

### 🗃️ `account.move` — Journal Entry

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                       | Label                                     | Type        | Req | Store | Relation                        |
| ------------------------------------------- | ----------------------------------------- | ----------- | --- | ----- | ------------------------------- |
| `abnormal_amount_warning`                   | Abnormal Amount Warning                   | `text`      |     |       |                                 |
| `abnormal_date_warning`                     | Abnormal Date Warning                     | `text`      |     |       |                                 |
| `access_token`                              | Security Token                            | `char`      |     | ✅    |                                 |
| `access_url`                                | Portal Access URL                         | `char`      |     |       |                                 |
| `access_warning`                            | Access warning                            | `text`      |     |       |                                 |
| `account_fiscal_country_group_codes`        | Account Fiscal Country Group Codes        | `json`      |     |       |                                 |
| `activity_calendar_event_id`                | Next Activity Calendar Event              | `many2one`  |     |       | calendar.event                  |
| `activity_date_deadline`                    | Next Activity Deadline                    | `date`      |     |       |                                 |
| `activity_exception_decoration`             | Activity Exception Decoration             | `selection` |     |       |                                 |
| `activity_exception_icon`                   | Icon                                      | `char`      |     |       |                                 |
| `activity_ids`                              | Activities                                | `one2many`  |     | ✅    | mail.activity                   |
| `activity_state`                            | Activity State                            | `selection` |     |       |                                 |
| `activity_summary`                          | Next Activity Summary                     | `char`      |     |       |                                 |
| `activity_type_icon`                        | Activity Type Icon                        | `char`      |     |       |                                 |
| `activity_type_id`                          | Next Activity Type                        | `many2one`  |     |       | mail.activity.type              |
| `activity_user_id`                          | Responsible User                          | `many2one`  |     |       | res.users                       |
| `adjusting_entries_count`                   | Adjusting Entries Count                   | `integer`   |     |       |                                 |
| `adjusting_entries_move_ids`                | Created Adjusting Entries                 | `many2many` |     | ✅    | account.move                    |
| `adjusting_entry_origin_label`              | Adjusting Entry Origin Label              | `char`      |     |       |                                 |
| `adjusting_entry_origin_move_ids`           | Adjusting Entry Origin Moves              | `many2many` |     | ✅    | account.move                    |
| `adjusting_entry_origin_moves_count`        | Adjusting Entry Origin Moves Count        | `integer`   |     |       |                                 |
| `alerts`                                    | Alerts                                    | `json`      |     |       |                                 |
| `always_tax_exigible`                       | Always Tax Exigible                       | `boolean`   |     | ✅    |                                 |
| `amount_paid`                               | Amount paid                               | `monetary`  |     |       |                                 |
| `amount_residual`                           | Amount Due                                | `monetary`  |     | ✅    |                                 |
| `amount_residual_signed`                    | Amount Due Signed                         | `monetary`  |     | ✅    |                                 |
| `amount_tax`                                | Tax                                       | `monetary`  |     | ✅    |                                 |
| `amount_tax_signed`                         | Tax Signed                                | `monetary`  |     | ✅    |                                 |
| `amount_total`                              | Total                                     | `monetary`  |     | ✅    |                                 |
| `amount_total_in_currency_signed`           | Total in Currency Signed                  | `monetary`  |     | ✅    |                                 |
| `amount_total_signed`                       | Total Signed                              | `monetary`  |     | ✅    |                                 |
| `amount_total_words`                        | Amount total in words                     | `char`      |     |       |                                 |
| `amount_untaxed`                            | Untaxed Amount                            | `monetary`  |     | ✅    |                                 |
| `amount_untaxed_in_currency_signed`         | Untaxed Amount Signed Currency            | `monetary`  |     | ✅    |                                 |
| `amount_untaxed_signed`                     | Untaxed Amount Signed                     | `monetary`  |     | ✅    |                                 |
| `asset_depreciation_ids`                    | Assets Depreciation Lines                 | `one2many`  |     | ✅    | account.asset.depreciation.line |
| `attachment_ids`                            | Attachments                               | `one2many`  |     | ✅    | ir.attachment                   |
| `audit_trail_message_ids`                   | Audit Trail Messages                      | `one2many`  |     | ✅    | mail.message                    |
| `authorized_transaction_ids`                | Authorized Transactions                   | `many2many` |     |       | payment.transaction             |
| `auto_post`                                 | Auto-post                                 | `selection` | ✅  | ✅    |                                 |
| `auto_post_origin_id`                       | First recurring entry                     | `many2one`  |     | ✅    | account.move                    |
| `auto_post_until`                           | Auto-post until                           | `date`      |     | ✅    |                                 |
| `bank_partner_id`                           | Bank Partner                              | `many2one`  |     |       | res.partner                     |
| `campaign_id`                               | Campaign                                  | `many2one`  |     | ✅    | utm.campaign                    |
| `checked`                                   | Reviewed                                  | `boolean`   |     | ✅    |                                 |
| `commercial_partner_id`                     | Commercial Entity                         | `many2one`  |     | ✅    | res.partner                     |
| `company_currency_id`                       | Company Currency                          | `many2one`  |     |       | res.currency                    |
| `company_id`                                | Company                                   | `many2one`  |     | ✅    | res.company                     |
| `company_price_include`                     | Default Sales Price Include               | `selection` |     |       |                                 |
| `country_code`                              | Country Code                              | `char`      |     |       |                                 |
| `create_date`                               | Created on                                | `datetime`  |     | ✅    |                                 |
| `create_uid`                                | Created by                                | `many2one`  |     | ✅    | res.users                       |
| `currency_id`                               | Currency                                  | `many2one`  | ✅  | ✅    | res.currency                    |
| `date`                                      | Date                                      | `date`      | ✅  | ✅    |                                 |
| `delivery_date`                             | Delivery Date                             | `date`      |     | ✅    |                                 |
| `direction_sign`                            | Direction Sign                            | `integer`   |     |       |                                 |
| `display_inactive_currency_warning`         | Display Inactive Currency Warning         | `boolean`   |     |       |                                 |
| `display_link_qr_code`                      | Display Link QR-code                      | `boolean`   |     |       |                                 |
| `display_name`                              | Display Name                              | `char`      |     |       |                                 |
| `display_qr_code`                           | Display QR-code                           | `boolean`   |     |       |                                 |
| `display_send_button`                       | Display Send Button                       | `boolean`   |     |       |                                 |
| `duplicated_ref_ids`                        | Duplicated Ref                            | `many2many` |     |       | account.move                    |
| `exchange_diff_partial_ids`                 | Related reconciliation                    | `one2many`  |     | ✅    | account.partial.reconcile       |
| `expected_currency_rate`                    | Expected Currency Rate                    | `float`     |     |       |                                 |
| `expense_ids`                               | Expense                                   | `one2many`  |     | ✅    | hr.expense                      |
| `fiscal_position_id`                        | Fiscal Position                           | `many2one`  |     | ✅    | account.fiscal.position         |
| `has_message`                               | Has Message                               | `boolean`   |     |       |                                 |
| `has_reconciled_entries`                    | Has Reconciled Entries                    | `boolean`   |     |       |                                 |
| `hide_post_button`                          | Hide Post Button                          | `boolean`   |     |       |                                 |
| `highest_name`                              | Highest Name                              | `char`      |     |       |                                 |
| `highlight_send_button`                     | Highlight Send Button                     | `boolean`   |     |       |                                 |
| `id`                                        | ID                                        | `integer`   |     | ✅    |                                 |
| `inalterable_hash`                          | Inalterability Hash                       | `char`      |     | ✅    |                                 |
| `incoterm_location`                         | Incoterm Location                         | `char`      |     | ✅    |                                 |
| `invoice_cash_rounding_id`                  | Cash Rounding Method                      | `many2one`  |     | ✅    | account.cash.rounding           |
| `invoice_currency_rate`                     | Currency Rate                             | `float`     |     | ✅    |                                 |
| `invoice_date`                              | Invoice/Bill Date                         | `date`      |     | ✅    |                                 |
| `invoice_date_due`                          | Due Date                                  | `date`      |     | ✅    |                                 |
| `invoice_filter_type_domain`                | Invoice Filter Type Domain                | `char`      |     |       |                                 |
| `invoice_has_outstanding`                   | Invoice Has Outstanding                   | `boolean`   |     |       |                                 |
| `invoice_incoterm_id`                       | Incoterm                                  | `many2one`  |     | ✅    | account.incoterms               |
| `invoice_incoterm_placeholder`              | Invoice Incoterm Placeholder              | `char`      |     |       |                                 |
| `invoice_line_ids`                          | Invoice lines                             | `one2many`  |     | ✅    | account.move.line               |
| `invoice_origin`                            | Origin                                    | `char`      |     | ✅    |                                 |
| `invoice_outstanding_credits_debits_widget` | Invoice Outstanding Credits Debits Widget | `binary`    |     |       |                                 |
| `invoice_partner_display_name`              | Invoice Partner Display Name              | `char`      |     | ✅    |                                 |
| `invoice_payments_widget`                   | Invoice Payments Widget                   | `binary`    |     |       |                                 |
| `invoice_payment_term_id`                   | Payment Terms                             | `many2one`  |     | ✅    | account.payment.term            |
| `invoice_pdf_report_file`                   | PDF File                                  | `binary`    |     | ✅    |                                 |
| `invoice_pdf_report_id`                     | PDF Attachment                            | `many2one`  |     |       | ir.attachment                   |
| `invoice_source_email`                      | Source Email                              | `char`      |     | ✅    |                                 |
| `invoice_user_id`                           | Salesperson                               | `many2one`  |     | ✅    | res.users                       |
| `invoice_vendor_bill_id`                    | Vendor Bill                               | `many2one`  |     |       | account.move                    |
| `is_being_sent`                             | Is Being Sent                             | `boolean`   |     |       |                                 |
| `is_draft_duplicated_ref_ids`               | Is Draft Duplicated Ref                   | `boolean`   |     |       |                                 |
| `is_manually_modified`                      | Is Manually Modified                      | `boolean`   |     | ✅    |                                 |
| `is_move_sent`                              | Is Move Sent                              | `boolean`   |     | ✅    |                                 |
| `is_purchase_matched`                       | Is Purchase Matched                       | `boolean`   |     |       |                                 |
| `is_sale_installed`                         | Is Sale Installed                         | `boolean`   |     |       |                                 |
| `is_storno`                                 | Is Storno                                 | `boolean`   |     |       |                                 |
| `journal_group_id`                          | Ledger                                    | `many2one`  |     |       | account.journal.group           |
| `journal_id`                                | Journal                                   | `many2one`  | ✅  | ✅    | account.journal                 |
| `journal_line_ids`                          | Journal Items (DEPRECATED)                | `one2many`  |     | ✅    | account.move.line               |
| `line_ids`                                  | Journal Items                             | `one2many`  |     | ✅    | account.move.line               |
| `made_sequence_gap`                         | Made Sequence Gap                         | `boolean`   |     | ✅    |                                 |
| `matched_payment_ids`                       | Matched Payments                          | `many2many` |     | ✅    | account.payment                 |
| `medium_id`                                 | Medium                                    | `many2one`  |     | ✅    | utm.medium                      |
| `message_attachment_count`                  | Attachment Count                          | `integer`   |     |       |                                 |
| `message_follower_ids`                      | Followers                                 | `one2many`  |     | ✅    | mail.followers                  |
| `message_has_error`                         | Message Delivery error                    | `boolean`   |     |       |                                 |
| `message_has_error_counter`                 | Number of errors                          | `integer`   |     |       |                                 |
| `message_has_sms_error`                     | SMS Delivery error                        | `boolean`   |     |       |                                 |
| `message_ids`                               | Messages                                  | `one2many`  |     | ✅    | mail.message                    |
| `message_is_follower`                       | Is Follower                               | `boolean`   |     |       |                                 |
| `message_main_attachment_id`                | Main Attachment                           | `many2one`  |     | ✅    | ir.attachment                   |
| `message_needaction`                        | Action Needed                             | `boolean`   |     |       |                                 |
| `message_needaction_counter`                | Number of Actions                         | `integer`   |     |       |                                 |
| `message_partner_ids`                       | Followers (Partners)                      | `many2many` |     |       | res.partner                     |
| `move_sent_values`                          | Sent                                      | `selection` |     |       |                                 |
| `move_type`                                 | Type                                      | `selection` | ✅  | ✅    |                                 |
| `my_activity_date_deadline`                 | My Activity Deadline                      | `date`      |     |       |                                 |
| `name`                                      | Number                                    | `char`      |     | ✅    |                                 |
| `name_placeholder`                          | Name Placeholder                          | `char`      |     |       |                                 |
| `narration`                                 | Terms and Conditions                      | `html`      |     | ✅    |                                 |
| `nb_expenses`                               | Number of Expenses                        | `integer`   |     |       |                                 |
| `need_cancel_request`                       | Need Cancel Request                       | `boolean`   |     |       |                                 |
| `needed_terms`                              | Needed Terms                              | `binary`    |     |       |                                 |
| `needed_terms_dirty`                        | Needed Terms Dirty                        | `boolean`   |     |       |                                 |
| `next_payment_date`                         | Next Payment Date                         | `date`      |     |       |                                 |
| `no_followup`                               | No Follow-Up                              | `boolean`   |     |       |                                 |
| `origin_payment_id`                         | Payment                                   | `many2one`  |     | ✅    | account.payment                 |
| `partner_bank_id`                           | Recipient Bank                            | `many2one`  |     | ✅    | res.partner.bank                |
| `partner_credit_warning`                    | Partner Credit Warning                    | `text`      |     |       |                                 |
| `partner_id`                                | Partner                                   | `many2one`  |     | ✅    | res.partner                     |
| `partner_shipping_id`                       | Delivery Address                          | `many2one`  |     | ✅    | res.partner                     |
| `payment_count`                             | Payment Count                             | `integer`   |     |       |                                 |
| `payment_ids`                               | Payments                                  | `one2many`  |     | ✅    | account.payment                 |
| `payment_reference`                         | Payment Reference                         | `char`      |     | ✅    |                                 |
| `payment_state`                             | Payment Status                            | `selection` |     | ✅    |                                 |
| `payment_term_details`                      | Payment Term Details                      | `binary`    |     |       |                                 |
| `posted_before`                             | Posted Before                             | `boolean`   |     | ✅    |                                 |
| `preferred_payment_method_line_id`          | Preferred Payment Method Line             | `many2one`  |     | ✅    | account.payment.method.line     |
| `purchase_id`                               | Purchase Order                            | `many2one`  |     |       | purchase.order                  |
| `purchase_order_count`                      | Purchase Order Count                      | `integer`   |     |       |                                 |
| `purchase_order_name`                       | Purchase Order Name                       | `char`      |     |       |                                 |
| `purchase_vendor_bill_id`                   | Auto-complete                             | `many2one`  |     |       | purchase.bill.union             |
| `purchase_warning_text`                     | Purchase Warning                          | `text`      |     |       |                                 |
| `qr_code_method`                            | Payment QR-code                           | `selection` |     | ✅    |                                 |
| `quick_edit_mode`                           | Quick Edit Mode                           | `boolean`   |     |       |                                 |
| `quick_edit_total_amount`                   | Total (Tax inc.)                          | `monetary`  |     | ✅    |                                 |
| `quick_encoding_vals`                       | Quick Encoding Vals                       | `json`      |     |       |                                 |
| `rating_ids`                                | Ratings                                   | `one2many`  |     | ✅    | rating.rating                   |
| `reconciled_payment_ids`                    | Reconciled Payments                       | `many2many` |     |       | account.payment                 |
| `ref`                                       | Reference                                 | `char`      |     | ✅    |                                 |
| `restrict_mode_hash_table`                  | Secure Posted Entries with Hash           | `boolean`   |     |       |                                 |
| `reversal_move_ids`                         | Reversal Move                             | `one2many`  |     | ✅    | account.move                    |
| `reversed_entry_id`                         | Reversal of                               | `many2one`  |     | ✅    | account.move                    |
| `sale_order_count`                          | Sale Order Count                          | `integer`   |     |       |                                 |
| `sale_warning_text`                         | Sale Warning                              | `text`      |     |       |                                 |
| `secured`                                   | Secured                                   | `boolean`   |     |       |                                 |
| `secure_sequence_number`                    | Inalterability No Gap Sequence #          | `integer`   |     | ✅    |                                 |
| `sending_data`                              | Sending Data                              | `json`      |     | ✅    |                                 |
| `sequence_number`                           | Sequence Number                           | `integer`   |     | ✅    |                                 |
| `sequence_prefix`                           | Sequence Prefix                           | `char`      |     | ✅    |                                 |
| `show_delivery_date`                        | Show Delivery Date                        | `boolean`   |     |       |                                 |
| `show_discount_details`                     | Show Discount Details                     | `boolean`   |     |       |                                 |
| `show_journal`                              | Show Journal                              | `boolean`   |     |       |                                 |
| `show_name_warning`                         | Show Name Warning                         | `boolean`   |     |       |                                 |
| `show_payment_term_details`                 | Show Payment Term Details                 | `boolean`   |     |       |                                 |
| `show_reset_to_draft_button`                | Show Reset To Draft Button                | `boolean`   |     |       |                                 |
| `show_taxable_supply_date`                  | Show Taxable Supply Date                  | `boolean`   |     |       |                                 |
| `show_update_fpos`                          | Has Fiscal Position Changed               | `boolean`   |     |       |                                 |
| `source_id`                                 | Source                                    | `many2one`  |     | ✅    | utm.source                      |
| `state`                                     | Status                                    | `selection` | ✅  | ✅    |                                 |
| `statement_id`                              | Statement                                 | `many2one`  |     |       | account.bank.statement          |
| `statement_line_id`                         | Statement Line                            | `many2one`  |     | ✅    | account.bank.statement.line     |
| `statement_line_ids`                        | Statements                                | `one2many`  |     | ✅    | account.bank.statement.line     |
| `status_in_payment`                         | Status In Payment                         | `selection` |     |       |                                 |
| `stock_move_ids`                            | Stock Move                                | `one2many`  |     | ✅    | stock.move                      |
| `suitable_journal_ids`                      | Suitable Journal                          | `many2many` |     |       | account.journal                 |
| `taxable_supply_date`                       | Taxable Supply Date                       | `date`      |     | ✅    |                                 |
| `taxable_supply_date_placeholder`           | Taxable Supply Date Placeholder           | `char`      |     |       |                                 |
| `tax_calculation_rounding_method`           | Tax calculation rounding method           | `selection` |     |       |                                 |
| `tax_cash_basis_created_move_ids`           | Cash Basis Entries                        | `one2many`  |     | ✅    | account.move                    |
| `tax_cash_basis_origin_move_id`             | Cash Basis Origin                         | `many2one`  |     | ✅    | account.move                    |
| `tax_cash_basis_rec_id`                     | Tax Cash Basis Entry of                   | `many2one`  |     | ✅    | account.partial.reconcile       |
| `tax_country_code`                          | Tax Country Code                          | `char`      |     |       |                                 |
| `tax_country_id`                            | Tax Country                               | `many2one`  |     |       | res.country                     |
| `taxes_legal_notes`                         | Taxes Legal Notes                         | `html`      |     |       |                                 |
| `tax_lock_date_message`                     | Tax Lock Date Message                     | `char`      |     |       |                                 |
| `tax_totals`                                | Invoice Totals                            | `binary`    |     |       |                                 |
| `team_id`                                   | Sales Team                                | `many2one`  |     | ✅    | crm.team                        |
| `transaction_count`                         | Transaction Count                         | `integer`   |     |       |                                 |
| `transaction_ids`                           | Transactions                              | `many2many` |     | ✅    | payment.transaction             |
| `type_name`                                 | Type Name                                 | `char`      |     |       |                                 |
| `ubl_cii_xml_file`                          | UBL/CII File                              | `binary`    |     | ✅    |                                 |
| `ubl_cii_xml_filename`                      | UBL/CII Filename                          | `char`      |     |       |                                 |
| `ubl_cii_xml_id`                            | Attachment                                | `many2one`  |     |       | ir.attachment                   |
| `user_id`                                   | User                                      | `many2one`  |     |       | res.users                       |
| `website_id`                                | Website                                   | `many2one`  |     | ✅    | website                         |
| `website_message_ids`                       | Website Messages                          | `one2many`  |     | ✅    | mail.message                    |
| `write_date`                                | Last Updated on                           | `datetime`  |     | ✅    |                                 |
| `write_uid`                                 | Last Updated by                           | `many2one`  |     | ✅    | res.users                       |

**Access Rights:**

| Name                             | Group                            | Perms     |
| -------------------------------- | -------------------------------- | --------- |
| account_move salesman            | Sales / User: Own Documents Only | `R`       |
| account.move                     | Accounting / Invoicing           | `R/W/C/D` |
| account.move manager             | Accounting / Advisor             | `R`       |
| account.move                     | Purchase / User                  | `R/W/C/D` |
| account.move.hr.expense.approver | Expenses / Team Approver         | `R`       |
| account.move readonly            | Auditor                          | `R`       |
| account.move.portal              | Role / Portal                    | `R`       |

**Record Rules:**

- **Account Entry** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`
- **All Journal Entries** (37) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Portal Personal Account Invoices** (10) `R/W/C/D`
  - Domain:
    `[('state', 'not in', ('cancel', 'draft')), ('move_type', 'in', ('out_invoice', 'out_refund', 'in_invoice', 'in_refund')), ('partner_id','child_of',[user.commercial_partner_id.id])]`
- **Readonly Move** (36) `R`
  - Domain: `[(1, '=', 1)]`
- **Readonly Move** (37) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Expense Team Approver Account Move** (76) `R/W/C/D`
  - Domain: `[('expense_ids', '!=', False)]`
- **Purchase User Account Move** (86) `R/W/C/D`
  - Domain: `[('move_type', 'in', ('in_invoice', 'in_refund', 'in_receipt'))]`
- **Personal Invoices** (25) `R/W/C/D`
  - Domain:
    `[('move_type', 'in', ('out_invoice', 'out_refund')), '|', ('invoice_user_id', '=', user.id), ('invoice_user_id', '=', False)]`
- **All Invoices** (26) `R/W/C/D`
  - Domain: `[('move_type', 'in', ('out_invoice', 'out_refund'))]`

### 🗃️ `product.template` — Product

> 📧 Mail Thread

This mixin adds rating statistics to mail.thread that already support ratings.

**Fields:**

| Field                                       | Label                                  | Type         | Req | Store | Relation                        |
| ------------------------------------------- | -------------------------------------- | ------------ | --- | ----- | ------------------------------- |
| `accessory_product_ids`                     | Accessory Products                     | `many2many`  |     | ✅    | product.product                 |
| `account_tag_ids`                           | Account Tags                           | `many2many`  |     | ✅    | account.account.tag             |
| `active`                                    | Active                                 | `boolean`    |     | ✅    |                                 |
| `activity_calendar_event_id`                | Next Activity Calendar Event           | `many2one`   |     |       | calendar.event                  |
| `activity_date_deadline`                    | Next Activity Deadline                 | `date`       |     |       |                                 |
| `activity_exception_decoration`             | Activity Exception Decoration          | `selection`  |     |       |                                 |
| `activity_exception_icon`                   | Icon                                   | `char`       |     |       |                                 |
| `activity_ids`                              | Activities                             | `one2many`   |     | ✅    | mail.activity                   |
| `activity_state`                            | Activity State                         | `selection`  |     |       |                                 |
| `activity_summary`                          | Next Activity Summary                  | `char`       |     |       |                                 |
| `activity_type_icon`                        | Activity Type Icon                     | `char`       |     |       |                                 |
| `activity_type_id`                          | Next Activity Type                     | `many2one`   |     |       | mail.activity.type              |
| `activity_user_id`                          | Responsible User                       | `many2one`   |     |       | res.users                       |
| `allow_out_of_stock_order`                  | Sell when Out-of-Stock                 | `boolean`    |     | ✅    |                                 |
| `alternative_product_ids`                   | Alternative Products                   | `many2many`  |     | ✅    | product.template                |
| `asset_category_id`                         | Asset Type                             | `many2one`   |     | ✅    | account.asset.category          |
| `attribute_line_ids`                        | Product Attributes                     | `one2many`   |     | ✅    | product.template.attribute.line |
| `available_threshold`                       | Show Threshold                         | `float`      |     | ✅    |                                 |
| `barcode`                                   | Barcode                                | `char`       |     |       |                                 |
| `base_unit_count`                           | Base Unit Count                        | `float`      | ✅  | ✅    |                                 |
| `base_unit_id`                              | Custom Unit of Measure                 | `many2one`   |     | ✅    | website.base.unit               |
| `base_unit_name`                            | Base Unit Name                         | `char`       |     |       |                                 |
| `base_unit_price`                           | Price Per Unit                         | `monetary`   |     |       |                                 |
| `can_be_expensed`                           | Expenses                               | `boolean`    |     | ✅    |                                 |
| `can_image_1024_be_zoomed`                  | Can Image 1024 be zoomed               | `boolean`    |     | ✅    |                                 |
| `can_publish`                               | Can Publish                            | `boolean`    |     |       |                                 |
| `categ_id`                                  | Product Category                       | `many2one`   |     | ✅    | product.category                |
| `color`                                     | Color Index                            | `integer`    |     | ✅    |                                 |
| `combo_ids`                                 | Combo Choices                          | `many2many`  |     | ✅    | product.combo                   |
| `company_id`                                | Company                                | `many2one`   |     | ✅    | res.company                     |
| `compare_list_price`                        | Compare to Price                       | `monetary`   |     | ✅    |                                 |
| `cost_currency_id`                          | Cost Currency                          | `many2one`   |     |       | res.currency                    |
| `cost_method`                               | Cost Method                            | `selection`  |     |       |                                 |
| `country_of_origin`                         | Origin of Goods                        | `many2one`   |     | ✅    | res.country                     |
| `create_date`                               | Created on                             | `datetime`   |     | ✅    |                                 |
| `create_uid`                                | Created by                             | `many2one`   |     | ✅    | res.users                       |
| `currency_id`                               | Currency                               | `many2one`   |     |       | res.currency                    |
| `default_code`                              | Internal Reference                     | `char`       |     | ✅    |                                 |
| `deferred_revenue_category_id`              | Deferred Revenue Type                  | `many2one`   |     | ✅    | account.asset.category          |
| `description`                               | Description                            | `html`       |     | ✅    |                                 |
| `description_ecommerce`                     | eCommerce Description                  | `html`       |     | ✅    |                                 |
| `description_picking`                       | Description on Picking                 | `text`       |     | ✅    |                                 |
| `description_pickingin`                     | Description on Receptions              | `text`       |     | ✅    |                                 |
| `description_pickingout`                    | Description on Delivery Orders         | `text`       |     | ✅    |                                 |
| `description_purchase`                      | Purchase Description                   | `text`       |     | ✅    |                                 |
| `description_sale`                          | Sales Description                      | `text`       |     | ✅    |                                 |
| `display_name`                              | Display Name                           | `char`       |     |       |                                 |
| `expense_policy`                            | Re-Invoice Costs                       | `selection`  |     | ✅    |                                 |
| `expense_policy_tooltip`                    | Expense Policy Tooltip                 | `char`       |     |       |                                 |
| `fiscal_country_codes`                      | Fiscal Country Codes                   | `char`       |     |       |                                 |
| `has_available_route_ids`                   | Routes can be selected on this product | `boolean`    |     |       |                                 |
| `has_configurable_attributes`               | Is a configurable product              | `boolean`    |     | ✅    |                                 |
| `has_message`                               | Has Message                            | `boolean`    |     |       |                                 |
| `hs_code`                                   | HS Code                                | `char`       |     | ✅    |                                 |
| `id`                                        | ID                                     | `integer`    |     | ✅    |                                 |
| `image_1024`                                | Image 1024                             | `binary`     |     | ✅    |                                 |
| `image_128`                                 | Image 128                              | `binary`     |     | ✅    |                                 |
| `image_1920`                                | Image                                  | `binary`     |     | ✅    |                                 |
| `image_256`                                 | Image 256                              | `binary`     |     | ✅    |                                 |
| `image_512`                                 | Image 512                              | `binary`     |     | ✅    |                                 |
| `incoming_qty`                              | Incoming                               | `float`      |     |       |                                 |
| `invoice_policy`                            | Invoicing Policy                       | `selection`  |     | ✅    |                                 |
| `is_dynamically_created`                    | Is Dynamically Created                 | `boolean`    |     |       |                                 |
| `is_favorite`                               | Favorite                               | `boolean`    |     | ✅    |                                 |
| `is_product_variant`                        | Is a product variant                   | `boolean`    |     |       |                                 |
| `is_published`                              | Is Published                           | `boolean`    |     | ✅    |                                 |
| `is_seo_optimized`                          | SEO optimized                          | `boolean`    |     | ✅    |                                 |
| `is_storable`                               | Track Inventory                        | `boolean`    |     | ✅    |                                 |
| `list_price`                                | Sales Price                            | `float`      |     | ✅    |                                 |
| `location_id`                               | Location                               | `many2one`   |     |       | stock.location                  |
| `lot_sequence_id`                           | Serial/Lot Numbers Sequence            | `many2one`   |     | ✅    | ir.sequence                     |
| `lot_valuated`                              | Valuation by Lot/Serial                | `boolean`    |     | ✅    |                                 |
| `message_attachment_count`                  | Attachment Count                       | `integer`    |     |       |                                 |
| `message_follower_ids`                      | Followers                              | `one2many`   |     | ✅    | mail.followers                  |
| `message_has_error`                         | Message Delivery error                 | `boolean`    |     |       |                                 |
| `message_has_error_counter`                 | Number of errors                       | `integer`    |     |       |                                 |
| `message_has_sms_error`                     | SMS Delivery error                     | `boolean`    |     |       |                                 |
| `message_ids`                               | Messages                               | `one2many`   |     | ✅    | mail.message                    |
| `message_is_follower`                       | Is Follower                            | `boolean`    |     |       |                                 |
| `message_needaction`                        | Action Needed                          | `boolean`    |     |       |                                 |
| `message_needaction_counter`                | Number of Actions                      | `integer`    |     |       |                                 |
| `message_partner_ids`                       | Followers (Partners)                   | `many2many`  |     |       | res.partner                     |
| `my_activity_date_deadline`                 | My Activity Deadline                   | `date`       |     |       |                                 |
| `name`                                      | Name                                   | `char`       | ✅  | ✅    |                                 |
| `nbr_moves_in`                              | Nbr Moves In                           | `integer`    |     |       |                                 |
| `nbr_moves_out`                             | Nbr Moves Out                          | `integer`    |     |       |                                 |
| `nbr_reordering_rules`                      | Reordering Rules                       | `integer`    |     |       |                                 |
| `next_serial`                               | Next Serial                            | `char`       |     |       |                                 |
| `optional_product_ids`                      | Optional Products                      | `many2many`  |     | ✅    | product.template                |
| `outgoing_qty`                              | Outgoing                               | `float`      |     |       |                                 |
| `out_of_stock_message`                      | Out-of-Stock Message                   | `html`       |     | ✅    |                                 |
| `pricelist_rule_ids`                        | Pricelist Rules                        | `one2many`   |     | ✅    | product.pricelist.item          |
| `product_document_count`                    | Documents Count                        | `integer`    |     |       |                                 |
| `product_document_ids`                      | Documents                              | `one2many`   |     | ✅    | product.document                |
| `product_properties`                        | Properties                             | `properties` |     | ✅    |                                 |
| `product_tag_ids`                           | Tags                                   | `many2many`  |     | ✅    | product.tag                     |
| `product_template_image_ids`                | Extra Product Media                    | `one2many`   |     | ✅    | product.image                   |
| `product_tooltip`                           | Product Tooltip                        | `char`       |     |       |                                 |
| `product_variant_count`                     | # Product Variants                     | `integer`    |     |       |                                 |
| `product_variant_id`                        | Product                                | `many2one`   |     |       | product.product                 |
| `product_variant_ids`                       | Products                               | `one2many`   | ✅  | ✅    | product.product                 |
| `property_account_expense_id`               | Expense Account                        | `many2one`   |     | ✅    | account.account                 |
| `property_account_income_id`                | Income Account                         | `many2one`   |     | ✅    | account.account                 |
| `property_price_difference_account_id`      | Price Difference Account               | `many2one`   |     | ✅    | account.account                 |
| `property_stock_inventory`                  | Inventory Location                     | `many2one`   |     | ✅    | stock.location                  |
| `property_stock_production`                 | Production Location                    | `many2one`   |     | ✅    | stock.location                  |
| `public_categ_ids`                          | Website Product Category               | `many2many`  |     | ✅    | product.public.category         |
| `publish_date`                              | Publish Date                           | `datetime`   | ✅  | ✅    |                                 |
| `purchased_product_qty`                     | Purchased                              | `float`      |     |       |                                 |
| `purchase_line_warn_msg`                    | Message for Purchase Order Line        | `text`       |     | ✅    |                                 |
| `purchase_method`                           | Control Policy                         | `selection`  |     | ✅    |                                 |
| `purchase_ok`                               | Purchase                               | `boolean`    |     | ✅    |                                 |
| `qty_available`                             | Quantity On Hand                       | `float`      |     |       |                                 |
| `rating_avg`                                | Average Rating                         | `float`      |     |       |                                 |
| `rating_avg_text`                           | Rating Avg Text                        | `selection`  |     |       |                                 |
| `rating_count`                              | Rating count                           | `integer`    |     |       |                                 |
| `rating_ids`                                | Ratings                                | `one2many`   |     | ✅    | rating.rating                   |
| `rating_last_feedback`                      | Rating Last Feedback                   | `text`       |     |       |                                 |
| `rating_last_image`                         | Rating Last Image                      | `binary`     |     |       |                                 |
| `rating_last_text`                          | Rating Text                            | `selection`  |     |       |                                 |
| `rating_last_value`                         | Rating Last Value                      | `float`      |     | ✅    |                                 |
| `rating_percentage_satisfaction`            | Rating Satisfaction                    | `float`      |     |       |                                 |
| `reordering_max_qty`                        | Reordering Max Qty                     | `float`      |     |       |                                 |
| `reordering_min_qty`                        | Reordering Min Qty                     | `float`      |     |       |                                 |
| `responsible_id`                            | Responsible                            | `many2one`   |     | ✅    | res.users                       |
| `route_from_categ_ids`                      | Category Routes                        | `many2many`  |     |       | stock.route                     |
| `route_ids`                                 | Routes                                 | `many2many`  |     | ✅    | stock.route                     |
| `sale_delay`                                | Customer Lead Time                     | `integer`    |     | ✅    |                                 |
| `sale_line_warn_msg`                        | Sales Order Line Warning               | `text`       |     | ✅    |                                 |
| `sale_ok`                                   | Sales                                  | `boolean`    |     | ✅    |                                 |
| `sales_count`                               | Sold                                   | `float`      |     |       |                                 |
| `seller_ids`                                | Vendors                                | `one2many`   |     | ✅    | product.supplierinfo            |
| `seo_name`                                  | Seo name                               | `char`       |     | ✅    |                                 |
| `sequence`                                  | Sequence                               | `integer`    |     | ✅    |                                 |
| `serial_prefix_format`                      | Custom Lot/Serial                      | `char`       |     |       |                                 |
| `service_to_purchase`                       | Subcontract Service                    | `boolean`    |     | ✅    |                                 |
| `service_tracking`                          | Create on Order                        | `selection`  | ✅  | ✅    |                                 |
| `service_type`                              | Track Service                          | `selection`  |     | ✅    |                                 |
| `show_availability`                         | Show availability Qty                  | `boolean`    |     | ✅    |                                 |
| `show_forecasted_qty_status_button`         | Show Forecasted Qty Status Button      | `boolean`    |     |       |                                 |
| `show_on_hand_qty_status_button`            | Show On Hand Qty Status Button         | `boolean`    |     |       |                                 |
| `show_qty_update_button`                    | Show Qty Update Button                 | `boolean`    |     |       |                                 |
| `standard_price`                            | Cost                                   | `float`      |     |       |                                 |
| `supplier_taxes_id`                         | Purchase Taxes                         | `many2many`  |     | ✅    | account.tax                     |
| `taxes_id`                                  | Sales Taxes                            | `many2many`  |     | ✅    | account.tax                     |
| `tax_string`                                | Tax String                             | `char`       |     |       |                                 |
| `tracking`                                  | Tracking                               | `selection`  | ✅  | ✅    |                                 |
| `type`                                      | Product Type                           | `selection`  | ✅  | ✅    |                                 |
| `uom_id`                                    | Unit                                   | `many2one`   | ✅  | ✅    | uom.uom                         |
| `uom_ids`                                   | Packagings                             | `many2many`  |     | ✅    | uom.uom                         |
| `uom_name`                                  | Unit Name                              | `char`       |     |       |                                 |
| `valid_product_template_attribute_line_ids` | Valid Product Attribute Lines          | `many2many`  |     |       | product.template.attribute.line |
| `valuation`                                 | Valuation                              | `selection`  |     |       |                                 |
| `variants_default_code`                     | Variants Default Code                  | `char`       |     | ✅    |                                 |
| `variant_seller_ids`                        | Variant Seller                         | `one2many`   |     | ✅    | product.supplierinfo            |
| `virtual_available`                         | Forecasted Quantity                    | `float`      |     |       |                                 |
| `visible_expense_policy`                    | Re-Invoice Policy visible              | `boolean`    |     |       |                                 |
| `volume`                                    | Volume                                 | `float`      |     | ✅    |                                 |
| `volume_uom_name`                           | Volume unit of measure label           | `char`       |     |       |                                 |
| `warehouse_id`                              | Warehouse                              | `many2one`   |     |       | stock.warehouse                 |
| `website_absolute_url`                      | Website Absolute URL                   | `char`       |     |       |                                 |
| `website_description`                       | Description for the website            | `html`       |     | ✅    |                                 |
| `website_id`                                | Website                                | `many2one`   |     | ✅    | website                         |
| `website_message_ids`                       | Website Messages                       | `one2many`   |     | ✅    | mail.message                    |
| `website_meta_description`                  | Website meta description               | `text`       |     | ✅    |                                 |
| `website_meta_keywords`                     | Website meta keywords                  | `char`       |     | ✅    |                                 |
| `website_meta_og_img`                       | Website opengraph image                | `char`       |     | ✅    |                                 |
| `website_meta_title`                        | Website meta title                     | `char`       |     | ✅    |                                 |
| `website_published`                         | Visible on current website             | `boolean`    |     |       |                                 |
| `website_ribbon_id`                         | Ribbon                                 | `many2one`   |     | ✅    | product.ribbon                  |
| `website_sequence`                          | Website Sequence                       | `integer`    |     | ✅    |                                 |
| `website_size_x`                            | Size X                                 | `integer`    |     | ✅    |                                 |
| `website_size_y`                            | Size Y                                 | `integer`    |     | ✅    |                                 |
| `website_url`                               | Website URL                            | `char`       |     |       |                                 |
| `weight`                                    | Weight                                 | `float`      |     | ✅    |                                 |
| `weight_uom_name`                           | Weight unit of measure label           | `char`       |     |       |                                 |
| `write_date`                                | Last Updated on                        | `datetime`   |     | ✅    |                                 |
| `write_uid`                                 | Last Updated by                        | `many2one`   |     | ✅    | res.users                       |

**Access Rights:**

| Name                           | Group             | Perms     |
| ------------------------------ | ----------------- | --------- |
| product.template purchase_user | Purchase / User   | `R`       |
| product.template.manager       | Products / Create | `R/W/C/D` |
| product.template stock user    | Inventory / User  | `R`       |
| product.template.public        | Role / Portal     | `R`       |
| product.template.public        | Role / Public     | `R`       |
| product.template.public        | Role / User       | `R`       |
| product.template.user          | Role / User       | `R`       |

**Record Rules:**

- **Product multi-company** (Global) `R/W/C/D`
  - Domain:
    ` ['|', ('company_id', 'parent_of', company_ids), ('company_id', '=', False)]`
- **Public product template** (10, 11) `R`
  - Domain: `[('website_published', '=', True), ('sale_ok', '=', True)]`

### 🗃️ `sale.order` — Sales Order

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                              | Label                              | Type        | Req | Store | Relation                    |
| ---------------------------------- | ---------------------------------- | ----------- | --- | ----- | --------------------------- |
| `access_token`                     | Security Token                     | `char`      |     | ✅    |                             |
| `access_url`                       | Portal Access URL                  | `char`      |     |       |                             |
| `access_warning`                   | Access warning                     | `text`      |     |       |                             |
| `activity_calendar_event_id`       | Next Activity Calendar Event       | `many2one`  |     |       | calendar.event              |
| `activity_date_deadline`           | Next Activity Deadline             | `date`      |     |       |                             |
| `activity_exception_decoration`    | Activity Exception Decoration      | `selection` |     |       |                             |
| `activity_exception_icon`          | Icon                               | `char`      |     |       |                             |
| `activity_ids`                     | Activities                         | `one2many`  |     | ✅    | mail.activity               |
| `activity_state`                   | Activity State                     | `selection` |     |       |                             |
| `activity_summary`                 | Next Activity Summary              | `char`      |     |       |                             |
| `activity_type_icon`               | Activity Type Icon                 | `char`      |     |       |                             |
| `activity_type_id`                 | Next Activity Type                 | `many2one`  |     |       | mail.activity.type          |
| `activity_user_id`                 | Responsible User                   | `many2one`  |     |       | res.users                   |
| `amount_delivery`                  | Delivery Amount                    | `monetary`  |     |       |                             |
| `amount_invoiced`                  | Already invoiced                   | `monetary`  |     |       |                             |
| `amount_paid`                      | Payment Transactions Amount        | `float`     |     |       |                             |
| `amount_tax`                       | Taxes                              | `monetary`  |     | ✅    |                             |
| `amount_to_invoice`                | Un-invoiced Balance                | `monetary`  |     |       |                             |
| `amount_total`                     | Total                              | `monetary`  |     | ✅    |                             |
| `amount_undiscounted`              | Amount Before Discount             | `float`     |     |       |                             |
| `amount_untaxed`                   | Untaxed Amount                     | `monetary`  |     | ✅    |                             |
| `attendee_count`                   | Attendee Count                     | `integer`   |     |       |                             |
| `authorized_transaction_ids`       | Authorized Transactions            | `many2many` |     |       | payment.transaction         |
| `available_quotation_document_ids` | Available Quotation Documents      | `many2many` |     |       | quotation.document          |
| `campaign_id`                      | Campaign                           | `many2one`  |     | ✅    | utm.campaign                |
| `carrier_id`                       | Delivery Method                    | `many2one`  |     | ✅    | delivery.carrier            |
| `cart_quantity`                    | Cart Quantity                      | `integer`   |     |       |                             |
| `cart_recovery_email_sent`         | Cart recovery email already sent   | `boolean`   |     | ✅    |                             |
| `client_order_ref`                 | Customer Reference                 | `char`      |     | ✅    |                             |
| `commitment_date`                  | Delivery Date                      | `datetime`  |     | ✅    |                             |
| `company_id`                       | Company                            | `many2one`  | ✅  | ✅    | res.company                 |
| `company_price_include`            | Default Sales Price Include        | `selection` |     |       |                             |
| `country_code`                     | Country code                       | `char`      |     |       |                             |
| `create_date`                      | Creation Date                      | `datetime`  |     | ✅    |                             |
| `create_uid`                       | Created by                         | `many2one`  |     | ✅    | res.users                   |
| `currency_id`                      | Currency                           | `many2one`  |     | ✅    | res.currency                |
| `currency_rate`                    | Currency Rate                      | `float`     |     | ✅    |                             |
| `customizable_pdf_form_fields`     | Customizable PDF Form Fields       | `json`      |     | ✅    |                             |
| `date_order`                       | Order Date                         | `datetime`  | ✅  | ✅    |                             |
| `delivery_count`                   | Delivery Orders                    | `integer`   |     |       |                             |
| `delivery_message`                 | Delivery Message                   | `char`      |     | ✅    |                             |
| `delivery_set`                     | Delivery Set                       | `boolean`   |     |       |                             |
| `delivery_status`                  | Delivery Status                    | `selection` |     | ✅    |                             |
| `display_name`                     | Display Name                       | `char`      |     |       |                             |
| `duplicated_order_ids`             | Duplicated Order                   | `many2many` |     |       | sale.order                  |
| `effective_date`                   | Effective Date                     | `datetime`  |     | ✅    |                             |
| `expected_date`                    | Expected Date                      | `datetime`  |     |       |                             |
| `expense_count`                    | # of Expenses                      | `integer`   |     |       |                             |
| `expense_ids`                      | Expenses                           | `one2many`  |     | ✅    | hr.expense                  |
| `fiscal_position_id`               | Fiscal Position                    | `many2one`  |     | ✅    | account.fiscal.position     |
| `has_active_pricelist`             | Has Active Pricelist               | `boolean`   |     |       |                             |
| `has_archived_products`            | Has Archived Products              | `boolean`   |     |       |                             |
| `has_authorized_transaction_ids`   | Has Authorized Transactions        | `boolean`   |     |       |                             |
| `has_message`                      | Has Message                        | `boolean`   |     |       |                             |
| `id`                               | ID                                 | `integer`   |     | ✅    |                             |
| `incoterm`                         | Incoterm                           | `many2one`  |     | ✅    | account.incoterms           |
| `incoterm_location`                | Incoterm Location                  | `char`      |     | ✅    |                             |
| `invoice_count`                    | Invoice Count                      | `integer`   |     |       |                             |
| `invoice_ids`                      | Invoices                           | `many2many` |     |       | account.move                |
| `invoice_status`                   | Invoice Status                     | `selection` |     | ✅    |                             |
| `is_abandoned_cart`                | Abandoned Cart                     | `boolean`   |     |       |                             |
| `is_all_service`                   | Service Product                    | `boolean`   |     |       |                             |
| `is_expired`                       | Is Expired                         | `boolean`   |     |       |                             |
| `is_pdf_quote_builder_available`   | Is Pdf Quote Builder Available     | `boolean`   |     |       |                             |
| `journal_id`                       | Invoicing Journal                  | `many2one`  |     | ✅    | account.journal             |
| `json_popover`                     | JSON data for the popover widget   | `char`      |     |       |                             |
| `late_availability`                | Late Availability                  | `boolean`   |     |       |                             |
| `locked`                           | Locked                             | `boolean`   |     | ✅    |                             |
| `medium_id`                        | Medium                             | `many2one`  |     | ✅    | utm.medium                  |
| `message_attachment_count`         | Attachment Count                   | `integer`   |     |       |                             |
| `message_follower_ids`             | Followers                          | `one2many`  |     | ✅    | mail.followers              |
| `message_has_error`                | Message Delivery error             | `boolean`   |     |       |                             |
| `message_has_error_counter`        | Number of errors                   | `integer`   |     |       |                             |
| `message_has_sms_error`            | SMS Delivery error                 | `boolean`   |     |       |                             |
| `message_ids`                      | Messages                           | `one2many`  |     | ✅    | mail.message                |
| `message_is_follower`              | Is Follower                        | `boolean`   |     |       |                             |
| `message_needaction`               | Action Needed                      | `boolean`   |     |       |                             |
| `message_needaction_counter`       | Number of Actions                  | `integer`   |     |       |                             |
| `message_partner_ids`              | Followers (Partners)               | `many2many` |     |       | res.partner                 |
| `my_activity_date_deadline`        | My Activity Deadline               | `date`      |     |       |                             |
| `name`                             | Order Reference                    | `char`      | ✅  | ✅    |                             |
| `note`                             | Terms and conditions               | `html`      |     | ✅    |                             |
| `only_services`                    | Only Services                      | `boolean`   |     |       |                             |
| `opportunity_id`                   | Opportunity                        | `many2one`  |     | ✅    | crm.lead                    |
| `order_line`                       | Order Lines                        | `one2many`  |     | ✅    | sale.order.line             |
| `origin`                           | Source Document                    | `char`      |     | ✅    |                             |
| `partner_credit_warning`           | Partner Credit Warning             | `text`      |     |       |                             |
| `partner_id`                       | Customer                           | `many2one`  | ✅  | ✅    | res.partner                 |
| `partner_invoice_id`               | Invoice Address                    | `many2one`  | ✅  | ✅    | res.partner                 |
| `partner_shipping_id`              | Delivery Address                   | `many2one`  | ✅  | ✅    | res.partner                 |
| `payment_term_id`                  | Payment Terms                      | `many2one`  |     | ✅    | account.payment.term        |
| `pending_email_template_id`        | Pending Email Template             | `many2one`  |     | ✅    | mail.template               |
| `picking_ids`                      | Transfers                          | `one2many`  |     | ✅    | stock.picking               |
| `picking_policy`                   | Shipping Policy                    | `selection` | ✅  | ✅    |                             |
| `pickup_location_data`             | Pickup Location Data               | `json`      |     | ✅    |                             |
| `preferred_payment_method_line_id` | Payment Method                     | `many2one`  |     | ✅    | account.payment.method.line |
| `prepayment_percent`               | Prepayment percentage              | `float`     |     | ✅    |                             |
| `pricelist_id`                     | Pricelist                          | `many2one`  |     | ✅    | product.pricelist           |
| `purchase_order_count`             | Number of Purchase Order Generated | `integer`   |     |       |                             |
| `quotation_document_ids`           | Headers/Footers                    | `many2many` |     | ✅    | quotation.document          |
| `rating_ids`                       | Ratings                            | `one2many`  |     | ✅    | rating.rating               |
| `recompute_delivery_price`         | Delivery cost should be recomputed | `boolean`   |     | ✅    |                             |
| `reference`                        | Payment Ref.                       | `char`      |     | ✅    |                             |
| `require_payment`                  | Online payment                     | `boolean`   |     | ✅    |                             |
| `require_signature`                | Online signature                   | `boolean`   |     | ✅    |                             |
| `sale_order_template_id`           | Quotation Template                 | `many2one`  |     | ✅    | sale.order.template         |
| `sale_warning_text`                | Sale Warning                       | `text`      |     |       |                             |
| `shipping_weight`                  | Shipping Weight                    | `float`     |     | ✅    |                             |
| `shop_warning`                     | Warning                            | `char`      |     | ✅    |                             |
| `show_json_popover`                | Has late picking                   | `boolean`   |     |       |                             |
| `show_update_fpos`                 | Has Fiscal Position Changed        | `boolean`   |     |       |                             |
| `show_update_pricelist`            | Has Pricelist Changed              | `boolean`   |     |       |                             |
| `signature`                        | Signature                          | `binary`    |     | ✅    |                             |
| `signed_by`                        | Signed By                          | `char`      |     | ✅    |                             |
| `signed_on`                        | Signed On                          | `datetime`  |     | ✅    |                             |
| `source_id`                        | Source                             | `many2one`  |     | ✅    | utm.source                  |
| `state`                            | Status                             | `selection` |     | ✅    |                             |
| `stock_reference_ids`              | References                         | `many2many` |     | ✅    | stock.reference             |
| `tag_ids`                          | Tags                               | `many2many` |     | ✅    | crm.tag                     |
| `tax_calculation_rounding_method`  | Tax Calculation Rounding Method    | `selection` |     |       |                             |
| `tax_country_id`                   | Tax Country                        | `many2one`  |     |       | res.country                 |
| `tax_totals`                       | Tax Totals                         | `binary`    |     |       |                             |
| `team_id`                          | Sales Team                         | `many2one`  |     | ✅    | crm.team                    |
| `terms_type`                       | Terms & Conditions format          | `selection` |     |       |                             |
| `transaction_ids`                  | Transactions                       | `many2many` |     | ✅    | payment.transaction         |
| `type_name`                        | Type Name                          | `char`      |     |       |                             |
| `user_id`                          | Salesperson                        | `many2one`  |     | ✅    | res.users                   |
| `validity_date`                    | Expiration                         | `date`      |     | ✅    |                             |
| `warehouse_id`                     | Warehouse                          | `many2one`  |     | ✅    | stock.warehouse             |
| `website_id`                       | Website                            | `many2one`  |     | ✅    | website                     |
| `website_message_ids`              | Website Messages                   | `one2many`  |     | ✅    | mail.message                |
| `website_order_line`               | Order Lines displayed on Website   | `one2many`  |     |       | sale.order.line             |
| `write_date`                       | Last Updated on                    | `datetime`  |     | ✅    |                             |
| `write_uid`                        | Last Updated by                    | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                    | Group                            | Perms     |
| ----------------------- | -------------------------------- | --------- |
| sale.order              | Sales / User: Own Documents Only | `R/W/C`   |
| sale.order.manager      | Sales / Administrator            | `R/W/C/D` |
| sale.order              | Accounting / Invoicing           | `R/W`     |
| sale.order.accountant   | Contact / Accountant             | `R/W`     |
| sale.order stock worker | Inventory / User                 | `R/W`     |
| sale.order.accountant   | Auditor                          | `R`       |
| sale.order.portal       | Role / Portal                    | `R`       |

**Record Rules:**

- **Sales Order multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`
- **Portal Personal Quotations/Sales Orders** (10) `R/W/D`
  - Domain: `[('partner_id','child_of',[user.commercial_partner_id.id])]`
- **Personal Orders** (25) `R/W/C/D`
  - Domain: `['|',('user_id','=',user.id),('user_id','=',False)]`
- **All Orders** (26) `R/W/C/D`
  - Domain: `[(1,'=',1)]`

### 🗃️ `hr.expense.split` — Expense Split

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                               | Label                                        | Type        | Req | Store | Relation                 |
| ----------------------------------- | -------------------------------------------- | ----------- | --- | ----- | ------------------------ |
| `analytic_distribution`             | Analytic Distribution                        | `json`      |     | ✅    |                          |
| `analytic_precision`                | Analytic Precision                           | `integer`   |     |       |                          |
| `approval_date`                     | Approval Date                                | `datetime`  |     | ✅    |                          |
| `approval_state`                    | Approval State                               | `selection` |     | ✅    |                          |
| `can_be_reinvoiced`                 | Can be reinvoiced                            | `boolean`   |     |       |                          |
| `company_id`                        | Company                                      | `many2one`  |     | ✅    | res.company              |
| `create_date`                       | Created on                                   | `datetime`  |     | ✅    |                          |
| `create_uid`                        | Created by                                   | `many2one`  |     | ✅    | res.users                |
| `currency_id`                       | Currency                                     | `many2one`  |     | ✅    | res.currency             |
| `display_name`                      | Display Name                                 | `char`      |     |       |                          |
| `distribution_analytic_account_ids` | Distribution Analytic Account                | `many2many` |     |       | account.analytic.account |
| `employee_id`                       | Employee                                     | `many2one`  | ✅  | ✅    | hr.employee              |
| `expense_id`                        | Expense                                      | `many2one`  |     | ✅    | hr.expense               |
| `id`                                | ID                                           | `integer`   |     | ✅    |                          |
| `manager_id`                        | Manager                                      | `many2one`  |     | ✅    | res.users                |
| `name`                              | Description                                  | `char`      | ✅  | ✅    |                          |
| `product_has_cost`                  | Is product with non zero cost selected       | `boolean`   |     | ✅    |                          |
| `product_has_tax`                   | Whether tax is defined on a selected product | `boolean`   |     |       |                          |
| `product_id`                        | Product                                      | `many2one`  | ✅  | ✅    | product.product          |
| `sale_order_id`                     | Customer to Reinvoice                        | `many2one`  |     | ✅    | sale.order               |
| `tax_amount_currency`               | Tax amount in Currency                       | `monetary`  |     |       |                          |
| `tax_ids`                           | Tax                                          | `many2many` |     | ✅    | account.tax              |
| `total_amount_currency`             | Total In Currency                            | `monetary`  | ✅  | ✅    |                          |
| `wizard_id`                         | Wizard                                       | `many2one`  |     | ✅    | hr.expense.split.wizard  |
| `write_date`                        | Last Updated on                              | `datetime`  |     | ✅    |                          |
| `write_uid`                         | Last Updated by                              | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                            | Group       | Perms     |
| ------------------------------- | ----------- | --------- |
| access.hr.expense.split.manager | Role / User | `R/W/C/D` |

### 🗃️ `account.move.line` — Journal Item

Override AccountInvoice_line to add the link to the purchase order line it is related to

**Fields:**

| Field                                          | Label                                    | Type        | Req | Store | Relation                     |
| ---------------------------------------------- | ---------------------------------------- | ----------- | --- | ----- | ---------------------------- |
| `account_code`                                 | Code                                     | `char`      |     |       |                              |
| `account_id`                                   | Account                                  | `many2one`  |     | ✅    | account.account              |
| `account_internal_group`                       | Internal Group                           | `selection` |     |       |                              |
| `account_name`                                 | Account Name                             | `char`      |     |       |                              |
| `account_root_id`                              | Account Root                             | `many2one`  |     |       | account.root                 |
| `account_type`                                 | Internal Type                            | `selection` |     |       |                              |
| `allowed_uom_ids`                              | Allowed Uom                              | `many2many` |     |       | uom.uom                      |
| `amount_currency`                              | Amount in Currency                       | `monetary`  |     | ✅    |                              |
| `amount_residual`                              | Residual Amount                          | `monetary`  |     | ✅    |                              |
| `amount_residual_currency`                     | Residual Amount in Currency              | `monetary`  |     | ✅    |                              |
| `analytic_distribution`                        | Analytic Distribution                    | `json`      |     | ✅    |                              |
| `analytic_line_ids`                            | Analytic lines                           | `one2many`  |     | ✅    | account.analytic.line        |
| `analytic_precision`                           | Analytic Precision                       | `integer`   |     |       |                              |
| `asset_category_id`                            | Asset Category                           | `many2one`  |     |       | account.asset.category       |
| `asset_end_date`                               | Asset End Date                           | `date`      |     | ✅    |                              |
| `asset_mrr`                                    | Monthly Recurring Revenue                | `float`     |     | ✅    |                              |
| `asset_start_date`                             | Asset Start Date                         | `date`      |     | ✅    |                              |
| `balance`                                      | Balance                                  | `monetary`  |     | ✅    |                              |
| `cogs_origin_id`                               | Cogs Origin                              | `many2one`  |     | ✅    | account.move.line            |
| `collapse_composition`                         | Hide Composition                         | `boolean`   |     | ✅    |                              |
| `collapse_prices`                              | Hide Prices                              | `boolean`   |     | ✅    |                              |
| `commercial_partner_country`                   | Commercial Partner Country               | `many2one`  |     |       | res.country                  |
| `company_currency_id`                          | Company Currency                         | `many2one`  |     | ✅    | res.currency                 |
| `company_id`                                   | Company                                  | `many2one`  |     | ✅    | res.company                  |
| `create_date`                                  | Created on                               | `datetime`  |     | ✅    |                              |
| `create_uid`                                   | Created by                               | `many2one`  |     | ✅    | res.users                    |
| `credit`                                       | Credit                                   | `monetary`  |     | ✅    |                              |
| `cumulated_balance`                            | Cumulated Balance                        | `monetary`  |     |       |                              |
| `currency_id`                                  | Currency                                 | `many2one`  | ✅  | ✅    | res.currency                 |
| `currency_rate`                                | Currency Rate                            | `float`     |     |       |                              |
| `date`                                         | Date                                     | `date`      |     | ✅    |                              |
| `date_maturity`                                | Due Date                                 | `date`      |     | ✅    |                              |
| `debit`                                        | Debit                                    | `monetary`  |     | ✅    |                              |
| `deductible_amount`                            | Deductibility                            | `float`     |     | ✅    |                              |
| `discount`                                     | Discount (%)                             | `float`     |     | ✅    |                              |
| `discount_allocation_dirty`                    | Discount Allocation Dirty                | `boolean`   |     |       |                              |
| `discount_allocation_key`                      | Discount Allocation Key                  | `binary`    |     |       |                              |
| `discount_allocation_needed`                   | Discount Allocation Needed               | `binary`    |     |       |                              |
| `discount_amount_currency`                     | Discount amount in Currency              | `monetary`  |     | ✅    |                              |
| `discount_balance`                             | Discount Balance                         | `monetary`  |     | ✅    |                              |
| `discount_date`                                | Discount Date                            | `date`      |     | ✅    |                              |
| `display_name`                                 | Display Name                             | `char`      |     |       |                              |
| `display_type`                                 | Display Type                             | `selection` | ✅  | ✅    |                              |
| `distribution_analytic_account_ids`            | Distribution Analytic Account            | `many2many` |     |       | account.analytic.account     |
| `epd_dirty`                                    | Epd Dirty                                | `boolean`   |     |       |                              |
| `epd_key`                                      | Epd Key                                  | `binary`    |     |       |                              |
| `epd_needed`                                   | Epd Needed                               | `binary`    |     |       |                              |
| `expense_id`                                   | Expense                                  | `many2one`  |     | ✅    | hr.expense                   |
| `extra_tax_data`                               | Extra Tax Data                           | `json`      |     | ✅    |                              |
| `full_reconcile_id`                            | Matching                                 | `many2one`  |     | ✅    | account.full.reconcile       |
| `group_tax_id`                                 | Originator Group of Taxes                | `many2one`  |     | ✅    | account.tax                  |
| `has_invalid_analytics`                        | Has Invalid Analytics                    | `boolean`   |     |       |                              |
| `id`                                           | ID                                       | `integer`   |     | ✅    |                              |
| `invoice_date`                                 | Invoice/Bill Date                        | `date`      |     | ✅    |                              |
| `is_account_reconcile`                         | Account Reconcile                        | `boolean`   |     |       |                              |
| `is_downpayment`                               | Is Downpayment                           | `boolean`   |     | ✅    |                              |
| `is_imported`                                  | Is Imported                              | `boolean`   |     | ✅    |                              |
| `is_refund`                                    | Is Refund                                | `boolean`   |     |       |                              |
| `is_same_currency`                             | Is Same Currency                         | `boolean`   |     |       |                              |
| `is_storno`                                    | Company Storno Accounting                | `boolean`   |     | ✅    |                              |
| `journal_group_id`                             | Ledger                                   | `many2one`  |     |       | account.journal.group        |
| `journal_id`                                   | Journal                                  | `many2one`  |     | ✅    | account.journal              |
| `matched_credit_ids`                           | Matched Credits                          | `one2many`  |     | ✅    | account.partial.reconcile    |
| `matched_debit_ids`                            | Matched Debits                           | `one2many`  |     | ✅    | account.partial.reconcile    |
| `matching_number`                              | Matching #                               | `char`      |     | ✅    |                              |
| `move_id`                                      | Journal Entry                            | `many2one`  | ✅  | ✅    | account.move                 |
| `move_name`                                    | Number                                   | `char`      |     | ✅    |                              |
| `move_type`                                    | Type                                     | `selection` |     |       |                              |
| `name`                                         | Label                                    | `char`      |     | ✅    |                              |
| `need_vehicle`                                 | Need Vehicle                             | `boolean`   |     |       |                              |
| `no_followup`                                  | No Follow-Up                             | `boolean`   |     | ✅    |                              |
| `parent_id`                                    | Parent Section Line                      | `many2one`  |     |       | account.move.line            |
| `parent_state`                                 | Status                                   | `selection` |     | ✅    |                              |
| `partner_id`                                   | Partner                                  | `many2one`  |     | ✅    | res.partner                  |
| `payment_date`                                 | Next Payment Date                        | `date`      |     |       |                              |
| `payment_id`                                   | Originator Payment                       | `many2one`  |     | ✅    | account.payment              |
| `price_subtotal`                               | Subtotal                                 | `monetary`  |     | ✅    |                              |
| `price_total`                                  | Total                                    | `monetary`  |     | ✅    |                              |
| `price_unit`                                   | Unit Price                               | `float`     |     | ✅    |                              |
| `product_category_id`                          | Product Category                         | `many2one`  |     |       | product.category             |
| `product_id`                                   | Product                                  | `many2one`  |     | ✅    | product.product              |
| `product_uom_id`                               | Unit                                     | `many2one`  |     | ✅    | uom.uom                      |
| `purchase_line_id`                             | Purchase Order Line                      | `many2one`  |     | ✅    | purchase.order.line          |
| `purchase_line_warn_msg`                       | Purchase Line Warn Msg                   | `text`      |     |       |                              |
| `purchase_order_id`                            | Purchase Order                           | `many2one`  |     |       | purchase.order               |
| `quantity`                                     | Quantity                                 | `float`     |     | ✅    |                              |
| `reconciled`                                   | Reconciled                               | `boolean`   |     | ✅    |                              |
| `reconciled_lines_excluding_exchange_diff_ids` | Reconciled Lines Excluding Exchange Diff | `many2many` |     |       | account.move.line            |
| `reconciled_lines_ids`                         | Reconciled Lines                         | `many2many` |     |       | account.move.line            |
| `reconcile_model_id`                           | Reconciliation Model                     | `many2one`  |     | ✅    | account.reconcile.model      |
| `ref`                                          | Reference                                | `char`      |     | ✅    |                              |
| `sale_line_ids`                                | Sales Order Lines                        | `many2many` |     | ✅    | sale.order.line              |
| `sale_line_warn_msg`                           | Sale Line Warn Msg                       | `text`      |     |       |                              |
| `search_account_id`                            | Search Account                           | `many2one`  |     |       | account.account              |
| `sequence`                                     | Sequence                                 | `integer`   |     | ✅    |                              |
| `statement_id`                                 | Statement                                | `many2one`  |     | ✅    | account.bank.statement       |
| `statement_line_id`                            | Originator Statement Line                | `many2one`  |     | ✅    | account.bank.statement.line  |
| `tax_base_amount`                              | Base Amount                              | `monetary`  |     | ✅    |                              |
| `tax_calculation_rounding_method`              | Tax calculation rounding method          | `selection` |     |       |                              |
| `tax_group_id`                                 | Originator tax group                     | `many2one`  |     | ✅    | account.tax.group            |
| `tax_ids`                                      | Taxes                                    | `many2many` |     | ✅    | account.tax                  |
| `tax_line_id`                                  | Originator Tax                           | `many2one`  |     | ✅    | account.tax                  |
| `tax_repartition_line_id`                      | Originator Tax Distribution Line         | `many2one`  |     | ✅    | account.tax.repartition.line |
| `tax_tag_ids`                                  | Tags                                     | `many2many` |     | ✅    | account.account.tag          |
| `term_key`                                     | Term Key                                 | `binary`    |     |       |                              |
| `translated_product_name`                      | Translated Product Name                  | `text`      |     |       |                              |
| `vehicle_id`                                   | Vehicle                                  | `many2one`  |     | ✅    | fleet.vehicle                |
| `vehicle_log_service_ids`                      | Vehicle Log Service                      | `one2many`  |     | ✅    | fleet.vehicle.log.services   |
| `write_date`                                   | Last Updated on                          | `datetime`  |     | ✅    |                              |
| `write_uid`                                    | Last Updated by                          | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                                  | Group                            | Perms     |
| ------------------------------------- | -------------------------------- | --------- |
| account_move_line salesman            | Sales / User: Own Documents Only | `R`       |
| account.move.line invoice             | Accounting / Invoicing           | `R/W/C/D` |
| account.move.line manager             | Accounting / Advisor             | `R`       |
| account.move.line                     | Purchase / User                  | `R/W/C`   |
| account.move.line                     | Purchase / Administrator         | `R/W/C/D` |
| account.move.line.hr.expense.approver | Expenses / Team Approver         | `R`       |
| account.move.line readonly            | Auditor                          | `R`       |
| account.move.line.portal              | Role / Portal                    | `R`       |

**Record Rules:**

- **Entry lines** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`
- **All Journal Items** (37) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Portal Invoice Lines** (10) `R/W/C/D`
  - Domain:
    `[('parent_state', 'not in', ('cancel', 'draft')), ('move_id.move_type', 'in', ('out_invoice', 'out_refund', 'in_invoice', 'in_refund')), ('move_id.partner_id','child_of',[user.commercial_partner_id.id])]`
- **Readonly Move Line** (36) `R`
  - Domain: `[(1, '=', 1)]`
- **Readonly Move Line** (37) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Expense Team Approver Account Move Line** (76) `R/W/C/D`
  - Domain: `[('expense_id', '!=', False)]`
- **Purchase User Account Move Line** (86) `R/W/C/D`
  - Domain: `[('move_id.move_type', 'in', ('in_invoice', 'in_refund', 'in_receipt'))]`
- **Personal Invoice Lines** (25) `R/W/C/D`
  - Domain:
    `[('move_id.move_type', 'in', ('out_invoice', 'out_refund')), '|', ('move_id.invoice_user_id', '=', user.id), ('move_id.invoice_user_id', '=', False)]`
- **All Invoice Lines** (26) `R/W/C/D`
  - Domain: `[('move_id.move_type', 'in', ('out_invoice', 'out_refund'))]`

### 🗃️ `sale.order.line` — Sales Order Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                    | Label                              | Type        | Req | Store | Relation                         |
| ---------------------------------------- | ---------------------------------- | ----------- | --- | ----- | -------------------------------- |
| `allowed_uom_ids`                        | Allowed Uom                        | `many2many` |     |       | uom.uom                          |
| `amount_invoiced`                        | Invoiced Amount                    | `monetary`  |     |       |                                  |
| `amount_to_invoice`                      | Un-invoiced Balance                | `monetary`  |     |       |                                  |
| `amount_to_invoice_at_date`              | Amount                             | `float`     |     |       |                                  |
| `analytic_distribution`                  | Analytic Distribution              | `json`      |     | ✅    |                                  |
| `analytic_line_ids`                      | Analytic lines                     | `one2many`  |     | ✅    | account.analytic.line            |
| `analytic_precision`                     | Analytic Precision                 | `integer`   |     |       |                                  |
| `available_product_document_ids`         | Available Product Documents        | `many2many` |     |       | product.document                 |
| `categ_id`                               | Product Category                   | `many2one`  |     |       | product.category                 |
| `collapse_composition`                   | Collapse Composition               | `boolean`   |     | ✅    |                                  |
| `collapse_prices`                        | Collapse Prices                    | `boolean`   |     | ✅    |                                  |
| `combo_item_id`                          | Combo Item                         | `many2one`  |     | ✅    | product.combo.item               |
| `company_id`                             | Company                            | `many2one`  |     | ✅    | res.company                      |
| `company_price_include`                  | Default Sales Price Include        | `selection` |     |       |                                  |
| `create_date`                            | Created on                         | `datetime`  |     | ✅    |                                  |
| `create_uid`                             | Created by                         | `many2one`  |     | ✅    | res.users                        |
| `currency_id`                            | Currency                           | `many2one`  |     | ✅    | res.currency                     |
| `customer_lead`                          | Lead Time                          | `float`     | ✅  | ✅    |                                  |
| `discount`                               | Discount (%)                       | `float`     |     | ✅    |                                  |
| `display_name`                           | Display Name                       | `char`      |     |       |                                  |
| `display_qty_widget`                     | Display Qty Widget                 | `boolean`   |     |       |                                  |
| `display_type`                           | Display Type                       | `selection` |     | ✅    |                                  |
| `distribution_analytic_account_ids`      | Distribution Analytic Account      | `many2many` |     |       | account.analytic.account         |
| `event_id`                               | Event                              | `many2one`  |     | ✅    | event.event                      |
| `event_slot_id`                          | Slot                               | `many2one`  |     | ✅    | event.slot                       |
| `event_ticket_id`                        | Ticket Type                        | `many2one`  |     | ✅    | event.event.ticket               |
| `expense_ids`                            | Expenses                           | `one2many`  |     | ✅    | hr.expense                       |
| `extra_tax_data`                         | Extra Tax Data                     | `json`      |     | ✅    |                                  |
| `forecast_expected_date`                 | Forecast Expected Date             | `datetime`  |     |       |                                  |
| `free_qty_today`                         | Free Qty Today                     | `float`     |     |       |                                  |
| `id`                                     | ID                                 | `integer`   |     | ✅    |                                  |
| `invoice_lines`                          | Invoice Lines                      | `many2many` |     | ✅    | account.move.line                |
| `invoice_status`                         | Invoice Status                     | `selection` |     | ✅    |                                  |
| `is_configurable_product`                | Is the product configurable?       | `boolean`   |     |       |                                  |
| `is_delivery`                            | Is a Delivery                      | `boolean`   |     | ✅    |                                  |
| `is_downpayment`                         | Is a down payment                  | `boolean`   |     | ✅    |                                  |
| `is_expense`                             | Is expense                         | `boolean`   |     | ✅    |                                  |
| `is_mto`                                 | Is Mto                             | `boolean`   |     |       |                                  |
| `is_multi_slots`                         | Is Multi Slots                     | `boolean`   |     |       |                                  |
| `is_optional`                            | Optional Line                      | `boolean`   |     | ✅    |                                  |
| `is_product_archived`                    | Is Product Archived                | `boolean`   |     |       |                                  |
| `is_storable`                            | Track Inventory                    | `boolean`   |     |       |                                  |
| `linked_line_id`                         | Linked Order Line                  | `many2one`  |     | ✅    | sale.order.line                  |
| `linked_line_ids`                        | Linked Order Lines                 | `one2many`  |     | ✅    | sale.order.line                  |
| `linked_virtual_id`                      | Linked Virtual                     | `char`      |     | ✅    |                                  |
| `move_ids`                               | Stock Moves                        | `one2many`  |     | ✅    | stock.move                       |
| `name`                                   | Description                        | `text`      | ✅  | ✅    |                                  |
| `name_short`                             | Name Short                         | `char`      |     |       |                                  |
| `order_id`                               | Order Reference                    | `many2one`  | ✅  | ✅    | sale.order                       |
| `order_partner_id`                       | Customer                           | `many2one`  |     | ✅    | res.partner                      |
| `parent_id`                              | Parent Section Line                | `many2one`  |     |       | sale.order.line                  |
| `pricelist_item_id`                      | Pricelist Item                     | `many2one`  |     |       | product.pricelist.item           |
| `price_reduce_taxexcl`                   | Price Reduce Tax excl              | `monetary`  |     | ✅    |                                  |
| `price_reduce_taxinc`                    | Price Reduce Tax incl              | `monetary`  |     | ✅    |                                  |
| `price_subtotal`                         | Subtotal                           | `monetary`  |     | ✅    |                                  |
| `price_tax`                              | Total Tax                          | `float`     |     | ✅    |                                  |
| `price_total`                            | Total                              | `monetary`  |     | ✅    |                                  |
| `price_unit`                             | Unit Price                         | `float`     | ✅  | ✅    |                                  |
| `product_custom_attribute_value_ids`     | Custom Values                      | `one2many`  |     | ✅    | product.attribute.custom.value   |
| `product_document_ids`                   | Product Documents                  | `many2many` |     | ✅    | product.document                 |
| `product_id`                             | Product                            | `many2one`  |     | ✅    | product.product                  |
| `product_no_variant_attribute_value_ids` | Extra Values                       | `many2many` |     | ✅    | product.template.attribute.value |
| `product_qty`                            | Product Qty                        | `float`     |     |       |                                  |
| `product_template_attribute_value_ids`   | Attribute Values                   | `many2many` |     |       | product.template.attribute.value |
| `product_template_id`                    | Product Template                   | `many2one`  |     |       | product.template                 |
| `product_type`                           | Product Type                       | `selection` |     |       |                                  |
| `product_uom_id`                         | Unit                               | `many2one`  |     | ✅    | uom.uom                          |
| `product_uom_qty`                        | Quantity                           | `float`     | ✅  | ✅    |                                  |
| `product_uom_readonly`                   | Product Uom Readonly               | `boolean`   |     |       |                                  |
| `product_updatable`                      | Can Edit Product                   | `boolean`   |     |       |                                  |
| `purchase_line_count`                    | Number of generated purchase items | `integer`   |     |       |                                  |
| `purchase_line_ids`                      | Generated Purchase Lines           | `one2many`  |     | ✅    | purchase.order.line              |
| `qty_available_today`                    | Qty Available Today                | `float`     |     |       |                                  |
| `qty_delivered`                          | Delivery Quantity                  | `float`     |     | ✅    |                                  |
| `qty_delivered_at_date`                  | Delivered                          | `float`     |     |       |                                  |
| `qty_delivered_method`                   | Method to update delivered qty     | `selection` |     | ✅    |                                  |
| `qty_invoiced`                           | Invoiced Quantity                  | `float`     |     | ✅    |                                  |
| `qty_invoiced_at_date`                   | Invoiced                           | `float`     |     |       |                                  |
| `qty_invoiced_posted`                    | Invoiced Quantity (posted)         | `float`     |     |       |                                  |
| `qty_to_deliver`                         | Qty To Deliver                     | `float`     |     |       |                                  |
| `qty_to_invoice`                         | Quantity To Invoice                | `float`     |     | ✅    |                                  |
| `recompute_delivery_price`               | Delivery cost should be recomputed | `boolean`   |     |       |                                  |
| `registration_ids`                       | Registrations                      | `one2many`  |     | ✅    | event.registration               |
| `route_ids`                              | Routes                             | `many2many` |     | ✅    | stock.route                      |
| `sale_line_warn_msg`                     | Sale Line Warn Msg                 | `text`      |     |       |                                  |
| `salesman_id`                            | Salesperson                        | `many2one`  |     | ✅    | res.users                        |
| `scheduled_date`                         | Scheduled Date                     | `datetime`  |     |       |                                  |
| `selected_combo_items`                   | Selected Combo Items               | `char`      |     |       |                                  |
| `sequence`                               | Sequence                           | `integer`   |     | ✅    |                                  |
| `service_tracking`                       | Create on Order                    | `selection` |     |       |                                  |
| `shop_warning`                           | Warning                            | `char`      |     | ✅    |                                  |
| `state`                                  | Order Status                       | `selection` |     | ✅    |                                  |
| `tax_calculation_rounding_method`        | Tax calculation rounding method    | `selection` |     |       |                                  |
| `tax_country_id`                         | Tax Country                        | `many2one`  |     |       | res.country                      |
| `tax_ids`                                | Taxes                              | `many2many` |     | ✅    | account.tax                      |
| `technical_price_unit`                   | Technical Price Unit               | `float`     |     | ✅    |                                  |
| `translated_product_name`                | Translated Product Name            | `text`      |     |       |                                  |
| `untaxed_amount_invoiced`                | Untaxed Invoiced Amount            | `monetary`  |     | ✅    |                                  |
| `untaxed_amount_to_invoice`              | Untaxed Amount To Invoice          | `monetary`  |     | ✅    |                                  |
| `virtual_available_at_date`              | Virtual Available At Date          | `float`     |     |       |                                  |
| `virtual_id`                             | Virtual                            | `char`      |     | ✅    |                                  |
| `warehouse_id`                           | Warehouse                          | `many2one`  |     | ✅    | stock.warehouse                  |
| `write_date`                             | Last Updated on                    | `datetime`  |     | ✅    |                                  |
| `write_uid`                              | Last Updated by                    | `many2one`  |     | ✅    | res.users                        |

**Access Rights:**

| Name                         | Group                            | Perms     |
| ---------------------------- | -------------------------------- | --------- |
| sale.order.line              | Sales / User: Own Documents Only | `R/W/C/D` |
| sale.order.line              | Accounting / Invoicing           | `R/W`     |
| sale.order.line accountant   | Contact / Accountant             | `R/W`     |
| sale.order.line stock worker | Inventory / User                 | `R/W`     |
| sale.order.line accountant   | Auditor                          | `R`       |
| sale.order.line.portal       | Role / Portal                    | `R`       |

**Record Rules:**

- **Sales Order Line multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`
- **Portal Sales Orders Line** (10) `R/W/C/D`
  - Domain: `[('order_id.partner_id','child_of',[user.commercial_partner_id.id])]`
- **Personal Order Lines** (25) `R/W/C/D`
  - Domain: `['|',('salesman_id','=',user.id),('salesman_id','=',False)]`
- **All Orders Lines** (26) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Stock User Sales Orders Line** (58) `R`
  - Domain: `[(1, '=', 1)]`
