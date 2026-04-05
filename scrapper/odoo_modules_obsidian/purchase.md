---
title: "Purchase"
module: "purchase"
state: "installed"
version: "19.0.1.2"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/app/purchase"
license: "LGPL-3"
category: "Purchase"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/________, odoo/app]
---

# 🟢 Purchase

> **Module:** `purchase` | **Version:** `19.0.1.2` **Category:** Purchase | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** https://www.odoo.com/app/purchase

## 🔗 Dependencies

[[account]]

## 📖 Description

# Odoo Supply Chain

Automate requisition-to-pay, control invoicing with the Odoo
<a href="<https://www.odoo.com/app/purchase>">Open Source Supply Chain</a>.

Automate procurement propositions, launch request for quotations, track purchase orders,
manage vendors' information, control products reception and check vendors' invoices.

# Automated Procurement Propositions

Reduce inventory level with procurement rules. Get the right purchase proposition at the
right time to reduce your inventory level. Improve your purchase and inventory
performance with procurement rules depending on stock levels, logistic rules, sales
orders, forecasted manufacturing orders, etc.

Send requests for quotations or purchase orders to your vendor in one click. Get access
to product receptions and invoices from your purchase order.

# Purchase Tenders

Launch purchase tenders, integrate vendor's answers in the process and compare
propositions. Choose the best offer and send purchase orders easily. Use reporting to
analyse the quality of your vendors afterwards.

# Email integrations

Integrate all vendor's communications on the purchase orders (or RfQs) to get a strong
traceability on the negotiation or after sales service issues. Use the claim management
module to track issues related to vendors.

# Standard Price, Average Price, FIFO

Use the costing method that reflects your business: standard price, average price, fifo
or lifo. Get your accounting entries and the right inventory valuation in real-time;
Odoo manages everything for you, transparently.

# Import Vendor Pricelists

Take smart purchase decisions using the best prices. Easily import vendor's pricelists
to make smarter purchase decisions based on promotions, prices depending on quantities
and special contract conditions. You can even base your sale price depending on your
vendor's prices.

# Control Products and Invoices

No product or order is left behind, the inventory control allows you to manage back
orders, refunds, product reception and quality control. Choose the right control method
according to your need.

Control vendor bills with no effort. Choose the right method according to your need:
pre-generate draft invoices based on purchase orders, on products receptions, create
invoices manually and import lines from purchase orders, etc.

## 🖥️ UI Components

### Menus

- `Purchase`
- `Purchase/Configuration`
- `Purchase/Configuration/Products`
- `Purchase/Configuration/Products/Attributes`
- `Purchase/Configuration/Products/Categories`
- `Purchase/Configuration/Products/Units & Packagings`
- `Purchase/Configuration/Settings`
- `Purchase/Configuration/Vendor Pricelists`
- `Purchase/Orders`
- `Purchase/Orders/Purchase Orders`
- `Purchase/Orders/Requests for Quotation`
- `Purchase/Orders/Vendors`
- `Purchase/Products`
- `Purchase/Products/Product Variants`
- `Purchase/Products/Products`
- `Purchase/Reporting`
- `Purchase/Reporting/Purchase`

### Views

- `* INHERIT Portal layout : purchase menu entries (qweb)`
- `* INHERIT Portal: My Purchase Order Update Dates (qweb)`
- `* INHERIT Purchase Order (qweb)`
- `* INHERIT Requests for Quotation / Purchase Orders (qweb)`
- `* INHERIT account.analytic.account.form.purchase (form)`
- `* INHERIT account.move.inherit.purchase (form)`
- `* INHERIT document_tax_totals (qweb)`
- `* INHERIT product.product.form (form)`
- `* INHERIT product.product.purchase.order (form)`
- `* INHERIT product.supplierinfo.list.view2 (list)`
- `* INHERIT product.supplierinfo.list.view2.product (list)`
- `* INHERIT product.template.purchase.button.inherit (form)`
- `* INHERIT product.template.search.purchase (search)`
- `* INHERIT product.template.supplier.form.inherit (form)`
- `* INHERIT product.view.kanban.catalog.purchase (kanban)`
- `* INHERIT product.view.search.catalog.inherit.purchase (search)`
- `* INHERIT purchase.order.view.kanban.without.dashboard (kanban)`
- `* INHERIT res.config.settings.view.form.inherit.purchase (form)`
- `* INHERIT res.partner.purchase.property.form.inherit (form)`
- `* INHERIT res.partner.view.purchase.buttons (form)`
- `My Purchase Orders (qweb)`
- `My Requests For Quotation (qweb)`
- `Purchase Order Portal Content (qweb)`
- `bill.to.po.wizard.form (form)`
- `product.month.graph (graph)`
- `product.month.pivot (pivot)`
- `purchase.bill.line.match.list (list)`
- `purchase.bill.union.list (list)`
- `purchase.bill.union.select (search)`
- `purchase.history.graph (graph)`
- `purchase.history.list (list)`
- `purchase.history.pivot (pivot)`
- `purchase.order.activity (activity)`
- `purchase.order.calendar (calendar)`
- `purchase.order.form (form)`
- `purchase.order.graph (graph)`
- `purchase.order.inherit.purchase.order.list (list)`
- `purchase.order.kanban (kanban)`
- `purchase.order.line.form2 (form)`
- `purchase.order.line.list (list)`
- `purchase.order.line.search (search)`
- `purchase.order.list (list)`
- `purchase.order.pivot (pivot)`
- `purchase.order.select (search)`
- `purchase.order.view.list (list)`
- `purchase.report.view.list (list)`
- `purchase_order_portal_content_totals_table (qweb)`
- `report.purchase.order.search (search)`
- `report_purchaseorder (qweb)`
- `report_purchaseorder_document (qweb)`
- `report_purchasequotation (qweb)`
- `report_purchasequotation_document (qweb)`
- `request.quotation.select (search)`
- `track_po_line_qty_received_template (qweb)`
- `track_po_line_template (qweb)`

### Reports

- `Purchase Order`
- `Request for Quotation`

## 🛠️ Technical Documentation

**18 model(s) defined by this module:**

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

### 🗃️ `product.product` — Product Variant

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                       | Label                                    | Type                    | Req | Store | Relation                         |
| ------------------------------------------- | ---------------------------------------- | ----------------------- | --- | ----- | -------------------------------- |
| `accessory_product_ids`                     | Accessory Products                       | `many2many`             |     |       | product.product                  |
| `account_tag_ids`                           | Account Tags                             | `many2many`             |     |       | account.account.tag              |
| `active`                                    | Active                                   | `boolean`               |     | ✅    |                                  |
| `activity_calendar_event_id`                | Next Activity Calendar Event             | `many2one`              |     |       | calendar.event                   |
| `activity_date_deadline`                    | Next Activity Deadline                   | `date`                  |     |       |                                  |
| `activity_exception_decoration`             | Activity Exception Decoration            | `selection`             |     |       |                                  |
| `activity_exception_icon`                   | Icon                                     | `char`                  |     |       |                                  |
| `activity_ids`                              | Activities                               | `one2many`              |     | ✅    | mail.activity                    |
| `activity_state`                            | Activity State                           | `selection`             |     |       |                                  |
| `activity_summary`                          | Next Activity Summary                    | `char`                  |     |       |                                  |
| `activity_type_icon`                        | Activity Type Icon                       | `char`                  |     |       |                                  |
| `activity_type_id`                          | Next Activity Type                       | `many2one`              |     |       | mail.activity.type               |
| `activity_user_id`                          | Responsible User                         | `many2one`              |     |       | res.users                        |
| `additional_product_tag_ids`                | Variant Tags                             | `many2many`             |     | ✅    | product.tag                      |
| `allow_out_of_stock_order`                  | Sell when Out-of-Stock                   | `boolean`               |     |       |                                  |
| `all_product_tag_ids`                       | All Product Tag                          | `many2many`             |     |       | product.tag                      |
| `alternative_product_ids`                   | Alternative Products                     | `many2many`             |     |       | product.template                 |
| `asset_category_id`                         | Asset Type                               | `many2one`              |     |       | account.asset.category           |
| `attribute_line_ids`                        | Product Attributes                       | `one2many`              |     |       | product.template.attribute.line  |
| `available_threshold`                       | Show Threshold                           | `float`                 |     |       |                                  |
| `avg_cost`                                  | Average Cost                             | `monetary`              |     |       |                                  |
| `barcode`                                   | Barcode                                  | `char`                  |     | ✅    |                                  |
| `base_unit_count`                           | Base Unit Count                          | `float`                 | ✅  | ✅    |                                  |
| `base_unit_id`                              | Custom Unit of Measure                   | `many2one`              |     | ✅    | website.base.unit                |
| `base_unit_name`                            | Base Unit Name                           | `char`                  |     |       |                                  |
| `base_unit_price`                           | Price Per Unit                           | `monetary`              |     |       |                                  |
| `can_be_expensed`                           | Expenses                                 | `boolean`               |     |       |                                  |
| `can_image_1024_be_zoomed`                  | Can Image 1024 be zoomed                 | `boolean`               |     |       |                                  |
| `can_image_variant_1024_be_zoomed`          | Can Variant Image 1024 be zoomed         | `boolean`               |     | ✅    |                                  |
| `can_publish`                               | Can Publish                              | `boolean`               |     |       |                                  |
| `categ_id`                                  | Product Category                         | `many2one`              |     |       | product.category                 |
| `code`                                      | Reference                                | `char`                  |     |       |                                  |
| `color`                                     | Color Index                              | `integer`               |     |       |                                  |
| `combination_indices`                       | Combination Indices                      | `char`                  |     | ✅    |                                  |
| `combo_ids`                                 | Combo Choices                            | `many2many`             |     |       | product.combo                    |
| `company_currency_id`                       | Valuation Currency                       | `many2one`              |     |       | res.currency                     |
| `company_id`                                | Company                                  | `many2one`              |     |       | res.company                      |
| `compare_list_price`                        | Compare to Price                         | `monetary`              |     |       |                                  |
| `cost_currency_id`                          | Cost Currency                            | `many2one`              |     |       | res.currency                     |
| `cost_method`                               | Cost Method                              | `selection`             |     |       |                                  |
| `country_of_origin`                         | Origin of Goods                          | `many2one`              |     |       | res.country                      |
| `create_date`                               | Created on                               | `datetime`              |     | ✅    |                                  |
| `create_uid`                                | Created by                               | `many2one`              |     | ✅    | res.users                        |
| `currency_id`                               | Currency                                 | `many2one`              |     |       | res.currency                     |
| `default_code`                              | Internal Reference                       | `char`                  |     | ✅    |                                  |
| `deferred_revenue_category_id`              | Deferred Revenue Type                    | `many2one`              |     |       | account.asset.category           |
| `description`                               | Description                              | `html`                  |     |       |                                  |
| `description_ecommerce`                     | eCommerce Description                    | `html`                  |     |       |                                  |
| `description_picking`                       | Description on Picking                   | `text`                  |     |       |                                  |
| `description_pickingin`                     | Description on Receptions                | `text`                  |     |       |                                  |
| `description_pickingout`                    | Description on Delivery Orders           | `text`                  |     |       |                                  |
| `description_purchase`                      | Purchase Description                     | `text`                  |     |       |                                  |
| `description_sale`                          | Sales Description                        | `text`                  |     |       |                                  |
| `display_name`                              | Display Name                             | `char`                  |     |       |                                  |
| `event_ticket_ids`                          | Event Tickets                            | `one2many`              |     | ✅    | event.event.ticket               |
| `expense_policy`                            | Re-Invoice Costs                         | `selection`             |     |       |                                  |
| `expense_policy_tooltip`                    | Expense Policy Tooltip                   | `char`                  |     |       |                                  |
| `fiscal_country_codes`                      | Fiscal Country Codes                     | `char`                  |     |       |                                  |
| `free_qty`                                  | Free To Use Quantity                     | `float`                 |     |       |                                  |
| `has_available_route_ids`                   | Routes can be selected on this product   | `boolean`               |     |       |                                  |
| `has_configurable_attributes`               | Is a configurable product                | `boolean`               |     |       |                                  |
| `has_message`                               | Has Message                              | `boolean`               |     |       |                                  |
| `hs_code`                                   | HS Code                                  | `char`                  |     |       |                                  |
| `id`                                        | ID                                       | `integer`               |     | ✅    |                                  |
| `image_1024`                                | Image 1024                               | `binary`                |     |       |                                  |
| `image_128`                                 | Image 128                                | `binary`                |     |       |                                  |
| `image_1920`                                | Image                                    | `binary`                |     |       |                                  |
| `image_256`                                 | Image 256                                | `binary`                |     |       |                                  |
| `image_512`                                 | Image 512                                | `binary`                |     |       |                                  |
| `image_variant_1024`                        | Variant Image 1024                       | `binary`                |     | ✅    |                                  |
| `image_variant_128`                         | Variant Image 128                        | `binary`                |     | ✅    |                                  |
| `image_variant_1920`                        | Variant Image                            | `binary`                |     | ✅    |                                  |
| `image_variant_256`                         | Variant Image 256                        | `binary`                |     | ✅    |                                  |
| `image_variant_512`                         | Variant Image 512                        | `binary`                |     | ✅    |                                  |
| `incoming_qty`                              | Incoming                                 | `float`                 |     |       |                                  |
| `invoice_policy`                            | Invoicing Policy                         | `selection`             |     |       |                                  |
| `is_dynamically_created`                    | Is Dynamically Created                   | `boolean`               |     |       |                                  |
| `is_favorite`                               | Favorite                                 | `boolean`               |     | ✅    |                                  |
| `is_in_purchase_order`                      | Is In Purchase Order                     | `boolean`               |     |       |                                  |
| `is_in_selected_section_of_order`           | Is In Selected Section Of Order          | `boolean`               |     | ✅    |                                  |
| `is_product_variant`                        | Is Product Variant                       | `boolean`               |     |       |                                  |
| `is_published`                              | Is Published                             | `boolean`               |     |       |                                  |
| `is_seo_optimized`                          | SEO optimized                            | `boolean`               |     |       |                                  |
| `is_storable`                               | Track Inventory                          | `boolean`               |     |       |                                  |
| `list_price`                                | Sales Price                              | `float`                 |     |       |                                  |
| `location_id`                               | Location                                 | `many2one`              |     |       | stock.location                   |
| `lot_properties_definition`                 | Lot Properties                           | `properties_definition` |     | ✅    |                                  |
| `lot_sequence_id`                           | Serial/Lot Numbers Sequence              | `many2one`              |     |       | ir.sequence                      |
| `lot_valuated`                              | Valuation by Lot/Serial                  | `boolean`               |     |       |                                  |
| `lst_price`                                 | Sales Price                              | `float`                 |     |       |                                  |
| `message_attachment_count`                  | Attachment Count                         | `integer`               |     |       |                                  |
| `message_follower_ids`                      | Followers                                | `one2many`              |     | ✅    | mail.followers                   |
| `message_has_error`                         | Message Delivery error                   | `boolean`               |     |       |                                  |
| `message_has_error_counter`                 | Number of errors                         | `integer`               |     |       |                                  |
| `message_has_sms_error`                     | SMS Delivery error                       | `boolean`               |     |       |                                  |
| `message_ids`                               | Messages                                 | `one2many`              |     | ✅    | mail.message                     |
| `message_is_follower`                       | Is Follower                              | `boolean`               |     |       |                                  |
| `message_needaction`                        | Action Needed                            | `boolean`               |     |       |                                  |
| `message_needaction_counter`                | Number of Actions                        | `integer`               |     |       |                                  |
| `message_partner_ids`                       | Followers (Partners)                     | `many2many`             |     |       | res.partner                      |
| `monthly_demand`                            | Monthly Demand                           | `float`                 |     |       |                                  |
| `my_activity_date_deadline`                 | My Activity Deadline                     | `date`                  |     |       |                                  |
| `name`                                      | Name                                     | `char`                  | ✅  |       |                                  |
| `nbr_moves_in`                              | Nbr Moves In                             | `integer`               |     |       |                                  |
| `nbr_moves_out`                             | Nbr Moves Out                            | `integer`               |     |       |                                  |
| `nbr_reordering_rules`                      | Reordering Rules                         | `integer`               |     |       |                                  |
| `next_serial`                               | Next Serial                              | `char`                  |     |       |                                  |
| `optional_product_ids`                      | Optional Products                        | `many2many`             |     |       | product.template                 |
| `orderpoint_ids`                            | Minimum Stock Rules                      | `one2many`              |     | ✅    | stock.warehouse.orderpoint       |
| `outgoing_qty`                              | Outgoing                                 | `float`                 |     |       |                                  |
| `out_of_stock_message`                      | Out-of-Stock Message                     | `html`                  |     |       |                                  |
| `partner_ref`                               | Customer Ref                             | `char`                  |     |       |                                  |
| `price_extra`                               | Variant Price Extra                      | `float`                 |     |       |                                  |
| `pricelist_rule_ids`                        | Pricelist Rules                          | `one2many`              |     |       | product.pricelist.item           |
| `product_catalog_product_is_in_sale_order`  | Product Catalog Product Is In Sale Order | `boolean`               |     |       |                                  |
| `product_document_count`                    | Documents Count                          | `integer`               |     |       |                                  |
| `product_document_ids`                      | Documents                                | `one2many`              |     | ✅    | product.document                 |
| `product_properties`                        | Properties                               | `properties`            |     |       |                                  |
| `product_tag_ids`                           | Tags                                     | `many2many`             |     |       | product.tag                      |
| `product_template_attribute_value_ids`      | Attribute Values                         | `many2many`             |     | ✅    | product.template.attribute.value |
| `product_template_image_ids`                | Extra Product Media                      | `one2many`              |     |       | product.image                    |
| `product_template_variant_value_ids`        | Variant Values                           | `many2many`             |     | ✅    | product.template.attribute.value |
| `product_tmpl_id`                           | Product Template                         | `many2one`              | ✅  | ✅    | product.template                 |
| `product_tooltip`                           | Product Tooltip                          | `char`                  |     |       |                                  |
| `product_uom_ids`                           | Unit Barcode                             | `one2many`              |     | ✅    | product.uom                      |
| `product_variant_count`                     | # Product Variants                       | `integer`               |     |       |                                  |
| `product_variant_id`                        | Product                                  | `many2one`              |     |       | product.product                  |
| `product_variant_ids`                       | Products                                 | `one2many`              | ✅  |       | product.product                  |
| `product_variant_image_ids`                 | Extra Variant Images                     | `one2many`              |     | ✅    | product.image                    |
| `property_account_expense_id`               | Expense Account                          | `many2one`              |     |       | account.account                  |
| `property_account_income_id`                | Income Account                           | `many2one`              |     |       | account.account                  |
| `property_price_difference_account_id`      | Price Difference Account                 | `many2one`              |     |       | account.account                  |
| `property_stock_inventory`                  | Inventory Location                       | `many2one`              |     |       | stock.location                   |
| `property_stock_production`                 | Production Location                      | `many2one`              |     |       | stock.location                   |
| `public_categ_ids`                          | Website Product Category                 | `many2many`             |     |       | product.public.category          |
| `publish_date`                              | Publish Date                             | `datetime`              | ✅  |       |                                  |
| `purchased_product_qty`                     | Purchased                                | `float`                 |     |       |                                  |
| `purchase_line_warn_msg`                    | Message for Purchase Order Line          | `text`                  |     |       |                                  |
| `purchase_method`                           | Control Policy                           | `selection`             |     |       |                                  |
| `purchase_ok`                               | Purchase                                 | `boolean`               |     |       |                                  |
| `purchase_order_line_ids`                   | PO Lines                                 | `one2many`              |     | ✅    | purchase.order.line              |
| `putaway_rule_ids`                          | Putaway Rules                            | `one2many`              |     | ✅    | stock.putaway.rule               |
| `qty_available`                             | Quantity On Hand                         | `float`                 |     |       |                                  |
| `rating_avg`                                | Average Rating                           | `float`                 |     |       |                                  |
| `rating_avg_text`                           | Rating Avg Text                          | `selection`             |     |       |                                  |
| `rating_count`                              | Rating count                             | `integer`               |     |       |                                  |
| `rating_ids`                                | Ratings                                  | `one2many`              |     | ✅    | rating.rating                    |
| `rating_last_feedback`                      | Rating Last Feedback                     | `text`                  |     |       |                                  |
| `rating_last_image`                         | Rating Last Image                        | `binary`                |     |       |                                  |
| `rating_last_text`                          | Rating Text                              | `selection`             |     |       |                                  |
| `rating_last_value`                         | Rating Last Value                        | `float`                 |     |       |                                  |
| `rating_percentage_satisfaction`            | Rating Satisfaction                      | `float`                 |     |       |                                  |
| `reordering_max_qty`                        | Reordering Max Qty                       | `float`                 |     |       |                                  |
| `reordering_min_qty`                        | Reordering Min Qty                       | `float`                 |     |       |                                  |
| `responsible_id`                            | Responsible                              | `many2one`              |     |       | res.users                        |
| `route_from_categ_ids`                      | Category Routes                          | `many2many`             |     |       | stock.route                      |
| `route_ids`                                 | Routes                                   | `many2many`             |     |       | stock.route                      |
| `sale_delay`                                | Customer Lead Time                       | `integer`               |     |       |                                  |
| `sale_line_warn_msg`                        | Sales Order Line Warning                 | `text`                  |     |       |                                  |
| `sale_ok`                                   | Sales                                    | `boolean`               |     |       |                                  |
| `sales_count`                               | Sold                                     | `float`                 |     |       |                                  |
| `seller_ids`                                | Vendors                                  | `one2many`              |     |       | product.supplierinfo             |
| `seo_name`                                  | Seo name                                 | `char`                  |     |       |                                  |
| `sequence`                                  | Sequence                                 | `integer`               |     |       |                                  |
| `serial_prefix_format`                      | Custom Lot/Serial                        | `char`                  |     |       |                                  |
| `service_to_purchase`                       | Subcontract Service                      | `boolean`               |     |       |                                  |
| `service_tracking`                          | Create on Order                          | `selection`             | ✅  |       |                                  |
| `service_type`                              | Track Service                            | `selection`             |     |       |                                  |
| `show_availability`                         | Show availability Qty                    | `boolean`               |     |       |                                  |
| `show_forecasted_qty_status_button`         | Show Forecasted Qty Status Button        | `boolean`               |     |       |                                  |
| `show_on_hand_qty_status_button`            | Show On Hand Qty Status Button           | `boolean`               |     |       |                                  |
| `show_qty_update_button`                    | Show Qty Update Button                   | `boolean`               |     |       |                                  |
| `standard_price`                            | Cost                                     | `float`                 |     | ✅    |                                  |
| `standard_price_update_warning`             | Standard Price Update Warning            | `char`                  |     |       |                                  |
| `stock_move_ids`                            | Stock Move                               | `one2many`              |     | ✅    | stock.move                       |
| `stock_notification_partner_ids`            | Back in stock Notifications              | `many2many`             |     | ✅    | res.partner                      |
| `stock_quant_ids`                           | Stock Quant                              | `one2many`              |     | ✅    | stock.quant                      |
| `storage_category_capacity_ids`             | Storage Category Capacity                | `one2many`              |     | ✅    | stock.storage.category.capacity  |
| `suggested_qty`                             | Suggested Qty                            | `integer`               |     |       |                                  |
| `suggest_estimated_price`                   | Suggest Estimated Price                  | `float`                 |     |       |                                  |
| `supplier_taxes_id`                         | Purchase Taxes                           | `many2many`             |     |       | account.tax                      |
| `taxes_id`                                  | Sales Taxes                              | `many2many`             |     |       | account.tax                      |
| `tax_string`                                | Tax String                               | `char`                  |     |       |                                  |
| `total_value`                               | Total Value                              | `monetary`              |     |       |                                  |
| `tracking`                                  | Tracking                                 | `selection`             | ✅  |       |                                  |
| `type`                                      | Product Type                             | `selection`             | ✅  |       |                                  |
| `uom_id`                                    | Unit                                     | `many2one`              | ✅  |       | uom.uom                          |
| `uom_ids`                                   | Packagings                               | `many2many`             |     |       | uom.uom                          |
| `uom_name`                                  | Unit Name                                | `char`                  |     |       |                                  |
| `valid_ean`                                 | Barcode is valid EAN                     | `boolean`               |     |       |                                  |
| `valid_product_template_attribute_line_ids` | Valid Product Attribute Lines            | `many2many`             |     |       | product.template.attribute.line  |
| `valuation`                                 | Valuation                                | `selection`             |     |       |                                  |
| `variant_ribbon_id`                         | Variant Ribbon                           | `many2one`              |     | ✅    | product.ribbon                   |
| `variants_default_code`                     | Variants Default Code                    | `char`                  |     |       |                                  |
| `variant_seller_ids`                        | Variant Seller                           | `one2many`              |     |       | product.supplierinfo             |
| `virtual_available`                         | Forecasted Quantity                      | `float`                 |     |       |                                  |
| `visible_expense_policy`                    | Re-Invoice Policy visible                | `boolean`               |     |       |                                  |
| `volume`                                    | Volume                                   | `float`                 |     | ✅    |                                  |
| `volume_uom_name`                           | Volume unit of measure label             | `char`                  |     |       |                                  |
| `warehouse_id`                              | Warehouse                                | `many2one`              |     |       | stock.warehouse                  |
| `website_absolute_url`                      | Website Absolute URL                     | `char`                  |     |       |                                  |
| `website_description`                       | Description for the website              | `html`                  |     |       |                                  |
| `website_id`                                | Website                                  | `many2one`              |     |       | website                          |
| `website_message_ids`                       | Website Messages                         | `one2many`              |     | ✅    | mail.message                     |
| `website_meta_description`                  | Website meta description                 | `text`                  |     |       |                                  |
| `website_meta_keywords`                     | Website meta keywords                    | `char`                  |     |       |                                  |
| `website_meta_og_img`                       | Website opengraph image                  | `char`                  |     |       |                                  |
| `website_meta_title`                        | Website meta title                       | `char`                  |     |       |                                  |
| `website_published`                         | Visible on current website               | `boolean`               |     |       |                                  |
| `website_ribbon_id`                         | Ribbon                                   | `many2one`              |     |       | product.ribbon                   |
| `website_sequence`                          | Website Sequence                         | `integer`               |     |       |                                  |
| `website_size_x`                            | Size X                                   | `integer`               |     |       |                                  |
| `website_size_y`                            | Size Y                                   | `integer`               |     |       |                                  |
| `website_url`                               | Website URL                              | `char`                  |     |       |                                  |
| `weight`                                    | Weight                                   | `float`                 |     | ✅    |                                  |
| `weight_uom_name`                           | Weight unit of measure label             | `char`                  |     |       |                                  |
| `write_date`                                | Write Date                               | `datetime`              |     | ✅    |                                  |
| `write_uid`                                 | Last Updated by                          | `many2one`              |     | ✅    | res.users                        |

**Access Rights:**

| Name                          | Group             | Perms     |
| ----------------------------- | ----------------- | --------- |
| product.product.purchase.user | Purchase / User   | `R`       |
| product.product manager       | Products / Create | `R/W/C/D` |
| product_product_stock_user    | Inventory / User  | `R`       |
| product.product.account.user  | Auditor           | `R`       |
| product.product.public        | Role / Portal     | `R`       |
| product.product.public        | Role / Public     | `R`       |
| product.product employee      | Role / User       | `R`       |
| product.product.public        | Role / User       | `R`       |

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

### 🗃️ `account.tax` — Tax

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                               | Label                             | Type        | Req | Store | Relation                     |
| ----------------------------------- | --------------------------------- | ----------- | --- | ----- | ---------------------------- |
| `active`                            | Active                            | `boolean`   |     | ✅    |                              |
| `amount`                            | Amount                            | `float`     | ✅  | ✅    |                              |
| `amount_type`                       | Tax Computation                   | `selection` | ✅  | ✅    |                              |
| `analytic`                          | Include in Analytic Cost          | `boolean`   |     | ✅    |                              |
| `cash_basis_transition_account_id`  | Cash Basis Transition Account     | `many2one`  |     | ✅    | account.account              |
| `children_tax_ids`                  | Children Taxes                    | `many2many` |     | ✅    | account.tax                  |
| `company_id`                        | Company                           | `many2one`  | ✅  | ✅    | res.company                  |
| `company_price_include`             | Default Sales Price Include       | `selection` |     |       |                              |
| `country_code`                      | Country Code                      | `char`      |     |       |                              |
| `country_id`                        | Country                           | `many2one`  | ✅  | ✅    | res.country                  |
| `create_date`                       | Created on                        | `datetime`  |     | ✅    |                              |
| `create_uid`                        | Created by                        | `many2one`  |     | ✅    | res.users                    |
| `description`                       | Description                       | `html`      |     | ✅    |                              |
| `display_alternative_taxes_field`   | Display Alternative Taxes Field   | `boolean`   |     |       |                              |
| `display_name`                      | Display Name                      | `char`      |     |       |                              |
| `fiscal_position_ids`               | Fiscal Position                   | `many2many` |     | ✅    | account.fiscal.position      |
| `has_message`                       | Has Message                       | `boolean`   |     |       |                              |
| `has_negative_factor`               | Has Negative Factor               | `boolean`   |     |       |                              |
| `hide_tax_exigibility`              | Hide Use Cash Basis Option        | `boolean`   |     |       |                              |
| `id`                                | ID                                | `integer`   |     | ✅    |                              |
| `include_base_amount`               | Affect Base of Subsequent Taxes   | `boolean`   |     | ✅    |                              |
| `invoice_label`                     | Label on Invoices                 | `char`      |     | ✅    |                              |
| `invoice_legal_notes`               | Legal Notes                       | `html`      |     | ✅    |                              |
| `invoice_repartition_line_ids`      | Distribution for Invoices         | `one2many`  |     | ✅    | account.tax.repartition.line |
| `is_base_affected`                  | Base Affected by Previous Taxes   | `boolean`   |     | ✅    |                              |
| `is_domestic`                       | Is Domestic                       | `boolean`   |     | ✅    |                              |
| `is_used`                           | Tax used                          | `boolean`   |     |       |                              |
| `message_attachment_count`          | Attachment Count                  | `integer`   |     |       |                              |
| `message_follower_ids`              | Followers                         | `one2many`  |     | ✅    | mail.followers               |
| `message_has_error`                 | Message Delivery error            | `boolean`   |     |       |                              |
| `message_has_error_counter`         | Number of errors                  | `integer`   |     |       |                              |
| `message_has_sms_error`             | SMS Delivery error                | `boolean`   |     |       |                              |
| `message_ids`                       | Messages                          | `one2many`  |     | ✅    | mail.message                 |
| `message_is_follower`               | Is Follower                       | `boolean`   |     |       |                              |
| `message_needaction`                | Action Needed                     | `boolean`   |     |       |                              |
| `message_needaction_counter`        | Number of Actions                 | `integer`   |     |       |                              |
| `message_partner_ids`               | Followers (Partners)              | `many2many` |     |       | res.partner                  |
| `name`                              | Tax Name                          | `char`      | ✅  | ✅    |                              |
| `original_tax_ids`                  | Replaces                          | `many2many` |     | ✅    | account.tax                  |
| `price_include`                     | Price Include                     | `boolean`   |     |       |                              |
| `price_include_override`            | Included in Price                 | `selection` |     | ✅    |                              |
| `rating_ids`                        | Ratings                           | `one2many`  |     | ✅    | rating.rating                |
| `refund_repartition_line_ids`       | Distribution for Refund Invoices  | `one2many`  |     | ✅    | account.tax.repartition.line |
| `repartition_line_ids`              | Distribution                      | `one2many`  |     | ✅    | account.tax.repartition.line |
| `repartition_lines_str`             | Repartition Lines                 | `char`      |     |       |                              |
| `replacing_tax_ids`                 | Replaced by                       | `many2many` |     | ✅    | account.tax                  |
| `sequence`                          | Sequence                          | `integer`   | ✅  | ✅    |                              |
| `tax_exigibility`                   | Tax Exigibility                   | `selection` |     | ✅    |                              |
| `tax_group_id`                      | Tax Group                         | `many2one`  | ✅  | ✅    | account.tax.group            |
| `tax_label`                         | Tax Label                         | `char`      |     |       |                              |
| `tax_scope`                         | Tax Scope                         | `selection` |     | ✅    |                              |
| `type_tax_use`                      | Tax Type                          | `selection` | ✅  | ✅    |                              |
| `ubl_cii_requires_exemption_reason` | Ubl Cii Requires Exemption Reason | `boolean`   |     |       |                              |
| `ubl_cii_tax_category_code`         | Tax Category Code                 | `selection` |     | ✅    |                              |
| `ubl_cii_tax_exemption_reason_code` | Tax Exemption Reason Code         | `selection` |     | ✅    |                              |
| `website_message_ids`               | Website Messages                  | `one2many`  |     | ✅    | mail.message                 |
| `write_date`                        | Last Updated on                   | `datetime`  |     | ✅    |                              |
| `write_uid`                         | Last Updated by                   | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                      | Group                            | Perms     |
| ------------------------- | -------------------------------- | --------- |
| account.tax.user          | Sales / User: Own Documents Only | `R`       |
| account.tax               | Accounting / Invoicing           | `R`       |
| account.tax               | Accounting / Advisor             | `R/W/C/D` |
| account.tax               | Purchase / User                  | `R`       |
| account.tax               | Purchase / Administrator         | `R`       |
| account.tax               | Auditor                          | `R`       |
| account.tax               | Role / Public                    | `R`       |
| account.tax internal user | Role / User                      | `R`       |

**Record Rules:**

- **Tax multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'parent_of', company_ids)]`

### 🗃️ `account.analytic.applicability` — Analytic Plan's Applicabilities

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                       | Type        | Req | Store | Relation              |
| ---------------------------- | --------------------------- | ----------- | --- | ----- | --------------------- |
| `account_prefix`             | Financial Accounts Prefixes | `char`      |     | ✅    |                       |
| `account_prefix_placeholder` | Account Prefix Placeholder  | `char`      |     |       |                       |
| `analytic_plan_id`           | Analytic Plan               | `many2one`  |     | ✅    | account.analytic.plan |
| `applicability`              | Applicability               | `selection` | ✅  | ✅    |                       |
| `business_domain`            | Domain                      | `selection` | ✅  | ✅    |                       |
| `company_id`                 | Company                     | `many2one`  |     | ✅    | res.company           |
| `create_date`                | Created on                  | `datetime`  |     | ✅    |                       |
| `create_uid`                 | Created by                  | `many2one`  |     | ✅    | res.users             |
| `display_account_prefix`     | Display Account Prefix      | `boolean`   |     |       |                       |
| `display_name`               | Display Name                | `char`      |     |       |                       |
| `id`                         | ID                          | `integer`   |     | ✅    |                       |
| `product_categ_id`           | Product Category            | `many2one`  |     | ✅    | product.category      |
| `write_date`                 | Last Updated on             | `datetime`  |     | ✅    |                       |
| `write_uid`                  | Last Updated by             | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                                      | Group                | Perms     |
| ----------------------------------------- | -------------------- | --------- |
| account.analytic.applicability accountant | Contact / Accountant | `R/W/C/D` |
| access_account_analytic_applicability     | Analytic Accounting  | `R/W/C/D` |

**Record Rules:**

- **Analytic applicability multi company rule** (Global) `R/W/C/D`
  - Domain: `['|',('company_id','=',False),('company_id', 'parent_of', company_ids)]`

### 🗃️ `bill.to.po.wizard` — Bill to Purchase Order

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field               | Label           | Type       | Req | Store | Relation       |
| ------------------- | --------------- | ---------- | --- | ----- | -------------- |
| `create_date`       | Created on      | `datetime` |     | ✅    |                |
| `create_uid`        | Created by      | `many2one` |     | ✅    | res.users      |
| `display_name`      | Display Name    | `char`     |     |       |                |
| `id`                | ID              | `integer`  |     | ✅    |                |
| `partner_id`        | Partner         | `many2one` |     | ✅    | res.partner    |
| `purchase_order_id` | Purchase Order  | `many2one` |     | ✅    | purchase.order |
| `write_date`        | Last Updated on | `datetime` |     | ✅    |                |
| `write_uid`         | Last Updated by | `many2one` |     | ✅    | res.users      |

**Access Rights:**

| Name                   | Group           | Perms   |
| ---------------------- | --------------- | ------- |
| bill.to.po.wizard user | Purchase / User | `R/W/C` |

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

### 🗃️ `purchase.bill.line.match` — Purchase Line and Vendor Bill line matching view

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label                   | Type       | Req | Store | Relation            |
| ------------------------- | ----------------------- | ---------- | --- | ----- | ------------------- |
| `account_move_id`         | Account Move            | `many2one` |     | ✅    | account.move        |
| `aml_id`                  | Aml                     | `many2one` |     | ✅    | account.move.line   |
| `billed_amount_untaxed`   | Billed Amount Untaxed   | `monetary` |     |       |                     |
| `company_id`              | Company                 | `many2one` |     | ✅    | res.company         |
| `currency_id`             | Currency                | `many2one` |     | ✅    | res.currency        |
| `display_name`            | Display Name            | `char`     |     |       |                     |
| `id`                      | ID                      | `integer`  |     | ✅    |                     |
| `line_amount_untaxed`     | Line Amount Untaxed     | `monetary` |     | ✅    |                     |
| `line_qty`                | Line Qty                | `float`    |     | ✅    |                     |
| `line_uom_id`             | Line Uom                | `many2one` |     | ✅    | uom.uom             |
| `partner_id`              | Partner                 | `many2one` |     | ✅    | res.partner         |
| `pol_id`                  | Pol                     | `many2one` |     | ✅    | purchase.order.line |
| `product_id`              | Product                 | `many2one` |     | ✅    | product.product     |
| `product_uom_id`          | Unit                    | `many2one` |     |       | uom.uom             |
| `product_uom_price`       | Product Uom Price       | `float`    |     |       |                     |
| `product_uom_qty`         | Product Uom Qty         | `float`    |     |       |                     |
| `purchase_amount_untaxed` | Purchase Amount Untaxed | `monetary` |     |       |                     |
| `purchase_order_id`       | Purchase Order          | `many2one` |     | ✅    | purchase.order      |
| `qty_invoiced`            | Qty Invoiced            | `float`    |     | ✅    |                     |
| `qty_to_invoice`          | Qty to invoice          | `float`    |     | ✅    |                     |
| `reference`               | Reference               | `char`     |     |       |                     |
| `state`                   | State                   | `char`     |     | ✅    |                     |

**Access Rights:**

| Name                              | Group                  | Perms |
| --------------------------------- | ---------------------- | ----- |
| purchase.bill.line.match invoice  | Accounting / Invoicing | `R/W` |
| purchase.bill.line.match user     | Purchase / User        | `R`   |
| purchase.bill.line.match readonly | Auditor                | `R`   |

### 🗃️ `purchase.order.line` — Purchase Order Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                    | Label                                                | Type        | Req | Store | Relation                         |
| ---------------------------------------- | ---------------------------------------------------- | ----------- | --- | ----- | -------------------------------- |
| `allowed_uom_ids`                        | Allowed Uom                                          | `many2many` |     |       | uom.uom                          |
| `amount_to_invoice_at_date`              | Amount                                               | `float`     |     |       |                                  |
| `analytic_distribution`                  | Analytic Distribution                                | `json`      |     | ✅    |                                  |
| `analytic_precision`                     | Analytic Precision                                   | `integer`   |     |       |                                  |
| `company_id`                             | Company                                              | `many2one`  |     | ✅    | res.company                      |
| `create_date`                            | Created on                                           | `datetime`  |     | ✅    |                                  |
| `create_uid`                             | Created by                                           | `many2one`  |     | ✅    | res.users                        |
| `currency_id`                            | Currency                                             | `many2one`  |     |       | res.currency                     |
| `date_approve`                           | Confirmation Date                                    | `datetime`  |     |       |                                  |
| `date_order`                             | Order Date                                           | `datetime`  |     |       |                                  |
| `date_planned`                           | Expected Arrival                                     | `datetime`  |     | ✅    |                                  |
| `discount`                               | Discount (%)                                         | `float`     |     | ✅    |                                  |
| `display_name`                           | Display Name                                         | `char`      |     |       |                                  |
| `display_type`                           | Display Type                                         | `selection` |     | ✅    |                                  |
| `distribution_analytic_account_ids`      | Distribution Analytic Account                        | `many2many` |     |       | account.analytic.account         |
| `forecasted_issue`                       | Forecasted Issue                                     | `boolean`   |     |       |                                  |
| `id`                                     | ID                                                   | `integer`   |     | ✅    |                                  |
| `invoice_lines`                          | Bill Lines                                           | `one2many`  |     | ✅    | account.move.line                |
| `is_downpayment`                         | Is Downpayment                                       | `boolean`   |     | ✅    |                                  |
| `is_storable`                            | Track Inventory                                      | `boolean`   |     |       |                                  |
| `location_final_id`                      | Location from procurement                            | `many2one`  |     | ✅    | stock.location                   |
| `move_dest_ids`                          | Downstream moves alt                                 | `many2many` |     | ✅    | stock.move                       |
| `move_ids`                               | Reservation                                          | `one2many`  |     | ✅    | stock.move                       |
| `name`                                   | Description                                          | `text`      | ✅  | ✅    |                                  |
| `order_id`                               | Order Reference                                      | `many2one`  | ✅  | ✅    | purchase.order                   |
| `orderpoint_id`                          | Orderpoint                                           | `many2one`  |     | ✅    | stock.warehouse.orderpoint       |
| `parent_id`                              | Parent Section Line                                  | `many2one`  |     |       | purchase.order.line              |
| `partner_id`                             | Partner                                              | `many2one`  |     | ✅    | res.partner                      |
| `price_subtotal`                         | Subtotal                                             | `monetary`  |     | ✅    |                                  |
| `price_tax`                              | Tax                                                  | `float`     |     | ✅    |                                  |
| `price_total`                            | Total                                                | `monetary`  |     | ✅    |                                  |
| `price_unit`                             | Unit Price                                           | `float`     | ✅  | ✅    |                                  |
| `price_unit_discounted`                  | Unit Price (Discounted)                              | `float`     |     |       |                                  |
| `price_unit_product_uom`                 | Unit Price Product UoM                               | `float`     |     |       |                                  |
| `product_description_variants`           | Custom Description                                   | `char`      |     | ✅    |                                  |
| `product_id`                             | Product                                              | `many2one`  |     | ✅    | product.product                  |
| `product_no_variant_attribute_value_ids` | Product attribute values that do not create variants | `many2many` |     | ✅    | product.template.attribute.value |
| `product_qty`                            | Quantity                                             | `float`     | ✅  | ✅    |                                  |
| `product_template_attribute_value_ids`   | Attribute Values                                     | `many2many` |     |       | product.template.attribute.value |
| `product_type`                           | Product Type                                         | `selection` |     |       |                                  |
| `product_uom_id`                         | Unit                                                 | `many2one`  |     | ✅    | uom.uom                          |
| `product_uom_qty`                        | Total Quantity                                       | `float`     |     | ✅    |                                  |
| `propagate_cancel`                       | Propagate cancellation                               | `boolean`   |     | ✅    |                                  |
| `purchase_line_warn_msg`                 | Purchase Line Warn Msg                               | `text`      |     |       |                                  |
| `qty_invoiced`                           | Billed Qty                                           | `float`     |     | ✅    |                                  |
| `qty_invoiced_at_date`                   | Billed                                               | `float`     |     |       |                                  |
| `qty_received`                           | Received Qty                                         | `float`     |     | ✅    |                                  |
| `qty_received_at_date`                   | Received                                             | `float`     |     |       |                                  |
| `qty_received_manual`                    | Manual Received Qty                                  | `float`     |     | ✅    |                                  |
| `qty_received_method`                    | Received Qty Method                                  | `selection` |     | ✅    |                                  |
| `qty_to_invoice`                         | To Invoice Quantity                                  | `float`     |     | ✅    |                                  |
| `sale_line_id`                           | Origin Sale Item                                     | `many2one`  |     | ✅    | sale.order.line                  |
| `sale_order_id`                          | Sale Order                                           | `many2one`  |     |       | sale.order                       |
| `selected_seller_id`                     | Selected Seller                                      | `many2one`  |     |       | product.supplierinfo             |
| `sequence`                               | Sequence                                             | `integer`   |     | ✅    |                                  |
| `state`                                  | Status                                               | `selection` |     |       |                                  |
| `tax_calculation_rounding_method`        | Tax calculation rounding method                      | `selection` |     |       |                                  |
| `tax_ids`                                | Taxes                                                | `many2many` |     | ✅    | account.tax                      |
| `technical_price_unit`                   | Technical Price Unit                                 | `float`     |     | ✅    |                                  |
| `translated_product_name`                | Translated Product Name                              | `text`      |     |       |                                  |
| `write_date`                             | Last Updated on                                      | `datetime`  |     | ✅    |                                  |
| `write_uid`                              | Last Updated by                                      | `many2one`  |     | ✅    | res.users                        |

**Access Rights:**

| Name                       | Group                    | Perms     |
| -------------------------- | ------------------------ | --------- |
| purchase.order.line        | Accounting / Invoicing   | `R/W`     |
| purchase.order.line user   | Purchase / User          | `R/W/C/D` |
| purchase.order.line        | Purchase / Administrator | `R/W/C/D` |
| purchase.order.line        | Inventory / User         | `R`       |
| purchase.order.line        | Auditor                  | `R`       |
| purchase.order.line.portal | Role / Portal            | `R`       |

**Record Rules:**

- **Purchase Order Line multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`
- **Portal Purchase Order Lines** (10) `R/W/C/D`
  - Domain: `[('order_id.partner_id','child_of',[user.commercial_partner_id.id])]`

### 🗃️ `purchase.report` — Purchase Report

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                   | Label                     | Type        | Req | Store | Relation                |
| ----------------------- | ------------------------- | ----------- | --- | ----- | ----------------------- |
| `category_id`           | Product Category          | `many2one`  |     | ✅    | product.category        |
| `commercial_partner_id` | Commercial Entity         | `many2one`  |     | ✅    | res.partner             |
| `company_id`            | Company                   | `many2one`  |     | ✅    | res.company             |
| `country_id`            | Partner Country           | `many2one`  |     | ✅    | res.country             |
| `currency_id`           | Currency                  | `many2one`  |     | ✅    | res.currency            |
| `date_approve`          | Confirmation Date         | `datetime`  |     | ✅    |                         |
| `date_order`            | Order Date                | `datetime`  |     | ✅    |                         |
| `days_to_arrival`       | Effective Days To Arrival | `float`     |     | ✅    |                         |
| `delay`                 | Days to Confirm           | `float`     |     | ✅    |                         |
| `delay_pass`            | Days to Receive           | `float`     |     | ✅    |                         |
| `display_name`          | Display Name              | `char`      |     |       |                         |
| `effective_date`        | Effective Date            | `datetime`  |     | ✅    |                         |
| `fiscal_position_id`    | Fiscal Position           | `many2one`  |     | ✅    | account.fiscal.position |
| `id`                    | ID                        | `integer`   |     | ✅    |                         |
| `nbr_lines`             | # of Lines                | `integer`   |     | ✅    |                         |
| `order_id`              | Order                     | `many2one`  |     | ✅    | purchase.order          |
| `partner_id`            | Vendor                    | `many2one`  |     | ✅    | res.partner             |
| `picking_type_id`       | Warehouse                 | `many2one`  |     | ✅    | stock.warehouse         |
| `price_average`         | Average Cost              | `monetary`  |     | ✅    |                         |
| `price_total`           | Total                     | `monetary`  |     | ✅    |                         |
| `product_id`            | Product                   | `many2one`  |     | ✅    | product.product         |
| `product_tmpl_id`       | Product Template          | `many2one`  |     | ✅    | product.template        |
| `product_uom_id`        | Reference Unit of Measure | `many2one`  |     | ✅    | uom.uom                 |
| `qty_billed`            | Qty Billed                | `float`     |     | ✅    |                         |
| `qty_ordered`           | Qty Ordered               | `float`     |     | ✅    |                         |
| `qty_received`          | Qty Received              | `float`     |     | ✅    |                         |
| `qty_to_be_billed`      | Qty to be Billed          | `float`     |     | ✅    |                         |
| `state`                 | Status                    | `selection` |     | ✅    |                         |
| `untaxed_total`         | Untaxed Total             | `monetary`  |     | ✅    |                         |
| `user_id`               | Buyer                     | `many2one`  |     | ✅    | res.users               |
| `volume`                | Volume                    | `float`     |     | ✅    |                         |
| `weight`                | Gross Weight              | `float`     |     | ✅    |                         |

**Access Rights:**

| Name                       | Group                    | Perms |
| -------------------------- | ------------------------ | ----- |
| purchase.stock.report user | Purchase / User          | `R`   |
| purchase.stock.report      | Purchase / Administrator | `R`   |

**Record Rules:**

- **Purchase Order Report multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`

### 🗃️ `purchase.bill.union` — Purchases & Bills Union

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label          | Type       | Req | Store | Relation       |
| ------------------- | -------------- | ---------- | --- | ----- | -------------- |
| `amount`            | Amount         | `float`    |     | ✅    |                |
| `company_id`        | Company        | `many2one` |     | ✅    | res.company    |
| `currency_id`       | Currency       | `many2one` |     | ✅    | res.currency   |
| `date`              | Date           | `date`     |     | ✅    |                |
| `display_name`      | Display Name   | `char`     |     |       |                |
| `id`                | ID             | `integer`  |     | ✅    |                |
| `name`              | Reference      | `char`     |     | ✅    |                |
| `partner_id`        | Vendor         | `many2one` |     | ✅    | res.partner    |
| `purchase_order_id` | Purchase Order | `many2one` |     | ✅    | purchase.order |
| `reference`         | Source         | `char`     |     | ✅    |                |
| `vendor_bill_id`    | Vendor Bill    | `many2one` |     | ✅    | account.move   |

**Access Rights:**

| Name                       | Group           | Perms |
| -------------------------- | --------------- | ----- |
| access_purchase_bill_union | Purchase / User | `R`   |

**Record Rules:**

- **Purchases & Bills Union multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

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

### 🗃️ `product.supplierinfo` — Supplier Pricelist

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label                    | Type       | Req | Store | Relation         |
| -------------------------- | ------------------------ | ---------- | --- | ----- | ---------------- |
| `company_id`               | Company                  | `many2one` |     | ✅    | res.company      |
| `create_date`              | Created on               | `datetime` |     | ✅    |                  |
| `create_uid`               | Created by               | `many2one` |     | ✅    | res.users        |
| `currency_id`              | Currency                 | `many2one` | ✅  | ✅    | res.currency     |
| `date_end`                 | End Date                 | `date`     |     | ✅    |                  |
| `date_start`               | Start Date               | `date`     |     | ✅    |                  |
| `delay`                    | Lead Time                | `integer`  | ✅  | ✅    |                  |
| `discount`                 | Discount (%)             | `float`    |     | ✅    |                  |
| `display_name`             | Display Name             | `char`     |     |       |                  |
| `id`                       | ID                       | `integer`  |     | ✅    |                  |
| `last_purchase_date`       | Last Purchase            | `date`     |     |       |                  |
| `min_qty`                  | Quantity                 | `float`    | ✅  | ✅    |                  |
| `partner_id`               | Vendor                   | `many2one` | ✅  | ✅    | res.partner      |
| `price`                    | Unit Price               | `float`    |     | ✅    |                  |
| `price_discounted`         | Discounted Price         | `float`    |     |       |                  |
| `product_code`             | Vendor Product Code      | `char`     |     | ✅    |                  |
| `product_id`               | Product Variant          | `many2one` |     | ✅    | product.product  |
| `product_name`             | Vendor Product Name      | `char`     |     | ✅    |                  |
| `product_tmpl_id`          | Product Template         | `many2one` | ✅  | ✅    | product.template |
| `product_uom_id`           | Unit                     | `many2one` | ✅  | ✅    | uom.uom          |
| `product_variant_count`    | Variant Count            | `integer`  |     |       |                  |
| `sequence`                 | Sequence                 | `integer`  |     | ✅    |                  |
| `show_set_supplier_button` | Show Set Supplier Button | `boolean`  |     |       |                  |
| `write_date`               | Last Updated on          | `datetime` |     | ✅    |                  |
| `write_uid`                | Last Updated by          | `many2one` |     | ✅    | res.users        |

**Access Rights:**

| Name                                  | Group                    | Perms     |
| ------------------------------------- | ------------------------ | --------- |
| product.supplierinfo purchase_manager | Purchase / Administrator | `R/W/C/D` |
| product.supplierinfo.manager          | Products / Create        | `R/W/C/D` |
| product.supplierinfo.user             | Role / User              | `R`       |

**Record Rules:**

- **product supplierinfo company rule** (Global) `R/W/C/D`
  - Domain:
    `['|', ('company_id', '=', False), ('company_id', 'parent_of', company_ids)]`
