---
title: "MTO Sale <-> Purchase"
module: "sale_purchase_stock"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Sales"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_____]
---

# 🟢 MTO Sale <-> Purchase

> **Module:** `sale_purchase_stock` | **Version:** `19.0.1.0` **Category:** Sales |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[sale_stock]] [[purchase_stock]] [[sale_purchase]]

## 📖 Description

Add relation information between Sale Orders and Purchase Orders if Make to Order (MTO)
is activated on one sold product.

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT purchase.order.form.sale.purchase.stock (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**5 model(s) defined by this module:**

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

### 🗃️ `stock.move` — Stock Move

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                        | Label                                                       | Type        | Req | Store | Relation                         |
| -------------------------------------------- | ----------------------------------------------------------- | ----------- | --- | ----- | -------------------------------- |
| `account_move_id`                            | stock_move_id                                               | `many2one`  |     | ✅    | account.move                     |
| `additional`                                 | Whether the move was added after the picking's confirmation | `boolean`   |     | ✅    |                                  |
| `allowed_uom_ids`                            | Allowed Uom                                                 | `many2many` |     |       | uom.uom                          |
| `analytic_account_line_ids`                  | Analytic Account Line                                       | `many2many` |     | ✅    | account.analytic.line            |
| `availability`                               | Forecasted Quantity                                         | `float`     |     |       |                                  |
| `company_currency_id`                        | Company Currency                                            | `many2one`  |     |       | res.currency                     |
| `company_id`                                 | Company                                                     | `many2one`  | ✅  | ✅    | res.company                      |
| `create_date`                                | Created on                                                  | `datetime`  |     | ✅    |                                  |
| `created_purchase_line_ids`                  | Created Purchase Order Lines                                | `many2many` |     | ✅    | purchase.order.line              |
| `create_uid`                                 | Created by                                                  | `many2one`  |     | ✅    | res.users                        |
| `date`                                       | Date Scheduled                                              | `datetime`  | ✅  | ✅    |                                  |
| `date_deadline`                              | Deadline                                                    | `datetime`  |     | ✅    |                                  |
| `delay_alert_date`                           | Delay Alert Date                                            | `datetime`  |     | ✅    |                                  |
| `description_picking`                        | Description Of Picking                                      | `text`      |     |       |                                  |
| `description_picking_manual`                 | Description Picking Manual                                  | `text`      |     | ✅    |                                  |
| `display_assign_serial`                      | Display Assign Serial                                       | `boolean`   |     |       |                                  |
| `display_import_lot`                         | Display Import Lot                                          | `boolean`   |     |       |                                  |
| `display_name`                               | Display Name                                                | `char`      |     |       |                                  |
| `forecast_availability`                      | Forecast Availability                                       | `float`     |     |       |                                  |
| `forecast_expected_date`                     | Forecasted Expected date                                    | `datetime`  |     |       |                                  |
| `has_lines_without_result_package`           | Has Lines Without Result Package                            | `boolean`   |     |       |                                  |
| `has_tracking`                               | Product with Tracking                                       | `selection` |     |       |                                  |
| `id`                                         | ID                                                          | `integer`   |     | ✅    |                                  |
| `inventory_name`                             | Inventory Name                                              | `char`      |     | ✅    |                                  |
| `is_date_editable`                           | Is Date Editable                                            | `boolean`   |     |       |                                  |
| `is_dropship`                                | Is Dropship                                                 | `boolean`   |     | ✅    |                                  |
| `is_in`                                      | Is Incoming (valued)                                        | `boolean`   |     | ✅    |                                  |
| `is_initial_demand_editable`                 | Is initial demand editable                                  | `boolean`   |     |       |                                  |
| `is_inventory`                               | Inventory                                                   | `boolean`   |     | ✅    |                                  |
| `is_locked`                                  | Is Locked                                                   | `boolean`   |     |       |                                  |
| `is_out`                                     | Is Outgoing (valued)                                        | `boolean`   |     | ✅    |                                  |
| `is_quantity_done_editable`                  | Is quantity done editable                                   | `boolean`   |     |       |                                  |
| `is_storable`                                | Track Inventory                                             | `boolean`   |     |       |                                  |
| `is_valued`                                  | Is Valued                                                   | `boolean`   |     |       |                                  |
| `location_dest_id`                           | Intermediate Location                                       | `many2one`  | ✅  | ✅    | stock.location                   |
| `location_dest_usage`                        | Destination Location Type                                   | `selection` |     |       |                                  |
| `location_final_id`                          | Final Location                                              | `many2one`  |     | ✅    | stock.location                   |
| `location_id`                                | Source Location                                             | `many2one`  | ✅  | ✅    | stock.location                   |
| `location_usage`                             | Source Location Type                                        | `selection` |     |       |                                  |
| `lot_ids`                                    | Serial Numbers                                              | `many2many` |     |       | stock.lot                        |
| `move_dest_ids`                              | Destination Moves                                           | `many2many` |     | ✅    | stock.move                       |
| `move_line_ids`                              | Move Line                                                   | `one2many`  |     | ✅    | stock.move.line                  |
| `move_lines_count`                           | Move Lines Count                                            | `integer`   |     |       |                                  |
| `move_orig_ids`                              | Original Move                                               | `many2many` |     | ✅    | stock.move                       |
| `never_product_template_attribute_value_ids` | Never attribute Values                                      | `many2many` |     | ✅    | product.template.attribute.value |
| `next_serial`                                | First SN/Lot                                                | `char`      |     | ✅    |                                  |
| `next_serial_count`                          | Number of SN/Lots                                           | `integer`   |     | ✅    |                                  |
| `orderpoint_id`                              | Original Reordering Rule                                    | `many2one`  |     | ✅    | stock.warehouse.orderpoint       |
| `origin`                                     | Source Document                                             | `char`      |     | ✅    |                                  |
| `origin_returned_move_id`                    | Origin return move                                          | `many2one`  |     | ✅    | stock.move                       |
| `package_ids`                                | Packages                                                    | `one2many`  |     |       | stock.package                    |
| `packaging_uom_id`                           | Packaging                                                   | `many2one`  |     | ✅    | uom.uom                          |
| `packaging_uom_qty`                          | Packaging Quantity                                          | `float`     |     | ✅    |                                  |
| `partner_id`                                 | Destination Address                                         | `many2one`  |     | ✅    | res.partner                      |
| `picked`                                     | Picked                                                      | `boolean`   |     | ✅    |                                  |
| `picking_code`                               | Type of Operation                                           | `selection` |     |       |                                  |
| `picking_id`                                 | Transfer                                                    | `many2one`  |     | ✅    | stock.picking                    |
| `picking_type_id`                            | Operation Type                                              | `many2one`  |     | ✅    | stock.picking.type               |
| `price_unit`                                 | Price Unit                                                  | `float`     |     | ✅    |                                  |
| `priority`                                   | Priority                                                    | `selection` |     | ✅    |                                  |
| `procurement_values`                         | Procurement Values                                          | `json`      |     |       |                                  |
| `procure_method`                             | Supply Method                                               | `selection` | ✅  | ✅    |                                  |
| `product_category_id`                        | Product Category                                            | `many2one`  |     |       | product.category                 |
| `product_id`                                 | Product                                                     | `many2one`  | ✅  | ✅    | product.product                  |
| `product_qty`                                | Real Quantity                                               | `float`     |     | ✅    |                                  |
| `product_tmpl_id`                            | Product Template                                            | `many2one`  |     |       | product.template                 |
| `product_uom`                                | Unit                                                        | `many2one`  | ✅  | ✅    | uom.uom                          |
| `product_uom_qty`                            | Demand                                                      | `float`     | ✅  | ✅    |                                  |
| `propagate_cancel`                           | Propagate cancel and split                                  | `boolean`   |     | ✅    |                                  |
| `purchase_line_id`                           | Purchase Order Line                                         | `many2one`  |     | ✅    | purchase.order.line              |
| `quantity`                                   | Quantity                                                    | `float`     |     | ✅    |                                  |
| `reference`                                  | Reference                                                   | `char`      |     | ✅    |                                  |
| `reference_ids`                              | References                                                  | `many2many` |     | ✅    | stock.reference                  |
| `remaining_qty`                              | Remaining Quantity                                          | `float`     |     |       |                                  |
| `remaining_value`                            | Remaining Value                                             | `monetary`  |     |       |                                  |
| `reservation_date`                           | Date to Reserve                                             | `date`      |     | ✅    |                                  |
| `restrict_partner_id`                        | Owner                                                       | `many2one`  |     | ✅    | res.partner                      |
| `returned_move_ids`                          | All returned moves                                          | `one2many`  |     | ✅    | stock.move                       |
| `route_ids`                                  | Destination route                                           | `many2many` |     | ✅    | stock.route                      |
| `rule_id`                                    | Stock Rule                                                  | `many2one`  |     | ✅    | stock.rule                       |
| `sale_line_id`                               | Sale Line                                                   | `many2one`  |     | ✅    | sale.order.line                  |
| `scrap_id`                                   | Scrap operation                                             | `many2one`  |     | ✅    | stock.scrap                      |
| `sequence`                                   | Sequence                                                    | `integer`   |     | ✅    |                                  |
| `show_details_visible`                       | Details Visible                                             | `boolean`   |     |       |                                  |
| `show_lots_m2o`                              | Show lot_id                                                 | `boolean`   |     |       |                                  |
| `show_lots_text`                             | Show lot_name                                               | `boolean`   |     |       |                                  |
| `show_operations`                            | Show Detailed Operations                                    | `boolean`   |     |       |                                  |
| `show_quant`                                 | Show Quant                                                  | `boolean`   |     |       |                                  |
| `standard_price`                             | Standard Price                                              | `float`     |     |       |                                  |
| `state`                                      | Status                                                      | `selection` |     | ✅    |                                  |
| `to_refund`                                  | Update quantities on SO/PO                                  | `boolean`   |     | ✅    |                                  |
| `value`                                      | Value                                                       | `monetary`  |     | ✅    |                                  |
| `value_computed_justification`               | Computed Value Description                                  | `text`      |     |       |                                  |
| `value_justification`                        | Value Description                                           | `text`      |     |       |                                  |
| `value_manual`                               | Manual Value                                                | `monetary`  |     |       |                                  |
| `warehouse_id`                               | Warehouse                                                   | `many2one`  |     | ✅    | stock.warehouse                  |
| `weight`                                     | Weight                                                      | `float`     |     | ✅    |                                  |
| `write_date`                                 | Last Updated on                                             | `datetime`  |     | ✅    |                                  |
| `write_uid`                                  | Last Updated by                                             | `many2one`  |     | ✅    | res.users                        |

**Access Rights:**

| Name                | Group                            | Perms     |
| ------------------- | -------------------------------- | --------- |
| stock_move salesman | Sales / User: Own Documents Only | `R/W/C`   |
| stock_move manager  | Sales / Administrator            | `R/W/C/D` |
| stock.move          | Accounting / Invoicing           | `R/W/C`   |
| stock.move          | Purchase / User                  | `R/W/C`   |
| stock.move          | Purchase / Administrator         | `R/W/C/D` |
| stock.move user     | Inventory / User                 | `R/W/C`   |
| stock.move manager  | Inventory / Administrator        | `R/W/C/D` |
| stock.move          | Auditor                          | `R`       |

**Record Rules:**

- **stock_move multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`

### 🗃️ `stock.rule` — Stock Rule

A rule describe what a procurement should do; produce, buy, move, ...

**Fields:**

| Field                      | Label                                 | Type        | Req | Store | Relation           |
| -------------------------- | ------------------------------------- | ----------- | --- | ----- | ------------------ |
| `action`                   | Action                                | `selection` | ✅  | ✅    |                    |
| `active`                   | Active                                | `boolean`   |     | ✅    |                    |
| `auto`                     | Automatic Move                        | `selection` | ✅  | ✅    |                    |
| `company_id`               | Company                               | `many2one`  |     | ✅    | res.company        |
| `create_date`              | Created on                            | `datetime`  |     | ✅    |                    |
| `create_uid`               | Created by                            | `many2one`  |     | ✅    | res.users          |
| `delay`                    | Lead Time                             | `integer`   |     | ✅    |                    |
| `display_name`             | Display Name                          | `char`      |     |       |                    |
| `id`                       | ID                                    | `integer`   |     | ✅    |                    |
| `location_dest_from_rule`  | Destination location origin from rule | `boolean`   |     | ✅    |                    |
| `location_dest_id`         | Destination Location                  | `many2one`  | ✅  | ✅    | stock.location     |
| `location_src_id`          | Source Location                       | `many2one`  |     | ✅    | stock.location     |
| `name`                     | Name                                  | `char`      | ✅  | ✅    |                    |
| `partner_address_id`       | Partner Address                       | `many2one`  |     | ✅    | res.partner        |
| `picking_type_code_domain` | Picking Type Code Domain              | `json`      |     |       |                    |
| `picking_type_id`          | Operation Type                        | `many2one`  | ✅  | ✅    | stock.picking.type |
| `procure_method`           | Supply Method                         | `selection` | ✅  | ✅    |                    |
| `propagate_cancel`         | Cancel Next Move                      | `boolean`   |     | ✅    |                    |
| `propagate_carrier`        | Propagation of carrier                | `boolean`   |     | ✅    |                    |
| `push_domain`              | Push Applicability                    | `char`      |     | ✅    |                    |
| `route_company_id`         | Route Company                         | `many2one`  |     |       | res.company        |
| `route_id`                 | Route                                 | `many2one`  | ✅  | ✅    | stock.route        |
| `route_sequence`           | Route Sequence                        | `integer`   |     | ✅    |                    |
| `rule_message`             | Rule Message                          | `html`      |     |       |                    |
| `sequence`                 | Sequence                              | `integer`   |     | ✅    |                    |
| `warehouse_id`             | Warehouse                             | `many2one`  |     | ✅    | stock.warehouse    |
| `write_date`               | Last Updated on                       | `datetime`  |     | ✅    |                    |
| `write_uid`                | Last Updated by                       | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                     | Group                            | Perms     |
| ------------------------ | -------------------------------- | --------- |
| stock.rule.flow          | Sales / User: Own Documents Only | `R`       |
| stock_rule salemanager   | Sales / Administrator            | `R/W/C/D` |
| stock_rule user          | Inventory / User                 | `R`       |
| stock_rule stock manager | Inventory / Administrator        | `R/W/C/D` |
| stock.rule.flow internal | Role / User                      | `R`       |

**Record Rules:**

- **product_pulled_flow multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
