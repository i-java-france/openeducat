---
title: "Accounting PDF Reports"
module: "accounting_pdf_reports"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Invoicing Management"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/____________________]
---

# 🟢 Accounting PDF Reports

> **Module:** `accounting_pdf_reports` | **Version:** `19.0.1.0` **Category:** Invoicing
> Management | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[account]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `Invoicing/Accounting/Ledgers`
- `Invoicing/Accounting/Ledgers/General Ledger`
- `Invoicing/Accounting/Ledgers/Partner Ledger`
- `Invoicing/Configuration/Financial Reports`
- `Invoicing/Configuration/Financial Reports/Account Reports`
- `Invoicing/Reporting/PDF Reports`
- `Invoicing/Reporting/PDF Reports/Aged Partner Balance`
- `Invoicing/Reporting/PDF Reports/Balance Sheet`
- `Invoicing/Reporting/PDF Reports/General Ledger`
- `Invoicing/Reporting/PDF Reports/Journals Audit`
- `Invoicing/Reporting/PDF Reports/Partner Ledger`
- `Invoicing/Reporting/PDF Reports/Profit and Loss`
- `Invoicing/Reporting/PDF Reports/Tax Report`
- `Invoicing/Reporting/PDF Reports/Trial Balance`

### Views

- `* INHERIT Accounting Report (form)`
- `* INHERIT General Ledger (form)`
- `* INHERIT Journals Audit (form)`
- `* INHERIT Partner Ledger (form)`
- `* INHERIT Tax Reports (form)`
- `* INHERIT Trial Balance (form)`
- `Aged Partner Balance (form)`
- `Common Report (form)`
- `account.account.type.form (form)`
- `account.account.type.search (search)`
- `account.account.type.tree (list)`
- `account.financial.report.form (form)`
- `account.financial.report.search (search)`
- `account.financial.report.tree (list)`
- `report_agedpartnerbalance (qweb)`
- `report_financial (qweb)`
- `report_general_ledger (qweb)`
- `report_journal (qweb)`
- `report_journal_entries (qweb)`
- `report_partnerledger (qweb)`
- `report_tax (qweb)`
- `report_trialbalance (qweb)`

### Reports

- `Aged Partner Balance`
- `Financial Report`
- `General Ledger`
- `Journals Audit`
- `Journals Entries`
- `Partner Ledger`
- `Tax Report`
- `Trial Balance`

## 🛠️ Technical Documentation

**26 model(s) defined by this module:**

### 🗃️ `account.aged.trial.balance` — Account Aged Trial balance Report

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field              | Label                | Type        | Req | Store | Relation        |
| ------------------ | -------------------- | ----------- | --- | ----- | --------------- |
| `company_id`       | Company              | `many2one`  | ✅  | ✅    | res.company     |
| `create_date`      | Created on           | `datetime`  |     | ✅    |                 |
| `create_uid`       | Created by           | `many2one`  |     | ✅    | res.users       |
| `date_from`        | Start Date           | `date`      |     | ✅    |                 |
| `date_to`          | End Date             | `date`      |     | ✅    |                 |
| `display_name`     | Display Name         | `char`      |     |       |                 |
| `id`               | ID                   | `integer`   |     | ✅    |                 |
| `journal_ids`      | Journals             | `many2many` | ✅  | ✅    | account.journal |
| `partner_ids`      | Partners             | `many2many` |     | ✅    | res.partner     |
| `period_length`    | Period Length (days) | `integer`   | ✅  | ✅    |                 |
| `result_selection` | Partner's            | `selection` | ✅  | ✅    |                 |
| `target_move`      | Target Moves         | `selection` | ✅  | ✅    |                 |
| `write_date`       | Last Updated on      | `datetime`  |     | ✅    |                 |
| `write_uid`        | Last Updated by      | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                                       | Group                | Perms     |
| ------------------------------------------ | -------------------- | --------- |
| access.account.aged.trial.balance.bmanager | Accounting / Advisor | `R/W/C/D` |
| access.account.aged.trial.balance          | Contact / Accountant | `R/W/C/D` |

### 🗃️ `account.common.account.report` — Account Common Account Report

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                  | Label             | Type        | Req | Store | Relation                 |
| ---------------------- | ----------------- | ----------- | --- | ----- | ------------------------ |
| `account_ids`          | Accounts          | `many2many` |     | ✅    | account.account          |
| `analytic_account_ids` | Analytic Accounts | `many2many` |     | ✅    | account.analytic.account |
| `company_id`           | Company           | `many2one`  | ✅  | ✅    | res.company              |
| `create_date`          | Created on        | `datetime`  |     | ✅    |                          |
| `create_uid`           | Created by        | `many2one`  |     | ✅    | res.users                |
| `date_from`            | Start Date        | `date`      |     | ✅    |                          |
| `date_to`              | End Date          | `date`      |     | ✅    |                          |
| `display_account`      | Display Accounts  | `selection` | ✅  | ✅    |                          |
| `display_name`         | Display Name      | `char`      |     |       |                          |
| `id`                   | ID                | `integer`   |     | ✅    |                          |
| `journal_ids`          | Journals          | `many2many` | ✅  | ✅    | account.journal          |
| `partner_ids`          | Partners          | `many2many` |     | ✅    | res.partner              |
| `target_move`          | Target Moves      | `selection` | ✅  | ✅    |                          |
| `write_date`           | Last Updated on   | `datetime`  |     | ✅    |                          |
| `write_uid`            | Last Updated by   | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                                 | Group       | Perms |
| ------------------------------------ | ----------- | ----- |
| access_account_common_account_report | Role / User | `R`   |

### 🗃️ `account.common.partner.report` — Account Common Partner Report

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field              | Label           | Type        | Req | Store | Relation        |
| ------------------ | --------------- | ----------- | --- | ----- | --------------- |
| `company_id`       | Company         | `many2one`  | ✅  | ✅    | res.company     |
| `create_date`      | Created on      | `datetime`  |     | ✅    |                 |
| `create_uid`       | Created by      | `many2one`  |     | ✅    | res.users       |
| `date_from`        | Start Date      | `date`      |     | ✅    |                 |
| `date_to`          | End Date        | `date`      |     | ✅    |                 |
| `display_name`     | Display Name    | `char`      |     |       |                 |
| `id`               | ID              | `integer`   |     | ✅    |                 |
| `journal_ids`      | Journals        | `many2many` | ✅  | ✅    | account.journal |
| `partner_ids`      | Partners        | `many2many` |     | ✅    | res.partner     |
| `result_selection` | Partner's       | `selection` | ✅  | ✅    |                 |
| `target_move`      | Target Moves    | `selection` | ✅  | ✅    |                 |
| `write_date`       | Last Updated on | `datetime`  |     | ✅    |                 |
| `write_uid`        | Last Updated by | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                                 | Group       | Perms |
| ------------------------------------ | ----------- | ----- |
| access_account_common_partner_report | Role / User | `R`   |

### 🗃️ `account.common.report` — Account Common Report

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation        |
| -------------- | --------------- | ----------- | --- | ----- | --------------- |
| `company_id`   | Company         | `many2one`  | ✅  | ✅    | res.company     |
| `create_date`  | Created on      | `datetime`  |     | ✅    |                 |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users       |
| `date_from`    | Start Date      | `date`      |     | ✅    |                 |
| `date_to`      | End Date        | `date`      |     | ✅    |                 |
| `display_name` | Display Name    | `char`      |     |       |                 |
| `id`           | ID              | `integer`   |     | ✅    |                 |
| `journal_ids`  | Journals        | `many2many` | ✅  | ✅    | account.journal |
| `target_move`  | Target Moves    | `selection` | ✅  | ✅    |                 |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |                 |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                         | Group       | Perms     |
| ---------------------------- | ----------- | --------- |
| access_account_common_report | Role / User | `R/W/C/D` |

### 🗃️ `accounting.report` — Accounting Report

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field               | Label                        | Type        | Req | Store | Relation                 |
| ------------------- | ---------------------------- | ----------- | --- | ----- | ------------------------ |
| `account_report_id` | Account Reports              | `many2one`  | ✅  | ✅    | account.financial.report |
| `company_id`        | Company                      | `many2one`  | ✅  | ✅    | res.company              |
| `create_date`       | Created on                   | `datetime`  |     | ✅    |                          |
| `create_uid`        | Created by                   | `many2one`  |     | ✅    | res.users                |
| `date_from`         | Start Date                   | `date`      |     | ✅    |                          |
| `date_from_cmp`     | Start Date                   | `date`      |     | ✅    |                          |
| `date_to`           | End Date                     | `date`      |     | ✅    |                          |
| `date_to_cmp`       | End Date                     | `date`      |     | ✅    |                          |
| `debit_credit`      | Display Debit/Credit Columns | `boolean`   |     | ✅    |                          |
| `display_name`      | Display Name                 | `char`      |     |       |                          |
| `enable_filter`     | Enable Comparison            | `boolean`   |     | ✅    |                          |
| `filter_cmp`        | Filter by                    | `selection` | ✅  | ✅    |                          |
| `id`                | ID                           | `integer`   |     | ✅    |                          |
| `journal_ids`       | Journals                     | `many2many` | ✅  | ✅    | account.journal          |
| `label_filter`      | Column Label                 | `char`      |     | ✅    |                          |
| `target_move`       | Target Moves                 | `selection` | ✅  | ✅    |                          |
| `write_date`        | Last Updated on              | `datetime`  |     | ✅    |                          |
| `write_uid`         | Last Updated by              | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                              | Group                | Perms     |
| --------------------------------- | -------------------- | --------- |
| access.accounting.report.bmanager | Accounting / Advisor | `R/W/C/D` |
| access.accounting.report          | Contact / Accountant | `R/W/C/D` |

### 🗃️ `account.report.partner.ledger` — Account Partner Ledger

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field              | Label              | Type        | Req | Store | Relation        |
| ------------------ | ------------------ | ----------- | --- | ----- | --------------- |
| `amount_currency`  | With Currency      | `boolean`   |     | ✅    |                 |
| `company_id`       | Company            | `many2one`  | ✅  | ✅    | res.company     |
| `create_date`      | Created on         | `datetime`  |     | ✅    |                 |
| `create_uid`       | Created by         | `many2one`  |     | ✅    | res.users       |
| `date_from`        | Start Date         | `date`      |     | ✅    |                 |
| `date_to`          | End Date           | `date`      |     | ✅    |                 |
| `display_name`     | Display Name       | `char`      |     |       |                 |
| `id`               | ID                 | `integer`   |     | ✅    |                 |
| `journal_ids`      | Journals           | `many2many` | ✅  | ✅    | account.journal |
| `partner_ids`      | Partners           | `many2many` |     | ✅    | res.partner     |
| `reconciled`       | Reconciled Entries | `boolean`   |     | ✅    |                 |
| `result_selection` | Partner's          | `selection` | ✅  | ✅    |                 |
| `target_move`      | Target Moves       | `selection` | ✅  | ✅    |                 |
| `write_date`       | Last Updated on    | `datetime`  |     | ✅    |                 |
| `write_uid`        | Last Updated by    | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                                          | Group                | Perms     |
| --------------------------------------------- | -------------------- | --------- |
| access.account.report.partner.ledger.bmanager | Accounting / Advisor | `R/W/C/D` |
| access.account.report.partner.ledger          | Contact / Accountant | `R/W/C/D` |

### 🗃️ `account.print.journal` — Account Print Journal

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field             | Label             | Type        | Req | Store | Relation        |
| ----------------- | ----------------- | ----------- | --- | ----- | --------------- |
| `amount_currency` | With Currency     | `boolean`   |     | ✅    |                 |
| `company_id`      | Company           | `many2one`  | ✅  | ✅    | res.company     |
| `create_date`     | Created on        | `datetime`  |     | ✅    |                 |
| `create_uid`      | Created by        | `many2one`  |     | ✅    | res.users       |
| `date_from`       | Start Date        | `date`      |     | ✅    |                 |
| `date_to`         | End Date          | `date`      |     | ✅    |                 |
| `display_name`    | Display Name      | `char`      |     |       |                 |
| `id`              | ID                | `integer`   |     | ✅    |                 |
| `journal_ids`     | Journals          | `many2many` | ✅  | ✅    | account.journal |
| `sort_selection`  | Entries Sorted by | `selection` | ✅  | ✅    |                 |
| `target_move`     | Target Moves      | `selection` | ✅  | ✅    |                 |
| `write_date`      | Last Updated on   | `datetime`  |     | ✅    |                 |
| `write_uid`       | Last Updated by   | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                                          | Group                | Perms     |
| --------------------------------------------- | -------------------- | --------- |
| access.account.account.print.journal.bmanager | Accounting / Advisor | `R/W/C/D` |
| access.account.print.journal                  | Contact / Accountant | `R/W/C`   |

### 🗃️ `account.financial.report` — Account Report

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label                  | Type        | Req | Store | Relation                 |
| ------------------- | ---------------------- | ----------- | --- | ----- | ------------------------ |
| `account_ids`       | Accounts               | `many2many` |     | ✅    | account.account          |
| `account_report_id` | Report Value           | `many2one`  |     | ✅    | account.financial.report |
| `account_type_ids`  | Account Types          | `many2many` |     | ✅    | account.account.type     |
| `children_ids`      | Account Report         | `one2many`  |     | ✅    | account.financial.report |
| `create_date`       | Created on             | `datetime`  |     | ✅    |                          |
| `create_uid`        | Created by             | `many2one`  |     | ✅    | res.users                |
| `display_detail`    | Display details        | `selection` |     | ✅    |                          |
| `display_name`      | Display Name           | `char`      |     |       |                          |
| `id`                | ID                     | `integer`   |     | ✅    |                          |
| `level`             | Level                  | `integer`   |     | ✅    |                          |
| `name`              | Report Name            | `char`      | ✅  | ✅    |                          |
| `parent_id`         | Parent                 | `many2one`  |     | ✅    | account.financial.report |
| `sequence`          | Sequence               | `integer`   |     | ✅    |                          |
| `sign`              | Sign on Reports        | `selection` | ✅  | ✅    |                          |
| `style_overwrite`   | Financial Report Style | `selection` |     | ✅    |                          |
| `type`              | Type                   | `selection` |     | ✅    |                          |
| `write_date`        | Last Updated on        | `datetime`  |     | ✅    |                          |
| `write_uid`         | Last Updated by        | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                                     | Group                | Perms     |
| ---------------------------------------- | -------------------- | --------- |
| access.account.financial.report.bmanager | Accounting / Advisor | `R/W/C/D` |
| access.account.financial.report.manager  | Contact / Accountant | `R/W/C/D` |

### 🗃️ `account.tax.report` — Account Tax Report

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label             | Type       | Req | Store | Relation                |
| --------------- | ----------------- | ---------- | --- | ----- | ----------------------- |
| `country_id`    | Country           | `many2one` | ✅  | ✅    | res.country             |
| `create_date`   | Created on        | `datetime` |     | ✅    |                         |
| `create_uid`    | Created by        | `many2one` |     | ✅    | res.users               |
| `display_name`  | Display Name      | `char`     |     |       |                         |
| `id`            | ID                | `integer`  |     | ✅    |                         |
| `line_ids`      | Report Lines      | `one2many` |     | ✅    | account.tax.report.line |
| `name`          | Name              | `char`     | ✅  | ✅    |                         |
| `root_line_ids` | Root Report Lines | `one2many` |     | ✅    | account.tax.report.line |
| `write_date`    | Last Updated on   | `datetime` |     | ✅    |                         |
| `write_uid`     | Last Updated by   | `many2one` |     | ✅    | res.users               |

**Access Rights:**

| Name                      | Group       | Perms     |
| ------------------------- | ----------- | --------- |
| access_account_tax_report | Role / User | `R/W/C/D` |

### 🗃️ `account.tax.report.line` — Account Tax Report Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                | Type        | Req | Store | Relation                   |
| -------------------------------- | -------------------- | ----------- | --- | ----- | -------------------------- |
| `carry_over_condition_method`    | Method               | `selection` |     | ✅    |                            |
| `carry_over_destination_line_id` | Destination          | `many2one`  |     | ✅    | account.tax.report.line    |
| `carryover_line_ids`             | Carryover lines      | `one2many`  |     | ✅    | account.tax.carryover.line |
| `children_line_ids`              | Children Lines       | `one2many`  |     | ✅    | account.tax.report.line    |
| `code`                           | Code                 | `char`      |     | ✅    |                            |
| `create_date`                    | Created on           | `datetime`  |     | ✅    |                            |
| `create_uid`                     | Created by           | `many2one`  |     | ✅    | res.users                  |
| `display_name`                   | Display Name         | `char`      |     |       |                            |
| `formula`                        | Formula              | `char`      |     | ✅    |                            |
| `id`                             | ID                   | `integer`   |     | ✅    |                            |
| `is_carryover_persistent`        | Persistent           | `boolean`   |     | ✅    |                            |
| `is_carryover_used_in_balance`   | Used in line balance | `boolean`   |     | ✅    |                            |
| `name`                           | Name                 | `char`      | ✅  | ✅    |                            |
| `parent_id`                      | Parent Line          | `many2one`  |     | ✅    | account.tax.report.line    |
| `parent_path`                    | Parent Path          | `char`      |     | ✅    |                            |
| `report_action_id`               | Report Action        | `many2one`  |     | ✅    | ir.actions.act_window      |
| `report_id`                      | Tax Report           | `many2one`  | ✅  | ✅    | account.tax.report         |
| `sequence`                       | Sequence             | `integer`   | ✅  | ✅    |                            |
| `tag_ids`                        | Tags                 | `many2many` |     | ✅    | account.account.tag        |
| `tag_name`                       | Tag Name             | `char`      |     | ✅    |                            |
| `write_date`                     | Last Updated on      | `datetime`  |     | ✅    |                            |
| `write_uid`                      | Last Updated by      | `many2one`  |     | ✅    | res.users                  |

**Access Rights:**

| Name                           | Group       | Perms     |
| ------------------------------ | ----------- | --------- |
| access_account_tax_report_line | Role / User | `R/W/C/D` |

### 🗃️ `account.account.type` — Account Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label                          | Type        | Req | Store | Relation  |
| ------------------------- | ------------------------------ | ----------- | --- | ----- | --------- |
| `create_date`             | Created on                     | `datetime`  |     | ✅    |           |
| `create_uid`              | Created by                     | `many2one`  |     | ✅    | res.users |
| `display_name`            | Display Name                   | `char`      |     |       |           |
| `id`                      | ID                             | `integer`   |     | ✅    |           |
| `include_initial_balance` | Bring Accounts Balance Forward | `boolean`   |     | ✅    |           |
| `name`                    | Account Type                   | `char`      | ✅  | ✅    |           |
| `type`                    | Type                           | `selection` |     | ✅    |           |
| `write_date`              | Last Updated on                | `datetime`  |     | ✅    |           |
| `write_uid`               | Last Updated by                | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                        | Group       | Perms     |
| --------------------------- | ----------- | --------- |
| access_account_account_type | Role / User | `R/W/C/D` |

### 🗃️ `report.accounting_pdf_reports.report_agedpartnerbalance` — Aged Partner Balance Report

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `account.analytic.distribution` — Analytic Account Distribution

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label            | Type       | Req | Store | Relation                 |
| -------------- | ---------------- | ---------- | --- | ----- | ------------------------ |
| `account_id`   | Analytic Account | `many2one` | ✅  | ✅    | account.analytic.account |
| `create_date`  | Created on       | `datetime` |     | ✅    |                          |
| `create_uid`   | Created by       | `many2one` |     | ✅    | res.users                |
| `display_name` | Display Name     | `char`     |     |       |                          |
| `id`           | ID               | `integer`  |     | ✅    |                          |
| `name`         | Name             | `char`     |     |       |                          |
| `percentage`   | Percentage       | `float`    | ✅  | ✅    |                          |
| `tag_id`       | Parent tag       | `many2one` | ✅  | ✅    | account.analytic.tag     |
| `write_date`   | Last Updated on  | `datetime` |     | ✅    |                          |
| `write_uid`    | Last Updated by  | `many2one` |     | ✅    | res.users                |

**Access Rights:**

| Name                                 | Group       | Perms     |
| ------------------------------------ | ----------- | --------- |
| access_account_analytic_distribution | Role / User | `R/W/C/D` |

### 🗃️ `account.analytic.tag` — Analytic Tags

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                          | Label                 | Type       | Req | Store | Relation                      |
| ------------------------------ | --------------------- | ---------- | --- | ----- | ----------------------------- |
| `active`                       | Active                | `boolean`  |     | ✅    |                               |
| `active_analytic_distribution` | Analytic Distribution | `boolean`  |     | ✅    |                               |
| `analytic_distribution_ids`    | Analytic Accounts     | `one2many` |     | ✅    | account.analytic.distribution |
| `color`                        | Color Index           | `integer`  |     | ✅    |                               |
| `company_id`                   | Company               | `many2one` |     | ✅    | res.company                   |
| `create_date`                  | Created on            | `datetime` |     | ✅    |                               |
| `create_uid`                   | Created by            | `many2one` |     | ✅    | res.users                     |
| `display_name`                 | Display Name          | `char`     |     |       |                               |
| `id`                           | ID                    | `integer`  |     | ✅    |                               |
| `name`                         | Analytic Tag          | `char`     | ✅  | ✅    |                               |
| `write_date`                   | Last Updated on       | `datetime` |     | ✅    |                               |
| `write_uid`                    | Last Updated by       | `many2one` |     | ✅    | res.users                     |

**Access Rights:**

| Name                        | Group       | Perms     |
| --------------------------- | ----------- | --------- |
| access_account_analytic_tag | Role / User | `R/W/C/D` |

### 🗃️ `account.common.journal.report` — Common Journal Report

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field             | Label           | Type        | Req | Store | Relation        |
| ----------------- | --------------- | ----------- | --- | ----- | --------------- |
| `amount_currency` | With Currency   | `boolean`   |     | ✅    |                 |
| `company_id`      | Company         | `many2one`  | ✅  | ✅    | res.company     |
| `create_date`     | Created on      | `datetime`  |     | ✅    |                 |
| `create_uid`      | Created by      | `many2one`  |     | ✅    | res.users       |
| `date_from`       | Start Date      | `date`      |     | ✅    |                 |
| `date_to`         | End Date        | `date`      |     | ✅    |                 |
| `display_name`    | Display Name    | `char`      |     |       |                 |
| `id`              | ID              | `integer`   |     | ✅    |                 |
| `journal_ids`     | Journals        | `many2many` | ✅  | ✅    | account.journal |
| `target_move`     | Target Moves    | `selection` | ✅  | ✅    |                 |
| `write_date`      | Last Updated on | `datetime`  |     | ✅    |                 |
| `write_uid`       | Last Updated by | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                                 | Group       | Perms     |
| ------------------------------------ | ----------- | --------- |
| access_account_common_journal_report | Role / User | `R/W/C/D` |

### 🗃️ `report.accounting_pdf_reports.report_financial` — Financial Reports

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `account.report.general.ledger` — General Ledger Report

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                  | Label                    | Type        | Req | Store | Relation                 |
| ---------------------- | ------------------------ | ----------- | --- | ----- | ------------------------ |
| `account_ids`          | Accounts                 | `many2many` |     | ✅    | account.account          |
| `analytic_account_ids` | Analytic Accounts        | `many2many` |     | ✅    | account.analytic.account |
| `company_id`           | Company                  | `many2one`  | ✅  | ✅    | res.company              |
| `create_date`          | Created on               | `datetime`  |     | ✅    |                          |
| `create_uid`           | Created by               | `many2one`  |     | ✅    | res.users                |
| `date_from`            | Start Date               | `date`      |     | ✅    |                          |
| `date_to`              | End Date                 | `date`      |     | ✅    |                          |
| `display_account`      | Display Accounts         | `selection` | ✅  | ✅    |                          |
| `display_name`         | Display Name             | `char`      |     |       |                          |
| `id`                   | ID                       | `integer`   |     | ✅    |                          |
| `initial_balance`      | Include Initial Balances | `boolean`   |     | ✅    |                          |
| `journal_ids`          | Journals                 | `many2many` | ✅  | ✅    | account.journal          |
| `partner_ids`          | Partners                 | `many2many` |     | ✅    | res.partner              |
| `sortby`               | Sort by                  | `selection` | ✅  | ✅    |                          |
| `target_move`          | Target Moves             | `selection` | ✅  | ✅    |                          |
| `write_date`           | Last Updated on          | `datetime`  |     | ✅    |                          |
| `write_uid`            | Last Updated by          | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                                          | Group                | Perms     |
| --------------------------------------------- | -------------------- | --------- |
| access.account.report.general.ledger.bmanager | Accounting / Advisor | `R/W/C/D` |
| access.account.report.general.ledger          | Contact / Accountant | `R/W/C/D` |

### 🗃️ `report.accounting_pdf_reports.report_general_ledger` — General Ledger Report

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `report.accounting_pdf_reports.report_journal` — Journal Audit Report

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

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

### 🗃️ `report.accounting_pdf_reports.report_partnerledger` — Partner Ledger Report

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `account.tax.carryover.line` — Tax carryover line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label           | Type       | Req | Store | Relation                |
| -------------------------------- | --------------- | ---------- | --- | ----- | ----------------------- |
| `amount`                         | Amount          | `float`    | ✅  | ✅    |                         |
| `company_id`                     | Company         | `many2one` | ✅  | ✅    | res.company             |
| `create_date`                    | Created on      | `datetime` |     | ✅    |                         |
| `create_uid`                     | Created by      | `many2one` |     | ✅    | res.users               |
| `date`                           | Date            | `date`     | ✅  | ✅    |                         |
| `display_name`                   | Display Name    | `char`     |     |       |                         |
| `foreign_vat_fiscal_position_id` | Fiscal position | `many2one` |     | ✅    | account.fiscal.position |
| `id`                             | ID              | `integer`  |     | ✅    |                         |
| `name`                           | Name            | `char`     | ✅  | ✅    |                         |
| `tax_report_country_id`          | Country         | `many2one` |     |       | res.country             |
| `tax_report_id`                  | Tax Report      | `many2one` |     |       | account.tax.report      |
| `tax_report_line_id`             | Tax report line | `many2one` |     | ✅    | account.tax.report.line |
| `write_date`                     | Last Updated on | `datetime` |     | ✅    |                         |
| `write_uid`                      | Last Updated by | `many2one` |     | ✅    | res.users               |

**Access Rights:**

| Name                              | Group       | Perms     |
| --------------------------------- | ----------- | --------- |
| access_account_tax_carryover_line | Role / User | `R/W/C/D` |

### 🗃️ `account.tax.report.wizard` — Tax Report

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation        |
| -------------- | --------------- | ----------- | --- | ----- | --------------- |
| `company_id`   | Company         | `many2one`  | ✅  | ✅    | res.company     |
| `create_date`  | Created on      | `datetime`  |     | ✅    |                 |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users       |
| `date_from`    | Date From       | `date`      | ✅  | ✅    |                 |
| `date_to`      | Date To         | `date`      | ✅  | ✅    |                 |
| `display_name` | Display Name    | `char`      |     |       |                 |
| `id`           | ID              | `integer`   |     | ✅    |                 |
| `journal_ids`  | Journals        | `many2many` | ✅  | ✅    | account.journal |
| `target_move`  | Target Moves    | `selection` | ✅  | ✅    |                 |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |                 |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                                      | Group                | Perms     |
| ----------------------------------------- | -------------------- | --------- |
| access.account.tax.report.wizard.bmanager | Accounting / Advisor | `R/W/C/D` |
| access.account.tax.report.wizard          | Contact / Accountant | `R/W/C/D` |

### 🗃️ `report.accounting_pdf_reports.report_tax` — Tax Report

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `report.accounting_pdf_reports.report_trialbalance` — Trial Balance Report

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `account.balance.report` — Trial Balance Report

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                  | Label             | Type        | Req | Store | Relation                 |
| ---------------------- | ----------------- | ----------- | --- | ----- | ------------------------ |
| `account_ids`          | Accounts          | `many2many` |     | ✅    | account.account          |
| `analytic_account_ids` | Analytic Accounts | `many2many` |     | ✅    | account.analytic.account |
| `company_id`           | Company           | `many2one`  | ✅  | ✅    | res.company              |
| `create_date`          | Created on        | `datetime`  |     | ✅    |                          |
| `create_uid`           | Created by        | `many2one`  |     | ✅    | res.users                |
| `date_from`            | Start Date        | `date`      |     | ✅    |                          |
| `date_to`              | End Date          | `date`      |     | ✅    |                          |
| `display_account`      | Display Accounts  | `selection` | ✅  | ✅    |                          |
| `display_name`         | Display Name      | `char`      |     |       |                          |
| `id`                   | ID                | `integer`   |     | ✅    |                          |
| `journal_ids`          | Journals          | `many2many` | ✅  | ✅    | account.journal          |
| `partner_ids`          | Partners          | `many2many` |     | ✅    | res.partner              |
| `target_move`          | Target Moves      | `selection` | ✅  | ✅    |                          |
| `write_date`           | Last Updated on   | `datetime`  |     | ✅    |                          |
| `write_uid`            | Last Updated by   | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                                   | Group                | Perms     |
| -------------------------------------- | -------------------- | --------- |
| access.account.balance.report.bmanager | Accounting / Advisor | `R/W/C/D` |
| access.account.balance.report          | Contact / Accountant | `R/W/C/D` |
