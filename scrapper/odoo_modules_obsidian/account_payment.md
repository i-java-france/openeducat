---
title: "Payment - Account"
module: "account_payment"
state: "installed"
version: "19.0.2.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Accounting"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/__________]
---

# 🟢 Payment - Account

> **Module:** `account_payment` | **Version:** `19.0.2.0` **Category:** Accounting |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[account]] [[payment]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `Invoicing/Configuration/Online Payments/Payment Methods`
- `Invoicing/Configuration/Online Payments/Payment Providers`
- `Invoicing/Configuration/Online Payments/Payment Tokens`
- `Invoicing/Configuration/Online Payments/Payment Transactions`

### Views

- `* INHERIT Invoice Payment Form (qweb)`
- `* INHERIT Invoice error display: payment errors (qweb)`
- `* INHERIT Invoice success display: payment success (qweb)`
- `* INHERIT Overdue invoices (qweb)`
- `* INHERIT Payment on My Invoices (qweb)`
- `* INHERIT Payment on My Invoices (qweb)`
- `* INHERIT Portal layout: overdue invoices (qweb)`
- `* INHERIT account.journal.form.inherit.payment (form)`
- `* INHERIT account.move.view.form.inherit.payment (form)`
- `* INHERIT account.payment.register.form.inherit.payment (form)`
- `* INHERIT account_payment.portal_docs_entry (qweb)`
- `* INHERIT payment.link.wizard.form.inherit.account_payment (form)`
- `* INHERIT payment.provider.form (form)`
- `* INHERIT payment.transaction.form (form)`
- `* INHERIT res.config.settings.view.form.inherit.account (form)`
- `* INHERIT view.account.payment.form.inherit.payment (form)`
- `Invoice Paid (qweb)`
- `Invoice Payment (qweb)`
- `Overdue payments (qweb)`
- `payment.refund.wizard.form (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**11 model(s) defined by this module:**

### 🗃️ `account.journal` — Journal

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                       | Label                                 | Type        | Req | Store | Relation                    |
| ------------------------------------------- | ------------------------------------- | ----------- | --- | ----- | --------------------------- |
| `access_token`                              | Security Token                        | `char`      |     | ✅    |                             |
| `access_url`                                | Portal Access URL                     | `char`      |     |       |                             |
| `access_warning`                            | Access warning                        | `text`      |     |       |                             |
| `account_fiscal_country_group_codes`        | Account Fiscal Country Group Codes    | `json`      |     |       |                             |
| `accounting_date`                           | Accounting Date                       | `date`      |     |       |                             |
| `active`                                    | Active                                | `boolean`   |     | ✅    |                             |
| `activity_calendar_event_id`                | Next Activity Calendar Event          | `many2one`  |     |       | calendar.event              |
| `activity_date_deadline`                    | Next Activity Deadline                | `date`      |     |       |                             |
| `activity_exception_decoration`             | Activity Exception Decoration         | `selection` |     |       |                             |
| `activity_exception_icon`                   | Icon                                  | `char`      |     |       |                             |
| `activity_ids`                              | Activities                            | `one2many`  |     | ✅    | mail.activity               |
| `activity_state`                            | Activity State                        | `selection` |     |       |                             |
| `activity_summary`                          | Next Activity Summary                 | `char`      |     |       |                             |
| `activity_type_icon`                        | Activity Type Icon                    | `char`      |     |       |                             |
| `activity_type_id`                          | Next Activity Type                    | `many2one`  |     |       | mail.activity.type          |
| `activity_user_id`                          | Responsible User                      | `many2one`  |     |       | res.users                   |
| `alias_defaults`                            | Default Values                        | `text`      |     |       |                             |
| `alias_domain`                              | Alias Domain Name                     | `char`      |     |       |                             |
| `alias_domain_id`                           | Alias Domain                          | `many2one`  |     |       | mail.alias.domain           |
| `alias_email`                               | Email Alias                           | `char`      |     |       |                             |
| `alias_id`                                  | Alias                                 | `many2one`  |     | ✅    | mail.alias                  |
| `alias_name`                                | Alias Name                            | `char`      |     |       |                             |
| `available_invoice_template_pdf_report_ids` | Available Invoice Template Pdf Report | `one2many`  |     |       | ir.actions.report           |
| `available_payment_method_ids`              | Available Payment Method              | `many2many` |     |       | account.payment.method      |
| `bank_acc_number`                           | Account Number                        | `char`      |     |       |                             |
| `bank_account_id`                           | Bank Account                          | `many2one`  |     | ✅    | res.partner.bank            |
| `bank_id`                                   | Bank                                  | `many2one`  |     |       | res.bank                    |
| `bank_statements_source`                    | Bank Feeds                            | `selection` |     | ✅    |                             |
| `code`                                      | Sequence Prefix                       | `char`      | ✅  | ✅    |                             |
| `color`                                     | Color Index                           | `integer`   |     | ✅    |                             |
| `company_id`                                | Company                               | `many2one`  | ✅  | ✅    | res.company                 |
| `company_partner_id`                        | Account Holder                        | `many2one`  |     |       | res.partner                 |
| `country_code`                              | Country Code                          | `char`      |     |       |                             |
| `create_date`                               | Created on                            | `datetime`  |     | ✅    |                             |
| `create_uid`                                | Created by                            | `many2one`  |     | ✅    | res.users                   |
| `currency_id`                               | Currency                              | `many2one`  |     | ✅    | res.currency                |
| `current_statement_balance`                 | Current Statement Balance             | `monetary`  |     |       |                             |
| `default_account_id`                        | Default Account                       | `many2one`  |     | ✅    | account.account             |
| `default_account_type`                      | Default Account Type                  | `char`      |     |       |                             |
| `display_alias_fields`                      | Display Alias Fields                  | `boolean`   |     |       |                             |
| `display_invoice_template_pdf_report_id`    | Display Invoice Template Pdf Report   | `boolean`   |     |       |                             |
| `display_name`                              | Display Name                          | `char`      |     |       |                             |
| `entries_count`                             | Entries Count                         | `integer`   |     |       |                             |
| `has_entries`                               | Has Entries                           | `boolean`   |     |       |                             |
| `has_invalid_statements`                    | Has Invalid Statements                | `boolean`   |     |       |                             |
| `has_message`                               | Has Message                           | `boolean`   |     |       |                             |
| `has_posted_entries`                        | Has Posted Entries                    | `boolean`   |     |       |                             |
| `has_sequence_holes`                        | Has Sequence Holes                    | `boolean`   |     |       |                             |
| `has_statement_lines`                       | Has Statement Lines                   | `boolean`   |     |       |                             |
| `has_unhashed_entries`                      | Unhashed Entries                      | `boolean`   |     |       |                             |
| `id`                                        | ID                                    | `integer`   |     | ✅    |                             |
| `inbound_payment_method_line_ids`           | Inbound Payment Methods               | `one2many`  |     | ✅    | account.payment.method.line |
| `incoming_einvoice_notification_email`      | Send Copy To                          | `char`      |     | ✅    |                             |
| `invoice_reference_model`                   | Communication Standard                | `selection` | ✅  | ✅    |                             |
| `invoice_reference_type`                    | Communication Type                    | `selection` | ✅  | ✅    |                             |
| `invoice_template_pdf_report_id`            | Invoice report                        | `many2one`  |     | ✅    | ir.actions.report           |
| `is_self_billing`                           | Self Billing                          | `boolean`   |     | ✅    |                             |
| `journal_group_ids`                         | Ledger Group                          | `many2many` |     | ✅    | account.journal.group       |
| `json_activity_data`                        | Json Activity Data                    | `text`      |     |       |                             |
| `kanban_dashboard`                          | Kanban Dashboard                      | `text`      |     |       |                             |
| `kanban_dashboard_graph`                    | Kanban Dashboard Graph                | `text`      |     |       |                             |
| `last_statement_id`                         | Last Statement                        | `many2one`  |     |       | account.bank.statement      |
| `loss_account_id`                           | Loss Account                          | `many2one`  |     | ✅    | account.account             |
| `message_attachment_count`                  | Attachment Count                      | `integer`   |     |       |                             |
| `message_follower_ids`                      | Followers                             | `one2many`  |     | ✅    | mail.followers              |
| `message_has_error`                         | Message Delivery error                | `boolean`   |     |       |                             |
| `message_has_error_counter`                 | Number of errors                      | `integer`   |     |       |                             |
| `message_has_sms_error`                     | SMS Delivery error                    | `boolean`   |     |       |                             |
| `message_ids`                               | Messages                              | `one2many`  |     | ✅    | mail.message                |
| `message_is_follower`                       | Is Follower                           | `boolean`   |     |       |                             |
| `message_needaction`                        | Action Needed                         | `boolean`   |     |       |                             |
| `message_needaction_counter`                | Number of Actions                     | `integer`   |     |       |                             |
| `message_partner_ids`                       | Followers (Partners)                  | `many2many` |     |       | res.partner                 |
| `my_activity_date_deadline`                 | My Activity Deadline                  | `date`      |     |       |                             |
| `name`                                      | Journal Name                          | `char`      | ✅  | ✅    |                             |
| `name_placeholder`                          | Name Placeholder                      | `char`      |     |       |                             |
| `non_deductible_account_id`                 | Private Share Account                 | `many2one`  |     | ✅    | account.account             |
| `outbound_payment_method_line_ids`          | Outbound Payment Methods              | `one2many`  |     | ✅    | account.payment.method.line |
| `payment_sequence`                          | Dedicated Payment Sequence            | `boolean`   |     | ✅    |                             |
| `profit_account_id`                         | Profit Account                        | `many2one`  |     | ✅    | account.account             |
| `rating_ids`                                | Ratings                               | `one2many`  |     | ✅    | rating.rating               |
| `refund_sequence`                           | Dedicated Credit Note Sequence        | `boolean`   |     | ✅    |                             |
| `restrict_mode_hash_table`                  | Secure Posted Entries with Hash       | `boolean`   |     | ✅    |                             |
| `selected_payment_method_codes`             | Selected Payment Method Codes         | `char`      |     |       |                             |
| `sequence`                                  | Sequence                              | `integer`   |     | ✅    |                             |
| `sequence_override_regex`                   | Sequence Override Regex               | `text`      |     | ✅    |                             |
| `show_fetch_in_einvoices_button`            | Show E-Invoice Buttons                | `boolean`   |     |       |                             |
| `show_on_dashboard`                         | Show journal on dashboard             | `boolean`   |     | ✅    |                             |
| `show_refresh_out_einvoices_status_button`  | Show E-Invoice Status Buttons         | `boolean`   |     |       |                             |
| `suspense_account_id`                       | Suspense Account                      | `many2one`  |     | ✅    | account.account             |
| `type`                                      | Type                                  | `selection` | ✅  | ✅    |                             |
| `website_message_ids`                       | Website Messages                      | `one2many`  |     | ✅    | mail.message                |
| `write_date`                                | Last Updated on                       | `datetime`  |     | ✅    |                             |
| `write_uid`                                 | Last Updated by                       | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                            | Group                            | Perms     |
| ------------------------------- | -------------------------------- | --------- |
| account.journal sale order.user | Sales / User: Own Documents Only | `R`       |
| account.journal invoice         | Accounting / Invoicing           | `R`       |
| account.journal                 | Accounting / Advisor             | `R/W/C/D` |
| account.journal                 | Purchase / User                  | `R`       |
| account.journal                 | Purchase / Administrator         | `R`       |
| account.journal.user            | Expenses / Team Approver         | `R`       |
| account.journal                 | Inventory / Administrator        | `R/W`     |
| account.journal stock manager   | Inventory / Administrator        | `R`       |
| account.journal                 | Auditor                          | `R`       |

**Record Rules:**

- **Journal multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'parent_of', company_ids)]`

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

### 🗃️ `account.payment` — Payments

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                 | Label                            | Type        | Req | Store | Relation                    |
| ------------------------------------- | -------------------------------- | ----------- | --- | ----- | --------------------------- |
| `activity_calendar_event_id`          | Next Activity Calendar Event     | `many2one`  |     |       | calendar.event              |
| `activity_date_deadline`              | Next Activity Deadline           | `date`      |     |       |                             |
| `activity_exception_decoration`       | Activity Exception Decoration    | `selection` |     |       |                             |
| `activity_exception_icon`             | Icon                             | `char`      |     |       |                             |
| `activity_ids`                        | Activities                       | `one2many`  |     | ✅    | mail.activity               |
| `activity_state`                      | Activity State                   | `selection` |     |       |                             |
| `activity_summary`                    | Next Activity Summary            | `char`      |     |       |                             |
| `activity_type_icon`                  | Activity Type Icon               | `char`      |     |       |                             |
| `activity_type_id`                    | Next Activity Type               | `many2one`  |     |       | mail.activity.type          |
| `activity_user_id`                    | Responsible User                 | `many2one`  |     |       | res.users                   |
| `amount`                              | Amount                           | `monetary`  |     | ✅    |                             |
| `amount_available_for_refund`         | Amount Available For Refund      | `monetary`  |     |       |                             |
| `amount_company_currency_signed`      | Amount Company Currency Signed   | `monetary`  |     | ✅    |                             |
| `amount_signed`                       | Amount Signed                    | `monetary`  |     |       |                             |
| `attachment_ids`                      | Attachments                      | `one2many`  |     | ✅    | ir.attachment               |
| `available_journal_ids`               | Available Journal                | `many2many` |     |       | account.journal             |
| `available_partner_bank_ids`          | Available Partner Bank           | `many2many` |     |       | res.partner.bank            |
| `available_payment_method_line_ids`   | Available Payment Method Line    | `many2many` |     |       | account.payment.method.line |
| `company_currency_id`                 | Company Currency                 | `many2one`  |     |       | res.currency                |
| `company_id`                          | Company                          | `many2one`  | ✅  | ✅    | res.company                 |
| `country_code`                        | Country Code                     | `char`      |     |       |                             |
| `create_date`                         | Created on                       | `datetime`  |     | ✅    |                             |
| `create_uid`                          | Created by                       | `many2one`  |     | ✅    | res.users                   |
| `currency_id`                         | Currency                         | `many2one`  |     | ✅    | res.currency                |
| `date`                                | Date                             | `date`      | ✅  | ✅    |                             |
| `destination_account_id`              | Destination Account              | `many2one`  |     | ✅    | account.account             |
| `display_name`                        | Display Name                     | `char`      |     |       |                             |
| `duplicate_payment_ids`               | Duplicate Payment                | `many2many` |     |       | account.payment             |
| `expense_ids`                         | Expense                          | `one2many`  |     |       | hr.expense                  |
| `has_message`                         | Has Message                      | `boolean`   |     |       |                             |
| `id`                                  | ID                               | `integer`   |     | ✅    |                             |
| `invoice_ids`                         | Invoices                         | `many2many` |     | ✅    | account.move                |
| `is_donation`                         | Is Donation                      | `boolean`   |     |       |                             |
| `is_matched`                          | Is Matched With a Bank Statement | `boolean`   |     | ✅    |                             |
| `is_reconciled`                       | Is Reconciled                    | `boolean`   |     | ✅    |                             |
| `is_sent`                             | Is Sent                          | `boolean`   |     | ✅    |                             |
| `journal_id`                          | Journal                          | `many2one`  | ✅  | ✅    | account.journal             |
| `memo`                                | Memo                             | `char`      |     | ✅    |                             |
| `message_attachment_count`            | Attachment Count                 | `integer`   |     |       |                             |
| `message_follower_ids`                | Followers                        | `one2many`  |     | ✅    | mail.followers              |
| `message_has_error`                   | Message Delivery error           | `boolean`   |     |       |                             |
| `message_has_error_counter`           | Number of errors                 | `integer`   |     |       |                             |
| `message_has_sms_error`               | SMS Delivery error               | `boolean`   |     |       |                             |
| `message_ids`                         | Messages                         | `one2many`  |     | ✅    | mail.message                |
| `message_is_follower`                 | Is Follower                      | `boolean`   |     |       |                             |
| `message_main_attachment_id`          | Main Attachment                  | `many2one`  |     | ✅    | ir.attachment               |
| `message_needaction`                  | Action Needed                    | `boolean`   |     |       |                             |
| `message_needaction_counter`          | Number of Actions                | `integer`   |     |       |                             |
| `message_partner_ids`                 | Followers (Partners)             | `many2many` |     |       | res.partner                 |
| `move_id`                             | Journal Entry                    | `many2one`  |     | ✅    | account.move                |
| `my_activity_date_deadline`           | My Activity Deadline             | `date`      |     |       |                             |
| `name`                                | Number                           | `char`      |     | ✅    |                             |
| `need_cancel_request`                 | Need Cancel Request              | `boolean`   |     |       |                             |
| `outstanding_account_id`              | Outstanding Account              | `many2one`  |     | ✅    | account.account             |
| `paired_internal_transfer_payment_id` | Paired Internal Transfer Payment | `many2one`  |     | ✅    | account.payment             |
| `partner_bank_id`                     | Recipient Bank Account           | `many2one`  |     | ✅    | res.partner.bank            |
| `partner_id`                          | Customer/Vendor                  | `many2one`  |     | ✅    | res.partner                 |
| `partner_type`                        | Partner Type                     | `selection` | ✅  | ✅    |                             |
| `payment_method_code`                 | Code                             | `char`      |     |       |                             |
| `payment_method_id`                   | Method                           | `many2one`  |     | ✅    | account.payment.method      |
| `payment_method_line_id`              | Payment Method                   | `many2one`  |     | ✅    | account.payment.method.line |
| `payment_receipt_title`               | Payment Receipt Title            | `char`      |     |       |                             |
| `payment_reference`                   | Payment Reference                | `char`      |     | ✅    |                             |
| `payment_token_id`                    | Saved Payment Token              | `many2one`  |     | ✅    | payment.token               |
| `payment_transaction_id`              | Payment Transaction              | `many2one`  |     | ✅    | payment.transaction         |
| `payment_type`                        | Payment Type                     | `selection` | ✅  | ✅    |                             |
| `qr_code`                             | QR Code URL                      | `html`      |     |       |                             |
| `rating_ids`                          | Ratings                          | `one2many`  |     | ✅    | rating.rating               |
| `reconciled_bill_ids`                 | Reconciled Bills                 | `many2many` |     |       | account.move                |
| `reconciled_bills_count`              | # Reconciled Bills               | `integer`   |     |       |                             |
| `reconciled_invoice_ids`              | Reconciled Invoices              | `many2many` |     |       | account.move                |
| `reconciled_invoices_count`           | # Reconciled Invoices            | `integer`   |     |       |                             |
| `reconciled_invoices_type`            | Reconciled Invoices Type         | `selection` |     |       |                             |
| `reconciled_statement_line_ids`       | Reconciled Statement Lines       | `many2many` |     |       | account.bank.statement.line |
| `reconciled_statement_lines_count`    | # Reconciled Statement Lines     | `integer`   |     |       |                             |
| `refunds_count`                       | Refunds Count                    | `integer`   |     |       |                             |
| `require_partner_bank_account`        | Require Partner Bank Account     | `boolean`   |     |       |                             |
| `show_partner_bank_account`           | Show Partner Bank Account        | `boolean`   |     |       |                             |
| `source_payment_id`                   | Source Payment                   | `many2one`  |     | ✅    | account.payment             |
| `state`                               | State                            | `selection` | ✅  | ✅    |                             |
| `suitable_payment_token_ids`          | Suitable Payment Token           | `many2many` |     |       | payment.token               |
| `use_electronic_payment_method`       | Use Electronic Payment Method    | `boolean`   |     |       |                             |
| `website_message_ids`                 | Website Messages                 | `one2many`  |     | ✅    | mail.message                |
| `write_date`                          | Last Updated on                  | `datetime`  |     | ✅    |                             |
| `write_uid`                           | Last Updated by                  | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name            | Group                  | Perms     |
| --------------- | ---------------------- | --------- |
| account.payment | Accounting / Invoicing | `R/W/C/D` |
| account.payment | Auditor                | `R`       |

**Record Rules:**

- **Account payment company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`

### 🗃️ `res.config.settings` — Config Settings

> ✳️ Transient (Wizard)

Enhanced configuration interface for exchange rate management

**Fields:**

| Field                                                | Label                                                                                           | Type        | Req | Store | Relation                         |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------- | --- | ----- | -------------------------------- |
| `access_token`                                       | Access Token                                                                                    | `char`      |     | ✅    |                                  |
| `account_cash_basis_base_account_id`                 | Base Tax Received Account                                                                       | `many2one`  |     |       | account.account                  |
| `account_default_credit_limit`                       | Default Credit Limit                                                                            | `monetary`  |     |       |                                  |
| `account_discount_expense_allocation_id`             | Customer Invoices Discounts Account                                                             | `many2one`  |     |       | account.account                  |
| `account_discount_income_allocation_id`              | Vendor Bills Discounts Account                                                                  | `many2one`  |     |       | account.account                  |
| `account_fiscal_country_id`                          | Fiscal Country Code                                                                             | `many2one`  |     |       | res.country                      |
| `account_journal_early_pay_discount_gain_account_id` | Early Discount Gain                                                                             | `many2one`  |     |       | account.account                  |
| `account_journal_early_pay_discount_loss_account_id` | Early Discount Loss                                                                             | `many2one`  |     |       | account.account                  |
| `account_journal_suspense_account_id`                | Bank Suspense                                                                                   | `many2one`  |     |       | account.account                  |
| `account_on_checkout`                                | Customer Accounts                                                                               | `selection` | ✅  |       |                                  |
| `account_price_include`                              | Default Sales Price Include                                                                     | `selection` | ✅  |       |                                  |
| `account_storno`                                     | Storno accounting                                                                               | `boolean`   |     |       |                                  |
| `account_use_credit_limit`                           | Sales Credit Limit                                                                              | `boolean`   |     |       |                                  |
| `active_provider_id`                                 | Active Provider                                                                                 | `many2one`  |     |       | payment.provider                 |
| `active_user_count`                                  | Number of Active Users                                                                          | `integer`   |     |       |                                  |
| `add_to_cart_action`                                 | Add To Cart Action                                                                              | `selection` |     |       |                                  |
| `alias_domain_id`                                    | Alias Domain                                                                                    | `many2one`  |     |       | mail.alias.domain                |
| `anglo_saxon_accounting`                             | Use anglo-saxon accounting                                                                      | `boolean`   |     |       |                                  |
| `annual_inventory_day`                               | Day of the month                                                                                | `integer`   |     |       |                                  |
| `annual_inventory_month`                             | Annual Inventory Month                                                                          | `selection` |     |       |                                  |
| `app_login_details_show`                             | Replace Login URL                                                                               | `boolean`   |     | ✅    |                                  |
| `app_login_name`                                     | Login Page Name                                                                                 | `char`      |     | ✅    |                                  |
| `app_login_url`                                      | Login Page URL                                                                                  | `char`      |     | ✅    |                                  |
| `app_ribbon_name`                                    | Show Demo Ribbon                                                                                | `char`      |     | ✅    |                                  |
| `app_ribbon_name_show`                               | Show Ribbon                                                                                     | `boolean`   |     | ✅    |                                  |
| `app_show_lang`                                      | Show Quick Language Switcher                                                                    | `boolean`   |     | ✅    |                                  |
| `app_system_name`                                    | System Name                                                                                     | `char`      |     | ✅    |                                  |
| `attendance_subject_generic`                         | Attendance Subject Generic                                                                      | `selection` |     | ✅    |                                  |
| `auth_signup_reset_password`                         | Enable password reset from Login page                                                           | `boolean`   |     | ✅    |                                  |
| `auth_signup_template_user_id`                       | Template user for new users created through signup                                              | `many2one`  |     | ✅    | res.users                        |
| `auth_signup_uninvited`                              | Customer Account                                                                                | `selection` |     |       |                                  |
| `auth_totp_enforce`                                  | Enforce two-factor authentication                                                               | `boolean`   |     | ✅    |                                  |
| `auth_totp_policy`                                   | Two-factor authentication enforcing policy                                                      | `selection` |     | ✅    |                                  |
| `automatic_email`                                    | Automatic Email                                                                                 | `boolean`   |     | ✅    |                                  |
| `automatic_invoice`                                  | Automatic Invoice                                                                               | `boolean`   |     | ✅    |                                  |
| `autopost_bills`                                     | Auto-validate bills                                                                             | `boolean`   |     |       |                                  |
| `barcode_nomenclature_id`                            | Nomenclature                                                                                    | `many2one`  |     |       | barcode.nomenclature             |
| `barcode_separator`                                  | Separator                                                                                       | `char`      |     | ✅    |                                  |
| `cart_abandoned_delay`                               | Abandoned Delay                                                                                 | `float`     |     |       |                                  |
| `cart_recovery_mail_template`                        | Cart Recovery Email                                                                             | `many2one`  |     |       | mail.template                    |
| `cdn_activated`                                      | Content Delivery Network (CDN)                                                                  | `boolean`   |     |       |                                  |
| `cdn_filters`                                        | CDN Filters                                                                                     | `text`      |     |       |                                  |
| `cdn_url`                                            | CDN Base URL                                                                                    | `char`      |     |       |                                  |
| `channel_id`                                         | Website Live Channel                                                                            | `many2one`  |     |       | im_livechat.channel              |
| `chart_template`                                     | Chart Template                                                                                  | `selection` |     | ✅    |                                  |
| `client_id`                                          | Client ID                                                                                       | `char`      |     | ✅    |                                  |
| `client_secret`                                      | Client Secret                                                                                   | `char`      |     | ✅    |                                  |
| `company_count`                                      | Number of Companies                                                                             | `integer`   |     |       |                                  |
| `company_country_code`                               | Company Country Code                                                                            | `char`      |     |       |                                  |
| `company_country_group_codes`                        | Country Group Codes                                                                             | `json`      |     |       |                                  |
| `company_currency_id`                                | Company Currency                                                                                | `many2one`  |     |       | res.currency                     |
| `company_expense_allowed_payment_method_line_ids`    | Payment methods available for expenses paid by company                                          | `many2many` |     |       | account.payment.method.line      |
| `company_id`                                         | Company                                                                                         | `many2one`  | ✅  | ✅    | res.company                      |
| `company_informations`                               | Company Informations                                                                            | `text`      |     |       |                                  |
| `company_name`                                       | Company Name                                                                                    | `char`      |     |       |                                  |
| `company_so_template_id`                             | Default Template                                                                                | `many2one`  |     |       | sale.order.template              |
| `confirmation_email_template_id`                     | Confirmation Email Template                                                                     | `many2one`  |     |       | mail.template                    |
| `contract_expiration_notice_period`                  | Contract Expiry Notice Period                                                                   | `integer`   |     |       |                                  |
| `country_code`                                       | Country Code                                                                                    | `char`      |     |       |                                  |
| `create_date`                                        | Created on                                                                                      | `datetime`  |     | ✅    |                                  |
| `create_uid`                                         | Created by                                                                                      | `many2one`  |     | ✅    | res.users                        |
| `crm_auto_assignment_action`                         | Auto Assignment Action                                                                          | `selection` |     | ✅    |                                  |
| `crm_auto_assignment_interval_number`                | Repeat every                                                                                    | `integer`   |     | ✅    |                                  |
| `crm_auto_assignment_interval_type`                  | Auto Assignment Interval Unit                                                                   | `selection` |     | ✅    |                                  |
| `crm_auto_assignment_run_datetime`                   | Auto Assignment Next Execution Date                                                             | `datetime`  |     | ✅    |                                  |
| `crm_use_auto_assignment`                            | Rule-Based Assignment                                                                           | `boolean`   |     | ✅    |                                  |
| `currency_exchange_journal_id`                       | Currency Exchange Journal                                                                       | `many2one`  |     |       | account.journal                  |
| `currency_id`                                        | Currency                                                                                        | `many2one`  | ✅  |       | res.currency                     |
| `days_to_purchase`                                   | Days to Purchase                                                                                | `float`     |     |       |                                  |
| `default_allow_out_of_stock_order`                   | Continue selling when out-of-stock                                                              | `boolean`   |     | ✅    |                                  |
| `default_available_threshold`                        | Show Threshold                                                                                  | `float`     |     | ✅    |                                  |
| `default_invoice_policy`                             | Invoicing Policy                                                                                | `selection` |     | ✅    |                                  |
| `default_picking_policy`                             | Picking Policy                                                                                  | `selection` | ✅  | ✅    |                                  |
| `default_show_availability`                          | Show availability Qty                                                                           | `boolean`   |     | ✅    |                                  |
| `delay_alert_contract`                               | Delay alert contract outdated                                                                   | `integer`   |     | ✅    |                                  |
| `digest_emails`                                      | Digest Emails                                                                                   | `boolean`   |     | ✅    |                                  |
| `digest_id`                                          | Digest Email                                                                                    | `many2one`  |     | ✅    | digest.digest                    |
| `display_account_storno`                             | Display Account Storno                                                                          | `boolean`   |     |       |                                  |
| `display_invoice_amount_total_words`                 | Total amount of invoice in letters                                                              | `boolean`   |     |       |                                  |
| `display_invoice_tax_company_currency`               | Taxes in company currency                                                                       | `boolean`   |     |       |                                  |
| `display_name`                                       | Display Name                                                                                    | `char`      |     |       |                                  |
| `documents_binary_max_size`                          | Size                                                                                            | `integer`   |     | ✅    |                                  |
| `documents_forbidden_extensions`                     | Extensions                                                                                      | `char`      |     | ✅    |                                  |
| `downpayment_account_id`                             | Downpayment Account                                                                             | `many2one`  |     |       | account.account                  |
| `ecommerce_access`                                   | Ecommerce Access                                                                                | `selection` |     |       |                                  |
| `email_primary_color`                                | Email Button Text                                                                               | `char`      |     |       |                                  |
| `email_secondary_color`                              | Email Button Color                                                                              | `char`      |     |       |                                  |
| `enable_academic_plan`                               | Academic Plan                                                                                   | `boolean`   |     | ✅    |                                  |
| `enable_create_student_user`                         | Create Student User                                                                             | `boolean`   |     | ✅    |                                  |
| `enable_exchange_rate_module`                        | Enable Exchange Rate Synchronization                                                            | `boolean`   |     | ✅    |                                  |
| `enable_recaptcha`                                   | Enable reCAPTCHA                                                                                | `boolean`   |     | ✅    |                                  |
| `expense_account_id`                                 | Expense Account                                                                                 | `many2one`  |     |       | account.account                  |
| `expense_currency_exchange_account_id`               | Loss Exchange Rate Account                                                                      | `many2one`  |     |       | account.account                  |
| `expense_journal_id`                                 | Default Expense Journal                                                                         | `many2one`  |     |       | account.journal                  |
| `external_email_server_default`                      | Use Custom Email Servers                                                                        | `boolean`   |     | ✅    |                                  |
| `external_report_layout_id`                          | Document Template                                                                               | `many2one`  |     |       | ir.ui.view                       |
| `fail_counter`                                       | Fail Mail                                                                                       | `integer`   |     |       |                                  |
| `favicon`                                            | Favicon                                                                                         | `binary`    |     |       |                                  |
| `fiscalyear_last_day`                                | Fiscalyear Last Day                                                                             | `integer`   |     |       |                                  |
| `fiscalyear_last_month`                              | Fiscalyear Last Month                                                                           | `selection` |     |       |                                  |
| `fiscalyear_lock_date`                               | Global Lock Date                                                                                | `date`      |     |       |                                  |
| `force_restrictive_audit_trail`                      | Forced Audit Trail                                                                              | `boolean`   |     |       |                                  |
| `global_calendar_user_id`                            | Calendar User                                                                                   | `many2one`  |     | ✅    | res.users                        |
| `google_analytics_key`                               | Google Analytics Key                                                                            | `char`      |     |       |                                  |
| `google_gmail_client_identifier`                     | Gmail Client Id                                                                                 | `char`      |     | ✅    |                                  |
| `google_gmail_client_secret`                         | Gmail Client Secret                                                                             | `char`      |     | ✅    |                                  |
| `google_maps_static_api_key`                         | Google Maps API key                                                                             | `char`      |     | ✅    |                                  |
| `google_maps_static_api_secret`                      | Google Maps API secret                                                                          | `char`      |     | ✅    |                                  |
| `google_search_console`                              | Google Search Console Key                                                                       | `char`      |     |       |                                  |
| `google_translate_api_key`                           | Message Translation API Key                                                                     | `char`      |     | ✅    |                                  |
| `group_analytic_accounting`                          | Analytic Accounting                                                                             | `boolean`   |     | ✅    |                                  |
| `group_auto_done_setting`                            | Lock Confirmed Sales                                                                            | `boolean`   |     | ✅    |                                  |
| `group_cash_rounding`                                | Cash Rounding                                                                                   | `boolean`   |     | ✅    |                                  |
| `group_discount_per_so_line`                         | Discounts                                                                                       | `boolean`   |     | ✅    |                                  |
| `group_fiscal_year`                                  | Fiscal Years                                                                                    | `boolean`   |     | ✅    |                                  |
| `group_gmc_feed`                                     | Google Merchant Center                                                                          | `boolean`   |     |       |                                  |
| `group_lot_on_delivery_slip`                         | Display Lots & Serial Numbers on Delivery Slips                                                 | `boolean`   |     | ✅    |                                  |
| `group_lot_on_invoice`                               | Display Lots & Serial Numbers on Invoices                                                       | `boolean`   |     | ✅    |                                  |
| `group_mass_mailing_campaign`                        | Mailing Campaigns                                                                               | `boolean`   |     | ✅    |                                  |
| `group_multi_currency`                               | Multi-Currencies                                                                                | `boolean`   |     | ✅    |                                  |
| `group_multi_website`                                | Multi-website                                                                                   | `boolean`   |     | ✅    |                                  |
| `group_product_price_comparison`                     | Comparison Price                                                                                | `boolean`   |     | ✅    |                                  |
| `group_product_pricelist`                            | Pricelists                                                                                      | `boolean`   |     | ✅    |                                  |
| `group_product_variant`                              | Variants                                                                                        | `boolean`   |     | ✅    |                                  |
| `group_proforma_sales`                               | Pro-Forma Invoice                                                                               | `boolean`   |     | ✅    |                                  |
| `group_sale_delivery_address`                        | Customer Addresses                                                                              | `boolean`   |     | ✅    |                                  |
| `group_sale_order_template`                          | Quotation Templates                                                                             | `boolean`   |     | ✅    |                                  |
| `group_send_reminder`                                | Receipt Reminder                                                                                | `boolean`   |     | ✅    |                                  |
| `group_show_uom_price`                               | Base Unit Price                                                                                 | `boolean`   |     | ✅    |                                  |
| `group_stock_adv_location`                           | Multi-Step Routes                                                                               | `boolean`   |     | ✅    |                                  |
| `group_stock_lot_print_gs1`                          | Print GS1 Barcodes for Lots & Serial Numbers                                                    | `boolean`   |     | ✅    |                                  |
| `group_stock_multi_locations`                        | Storage Locations                                                                               | `boolean`   |     | ✅    |                                  |
| `group_stock_production_lot`                         | Lots & Serial Numbers                                                                           | `boolean`   |     | ✅    |                                  |
| `group_stock_reception_report`                       | Reception Report                                                                                | `boolean`   |     | ✅    |                                  |
| `group_stock_sign_delivery`                          | Signature                                                                                       | `boolean`   |     | ✅    |                                  |
| `group_stock_tracking_lot`                           | Packages                                                                                        | `boolean`   |     | ✅    |                                  |
| `group_stock_tracking_owner`                         | Consignment                                                                                     | `boolean`   |     | ✅    |                                  |
| `group_uom`                                          | Units of Measure & Packagings                                                                   | `boolean`   |     | ✅    |                                  |
| `group_use_lead`                                     | Leads                                                                                           | `boolean`   |     | ✅    |                                  |
| `group_use_recurring_revenues`                       | Recurring Revenues                                                                              | `boolean`   |     | ✅    |                                  |
| `group_warning_purchase`                             | Purchase Warnings                                                                               | `boolean`   |     | ✅    |                                  |
| `group_warning_sale`                                 | Sale Order Warnings                                                                             | `boolean`   |     | ✅    |                                  |
| `group_warning_stock`                                | Warnings for Stock                                                                              | `boolean`   |     | ✅    |                                  |
| `hard_lock_date`                                     | Hard Lock Date                                                                                  | `date`      |     |       |                                  |
| `has_accounting_entries`                             | Has Accounting Entries                                                                          | `boolean`   |     |       |                                  |
| `has_chart_of_accounts`                              | Company has a chart of accounts                                                                 | `boolean`   |     |       |                                  |
| `has_default_share_image`                            | Use a image by default for sharing                                                              | `boolean`   |     |       |                                  |
| `has_enabled_provider`                               | Has Enabled Provider                                                                            | `boolean`   |     |       |                                  |
| `has_google_analytics`                               | Google Analytics                                                                                | `boolean`   |     |       |                                  |
| `has_google_search_console`                          | Google Search Console                                                                           | `boolean`   |     |       |                                  |
| `has_plausible_shared_key`                           | Plausible Analytics                                                                             | `boolean`   |     |       |                                  |
| `horizon_days`                                       | Replenishment Horizon                                                                           | `float`     |     |       |                                  |
| `hr_expense_alias_domain_id`                         | Hr Expense Alias Domain                                                                         | `many2one`  |     |       | mail.alias.domain                |
| `hr_expense_alias_prefix`                            | Default Alias Name for Expenses                                                                 | `char`      |     | ✅    |                                  |
| `hr_expense_use_mailgateway`                         | Let your employees record expenses by email                                                     | `boolean`   |     | ✅    |                                  |
| `hr_presence_control_email`                          | Based on number of emails sent                                                                  | `boolean`   |     |       |                                  |
| `hr_presence_control_email_amount`                   | # emails to send                                                                                | `integer`   |     |       |                                  |
| `hr_presence_control_ip`                             | Based on IP Address                                                                             | `boolean`   |     |       |                                  |
| `hr_presence_control_ip_list`                        | Valid IP addresses                                                                              | `char`      |     |       |                                  |
| `hr_presence_control_login`                          | Based on user status in system                                                                  | `boolean`   |     |       |                                  |
| `id`                                                 | ID                                                                                              | `integer`   |     | ✅    |                                  |
| `income_account_id`                                  | Income Account                                                                                  | `many2one`  |     |       | account.account                  |
| `income_currency_exchange_account_id`                | Gain Exchange Rate Account                                                                      | `many2one`  |     |       | account.account                  |
| `incoterm_id`                                        | Default incoterm                                                                                | `many2one`  |     |       | account.incoterms                |
| `invoice_mail_template_id`                           | Email Template                                                                                  | `many2one`  |     | ✅    | mail.template                    |
| `invoice_terms`                                      | Terms & Conditions                                                                              | `html`      |     |       |                                  |
| `invoice_terms_html`                                 | Terms & Conditions as a Web page                                                                | `html`      |     |       |                                  |
| `is_account_peppol_eligible`                         | PEPPOL eligible                                                                                 | `boolean`   |     |       |                                  |
| `is_batch_and_subject_constraint`                    | Batch and Subject Constraint                                                                    | `boolean`   |     | ✅    |                                  |
| `is_batch_constraint`                                | Batch Constraint                                                                                | `boolean`   |     | ✅    |                                  |
| `is_classroom_constraint`                            | Classroom Constraint                                                                            | `boolean`   |     | ✅    |                                  |
| `is_faculty_constraint`                              | Faculty Constraint                                                                              | `boolean`   |     | ✅    |                                  |
| `is_hash_verified`                                   | Is Hash Verified                                                                                | `boolean`   |     |       |                                  |
| `is_installed_sale`                                  | Is the Sale Module Installed                                                                    | `boolean`   |     | ✅    |                                  |
| `is_mail_sent`                                       | Is Mail Sent                                                                                    | `boolean`   |     |       |                                  |
| `is_membership_multi`                                | Multi Teams                                                                                     | `boolean`   |     | ✅    |                                  |
| `is_newsletter_enabled`                              | Is Newsletter Enabled                                                                           | `boolean`   |     | ✅    |                                  |
| `is_root_company`                                    | Is Root Company                                                                                 | `boolean`   |     |       |                                  |
| `language_count`                                     | Number of Languages                                                                             | `integer`   |     |       |                                  |
| `language_ids`                                       | Languages                                                                                       | `many2many` |     |       | res.lang                         |
| `lead_enrich_auto`                                   | Enrich lead automatically                                                                       | `selection` |     | ✅    |                                  |
| `lead_mining_in_pipeline`                            | Create a lead mining request directly from the opportunity pipeline.                            | `boolean`   |     | ✅    |                                  |
| `link_qr_code`                                       | Display Link QR-code                                                                            | `boolean`   |     |       |                                  |
| `lock_confirmed_po`                                  | Lock Confirmed Orders                                                                           | `boolean`   |     | ✅    |                                  |
| `mass_mailing_mail_server_id`                        | Mail Server                                                                                     | `many2one`  |     | ✅    | ir.mail_server                   |
| `mass_mailing_outgoing_mail_server`                  | Dedicated Server                                                                                | `boolean`   |     | ✅    |                                  |
| `mass_mailing_reports`                               | 24H Stat Mailing Reports                                                                        | `boolean`   |     | ✅    |                                  |
| `mass_mailing_split_contact_name`                    | Split First and Last Name                                                                       | `boolean`   |     | ✅    |                                  |
| `menu_bg_image`                                      | Apps Menu Footer Image                                                                          | `binary`    |     |       |                                  |
| `microsoft_outlook_client_identifier`                | Outlook Client Id                                                                               | `char`      |     | ✅    |                                  |
| `microsoft_outlook_client_secret`                    | Outlook Client Secret                                                                           | `char`      |     | ✅    |                                  |
| `module_account_3way_match`                          | 3-way matching: purchases, receptions and bills                                                 | `boolean`   |     | ✅    |                                  |
| `module_account_accountant`                          | Accounting                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_account_bank_statement_extract`              | Bank Statement Digitization                                                                     | `boolean`   |     | ✅    |                                  |
| `module_account_bank_statement_import_qif`           | Import .qif files                                                                               | `boolean`   |     | ✅    |                                  |
| `module_account_batch_payment`                       | Use batch payments                                                                              | `boolean`   |     | ✅    |                                  |
| `module_account_budget`                              | Budget Management                                                                               | `boolean`   |     | ✅    |                                  |
| `module_account_check_printing`                      | Allow check printing and deposits                                                               | `boolean`   |     | ✅    |                                  |
| `module_account_extract`                             | Document Digitization                                                                           | `boolean`   |     | ✅    |                                  |
| `module_account_inter_company_rules`                 | Manage Inter Company                                                                            | `boolean`   |     | ✅    |                                  |
| `module_account_intrastat`                           | Intrastat                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_account_invoice_extract`                     | Invoice Digitization                                                                            | `boolean`   |     | ✅    |                                  |
| `module_account_iso20022`                            | SEPA Credit Transfer / ISO20022                                                                 | `boolean`   |     | ✅    |                                  |
| `module_account_payment`                             | Invoice Online Payment                                                                          | `boolean`   |     | ✅    |                                  |
| `module_account_peppol`                              | PEPPOL Invoicing                                                                                | `boolean`   |     | ✅    |                                  |
| `module_account_reports`                             | Dynamic Reports                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_account_sepa_direct_debit`                   | Use SEPA Direct Debit                                                                           | `boolean`   |     | ✅    |                                  |
| `module_auth_ldap`                                   | LDAP Authentication                                                                             | `boolean`   |     | ✅    |                                  |
| `module_auth_oauth`                                  | Use external authentication providers (OAuth)                                                   | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup`                        | Database Backup to Local Server                                                                 | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_dropbox`                | Database Backup to Dropbox                                                                      | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_ftp`                    | Database Backup to Remote FTP Server                                                            | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_google_drive`           | Database Backup to Google Drive                                                                 | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_onedrive`               | Database Backup to Onedrive                                                                     | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_sftp`                   | Database Backup to Remote SFTP Server                                                           | `boolean`   |     | ✅    |                                  |
| `module_backend_theme`                               | Backend Theme                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_base_geolocalize`                            | GeoLocalize                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_base_import`                                 | Allow users to import data from CSV/XLS/XLSX/ODS files                                          | `boolean`   |     | ✅    |                                  |
| `module_bigbluebutton`                               | Bigbluebutton Enterprise                                                                        | `boolean`   |     | ✅    |                                  |
| `module_crm_iap_enrich`                              | Enrich your leads automatically with company data based on their email address.                 | `boolean`   |     | ✅    |                                  |
| `module_crm_iap_mine`                                | Generate new leads based on their country, industries, size, etc.                               | `boolean`   |     | ✅    |                                  |
| `module_currency_rate_live`                          | Automatic Currency Rates                                                                        | `boolean`   |     | ✅    |                                  |
| `module_delivery`                                    | Delivery Methods                                                                                | `boolean`   |     | ✅    |                                  |
| `module_delivery_bpost`                              | bpost Connector                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_delivery_dhl`                                | DHL Express Connector                                                                           | `boolean`   |     | ✅    |                                  |
| `module_delivery_easypost`                           | Easypost Connector                                                                              | `boolean`   |     | ✅    |                                  |
| `module_delivery_envia`                              | Envia.com Connector                                                                             | `boolean`   |     | ✅    |                                  |
| `module_delivery_fedex_rest`                         | FedEx Connector                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_delivery_sendcloud`                          | Sendcloud Connector                                                                             | `boolean`   |     | ✅    |                                  |
| `module_delivery_shiprocket`                         | Shiprocket Connector                                                                            | `boolean`   |     | ✅    |                                  |
| `module_delivery_starshipit`                         | Starshipit Connector                                                                            | `boolean`   |     | ✅    |                                  |
| `module_delivery_ups_rest`                           | UPS Connector                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_delivery_usps_rest`                          | USPS Connector                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_event_booth`                                 | Booth Management                                                                                | `boolean`   |     | ✅    |                                  |
| `module_event_sale`                                  | Tickets with Sale                                                                               | `boolean`   |     | ✅    |                                  |
| `module_google_address_autocomplete`                 | Google Address Autocomplete                                                                     | `boolean`   |     | ✅    |                                  |
| `module_google_calendar`                             | Allow the users to synchronize their calendar with Google Calendar                              | `boolean`   |     | ✅    |                                  |
| `module_google_gmail`                                | Support Gmail Authentication                                                                    | `boolean`   |     | ✅    |                                  |
| `module_googlemeet`                                  | Google Meet                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_google_recaptcha`                            | reCAPTCHA                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_helpdesk_elearning`                          | E-Learning                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_helpdesk_forum`                              | Helpdesk Forum                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_helpdesk_project_ext`                        | Helpdesk project                                                                                | `boolean`   |     | ✅    |                                  |
| `module_hr_attendance`                               | Based on attendances                                                                            | `boolean`   |     |       |                                  |
| `module_hr_expense_extract`                          | Send bills to OCR to generate expenses                                                          | `boolean`   |     | ✅    |                                  |
| `module_hr_expense_stripe`                           | Link your stripe issuing account to manage company credit cards for your employees through Odoo | `boolean`   |     | ✅    |                                  |
| `module_hr_payroll_expense`                          | Reimburse Expenses in Payslip                                                                   | `boolean`   |     | ✅    |                                  |
| `module_hr_presence`                                 | Advanced Presence Control                                                                       | `boolean`   |     | ✅    |                                  |
| `module_hr_recruitment_extract`                      | Send CV to OCR to fill applications                                                             | `boolean`   |     | ✅    |                                  |
| `module_hr_recruitment_survey`                       | Interview Forms                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_hr_skills`                                   | Skills Management                                                                               | `boolean`   |     | ✅    |                                  |
| `module_loyalty`                                     | Promotions, Coupons, Gift Card & Loyalty Program                                                | `boolean`   |     | ✅    |                                  |
| `module_mail_plugin`                                 | Allow integration with the mail plugins                                                         | `boolean`   |     | ✅    |                                  |
| `module_microsoft_calendar`                          | Allow the users to synchronize their calendar with Outlook Calendar                             | `boolean`   |     | ✅    |                                  |
| `module_microsoft_outlook`                           | Support Outlook Authentication                                                                  | `boolean`   |     | ✅    |                                  |
| `module_online_appointment`                          | Online Appointment Enterprise                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_achievement_enterprise`           | Achievement Enterprise                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_activity`                         | Activity                                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_activity_enterprise`              | Activity Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_admission`                        | Admission                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_admission_enterprise`             | Admission Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_admission_grading_bridge`         | Admission Grading Bridge                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_blog_enterprise`           | Alumni Blog Enterprise                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_enterprise`                | Alumni Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_event_enterprise`          | Alumni Event Enterprise                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_job_enterprise`            | Alumni Job Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_asset_request_enterprise`         | Asset Request Enterprise                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment`                       | Assignment                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_enterprise`            | Assignment Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_grading_bridge`        | Assignment Gradebook Bridge                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_grading_enterprise`    | Assignment Grading Enterprise                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_rubrics`               | Assignment Rubrics                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance`                       | Attendance                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance_enterprise`            | Attendance Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance_face_recognition`      | Attendance Face Recognition                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance_report_xlsx`           | Attendance Xlsx Report                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_campus_enterprise`                | Campus Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_classroom`                        | Classroom                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_classroom_enterprise`             | Classroom Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_convocation`                      | Convocation                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_crm_enterprise`                   | CRM Enterprise                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_dashboard_kpi`                    | Dashboard KPI                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_digital_library`                  | Digital Library                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_openeducat_discipline`                       | Discipline Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_dynamic_admission`                | Dynamic Admission                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_event_enterprise`                 | Event Enterprise                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam`                             | Exam                                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_enterprise`                  | Exam Enterprise                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_gpa_enterprise`              | Exam GPA Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_grading_bridge`              | Exam Grading Bridge                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_migration_bridge`            | Student Migration Exam Bridge                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_facility`                         | Facility                                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_facility_enterprise`              | Facility Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_fees`                             | Fees                                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_fees_parent_bridge`               | Fees Parent Bridge                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_fees_plan`                        | Fees Plan                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_grading`                          | Grading                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_grading_migration_bridge`         | Student Migration Grading Bridge                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_grievance_enterprise`             | Grievance                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_health_enterprise`                | Health Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_jitsi_enterprise`                 | Jitsi Enterprise                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_job_enterprise`                   | Job Enterprise                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lesson`                           | Lesson Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_library`                          | Library                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_library_barcode`                  | Library Barcode Enterprise                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_library_enterprise`               | Library Enterprise                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live`                             | Live Meeting                                                                                    | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live_assignment`                  | Live Meeting Assignment                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live_attendance`                  | Live Meeting Attendance                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live_attentiveness`               | Live Meeting Attentiveness                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms`                              | LMS Enterprise                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_admission`                    | LMS Admission                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_blog`                         | LMS Blog Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_forum`                        | LMS Forum Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_gamification`                 | LMS Gamification Enterprise                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_h5p`                          | LMS H5P Enterprise                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_sale`                         | LMS Sale Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_survey`                       | LMS Survey Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_mass_subject_registration`        | Mass Subject Registration                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_meeting_enterprise`               | Meeting Enterprise                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_notice_board_enterprise`          | Notice Board Enterprise                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_omr`                              | OMR                                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_parent`                           | Parent                                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_parent_enterprise`                | Parent Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_placement_enterprise`             | Placement Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_placement_job_enterprise`         | Placement Job Enterprise                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_quiz`                             | Quiz Enterprise                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_openeducat_quiz_anti_cheating`               | Quiz Anti Cheating                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_scholarship_enterprise`           | Scholarship Enterprise                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_secure`                           | Secure QR                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_skill_enterprise`                 | Skill Enterprise                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_skypemeet`                        | Skype Meet                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_attendance_enterprise`    | Student Attendance Kiosk                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_feedback_management`      | Student Feedback                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_leave_enterprise`         | Student Leave                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_mentor`                   | Student Mentor                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_progress_enterprise`      | Student Progress Enterprise                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_skill_assessment`         | Skill Assessment Enterprise                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_withdrawal_mgmt`          | Student Withdrawal Management                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_subject_material_allocation`      | Subject Material Allocation                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_thesis`                           | Thesis                                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_timetable`                        | Timetable                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_timetable_enterprise`             | Timetable Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_transportation_enterprise`        | Transportation Enterprise                                                                       | `boolean`   |     | ✅    |                                  |
| `module_partner_autocomplete`                        | Partner Autocomplete                                                                            | `boolean`   |     | ✅    |                                  |
| `module_partnership`                                 | Membership / Partnership                                                                        | `boolean`   |     | ✅    |                                  |
| `module_pos_event`                                   | Tickets with PoS                                                                                | `boolean`   |     | ✅    |                                  |
| `module_product_email_template`                      | Specific Email                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_product_expiry`                              | Expiration Dates                                                                                | `boolean`   |     | ✅    |                                  |
| `module_product_margin`                              | Allow Product Margin                                                                            | `boolean`   |     | ✅    |                                  |
| `module_purchase_product_matrix`                     | Purchase Grid Entry                                                                             | `boolean`   |     | ✅    |                                  |
| `module_purchase_requisition`                        | Purchase Agreements                                                                             | `boolean`   |     | ✅    |                                  |
| `module_quality_control`                             | Quality                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_quality_control_worksheet`                   | Quality Worksheet                                                                               | `boolean`   |     | ✅    |                                  |
| `module_sale_amazon`                                 | Amazon Sync                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_sale_commission`                             | Commissions                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_sale_gelato`                                 | Gelato                                                                                          | `boolean`   |     | ✅    |                                  |
| `module_sale_loyalty`                                | Coupons & Loyalty                                                                               | `boolean`   |     | ✅    |                                  |
| `module_sale_margin`                                 | Margins                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_sale_pdf_quote_builder`                      | PDF Quote builder                                                                               | `boolean`   |     | ✅    |                                  |
| `module_sale_product_matrix`                         | Sales Grid Entry                                                                                | `boolean`   |     | ✅    |                                  |
| `module_sale_shopee`                                 | Shopee Sync                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_sms`                                         | SMS                                                                                             | `boolean`   |     | ✅    |                                  |
| `module_snailmail_account`                           | Snailmail                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_stock_barcode`                               | Barcode Scanner                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_stock_barcode_barcodelookup`                 | Stock Barcode Database                                                                          | `boolean`   |     | ✅    |                                  |
| `module_stock_dropshipping`                          | Dropshipping                                                                                    | `boolean`   |     | ✅    |                                  |
| `module_stock_fleet`                                 | Dispatch Management System                                                                      | `boolean`   |     | ✅    |                                  |
| `module_stock_landed_costs`                          | Landed Costs                                                                                    | `boolean`   |     | ✅    |                                  |
| `module_stock_picking_batch`                         | Batch, Wave & Cluster Transfers                                                                 | `boolean`   |     | ✅    |                                  |
| `module_stock_sms`                                   | SMS Confirmation                                                                                | `boolean`   |     | ✅    |                                  |
| `module_teams`                                       | Teams                                                                                           | `boolean`   |     | ✅    |                                  |
| `module_voip`                                        | Phone                                                                                           | `boolean`   |     | ✅    |                                  |
| `module_website_cf_turnstile`                        | Cloudflare Turnstile                                                                            | `boolean`   |     | ✅    |                                  |
| `module_website_crm_iap_reveal`                      | Create Leads/Opportunities from your website's traffic                                          | `boolean`   |     | ✅    |                                  |
| `module_website_event_exhibitor`                     | Advanced Sponsors                                                                               | `boolean`   |     | ✅    |                                  |
| `module_website_event_sale`                          | Online Ticketing                                                                                | `boolean`   |     | ✅    |                                  |
| `module_website_event_track`                         | Tracks and Agenda                                                                               | `boolean`   |     | ✅    |                                  |
| `module_website_event_track_live`                    | Live Mode                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_website_event_track_quiz`                    | Quiz on Tracks                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_website_helpdesk_mgmt`                       | Helpdesk Website                                                                                | `boolean`   |     | ✅    |                                  |
| `module_website_hr_recruitment`                      | Online Posting                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_website_livechat`                            | Module Website Livechat                                                                         | `boolean`   |     | ✅    |                                  |
| `module_website_sale_autocomplete`                   | Address Autocomplete                                                                            | `boolean`   |     | ✅    |                                  |
| `module_website_sale_collect`                        | Click & Collect                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_web_unsplash`                                | Unsplash Image Library                                                                          | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_account_templates`                  | Account Templates                                                                               | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_ecommerce_templates`                | Whatsapp Ecommerce Templates                                                                    | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_education_templates`                | Education Templates                                                                             | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_other_templates`                    | Other Templates                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_services_templates`                 | Services Templates                                                                              | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_special_occasions_template`         | Special Occasions Templates                                                                     | `boolean`   |     | ✅    |                                  |
| `module_zoom`                                        | Zoom                                                                                            | `boolean`   |     | ✅    |                                  |
| `newsletter_id`                                      | Newsletter List                                                                                 | `many2one`  |     |       | mailing.list                     |
| `next_execution_timestamp`                           | Next Execution Time                                                                             | `datetime`  |     |       |                                  |
| `onboarding_payment_module`                          | Onboarding Payment Module                                                                       | `selection` |     |       |                                  |
| `openeducat_instance_hash_key`                       | OpenEducat Instance Hash Key                                                                    | `char`      |     |       |                                  |
| `openeducat_instance_hash_msg`                       | Instance Hash Key Message                                                                       | `char`      |     |       |                                  |
| `openeducat_instance_key`                            | OpenEducat Instance Key                                                                         | `char`      |     |       |                                  |
| `parent_qrcode`                                      | QR Code                                                                                         | `boolean`   |     | ✅    |                                  |
| `partner_autocomplete_insufficient_credit`           | Insufficient credit                                                                             | `boolean`   |     |       |                                  |
| `pay_invoices_online`                                | Pay Invoices Online                                                                             | `boolean`   |     | ✅    |                                  |
| `plausible_shared_key`                               | Plausible auth Key                                                                              | `char`      |     |       |                                  |
| `plausible_site`                                     | Plausible Site (e.g. domain.com)                                                                | `char`      |     |       |                                  |
| `po_double_validation`                               | Levels of Approvals \*                                                                          | `selection` |     |       |                                  |
| `po_double_validation_amount`                        | Minimum Amount                                                                                  | `monetary`  |     |       |                                  |
| `po_lock`                                            | Purchase Order Modification \*                                                                  | `selection` |     |       |                                  |
| `po_order_approval`                                  | Purchase Order Approval                                                                         | `boolean`   |     | ✅    |                                  |
| `portal_allow_api_keys`                              | Customer API Keys                                                                               | `boolean`   |     |       |                                  |
| `portal_confirmation_pay`                            | Online Payment                                                                                  | `boolean`   |     |       |                                  |
| `portal_confirmation_sign`                           | Online Signature                                                                                | `boolean`   |     |       |                                  |
| `predictive_lead_scoring_field_labels`               | Predictive Lead Scoring Field Labels                                                            | `char`      |     |       |                                  |
| `predictive_lead_scoring_fields`                     | Lead Scoring Frequency Fields                                                                   | `many2many` |     |       | crm.lead.scoring.frequency.field |
| `predictive_lead_scoring_fields_str`                 | Lead Scoring Frequency Fields in String                                                         | `char`      |     | ✅    |                                  |
| `predictive_lead_scoring_start_date`                 | Lead Scoring Starting Date                                                                      | `date`      |     |       |                                  |
| `predictive_lead_scoring_start_date_str`             | Lead Scoring Starting Date in String                                                            | `char`      |     | ✅    |                                  |
| `prepayment_percent`                                 | Prepayment percentage                                                                           | `float`     |     |       |                                  |
| `preview_ready`                                      | Display preview button                                                                          | `boolean`   |     |       |                                  |
| `product_volume_volume_in_cubic_feet`                | Volume unit of measure                                                                          | `selection` |     | ✅    |                                  |
| `product_weight_in_lbs`                              | Weight unit of measure                                                                          | `selection` |     | ✅    |                                  |
| `profiling_enabled_until`                            | Profiling enabled until                                                                         | `datetime`  |     | ✅    |                                  |
| `purchase_lock_date`                                 | Purchases Lock Date                                                                             | `date`      |     |       |                                  |
| `purchase_tax_id`                                    | Default Purchase Tax                                                                            | `many2one`  |     |       | account.tax                      |
| `qr_code`                                            | Display SEPA QR-code                                                                            | `boolean`   |     |       |                                  |
| `quick_edit_mode`                                    | Quick encoding                                                                                  | `selection` |     |       |                                  |
| `quotation_validity_days`                            | Default Quotation Validity                                                                      | `integer`   |     |       |                                  |
| `rate_provider_selection`                            | Exchange Rate Provider                                                                          | `selection` |     |       |                                  |
| `recaptcha_min_score`                                | Minimum score                                                                                   | `float`     |     | ✅    |                                  |
| `recaptcha_private_key`                              | Secret Key                                                                                      | `char`      |     | ✅    |                                  |
| `recaptcha_public_key`                               | Site Key                                                                                        | `char`      |     | ✅    |                                  |
| `refresh_token`                                      | Refresh Token                                                                                   | `char`      |     | ✅    |                                  |
| `replenish_on_order`                                 | Replenish on Order (MTO)                                                                        | `boolean`   |     |       |                                  |
| `report_footer`                                      | Custom Report Footer                                                                            | `html`      |     |       |                                  |
| `resource_calendar_id`                               | Company Working Hours                                                                           | `many2one`  |     |       | resource.calendar                |
| `restrictive_audit_trail`                            | Restricted Audit Trail                                                                          | `boolean`   |     |       |                                  |
| `restrict_template_rendering`                        | Restrict Template Rendering                                                                     | `boolean`   |     | ✅    |                                  |
| `sale_lock_date`                                     | Sales Lock Date                                                                                 | `date`      |     |       |                                  |
| `salesperson_id`                                     | Salesperson                                                                                     | `many2one`  |     |       | res.users                        |
| `salesteam_id`                                       | Sales Team                                                                                      | `many2one`  |     |       | crm.team                         |
| `sale_tax_id`                                        | Default Sale Tax                                                                                | `many2one`  |     |       | account.tax                      |
| `secure_qr_code`                                     | Secure Qr Code                                                                                  | `selection` |     | ✅    |                                  |
| `security_lead`                                      | Security Lead Time                                                                              | `float`     |     |       |                                  |
| `send_abandoned_cart_email`                          | Abandoned Email                                                                                 | `boolean`   |     |       |                                  |
| `sfu_server_key`                                     | SFU Server key                                                                                  | `char`      |     | ✅    |                                  |
| `sfu_server_url`                                     | SFU Server URL                                                                                  | `char`      |     | ✅    |                                  |
| `shared_user_account`                                | Shared Customer Accounts                                                                        | `boolean`   |     |       |                                  |
| `show_blacklist_buttons`                             | Blacklist Option when Unsubscribing                                                             | `boolean`   |     | ✅    |                                  |
| `show_branding_in_footer`                            | Show Branding In Footer                                                                         | `boolean`   |     | ✅    |                                  |
| `show_effect`                                        | Show Effect                                                                                     | `boolean`   |     | ✅    |                                  |
| `show_line_subtotals_tax_selection`                  | Line Subtotals Tax Display                                                                      | `selection` |     |       |                                  |
| `show_sale_receipts`                                 | Sale Receipt                                                                                    | `boolean`   |     | ✅    |                                  |
| `snailmail_color`                                    | Print In Color                                                                                  | `boolean`   |     |       |                                  |
| `snailmail_cover`                                    | Add a Cover Page                                                                                | `boolean`   |     |       |                                  |
| `snailmail_cover_readonly`                           | Snailmail Cover Readonly                                                                        | `boolean`   |     |       |                                  |
| `snailmail_duplex`                                   | Print Both sides                                                                                | `boolean`   |     |       |                                  |
| `social_default_image`                               | Default Social Share Image                                                                      | `binary`    |     |       |                                  |
| `stock_confirmation_type`                            | Stock Text Validation type                                                                      | `selection` |     |       |                                  |
| `stock_move_email_validation`                        | Email Confirmation picking                                                                      | `boolean`   |     |       |                                  |
| `stock_sms_confirmation_template_id`                 | SMS Template                                                                                    | `many2one`  |     |       | sms.template                     |
| `stock_text_confirmation`                            | Stock Text Validation with stock move                                                           | `boolean`   |     |       |                                  |
| `synchronization_batch_size`                         | Batch Size                                                                                      | `integer`   |     |       |                                  |
| `synchronization_frequency`                          | Synchronization Frequency                                                                       | `selection` |     |       |                                  |
| `tax_calculation_rounding_method`                    | Tax calculation rounding method                                                                 | `selection` |     |       |                                  |
| `tax_cash_basis_journal_id`                          | Tax Cash Basis Journal                                                                          | `many2one`  |     |       | account.journal                  |
| `tax_exigibility`                                    | Cash Basis                                                                                      | `boolean`   |     |       |                                  |
| `tax_lock_date`                                      | Tax Lock Date                                                                                   | `date`      |     |       |                                  |
| `tenor_api_key`                                      | Tenor API key                                                                                   | `char`      |     | ✅    |                                  |
| `terms_type`                                         | Terms & Conditions format                                                                       | `selection` |     |       |                                  |
| `transfer_account_id`                                | Internal Transfer                                                                               | `many2one`  |     |       | account.account                  |
| `twilio_account_sid`                                 | Account SID                                                                                     | `char`      |     | ✅    |                                  |
| `twilio_account_token`                               | Account Auth Token                                                                              | `char`      |     | ✅    |                                  |
| `unsplash_access_key`                                | Access Key                                                                                      | `char`      |     | ✅    |                                  |
| `unsplash_app_id`                                    | Application ID                                                                                  | `char`      |     | ✅    |                                  |
| `use_event_barcode`                                  | Use Event Barcode                                                                               | `boolean`   |     | ✅    |                                  |
| `use_google_maps_static_api`                         | Google Maps static API                                                                          | `boolean`   |     | ✅    |                                  |
| `use_invoice_terms`                                  | Default Terms & Conditions                                                                      | `boolean`   |     | ✅    |                                  |
| `use_project`                                        | Use Projects                                                                                    | `boolean`   |     | ✅    |                                  |
| `use_security_lead`                                  | Security Lead Time for Sales                                                                    | `boolean`   |     | ✅    |                                  |
| `use_sfu_server`                                     | Use SFU server                                                                                  | `boolean`   |     | ✅    |                                  |
| `use_twilio_rtc_servers`                             | Use Twilio ICE servers                                                                          | `boolean`   |     | ✅    |                                  |
| `use_website_form`                                   | Website Form                                                                                    | `boolean`   |     | ✅    |                                  |
| `verify_date`                                        | Verify Date                                                                                     | `char`      |     |       |                                  |
| `web_app_name`                                       | Web App Name                                                                                    | `char`      |     | ✅    |                                  |
| `website_block_third_party_domains`                  | Block 3rd-party domains                                                                         | `boolean`   |     |       |                                  |
| `website_company_id`                                 | Website Company                                                                                 | `many2one`  |     |       | res.company                      |
| `website_cookies_bar`                                | Cookies Bar                                                                                     | `boolean`   |     |       |                                  |
| `website_default_lang_code`                          | Default language code                                                                           | `char`      |     |       |                                  |
| `website_default_lang_id`                            | Default language                                                                                | `many2one`  |     |       | res.lang                         |
| `website_domain`                                     | Website Domain                                                                                  | `char`      |     |       |                                  |
| `website_homepage_url`                               | Homepage Url                                                                                    | `char`      |     |       |                                  |
| `website_id`                                         | website                                                                                         | `many2one`  |     | ✅    | website                          |
| `website_language_count`                             | Number of languages                                                                             | `integer`   |     |       |                                  |
| `website_logo`                                       | Website Logo                                                                                    | `binary`    |     |       |                                  |
| `website_name`                                       | Website Name                                                                                    | `char`      |     |       |                                  |
| `website_sale_contact_us_button_url`                 | Button Url                                                                                      | `char`      |     |       |                                  |
| `website_sale_prevent_zero_price_sale`               | Prevent Sale of Zero Priced Product                                                             | `boolean`   |     |       |                                  |
| `website_warehouse_id`                               | Warehouse                                                                                       | `many2one`  |     |       | stock.warehouse                  |
| `whatsapp_business_id`                               | Business Account                                                                                | `many2one`  |     | ✅    | whatsapp.business                |
| `work_permit_expiration_notice_period`               | Work Permit Expiry Notice Period                                                                | `integer`   |     |       |                                  |
| `write_date`                                         | Last Updated on                                                                                 | `datetime`  |     | ✅    |                                  |
| `write_uid`                                          | Last Updated by                                                                                 | `many2one`  |     | ✅    | res.users                        |

**Access Rights:**

| Name                       | Group                | Perms   |
| -------------------------- | -------------------- | ------- |
| access.res.config.settings | Role / Administrator | `R/W/C` |

### 🗃️ `payment.link.wizard` — Generate Sales Payment Link

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                       | Label                              | Type       | Req | Store | Relation     |
| --------------------------- | ---------------------------------- | ---------- | --- | ----- | ------------ |
| `amount`                    | Amount                             | `monetary` | ✅  | ✅    |              |
| `amount_max`                | Amount Max                         | `monetary` |     | ✅    |              |
| `amount_paid`               | Already Paid                       | `monetary` |     | ✅    |              |
| `company_id`                | Company                            | `many2one` |     |       | res.company  |
| `confirmation_message`      | Confirmation Message               | `char`     |     |       |              |
| `create_date`               | Created on                         | `datetime` |     | ✅    |              |
| `create_uid`                | Created by                         | `many2one` |     | ✅    | res.users    |
| `currency_id`               | Currency                           | `many2one` |     | ✅    | res.currency |
| `discount_date`             | Discount Date                      | `date`     |     | ✅    |              |
| `display_name`              | Display Name                       | `char`     |     |       |              |
| `display_open_installments` | Display Open Installments          | `boolean`  |     |       |              |
| `epd_info`                  | Early Payment Discount Information | `char`     |     |       |              |
| `has_eligible_epd`          | Has Eligible Epd                   | `boolean`  |     | ✅    |              |
| `id`                        | ID                                 | `integer`  |     | ✅    |              |
| `invoice_amount_due`        | Amount Due                         | `monetary` |     |       |              |
| `link`                      | Payment Link                       | `char`     |     |       |              |
| `open_installments`         | Open Installments                  | `json`     |     | ✅    |              |
| `open_installments_preview` | Open Installments Preview          | `html`     |     |       |              |
| `partner_email`             | Email                              | `char`     |     |       |              |
| `partner_id`                | Partner                            | `many2one` |     | ✅    | res.partner  |
| `prepayment_amount`         | Prepayment Amount                  | `monetary` |     | ✅    |              |
| `res_id`                    | Related Document ID                | `integer`  | ✅  | ✅    |              |
| `res_model`                 | Related Document Model             | `char`     | ✅  | ✅    |              |
| `warning_message`           | Warning Message                    | `char`     |     |       |              |
| `write_date`                | Last Updated on                    | `datetime` |     | ✅    |              |
| `write_uid`                 | Last Updated by                    | `many2one` |     | ✅    | res.users    |

**Access Rights:**

| Name                            | Group                            | Perms   |
| ------------------------------- | -------------------------------- | ------- |
| access.payment.link.wizard.sale | Sales / User: Own Documents Only | `R/W/C` |
| payment.link.wizard             | Accounting / Invoicing           | `R/W/C` |
| access_payment_link_wizard      | Role / User                      | `-`     |

### 🗃️ `account.payment.register` — Pay

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                               | Label                            | Type        | Req | Store | Relation                    |
| ----------------------------------- | -------------------------------- | ----------- | --- | ----- | --------------------------- |
| `actionable_errors`                 | Actionable Errors                | `json`      |     |       |                             |
| `amount`                            | Amount                           | `monetary`  |     | ✅    |                             |
| `available_journal_ids`             | Available Journal                | `many2many` |     |       | account.journal             |
| `available_partner_bank_ids`        | Available Partner Bank           | `many2many` |     |       | res.partner.bank            |
| `available_payment_method_line_ids` | Available Payment Method Line    | `many2many` |     |       | account.payment.method.line |
| `batches`                           | Batches                          | `binary`    |     |       |                             |
| `can_edit_wizard`                   | Can Edit Wizard                  | `boolean`   |     | ✅    |                             |
| `can_group_payments`                | Can Group Payments               | `boolean`   |     | ✅    |                             |
| `communication`                     | Memo                             | `char`      |     | ✅    |                             |
| `company_currency_id`               | Company Currency                 | `many2one`  |     |       | res.currency                |
| `company_id`                        | Company                          | `many2one`  |     | ✅    | res.company                 |
| `country_code`                      | Country Code                     | `char`      |     |       |                             |
| `create_date`                       | Created on                       | `datetime`  |     | ✅    |                             |
| `create_uid`                        | Created by                       | `many2one`  |     | ✅    | res.users                   |
| `currency_id`                       | Currency                         | `many2one`  |     | ✅    | res.currency                |
| `custom_user_amount`                | Custom User Amount               | `monetary`  |     | ✅    |                             |
| `custom_user_currency_id`           | Custom User Currency             | `many2one`  |     | ✅    | res.currency                |
| `display_name`                      | Display Name                     | `char`      |     |       |                             |
| `duplicate_payment_ids`             | Duplicate Payment                | `many2many` |     |       | account.payment             |
| `early_payment_discount_mode`       | Early Payment Discount Mode      | `boolean`   |     |       |                             |
| `group_payment`                     | Group Payments                   | `boolean`   |     | ✅    |                             |
| `hide_writeoff_section`             | Hide Writeoff Section            | `boolean`   |     |       |                             |
| `id`                                | ID                               | `integer`   |     | ✅    |                             |
| `installments_mode`                 | Installments Mode                | `selection` |     | ✅    |                             |
| `installments_switch_amount`        | Installments Switch Amount       | `monetary`  |     |       |                             |
| `installments_switch_html`          | Installments Switch Html         | `html`      |     |       |                             |
| `is_register_payment_on_draft`      | Is Register Payment On Draft     | `boolean`   |     |       |                             |
| `journal_id`                        | Journal                          | `many2one`  |     | ✅    | account.journal             |
| `line_ids`                          | Journal items                    | `many2many` |     | ✅    | account.move.line           |
| `missing_account_partners`          | Missing Account Partners         | `many2many` |     |       | res.partner                 |
| `partner_bank_id`                   | Recipient Bank Account           | `many2one`  |     | ✅    | res.partner.bank            |
| `partner_id`                        | Customer/Vendor                  | `many2one`  |     | ✅    | res.partner                 |
| `partner_type`                      | Partner Type                     | `selection` |     | ✅    |                             |
| `payment_date`                      | Payment Date                     | `date`      | ✅  | ✅    |                             |
| `payment_difference`                | Payment Difference               | `monetary`  |     |       |                             |
| `payment_difference_handling`       | Payment Difference Handling      | `selection` |     | ✅    |                             |
| `payment_method_code`               | Code                             | `char`      |     |       |                             |
| `payment_method_line_id`            | Payment Method                   | `many2one`  |     | ✅    | account.payment.method.line |
| `payment_token_id`                  | Saved payment token              | `many2one`  |     | ✅    | payment.token               |
| `payment_type`                      | Payment Type                     | `selection` |     | ✅    |                             |
| `qr_code`                           | QR Code URL                      | `html`      |     |       |                             |
| `require_partner_bank_account`      | Require Partner Bank Account     | `boolean`   |     |       |                             |
| `show_partner_bank_account`         | Show Partner Bank Account        | `boolean`   |     |       |                             |
| `show_payment_difference`           | Show Payment Difference          | `boolean`   |     |       |                             |
| `source_amount`                     | Amount to Pay (company currency) | `monetary`  |     | ✅    |                             |
| `source_amount_currency`            | Amount to Pay (foreign currency) | `monetary`  |     | ✅    |                             |
| `source_currency_id`                | Source Currency                  | `many2one`  |     | ✅    | res.currency                |
| `suitable_payment_token_ids`        | Suitable Payment Token           | `many2many` |     |       | payment.token               |
| `total_payments_amount`             | Total Payments Amount            | `integer`   |     |       |                             |
| `untrusted_bank_ids`                | Untrusted Bank                   | `many2many` |     |       | res.partner.bank            |
| `untrusted_payments_count`          | Untrusted Payments Count         | `integer`   |     |       |                             |
| `use_electronic_payment_method`     | Use Electronic Payment Method    | `boolean`   |     |       |                             |
| `write_date`                        | Last Updated on                  | `datetime`  |     | ✅    |                             |
| `writeoff_account_id`               | Difference Account               | `many2one`  |     | ✅    | account.account             |
| `writeoff_is_exchange_account`      | Writeoff Is Exchange Account     | `boolean`   |     |       |                             |
| `writeoff_label`                    | Journal Item Label               | `char`      |     | ✅    |                             |
| `write_uid`                         | Last Updated by                  | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                            | Group                  | Perms   |
| ------------------------------- | ---------------------- | ------- |
| access.account.payment.register | Accounting / Invoicing | `R/W/C` |

### 🗃️ `account.payment.method` — Payment Methods

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation  |
| -------------- | --------------- | ----------- | --- | ----- | --------- |
| `code`         | Code            | `char`      | ✅  | ✅    |           |
| `create_date`  | Created on      | `datetime`  |     | ✅    |           |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users |
| `display_name` | Display Name    | `char`      |     |       |           |
| `id`           | ID              | `integer`   |     | ✅    |           |
| `name`         | Name            | `char`      | ✅  | ✅    |           |
| `payment_type` | Payment Type    | `selection` | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                   | Group                  | Perms   |
| ---------------------- | ---------------------- | ------- |
| account.payment.method | Accounting / Invoicing | `R/W/D` |
| account.payment.method | Role / User            | `R`     |

### 🗃️ `account.payment.method.line` — Payment Methods

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                          | Label                    | Type        | Req | Store | Relation               |
| ------------------------------ | ------------------------ | ----------- | --- | ----- | ---------------------- |
| `available_payment_method_ids` | Available Payment Method | `many2many` |     |       | account.payment.method |
| `code`                         | Code                     | `char`      |     |       |                        |
| `company_id`                   | Company                  | `many2one`  |     |       | res.company            |
| `create_date`                  | Created on               | `datetime`  |     | ✅    |                        |
| `create_uid`                   | Created by               | `many2one`  |     | ✅    | res.users              |
| `default_account_id`           | Default Account          | `many2one`  |     |       | account.account        |
| `display_name`                 | Display Name             | `char`      |     |       |                        |
| `id`                           | ID                       | `integer`   |     | ✅    |                        |
| `journal_id`                   | Journal                  | `many2one`  |     | ✅    | account.journal        |
| `name`                         | Name                     | `char`      |     | ✅    |                        |
| `payment_account_id`           | Payment Account          | `many2one`  |     | ✅    | account.account        |
| `payment_method_id`            | Payment Method           | `many2one`  | ✅  | ✅    | account.payment.method |
| `payment_provider_id`          | Payment Provider         | `many2one`  |     | ✅    | payment.provider       |
| `payment_provider_state`       | State                    | `selection` |     |       |                        |
| `payment_type`                 | Payment Type             | `selection` |     |       |                        |
| `sequence`                     | Sequence                 | `integer`   |     | ✅    |                        |
| `write_date`                   | Last Updated on          | `datetime`  |     | ✅    |                        |
| `write_uid`                    | Last Updated by          | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                        | Group                  | Perms     |
| --------------------------- | ---------------------- | --------- |
| account.payment.method.line | Accounting / Invoicing | `R/W/C/D` |
| account.payment.method.line | Role / User            | `R`       |

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

### 🗃️ `payment.refund.wizard` — Payment Refund Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                         | Label                  | Type        | Req | Store | Relation            |
| ----------------------------- | ---------------------- | ----------- | --- | ----- | ------------------- |
| `amount_available_for_refund` | Maximum Refund Allowed | `monetary`  |     |       |                     |
| `amount_to_refund`            | Refund Amount          | `monetary`  |     | ✅    |                     |
| `create_date`                 | Created on             | `datetime`  |     | ✅    |                     |
| `create_uid`                  | Created by             | `many2one`  |     | ✅    | res.users           |
| `currency_id`                 | Currency               | `many2one`  |     |       | res.currency        |
| `display_name`                | Display Name           | `char`      |     |       |                     |
| `has_pending_refund`          | Has a pending refund   | `boolean`   |     |       |                     |
| `id`                          | ID                     | `integer`   |     | ✅    |                     |
| `payment_amount`              | Payment Amount         | `monetary`  |     |       |                     |
| `payment_id`                  | Payment                | `many2one`  |     | ✅    | account.payment     |
| `refunded_amount`             | Refunded Amount        | `monetary`  |     |       |                     |
| `support_refund`              | Refund                 | `selection` |     |       |                     |
| `transaction_id`              | Payment Transaction    | `many2one`  |     |       | payment.transaction |
| `write_date`                  | Last Updated on        | `datetime`  |     | ✅    |                     |
| `write_uid`                   | Last Updated by        | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                  | Group                  | Perms   |
| --------------------- | ---------------------- | ------- |
| payment.refund.wizard | Accounting / Invoicing | `R/W/C` |

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
