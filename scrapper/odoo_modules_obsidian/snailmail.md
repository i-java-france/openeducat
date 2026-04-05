---
title: "Snail Mail"
module: "snailmail"
state: "installed"
version: "19.0.0.4"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Tools"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_____]
---

# 🟢 Snail Mail

> **Module:** `snailmail` | **Version:** `19.0.0.4` **Category:** Tools | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[iap_mail]] [[mail]]

## 📖 Description

# Allows users to send documents by post

## 🖥️ UI Components

### Menus

- `Settings/Technical/Email/Snailmail Letters`

### Views

- `* INHERIT minimal_layout (qweb)`
- `* INHERIT report_layout (qweb)`
- `snailmail.letter.form (form)`
- `snailmail.letter.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**8 model(s) defined by this module:**

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

### 🗃️ `res.partner` — Contact

> 📧 Mail Thread

Update of res.partner class to take into account the livechat username.

**Fields:**

| Field                                       | Label                                               | Type         | Req | Store | Relation                    |
| ------------------------------------------- | --------------------------------------------------- | ------------ | --- | ----- | --------------------------- |
| `account_move_count`                        | Account Move Count                                  | `integer`    |     |       |                             |
| `active`                                    | Active                                              | `boolean`    |     | ✅    |                             |
| `active_lang_count`                         | Active Lang Count                                   | `integer`    |     |       |                             |
| `activity_calendar_event_id`                | Next Activity Calendar Event                        | `many2one`   |     |       | calendar.event              |
| `activity_date_deadline`                    | Next Activity Deadline                              | `date`       |     |       |                             |
| `activity_exception_decoration`             | Activity Exception Decoration                       | `selection`  |     |       |                             |
| `activity_exception_icon`                   | Icon                                                | `char`       |     |       |                             |
| `activity_ids`                              | Activities                                          | `one2many`   |     | ✅    | mail.activity               |
| `activity_state`                            | Activity State                                      | `selection`  |     |       |                             |
| `activity_summary`                          | Next Activity Summary                               | `char`       |     |       |                             |
| `activity_type_icon`                        | Activity Type Icon                                  | `char`       |     |       |                             |
| `activity_type_id`                          | Next Activity Type                                  | `many2one`   |     |       | mail.activity.type          |
| `activity_user_id`                          | Responsible User                                    | `many2one`   |     |       | res.users                   |
| `applicant_ids`                             | Applicants                                          | `one2many`   |     | ✅    | hr.applicant                |
| `application_count`                         | Applications                                        | `integer`    |     |       |                             |
| `application_statistics`                    | Stats                                               | `json`       |     |       |                             |
| `autopost_bills`                            | Auto-post bills                                     | `selection`  | ✅  | ✅    |                             |
| `available_invoice_template_pdf_report_ids` | Available Invoice Template Pdf Report               | `one2many`   |     |       | ir.actions.report           |
| `available_peppol_eas`                      | Available Peppol Eas                                | `json`       |     |       |                             |
| `avatar_1024`                               | Avatar 1024                                         | `binary`     |     |       |                             |
| `avatar_128`                                | Avatar 128                                          | `binary`     |     |       |                             |
| `avatar_1920`                               | Avatar                                              | `binary`     |     |       |                             |
| `avatar_256`                                | Avatar 256                                          | `binary`     |     |       |                             |
| `avatar_512`                                | Avatar 512                                          | `binary`     |     |       |                             |
| `bank_account_count`                        | Bank                                                | `integer`    |     |       |                             |
| `bank_ids`                                  | Banks                                               | `one2many`   |     | ✅    | res.partner.bank            |
| `barcode`                                   | Barcode                                             | `char`       |     | ✅    |                             |
| `buyer_id`                                  | Buyer                                               | `many2one`   |     | ✅    | res.users                   |
| `calendar_last_notif_ack`                   | Last notification marked as read from base Calendar | `datetime`   |     | ✅    |                             |
| `can_publish`                               | Can Publish                                         | `boolean`    |     |       |                             |
| `category_id`                               | Tags                                                | `many2many`  |     | ✅    | res.partner.category        |
| `certifications_company_count`              | Company Certifications Count                        | `integer`    |     |       |                             |
| `certifications_count`                      | Certifications Count                                | `integer`    |     |       |                             |
| `channel_ids`                               | Channels                                            | `many2many`  |     | ✅    | discuss.channel             |
| `channel_member_ids`                        | Channel Member                                      | `one2many`   |     | ✅    | discuss.channel.member      |
| `chatbot_script_ids`                        | Chatbot Script                                      | `one2many`   |     | ✅    | chatbot.script              |
| `child_ids`                                 | Contact                                             | `one2many`   |     | ✅    | res.partner                 |
| `city`                                      | City                                                | `char`       |     | ✅    |                             |
| `code`                                      | Company Code                                        | `char`       |     | ✅    |                             |
| `color`                                     | Color Index                                         | `integer`    |     | ✅    |                             |
| `comment`                                   | Notes                                               | `html`       |     | ✅    |                             |
| `commercial_company_name`                   | Company Name Entity                                 | `char`       |     | ✅    |                             |
| `commercial_partner_id`                     | Commercial Entity                                   | `many2one`   |     | ✅    | res.partner                 |
| `company_id`                                | Company                                             | `many2one`   |     | ✅    | res.company                 |
| `company_name`                              | Company Name                                        | `char`       |     | ✅    |                             |
| `company_registry`                          | Company ID                                          | `char`       |     | ✅    |                             |
| `company_registry_label`                    | Company ID Label                                    | `char`       |     |       |                             |
| `company_registry_placeholder`              | Company Registry Placeholder                        | `char`       |     |       |                             |
| `company_type`                              | Company Type                                        | `selection`  |     |       |                             |
| `complete_name`                             | Complete Name                                       | `char`       |     | ✅    |                             |
| `contact_address`                           | Complete Address                                    | `char`       |     |       |                             |
| `contact_address_inline`                    | Inlined Complete Address                            | `char`       |     |       |                             |
| `contract_ids`                              | Partner Contracts                                   | `one2many`   |     | ✅    | account.analytic.account    |
| `country_code`                              | Country Code                                        | `char`       |     |       |                             |
| `country_id`                                | Country                                             | `many2one`   |     | ✅    | res.country                 |
| `create_date`                               | Created on                                          | `datetime`   |     | ✅    |                             |
| `create_uid`                                | Created by                                          | `many2one`   |     | ✅    | res.users                   |
| `credit`                                    | Total Receivable                                    | `monetary`   |     |       |                             |
| `credit_limit`                              | Credit Limit                                        | `float`      |     | ✅    |                             |
| `credit_to_invoice`                         | Credit To Invoice                                   | `monetary`   |     |       |                             |
| `currency_id`                               | Currency                                            | `many2one`   |     |       | res.currency                |
| `customer_rank`                             | Customer Rank                                       | `integer`    |     | ✅    |                             |
| `days_sales_outstanding`                    | Days Sales Outstanding (DSO)                        | `float`      |     |       |                             |
| `debit`                                     | Total Payable                                       | `monetary`   |     |       |                             |
| `display_invoice_edi_format`                | Display Invoice Edi Format                          | `boolean`    |     |       |                             |
| `display_invoice_template_pdf_report_id`    | Display Invoice Template Pdf Report                 | `boolean`    |     |       |                             |
| `display_name`                              | Display Name                                        | `char`       |     |       |                             |
| `duplicate_bank_partner_ids`                | Duplicate Bank Partner                              | `many2many`  |     |       | res.partner                 |
| `email`                                     | Email                                               | `char`       |     | ✅    |                             |
| `email_formatted`                           | Formatted Email                                     | `char`       |     |       |                             |
| `email_normalized`                          | Normalized Email                                    | `char`       |     | ✅    |                             |
| `employee`                                  | Employee                                            | `boolean`    |     | ✅    |                             |
| `employee_ids`                              | Employees                                           | `one2many`   |     | ✅    | hr.employee                 |
| `employees_count`                           | Employees Count                                     | `integer`    |     |       |                             |
| `event_count`                               | # Events                                            | `integer`    |     |       |                             |
| `fiscal_country_codes`                      | Fiscal Country Codes                                | `char`       |     |       |                             |
| `fiscal_country_group_codes`                | Fiscal Country Group Codes                          | `json`       |     |       |                             |
| `function`                                  | Job Position                                        | `char`       |     | ✅    |                             |
| `global_location_number`                    | GLN                                                 | `char`       |     | ✅    |                             |
| `group_on`                                  | Week Day                                            | `selection`  | ✅  | ✅    |                             |
| `group_rfq`                                 | Group RFQ                                           | `selection`  | ✅  | ✅    |                             |
| `has_message`                               | Has Message                                         | `boolean`    |     |       |                             |
| `head_office`                               | Head Office                                         | `char`       |     | ✅    |                             |
| `hr_contact`                                | HR Contact                                          | `char`       |     | ✅    |                             |
| `hr_email`                                  | HR Email                                            | `char`       |     | ✅    |                             |
| `hr_name`                                   | HR Name                                             | `char`       |     | ✅    |                             |
| `id`                                        | ID                                                  | `integer`    |     | ✅    |                             |
| `ignore_abnormal_invoice_amount`            | Ignore Abnormal Invoice Amount                      | `boolean`    |     | ✅    |                             |
| `ignore_abnormal_invoice_date`              | Ignore Abnormal Invoice Date                        | `boolean`    |     | ✅    |                             |
| `image_1024`                                | Image 1024                                          | `binary`     |     | ✅    |                             |
| `image_128`                                 | Image 128                                           | `binary`     |     | ✅    |                             |
| `image_1920`                                | Image                                               | `binary`     |     | ✅    |                             |
| `image_256`                                 | Image 256                                           | `binary`     |     | ✅    |                             |
| `image_512`                                 | Image 512                                           | `binary`     |     | ✅    |                             |
| `im_status`                                 | IM Status                                           | `char`       |     |       |                             |
| `industry_id`                               | Industry                                            | `many2one`   |     | ✅    | res.partner.industry        |
| `invoice_edi_format`                        | eInvoice format                                     | `selection`  |     |       |                             |
| `invoice_edi_format_store`                  | Invoice Edi Format Store                            | `char`       |     | ✅    |                             |
| `invoice_ids`                               | Invoices                                            | `one2many`   |     | ✅    | account.move                |
| `invoice_sending_method`                    | Invoice sending                                     | `selection`  |     | ✅    |                             |
| `invoice_template_pdf_report_id`            | Invoice report                                      | `many2one`   |     | ✅    | ir.actions.report           |
| `is_blacklisted`                            | Blacklist                                           | `boolean`    |     |       |                             |
| `is_company`                                | Is a Company                                        | `boolean`    |     | ✅    |                             |
| `is_in_call`                                | Is In Call                                          | `boolean`    |     |       |                             |
| `is_parent`                                 | Is a Parent                                         | `boolean`    |     | ✅    |                             |
| `is_peppol_edi_format`                      | Is Peppol Edi Format                                | `boolean`    |     |       |                             |
| `is_pickup_location`                        | Is Pickup Location                                  | `boolean`    |     | ✅    |                             |
| `is_public`                                 | Is Public                                           | `boolean`    |     |       |                             |
| `is_published`                              | Is Published                                        | `boolean`    |     | ✅    |                             |
| `is_seo_optimized`                          | SEO optimized                                       | `boolean`    |     | ✅    |                             |
| `is_student`                                | Is a Student                                        | `boolean`    |     | ✅    |                             |
| `is_ubl_format`                             | Is Ubl Format                                       | `boolean`    |     |       |                             |
| `is_venue`                                  | Venue                                               | `boolean`    |     | ✅    |                             |
| `lang`                                      | Language                                            | `selection`  |     | ✅    |                             |
| `leave_date_to`                             | Leave Date To                                       | `date`       |     |       |                             |
| `livechat_channel_count`                    | Livechat Channel Count                              | `integer`    |     |       |                             |
| `main_user_id`                              | Main User                                           | `many2one`   |     |       | res.users                   |
| `meeting_count`                             | # Meetings                                          | `integer`    |     |       |                             |
| `meeting_ids`                               | Meetings                                            | `many2many`  |     | ✅    | calendar.event              |
| `message_attachment_count`                  | Attachment Count                                    | `integer`    |     |       |                             |
| `message_bounce`                            | Bounce                                              | `integer`    |     | ✅    |                             |
| `message_follower_ids`                      | Followers                                           | `one2many`   |     | ✅    | mail.followers              |
| `message_has_error`                         | Message Delivery error                              | `boolean`    |     |       |                             |
| `message_has_error_counter`                 | Number of errors                                    | `integer`    |     |       |                             |
| `message_has_sms_error`                     | SMS Delivery error                                  | `boolean`    |     |       |                             |
| `message_ids`                               | Messages                                            | `one2many`   |     | ✅    | mail.message                |
| `message_is_follower`                       | Is Follower                                         | `boolean`    |     |       |                             |
| `message_needaction`                        | Action Needed                                       | `boolean`    |     |       |                             |
| `message_needaction_counter`                | Number of Actions                                   | `integer`    |     |       |                             |
| `message_partner_ids`                       | Followers (Partners)                                | `many2many`  |     |       | res.partner                 |
| `my_activity_date_deadline`                 | My Activity Deadline                                | `date`       |     |       |                             |
| `name`                                      | Name                                                | `char`       |     | ✅    |                             |
| `offline_since`                             | Offline since                                       | `datetime`   |     |       |                             |
| `on_time_rate`                              | On-Time Delivery Rate                               | `float`      |     |       |                             |
| `opportunity_count`                         | Opportunity Count                                   | `integer`    |     |       |                             |
| `opportunity_ids`                           | Opportunities                                       | `one2many`   |     | ✅    | crm.lead                    |
| `parent_id`                                 | Related Company                                     | `many2one`   |     | ✅    | res.partner                 |
| `parent_name`                               | Parent name                                         | `char`       |     |       |                             |
| `partner_company_registry_placeholder`      | Partner Company Registry Placeholder                | `char`       |     |       |                             |
| `partner_latitude`                          | Geo Latitude                                        | `float`      |     | ✅    |                             |
| `partner_longitude`                         | Geo Longitude                                       | `float`      |     | ✅    |                             |
| `partner_share`                             | Share Partner                                       | `boolean`    |     | ✅    |                             |
| `partner_vat_placeholder`                   | Partner Vat Placeholder                             | `char`       |     |       |                             |
| `payment_token_count`                       | Payment Token Count                                 | `integer`    |     |       |                             |
| `payment_token_ids`                         | Payment Tokens                                      | `one2many`   |     | ✅    | payment.token               |
| `peppol_eas`                                | Peppol e-address (EAS)                              | `selection`  |     | ✅    |                             |
| `peppol_endpoint`                           | Peppol Endpoint                                     | `char`       |     | ✅    |                             |
| `phone`                                     | Phone                                               | `char`       |     | ✅    |                             |
| `phone_blacklisted`                         | Blacklisted Phone is Phone                          | `boolean`    |     |       |                             |
| `phone_mobile_search`                       | Phone Number                                        | `char`       |     |       |                             |
| `phone_sanitized`                           | Sanitized Number                                    | `char`       |     | ✅    |                             |
| `phone_sanitized_blacklisted`               | Phone Blacklisted                                   | `boolean`    |     |       |                             |
| `picking_warn_msg`                          | Message for Stock Picking                           | `text`       |     | ✅    |                             |
| `properties`                                | Properties                                          | `properties` |     | ✅    |                             |
| `properties_base_definition_id`             | Properties Base Definition                          | `many2one`   |     |       | properties.base.definition  |
| `property_account_payable_id`               | Account Payable                                     | `many2one`   |     | ✅    | account.account             |
| `property_account_position_id`              | Fiscal Position                                     | `many2one`   |     | ✅    | account.fiscal.position     |
| `property_account_receivable_id`            | Account Receivable                                  | `many2one`   |     | ✅    | account.account             |
| `property_delivery_carrier_id`              | Delivery Method                                     | `many2one`   |     | ✅    | delivery.carrier            |
| `property_inbound_payment_method_line_id`   | Property Inbound Payment Method Line                | `many2one`   |     | ✅    | account.payment.method.line |
| `property_outbound_payment_method_line_id`  | Property Outbound Payment Method Line               | `many2one`   |     | ✅    | account.payment.method.line |
| `property_payment_term_id`                  | Customer Payment Terms                              | `many2one`   |     | ✅    | account.payment.term        |
| `property_product_pricelist`                | Pricelist                                           | `many2one`   |     |       | product.pricelist           |
| `property_purchase_currency_id`             | Supplier Currency                                   | `many2one`   |     | ✅    | res.currency                |
| `property_stock_customer`                   | Customer Location                                   | `many2one`   |     | ✅    | stock.location              |
| `property_stock_supplier`                   | Vendor Location                                     | `many2one`   |     | ✅    | stock.location              |
| `property_supplier_payment_term_id`         | Vendor Payment Terms                                | `many2one`   |     | ✅    | account.payment.term        |
| `purchase_line_ids`                         | Purchase Lines                                      | `one2many`   |     | ✅    | purchase.order.line         |
| `purchase_order_count`                      | Purchase Order Count                                | `integer`    |     |       |                             |
| `purchase_warn_msg`                         | Message for Purchase Order                          | `text`       |     | ✅    |                             |
| `rating_ids`                                | Ratings                                             | `one2many`   |     | ✅    | rating.rating               |
| `receipt_reminder_email`                    | Receipt Reminder                                    | `boolean`    |     | ✅    |                             |
| `ref`                                       | Reference                                           | `char`       |     | ✅    |                             |
| `ref_company_ids`                           | Companies that refers to partner                    | `one2many`   |     | ✅    | res.company                 |
| `reminder_date_before_receipt`              | Days Before Receipt                                 | `integer`    |     | ✅    |                             |
| `rtc_session_ids`                           | Rtc Session                                         | `one2many`   |     | ✅    | discuss.channel.rtc.session |
| `sale_order_count`                          | Sale Order Count                                    | `integer`    |     |       |                             |
| `sale_order_ids`                            | Sales Order                                         | `one2many`   |     | ✅    | sale.order                  |
| `sale_warn_msg`                             | Message for Sales Order                             | `text`       |     | ✅    |                             |
| `same_company_registry_partner_id`          | Partner with same Company Registry                  | `many2one`   |     |       | res.partner                 |
| `same_vat_partner_id`                       | Partner with same Tax ID                            | `many2one`   |     |       | res.partner                 |
| `self`                                      | Self                                                | `many2one`   |     |       | res.partner                 |
| `seo_name`                                  | Seo name                                            | `char`       |     | ✅    |                             |
| `show_credit_limit`                         | Show Credit Limit                                   | `boolean`    |     |       |                             |
| `signup_type`                               | Signup Token Type                                   | `char`       |     | ✅    |                             |
| `specific_property_product_pricelist`       | Specific Property Product Pricelist                 | `many2one`   |     | ✅    | product.pricelist           |
| `state_id`                                  | State                                               | `many2one`   |     | ✅    | res.country.state           |
| `static_map_url`                            | Static Map Url                                      | `char`       |     |       |                             |
| `static_map_url_is_valid`                   | Static Map Url Is Valid                             | `boolean`    |     |       |                             |
| `street`                                    | Street                                              | `char`       |     | ✅    |                             |
| `street2`                                   | Street2                                             | `char`       |     | ✅    |                             |
| `suggest_based_on`                          | Suggest Based On                                    | `char`       |     | ✅    |                             |
| `suggest_days`                              | Suggest Days                                        | `integer`    |     | ✅    |                             |
| `suggest_percent`                           | Suggest Percent                                     | `integer`    |     | ✅    |                             |
| `supplier_invoice_count`                    | # Vendor Bills                                      | `integer`    |     |       |                             |
| `supplier_rank`                             | Supplier Rank                                       | `integer`    |     | ✅    |                             |
| `ticket_count`                              | Ticket Count                                        | `integer`    |     |       |                             |
| `title`                                     | Title                                               | `many2one`   |     | ✅    | res.partner.title           |
| `total_invoiced`                            | Total Invoiced                                      | `monetary`   |     |       |                             |
| `trust`                                     | Degree of trust you have in this debtor             | `selection`  |     | ✅    |                             |
| `type`                                      | Address Type                                        | `selection`  |     | ✅    |                             |
| `type_address_label`                        | Address Type Description                            | `char`       |     |       |                             |
| `tz`                                        | Timezone                                            | `selection`  |     | ✅    |                             |
| `tz_offset`                                 | Timezone offset                                     | `char`       |     |       |                             |
| `use_partner_credit_limit`                  | Partner Limit                                       | `boolean`    |     |       |                             |
| `user_id`                                   | Salesperson                                         | `many2one`   |     | ✅    | res.users                   |
| `user_ids`                                  | Users                                               | `one2many`   |     | ✅    | res.users                   |
| `user_livechat_username`                    | User Livechat Username                              | `char`       |     |       |                             |
| `vat`                                       | Tax ID                                              | `char`       |     | ✅    |                             |
| `vat_label`                                 | Tax ID Label                                        | `char`       |     |       |                             |
| `visitor_ids`                               | Visitors                                            | `one2many`   |     | ✅    | website.visitor             |
| `website`                                   | Website Link                                        | `char`       |     | ✅    |                             |
| `website_absolute_url`                      | Website Absolute URL                                | `char`       |     |       |                             |
| `website_description`                       | Website Partner Full Description                    | `html`       |     | ✅    |                             |
| `website_id`                                | Website                                             | `many2one`   |     | ✅    | website                     |
| `website_message_ids`                       | Website Messages                                    | `one2many`   |     | ✅    | mail.message                |
| `website_meta_description`                  | Website meta description                            | `text`       |     | ✅    |                             |
| `website_meta_keywords`                     | Website meta keywords                               | `char`       |     | ✅    |                             |
| `website_meta_og_img`                       | Website opengraph image                             | `char`       |     | ✅    |                             |
| `website_meta_title`                        | Website meta title                                  | `char`       |     | ✅    |                             |
| `website_published`                         | Visible on current website                          | `boolean`    |     |       |                             |
| `website_short_description`                 | Website Partner Short Description                   | `text`       |     | ✅    |                             |
| `website_url`                               | Website URL                                         | `char`       |     |       |                             |
| `wishlist_ids`                              | Wishlist                                            | `one2many`   |     | ✅    | product.wishlist            |
| `write_date`                                | Last Updated on                                     | `datetime`   |     | ✅    |                             |
| `write_uid`                                 | Last Updated by                                     | `many2one`   |     | ✅    | res.users                   |
| `zip`                                       | Zip                                                 | `char`       |     | ✅    |                             |

**Access Rights:**

| Name                              | Group                                        | Perms     |
| --------------------------------- | -------------------------------------------- | --------- |
| res.partner.crm.user              | Sales / User: Own Documents Only             | `R/W/C`   |
| res.partner.sale.user             | Sales / User: Own Documents Only             | `R`       |
| res.partner.crm.manager           | Sales / Administrator                        | `R`       |
| res.partner.sale.manager          | Sales / Administrator                        | `R/W/C`   |
| res_partner group_account_manager | Accounting / Advisor                         | `R`       |
| res.partner purchase              | Purchase / User                              | `R`       |
| res.partner.purchase.manager      | Purchase / Administrator                     | `R/W/C`   |
| res.partner.user                  | Recruitment / Officer: Manage all applicants | `R/W/C/D` |
| name_op_res_partner_student       | OpenEduCat / Manager                         | `R/W/C/D` |
| name_op_res_partner_faculty       | OpenEduCat / User                            | `R/W/C`   |
| name_op_res_partner_library       | Library / Manager                            | `R`       |
| res_partner group_partner_manager | Contact / Creation                           | `R/W/C/D` |
| res_partner group_stock_manager   | Inventory / Administrator                    | `R/W/C`   |
| res_partner group_portal          | Role / Portal                                | `R`       |
| res_partner group_public          | Role / Public                                | `R`       |
| res_partner group_user            | Role / User                                  | `R`       |

**Record Rules:**

- **res.partner company** (Global) `R/W/C/D`
  - Domain:
    `['|', '|', ('partner_share', '=', False), ('company_id', 'parent_of', company_ids), ('company_id', '=', False)]`
- **res_partner: portal/public: read access on my commercial partner** (10, 11) `R`
  - Domain: `[('id', 'child_of', user.commercial_partner_id.id)]`

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

### 🗃️ `snailmail.letter` — Snailmail Letter

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field              | Label                               | Type        | Req | Store | Relation          |
| ------------------ | ----------------------------------- | ----------- | --- | ----- | ----------------- |
| `attachment_datas` | Document                            | `binary`    |     |       |                   |
| `attachment_fname` | Attachment Filename                 | `char`      |     |       |                   |
| `attachment_id`    | Attachment                          | `many2one`  |     | ✅    | ir.attachment     |
| `city`             | City                                | `char`      |     | ✅    |                   |
| `color`            | Color                               | `boolean`   |     | ✅    |                   |
| `company_id`       | Company                             | `many2one`  | ✅  | ✅    | res.company       |
| `country_id`       | Country                             | `many2one`  |     | ✅    | res.country       |
| `cover`            | Cover Page                          | `boolean`   |     | ✅    |                   |
| `create_date`      | Created on                          | `datetime`  |     | ✅    |                   |
| `create_uid`       | Created by                          | `many2one`  |     | ✅    | res.users         |
| `display_name`     | Display Name                        | `char`      |     |       |                   |
| `duplex`           | Both side                           | `boolean`   |     | ✅    |                   |
| `error_code`       | Error                               | `selection` |     | ✅    |                   |
| `id`               | ID                                  | `integer`   |     | ✅    |                   |
| `info_msg`         | Information                         | `html`      |     | ✅    |                   |
| `message_id`       | Snailmail Status Message            | `many2one`  |     | ✅    | mail.message      |
| `model`            | Model                               | `char`      | ✅  | ✅    |                   |
| `notification_ids` | Notifications                       | `one2many`  |     | ✅    | mail.notification |
| `partner_id`       | Recipient                           | `many2one`  | ✅  | ✅    | res.partner       |
| `reference`        | Related Record                      | `char`      |     |       |                   |
| `report_template`  | Optional report to print and attach | `many2one`  |     | ✅    | ir.actions.report |
| `res_id`           | Document ID                         | `integer`   | ✅  | ✅    |                   |
| `state`            | Status                              | `selection` | ✅  | ✅    |                   |
| `state_id`         | State                               | `many2one`  |     | ✅    | res.country.state |
| `street`           | Street                              | `char`      |     | ✅    |                   |
| `street2`          | Street2                             | `char`      |     | ✅    |                   |
| `user_id`          | Sent by                             | `many2one`  |     | ✅    | res.users         |
| `write_date`       | Last Updated on                     | `datetime`  |     | ✅    |                   |
| `write_uid`        | Last Updated by                     | `many2one`  |     | ✅    | res.users         |
| `zip`              | Zip                                 | `char`      |     | ✅    |                   |

**Access Rights:**

| Name                    | Group                | Perms     |
| ----------------------- | -------------------- | --------- |
| snailmail.letter.system | Role / Administrator | `R/W/C/D` |
| snailmail.letter.user   | Role / User          | `R/W/C`   |
