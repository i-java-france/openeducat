---
title: "WMS Accounting"
module: "stock_account"
state: "installed"
version: "19.0.1.1"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Inventory"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 WMS Accounting

> **Module:** `stock_account` | **Version:** `19.0.1.1` **Category:** Inventory |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

_none_

## 📖 Description

# WMS Accounting module

This module makes the link between the 'stock' and 'account' modules and allows you to
create accounting entries to value your stock movements

## Key Features

- Stock Valuation (periodical or automatic)
- Invoice from Picking

## Dashboard / Reports for Warehouse Management includes:

- Stock Inventory Value at given date (support dates in the past)

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT account.account.form (form)`
- `* INHERIT product.category.stock.property.form.inherit (form)`
- `* INHERIT product.category.stock.property.form.inherit.stock (form)`
- `* INHERIT product.product.list.inherit.stock.account.at.date (list)`
- `* INHERIT product.product.stock.list.inherit.stock.account (list)`
- `* INHERIT product.template.list.inherit.stock.account (list)`
- `* INHERIT res.config.settings.view.form.inherit.stock.account (form)`
- `* INHERIT stock.account.view.picking.form (form)`
- `* INHERIT stock.inventory.adjustment.name.form.view.inherit.stock.account (form)`
- `* INHERIT stock.location.form.inherit (form)`
- `* INHERIT stock.move.search.inherit.stock.account (search)`
- `* INHERIT stock.move.view.list.inherit.stock.account (list)`
- `* INHERIT stock.quant.inventory.list.editable.inherit.stock.account (list)`
- `* INHERIT stock.quant.list.editable.inherit (list)`
- `* INHERIT stock.quant.list.inherit (list)`
- `* INHERIT stock.return.picking.stock.account.form (form)`
- `* INHERIT stock_account_report_invoice_document (qweb)`
- `* INHERIT view.production.lot.form.stock.account (form)`
- `* INHERIT view.template.property.form.stock.account (form)`
- `product.value.form.view (form)`
- `stock.avco.report.view.list (list)`
- `stock.move.view.list.valuation (list)`

### Reports

_none_

## 🛠️ Technical Documentation

_No models defined by this module._
