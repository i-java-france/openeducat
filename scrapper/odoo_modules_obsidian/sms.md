---
title: "SMS gateway"
module: "sms"
state: "installed"
version: "19.0.3.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Sales"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_____]
---

# 🟢 SMS gateway

> **Module:** `sms` | **Version:** `19.0.3.0` **Category:** Sales | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[base]] [[iap_mail]] [[mail]] [[phone_validation]]

## 📖 Description

# This module gives a framework for SMS text messaging

The service is provided by the In App Purchase Odoo platform.

## 🖥️ UI Components

### Menus

- `Settings/Technical/Phone / SMS/SMS`
- `Settings/Technical/Phone / SMS/SMS Templates`

### Views

- `* INHERIT iap.account.view.form (form)`
- `* INHERIT ir.actions.server.view.form.inherit.sms (form)`
- `* INHERIT mail.notification.view.form (form)`
- `* INHERIT mail.notification.view.list (list)`
- `* INHERIT res.config.settings.view.form.inherit.sms (form)`
- `* INHERIT res.partner.view.form.inherit.sms (form)`
- `sms.account.code.view.form (form)`
- `sms.account.phone.view.form (form)`
- `sms.account.sender.view.form (form)`
- `sms.composer.view.form (form)`
- `sms.sms.view.form (form)`
- `sms.sms.view.list (list)`
- `sms.sms.view.search (search)`
- `sms.template.preview.form (form)`
- `sms.template.reset.view.form (form)`
- `sms.template.view.form (form)`
- `sms.template.view.list (list)`
- `sms.template.view.search (search)`

### Reports

_none_

## 🛠️ Technical Documentation

**18 model(s) defined by this module:**

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

### 🗃️ `mail.thread` — Email Thread

> 📧 Mail Thread

Update MailThread to add the support of bounce management in mass mailing traces.

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |

### 🗃️ `iap.account` — IAP Account

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `account_token`              | Account Token          | `char`      |     | ✅    |                |
| `balance`                    | Balance                | `char`      |     | ✅    |                |
| `company_ids`                | Company                | `many2many` |     | ✅    | res.company    |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users      |
| `description`                | Description            | `char`      |     |       |                |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `name`                       | Name                   | `char`      |     | ✅    |                |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `sender_name`                | Sender Name            | `char`      |     | ✅    |                |
| `service_id`                 | Service                | `many2one`  | ✅  | ✅    | iap.service    |
| `service_locked`             | Service Locked         | `boolean`   |     | ✅    |                |
| `service_name`               | Technical Name         | `char`      |     |       |                |
| `state`                      | State                  | `selection` |     | ✅    |                |
| `warning_threshold`          | Email Alert Threshold  | `float`     |     | ✅    |                |
| `warning_user_ids`           | Email Alert Recipients | `many2many` |     | ✅    | res.users      |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                | Group                | Perms     |
| ------------------- | -------------------- | --------- |
| iap.account.manager | Role / Administrator | `R/W/C/D` |
| iap.account.user    | Role / User          | `R/C`     |

**Record Rules:**

- **User IAP Account** (1) `R/W/C/D`
  - Domain: `['|', ('company_ids', '=', False), ('company_ids', 'in', company_ids)]`

### 🗃️ `ir.actions.server` — Server Action

> 📧 Mail Thread

Add website option in server actions.

**Fields:**

| Field                               | Label                         | Type        | Req | Store | Relation                  |
| ----------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------- |
| `action_class`                      | Action Class                  | `char`      |     | ✅    |                           |
| `activity_calendar_event_id`        | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event            |
| `activity_date_deadline`            | Next Activity Deadline        | `date`      |     |       |                           |
| `activity_date_deadline_range`      | Due Date In                   | `integer`   |     | ✅    |                           |
| `activity_date_deadline_range_type` | Due type                      | `selection` |     | ✅    |                           |
| `activity_exception_decoration`     | Activity Exception Decoration | `selection` |     |       |                           |
| `activity_exception_icon`           | Icon                          | `char`      |     |       |                           |
| `activity_ids`                      | Activities                    | `one2many`  |     | ✅    | mail.activity             |
| `activity_note`                     | Note                          | `html`      |     | ✅    |                           |
| `activity_state`                    | Activity State                | `selection` |     |       |                           |
| `activity_summary`                  | Title                         | `char`      |     | ✅    |                           |
| `activity_type_icon`                | Activity Type Icon            | `char`      |     |       |                           |
| `activity_type_id`                  | Activity Type                 | `many2one`  |     | ✅    | mail.activity.type        |
| `activity_user_field_name`          | User Field                    | `char`      |     | ✅    |                           |
| `activity_user_id`                  | Responsible                   | `many2one`  |     | ✅    | res.users                 |
| `activity_user_type`                | User Type                     | `selection` |     | ✅    |                           |
| `allowed_states`                    | Allowed states                | `json`      |     |       |                           |
| `automated_name`                    | Automated Name                | `char`      |     | ✅    |                           |
| `available_model_ids`               | Available Models              | `many2many` |     |       | ir.model                  |
| `base_automation_id`                | Automation Rule               | `many2one`  |     | ✅    | base.automation           |
| `binding_model_id`                  | Binding Model                 | `many2one`  |     | ✅    | ir.model                  |
| `binding_type`                      | Binding Type                  | `selection` | ✅  | ✅    |                           |
| `binding_view_types`                | Binding View Types            | `char`      |     | ✅    |                           |
| `child_ids`                         | Child Actions                 | `one2many`  |     | ✅    | ir.actions.server         |
| `code`                              | Python Code                   | `text`      |     | ✅    |                           |
| `create_date`                       | Created on                    | `datetime`  |     | ✅    |                           |
| `create_uid`                        | Created by                    | `many2one`  |     | ✅    | res.users                 |
| `crud_model_id`                     | Record to Create              | `many2one`  |     | ✅    | ir.model                  |
| `crud_model_name`                   | Target Model Name             | `char`      |     |       |                           |
| `display_name`                      | Display Name                  | `char`      |     |       |                           |
| `evaluation_type`                   | Value Type                    | `selection` |     | ✅    |                           |
| `followers_partner_field_name`      | Followers Field               | `char`      |     | ✅    |                           |
| `followers_type`                    | Followers Type                | `selection` |     | ✅    |                           |
| `group_ids`                         | Allowed Groups                | `many2many` |     | ✅    | res.groups                |
| `has_message`                       | Has Message                   | `boolean`   |     |       |                           |
| `help`                              | Action Description            | `html`      |     | ✅    |                           |
| `html_value`                        | Html Value                    | `html`      |     | ✅    |                           |
| `icon`                              | Icon                          | `char`      |     | ✅    |                           |
| `id`                                | ID                            | `integer`   |     | ✅    |                           |
| `ir_cron_ids`                       | Scheduled Action              | `one2many`  |     | ✅    | ir.cron                   |
| `link_field_id`                     | Link Field                    | `many2one`  |     | ✅    | ir.model.fields           |
| `mail_post_autofollow`              | Subscribe Recipients          | `boolean`   |     | ✅    |                           |
| `mail_post_method`                  | Send Email As                 | `selection` |     | ✅    |                           |
| `message_attachment_count`          | Attachment Count              | `integer`   |     |       |                           |
| `message_follower_ids`              | Followers                     | `one2many`  |     | ✅    | mail.followers            |
| `message_has_error`                 | Message Delivery error        | `boolean`   |     |       |                           |
| `message_has_error_counter`         | Number of errors              | `integer`   |     |       |                           |
| `message_has_sms_error`             | SMS Delivery error            | `boolean`   |     |       |                           |
| `message_ids`                       | Messages                      | `one2many`  |     | ✅    | mail.message              |
| `message_is_follower`               | Is Follower                   | `boolean`   |     |       |                           |
| `message_needaction`                | Action Needed                 | `boolean`   |     |       |                           |
| `message_needaction_counter`        | Number of Actions             | `integer`   |     |       |                           |
| `message_partner_ids`               | Followers (Partners)          | `many2many` |     |       | res.partner               |
| `model_id`                          | Model                         | `many2one`  | ✅  | ✅    | ir.model                  |
| `model_name`                        | Model Name                    | `char`      |     |       |                           |
| `my_activity_date_deadline`         | My Activity Deadline          | `date`      |     |       |                           |
| `name`                              | Action Name                   | `char`      | ✅  | ✅    |                           |
| `parent_id`                         | Parent Action                 | `many2one`  |     | ✅    | ir.actions.server         |
| `partner_ids`                       | Partner                       | `many2many` |     | ✅    | res.partner               |
| `path`                              | Path to show in the URL       | `char`      |     | ✅    |                           |
| `rating_ids`                        | Ratings                       | `one2many`  |     | ✅    | rating.rating             |
| `resource_ref`                      | Record                        | `reference` |     | ✅    |                           |
| `selection_value`                   | Custom Value                  | `many2one`  |     | ✅    | ir.model.fields.selection |
| `sequence`                          | Sequence                      | `integer`   |     | ✅    |                           |
| `sequence_id`                       | Sequence to use               | `many2one`  |     | ✅    | ir.sequence               |
| `show_code_history`                 | Show Code History             | `boolean`   |     |       |                           |
| `sms_method`                        | Send SMS As                   | `selection` |     | ✅    |                           |
| `sms_template_id`                   | SMS Template                  | `many2one`  |     | ✅    | sms.template              |
| `state`                             | Type                          | `selection` | ✅  | ✅    |                           |
| `template_id`                       | Email Template                | `many2one`  |     | ✅    | mail.template             |
| `type`                              | Action Type                   | `char`      | ✅  | ✅    |                           |
| `update_boolean_value`              | Boolean Value                 | `selection` |     | ✅    |                           |
| `update_field_id`                   | Field to Update               | `many2one`  |     | ✅    | ir.model.fields           |
| `update_field_type`                 | Field Type                    | `selection` |     |       |                           |
| `update_m2m_operation`              | Many2many Operations          | `selection` |     | ✅    |                           |
| `update_path`                       | Field to Update Path          | `char`      |     | ✅    |                           |
| `update_related_model_id`           | Update Related Model          | `many2one`  |     | ✅    | ir.model                  |
| `usage`                             | Usage                         | `selection` | ✅  | ✅    |                           |
| `value`                             | Value                         | `text`      |     | ✅    |                           |
| `value_field_to_show`               | Value Field To Show           | `selection` |     |       |                           |
| `warning`                           | Warning                       | `text`      |     |       |                           |
| `webhook_field_ids`                 | Webhook Fields                | `many2many` |     | ✅    | ir.model.fields           |
| `webhook_sample_payload`            | Sample Payload                | `text`      |     |       |                           |
| `webhook_url`                       | Webhook URL                   | `char`      |     | ✅    |                           |
| `website_message_ids`               | Website Messages              | `one2many`  |     | ✅    | mail.message              |
| `website_path`                      | Website Path                  | `char`      |     | ✅    |                           |
| `website_published`                 | Available on the Website      | `boolean`   |     | ✅    |                           |
| `website_url`                       | Website Url                   | `char`      |     |       |                           |
| `write_date`                        | Last Updated on               | `datetime`  |     | ✅    |                           |
| `write_uid`                         | Last Updated by               | `many2one`  |     | ✅    | res.users                 |
| `xml_id`                            | External ID                   | `char`      |     |       |                           |

**Access Rights:**

| Name                           | Group                | Perms     |
| ------------------------------ | -------------------- | --------- |
| ir_actions_server_group_system | Role / Administrator | `R/W/C/D` |

### 🗃️ `base` — Base

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `mail.followers` — Document Followers

mail_followers holds the data related to the follow mechanism inside Odoo. Partners can
choose to follow documents (records) of any kind that inherits from mail.thread.
Following documents allow to receive notifications for new messages. A subscription is
characterized by:

    :param: res_model: model of the followed objects
    :param: res_id: ID of resource (may be 0 for every objects)

**Fields:**

| Field          | Label                       | Type                 | Req | Store | Relation             |
| -------------- | --------------------------- | -------------------- | --- | ----- | -------------------- |
| `display_name` | Display Name                | `char`               |     |       |                      |
| `email`        | Email                       | `char`               |     |       |                      |
| `id`           | ID                          | `integer`            |     | ✅    |                      |
| `is_active`    | Is Active                   | `boolean`            |     |       |                      |
| `name`         | Name                        | `char`               |     |       |                      |
| `partner_id`   | Related Partner             | `many2one`           | ✅  | ✅    | res.partner          |
| `res_id`       | Related Document ID         | `many2one_reference` |     | ✅    |                      |
| `res_model`    | Related Document Model Name | `char`               | ✅  | ✅    |                      |
| `subtype_ids`  | Subtype                     | `many2many`          |     | ✅    | mail.message.subtype |

**Access Rights:**

| Name                  | Group                | Perms     |
| --------------------- | -------------------- | --------- |
| mail.followers.system | Role / Administrator | `R/W/C/D` |
| mail.followers.user   | Role / User          | `R`       |

### 🗃️ `sms.tracker` — Link SMS to mailing/sms tracking models

Relationship between a sent SMS and tracking records such as notifications and traces.

    This model acts as an extension of a `mail.notification` or a `mailing.trace` and allows to
    update those based on the SMS provider responses both at sending and when later receiving
    sent/delivery reports (see `SmsController`).
    SMS trackers are supposed to be created manually when necessary, and tied to their related
    SMS through the SMS UUID field. (They are not tied to the SMS records directly as those can
    be deleted when sent).

    Note: Only admins/system user should need to access (a fortiori modify) these technical
      records so no "sudo" is used nor should be required here.

**Fields:**

| Field                  | Label             | Type       | Req | Store | Relation          |
| ---------------------- | ----------------- | ---------- | --- | ----- | ----------------- |
| `create_date`          | Created on        | `datetime` |     | ✅    |                   |
| `create_uid`           | Created by        | `many2one` |     | ✅    | res.users         |
| `display_name`         | Display Name      | `char`     |     |       |                   |
| `id`                   | ID                | `integer`  |     | ✅    |                   |
| `mail_notification_id` | Mail Notification | `many2one` |     | ✅    | mail.notification |
| `sms_uuid`             | SMS uuid          | `char`     | ✅  | ✅    |                   |
| `write_date`           | Last Updated on   | `datetime` |     | ✅    |                   |
| `write_uid`            | Last Updated by   | `many2one` |     | ✅    | res.users         |

**Access Rights:**

| Name                      | Group                | Perms     |
| ------------------------- | -------------------- | --------- |
| access.sms.tracker.system | Role / Administrator | `R/W/C/D` |
| access.sms.tracker.all    | Everyone             | `-`       |

### 🗃️ `mail.message` — Message

Override MailMessage class in order to add a new type: SMS messages. Those messages
comes with their own notification method, using SMS gateway.

**Fields:**

| Field                             | Label                              | Type                 | Req | Store | Relation                  |
| --------------------------------- | ---------------------------------- | -------------------- | --- | ----- | ------------------------- |
| `account_audit_log_account_id`    | Account                            | `many2one`           |     |       | account.account           |
| `account_audit_log_company_id`    | Company                            | `many2one`           |     |       | res.company               |
| `account_audit_log_move_id`       | Journal Entry                      | `many2one`           |     |       | account.move              |
| `account_audit_log_partner_id`    | Partner                            | `many2one`           |     |       | res.partner               |
| `account_audit_log_preview`       | Description                        | `text`               |     |       |                           |
| `account_audit_log_restricted`    | Protected by restricted Audit Logs | `boolean`            |     |       |                           |
| `account_audit_log_tax_id`        | Tax                                | `many2one`           |     |       | account.tax               |
| `attachment_ids`                  | Attachments                        | `many2many`          |     | ✅    | ir.attachment             |
| `author_avatar`                   | Author's avatar                    | `binary`             |     |       |                           |
| `author_guest_id`                 | Guest                              | `many2one`           |     | ✅    | mail.guest                |
| `author_id`                       | Author                             | `many2one`           |     | ✅    | res.partner               |
| `body`                            | Contents                           | `html`               |     | ✅    |                           |
| `call_history_ids`                | Call History                       | `one2many`           |     | ✅    | discuss.call.history      |
| `channel_id`                      | Channel                            | `many2one`           |     |       | discuss.channel           |
| `child_ids`                       | Child Messages                     | `one2many`           |     | ✅    | mail.message              |
| `create_date`                     | Created on                         | `datetime`           |     | ✅    |                           |
| `create_uid`                      | Created by                         | `many2one`           |     | ✅    | res.users                 |
| `date`                            | Date                               | `datetime`           |     | ✅    |                           |
| `display_name`                    | Display Name                       | `char`               |     |       |                           |
| `email_add_signature`             | Email Add Signature                | `boolean`            |     | ✅    |                           |
| `email_from`                      | From                               | `char`               |     | ✅    |                           |
| `email_layout_xmlid`              | Layout                             | `char`               |     | ✅    |                           |
| `has_error`                       | Has error                          | `boolean`            |     |       |                           |
| `has_sms_error`                   | Has SMS error                      | `boolean`            |     |       |                           |
| `id`                              | ID                                 | `integer`            |     | ✅    |                           |
| `incoming_email_cc`               | Emails Cc                          | `char`               |     | ✅    |                           |
| `incoming_email_to`               | Emails To                          | `text`               |     | ✅    |                           |
| `is_current_user_or_guest_author` | Is Current User Or Guest Author    | `boolean`            |     |       |                           |
| `is_internal`                     | Employee Only                      | `boolean`            |     | ✅    |                           |
| `letter_ids`                      | Letter                             | `one2many`           |     | ✅    | snailmail.letter          |
| `linked_message_ids`              | Linked Message                     | `many2many`          |     |       | mail.message              |
| `mail_activity_type_id`           | Mail Activity Type                 | `many2one`           |     | ✅    | mail.activity.type        |
| `mail_ids`                        | Mails                              | `one2many`           |     | ✅    | mail.mail                 |
| `mail_server_id`                  | Outgoing mail server               | `many2one`           |     | ✅    | ir.mail_server            |
| `message_id`                      | Message-Id                         | `char`               |     | ✅    |                           |
| `message_link_preview_ids`        | Message Link Preview               | `one2many`           |     | ✅    | mail.message.link.preview |
| `message_type`                    | Type                               | `selection`          | ✅  | ✅    |                           |
| `model`                           | Related Document Model             | `char`               |     | ✅    |                           |
| `needaction`                      | Need Action                        | `boolean`            |     |       |                           |
| `notification_ids`                | Notifications                      | `one2many`           |     | ✅    | mail.notification         |
| `notified_partner_ids`            | Partners with Need Action          | `many2many`          |     | ✅    | res.partner               |
| `outgoing_email_to`               | emails To                          | `char`               |     | ✅    |                           |
| `parent_id`                       | Parent Message                     | `many2one`           |     | ✅    | mail.message              |
| `partner_ids`                     | Recipients                         | `many2many`          |     | ✅    | res.partner               |
| `pinned_at`                       | Pinned                             | `datetime`           |     | ✅    |                           |
| `preview`                         | Preview                            | `char`               |     |       |                           |
| `rating_id`                       | Rating                             | `many2one`           |     |       | rating.rating             |
| `rating_ids`                      | Related ratings                    | `one2many`           |     | ✅    | rating.rating             |
| `rating_value`                    | Rating Value                       | `float`              |     |       |                           |
| `reaction_ids`                    | Reactions                          | `one2many`           |     | ✅    | mail.message.reaction     |
| `record_alias_domain_id`          | Alias Domain                       | `many2one`           |     | ✅    | mail.alias.domain         |
| `record_company_id`               | Company                            | `many2one`           |     | ✅    | res.company               |
| `record_name`                     | Message Record Name                | `char`               |     |       |                           |
| `reply_to`                        | Reply-To                           | `char`               |     | ✅    |                           |
| `reply_to_force_new`              | No threading for answers           | `boolean`            |     | ✅    |                           |
| `res_id`                          | Related Document ID                | `many2one_reference` |     | ✅    |                           |
| `snailmail_error`                 | Snailmail message in error         | `boolean`            |     |       |                           |
| `starred`                         | Starred                            | `boolean`            |     |       |                           |
| `starred_partner_ids`             | Favorited By                       | `many2many`          |     | ✅    | res.partner               |
| `subject`                         | Subject                            | `char`               |     | ✅    |                           |
| `subtype_id`                      | Subtype                            | `many2one`           |     | ✅    | mail.message.subtype      |
| `tracking_value_ids`              | Tracking values                    | `one2many`           |     | ✅    | mail.tracking.value       |
| `write_date`                      | Last Updated on                    | `datetime`           |     | ✅    |                           |
| `write_uid`                       | Last Updated by                    | `many2one`           |     | ✅    | res.users                 |

**Access Rights:**

| Name                | Group         | Perms     |
| ------------------- | ------------- | --------- |
| mail.message.portal | Role / Portal | `R/W/C/D` |
| mail.message.all    | Role / Public | `R`       |
| mail.message.user   | Role / User   | `R/W/C/D` |

**Record Rules:**

- **User: All Chatter** (83) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `mail.notification` — Message Notifications

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                 | Label              | Type        | Req | Store | Relation         |
| --------------------- | ------------------ | ----------- | --- | ----- | ---------------- |
| `author_id`           | Author             | `many2one`  |     | ✅    | res.partner      |
| `display_name`        | Display Name       | `char`      |     |       |                  |
| `failure_reason`      | Failure reason     | `text`      |     | ✅    |                  |
| `failure_type`        | Failure type       | `selection` |     | ✅    |                  |
| `id`                  | ID                 | `integer`   |     | ✅    |                  |
| `is_read`             | Is Read            | `boolean`   |     | ✅    |                  |
| `letter_id`           | Snailmail Letter   | `many2one`  |     | ✅    | snailmail.letter |
| `mail_email_address`  | Mail Email Address | `char`      |     | ✅    |                  |
| `mail_mail_id`        | Mail               | `many2one`  |     | ✅    | mail.mail        |
| `mail_message_id`     | Message            | `many2one`  | ✅  | ✅    | mail.message     |
| `notification_status` | Status             | `selection` |     | ✅    |                  |
| `notification_type`   | Notification Type  | `selection` | ✅  | ✅    |                  |
| `read_date`           | Read Date          | `datetime`  |     | ✅    |                  |
| `res_partner_id`      | Recipient          | `many2one`  |     | ✅    | res.partner      |
| `sms_id`              | SMS                | `many2one`  |     |       | sms.sms          |
| `sms_id_int`          | SMS ID             | `integer`   |     | ✅    |                  |
| `sms_number`          | SMS Number         | `char`      |     | ✅    |                  |
| `sms_tracker_ids`     | SMS Trackers       | `one2many`  |     | ✅    | sms.tracker      |

**Access Rights:**

| Name                     | Group                | Perms     |
| ------------------------ | -------------------- | --------- |
| mail.notification.system | Role / Administrator | `R/W/C/D` |
| mail.notification.portal | Role / Portal        | `R`       |
| mail.notification.user   | Role / User          | `R/W/C`   |

**Record Rules:**

- **mail.notifications: group_user: write its own entries** (10, 1) `W`
  - Domain: `[('res_partner_id', '=', user.partner_id.id)]`
- **mail.notifications: group_portal: own entries** (10) `R/W/C/D`
  - Domain:
    `['|', ('res_partner_id', '=', user.partner_id.id), ('author_id', '=', user.partner_id.id)]`

### 🗃️ `ir.model` — Models

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                      | Type        | Req | Store | Relation        |
| ------------------------------- | -------------------------- | ----------- | --- | ----- | --------------- |
| `abstract`                      | Abstract Model             | `boolean`   |     | ✅    |                 |
| `access_ids`                    | Access                     | `one2many`  |     | ✅    | ir.model.access |
| `count`                         | Count (Incl. Archived)     | `integer`   |     |       |                 |
| `create_date`                   | Created on                 | `datetime`  |     | ✅    |                 |
| `create_uid`                    | Created by                 | `many2one`  |     | ✅    | res.users       |
| `display_name`                  | Display Name               | `char`      |     |       |                 |
| `field_id`                      | Fields                     | `one2many`  | ✅  | ✅    | ir.model.fields |
| `fold_name`                     | Fold Field                 | `char`      |     | ✅    |                 |
| `id`                            | ID                         | `integer`   |     | ✅    |                 |
| `info`                          | Information                | `text`      |     | ✅    |                 |
| `inherited_model_ids`           | Inherited models           | `many2many` |     |       | ir.model        |
| `is_mail_activity`              | Has Mail Activity          | `boolean`   |     | ✅    |                 |
| `is_mail_blacklist`             | Has Mail Blacklist         | `boolean`   |     | ✅    |                 |
| `is_mailing_enabled`            | Mailing Enabled            | `boolean`   |     |       |                 |
| `is_mail_thread`                | Has Mail Thread            | `boolean`   |     | ✅    |                 |
| `is_mail_thread_sms`            | Mail Thread SMS            | `boolean`   |     |       |                 |
| `is_phone_whatsapp`             | Whatsapp Contact           | `boolean`   |     |       |                 |
| `model`                         | Model                      | `char`      | ✅  | ✅    |                 |
| `modules`                       | In Apps                    | `char`      |     |       |                 |
| `name`                          | Model Description          | `char`      | ✅  | ✅    |                 |
| `order`                         | Order                      | `char`      | ✅  | ✅    |                 |
| `rule_ids`                      | Record Rules               | `one2many`  |     | ✅    | ir.rule         |
| `state`                         | Type                       | `selection` |     | ✅    |                 |
| `transient`                     | Transient Model            | `boolean`   |     | ✅    |                 |
| `view_ids`                      | Views                      | `one2many`  |     |       | ir.ui.view      |
| `website_form_access`           | Allowed to use in forms    | `boolean`   |     | ✅    |                 |
| `website_form_default_field_id` | Field for custom form data | `many2one`  |     | ✅    | ir.model.fields |
| `website_form_key`              | Website Form Key           | `char`      |     | ✅    |                 |
| `website_form_label`            | Label for form action      | `char`      |     | ✅    |                 |
| `write_date`                    | Last Updated on            | `datetime`  |     | ✅    |                 |
| `write_uid`                     | Last Updated by            | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                       | Group                  | Perms     |
| -------------------------- | ---------------------- | --------- |
| access_ir_model            | Email Marketing / User | `R`       |
| ir_model group_erp_manager | Access Rights          | `R/W/C/D` |
| ir_model_all               | Role / User            | `-`       |

### 🗃️ `sms.sms` — Outgoing SMS

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label               | Type        | Req | Store | Relation     |
| ----------------- | ------------------- | ----------- | --- | ----- | ------------ |
| `body`            | Body                | `text`      |     | ✅    |              |
| `create_date`     | Created on          | `datetime`  |     | ✅    |              |
| `create_uid`      | Created by          | `many2one`  |     | ✅    | res.users    |
| `display_name`    | Display Name        | `char`      |     |       |              |
| `failure_type`    | Failure Type        | `selection` |     | ✅    |              |
| `id`              | ID                  | `integer`   |     | ✅    |              |
| `mail_message_id` | Mail Message        | `many2one`  |     | ✅    | mail.message |
| `number`          | Number              | `char`      |     | ✅    |              |
| `partner_id`      | Customer            | `many2one`  |     | ✅    | res.partner  |
| `sms_tracker_id`  | SMS trackers        | `many2one`  |     |       | sms.tracker  |
| `state`           | SMS Status          | `selection` | ✅  | ✅    |              |
| `to_delete`       | Marked for deletion | `boolean`   |     | ✅    |              |
| `uuid`            | UUID                | `char`      |     | ✅    |              |
| `write_date`      | Last Updated on     | `datetime`  |     | ✅    |              |
| `write_uid`       | Last Updated by     | `many2one`  |     | ✅    | res.users    |

**Access Rights:**

| Name                  | Group                | Perms     |
| --------------------- | -------------------- | --------- |
| access.sms.sms.system | Role / Administrator | `R/W/C/D` |
| access.sms.sms.all    | Everyone             | `-`       |

### 🗃️ `sms.composer` — Send SMS Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                          | Label                      | Type        | Req | Store | Relation     |
| ------------------------------ | -------------------------- | ----------- | --- | ----- | ------------ |
| `body`                         | Message                    | `text`      | ✅  | ✅    |              |
| `comment_single_recipient`     | Single Mode                | `boolean`   |     |       |              |
| `composition_mode`             | Composition Mode           | `selection` | ✅  | ✅    |              |
| `create_date`                  | Created on                 | `datetime`  |     | ✅    |              |
| `create_uid`                   | Created by                 | `many2one`  |     | ✅    | res.users    |
| `display_name`                 | Display Name               | `char`      |     |       |              |
| `id`                           | ID                         | `integer`   |     | ✅    |              |
| `mass_force_send`              | Send directly              | `boolean`   |     | ✅    |              |
| `mass_keep_log`                | Keep a note on document    | `boolean`   |     | ✅    |              |
| `number_field_name`            | Number Field               | `char`      |     | ✅    |              |
| `numbers`                      | Recipients (Numbers)       | `char`      |     | ✅    |              |
| `recipient_invalid_count`      | # Invalid recipients       | `integer`   |     |       |              |
| `recipient_single_description` | Recipients (Partners)      | `text`      |     |       |              |
| `recipient_single_number`      | Stored Recipient Number    | `char`      |     |       |              |
| `recipient_single_number_itf`  | Recipient Number           | `char`      |     | ✅    |              |
| `recipient_single_valid`       | Is valid                   | `boolean`   |     |       |              |
| `recipient_valid_count`        | # Valid recipients         | `integer`   |     |       |              |
| `res_id`                       | Document ID                | `integer`   |     | ✅    |              |
| `res_ids`                      | Document IDs               | `char`      |     | ✅    |              |
| `res_ids_count`                | Visible records count      | `integer`   |     |       |              |
| `res_model`                    | Document Model Name        | `char`      |     | ✅    |              |
| `res_model_description`        | Document Model Description | `char`      |     |       |              |
| `sanitized_numbers`            | Sanitized Number           | `char`      |     |       |              |
| `template_id`                  | Use Template               | `many2one`  |     | ✅    | sms.template |
| `use_exclusion_list`           | Use Exclusion List         | `boolean`   |     | ✅    |              |
| `write_date`                   | Last Updated on            | `datetime`  |     | ✅    |              |
| `write_uid`                    | Last Updated by            | `many2one`  |     | ✅    | res.users    |

**Access Rights:**

| Name                | Group       | Perms   |
| ------------------- | ----------- | ------- |
| access.sms.composer | Role / User | `R/W/C` |

### 🗃️ `sms.account.phone` — SMS Account Registration Phone Number Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `account_id`   | Account         | `many2one` | ✅  | ✅    | iap.account |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `phone_number` | Phone Number    | `char`     | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                            | Group                | Perms     |
| ------------------------------- | -------------------- | --------- |
| access.sms.account.phone.system | Role / Administrator | `R/W/C/D` |

### 🗃️ `sms.account.sender` — SMS Account Sender Name Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `account_id`   | Account         | `many2one` | ✅  | ✅    | iap.account |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `sender_name`  | Sender Name     | `char`     |     | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                             | Group                | Perms     |
| -------------------------------- | -------------------- | --------- |
| access.sms.account.sender.system | Role / Administrator | `R/W/C/D` |

### 🗃️ `sms.account.code` — SMS Account Verification Code Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field               | Label             | Type       | Req | Store | Relation    |
| ------------------- | ----------------- | ---------- | --- | ----- | ----------- |
| `account_id`        | Account           | `many2one` | ✅  | ✅    | iap.account |
| `create_date`       | Created on        | `datetime` |     | ✅    |             |
| `create_uid`        | Created by        | `many2one` |     | ✅    | res.users   |
| `display_name`      | Display Name      | `char`     |     |       |             |
| `id`                | ID                | `integer`  |     | ✅    |             |
| `verification_code` | Verification Code | `char`     | ✅  | ✅    |             |
| `write_date`        | Last Updated on   | `datetime` |     | ✅    |             |
| `write_uid`         | Last Updated by   | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                           | Group                | Perms     |
| ------------------------------ | -------------------- | --------- |
| access.sms.account.code.system | Role / Administrator | `R/W/C/D` |

### 🗃️ `sms.template.preview` — SMS Template Preview

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field             | Label                     | Type        | Req | Store | Relation     |
| ----------------- | ------------------------- | ----------- | --- | ----- | ------------ |
| `body`            | Body                      | `char`      |     |       |              |
| `create_date`     | Created on                | `datetime`  |     | ✅    |              |
| `create_uid`      | Created by                | `many2one`  |     | ✅    | res.users    |
| `display_name`    | Display Name              | `char`      |     |       |              |
| `id`              | ID                        | `integer`   |     | ✅    |              |
| `lang`            | Template Preview Language | `selection` |     | ✅    |              |
| `model_id`        | Applies to                | `many2one`  |     |       | ir.model     |
| `no_record`       | No Record                 | `boolean`   |     |       |              |
| `resource_ref`    | Record reference          | `reference` |     | ✅    |              |
| `sms_template_id` | Sms Template              | `many2one`  | ✅  | ✅    | sms.template |
| `write_date`      | Last Updated on           | `datetime`  |     | ✅    |              |
| `write_uid`       | Last Updated by           | `many2one`  |     | ✅    | res.users    |

**Access Rights:**

| Name                        | Group       | Perms   |
| --------------------------- | ----------- | ------- |
| access.sms.template.preview | Role / User | `R/W/C` |

### 🗃️ `sms.template.reset` — SMS Template Reset

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation     |
| -------------- | --------------- | ----------- | --- | ----- | ------------ |
| `create_date`  | Created on      | `datetime`  |     | ✅    |              |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users    |
| `display_name` | Display Name    | `char`      |     |       |              |
| `id`           | ID              | `integer`   |     | ✅    |              |
| `template_ids` | Template        | `many2many` |     | ✅    | sms.template |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |              |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users    |

**Access Rights:**

| Name                      | Group                | Perms     |
| ------------------------- | -------------------- | --------- |
| access.sms.template.reset | Mail Template Editor | `R/W/C/D` |

### 🗃️ `sms.template` — SMS Templates

Templates for sending SMS

**Fields:**

| Field               | Label                  | Type       | Req | Store | Relation              |
| ------------------- | ---------------------- | ---------- | --- | ----- | --------------------- |
| `body`              | Body                   | `char`     | ✅  | ✅    |                       |
| `create_date`       | Created on             | `datetime` |     | ✅    |                       |
| `create_uid`        | Created by             | `many2one` |     | ✅    | res.users             |
| `display_name`      | Display Name           | `char`     |     |       |                       |
| `id`                | ID                     | `integer`  |     | ✅    |                       |
| `lang`              | Language               | `char`     |     | ✅    |                       |
| `model`             | Related Document Model | `char`     |     | ✅    |                       |
| `model_id`          | Applies to             | `many2one` | ✅  | ✅    | ir.model              |
| `name`              | Name                   | `char`     |     | ✅    |                       |
| `render_model`      | Rendering Model        | `char`     |     |       |                       |
| `sidebar_action_id` | Sidebar action         | `many2one` |     | ✅    | ir.actions.act_window |
| `template_fs`       | Template Filename      | `char`     |     | ✅    |                       |
| `write_date`        | Last Updated on        | `datetime` |     | ✅    |                       |
| `write_uid`         | Last Updated by        | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                              | Group                     | Perms     |
| --------------------------------- | ------------------------- | --------- |
| access.sms.template.sale.manager  | Sales / Administrator     | `R/W/C/D` |
| access.sms.template.sale.manager  | Sales / Administrator     | `R/W/C/D` |
| access.sms.template.event.manager | Events / Administrator    | `R/W/C/D` |
| access.sms.template.stock.manager | Inventory / Administrator | `R/W/C/D` |
| access.sms.template.system        | Role / Administrator      | `R/W/C/D` |
| access.sms.template.user          | Role / User               | `R`       |
| access.sms.template.all           | Everyone                  | `-`       |

**Record Rules:**

- **SMS Template: system group granted all** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **SMS Template: event manager CUD on event / registrations templates** (34) `W/C/D`
  - Domain: `[('model_id.model', 'in', ('event.event', 'event.registration'))]`
- **SMS Template: sale manager CUD on opportunity / partner templates** (27) `W/C/D`
  - Domain: `[('model_id.model', 'in', ('crm.lead', 'res.partner'))]`
- **SMS Template: stock manager CUD on stock picking templates** (59) `W/C/D`
  - Domain: `[('model_id.model', '=', 'stock.picking')]`
- **SMS Template: sale manager CUD on sale orders** (27) `W/C/D`
  - Domain: `[('model_id.model', 'in', ('sale.order', 'res.partner'))]`
