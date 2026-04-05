---
title: "Sale Purchase"
module: "sale_purchase"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/"
license: "LGPL-3"
category: "Sales"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_____]
---

# 🟢 Sale Purchase

> **Module:** `sale_purchase` | **Version:** `19.0.1.0` **Category:** Sales |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** https://www.odoo.com/

## 🔗 Dependencies

[[sale]] [[purchase]]

## 📖 Description

Allows the outsourcing of services. This module allows one to sell services provided by
external providers and will automatically generate purchase orders directed to the
service seller.

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT product.template.form.inherit (form)`
- `* INHERIT purchase.order.inherited.form.sale (form)`
- `* INHERIT sale.order.inherited.form.purchase (form)`
- `Message: Alert on purchase orders when ordered quantity decreased on Sales Orders (qweb)`
- `Message: Alert on purchase orders when sales orders are cancelled (qweb)`
- `Message: Alert on sale orders when purchase orders are cancelled (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**5 model(s) defined by this module:**

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

### 🗃️ `sale.order` — Sales Order

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                              | Label                              | Type        | Req | Store | Relation                    |
| ---------------------------------- | ---------------------------------- | ----------- | --- | ----- | --------------------------- |
| `access_token`                     | Security Token                     | `char`      |     | ✅    |                             |
| `access_url`                       | Portal Access URL                  | `char`      |     |       |                             |
| `access_warning`                   | Access warning                     | `text`      |     |       |                             |
| `activity_calendar_event_id`       | Next Activity Calendar Event       | `many2one`  |     |       | calendar.event              |
| `activity_date_deadline`           | Next Activity Deadline             | `date`      |     |       |                             |
| `activity_exception_decoration`    | Activity Exception Decoration      | `selection` |     |       |                             |
| `activity_exception_icon`          | Icon                               | `char`      |     |       |                             |
| `activity_ids`                     | Activities                         | `one2many`  |     | ✅    | mail.activity               |
| `activity_state`                   | Activity State                     | `selection` |     |       |                             |
| `activity_summary`                 | Next Activity Summary              | `char`      |     |       |                             |
| `activity_type_icon`               | Activity Type Icon                 | `char`      |     |       |                             |
| `activity_type_id`                 | Next Activity Type                 | `many2one`  |     |       | mail.activity.type          |
| `activity_user_id`                 | Responsible User                   | `many2one`  |     |       | res.users                   |
| `amount_delivery`                  | Delivery Amount                    | `monetary`  |     |       |                             |
| `amount_invoiced`                  | Already invoiced                   | `monetary`  |     |       |                             |
| `amount_paid`                      | Payment Transactions Amount        | `float`     |     |       |                             |
| `amount_tax`                       | Taxes                              | `monetary`  |     | ✅    |                             |
| `amount_to_invoice`                | Un-invoiced Balance                | `monetary`  |     |       |                             |
| `amount_total`                     | Total                              | `monetary`  |     | ✅    |                             |
| `amount_undiscounted`              | Amount Before Discount             | `float`     |     |       |                             |
| `amount_untaxed`                   | Untaxed Amount                     | `monetary`  |     | ✅    |                             |
| `attendee_count`                   | Attendee Count                     | `integer`   |     |       |                             |
| `authorized_transaction_ids`       | Authorized Transactions            | `many2many` |     |       | payment.transaction         |
| `available_quotation_document_ids` | Available Quotation Documents      | `many2many` |     |       | quotation.document          |
| `campaign_id`                      | Campaign                           | `many2one`  |     | ✅    | utm.campaign                |
| `carrier_id`                       | Delivery Method                    | `many2one`  |     | ✅    | delivery.carrier            |
| `cart_quantity`                    | Cart Quantity                      | `integer`   |     |       |                             |
| `cart_recovery_email_sent`         | Cart recovery email already sent   | `boolean`   |     | ✅    |                             |
| `client_order_ref`                 | Customer Reference                 | `char`      |     | ✅    |                             |
| `commitment_date`                  | Delivery Date                      | `datetime`  |     | ✅    |                             |
| `company_id`                       | Company                            | `many2one`  | ✅  | ✅    | res.company                 |
| `company_price_include`            | Default Sales Price Include        | `selection` |     |       |                             |
| `country_code`                     | Country code                       | `char`      |     |       |                             |
| `create_date`                      | Creation Date                      | `datetime`  |     | ✅    |                             |
| `create_uid`                       | Created by                         | `many2one`  |     | ✅    | res.users                   |
| `currency_id`                      | Currency                           | `many2one`  |     | ✅    | res.currency                |
| `currency_rate`                    | Currency Rate                      | `float`     |     | ✅    |                             |
| `customizable_pdf_form_fields`     | Customizable PDF Form Fields       | `json`      |     | ✅    |                             |
| `date_order`                       | Order Date                         | `datetime`  | ✅  | ✅    |                             |
| `delivery_count`                   | Delivery Orders                    | `integer`   |     |       |                             |
| `delivery_message`                 | Delivery Message                   | `char`      |     | ✅    |                             |
| `delivery_set`                     | Delivery Set                       | `boolean`   |     |       |                             |
| `delivery_status`                  | Delivery Status                    | `selection` |     | ✅    |                             |
| `display_name`                     | Display Name                       | `char`      |     |       |                             |
| `duplicated_order_ids`             | Duplicated Order                   | `many2many` |     |       | sale.order                  |
| `effective_date`                   | Effective Date                     | `datetime`  |     | ✅    |                             |
| `expected_date`                    | Expected Date                      | `datetime`  |     |       |                             |
| `expense_count`                    | # of Expenses                      | `integer`   |     |       |                             |
| `expense_ids`                      | Expenses                           | `one2many`  |     | ✅    | hr.expense                  |
| `fiscal_position_id`               | Fiscal Position                    | `many2one`  |     | ✅    | account.fiscal.position     |
| `has_active_pricelist`             | Has Active Pricelist               | `boolean`   |     |       |                             |
| `has_archived_products`            | Has Archived Products              | `boolean`   |     |       |                             |
| `has_authorized_transaction_ids`   | Has Authorized Transactions        | `boolean`   |     |       |                             |
| `has_message`                      | Has Message                        | `boolean`   |     |       |                             |
| `id`                               | ID                                 | `integer`   |     | ✅    |                             |
| `incoterm`                         | Incoterm                           | `many2one`  |     | ✅    | account.incoterms           |
| `incoterm_location`                | Incoterm Location                  | `char`      |     | ✅    |                             |
| `invoice_count`                    | Invoice Count                      | `integer`   |     |       |                             |
| `invoice_ids`                      | Invoices                           | `many2many` |     |       | account.move                |
| `invoice_status`                   | Invoice Status                     | `selection` |     | ✅    |                             |
| `is_abandoned_cart`                | Abandoned Cart                     | `boolean`   |     |       |                             |
| `is_all_service`                   | Service Product                    | `boolean`   |     |       |                             |
| `is_expired`                       | Is Expired                         | `boolean`   |     |       |                             |
| `is_pdf_quote_builder_available`   | Is Pdf Quote Builder Available     | `boolean`   |     |       |                             |
| `journal_id`                       | Invoicing Journal                  | `many2one`  |     | ✅    | account.journal             |
| `json_popover`                     | JSON data for the popover widget   | `char`      |     |       |                             |
| `late_availability`                | Late Availability                  | `boolean`   |     |       |                             |
| `locked`                           | Locked                             | `boolean`   |     | ✅    |                             |
| `medium_id`                        | Medium                             | `many2one`  |     | ✅    | utm.medium                  |
| `message_attachment_count`         | Attachment Count                   | `integer`   |     |       |                             |
| `message_follower_ids`             | Followers                          | `one2many`  |     | ✅    | mail.followers              |
| `message_has_error`                | Message Delivery error             | `boolean`   |     |       |                             |
| `message_has_error_counter`        | Number of errors                   | `integer`   |     |       |                             |
| `message_has_sms_error`            | SMS Delivery error                 | `boolean`   |     |       |                             |
| `message_ids`                      | Messages                           | `one2many`  |     | ✅    | mail.message                |
| `message_is_follower`              | Is Follower                        | `boolean`   |     |       |                             |
| `message_needaction`               | Action Needed                      | `boolean`   |     |       |                             |
| `message_needaction_counter`       | Number of Actions                  | `integer`   |     |       |                             |
| `message_partner_ids`              | Followers (Partners)               | `many2many` |     |       | res.partner                 |
| `my_activity_date_deadline`        | My Activity Deadline               | `date`      |     |       |                             |
| `name`                             | Order Reference                    | `char`      | ✅  | ✅    |                             |
| `note`                             | Terms and conditions               | `html`      |     | ✅    |                             |
| `only_services`                    | Only Services                      | `boolean`   |     |       |                             |
| `opportunity_id`                   | Opportunity                        | `many2one`  |     | ✅    | crm.lead                    |
| `order_line`                       | Order Lines                        | `one2many`  |     | ✅    | sale.order.line             |
| `origin`                           | Source Document                    | `char`      |     | ✅    |                             |
| `partner_credit_warning`           | Partner Credit Warning             | `text`      |     |       |                             |
| `partner_id`                       | Customer                           | `many2one`  | ✅  | ✅    | res.partner                 |
| `partner_invoice_id`               | Invoice Address                    | `many2one`  | ✅  | ✅    | res.partner                 |
| `partner_shipping_id`              | Delivery Address                   | `many2one`  | ✅  | ✅    | res.partner                 |
| `payment_term_id`                  | Payment Terms                      | `many2one`  |     | ✅    | account.payment.term        |
| `pending_email_template_id`        | Pending Email Template             | `many2one`  |     | ✅    | mail.template               |
| `picking_ids`                      | Transfers                          | `one2many`  |     | ✅    | stock.picking               |
| `picking_policy`                   | Shipping Policy                    | `selection` | ✅  | ✅    |                             |
| `pickup_location_data`             | Pickup Location Data               | `json`      |     | ✅    |                             |
| `preferred_payment_method_line_id` | Payment Method                     | `many2one`  |     | ✅    | account.payment.method.line |
| `prepayment_percent`               | Prepayment percentage              | `float`     |     | ✅    |                             |
| `pricelist_id`                     | Pricelist                          | `many2one`  |     | ✅    | product.pricelist           |
| `purchase_order_count`             | Number of Purchase Order Generated | `integer`   |     |       |                             |
| `quotation_document_ids`           | Headers/Footers                    | `many2many` |     | ✅    | quotation.document          |
| `rating_ids`                       | Ratings                            | `one2many`  |     | ✅    | rating.rating               |
| `recompute_delivery_price`         | Delivery cost should be recomputed | `boolean`   |     | ✅    |                             |
| `reference`                        | Payment Ref.                       | `char`      |     | ✅    |                             |
| `require_payment`                  | Online payment                     | `boolean`   |     | ✅    |                             |
| `require_signature`                | Online signature                   | `boolean`   |     | ✅    |                             |
| `sale_order_template_id`           | Quotation Template                 | `many2one`  |     | ✅    | sale.order.template         |
| `sale_warning_text`                | Sale Warning                       | `text`      |     |       |                             |
| `shipping_weight`                  | Shipping Weight                    | `float`     |     | ✅    |                             |
| `shop_warning`                     | Warning                            | `char`      |     | ✅    |                             |
| `show_json_popover`                | Has late picking                   | `boolean`   |     |       |                             |
| `show_update_fpos`                 | Has Fiscal Position Changed        | `boolean`   |     |       |                             |
| `show_update_pricelist`            | Has Pricelist Changed              | `boolean`   |     |       |                             |
| `signature`                        | Signature                          | `binary`    |     | ✅    |                             |
| `signed_by`                        | Signed By                          | `char`      |     | ✅    |                             |
| `signed_on`                        | Signed On                          | `datetime`  |     | ✅    |                             |
| `source_id`                        | Source                             | `many2one`  |     | ✅    | utm.source                  |
| `state`                            | Status                             | `selection` |     | ✅    |                             |
| `stock_reference_ids`              | References                         | `many2many` |     | ✅    | stock.reference             |
| `tag_ids`                          | Tags                               | `many2many` |     | ✅    | crm.tag                     |
| `tax_calculation_rounding_method`  | Tax Calculation Rounding Method    | `selection` |     |       |                             |
| `tax_country_id`                   | Tax Country                        | `many2one`  |     |       | res.country                 |
| `tax_totals`                       | Tax Totals                         | `binary`    |     |       |                             |
| `team_id`                          | Sales Team                         | `many2one`  |     | ✅    | crm.team                    |
| `terms_type`                       | Terms & Conditions format          | `selection` |     |       |                             |
| `transaction_ids`                  | Transactions                       | `many2many` |     | ✅    | payment.transaction         |
| `type_name`                        | Type Name                          | `char`      |     |       |                             |
| `user_id`                          | Salesperson                        | `many2one`  |     | ✅    | res.users                   |
| `validity_date`                    | Expiration                         | `date`      |     | ✅    |                             |
| `warehouse_id`                     | Warehouse                          | `many2one`  |     | ✅    | stock.warehouse             |
| `website_id`                       | Website                            | `many2one`  |     | ✅    | website                     |
| `website_message_ids`              | Website Messages                   | `one2many`  |     | ✅    | mail.message                |
| `website_order_line`               | Order Lines displayed on Website   | `one2many`  |     |       | sale.order.line             |
| `write_date`                       | Last Updated on                    | `datetime`  |     | ✅    |                             |
| `write_uid`                        | Last Updated by                    | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                    | Group                            | Perms     |
| ----------------------- | -------------------------------- | --------- |
| sale.order              | Sales / User: Own Documents Only | `R/W/C`   |
| sale.order.manager      | Sales / Administrator            | `R/W/C/D` |
| sale.order              | Accounting / Invoicing           | `R/W`     |
| sale.order.accountant   | Contact / Accountant             | `R/W`     |
| sale.order stock worker | Inventory / User                 | `R/W`     |
| sale.order.accountant   | Auditor                          | `R`       |
| sale.order.portal       | Role / Portal                    | `R`       |

**Record Rules:**

- **Sales Order multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`
- **Portal Personal Quotations/Sales Orders** (10) `R/W/D`
  - Domain: `[('partner_id','child_of',[user.commercial_partner_id.id])]`
- **Personal Orders** (25) `R/W/C/D`
  - Domain: `['|',('user_id','=',user.id),('user_id','=',False)]`
- **All Orders** (26) `R/W/C/D`
  - Domain: `[(1,'=',1)]`

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

### 🗃️ `sale.order.line` — Sales Order Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                    | Label                              | Type        | Req | Store | Relation                         |
| ---------------------------------------- | ---------------------------------- | ----------- | --- | ----- | -------------------------------- |
| `allowed_uom_ids`                        | Allowed Uom                        | `many2many` |     |       | uom.uom                          |
| `amount_invoiced`                        | Invoiced Amount                    | `monetary`  |     |       |                                  |
| `amount_to_invoice`                      | Un-invoiced Balance                | `monetary`  |     |       |                                  |
| `amount_to_invoice_at_date`              | Amount                             | `float`     |     |       |                                  |
| `analytic_distribution`                  | Analytic Distribution              | `json`      |     | ✅    |                                  |
| `analytic_line_ids`                      | Analytic lines                     | `one2many`  |     | ✅    | account.analytic.line            |
| `analytic_precision`                     | Analytic Precision                 | `integer`   |     |       |                                  |
| `available_product_document_ids`         | Available Product Documents        | `many2many` |     |       | product.document                 |
| `categ_id`                               | Product Category                   | `many2one`  |     |       | product.category                 |
| `collapse_composition`                   | Collapse Composition               | `boolean`   |     | ✅    |                                  |
| `collapse_prices`                        | Collapse Prices                    | `boolean`   |     | ✅    |                                  |
| `combo_item_id`                          | Combo Item                         | `many2one`  |     | ✅    | product.combo.item               |
| `company_id`                             | Company                            | `many2one`  |     | ✅    | res.company                      |
| `company_price_include`                  | Default Sales Price Include        | `selection` |     |       |                                  |
| `create_date`                            | Created on                         | `datetime`  |     | ✅    |                                  |
| `create_uid`                             | Created by                         | `many2one`  |     | ✅    | res.users                        |
| `currency_id`                            | Currency                           | `many2one`  |     | ✅    | res.currency                     |
| `customer_lead`                          | Lead Time                          | `float`     | ✅  | ✅    |                                  |
| `discount`                               | Discount (%)                       | `float`     |     | ✅    |                                  |
| `display_name`                           | Display Name                       | `char`      |     |       |                                  |
| `display_qty_widget`                     | Display Qty Widget                 | `boolean`   |     |       |                                  |
| `display_type`                           | Display Type                       | `selection` |     | ✅    |                                  |
| `distribution_analytic_account_ids`      | Distribution Analytic Account      | `many2many` |     |       | account.analytic.account         |
| `event_id`                               | Event                              | `many2one`  |     | ✅    | event.event                      |
| `event_slot_id`                          | Slot                               | `many2one`  |     | ✅    | event.slot                       |
| `event_ticket_id`                        | Ticket Type                        | `many2one`  |     | ✅    | event.event.ticket               |
| `expense_ids`                            | Expenses                           | `one2many`  |     | ✅    | hr.expense                       |
| `extra_tax_data`                         | Extra Tax Data                     | `json`      |     | ✅    |                                  |
| `forecast_expected_date`                 | Forecast Expected Date             | `datetime`  |     |       |                                  |
| `free_qty_today`                         | Free Qty Today                     | `float`     |     |       |                                  |
| `id`                                     | ID                                 | `integer`   |     | ✅    |                                  |
| `invoice_lines`                          | Invoice Lines                      | `many2many` |     | ✅    | account.move.line                |
| `invoice_status`                         | Invoice Status                     | `selection` |     | ✅    |                                  |
| `is_configurable_product`                | Is the product configurable?       | `boolean`   |     |       |                                  |
| `is_delivery`                            | Is a Delivery                      | `boolean`   |     | ✅    |                                  |
| `is_downpayment`                         | Is a down payment                  | `boolean`   |     | ✅    |                                  |
| `is_expense`                             | Is expense                         | `boolean`   |     | ✅    |                                  |
| `is_mto`                                 | Is Mto                             | `boolean`   |     |       |                                  |
| `is_multi_slots`                         | Is Multi Slots                     | `boolean`   |     |       |                                  |
| `is_optional`                            | Optional Line                      | `boolean`   |     | ✅    |                                  |
| `is_product_archived`                    | Is Product Archived                | `boolean`   |     |       |                                  |
| `is_storable`                            | Track Inventory                    | `boolean`   |     |       |                                  |
| `linked_line_id`                         | Linked Order Line                  | `many2one`  |     | ✅    | sale.order.line                  |
| `linked_line_ids`                        | Linked Order Lines                 | `one2many`  |     | ✅    | sale.order.line                  |
| `linked_virtual_id`                      | Linked Virtual                     | `char`      |     | ✅    |                                  |
| `move_ids`                               | Stock Moves                        | `one2many`  |     | ✅    | stock.move                       |
| `name`                                   | Description                        | `text`      | ✅  | ✅    |                                  |
| `name_short`                             | Name Short                         | `char`      |     |       |                                  |
| `order_id`                               | Order Reference                    | `many2one`  | ✅  | ✅    | sale.order                       |
| `order_partner_id`                       | Customer                           | `many2one`  |     | ✅    | res.partner                      |
| `parent_id`                              | Parent Section Line                | `many2one`  |     |       | sale.order.line                  |
| `pricelist_item_id`                      | Pricelist Item                     | `many2one`  |     |       | product.pricelist.item           |
| `price_reduce_taxexcl`                   | Price Reduce Tax excl              | `monetary`  |     | ✅    |                                  |
| `price_reduce_taxinc`                    | Price Reduce Tax incl              | `monetary`  |     | ✅    |                                  |
| `price_subtotal`                         | Subtotal                           | `monetary`  |     | ✅    |                                  |
| `price_tax`                              | Total Tax                          | `float`     |     | ✅    |                                  |
| `price_total`                            | Total                              | `monetary`  |     | ✅    |                                  |
| `price_unit`                             | Unit Price                         | `float`     | ✅  | ✅    |                                  |
| `product_custom_attribute_value_ids`     | Custom Values                      | `one2many`  |     | ✅    | product.attribute.custom.value   |
| `product_document_ids`                   | Product Documents                  | `many2many` |     | ✅    | product.document                 |
| `product_id`                             | Product                            | `many2one`  |     | ✅    | product.product                  |
| `product_no_variant_attribute_value_ids` | Extra Values                       | `many2many` |     | ✅    | product.template.attribute.value |
| `product_qty`                            | Product Qty                        | `float`     |     |       |                                  |
| `product_template_attribute_value_ids`   | Attribute Values                   | `many2many` |     |       | product.template.attribute.value |
| `product_template_id`                    | Product Template                   | `many2one`  |     |       | product.template                 |
| `product_type`                           | Product Type                       | `selection` |     |       |                                  |
| `product_uom_id`                         | Unit                               | `many2one`  |     | ✅    | uom.uom                          |
| `product_uom_qty`                        | Quantity                           | `float`     | ✅  | ✅    |                                  |
| `product_uom_readonly`                   | Product Uom Readonly               | `boolean`   |     |       |                                  |
| `product_updatable`                      | Can Edit Product                   | `boolean`   |     |       |                                  |
| `purchase_line_count`                    | Number of generated purchase items | `integer`   |     |       |                                  |
| `purchase_line_ids`                      | Generated Purchase Lines           | `one2many`  |     | ✅    | purchase.order.line              |
| `qty_available_today`                    | Qty Available Today                | `float`     |     |       |                                  |
| `qty_delivered`                          | Delivery Quantity                  | `float`     |     | ✅    |                                  |
| `qty_delivered_at_date`                  | Delivered                          | `float`     |     |       |                                  |
| `qty_delivered_method`                   | Method to update delivered qty     | `selection` |     | ✅    |                                  |
| `qty_invoiced`                           | Invoiced Quantity                  | `float`     |     | ✅    |                                  |
| `qty_invoiced_at_date`                   | Invoiced                           | `float`     |     |       |                                  |
| `qty_invoiced_posted`                    | Invoiced Quantity (posted)         | `float`     |     |       |                                  |
| `qty_to_deliver`                         | Qty To Deliver                     | `float`     |     |       |                                  |
| `qty_to_invoice`                         | Quantity To Invoice                | `float`     |     | ✅    |                                  |
| `recompute_delivery_price`               | Delivery cost should be recomputed | `boolean`   |     |       |                                  |
| `registration_ids`                       | Registrations                      | `one2many`  |     | ✅    | event.registration               |
| `route_ids`                              | Routes                             | `many2many` |     | ✅    | stock.route                      |
| `sale_line_warn_msg`                     | Sale Line Warn Msg                 | `text`      |     |       |                                  |
| `salesman_id`                            | Salesperson                        | `many2one`  |     | ✅    | res.users                        |
| `scheduled_date`                         | Scheduled Date                     | `datetime`  |     |       |                                  |
| `selected_combo_items`                   | Selected Combo Items               | `char`      |     |       |                                  |
| `sequence`                               | Sequence                           | `integer`   |     | ✅    |                                  |
| `service_tracking`                       | Create on Order                    | `selection` |     |       |                                  |
| `shop_warning`                           | Warning                            | `char`      |     | ✅    |                                  |
| `state`                                  | Order Status                       | `selection` |     | ✅    |                                  |
| `tax_calculation_rounding_method`        | Tax calculation rounding method    | `selection` |     |       |                                  |
| `tax_country_id`                         | Tax Country                        | `many2one`  |     |       | res.country                      |
| `tax_ids`                                | Taxes                              | `many2many` |     | ✅    | account.tax                      |
| `technical_price_unit`                   | Technical Price Unit               | `float`     |     | ✅    |                                  |
| `translated_product_name`                | Translated Product Name            | `text`      |     |       |                                  |
| `untaxed_amount_invoiced`                | Untaxed Invoiced Amount            | `monetary`  |     | ✅    |                                  |
| `untaxed_amount_to_invoice`              | Untaxed Amount To Invoice          | `monetary`  |     | ✅    |                                  |
| `virtual_available_at_date`              | Virtual Available At Date          | `float`     |     |       |                                  |
| `virtual_id`                             | Virtual                            | `char`      |     | ✅    |                                  |
| `warehouse_id`                           | Warehouse                          | `many2one`  |     | ✅    | stock.warehouse                  |
| `write_date`                             | Last Updated on                    | `datetime`  |     | ✅    |                                  |
| `write_uid`                              | Last Updated by                    | `many2one`  |     | ✅    | res.users                        |

**Access Rights:**

| Name                         | Group                            | Perms     |
| ---------------------------- | -------------------------------- | --------- |
| sale.order.line              | Sales / User: Own Documents Only | `R/W/C/D` |
| sale.order.line              | Accounting / Invoicing           | `R/W`     |
| sale.order.line accountant   | Contact / Accountant             | `R/W`     |
| sale.order.line stock worker | Inventory / User                 | `R/W`     |
| sale.order.line accountant   | Auditor                          | `R`       |
| sale.order.line.portal       | Role / Portal                    | `R`       |

**Record Rules:**

- **Sales Order Line multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`
- **Portal Sales Orders Line** (10) `R/W/C/D`
  - Domain: `[('order_id.partner_id','child_of',[user.commercial_partner_id.id])]`
- **Personal Order Lines** (25) `R/W/C/D`
  - Domain: `['|',('salesman_id','=',user.id),('salesman_id','=',False)]`
- **All Orders Lines** (26) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Stock User Sales Orders Line** (58) `R`
  - Domain: `[(1, '=', 1)]`
