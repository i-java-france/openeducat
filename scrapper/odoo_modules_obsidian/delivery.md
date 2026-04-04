---
title: "Delivery Costs"
module: "delivery"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Delivery"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/________]
---

# 🟢 Delivery Costs

> **Module:** `delivery` | **Version:** `19.0.1.0` **Category:** Delivery | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[sale]] [[payment_custom]]

## 📖 Description

# Allows you to add delivery methods in sale orders.

You can define your own carrier for prices. The system is able to add and compute the
shipping line.

## 🖥️ UI Components

### Menus

- `Sales/Configuration/Sales Orders/Delivery Methods`

### Views

- `* INHERIT COD Provider Form (form)`
- `* INHERIT Delivery Provider Module Kanban (kanban)`
- `* INHERIT Delivery Provider Module List (list)`
- `* INHERIT delivery.sale.order.form.view.with_carrier (form)`
- `* INHERIT delivery_report_saleorder_document (qweb)`
- `* INHERIT delivery_submit_button (qweb)`
- `* INHERIT res.config.settings.view.form.inherit.delivery (form)`
- `* INHERIT res.partner.carrier.property.form.inherit (form)`
- `choose.delivery.carrier.form (form)`
- `delivery.carrier.form (form)`
- `delivery.carrier.list (list)`
- `delivery.carrier.search (search)`
- `delivery.price.rule.form (form)`
- `delivery.price.rule.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**12 model(s) defined by this module:**

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

### 🗃️ `product.category` — Product Category

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                  | Label                      | Type                    | Req | Store | Relation           |
| -------------------------------------- | -------------------------- | ----------------------- | --- | ----- | ------------------ |
| `account_stock_variation_id`           | Stock Variation Account    | `many2one`              |     |       | account.account    |
| `anglo_saxon_accounting`               | Use Anglo-Saxon Accounting | `boolean`               |     |       |                    |
| `child_id`                             | Child Categories           | `one2many`              |     | ✅    | product.category   |
| `complete_name`                        | Complete Name              | `char`                  |     | ✅    |                    |
| `create_date`                          | Created on                 | `datetime`              |     | ✅    |                    |
| `create_uid`                           | Created by                 | `many2one`              |     | ✅    | res.users          |
| `display_name`                         | Display Name               | `char`                  |     |       |                    |
| `filter_for_stock_putaway_rule`        | stock.putaway.rule         | `boolean`               |     |       |                    |
| `has_message`                          | Has Message                | `boolean`               |     |       |                    |
| `id`                                   | ID                         | `integer`               |     | ✅    |                    |
| `message_attachment_count`             | Attachment Count           | `integer`               |     |       |                    |
| `message_follower_ids`                 | Followers                  | `one2many`              |     | ✅    | mail.followers     |
| `message_has_error`                    | Message Delivery error     | `boolean`               |     |       |                    |
| `message_has_error_counter`            | Number of errors           | `integer`               |     |       |                    |
| `message_has_sms_error`                | SMS Delivery error         | `boolean`               |     |       |                    |
| `message_ids`                          | Messages                   | `one2many`              |     | ✅    | mail.message       |
| `message_is_follower`                  | Is Follower                | `boolean`               |     |       |                    |
| `message_needaction`                   | Action Needed              | `boolean`               |     |       |                    |
| `message_needaction_counter`           | Number of Actions          | `integer`               |     |       |                    |
| `message_partner_ids`                  | Followers (Partners)       | `many2many`             |     |       | res.partner        |
| `name`                                 | Name                       | `char`                  | ✅  | ✅    |                    |
| `packaging_reserve_method`             | Reserve Packagings         | `selection`             |     | ✅    |                    |
| `parent_id`                            | Parent Category            | `many2one`              |     | ✅    | product.category   |
| `parent_path`                          | Parent Path                | `char`                  |     | ✅    |                    |
| `parent_route_ids`                     | Parent Routes              | `many2many`             |     |       | stock.route        |
| `product_count`                        | # Products                 | `integer`               |     |       |                    |
| `product_properties_definition`        | Product Properties         | `properties_definition` |     | ✅    |                    |
| `property_account_expense_categ_id`    | Expense Account            | `many2one`              |     | ✅    | account.account    |
| `property_account_income_categ_id`     | Income Account             | `many2one`              |     | ✅    | account.account    |
| `property_cost_method`                 | Costing Method             | `selection`             |     | ✅    |                    |
| `property_price_difference_account_id` | Price Difference Account   | `many2one`              |     | ✅    | account.account    |
| `property_stock_journal`               | Stock Journal              | `many2one`              |     | ✅    | account.journal    |
| `property_stock_valuation_account_id`  | Stock Valuation Account    | `many2one`              |     | ✅    | account.account    |
| `property_valuation`                   | Inventory Valuation        | `selection`             |     | ✅    |                    |
| `putaway_rule_ids`                     | Putaway Rules              | `one2many`              |     | ✅    | stock.putaway.rule |
| `rating_ids`                           | Ratings                    | `one2many`              |     | ✅    | rating.rating      |
| `removal_strategy_id`                  | Force Removal Strategy     | `many2one`              |     | ✅    | product.removal    |
| `route_ids`                            | Routes                     | `many2many`             |     | ✅    | stock.route        |
| `total_route_ids`                      | Total routes               | `many2many`             |     |       | stock.route        |
| `website_message_ids`                  | Website Messages           | `one2many`              |     | ✅    | mail.message       |
| `write_date`                           | Last Updated on            | `datetime`              |     | ✅    |                    |
| `write_uid`                            | Last Updated by            | `many2one`              |     | ✅    | res.users          |

**Access Rights:**

| Name                     | Group             | Perms     |
| ------------------------ | ----------------- | --------- |
| product.category.manager | Products / Create | `R/W/C/D` |
| product.category.public  | Role / Portal     | `R`       |
| product.category.public  | Role / Public     | `R`       |
| product.category.public  | Role / User       | `R`       |
| product.category.user    | Role / User       | `R`       |

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

### 🗃️ `choose.delivery.carrier` — Delivery Carrier Selection Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                   | Label              | Type        | Req | Store | Relation         |
| ----------------------- | ------------------ | ----------- | --- | ----- | ---------------- |
| `available_carrier_ids` | Available Carriers | `many2many` |     |       | delivery.carrier |
| `carrier_id`            | Shipping Method    | `many2one`  | ✅  | ✅    | delivery.carrier |
| `company_id`            | Company            | `many2one`  |     |       | res.company      |
| `create_date`           | Created on         | `datetime`  |     | ✅    |                  |
| `create_uid`            | Created by         | `many2one`  |     | ✅    | res.users        |
| `currency_id`           | Currency           | `many2one`  |     |       | res.currency     |
| `delivery_message`      | Delivery Message   | `text`      |     | ✅    |                  |
| `delivery_price`        | Delivery Price     | `float`     |     | ✅    |                  |
| `delivery_type`         | Provider           | `selection` |     |       |                  |
| `display_name`          | Display Name       | `char`      |     |       |                  |
| `display_price`         | Cost               | `float`     |     | ✅    |                  |
| `id`                    | ID                 | `integer`   |     | ✅    |                  |
| `invoicing_message`     | Invoicing Message  | `text`      |     |       |                  |
| `order_id`              | Order              | `many2one`  | ✅  | ✅    | sale.order       |
| `partner_id`            | Customer           | `many2one`  | ✅  |       | res.partner      |
| `total_weight`          | Total Order Weight | `float`     |     |       |                  |
| `weight_uom_name`       | Weight Uom Name    | `char`      |     | ✅    |                  |
| `write_date`            | Last Updated on    | `datetime`  |     | ✅    |                  |
| `write_uid`             | Last Updated by    | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                                      | Group                            | Perms   |
| ----------------------------------------- | -------------------------------- | ------- |
| delivery.choose.delivery.carrier          | Sales / User: Own Documents Only | `R/W/C` |
| access.choose.delivery.carrier stock_user | Inventory / User                 | `R/W/C` |

### 🗃️ `delivery.price.rule` — Delivery Price Rules

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label           | Type        | Req | Store | Relation         |
| ----------------- | --------------- | ----------- | --- | ----- | ---------------- |
| `carrier_id`      | Carrier         | `many2one`  | ✅  | ✅    | delivery.carrier |
| `create_date`     | Created on      | `datetime`  |     | ✅    |                  |
| `create_uid`      | Created by      | `many2one`  |     | ✅    | res.users        |
| `currency_id`     | Currency        | `many2one`  |     |       | res.currency     |
| `display_name`    | Display Name    | `char`      |     |       |                  |
| `id`              | ID              | `integer`   |     | ✅    |                  |
| `list_base_price` | Sale Base Price | `float`     | ✅  | ✅    |                  |
| `list_price`      | Sale Price      | `float`     | ✅  | ✅    |                  |
| `max_value`       | Maximum Value   | `float`     | ✅  | ✅    |                  |
| `name`            | Name            | `char`      |     |       |                  |
| `operator`        | Operator        | `selection` | ✅  | ✅    |                  |
| `sequence`        | Sequence        | `integer`   | ✅  | ✅    |                  |
| `variable`        | Variable        | `selection` | ✅  | ✅    |                  |
| `variable_factor` | Variable Factor | `selection` | ✅  | ✅    |                  |
| `write_date`      | Last Updated on | `datetime`  |     | ✅    |                  |
| `write_uid`       | Last Updated by | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                              | Group                            | Perms     |
| --------------------------------- | -------------------------------- | --------- |
| delivery.price.rule               | Sales / User: Own Documents Only | `R`       |
| delivery.price.rule               | Sales / Administrator            | `R/W/C/D` |
| delivery.price.rule               | Sales / Administrator            | `R/W/C/D` |
| delivery.price.rule stock_manager | Inventory / User                 | `R`       |
| delivery.price.rule stock_manager | Inventory / Administrator        | `R/W/C/D` |

### 🗃️ `delivery.zip.prefix` — Delivery Zip Prefix

Zip prefix that a delivery.carrier will deliver to.

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Prefix          | `char`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                              | Group                            | Perms     |
| --------------------------------- | -------------------------------- | --------- |
| delivery.zip.prefix               | Sales / User: Own Documents Only | `R`       |
| delivery.zip.prefix               | Contact / Creation               | `R/W/C/D` |
| delivery.zip.prefix stock_manager | Inventory / User                 | `R`       |
| delivery.zip.prefix stock_manager | Inventory / Administrator        | `R/W/C/D` |

### 🗃️ `ir.http` — HTTP Routing

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.module.module` — Module

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                             | Label                           | Type        | Req | Store | Relation                    |
| --------------------------------- | ------------------------------- | ----------- | --- | ----- | --------------------------- |
| `account_templates`               | Account Templates               | `binary`    |     |       |                             |
| `application`                     | Application                     | `boolean`   |     | ✅    |                             |
| `author`                          | Author                          | `char`      |     | ✅    |                             |
| `auto_install`                    | Automatic Installation          | `boolean`   |     | ✅    |                             |
| `category_id`                     | Category                        | `many2one`  |     | ✅    | ir.module.category          |
| `contributors`                    | Contributors                    | `text`      |     | ✅    |                             |
| `country_ids`                     | Country                         | `many2many` |     | ✅    | res.country                 |
| `create_date`                     | Created on                      | `datetime`  |     | ✅    |                             |
| `create_uid`                      | Created by                      | `many2one`  |     | ✅    | res.users                   |
| `demo`                            | Demo Data                       | `boolean`   |     | ✅    |                             |
| `dependencies_id`                 | Dependencies                    | `one2many`  |     | ✅    | ir.module.module.dependency |
| `description`                     | Description                     | `text`      |     | ✅    |                             |
| `description_html`                | Description HTML                | `html`      |     |       |                             |
| `display_name`                    | Display Name                    | `char`      |     |       |                             |
| `exclusion_ids`                   | Exclusions                      | `one2many`  |     | ✅    | ir.module.module.exclusion  |
| `has_iap`                         | Has Iap                         | `boolean`   |     |       |                             |
| `icon`                            | Icon URL                        | `char`      |     | ✅    |                             |
| `icon_flag`                       | Flag                            | `char`      |     |       |                             |
| `icon_image`                      | Icon                            | `binary`    |     |       |                             |
| `id`                              | ID                              | `integer`   |     | ✅    |                             |
| `image_ids`                       | Screenshots                     | `one2many`  |     | ✅    | ir.attachment               |
| `imported`                        | Imported Module                 | `boolean`   |     | ✅    |                             |
| `installed_version`               | Latest Version                  | `char`      |     |       |                             |
| `is_installed_on_current_website` | Is Installed On Current Website | `boolean`   |     |       |                             |
| `latest_version`                  | Installed Version               | `char`      |     | ✅    |                             |
| `license`                         | License                         | `selection` |     | ✅    |                             |
| `maintainer`                      | Maintainer                      | `char`      |     | ✅    |                             |
| `menus_by_module`                 | Menus                           | `text`      |     | ✅    |                             |
| `module_type`                     | Module Type                     | `selection` |     | ✅    |                             |
| `name`                            | Technical Name                  | `char`      | ✅  | ✅    |                             |
| `published_version`               | Published Version               | `char`      |     | ✅    |                             |
| `reports_by_module`               | Reports                         | `text`      |     | ✅    |                             |
| `sequence`                        | Sequence                        | `integer`   |     | ✅    |                             |
| `shortdesc`                       | Module Name                     | `char`      |     | ✅    |                             |
| `state`                           | Status                          | `selection` |     | ✅    |                             |
| `summary`                         | Summary                         | `char`      |     | ✅    |                             |
| `to_buy`                          | Odoo Enterprise Module          | `boolean`   |     | ✅    |                             |
| `url`                             | URL                             | `char`      |     | ✅    |                             |
| `views_by_module`                 | Views                           | `text`      |     | ✅    |                             |
| `website`                         | Website                         | `char`      |     | ✅    |                             |
| `write_date`                      | Last Updated on                 | `datetime`  |     | ✅    |                             |
| `write_uid`                       | Last Updated by                 | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                        | Group                | Perms     |
| --------------------------- | -------------------- | --------- |
| ir_module_module group_user | Role / Administrator | `R/W/C/D` |
| ir_module_module group_user | Role / User          | `R`       |

### 🗃️ `payment.provider` — Payment Provider

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                          | Type        | Req | Store | Relation         |
| ------------------------------- | ------------------------------ | ----------- | --- | ----- | ---------------- |
| `allow_express_checkout`        | Allow Express Checkout         | `boolean`   |     | ✅    |                  |
| `allow_tokenization`            | Allow Saving Payment Methods   | `boolean`   |     | ✅    |                  |
| `auth_msg`                      | Authorize Message              | `html`      |     | ✅    |                  |
| `available_country_ids`         | Countries                      | `many2many` |     | ✅    | res.country      |
| `available_currency_ids`        | Currencies                     | `many2many` |     | ✅    | res.currency     |
| `cancel_msg`                    | Cancelled Message              | `html`      |     | ✅    |                  |
| `capture_manually`              | Capture Amount Manually        | `boolean`   |     | ✅    |                  |
| `code`                          | Code                           | `selection` | ✅  | ✅    |                  |
| `color`                         | Color                          | `integer`   |     | ✅    |                  |
| `company_id`                    | Company                        | `many2one`  | ✅  | ✅    | res.company      |
| `create_date`                   | Created on                     | `datetime`  |     | ✅    |                  |
| `create_uid`                    | Created by                     | `many2one`  |     | ✅    | res.users        |
| `custom_mode`                   | Custom Mode                    | `selection` |     | ✅    |                  |
| `display_name`                  | Display Name                   | `char`      |     |       |                  |
| `done_msg`                      | Done Message                   | `html`      |     | ✅    |                  |
| `express_checkout_form_view_id` | Express Checkout Form Template | `many2one`  |     | ✅    | ir.ui.view       |
| `id`                            | ID                             | `integer`   |     | ✅    |                  |
| `image_128`                     | Image                          | `binary`    |     | ✅    |                  |
| `inline_form_view_id`           | Inline Form Template           | `many2one`  |     | ✅    | ir.ui.view       |
| `is_published`                  | Published                      | `boolean`   |     | ✅    |                  |
| `journal_id`                    | Payment Journal                | `many2one`  |     |       | account.journal  |
| `main_currency_id`              | Currency                       | `many2one`  |     |       | res.currency     |
| `maximum_amount`                | Maximum Amount                 | `monetary`  |     | ✅    |                  |
| `module_id`                     | Corresponding Module           | `many2one`  |     | ✅    | ir.module.module |
| `module_state`                  | Installation State             | `selection` |     |       |                  |
| `module_to_buy`                 | Odoo Enterprise Module         | `boolean`   |     |       |                  |
| `name`                          | Name                           | `char`      | ✅  | ✅    |                  |
| `payment_method_ids`            | Supported Payment Methods      | `many2many` |     | ✅    | payment.method   |
| `pending_msg`                   | Pending Message                | `html`      |     | ✅    |                  |
| `pre_msg`                       | Help Message                   | `html`      |     | ✅    |                  |
| `qr_code`                       | Enable QR Codes                | `boolean`   |     | ✅    |                  |
| `redirect_form_view_id`         | Redirect Form Template         | `many2one`  |     | ✅    | ir.ui.view       |
| `sequence`                      | Sequence                       | `integer`   |     | ✅    |                  |
| `so_reference_type`             | Communication                  | `selection` |     | ✅    |                  |
| `state`                         | State                          | `selection` | ✅  | ✅    |                  |
| `support_express_checkout`      | Express Checkout               | `boolean`   |     |       |                  |
| `support_manual_capture`        | Manual Capture Supported       | `selection` |     |       |                  |
| `support_refund`                | Refund                         | `selection` |     |       |                  |
| `support_tokenization`          | Tokenization                   | `boolean`   |     |       |                  |
| `token_inline_form_view_id`     | Token Inline Form Template     | `many2one`  |     | ✅    | ir.ui.view       |
| `website_id`                    | Website                        | `many2one`  |     | ✅    | website          |
| `write_date`                    | Last Updated on                | `datetime`  |     | ✅    |                  |
| `write_uid`                     | Last Updated by                | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                    | Group                | Perms     |
| ----------------------- | -------------------- | --------- |
| payment.provider.system | Role / Administrator | `R/W/C/D` |

**Record Rules:**

- **Access providers in own companies only** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'parent_of', company_ids)]`

### 🗃️ `payment.transaction` — Payment Transaction

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                       | Label                   | Type        | Req | Store | Relation            |
| --------------------------- | ----------------------- | ----------- | --- | ----- | ------------------- |
| `amount`                    | Amount                  | `monetary`  | ✅  | ✅    |                     |
| `capture_manually`          | Capture Amount Manually | `boolean`   |     |       |                     |
| `child_transaction_ids`     | Child Transactions      | `one2many`  |     | ✅    | payment.transaction |
| `company_id`                | Company                 | `many2one`  |     | ✅    | res.company         |
| `create_date`               | Created on              | `datetime`  |     | ✅    |                     |
| `create_uid`                | Created by              | `many2one`  |     | ✅    | res.users           |
| `currency_id`               | Currency                | `many2one`  | ✅  | ✅    | res.currency        |
| `display_name`              | Display Name            | `char`      |     |       |                     |
| `id`                        | ID                      | `integer`   |     | ✅    |                     |
| `invoice_ids`               | Invoices                | `many2many` |     | ✅    | account.move        |
| `invoices_count`            | Invoices Count          | `integer`   |     |       |                     |
| `is_donation`               | Is donation             | `boolean`   |     | ✅    |                     |
| `is_live`                   | Production Environment  | `boolean`   |     | ✅    |                     |
| `is_post_processed`         | Is Post-processed       | `boolean`   |     | ✅    |                     |
| `landing_route`             | Landing Route           | `char`      |     | ✅    |                     |
| `last_state_change`         | Last State Change Date  | `datetime`  |     | ✅    |                     |
| `operation`                 | Operation               | `selection` |     | ✅    |                     |
| `partner_address`           | Address                 | `char`      |     | ✅    |                     |
| `partner_city`              | City                    | `char`      |     | ✅    |                     |
| `partner_country_id`        | Country                 | `many2one`  |     | ✅    | res.country         |
| `partner_email`             | Email                   | `char`      |     | ✅    |                     |
| `partner_id`                | Customer                | `many2one`  | ✅  | ✅    | res.partner         |
| `partner_lang`              | Language                | `selection` |     | ✅    |                     |
| `partner_name`              | Partner Name            | `char`      |     | ✅    |                     |
| `partner_phone`             | Phone                   | `char`      |     | ✅    |                     |
| `partner_state_id`          | State                   | `many2one`  |     | ✅    | res.country.state   |
| `partner_zip`               | Zip                     | `char`      |     | ✅    |                     |
| `payment_id`                | Payment                 | `many2one`  |     | ✅    | account.payment     |
| `payment_method_code`       | Payment Method Code     | `char`      |     |       |                     |
| `payment_method_id`         | Payment Method          | `many2one`  | ✅  | ✅    | payment.method      |
| `primary_payment_method_id` | Primary Payment Method  | `many2one`  |     |       | payment.method      |
| `provider_code`             | Provider Code           | `selection` |     |       |                     |
| `provider_id`               | Provider                | `many2one`  | ✅  | ✅    | payment.provider    |
| `provider_reference`        | Provider Reference      | `char`      |     | ✅    |                     |
| `reference`                 | Reference               | `char`      | ✅  | ✅    |                     |
| `refunds_count`             | Refunds Count           | `integer`   |     |       |                     |
| `sale_order_ids`            | Sales Orders            | `many2many` |     | ✅    | sale.order          |
| `sale_order_ids_nbr`        | # of Sales Orders       | `integer`   |     |       |                     |
| `source_transaction_id`     | Source Transaction      | `many2one`  |     | ✅    | payment.transaction |
| `state`                     | Status                  | `selection` | ✅  | ✅    |                     |
| `state_message`             | Message                 | `text`      |     | ✅    |                     |
| `token_id`                  | Payment Token           | `many2one`  |     | ✅    | payment.token       |
| `tokenize`                  | Create Token            | `boolean`   |     | ✅    |                     |
| `write_date`                | Last Updated on         | `datetime`  |     | ✅    |                     |
| `write_uid`                 | Last Updated by         | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                       | Group                  | Perms     |
| -------------------------- | ---------------------- | --------- |
| payment.transaction.user   | Accounting / Invoicing | `R/W/C`   |
| payment.transaction.system | Role / Administrator   | `R/W/C/D` |

**Record Rules:**

- **Access transactions in own companies only** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`
- **Access every payment transaction** (25) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

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

### 🗃️ `delivery.carrier` — Shipping Methods

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                          | Label                                        | Type        | Req | Store | Relation            |
| ------------------------------ | -------------------------------------------- | ----------- | --- | ----- | ------------------- |
| `active`                       | Active                                       | `boolean`   |     | ✅    |                     |
| `allow_cash_on_delivery`       | Cash on Delivery                             | `boolean`   |     | ✅    |                     |
| `amount`                       | Amount                                       | `float`     |     | ✅    |                     |
| `can_generate_return`          | Can Generate Return                          | `boolean`   |     |       |                     |
| `can_publish`                  | Can Publish                                  | `boolean`   |     |       |                     |
| `carrier_description`          | Carrier Description                          | `text`      |     | ✅    |                     |
| `company_id`                   | Company                                      | `many2one`  |     | ✅    | res.company         |
| `country_ids`                  | Countries                                    | `many2many` |     | ✅    | res.country         |
| `create_date`                  | Created on                                   | `datetime`  |     | ✅    |                     |
| `create_uid`                   | Created by                                   | `many2one`  |     | ✅    | res.users           |
| `currency_id`                  | Currency                                     | `many2one`  |     |       | res.currency        |
| `debug_logging`                | Debug logging                                | `boolean`   |     | ✅    |                     |
| `delivery_type`                | Provider                                     | `selection` | ✅  | ✅    |                     |
| `display_name`                 | Display Name                                 | `char`      |     |       |                     |
| `excluded_tag_ids`             | Excluded Tags                                | `many2many` |     | ✅    | product.tag         |
| `fixed_margin`                 | Fixed Margin                                 | `float`     |     | ✅    |                     |
| `fixed_price`                  | Fixed Price                                  | `float`     |     | ✅    |                     |
| `free_over`                    | Free if order amount is above                | `boolean`   |     | ✅    |                     |
| `get_return_label_from_portal` | Return Label Accessible from Customer Portal | `boolean`   |     | ✅    |                     |
| `id`                           | ID                                           | `integer`   |     | ✅    |                     |
| `integration_level`            | Integration Level                            | `selection` |     | ✅    |                     |
| `invoice_policy`               | Invoicing Policy                             | `selection` | ✅  | ✅    |                     |
| `is_published`                 | Is Published                                 | `boolean`   |     | ✅    |                     |
| `margin`                       | Margin                                       | `float`     |     | ✅    |                     |
| `max_volume`                   | Max Volume                                   | `float`     |     | ✅    |                     |
| `max_weight`                   | Max Weight                                   | `float`     |     | ✅    |                     |
| `must_have_tag_ids`            | Must Have Tags                               | `many2many` |     | ✅    | product.tag         |
| `name`                         | Delivery Method                              | `char`      | ✅  | ✅    |                     |
| `price_rule_ids`               | Pricing Rules                                | `one2many`  |     | ✅    | delivery.price.rule |
| `prod_environment`             | Environment                                  | `boolean`   |     | ✅    |                     |
| `product_id`                   | Delivery Product                             | `many2one`  | ✅  | ✅    | product.product     |
| `return_label_on_delivery`     | Generate Return Label                        | `boolean`   |     | ✅    |                     |
| `route_ids`                    | Routes                                       | `many2many` |     | ✅    | stock.route         |
| `sequence`                     | Sequence                                     | `integer`   |     | ✅    |                     |
| `shipping_insurance`           | Insurance Percentage                         | `integer`   |     | ✅    |                     |
| `state_ids`                    | States                                       | `many2many` |     | ✅    | res.country.state   |
| `supports_shipping_insurance`  | Supports Shipping Insurance                  | `boolean`   |     |       |                     |
| `tracking_url`                 | Tracking Link                                | `char`      |     | ✅    |                     |
| `volume_uom_name`              | Volume unit of measure label                 | `char`      |     |       |                     |
| `website_absolute_url`         | Website Absolute URL                         | `char`      |     |       |                     |
| `website_description`          | Description for Online Quotations            | `text`      |     |       |                     |
| `website_id`                   | Website                                      | `many2one`  |     | ✅    | website             |
| `website_published`            | Visible on current website                   | `boolean`   |     |       |                     |
| `website_url`                  | Website URL                                  | `char`      |     |       |                     |
| `weight_uom_name`              | Weight unit of measure label                 | `char`      |     |       |                     |
| `write_date`                   | Last Updated on                              | `datetime`  |     | ✅    |                     |
| `write_uid`                    | Last Updated by                              | `many2one`  |     | ✅    | res.users           |
| `zip_prefix_ids`               | Zip Prefixes                                 | `many2many` |     | ✅    | delivery.zip.prefix |

**Access Rights:**

| Name                             | Group                            | Perms     |
| -------------------------------- | -------------------------------- | --------- |
| delivery.carrier                 | Sales / User: Own Documents Only | `R`       |
| delivery.carrier                 | Sales / Administrator            | `R/W/C/D` |
| delivery.carrier partner_manager | Contact / Creation               | `R`       |
| delivery.carrier stock_user      | Inventory / User                 | `R`       |
| delivery.carrier stock_manager   | Inventory / Administrator        | `R/W/C/D` |
| delivery.carrier                 | Role / Administrator             | `R`       |

**Record Rules:**

- **Delivery Carrier multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
