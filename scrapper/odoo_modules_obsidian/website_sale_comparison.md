---
title: "Product Comparison"
module: "website_sale_comparison"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Website"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/w______]
---

# 🟢 Product Comparison

> **Module:** `website_sale_comparison` | **Version:** `19.0.1.0` **Category:** Website
> | **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[website_sale]]

## 📖 Description

This module adds a comparison tool to your eCommerce shop, so that your shoppers can
easily compare products based on their attributes. It will considerably accelerate their
purchasing decision.

To configure product attributes, activate _Attributes & Variants_ in the Website
settings. This will add a dedicated section in the product form. In the configuration,
this module adds a category field to product attributes in order to structure the
shopper's comparison table.

Finally, the module comes with an option to display an attribute summary table in
product web pages (available in Customize menu).

## 🖥️ UI Components

### Menus

- `Website/eCommerce/Products/Attribute Categories`

### Views

- `* INHERIT Add to comparison in product page (qweb)`
- `* INHERIT Comparison List Button (qweb)`
- `* INHERIT Product attributes table (qweb)`
- `* INHERIT Specifications Accordion Item (qweb)`
- `* INHERIT product.attribute.form.inherit (form)`
- `* INHERIT product.attribute.list.inherit (list)`
- `Comparator Page (qweb)`
- `Specifications Table (qweb)`
- `product.attribute.category.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**4 model(s) defined by this module:**

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

### 🗃️ `product.attribute` — Product Attribute

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label                   | Type        | Req | Store | Relation                         |
| ------------------------- | ----------------------- | ----------- | --- | ----- | -------------------------------- |
| `active`                  | Active                  | `boolean`   |     | ✅    |                                  |
| `attribute_line_ids`      | Lines                   | `one2many`  |     | ✅    | product.template.attribute.line  |
| `category_id`             | eCommerce Category      | `many2one`  |     | ✅    | product.attribute.category       |
| `create_date`             | Created on              | `datetime`  |     | ✅    |                                  |
| `create_uid`              | Created by              | `many2one`  |     | ✅    | res.users                        |
| `create_variant`          | Variant Creation        | `selection` | ✅  | ✅    |                                  |
| `display_name`            | Display Name            | `char`      |     |       |                                  |
| `display_type`            | Display Type            | `selection` | ✅  | ✅    |                                  |
| `id`                      | ID                      | `integer`   |     | ✅    |                                  |
| `is_thumbnail_visible`    | Show Thumbnails         | `boolean`   |     | ✅    |                                  |
| `name`                    | Attribute               | `char`      | ✅  | ✅    |                                  |
| `number_related_products` | Number Related Products | `integer`   |     |       |                                  |
| `preview_variants`        | On Product Cards        | `selection` |     | ✅    |                                  |
| `product_tmpl_ids`        | Related Products        | `many2many` |     | ✅    | product.template                 |
| `sequence`                | Sequence                | `integer`   |     | ✅    |                                  |
| `template_value_ids`      | Template Values         | `one2many`  |     | ✅    | product.template.attribute.value |
| `value_ids`               | Values                  | `one2many`  |     | ✅    | product.attribute.value          |
| `visibility`              | Visibility              | `selection` |     | ✅    |                                  |
| `write_date`              | Last Updated on         | `datetime`  |     | ✅    |                                  |
| `write_uid`               | Last Updated by         | `many2one`  |     | ✅    | res.users                        |

**Access Rights:**

| Name                      | Group                     | Perms     |
| ------------------------- | ------------------------- | --------- |
| product.attribute manager | Products / Create         | `R/W/C/D` |
| product.attribute manager | Inventory / Administrator | `R/W/C/D` |
| product.attribute public  | Role / Portal             | `R`       |
| product.attribute public  | Role / Public             | `R`       |
| product.attribute         | Role / User               | `R`       |
| product.attribute public  | Role / User               | `R`       |

### 🗃️ `product.attribute.category` — Product Attribute Category

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label              | Type       | Req | Store | Relation          |
| --------------- | ------------------ | ---------- | --- | ----- | ----------------- |
| `attribute_ids` | Related Attributes | `one2many` |     | ✅    | product.attribute |
| `create_date`   | Created on         | `datetime` |     | ✅    |                   |
| `create_uid`    | Created by         | `many2one` |     | ✅    | res.users         |
| `display_name`  | Display Name       | `char`     |     |       |                   |
| `id`            | ID                 | `integer`  |     | ✅    |                   |
| `name`          | Category Name      | `char`     | ✅  | ✅    |                   |
| `sequence`      | Sequence           | `integer`  |     | ✅    |                   |
| `write_date`    | Last Updated on    | `datetime` |     | ✅    |                   |
| `write_uid`     | Last Updated by    | `many2one` |     | ✅    | res.users         |

**Access Rights:**

| Name                                    | Group                 | Perms     |
| --------------------------------------- | --------------------- | --------- |
| product.attribute.category sale manager | Sales / Administrator | `R/W/C/D` |
| product.attribute.category public       | Role / Portal         | `R`       |
| product.attribute.category public       | Role / Public         | `R`       |
| product.attribute.category public       | Role / User           | `R`       |

### 🗃️ `product.template.attribute.line` — Product Template Attribute Line

Attributes available on product.template with their selected values in a m2m. Used as a
configuration model to generate the appropriate product.template.attribute.value

**Fields:**

| Field                        | Label                    | Type        | Req | Store | Relation                         |
| ---------------------------- | ------------------------ | ----------- | --- | ----- | -------------------------------- |
| `active`                     | Active                   | `boolean`   |     | ✅    |                                  |
| `attribute_id`               | Attribute                | `many2one`  | ✅  | ✅    | product.attribute                |
| `create_date`                | Created on               | `datetime`  |     | ✅    |                                  |
| `create_uid`                 | Created by               | `many2one`  |     | ✅    | res.users                        |
| `display_name`               | Display Name             | `char`      |     |       |                                  |
| `id`                         | ID                       | `integer`   |     | ✅    |                                  |
| `product_template_value_ids` | Product Attribute Values | `one2many`  |     | ✅    | product.template.attribute.value |
| `product_tmpl_id`            | Product Template         | `many2one`  | ✅  | ✅    | product.template                 |
| `sequence`                   | Sequence                 | `integer`   |     | ✅    |                                  |
| `value_count`                | Value Count              | `integer`   |     | ✅    |                                  |
| `value_ids`                  | Values                   | `many2many` |     | ✅    | product.attribute.value          |
| `write_date`                 | Last Updated on          | `datetime`  |     | ✅    |                                  |
| `write_uid`                  | Last Updated by          | `many2one`  |     | ✅    | res.users                        |

**Access Rights:**

| Name                                    | Group             | Perms     |
| --------------------------------------- | ----------------- | --------- |
| product.template.attribute line manager | Products / Create | `R/W/C/D` |
| product.template.attribute line public  | Role / Portal     | `R`       |
| product.template.attribute line public  | Role / Public     | `R`       |
| product.template.attribute line         | Role / User       | `R`       |
| product.template.attribute line public  | Role / User       | `R`       |
