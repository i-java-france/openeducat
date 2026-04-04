---
title: "Mass mailing on sale orders"
module: "mass_mailing_sale"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Email Marketing"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_______________]
---

# 🟢 Mass mailing on sale orders

> **Module:** `mass_mailing_sale` | **Version:** `19.0.1.0` **Category:** Email
> Marketing | **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[sale]] [[mass_mailing]]

## 📖 Description

UTM and mass mailing on sale orders

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT mailing.mailing.view.form.inherit.sale (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

### 🗃️ `mailing.mailing` — Mass Mailing

> 📧 Mail Thread

Mass Mailing models the sending of emails to a list of recipients for a mass mailing
campaign.

**Fields:**

| Field                           | Label                                       | Type        | Req | Store | Relation           |
| ------------------------------- | ------------------------------------------- | ----------- | --- | ----- | ------------------ |
| `ab_testing_completed`          | A/B Testing Campaign Finished               | `boolean`   |     |       |                    |
| `ab_testing_description`        | A/B Testing Description                     | `html`      |     |       |                    |
| `ab_testing_enabled`            | Allow A/B Testing                           | `boolean`   |     | ✅    |                    |
| `ab_testing_is_winner_mailing`  | Is the Winner of its Campaign               | `boolean`   |     |       |                    |
| `ab_testing_mailings_count`     | A/B Test Mailings #                         | `integer`   |     |       |                    |
| `ab_testing_pc`                 | A/B Testing percentage                      | `integer`   |     | ✅    |                    |
| `ab_testing_schedule_datetime`  | Send Final On                               | `datetime`  |     |       |                    |
| `ab_testing_winner_selection`   | Winner Selection                            | `selection` |     |       |                    |
| `active`                        | Active                                      | `boolean`   |     | ✅    |                    |
| `activity_calendar_event_id`    | Next Activity Calendar Event                | `many2one`  |     |       | calendar.event     |
| `activity_date_deadline`        | Next Activity Deadline                      | `date`      |     |       |                    |
| `activity_exception_decoration` | Activity Exception Decoration               | `selection` |     |       |                    |
| `activity_exception_icon`       | Icon                                        | `char`      |     |       |                    |
| `activity_ids`                  | Activities                                  | `one2many`  |     | ✅    | mail.activity      |
| `activity_state`                | Activity State                              | `selection` |     |       |                    |
| `activity_summary`              | Next Activity Summary                       | `char`      |     |       |                    |
| `activity_type_icon`            | Activity Type Icon                          | `char`      |     |       |                    |
| `activity_type_id`              | Next Activity Type                          | `many2one`  |     |       | mail.activity.type |
| `activity_user_id`              | Responsible User                            | `many2one`  |     |       | res.users          |
| `attachment_ids`                | Attachments                                 | `many2many` |     | ✅    | ir.attachment      |
| `automated_marketing`           | Specific mailing used in marketing campaign | `boolean`   |     | ✅    |                    |
| `body_arch`                     | Body                                        | `html`      |     | ✅    |                    |
| `body_html`                     | Body converted to be sent by mail           | `html`      |     | ✅    |                    |
| `bounced`                       | Bounced                                     | `integer`   |     |       |                    |
| `bounced_ratio`                 | Bounced Ratio                               | `float`     |     |       |                    |
| `calendar_date`                 | Calendar Date                               | `datetime`  |     | ✅    |                    |
| `campaign_id`                   | UTM Campaign                                | `many2one`  |     | ✅    | utm.campaign       |
| `canceled`                      | Canceled                                    | `integer`   |     |       |                    |
| `clicked`                       | Clicked                                     | `integer`   |     |       |                    |
| `clicks_ratio`                  | Number of Clicks                            | `float`     |     |       |                    |
| `color`                         | Color Index                                 | `integer`   |     | ✅    |                    |
| `contact_list_ids`              | Mailing Lists                               | `many2many` |     | ✅    | mailing.list       |
| `create_date`                   | Created on                                  | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                                  | `many2one`  |     | ✅    | res.users          |
| `crm_lead_count`                | Leads/Opportunities Count                   | `integer`   |     |       |                    |
| `delivered`                     | Delivered                                   | `integer`   |     |       |                    |
| `display_name`                  | Display Name                                | `char`      |     |       |                    |
| `email_from`                    | Send From                                   | `char`      |     | ✅    |                    |
| `expected`                      | Expected                                    | `integer`   |     |       |                    |
| `failed`                        | Failed                                      | `integer`   |     |       |                    |
| `favorite`                      | Favorite                                    | `boolean`   |     | ✅    |                    |
| `favorite_date`                 | Favorite Date                               | `datetime`  |     | ✅    |                    |
| `has_message`                   | Has Message                                 | `boolean`   |     |       |                    |
| `id`                            | ID                                          | `integer`   |     | ✅    |                    |
| `is_ab_test_sent`               | Is Ab Test Sent                             | `boolean`   |     |       |                    |
| `is_body_empty`                 | Is Body Empty                               | `boolean`   |     |       |                    |
| `keep_archives`                 | Keep Archives                               | `boolean`   |     | ✅    |                    |
| `kpi_mail_required`             | KPI mail required                           | `boolean`   |     | ✅    |                    |
| `lang`                          | Language                                    | `char`      |     | ✅    |                    |
| `link_trackers_count`           | Link Trackers Count                         | `integer`   |     |       |                    |
| `mailing_domain`                | Domain                                      | `char`      |     | ✅    |                    |
| `mailing_filter_count`          | # Favorite Filters                          | `integer`   |     |       |                    |
| `mailing_filter_domain`         | Favorite filter domain                      | `char`      |     |       |                    |
| `mailing_filter_id`             | Favorite Filter                             | `many2one`  |     | ✅    | mailing.filter     |
| `mailing_model_id`              | Recipients Model                            | `many2one`  | ✅  | ✅    | ir.model           |
| `mailing_model_name`            | Recipients Model Name                       | `char`      |     |       |                    |
| `mailing_model_real`            | Recipients Real Model                       | `char`      |     |       |                    |
| `mailing_on_mailing_list`       | Based on Mailing Lists                      | `boolean`   |     |       |                    |
| `mailing_trace_ids`             | Emails Statistics                           | `one2many`  |     | ✅    | mailing.trace      |
| `mailing_type`                  | Mailing Type                                | `selection` | ✅  | ✅    |                    |
| `mailing_type_description`      | Mailing Type Description                    | `char`      |     |       |                    |
| `mail_server_available`         | Mail Server Available                       | `boolean`   |     |       |                    |
| `mail_server_id`                | Mail Server                                 | `many2one`  |     | ✅    | ir.mail_server     |
| `marketing_activity_ids`        | Marketing Activities                        | `one2many`  |     | ✅    | marketing.activity |
| `medium_id`                     | Medium                                      | `many2one`  |     | ✅    | utm.medium         |
| `message_attachment_count`      | Attachment Count                            | `integer`   |     |       |                    |
| `message_follower_ids`          | Followers                                   | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`             | Message Delivery error                      | `boolean`   |     |       |                    |
| `message_has_error_counter`     | Number of errors                            | `integer`   |     |       |                    |
| `message_has_sms_error`         | SMS Delivery error                          | `boolean`   |     |       |                    |
| `message_ids`                   | Messages                                    | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`           | Is Follower                                 | `boolean`   |     |       |                    |
| `message_needaction`            | Action Needed                               | `boolean`   |     |       |                    |
| `message_needaction_counter`    | Number of Actions                           | `integer`   |     |       |                    |
| `message_partner_ids`           | Followers (Partners)                        | `many2many` |     |       | res.partner        |
| `my_activity_date_deadline`     | My Activity Deadline                        | `date`      |     |       |                    |
| `name`                          | Name                                        | `char`      |     |       |                    |
| `next_departure`                | Scheduled date                              | `datetime`  |     |       |                    |
| `next_departure_is_past`        | Next Departure Is Past                      | `boolean`   |     |       |                    |
| `opened`                        | Opened                                      | `integer`   |     |       |                    |
| `opened_ratio`                  | Opened Ratio                                | `float`     |     |       |                    |
| `pending`                       | Pending                                     | `integer`   |     |       |                    |
| `preview`                       | Preview                                     | `char`      |     | ✅    |                    |
| `process`                       | Process                                     | `integer`   |     |       |                    |
| `rating_ids`                    | Ratings                                     | `one2many`  |     | ✅    | rating.rating      |
| `received_ratio`                | Received Ratio                              | `float`     |     |       |                    |
| `render_model`                  | Rendering Model                             | `char`      |     |       |                    |
| `replied`                       | Replied                                     | `integer`   |     |       |                    |
| `replied_ratio`                 | Replied Ratio                               | `float`     |     |       |                    |
| `reply_to`                      | Reply To                                    | `char`      |     | ✅    |                    |
| `reply_to_mode`                 | Reply-To Mode                               | `selection` |     | ✅    |                    |
| `sale_invoiced_amount`          | Invoiced Amount                             | `integer`   |     |       |                    |
| `sale_quotation_count`          | Quotation Count                             | `integer`   |     |       |                    |
| `scheduled`                     | Scheduled                                   | `integer`   |     |       |                    |
| `schedule_date`                 | Scheduled for                               | `datetime`  |     | ✅    |                    |
| `schedule_type`                 | Schedule                                    | `selection` | ✅  | ✅    |                    |
| `sent`                          | Sent                                        | `integer`   |     |       |                    |
| `sent_date`                     | Sent Date                                   | `datetime`  |     | ✅    |                    |
| `source_id`                     | Source                                      | `many2one`  | ✅  | ✅    | utm.source         |
| `state`                         | Status                                      | `selection` | ✅  | ✅    |                    |
| `subject`                       | Subject                                     | `char`      | ✅  | ✅    |                    |
| `total`                         | Total                                       | `integer`   |     |       |                    |
| `use_exclusion_list`            | Use Exclusion List                          | `boolean`   |     | ✅    |                    |
| `use_leads`                     | Use Leads                                   | `boolean`   |     |       |                    |
| `user_id`                       | Responsible                                 | `many2one`  |     | ✅    | res.users          |
| `warning_message`               | Warning Message                             | `char`      |     |       |                    |
| `website_message_ids`           | Website Messages                            | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on                             | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by                             | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                           | Group                  | Perms     |
| ------------------------------ | ---------------------- | --------- |
| access.mailing.mailing.mm.user | Email Marketing / User | `R/W/C/D` |
| access.mailing.mailing.system  | Role / Administrator   | `R/W/C/D` |

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

### 🗃️ `utm.campaign` — UTM Campaign

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                                      | Type        | Req | Store | Relation        |
| ------------------------------- | ------------------------------------------ | ----------- | --- | ----- | --------------- |
| `ab_testing_completed`          | A/B Testing Campaign Finished              | `boolean`   |     | ✅    |                 |
| `ab_testing_mailings_count`     | A/B Test Mailings #                        | `integer`   |     |       |                 |
| `ab_testing_schedule_datetime`  | Send Final On                              | `datetime`  |     | ✅    |                 |
| `ab_testing_winner_mailing_id`  | A/B Campaign Winner Mailing                | `many2one`  |     | ✅    | mailing.mailing |
| `ab_testing_winner_selection`   | Winner Selection                           | `selection` |     | ✅    |                 |
| `active`                        | Active                                     | `boolean`   |     | ✅    |                 |
| `bounced_ratio`                 | Bounced Ratio                              | `float`     |     |       |                 |
| `click_count`                   | Number of clicks generated by the campaign | `integer`   |     |       |                 |
| `color`                         | Color Index                                | `integer`   |     | ✅    |                 |
| `company_id`                    | Company                                    | `many2one`  |     | ✅    | res.company     |
| `create_date`                   | Created on                                 | `datetime`  |     | ✅    |                 |
| `create_uid`                    | Created by                                 | `many2one`  |     | ✅    | res.users       |
| `crm_lead_count`                | Leads/Opportunities count                  | `integer`   |     |       |                 |
| `currency_id`                   | Currency                                   | `many2one`  |     |       | res.currency    |
| `display_name`                  | Display Name                               | `char`      |     |       |                 |
| `id`                            | ID                                         | `integer`   |     | ✅    |                 |
| `invoiced_amount`               | Revenues generated by the campaign         | `integer`   |     |       |                 |
| `is_auto_campaign`              | Automatically Generated Campaign           | `boolean`   |     | ✅    |                 |
| `is_mailing_campaign_activated` | Is Mailing Campaign Activated              | `boolean`   |     |       |                 |
| `mailing_mail_count`            | Number of Mass Mailing                     | `integer`   |     |       |                 |
| `mailing_mail_ids`              | Mass Mailings                              | `one2many`  |     | ✅    | mailing.mailing |
| `name`                          | Campaign Identifier                        | `char`      | ✅  | ✅    |                 |
| `opened_ratio`                  | Opened Ratio                               | `float`     |     |       |                 |
| `quotation_count`               | Quotation Count                            | `integer`   |     |       |                 |
| `received_ratio`                | Received Ratio                             | `float`     |     |       |                 |
| `replied_ratio`                 | Replied Ratio                              | `float`     |     |       |                 |
| `stage_id`                      | Stage                                      | `many2one`  | ✅  | ✅    | utm.stage       |
| `tag_ids`                       | Tags                                       | `many2many` |     | ✅    | utm.tag         |
| `title`                         | Campaign Name                              | `char`      | ✅  | ✅    |                 |
| `use_leads`                     | Use Leads                                  | `boolean`   |     |       |                 |
| `user_id`                       | Responsible                                | `many2one`  | ✅  | ✅    | res.users       |
| `write_date`                    | Last Updated on                            | `datetime`  |     | ✅    |                 |
| `write_uid`                     | Last Updated by                            | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                     | Group                  | Perms     |
| ------------------------ | ---------------------- | --------- |
| utm.campaign             | Email Marketing / User | `R/W/C/D` |
| utm.campaign.system      | Role / Administrator   | `R/W/C/D` |
| access_utm_campaign_user | Role / User            | `R/W/C`   |
