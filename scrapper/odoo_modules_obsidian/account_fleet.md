---
title: "Accounting/Fleet bridge"
module: "account_fleet"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Accounting"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/__________]
---

# 🟢 Accounting/Fleet bridge

> **Module:** `account_fleet` | **Version:** `19.0.1.0` **Category:** Accounting |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[fleet]] [[account]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT account.move.form (form)`
- `* INHERIT account.move.list.inherit.fleet (list)`
- `* INHERIT fleet.vehicle.form (form)`
- `* INHERIT fleet.vehicle.log.services.form.inherit.account (form)`
- `* INHERIT view.move.line.list.fleet (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**5 model(s) defined by this module:**

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

### 🗃️ `fleet.vehicle.log.services` — Services for vehicles

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                  |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------- |
| `account_move_line_id`          | Account Move Line             | `many2one`  |     | ✅    | account.move.line         |
| `account_move_state`            | Status                        | `selection` |     |       |                           |
| `active`                        | Active                        | `boolean`   |     | ✅    |                           |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event            |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                           |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                           |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                           |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity             |
| `activity_state`                | Activity State                | `selection` |     |       |                           |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                           |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                           |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type        |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users                 |
| `amount`                        | Cost                          | `monetary`  |     | ✅    |                           |
| `brand_id`                      | Brand                         | `many2one`  |     | ✅    | fleet.vehicle.model.brand |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company               |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                           |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users                 |
| `currency_id`                   | Currency                      | `many2one`  |     |       | res.currency              |
| `date`                          | Date                          | `date`      |     | ✅    |                           |
| `description`                   | Description                   | `char`      |     | ✅    |                           |
| `display_name`                  | Display Name                  | `char`      |     |       |                           |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                           |
| `id`                            | ID                            | `integer`   |     | ✅    |                           |
| `inv_ref`                       | Vendor Reference              | `char`      |     | ✅    |                           |
| `manager_id`                    | Fleet Manager                 | `many2one`  |     | ✅    | res.users                 |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                           |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers            |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                           |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                           |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                           |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message              |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                           |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                           |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                           |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner               |
| `model_id`                      | Model                         | `many2one`  |     | ✅    | fleet.vehicle.model       |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                           |
| `notes`                         | Notes                         | `text`      |     | ✅    |                           |
| `odometer`                      | Odometer Value                | `float`     |     |       |                           |
| `odometer_id`                   | Odometer                      | `many2one`  |     | ✅    | fleet.vehicle.odometer    |
| `odometer_unit`                 | Unit                          | `selection` |     |       |                           |
| `purchaser_employee_id`         | Driver (Employee)             | `many2one`  |     | ✅    | hr.employee               |
| `purchaser_id`                  | Driver                        | `many2one`  |     | ✅    | res.partner               |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating             |
| `service_type_id`               | Service Type                  | `many2one`  | ✅  | ✅    | fleet.service.type        |
| `state`                         | Stage                         | `selection` |     | ✅    |                           |
| `vehicle_id`                    | Vehicle                       | `many2one`  | ✅  | ✅    | fleet.vehicle             |
| `vendor_id`                     | Vendor                        | `many2one`  |     | ✅    | res.partner               |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message              |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                           |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name                                    | Group                                | Perms     |
| --------------------------------------- | ------------------------------------ | --------- |
| fleet_vehicle_log_services_access_right | Fleet / Officer: Manage all vehicles | `R`       |
| fleet_vehicle_log_services_access_right | Fleet / Administrator                | `R/W/C/D` |

**Record Rules:**

- **Administrator has all rights on vehicle's services** (21) `R/W/C/D`
- **Fleet log services: Multi Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `fleet.vehicle` — Vehicle

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type         | Req | Store | Relation                      |
| ------------------------------- | ----------------------------- | ------------ | --- | ----- | ----------------------------- |
| `account_move_ids`              | Account Move                  | `one2many`   |     |       | account.move                  |
| `acquisition_date`              | Registration Date             | `date`       |     | ✅    |                               |
| `active`                        | Active                        | `boolean`    |     | ✅    |                               |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`   |     |       | calendar.event                |
| `activity_date_deadline`        | Next Activity Deadline        | `date`       |     |       |                               |
| `activity_exception_decoration` | Activity Exception Decoration | `selection`  |     |       |                               |
| `activity_exception_icon`       | Icon                          | `char`       |     |       |                               |
| `activity_ids`                  | Activities                    | `one2many`   |     | ✅    | mail.activity                 |
| `activity_state`                | Activity State                | `selection`  |     |       |                               |
| `activity_summary`              | Next Activity Summary         | `char`       |     |       |                               |
| `activity_type_icon`            | Activity Type Icon            | `char`       |     |       |                               |
| `activity_type_id`              | Next Activity Type            | `many2one`   |     |       | mail.activity.type            |
| `activity_user_id`              | Responsible User              | `many2one`   |     |       | res.users                     |
| `avatar_1024`                   | Avatar 1024                   | `binary`     |     |       |                               |
| `avatar_128`                    | Avatar 128                    | `binary`     |     |       |                               |
| `avatar_1920`                   | Avatar                        | `binary`     |     |       |                               |
| `avatar_256`                    | Avatar 256                    | `binary`     |     |       |                               |
| `avatar_512`                    | Avatar 512                    | `binary`     |     |       |                               |
| `bill_count`                    | Bills Count                   | `integer`    |     |       |                               |
| `brand_id`                      | Brand                         | `many2one`   |     | ✅    | fleet.vehicle.model.brand     |
| `car_value`                     | Catalog Value (VAT Incl.)     | `float`      |     | ✅    |                               |
| `category_id`                   | Category                      | `many2one`   |     | ✅    | fleet.vehicle.model.category  |
| `co2`                           | CO₂ Emissions                 | `float`      |     | ✅    |                               |
| `co2_emission_unit`             | Co2 Emission Unit             | `selection`  | ✅  | ✅    |                               |
| `co2_standard`                  | Emission Standard             | `char`       |     | ✅    |                               |
| `color`                         | Color                         | `char`       |     | ✅    |                               |
| `company_id`                    | Company                       | `many2one`   |     | ✅    | res.company                   |
| `contract_count`                | Contract Count                | `integer`    |     |       |                               |
| `contract_date_start`           | First Contract Date           | `date`       |     | ✅    |                               |
| `contract_renewal_due_soon`     | Has Contracts to renew        | `boolean`    |     |       |                               |
| `contract_renewal_overdue`      | Has Contracts Overdue         | `boolean`    |     |       |                               |
| `contract_state`                | Last Contract State           | `selection`  |     |       |                               |
| `country_code`                  | Country Code                  | `char`       |     |       |                               |
| `country_id`                    | Country                       | `many2one`   |     |       | res.country                   |
| `create_date`                   | Created on                    | `datetime`   |     | ✅    |                               |
| `create_uid`                    | Created by                    | `many2one`   |     | ✅    | res.users                     |
| `currency_id`                   | Currency                      | `many2one`   |     |       | res.currency                  |
| `description`                   | Vehicle Description           | `html`       |     | ✅    |                               |
| `display_name`                  | Display Name                  | `char`       |     |       |                               |
| `doors`                         | Number of Doors               | `integer`    |     | ✅    |                               |
| `driver_employee_id`            | Driver (Employee)             | `many2one`   |     | ✅    | hr.employee                   |
| `driver_employee_name`          | Employee Name                 | `char`       |     |       |                               |
| `driver_id`                     | Driver                        | `many2one`   |     | ✅    | res.partner                   |
| `electric_assistance`           | Electric Assistance           | `boolean`    |     | ✅    |                               |
| `frame_size`                    | Frame Size                    | `float`      |     | ✅    |                               |
| `frame_type`                    | Bike Frame Type               | `selection`  |     | ✅    |                               |
| `fuel_type`                     | Fuel Type                     | `selection`  |     | ✅    |                               |
| `future_driver_employee_id`     | Future Driver (Employee)      | `many2one`   |     | ✅    | hr.employee                   |
| `future_driver_id`              | Future Driver                 | `many2one`   |     | ✅    | res.partner                   |
| `has_message`                   | Has Message                   | `boolean`    |     |       |                               |
| `history_count`                 | Drivers History Count         | `integer`    |     |       |                               |
| `horsepower`                    | Horsepower                    | `float`      |     | ✅    |                               |
| `horsepower_tax`                | Horsepower Taxation           | `float`      |     | ✅    |                               |
| `id`                            | ID                            | `integer`    |     | ✅    |                               |
| `image_1024`                    | Image 1024                    | `binary`     |     | ✅    |                               |
| `image_128`                     | Image 128                     | `binary`     |     | ✅    |                               |
| `image_1920`                    | Image                         | `binary`     |     | ✅    |                               |
| `image_256`                     | Image 256                     | `binary`     |     | ✅    |                               |
| `image_512`                     | Image 512                     | `binary`     |     | ✅    |                               |
| `license_plate`                 | License Plate                 | `char`       |     | ✅    |                               |
| `location`                      | Location                      | `char`       |     | ✅    |                               |
| `log_contracts`                 | Contracts                     | `one2many`   |     | ✅    | fleet.vehicle.log.contract    |
| `log_drivers`                   | Assignment Logs               | `one2many`   |     | ✅    | fleet.vehicle.assignation.log |
| `log_services`                  | Services Logs                 | `one2many`   |     | ✅    | fleet.vehicle.log.services    |
| `manager_id`                    | Fleet Manager                 | `many2one`   |     | ✅    | res.users                     |
| `message_attachment_count`      | Attachment Count              | `integer`    |     |       |                               |
| `message_follower_ids`          | Followers                     | `one2many`   |     | ✅    | mail.followers                |
| `message_has_error`             | Message Delivery error        | `boolean`    |     |       |                               |
| `message_has_error_counter`     | Number of errors              | `integer`    |     |       |                               |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`    |     |       |                               |
| `message_ids`                   | Messages                      | `one2many`   |     | ✅    | mail.message                  |
| `message_is_follower`           | Is Follower                   | `boolean`    |     |       |                               |
| `message_needaction`            | Action Needed                 | `boolean`    |     |       |                               |
| `message_needaction_counter`    | Number of Actions             | `integer`    |     |       |                               |
| `message_partner_ids`           | Followers (Partners)          | `many2many`  |     |       | res.partner                   |
| `mobility_card`                 | Mobility Card                 | `char`       |     | ✅    |                               |
| `model_id`                      | Model                         | `many2one`   | ✅  | ✅    | fleet.vehicle.model           |
| `model_year`                    | Model Year                    | `selection`  |     | ✅    |                               |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`       |     |       |                               |
| `name`                          | Name                          | `char`       |     | ✅    |                               |
| `net_car_value`                 | Purchase Value                | `float`      |     | ✅    |                               |
| `next_assignation_date`         | Assignment Date               | `date`       |     | ✅    |                               |
| `odometer`                      | Last Odometer                 | `float`      |     |       |                               |
| `odometer_count`                | Odometer                      | `integer`    |     |       |                               |
| `odometer_unit`                 | Odometer Unit                 | `selection`  | ✅  | ✅    |                               |
| `order_date`                    | Order Date                    | `date`       |     | ✅    |                               |
| `plan_to_change_bike`           | Plan To Change Bike           | `boolean`    |     | ✅    |                               |
| `plan_to_change_car`            | Plan To Change Car            | `boolean`    |     | ✅    |                               |
| `power`                         | Power                         | `float`      |     | ✅    |                               |
| `power_unit`                    | Power Unit                    | `selection`  | ✅  | ✅    |                               |
| `range_unit`                    | Range Unit                    | `selection`  | ✅  | ✅    |                               |
| `rating_ids`                    | Ratings                       | `one2many`   |     | ✅    | rating.rating                 |
| `residual_value`                | Residual Value                | `float`      |     | ✅    |                               |
| `seats`                         | Seating Capacity              | `integer`    |     | ✅    |                               |
| `service_activity`              | Service Activity              | `selection`  |     |       |                               |
| `service_count`                 | Services                      | `integer`    |     |       |                               |
| `state_id`                      | State                         | `many2one`   |     | ✅    | fleet.vehicle.state           |
| `tag_ids`                       | Tags                          | `many2many`  |     | ✅    | fleet.vehicle.tag             |
| `trailer_hook`                  | Trailer Hitch                 | `boolean`    |     | ✅    |                               |
| `transmission`                  | Transmission                  | `selection`  |     | ✅    |                               |
| `vehicle_properties`            | Properties                    | `properties` |     | ✅    |                               |
| `vehicle_range`                 | Range                         | `integer`    |     | ✅    |                               |
| `vehicle_type`                  | Vehicle Type                  | `selection`  |     |       |                               |
| `vin_sn`                        | Chassis Number                | `char`       |     | ✅    |                               |
| `website_message_ids`           | Website Messages              | `one2many`   |     | ✅    | mail.message                  |
| `write_date`                    | Last Updated on               | `datetime`   |     | ✅    |                               |
| `write_off_date`                | Cancellation Date             | `date`       |     | ✅    |                               |
| `write_uid`                     | Last Updated by               | `many2one`   |     | ✅    | res.users                     |

**Access Rights:**

| Name                                     | Group                                     | Perms     |
| ---------------------------------------- | ----------------------------------------- | --------- |
| hr_fleet_vehicle_access_right_hr_officer | Employees / Officer: Manage all employees | `R`       |
| fleet_vehicle_access_right               | Fleet / Officer: Manage all vehicles      | `R/W/C/D` |
| fleet_vehicle_access_right               | Fleet / Administrator                     | `R/W/C/D` |
| name_fleet_vehicle_transport_user        | Transportation Privilege / User           | `R`       |

**Record Rules:**

- **Administrator has all rights on vehicle** (21) `R/W/C/D`
- **Fleet vehicle: Multi Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Hr Officer read rights on vehicle with employees assigned** (49) `R`
  - Domain:
    `['|', ('driver_employee_id', '!=', False), ('future_driver_employee_id', '!=', False)]`

### 🗃️ `account.automatic.entry.wizard` — Create Automatic Entries

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                     | Label                      | Type        | Req | Store | Relation          |
| ------------------------- | -------------------------- | ----------- | --- | ----- | ----------------- |
| `account_type`            | Account Type               | `selection` |     | ✅    |                   |
| `action`                  | Action                     | `selection` | ✅  | ✅    |                   |
| `company_currency_id`     | Currency                   | `many2one`  |     |       | res.currency      |
| `company_id`              | Company                    | `many2one`  | ✅  | ✅    | res.company       |
| `create_date`             | Created on                 | `datetime`  |     | ✅    |                   |
| `create_uid`              | Created by                 | `many2one`  |     | ✅    | res.users         |
| `date`                    | Date                       | `date`      | ✅  | ✅    |                   |
| `destination_account_id`  | To                         | `many2one`  |     | ✅    | account.account   |
| `display_currency_helper` | Currency Conversion Helper | `boolean`   |     |       |                   |
| `display_name`            | Display Name               | `char`      |     |       |                   |
| `expense_accrual_account` | Expense Accrual Account    | `many2one`  |     |       | account.account   |
| `id`                      | ID                         | `integer`   |     | ✅    |                   |
| `journal_id`              | Journal                    | `many2one`  | ✅  |       | account.journal   |
| `lock_date_message`       | Lock Date Message          | `char`      |     |       |                   |
| `move_data`               | Move Data                  | `text`      |     |       |                   |
| `move_line_ids`           | Move Line                  | `many2many` |     | ✅    | account.move.line |
| `percentage`              | Percentage                 | `float`     |     | ✅    |                   |
| `preview_move_data`       | Preview Move Data          | `text`      |     |       |                   |
| `revenue_accrual_account` | Revenue Accrual Account    | `many2one`  |     |       | account.account   |
| `total_amount`            | Total Amount               | `monetary`  |     | ✅    |                   |
| `write_date`              | Last Updated on            | `datetime`  |     | ✅    |                   |
| `write_uid`               | Last Updated by            | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                                  | Group                | Perms   |
| ------------------------------------- | -------------------- | ------- |
| access.account.automatic.entry.wizard | Contact / Accountant | `R/W/C` |

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
