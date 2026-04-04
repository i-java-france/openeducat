---
title: "Sales PDF Quotation Builder"
module: "sale_pdf_quote_builder"
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

# 🟢 Sales PDF Quotation Builder

> **Module:** `sale_pdf_quote_builder` | **Version:** `19.0.1.0` **Category:** Sales |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[sale_management]]

## 📖 Description

Build nice quotations

## 🖥️ UI Components

### Menus

- `Sales/Configuration/Sales Orders/Headers/Footers`

### Views

- `* INHERIT product.document.form.sale (form)`
- `* INHERIT res.config.settings.view.form.inherit.sale.pdf.quote.builder (form)`
- `* INHERIT sale.order.form.pdf.quote.builder (form)`
- `* INHERIT sale.order.template.form (form)`
- `quotation.document.form (form)`
- `quotation.document.kanban (kanban)`
- `quotation.document.list (list)`
- `quotation.document.search (search)`
- `sale.pdf.form.field.list (list)`
- `sale.pdf.form.field.search (search)`

### Reports

- `Quotation / Order`

## 🛠️ Technical Documentation

**7 model(s) defined by this module:**

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

### 🗃️ `sale.pdf.form.field` — Form fields of inside quotation documents.

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                    | Label               | Type        | Req | Store | Relation           |
| ------------------------ | ------------------- | ----------- | --- | ----- | ------------------ |
| `create_date`            | Created on          | `datetime`  |     | ✅    |                    |
| `create_uid`             | Created by          | `many2one`  |     | ✅    | res.users          |
| `display_name`           | Display Name        | `char`      |     |       |                    |
| `document_type`          | Document Type       | `selection` | ✅  | ✅    |                    |
| `id`                     | ID                  | `integer`   |     | ✅    |                    |
| `name`                   | Form Field Name     | `char`      | ✅  | ✅    |                    |
| `path`                   | Path                | `char`      |     | ✅    |                    |
| `product_document_ids`   | Product Documents   | `many2many` |     | ✅    | product.document   |
| `quotation_document_ids` | Quotation Documents | `many2many` |     | ✅    | quotation.document |
| `write_date`             | Last Updated on     | `datetime`  |     | ✅    |                    |
| `write_uid`              | Last Updated by     | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                            | Group                | Perms     |
| ------------------------------- | -------------------- | --------- |
| access_sale_pdf_form_field_user | Role / Administrator | `R/W/C/D` |
| access_sale_pdf_form_field_user | Role / User          | `R`       |

### 🗃️ `product.document` — Product Document

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                   | Label                                        | Type                 | Req | Store | Relation               |
| ----------------------- | -------------------------------------------- | -------------------- | --- | ----- | ---------------------- |
| `access_token`          | Access Token                                 | `char`               |     |       |                        |
| `active`                | Active                                       | `boolean`            |     | ✅    |                        |
| `attached_on_sale`      | Sale : Visible at                            | `selection`          | ✅  | ✅    |                        |
| `checksum`              | Checksum/SHA1                                | `char`               |     |       |                        |
| `company_id`            | Company                                      | `many2one`           |     |       | res.company            |
| `create_date`           | Created on                                   | `datetime`           |     | ✅    |                        |
| `create_uid`            | Created by                                   | `many2one`           |     | ✅    | res.users              |
| `datas`                 | File Content (base64)                        | `binary`             |     |       |                        |
| `db_datas`              | Database Data                                | `binary`             |     |       |                        |
| `description`           | Description                                  | `text`               |     |       |                        |
| `display_name`          | Display Name                                 | `char`               |     |       |                        |
| `file_size`             | File Size                                    | `integer`            |     |       |                        |
| `form_field_ids`        | Form Fields Included                         | `many2many`          |     | ✅    | sale.pdf.form.field    |
| `has_thumbnail`         | Has Thumbnail                                | `boolean`            |     |       |                        |
| `id`                    | ID                                           | `integer`            |     | ✅    |                        |
| `image_height`          | Image Height                                 | `integer`            |     |       |                        |
| `image_src`             | Image Src                                    | `char`               |     |       |                        |
| `image_width`           | Image Width                                  | `integer`            |     |       |                        |
| `index_content`         | Indexed Content                              | `text`               |     |       |                        |
| `ir_attachment_id`      | Related attachment                           | `many2one`           | ✅  | ✅    | ir.attachment          |
| `key`                   | Key                                          | `char`               |     |       |                        |
| `local_url`             | Attachment URL                               | `char`               |     |       |                        |
| `media_link`            | Media Link                                   | `char`               |     |       |                        |
| `mimetype`              | Mime Type                                    | `char`               |     |       |                        |
| `name`                  | Name                                         | `char`               | ✅  |       |                        |
| `original_id`           | Original (unoptimized, unresized) attachment | `many2one`           |     |       | ir.attachment          |
| `public`                | Is public document                           | `boolean`            |     |       |                        |
| `raw`                   | File Content (raw)                           | `binary`             |     |       |                        |
| `res_field`             | Resource Field                               | `char`               |     |       |                        |
| `res_id`                | Resource ID                                  | `many2one_reference` |     |       |                        |
| `res_model`             | Resource Model                               | `char`               |     |       |                        |
| `res_name`              | Resource Name                                | `char`               |     |       |                        |
| `sequence`              | Sequence                                     | `integer`            |     | ✅    |                        |
| `shown_on_product_page` | Publish on website                           | `boolean`            |     | ✅    |                        |
| `store_fname`           | Stored Filename                              | `char`               |     |       |                        |
| `theme_template_id`     | Theme Template                               | `many2one`           |     |       | theme.ir.attachment    |
| `thumbnail`             | Thumbnail                                    | `binary`             |     |       |                        |
| `type`                  | Type                                         | `selection`          | ✅  |       |                        |
| `url`                   | Url                                          | `char`               |     |       |                        |
| `voice_ids`             | Voice                                        | `one2many`           |     |       | discuss.voice.metadata |
| `website_id`            | Website                                      | `many2one`           |     |       | website                |
| `whatsapp_media_id`     | whatsapp Media Id                            | `char`               |     |       |                        |
| `write_date`            | Last Updated on                              | `datetime`           |     | ✅    |                        |
| `write_uid`             | Last Updated by                              | `many2one`           |     | ✅    | res.users              |

**Access Rights:**

| Name                                 | Group                 | Perms     |
| ------------------------------------ | --------------------- | --------- |
| access_product_document_sale_manager | Sales / Administrator | `R/W/C/D` |
| access_product_document_manager      | Products / Create     | `R/W/C/D` |
| access_product_document_user         | Role / User           | `R`       |

**Record Rules:**

- **Product multi-company** (Global) `R/W/C/D`
  - Domain:
    ` ['|', ('company_id', 'parent_of', company_ids), ('company_id', '=', False)]`

### 🗃️ `quotation.document` — Quotation's Headers & Footers

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                    | Label                                        | Type                 | Req | Store | Relation               |
| ------------------------ | -------------------------------------------- | -------------------- | --- | ----- | ---------------------- |
| `access_token`           | Access Token                                 | `char`               |     |       |                        |
| `active`                 | Active                                       | `boolean`            |     | ✅    |                        |
| `add_by_default`         | Add By Default                               | `boolean`            |     | ✅    |                        |
| `checksum`               | Checksum/SHA1                                | `char`               |     |       |                        |
| `company_id`             | Company                                      | `many2one`           |     |       | res.company            |
| `create_date`            | Created on                                   | `datetime`           |     | ✅    |                        |
| `create_uid`             | Created by                                   | `many2one`           |     | ✅    | res.users              |
| `datas`                  | File Content (base64)                        | `binary`             |     |       |                        |
| `db_datas`               | Database Data                                | `binary`             |     |       |                        |
| `description`            | Description                                  | `text`               |     |       |                        |
| `display_name`           | Display Name                                 | `char`               |     |       |                        |
| `document_type`          | Document Type                                | `selection`          | ✅  | ✅    |                        |
| `file_size`              | File Size                                    | `integer`            |     |       |                        |
| `form_field_ids`         | Form Fields Included                         | `many2many`          |     | ✅    | sale.pdf.form.field    |
| `has_thumbnail`          | Has Thumbnail                                | `boolean`            |     |       |                        |
| `id`                     | ID                                           | `integer`            |     | ✅    |                        |
| `image_height`           | Image Height                                 | `integer`            |     |       |                        |
| `image_src`              | Image Src                                    | `char`               |     |       |                        |
| `image_width`            | Image Width                                  | `integer`            |     |       |                        |
| `index_content`          | Indexed Content                              | `text`               |     |       |                        |
| `ir_attachment_id`       | Related attachment                           | `many2one`           | ✅  | ✅    | ir.attachment          |
| `key`                    | Key                                          | `char`               |     |       |                        |
| `local_url`              | Attachment URL                               | `char`               |     |       |                        |
| `media_link`             | Media Link                                   | `char`               |     |       |                        |
| `mimetype`               | Mime Type                                    | `char`               |     |       |                        |
| `name`                   | Name                                         | `char`               | ✅  |       |                        |
| `original_id`            | Original (unoptimized, unresized) attachment | `many2one`           |     |       | ir.attachment          |
| `public`                 | Is public document                           | `boolean`            |     |       |                        |
| `quotation_template_ids` | Quotation Templates                          | `many2many`          |     | ✅    | sale.order.template    |
| `raw`                    | File Content (raw)                           | `binary`             |     |       |                        |
| `res_field`              | Resource Field                               | `char`               |     |       |                        |
| `res_id`                 | Resource ID                                  | `many2one_reference` |     |       |                        |
| `res_model`              | Resource Model                               | `char`               |     |       |                        |
| `res_name`               | Resource Name                                | `char`               |     |       |                        |
| `sequence`               | Sequence                                     | `integer`            |     | ✅    |                        |
| `store_fname`            | Stored Filename                              | `char`               |     |       |                        |
| `theme_template_id`      | Theme Template                               | `many2one`           |     |       | theme.ir.attachment    |
| `thumbnail`              | Thumbnail                                    | `binary`             |     |       |                        |
| `type`                   | Type                                         | `selection`          | ✅  |       |                        |
| `url`                    | Url                                          | `char`               |     |       |                        |
| `voice_ids`              | Voice                                        | `one2many`           |     |       | discuss.voice.metadata |
| `website_id`             | Website                                      | `many2one`           |     |       | website                |
| `whatsapp_media_id`      | whatsapp Media Id                            | `char`               |     |       |                        |
| `write_date`             | Last Updated on                              | `datetime`           |     | ✅    |                        |
| `write_uid`              | Last Updated by                              | `many2one`           |     | ✅    | res.users              |

**Access Rights:**

| Name                                    | Group                 | Perms     |
| --------------------------------------- | --------------------- | --------- |
| access_quotation_document_sales_manager | Sales / Administrator | `R/W/C/D` |
| access_quotation_document_user          | Role / User           | `R`       |

**Record Rules:**

- **Quotation document multi-company rule** (Global) `R/W/C/D`
  - Domain:
    `         ['|', ('company_id', '=', False), ('company_id', 'parent_of', company_ids)]     `

### 🗃️ `sale.order.template` — Quotation Template

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                          | Label                 | Type        | Req | Store | Relation                 |
| ------------------------------ | --------------------- | ----------- | --- | ----- | ------------------------ |
| `active`                       | Active                | `boolean`   |     | ✅    |                          |
| `company_id`                   | Company               | `many2one`  |     | ✅    | res.company              |
| `create_date`                  | Created on            | `datetime`  |     | ✅    |                          |
| `create_uid`                   | Created by            | `many2one`  |     | ✅    | res.users                |
| `display_name`                 | Display Name          | `char`      |     |       |                          |
| `id`                           | ID                    | `integer`   |     | ✅    |                          |
| `journal_id`                   | Invoicing Journal     | `many2one`  |     | ✅    | account.journal          |
| `mail_template_id`             | Confirmation Mail     | `many2one`  |     | ✅    | mail.template            |
| `name`                         | Quotation Template    | `char`      | ✅  | ✅    |                          |
| `note`                         | Terms and conditions  | `html`      |     | ✅    |                          |
| `number_of_days`               | Quotation Duration    | `integer`   |     | ✅    |                          |
| `prepayment_percent`           | Prepayment percentage | `float`     |     | ✅    |                          |
| `quotation_document_ids`       | Headers and footers   | `many2many` |     | ✅    | quotation.document       |
| `require_payment`              | Online Payment        | `boolean`   |     | ✅    |                          |
| `require_signature`            | Online Signature      | `boolean`   |     | ✅    |                          |
| `sale_order_template_line_ids` | Lines                 | `one2many`  |     | ✅    | sale.order.template.line |
| `sequence`                     | Sequence              | `integer`   |     | ✅    |                          |
| `write_date`                   | Last Updated on       | `datetime`  |     | ✅    |                          |
| `write_uid`                    | Last Updated by       | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                | Group                            | Perms     |
| ------------------- | -------------------------------- | --------- |
| sale.order.template | Sales / User: Own Documents Only | `R`       |
| sale.order.template | Sales / Administrator            | `R/W/C/D` |
| sale.order.template | Role / Administrator             | `R`       |

**Record Rules:**

- **Quotation Template multi-company** (Global) `R/W/C/D`
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
