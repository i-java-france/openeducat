---
title: "Import/Export electronic orders with UBL"
module: "purchase_edi_ubl_bis3"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Purchase"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/________]
---

# 🟢 Import/Export electronic orders with UBL

> **Module:** `purchase_edi_ubl_bis3` | **Version:** `19.0.1.0` **Category:** Purchase |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[purchase]] [[account_edi_ubl_cii]]

## 📖 Description

Allows to export and import formats: UBL Bis 3. When generating the PDF on the order,
the PDF will be embedded inside the xml for all UBL formats. This allows the receiver to
retrieve the PDF with only the xml file.

## 🖥️ UI Components

### Menus

_none_

### Views

_none_

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

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

### 🗃️ `purchase.order` — Purchase Order

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                             | Label                                                                     | Type        | Req | Store | Relation                |
| --------------------------------- | ------------------------------------------------------------------------- | ----------- | --- | ----- | ----------------------- |
| `access_token`                    | Security Token                                                            | `char`      |     | ✅    |                         |
| `access_url`                      | Portal Access URL                                                         | `char`      |     |       |                         |
| `access_warning`                  | Access warning                                                            | `text`      |     |       |                         |
| `acknowledged`                    | Acknowledged                                                              | `boolean`   |     | ✅    |                         |
| `activity_calendar_event_id`      | Next Activity Calendar Event                                              | `many2one`  |     |       | calendar.event          |
| `activity_date_deadline`          | Next Activity Deadline                                                    | `date`      |     |       |                         |
| `activity_exception_decoration`   | Activity Exception Decoration                                             | `selection` |     |       |                         |
| `activity_exception_icon`         | Icon                                                                      | `char`      |     |       |                         |
| `activity_ids`                    | Activities                                                                | `one2many`  |     | ✅    | mail.activity           |
| `activity_state`                  | Activity State                                                            | `selection` |     |       |                         |
| `activity_summary`                | Next Activity Summary                                                     | `char`      |     |       |                         |
| `activity_type_icon`              | Activity Type Icon                                                        | `char`      |     |       |                         |
| `activity_type_id`                | Next Activity Type                                                        | `many2one`  |     |       | mail.activity.type      |
| `activity_user_id`                | Responsible User                                                          | `many2one`  |     |       | res.users               |
| `amount_tax`                      | Taxes                                                                     | `monetary`  |     | ✅    |                         |
| `amount_total`                    | Total                                                                     | `monetary`  |     | ✅    |                         |
| `amount_total_cc`                 | Total in currency                                                         | `monetary`  |     | ✅    |                         |
| `amount_untaxed`                  | Untaxed Amount                                                            | `monetary`  |     | ✅    |                         |
| `company_currency_id`             | Company Currency                                                          | `many2one`  |     |       | res.currency            |
| `company_id`                      | Company                                                                   | `many2one`  | ✅  | ✅    | res.company             |
| `company_price_include`           | Default Sales Price Include                                               | `selection` |     |       |                         |
| `country_code`                    | Country code                                                              | `char`      |     |       |                         |
| `create_date`                     | Created on                                                                | `datetime`  |     | ✅    |                         |
| `create_uid`                      | Created by                                                                | `many2one`  |     | ✅    | res.users               |
| `currency_id`                     | Currency                                                                  | `many2one`  | ✅  | ✅    | res.currency            |
| `currency_rate`                   | Currency Rate                                                             | `float`     |     | ✅    |                         |
| `date_approve`                    | Confirmation Date                                                         | `datetime`  |     | ✅    |                         |
| `date_calendar_start`             | Date Calendar Start                                                       | `datetime`  |     | ✅    |                         |
| `date_order`                      | Order Deadline                                                            | `datetime`  | ✅  | ✅    |                         |
| `date_planned`                    | Expected Arrival                                                          | `datetime`  |     | ✅    |                         |
| `default_location_dest_id_usage`  | Destination Location Type                                                 | `selection` |     |       |                         |
| `dest_address_id`                 | Dropship Address                                                          | `many2one`  |     | ✅    | res.partner             |
| `display_name`                    | Display Name                                                              | `char`      |     |       |                         |
| `duplicated_order_ids`            | Duplicated Order                                                          | `many2many` |     |       | purchase.order          |
| `effective_date`                  | Arrival                                                                   | `datetime`  |     | ✅    |                         |
| `fiscal_position_id`              | Fiscal Position                                                           | `many2one`  |     | ✅    | account.fiscal.position |
| `has_message`                     | Has Message                                                               | `boolean`   |     |       |                         |
| `has_sale_order`                  | Technical field for whether the purchase order has associated sale orders | `boolean`   |     |       |                         |
| `id`                              | ID                                                                        | `integer`   |     | ✅    |                         |
| `incoming_picking_count`          | Incoming Shipment count                                                   | `integer`   |     |       |                         |
| `incoterm_id`                     | Incoterm                                                                  | `many2one`  |     | ✅    | account.incoterms       |
| `incoterm_location`               | Incoterm Location                                                         | `char`      |     | ✅    |                         |
| `invoice_count`                   | Bill Count                                                                | `integer`   |     | ✅    |                         |
| `invoice_ids`                     | Bills                                                                     | `many2many` |     | ✅    | account.move            |
| `invoice_status`                  | Billing Status                                                            | `selection` |     | ✅    |                         |
| `is_late`                         | Is Late                                                                   | `boolean`   |     |       |                         |
| `is_shipped`                      | Is Shipped                                                                | `boolean`   |     |       |                         |
| `lock_confirmed_po`               | Purchase Order Modification                                               | `selection` |     |       |                         |
| `locked`                          | Locked                                                                    | `boolean`   |     | ✅    |                         |
| `message_attachment_count`        | Attachment Count                                                          | `integer`   |     |       |                         |
| `message_follower_ids`            | Followers                                                                 | `one2many`  |     | ✅    | mail.followers          |
| `message_has_error`               | Message Delivery error                                                    | `boolean`   |     |       |                         |
| `message_has_error_counter`       | Number of errors                                                          | `integer`   |     |       |                         |
| `message_has_sms_error`           | SMS Delivery error                                                        | `boolean`   |     |       |                         |
| `message_ids`                     | Messages                                                                  | `one2many`  |     | ✅    | mail.message            |
| `message_is_follower`             | Is Follower                                                               | `boolean`   |     |       |                         |
| `message_needaction`              | Action Needed                                                             | `boolean`   |     |       |                         |
| `message_needaction_counter`      | Number of Actions                                                         | `integer`   |     |       |                         |
| `message_partner_ids`             | Followers (Partners)                                                      | `many2many` |     |       | res.partner             |
| `my_activity_date_deadline`       | My Activity Deadline                                                      | `date`      |     |       |                         |
| `name`                            | Order Reference                                                           | `char`      | ✅  | ✅    |                         |
| `note`                            | Terms and Conditions                                                      | `html`      |     | ✅    |                         |
| `on_time_rate`                    | On-Time Delivery Rate                                                     | `float`     |     |       |                         |
| `order_line`                      | Order Lines                                                               | `one2many`  |     | ✅    | purchase.order.line     |
| `origin`                          | Source                                                                    | `char`      |     | ✅    |                         |
| `partner_bill_count`              | # Vendor Bills                                                            | `integer`   |     |       |                         |
| `partner_id`                      | Vendor                                                                    | `many2one`  | ✅  | ✅    | res.partner             |
| `partner_ref`                     | Vendor Reference                                                          | `char`      |     | ✅    |                         |
| `payment_term_id`                 | Payment Terms                                                             | `many2one`  |     | ✅    | account.payment.term    |
| `picking_ids`                     | Receptions                                                                | `many2many` |     | ✅    | stock.picking           |
| `picking_type_id`                 | Deliver To                                                                | `many2one`  | ✅  | ✅    | stock.picking.type      |
| `priority`                        | Priority                                                                  | `selection` |     | ✅    |                         |
| `product_id`                      | Product                                                                   | `many2one`  |     |       | product.product         |
| `purchase_warning_text`           | Purchase Warning                                                          | `text`      |     |       |                         |
| `rating_ids`                      | Ratings                                                                   | `one2many`  |     | ✅    | rating.rating           |
| `receipt_reminder_email`          | Receipt Reminder Email                                                    | `boolean`   |     | ✅    |                         |
| `receipt_status`                  | Receipt Status                                                            | `selection` |     | ✅    |                         |
| `reference_ids`                   | References                                                                | `many2many` |     | ✅    | stock.reference         |
| `reminder_date_before_receipt`    | Days Before Receipt                                                       | `integer`   |     | ✅    |                         |
| `sale_order_count`                | Number of Source Sale                                                     | `integer`   |     |       |                         |
| `show_comparison`                 | Show Comparison                                                           | `boolean`   |     |       |                         |
| `state`                           | Status                                                                    | `selection` |     | ✅    |                         |
| `tax_calculation_rounding_method` | Tax calculation rounding method                                           | `selection` |     |       |                         |
| `tax_country_id`                  | Tax Country                                                               | `many2one`  |     |       | res.country             |
| `tax_totals`                      | Tax Totals                                                                | `binary`    |     |       |                         |
| `user_id`                         | Buyer                                                                     | `many2one`  |     | ✅    | res.users               |
| `website_message_ids`             | Website Messages                                                          | `one2many`  |     | ✅    | mail.message            |
| `write_date`                      | Last Updated on                                                           | `datetime`  |     | ✅    |                         |
| `write_uid`                       | Last Updated by                                                           | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name                  | Group                    | Perms     |
| --------------------- | ------------------------ | --------- |
| purchase.order        | Accounting / Invoicing   | `R/W`     |
| purchase.order        | Purchase / User          | `R/W/C/D` |
| purchase.order        | Purchase / Administrator | `R/W/C/D` |
| purchase.order        | Inventory / User         | `R`       |
| purchase.order        | Auditor                  | `R`       |
| purchase.order.portal | Role / Portal            | `R`       |

**Record Rules:**

- **Purchase Order multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`
- **Portal Purchase Orders** (10) `R/W/D`
  - Domain: `[('partner_id', 'child_of', [user.commercial_partner_id.id])]`

### 🗃️ `purchase.edi.xml.ubl_bis3` — Purchase UBL BIS Ordering 3.5

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |
