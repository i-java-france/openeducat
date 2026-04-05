---
title: "Inventory"
module: "stock"
state: "installed"
version: "19.0.1.1"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/app/inventory"
license: "LGPL-3"
category: "Inventory"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________, odoo/app]
---

# 🟢 Inventory

> **Module:** `stock` | **Version:** `19.0.1.1` **Category:** Inventory | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** https://www.odoo.com/app/inventory

## 🔗 Dependencies

_none_

## 📖 Description

## 🖥️ UI Components

### Menus

- `Inventory`
- `Inventory/Configuration`
- `Inventory/Configuration/Delivery`
- `Inventory/Configuration/Delivery/Package Types`
- `Inventory/Configuration/Products`
- `Inventory/Configuration/Products/Attributes`
- `Inventory/Configuration/Products/Barcode Nomenclatures`
- `Inventory/Configuration/Products/Categories`
- `Inventory/Configuration/Products/Units & Packagings`
- `Inventory/Configuration/Settings`
- `Inventory/Configuration/Warehouse Management`
- `Inventory/Configuration/Warehouse Management/Locations`
- `Inventory/Configuration/Warehouse Management/Operations Types`
- `Inventory/Configuration/Warehouse Management/Putaway Rules`
- `Inventory/Configuration/Warehouse Management/Routes`
- `Inventory/Configuration/Warehouse Management/Rules`
- `Inventory/Configuration/Warehouse Management/Storage Categories`
- `Inventory/Configuration/Warehouse Management/Warehouses`
- `Inventory/Operations`
- `Inventory/Operations/Adjustments`
- `Inventory/Operations/Adjustments/Physical Inventory`
- `Inventory/Operations/Adjustments/Scrap`
- `Inventory/Operations/Procurement`
- `Inventory/Operations/Procurement/References`
- `Inventory/Operations/Procurement/Replenishment`
- `Inventory/Operations/Procurement: run scheduler`
- `Inventory/Operations/Transfers`
- `Inventory/Operations/Transfers/Deliveries`
- `Inventory/Operations/Transfers/Internal`
- `Inventory/Operations/Transfers/Receipts`
- `Inventory/Overview`
- `Inventory/Products`
- `Inventory/Products/Lots / Serial Numbers`
- `Inventory/Products/Packages`
- `Inventory/Products/Product Variants`
- `Inventory/Products/Products`
- `Inventory/Reporting`
- `Inventory/Reporting/Locations`
- `Inventory/Reporting/Moves Analysis`
- `Inventory/Reporting/Moves History`
- `Inventory/Reporting/Stock`

### Views

- `* INHERIT Product Template Kanban Stock (kanban)`
- `* INHERIT product.category.form (form)`
- `* INHERIT product.label.layout.form (form)`
- `* INHERIT product.label.layout.form.stock (form)`
- `* INHERIT product.product.procurement (form)`
- `* INHERIT product.product.search.stock.form (search)`
- `* INHERIT product.product.search.stock.form.stock.report (search)`
- `* INHERIT product.search.stock.form (search)`
- `* INHERIT product.stock.list.inherit (list)`
- `* INHERIT product.template.search.inherit.stock (search)`
- `* INHERIT product.template.search.stock.form (search)`
- `* INHERIT product.template.stock.list.inherit (list)`
- `* INHERIT product.template.stock.property.form.inherit (form)`
- `* INHERIT product.template_procurement (form)`
- `* INHERIT product.view.kanban.catalog.inherit.stock (kanban)`
- `* INHERIT res.config.settings.view.form.inherit.stock (form)`
- `* INHERIT res.partner.stock.property.form.inherit (form)`
- `* INHERIT res.partner.stock.warning (form)`
- `* INHERIT stock.location.form.editable (form)`
- `* INHERIT stock.location.list2.editable (list)`
- `* INHERIT stock.move.line.mobile.form (form)`
- `* INHERIT stock.quant.list (list)`
- `* INHERIT stock.rule.form (form)`
- `* INHERIT stock.warehouse.orderpoint.list.editable.inherit.show_trigger (list)`
- `* INHERIT stock.warn.insufficient.qty.scrap (form)`
- `* INHERIT uom.uom.form.inherit (form)`
- `* INHERIT uom.uom.list.inherit (list)`
- `Help Message (qweb)`
- `Inventory Report at Date (form)`
- `Operation Types (form)`
- `Operation types (list)`
- `Production Lots Filter (search)`
- `Replenish (form)`
- `Return lines (form)`
- `Stock Orderpoint Snooze (form)`
- `Stock Relocation (form)`
- `Stock Replenishment Information (form)`
- `Stock Rules Report (form)`
- `alternative_zpl_label (qweb)`
- `exception_on_picking (qweb)`
- `inventory.reset.warning.view (form)`
- `inventory.set.warning.view (form)`
- `jewelry_zpl_label (qweb)`
- `label_lot_template_view (qweb)`
- `label_package_history_template_view (qweb)`
- `label_package_template_view (qweb)`
- `label_packaging_barcode_view (qweb)`
- `label_picking_type_view (qweb)`
- `label_product_product_view (qweb)`
- `label_transfer_template_view_pdf (qweb)`
- `label_transfer_template_view_zpl (qweb)`
- `lot.label.layout.form (form)`
- `message_body (qweb)`
- `message_head (qweb)`
- `normal_zpl_label (qweb)`
- `picking.label.type.form (form)`
- `product.product.stock.list (list)`
- `product.removal.form (form)`
- `report_delivery_document (qweb)`
- `report_deliveryslip (qweb)`
- `report_generic_barcode (qweb)`
- `report_inventory (qweb)`
- `report_location_barcode (qweb)`
- `report_lot_label (qweb)`
- `report_package_barcode (qweb)`
- `report_package_barcode_content (qweb)`
- `report_package_barcode_small (qweb)`
- `report_package_history_barcode (qweb)`
- `report_package_history_barcode_small (qweb)`
- `report_picking (qweb)`
- `report_picking_packages (qweb)`
- `report_picking_type_label (qweb)`
- `report_reception (qweb)`
- `report_reception_body (qweb)`
- `report_reception_report_label (qweb)`
- `report_return_document (qweb)`
- `report_stock_body_print (qweb)`
- `report_stock_inventory_print (qweb)`
- `report_stock_rule (qweb)`
- `report_stock_rule_left_arrow (qweb)`
- `report_stock_rule_line (qweb)`
- `report_stock_rule_right_arrow (qweb)`
- `report_stock_rule_suspension_points (qweb)`
- `report_stock_rule_vertical_bar (qweb)`
- `small_zpl_label (qweb)`
- `stock.inventory.adjustment.name.form.view (form)`
- `stock.inventory.conflict.form.view (form)`
- `stock.location.form (form)`
- `stock.location.list (list)`
- `stock.location.route.form (form)`
- `stock.location.route.list (list)`
- `stock.location.route.search (search)`
- `stock.location.search (search)`
- `stock.move.form (form)`
- `stock.move.graph (graph)`
- `stock.move.kanban (kanban)`
- `stock.move.line.form (form)`
- `stock.move.line.kanban (kanban)`
- `stock.move.line.list (list)`
- `stock.move.line.list.detailed (list)`
- `stock.move.line.operations.list (list)`
- `stock.move.line.operations.list (list)`
- `stock.move.line.pivot (pivot)`
- `stock.move.line.search (search)`
- `stock.move.list (list)`
- `stock.move.operations.form (form)`
- `stock.move.pivot (pivot)`
- `stock.move.search (search)`
- `stock.move.tree2 (list)`
- `stock.package.add.package.list (list)`
- `stock.package.destination.view (form)`
- `stock.package.form (form)`
- `stock.package.history.list (list)`
- `stock.package.history.search (search)`
- `stock.package.kanban (kanban)`
- `stock.package.list (list)`
- `stock.package.list.editable (list)`
- `stock.package.search (search)`
- `stock.package.type.form (form)`
- `stock.package.type.list (list)`
- `stock.picking.calendar (calendar)`
- `stock.picking.form (form)`
- `stock.picking.internal.search (search)`
- `stock.picking.kanban (kanban)`
- `stock.picking.list (list)`
- `stock.picking.move.list (list)`
- `stock.picking.type.filter (search)`
- `stock.picking.type.kanban (kanban)`
- `stock.picking.view.activity (activity)`
- `stock.production.lot.form (form)`
- `stock.production.lot.kanban (kanban)`
- `stock.production.lot.list (list)`
- `stock.put.in.pack.form (form)`
- `stock.putaway.rule.list (list)`
- `stock.putaway.rule.search (search)`
- `stock.quant.form.editable (form)`
- `stock.quant.graph (graph)`
- `stock.quant.inventory.list.editable (list)`
- `stock.quant.list (list)`
- `stock.quant.list.editable (list)`
- `stock.quant.pivot (pivot)`
- `stock.quant.search (search)`
- `stock.reference.form (form)`
- `stock.reference.list (list)`
- `stock.reference.search (search)`
- `stock.replenishment.option.list.view (list)`
- `stock.replenishment.warning.view (form)`
- `stock.report_return_slip (qweb)`
- `stock.request.count.form.view (form)`
- `stock.rule.form (form)`
- `stock.rule.list (list)`
- `stock.rule.select (search)`
- `stock.scrap.form (form)`
- `stock.scrap.form2 (form)`
- `stock.scrap.kanban (kanban)`
- `stock.scrap.list (list)`
- `stock.scrap.search (search)`
- `stock.storage.category.capacity.list (list)`
- `stock.storage.category.form (form)`
- `stock.storage.category.list (list)`
- `stock.warehouse (form)`
- `stock.warehouse.list (list)`
- `stock.warehouse.orderpoint.form (form)`
- `stock.warehouse.orderpoint.kanban (kanban)`
- `stock.warehouse.orderpoint.list.editable (list)`
- `stock.warehouse.orderpoint.reorder.search (search)`
- `stock.warehouse.orderpoint.search (search)`
- `stock.warehouse.search (search)`
- `stock.warn.insufficient.qty (form)`
- `stock_backorder_confirmation (form)`
- `stock_report_delivery_aggregated_move_lines (qweb)`
- `stock_report_delivery_has_serial_move_line (qweb)`
- `stock_report_delivery_no_package_section_line (qweb)`
- `stock_report_delivery_package_section_line (qweb)`
- `stock_report_view_graph (graph)`
- `track_move_template (qweb)`
- `view.stock.quant.form (form)`

### Reports

- `Count Sheet`
- `Delivery Slip`
- `Location Barcode`
- `Lot/Serial Number (PDF)`
- `Lot/Serial Number (ZPL)`
- `Operation type (PDF)`
- `Operation type (ZPL)`
- `Package Barcode (PDF)`
- `Package Barcode (PDF)`
- `Package Barcode (ZPL)`
- `Package Barcode (ZPL)`
- `Package Barcode with Contents`
- `Package Barcode with Contents`
- `Packages`
- `Packaging Barcodes (ZPL)`
- `Picking Operations`
- `Product Label (ZPL)`
- `Product Routes Report`
- `Reception Report`
- `Reception Report Label`
- `Return slip`

## 🛠️ Technical Documentation

_No models defined by this module._
