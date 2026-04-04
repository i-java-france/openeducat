---
title: "Delivery - Stock"
module: "stock_delivery"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Shipping Connectors"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/___________________]
---

# 🟢 Delivery - Stock

> **Module:** `stock_delivery` | **Version:** `19.0.1.0` **Category:** Shipping
> Connectors | **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

_none_

## 📖 Description

# Allows you to add delivery methods in pickings.

When creating invoices from picking, the system is able to add and compute the shipping
line.

## 🖥️ UI Components

### Menus

- `Inventory/Configuration/Delivery/Delivery Methods`
- `Inventory/Configuration/Delivery/Zip Prefix`

### Views

- `* INHERIT Shipping tracking on orders followup (qweb)`
- `* INHERIT alternative_zpl_label (qweb)`
- `* INHERIT choose.delivery.carrier.form (form)`
- `* INHERIT delivery.carrier.form (form)`
- `* INHERIT delivery.stock.picking_withcarrier.form.view (form)`
- `* INHERIT delivery_stock_report_delivery_no_package_section_line (qweb)`
- `* INHERIT label_package_template_view_delivery (qweb)`
- `* INHERIT normal_zpl_label (qweb)`
- `* INHERIT product.template.form.hs_code (form)`
- `* INHERIT report_delivery_document2 (qweb)`
- `* INHERIT report_package_barcode_delivery (qweb)`
- `* INHERIT report_package_barcode_small_delivery (qweb)`
- `* INHERIT report_shipping2 (qweb)`
- `* INHERIT stock.move.line.list.detailed (list)`
- `* INHERIT stock.move.line.search.delivery (search)`
- `* INHERIT stock.package.type.form.delivery (form)`
- `* INHERIT stock.package.type.list.delivery (list)`
- `* INHERIT stock.package.weight.form (form)`
- `* INHERIT stock.picking.delivery.list.inherit.delivery (list)`
- `* INHERIT stock.picking.type.list.delivery (form)`
- `* INHERIT stock.picking_withweight.internal.move.form.view (form)`
- `* INHERIT stock.put.in.pack.form (form)`
- `* INHERIT stock.route.form (form)`
- `* INHERIT stock.rule.list.delivery (form)`
- `* INHERIT stock_report_delivery_aggregated_move_lines_inherit_delivery (qweb)`
- `* INHERIT stock_report_delivery_has_serial_move_line_inherit_delivery (qweb)`
- `* INHERIT stock_report_delivery_package_section_line_inherit_delivery (qweb)`
- `delivery.carrier.warning.url.form (form)`

### Reports

_none_

## 🛠️ Technical Documentation

_No models defined by this module._
