---
title: "Sales"
module: "sale_management"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/app/sales"
license: "LGPL-3"
category: "Sales"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_____, odoo/app]
---

# 🟢 Sales

> **Module:** `sale_management` | **Version:** `19.0.1.0` **Category:** Sales |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:**
> https://www.odoo.com/app/sales

## 🔗 Dependencies

[[sale]] [[digest]]

## 📖 Description

# Manage sales quotations and orders

This application allows you to manage your sales goals in an effective and efficient
manner by keeping track of all sales orders and history.

It handles the full sales workflow:

- **Quotation** -> **Sales order** -> **Invoice**

## Preferences (only with Warehouse Management installed)

If you also installed the Warehouse Management, you can deal with the following
preferences:

- Shipping: Choice of delivery at once or partial delivery
- Invoicing: choose how invoices will be paid
- Incoterms: International Commercial terms

With this module you can personnalize the sales order and invoice report with
categories, subtotals or page-breaks.

## The Dashboard for the Sales Manager will include

- My Quotations
- Monthly Turnover (Graph)

## 🖥️ UI Components

### Menus

- `Sales/Configuration/Sales Orders/Quotation Templates`

### Views

- `* INHERIT Order Options (qweb)`
- `* INHERIT digest.digest.view.form.inherit.sale_management (form)`
- `* INHERIT res.config.settings.view.form.inherit.sale.management (form)`
- `* INHERIT sale.order.form.inherit.sale_management (form)`
- `Order Quantity (qweb)`
- `sale.order.template.form (form)`
- `sale.order.template.list (list)`
- `sale.order.template.search (search)`

### Reports

_none_

## 🛠️ Technical Documentation

**7 model(s) defined by this module:**

### 🗃️ `res.company` — Companies

> 📧 Mail Thread

Advanced orchestration layer for exchange rate management

**Fields:**

| Field                                                | Label                                                  | Type                    | Req | Store | Relation                    |
| ---------------------------------------------------- | ------------------------------------------------------ | ----------------------- | --- | ----- | --------------------------- |
| `account_cash_basis_base_account_id`                 | Base Tax Received Account                              | `many2one`              |     | ✅    | account.account             |
| `account_default_pos_receivable_account_id`          | Default PoS Receivable Account                         | `many2one`              |     | ✅    | account.account             |
| `account_discount_expense_allocation_id`             | Separate account for expense discount                  | `many2one`              |     | ✅    | account.account             |
| `account_discount_income_allocation_id`              | Separate account for income discount                   | `many2one`              |     | ✅    | account.account             |
| `account_enabled_tax_country_ids`                    | l10n-used countries                                    | `many2many`             |     |       | res.country                 |
| `account_fiscal_country_group_codes`                 | Account Fiscal Country Group Codes                     | `json`                  |     |       |                             |
| `account_fiscal_country_id`                          | Fiscal Country                                         | `many2one`              |     | ✅    | res.country                 |
| `account_journal_early_pay_discount_gain_account_id` | Cash Discount Write-Off Gain Account                   | `many2one`              |     | ✅    | account.account             |
| `account_journal_early_pay_discount_loss_account_id` | Cash Discount Write-Off Loss Account                   | `many2one`              |     | ✅    | account.account             |
| `account_journal_suspense_account_id`                | Journal Suspense Account                               | `many2one`              |     | ✅    | account.account             |
| `account_opening_date`                               | Opening Entry                                          | `date`                  |     | ✅    |                             |
| `account_opening_journal_id`                         | Opening Journal                                        | `many2one`              |     |       | account.journal             |
| `account_opening_move_id`                            | Opening Journal Entry                                  | `many2one`              |     | ✅    | account.move                |
| `account_price_include`                              | Default Sales Price Include                            | `selection`             | ✅  | ✅    |                             |
| `account_production_wip_account_id`                  | Production WIP Account                                 | `many2one`              |     | ✅    | account.account             |
| `account_production_wip_overhead_account_id`         | Production WIP Overhead Account                        | `many2one`              |     | ✅    | account.account             |
| `account_purchase_receipt_fiscal_position_id`        | Default Purchase Receipt Fiscal Position               | `many2one`              |     | ✅    | account.fiscal.position     |
| `account_purchase_tax_id`                            | Default Purchase Tax                                   | `many2one`              |     | ✅    | account.tax                 |
| `account_sale_tax_id`                                | Default Sale Tax                                       | `many2one`              |     | ✅    | account.tax                 |
| `account_stock_journal_id`                           | Stock Journal                                          | `many2one`              |     | ✅    | account.journal             |
| `account_stock_valuation_id`                         | Stock Valuation Account                                | `many2one`              |     | ✅    | account.account             |
| `account_storno`                                     | Storno accounting                                      | `boolean`               |     | ✅    |                             |
| `account_use_credit_limit`                           | Sales Credit Limit                                     | `boolean`               |     | ✅    |                             |
| `accreditation`                                      | Accreditation                                          | `text`                  |     | ✅    |                             |
| `active`                                             | Active                                                 | `boolean`               |     | ✅    |                             |
| `affiliation_ids`                                    | Affiliation Board                                      | `one2many`              |     | ✅    | op.board.affiliation        |
| `alias_domain_id`                                    | Email Domain                                           | `many2one`              |     | ✅    | mail.alias.domain           |
| `all_child_ids`                                      | All Child                                              | `one2many`              |     | ✅    | res.company                 |
| `anglo_saxon_accounting`                             | Use anglo-saxon accounting                             | `boolean`               |     | ✅    |                             |
| `annual_inventory_day`                               | Day of the month                                       | `integer`               |     | ✅    |                             |
| `annual_inventory_month`                             | Annual Inventory Month                                 | `selection`             |     | ✅    |                             |
| `approval_authority`                                 | Approval Authority                                     | `text`                  |     | ✅    |                             |
| `automatic_entry_default_journal_id`                 | Automatic Entry Default Journal                        | `many2one`              |     | ✅    | account.journal             |
| `autopost_bills`                                     | Auto-validate bills                                    | `boolean`               |     | ✅    |                             |
| `bank_account_code_prefix`                           | Prefix of the bank accounts                            | `char`                  |     | ✅    |                             |
| `bank_ids`                                           | Banks                                                  | `one2many`              |     |       | res.partner.bank            |
| `bank_journal_ids`                                   | Bank Journals                                          | `one2many`              |     | ✅    | account.journal             |
| `batch_payment_sequence_id`                          | Batch Payment Sequence                                 | `many2one`              |     | ✅    | ir.sequence                 |
| `bounce_email`                                       | Bounce Email                                           | `char`                  |     |       |                             |
| `bounce_formatted`                                   | Bounce                                                 | `char`                  |     |       |                             |
| `cash_account_code_prefix`                           | Prefix of the cash accounts                            | `char`                  |     | ✅    |                             |
| `catchall_email`                                     | Catchall Email                                         | `char`                  |     |       |                             |
| `catchall_formatted`                                 | Catchall                                               | `char`                  |     |       |                             |
| `chart_template`                                     | Chart Template                                         | `selection`             |     | ✅    |                             |
| `child_company_count`                                | Child Company Count                                    | `integer`               |     |       |                             |
| `child_ids`                                          | Branches                                               | `one2many`              |     | ✅    | res.company                 |
| `city`                                               | City                                                   | `char`                  |     |       |                             |
| `color`                                              | Color Index                                            | `integer`               |     |       |                             |
| `company_batch_count`                                | Company Batch Count                                    | `integer`               |     |       |                             |
| `company_course_count`                               | Company Course Count                                   | `integer`               |     |       |                             |
| `company_details`                                    | Company Details                                        | `html`                  |     | ✅    |                             |
| `company_expense_allowed_payment_method_line_ids`    | Payment methods available for expenses paid by company | `many2many`             |     | ✅    | account.payment.method.line |
| `company_registry`                                   | Company ID                                             | `char`                  |     |       |                             |
| `company_registry_placeholder`                       | Company Registry Placeholder                           | `char`                  |     |       |                             |
| `company_student_count`                              | Company Student Count                                  | `integer`               |     |       |                             |
| `company_subject_count`                              | Company Subject Count                                  | `integer`               |     |       |                             |
| `company_vat_placeholder`                            | Company Vat Placeholder                                | `char`                  |     |       |                             |
| `contract_expiration_notice_period`                  | Contract Expiry Notice Period                          | `integer`               |     | ✅    |                             |
| `cost_method`                                        | Cost Method                                            | `selection`             | ✅  | ✅    |                             |
| `country_code`                                       | Country Code                                           | `char`                  |     |       |                             |
| `country_id`                                         | Country                                                | `many2one`              |     |       | res.country                 |
| `create_date`                                        | Created on                                             | `datetime`              |     | ✅    |                             |
| `create_uid`                                         | Created by                                             | `many2one`              |     | ✅    | res.users                   |
| `currency_exchange_journal_id`                       | Exchange Gain or Loss Journal                          | `many2one`              |     | ✅    | account.journal             |
| `currency_id`                                        | Currency                                               | `many2one`              | ✅  | ✅    | res.currency                |
| `custom_bg_image`                                    | Custom Background Image                                | `binary`                |     | ✅    |                             |
| `dashboard_background`                               | Dashboard Background                                   | `binary`                |     | ✅    |                             |
| `days_to_purchase`                                   | Days to Purchase                                       | `float`                 |     | ✅    |                             |
| `default_cash_difference_expense_account_id`         | Cash Difference Expense                                | `many2one`              |     | ✅    | account.account             |
| `default_cash_difference_income_account_id`          | Cash Difference Income                                 | `many2one`              |     | ✅    | account.account             |
| `default_from_email`                                 | Default From                                           | `char`                  |     |       |                             |
| `display_account_storno`                             | Display Account Storno                                 | `boolean`               |     |       |                             |
| `display_invoice_amount_total_words`                 | Total amount of invoice in letters                     | `boolean`               |     | ✅    |                             |
| `display_invoice_tax_company_currency`               | Taxes in company currency                              | `boolean`               |     | ✅    |                             |
| `display_name`                                       | Display Name                                           | `char`                  |     |       |                             |
| `domestic_fiscal_position_id`                        | Domestic Fiscal Position                               | `many2one`              |     | ✅    | account.fiscal.position     |
| `downpayment_account_id`                             | Downpayment Account                                    | `many2one`              |     | ✅    | account.account             |
| `email`                                              | Email                                                  | `char`                  |     | ✅    |                             |
| `email_formatted`                                    | Formatted Email                                        | `char`                  |     |       |                             |
| `email_primary_color`                                | Email Button Text                                      | `char`                  |     | ✅    |                             |
| `email_secondary_color`                              | Email Button Color                                     | `char`                  |     | ✅    |                             |
| `employee_properties_definition`                     | Employee Properties                                    | `properties_definition` |     | ✅    |                             |
| `error_tolerance_threshold`                          | Error Tolerance                                        | `float`                 |     | ✅    |                             |
| `expects_chart_of_accounts`                          | Expects a Chart of Accounts                            | `boolean`               |     | ✅    |                             |
| `expense_account_id`                                 | Expense Account                                        | `many2one`              |     | ✅    | account.account             |
| `expense_accrual_account_id`                         | Expense Accrual Account                                | `many2one`              |     | ✅    | account.account             |
| `expense_currency_exchange_account_id`               | Loss Exchange Rate Account                             | `many2one`              |     | ✅    | account.account             |
| `expense_journal_id`                                 | Default Expense Journal                                | `many2one`              |     | ✅    | account.journal             |
| `external_report_layout_id`                          | Document Template                                      | `many2one`              |     | ✅    | ir.ui.view                  |
| `fiscal_position_ids`                                | Fiscal Position                                        | `one2many`              |     | ✅    | account.fiscal.position     |
| `fiscalyear_last_day`                                | Fiscalyear Last Day                                    | `integer`               | ✅  | ✅    |                             |
| `fiscalyear_last_month`                              | Fiscalyear Last Month                                  | `selection`             | ✅  | ✅    |                             |
| `fiscalyear_lock_date`                               | Global Lock Date                                       | `date`                  |     | ✅    |                             |
| `font`                                               | Font                                                   | `selection`             |     | ✅    |                             |
| `force_restrictive_audit_trail`                      | Force Audit Trail                                      | `boolean`               |     |       |                             |
| `google_font`                                        | Google Font                                            | `char`                  |     | ✅    |                             |
| `hard_lock_date`                                     | Hard Lock Date                                         | `date`                  |     | ✅    |                             |
| `has_message`                                        | Has Message                                            | `boolean`               |     |       |                             |
| `has_received_warning_stock_sms`                     | Has Received Warning Stock Sms                         | `boolean`               |     | ✅    |                             |
| `horizon_days`                                       | Replenishment Horizon                                  | `float`                 | ✅  | ✅    |                             |
| `hr_presence_control_attendance`                     | Based on attendances                                   | `boolean`               |     | ✅    |                             |
| `hr_presence_control_email`                          | Based on number of emails sent                         | `boolean`               |     | ✅    |                             |
| `hr_presence_control_email_amount`                   | # emails to send                                       | `integer`               |     | ✅    |                             |
| `hr_presence_control_ip`                             | Based on IP Address                                    | `boolean`               |     | ✅    |                             |
| `hr_presence_control_ip_list`                        | Valid IP addresses                                     | `char`                  |     | ✅    |                             |
| `hr_presence_control_login`                          | Based on user status in system                         | `boolean`               |     | ✅    |                             |
| `iap_enrich_auto_done`                               | Enrich Done                                            | `boolean`               |     | ✅    |                             |
| `id`                                                 | ID                                                     | `integer`               |     | ✅    |                             |
| `income_account_id`                                  | Income Account                                         | `many2one`              |     | ✅    | account.account             |
| `income_currency_exchange_account_id`                | Gain Exchange Rate Account                             | `many2one`              |     | ✅    | account.account             |
| `incoterm_id`                                        | Default incoterm                                       | `many2one`              |     | ✅    | account.incoterms           |
| `internal_transit_location_id`                       | Internal Transit Location                              | `many2one`              |     | ✅    | stock.location              |
| `inventory_period`                                   | Inventory Period                                       | `selection`             | ✅  | ✅    |                             |
| `inventory_valuation`                                | Valuation                                              | `selection`             |     | ✅    |                             |
| `invoice_terms`                                      | Default Terms and Conditions                           | `html`                  |     | ✅    |                             |
| `invoice_terms_html`                                 | Default Terms and Conditions as a Web page             | `html`                  |     | ✅    |                             |
| `is_company_details_empty`                           | Is Company Details Empty                               | `boolean`               |     |       |                             |
| `is_hash_verified`                                   | Is Hash Verified                                       | `boolean`               |     | ✅    |                             |
| `is_mail_sent`                                       | Is Mail Sent                                           | `boolean`               |     | ✅    |                             |
| `job_properties_definition`                          | Job Properties                                         | `properties_definition` |     | ✅    |                             |
| `layout_background`                                  | Layout Background                                      | `selection`             | ✅  | ✅    |                             |
| `layout_background_image`                            | Background Image                                       | `binary`                |     | ✅    |                             |
| `link_qr_code`                                       | Display Link QR-code                                   | `boolean`               |     | ✅    |                             |
| `logo`                                               | Company Logo                                           | `binary`                |     |       |                             |
| `logo_web`                                           | Logo Web                                               | `binary`                |     | ✅    |                             |
| `meeting_enterprise_onboard_panel`                   | State of the meeting onboarding step                   | `selection`             |     | ✅    |                             |
| `menu_bg_image`                                      | Apps Menu Footer Image                                 | `binary`                |     | ✅    |                             |
| `message_attachment_count`                           | Attachment Count                                       | `integer`               |     |       |                             |
| `message_follower_ids`                               | Followers                                              | `one2many`              |     | ✅    | mail.followers              |
| `message_has_error`                                  | Message Delivery error                                 | `boolean`               |     |       |                             |
| `message_has_error_counter`                          | Number of errors                                       | `integer`               |     |       |                             |
| `message_has_sms_error`                              | SMS Delivery error                                     | `boolean`               |     |       |                             |
| `message_ids`                                        | Messages                                               | `one2many`              |     | ✅    | mail.message                |
| `message_is_follower`                                | Is Follower                                            | `boolean`               |     |       |                             |
| `message_needaction`                                 | Action Needed                                          | `boolean`               |     |       |                             |
| `message_needaction_counter`                         | Number of Actions                                      | `integer`               |     |       |                             |
| `message_partner_ids`                                | Followers (Partners)                                   | `many2many`             |     |       | res.partner                 |
| `multi_vat_foreign_country_ids`                      | Foreign VAT countries                                  | `many2many`             |     |       | res.country                 |
| `name`                                               | Company Name                                           | `char`                  | ✅  | ✅    |                             |
| `next_execution_timestamp`                           | Next Execution Time                                    | `datetime`              |     | ✅    |                             |
| `nomenclature_id`                                    | Nomenclature                                           | `many2one`              |     | ✅    | barcode.nomenclature        |
| `onboarding_meeting_layout_state`                    | State of the onboarding meeting layout step            | `selection`             |     | ✅    |                             |
| `openeducat_instance_hash_key`                       | OpenEducat Instance Hash Key                           | `char`                  |     | ✅    |                             |
| `openeducat_instance_hash_msg`                       | Instance Hash Key Message                              | `char`                  |     | ✅    |                             |
| `openeducat_instance_key`                            | OpenEducat Instance Key                                | `char`                  |     | ✅    |                             |
| `paperformat_id`                                     | Paper format                                           | `many2one`              |     | ✅    | report.paperformat          |
| `parent_company_id`                                  | Company                                                | `many2one`              |     | ✅    | res.company                 |
| `parent_id`                                          | Parent Company                                         | `many2one`              |     | ✅    | res.company                 |
| `parent_ids`                                         | Parent                                                 | `many2many`             |     |       | res.company                 |
| `parent_path`                                        | Parent Path                                            | `char`                  |     | ✅    |                             |
| `partner_id`                                         | Partner                                                | `many2one`              | ✅  | ✅    | res.partner                 |
| `phone`                                              | Phone                                                  | `char`                  |     | ✅    |                             |
| `po_double_validation`                               | Levels of Approvals                                    | `selection`             |     | ✅    |                             |
| `po_double_validation_amount`                        | Double validation amount                               | `monetary`              |     | ✅    |                             |
| `po_lock`                                            | Purchase Order Modification                            | `selection`             |     | ✅    |                             |
| `portal_confirmation_pay`                            | Online Payment                                         | `boolean`               |     | ✅    |                             |
| `portal_confirmation_sign`                           | Online Signature                                       | `boolean`               |     | ✅    |                             |
| `preloader_option`                                   | Preloader Option                                       | `selection`             |     | ✅    |                             |
| `prepayment_percent`                                 | Prepayment percentage                                  | `float`                 |     | ✅    |                             |
| `price_difference_account_id`                        | Price Difference Account                               | `many2one`              |     | ✅    | account.account             |
| `primary_color`                                      | Primary Color                                          | `char`                  |     | ✅    |                             |
| `purchase_lock_date`                                 | Purchase Lock date                                     | `date`                  |     | ✅    |                             |
| `qr_code`                                            | Display QR-code on invoices                            | `boolean`               |     | ✅    |                             |
| `quick_edit_mode`                                    | Quick encoding                                         | `selection`             |     | ✅    |                             |
| `quotation_validity_days`                            | Default Quotation Validity                             | `integer`               |     | ✅    |                             |
| `rate_provider_selection`                            | Exchange Rate Provider                                 | `selection`             |     | ✅    |                             |
| `rating_ids`                                         | Ratings                                                | `one2many`              |     | ✅    | rating.rating               |
| `report_footer`                                      | Report Footer                                          | `html`                  |     | ✅    |                             |
| `report_header`                                      | Company Tagline                                        | `html`                  |     | ✅    |                             |
| `resource_calendar_id`                               | Default Working Hours                                  | `many2one`              |     | ✅    | resource.calendar           |
| `resource_calendar_ids`                              | Working Hours                                          | `one2many`              |     | ✅    | resource.calendar           |
| `restrictive_audit_trail`                            | Restrictive Audit Trail                                | `boolean`               |     | ✅    |                             |
| `revenue_accrual_account_id`                         | Revenue Accrual Account                                | `many2one`              |     | ✅    | account.account             |
| `root_id`                                            | Root                                                   | `many2one`              |     |       | res.company                 |
| `sale_discount_product_id`                           | Discount Product                                       | `many2one`              |     | ✅    | product.product             |
| `sale_lock_date`                                     | Sales Lock Date                                        | `date`                  |     | ✅    |                             |
| `sale_onboarding_payment_method`                     | Sale onboarding selected payment method                | `selection`             |     | ✅    |                             |
| `sale_order_template_id`                             | Default Sale Template                                  | `many2one`              |     | ✅    | sale.order.template         |
| `secondary_color`                                    | Secondary Color                                        | `char`                  |     | ✅    |                             |
| `security_lead`                                      | Sales Safety Days                                      | `float`                 | ✅  | ✅    |                             |
| `sequence`                                           | Sequence                                               | `integer`               |     | ✅    |                             |
| `sidebar_bg_image`                                   | Sidebar Background                                     | `binary`                |     | ✅    |                             |
| `sidebar_company_logo`                               | Sidebar Logo                                           | `binary`                |     | ✅    |                             |
| `signature`                                          | Signature                                              | `binary`                |     | ✅    |                             |
| `snailmail_color`                                    | Snailmail Color                                        | `boolean`               |     | ✅    |                             |
| `snailmail_cover`                                    | Add a Cover Page                                       | `boolean`               |     | ✅    |                             |
| `snailmail_duplex`                                   | Both sides                                             | `boolean`               |     | ✅    |                             |
| `social_discord`                                     | Discord Account                                        | `char`                  |     | ✅    |                             |
| `social_facebook`                                    | Facebook Account                                       | `char`                  |     | ✅    |                             |
| `social_github`                                      | GitHub Account                                         | `char`                  |     | ✅    |                             |
| `social_instagram`                                   | Instagram Account                                      | `char`                  |     | ✅    |                             |
| `social_linkedin`                                    | LinkedIn Account                                       | `char`                  |     | ✅    |                             |
| `social_tiktok`                                      | TikTok Account                                         | `char`                  |     | ✅    |                             |
| `social_twitter`                                     | X Account                                              | `char`                  |     | ✅    |                             |
| `social_youtube`                                     | Youtube Account                                        | `char`                  |     | ✅    |                             |
| `state_id`                                           | Fed. State                                             | `many2one`              |     |       | res.country.state           |
| `stock_confirmation_type`                            | Stock Confirmation Type                                | `selection`             |     | ✅    |                             |
| `stock_mail_confirmation_template_id`                | Email Template confirmation picking                    | `many2one`              |     | ✅    | mail.template               |
| `stock_move_email_validation`                        | Email Confirmation picking                             | `boolean`               |     | ✅    |                             |
| `stock_sms_confirmation_template_id`                 | SMS Template                                           | `many2one`              |     | ✅    | sms.template                |
| `stock_text_confirmation`                            | Stock Text Confirmation                                | `boolean`               |     | ✅    |                             |
| `street`                                             | Street                                                 | `char`                  |     |       |                             |
| `street2`                                            | Street2                                                | `char`                  |     |       |                             |
| `synchronization_batch_size`                         | Batch Size                                             | `integer`               |     | ✅    |                             |
| `synchronization_frequency`                          | Synchronization Frequency                              | `selection`             |     | ✅    |                             |
| `tax_calculation_rounding_method`                    | Tax Calculation Rounding Method                        | `selection`             |     | ✅    |                             |
| `tax_cash_basis_journal_id`                          | Cash Basis Journal                                     | `many2one`              |     | ✅    | account.journal             |
| `tax_exigibility`                                    | Use Cash Basis                                         | `boolean`               |     | ✅    |                             |
| `tax_lock_date`                                      | Tax Return Lock Date                                   | `date`                  |     | ✅    |                             |
| `terms_type`                                         | Terms & Conditions format                              | `selection`             |     | ✅    |                             |
| `theme_background_color`                             | Theme Background Color                                 | `char`                  |     | ✅    |                             |
| `theme_color_brand`                                  | Theme Brand Color                                      | `char`                  |     | ✅    |                             |
| `theme_font_name`                                    | Select Font                                            | `selection`             |     | ✅    |                             |
| `theme_menu_style`                                   | Menu Style                                             | `selection`             |     | ✅    |                             |
| `theme_sidebar_color`                                | Theme Sidebar Color                                    | `char`                  |     | ✅    |                             |
| `theme_sidebar_text_color`                           | Sidebar Text Color                                     | `char`                  |     | ✅    |                             |
| `transfer_account_code_prefix`                       | Prefix of the transfer accounts                        | `char`                  |     | ✅    |                             |
| `transfer_account_id`                                | Inter-Banks Transfer Account                           | `many2one`              |     | ✅    | account.account             |
| `uninstalled_l10n_module_ids`                        | Uninstalled L10N Module                                | `many2many`             |     |       | ir.module.module            |
| `user_fiscalyear_lock_date`                          | User Fiscalyear Lock Date                              | `date`                  |     |       |                             |
| `user_hard_lock_date`                                | User Hard Lock Date                                    | `date`                  |     |       |                             |
| `user_ids`                                           | Accepted Users                                         | `many2many`             |     | ✅    | res.users                   |
| `user_purchase_lock_date`                            | User Purchase Lock Date                                | `date`                  |     |       |                             |
| `user_sale_lock_date`                                | User Sale Lock Date                                    | `date`                  |     |       |                             |
| `user_tax_lock_date`                                 | User Tax Lock Date                                     | `date`                  |     |       |                             |
| `uses_default_logo`                                  | Uses Default Logo                                      | `boolean`               |     | ✅    |                             |
| `vat`                                                | Tax ID                                                 | `char`                  |     |       |                             |
| `verify_date`                                        | Verify Date                                            | `char`                  |     | ✅    |                             |
| `website`                                            | Website Link                                           | `char`                  |     |       |                             |
| `website_id`                                         | Website                                                | `many2one`              |     | ✅    | website                     |
| `website_message_ids`                                | Website Messages                                       | `one2many`              |     | ✅    | mail.message                |
| `work_permit_expiration_notice_period`               | Work Permit Expiry Notice Period                       | `integer`               |     | ✅    |                             |
| `write_date`                                         | Last Updated on                                        | `datetime`              |     | ✅    |                             |
| `write_uid`                                          | Last Updated by                                        | `many2one`              |     | ✅    | res.users                   |
| `zip`                                                | Zip                                                    | `char`                  |     |       |                             |

**Access Rights:**

| Name                          | Group         | Perms     |
| ----------------------------- | ------------- | --------- |
| res_company group_erp_manager | Access Rights | `R/W/C/D` |
| res_company group_user        | Role / Portal | `R`       |
| res_company group_user        | Role / Public | `R`       |
| res_company group_user        | Role / User   | `R`       |

**Record Rules:**

- **company rule portal** (10) `R/W/C/D`
  - Domain: `[('id','in', company_ids)]`
- **company rule employee** (1) `R/W/C/D`
  - Domain: `[('id','in', company_ids)]`
- **company rule public** (11) `R/W/C/D`
  - Domain: `[('id','in', company_ids)]`
- **company rule erp manager** (2) `R/W/C/D`
  - Domain: `[(1,'=',1)]`

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

### 🗃️ `digest.digest` — Digest

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                     | Label                                   | Type        | Req | Store | Relation     |
| ----------------------------------------- | --------------------------------------- | ----------- | --- | ----- | ------------ |
| `available_fields`                        | Available Fields                        | `char`      |     |       |              |
| `company_id`                              | Company                                 | `many2one`  |     | ✅    | res.company  |
| `create_date`                             | Created on                              | `datetime`  |     | ✅    |              |
| `create_uid`                              | Created by                              | `many2one`  |     | ✅    | res.users    |
| `currency_id`                             | Currency                                | `many2one`  |     |       | res.currency |
| `display_name`                            | Display Name                            | `char`      |     |       |              |
| `id`                                      | ID                                      | `integer`   |     | ✅    |              |
| `is_subscribed`                           | Is user subscribed                      | `boolean`   |     |       |              |
| `kpi_account_total_revenue`               | Revenue                                 | `boolean`   |     | ✅    |              |
| `kpi_account_total_revenue_value`         | Kpi Account Total Revenue Value         | `monetary`  |     |       |              |
| `kpi_all_sale_total`                      | All Sales                               | `boolean`   |     | ✅    |              |
| `kpi_all_sale_total_value`                | Kpi All Sale Total Value                | `monetary`  |     |       |              |
| `kpi_crm_lead_created`                    | New Leads                               | `boolean`   |     | ✅    |              |
| `kpi_crm_lead_created_value`              | Kpi Crm Lead Created Value              | `integer`   |     |       |              |
| `kpi_crm_opportunities_won`               | Opportunities Won                       | `boolean`   |     | ✅    |              |
| `kpi_crm_opportunities_won_value`         | Kpi Crm Opportunities Won Value         | `integer`   |     |       |              |
| `kpi_hr_recruitment_new_colleagues`       | New Employees                           | `boolean`   |     | ✅    |              |
| `kpi_hr_recruitment_new_colleagues_value` | Kpi Hr Recruitment New Colleagues Value | `integer`   |     |       |              |
| `kpi_livechat_conversations`              | Conversations handled                   | `boolean`   |     | ✅    |              |
| `kpi_livechat_conversations_value`        | Kpi Livechat Conversations Value        | `integer`   |     |       |              |
| `kpi_livechat_rating`                     | % of Happiness                          | `boolean`   |     | ✅    |              |
| `kpi_livechat_rating_value`               | Kpi Livechat Rating Value               | `float`     |     |       |              |
| `kpi_livechat_response`                   | Time to answer (sec)                    | `boolean`   |     | ✅    |              |
| `kpi_livechat_response_value`             | Kpi Livechat Response Value             | `float`     |     |       |              |
| `kpi_mail_message_total`                  | Messages Sent                           | `boolean`   |     | ✅    |              |
| `kpi_mail_message_total_value`            | Kpi Mail Message Total Value            | `integer`   |     |       |              |
| `kpi_res_users_connected`                 | Connected Users                         | `boolean`   |     | ✅    |              |
| `kpi_res_users_connected_value`           | Kpi Res Users Connected Value           | `integer`   |     |       |              |
| `kpi_website_sale_total`                  | eCommerce Sales                         | `boolean`   |     | ✅    |              |
| `kpi_website_sale_total_value`            | Kpi Website Sale Total Value            | `monetary`  |     |       |              |
| `name`                                    | Name                                    | `char`      | ✅  | ✅    |              |
| `next_run_date`                           | Next Mailing Date                       | `date`      |     | ✅    |              |
| `periodicity`                             | Periodicity                             | `selection` | ✅  | ✅    |              |
| `state`                                   | Status                                  | `selection` |     | ✅    |              |
| `user_ids`                                | Recipients                              | `many2many` |     | ✅    | res.users    |
| `write_date`                              | Last Updated on                         | `datetime`  |     | ✅    |              |
| `write_uid`                               | Last Updated by                         | `many2one`  |     | ✅    | res.users    |

**Access Rights:**

| Name                         | Group         | Perms     |
| ---------------------------- | ------------- | --------- |
| digest.digest.administration | Access Rights | `R/W/C/D` |
| digest.digest.user           | Role / User   | `R`       |

### 🗃️ `sale.order.template` — Quotation Template

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                          | Label                 | Type        | Req | Store | Relation                 |
| ------------------------------ | --------------------- | ----------- | --- | ----- | ------------------------ |
| `active`                       | Active                | `boolean`   |     | ✅    |                          |
| `company_id`                   | Company               | `many2one`  |     | ✅    | res.company              |
| `create_date`                  | Created on            | `datetime`  |     | ✅    |                          |
| `create_uid`                   | Created by            | `many2one`  |     | ✅    | res.users                |
| `display_name`                 | Display Name          | `char`      |     |       |                          |
| `id`                           | ID                    | `integer`   |     | ✅    |                          |
| `journal_id`                   | Invoicing Journal     | `many2one`  |     | ✅    | account.journal          |
| `mail_template_id`             | Confirmation Mail     | `many2one`  |     | ✅    | mail.template            |
| `name`                         | Quotation Template    | `char`      | ✅  | ✅    |                          |
| `note`                         | Terms and conditions  | `html`      |     | ✅    |                          |
| `number_of_days`               | Quotation Duration    | `integer`   |     | ✅    |                          |
| `prepayment_percent`           | Prepayment percentage | `float`     |     | ✅    |                          |
| `quotation_document_ids`       | Headers and footers   | `many2many` |     | ✅    | quotation.document       |
| `require_payment`              | Online Payment        | `boolean`   |     | ✅    |                          |
| `require_signature`            | Online Signature      | `boolean`   |     | ✅    |                          |
| `sale_order_template_line_ids` | Lines                 | `one2many`  |     | ✅    | sale.order.template.line |
| `sequence`                     | Sequence              | `integer`   |     | ✅    |                          |
| `write_date`                   | Last Updated on       | `datetime`  |     | ✅    |                          |
| `write_uid`                    | Last Updated by       | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                | Group                            | Perms     |
| ------------------- | -------------------------------- | --------- |
| sale.order.template | Sales / User: Own Documents Only | `R`       |
| sale.order.template | Sales / Administrator            | `R/W/C/D` |
| sale.order.template | Role / Administrator             | `R`       |

**Record Rules:**

- **Quotation Template multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `sale.order.template.line` — Quotation Template Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                    | Label                        | Type        | Req | Store | Relation                 |
| ------------------------ | ---------------------------- | ----------- | --- | ----- | ------------------------ |
| `allowed_uom_ids`        | Allowed Uom                  | `many2many` |     |       | uom.uom                  |
| `company_id`             | Company                      | `many2one`  |     | ✅    | res.company              |
| `create_date`            | Created on                   | `datetime`  |     | ✅    |                          |
| `create_uid`             | Created by                   | `many2one`  |     | ✅    | res.users                |
| `display_name`           | Display Name                 | `char`      |     |       |                          |
| `display_type`           | Display Type                 | `selection` |     | ✅    |                          |
| `id`                     | ID                           | `integer`   |     | ✅    |                          |
| `is_optional`            | Optional Line                | `boolean`   |     | ✅    |                          |
| `name`                   | Description                  | `text`      |     | ✅    |                          |
| `parent_id`              | Parent Section Line          | `many2one`  |     |       | sale.order.template.line |
| `product_id`             | Product                      | `many2one`  |     | ✅    | product.product          |
| `product_uom_id`         | Unit                         | `many2one`  |     | ✅    | uom.uom                  |
| `product_uom_qty`        | Quantity                     | `float`     | ✅  | ✅    |                          |
| `sale_order_template_id` | Quotation Template Reference | `many2one`  | ✅  | ✅    | sale.order.template      |
| `sequence`               | Sequence                     | `integer`   |     | ✅    |                          |
| `write_date`             | Last Updated on              | `datetime`  |     | ✅    |                          |
| `write_uid`              | Last Updated by              | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                     | Group                            | Perms     |
| ------------------------ | -------------------------------- | --------- |
| sale.order.template.line | Sales / User: Own Documents Only | `R`       |
| sale.order.template.line | Sales / Administrator            | `R/W/C/D` |

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
