---
title: "Invoicing"
module: "account"
state: "installed"
version: "19.0.1.4"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/app/invoicing"
license: "LGPL-3"
category: "Accounting"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/__________, odoo/app]
---

# 🟢 Invoicing

> **Module:** `account` | **Version:** `19.0.1.4` **Category:** Accounting |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:**
> https://www.odoo.com/app/invoicing

## 🔗 Dependencies

[[base_setup]] [[onboarding]] [[product]] [[analytic]] [[portal]] [[digest]]

## 📖 Description

# Invoicing & Payments

The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your
accounting, even when you are not an accountant. It provides an easy way to follow up on
your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to
keep your books, and you still want to keep track of payments. This module also offers
you an easy method of registering payments, without having to encode complete abstracts
of account.

## 🖥️ UI Components

### Menus

- `Invoicing`
- `Invoicing/Accounting`
- `Invoicing/Accounting/Closing`
- `Invoicing/Accounting/Closing/Secure Entries`
- `Invoicing/Accounting/Transactions`
- `Invoicing/Accounting/Transactions/Analytic Items`
- `Invoicing/Accounting/Transactions/Journal Entries`
- `Invoicing/Configuration`
- `Invoicing/Configuration/Accounting`
- `Invoicing/Configuration/Accounting/Cash Roundings`
- `Invoicing/Configuration/Accounting/Chart of Accounts`
- `Invoicing/Configuration/Accounting/Currencies`
- `Invoicing/Configuration/Accounting/Fiscal Positions`
- `Invoicing/Configuration/Accounting/Journals`
- `Invoicing/Configuration/Accounting/Multi-Ledger`
- `Invoicing/Configuration/Accounting/Reporting`
- `Invoicing/Configuration/Accounting/Tax Groups`
- `Invoicing/Configuration/Accounting/Taxes`
- `Invoicing/Configuration/Analytic Accounting`
- `Invoicing/Configuration/Analytic Accounting/Analytic Accounts`
- `Invoicing/Configuration/Analytic Accounting/Analytic Distribution Models`
- `Invoicing/Configuration/Analytic Accounting/Analytic Plans`
- `Invoicing/Configuration/Invoicing`
- `Invoicing/Configuration/Invoicing/Incoterms`
- `Invoicing/Configuration/Invoicing/Payment Terms`
- `Invoicing/Configuration/Invoicing/Product Categories`
- `Invoicing/Configuration/Online Payments`
- `Invoicing/Configuration/Settings`
- `Invoicing/Customers`
- `Invoicing/Customers/Credit Notes`
- `Invoicing/Customers/Customers`
- `Invoicing/Customers/Invoices`
- `Invoicing/Customers/Payments`
- `Invoicing/Customers/Products`
- `Invoicing/Dashboard`
- `Invoicing/Reporting`
- `Invoicing/Reporting/Management`
- `Invoicing/Reporting/Management/Analytic Report`
- `Invoicing/Reporting/Management/Invoice Analysis`
- `Invoicing/Reporting/Partner Reports`
- `Invoicing/Reporting/Statement Reports`
- `Invoicing/Reporting/Taxes & Fiscal`
- `Invoicing/Review`
- `Invoicing/Review/Control`
- `Invoicing/Review/Control/Journal Items`
- `Invoicing/Review/Logs`
- `Invoicing/Review/Logs/Audit Trail`
- `Invoicing/Vendors`
- `Invoicing/Vendors/Bills`
- `Invoicing/Vendors/Payments`
- `Invoicing/Vendors/Products`
- `Invoicing/Vendors/Refunds`
- `Invoicing/Vendors/Vendors`

### Views

- `* INHERIT Document Layout (form)`
- `* INHERIT Invoice/Bill (qweb)`
- `* INHERIT Invoices / Bills (qweb)`
- `* INHERIT Portal layout : invoice menu entries (qweb)`
- `* INHERIT account.analytic.account.form.inherit (form)`
- `* INHERIT account.analytic.account.list.inherit (list)`
- `* INHERIT account.analytic.distribution.model.inherit.form (form)`
- `* INHERIT account.analytic.distribution.model.inherit.list (list)`
- `* INHERIT account.analytic.line.form.inherit.account (form)`
- `* INHERIT account.analytic.line.list.inherit.account (list)`
- `* INHERIT account.analytic.line.pivot (pivot)`
- `* INHERIT account.analytic.line.select.inherit.account (search)`
- `* INHERIT account.analytic.plan.inherit.form (form)`
- `* INHERIT account.duplicated.moves.list.js (list)`
- `* INHERIT account.fiscal.position.tax.list (list)`
- `* INHERIT account.invoice.select (search)`
- `* INHERIT account.move.line.kanban.mobile (kanban)`
- `* INHERIT account.move.line.list.grouped.bank.cash (list)`
- `* INHERIT account.move.line.list.grouped.misc (list)`
- `* INHERIT account.move.line.list.grouped.misc (list)`
- `* INHERIT account.move.line.list.grouped.partner (list)`
- `* INHERIT account.move.line.list.grouped.sales.purchase (list)`
- `* INHERIT account.move.line.tax.audit.list (list)`
- `* INHERIT account.move.list.multi.edit (list)`
- `* INHERIT account.move.with.gaps.in.sequence.filter (search)`
- `* INHERIT account.onboarding.tax.list (list)`
- `* INHERIT account.out.invoice.list (list)`
- `* INHERIT account.out.invoice.list (list)`
- `* INHERIT account.out.invoice.list (list)`
- `* INHERIT account.out.invoice.list (list)`
- `* INHERIT account.out.invoice.list (list)`
- `* INHERIT account.supplier.payment.list (list)`
- `* INHERIT account.supplier.payment.list (list)`
- `* INHERIT digest.digest.view.form.inherit.account.account (form)`
- `* INHERIT document_tax_totals (qweb)`
- `* INHERIT ir.actions.report.form.inherit.account (form)`
- `* INHERIT ir.module.module.list.inherit.account (search)`
- `* INHERIT partner.view.buttons (form)`
- `* INHERIT portal_my_details (qweb)`
- `* INHERIT product.category.property.form.inherit (form)`
- `* INHERIT product.product.view.form.normalized.account.inherit (form)`
- `* INHERIT product.template.form.inherit (form)`
- `* INHERIT product.template.list.purchasable.inherit (list)`
- `* INHERIT product.template.list.sellable.inherit (list)`
- `* INHERIT product.view.search.catalog.inherit.account (search)`
- `* INHERIT product_uom_form_view_inherit (form)`
- `* INHERIT report_invoice_document_preview (qweb)`
- `* INHERIT report_invoice_wizard_preview_inherit_account (qweb)`
- `* INHERIT report_statement_internal_layout (qweb)`
- `* INHERIT res.company.form.inherit.account (form)`
- `* INHERIT res.config.settings.view.form.inherit.account (form)`
- `* INHERIT res.config.settings.view.form.inherit.base_setup (form)`
- `* INHERIT res.country.group.form.inherit.account (form)`
- `* INHERIT res.currency.form.inherit (form)`
- `* INHERIT res.partner.bank.form.inherit.account (form)`
- `* INHERIT res.partner.bank.search.inherit (search)`
- `* INHERIT res.partner.list.inherit.account (list)`
- `* INHERIT res.partner.property.form.inherit (form)`
- `* INHERIT res.partner.search.inherit (search)`
- `Account Terms and Conditions Setting Banner (qweb)`
- `Autopost Bills (form)`
- `Confirm Entries (form)`
- `Invoice error/warning display (qweb)`
- `Invoice success display (qweb)`
- `My Invoices and Payments (qweb)`
- `My journal email notification settings (qweb)`
- `Re-sequence Journal Entries (form)`
- `Tags (form)`
- `Tags (list)`
- `Terms & Conditions (qweb)`
- `account.account.form (form)`
- `account.account.kanban (kanban)`
- `account.account.list (list)`
- `account.account.search (search)`
- `account.accrued.orders.wizard.view (form)`
- `account.automatic.entry.wizard.form (form)`
- `account.bank.statement.graph (graph)`
- `account.bank.statement.list (list)`
- `account.bank.statement.pivot (pivot)`
- `account.bank.statement.search (search)`
- `account.cash.rounding.form (form)`
- `account.cash.rounding.list (list)`
- `account.cash.rounding.search (search)`
- `account.financial.year.op.setup.wizard.form (form)`
- `account.fiscal.position.filter (search)`
- `account.fiscal.position.form (form)`
- `account.fiscal.position.list (list)`
- `account.full.reconcile.form (form)`
- `account.group.form (form)`
- `account.group.list (list)`
- `account.group.search (search)`
- `account.incoterms.form (form)`
- `account.incoterms.list (list)`
- `account.incoterms.search (search)`
- `account.invoice.line.tax.search (list)`
- `account.invoice.list (list)`
- `account.invoice.report.graph (graph)`
- `account.invoice.report.pivot (pivot)`
- `account.invoice.report.search (search)`
- `account.invoice.report.view.list (list)`
- `account.invoice.select (search)`
- `account.journal.dashboard.kanban (kanban)`
- `account.journal.form (form)`
- `account.journal.group.form (form)`
- `account.journal.group.list (list)`
- `account.journal.kanban (kanban)`
- `account.journal.list (list)`
- `account.journal.search (search)`
- `account.lock_exception.form (form)`
- `account.merge.wizard.form (form)`
- `account.move.form (form)`
- `account.move.kanban (kanban)`
- `account.move.line.form (form)`
- `account.move.line.graph (graph)`
- `account.move.line.kanban (kanban)`
- `account.move.line.list (list)`
- `account.move.line.payment.list (list)`
- `account.move.line.payment.search (search)`
- `account.move.line.pivot (pivot)`
- `account.move.line.search (search)`
- `account.move.list (list)`
- `account.move.reversal.form (form)`
- `account.move.select (search)`
- `account.move.send.batch.wizard.form (form)`
- `account.move.send.wizard.form (form)`
- `account.move.view.activity (activity)`
- `account.online.sync.res.partner.bank.setup.form (form)`
- `account.online.sync.res.partner.credit.card.setup.form (form)`
- `account.payment.form (form)`
- `account.payment.graph (graph)`
- `account.payment.kanban (kanban)`
- `account.payment.list (list)`
- `account.payment.method.line.kanban (kanban)`
- `account.payment.method.line.list (list)`
- `account.payment.register.form (form)`
- `account.payment.search (search)`
- `account.payment.term.form (form)`
- `account.payment.term.kanban (kanban)`
- `account.payment.term.list (list)`
- `account.payment.term.search (search)`
- `account.reconcile.model.form (form)`
- `account.reconcile.model.list (list)`
- `account.reconcile.model.search (search)`
- `account.secure.entries.wizard.form (form)`
- `account.setup.opening.move.line.list (list)`
- `account.tag.view.search (search)`
- `account.tax.form (form)`
- `account.tax.group.form (form)`
- `account.tax.group.list (list)`
- `account.tax.group.search.filters (search)`
- `account.tax.kanban (kanban)`
- `account.tax.list (list)`
- `account.tax.repartition.line.list (list)`
- `account.tax.search (search)`
- `account.tax.search.filters (search)`
- `account_default_terms_and_conditions (qweb)`
- `bill_preview (qweb)`
- `document_tax_totals_company_currency_template (qweb)`
- `document_tax_totals_template (qweb)`
- `email_template_mail_gateway_failed (qweb)`
- `mail.message.list.inherit.audit.log (list)`
- `mail.message.search (search)`
- `portal_invoice_required_fields_form (qweb)`
- `report_hash_integrity (qweb)`
- `report_invoice (qweb)`
- `report_invoice_document (qweb)`
- `report_invoice_qr_code_preview (qweb)`
- `report_invoice_with_payments (qweb)`
- `report_invoice_wizard_iframe (qweb)`
- `report_original_vendor_bill (qweb)`
- `report_payment_receipt (qweb)`
- `report_payment_receipt_document (qweb)`
- `report_statement (qweb)`
- `res.company.form.view.onboarding (form)`
- `res.company.form.view.onboarding.sale.tax (form)`
- `res.company.view.form.terms (form)`
- `res.partner.list (list)`
- `tests_shared_js_python (qweb)`

### Reports

- `Hash integrity result PDF`
- `Invoice PDF`
- `Original Bills`
- `PDF without Payment`
- `Payment Receipt`
- `Statement`

## 🛠️ Technical Documentation

**84 model(s) defined by this module:**

### 🗃️ `account.account` — Account

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                          | Type        | Req | Store | Relation             |
| ------------------------------- | ------------------------------ | ----------- | --- | ----- | -------------------- |
| `account_stock_expense_id`      | Expense Account                | `many2one`  |     | ✅    | account.account      |
| `account_stock_variation_id`    | Variation Account              | `many2one`  |     | ✅    | account.account      |
| `account_type`                  | Type                           | `selection` | ✅  | ✅    |                      |
| `active`                        | Active                         | `boolean`   |     | ✅    |                      |
| `activity_calendar_event_id`    | Next Activity Calendar Event   | `many2one`  |     |       | calendar.event       |
| `activity_date_deadline`        | Next Activity Deadline         | `date`      |     |       |                      |
| `activity_exception_decoration` | Activity Exception Decoration  | `selection` |     |       |                      |
| `activity_exception_icon`       | Icon                           | `char`      |     |       |                      |
| `activity_ids`                  | Activities                     | `one2many`  |     | ✅    | mail.activity        |
| `activity_state`                | Activity State                 | `selection` |     |       |                      |
| `activity_summary`              | Next Activity Summary          | `char`      |     |       |                      |
| `activity_type_icon`            | Activity Type Icon             | `char`      |     |       |                      |
| `activity_type_id`              | Next Activity Type             | `many2one`  |     |       | mail.activity.type   |
| `activity_user_id`              | Responsible User               | `many2one`  |     |       | res.users            |
| `code`                          | Code                           | `char`      |     |       |                      |
| `code_mapping_ids`              | Code Mapping                   | `one2many`  |     | ✅    | account.code.mapping |
| `code_store`                    | Code Store                     | `char`      |     | ✅    |                      |
| `company_currency_id`           | Company Currency               | `many2one`  |     |       | res.currency         |
| `company_fiscal_country_code`   | Company Fiscal Country Code    | `char`      |     |       |                      |
| `company_ids`                   | Companies                      | `many2many` | ✅  | ✅    | res.company          |
| `create_date`                   | Created on                     | `datetime`  |     | ✅    |                      |
| `create_uid`                    | Created by                     | `many2one`  |     | ✅    | res.users            |
| `currency_id`                   | Account Currency               | `many2one`  |     | ✅    | res.currency         |
| `current_balance`               | Current Balance                | `float`     |     |       |                      |
| `description`                   | Description                    | `text`      |     | ✅    |                      |
| `display_mapping_tab`           | Display Mapping Tab            | `boolean`   |     |       |                      |
| `display_name`                  | Display Name                   | `char`      |     |       |                      |
| `group_id`                      | Group                          | `many2one`  |     |       | account.group        |
| `has_message`                   | Has Message                    | `boolean`   |     |       |                      |
| `id`                            | ID                             | `integer`   |     | ✅    |                      |
| `include_initial_balance`       | Bring Accounts Balance Forward | `boolean`   |     |       |                      |
| `internal_group`                | Internal Group                 | `selection` |     |       |                      |
| `message_attachment_count`      | Attachment Count               | `integer`   |     |       |                      |
| `message_follower_ids`          | Followers                      | `one2many`  |     | ✅    | mail.followers       |
| `message_has_error`             | Message Delivery error         | `boolean`   |     |       |                      |
| `message_has_error_counter`     | Number of errors               | `integer`   |     |       |                      |
| `message_has_sms_error`         | SMS Delivery error             | `boolean`   |     |       |                      |
| `message_ids`                   | Messages                       | `one2many`  |     | ✅    | mail.message         |
| `message_is_follower`           | Is Follower                    | `boolean`   |     |       |                      |
| `message_needaction`            | Action Needed                  | `boolean`   |     |       |                      |
| `message_needaction_counter`    | Number of Actions              | `integer`   |     |       |                      |
| `message_partner_ids`           | Followers (Partners)           | `many2many` |     |       | res.partner          |
| `my_activity_date_deadline`     | My Activity Deadline           | `date`      |     |       |                      |
| `name`                          | Account Name                   | `char`      | ✅  | ✅    |                      |
| `non_trade`                     | Non Trade                      | `boolean`   |     | ✅    |                      |
| `note`                          | Internal Notes                 | `text`      |     | ✅    |                      |
| `opening_balance`               | Opening Balance                | `monetary`  |     |       |                      |
| `opening_credit`                | Opening Credit                 | `monetary`  |     |       |                      |
| `opening_debit`                 | Opening Debit                  | `monetary`  |     |       |                      |
| `placeholder_code`              | Display code                   | `char`      |     |       |                      |
| `rating_ids`                    | Ratings                        | `one2many`  |     | ✅    | rating.rating        |
| `reconcile`                     | Allow Reconciliation           | `boolean`   |     | ✅    |                      |
| `related_taxes_amount`          | Related Taxes Amount           | `integer`   |     |       |                      |
| `root_id`                       | Root                           | `many2one`  |     |       | account.root         |
| `tag_ids`                       | Tags                           | `many2many` |     | ✅    | account.account.tag  |
| `tax_ids`                       | Default Taxes                  | `many2many` |     | ✅    | account.tax          |
| `used`                          | Used                           | `boolean`   |     |       |                      |
| `website_message_ids`           | Website Messages               | `one2many`  |     | ✅    | mail.message         |
| `write_date`                    | Last Updated on                | `datetime`  |     | ✅    |                      |
| `write_uid`                     | Last Updated by                | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                             | Group                            | Perms     |
| -------------------------------- | -------------------------------- | --------- |
| account_account salesman         | Sales / User: Own Documents Only | `R`       |
| account.account invoice          | Accounting / Invoicing           | `R`       |
| account.account                  | Accounting / Advisor             | `R/W/C/D` |
| account.account purchase manager | Purchase / Administrator         | `R`       |
| account.account partner manager  | Contact / Creation               | `R`       |
| account.account stock manager    | Inventory / Administrator        | `R`       |
| account.account.readonly         | Auditor                          | `R`       |
| account.account user             | Role / User                      | `R`       |

**Record Rules:**

- **Account multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_ids', 'parent_of', company_ids)]`

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

### 🗃️ `account.reconcile.model` — Preset to create journal entries during a invoices and payments matching

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation                     |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ---------------------------- |
| `active`                     | Active                 | `boolean`   |     | ✅    |                              |
| `can_be_proposed`            | Can Be Proposed        | `boolean`   |     | ✅    |                              |
| `company_id`                 | Company                | `many2one`  | ✅  | ✅    | res.company                  |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                              |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users                    |
| `display_name`               | Display Name           | `char`      |     |       |                              |
| `has_message`                | Has Message            | `boolean`   |     |       |                              |
| `id`                         | ID                     | `integer`   |     | ✅    |                              |
| `line_ids`                   | Line                   | `one2many`  |     | ✅    | account.reconcile.model.line |
| `mapped_partner_id`          | Mapped Partner         | `many2one`  |     | ✅    | res.partner                  |
| `match_amount`               | Amount                 | `selection` |     | ✅    |                              |
| `match_amount_max`           | Amount Max Parameter   | `float`     |     | ✅    |                              |
| `match_amount_min`           | Amount Min Parameter   | `float`     |     | ✅    |                              |
| `match_journal_ids`          | Journals               | `many2many` |     | ✅    | account.journal              |
| `match_label`                | Label                  | `selection` |     | ✅    |                              |
| `match_label_param`          | Label Parameter        | `char`      |     | ✅    |                              |
| `match_partner_ids`          | Partners               | `many2many` |     | ✅    | res.partner                  |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                              |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers               |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                              |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                              |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                              |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message                 |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                              |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                              |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                              |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner                  |
| `name`                       | Name                   | `char`      | ✅  | ✅    |                              |
| `next_activity_type_id`      | Next Activity          | `many2one`  |     | ✅    | mail.activity.type           |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating                |
| `sequence`                   | Sequence               | `integer`   | ✅  | ✅    |                              |
| `trigger`                    | Trigger                | `selection` | ✅  | ✅    |                              |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message                 |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                              |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                             | Group                  | Perms     |
| -------------------------------- | ---------------------- | --------- |
| account.reconcile.model.billing  | Accounting / Invoicing | `R/C`     |
| account.reconcile.model.readonly | Auditor                | `R`       |
| account.reconcile.model          | Basic                  | `R/W/C/D` |

**Record Rules:**

- **Account reconcile model template company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'parent_of', company_ids)]`

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

### 🗃️ `product.category` — Product Category

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                  | Label                      | Type                    | Req | Store | Relation           |
| -------------------------------------- | -------------------------- | ----------------------- | --- | ----- | ------------------ |
| `account_stock_variation_id`           | Stock Variation Account    | `many2one`              |     |       | account.account    |
| `anglo_saxon_accounting`               | Use Anglo-Saxon Accounting | `boolean`               |     |       |                    |
| `child_id`                             | Child Categories           | `one2many`              |     | ✅    | product.category   |
| `complete_name`                        | Complete Name              | `char`                  |     | ✅    |                    |
| `create_date`                          | Created on                 | `datetime`              |     | ✅    |                    |
| `create_uid`                           | Created by                 | `many2one`              |     | ✅    | res.users          |
| `display_name`                         | Display Name               | `char`                  |     |       |                    |
| `filter_for_stock_putaway_rule`        | stock.putaway.rule         | `boolean`               |     |       |                    |
| `has_message`                          | Has Message                | `boolean`               |     |       |                    |
| `id`                                   | ID                         | `integer`               |     | ✅    |                    |
| `message_attachment_count`             | Attachment Count           | `integer`               |     |       |                    |
| `message_follower_ids`                 | Followers                  | `one2many`              |     | ✅    | mail.followers     |
| `message_has_error`                    | Message Delivery error     | `boolean`               |     |       |                    |
| `message_has_error_counter`            | Number of errors           | `integer`               |     |       |                    |
| `message_has_sms_error`                | SMS Delivery error         | `boolean`               |     |       |                    |
| `message_ids`                          | Messages                   | `one2many`              |     | ✅    | mail.message       |
| `message_is_follower`                  | Is Follower                | `boolean`               |     |       |                    |
| `message_needaction`                   | Action Needed              | `boolean`               |     |       |                    |
| `message_needaction_counter`           | Number of Actions          | `integer`               |     |       |                    |
| `message_partner_ids`                  | Followers (Partners)       | `many2many`             |     |       | res.partner        |
| `name`                                 | Name                       | `char`                  | ✅  | ✅    |                    |
| `packaging_reserve_method`             | Reserve Packagings         | `selection`             |     | ✅    |                    |
| `parent_id`                            | Parent Category            | `many2one`              |     | ✅    | product.category   |
| `parent_path`                          | Parent Path                | `char`                  |     | ✅    |                    |
| `parent_route_ids`                     | Parent Routes              | `many2many`             |     |       | stock.route        |
| `product_count`                        | # Products                 | `integer`               |     |       |                    |
| `product_properties_definition`        | Product Properties         | `properties_definition` |     | ✅    |                    |
| `property_account_expense_categ_id`    | Expense Account            | `many2one`              |     | ✅    | account.account    |
| `property_account_income_categ_id`     | Income Account             | `many2one`              |     | ✅    | account.account    |
| `property_cost_method`                 | Costing Method             | `selection`             |     | ✅    |                    |
| `property_price_difference_account_id` | Price Difference Account   | `many2one`              |     | ✅    | account.account    |
| `property_stock_journal`               | Stock Journal              | `many2one`              |     | ✅    | account.journal    |
| `property_stock_valuation_account_id`  | Stock Valuation Account    | `many2one`              |     | ✅    | account.account    |
| `property_valuation`                   | Inventory Valuation        | `selection`             |     | ✅    |                    |
| `putaway_rule_ids`                     | Putaway Rules              | `one2many`              |     | ✅    | stock.putaway.rule |
| `rating_ids`                           | Ratings                    | `one2many`              |     | ✅    | rating.rating      |
| `removal_strategy_id`                  | Force Removal Strategy     | `many2one`              |     | ✅    | product.removal    |
| `route_ids`                            | Routes                     | `many2many`             |     | ✅    | stock.route        |
| `total_route_ids`                      | Total routes               | `many2many`             |     |       | stock.route        |
| `website_message_ids`                  | Website Messages           | `one2many`              |     | ✅    | mail.message       |
| `write_date`                           | Last Updated on            | `datetime`              |     | ✅    |                    |
| `write_uid`                            | Last Updated by            | `many2one`              |     | ✅    | res.users          |

**Access Rights:**

| Name                     | Group             | Perms     |
| ------------------------ | ----------------- | --------- |
| product.category.manager | Products / Create | `R/W/C/D` |
| product.category.public  | Role / Portal     | `R`       |
| product.category.public  | Role / Public     | `R`       |
| product.category.public  | Role / User       | `R`       |
| product.category.user    | Role / User       | `R`       |

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

### 🗃️ `res.groups` — Access Groups

Update of res.users class - add a preference about username for livechat purpose

**Fields:**

| Field                  | Label                                     | Type        | Req | Store | Relation             |
| ---------------------- | ----------------------------------------- | ----------- | --- | ----- | -------------------- |
| `all_implied_by_ids`   | Transitively Implying Groups              | `many2many` |     |       | res.groups           |
| `all_implied_ids`      | Transitively Implied Groups               | `many2many` |     |       | res.groups           |
| `all_user_ids`         | Users and implied users                   | `many2many` |     |       | res.users            |
| `all_users_count`      | # Users                                   | `integer`   |     |       |                      |
| `api_key_duration`     | API Keys maximum duration days            | `float`     |     | ✅    |                      |
| `comment`              | Comment                                   | `text`      |     | ✅    |                      |
| `create_date`          | Created on                                | `datetime`  |     | ✅    |                      |
| `create_uid`           | Created by                                | `many2one`  |     | ✅    | res.users            |
| `disjoint_ids`         | Disjoint Groups                           | `many2many` |     |       | res.groups           |
| `display_name`         | Display Name                              | `char`      |     |       |                      |
| `full_name`            | Group Name                                | `char`      |     |       |                      |
| `id`                   | ID                                        | `integer`   |     | ✅    |                      |
| `implied_by_ids`       | Implying Groups                           | `many2many` |     | ✅    | res.groups           |
| `implied_ids`          | Implied Groups                            | `many2many` |     | ✅    | res.groups           |
| `menu_access`          | Access Menu                               | `many2many` |     | ✅    | ir.ui.menu           |
| `model_access`         | Access Controls                           | `one2many`  |     | ✅    | ir.model.access      |
| `name`                 | Name                                      | `char`      | ✅  | ✅    |                      |
| `parent_ids`           | Parents                                   | `many2many` |     | ✅    | res.groups           |
| `privilege_id`         | Privilege                                 | `many2one`  |     | ✅    | res.groups.privilege |
| `role_count`           | # Roles                                   | `integer`   |     |       |                      |
| `role_id`              | Role                                      | `one2many`  |     | ✅    | res.users.role       |
| `role_ids`             | Roles                                     | `many2many` |     |       | res.users.role       |
| `rule_groups`          | Rules                                     | `many2many` |     | ✅    | ir.rule              |
| `sequence`             | Sequence                                  | `integer`   |     | ✅    |                      |
| `share`                | Share Group                               | `boolean`   |     | ✅    |                      |
| `trans_parent_ids`     | Parent Groups                             | `many2many` |     |       | res.groups           |
| `user_ids`             | User                                      | `many2many` |     | ✅    | res.users            |
| `view_access`          | Views                                     | `many2many` |     | ✅    | ir.ui.view           |
| `view_group_hierarchy` | Technical field for default group setting | `json`      |     |       |                      |
| `write_date`           | Last Updated on                           | `datetime`  |     | ✅    |                      |
| `write_uid`            | Last Updated by                           | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                         | Group         | Perms     |
| ---------------------------- | ------------- | --------- |
| res_groups group_erp_manager | Access Rights | `R/W/C/D` |
| res_groups group_user        | Role / User   | `R`       |

### 🗃️ `account.cash.rounding` — Account Cash Rounding

    In some countries, we need to be able to make appear on an invoice a rounding line, appearing there only because the
    smallest coinage has been removed from the circulation. For example, in Switzerland invoices have to be rounded to
    0.05 CHF because coins of 0.01 CHF and 0.02 CHF aren't used anymore.
    see https://en.wikipedia.org/wiki/Cash_rounding for more details.

**Fields:**

| Field               | Label              | Type        | Req | Store | Relation        |
| ------------------- | ------------------ | ----------- | --- | ----- | --------------- |
| `create_date`       | Created on         | `datetime`  |     | ✅    |                 |
| `create_uid`        | Created by         | `many2one`  |     | ✅    | res.users       |
| `display_name`      | Display Name       | `char`      |     |       |                 |
| `id`                | ID                 | `integer`   |     | ✅    |                 |
| `loss_account_id`   | Loss Account       | `many2one`  |     | ✅    | account.account |
| `name`              | Name               | `char`      | ✅  | ✅    |                 |
| `profit_account_id` | Profit Account     | `many2one`  |     | ✅    | account.account |
| `rounding`          | Rounding Precision | `float`     | ✅  | ✅    |                 |
| `rounding_method`   | Rounding Method    | `selection` | ✅  | ✅    |                 |
| `strategy`          | Rounding Strategy  | `selection` | ✅  | ✅    |                 |
| `write_date`        | Last Updated on    | `datetime`  |     | ✅    |                 |
| `write_uid`         | Last Updated by    | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                  | Group                  | Perms     |
| --------------------- | ---------------------- | --------- |
| account.cash.rounding | Accounting / Invoicing | `R/W/C/D` |
| account.cash.rounding | Auditor                | `R`       |

### 🗃️ `account.chart.template` — Account Chart Template

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `account.root` — Account codes first 2 digits

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label        | Type       | Req | Store | Relation     |
| -------------- | ------------ | ---------- | --- | ----- | ------------ |
| `display_name` | Display Name | `char`     |     |       |              |
| `id`           | ID           | `integer`  |     | ✅    |              |
| `name`         | Name         | `char`     |     |       |              |
| `parent_id`    | Parent       | `many2one` |     |       | account.root |

**Access Rights:**

| Name         | Group                | Perms |
| ------------ | -------------------- | ----- |
| account.root | Accounting / Advisor | `R`   |
| account.root | Auditor              | `R`   |

### 🗃️ `account.group` — Account Group

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label             | Type       | Req | Store | Relation      |
| ------------------- | ----------------- | ---------- | --- | ----- | ------------- |
| `code_prefix_end`   | Code Prefix End   | `char`     |     | ✅    |               |
| `code_prefix_start` | Code Prefix Start | `char`     |     | ✅    |               |
| `company_id`        | Company           | `many2one` | ✅  | ✅    | res.company   |
| `create_date`       | Created on        | `datetime` |     | ✅    |               |
| `create_uid`        | Created by        | `many2one` |     | ✅    | res.users     |
| `display_name`      | Display Name      | `char`     |     |       |               |
| `id`                | ID                | `integer`  |     | ✅    |               |
| `name`              | Name              | `char`     | ✅  | ✅    |               |
| `parent_id`         | Parent            | `many2one` |     | ✅    | account.group |
| `write_date`        | Last Updated on   | `datetime` |     | ✅    |               |
| `write_uid`         | Last Updated by   | `many2one` |     | ✅    | res.users     |

**Access Rights:**

| Name                | Group                | Perms     |
| ------------------- | -------------------- | --------- |
| account.group       | Accounting / Advisor | `R/W/C/D` |
| account.group       | Auditor              | `R`       |
| account.group.basic | Basic                | `R`       |

**Record Rules:**

- **Account Group multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'parent_of', company_ids)]`

### 🗃️ `account.report` — Accounting Report

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                   | Type        | Req | Store | Relation              |
| ----------------------------- | ----------------------- | ----------- | --- | ----- | --------------------- |
| `active`                      | Active                  | `boolean`   |     | ✅    |                       |
| `allow_foreign_vat`           | Allow Foreign VAT       | `boolean`   |     | ✅    |                       |
| `availability_condition`      | Availability            | `selection` |     | ✅    |                       |
| `chart_template`              | Chart of Accounts       | `selection` |     | ✅    |                       |
| `column_ids`                  | Columns                 | `one2many`  |     | ✅    | account.report.column |
| `country_id`                  | Country                 | `many2one`  |     | ✅    | res.country           |
| `create_date`                 | Created on              | `datetime`  |     | ✅    |                       |
| `create_uid`                  | Created by              | `many2one`  |     | ✅    | res.users             |
| `currency_translation`        | Currency Translation    | `selection` |     | ✅    |                       |
| `default_opening_date_filter` | Default Opening         | `selection` |     | ✅    |                       |
| `display_name`                | Display Name            | `char`      |     |       |                       |
| `filter_account_type`         | Account Types           | `selection` |     | ✅    |                       |
| `filter_aml_ir_filters`       | Favorite Filters        | `boolean`   |     | ✅    |                       |
| `filter_analytic`             | Analytic Filter         | `boolean`   |     | ✅    |                       |
| `filter_budgets`              | Budgets                 | `boolean`   |     | ✅    |                       |
| `filter_date_range`           | Date Range              | `boolean`   |     | ✅    |                       |
| `filter_growth_comparison`    | Growth Comparison       | `boolean`   |     | ✅    |                       |
| `filter_hide_0_lines`         | Hide lines at 0         | `selection` |     | ✅    |                       |
| `filter_hierarchy`            | Account Groups          | `selection` |     | ✅    |                       |
| `filter_journals`             | Journals                | `boolean`   |     | ✅    |                       |
| `filter_multi_company`        | Multi-Company           | `selection` |     | ✅    |                       |
| `filter_partner`              | Partners                | `boolean`   |     | ✅    |                       |
| `filter_period_comparison`    | Period Comparison       | `boolean`   |     | ✅    |                       |
| `filter_show_draft`           | Draft Entries           | `boolean`   |     | ✅    |                       |
| `filter_unfold_all`           | Unfold All              | `boolean`   |     | ✅    |                       |
| `filter_unreconciled`         | Unreconciled Entries    | `boolean`   |     | ✅    |                       |
| `id`                          | ID                      | `integer`   |     | ✅    |                       |
| `integer_rounding`            | Integer Rounding        | `selection` |     | ✅    |                       |
| `line_ids`                    | Lines                   | `one2many`  |     | ✅    | account.report.line   |
| `load_more_limit`             | Load More Limit         | `integer`   |     | ✅    |                       |
| `name`                        | Name                    | `char`      | ✅  | ✅    |                       |
| `only_tax_exigible`           | Only Tax Exigible Lines | `boolean`   |     | ✅    |                       |
| `prefix_groups_threshold`     | Prefix Groups Threshold | `integer`   |     | ✅    |                       |
| `root_report_id`              | Root Report             | `many2one`  |     | ✅    | account.report        |
| `search_bar`                  | Search Bar              | `boolean`   |     | ✅    |                       |
| `section_main_report_ids`     | Section Of              | `many2many` |     | ✅    | account.report        |
| `section_report_ids`          | Sections                | `many2many` |     | ✅    | account.report        |
| `sequence`                    | Sequence                | `integer`   |     | ✅    |                       |
| `use_sections`                | Composite Report        | `boolean`   |     | ✅    |                       |
| `variant_report_ids`          | Variants                | `one2many`  |     | ✅    | account.report        |
| `write_date`                  | Last Updated on         | `datetime`  |     | ✅    |                       |
| `write_uid`                   | Last Updated by         | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                    | Group                | Perms     |
| ----------------------- | -------------------- | --------- |
| account.report.ac.user  | Accounting / Advisor | `R/W/C/D` |
| account.report.readonly | Auditor              | `R`       |
| account.report.basic    | Basic                | `R`       |

### 🗃️ `account.report.column` — Accounting Report Column

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                    | Label               | Type        | Req | Store | Relation              |
| ------------------------ | ------------------- | ----------- | --- | ----- | --------------------- |
| `blank_if_zero`          | Blank if Zero       | `boolean`   |     | ✅    |                       |
| `create_date`            | Created on          | `datetime`  |     | ✅    |                       |
| `create_uid`             | Created by          | `many2one`  |     | ✅    | res.users             |
| `custom_audit_action_id` | Custom Audit Action | `many2one`  |     | ✅    | ir.actions.act_window |
| `display_name`           | Display Name        | `char`      |     |       |                       |
| `expression_label`       | Expression Label    | `char`      | ✅  | ✅    |                       |
| `figure_type`            | Figure Type         | `selection` | ✅  | ✅    |                       |
| `id`                     | ID                  | `integer`   |     | ✅    |                       |
| `name`                   | Name                | `char`      | ✅  | ✅    |                       |
| `report_id`              | Report              | `many2one`  |     | ✅    | account.report        |
| `sequence`               | Sequence            | `integer`   |     | ✅    |                       |
| `sortable`               | Sortable            | `boolean`   |     | ✅    |                       |
| `write_date`             | Last Updated on     | `datetime`  |     | ✅    |                       |
| `write_uid`              | Last Updated by     | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                           | Group                | Perms     |
| ------------------------------ | -------------------- | --------- |
| account.report.column.ac.user  | Accounting / Advisor | `R/W/C/D` |
| account.report.column.readonly | Auditor              | `R`       |
| account.report.column.basic    | Basic                | `R`       |

### 🗃️ `account.report.expression` — Accounting Report Expression

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label                        | Type        | Req | Store | Relation            |
| ------------------- | ---------------------------- | ----------- | --- | ----- | ------------------- |
| `auditable`         | Auditable                    | `boolean`   |     | ✅    |                     |
| `blank_if_zero`     | Blank if Zero                | `boolean`   |     | ✅    |                     |
| `carryover_target`  | Carry Over To                | `char`      |     | ✅    |                     |
| `create_date`       | Created on                   | `datetime`  |     | ✅    |                     |
| `create_uid`        | Created by                   | `many2one`  |     | ✅    | res.users           |
| `date_scope`        | Date Scope                   | `selection` | ✅  | ✅    |                     |
| `display_name`      | Display Name                 | `char`      |     |       |                     |
| `engine`            | Computation Engine           | `selection` | ✅  | ✅    |                     |
| `figure_type`       | Figure Type                  | `selection` |     | ✅    |                     |
| `formula`           | Formula                      | `char`      | ✅  | ✅    |                     |
| `green_on_positive` | Is Growth Good when Positive | `boolean`   |     | ✅    |                     |
| `id`                | ID                           | `integer`   |     | ✅    |                     |
| `label`             | Label                        | `char`      | ✅  | ✅    |                     |
| `report_line_id`    | Report Line                  | `many2one`  | ✅  | ✅    | account.report.line |
| `report_line_name`  | Report Line Name             | `char`      |     |       |                     |
| `subformula`        | Subformula                   | `char`      |     | ✅    |                     |
| `write_date`        | Last Updated on              | `datetime`  |     | ✅    |                     |
| `write_uid`         | Last Updated by              | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                               | Group                | Perms     |
| ---------------------------------- | -------------------- | --------- |
| account.report.expression.ac.user  | Accounting / Advisor | `R/W/C/D` |
| account.report.expression.readonly | Auditor              | `R`       |
| account.report.expression.basic    | Basic                | `R`       |

### 🗃️ `account.report.external.value` — Accounting Report External Value

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                               | Label                   | Type       | Req | Store | Relation                  |
| ----------------------------------- | ----------------------- | ---------- | --- | ----- | ------------------------- |
| `carryover_origin_expression_label` | Origin Expression Label | `char`     |     | ✅    |                           |
| `carryover_origin_report_line_id`   | Origin Line             | `many2one` |     | ✅    | account.report.line       |
| `company_id`                        | Company                 | `many2one` | ✅  | ✅    | res.company               |
| `create_date`                       | Created on              | `datetime` |     | ✅    |                           |
| `create_uid`                        | Created by              | `many2one` |     | ✅    | res.users                 |
| `date`                              | Date                    | `date`     | ✅  | ✅    |                           |
| `display_name`                      | Display Name            | `char`     |     |       |                           |
| `id`                                | ID                      | `integer`  |     | ✅    |                           |
| `name`                              | Name                    | `char`     | ✅  | ✅    |                           |
| `report_country_id`                 | Country                 | `many2one` |     |       | res.country               |
| `target_report_expression_id`       | Target Expression       | `many2one` | ✅  | ✅    | account.report.expression |
| `target_report_expression_label`    | Target Expression Label | `char`     |     |       |                           |
| `target_report_line_id`             | Target Line             | `many2one` |     |       | account.report.line       |
| `text_value`                        | Text Value              | `char`     |     | ✅    |                           |
| `value`                             | Numeric Value           | `float`    |     | ✅    |                           |
| `write_date`                        | Last Updated on         | `datetime` |     | ✅    |                           |
| `write_uid`                         | Last Updated by         | `many2one` |     | ✅    | res.users                 |

**Access Rights:**

| Name                                   | Group                | Perms     |
| -------------------------------------- | -------------------- | --------- |
| account.report.external.value.ac.user  | Accounting / Advisor | `R/W/C/D` |
| account.report.external.value.readonly | Auditor              | `R`       |

**Record Rules:**

- **Report External Value multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`

### 🗃️ `account.report.line` — Accounting Report Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                   | Label                          | Type        | Req | Store | Relation                  |
| ----------------------- | ------------------------------ | ----------- | --- | ----- | ------------------------- |
| `account_codes_formula` | Account Codes Formula Shortcut | `char`      |     |       |                           |
| `action_id`             | Action                         | `many2one`  |     | ✅    | ir.actions.actions        |
| `aggregation_formula`   | Aggregation Formula Shortcut   | `char`      |     |       |                           |
| `children_ids`          | Child Lines                    | `one2many`  |     | ✅    | account.report.line       |
| `code`                  | Code                           | `char`      |     | ✅    |                           |
| `create_date`           | Created on                     | `datetime`  |     | ✅    |                           |
| `create_uid`            | Created by                     | `many2one`  |     | ✅    | res.users                 |
| `display_name`          | Display Name                   | `char`      |     |       |                           |
| `domain_formula`        | Domain Formula Shortcut        | `char`      |     |       |                           |
| `expression_ids`        | Expressions                    | `one2many`  |     | ✅    | account.report.expression |
| `external_formula`      | External Formula Shortcut      | `char`      |     |       |                           |
| `foldable`              | Foldable                       | `boolean`   |     | ✅    |                           |
| `groupby`               | Group By                       | `char`      |     | ✅    |                           |
| `hide_if_zero`          | Hide if Zero                   | `boolean`   |     | ✅    |                           |
| `hierarchy_level`       | Level                          | `integer`   | ✅  | ✅    |                           |
| `horizontal_split_side` | Horizontal Split Side          | `selection` |     | ✅    |                           |
| `id`                    | ID                             | `integer`   |     | ✅    |                           |
| `name`                  | Name                           | `char`      | ✅  | ✅    |                           |
| `parent_id`             | Parent Line                    | `many2one`  |     | ✅    | account.report.line       |
| `print_on_new_page`     | Print On New Page              | `boolean`   |     | ✅    |                           |
| `report_id`             | Parent Report                  | `many2one`  | ✅  | ✅    | account.report            |
| `sequence`              | Sequence                       | `integer`   |     | ✅    |                           |
| `tax_tags_formula`      | Tax Tags Formula Shortcut      | `char`      |     |       |                           |
| `user_groupby`          | User Group By                  | `char`      |     | ✅    |                           |
| `write_date`            | Last Updated on                | `datetime`  |     | ✅    |                           |
| `write_uid`             | Last Updated by                | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name                         | Group                | Perms     |
| ---------------------------- | -------------------- | --------- |
| account.report.line.ac.user  | Accounting / Advisor | `R/W/C/D` |
| account.report.line.readonly | Auditor              | `R`       |
| account.report.line.basic    | Basic                | `R`       |

### 🗃️ `account.journal.group` — Account Journal Group

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label             | Type        | Req | Store | Relation        |
| ---------------------- | ----------------- | ----------- | --- | ----- | --------------- |
| `company_id`           | Company           | `many2one`  |     | ✅    | res.company     |
| `create_date`          | Created on        | `datetime`  |     | ✅    |                 |
| `create_uid`           | Created by        | `many2one`  |     | ✅    | res.users       |
| `display_name`         | Display Name      | `char`      |     |       |                 |
| `excluded_journal_ids` | Excluded Journals | `many2many` |     | ✅    | account.journal |
| `id`                   | ID                | `integer`   |     | ✅    |                 |
| `name`                 | Ledger group      | `char`      | ✅  | ✅    |                 |
| `sequence`             | Sequence          | `integer`   |     | ✅    |                 |
| `write_date`           | Last Updated on   | `datetime`  |     | ✅    |                 |
| `write_uid`            | Last Updated by   | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                           | Group                  | Perms     |
| ------------------------------ | ---------------------- | --------- |
| account.journal.group invoice  | Accounting / Invoicing | `R`       |
| account.journal.group manager  | Accounting / Advisor   | `R/W/C/D` |
| account.journal.group readonly | Auditor                | `R`       |

**Record Rules:**

- **Multi-ledger multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|', ('company_id', '=', False), ('company_id', 'parent_of', company_ids)]`

### 🗃️ `account.lock_exception` — Account Lock Exception

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label                | Type        | Req | Store | Relation    |
| ---------------------- | -------------------- | ----------- | --- | ----- | ----------- |
| `active`               | Active               | `boolean`   |     | ✅    |             |
| `company_id`           | Company              | `many2one`  | ✅  | ✅    | res.company |
| `company_lock_date`    | Original Lock Date   | `date`      |     | ✅    |             |
| `create_date`          | Created on           | `datetime`  |     | ✅    |             |
| `create_uid`           | Created by           | `many2one`  |     | ✅    | res.users   |
| `display_name`         | Display Name         | `char`      |     |       |             |
| `end_datetime`         | End Date             | `datetime`  |     | ✅    |             |
| `fiscalyear_lock_date` | Global Lock Date     | `date`      |     |       |             |
| `id`                   | ID                   | `integer`   |     | ✅    |             |
| `lock_date`            | Changed Lock Date    | `date`      |     | ✅    |             |
| `lock_date_field`      | Lock Date Field      | `selection` | ✅  | ✅    |             |
| `purchase_lock_date`   | Purchase Lock Date   | `date`      |     |       |             |
| `reason`               | Reason               | `char`      |     | ✅    |             |
| `sale_lock_date`       | Sales Lock Date      | `date`      |     |       |             |
| `state`                | State                | `selection` |     |       |             |
| `tax_lock_date`        | Tax Return Lock Date | `date`      |     |       |             |
| `user_id`              | User                 | `many2one`  |     | ✅    | res.users   |
| `write_date`           | Last Updated on      | `datetime`  |     | ✅    |             |
| `write_uid`            | Last Updated by      | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                           | Group                | Perms |
| ------------------------------ | -------------------- | ----- |
| account.lock_exception manager | Accounting / Advisor | `R/C` |
| account.lock_exception         | Role / User          | `R`   |

### 🗃️ `account.merge.wizard` — Account merge wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                  | Label                | Type        | Req | Store | Relation                  |
| ---------------------- | -------------------- | ----------- | --- | ----- | ------------------------- |
| `account_ids`          | Account              | `many2many` |     | ✅    | account.account           |
| `create_date`          | Created on           | `datetime`  |     | ✅    |                           |
| `create_uid`           | Created by           | `many2one`  |     | ✅    | res.users                 |
| `disable_merge_button` | Disable Merge Button | `boolean`   |     |       |                           |
| `display_name`         | Display Name         | `char`      |     |       |                           |
| `id`                   | ID                   | `integer`   |     | ✅    |                           |
| `is_group_by_name`     | Group by name?       | `boolean`   |     | ✅    |                           |
| `wizard_line_ids`      | Wizard Line          | `one2many`  |     | ✅    | account.merge.wizard.line |
| `write_date`           | Last Updated on      | `datetime`  |     | ✅    |                           |
| `write_uid`            | Last Updated by      | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name                 | Group                | Perms     |
| -------------------- | -------------------- | --------- |
| account.merge.wizard | Accounting / Advisor | `R/W/C/D` |

### 🗃️ `account.merge.wizard.line` — Account merge wizard line

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                        | Label                      | Type        | Req | Store | Relation             |
| ---------------------------- | -------------------------- | ----------- | --- | ----- | -------------------- |
| `account_has_hashed_entries` | Account Has Hashed Entries | `boolean`   |     |       |                      |
| `account_id`                 | Account                    | `many2one`  |     | ✅    | account.account      |
| `company_ids`                | Companies                  | `many2many` |     |       | res.company          |
| `create_date`                | Created on                 | `datetime`  |     | ✅    |                      |
| `create_uid`                 | Created by                 | `many2one`  |     | ✅    | res.users            |
| `display_name`               | Display Name               | `char`      |     |       |                      |
| `display_type`               | Display Type               | `selection` | ✅  | ✅    |                      |
| `grouping_key`               | Grouping Key               | `char`      |     | ✅    |                      |
| `id`                         | ID                         | `integer`   |     | ✅    |                      |
| `info`                       | Info                       | `char`      |     |       |                      |
| `is_selected`                | Is Selected                | `boolean`   |     | ✅    |                      |
| `sequence`                   | Sequence                   | `integer`   |     | ✅    |                      |
| `wizard_id`                  | Wizard                     | `many2one`  | ✅  | ✅    | account.merge.wizard |
| `write_date`                 | Last Updated on            | `datetime`  |     | ✅    |                      |
| `write_uid`                  | Last Updated by            | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                      | Group                | Perms     |
| ------------------------- | -------------------- | --------- |
| account.merge.wizard.line | Accounting / Advisor | `R/W/C/D` |

### 🗃️ `account.move.reversal` — Account Move Reversal

> ✳️ Transient (Wizard)

    Account move reversal wizard, it cancel an account move by reversing it.

**Fields:**

| Field                   | Label                           | Type        | Req | Store | Relation        |
| ----------------------- | ------------------------------- | ----------- | --- | ----- | --------------- |
| `available_journal_ids` | Available Journal               | `many2many` |     |       | account.journal |
| `company_id`            | Company                         | `many2one`  | ✅  | ✅    | res.company     |
| `country_code`          | Country Code                    | `char`      |     |       |                 |
| `create_date`           | Created on                      | `datetime`  |     | ✅    |                 |
| `create_uid`            | Created by                      | `many2one`  |     | ✅    | res.users       |
| `currency_id`           | Currency                        | `many2one`  |     |       | res.currency    |
| `date`                  | Reversal date                   | `date`      |     | ✅    |                 |
| `display_name`          | Display Name                    | `char`      |     |       |                 |
| `id`                    | ID                              | `integer`   |     | ✅    |                 |
| `journal_id`            | Journal                         | `many2one`  | ✅  | ✅    | account.journal |
| `move_ids`              | Move                            | `many2many` |     | ✅    | account.move    |
| `move_type`             | Move Type                       | `char`      |     |       |                 |
| `new_move_ids`          | New Move                        | `many2many` |     | ✅    | account.move    |
| `reason`                | Reason displayed on Credit Note | `char`      |     | ✅    |                 |
| `residual`              | Residual                        | `monetary`  |     |       |                 |
| `write_date`            | Last Updated on                 | `datetime`  |     | ✅    |                 |
| `write_uid`             | Last Updated by                 | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                         | Group                  | Perms   |
| ---------------------------- | ---------------------- | ------- |
| access.account.move.reversal | Accounting / Invoicing | `R/W/C` |

### 🗃️ `account.move.send` — Account Move Send

Shared class between the two sending wizards. See 'account.move.send.batch.wizard' for
multiple invoices sending wizard (async) and 'account.move.send.wizard' for single
invoice sending wizard (sync).

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `account.move.send.batch.wizard` — Account Move Send Batch Wizard

> ✳️ Transient (Wizard)

Wizard that handles the sending of multiple invoices.

**Fields:**

| Field                 | Label               | Type        | Req | Store | Relation     |
| --------------------- | ------------------- | ----------- | --- | ----- | ------------ |
| `alerts`              | Alerts              | `json`      |     |       |              |
| `create_date`         | Created on          | `datetime`  |     | ✅    |              |
| `create_uid`          | Created by          | `many2one`  |     | ✅    | res.users    |
| `display_name`        | Display Name        | `char`      |     |       |              |
| `id`                  | ID                  | `integer`   |     | ✅    |              |
| `move_ids`            | Move                | `many2many` | ✅  | ✅    | account.move |
| `send_by_post_stamps` | Send By Post Stamps | `integer`   |     |       |              |
| `summary_data`        | Summary Data        | `json`      |     |       |              |
| `write_date`          | Last Updated on     | `datetime`  |     | ✅    |              |
| `write_uid`           | Last Updated by     | `many2one`  |     | ✅    | res.users    |

**Access Rights:**

| Name                                           | Group                            | Perms     |
| ---------------------------------------------- | -------------------------------- | --------- |
| access.account.move.send.batch.wizard.salesman | Sales / User: Own Documents Only | `R/W/C`   |
| access.account.move.send.batch.wizard          | Accounting / Invoicing           | `R/W/C/D` |

**Record Rules:**

- **Readonly Invoice Send and Print (batch)** (37) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Personal Invoice Send and Print (batch mode)** (25) `R/W/C/D`
  - Domain:
    `[('move_ids.move_type', 'in', ('out_invoice', 'out_refund')), '|', ('move_ids.invoice_user_id', '=', user.id), ('move_ids.invoice_user_id', '=', False)]`
- **All Invoice Send and Print (batch mode)** (26) `R/W/C/D`
  - Domain: `[('move_ids.move_type', 'in', ('out_invoice', 'out_refund'))]`

### 🗃️ `account.move.send.wizard` — Account Move Send Wizard

> ✳️ Transient (Wizard)

Wizard that handles the sending a single invoice.

**Fields:**

| Field                        | Label                                    | Type        | Req | Store | Relation          |
| ---------------------------- | ---------------------------------------- | ----------- | --- | ----- | ----------------- |
| `alerts`                     | Alerts                                   | `json`      |     |       |                   |
| `attachments_not_supported`  | Attachments Not Supported                | `json`      |     |       |                   |
| `available_pdf_report_ids`   | Available Pdf Report                     | `one2many`  |     |       | ir.actions.report |
| `body`                       | Contents                                 | `html`      |     | ✅    |                   |
| `body_has_template_value`    | Body content is the same as the template | `boolean`   |     |       |                   |
| `can_edit_body`              | Can Edit Body                            | `boolean`   |     |       |                   |
| `company_id`                 | Company                                  | `many2one`  |     |       | res.company       |
| `create_date`                | Created on                               | `datetime`  |     | ✅    |                   |
| `create_uid`                 | Created by                               | `many2one`  |     | ✅    | res.users         |
| `display_attachments_widget` | Display Attachments Widget               | `boolean`   |     |       |                   |
| `display_name`               | Display Name                             | `char`      |     |       |                   |
| `display_pdf_report_id`      | Display Pdf Report                       | `boolean`   |     |       |                   |
| `extra_edi_checkboxes`       | Extra Edi Checkboxes                     | `json`      |     | ✅    |                   |
| `extra_edis`                 | Extra Edis                               | `json`      |     |       |                   |
| `id`                         | ID                                       | `integer`   |     | ✅    |                   |
| `invoice_edi_format`         | Invoice Edi Format                       | `selection` |     |       |                   |
| `is_mail_template_editor`    | Is Editor                                | `boolean`   |     |       |                   |
| `lang`                       | Language                                 | `char`      |     | ✅    |                   |
| `mail_attachments_widget`    | Mail Attachments Widget                  | `json`      |     | ✅    |                   |
| `mail_partner_ids`           | To                                       | `many2many` |     | ✅    | res.partner       |
| `model`                      | Related Document Model                   | `char`      |     | ✅    |                   |
| `move_id`                    | Move                                     | `many2one`  | ✅  | ✅    | account.move      |
| `pdf_report_id`              | Invoice report                           | `many2one`  |     | ✅    | ir.actions.report |
| `render_model`               | Rendering Model                          | `char`      |     |       |                   |
| `res_ids`                    | Related Document IDs                     | `text`      |     | ✅    |                   |
| `sending_method_checkboxes`  | Sending Method Checkboxes                | `json`      |     | ✅    |                   |
| `sending_methods`            | Sending Methods                          | `json`      |     |       |                   |
| `subject`                    | Subject                                  | `char`      |     | ✅    |                   |
| `template_id`                | Mail Template                            | `many2one`  |     | ✅    | mail.template     |
| `template_name`              | Template Name                            | `char`      |     | ✅    |                   |
| `write_date`                 | Last Updated on                          | `datetime`  |     | ✅    |                   |
| `write_uid`                  | Last Updated by                          | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                                     | Group                            | Perms     |
| ---------------------------------------- | -------------------------------- | --------- |
| access.account.move.send.wizard.salesman | Sales / User: Own Documents Only | `R/W/C`   |
| access.account.move.send.wizard          | Accounting / Invoicing           | `R/W/C/D` |

**Record Rules:**

- **Readonly Invoice Send and Print (single)** (37) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Personal Invoice Send and Print (single mode)** (25) `R/W/C/D`
  - Domain:
    `[('move_id.move_type', 'in', ('out_invoice', 'out_refund')), '|', ('move_id.invoice_user_id', '=', user.id), ('move_id.invoice_user_id', '=', False)]`
- **All Invoice Send and Print (single mode)** (26) `R/W/C/D`
  - Domain: `[('move_id.move_type', 'in', ('out_invoice', 'out_refund'))]`

### 🗃️ `report.account.report_invoice` — Account report without payment lines

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `report.account.report_invoice_with_payments` — Account report with payment lines

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `account.fiscal.position.account` — Accounts Mapping of Fiscal Position

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label                  | Type       | Req | Store | Relation                |
| ----------------- | ---------------------- | ---------- | --- | ----- | ----------------------- |
| `account_dest_id` | Account to Use Instead | `many2one` | ✅  | ✅    | account.account         |
| `account_src_id`  | Account on Product     | `many2one` | ✅  | ✅    | account.account         |
| `company_id`      | Company                | `many2one` |     | ✅    | res.company             |
| `create_date`     | Created on             | `datetime` |     | ✅    |                         |
| `create_uid`      | Created by             | `many2one` |     | ✅    | res.users               |
| `display_name`    | Display Name           | `char`     |     |       |                         |
| `id`              | ID                     | `integer`  |     | ✅    |                         |
| `position_id`     | Fiscal Position        | `many2one` | ✅  | ✅    | account.fiscal.position |
| `write_date`      | Last Updated on        | `datetime` |     | ✅    |                         |
| `write_uid`       | Last Updated by        | `many2one` |     | ✅    | res.users               |

**Access Rights:**

| Name                                    | Group                | Perms     |
| --------------------------------------- | -------------------- | --------- |
| account.fiscal.position account.manager | Accounting / Advisor | `R/W/C/D` |
| account.fiscal.position all             | Role / User          | `R`       |

### 🗃️ `account.account.tag` — Account Tag

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label             | Type        | Req | Store | Relation                  |
| ---------------------- | ----------------- | ----------- | --- | ----- | ------------------------- |
| `active`               | Active            | `boolean`   |     | ✅    |                           |
| `applicability`        | Applicability     | `selection` | ✅  | ✅    |                           |
| `balance_negate`       | Balance Negate    | `boolean`   |     |       |                           |
| `color`                | Color Index       | `integer`   |     | ✅    |                           |
| `country_id`           | Country           | `many2one`  |     | ✅    | res.country               |
| `create_date`          | Created on        | `datetime`  |     | ✅    |                           |
| `create_uid`           | Created by        | `many2one`  |     | ✅    | res.users                 |
| `display_name`         | Display Name      | `char`      |     |       |                           |
| `id`                   | ID                | `integer`   |     | ✅    |                           |
| `name`                 | Tag Name          | `char`      | ✅  | ✅    |                           |
| `report_expression_id` | Report Expression | `many2one`  |     |       | account.report.expression |
| `write_date`           | Last Updated on   | `datetime`  |     | ✅    |                           |
| `write_uid`            | Last Updated by   | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name                              | Group                            | Perms     |
| --------------------------------- | -------------------------------- | --------- |
| account.account.tag.sale.salesman | Sales / User: Own Documents Only | `R`       |
| account.account.tag               | Accounting / Invoicing           | `R`       |
| account.account.tag               | Purchase / User                  | `R`       |
| account.account.tag               | Contact / Accountant             | `R/W/C/D` |
| account.account.tag               | Auditor                          | `R`       |
| account.account.tag internal user | Role / User                      | `R`       |

### 🗃️ `account.accrued.orders.wizard` — Accrued Orders Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field            | Label            | Type       | Req | Store | Relation        |
| ---------------- | ---------------- | ---------- | --- | ----- | --------------- |
| `account_id`     | Accrual Account  | `many2one` | ✅  | ✅    | account.account |
| `amount`         | Amount           | `monetary` |     | ✅    |                 |
| `company_id`     | Company          | `many2one` |     | ✅    | res.company     |
| `create_date`    | Created on       | `datetime` |     | ✅    |                 |
| `create_uid`     | Created by       | `many2one` |     | ✅    | res.users       |
| `currency_id`    | Company Currency | `many2one` |     | ✅    | res.currency    |
| `date`           | Date             | `date`     | ✅  | ✅    |                 |
| `display_amount` | Display Amount   | `boolean`  |     |       |                 |
| `display_name`   | Display Name     | `char`     |     |       |                 |
| `id`             | ID               | `integer`  |     | ✅    |                 |
| `journal_id`     | Journal          | `many2one` | ✅  | ✅    | account.journal |
| `preview_data`   | Preview Data     | `text`     |     |       |                 |
| `reversal_date`  | Reversal Date    | `date`     | ✅  | ✅    |                 |
| `write_date`     | Last Updated on  | `datetime` |     | ✅    |                 |
| `write_uid`      | Last Updated by  | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                                  | Group                | Perms   |
| ------------------------------------- | -------------------- | ------- |
| account.account.accrued.orders.wizard | Contact / Accountant | `R/W/C` |

### 🗃️ `account.analytic.distribution.model` — Analytic Distribution Model

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                               | Label                         | Type        | Req | Store | Relation                 |
| ----------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------ |
| `account_prefix`                    | Accounts Prefix               | `char`      |     | ✅    |                          |
| `analytic_distribution`             | Analytic Distribution         | `json`      |     | ✅    |                          |
| `analytic_precision`                | Analytic Precision            | `integer`   |     |       |                          |
| `company_id`                        | Company                       | `many2one`  |     | ✅    | res.company              |
| `create_date`                       | Created on                    | `datetime`  |     | ✅    |                          |
| `create_uid`                        | Created by                    | `many2one`  |     | ✅    | res.users                |
| `display_name`                      | Display Name                  | `char`      |     |       |                          |
| `distribution_analytic_account_ids` | Distribution Analytic Account | `many2many` |     |       | account.analytic.account |
| `id`                                | ID                            | `integer`   |     | ✅    |                          |
| `partner_category_id`               | Partner Category              | `many2one`  |     | ✅    | res.partner.category     |
| `partner_id`                        | Partner                       | `many2one`  |     | ✅    | res.partner              |
| `prefix_placeholder`                | Prefix Placeholder            | `char`      |     |       |                          |
| `product_categ_id`                  | Product Category              | `many2one`  |     | ✅    | product.category         |
| `product_id`                        | Product                       | `many2one`  |     | ✅    | product.product          |
| `sequence`                          | Sequence                      | `integer`   |     | ✅    |                          |
| `write_date`                        | Last Updated on               | `datetime`  |     | ✅    |                          |
| `write_uid`                         | Last Updated by               | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                                       | Group                  | Perms     |
| ------------------------------------------ | ---------------------- | --------- |
| account.analytic.distribution invoice      | Accounting / Invoicing | `R/W/C/D` |
| access_account_analytic_distribution_model | Analytic Accounting    | `R/W/C/D` |
| account.analytic.distribution invoice      | Auditor                | `R`       |

**Record Rules:**

- **Analytic distribution model multi company rule** (Global) `R/W/C/D`
  - Domain: `['|',('company_id','=',False),('company_id', 'parent_of', company_ids)]`

### 🗃️ `account.analytic.line` — Analytic Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                   | Label                 | Type        | Req | Store | Relation                 |
| ----------------------- | --------------------- | ----------- | --- | ----- | ------------------------ |
| `account_id`            | Project Account       | `many2one`  |     | ✅    | account.analytic.account |
| `amount`                | Amount                | `monetary`  | ✅  | ✅    |                          |
| `analytic_distribution` | Analytic Distribution | `json`      |     |       |                          |
| `analytic_precision`    | Analytic Precision    | `integer`   |     |       |                          |
| `auto_account_id`       | Analytic Account      | `many2one`  |     |       | account.analytic.account |
| `category`              | Category              | `selection` |     | ✅    |                          |
| `code`                  | Code                  | `char`      |     | ✅    |                          |
| `company_id`            | Company               | `many2one`  | ✅  | ✅    | res.company              |
| `create_date`           | Created on            | `datetime`  |     | ✅    |                          |
| `create_uid`            | Created by            | `many2one`  |     | ✅    | res.users                |
| `currency_id`           | Currency              | `many2one`  |     | ✅    | res.currency             |
| `date`                  | Date                  | `date`      | ✅  | ✅    |                          |
| `display_name`          | Display Name          | `char`      |     |       |                          |
| `fiscal_year_search`    | Fiscal Year Search    | `boolean`   |     |       |                          |
| `general_account_id`    | Financial Account     | `many2one`  |     | ✅    | account.account          |
| `id`                    | ID                    | `integer`   |     | ✅    |                          |
| `journal_id`            | Financial Journal     | `many2one`  |     | ✅    | account.journal          |
| `move_line_id`          | Journal Item          | `many2one`  |     | ✅    | account.move.line        |
| `name`                  | Description           | `char`      | ✅  | ✅    |                          |
| `partner_id`            | Partner               | `many2one`  |     | ✅    | res.partner              |
| `product_id`            | Product               | `many2one`  |     | ✅    | product.product          |
| `product_uom_id`        | Unit                  | `many2one`  |     | ✅    | uom.uom                  |
| `ref`                   | Ref.                  | `char`      |     | ✅    |                          |
| `so_line`               | Sales Order Item      | `many2one`  |     | ✅    | sale.order.line          |
| `unit_amount`           | Quantity              | `float`     |     | ✅    |                          |
| `user_id`               | User                  | `many2one`  |     | ✅    | res.users                |
| `write_date`            | Last Updated on       | `datetime`  |     | ✅    |                          |
| `write_uid`             | Last Updated by       | `many2one`  |     | ✅    | res.users                |
| `x_plan2_id`            | Departments           | `many2one`  |     | ✅    | account.analytic.account |
| `x_plan3_id`            | Internal              | `many2one`  |     | ✅    | account.analytic.account |

**Access Rights:**

| Name                          | Group                    | Perms     |
| ----------------------------- | ------------------------ | --------- |
| account.analytic.line invoice | Accounting / Invoicing   | `R/W/C/D` |
| account.analytic.line manager | Accounting / Advisor     | `R`       |
| account.analytic.line         | Purchase / User          | `R`       |
| account.analytic.line.user    | Expenses / Team Approver | `R/W/C/D` |
| access_account_analytic_line  | Analytic Accounting      | `R/W/C/D` |
| account.analytic.line invoice | Auditor                  | `R`       |

**Record Rules:**

- **Analytic line multi company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`
- **account.analytic.line.billing.user** (37) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **account.analytic.line.readonly.user** (36) `R`
  - Domain: `[(1, '=', 1)]`

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

### 🗃️ `ir.attachment` — Attachment

Attachments are used to link binary files or url to any openerp document.

    External attachment storage
    ---------------------------

    The computed field ``datas`` is implemented using ``_file_read``,
    ``_file_write`` and ``_file_delete``, which can be overridden to implement
    other storage engines. Such methods should check for other location pseudo
    uri (example: hdfs://hadoopserver).

    The default implementation is the file:dirname location that stores files
    on the local filesystem using name based on their sha1 hash

**Fields:**

| Field               | Label                                        | Type                 | Req | Store | Relation               |
| ------------------- | -------------------------------------------- | -------------------- | --- | ----- | ---------------------- |
| `access_token`      | Access Token                                 | `char`               |     | ✅    |                        |
| `checksum`          | Checksum/SHA1                                | `char`               |     | ✅    |                        |
| `company_id`        | Company                                      | `many2one`           |     | ✅    | res.company            |
| `create_date`       | Created on                                   | `datetime`           |     | ✅    |                        |
| `create_uid`        | Created by                                   | `many2one`           |     | ✅    | res.users              |
| `datas`             | File Content (base64)                        | `binary`             |     |       |                        |
| `db_datas`          | Database Data                                | `binary`             |     | ✅    |                        |
| `description`       | Description                                  | `text`               |     | ✅    |                        |
| `display_name`      | Display Name                                 | `char`               |     |       |                        |
| `file_size`         | File Size                                    | `integer`            |     | ✅    |                        |
| `has_thumbnail`     | Has Thumbnail                                | `boolean`            |     |       |                        |
| `id`                | ID                                           | `integer`            |     | ✅    |                        |
| `image_height`      | Image Height                                 | `integer`            |     |       |                        |
| `image_src`         | Image Src                                    | `char`               |     |       |                        |
| `image_width`       | Image Width                                  | `integer`            |     |       |                        |
| `index_content`     | Indexed Content                              | `text`               |     | ✅    |                        |
| `key`               | Key                                          | `char`               |     | ✅    |                        |
| `local_url`         | Attachment URL                               | `char`               |     |       |                        |
| `media_link`        | Media Link                                   | `char`               |     | ✅    |                        |
| `mimetype`          | Mime Type                                    | `char`               |     | ✅    |                        |
| `name`              | Name                                         | `char`               | ✅  | ✅    |                        |
| `original_id`       | Original (unoptimized, unresized) attachment | `many2one`           |     | ✅    | ir.attachment          |
| `public`            | Is public document                           | `boolean`            |     | ✅    |                        |
| `raw`               | File Content (raw)                           | `binary`             |     |       |                        |
| `res_field`         | Resource Field                               | `char`               |     | ✅    |                        |
| `res_id`            | Resource ID                                  | `many2one_reference` |     | ✅    |                        |
| `res_model`         | Resource Model                               | `char`               |     | ✅    |                        |
| `res_name`          | Resource Name                                | `char`               |     |       |                        |
| `store_fname`       | Stored Filename                              | `char`               |     | ✅    |                        |
| `theme_template_id` | Theme Template                               | `many2one`           |     | ✅    | theme.ir.attachment    |
| `thumbnail`         | Thumbnail                                    | `binary`             |     | ✅    |                        |
| `type`              | Type                                         | `selection`          | ✅  | ✅    |                        |
| `url`               | Url                                          | `char`               |     | ✅    |                        |
| `voice_ids`         | Voice                                        | `one2many`           |     | ✅    | discuss.voice.metadata |
| `website_id`        | Website                                      | `many2one`           |     | ✅    | website                |
| `whatsapp_media_id` | whatsapp Media Id                            | `char`               |     | ✅    |                        |
| `write_date`        | Last Updated on                              | `datetime`           |     | ✅    |                        |
| `write_uid`         | Last Updated by                              | `many2one`           |     | ✅    | res.users              |

**Access Rights:**

| Name                              | Group       | Perms     |
| --------------------------------- | ----------- | --------- |
| ir_attachment group_user          | Role / User | `R/W/C/D` |
| ir_attachment group_portal_public | Everyone    | `-`       |

### 🗃️ `sequence.mixin` — Automatic sequence

Mechanism used to have an editable sequence number.

    Be careful of how you use this regarding the prefixes. More info in the
    docstring of _get_last_sequence.

**Fields:**

| Field             | Label           | Type      | Req | Store | Relation |
| ----------------- | --------------- | --------- | --- | ----- | -------- |
| `display_name`    | Display Name    | `char`    |     |       |          |
| `id`              | ID              | `integer` |     | ✅    |          |
| `sequence_number` | Sequence Number | `integer` |     | ✅    |          |
| `sequence_prefix` | Sequence Prefix | `char`    |     | ✅    |          |

### 🗃️ `account.autopost.bills.wizard` — Autopost Bills Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                 | Label                                                   | Type       | Req | Store | Relation    |
| --------------------- | ------------------------------------------------------- | ---------- | --- | ----- | ----------- |
| `create_date`         | Created on                                              | `datetime` |     | ✅    |             |
| `create_uid`          | Created by                                              | `many2one` |     | ✅    | res.users   |
| `display_name`        | Display Name                                            | `char`     |     |       |             |
| `id`                  | ID                                                      | `integer`  |     | ✅    |             |
| `nb_unmodified_bills` | Number of bills previously unmodified from this partner | `integer`  |     | ✅    |             |
| `partner_id`          | Partner                                                 | `many2one` |     | ✅    | res.partner |
| `partner_name`        | Name                                                    | `char`     |     |       |             |
| `write_date`          | Last Updated on                                         | `datetime` |     | ✅    |             |
| `write_uid`           | Last Updated by                                         | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                                 | Group                  | Perms   |
| ------------------------------------ | ---------------------- | ------- |
| access.account.autopost.bills.wizard | Accounting / Invoicing | `R/W/C` |

### 🗃️ `account.setup.bank.manual.config` — Bank setup manual config

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                                  | Label                                | Type        | Req | Store | Relation           |
| -------------------------------------- | ------------------------------------ | ----------- | --- | ----- | ------------------ |
| `acc_holder_name`                      | Account Holder Name                  | `char`      |     |       |                    |
| `acc_number`                           | Account Number                       | `char`      | ✅  |       |                    |
| `acc_type`                             | Type                                 | `selection` |     |       |                    |
| `active`                               | Active                               | `boolean`   |     |       |                    |
| `activity_calendar_event_id`           | Next Activity Calendar Event         | `many2one`  |     |       | calendar.event     |
| `activity_date_deadline`               | Next Activity Deadline               | `date`      |     |       |                    |
| `activity_exception_decoration`        | Activity Exception Decoration        | `selection` |     |       |                    |
| `activity_exception_icon`              | Icon                                 | `char`      |     |       |                    |
| `activity_ids`                         | Activities                           | `one2many`  |     |       | mail.activity      |
| `activity_state`                       | Activity State                       | `selection` |     |       |                    |
| `activity_summary`                     | Next Activity Summary                | `char`      |     |       |                    |
| `activity_type_icon`                   | Activity Type Icon                   | `char`      |     |       |                    |
| `activity_type_id`                     | Next Activity Type                   | `many2one`  |     |       | mail.activity.type |
| `activity_user_id`                     | Responsible User                     | `many2one`  |     |       | res.users          |
| `allow_out_payment`                    | Send Money                           | `boolean`   |     |       |                    |
| `bank_bic`                             | Bic                                  | `char`      |     |       |                    |
| `bank_city`                            | City                                 | `char`      |     |       |                    |
| `bank_country`                         | Country                              | `many2one`  |     |       | res.country        |
| `bank_email`                           | Email                                | `char`      |     |       |                    |
| `bank_id`                              | Bank                                 | `many2one`  |     |       | res.bank           |
| `bank_name`                            | Name                                 | `char`      |     |       |                    |
| `bank_phone`                           | Phone                                | `char`      |     |       |                    |
| `bank_state`                           | Fed. State                           | `many2one`  |     |       | res.country.state  |
| `bank_street`                          | Street                               | `char`      |     |       |                    |
| `bank_street2`                         | Street2                              | `char`      |     |       |                    |
| `bank_zip`                             | Zip                                  | `char`      |     |       |                    |
| `clearing_number`                      | Clearing Number                      | `char`      |     |       |                    |
| `color`                                | Color                                | `integer`   |     |       |                    |
| `company_id`                           | Company                              | `many2one`  | ✅  |       | res.company        |
| `country_code`                         | Country Code                         | `char`      |     |       |                    |
| `create_date`                          | Created on                           | `datetime`  |     | ✅    |                    |
| `create_uid`                           | Created by                           | `many2one`  |     | ✅    | res.users          |
| `currency_id`                          | Currency                             | `many2one`  |     |       | res.currency       |
| `currency_symbol`                      | Symbol                               | `char`      |     |       |                    |
| `display_name`                         | Display Name                         | `char`      |     |       |                    |
| `duplicate_bank_partner_ids`           | Duplicate Bank Partner               | `many2many` |     |       | res.partner        |
| `employee_has_multiple_bank_accounts`  | Has Multiple Bank Accounts           | `boolean`   |     |       |                    |
| `employee_id`                          | Employee                             | `many2many` |     |       | hr.employee        |
| `employee_salary_amount`               | Salary Allocation                    | `float`     |     |       |                    |
| `employee_salary_amount_is_percentage` | Employee Salary Amount Is Percentage | `boolean`   |     |       |                    |
| `has_iban_warning`                     | Has Iban Warning                     | `boolean`   |     |       |                    |
| `has_message`                          | Has Message                          | `boolean`   |     |       |                    |
| `has_money_transfer_warning`           | Has Money Transfer Warning           | `boolean`   |     |       |                    |
| `id`                                   | ID                                   | `integer`   |     | ✅    |                    |
| `journal_id`                           | Account Journal                      | `one2many`  |     |       | account.journal    |
| `l10n_us_bank_account_type`            | Bank Account Type                    | `selection` | ✅  |       |                    |
| `linked_journal_id`                    | Journal                              | `many2one`  |     |       | account.journal    |
| `lock_trust_fields`                    | Lock Trust Fields                    | `boolean`   |     |       |                    |
| `message_attachment_count`             | Attachment Count                     | `integer`   |     |       |                    |
| `message_follower_ids`                 | Followers                            | `one2many`  |     |       | mail.followers     |
| `message_has_error`                    | Message Delivery error               | `boolean`   |     |       |                    |
| `message_has_error_counter`            | Number of errors                     | `integer`   |     |       |                    |
| `message_has_sms_error`                | SMS Delivery error                   | `boolean`   |     |       |                    |
| `message_ids`                          | Messages                             | `one2many`  |     |       | mail.message       |
| `message_is_follower`                  | Is Follower                          | `boolean`   |     |       |                    |
| `message_needaction`                   | Action Needed                        | `boolean`   |     |       |                    |
| `message_needaction_counter`           | Number of Actions                    | `integer`   |     |       |                    |
| `message_partner_ids`                  | Followers (Partners)                 | `many2many` |     |       | res.partner        |
| `money_transfer_service`               | Money Transfer Service               | `char`      |     |       |                    |
| `my_activity_date_deadline`            | My Activity Deadline                 | `date`      |     |       |                    |
| `new_journal_name`                     | New Journal Name                     | `char`      | ✅  | ✅    |                    |
| `note`                                 | Notes                                | `text`      |     |       |                    |
| `num_journals_without_account_bank`    | Num Journals Without Account Bank    | `integer`   |     | ✅    |                    |
| `num_journals_without_account_credit`  | Num Journals Without Account Credit  | `integer`   |     | ✅    |                    |
| `partner_country_name`                 | Country Name                         | `char`      |     |       |                    |
| `partner_customer_rank`                | Customer Rank                        | `integer`   |     |       |                    |
| `partner_id`                           | Account Holder                       | `many2one`  | ✅  |       | res.partner        |
| `partner_supplier_rank`                | Supplier Rank                        | `integer`   |     |       |                    |
| `rating_ids`                           | Ratings                              | `one2many`  |     |       | rating.rating      |
| `related_moves`                        | Related Moves                        | `one2many`  |     |       | account.move       |
| `res_partner_bank_id`                  | Res Partner Bank                     | `many2one`  | ✅  | ✅    | res.partner.bank   |
| `sanitized_acc_number`                 | Sanitized Account Number             | `char`      |     |       |                    |
| `sequence`                             | Sequence                             | `integer`   |     |       |                    |
| `show_aba_routing`                     | Show Aba Routing                     | `boolean`   |     |       |                    |
| `user_has_group_validate_bank_account` | User Has Group Validate Bank Account | `boolean`   |     |       |                    |
| `website_message_ids`                  | Website Messages                     | `one2many`  |     |       | mail.message       |
| `write_date`                           | Last Updated on                      | `datetime`  |     | ✅    |                    |
| `write_uid`                            | Last Updated by                      | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                    | Group                | Perms   |
| --------------------------------------- | -------------------- | ------- |
| access.account.setup.bank.manual.config | Accounting / Advisor | `R/W/C` |

### 🗃️ `account.bank.statement` — Bank Statement

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                  | Type        | Req | Store | Relation                    |
| -------------------------------- | ---------------------- | ----------- | --- | ----- | --------------------------- |
| `attachment_ids`                 | Attachments            | `many2many` |     | ✅    | ir.attachment               |
| `balance_end`                    | Computed Balance       | `monetary`  |     | ✅    |                             |
| `balance_end_real`               | Ending Balance         | `monetary`  |     | ✅    |                             |
| `balance_start`                  | Starting Balance       | `monetary`  |     | ✅    |                             |
| `company_id`                     | Company                | `many2one`  |     | ✅    | res.company                 |
| `create_date`                    | Created on             | `datetime`  |     | ✅    |                             |
| `create_uid`                     | Created by             | `many2one`  |     | ✅    | res.users                   |
| `currency_id`                    | Currency               | `many2one`  |     | ✅    | res.currency                |
| `date`                           | Date                   | `date`      |     | ✅    |                             |
| `display_name`                   | Display Name           | `char`      |     |       |                             |
| `first_line_index`               | First Line Index       | `char`      |     | ✅    | account.bank.statement.line |
| `id`                             | ID                     | `integer`   |     | ✅    |                             |
| `is_complete`                    | Is Complete            | `boolean`   |     | ✅    |                             |
| `is_valid`                       | Is Valid               | `boolean`   |     |       |                             |
| `journal_has_invalid_statements` | Has Invalid Statements | `boolean`   |     |       |                             |
| `journal_id`                     | Journal                | `many2one`  |     | ✅    | account.journal             |
| `line_ids`                       | Statement lines        | `one2many`  |     | ✅    | account.bank.statement.line |
| `name`                           | Reference              | `char`      |     | ✅    |                             |
| `problem_description`            | Problem Description    | `text`      |     |       |                             |
| `reference`                      | External Reference     | `char`      |     | ✅    |                             |
| `write_date`                     | Last Updated on        | `datetime`  |     | ✅    |                             |
| `write_uid`                      | Last Updated by        | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                                 | Group                  | Perms     |
| ------------------------------------ | ---------------------- | --------- |
| account.bank.statement.group.invoice | Accounting / Invoicing | `R`       |
| account.bank.statement.group.invoice | Auditor                | `R`       |
| account.bank.statement               | Basic                  | `R/W/C/D` |

**Record Rules:**

- **Account bank statement company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `account.bank.statement.line` — Bank Statement Line

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
| `access_token`                              | Security Token                            | `char`      |     |       |                                 |
| `access_url`                                | Portal Access URL                         | `char`      |     |       |                                 |
| `access_warning`                            | Access warning                            | `text`      |     |       |                                 |
| `account_fiscal_country_group_codes`        | Account Fiscal Country Group Codes        | `json`      |     |       |                                 |
| `account_number`                            | Bank Account Number                       | `char`      |     | ✅    |                                 |
| `activity_calendar_event_id`                | Next Activity Calendar Event              | `many2one`  |     |       | calendar.event                  |
| `activity_date_deadline`                    | Next Activity Deadline                    | `date`      |     |       |                                 |
| `activity_exception_decoration`             | Activity Exception Decoration             | `selection` |     |       |                                 |
| `activity_exception_icon`                   | Icon                                      | `char`      |     |       |                                 |
| `activity_ids`                              | Activities                                | `one2many`  |     |       | mail.activity                   |
| `activity_state`                            | Activity State                            | `selection` |     |       |                                 |
| `activity_summary`                          | Next Activity Summary                     | `char`      |     |       |                                 |
| `activity_type_icon`                        | Activity Type Icon                        | `char`      |     |       |                                 |
| `activity_type_id`                          | Next Activity Type                        | `many2one`  |     |       | mail.activity.type              |
| `activity_user_id`                          | Responsible User                          | `many2one`  |     |       | res.users                       |
| `adjusting_entries_count`                   | Adjusting Entries Count                   | `integer`   |     |       |                                 |
| `adjusting_entries_move_ids`                | Created Adjusting Entries                 | `many2many` |     |       | account.move                    |
| `adjusting_entry_origin_label`              | Adjusting Entry Origin Label              | `char`      |     |       |                                 |
| `adjusting_entry_origin_move_ids`           | Adjusting Entry Origin Moves              | `many2many` |     |       | account.move                    |
| `adjusting_entry_origin_moves_count`        | Adjusting Entry Origin Moves Count        | `integer`   |     |       |                                 |
| `alerts`                                    | Alerts                                    | `json`      |     |       |                                 |
| `always_tax_exigible`                       | Always Tax Exigible                       | `boolean`   |     |       |                                 |
| `amount`                                    | Amount                                    | `monetary`  |     | ✅    |                                 |
| `amount_currency`                           | Amount in Currency                        | `monetary`  |     | ✅    |                                 |
| `amount_paid`                               | Amount paid                               | `monetary`  |     |       |                                 |
| `amount_residual`                           | Residual Amount                           | `float`     |     | ✅    |                                 |
| `amount_residual_signed`                    | Amount Due Signed                         | `monetary`  |     |       |                                 |
| `amount_tax`                                | Tax                                       | `monetary`  |     |       |                                 |
| `amount_tax_signed`                         | Tax Signed                                | `monetary`  |     |       |                                 |
| `amount_total`                              | Total                                     | `monetary`  |     |       |                                 |
| `amount_total_in_currency_signed`           | Total in Currency Signed                  | `monetary`  |     |       |                                 |
| `amount_total_signed`                       | Total Signed                              | `monetary`  |     |       |                                 |
| `amount_total_words`                        | Amount total in words                     | `char`      |     |       |                                 |
| `amount_untaxed`                            | Untaxed Amount                            | `monetary`  |     |       |                                 |
| `amount_untaxed_in_currency_signed`         | Untaxed Amount Signed Currency            | `monetary`  |     |       |                                 |
| `amount_untaxed_signed`                     | Untaxed Amount Signed                     | `monetary`  |     |       |                                 |
| `asset_depreciation_ids`                    | Assets Depreciation Lines                 | `one2many`  |     |       | account.asset.depreciation.line |
| `attachment_ids`                            | Attachments                               | `one2many`  |     |       | ir.attachment                   |
| `audit_trail_message_ids`                   | Audit Trail Messages                      | `one2many`  |     |       | mail.message                    |
| `authorized_transaction_ids`                | Authorized Transactions                   | `many2many` |     |       | payment.transaction             |
| `auto_post`                                 | Auto-post                                 | `selection` | ✅  |       |                                 |
| `auto_post_origin_id`                       | First recurring entry                     | `many2one`  |     |       | account.move                    |
| `auto_post_until`                           | Auto-post until                           | `date`      |     |       |                                 |
| `bank_partner_id`                           | Bank Partner                              | `many2one`  |     |       | res.partner                     |
| `campaign_id`                               | Campaign                                  | `many2one`  |     |       | utm.campaign                    |
| `checked`                                   | Reviewed                                  | `boolean`   |     |       |                                 |
| `commercial_partner_id`                     | Commercial Entity                         | `many2one`  |     |       | res.partner                     |
| `company_currency_id`                       | Company Currency                          | `many2one`  |     |       | res.currency                    |
| `company_id`                                | Company                                   | `many2one`  | ✅  | ✅    | res.company                     |
| `company_price_include`                     | Default Sales Price Include               | `selection` |     |       |                                 |
| `country_code`                              | Country Code                              | `char`      |     |       |                                 |
| `create_date`                               | Created on                                | `datetime`  |     | ✅    |                                 |
| `create_uid`                                | Created by                                | `many2one`  |     | ✅    | res.users                       |
| `currency_id`                               | Journal Currency                          | `many2one`  |     | ✅    | res.currency                    |
| `date`                                      | Date                                      | `date`      | ✅  |       |                                 |
| `delivery_date`                             | Delivery Date                             | `date`      |     |       |                                 |
| `direction_sign`                            | Direction Sign                            | `integer`   |     |       |                                 |
| `display_inactive_currency_warning`         | Display Inactive Currency Warning         | `boolean`   |     |       |                                 |
| `display_link_qr_code`                      | Display Link QR-code                      | `boolean`   |     |       |                                 |
| `display_name`                              | Display Name                              | `char`      |     |       |                                 |
| `display_qr_code`                           | Display QR-code                           | `boolean`   |     |       |                                 |
| `display_send_button`                       | Display Send Button                       | `boolean`   |     |       |                                 |
| `duplicated_ref_ids`                        | Duplicated Ref                            | `many2many` |     |       | account.move                    |
| `exchange_diff_partial_ids`                 | Related reconciliation                    | `one2many`  |     |       | account.partial.reconcile       |
| `expected_currency_rate`                    | Expected Currency Rate                    | `float`     |     |       |                                 |
| `expense_ids`                               | Expense                                   | `one2many`  |     |       | hr.expense                      |
| `fiscal_position_id`                        | Fiscal Position                           | `many2one`  |     |       | account.fiscal.position         |
| `foreign_currency_id`                       | Foreign Currency                          | `many2one`  |     | ✅    | res.currency                    |
| `has_message`                               | Has Message                               | `boolean`   |     |       |                                 |
| `has_reconciled_entries`                    | Has Reconciled Entries                    | `boolean`   |     |       |                                 |
| `hide_post_button`                          | Hide Post Button                          | `boolean`   |     |       |                                 |
| `highest_name`                              | Highest Name                              | `char`      |     |       |                                 |
| `highlight_send_button`                     | Highlight Send Button                     | `boolean`   |     |       |                                 |
| `id`                                        | ID                                        | `integer`   |     | ✅    |                                 |
| `inalterable_hash`                          | Inalterability Hash                       | `char`      |     |       |                                 |
| `incoterm_location`                         | Incoterm Location                         | `char`      |     |       |                                 |
| `internal_index`                            | Internal Reference                        | `char`      |     | ✅    |                                 |
| `invoice_cash_rounding_id`                  | Cash Rounding Method                      | `many2one`  |     |       | account.cash.rounding           |
| `invoice_currency_rate`                     | Currency Rate                             | `float`     |     |       |                                 |
| `invoice_date`                              | Invoice/Bill Date                         | `date`      |     |       |                                 |
| `invoice_date_due`                          | Due Date                                  | `date`      |     |       |                                 |
| `invoice_filter_type_domain`                | Invoice Filter Type Domain                | `char`      |     |       |                                 |
| `invoice_has_outstanding`                   | Invoice Has Outstanding                   | `boolean`   |     |       |                                 |
| `invoice_incoterm_id`                       | Incoterm                                  | `many2one`  |     |       | account.incoterms               |
| `invoice_incoterm_placeholder`              | Invoice Incoterm Placeholder              | `char`      |     |       |                                 |
| `invoice_line_ids`                          | Invoice lines                             | `one2many`  |     |       | account.move.line               |
| `invoice_origin`                            | Origin                                    | `char`      |     |       |                                 |
| `invoice_outstanding_credits_debits_widget` | Invoice Outstanding Credits Debits Widget | `binary`    |     |       |                                 |
| `invoice_partner_display_name`              | Invoice Partner Display Name              | `char`      |     |       |                                 |
| `invoice_payments_widget`                   | Invoice Payments Widget                   | `binary`    |     |       |                                 |
| `invoice_payment_term_id`                   | Payment Terms                             | `many2one`  |     |       | account.payment.term            |
| `invoice_pdf_report_file`                   | PDF File                                  | `binary`    |     |       |                                 |
| `invoice_pdf_report_id`                     | PDF Attachment                            | `many2one`  |     |       | ir.attachment                   |
| `invoice_source_email`                      | Source Email                              | `char`      |     |       |                                 |
| `invoice_user_id`                           | Salesperson                               | `many2one`  |     |       | res.users                       |
| `invoice_vendor_bill_id`                    | Vendor Bill                               | `many2one`  |     |       | account.move                    |
| `is_being_sent`                             | Is Being Sent                             | `boolean`   |     |       |                                 |
| `is_draft_duplicated_ref_ids`               | Is Draft Duplicated Ref                   | `boolean`   |     |       |                                 |
| `is_manually_modified`                      | Is Manually Modified                      | `boolean`   |     |       |                                 |
| `is_move_sent`                              | Is Move Sent                              | `boolean`   |     |       |                                 |
| `is_purchase_matched`                       | Is Purchase Matched                       | `boolean`   |     |       |                                 |
| `is_reconciled`                             | Is Reconciled                             | `boolean`   |     | ✅    |                                 |
| `is_sale_installed`                         | Is Sale Installed                         | `boolean`   |     |       |                                 |
| `is_storno`                                 | Is Storno                                 | `boolean`   |     |       |                                 |
| `journal_group_id`                          | Ledger                                    | `many2one`  |     |       | account.journal.group           |
| `journal_id`                                | Journal                                   | `many2one`  | ✅  | ✅    | account.journal                 |
| `journal_line_ids`                          | Journal Items (DEPRECATED)                | `one2many`  |     |       | account.move.line               |
| `line_ids`                                  | Journal Items                             | `one2many`  |     |       | account.move.line               |
| `made_sequence_gap`                         | Made Sequence Gap                         | `boolean`   |     |       |                                 |
| `matched_payment_ids`                       | Matched Payments                          | `many2many` |     |       | account.payment                 |
| `medium_id`                                 | Medium                                    | `many2one`  |     |       | utm.medium                      |
| `message_attachment_count`                  | Attachment Count                          | `integer`   |     |       |                                 |
| `message_follower_ids`                      | Followers                                 | `one2many`  |     |       | mail.followers                  |
| `message_has_error`                         | Message Delivery error                    | `boolean`   |     |       |                                 |
| `message_has_error_counter`                 | Number of errors                          | `integer`   |     |       |                                 |
| `message_has_sms_error`                     | SMS Delivery error                        | `boolean`   |     |       |                                 |
| `message_ids`                               | Messages                                  | `one2many`  |     |       | mail.message                    |
| `message_is_follower`                       | Is Follower                               | `boolean`   |     |       |                                 |
| `message_main_attachment_id`                | Main Attachment                           | `many2one`  |     |       | ir.attachment                   |
| `message_needaction`                        | Action Needed                             | `boolean`   |     |       |                                 |
| `message_needaction_counter`                | Number of Actions                         | `integer`   |     |       |                                 |
| `message_partner_ids`                       | Followers (Partners)                      | `many2many` |     |       | res.partner                     |
| `move_id`                                   | Journal Entry                             | `many2one`  | ✅  | ✅    | account.move                    |
| `move_sent_values`                          | Sent                                      | `selection` |     |       |                                 |
| `move_type`                                 | Type                                      | `selection` | ✅  |       |                                 |
| `my_activity_date_deadline`                 | My Activity Deadline                      | `date`      |     |       |                                 |
| `name`                                      | Number                                    | `char`      |     |       |                                 |
| `name_placeholder`                          | Name Placeholder                          | `char`      |     |       |                                 |
| `narration`                                 | Terms and Conditions                      | `html`      |     |       |                                 |
| `nb_expenses`                               | Number of Expenses                        | `integer`   |     |       |                                 |
| `need_cancel_request`                       | Need Cancel Request                       | `boolean`   |     |       |                                 |
| `needed_terms`                              | Needed Terms                              | `binary`    |     |       |                                 |
| `needed_terms_dirty`                        | Needed Terms Dirty                        | `boolean`   |     |       |                                 |
| `next_payment_date`                         | Next Payment Date                         | `date`      |     |       |                                 |
| `no_followup`                               | No Follow-Up                              | `boolean`   |     |       |                                 |
| `origin_payment_id`                         | Payment                                   | `many2one`  |     |       | account.payment                 |
| `partner_bank_id`                           | Recipient Bank                            | `many2one`  |     |       | res.partner.bank                |
| `partner_credit_warning`                    | Partner Credit Warning                    | `text`      |     |       |                                 |
| `partner_id`                                | Partner                                   | `many2one`  |     | ✅    | res.partner                     |
| `partner_name`                              | Partner Name                              | `char`      |     | ✅    |                                 |
| `partner_shipping_id`                       | Delivery Address                          | `many2one`  |     |       | res.partner                     |
| `payment_count`                             | Payment Count                             | `integer`   |     |       |                                 |
| `payment_ids`                               | Auto-generated Payments                   | `many2many` |     | ✅    | account.payment                 |
| `payment_ref`                               | Label                                     | `char`      |     | ✅    |                                 |
| `payment_reference`                         | Payment Reference                         | `char`      |     |       |                                 |
| `payment_state`                             | Payment Status                            | `selection` |     |       |                                 |
| `payment_term_details`                      | Payment Term Details                      | `binary`    |     |       |                                 |
| `posted_before`                             | Posted Before                             | `boolean`   |     |       |                                 |
| `preferred_payment_method_line_id`          | Preferred Payment Method Line             | `many2one`  |     |       | account.payment.method.line     |
| `purchase_id`                               | Purchase Order                            | `many2one`  |     |       | purchase.order                  |
| `purchase_order_count`                      | Purchase Order Count                      | `integer`   |     |       |                                 |
| `purchase_order_name`                       | Purchase Order Name                       | `char`      |     |       |                                 |
| `purchase_vendor_bill_id`                   | Auto-complete                             | `many2one`  |     |       | purchase.bill.union             |
| `purchase_warning_text`                     | Purchase Warning                          | `text`      |     |       |                                 |
| `qr_code_method`                            | Payment QR-code                           | `selection` |     |       |                                 |
| `quick_edit_mode`                           | Quick Edit Mode                           | `boolean`   |     |       |                                 |
| `quick_edit_total_amount`                   | Total (Tax inc.)                          | `monetary`  |     |       |                                 |
| `quick_encoding_vals`                       | Quick Encoding Vals                       | `json`      |     |       |                                 |
| `rating_ids`                                | Ratings                                   | `one2many`  |     |       | rating.rating                   |
| `reconciled_payment_ids`                    | Reconciled Payments                       | `many2many` |     |       | account.payment                 |
| `ref`                                       | Reference                                 | `char`      |     |       |                                 |
| `restrict_mode_hash_table`                  | Secure Posted Entries with Hash           | `boolean`   |     |       |                                 |
| `reversal_move_ids`                         | Reversal Move                             | `one2many`  |     |       | account.move                    |
| `reversed_entry_id`                         | Reversal of                               | `many2one`  |     |       | account.move                    |
| `running_balance`                           | Running Balance                           | `monetary`  |     |       |                                 |
| `sale_order_count`                          | Sale Order Count                          | `integer`   |     |       |                                 |
| `sale_warning_text`                         | Sale Warning                              | `text`      |     |       |                                 |
| `secured`                                   | Secured                                   | `boolean`   |     |       |                                 |
| `secure_sequence_number`                    | Inalterability No Gap Sequence #          | `integer`   |     |       |                                 |
| `sending_data`                              | Sending Data                              | `json`      |     |       |                                 |
| `sequence`                                  | Sequence                                  | `integer`   |     | ✅    |                                 |
| `sequence_number`                           | Sequence Number                           | `integer`   |     |       |                                 |
| `sequence_prefix`                           | Sequence Prefix                           | `char`      |     |       |                                 |
| `show_delivery_date`                        | Show Delivery Date                        | `boolean`   |     |       |                                 |
| `show_discount_details`                     | Show Discount Details                     | `boolean`   |     |       |                                 |
| `show_journal`                              | Show Journal                              | `boolean`   |     |       |                                 |
| `show_name_warning`                         | Show Name Warning                         | `boolean`   |     |       |                                 |
| `show_payment_term_details`                 | Show Payment Term Details                 | `boolean`   |     |       |                                 |
| `show_reset_to_draft_button`                | Show Reset To Draft Button                | `boolean`   |     |       |                                 |
| `show_taxable_supply_date`                  | Show Taxable Supply Date                  | `boolean`   |     |       |                                 |
| `show_update_fpos`                          | Has Fiscal Position Changed               | `boolean`   |     |       |                                 |
| `source_id`                                 | Source                                    | `many2one`  |     |       | utm.source                      |
| `state`                                     | Status                                    | `selection` | ✅  |       |                                 |
| `statement_balance_end_real`                | Ending Balance                            | `monetary`  |     |       |                                 |
| `statement_complete`                        | Is Complete                               | `boolean`   |     |       |                                 |
| `statement_id`                              | Statement                                 | `many2one`  |     | ✅    | account.bank.statement          |
| `statement_line_id`                         | Statement Line                            | `many2one`  |     |       | account.bank.statement.line     |
| `statement_line_ids`                        | Statements                                | `one2many`  |     |       | account.bank.statement.line     |
| `statement_name`                            | Statement Name                            | `char`      |     |       |                                 |
| `statement_valid`                           | Is Valid                                  | `boolean`   |     |       |                                 |
| `status_in_payment`                         | Status In Payment                         | `selection` |     |       |                                 |
| `stock_move_ids`                            | Stock Move                                | `one2many`  |     |       | stock.move                      |
| `suitable_journal_ids`                      | Suitable Journal                          | `many2many` |     |       | account.journal                 |
| `taxable_supply_date`                       | Taxable Supply Date                       | `date`      |     |       |                                 |
| `taxable_supply_date_placeholder`           | Taxable Supply Date Placeholder           | `char`      |     |       |                                 |
| `tax_calculation_rounding_method`           | Tax calculation rounding method           | `selection` |     |       |                                 |
| `tax_cash_basis_created_move_ids`           | Cash Basis Entries                        | `one2many`  |     |       | account.move                    |
| `tax_cash_basis_origin_move_id`             | Cash Basis Origin                         | `many2one`  |     |       | account.move                    |
| `tax_cash_basis_rec_id`                     | Tax Cash Basis Entry of                   | `many2one`  |     |       | account.partial.reconcile       |
| `tax_country_code`                          | Tax Country Code                          | `char`      |     |       |                                 |
| `tax_country_id`                            | Tax Country                               | `many2one`  |     |       | res.country                     |
| `taxes_legal_notes`                         | Taxes Legal Notes                         | `html`      |     |       |                                 |
| `tax_lock_date_message`                     | Tax Lock Date Message                     | `char`      |     |       |                                 |
| `tax_totals`                                | Invoice Totals                            | `binary`    |     |       |                                 |
| `team_id`                                   | Sales Team                                | `many2one`  |     |       | crm.team                        |
| `transaction_count`                         | Transaction Count                         | `integer`   |     |       |                                 |
| `transaction_details`                       | Transaction Details                       | `json`      |     | ✅    |                                 |
| `transaction_ids`                           | Transactions                              | `many2many` |     |       | payment.transaction             |
| `transaction_type`                          | Transaction Type                          | `char`      |     | ✅    |                                 |
| `type_name`                                 | Type Name                                 | `char`      |     |       |                                 |
| `ubl_cii_xml_file`                          | UBL/CII File                              | `binary`    |     |       |                                 |
| `ubl_cii_xml_filename`                      | UBL/CII Filename                          | `char`      |     |       |                                 |
| `ubl_cii_xml_id`                            | Attachment                                | `many2one`  |     |       | ir.attachment                   |
| `user_id`                                   | User                                      | `many2one`  |     |       | res.users                       |
| `website_id`                                | Website                                   | `many2one`  |     |       | website                         |
| `website_message_ids`                       | Website Messages                          | `one2many`  |     |       | mail.message                    |
| `write_date`                                | Last Updated on                           | `datetime`  |     | ✅    |                                 |
| `write_uid`                                 | Last Updated by                           | `many2one`  |     | ✅    | res.users                       |

**Access Rights:**

| Name                                      | Group                  | Perms     |
| ----------------------------------------- | ---------------------- | --------- |
| account.bank.statement.line.group.invoice | Accounting / Invoicing | `R`       |
| account.bank.statement.line.group.invoice | Auditor                | `R`       |
| account.bank.statement.line               | Basic                  | `R/W/C/D` |

**Record Rules:**

- **Account bank statement line company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`

### 🗃️ `account.document.import.mixin` — Business document import mixin

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `base.document.layout` — Company Document Layout

> ✳️ Transient (Wizard)

    Customise the company document layout and display a live preview

**Fields:**

| Field                       | Label                       | Type        | Req | Store | Relation           |
| --------------------------- | --------------------------- | ----------- | --- | ----- | ------------------ |
| `account_number`            | Account Number              | `char`      |     |       |                    |
| `company_details`           | Company Details             | `html`      |     |       |                    |
| `company_id`                | Company                     | `many2one`  | ✅  | ✅    | res.company        |
| `country_id`                | Country                     | `many2one`  |     |       | res.country        |
| `create_date`               | Created on                  | `datetime`  |     | ✅    |                    |
| `create_uid`                | Created by                  | `many2one`  |     | ✅    | res.users          |
| `custom_colors`             | Custom Colors               | `boolean`   |     |       |                    |
| `display_name`              | Display Name                | `char`      |     |       |                    |
| `email`                     | Email                       | `char`      |     |       |                    |
| `external_report_layout_id` | Document Template           | `many2one`  |     |       | ir.ui.view         |
| `font`                      | Font                        | `selection` |     |       |                    |
| `from_invoice`              | From Invoice                | `boolean`   |     | ✅    |                    |
| `id`                        | ID                          | `integer`   |     | ✅    |                    |
| `is_company_details_empty`  | Is Company Details Empty    | `boolean`   |     |       |                    |
| `layout_background`         | Layout Background           | `selection` |     |       |                    |
| `layout_background_image`   | Background Image            | `binary`    |     |       |                    |
| `logo`                      | Company Logo                | `binary`    |     |       |                    |
| `logo_primary_color`        | Logo Primary Color          | `char`      |     |       |                    |
| `logo_secondary_color`      | Logo Secondary Color        | `char`      |     |       |                    |
| `name`                      | Company Name                | `char`      |     |       |                    |
| `paperformat_id`            | Paper format                | `many2one`  |     |       | report.paperformat |
| `partner_id`                | Partner                     | `many2one`  |     |       | res.partner        |
| `phone`                     | Phone                       | `char`      |     |       |                    |
| `preview`                   | Preview                     | `html`      |     |       |                    |
| `preview_logo`              | Preview logo                | `binary`    |     |       |                    |
| `primary_color`             | Primary Color               | `char`      |     |       |                    |
| `qr_code`                   | Display QR-code on invoices | `boolean`   |     |       |                    |
| `report_footer`             | Report Footer               | `html`      |     |       |                    |
| `report_header`             | Company Tagline             | `html`      |     |       |                    |
| `report_layout_id`          | Report Layout               | `many2one`  |     | ✅    | report.layout      |
| `secondary_color`           | Secondary Color             | `char`      |     |       |                    |
| `vat`                       | Tax ID                      | `char`      |     |       |                    |
| `website`                   | Website Link                | `char`      |     |       |                    |
| `write_date`                | Last Updated on             | `datetime`  |     | ✅    |                    |
| `write_uid`                 | Last Updated by             | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                        | Group                | Perms   |
| --------------------------- | -------------------- | ------- |
| access.base.document.layout | Role / Administrator | `R/W/C` |

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

### 🗃️ `res.country.group` — Country Group

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label             | Type        | Req | Store | Relation          |
| ------------------- | ----------------- | ----------- | --- | ----- | ----------------- |
| `code`              | Code              | `char`      |     | ✅    |                   |
| `country_ids`       | Countries         | `many2many` |     | ✅    | res.country       |
| `create_date`       | Created on        | `datetime`  |     | ✅    |                   |
| `create_uid`        | Created by        | `many2one`  |     | ✅    | res.users         |
| `display_name`      | Display Name      | `char`      |     |       |                   |
| `exclude_state_ids` | Fiscal Exceptions | `many2many` |     | ✅    | res.country.state |
| `id`                | ID                | `integer`   |     | ✅    |                   |
| `name`              | Name              | `char`      | ✅  | ✅    |                   |
| `pricelist_ids`     | Pricelists        | `many2many` |     | ✅    | product.pricelist |
| `write_date`        | Last Updated on   | `datetime`  |     | ✅    |                   |
| `write_uid`         | Last Updated by   | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                             | Group              | Perms     |
| -------------------------------- | ------------------ | --------- |
| res_country_group group_user     | Contact / Creation | `R/W/C/D` |
| res_country_group group_user_all | Role / Portal      | `R`       |
| res_country_group group_user_all | Role / Public      | `R`       |
| res_country_group group_user_all | Role / User        | `R`       |

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

### 🗃️ `res.currency` — Currency

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                       | Type        | Req | Store | Relation          |
| ----------------------------- | --------------------------- | ----------- | --- | ----- | ----------------- |
| `active`                      | Active                      | `boolean`   |     | ✅    |                   |
| `create_date`                 | Created on                  | `datetime`  |     | ✅    |                   |
| `create_uid`                  | Created by                  | `many2one`  |     | ✅    | res.users         |
| `currency_subunit_label`      | Currency Subunit            | `char`      |     | ✅    |                   |
| `currency_unit_label`         | Currency Unit               | `char`      |     | ✅    |                   |
| `date`                        | Date                        | `date`      |     |       |                   |
| `decimal_places`              | Decimal Places              | `integer`   |     | ✅    |                   |
| `display_name`                | Display Name                | `char`      |     |       |                   |
| `display_rounding_warning`    | Display Rounding Warning    | `boolean`   |     |       |                   |
| `fiscal_country_codes`        | Fiscal Country Codes        | `char`      |     |       |                   |
| `full_name`                   | Name                        | `char`      |     | ✅    |                   |
| `id`                          | ID                          | `integer`   |     | ✅    |                   |
| `inverse_rate`                | Inverse Rate                | `float`     |     |       |                   |
| `is_current_company_currency` | Is Current Company Currency | `boolean`   |     |       |                   |
| `iso_numeric`                 | Currency numeric code.      | `integer`   |     | ✅    |                   |
| `name`                        | Currency                    | `char`      | ✅  | ✅    |                   |
| `position`                    | Symbol Position             | `selection` |     | ✅    |                   |
| `rate`                        | Current Rate                | `float`     |     |       |                   |
| `rate_ids`                    | Rates                       | `one2many`  |     | ✅    | res.currency.rate |
| `rate_string`                 | Rate String                 | `char`      |     |       |                   |
| `rounding`                    | Rounding Factor             | `float`     |     | ✅    |                   |
| `symbol`                      | Symbol                      | `char`      | ✅  | ✅    |                   |
| `write_date`                  | Last Updated on             | `datetime`  |     | ✅    |                   |
| `write_uid`                   | Last Updated by             | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                         | Group                | Perms     |
| ---------------------------- | -------------------- | --------- |
| res.currency account manager | Accounting / Advisor | `R/W/C/D` |
| res_currency group_system    | Role / Administrator | `R/W/C/D` |
| res_currency group_all       | Role / Portal        | `R`       |
| res_currency group_all       | Role / Public        | `R`       |
| res_currency group_all       | Role / User          | `R`       |

### 🗃️ `decimal.precision` — Decimal Precision

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `digits`       | Digits          | `integer`  | ✅  | ✅    |           |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Usage           | `char`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                            | Group                | Perms |
| ------------------------------- | -------------------- | ----- |
| decimal.precision configuration | Role / Administrator | `R/W` |

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

### 🗃️ `mail.template` — Email Templates

Templates for sending email

**Fields:**

| Field                 | Label                     | Type        | Req | Store | Relation              |
| --------------------- | ------------------------- | ----------- | --- | ----- | --------------------- |
| `active`              | Active                    | `boolean`   |     | ✅    |                       |
| `attachment_ids`      | Attachments               | `many2many` |     | ✅    | ir.attachment         |
| `auto_delete`         | Auto Delete               | `boolean`   |     | ✅    |                       |
| `body_html`           | Body                      | `html`      |     | ✅    |                       |
| `can_write`           | Can Write                 | `boolean`   |     |       |                       |
| `create_date`         | Created on                | `datetime`  |     | ✅    |                       |
| `create_uid`          | Created by                | `many2one`  |     | ✅    | res.users             |
| `description`         | Template Description      | `text`      |     | ✅    |                       |
| `display_name`        | Display Name              | `char`      |     |       |                       |
| `email_cc`            | Cc                        | `char`      |     | ✅    |                       |
| `email_from`          | Send From                 | `char`      |     | ✅    |                       |
| `email_layout_xmlid`  | Email Notification Layout | `char`      |     | ✅    |                       |
| `email_to`            | To (Emails)               | `char`      |     | ✅    |                       |
| `has_dynamic_reports` | Has Dynamic Reports       | `boolean`   |     |       |                       |
| `has_mail_server`     | Has Mail Server           | `boolean`   |     |       |                       |
| `id`                  | ID                        | `integer`   |     | ✅    |                       |
| `is_template_editor`  | Is Template Editor        | `boolean`   |     |       |                       |
| `lang`                | Language                  | `char`      |     | ✅    |                       |
| `mail_server_id`      | Outgoing Mail Server      | `many2one`  |     | ✅    | ir.mail_server        |
| `model`               | Related Document Model    | `char`      |     | ✅    |                       |
| `model_id`            | Applies to                | `many2one`  |     | ✅    | ir.model              |
| `name`                | Name                      | `char`      |     | ✅    |                       |
| `partner_to`          | To (Partners)             | `char`      |     | ✅    |                       |
| `ref_ir_act_window`   | Sidebar action            | `many2one`  |     | ✅    | ir.actions.act_window |
| `render_model`        | Rendering Model           | `char`      |     |       |                       |
| `reply_to`            | Reply To                  | `char`      |     | ✅    |                       |
| `report_template_ids` | Dynamic Reports           | `many2many` |     | ✅    | ir.actions.report     |
| `scheduled_date`      | Scheduled Date            | `char`      |     | ✅    |                       |
| `subject`             | Subject                   | `char`      |     | ✅    |                       |
| `template_category`   | Template Category         | `selection` |     |       |                       |
| `template_fs`         | Template Filename         | `char`      |     | ✅    |                       |
| `use_default_to`      | Default Recipients        | `boolean`   |     | ✅    |                       |
| `user_id`             | Owner                     | `many2one`  |     | ✅    | res.users             |
| `write_date`          | Last Updated on           | `datetime`  |     | ✅    |                       |
| `write_uid`           | Last Updated by           | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                        | Group                | Perms     |
| --------------------------- | -------------------- | --------- |
| mail.template_editor        | Mail Template Editor | `R/W/C/D` |
| mail.template_system        | Role / Administrator | `R/W/C/D` |
| access_mail_template_portal | Role / Portal        | `R/W/C/D` |
| access_mail_template_public | Role / Public        | `R/W/C/D` |
| mail.template               | Role / User          | `R/W/C/D` |

**Record Rules:**

- **Employees can only modify templates they have created or been assigned** (1) `W/C/D`
  - Domain: `['|', ('create_uid', '=', user.id), ('user_id', '=', user.id)]`
- **Mail Template Editors - Edit All Templates** (17, 4) `W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `account.fiscal.position` — Fiscal Position

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label                       | Type        | Req | Store | Relation                        |
| ------------------------- | --------------------------- | ----------- | --- | ----- | ------------------------------- |
| `account_ids`             | Account Mapping             | `one2many`  |     | ✅    | account.fiscal.position.account |
| `account_map`             | Account Map                 | `binary`    |     |       |                                 |
| `active`                  | Active                      | `boolean`   |     | ✅    |                                 |
| `auto_apply`              | Detect Automatically        | `boolean`   |     | ✅    |                                 |
| `company_country_id`      | Company Country             | `many2one`  |     |       | res.country                     |
| `company_id`              | Company                     | `many2one`  | ✅  | ✅    | res.company                     |
| `country_group_id`        | Country Group               | `many2one`  |     | ✅    | res.country.group               |
| `country_id`              | Country                     | `many2one`  |     | ✅    | res.country                     |
| `create_date`             | Created on                  | `datetime`  |     | ✅    |                                 |
| `create_uid`              | Created by                  | `many2one`  |     | ✅    | res.users                       |
| `display_name`            | Display Name                | `char`      |     |       |                                 |
| `fiscal_country_codes`    | Company Fiscal Country Code | `char`      |     |       |                                 |
| `foreign_vat`             | Foreign Tax ID              | `char`      |     | ✅    |                                 |
| `foreign_vat_header_mode` | Foreign Vat Header Mode     | `selection` |     |       |                                 |
| `id`                      | ID                          | `integer`   |     | ✅    |                                 |
| `is_domestic`             | Is Domestic                 | `boolean`   |     | ✅    |                                 |
| `name`                    | Fiscal Position             | `char`      | ✅  | ✅    |                                 |
| `note`                    | Notes                       | `html`      |     | ✅    |                                 |
| `sequence`                | Sequence                    | `integer`   |     | ✅    |                                 |
| `state_ids`               | Federal States              | `many2many` |     | ✅    | res.country.state               |
| `states_count`            | States Count                | `integer`   |     |       |                                 |
| `tax_ids`                 | Taxes                       | `many2many` |     | ✅    | account.tax                     |
| `tax_map`                 | Tax Map                     | `binary`    |     |       |                                 |
| `vat_required`            | VAT required                | `boolean`   |     | ✅    |                                 |
| `write_date`              | Last Updated on             | `datetime`  |     | ✅    |                                 |
| `write_uid`               | Last Updated by             | `many2one`  |     | ✅    | res.users                       |
| `zip_from`                | Zip Range From              | `char`      |     | ✅    |                                 |
| `zip_to`                  | Zip Range To                | `char`      |     | ✅    |                                 |

**Access Rights:**

| Name                                    | Group                | Perms     |
| --------------------------------------- | -------------------- | --------- |
| account.fiscal.position account.manager | Accounting / Advisor | `R/W/C/D` |
| account.fiscal.position purchase        | Purchase / User      | `R`       |
| fiscal position public                  | Role / Portal        | `R`       |
| account.fiscal.position all             | Role / User          | `R`       |

**Record Rules:**

- **Account fiscal Mapping company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'parent_of', company_ids)]`

### 🗃️ `account.full.reconcile` — Full Reconcile

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                   | Label                 | Type       | Req | Store | Relation                  |
| ----------------------- | --------------------- | ---------- | --- | ----- | ------------------------- |
| `create_date`           | Created on            | `datetime` |     | ✅    |                           |
| `create_uid`            | Created by            | `many2one` |     | ✅    | res.users                 |
| `display_name`          | Display Name          | `char`     |     |       |                           |
| `id`                    | ID                    | `integer`  |     | ✅    |                           |
| `partial_reconcile_ids` | Reconciliation Parts  | `one2many` |     | ✅    | account.partial.reconcile |
| `reconciled_line_ids`   | Matched Journal Items | `one2many` |     | ✅    | account.move.line         |
| `write_date`            | Last Updated on       | `datetime` |     | ✅    |                           |
| `write_uid`             | Last Updated by       | `many2one` |     | ✅    | res.users                 |

**Access Rights:**

| Name                                 | Group                  | Perms     |
| ------------------------------------ | ---------------------- | --------- |
| account.full.reconcile.group.invoice | Accounting / Invoicing | `R/W/C/D` |
| account.full.reconcile               | Contact / Accountant   | `R/W/C/D` |
| account.full.reconcile.group.invoice | Auditor                | `R`       |

### 🗃️ `report.account.report_hash_integrity` — Get hash integrity result as PDF.

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.http` — HTTP Routing

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `account.incoterms` — Incoterms

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `active`       | Active          | `boolean`  |     | ✅    |           |
| `code`         | Code            | `char`     | ✅  | ✅    |           |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Name            | `char`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                      | Group                | Perms     |
| ------------------------- | -------------------- | --------- |
| account.incoterms manager | Accounting / Advisor | `R/W/C/D` |
| account.incoterms all     | Role / User          | `R`       |

### 🗃️ `account.invoice.report` — Invoices Statistics

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label                      | Type        | Req | Store | Relation                |
| ------------------------- | -------------------------- | ----------- | --- | ----- | ----------------------- |
| `account_id`              | Revenue/Expense Account    | `many2one`  |     | ✅    | account.account         |
| `commercial_partner_id`   | Main Partner               | `many2one`  |     | ✅    | res.partner             |
| `company_currency_id`     | Company Currency           | `many2one`  |     | ✅    | res.currency            |
| `company_id`              | Company                    | `many2one`  |     | ✅    | res.company             |
| `country_id`              | Country                    | `many2one`  |     | ✅    | res.country             |
| `currency_id`             | Currency                   | `many2one`  |     | ✅    | res.currency            |
| `display_name`            | Display Name               | `char`      |     |       |                         |
| `fiscal_position_id`      | Fiscal Position            | `many2one`  |     | ✅    | account.fiscal.position |
| `id`                      | ID                         | `integer`   |     | ✅    |                         |
| `inventory_value`         | Inventory Value            | `float`     |     | ✅    |                         |
| `invoice_date`            | Invoice Date               | `date`      |     | ✅    |                         |
| `invoice_date_due`        | Due Date                   | `date`      |     | ✅    |                         |
| `invoice_user_id`         | Salesperson                | `many2one`  |     | ✅    | res.users               |
| `journal_id`              | Journal                    | `many2one`  |     | ✅    | account.journal         |
| `move_id`                 | Move                       | `many2one`  |     | ✅    | account.move            |
| `move_type`               | Move Type                  | `selection` |     | ✅    |                         |
| `partner_id`              | Partner                    | `many2one`  |     | ✅    | res.partner             |
| `payment_state`           | Payment Status             | `selection` |     | ✅    |                         |
| `price_average`           | Average Price              | `float`     |     | ✅    |                         |
| `price_margin`            | Margin                     | `float`     |     | ✅    |                         |
| `price_subtotal`          | Untaxed Amount             | `float`     |     | ✅    |                         |
| `price_subtotal_currency` | Untaxed Amount in Currency | `float`     |     | ✅    |                         |
| `price_total`             | Total                      | `float`     |     | ✅    |                         |
| `price_total_currency`    | Total in Currency          | `float`     |     | ✅    |                         |
| `product_categ_id`        | Product Category           | `many2one`  |     | ✅    | product.category        |
| `product_id`              | Product                    | `many2one`  |     | ✅    | product.product         |
| `product_uom_id`          | Unit                       | `many2one`  |     | ✅    | uom.uom                 |
| `quantity`                | Product Quantity           | `float`     |     | ✅    |                         |
| `state`                   | Invoice Status             | `selection` |     | ✅    |                         |
| `team_id`                 | Sales Team                 | `many2one`  |     | ✅    | crm.team                |

**Access Rights:**

| Name                           | Group                  | Perms |
| ------------------------------ | ---------------------- | ----- |
| account.invoice.report_billing | Accounting / Invoicing | `R`   |
| account.invoice.report         | Accounting / Advisor   | `R`   |
| account.invoice.report_user    | Auditor                | `R`   |

**Record Rules:**

- **Invoice Analysis multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`
- **Personal Invoices Analysis** (25) `R/W/C/D`
  - Domain: `['|', ('invoice_user_id', '=', user.id), ('invoice_user_id', '=', False)]`
- **All Invoices Analysis** (26) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

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

### 🗃️ `kpi.provider` — KPI Provider

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `mail.tracking.value` — Mail Tracking Value

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label                     | Type       | Req | Store | Relation        |
| -------------------- | ------------------------- | ---------- | --- | ----- | --------------- |
| `create_date`        | Created on                | `datetime` |     | ✅    |                 |
| `create_uid`         | Created by                | `many2one` |     | ✅    | res.users       |
| `currency_id`        | Currency                  | `many2one` |     | ✅    | res.currency    |
| `display_name`       | Display Name              | `char`     |     |       |                 |
| `field_id`           | Field                     | `many2one` |     | ✅    | ir.model.fields |
| `field_info`         | Removed field information | `json`     |     | ✅    |                 |
| `id`                 | ID                        | `integer`  |     | ✅    |                 |
| `mail_message_id`    | Message ID                | `many2one` | ✅  | ✅    | mail.message    |
| `new_value_char`     | New Value Char            | `char`     |     | ✅    |                 |
| `new_value_datetime` | New Value Datetime        | `datetime` |     | ✅    |                 |
| `new_value_float`    | New Value Float           | `float`    |     | ✅    |                 |
| `new_value_integer`  | New Value Integer         | `integer`  |     | ✅    |                 |
| `new_value_text`     | New Value Text            | `text`     |     | ✅    |                 |
| `old_value_char`     | Old Value Char            | `char`     |     | ✅    |                 |
| `old_value_datetime` | Old Value DateTime        | `datetime` |     | ✅    |                 |
| `old_value_float`    | Old Value Float           | `float`    |     | ✅    |                 |
| `old_value_integer`  | Old Value Integer         | `integer`  |     | ✅    |                 |
| `old_value_text`     | Old Value Text            | `text`     |     | ✅    |                 |
| `write_date`         | Last Updated on           | `datetime` |     | ✅    |                 |
| `write_uid`          | Last Updated by           | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                       | Group                | Perms     |
| -------------------------- | -------------------- | --------- |
| mail.tracking.value.system | Role / Administrator | `R/W/C/D` |

### 🗃️ `account.code.mapping` — Mapping of account codes per company

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label        | Type       | Req | Store | Relation        |
| -------------- | ------------ | ---------- | --- | ----- | --------------- |
| `account_id`   | Account      | `many2one` |     |       | account.account |
| `code`         | Code         | `char`     |     |       |                 |
| `company_id`   | Company      | `many2one` |     |       | res.company     |
| `display_name` | Display Name | `char`     |     |       |                 |
| `id`           | ID           | `integer`  |     | ✅    |                 |

**Access Rights:**

| Name                 | Group                | Perms |
| -------------------- | -------------------- | ----- |
| account.code.mapping | Accounting / Advisor | `R/W` |
| account.code.mapping | Auditor              | `R`   |

### 🗃️ `base.partner.merge.automatic.wizard` — Merge Partner Wizard

> ✳️ Transient (Wizard)

        The idea behind this wizard is to create a list of potential partners to
        merge. We use two objects, the first one is the wizard for the end-user.
        And the second will contain the partner list to merge.

**Fields:**

| Field                  | Label                                   | Type        | Req | Store | Relation                |
| ---------------------- | --------------------------------------- | ----------- | --- | ----- | ----------------------- |
| `create_date`          | Created on                              | `datetime`  |     | ✅    |                         |
| `create_uid`           | Created by                              | `many2one`  |     | ✅    | res.users               |
| `current_line_id`      | Current Line                            | `many2one`  |     | ✅    | base.partner.merge.line |
| `display_name`         | Display Name                            | `char`      |     |       |                         |
| `dst_partner_id`       | Destination Contact                     | `many2one`  |     | ✅    | res.partner             |
| `exclude_contact`      | A user associated to the contact        | `boolean`   |     | ✅    |                         |
| `exclude_journal_item` | Journal Items associated to the contact | `boolean`   |     | ✅    |                         |
| `group_by_email`       | Email                                   | `boolean`   |     | ✅    |                         |
| `group_by_is_company`  | Is Company                              | `boolean`   |     | ✅    |                         |
| `group_by_name`        | Name                                    | `boolean`   |     | ✅    |                         |
| `group_by_parent_id`   | Parent Company                          | `boolean`   |     | ✅    |                         |
| `group_by_vat`         | VAT                                     | `boolean`   |     | ✅    |                         |
| `id`                   | ID                                      | `integer`   |     | ✅    |                         |
| `line_ids`             | Lines                                   | `one2many`  |     | ✅    | base.partner.merge.line |
| `maximum_group`        | Maximum of Group of Contacts            | `integer`   |     | ✅    |                         |
| `number_group`         | Group of Contacts                       | `integer`   |     | ✅    |                         |
| `partner_ids`          | Contacts                                | `many2many` |     | ✅    | res.partner             |
| `state`                | State                                   | `selection` | ✅  | ✅    |                         |
| `write_date`           | Last Updated on                         | `datetime`  |     | ✅    |                         |
| `write_uid`            | Last Updated by                         | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name                                       | Group              | Perms   |
| ------------------------------------------ | ------------------ | ------- |
| access.base.partner.merge.automatic.wizard | Contact / Creation | `R/W/C` |

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

### 🗃️ `ir.module.module` — Module

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                             | Label                           | Type        | Req | Store | Relation                    |
| --------------------------------- | ------------------------------- | ----------- | --- | ----- | --------------------------- |
| `account_templates`               | Account Templates               | `binary`    |     |       |                             |
| `application`                     | Application                     | `boolean`   |     | ✅    |                             |
| `author`                          | Author                          | `char`      |     | ✅    |                             |
| `auto_install`                    | Automatic Installation          | `boolean`   |     | ✅    |                             |
| `category_id`                     | Category                        | `many2one`  |     | ✅    | ir.module.category          |
| `contributors`                    | Contributors                    | `text`      |     | ✅    |                             |
| `country_ids`                     | Country                         | `many2many` |     | ✅    | res.country                 |
| `create_date`                     | Created on                      | `datetime`  |     | ✅    |                             |
| `create_uid`                      | Created by                      | `many2one`  |     | ✅    | res.users                   |
| `demo`                            | Demo Data                       | `boolean`   |     | ✅    |                             |
| `dependencies_id`                 | Dependencies                    | `one2many`  |     | ✅    | ir.module.module.dependency |
| `description`                     | Description                     | `text`      |     | ✅    |                             |
| `description_html`                | Description HTML                | `html`      |     |       |                             |
| `display_name`                    | Display Name                    | `char`      |     |       |                             |
| `exclusion_ids`                   | Exclusions                      | `one2many`  |     | ✅    | ir.module.module.exclusion  |
| `has_iap`                         | Has Iap                         | `boolean`   |     |       |                             |
| `icon`                            | Icon URL                        | `char`      |     | ✅    |                             |
| `icon_flag`                       | Flag                            | `char`      |     |       |                             |
| `icon_image`                      | Icon                            | `binary`    |     |       |                             |
| `id`                              | ID                              | `integer`   |     | ✅    |                             |
| `image_ids`                       | Screenshots                     | `one2many`  |     | ✅    | ir.attachment               |
| `imported`                        | Imported Module                 | `boolean`   |     | ✅    |                             |
| `installed_version`               | Latest Version                  | `char`      |     |       |                             |
| `is_installed_on_current_website` | Is Installed On Current Website | `boolean`   |     |       |                             |
| `latest_version`                  | Installed Version               | `char`      |     | ✅    |                             |
| `license`                         | License                         | `selection` |     | ✅    |                             |
| `maintainer`                      | Maintainer                      | `char`      |     | ✅    |                             |
| `menus_by_module`                 | Menus                           | `text`      |     | ✅    |                             |
| `module_type`                     | Module Type                     | `selection` |     | ✅    |                             |
| `name`                            | Technical Name                  | `char`      | ✅  | ✅    |                             |
| `published_version`               | Published Version               | `char`      |     | ✅    |                             |
| `reports_by_module`               | Reports                         | `text`      |     | ✅    |                             |
| `sequence`                        | Sequence                        | `integer`   |     | ✅    |                             |
| `shortdesc`                       | Module Name                     | `char`      |     | ✅    |                             |
| `state`                           | Status                          | `selection` |     | ✅    |                             |
| `summary`                         | Summary                         | `char`      |     | ✅    |                             |
| `to_buy`                          | Odoo Enterprise Module          | `boolean`   |     | ✅    |                             |
| `url`                             | URL                             | `char`      |     | ✅    |                             |
| `views_by_module`                 | Views                           | `text`      |     | ✅    |                             |
| `website`                         | Website                         | `char`      |     | ✅    |                             |
| `write_date`                      | Last Updated on                 | `datetime`  |     | ✅    |                             |
| `write_uid`                       | Last Updated by                 | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                        | Group                | Perms     |
| --------------------------- | -------------------- | --------- |
| ir_module_module group_user | Role / Administrator | `R/W/C/D` |
| ir_module_module group_user | Role / User          | `R`       |

### 🗃️ `onboarding.onboarding.step` — Onboarding Step

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                               | Type        | Req | Store | Relation                 |
| ----------------------------- | ----------------------------------- | ----------- | --- | ----- | ------------------------ |
| `button_text`                 | Button text                         | `char`      | ✅  | ✅    |                          |
| `create_date`                 | Created on                          | `datetime`  |     | ✅    |                          |
| `create_uid`                  | Created by                          | `many2one`  |     | ✅    | res.users                |
| `current_progress_step_id`    | Step Progress                       | `many2one`  |     |       | onboarding.progress.step |
| `current_step_state`          | Completion State                    | `selection` |     |       |                          |
| `description`                 | Description                         | `char`      |     | ✅    |                          |
| `display_name`                | Display Name                        | `char`      |     |       |                          |
| `done_icon`                   | Font Awesome Icon when completed    | `char`      |     | ✅    |                          |
| `done_text`                   | Text to show when step is completed | `char`      |     | ✅    |                          |
| `id`                          | ID                                  | `integer`   |     | ✅    |                          |
| `is_per_company`              | Is per company                      | `boolean`   |     | ✅    |                          |
| `onboarding_ids`              | Onboardings                         | `many2many` |     | ✅    | onboarding.onboarding    |
| `panel_step_open_action_name` | Opening action                      | `char`      |     | ✅    |                          |
| `progress_ids`                | Onboarding Progress Step Records    | `one2many`  |     | ✅    | onboarding.progress.step |
| `sequence`                    | Sequence                            | `integer`   |     | ✅    |                          |
| `step_image`                  | Step Image                          | `binary`    |     | ✅    |                          |
| `step_image_alt`              | Alt Text for the Step Image         | `char`      |     | ✅    |                          |
| `step_image_filename`         | Step Image Filename                 | `char`      |     | ✅    |                          |
| `title`                       | Title                               | `char`      |     | ✅    |                          |
| `write_date`                  | Last Updated on                     | `datetime`  |     | ✅    |                          |
| `write_uid`                   | Last Updated by                     | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                               | Group                | Perms     |
| ---------------------------------- | -------------------- | --------- |
| onboarding.onboarding.step.manager | Role / Administrator | `R/W/C/D` |
| onboarding.onboarding.step.user    | Role / User          | `-`       |
| onboarding.onboarding.step.all     | Everyone             | `-`       |

### 🗃️ `account.financial.year.op` — Opening Balance of Financial Year

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                   | Label                 | Type        | Req | Store | Relation    |
| ----------------------- | --------------------- | ----------- | --- | ----- | ----------- |
| `company_id`            | Company               | `many2one`  | ✅  | ✅    | res.company |
| `create_date`           | Created on            | `datetime`  |     | ✅    |             |
| `create_uid`            | Created by            | `many2one`  |     | ✅    | res.users   |
| `display_name`          | Display Name          | `char`      |     |       |             |
| `fiscalyear_last_day`   | Fiscalyear Last Day   | `integer`   | ✅  |       |             |
| `fiscalyear_last_month` | Fiscalyear Last Month | `selection` | ✅  |       |             |
| `id`                    | ID                    | `integer`   |     | ✅    |             |
| `opening_date`          | Opening Date          | `date`      | ✅  |       |             |
| `opening_move_posted`   | Opening Move Posted   | `boolean`   |     |       |             |
| `write_date`            | Last Updated on       | `datetime`  |     | ✅    |             |
| `write_uid`             | Last Updated by       | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                             | Group                | Perms   |
| -------------------------------- | -------------------- | ------- |
| access.account.financial.year.op | Accounting / Advisor | `R/W/C` |

### 🗃️ `account.partial.reconcile` — Partial Reconcile

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                    | Label                                          | Type       | Req | Store | Relation               |
| ------------------------ | ---------------------------------------------- | ---------- | --- | ----- | ---------------------- |
| `amount`                 | Amount                                         | `monetary` |     | ✅    |                        |
| `company_currency_id`    | Company Currency                               | `many2one` |     |       | res.currency           |
| `company_id`             | Company                                        | `many2one` |     | ✅    | res.company            |
| `create_date`            | Created on                                     | `datetime` |     | ✅    |                        |
| `create_uid`             | Created by                                     | `many2one` |     | ✅    | res.users              |
| `credit_amount_currency` | Credit Amount Currency                         | `monetary` |     | ✅    |                        |
| `credit_currency_id`     | Currency of the credit journal item.           | `many2one` |     | ✅    | res.currency           |
| `credit_move_id`         | Credit Move                                    | `many2one` | ✅  | ✅    | account.move.line      |
| `debit_amount_currency`  | Debit Amount Currency                          | `monetary` |     | ✅    |                        |
| `debit_currency_id`      | Currency of the debit journal item.            | `many2one` |     | ✅    | res.currency           |
| `debit_move_id`          | Debit Move                                     | `many2one` | ✅  | ✅    | account.move.line      |
| `display_name`           | Display Name                                   | `char`     |     |       |                        |
| `draft_caba_move_vals`   | Values that created the draft cash-basis entry | `json`     |     | ✅    |                        |
| `exchange_move_id`       | Exchange Move                                  | `many2one` |     | ✅    | account.move           |
| `full_reconcile_id`      | Full Reconcile                                 | `many2one` |     | ✅    | account.full.reconcile |
| `id`                     | ID                                             | `integer`  |     | ✅    |                        |
| `max_date`               | Max Date of Matched Lines                      | `date`     |     | ✅    |                        |
| `write_date`             | Last Updated on                                | `datetime` |     | ✅    |                        |
| `write_uid`              | Last Updated by                                | `many2one` |     | ✅    | res.users              |

**Access Rights:**

| Name                                    | Group                            | Perms     |
| --------------------------------------- | -------------------------------- | --------- |
| account_partial_reconcile salesman      | Sales / User: Own Documents Only | `R`       |
| account.partial.reconcile.group.invoice | Accounting / Invoicing           | `R/W/C/D` |
| account.partial.reconcile.purchase.user | Purchase / User                  | `R`       |
| account.partial.reconcile               | Contact / Accountant             | `R/W/C/D` |
| account.partial.reconcile               | Inventory / Administrator        | `R/W/C/D` |
| account.partial.reconcile.readonly      | Auditor                          | `R`       |

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

### 🗃️ `account.payment.term` — Payment Terms

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                       | Type        | Req | Store | Relation                  |
| -------------------------------- | --------------------------- | ----------- | --- | ----- | ------------------------- |
| `active`                         | Active                      | `boolean`   |     | ✅    |                           |
| `company_id`                     | Company                     | `many2one`  |     | ✅    | res.company               |
| `create_date`                    | Created on                  | `datetime`  |     | ✅    |                           |
| `create_uid`                     | Created by                  | `many2one`  |     | ✅    | res.users                 |
| `currency_id`                    | Currency                    | `many2one`  |     |       | res.currency              |
| `discount_days`                  | Discount Days               | `integer`   |     | ✅    |                           |
| `discount_percentage`            | Discount %                  | `float`     |     | ✅    |                           |
| `display_name`                   | Display Name                | `char`      |     |       |                           |
| `display_on_invoice`             | Show installment dates      | `boolean`   |     | ✅    |                           |
| `early_discount`                 | Early Discount              | `boolean`   |     | ✅    |                           |
| `early_pay_discount_computation` | Cash Discount Tax Reduction | `selection` |     | ✅    |                           |
| `example_amount`                 | Example Amount              | `monetary`  |     |       |                           |
| `example_date`                   | Date example                | `date`      |     |       |                           |
| `example_invalid`                | Example Invalid             | `boolean`   |     |       |                           |
| `example_preview`                | Example Preview             | `html`      |     |       |                           |
| `example_preview_discount`       | Example Preview Discount    | `html`      |     |       |                           |
| `fiscal_country_codes`           | Fiscal Country Codes        | `char`      |     |       |                           |
| `id`                             | ID                          | `integer`   |     | ✅    |                           |
| `line_ids`                       | Terms                       | `one2many`  |     | ✅    | account.payment.term.line |
| `name`                           | Payment Terms               | `char`      | ✅  | ✅    |                           |
| `note`                           | Description on the Invoice  | `html`      |     | ✅    |                           |
| `sequence`                       | Sequence                    | `integer`   | ✅  | ✅    |                           |
| `write_date`                     | Last Updated on             | `datetime`  |     | ✅    |                           |
| `write_uid`                      | Last Updated by             | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name                                 | Group                            | Perms     |
| ------------------------------------ | -------------------------------- | --------- |
| account_payment_term salesman        | Sales / User: Own Documents Only | `R`       |
| account.payment.term                 | Accounting / Advisor             | `R/W/C/D` |
| account.payment.term                 | Role / Portal                    | `R`       |
| payment term public                  | Role / Portal                    | `R`       |
| account.payment.term partner manager | Role / User                      | `R`       |

**Record Rules:**

- **Account payment term company rule** (Global) `R/W/C/D`
  - Domain:
    `['|', ('company_id', '=', False), ('company_id', 'parent_of', company_ids)]`

### 🗃️ `account.payment.term.line` — Payment Terms Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label                   | Type        | Req | Store | Relation             |
| ------------------------- | ----------------------- | ----------- | --- | ----- | -------------------- |
| `create_date`             | Created on              | `datetime`  |     | ✅    |                      |
| `create_uid`              | Created by              | `many2one`  |     | ✅    | res.users            |
| `days_next_month`         | Days on the next month  | `char`      |     | ✅    |                      |
| `delay_type`              | Delay Type              | `selection` | ✅  | ✅    |                      |
| `display_days_next_month` | Display Days Next Month | `boolean`   |     |       |                      |
| `display_name`            | Display Name            | `char`      |     |       |                      |
| `id`                      | ID                      | `integer`   |     | ✅    |                      |
| `nb_days`                 | Days                    | `integer`   |     | ✅    |                      |
| `payment_id`              | Payment Terms           | `many2one`  | ✅  | ✅    | account.payment.term |
| `value`                   | Value                   | `selection` | ✅  | ✅    |                      |
| `value_amount`            | Due                     | `float`     |     | ✅    |                      |
| `write_date`              | Last Updated on         | `datetime`  |     | ✅    |                      |
| `write_uid`               | Last Updated by         | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                                      | Group                | Perms     |
| ----------------------------------------- | -------------------- | --------- |
| account.payment.term.line                 | Accounting / Advisor | `R/W/C/D` |
| account.payment.term.line partner manager | Role / User          | `R`       |

### 🗃️ `product.catalog.mixin` — Product Catalog Mixin

This mixin should be inherited when the model should be able to work with the product
catalog. It assumes the model using this mixin has a O2M field where the products are
added/removed and this field's co-related model should has a method named
`_get_product_catalog_lines_data`.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `uom.uom` — Product Unit of Measure

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label                | Type        | Req | Store | Relation           |
| ---------------------- | -------------------- | ----------- | --- | ----- | ------------------ |
| `active`               | Active               | `boolean`   |     | ✅    |                    |
| `create_date`          | Created on           | `datetime`  |     | ✅    |                    |
| `create_uid`           | Created by           | `many2one`  |     | ✅    | res.users          |
| `display_name`         | Display Name         | `char`      |     |       |                    |
| `factor`               | Absolute Quantity    | `float`     |     | ✅    |                    |
| `fiscal_country_codes` | Fiscal Country Codes | `char`      |     |       |                    |
| `id`                   | ID                   | `integer`   |     | ✅    |                    |
| `name`                 | Unit Name            | `char`      | ✅  | ✅    |                    |
| `package_type_id`      | Package Type         | `many2one`  |     | ✅    | stock.package.type |
| `parent_path`          | Parent Path          | `char`      |     | ✅    |                    |
| `product_uom_ids`      | Barcodes             | `one2many`  |     | ✅    | product.uom        |
| `related_uom_ids`      | Related UoMs         | `one2many`  |     | ✅    | uom.uom            |
| `relative_factor`      | Contains             | `float`     | ✅  | ✅    |                    |
| `relative_uom_id`      | Reference Unit       | `many2one`  |     | ✅    | uom.uom            |
| `rounding`             | Rounding Precision   | `float`     |     |       |                    |
| `route_ids`            | Routes               | `many2many` |     |       | stock.route        |
| `sequence`             | Sequence             | `integer`   |     | ✅    |                    |
| `write_date`           | Last Updated on      | `datetime`  |     | ✅    |                    |
| `write_uid`            | Last Updated by      | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                    | Group                            | Perms     |
| ----------------------- | -------------------------------- | --------- |
| uom.uom.user            | Sales / User: Own Documents Only | `R`       |
| uom.uom.product.manager | Products / Create                | `R/W/C/D` |
| uom.uom.manager         | Role / Administrator             | `R/W/C/D` |
| uom.uom portal          | Role / Portal                    | `R`       |
| uom.uom public          | Role / Public                    | `R`       |
| uom.uom.user            | Role / User                      | `R`       |

### 🗃️ `account.resequence.wizard` — Remake the sequence of Journal Entries.

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                   | Label                 | Type        | Req | Store | Relation     |
| ----------------------- | --------------------- | ----------- | --- | ----- | ------------ |
| `create_date`           | Created on            | `datetime`  |     | ✅    |              |
| `create_uid`            | Created by            | `many2one`  |     | ✅    | res.users    |
| `display_name`          | Display Name          | `char`      |     |       |              |
| `end_date`              | End Date              | `date`      |     | ✅    |              |
| `first_date`            | First Date            | `date`      |     | ✅    |              |
| `first_name`            | First New Sequence    | `char`      | ✅  | ✅    |              |
| `id`                    | ID                    | `integer`   |     | ✅    |              |
| `move_ids`              | Move                  | `many2many` |     | ✅    | account.move |
| `new_values`            | New Values            | `text`      |     |       |              |
| `ordering`              | Ordering              | `selection` | ✅  | ✅    |              |
| `preview_moves`         | Preview Moves         | `text`      |     |       |              |
| `sequence_number_reset` | Sequence Number Reset | `char`      |     |       |              |
| `write_date`            | Last Updated on       | `datetime`  |     | ✅    |              |
| `write_uid`             | Last Updated by       | `many2one`  |     | ✅    | res.users    |

**Access Rights:**

| Name                             | Group                | Perms   |
| -------------------------------- | -------------------- | ------- |
| access.account.resequence.wizard | Accounting / Advisor | `R/W/C` |

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

### 🗃️ `account.reconcile.model.line` — Rules for the reconciliation model

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                               | Label                         | Type        | Req | Store | Relation                 |
| ----------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------ |
| `account_id`                        | Account                       | `many2one`  |     | ✅    | account.account          |
| `amount`                            | Float Amount                  | `float`     |     | ✅    |                          |
| `amount_string`                     | Amount                        | `char`      | ✅  | ✅    |                          |
| `amount_type`                       | Amount Type                   | `selection` | ✅  | ✅    |                          |
| `analytic_distribution`             | Analytic Distribution         | `json`      |     | ✅    |                          |
| `analytic_precision`                | Analytic Precision            | `integer`   |     |       |                          |
| `company_id`                        | Company                       | `many2one`  |     | ✅    | res.company              |
| `create_date`                       | Created on                    | `datetime`  |     | ✅    |                          |
| `create_uid`                        | Created by                    | `many2one`  |     | ✅    | res.users                |
| `display_name`                      | Display Name                  | `char`      |     |       |                          |
| `distribution_analytic_account_ids` | Distribution Analytic Account | `many2many` |     |       | account.analytic.account |
| `id`                                | ID                            | `integer`   |     | ✅    |                          |
| `label`                             | Label                         | `char`      |     | ✅    |                          |
| `model_id`                          | Model                         | `many2one`  |     | ✅    | account.reconcile.model  |
| `partner_id`                        | Partner                       | `many2one`  |     | ✅    | res.partner              |
| `sequence`                          | Sequence                      | `integer`   | ✅  | ✅    |                          |
| `tax_ids`                           | Taxes                         | `many2many` |     | ✅    | account.tax              |
| `write_date`                        | Last Updated on               | `datetime`  |     | ✅    |                          |
| `write_uid`                         | Last Updated by               | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                                  | Group                  | Perms     |
| ------------------------------------- | ---------------------- | --------- |
| account.reconcile.model.line.billing  | Accounting / Invoicing | `R/C`     |
| account.reconcile.model.line.readonly | Auditor                | `R`       |
| account.reconcile.model.line          | Basic                  | `R/W/C/D` |

**Record Rules:**

- **Account reconcile model_line template company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'parent_of', company_ids)]`

### 🗃️ `account.secure.entries.wizard` — Secure Journal Entries

> ✳️ Transient (Wizard)

    This wizard is used to secure journal entries (with a hash)

**Fields:**

| Field                                  | Label                            | Type        | Req | Store | Relation                    |
| -------------------------------------- | -------------------------------- | ----------- | --- | ----- | --------------------------- |
| `chains_to_hash_with_gaps`             | Chains To Hash With Gaps         | `json`      |     |       |                             |
| `company_id`                           | Company                          | `many2one`  | ✅  | ✅    | res.company                 |
| `country_code`                         | Country Code                     | `char`      |     |       |                             |
| `create_date`                          | Created on                       | `datetime`  |     | ✅    |                             |
| `create_uid`                           | Created by                       | `many2one`  |     | ✅    | res.users                   |
| `display_name`                         | Display Name                     | `char`      |     |       |                             |
| `hash_date`                            | Hash All Entries                 | `date`      | ✅  | ✅    |                             |
| `id`                                   | ID                               | `integer`   |     | ✅    |                             |
| `max_hash_date`                        | Max Hash Date                    | `date`      |     |       |                             |
| `move_to_hash_ids`                     | Move To Hash                     | `many2many` |     |       | account.move                |
| `not_hashable_unlocked_move_ids`       | Not Hashable Unlocked Move       | `many2many` |     |       | account.move                |
| `unreconciled_bank_statement_line_ids` | Unreconciled Bank Statement Line | `many2many` |     |       | account.bank.statement.line |
| `warnings`                             | Warnings                         | `json`      |     |       |                             |
| `write_date`                           | Last Updated on                  | `datetime`  |     | ✅    |                             |
| `write_uid`                            | Last Updated by                  | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                                 | Group                | Perms   |
| ------------------------------------ | -------------------- | ------- |
| access.account.secure.entries.wizard | Accounting / Advisor | `R/W/C` |

### 🗃️ `account.tax.group` — Tax Group

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                  | Type       | Req | Store | Relation        |
| -------------------------------- | ---------------------- | ---------- | --- | ----- | --------------- |
| `advance_tax_payment_account_id` | Tax Advance Account    | `many2one` |     | ✅    | account.account |
| `company_id`                     | Company                | `many2one` | ✅  | ✅    | res.company     |
| `country_code`                   | Country Code           | `char`     |     |       |                 |
| `country_id`                     | Country                | `many2one` |     | ✅    | res.country     |
| `create_date`                    | Created on             | `datetime` |     | ✅    |                 |
| `create_uid`                     | Created by             | `many2one` |     | ✅    | res.users       |
| `display_name`                   | Display Name           | `char`     |     |       |                 |
| `id`                             | ID                     | `integer`  |     | ✅    |                 |
| `name`                           | Name                   | `char`     | ✅  | ✅    |                 |
| `pos_receipt_label`              | PoS receipt label      | `char`     |     | ✅    |                 |
| `preceding_subtotal`             | Preceding Subtotal     | `char`     |     | ✅    |                 |
| `sequence`                       | Sequence               | `integer`  |     | ✅    |                 |
| `tax_payable_account_id`         | Tax Payable Account    | `many2one` |     | ✅    | account.account |
| `tax_receivable_account_id`      | Tax Receivable Account | `many2one` |     | ✅    | account.account |
| `write_date`                     | Last Updated on        | `datetime` |     | ✅    |                 |
| `write_uid`                      | Last Updated by        | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                            | Group                            | Perms     |
| ------------------------------- | -------------------------------- | --------- |
| account.tax.group sale manager  | Sales / User: Own Documents Only | `R`       |
| account.tax.group               | Accounting / Invoicing           | `R`       |
| account.tax.group               | Accounting / Advisor             | `R/W/C/D` |
| account.tax.group               | Auditor                          | `R`       |
| account.tax.group internal user | Role / User                      | `R`       |

**Record Rules:**

- **Tax group multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'parent_of', company_ids)]`

### 🗃️ `account.tax.repartition.line` — Tax Repartition Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label             | Type        | Req | Store | Relation            |
| -------------------- | ----------------- | ----------- | --- | ----- | ------------------- |
| `account_id`         | Account           | `many2one`  |     | ✅    | account.account     |
| `company_id`         | Company           | `many2one`  |     | ✅    | res.company         |
| `create_date`        | Created on        | `datetime`  |     | ✅    |                     |
| `create_uid`         | Created by        | `many2one`  |     | ✅    | res.users           |
| `display_name`       | Display Name      | `char`      |     |       |                     |
| `document_type`      | Related to        | `selection` | ✅  | ✅    |                     |
| `factor`             | Factor Ratio      | `float`     |     |       |                     |
| `factor_percent`     | %                 | `float`     | ✅  | ✅    |                     |
| `id`                 | ID                | `integer`   |     | ✅    |                     |
| `repartition_type`   | Based On          | `selection` | ✅  | ✅    |                     |
| `sequence`           | Sequence          | `integer`   |     | ✅    |                     |
| `tag_ids`            | Tax Grids         | `many2many` |     | ✅    | account.account.tag |
| `tag_ids_domain`     | tag domain        | `binary`    |     |       |                     |
| `tax_id`             | Tax               | `many2one`  |     | ✅    | account.tax         |
| `use_in_tax_closing` | Tax Closing Entry | `boolean`   |     | ✅    |                     |
| `write_date`         | Last Updated on   | `datetime`  |     | ✅    |                     |
| `write_uid`          | Last Updated by   | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                                 | Group                  | Perms     |
| ------------------------------------ | ---------------------- | --------- |
| account.tax repartition.line.invoice | Accounting / Invoicing | `R`       |
| account.tax repartition.line.manager | Accounting / Advisor   | `R/W/C/D` |
| account.tax repartition.line.invoice | Auditor                | `R`       |
| account.tax repartition.line.user    | Role / User            | `R`       |

**Record Rules:**

- **Tax Repartition multi-company** (Global) `R/W/C/D`
  - Domain: `['|',('company_id','=',False), ('company_id', 'parent_of', company_ids)]`

### 🗃️ `validate.account.move` — Validate Account Move

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                         | Label                   | Type        | Req | Store | Relation     |
| ----------------------------- | ----------------------- | ----------- | --- | ----- | ------------ |
| `abnormal_amount_partner_ids` | Abnormal Amount Partner | `one2many`  |     |       | res.partner  |
| `abnormal_date_partner_ids`   | Abnormal Date Partner   | `one2many`  |     |       | res.partner  |
| `create_date`                 | Created on              | `datetime`  |     | ✅    |              |
| `create_uid`                  | Created by              | `many2one`  |     | ✅    | res.users    |
| `display_force_hash`          | Display Force Hash      | `boolean`   |     |       |              |
| `display_force_post`          | Display Force Post      | `boolean`   |     |       |              |
| `display_name`                | Display Name            | `char`      |     |       |              |
| `force_hash`                  | Force Hash              | `boolean`   |     | ✅    |              |
| `force_post`                  | Force                   | `boolean`   |     | ✅    |              |
| `id`                          | ID                      | `integer`   |     | ✅    |              |
| `ignore_abnormal_amount`      | Ignore Abnormal Amount  | `boolean`   |     | ✅    |              |
| `ignore_abnormal_date`        | Ignore Abnormal Date    | `boolean`   |     | ✅    |              |
| `is_entries`                  | Is Entries              | `boolean`   |     |       |              |
| `move_ids`                    | Move                    | `many2many` |     | ✅    | account.move |
| `write_date`                  | Last Updated on         | `datetime`  |     | ✅    |              |
| `write_uid`                   | Last Updated by         | `many2one`  |     | ✅    | res.users    |

**Access Rights:**

| Name                         | Group                  | Perms   |
| ---------------------------- | ---------------------- | ------- |
| access.validate.account.move | Accounting / Invoicing | `R/W/C` |
