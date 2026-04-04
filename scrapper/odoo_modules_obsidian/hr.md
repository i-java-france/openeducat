---
title: "Employees"
module: "hr"
state: "installed"
version: "19.0.1.1"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/app/employees"
license: "LGPL-3"
category: "Employees"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________, odoo/app]
---

# 🟢 Employees

> **Module:** `hr` | **Version:** `19.0.1.1` **Category:** Employees | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** https://www.odoo.com/app/employees

## 🔗 Dependencies

[[base_setup]] [[digest]] [[phone_validation]] [[resource_mail]] [[web]]

## 📖 Description

# Odoo Human Resources

With Odoo <a href="<https://www.odoo.com/app/employees>">Human Resources</a>, manage the
most important asset in your company: People

Get all your HR operations managed easily: knowledge sharing, recruitments, appraisals,
timesheets, contracts, attendances, payroll, etc.

Each need is provided by a specific app that you activate on demand.

# Manage Your Employees

Oversee all important information in your company address book. Some information are
restricted to HR managers, others are public to easily look colleagues.

Record employee contracts and get alerts when they have to be renewed.

# Streamline Your Recruitment Process

Index resumes, track applicants, search profiles with
<a href="<https://www.odoo.com/app/employees>">Odoo HR</a>.

Post job offers and keep track of each application received. Follow applicants in your
recruitment process with the smart kanban view.

Save time by automating some communications with email templates. Resumes are indexed
automatically, allowing you to easily find for specific profiles.

# Enterprise Social Network

Break down information silos. Share knowledge and best practices amongst all employees.
Follow specific people or documents and join groups of interests to share expertise and
documents.

Interact with your coworkers in real time with website live chat.

# Track time and attendances

Keep track of the time spent by project, client or task. It's easy to record timesheets
or check attendances for each employee. Get your analytic accounting posted
automatically based on time spent on your projects.

# Time Off Management

Keep track of the vacation days accrued by each employee. Employees enter their requests
(paid time off, sick time off, etc), for managers to approve and validate. It's all done
in just a few clicks. The agenda of each employee is updated accordingly.

# Keep Track of Employee Expenses

Get rid of the paper work and follow employee's expenses directly in Odoo. Don't loose
time or money by controlling the full flow: expense validation, reimbursement of
employees, posting in the accounting and re-invoicing to customers.

# Follow Periodic Appraisals

Set-up appraisals plans and/or surveys for your employees and watch their evolution.
Define steps for interviews and Odoo will notify managers or subordinates automatically
to prepare appraisals. Keep track of the progress of your staff periodically.

# Boost Engagement With Gamification

### Define clear objective and provide real time feedback

Inspire achievement with challenges, goals and rewards. Define clear objectives and
provide real time feedback and tangible results. Showcase the top performers to the
entire channel and publicly recognize a job well done.

### Leaderboards

Promote leaders and competition amongst Sales Team with performance ratios.

### Personal Objectives

Assign clear goals to users to align them with the company objectives.

### Team Targets

Compare revenues with forecasts and budgets in real time.

## 🖥️ UI Components

### Menus

- `Employees`
- `Employees/Configuration`
- `Employees/Configuration/Employee`
- `Employees/Configuration/Employee/Departure Reasons`
- `Employees/Configuration/Employee/Onboarding / Offboarding`
- `Employees/Configuration/Employee/Tags`
- `Employees/Configuration/Employee/Work Locations`
- `Employees/Configuration/Employee/Working Schedules`
- `Employees/Configuration/Recruitment`
- `Employees/Configuration/Recruitment/Contract Templates`
- `Employees/Configuration/Recruitment/Employment Types`
- `Employees/Configuration/Recruitment/Job Positions`
- `Employees/Configuration/Settings`
- `Employees/Departments`
- `Employees/Directory`
- `Employees/Employees`
- `Employees/Human Resources`
- `Employees/Reporting`

### Views

- `* INHERIT discuss.channel.view.form.inherit.hr (form)`
- `* INHERIT mail.activity.plan.template.view.form.inherit.hr (form)`
- `* INHERIT mail.activity.plan.view.form.hr.employee (form)`
- `* INHERIT mail.activity.plan.view.form.inherit.hr (form)`
- `* INHERIT mail.activity.plan.view.list.inherit.hr (list)`
- `* INHERIT mail.activity.schedule.view.form.inherit.hr (form)`
- `* INHERIT res.config.settings.view.form.inherit.hr (form)`
- `* INHERIT res.partner.bank.form.inherit.hr (form)`
- `* INHERIT res.partner.search.inherit (search)`
- `* INHERIT res.partner.view.form.inherit.hr (form)`
- `* INHERIT res.users.form.inherit (form)`
- `* INHERIT res.users.preferences.form.inherit (form)`
- `* INHERIT res.users.preferences.form.resource (form)`
- `* INHERIT res.users.preferences.form.simplified.inherit (form)`
- `* INHERIT view.employee.form.smartbutton.inherited (form)`
- `* INHERIT view.users.simple.form.hr (form)`
- `* INHERIT view.users.simple.form.inherit.hr (form)`
- `hr.bank.account.allocation.wizard.form (form)`
- `hr.bank.account.allocation.wizard.line.list (list)`
- `hr.contract.template.form (form)`
- `hr.contract.template.list (list)`
- `hr.contract.type form (form)`
- `hr.contract.type list (list)`
- `hr.department.form (form)`
- `hr.department.kanban (kanban)`
- `hr.department.list (list)`
- `hr.department.search (search)`
- `hr.departure.reason form (form)`
- `hr.departure.reason list (list)`
- `hr.departure.wizard.view.form (form)`
- `hr.employee.activity (activity)`
- `hr.employee.category.form (form)`
- `hr.employee.category.list (list)`
- `hr.employee.form (form)`
- `hr.employee.kanban (kanban)`
- `hr.employee.kanban (kanban)`
- `hr.employee.list (list)`
- `hr.employee.list (list)`
- `hr.employee.list (list)`
- `hr.employee.list.activites.view (list)`
- `hr.employee.public.form (form)`
- `hr.employee.search (search)`
- `hr.employee.search (search)`
- `hr.employee.view.graph (graph)`
- `hr.employee.view.pivot (pivot)`
- `hr.job.form (form)`
- `hr.job.kanban (kanban)`
- `hr.job.list (list)`
- `hr.job.search (search)`
- `hr.version.graph (graph)`
- `hr.version.list (list)`
- `hr.version.pivot (pivot)`
- `hr.version.search (search)`
- `hr.version.wizard.view.form (form)`
- `hr.work.location.view.form (form)`
- `hr.work.location.view.list (list)`
- `hr_employee_plan_activity_summary (qweb)`
- `print_employee_badge (qweb)`

### Reports

- `Print Badge`

## 🛠️ Technical Documentation

**31 model(s) defined by this module:**

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

### 🗃️ `hr.department` — Department

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation           |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------ |
| `absence_of_today`              | Absence by Today              | `integer`   |     |       |                    |
| `active`                        | Active                        | `boolean`   |     | ✅    |                    |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event     |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                    |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                    |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                    |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity      |
| `activity_state`                | Activity State                | `selection` |     |       |                    |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                    |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                    |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users          |
| `allocation_to_approve_count`   | Allocation to Approve         | `integer`   |     |       |                    |
| `child_ids`                     | Child Departments             | `one2many`  |     | ✅    | hr.department      |
| `color`                         | Color Index                   | `integer`   |     | ✅    |                    |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company        |
| `complete_name`                 | Complete Name                 | `char`      |     |       |                    |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `expected_employee`             | Expected Employee             | `integer`   |     |       |                    |
| `expenses_to_approve_count`     | Expenses to Approve           | `integer`   |     |       |                    |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `has_read_access`               | Has Read Access               | `boolean`   |     |       |                    |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
| `jobs_ids`                      | Jobs                          | `one2many`  |     | ✅    | hr.job             |
| `leave_to_approve_count`        | Time Off to Approve           | `integer`   |     |       |                    |
| `manager_id`                    | Manager                       | `many2one`  |     | ✅    | hr.employee        |
| `master_department_id`          | Master Department             | `many2one`  |     | ✅    | hr.department      |
| `member_ids`                    | Members                       | `one2many`  |     | ✅    | hr.employee        |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                    |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                    |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                    |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                    |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                    |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                    |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                    |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner        |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                    |
| `name`                          | Department Name               | `char`      | ✅  | ✅    |                    |
| `new_applicant_count`           | New Applicant                 | `integer`   |     |       |                    |
| `new_hired_employee`            | New Hired Employee            | `integer`   |     |       |                    |
| `note`                          | Note                          | `text`      |     | ✅    |                    |
| `parent_id`                     | Parent Department             | `many2one`  |     | ✅    | hr.department      |
| `parent_path`                   | Parent Path                   | `char`      |     | ✅    |                    |
| `plan_ids`                      | Plan                          | `one2many`  |     | ✅    | mail.activity.plan |
| `plans_count`                   | Plans Count                   | `integer`   |     |       |                    |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `total_employee`                | Total Employee                | `integer`   |     |       |                    |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                   | Group                                     | Perms     |
| ---------------------- | ----------------------------------------- | --------- |
| hr.department.user     | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.department.public   | Role / Public                             | `R`       |
| hr.department.employee | Role / User                               | `R`       |

**Record Rules:**

- **Department multi company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Job department: Public** (11) `R`
  - Domain:
    `['|', ('jobs_ids.website_published', '=', True), ('child_ids', 'not in', [])]`

### 🗃️ `discuss.channel` — Discussion Channel

> 📧 Mail Thread

Chat Session Reprensenting a conversation between users. It extends the base method for
anonymous usage.

**Fields:**

| Field                                    | Label                                                                                       | Type        | Req | Store | Relation                           |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- | ----------- | --- | ----- | ---------------------------------- |
| `active`                                 | Active                                                                                      | `boolean`   |     | ✅    |                                    |
| `avatar_128`                             | Avatar                                                                                      | `binary`    |     |       |                                    |
| `avatar_cache_key`                       | Avatar Cache Key                                                                            | `char`      |     |       |                                    |
| `calendar_event_ids`                     | Calendar Event                                                                              | `one2many`  |     | ✅    | calendar.event                     |
| `call_history_ids`                       | Call History                                                                                | `one2many`  |     | ✅    | discuss.call.history               |
| `channel_member_ids`                     | Members                                                                                     | `one2many`  |     | ✅    | discuss.channel.member             |
| `channel_name_member_ids`                | Channel Name Member                                                                         | `one2many`  |     |       | discuss.channel.member             |
| `channel_partner_ids`                    | Partners                                                                                    | `many2many` |     |       | res.partner                        |
| `channel_type`                           | Channel Type                                                                                | `selection` | ✅  | ✅    |                                    |
| `chatbot_current_step_id`                | Chatbot Current Step                                                                        | `many2one`  |     | ✅    | chatbot.script.step                |
| `chatbot_message_ids`                    | Chatbot Messages                                                                            | `one2many`  |     | ✅    | chatbot.message                    |
| `country_id`                             | Country                                                                                     | `many2one`  |     | ✅    | res.country                        |
| `create_date`                            | Created on                                                                                  | `datetime`  |     | ✅    |                                    |
| `create_uid`                             | Created by                                                                                  | `many2one`  |     | ✅    | res.users                          |
| `default_display_mode`                   | Default Display Mode                                                                        | `selection` |     | ✅    |                                    |
| `description`                            | Description                                                                                 | `text`      |     | ✅    |                                    |
| `display_name`                           | Display Name                                                                                | `char`      |     |       |                                    |
| `duration`                               | Duration                                                                                    | `float`     |     |       |                                    |
| `faculty_id`                             | Faculty                                                                                     | `many2one`  |     | ✅    | op.faculty                         |
| `from_message_id`                        | From Message                                                                                | `many2one`  |     | ✅    | mail.message                       |
| `group_ids`                              | Auto Subscription                                                                           | `many2many` |     | ✅    | res.groups                         |
| `group_public_id`                        | Authorized Group                                                                            | `many2one`  |     | ✅    | res.groups                         |
| `has_crm_lead`                           | Has Crm Lead                                                                                | `boolean`   |     | ✅    |                                    |
| `has_message`                            | Has Message                                                                                 | `boolean`   |     |       |                                    |
| `id`                                     | ID                                                                                          | `integer`   |     | ✅    |                                    |
| `image_128`                              | Image                                                                                       | `binary`    |     | ✅    |                                    |
| `invitation_url`                         | Invitation URL                                                                              | `char`      |     |       |                                    |
| `invited_member_ids`                     | Invited Member                                                                              | `one2many`  |     |       | discuss.channel.member             |
| `is_created_student`                     | Is Created Student                                                                          | `boolean`   |     | ✅    |                                    |
| `is_editable`                            | Is Editable                                                                                 | `boolean`   |     |       |                                    |
| `is_member`                              | Is Member                                                                                   | `boolean`   |     |       |                                    |
| `is_pending_chat_request`                | When created from an operator, whether the channel is yet to be opened on the visitor side. | `boolean`   |     | ✅    |                                    |
| `last_interest_dt`                       | Last Interest                                                                               | `datetime`  |     | ✅    |                                    |
| `lead_ids`                               | Leads                                                                                       | `one2many`  |     | ✅    | crm.lead                           |
| `livechat_agent_history_ids`             | Agents (History)                                                                            | `one2many`  |     |       | im_livechat.channel.member.history |
| `livechat_agent_partner_ids`             | Agents                                                                                      | `many2many` |     | ✅    | res.partner                        |
| `livechat_agent_providing_help_history`  | Help Provided (Agent)                                                                       | `many2one`  |     | ✅    | im_livechat.channel.member.history |
| `livechat_agent_requesting_help_history` | Help Requested (Agent)                                                                      | `many2one`  |     | ✅    | im_livechat.channel.member.history |
| `livechat_bot_history_ids`               | Bots (History)                                                                              | `one2many`  |     |       | im_livechat.channel.member.history |
| `livechat_bot_partner_ids`               | Bots                                                                                        | `many2many` |     | ✅    | res.partner                        |
| `livechat_channel_id`                    | Channel                                                                                     | `many2one`  |     | ✅    | im_livechat.channel                |
| `livechat_channel_member_history_ids`    | Livechat Channel Member History                                                             | `one2many`  |     | ✅    | im_livechat.channel.member.history |
| `livechat_conversation_tag_ids`          | Live Chat Conversation Tags                                                                 | `many2many` |     | ✅    | im_livechat.conversation.tag       |
| `livechat_customer_guest_ids`            | Customers (Guests)                                                                          | `many2many` |     |       | mail.guest                         |
| `livechat_customer_history_ids`          | Customers (History)                                                                         | `one2many`  |     |       | im_livechat.channel.member.history |
| `livechat_customer_partner_ids`          | Customers (Partners)                                                                        | `many2many` |     | ✅    | res.partner                        |
| `livechat_end_dt`                        | Session end date                                                                            | `datetime`  |     | ✅    |                                    |
| `livechat_expertise_ids`                 | Livechat Expertise                                                                          | `many2many` |     | ✅    | im_livechat.expertise              |
| `livechat_failure`                       | Live Chat Session Failure                                                                   | `selection` |     | ✅    |                                    |
| `livechat_is_escalated`                  | Is session escalated                                                                        | `boolean`   |     | ✅    |                                    |
| `livechat_lang_id`                       | Language                                                                                    | `many2one`  |     | ✅    | res.lang                           |
| `livechat_matches_self_expertise`        | Livechat Matches Self Expertise                                                             | `boolean`   |     |       |                                    |
| `livechat_matches_self_lang`             | Livechat Matches Self Lang                                                                  | `boolean`   |     |       |                                    |
| `livechat_note`                          | Live Chat Note                                                                              | `html`      |     | ✅    |                                    |
| `livechat_operator_id`                   | Operator                                                                                    | `many2one`  |     | ✅    | res.partner                        |
| `livechat_outcome`                       | Livechat Outcome                                                                            | `selection` |     | ✅    |                                    |
| `livechat_start_hour`                    | Session Start Hour                                                                          | `float`     |     | ✅    |                                    |
| `livechat_state`                         | Livechat State                                                                              | `selection` |     | ✅    |                                    |
| `livechat_status`                        | Livechat Status                                                                             | `selection` |     | ✅    |                                    |
| `livechat_visitor_id`                    | Visitor                                                                                     | `many2one`  |     | ✅    | website.visitor                    |
| `livechat_week_day`                      | Day of the Week                                                                             | `selection` |     | ✅    |                                    |
| `member_count`                           | Member Count                                                                                | `integer`   |     |       |                                    |
| `message_attachment_count`               | Attachment Count                                                                            | `integer`   |     |       |                                    |
| `message_count`                          | # Messages                                                                                  | `integer`   |     |       |                                    |
| `message_follower_ids`                   | Followers                                                                                   | `one2many`  |     | ✅    | mail.followers                     |
| `message_has_error`                      | Message Delivery error                                                                      | `boolean`   |     |       |                                    |
| `message_has_error_counter`              | Number of errors                                                                            | `integer`   |     |       |                                    |
| `message_has_sms_error`                  | SMS Delivery error                                                                          | `boolean`   |     |       |                                    |
| `message_ids`                            | Messages                                                                                    | `one2many`  |     | ✅    | mail.message                       |
| `message_is_follower`                    | Is Follower                                                                                 | `boolean`   |     |       |                                    |
| `message_needaction`                     | Action Needed                                                                               | `boolean`   |     |       |                                    |
| `message_needaction_counter`             | Number of Actions                                                                           | `integer`   |     |       |                                    |
| `message_partner_ids`                    | Followers (Partners)                                                                        | `many2many` |     |       | res.partner                        |
| `name`                                   | Name                                                                                        | `char`      | ✅  | ✅    |                                    |
| `parent_channel_id`                      | Parent Channel                                                                              | `many2one`  |     | ✅    | discuss.channel                    |
| `pinned_message_ids`                     | Pinned Messages                                                                             | `one2many`  |     | ✅    | mail.message                       |
| `rating_avg`                             | Average Rating                                                                              | `float`     |     |       |                                    |
| `rating_avg_text`                        | Rating Avg Text                                                                             | `selection` |     |       |                                    |
| `rating_count`                           | Rating count                                                                                | `integer`   |     |       |                                    |
| `rating_ids`                             | Ratings                                                                                     | `one2many`  |     | ✅    | rating.rating                      |
| `rating_last_feedback`                   | Rating Last Feedback                                                                        | `text`      |     |       |                                    |
| `rating_last_image`                      | Rating Last Image                                                                           | `binary`    |     |       |                                    |
| `rating_last_text`                       | Rating Text                                                                                 | `selection` |     | ✅    |                                    |
| `rating_last_value`                      | Rating Last Value                                                                           | `float`     |     | ✅    |                                    |
| `rating_percentage_satisfaction`         | Rating Satisfaction                                                                         | `float`     |     |       |                                    |
| `rtc_session_ids`                        | Rtc Session                                                                                 | `one2many`  |     | ✅    | discuss.channel.rtc.session        |
| `self_member_id`                         | Self Member                                                                                 | `many2one`  |     |       | discuss.channel.member             |
| `sfu_channel_uuid`                       | Sfu Channel Uuid                                                                            | `char`      |     | ✅    |                                    |
| `sfu_server_url`                         | Sfu Server Url                                                                              | `char`      |     | ✅    |                                    |
| `student_id`                             | Student                                                                                     | `many2one`  |     | ✅    | op.student                         |
| `sub_channel_ids`                        | Sub Channels                                                                                | `one2many`  |     | ✅    | discuss.channel                    |
| `subscription_department_ids`            | HR Departments                                                                              | `many2many` |     | ✅    | hr.department                      |
| `uuid`                                   | UUID                                                                                        | `char`      |     | ✅    |                                    |
| `website_message_ids`                    | Website Messages                                                                            | `one2many`  |     | ✅    | mail.message                       |
| `whatsapp_contact`                       | Whatsapp Contact                                                                            | `many2one`  |     | ✅    | whatsapp.contact                   |
| `write_date`                             | Last Updated on                                                                             | `datetime`  |     | ✅    |                                    |
| `write_uid`                              | Last Updated by                                                                             | `many2one`  |     | ✅    | res.users                          |

**Access Rights:**

| Name                   | Group                | Perms     |
| ---------------------- | -------------------- | --------- |
| discuss.channel.system | Role / Administrator | `R/W/C/D` |
| discuss.channel.portal | Role / Portal        | `R`       |
| discuss.channel.portal | Role / Portal        | `R/W/C/D` |
| discuss.channel.public | Role / Public        | `R`       |
| discuss.channel.user   | Role / User          | `R/W/C`   |

**Record Rules:**

- **discuss.channel: can access channels (as member or as group allowed)** (10, 11, 1)
  `R/W/C/D`
  - Domain:
    `             [                 "|",                     "&",                         ("channel_type", "!=", "channel"),                         "|",                             ("is_member", "=", True),                             ("parent_channel_id.is_member", "=", True),                     "&",                         ("channel_type", "=", "channel"),                         "|",                             ("group_public_id", "=", False),                             ("group_public_id", "in", user.all_group_ids.ids),             ]         `
- **discuss.channel: admin full access** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **discuss.channel: livechat users can read all livechat channels** (51) `R`
  - Domain: `[('channel_type', '=', 'livechat')]`
- **discuss.channel: sales users can read lead's origin channel** (25) `R`
  - Domain: `[("has_crm_lead", "=", True)]`

### 🗃️ `hr.employee` — Employee

> 📧 Mail Thread

    NB: Any field only available on the model hr.employee (i.e. not on the
    hr.employee.public model) should have `groups="hr.group_hr_user"` on its
    definition to avoid being prefetched when the user hasn't access to the
    hr.employee model. Indeed, the prefetch loads the data for all the fields
    that are available according to the group defined on them.

**Fields:**

| Field                            | Label                           | Type         | Req | Store | Relation                  |
| -------------------------------- | ------------------------------- | ------------ | --- | ----- | ------------------------- |
| `active`                         | Active                          | `boolean`    |     | ✅    |                           |
| `active_employee`                | Active Employee                 | `boolean`    |     |       |                           |
| `activity_calendar_event_id`     | Next Activity Calendar Event    | `many2one`   |     |       | calendar.event            |
| `activity_date_deadline`         | Next Activity Deadline          | `date`       |     |       |                           |
| `activity_exception_decoration`  | Activity Exception Decoration   | `selection`  |     |       |                           |
| `activity_exception_icon`        | Icon                            | `char`       |     |       |                           |
| `activity_ids`                   | Activities                      | `one2many`   |     | ✅    | mail.activity             |
| `activity_state`                 | Activity State                  | `selection`  |     |       |                           |
| `activity_summary`               | Next Activity Summary           | `char`       |     |       |                           |
| `activity_type_icon`             | Activity Type Icon              | `char`       |     |       |                           |
| `activity_type_id`               | Next Activity Type              | `many2one`   |     |       | mail.activity.type        |
| `activity_user_id`               | Responsible User                | `many2one`   |     |       | res.users                 |
| `additional_note`                | Additional Note                 | `text`       |     |       |                           |
| `address_id`                     | Work Address                    | `many2one`   |     |       | res.partner               |
| `allocation_count`               | Total number of days allocated. | `float`      |     |       |                           |
| `allocation_display`             | Allocation Display              | `char`       |     |       |                           |
| `allocation_remaining_display`   | Allocation Remaining Display    | `char`       |     |       |                           |
| `allocations_count`              | Total number of allocations     | `integer`    |     |       |                           |
| `allowed_country_state_ids`      | Allowed Country State           | `many2many`  |     |       | res.country.state         |
| `applicant_ids`                  | Applicants                      | `one2many`   |     | ✅    | hr.applicant              |
| `avatar_1024`                    | Avatar 1024                     | `binary`     |     |       |                           |
| `avatar_128`                     | Avatar 128                      | `binary`     |     |       |                           |
| `avatar_1920`                    | Avatar                          | `binary`     |     |       |                           |
| `avatar_256`                     | Avatar 256                      | `binary`     |     |       |                           |
| `avatar_512`                     | Avatar 512                      | `binary`     |     |       |                           |
| `badge_ids`                      | Employee Badges                 | `one2many`   |     |       | gamification.badge.user   |
| `bank_account_ids`               | Bank Accounts                   | `many2many`  |     | ✅    | res.partner.bank          |
| `barcode`                        | Badge ID                        | `char`       |     | ✅    |                           |
| `birthday`                       | Birthday                        | `date`       |     | ✅    |                           |
| `birthday_public_display`        | Show to all employees           | `boolean`    |     | ✅    |                           |
| `birthday_public_display_string` | Public Date of Birth            | `char`       |     |       |                           |
| `car_ids`                        | Vehicles (private)              | `one2many`   |     | ✅    | fleet.vehicle             |
| `category_ids`                   | Tags                            | `many2many`  |     | ✅    | hr.employee.category      |
| `certificate`                    | Certificate Level               | `selection`  |     | ✅    |                           |
| `certification_ids`              | Certification                   | `one2many`   |     |       | hr.employee.skill         |
| `child_all_count`                | Indirect Subordinates Count     | `integer`    |     |       |                           |
| `child_count`                    | Direct Subordinates Count       | `integer`    |     |       |                           |
| `child_ids`                      | Direct subordinates             | `one2many`   |     | ✅    | hr.employee               |
| `children`                       | Dependent Children              | `integer`    |     |       |                           |
| `coach_id`                       | Coach                           | `many2one`   |     | ✅    | hr.employee               |
| `color`                          | Color Index                     | `integer`    |     | ✅    |                           |
| `company_country_code`           | Company Country Code            | `char`       |     |       |                           |
| `company_country_id`             | Company Country                 | `many2one`   |     |       | res.country               |
| `company_id`                     | Company                         | `many2one`   | ✅  | ✅    | res.company               |
| `contract_date_end`              | Contract End Date               | `date`       |     |       |                           |
| `contract_date_start`            | Contract Start Date             | `date`       |     |       |                           |
| `contract_template_id`           | Contract Template               | `many2one`   |     |       | hr.version                |
| `contract_type_id`               | Contract Type                   | `many2one`   |     |       | hr.contract.type          |
| `contract_wage`                  | Contract Wage                   | `monetary`   |     |       |                           |
| `country_code`                   | Country Code                    | `char`       |     |       |                           |
| `country_id`                     | Nationality (Country)           | `many2one`   |     |       | res.country               |
| `country_of_birth`               | Country of Birth                | `many2one`   |     | ✅    | res.country               |
| `create_date`                    | Created on                      | `datetime`   |     | ✅    |                           |
| `create_uid`                     | Created by                      | `many2one`   |     | ✅    | res.users                 |
| `currency_id`                    | Currency                        | `many2one`   |     |       | res.currency              |
| `current_date_version`           | Current Date Version            | `date`       |     |       |                           |
| `current_employee_skill_ids`     | Current Employee Skill          | `one2many`   |     |       | hr.employee.skill         |
| `current_leave_id`               | Current Time Off Type           | `many2one`   |     |       | hr.leave.type             |
| `current_leave_state`            | Current Time Off Status         | `selection`  |     |       |                           |
| `current_version_id`             | Current Version                 | `many2one`   |     | ✅    | hr.version                |
| `date_end`                       | Date End                        | `date`       |     |       |                           |
| `date_start`                     | Date Start                      | `date`       |     |       |                           |
| `date_version`                   | Date Version                    | `date`       | ✅  |       |                           |
| `department_color`               | Department Color                | `integer`    |     |       |                           |
| `department_id`                  | Department                      | `many2one`   |     |       | hr.department             |
| `departure_date`                 | Departure Date                  | `date`       |     |       |                           |
| `departure_description`          | Additional Information          | `html`       |     |       |                           |
| `departure_reason_id`            | Departure Reason                | `many2one`   |     |       | hr.departure.reason       |
| `direct_badge_ids`               | Direct Badge                    | `one2many`   |     | ✅    | gamification.badge.user   |
| `display_certification_page`     | Display Certification Page      | `boolean`    |     |       |                           |
| `display_name`                   | Display Name                    | `char`       |     |       |                           |
| `distance_home_work`             | Home-Work Distance              | `integer`    |     |       |                           |
| `distance_home_work_unit`        | Home-Work Distance unit         | `selection`  | ✅  |       |                           |
| `driving_license`                | Driving License                 | `binary`     |     | ✅    |                           |
| `email`                          | Email                           | `char`       |     |       |                           |
| `emergency_contact`              | Emergency Contact               | `char`       |     | ✅    |                           |
| `emergency_phone`                | Emergency Phone                 | `char`       |     | ✅    |                           |
| `employee_cars_count`            | Cars                            | `integer`    |     |       |                           |
| `employee_id`                    | Employee                        | `many2one`   |     |       | hr.employee               |
| `employee_properties`            | Properties                      | `properties` |     | ✅    |                           |
| `employee_skill_ids`             | Skills                          | `one2many`   |     | ✅    | hr.employee.skill         |
| `employee_type`                  | Employee Type                   | `selection`  | ✅  |       |                           |
| `exceptional_location_id`        | Current                         | `many2one`   |     |       | hr.work.location          |
| `expense_manager_id`             | Expense Approver                | `many2one`   |     | ✅    | res.users                 |
| `filter_for_expense`             | Filter For Expense              | `boolean`    |     |       |                           |
| `friday_location_id`             | Friday                          | `many2one`   |     | ✅    | hr.work.location          |
| `goal_ids`                       | Employee HR Goals               | `one2many`   |     |       | gamification.goal         |
| `has_badges`                     | Has Badges                      | `boolean`    |     |       |                           |
| `has_message`                    | Has Message                     | `boolean`    |     |       |                           |
| `has_multiple_bank_accounts`     | Has Multiple Bank Accounts      | `boolean`    |     |       |                           |
| `has_work_permit`                | Work Permit                     | `binary`     |     | ✅    |                           |
| `hr_icon_display`                | Hr Icon Display                 | `selection`  |     |       |                           |
| `hr_presence_state`              | Hr Presence State               | `selection`  |     |       |                           |
| `hr_responsible_id`              | HR Responsible                  | `many2one`   | ✅  |       | res.users                 |
| `id`                             | ID                              | `integer`    |     | ✅    |                           |
| `id_card`                        | ID Card Copy                    | `binary`     |     | ✅    |                           |
| `identification_id`              | Identification No               | `char`       |     |       |                           |
| `image_1024`                     | Image 1024                      | `binary`     |     | ✅    |                           |
| `image_128`                      | Image 128                       | `binary`     |     | ✅    |                           |
| `image_1920`                     | Image                           | `binary`     |     | ✅    |                           |
| `image_256`                      | Image 256                       | `binary`     |     | ✅    |                           |
| `image_512`                      | Image 512                       | `binary`     |     | ✅    |                           |
| `im_status`                      | IM Status                       | `char`       |     |       |                           |
| `is_absent`                      | Absent Today                    | `boolean`    |     |       |                           |
| `is_current`                     | Is Current                      | `boolean`    |     |       |                           |
| `is_custom_job_title`            | Is Custom Job Title             | `boolean`    |     |       |                           |
| `is_flexible`                    | Is Flexible                     | `boolean`    |     |       |                           |
| `is_fully_flexible`              | Is Fully Flexible               | `boolean`    |     |       |                           |
| `is_future`                      | Is Future                       | `boolean`    |     |       |                           |
| `is_in_contract`                 | Is In Contract                  | `boolean`    |     |       |                           |
| `is_past`                        | Is Past                         | `boolean`    |     |       |                           |
| `is_subordinate`                 | Is Subordinate                  | `boolean`    |     |       |                           |
| `is_trusted_bank_account`        | Is Trusted Bank Account         | `boolean`    |     |       |                           |
| `is_user_active`                 | User's active                   | `boolean`    |     |       |                           |
| `job_id`                         | Job                             | `many2one`   |     |       | hr.job                    |
| `job_title`                      | Job Title                       | `char`       |     |       |                           |
| `km_home_work`                   | Home-Work Distance in Km        | `integer`    |     |       |                           |
| `lang`                           | Lang                            | `selection`  |     | ✅    |                           |
| `last_activity`                  | Last Activity                   | `date`       |     |       |                           |
| `last_activity_time`             | Last Activity Time              | `char`       |     |       |                           |
| `last_modified_date`             | Last Modified on                | `datetime`   | ✅  |       |                           |
| `last_modified_uid`              | Last Modified by                | `many2one`   | ✅  |       | res.users                 |
| `leave_date_from`                | From Date                       | `date`       |     |       |                           |
| `leave_date_to`                  | To Date                         | `date`       |     |       |                           |
| `leave_manager_id`               | Time Off Approver               | `many2one`   |     | ✅    | res.users                 |
| `legal_name`                     | Legal Name                      | `char`       |     | ✅    |                           |
| `license_plate`                  | License Plate                   | `char`       |     |       |                           |
| `marital`                        | Marital Status                  | `selection`  | ✅  |       |                           |
| `member_of_department`           | Member of department            | `boolean`    |     |       |                           |
| `message_attachment_count`       | Attachment Count                | `integer`    |     |       |                           |
| `message_follower_ids`           | Followers                       | `one2many`   |     | ✅    | mail.followers            |
| `message_has_error`              | Message Delivery error          | `boolean`    |     |       |                           |
| `message_has_error_counter`      | Number of errors                | `integer`    |     |       |                           |
| `message_has_sms_error`          | SMS Delivery error              | `boolean`    |     |       |                           |
| `message_ids`                    | Messages                        | `one2many`   |     | ✅    | mail.message              |
| `message_is_follower`            | Is Follower                     | `boolean`    |     |       |                           |
| `message_main_attachment_id`     | Main Attachment                 | `many2one`   |     | ✅    | ir.attachment             |
| `message_needaction`             | Action Needed                   | `boolean`    |     |       |                           |
| `message_needaction_counter`     | Number of Actions               | `integer`    |     |       |                           |
| `message_partner_ids`            | Followers (Partners)            | `many2many`  |     |       | res.partner               |
| `mobile_phone`                   | Work Mobile                     | `char`       |     | ✅    |                           |
| `mobility_card`                  | Mobility Card                   | `char`       |     | ✅    |                           |
| `monday_location_id`             | Monday                          | `many2one`   |     | ✅    | hr.work.location          |
| `my_activity_date_deadline`      | My Activity Deadline            | `date`       |     |       |                           |
| `name`                           | Employee Name                   | `char`       |     | ✅    |                           |
| `newly_hired`                    | Newly Hired                     | `boolean`    |     |       |                           |
| `parent_id`                      | Manager                         | `many2one`   |     | ✅    | hr.employee               |
| `passport_expiration_date`       | Passport Expiration Date        | `date`       |     |       |                           |
| `passport_id`                    | Passport No                     | `char`       |     |       |                           |
| `permit_no`                      | Work Permit No                  | `char`       |     | ✅    |                           |
| `phone`                          | Phone                           | `char`       |     |       |                           |
| `pin`                            | PIN                             | `char`       |     | ✅    |                           |
| `place_of_birth`                 | Place of Birth                  | `char`       |     | ✅    |                           |
| `primary_bank_account_id`        | Primary Bank Account            | `many2one`   |     |       | res.partner.bank          |
| `private_car_plate`              | Private Car Plate               | `char`       |     | ✅    |                           |
| `private_city`                   | Private City                    | `char`       |     |       |                           |
| `private_country_id`             | Private Country                 | `many2one`   |     |       | res.country               |
| `private_email`                  | Private Email                   | `char`       |     | ✅    |                           |
| `private_phone`                  | Private Phone                   | `char`       |     | ✅    |                           |
| `private_state_id`               | Private State                   | `many2one`   |     |       | res.country.state         |
| `private_street`                 | Private Street                  | `char`       |     |       |                           |
| `private_street2`                | Private Street2                 | `char`       |     |       |                           |
| `private_zip`                    | Private Zip                     | `char`       |     |       |                           |
| `rating_ids`                     | Ratings                         | `one2many`   |     | ✅    | rating.rating             |
| `related_partners_count`         | Related Partners Count          | `integer`    |     |       |                           |
| `resource_calendar_id`           | Default Working Hours           | `many2one`   |     |       | resource.calendar         |
| `resource_id`                    | Resource                        | `many2one`   | ✅  | ✅    | resource.resource         |
| `resume_line_ids`                | Resume lines                    | `one2many`   |     | ✅    | hr.resume.line            |
| `salary_distribution`            | Salary Distribution             | `json`       |     | ✅    |                           |
| `saturday_location_id`           | Saturday                        | `many2one`   |     | ✅    | hr.work.location          |
| `sex`                            | Gender                          | `selection`  |     |       |                           |
| `share`                          | Share User                      | `boolean`    |     |       |                           |
| `show_hr_icon_display`           | Show Hr Icon Display            | `boolean`    |     |       |                           |
| `show_leaves`                    | Able to see Remaining Time Off  | `boolean`    |     |       |                           |
| `skill_ids`                      | Skill                           | `many2many`  |     | ✅    | hr.skill                  |
| `spouse_birthdate`               | Spouse Birthdate                | `date`       |     |       |                           |
| `spouse_complete_name`           | Spouse Legal Name               | `char`       |     |       |                           |
| `ssnid`                          | SSN No                          | `char`       |     |       |                           |
| `structure_type_id`              | Salary Structure Type           | `many2one`   |     |       | hr.payroll.structure.type |
| `study_field`                    | Field of Study                  | `char`       |     | ✅    |                           |
| `study_school`                   | School                          | `char`       |     | ✅    |                           |
| `subordinate_ids`                | Subordinates                    | `one2many`   |     |       | hr.employee               |
| `sunday_location_id`             | Sunday                          | `many2one`   |     | ✅    | hr.work.location          |
| `thursday_location_id`           | Thursday                        | `many2one`   |     | ✅    | hr.work.location          |
| `today_location_name`            | Today Location Name             | `char`       |     | ✅    |                           |
| `trial_date_end`                 | End of Trial Period             | `date`       |     |       |                           |
| `tuesday_location_id`            | Tuesday                         | `many2one`   |     | ✅    | hr.work.location          |
| `tz`                             | Timezone                        | `selection`  |     |       |                           |
| `user_id`                        | User                            | `many2one`   |     | ✅    | res.users                 |
| `user_partner_id`                | User's partner                  | `many2one`   |     |       | res.partner               |
| `version_id`                     | Version                         | `many2one`   | ✅  |       | hr.version                |
| `version_ids`                    | Employee Versions               | `one2many`   | ✅  | ✅    | hr.version                |
| `versions_count`                 | Versions Count                  | `integer`    |     |       |                           |
| `visa_expire`                    | Visa Expiration Date            | `date`       |     | ✅    |                           |
| `visa_no`                        | Visa No                         | `char`       |     | ✅    |                           |
| `wage`                           | Wage                            | `monetary`   |     |       |                           |
| `website_message_ids`            | Website Messages                | `one2many`   |     | ✅    | mail.message              |
| `wednesday_location_id`          | Wednesday                       | `many2one`   |     | ✅    | hr.work.location          |
| `work_contact_id`                | Work Contact                    | `many2one`   |     | ✅    | res.partner               |
| `work_email`                     | Work Email                      | `char`       |     | ✅    |                           |
| `work_location_id`               | Work Location                   | `many2one`   |     |       | hr.work.location          |
| `work_location_name`             | Work Location Name              | `char`       |     |       |                           |
| `work_location_type`             | Work Location Type              | `selection`  |     |       |                           |
| `work_permit_expiration_date`    | Work Permit Expiration Date     | `date`       |     | ✅    |                           |
| `work_permit_name`               | work_permit_name                | `char`       |     |       |                           |
| `work_permit_scheduled_activity` | Work Permit Scheduled Activity  | `boolean`    |     | ✅    |                           |
| `work_phone`                     | Work Phone                      | `char`       |     | ✅    |                           |
| `write_date`                     | Last Updated on                 | `datetime`   |     | ✅    |                           |
| `write_uid`                      | Last Updated by                 | `many2one`   |     | ✅    | res.users                 |

**Access Rights:**

| Name                         | Group                                     | Perms     |
| ---------------------------- | ----------------------------------------- | --------- |
| hr.employee user             | Employees / Officer: Manage all employees | `R/W/C/D` |
| name_hr_employee_back_office | OpenEduCat / Manager                      | `R/W/C`   |
| name_hr_employee_student     | OpenEduCat / Manager                      | `R`       |
| hr.employee system user      | Role / Administrator                      | `R`       |

**Record Rules:**

- **Employee multi company rule** (Global) `R/W/C/D`
  - Domain:
    `['|', '|', '|',         ('company_id', 'in', company_ids + [False]),         ('parent_id.user_id', '=', user.id),         ('id', '=', user.employee_id.parent_id.id),         ('user_id', '=', user.id)     ]`
- **HR multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `hr.version` — Employee Contract

> 📧 Mail Thread

Write and Create: Special case when setting a contract as running: If there is already a
validated time off over another contract with a different schedule, split the time off,
before the \_check_contracts raises an issue. If there are existing leaves that are
spanned by this new contract, update their resource calendar to the current one.

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                  |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------- |
| `active`                        | Active                        | `boolean`   |     | ✅    |                           |
| `active_employee`               | Active Employee               | `boolean`   |     |       |                           |
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
| `additional_note`               | Additional Note               | `text`      |     | ✅    |                           |
| `address_id`                    | Work Address                  | `many2one`  |     | ✅    | res.partner               |
| `allowed_country_state_ids`     | Allowed Country State         | `many2many` |     |       | res.country.state         |
| `children`                      | Dependent Children            | `integer`   |     | ✅    |                           |
| `company_country_id`            | Company country               | `many2one`  |     |       | res.country               |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company               |
| `contract_date_end`             | Contract End Date             | `date`      |     | ✅    |                           |
| `contract_date_start`           | Contract Start Date           | `date`      |     | ✅    |                           |
| `contract_template_id`          | Contract Template             | `many2one`  |     | ✅    | hr.version                |
| `contract_type_id`              | Contract Type                 | `many2one`  |     | ✅    | hr.contract.type          |
| `contract_wage`                 | Contract Wage                 | `monetary`  |     |       |                           |
| `country_code`                  | Country Code                  | `char`      |     |       |                           |
| `country_id`                    | Nationality (Country)         | `many2one`  |     | ✅    | res.country               |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                           |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users                 |
| `currency_id`                   | Currency                      | `many2one`  |     |       | res.currency              |
| `date_end`                      | Date End                      | `date`      |     |       |                           |
| `date_start`                    | Date Start                    | `date`      |     |       |                           |
| `date_version`                  | Date Version                  | `date`      | ✅  | ✅    |                           |
| `department_id`                 | Department                    | `many2one`  |     | ✅    | hr.department             |
| `departure_date`                | Departure Date                | `date`      |     | ✅    |                           |
| `departure_description`         | Additional Information        | `html`      |     | ✅    |                           |
| `departure_reason_id`           | Departure Reason              | `many2one`  |     | ✅    | hr.departure.reason       |
| `display_name`                  | Display Name                  | `char`      |     |       |                           |
| `distance_home_work`            | Home-Work Distance            | `integer`   |     | ✅    |                           |
| `distance_home_work_unit`       | Home-Work Distance unit       | `selection` | ✅  | ✅    |                           |
| `employee_id`                   | Employee                      | `many2one`  |     | ✅    | hr.employee               |
| `employee_type`                 | Employee Type                 | `selection` | ✅  | ✅    |                           |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                           |
| `hr_responsible_id`             | HR Responsible                | `many2one`  | ✅  | ✅    | res.users                 |
| `id`                            | ID                            | `integer`   |     | ✅    |                           |
| `identification_id`             | Identification No             | `char`      |     | ✅    |                           |
| `is_current`                    | Is Current                    | `boolean`   |     |       |                           |
| `is_custom_job_title`           | Is Custom Job Title           | `boolean`   |     | ✅    |                           |
| `is_flexible`                   | Is Flexible                   | `boolean`   |     | ✅    |                           |
| `is_fully_flexible`             | Is Fully Flexible             | `boolean`   |     | ✅    |                           |
| `is_future`                     | Is Future                     | `boolean`   |     |       |                           |
| `is_in_contract`                | Is In Contract                | `boolean`   |     |       |                           |
| `is_past`                       | Is Past                       | `boolean`   |     |       |                           |
| `job_id`                        | Job                           | `many2one`  |     | ✅    | hr.job                    |
| `job_title`                     | Job Title                     | `char`      |     | ✅    |                           |
| `km_home_work`                  | Home-Work Distance in Km      | `integer`   |     | ✅    |                           |
| `last_modified_date`            | Last Modified on              | `datetime`  | ✅  | ✅    |                           |
| `last_modified_uid`             | Last Modified by              | `many2one`  | ✅  | ✅    | res.users                 |
| `marital`                       | Marital Status                | `selection` | ✅  | ✅    |                           |
| `member_of_department`          | Member of department          | `boolean`   |     |       |                           |
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
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                           |
| `name`                          | Name                          | `char`      |     | ✅    |                           |
| `passport_expiration_date`      | Passport Expiration Date      | `date`      |     | ✅    |                           |
| `passport_id`                   | Passport No                   | `char`      |     | ✅    |                           |
| `private_city`                  | Private City                  | `char`      |     | ✅    |                           |
| `private_country_id`            | Private Country               | `many2one`  |     | ✅    | res.country               |
| `private_state_id`              | Private State                 | `many2one`  |     | ✅    | res.country.state         |
| `private_street`                | Private Street                | `char`      |     | ✅    |                           |
| `private_street2`               | Private Street2               | `char`      |     | ✅    |                           |
| `private_zip`                   | Private Zip                   | `char`      |     | ✅    |                           |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating             |
| `resource_calendar_id`          | Working Hours                 | `many2one`  |     | ✅    | resource.calendar         |
| `sex`                           | Gender                        | `selection` |     | ✅    |                           |
| `spouse_birthdate`              | Spouse Birthdate              | `date`      |     | ✅    |                           |
| `spouse_complete_name`          | Spouse Legal Name             | `char`      |     | ✅    |                           |
| `ssnid`                         | SSN No                        | `char`      |     | ✅    |                           |
| `structure_type_id`             | Salary Structure Type         | `many2one`  |     | ✅    | hr.payroll.structure.type |
| `trial_date_end`                | End of Trial Period           | `date`      |     | ✅    |                           |
| `tz`                            | Timezone                      | `selection` |     |       |                           |
| `wage`                          | Wage                          | `monetary`  |     | ✅    |                           |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message              |
| `work_location_id`              | Work Location                 | `many2one`  |     | ✅    | hr.work.location          |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                           |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name               | Group                                     | Perms     |
| ------------------ | ----------------------------------------- | --------- |
| hr.version.user    | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.version.manager | Employees / Administrator                 | `R/W/C/D` |

**Record Rules:**

- **HR Contract: Contract Manager** (50) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **HR Contract: Multi Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`

### 🗃️ `hr.job` — Job Position

> 📧 Mail Thread

A mixin for models that inherits mail.alias to have a one-to-one relation between the
model and its alias.

**Fields:**

| Field                             | Label                               | Type                    | Req | Store | Relation              |
| --------------------------------- | ----------------------------------- | ----------------------- | --- | ----- | --------------------- |
| `active`                          | Active                              | `boolean`               |     | ✅    |                       |
| `activity_calendar_event_id`      | Next Activity Calendar Event        | `many2one`              |     |       | calendar.event        |
| `activity_count`                  | Activity Count                      | `integer`               |     |       |                       |
| `activity_date_deadline`          | Next Activity Deadline              | `date`                  |     |       |                       |
| `activity_exception_decoration`   | Activity Exception Decoration       | `selection`             |     |       |                       |
| `activity_exception_icon`         | Icon                                | `char`                  |     |       |                       |
| `activity_ids`                    | Activities                          | `one2many`              |     | ✅    | mail.activity         |
| `activity_state`                  | Activity State                      | `selection`             |     |       |                       |
| `activity_summary`                | Next Activity Summary               | `char`                  |     |       |                       |
| `activity_type_icon`              | Activity Type Icon                  | `char`                  |     |       |                       |
| `activity_type_id`                | Next Activity Type                  | `many2one`              |     |       | mail.activity.type    |
| `activity_user_id`                | Responsible User                    | `many2one`              |     |       | res.users             |
| `address_id`                      | Job Location                        | `many2one`              |     | ✅    | res.partner           |
| `alias_bounced_content`           | Custom Bounced Message              | `html`                  |     |       |                       |
| `alias_contact`                   | Alias Contact Security              | `selection`             | ✅  |       |                       |
| `alias_defaults`                  | Default Values                      | `text`                  | ✅  |       |                       |
| `alias_domain`                    | Alias Domain Name                   | `char`                  |     |       |                       |
| `alias_domain_id`                 | Alias Domain                        | `many2one`              |     |       | mail.alias.domain     |
| `alias_email`                     | Email Alias                         | `char`                  |     |       |                       |
| `alias_force_thread_id`           | Record Thread ID                    | `integer`               |     |       |                       |
| `alias_full_name`                 | Alias Email                         | `char`                  |     |       |                       |
| `alias_id`                        | Alias                               | `many2one`              | ✅  | ✅    | mail.alias            |
| `alias_incoming_local`            | Local-part based incoming detection | `boolean`               |     |       |                       |
| `alias_model_id`                  | Aliased Model                       | `many2one`              | ✅  |       | ir.model              |
| `alias_name`                      | Alias Name                          | `char`                  |     |       |                       |
| `alias_parent_model_id`           | Parent Model                        | `many2one`              |     |       | ir.model              |
| `alias_parent_thread_id`          | Parent Record Thread ID             | `integer`               |     |       |                       |
| `alias_status`                    | Alias Status                        | `selection`             |     |       |                       |
| `all_application_count`           | All Application Count               | `integer`               |     |       |                       |
| `allowed_user_ids`                | Allowed User                        | `many2many`             |     |       | res.users             |
| `applicant_hired`                 | Applicants Hired                    | `integer`               |     |       |                       |
| `applicant_matching_score`        | Matching Score(%)                   | `float`                 |     |       |                       |
| `applicant_properties_definition` | Applicant Properties                | `properties_definition` |     | ✅    |                       |
| `application_count`               | Application Count                   | `integer`               |     |       |                       |
| `application_ids`                 | Job Applications                    | `one2many`              |     | ✅    | hr.applicant          |
| `can_publish`                     | Can Publish                         | `boolean`               |     |       |                       |
| `color`                           | Color Index                         | `integer`               |     | ✅    |                       |
| `company_id`                      | Company                             | `many2one`              |     | ✅    | res.company           |
| `contract_type_id`                | Employment Type                     | `many2one`              |     | ✅    | hr.contract.type      |
| `create_date`                     | Created on                          | `datetime`              |     | ✅    |                       |
| `create_uid`                      | Created by                          | `many2one`              |     | ✅    | res.users             |
| `current_job_skill_ids`           | Current Job Skill                   | `one2many`              |     |       | hr.job.skill          |
| `department_id`                   | Department                          | `many2one`              |     | ✅    | hr.department         |
| `description`                     | Job Description                     | `html`                  |     | ✅    |                       |
| `display_name`                    | Display Name                        | `char`                  |     |       |                       |
| `document_ids`                    | Documents                           | `one2many`              |     |       | ir.attachment         |
| `documents_count`                 | Document Count                      | `integer`               |     |       |                       |
| `employee_count`                  | Employee Count                      | `integer`               |     |       |                       |
| `employee_ids`                    | Employees                           | `one2many`              |     | ✅    | hr.employee           |
| `expected_degree`                 | Expected Degree                     | `many2one`              |     | ✅    | hr.recruitment.degree |
| `expected_employees`              | Total Forecasted Employees          | `integer`               |     |       |                       |
| `extended_interviewer_ids`        | Extended Interviewer                | `many2many`             |     | ✅    | res.users             |
| `favorite_user_ids`               | Favorite User                       | `many2many`             |     | ✅    | res.users             |
| `full_url`                        | job URL                             | `char`                  |     |       |                       |
| `has_message`                     | Has Message                         | `boolean`               |     |       |                       |
| `id`                              | ID                                  | `integer`               |     | ✅    |                       |
| `industry_id`                     | Industry                            | `many2one`              |     | ✅    | res.partner.industry  |
| `interviewer_ids`                 | Interviewers                        | `many2many`             |     | ✅    | res.users             |
| `is_favorite`                     | Is Favorite                         | `boolean`               |     |       |                       |
| `is_published`                    | Is Published                        | `boolean`               |     | ✅    |                       |
| `is_seo_optimized`                | SEO optimized                       | `boolean`               |     | ✅    |                       |
| `job_details`                     | Process Details                     | `html`                  |     | ✅    |                       |
| `job_properties`                  | Properties                          | `properties`            |     | ✅    |                       |
| `job_skill_ids`                   | Skills                              | `one2many`              |     | ✅    | hr.job.skill          |
| `job_source_ids`                  | Job Source                          | `one2many`              |     | ✅    | hr.recruitment.source |
| `manager_id`                      | Department Manager                  | `many2one`              |     | ✅    | hr.employee           |
| `message_attachment_count`        | Attachment Count                    | `integer`               |     |       |                       |
| `message_follower_ids`            | Followers                           | `one2many`              |     | ✅    | mail.followers        |
| `message_has_error`               | Message Delivery error              | `boolean`               |     |       |                       |
| `message_has_error_counter`       | Number of errors                    | `integer`               |     |       |                       |
| `message_has_sms_error`           | SMS Delivery error                  | `boolean`               |     |       |                       |
| `message_ids`                     | Messages                            | `one2many`              |     | ✅    | mail.message          |
| `message_is_follower`             | Is Follower                         | `boolean`               |     |       |                       |
| `message_needaction`              | Action Needed                       | `boolean`               |     |       |                       |
| `message_needaction_counter`      | Number of Actions                   | `integer`               |     |       |                       |
| `message_partner_ids`             | Followers (Partners)                | `many2many`             |     |       | res.partner           |
| `my_activity_date_deadline`       | My Activity Deadline                | `date`                  |     |       |                       |
| `name`                            | Job Position                        | `char`                  | ✅  | ✅    |                       |
| `new_application_count`           | New Application                     | `integer`               |     |       |                       |
| `no_of_employee`                  | Current Number of Employees         | `integer`               |     |       |                       |
| `no_of_hired_employee`            | Hired                               | `integer`               |     | ✅    |                       |
| `no_of_recruitment`               | Target                              | `integer`               |     | ✅    |                       |
| `old_application_count`           | Old Application                     | `integer`               |     |       |                       |
| `open_application_count`          | Open Application Count              | `integer`               |     |       |                       |
| `published_date`                  | Published Date                      | `date`                  |     | ✅    |                       |
| `rating_ids`                      | Ratings                             | `one2many`              |     | ✅    | rating.rating         |
| `requirements`                    | Requirements                        | `text`                  |     | ✅    |                       |
| `seo_name`                        | Seo name                            | `char`                  |     | ✅    |                       |
| `sequence`                        | Sequence                            | `integer`               |     | ✅    |                       |
| `skill_ids`                       | Skill                               | `many2many`             |     | ✅    | hr.skill              |
| `user_id`                         | Recruiter                           | `many2one`              |     | ✅    | res.users             |
| `website_absolute_url`            | Website Absolute URL                | `char`                  |     |       |                       |
| `website_description`             | Website description                 | `html`                  |     | ✅    |                       |
| `website_id`                      | Website                             | `many2one`              |     | ✅    | website               |
| `website_message_ids`             | Website Messages                    | `one2many`              |     | ✅    | mail.message          |
| `website_meta_description`        | Website meta description            | `text`                  |     | ✅    |                       |
| `website_meta_keywords`           | Website meta keywords               | `char`                  |     | ✅    |                       |
| `website_meta_og_img`             | Website opengraph image             | `char`                  |     | ✅    |                       |
| `website_meta_title`              | Website meta title                  | `char`                  |     | ✅    |                       |
| `website_published`               | Visible on current website          | `boolean`               |     |       |                       |
| `website_url`                     | Website URL                         | `char`                  |     |       |                       |
| `write_date`                      | Last Updated on                     | `datetime`              |     | ✅    |                       |
| `write_uid`                       | Last Updated by                     | `many2one`              |     | ✅    | res.users             |

**Access Rights:**

| Name               | Group                                        | Perms     |
| ------------------ | -------------------------------------------- | --------- |
| hr.job user        | Employees / Officer: Manage all employees    | `R`       |
| hr.job.interviewer | Recruitment / Interviewer                    | `R`       |
| hr.job user        | Recruitment / Officer: Manage all applicants | `R/W/C/D` |
| hr.job.public      | Role / Portal                                | `R`       |
| hr.job.public      | Role / Public                                | `R`       |
| hr.job.employee    | Role / User                                  | `R`       |
| hr.job.public      | Role / User                                  | `R`       |

**Record Rules:**

- **Job multi company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **User: All Applicants** (83) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Job Positions: Public** (11) `R`
  - Domain: `[('website_published', '=', True)]`
- **Job Positions: Portal** (10) `R`
  - Domain: `[('website_published', '=', True)]`
- **Job Positions: HR Officer** (83) `R`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `mail.activity.plan` — Activity Plan

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                   | Label                     | Type        | Req | Store | Relation                    |
| ----------------------- | ------------------------- | ----------- | --- | ----- | --------------------------- |
| `active`                | Active                    | `boolean`   |     | ✅    |                             |
| `company_id`            | Company                   | `many2one`  |     | ✅    | res.company                 |
| `create_date`           | Created on                | `datetime`  |     | ✅    |                             |
| `create_uid`            | Created by                | `many2one`  |     | ✅    | res.users                   |
| `department_assignable` | Department Assignable     | `boolean`   |     |       |                             |
| `department_id`         | Department                | `many2one`  |     | ✅    | hr.department               |
| `display_name`          | Display Name              | `char`      |     |       |                             |
| `has_user_on_demand`    | Has on demand responsible | `boolean`   |     |       |                             |
| `id`                    | ID                        | `integer`   |     | ✅    |                             |
| `name`                  | Name                      | `char`      | ✅  | ✅    |                             |
| `res_model`             | Model                     | `selection` | ✅  | ✅    |                             |
| `res_model_id`          | Applies to                | `many2one`  | ✅  | ✅    | ir.model                    |
| `steps_count`           | Steps Count               | `integer`   |     |       |                             |
| `template_ids`          | Activities                | `one2many`  |     | ✅    | mail.activity.plan.template |
| `write_date`            | Last Updated on           | `datetime`  |     | ✅    |                             |
| `write_uid`             | Last Updated by           | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                                      | Group                       | Perms     |
| ----------------------------------------- | --------------------------- | --------- |
| mail.activity.plan.sale.manager           | Sales / Administrator       | `R/W/C/D` |
| mail.activity.plan.sale.manager           | Sales / Administrator       | `R/W/C/D` |
| mail.activity.plan.hr.manager             | Employees / Administrator   | `R/W/C/D` |
| mail.activity.plan.hr.recruitment.manager | Recruitment / Administrator | `R/W/C/D` |
| mail.activity.plan.system                 | Role / Administrator        | `R/W/C/D` |
| mail.activity.plan.user                   | Role / User                 | `R`       |

**Record Rules:**

- **Administrators can access all activity plans.** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Manager can manage lead plans** (27) `W/C/D`
  - Domain: `[('res_model', '=', 'crm.lead')]`
- **Manager can edit employee plan** (50) `W/C/D`
  - Domain: `[('res_model', '=', 'hr.employee')]`
- **Manager can manage applicant plans** (84) `W/C/D`
  - Domain: `[('res_model', '=', 'hr.applicant')]`
- **Manager can manage sale order plans** (27) `W/C/D`
  - Domain: `[('res_model', '=', 'sale.order')]`

### 🗃️ `mail.activity.plan.template` — Activity plan template

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label           | Type        | Req | Store | Relation           |
| ------------------- | --------------- | ----------- | --- | ----- | ------------------ |
| `activity_type_id`  | Activity Type   | `many2one`  | ✅  | ✅    | mail.activity.type |
| `company_id`        | Company         | `many2one`  |     |       | res.company        |
| `create_date`       | Created on      | `datetime`  |     | ✅    |                    |
| `create_uid`        | Created by      | `many2one`  |     | ✅    | res.users          |
| `delay_count`       | Interval        | `integer`   |     | ✅    |                    |
| `delay_from`        | Trigger         | `selection` | ✅  | ✅    |                    |
| `delay_unit`        | Delay units     | `selection` | ✅  | ✅    |                    |
| `display_name`      | Display Name    | `char`      |     |       |                    |
| `icon`              | Icon            | `char`      |     |       |                    |
| `id`                | ID              | `integer`   |     | ✅    |                    |
| `next_activity_ids` | Next Activities | `many2many` |     | ✅    | mail.activity.type |
| `note`              | Note            | `html`      |     | ✅    |                    |
| `plan_id`           | Plan            | `many2one`  | ✅  | ✅    | mail.activity.plan |
| `res_model`         | Model           | `selection` |     |       |                    |
| `responsible_id`    | Assigned to     | `many2one`  |     | ✅    | res.users          |
| `responsible_type`  | Assignment      | `selection` | ✅  | ✅    |                    |
| `sequence`          | Sequence        | `integer`   |     | ✅    |                    |
| `summary`           | Summary         | `char`      |     | ✅    |                    |
| `write_date`        | Last Updated on | `datetime`  |     | ✅    |                    |
| `write_uid`         | Last Updated by | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                               | Group                       | Perms     |
| -------------------------------------------------- | --------------------------- | --------- |
| mail.activity.plan.template.sale.manager           | Sales / Administrator       | `R/W/C/D` |
| mail.activity.plan.template.sale.manager           | Sales / Administrator       | `R/W/C/D` |
| mail.activity.plan.template.hr.manager             | Employees / Administrator   | `R/W/C/D` |
| mail.activity.plan.template.hr.recruitment.manager | Recruitment / Administrator | `R/W/C/D` |
| mail.activity.plan.template.system                 | Role / Administrator        | `R/W/C/D` |
| mail.activity.plan.template.user                   | Role / User                 | `R`       |

**Record Rules:**

- **Administrators can access all activity plan templates.** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Manager can manage lead plan templates** (27) `W/C/D`
  - Domain: `[('plan_id.res_model', '=', 'crm.lead')]`
- **Manager can edit employee plan template** (50) `W/C/D`
  - Domain: `[('plan_id.res_model', '=', 'hr.employee')]`
- **Manager can manage applicant plan templates** (84) `W/C/D`
  - Domain: `[('plan_id.res_model', '=', 'hr.applicant')]`
- **Manager can manage sale order plan templates** (27) `W/C/D`
  - Domain: `[('plan_id.res_model', '=', 'sale.order')]`

### 🗃️ `mail.activity.schedule` — Activity schedule plan Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                        | Label                      | Type        | Req | Store | Relation                    |
| ---------------------------- | -------------------------- | ----------- | --- | ----- | --------------------------- |
| `activity_category`          | Action                     | `selection` |     |       |                             |
| `activity_type_id`           | Activity Type              | `many2one`  |     | ✅    | mail.activity.type          |
| `activity_user_id`           | Assigned to                | `many2one`  |     | ✅    | res.users                   |
| `chaining_type`              | Chaining Type              | `selection` |     |       |                             |
| `company_id`                 | Company                    | `many2one`  |     |       | res.company                 |
| `create_date`                | Created on                 | `datetime`  |     | ✅    |                             |
| `create_uid`                 | Created by                 | `many2one`  |     | ✅    | res.users                   |
| `date_deadline`              | Due Date                   | `date`      |     | ✅    |                             |
| `department_id`              | Department                 | `many2one`  |     |       | hr.department               |
| `display_name`               | Display Name               | `char`      |     |       |                             |
| `error`                      | Error                      | `html`      |     |       |                             |
| `has_error`                  | Has Error                  | `boolean`   |     |       |                             |
| `has_warning`                | Has Warning                | `boolean`   |     |       |                             |
| `id`                         | ID                         | `integer`   |     | ✅    |                             |
| `is_batch_mode`              | Use in batch               | `boolean`   |     |       |                             |
| `note`                       | Note                       | `html`      |     | ✅    |                             |
| `plan_available_ids`         | Plan Available             | `many2many` |     | ✅    | mail.activity.plan          |
| `plan_date`                  | Plan Date                  | `date`      |     | ✅    |                             |
| `plan_department_filterable` | Plan Department Filterable | `boolean`   |     |       |                             |
| `plan_has_user_on_demand`    | Has on demand responsible  | `boolean`   |     |       |                             |
| `plan_id`                    | Plan                       | `many2one`  |     | ✅    | mail.activity.plan          |
| `plan_on_demand_user_id`     | Assigned To                | `many2one`  |     | ✅    | res.users                   |
| `plan_schedule_line_ids`     | Schedule Lines             | `one2many`  |     |       | mail.activity.schedule.line |
| `res_ids`                    | Document IDs               | `text`      |     | ✅    |                             |
| `res_model`                  | Model                      | `char`      |     | ✅    |                             |
| `res_model_id`               | Applies to                 | `many2one`  |     | ✅    | ir.model                    |
| `summary`                    | Summary                    | `char`      |     | ✅    |                             |
| `warning`                    | Warning                    | `html`      |     |       |                             |
| `write_date`                 | Last Updated on            | `datetime`  |     | ✅    |                             |
| `write_uid`                  | Last Updated by            | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                        | Group       | Perms   |
| --------------------------- | ----------- | ------- |
| mail.activity.schedule.user | Role / User | `R/W/C` |

### 🗃️ `hr.bank.account.allocation.wizard.line` — Bank Account Allocation Line (Wizard)

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field             | Label           | Type        | Req | Store | Relation                          |
| ----------------- | --------------- | ----------- | --- | ----- | --------------------------------- |
| `acc_number`      | Account Number  | `char`      |     |       |                                   |
| `amount`          | Amount          | `float`     |     | ✅    |                                   |
| `amount_type`     | Amount Type     | `selection` |     | ✅    |                                   |
| `bank_account_id` | Bank Account    | `many2one`  | ✅  | ✅    | res.partner.bank                  |
| `create_date`     | Created on      | `datetime`  |     | ✅    |                                   |
| `create_uid`      | Created by      | `many2one`  |     | ✅    | res.users                         |
| `display_name`    | Display Name    | `char`      |     |       |                                   |
| `id`              | ID              | `integer`   |     | ✅    |                                   |
| `sequence`        | Sequence        | `integer`   |     | ✅    |                                   |
| `symbol`          | Symbol          | `char`      |     |       |                                   |
| `trusted`         | Trusted         | `boolean`   |     | ✅    |                                   |
| `wizard_id`       | Wizard          | `many2one`  | ✅  | ✅    | hr.bank.account.allocation.wizard |
| `write_date`      | Last Updated on | `datetime`  |     | ✅    |                                   |
| `write_uid`       | Last Updated by | `many2one`  |     | ✅    | res.users                         |

**Access Rights:**

| Name                                          | Group                                     | Perms     |
| --------------------------------------------- | ----------------------------------------- | --------- |
| access.hr.bank.account.allocation.wizard.line | Employees / Officer: Manage all employees | `R/W/C/D` |

### 🗃️ `hr.bank.account.allocation.wizard` — Bank Account Allocation Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field            | Label           | Type       | Req | Store | Relation                               |
| ---------------- | --------------- | ---------- | --- | ----- | -------------------------------------- |
| `allocation_ids` | Allocations     | `one2many` |     | ✅    | hr.bank.account.allocation.wizard.line |
| `create_date`    | Created on      | `datetime` |     | ✅    |                                        |
| `create_uid`     | Created by      | `many2one` |     | ✅    | res.users                              |
| `display_name`   | Display Name    | `char`     |     |       |                                        |
| `employee_id`    | Employee        | `many2one` | ✅  | ✅    | hr.employee                            |
| `id`             | ID              | `integer`  |     | ✅    |                                        |
| `write_date`     | Last Updated on | `datetime` |     | ✅    |                                        |
| `write_uid`      | Last Updated by | `many2one` |     | ✅    | res.users                              |

**Access Rights:**

| Name                                     | Group                                     | Perms   |
| ---------------------------------------- | ----------------------------------------- | ------- |
| access.hr.bank.account.allocation.wizard | Employees / Officer: Manage all employees | `R/W/C` |

### 🗃️ `base` — Base

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

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

### 🗃️ `hr.version.wizard` — Contract Template Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                  | Label             | Type       | Req | Store | Relation   |
| ---------------------- | ----------------- | ---------- | --- | ----- | ---------- |
| `contract_template_id` | Contract Template | `many2one` | ✅  | ✅    | hr.version |
| `create_date`          | Created on        | `datetime` |     | ✅    |            |
| `create_uid`           | Created by        | `many2one` |     | ✅    | res.users  |
| `display_name`         | Display Name      | `char`     |     |       |            |
| `id`                   | ID                | `integer`  |     | ✅    |            |
| `write_date`           | Last Updated on   | `datetime` |     | ✅    |            |
| `write_uid`            | Last Updated by   | `many2one` |     | ✅    | res.users  |

**Access Rights:**

| Name                     | Group                                     | Perms   |
| ------------------------ | ----------------------------------------- | ------- |
| access.hr.version.wizard | Employees / Officer: Manage all employees | `R/W/C` |

### 🗃️ `hr.contract.type` — Contract Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `code`         | Code            | `char`     |     | ✅    |             |
| `country_id`   | Country         | `many2one` |     | ✅    | res.country |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Name            | `char`     | ✅  | ✅    |             |
| `sequence`     | Sequence        | `integer`  |     | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                     | Group                                     | Perms     |
| ------------------------ | ----------------------------------------- | --------- |
| hr.contract.type.manager | Employees / Officer: Manage all employees | `R/W/C/D` |

**Record Rules:**

- **HR Contract Type: Multi Company** (Global) `R/W/C/D`
  - Domain:
    `['|', ('country_id', '=', False), ('country_id', 'in', user.env.companies.country_id.ids)]`

### 🗃️ `hr.departure.reason` — Departure Reason

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `country_code` | Country Code    | `char`     |     |       |             |
| `country_id`   | Country         | `many2one` |     | ✅    | res.country |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Reason          | `char`     | ✅  | ✅    |             |
| `sequence`     | Sequence        | `integer`  |     | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                            | Group                                     | Perms     |
| ------------------------------- | ----------------------------------------- | --------- |
| access_hr_departure_reason_user | Employees / Officer: Manage all employees | `R/W/C/D` |

**Record Rules:**

- **Departure Reason: multi company** (Global) `R/W/C/D`
  - Domain:
    `[('country_code', 'in', user.env.companies.mapped('country_code') + [False])]`

### 🗃️ `hr.departure.wizard` — Departure Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                   | Label                  | Type        | Req | Store | Relation            |
| ----------------------- | ---------------------- | ----------- | --- | ----- | ------------------- |
| `create_date`           | Created on             | `datetime`  |     | ✅    |                     |
| `create_uid`            | Created by             | `many2one`  |     | ✅    | res.users           |
| `departure_date`        | Contract End Date      | `date`      | ✅  | ✅    |                     |
| `departure_description` | Additional Information | `html`      |     | ✅    |                     |
| `departure_reason_id`   | Departure Reason       | `many2one`  | ✅  | ✅    | hr.departure.reason |
| `display_name`          | Display Name           | `char`      |     |       |                     |
| `employee_ids`          | Employees              | `many2many` | ✅  | ✅    | hr.employee         |
| `id`                    | ID                     | `integer`   |     | ✅    |                     |
| `is_user_employee`      | User Employee          | `boolean`   |     |       |                     |
| `release_campany_car`   | Release Company Car    | `boolean`   |     | ✅    |                     |
| `remove_related_user`   | Related User           | `boolean`   |     | ✅    |                     |
| `set_date_end`          | Set Contract End Date  | `boolean`   |     | ✅    |                     |
| `write_date`            | Last Updated on        | `datetime`  |     | ✅    |                     |
| `write_uid`             | Last Updated by        | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                       | Group                                     | Perms   |
| -------------------------- | ----------------------------------------- | ------- |
| access.hr.departure.wizard | Employees / Officer: Manage all employees | `R/W/C` |

### 🗃️ `mail.alias` — Email Aliases

A Mail Alias is a mapping of an email address with a given Odoo Document model. It is
used by Odoo's mail gateway when processing incoming emails sent to the system. If the
recipient address (To) of the message matches a Mail MailAlias, the message will be
either processed following the rules of that alias. If the message is a reply it will be
attached to the existing discussion on the corresponding record, otherwise a new record
of the corresponding model will be created.

       This is meant to be used in combination with a catch-all email configuration
       on the company's mail server, so that as soon as a new mail.alias is
       created, it becomes immediately usable and Odoo will accept email for it.

**Fields:**

| Field                    | Label                               | Type        | Req | Store | Relation          |
| ------------------------ | ----------------------------------- | ----------- | --- | ----- | ----------------- |
| `alias_bounced_content`  | Custom Bounced Message              | `html`      |     | ✅    |                   |
| `alias_contact`          | Alias Contact Security              | `selection` | ✅  | ✅    |                   |
| `alias_defaults`         | Default Values                      | `text`      | ✅  | ✅    |                   |
| `alias_domain`           | Alias domain name                   | `char`      |     |       |                   |
| `alias_domain_id`        | Alias Domain                        | `many2one`  |     | ✅    | mail.alias.domain |
| `alias_force_thread_id`  | Record Thread ID                    | `integer`   |     | ✅    |                   |
| `alias_full_name`        | Alias Email                         | `char`      |     | ✅    |                   |
| `alias_incoming_local`   | Local-part based incoming detection | `boolean`   |     | ✅    |                   |
| `alias_model_id`         | Aliased Model                       | `many2one`  | ✅  | ✅    | ir.model          |
| `alias_name`             | Alias Name                          | `char`      |     | ✅    |                   |
| `alias_parent_model_id`  | Parent Model                        | `many2one`  |     | ✅    | ir.model          |
| `alias_parent_thread_id` | Parent Record Thread ID             | `integer`   |     | ✅    |                   |
| `alias_status`           | Alias Status                        | `selection` |     | ✅    |                   |
| `create_date`            | Created on                          | `datetime`  |     | ✅    |                   |
| `create_uid`             | Created by                          | `many2one`  |     | ✅    | res.users         |
| `display_name`           | Display Name                        | `char`      |     |       |                   |
| `id`                     | ID                                  | `integer`   |     | ✅    |                   |
| `write_date`             | Last Updated on                     | `datetime`  |     | ✅    |                   |
| `write_uid`              | Last Updated by                     | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name              | Group                | Perms     |
| ----------------- | -------------------- | --------- |
| mail.alias.system | Role / Administrator | `R/W/C/D` |
| mail.alias.user   | Role / User          | `R`       |

### 🗃️ `hr.employee.category` — Employee Category

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation    |
| -------------- | --------------- | ----------- | --- | ----- | ----------- |
| `color`        | Color Index     | `integer`   |     | ✅    |             |
| `create_date`  | Created on      | `datetime`  |     | ✅    |             |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`      |     |       |             |
| `employee_ids` | Employees       | `many2many` |     | ✅    | hr.employee |
| `id`           | ID              | `integer`   |     | ✅    |             |
| `name`         | Tag Name        | `char`      | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                      | Group                                     | Perms     |
| ------------------------- | ----------------------------------------- | --------- |
| hr.employee.category.user | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.employee.category.emp  | Role / User                               | `R`       |

### 🗃️ `hr.manager.department.report` — Hr Manager Department Report

The base model, which is implicitly inherited by all models.

**Fields:**

| Field                           | Label                         | Type       | Req | Store | Relation    |
| ------------------------------- | ----------------------------- | ---------- | --- | ----- | ----------- |
| `display_name`                  | Display Name                  | `char`     |     |       |             |
| `employee_id`                   | Employee                      | `many2one` |     | ✅    | hr.employee |
| `has_department_manager_access` | Has Department Manager Access | `boolean`  |     |       |             |
| `id`                            | ID                            | `integer`  |     | ✅    |             |

### 🗃️ `hr.mixin` — hr.mixin

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.ui.menu` — Menu

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label           | Type        | Req | Store | Relation   |
| --------------- | --------------- | ----------- | --- | ----- | ---------- |
| `action`        | Action          | `reference` |     | ✅    |            |
| `active`        | Active          | `boolean`   |     | ✅    |            |
| `child_id`      | Child IDs       | `one2many`  |     | ✅    | ir.ui.menu |
| `complete_name` | Full Path       | `char`      |     |       |            |
| `create_date`   | Created on      | `datetime`  |     | ✅    |            |
| `create_uid`    | Created by      | `many2one`  |     | ✅    | res.users  |
| `display_name`  | Display Name    | `char`      |     |       |            |
| `group_ids`     | Groups          | `many2many` |     | ✅    | res.groups |
| `id`            | ID              | `integer`   |     | ✅    |            |
| `name`          | Menu            | `char`      | ✅  | ✅    |            |
| `parent_id`     | Parent Menu     | `many2one`  |     | ✅    | ir.ui.menu |
| `parent_path`   | Parent Path     | `char`      |     | ✅    |            |
| `sequence`      | Sequence        | `integer`   |     | ✅    |            |
| `web_icon`      | Web Icon File   | `char`      |     | ✅    |            |
| `web_icon_data` | Web Icon Image  | `binary`    |     | ✅    |            |
| `write_date`    | Last Updated on | `datetime`  |     | ✅    |            |
| `write_uid`     | Last Updated by | `many2one`  |     | ✅    | res.users  |

**Access Rights:**

| Name                    | Group                | Perms     |
| ----------------------- | -------------------- | --------- |
| ir_ui_menu group_system | Role / Administrator | `R/W/C/D` |
| ir_ui_menu group_user   | Role / User          | `R`       |

### 🗃️ `hr.employee.public` — Public Employee

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                          | Type        | Req | Store | Relation                |
| -------------------------------- | ------------------------------ | ----------- | --- | ----- | ----------------------- |
| `active`                         | Active                         | `boolean`   |     | ✅    |                         |
| `address_id`                     | Address                        | `many2one`  |     | ✅    | res.partner             |
| `allocation_display`             | Allocation Display             | `char`      |     |       |                         |
| `allocation_remaining_display`   | Allocation Remaining Display   | `char`      |     |       |                         |
| `avatar_1024`                    | Avatar 1024                    | `binary`    |     |       |                         |
| `avatar_128`                     | Avatar 128                     | `binary`    |     |       |                         |
| `avatar_1920`                    | Avatar                         | `binary`    |     |       |                         |
| `avatar_256`                     | Avatar 256                     | `binary`    |     |       |                         |
| `avatar_512`                     | Avatar 512                     | `binary`    |     |       |                         |
| `badge_ids`                      | Badge                          | `one2many`  |     |       | gamification.badge.user |
| `birthday_public_display_string` | Public Date of Birth           | `char`      |     |       |                         |
| `certification_ids`              | Certification                  | `one2many`  |     |       | hr.employee.skill       |
| `child_all_count`                | Child All Count                | `integer`   |     |       |                         |
| `child_count`                    | Child Count                    | `integer`   |     |       |                         |
| `child_ids`                      | Direct subordinates            | `one2many`  |     | ✅    | hr.employee.public      |
| `coach_id`                       | Coach                          | `many2one`  |     | ✅    | hr.employee.public      |
| `color`                          | Color                          | `integer`   |     | ✅    |                         |
| `company_id`                     | Company                        | `many2one`  |     | ✅    | res.company             |
| `country_code`                   | Country Code                   | `char`      |     |       |                         |
| `create_date`                    | Create Date                    | `datetime`  |     | ✅    |                         |
| `create_uid`                     | Created by                     | `many2one`  |     | ✅    | res.users               |
| `current_employee_skill_ids`     | Current Employee Skill         | `one2many`  |     |       | hr.employee.skill       |
| `department_color`               | Department Color               | `integer`   |     |       |                         |
| `department_id`                  | Department                     | `many2one`  |     | ✅    | hr.department           |
| `display_certification_page`     | Display Certification Page     | `boolean`   |     |       |                         |
| `display_name`                   | Display Name                   | `char`      |     |       |                         |
| `email`                          | Email                          | `char`      |     |       |                         |
| `employee_id`                    | Employee                       | `many2one`  |     | ✅    | hr.employee             |
| `employee_skill_ids`             | Skills                         | `one2many`  |     | ✅    | hr.employee.skill       |
| `expense_manager_id`             | Expense Manager                | `many2one`  |     | ✅    | res.users               |
| `filter_for_expense`             | Filter For Expense             | `boolean`   |     |       |                         |
| `friday_location_id`             | Friday                         | `many2one`  |     | ✅    | hr.work.location        |
| `has_badges`                     | Has Badges                     | `boolean`   |     |       |                         |
| `hr_icon_display`                | Hr Icon Display                | `selection` |     |       |                         |
| `hr_presence_state`              | Hr Presence State              | `selection` |     |       |                         |
| `id`                             | ID                             | `integer`   |     | ✅    |                         |
| `image_1024`                     | Image 1024                     | `binary`    |     |       |                         |
| `image_128`                      | Image 128                      | `binary`    |     |       |                         |
| `image_1920`                     | Image                          | `binary`    |     |       |                         |
| `image_256`                      | Image 256                      | `binary`    |     |       |                         |
| `image_512`                      | Image 512                      | `binary`    |     |       |                         |
| `im_status`                      | IM Status                      | `char`      |     |       |                         |
| `is_absent`                      | Absent Today                   | `boolean`   |     |       |                         |
| `is_manager`                     | Is Manager                     | `boolean`   |     |       |                         |
| `is_subordinate`                 | Is Subordinate                 | `boolean`   |     |       |                         |
| `is_user`                        | Is User                        | `boolean`   |     |       |                         |
| `job_id`                         | Job                            | `many2one`  |     | ✅    | hr.job                  |
| `job_title`                      | Job Title                      | `char`      |     |       |                         |
| `last_activity`                  | Last Activity                  | `date`      |     |       |                         |
| `last_activity_time`             | Last Activity Time             | `char`      |     |       |                         |
| `leave_date_to`                  | To Date                        | `date`      |     |       |                         |
| `leave_manager_id`               | Time Off Approver              | `many2one`  |     | ✅    | res.users               |
| `member_of_department`           | Member Of Department           | `boolean`   |     |       |                         |
| `mobile_phone`                   | Mobile Phone                   | `char`      |     | ✅    |                         |
| `mobility_card`                  | Mobility Card                  | `char`      |     | ✅    |                         |
| `monday_location_id`             | Monday                         | `many2one`  |     | ✅    | hr.work.location        |
| `name`                           | Name                           | `char`      |     | ✅    |                         |
| `newly_hired`                    | Newly Hired                    | `boolean`   |     |       |                         |
| `parent_id`                      | Manager                        | `many2one`  |     | ✅    | hr.employee.public      |
| `phone`                          | Phone                          | `char`      |     |       |                         |
| `resource_calendar_id`           | Resource Calendar              | `many2one`  |     | ✅    | resource.calendar       |
| `resource_id`                    | Resource                       | `many2one`  |     | ✅    | resource.resource       |
| `resume_line_ids`                | Resume lines                   | `one2many`  |     | ✅    | hr.resume.line          |
| `saturday_location_id`           | Saturday                       | `many2one`  |     | ✅    | hr.work.location        |
| `share`                          | Share User                     | `boolean`   |     |       |                         |
| `show_hr_icon_display`           | Show Hr Icon Display           | `boolean`   |     |       |                         |
| `show_leaves`                    | Able to see Remaining Time Off | `boolean`   |     |       |                         |
| `subordinate_ids`                | Subordinates                   | `one2many`  |     |       | hr.employee             |
| `sunday_location_id`             | Sunday                         | `many2one`  |     | ✅    | hr.work.location        |
| `thursday_location_id`           | Thursday                       | `many2one`  |     | ✅    | hr.work.location        |
| `today_location_name`            | Today Location Name            | `char`      |     | ✅    |                         |
| `tuesday_location_id`            | Tuesday                        | `many2one`  |     | ✅    | hr.work.location        |
| `tz`                             | Timezone                       | `selection` |     |       |                         |
| `user_id`                        | User                           | `many2one`  |     | ✅    | res.users               |
| `user_partner_id`                | User's partner                 | `many2one`  |     |       | res.partner             |
| `wednesday_location_id`          | Wednesday                      | `many2one`  |     | ✅    | hr.work.location        |
| `work_contact_id`                | Work Contact                   | `many2one`  |     | ✅    | res.partner             |
| `work_email`                     | Work Email                     | `char`      |     | ✅    |                         |
| `work_location_id`               | Work Location                  | `many2one`  |     | ✅    | hr.work.location        |
| `work_location_name`             | Work Location Name             | `char`      |     |       |                         |
| `work_location_type`             | Work Location Type             | `selection` |     |       |                         |
| `work_phone`                     | Work Phone                     | `char`      |     | ✅    |                         |
| `write_date`                     | Last Updated on                | `datetime`  |     | ✅    |                         |
| `write_uid`                      | Last Updated by                | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name               | Group       | Perms |
| ------------------ | ----------- | ----- |
| hr.employee_public | Role / User | `R`   |

**Record Rules:**

- **Employee multi company rule** (Global) `R/W/C/D`
  - Domain:
    `['|', '|', '|',         ('company_id', 'in', company_ids + [False]),         ('parent_id.user_id', '=', user.id),         ('id', '=', user.employee_id.parent_id.id),         ('user_id', '=', user.id)     ]`

### 🗃️ `resource.resource` — Resources

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label                | Type        | Req | Store | Relation          |
| ---------------------- | -------------------- | ----------- | --- | ----- | ----------------- |
| `active`               | Active               | `boolean`   |     | ✅    |                   |
| `avatar_128`           | Avatar 128           | `binary`    |     |       |                   |
| `calendar_id`          | Working Time         | `many2one`  |     | ✅    | resource.calendar |
| `color`                | Color                | `integer`   |     | ✅    |                   |
| `company_id`           | Company              | `many2one`  |     | ✅    | res.company       |
| `create_date`          | Created on           | `datetime`  |     | ✅    |                   |
| `create_uid`           | Created by           | `many2one`  |     | ✅    | res.users         |
| `department_id`        | Department           | `many2one`  |     |       | hr.department     |
| `display_name`         | Display Name         | `char`      |     |       |                   |
| `email`                | Email                | `char`      |     |       |                   |
| `employee_id`          | Employee             | `one2many`  |     | ✅    | hr.employee       |
| `employee_skill_ids`   | Skills               | `one2many`  |     |       | hr.employee.skill |
| `hr_icon_display`      | Hr Icon Display      | `selection` |     |       |                   |
| `id`                   | ID                   | `integer`   |     | ✅    |                   |
| `im_status`            | IM Status            | `char`      |     |       |                   |
| `job_title`            | Job Title            | `char`      |     |       |                   |
| `leave_date_to`        | To Date              | `date`      |     |       |                   |
| `name`                 | Name                 | `char`      | ✅  | ✅    |                   |
| `phone`                | Phone                | `char`      |     |       |                   |
| `resource_type`        | Type                 | `selection` | ✅  | ✅    |                   |
| `share`                | Share User           | `boolean`   |     |       |                   |
| `show_hr_icon_display` | Show Hr Icon Display | `boolean`   |     |       |                   |
| `time_efficiency`      | Efficiency Factor    | `float`     | ✅  | ✅    |                   |
| `tz`                   | Timezone             | `selection` | ✅  | ✅    |                   |
| `user_id`              | User                 | `many2one`  |     | ✅    | res.users         |
| `work_email`           | Work Email           | `char`      |     |       |                   |
| `work_location_id`     | Work Location        | `many2one`  |     |       | hr.work.location  |
| `work_phone`           | Work Phone           | `char`      |     |       |                   |
| `write_date`           | Last Updated on      | `datetime`  |     | ✅    |                   |
| `write_uid`            | Last Updated by      | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                                     | Group                                     | Perms     |
| ---------------------------------------- | ----------------------------------------- | --------- |
| resource.resource.user                   | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.employee.resource.manager             | Employees / Administrator                 | `R/W/C/D` |
| name_resource_resource_back_office_admin | OpenEduCat / Manager                      | `R/W/C`   |
| resource.resource                        | Role / Administrator                      | `R`       |
| resource.resource all                    | Role / User                               | `R`       |

**Record Rules:**

- **resource.resource multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `resource.calendar.leaves` — Resource Time Off Detail

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                     | Type        | Req | Store | Relation          |
| ---------------------------- | ------------------------- | ----------- | --- | ----- | ----------------- |
| `calendar_id`                | Working Hours             | `many2one`  |     | ✅    | resource.calendar |
| `company_id`                 | Company                   | `many2one`  |     | ✅    | res.company       |
| `create_date`                | Created on                | `datetime`  |     | ✅    |                   |
| `create_uid`                 | Created by                | `many2one`  |     | ✅    | res.users         |
| `date_from`                  | Start Date                | `datetime`  | ✅  | ✅    |                   |
| `date_to`                    | End Date                  | `datetime`  | ✅  | ✅    |                   |
| `display_name`               | Display Name              | `char`      |     |       |                   |
| `elligible_for_accrual_rate` | Eligible for Accrual Rate | `boolean`   |     | ✅    |                   |
| `holiday_id`                 | Time Off Request          | `many2one`  |     | ✅    | hr.leave          |
| `id`                         | ID                        | `integer`   |     | ✅    |                   |
| `name`                       | Reason                    | `char`      |     | ✅    |                   |
| `resource_id`                | Resource                  | `many2one`  |     | ✅    | resource.resource |
| `time_type`                  | Time Type                 | `selection` |     | ✅    |                   |
| `write_date`                 | Last Updated on           | `datetime`  |     | ✅    |                   |
| `write_uid`                  | Last Updated by           | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                          | Group                                   | Perms     |
| ----------------------------- | --------------------------------------- | --------- |
| resource_calendar_leaves_user | Time Off / Officer: Manage all requests | `R/W/C/D` |
| resource.calendar.leaves      | Role / Administrator                    | `R/W/C/D` |
| resource.calendar.leaves      | Role / User                             | `R/W/C/D` |

**Record Rules:**

- **resource.calendar.leaves: employee reads own or global** (1) `R`
  - Domain:
    `['|', ('resource_id', '=', False), ('resource_id.user_id', 'in', [False, user.id])]`
- **resource.calendar.leaves: employee modifies own** (1) `W/C/D`
  - Domain:
    `[('resource_id', '!=', False), ('resource_id.user_id', 'in', [False, user.id])]`
- **resource.calendar.leaves: admin modifies global** (2) `W/C/D`
  - Domain: `[('resource_id', '=', False)]`
- **resource.calendar.leaves: multi-company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Time Off Resources: Approver** (1) `R`
  - Domain: `[(1,'=',1)]`
- **Time Off Resources: All Approver** (80) `R/W/C/D`
  - Domain: `[(1,'=',1)]`

### 🗃️ `resource.calendar` — Resource Working Time

Calendar model for a resource. It has

    - attendance_ids: list of resource.calendar.attendance that are a working
                    interval in a given weekday.
    - leave_ids: list of leaves linked to this calendar. A leave can be general
                or linked to a specific resource, depending on its resource_id.

    All methods in this class use intervals. An interval is a tuple holding
    (begin_datetime, end_datetime). A list of intervals is therefore a list of
    tuples, holding several intervals of work or leaves.

**Fields:**

| Field                      | Label                        | Type        | Req | Store | Relation                     |
| -------------------------- | ---------------------------- | ----------- | --- | ----- | ---------------------------- |
| `active`                   | Active                       | `boolean`   |     | ✅    |                              |
| `associated_leaves_count`  | Time Off Count               | `integer`   |     |       |                              |
| `attendance_ids`           | Working Time                 | `one2many`  |     | ✅    | resource.calendar.attendance |
| `attendance_ids_1st_week`  | Working Time 1st Week        | `one2many`  |     |       | resource.calendar.attendance |
| `attendance_ids_2nd_week`  | Working Time 2nd Week        | `one2many`  |     |       | resource.calendar.attendance |
| `company_id`               | Company                      | `many2one`  |     | ✅    | res.company                  |
| `create_date`              | Created on                   | `datetime`  |     | ✅    |                              |
| `create_uid`               | Created by                   | `many2one`  |     | ✅    | res.users                    |
| `display_name`             | Display Name                 | `char`      |     |       |                              |
| `duration_based`           | Attendance based on duration | `boolean`   |     | ✅    |                              |
| `flexible_hours`           | Flexible Hours               | `boolean`   |     | ✅    |                              |
| `full_time_required_hours` | Full Time Equivalent         | `float`     |     | ✅    |                              |
| `global_leave_ids`         | Global Time Off              | `one2many`  |     | ✅    | resource.calendar.leaves     |
| `hours_per_day`            | Average Hour per Day         | `float`     |     | ✅    |                              |
| `hours_per_week`           | Hours per Week               | `float`     |     | ✅    |                              |
| `id`                       | ID                           | `integer`   |     | ✅    |                              |
| `is_fulltime`              | Is Full Time                 | `boolean`   |     |       |                              |
| `leave_ids`                | Time Off                     | `one2many`  |     | ✅    | resource.calendar.leaves     |
| `name`                     | Name                         | `char`      | ✅  | ✅    |                              |
| `schedule_type`            | Schedule Type                | `selection` | ✅  | ✅    |                              |
| `two_weeks_calendar`       | Calendar in 2 weeks mode     | `boolean`   |     | ✅    |                              |
| `two_weeks_explanation`    | Explanation                  | `char`      |     |       |                              |
| `tz`                       | Timezone                     | `selection` | ✅  | ✅    |                              |
| `tz_offset`                | Timezone offset              | `char`      |     |       |                              |
| `work_resources_count`     | Work Resources count         | `integer`   |     |       |                              |
| `work_time_rate`           | Work Time Rate               | `float`     |     |       |                              |
| `write_date`               | Last Updated on              | `datetime`  |     | ✅    |                              |
| `write_uid`                | Last Updated by              | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                               | Group                                     | Perms     |
| ---------------------------------- | ----------------------------------------- | --------- |
| hr.employee.resource.calendar.user | Employees / Officer: Manage all employees | `R/W/C/D` |
| resource.calendar.system           | Role / Administrator                      | `R/W/C/D` |
| resource.calendar.user             | Role / User                               | `R`       |

### 🗃️ `hr.payroll.structure.type` — Salary Structure Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                          | Label                 | Type       | Req | Store | Relation          |
| ------------------------------ | --------------------- | ---------- | --- | ----- | ----------------- |
| `country_code`                 | Country Code          | `char`     |     |       |                   |
| `country_id`                   | Country               | `many2one` |     | ✅    | res.country       |
| `create_date`                  | Created on            | `datetime` |     | ✅    |                   |
| `create_uid`                   | Created by            | `many2one` |     | ✅    | res.users         |
| `default_resource_calendar_id` | Working Hours         | `many2one` |     | ✅    | resource.calendar |
| `display_name`                 | Display Name          | `char`     |     |       |                   |
| `id`                           | ID                    | `integer`  |     | ✅    |                   |
| `name`                         | Salary Structure Type | `char`     |     | ✅    |                   |
| `write_date`                   | Last Updated on       | `datetime` |     | ✅    |                   |
| `write_uid`                    | Last Updated by       | `many2one` |     | ✅    | res.users         |

**Access Rights:**

| Name                                       | Group                     | Perms     |
| ------------------------------------------ | ------------------------- | --------- |
| hr.payroll.structure.type.contract.manager | Employees / Administrator | `R/W/C/D` |

**Record Rules:**

- **HR Payroll Structure Type: Multi Company** (Global) `R/W/C/D`
  - Domain:
    `['|', ('country_id', '=', False), ('country_id', 'in', user.env.companies.mapped('country_id').ids)]`

### 🗃️ `res.users` — User

Update of res.users class - add a preference about username for livechat purpose

**Fields:**

| Field                                       | Label                                                 | Type         | Req | Store | Relation                    |
| ------------------------------------------- | ----------------------------------------------------- | ------------ | --- | ----- | --------------------------- |
| `accesses_count`                            | # Access Rights                                       | `integer`    |     |       |                             |
| `access_token`                              | Access Token                                          | `char`       |     | ✅    |                             |
| `account_move_count`                        | Account Move Count                                    | `integer`    |     |       |                             |
| `action_id`                                 | Home Action                                           | `many2one`   |     | ✅    | ir.actions.actions          |
| `active`                                    | Active                                                | `boolean`    |     | ✅    |                             |
| `active_lang_count`                         | Active Lang Count                                     | `integer`    |     |       |                             |
| `active_partner`                            | Partner is Active                                     | `boolean`    |     |       |                             |
| `activity_calendar_event_id`                | Next Activity Calendar Event                          | `many2one`   |     |       | calendar.event              |
| `activity_date_deadline`                    | Next Activity Deadline                                | `date`       |     |       |                             |
| `activity_exception_decoration`             | Activity Exception Decoration                         | `selection`  |     |       |                             |
| `activity_exception_icon`                   | Icon                                                  | `char`       |     |       |                             |
| `activity_ids`                              | Activities                                            | `one2many`   |     |       | mail.activity               |
| `activity_state`                            | Activity State                                        | `selection`  |     |       |                             |
| `activity_summary`                          | Next Activity Summary                                 | `char`       |     |       |                             |
| `activity_type_icon`                        | Activity Type Icon                                    | `char`       |     |       |                             |
| `activity_type_id`                          | Next Activity Type                                    | `many2one`   |     |       | mail.activity.type          |
| `activity_user_id`                          | Responsible User                                      | `many2one`   |     |       | res.users                   |
| `additional_note`                           | Additional Note                                       | `text`       |     |       |                             |
| `all_group_ids`                             | Groups and implied groups                             | `many2many`  |     |       | res.groups                  |
| `api_key_ids`                               | API Keys                                              | `one2many`   |     | ✅    | res.users.apikeys           |
| `applicant_ids`                             | Applicants                                            | `one2many`   |     |       | hr.applicant                |
| `application_count`                         | Applications                                          | `integer`    |     |       |                             |
| `application_statistics`                    | Stats                                                 | `json`       |     |       |                             |
| `auth_passkey_key_ids`                      | Auth Passkey Key                                      | `one2many`   |     | ✅    | auth.passkey.key            |
| `autopost_bills`                            | Auto-post bills                                       | `selection`  | ✅  |       |                             |
| `available_invoice_template_pdf_report_ids` | Available Invoice Template Pdf Report                 | `one2many`   |     |       | ir.actions.report           |
| `available_peppol_eas`                      | Available Peppol Eas                                  | `json`       |     |       |                             |
| `avatar_1024`                               | Avatar 1024                                           | `binary`     |     |       |                             |
| `avatar_128`                                | Avatar 128                                            | `binary`     |     |       |                             |
| `avatar_1920`                               | Avatar                                                | `binary`     |     |       |                             |
| `avatar_256`                                | Avatar 256                                            | `binary`     |     |       |                             |
| `avatar_512`                                | Avatar 512                                            | `binary`     |     |       |                             |
| `badge_ids`                                 | Badges                                                | `one2many`   |     | ✅    | gamification.badge.user     |
| `bank_account_count`                        | Bank                                                  | `integer`    |     |       |                             |
| `bank_account_ids`                          | Bank Accounts                                         | `many2many`  |     |       | res.partner.bank            |
| `bank_ids`                                  | Banks                                                 | `one2many`   |     |       | res.partner.bank            |
| `barcode`                                   | Badge ID                                              | `char`       |     |       |                             |
| `bronze_badge`                              | Bronze badges count                                   | `integer`    |     |       |                             |
| `buyer_id`                                  | Buyer                                                 | `many2one`   |     |       | res.users                   |
| `calendar_default_privacy`                  | Calendar Default Privacy                              | `selection`  |     |       |                             |
| `calendar_last_notif_ack`                   | Last notification marked as read from base Calendar   | `datetime`   |     |       |                             |
| `can_edit_role`                             | Can Edit Role                                         | `boolean`    |     |       |                             |
| `can_publish`                               | Can Publish                                           | `boolean`    |     |       |                             |
| `category_id`                               | Tags                                                  | `many2many`  |     |       | res.partner.category        |
| `category_ids`                              | Employee Tags                                         | `many2many`  |     |       | hr.employee.category        |
| `certifications_company_count`              | Company Certifications Count                          | `integer`    |     |       |                             |
| `certifications_count`                      | Certifications Count                                  | `integer`    |     |       |                             |
| `channel_ids`                               | Channels                                              | `many2many`  |     |       | discuss.channel             |
| `channel_member_ids`                        | Channel Member                                        | `one2many`   |     |       | discuss.channel.member      |
| `chatbot_script_ids`                        | Chatbot Script                                        | `one2many`   |     |       | chatbot.script              |
| `chatter_position`                          | Chatter Position                                      | `selection`  |     | ✅    |                             |
| `child_ids`                                 | Childs                                                | `many2many`  |     | ✅    | res.users                   |
| `city`                                      | City                                                  | `char`       |     |       |                             |
| `client_id`                                 | Client ID                                             | `char`       |     | ✅    |                             |
| `client_secret`                             | Client Secret                                         | `char`       |     | ✅    |                             |
| `code`                                      | Company Code                                          | `char`       |     |       |                             |
| `color`                                     | Color Index                                           | `integer`    |     |       |                             |
| `comment`                                   | Notes                                                 | `html`       |     |       |                             |
| `commercial_company_name`                   | Company Name Entity                                   | `char`       |     |       |                             |
| `commercial_partner_id`                     | Commercial Entity                                     | `many2one`   |     |       | res.partner                 |
| `companies_count`                           | Number of Companies                                   | `integer`    |     |       |                             |
| `company_id`                                | Company                                               | `many2one`   | ✅  | ✅    | res.company                 |
| `company_ids`                               | Companies                                             | `many2many`  |     | ✅    | res.company                 |
| `company_name`                              | Company Name                                          | `char`       |     |       |                             |
| `company_registry`                          | Company ID                                            | `char`       |     |       |                             |
| `company_registry_label`                    | Company ID Label                                      | `char`       |     |       |                             |
| `company_registry_placeholder`              | Company Registry Placeholder                          | `char`       |     |       |                             |
| `company_type`                              | Company Type                                          | `selection`  |     |       |                             |
| `complete_name`                             | Complete Name                                         | `char`       |     |       |                             |
| `contact_address`                           | Complete Address                                      | `char`       |     |       |                             |
| `contact_address_inline`                    | Inlined Complete Address                              | `char`       |     |       |                             |
| `contract_ids`                              | Partner Contracts                                     | `one2many`   |     |       | account.analytic.account    |
| `country_code`                              | Country Code                                          | `char`       |     |       |                             |
| `country_id`                                | Country                                               | `many2one`   |     |       | res.country                 |
| `create_date`                               | Create Date                                           | `datetime`   |     | ✅    |                             |
| `create_employee`                           | Technical field, whether to create an employee        | `boolean`    |     |       |                             |
| `create_employee_id`                        | Technical field, bind user to this employee on create | `many2one`   |     |       | hr.employee                 |
| `create_uid`                                | Created by                                            | `many2one`   |     | ✅    | res.users                   |
| `credit`                                    | Total Receivable                                      | `monetary`   |     |       |                             |
| `credit_limit`                              | Credit Limit                                          | `float`      |     |       |                             |
| `credit_to_invoice`                         | Credit To Invoice                                     | `monetary`   |     |       |                             |
| `crm_team_ids`                              | Sales Teams                                           | `many2many`  |     |       | crm.team                    |
| `crm_team_member_ids`                       | Sales Team Members                                    | `one2many`   |     | ✅    | crm.team.member             |
| `currency_id`                               | Currency                                              | `many2one`   |     |       | res.currency                |
| `customer_rank`                             | Customer Rank                                         | `integer`    |     |       |                             |
| `dark_mode`                                 | Dark Mode                                             | `boolean`    |     | ✅    |                             |
| `days_sales_outstanding`                    | Days Sales Outstanding (DSO)                          | `float`      |     |       |                             |
| `debit`                                     | Total Payable                                         | `monetary`   |     |       |                             |
| `department_count`                          | Number of Departments                                 | `integer`    |     |       |                             |
| `department_ids`                            | Allowed Department                                    | `many2many`  |     | ✅    | op.department               |
| `dept_id`                                   | Department Name                                       | `many2one`   |     | ✅    | op.department               |
| `device_ids`                                | User devices                                          | `one2many`   |     | ✅    | res.device                  |
| `display_invoice_edi_format`                | Display Invoice Edi Format                            | `boolean`    |     |       |                             |
| `display_invoice_template_pdf_report_id`    | Display Invoice Template Pdf Report                   | `boolean`    |     |       |                             |
| `display_name`                              | Display Name                                          | `char`       |     |       |                             |
| `duplicate_bank_partner_ids`                | Duplicate Bank Partner                                | `many2many`  |     |       | res.partner                 |
| `email`                                     | Email                                                 | `char`       |     |       |                             |
| `email_domain_placeholder`                  | Email Domain Placeholder                              | `char`       |     |       |                             |
| `email_formatted`                           | Formatted Email                                       | `char`       |     |       |                             |
| `email_normalized`                          | Normalized Email                                      | `char`       |     |       |                             |
| `emergency_contact`                         | Emergency Contact                                     | `char`       |     |       |                             |
| `emergency_phone`                           | Emergency Phone                                       | `char`       |     |       |                             |
| `employee`                                  | Employee                                              | `boolean`    |     |       |                             |
| `employee_bank_account_ids`                 | Employee's Bank Accounts                              | `many2many`  |     |       | res.partner.bank            |
| `employee_count`                            | Employee Count                                        | `integer`    |     |       |                             |
| `employee_id`                               | Company employee                                      | `many2one`   |     |       | hr.employee                 |
| `employee_ids`                              | Related employee                                      | `one2many`   |     | ✅    | hr.employee                 |
| `employee_resource_calendar_id`             | Employee's Working Hours                              | `many2one`   |     |       | resource.calendar           |
| `employees_count`                           | Employees Count                                       | `integer`    |     |       |                             |
| `esign_initials`                            | Digitial Initials                                     | `binary`     |     | ✅    |                             |
| `esign_signature`                           | Digital Signature                                     | `binary`     |     | ✅    |                             |
| `event_count`                               | # Events                                              | `integer`    |     |       |                             |
| `fiscal_country_codes`                      | Fiscal Country Codes                                  | `char`       |     |       |                             |
| `fiscal_country_group_codes`                | Fiscal Country Group Codes                            | `json`       |     |       |                             |
| `friday_location_id`                        | Fridays                                               | `many2one`   |     |       | hr.work.location            |
| `function`                                  | Job Position                                          | `char`       |     |       |                             |
| `global_location_number`                    | GLN                                                   | `char`       |     |       |                             |
| `goal_ids`                                  | Goal                                                  | `one2many`   |     | ✅    | gamification.goal           |
| `gold_badge`                                | Gold badges count                                     | `integer`    |     |       |                             |
| `grievance_team_id`                         | Grievance Team                                        | `many2one`   |     | ✅    | grievance.team              |
| `group_ids`                                 | Groups                                                | `many2many`  |     | ✅    | res.groups                  |
| `group_on`                                  | Week Day                                              | `selection`  | ✅  |       |                             |
| `group_rfq`                                 | Group RFQ                                             | `selection`  | ✅  |       |                             |
| `groups_count`                              | # Groups                                              | `integer`    |     |       |                             |
| `has_access_livechat`                       | Has access to Livechat                                | `boolean`    |     |       |                             |
| `has_external_mail_server`                  | Has External Mail Server                              | `boolean`    |     |       |                             |
| `has_message`                               | Has Message                                           | `boolean`    |     |       |                             |
| `head_office`                               | Head Office                                           | `char`       |     |       |                             |
| `hr_contact`                                | HR Contact                                            | `char`       |     |       |                             |
| `hr_email`                                  | HR Email                                              | `char`       |     |       |                             |
| `hr_name`                                   | HR Name                                               | `char`       |     |       |                             |
| `id`                                        | ID                                                    | `integer`    |     | ✅    |                             |
| `ignore_abnormal_invoice_amount`            | Ignore Abnormal Invoice Amount                        | `boolean`    |     |       |                             |
| `ignore_abnormal_invoice_date`              | Ignore Abnormal Invoice Date                          | `boolean`    |     |       |                             |
| `image_1024`                                | Image 1024                                            | `binary`     |     |       |                             |
| `image_128`                                 | Image 128                                             | `binary`     |     |       |                             |
| `image_1920`                                | Image                                                 | `binary`     |     |       |                             |
| `image_256`                                 | Image 256                                             | `binary`     |     |       |                             |
| `image_512`                                 | Image 512                                             | `binary`     |     |       |                             |
| `im_status`                                 | IM Status                                             | `char`       |     |       |                             |
| `industry_id`                               | Industry                                              | `many2one`   |     |       | res.partner.industry        |
| `invoice_edi_format`                        | eInvoice format                                       | `selection`  |     |       |                             |
| `invoice_edi_format_store`                  | Invoice Edi Format Store                              | `char`       |     |       |                             |
| `invoice_ids`                               | Invoices                                              | `one2many`   |     |       | account.move                |
| `invoice_sending_method`                    | Invoice sending                                       | `selection`  |     |       |                             |
| `invoice_template_pdf_report_id`            | Invoice report                                        | `many2one`   |     |       | ir.actions.report           |
| `is_blacklisted`                            | Blacklist                                             | `boolean`    |     |       |                             |
| `is_company`                                | Is a Company                                          | `boolean`    |     |       |                             |
| `is_hr_user`                                | Is Hr User                                            | `boolean`    |     |       |                             |
| `is_in_call`                                | Is in call                                            | `boolean`    |     |       |                             |
| `is_out_of_office`                          | Out of Office                                         | `boolean`    |     |       |                             |
| `is_parent`                                 | Is a Parent                                           | `boolean`    |     |       |                             |
| `is_peppol_edi_format`                      | Is Peppol Edi Format                                  | `boolean`    |     |       |                             |
| `is_pickup_location`                        | Is Pickup Location                                    | `boolean`    |     |       |                             |
| `is_public`                                 | Is Public                                             | `boolean`    |     |       |                             |
| `is_published`                              | Is Published                                          | `boolean`    |     |       |                             |
| `is_seo_optimized`                          | SEO optimized                                         | `boolean`    |     |       |                             |
| `is_student`                                | Is a Student                                          | `boolean`    |     |       |                             |
| `is_system`                                 | Is System                                             | `boolean`    |     |       |                             |
| `is_ubl_format`                             | Is Ubl Format                                         | `boolean`    |     |       |                             |
| `is_venue`                                  | Venue                                                 | `boolean`    |     |       |                             |
| `job_title`                                 | Job Title                                             | `char`       |     |       |                             |
| `karma`                                     | Karma                                                 | `integer`    |     | ✅    |                             |
| `karma_tracking_ids`                        | Karma Changes                                         | `one2many`   |     | ✅    | gamification.karma.tracking |
| `km_home_work`                              | Home-Work Distance in Km                              | `integer`    |     |       |                             |
| `lang`                                      | Language                                              | `selection`  |     |       |                             |
| `leave_date_to`                             | To Date                                               | `date`       |     |       |                             |
| `livechat_channel_count`                    | Livechat Channel Count                                | `integer`    |     |       |                             |
| `livechat_channel_ids`                      | Livechat Channel                                      | `many2many`  |     | ✅    | im_livechat.channel         |
| `livechat_expertise_ids`                    | Live Chat Expertise                                   | `many2many`  |     |       | im_livechat.expertise       |
| `livechat_is_in_call`                       | Livechat Is In Call                                   | `boolean`    |     |       |                             |
| `livechat_lang_ids`                         | Livechat Languages                                    | `many2many`  |     |       | res.lang                    |
| `livechat_ongoing_session_count`            | Number of Ongoing sessions                            | `integer`    |     |       |                             |
| `livechat_username`                         | Livechat Username                                     | `char`       |     |       |                             |
| `log_ids`                                   | User log entries                                      | `one2many`   |     | ✅    | res.users.log               |
| `login`                                     | Login                                                 | `char`       | ✅  | ✅    |                             |
| `login_date`                                | Latest Login                                          | `datetime`   |     |       |                             |
| `logo_visible`                              | Show Company Logo in Sidebar                          | `boolean`    |     | ✅    |                             |
| `main_user_id`                              | Main User                                             | `many2one`   |     |       | res.users                   |
| `manual_im_status`                          | IM status manually set by the user                    | `selection`  |     | ✅    |                             |
| `meeting_count`                             | # Meetings                                            | `integer`    |     |       |                             |
| `meeting_ids`                               | Meetings                                              | `many2many`  |     |       | calendar.event              |
| `message_attachment_count`                  | Attachment Count                                      | `integer`    |     |       |                             |
| `message_bounce`                            | Bounce                                                | `integer`    |     |       |                             |
| `message_follower_ids`                      | Followers                                             | `one2many`   |     |       | mail.followers              |
| `message_has_error`                         | Message Delivery error                                | `boolean`    |     |       |                             |
| `message_has_error_counter`                 | Number of errors                                      | `integer`    |     |       |                             |
| `message_has_sms_error`                     | SMS Delivery error                                    | `boolean`    |     |       |                             |
| `message_ids`                               | Messages                                              | `one2many`   |     |       | mail.message                |
| `message_is_follower`                       | Is Follower                                           | `boolean`    |     |       |                             |
| `message_needaction`                        | Action Needed                                         | `boolean`    |     |       |                             |
| `message_needaction_counter`                | Number of Actions                                     | `integer`    |     |       |                             |
| `message_partner_ids`                       | Followers (Partners)                                  | `many2many`  |     |       | res.partner                 |
| `mobile_phone`                              | Work Mobile                                           | `char`       |     |       |                             |
| `monday_location_id`                        | Mondays                                               | `many2one`   |     |       | hr.work.location            |
| `my_activity_date_deadline`                 | My Activity Deadline                                  | `date`       |     |       |                             |
| `name`                                      | Name                                                  | `char`       |     |       |                             |
| `new_password`                              | Set Password                                          | `char`       |     |       |                             |
| `next_rank_id`                              | Next Rank                                             | `many2one`   |     | ✅    | gamification.karma.rank     |
| `notification_type`                         | Notification                                          | `selection`  | ✅  | ✅    |                             |
| `odoobot_failed`                            | Odoobot Failed                                        | `boolean`    |     | ✅    |                             |
| `odoobot_state`                             | OdooBot Status                                        | `selection`  |     | ✅    |                             |
| `offline_since`                             | Offline since                                         | `datetime`   |     |       |                             |
| `onesignal_device_id`                       | One Signal Device ID                                  | `char`       |     | ✅    |                             |
| `on_time_rate`                              | On-Time Delivery Rate                                 | `float`      |     |       |                             |
| `opportunity_count`                         | Opportunity Count                                     | `integer`    |     |       |                             |
| `opportunity_ids`                           | Opportunities                                         | `one2many`   |     |       | crm.lead                    |
| `outgoing_mail_server_id`                   | Outgoing Mail Server                                  | `many2one`   |     |       | ir.mail_server              |
| `outgoing_mail_server_type`                 | Outgoing Mail Server Type                             | `selection`  | ✅  |       |                             |
| `out_of_office_from`                        | Out Of Office From                                    | `datetime`   |     | ✅    |                             |
| `out_of_office_message`                     | Vacation Responder                                    | `html`       |     | ✅    |                             |
| `out_of_office_to`                          | Out Of Office To                                      | `datetime`   |     | ✅    |                             |
| `parent_id`                                 | Related Company                                       | `many2one`   |     |       | res.partner                 |
| `parent_name`                               | Parent name                                           | `char`       |     |       |                             |
| `partner_company_registry_placeholder`      | Partner Company Registry Placeholder                  | `char`       |     |       |                             |
| `partner_id`                                | Related Partner                                       | `many2one`   | ✅  | ✅    | res.partner                 |
| `partner_latitude`                          | Geo Latitude                                          | `float`      |     |       |                             |
| `partner_longitude`                         | Geo Longitude                                         | `float`      |     |       |                             |
| `partner_share`                             | Share Partner                                         | `boolean`    |     |       |                             |
| `partner_vat_placeholder`                   | Partner Vat Placeholder                               | `char`       |     |       |                             |
| `password`                                  | Password                                              | `char`       |     |       |                             |
| `payment_token_count`                       | Payment Token Count                                   | `integer`    |     |       |                             |
| `payment_token_ids`                         | Payment Tokens                                        | `one2many`   |     |       | payment.token               |
| `peppol_eas`                                | Peppol e-address (EAS)                                | `selection`  |     |       |                             |
| `peppol_endpoint`                           | Peppol Endpoint                                       | `char`       |     |       |                             |
| `phone`                                     | Phone                                                 | `char`       |     |       |                             |
| `phone_blacklisted`                         | Blacklisted Phone is Phone                            | `boolean`    |     |       |                             |
| `phone_mobile_search`                       | Phone Number                                          | `char`       |     |       |                             |
| `phone_sanitized`                           | Sanitized Number                                      | `char`       |     |       |                             |
| `phone_sanitized_blacklisted`               | Phone Blacklisted                                     | `boolean`    |     |       |                             |
| `picking_warn_msg`                          | Message for Stock Picking                             | `text`       |     |       |                             |
| `pin`                                       | PIN                                                   | `char`       |     |       |                             |
| `pin_whatsapp_contact_id`                   | Pin Whatsapp Contact                                  | `char`       |     | ✅    |                             |
| `placement_team_id`                         | Placement Team Members                                | `many2one`   |     | ✅    | op.placement.cell           |
| `presence_ids`                              | Presence                                              | `one2many`   |     | ✅    | mail.presence               |
| `private_city`                              | Private City                                          | `char`       |     |       |                             |
| `private_country_id`                        | Private Country                                       | `many2one`   |     |       | res.country                 |
| `private_email`                             | Private Email                                         | `char`       |     |       |                             |
| `private_phone`                             | Private Phone                                         | `char`       |     |       |                             |
| `private_state_id`                          | Private State                                         | `many2one`   |     |       | res.country.state           |
| `private_street`                            | Private Street                                        | `char`       |     |       |                             |
| `private_street2`                           | Private Street2                                       | `char`       |     |       |                             |
| `private_zip`                               | Private Zip                                           | `char`       |     |       |                             |
| `properties`                                | Properties                                            | `properties` |     |       |                             |
| `properties_base_definition_id`             | Properties Base Definition                            | `many2one`   |     |       | properties.base.definition  |
| `property_account_payable_id`               | Account Payable                                       | `many2one`   |     |       | account.account             |
| `property_account_position_id`              | Fiscal Position                                       | `many2one`   |     |       | account.fiscal.position     |
| `property_account_receivable_id`            | Account Receivable                                    | `many2one`   |     |       | account.account             |
| `property_delivery_carrier_id`              | Delivery Method                                       | `many2one`   |     |       | delivery.carrier            |
| `property_inbound_payment_method_line_id`   | Property Inbound Payment Method Line                  | `many2one`   |     |       | account.payment.method.line |
| `property_outbound_payment_method_line_id`  | Property Outbound Payment Method Line                 | `many2one`   |     |       | account.payment.method.line |
| `property_payment_term_id`                  | Customer Payment Terms                                | `many2one`   |     |       | account.payment.term        |
| `property_product_pricelist`                | Pricelist                                             | `many2one`   |     |       | product.pricelist           |
| `property_purchase_currency_id`             | Supplier Currency                                     | `many2one`   |     |       | res.currency                |
| `property_stock_customer`                   | Customer Location                                     | `many2one`   |     |       | stock.location              |
| `property_stock_supplier`                   | Vendor Location                                       | `many2one`   |     |       | stock.location              |
| `property_supplier_payment_term_id`         | Vendor Payment Terms                                  | `many2one`   |     |       | account.payment.term        |
| `property_warehouse_id`                     | Default Warehouse                                     | `many2one`   |     | ✅    | stock.warehouse             |
| `purchase_line_ids`                         | Purchase Lines                                        | `one2many`   |     |       | purchase.order.line         |
| `purchase_order_count`                      | Purchase Order Count                                  | `integer`    |     |       |                             |
| `purchase_warn_msg`                         | Message for Purchase Order                            | `text`       |     |       |                             |
| `rank_id`                                   | Rank                                                  | `many2one`   |     | ✅    | gamification.karma.rank     |
| `rating_ids`                                | Ratings                                               | `one2many`   |     |       | rating.rating               |
| `receipt_reminder_email`                    | Receipt Reminder                                      | `boolean`    |     |       |                             |
| `ref`                                       | Reference                                             | `char`       |     |       |                             |
| `ref_company_ids`                           | Companies that refers to partner                      | `one2many`   |     |       | res.company                 |
| `refresh_token`                             | Refresh Token                                         | `char`       |     | ✅    |                             |
| `reminder_date_before_receipt`              | Days Before Receipt                                   | `integer`    |     |       |                             |
| `resource_calendar_id`                      | Default Working Hours                                 | `many2one`   |     |       | resource.calendar           |
| `resource_ids`                              | Resources                                             | `one2many`   |     | ✅    | resource.resource           |
| `res_users_settings_id`                     | Settings                                              | `many2one`   |     |       | res.users.settings          |
| `res_users_settings_ids`                    | Res Users Settings                                    | `one2many`   |     | ✅    | res.users.settings          |
| `role`                                      | Role                                                  | `selection`  |     |       |                             |
| `role_ids`                                  | User Roles                                            | `many2many`  |     | ✅    | res.role                    |
| `role_line_ids`                             | Role lines                                            | `one2many`   |     | ✅    | res.users.role.line         |
| `rtc_session_ids`                           | Rtc Session                                           | `one2many`   |     |       | discuss.channel.rtc.session |
| `rules_count`                               | # Record Rules                                        | `integer`    |     |       |                             |
| `sale_order_count`                          | Sale Order Count                                      | `integer`    |     |       |                             |
| `sale_order_ids`                            | Sales Order                                           | `one2many`   |     |       | sale.order                  |
| `sale_team_id`                              | User Sales Team                                       | `many2one`   |     | ✅    | crm.team                    |
| `sale_warn_msg`                             | Message for Sales Order                               | `text`       |     |       |                             |
| `same_company_registry_partner_id`          | Partner with same Company Registry                    | `many2one`   |     |       | res.partner                 |
| `same_vat_partner_id`                       | Partner with same Tax ID                              | `many2one`   |     |       | res.partner                 |
| `saturday_location_id`                      | Saturdays                                             | `many2one`   |     |       | hr.work.location            |
| `self`                                      | Self                                                  | `many2one`   |     |       | res.partner                 |
| `seo_name`                                  | Seo name                                              | `char`       |     |       |                             |
| `share`                                     | Share User                                            | `boolean`    |     | ✅    |                             |
| `show_alert`                                | Show Alert                                            | `boolean`    |     |       |                             |
| `show_credit_limit`                         | Show Credit Limit                                     | `boolean`    |     |       |                             |
| `signature`                                 | Email Signature                                       | `html`       |     | ✅    |                             |
| `signup_type`                               | Signup Token Type                                     | `char`       |     |       |                             |
| `silver_badge`                              | Silver badges count                                   | `integer`    |     |       |                             |
| `specific_property_product_pricelist`       | Specific Property Product Pricelist                   | `many2one`   |     |       | product.pricelist           |
| `state`                                     | Status                                                | `selection`  |     |       |                             |
| `state_id`                                  | State                                                 | `many2one`   |     |       | res.country.state           |
| `static_map_url`                            | Static Map Url                                        | `char`       |     |       |                             |
| `static_map_url_is_valid`                   | Static Map Url Is Valid                               | `boolean`    |     |       |                             |
| `street`                                    | Street                                                | `char`       |     |       |                             |
| `street2`                                   | Street2                                               | `char`       |     |       |                             |
| `student_line`                              | Line                                                  | `many2one`   |     | ✅    | op.student                  |
| `suggest_based_on`                          | Suggest Based On                                      | `char`       |     |       |                             |
| `suggest_days`                              | Suggest Days                                          | `integer`    |     |       |                             |
| `suggest_percent`                           | Suggest Percent                                       | `integer`    |     |       |                             |
| `sunday_location_id`                        | Sundays                                               | `many2one`   |     |       | hr.work.location            |
| `supplier_invoice_count`                    | # Vendor Bills                                        | `integer`    |     |       |                             |
| `supplier_rank`                             | Supplier Rank                                         | `integer`    |     |       |                             |
| `thursday_location_id`                      | Thursdays                                             | `many2one`   |     |       | hr.work.location            |
| `ticket_count`                              | Ticket Count                                          | `integer`    |     |       |                             |
| `title`                                     | Title                                                 | `many2one`   |     |       | res.partner.title           |
| `total_invoiced`                            | Total Invoiced                                        | `monetary`   |     |       |                             |
| `totp_enabled`                              | Two-factor authentication                             | `boolean`    |     |       |                             |
| `totp_last_counter`                         | Totp Last Counter                                     | `integer`    |     | ✅    |                             |
| `totp_secret`                               | Totp Secret                                           | `char`       |     |       |                             |
| `totp_trusted_device_ids`                   | Trusted Devices                                       | `one2many`   |     | ✅    | auth_totp.device            |
| `tour_enabled`                              | Onboarding                                            | `boolean`    |     | ✅    |                             |
| `trust`                                     | Degree of trust you have in this debtor               | `selection`  |     |       |                             |
| `tuesday_location_id`                       | Tuesdays                                              | `many2one`   |     |       | hr.work.location            |
| `type`                                      | Address Type                                          | `selection`  |     |       |                             |
| `type_address_label`                        | Address Type Description                              | `char`       |     |       |                             |
| `tz`                                        | Timezone                                              | `selection`  |     |       |                             |
| `tz_offset`                                 | Timezone offset                                       | `char`       |     |       |                             |
| `use_partner_credit_limit`                  | Partner Limit                                         | `boolean`    |     |       |                             |
| `user_id`                                   | Salesperson                                           | `many2one`   |     |       | res.users                   |
| `user_ids`                                  | Users                                                 | `one2many`   |     |       | res.users                   |
| `user_line`                                 | User Line                                             | `one2many`   |     | ✅    | op.student                  |
| `user_livechat_username`                    | User Livechat Username                                | `char`       |     |       |                             |
| `vat`                                       | Tax ID                                                | `char`       |     |       |                             |
| `vat_label`                                 | Tax ID Label                                          | `char`       |     |       |                             |
| `view_group_hierarchy`                      | Technical field for user group setting                | `json`       |     |       |                             |
| `visa_expire`                               | Visa Expiration Date                                  | `date`       |     |       |                             |
| `visitor_ids`                               | Visitors                                              | `one2many`   |     |       | website.visitor             |
| `website`                                   | Website Link                                          | `char`       |     |       |                             |
| `website_absolute_url`                      | Website Absolute URL                                  | `char`       |     |       |                             |
| `website_description`                       | Website Partner Full Description                      | `html`       |     |       |                             |
| `website_id`                                | Website                                               | `many2one`   |     | ✅    | website                     |
| `website_message_ids`                       | Website Messages                                      | `one2many`   |     |       | mail.message                |
| `website_meta_description`                  | Website meta description                              | `text`       |     |       |                             |
| `website_meta_keywords`                     | Website meta keywords                                 | `char`       |     |       |                             |
| `website_meta_og_img`                       | Website opengraph image                               | `char`       |     |       |                             |
| `website_meta_title`                        | Website meta title                                    | `char`       |     |       |                             |
| `website_published`                         | Visible on current website                            | `boolean`    |     |       |                             |
| `website_short_description`                 | Website Partner Short Description                     | `text`       |     |       |                             |
| `website_url`                               | Website URL                                           | `char`       |     |       |                             |
| `wednesday_location_id`                     | Wednesdays                                            | `many2one`   |     |       | hr.work.location            |
| `wishlist_ids`                              | Wishlist                                              | `one2many`   |     |       | product.wishlist            |
| `work_contact_id`                           | Work Contact                                          | `many2one`   |     |       | res.partner                 |
| `work_email`                                | Work Email                                            | `char`       |     |       |                             |
| `work_location_id`                          | Work Location                                         | `many2one`   |     |       | hr.work.location            |
| `work_location_name`                        | Work Location Name                                    | `char`       |     |       |                             |
| `work_location_type`                        | Work Location Type                                    | `selection`  |     |       |                             |
| `work_phone`                                | Work Phone                                            | `char`       |     |       |                             |
| `write_date`                                | Last Updated on                                       | `datetime`   |     | ✅    |                             |
| `write_uid`                                 | Last Updated by                                       | `many2one`   |     | ✅    | res.users                   |
| `zip`                                       | Zip                                                   | `char`       |     |       |                             |

**Access Rights:**

| Name                             | Group            | Perms     |
| -------------------------------- | ---------------- | --------- |
| access_op_placement_cell_res     | Placement / User | `R/W/C`   |
| name_res_users_back_office_admin | Parent / Manager | `R/W/C/D` |
| res_users group_erp_manager      | Access Rights    | `R/W/C/D` |
| res_users all                    | Role / Portal    | `R`       |
| res_users all                    | Role / Public    | `R`       |
| res_users all                    | Role / User      | `R`       |

**Record Rules:**

- **user rule** (Global) `R/W/C/D`
  - Domain: `['|', ('share', '=', False), ('company_ids', 'in', company_ids)]`
- **portal user access** (10) `R/W/C/D`
  - Domain: `[('commercial_partner_id', '=', user.commercial_partner_id.id)]`

### 🗃️ `hr.work.location` — Work Location

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label           | Type        | Req | Store | Relation    |
| ----------------- | --------------- | ----------- | --- | ----- | ----------- |
| `active`          | Active          | `boolean`   |     | ✅    |             |
| `address_id`      | Work Address    | `many2one`  | ✅  | ✅    | res.partner |
| `company_id`      | Company         | `many2one`  | ✅  | ✅    | res.company |
| `create_date`     | Created on      | `datetime`  |     | ✅    |             |
| `create_uid`      | Created by      | `many2one`  |     | ✅    | res.users   |
| `display_name`    | Display Name    | `char`      |     |       |             |
| `id`              | ID              | `integer`   |     | ✅    |             |
| `location_number` | Location Number | `char`      |     | ✅    |             |
| `location_type`   | Cover Image     | `selection` | ✅  | ✅    |             |
| `name`            | Work Location   | `char`      | ✅  | ✅    |             |
| `write_date`      | Last Updated on | `datetime`  |     | ✅    |             |
| `write_uid`       | Last Updated by | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                            | Group                     | Perms     |
| ------------------------------- | ------------------------- | --------- |
| access_hr_work_location_manager | Employees / Administrator | `R/W/C/D` |
| access_hr_work_location_user    | Role / User               | `R`       |
