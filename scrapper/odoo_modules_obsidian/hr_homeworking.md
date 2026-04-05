---
title: "Remote Work"
module: "hr_homeworking"
state: "installed"
version: "19.0.2.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Remote Work"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_______w___]
---

# 🟢 Remote Work

> **Module:** `hr_homeworking` | **Version:** `19.0.2.0` **Category:** Remote Work |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[hr]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT hr.employee.list.timesheet (list)`
- `* INHERIT res.users.form.inherit (form)`
- `* INHERIT res.users.preferences.form.inherit (form)`
- `* INHERIT view.employee.form.inherit.hr (form)`
- `* INHERIT view.employee.form.inherit.hr (search)`

### Reports

_none_

## 🛠️ Technical Documentation

**6 model(s) defined by this module:**

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

### 🗃️ `hr.employee` — Employee

> 📧 Mail Thread

    NB: Any field only available on the model hr.employee (i.e. not on the
    hr.employee.public model) should have `groups="hr.group_hr_user"` on its
    definition to avoid being prefetched when the user hasn't access to the
    hr.employee model. Indeed, the prefetch loads the data for all the fields
    that are available according to the group defined on them.

**Fields:**

| Field                            | Label                           | Type         | Req | Store | Relation                  |
| -------------------------------- | ------------------------------- | ------------ | --- | ----- | ------------------------- |
| `active`                         | Active                          | `boolean`    |     | ✅    |                           |
| `active_employee`                | Active Employee                 | `boolean`    |     |       |                           |
| `activity_calendar_event_id`     | Next Activity Calendar Event    | `many2one`   |     |       | calendar.event            |
| `activity_date_deadline`         | Next Activity Deadline          | `date`       |     |       |                           |
| `activity_exception_decoration`  | Activity Exception Decoration   | `selection`  |     |       |                           |
| `activity_exception_icon`        | Icon                            | `char`       |     |       |                           |
| `activity_ids`                   | Activities                      | `one2many`   |     | ✅    | mail.activity             |
| `activity_state`                 | Activity State                  | `selection`  |     |       |                           |
| `activity_summary`               | Next Activity Summary           | `char`       |     |       |                           |
| `activity_type_icon`             | Activity Type Icon              | `char`       |     |       |                           |
| `activity_type_id`               | Next Activity Type              | `many2one`   |     |       | mail.activity.type        |
| `activity_user_id`               | Responsible User                | `many2one`   |     |       | res.users                 |
| `additional_note`                | Additional Note                 | `text`       |     |       |                           |
| `address_id`                     | Work Address                    | `many2one`   |     |       | res.partner               |
| `allocation_count`               | Total number of days allocated. | `float`      |     |       |                           |
| `allocation_display`             | Allocation Display              | `char`       |     |       |                           |
| `allocation_remaining_display`   | Allocation Remaining Display    | `char`       |     |       |                           |
| `allocations_count`              | Total number of allocations     | `integer`    |     |       |                           |
| `allowed_country_state_ids`      | Allowed Country State           | `many2many`  |     |       | res.country.state         |
| `applicant_ids`                  | Applicants                      | `one2many`   |     | ✅    | hr.applicant              |
| `avatar_1024`                    | Avatar 1024                     | `binary`     |     |       |                           |
| `avatar_128`                     | Avatar 128                      | `binary`     |     |       |                           |
| `avatar_1920`                    | Avatar                          | `binary`     |     |       |                           |
| `avatar_256`                     | Avatar 256                      | `binary`     |     |       |                           |
| `avatar_512`                     | Avatar 512                      | `binary`     |     |       |                           |
| `badge_ids`                      | Employee Badges                 | `one2many`   |     |       | gamification.badge.user   |
| `bank_account_ids`               | Bank Accounts                   | `many2many`  |     | ✅    | res.partner.bank          |
| `barcode`                        | Badge ID                        | `char`       |     | ✅    |                           |
| `birthday`                       | Birthday                        | `date`       |     | ✅    |                           |
| `birthday_public_display`        | Show to all employees           | `boolean`    |     | ✅    |                           |
| `birthday_public_display_string` | Public Date of Birth            | `char`       |     |       |                           |
| `car_ids`                        | Vehicles (private)              | `one2many`   |     | ✅    | fleet.vehicle             |
| `category_ids`                   | Tags                            | `many2many`  |     | ✅    | hr.employee.category      |
| `certificate`                    | Certificate Level               | `selection`  |     | ✅    |                           |
| `certification_ids`              | Certification                   | `one2many`   |     |       | hr.employee.skill         |
| `child_all_count`                | Indirect Subordinates Count     | `integer`    |     |       |                           |
| `child_count`                    | Direct Subordinates Count       | `integer`    |     |       |                           |
| `child_ids`                      | Direct subordinates             | `one2many`   |     | ✅    | hr.employee               |
| `children`                       | Dependent Children              | `integer`    |     |       |                           |
| `coach_id`                       | Coach                           | `many2one`   |     | ✅    | hr.employee               |
| `color`                          | Color Index                     | `integer`    |     | ✅    |                           |
| `company_country_code`           | Company Country Code            | `char`       |     |       |                           |
| `company_country_id`             | Company Country                 | `many2one`   |     |       | res.country               |
| `company_id`                     | Company                         | `many2one`   | ✅  | ✅    | res.company               |
| `contract_date_end`              | Contract End Date               | `date`       |     |       |                           |
| `contract_date_start`            | Contract Start Date             | `date`       |     |       |                           |
| `contract_template_id`           | Contract Template               | `many2one`   |     |       | hr.version                |
| `contract_type_id`               | Contract Type                   | `many2one`   |     |       | hr.contract.type          |
| `contract_wage`                  | Contract Wage                   | `monetary`   |     |       |                           |
| `country_code`                   | Country Code                    | `char`       |     |       |                           |
| `country_id`                     | Nationality (Country)           | `many2one`   |     |       | res.country               |
| `country_of_birth`               | Country of Birth                | `many2one`   |     | ✅    | res.country               |
| `create_date`                    | Created on                      | `datetime`   |     | ✅    |                           |
| `create_uid`                     | Created by                      | `many2one`   |     | ✅    | res.users                 |
| `currency_id`                    | Currency                        | `many2one`   |     |       | res.currency              |
| `current_date_version`           | Current Date Version            | `date`       |     |       |                           |
| `current_employee_skill_ids`     | Current Employee Skill          | `one2many`   |     |       | hr.employee.skill         |
| `current_leave_id`               | Current Time Off Type           | `many2one`   |     |       | hr.leave.type             |
| `current_leave_state`            | Current Time Off Status         | `selection`  |     |       |                           |
| `current_version_id`             | Current Version                 | `many2one`   |     | ✅    | hr.version                |
| `date_end`                       | Date End                        | `date`       |     |       |                           |
| `date_start`                     | Date Start                      | `date`       |     |       |                           |
| `date_version`                   | Date Version                    | `date`       | ✅  |       |                           |
| `department_color`               | Department Color                | `integer`    |     |       |                           |
| `department_id`                  | Department                      | `many2one`   |     |       | hr.department             |
| `departure_date`                 | Departure Date                  | `date`       |     |       |                           |
| `departure_description`          | Additional Information          | `html`       |     |       |                           |
| `departure_reason_id`            | Departure Reason                | `many2one`   |     |       | hr.departure.reason       |
| `direct_badge_ids`               | Direct Badge                    | `one2many`   |     | ✅    | gamification.badge.user   |
| `display_certification_page`     | Display Certification Page      | `boolean`    |     |       |                           |
| `display_name`                   | Display Name                    | `char`       |     |       |                           |
| `distance_home_work`             | Home-Work Distance              | `integer`    |     |       |                           |
| `distance_home_work_unit`        | Home-Work Distance unit         | `selection`  | ✅  |       |                           |
| `driving_license`                | Driving License                 | `binary`     |     | ✅    |                           |
| `email`                          | Email                           | `char`       |     |       |                           |
| `emergency_contact`              | Emergency Contact               | `char`       |     | ✅    |                           |
| `emergency_phone`                | Emergency Phone                 | `char`       |     | ✅    |                           |
| `employee_cars_count`            | Cars                            | `integer`    |     |       |                           |
| `employee_id`                    | Employee                        | `many2one`   |     |       | hr.employee               |
| `employee_properties`            | Properties                      | `properties` |     | ✅    |                           |
| `employee_skill_ids`             | Skills                          | `one2many`   |     | ✅    | hr.employee.skill         |
| `employee_type`                  | Employee Type                   | `selection`  | ✅  |       |                           |
| `exceptional_location_id`        | Current                         | `many2one`   |     |       | hr.work.location          |
| `expense_manager_id`             | Expense Approver                | `many2one`   |     | ✅    | res.users                 |
| `filter_for_expense`             | Filter For Expense              | `boolean`    |     |       |                           |
| `friday_location_id`             | Friday                          | `many2one`   |     | ✅    | hr.work.location          |
| `goal_ids`                       | Employee HR Goals               | `one2many`   |     |       | gamification.goal         |
| `has_badges`                     | Has Badges                      | `boolean`    |     |       |                           |
| `has_message`                    | Has Message                     | `boolean`    |     |       |                           |
| `has_multiple_bank_accounts`     | Has Multiple Bank Accounts      | `boolean`    |     |       |                           |
| `has_work_permit`                | Work Permit                     | `binary`     |     | ✅    |                           |
| `hr_icon_display`                | Hr Icon Display                 | `selection`  |     |       |                           |
| `hr_presence_state`              | Hr Presence State               | `selection`  |     |       |                           |
| `hr_responsible_id`              | HR Responsible                  | `many2one`   | ✅  |       | res.users                 |
| `id`                             | ID                              | `integer`    |     | ✅    |                           |
| `id_card`                        | ID Card Copy                    | `binary`     |     | ✅    |                           |
| `identification_id`              | Identification No               | `char`       |     |       |                           |
| `image_1024`                     | Image 1024                      | `binary`     |     | ✅    |                           |
| `image_128`                      | Image 128                       | `binary`     |     | ✅    |                           |
| `image_1920`                     | Image                           | `binary`     |     | ✅    |                           |
| `image_256`                      | Image 256                       | `binary`     |     | ✅    |                           |
| `image_512`                      | Image 512                       | `binary`     |     | ✅    |                           |
| `im_status`                      | IM Status                       | `char`       |     |       |                           |
| `is_absent`                      | Absent Today                    | `boolean`    |     |       |                           |
| `is_current`                     | Is Current                      | `boolean`    |     |       |                           |
| `is_custom_job_title`            | Is Custom Job Title             | `boolean`    |     |       |                           |
| `is_flexible`                    | Is Flexible                     | `boolean`    |     |       |                           |
| `is_fully_flexible`              | Is Fully Flexible               | `boolean`    |     |       |                           |
| `is_future`                      | Is Future                       | `boolean`    |     |       |                           |
| `is_in_contract`                 | Is In Contract                  | `boolean`    |     |       |                           |
| `is_past`                        | Is Past                         | `boolean`    |     |       |                           |
| `is_subordinate`                 | Is Subordinate                  | `boolean`    |     |       |                           |
| `is_trusted_bank_account`        | Is Trusted Bank Account         | `boolean`    |     |       |                           |
| `is_user_active`                 | User's active                   | `boolean`    |     |       |                           |
| `job_id`                         | Job                             | `many2one`   |     |       | hr.job                    |
| `job_title`                      | Job Title                       | `char`       |     |       |                           |
| `km_home_work`                   | Home-Work Distance in Km        | `integer`    |     |       |                           |
| `lang`                           | Lang                            | `selection`  |     | ✅    |                           |
| `last_activity`                  | Last Activity                   | `date`       |     |       |                           |
| `last_activity_time`             | Last Activity Time              | `char`       |     |       |                           |
| `last_modified_date`             | Last Modified on                | `datetime`   | ✅  |       |                           |
| `last_modified_uid`              | Last Modified by                | `many2one`   | ✅  |       | res.users                 |
| `leave_date_from`                | From Date                       | `date`       |     |       |                           |
| `leave_date_to`                  | To Date                         | `date`       |     |       |                           |
| `leave_manager_id`               | Time Off Approver               | `many2one`   |     | ✅    | res.users                 |
| `legal_name`                     | Legal Name                      | `char`       |     | ✅    |                           |
| `license_plate`                  | License Plate                   | `char`       |     |       |                           |
| `marital`                        | Marital Status                  | `selection`  | ✅  |       |                           |
| `member_of_department`           | Member of department            | `boolean`    |     |       |                           |
| `message_attachment_count`       | Attachment Count                | `integer`    |     |       |                           |
| `message_follower_ids`           | Followers                       | `one2many`   |     | ✅    | mail.followers            |
| `message_has_error`              | Message Delivery error          | `boolean`    |     |       |                           |
| `message_has_error_counter`      | Number of errors                | `integer`    |     |       |                           |
| `message_has_sms_error`          | SMS Delivery error              | `boolean`    |     |       |                           |
| `message_ids`                    | Messages                        | `one2many`   |     | ✅    | mail.message              |
| `message_is_follower`            | Is Follower                     | `boolean`    |     |       |                           |
| `message_main_attachment_id`     | Main Attachment                 | `many2one`   |     | ✅    | ir.attachment             |
| `message_needaction`             | Action Needed                   | `boolean`    |     |       |                           |
| `message_needaction_counter`     | Number of Actions               | `integer`    |     |       |                           |
| `message_partner_ids`            | Followers (Partners)            | `many2many`  |     |       | res.partner               |
| `mobile_phone`                   | Work Mobile                     | `char`       |     | ✅    |                           |
| `mobility_card`                  | Mobility Card                   | `char`       |     | ✅    |                           |
| `monday_location_id`             | Monday                          | `many2one`   |     | ✅    | hr.work.location          |
| `my_activity_date_deadline`      | My Activity Deadline            | `date`       |     |       |                           |
| `name`                           | Employee Name                   | `char`       |     | ✅    |                           |
| `newly_hired`                    | Newly Hired                     | `boolean`    |     |       |                           |
| `parent_id`                      | Manager                         | `many2one`   |     | ✅    | hr.employee               |
| `passport_expiration_date`       | Passport Expiration Date        | `date`       |     |       |                           |
| `passport_id`                    | Passport No                     | `char`       |     |       |                           |
| `permit_no`                      | Work Permit No                  | `char`       |     | ✅    |                           |
| `phone`                          | Phone                           | `char`       |     |       |                           |
| `pin`                            | PIN                             | `char`       |     | ✅    |                           |
| `place_of_birth`                 | Place of Birth                  | `char`       |     | ✅    |                           |
| `primary_bank_account_id`        | Primary Bank Account            | `many2one`   |     |       | res.partner.bank          |
| `private_car_plate`              | Private Car Plate               | `char`       |     | ✅    |                           |
| `private_city`                   | Private City                    | `char`       |     |       |                           |
| `private_country_id`             | Private Country                 | `many2one`   |     |       | res.country               |
| `private_email`                  | Private Email                   | `char`       |     | ✅    |                           |
| `private_phone`                  | Private Phone                   | `char`       |     | ✅    |                           |
| `private_state_id`               | Private State                   | `many2one`   |     |       | res.country.state         |
| `private_street`                 | Private Street                  | `char`       |     |       |                           |
| `private_street2`                | Private Street2                 | `char`       |     |       |                           |
| `private_zip`                    | Private Zip                     | `char`       |     |       |                           |
| `rating_ids`                     | Ratings                         | `one2many`   |     | ✅    | rating.rating             |
| `related_partners_count`         | Related Partners Count          | `integer`    |     |       |                           |
| `resource_calendar_id`           | Default Working Hours           | `many2one`   |     |       | resource.calendar         |
| `resource_id`                    | Resource                        | `many2one`   | ✅  | ✅    | resource.resource         |
| `resume_line_ids`                | Resume lines                    | `one2many`   |     | ✅    | hr.resume.line            |
| `salary_distribution`            | Salary Distribution             | `json`       |     | ✅    |                           |
| `saturday_location_id`           | Saturday                        | `many2one`   |     | ✅    | hr.work.location          |
| `sex`                            | Gender                          | `selection`  |     |       |                           |
| `share`                          | Share User                      | `boolean`    |     |       |                           |
| `show_hr_icon_display`           | Show Hr Icon Display            | `boolean`    |     |       |                           |
| `show_leaves`                    | Able to see Remaining Time Off  | `boolean`    |     |       |                           |
| `skill_ids`                      | Skill                           | `many2many`  |     | ✅    | hr.skill                  |
| `spouse_birthdate`               | Spouse Birthdate                | `date`       |     |       |                           |
| `spouse_complete_name`           | Spouse Legal Name               | `char`       |     |       |                           |
| `ssnid`                          | SSN No                          | `char`       |     |       |                           |
| `structure_type_id`              | Salary Structure Type           | `many2one`   |     |       | hr.payroll.structure.type |
| `study_field`                    | Field of Study                  | `char`       |     | ✅    |                           |
| `study_school`                   | School                          | `char`       |     | ✅    |                           |
| `subordinate_ids`                | Subordinates                    | `one2many`   |     |       | hr.employee               |
| `sunday_location_id`             | Sunday                          | `many2one`   |     | ✅    | hr.work.location          |
| `thursday_location_id`           | Thursday                        | `many2one`   |     | ✅    | hr.work.location          |
| `today_location_name`            | Today Location Name             | `char`       |     | ✅    |                           |
| `trial_date_end`                 | End of Trial Period             | `date`       |     |       |                           |
| `tuesday_location_id`            | Tuesday                         | `many2one`   |     | ✅    | hr.work.location          |
| `tz`                             | Timezone                        | `selection`  |     |       |                           |
| `user_id`                        | User                            | `many2one`   |     | ✅    | res.users                 |
| `user_partner_id`                | User's partner                  | `many2one`   |     |       | res.partner               |
| `version_id`                     | Version                         | `many2one`   | ✅  |       | hr.version                |
| `version_ids`                    | Employee Versions               | `one2many`   | ✅  | ✅    | hr.version                |
| `versions_count`                 | Versions Count                  | `integer`    |     |       |                           |
| `visa_expire`                    | Visa Expiration Date            | `date`       |     | ✅    |                           |
| `visa_no`                        | Visa No                         | `char`       |     | ✅    |                           |
| `wage`                           | Wage                            | `monetary`   |     |       |                           |
| `website_message_ids`            | Website Messages                | `one2many`   |     | ✅    | mail.message              |
| `wednesday_location_id`          | Wednesday                       | `many2one`   |     | ✅    | hr.work.location          |
| `work_contact_id`                | Work Contact                    | `many2one`   |     | ✅    | res.partner               |
| `work_email`                     | Work Email                      | `char`       |     | ✅    |                           |
| `work_location_id`               | Work Location                   | `many2one`   |     |       | hr.work.location          |
| `work_location_name`             | Work Location Name              | `char`       |     |       |                           |
| `work_location_type`             | Work Location Type              | `selection`  |     |       |                           |
| `work_permit_expiration_date`    | Work Permit Expiration Date     | `date`       |     | ✅    |                           |
| `work_permit_name`               | work_permit_name                | `char`       |     |       |                           |
| `work_permit_scheduled_activity` | Work Permit Scheduled Activity  | `boolean`    |     | ✅    |                           |
| `work_phone`                     | Work Phone                      | `char`       |     | ✅    |                           |
| `write_date`                     | Last Updated on                 | `datetime`   |     | ✅    |                           |
| `write_uid`                      | Last Updated by                 | `many2one`   |     | ✅    | res.users                 |

**Access Rights:**

| Name                         | Group                                     | Perms     |
| ---------------------------- | ----------------------------------------- | --------- |
| hr.employee user             | Employees / Officer: Manage all employees | `R/W/C/D` |
| name_hr_employee_back_office | OpenEduCat / Manager                      | `R/W/C`   |
| name_hr_employee_student     | OpenEduCat / Manager                      | `R`       |
| hr.employee system user      | Role / Administrator                      | `R`       |

**Record Rules:**

- **Employee multi company rule** (Global) `R/W/C/D`
  - Domain:
    `['|', '|', '|',         ('company_id', 'in', company_ids + [False]),         ('parent_id.user_id', '=', user.id),         ('id', '=', user.employee_id.parent_id.id),         ('user_id', '=', user.id)     ]`
- **HR multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `hr.employee.location` — Employee Location

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label           | Type        | Req | Store | Relation         |
| -------------------- | --------------- | ----------- | --- | ----- | ---------------- |
| `create_date`        | Created on      | `datetime`  |     | ✅    |                  |
| `create_uid`         | Created by      | `many2one`  |     | ✅    | res.users        |
| `date`               | Date            | `date`      |     | ✅    |                  |
| `day_week_string`    | Day Week String | `char`      |     |       |                  |
| `display_name`       | Display Name    | `char`      |     |       |                  |
| `employee_id`        | Employee        | `many2one`  | ✅  | ✅    | hr.employee      |
| `employee_name`      | Employee Name   | `char`      |     |       |                  |
| `id`                 | ID              | `integer`   |     | ✅    |                  |
| `work_location_id`   | Location        | `many2one`  | ✅  | ✅    | hr.work.location |
| `work_location_name` | Location name   | `char`      |     |       |                  |
| `work_location_type` | Cover Image     | `selection` |     |       |                  |
| `write_date`         | Last Updated on | `datetime`  |     | ✅    |                  |
| `write_uid`          | Last Updated by | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                 | Group                                     | Perms     |
| -------------------- | ----------------------------------------- | --------- |
| hr.employee.location | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.employee.location | Role / User                               | `R/W/C/D` |

**Record Rules:**

- **homeworking: own** (1) `R/W/C/D`
  - Domain: `[             ('employee_id', '=', user.employee_id.id)         ]`
- **homeworking: admin** (49) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `hr.employee.public` — Public Employee

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                          | Type        | Req | Store | Relation                |
| -------------------------------- | ------------------------------ | ----------- | --- | ----- | ----------------------- |
| `active`                         | Active                         | `boolean`   |     | ✅    |                         |
| `address_id`                     | Address                        | `many2one`  |     | ✅    | res.partner             |
| `allocation_display`             | Allocation Display             | `char`      |     |       |                         |
| `allocation_remaining_display`   | Allocation Remaining Display   | `char`      |     |       |                         |
| `avatar_1024`                    | Avatar 1024                    | `binary`    |     |       |                         |
| `avatar_128`                     | Avatar 128                     | `binary`    |     |       |                         |
| `avatar_1920`                    | Avatar                         | `binary`    |     |       |                         |
| `avatar_256`                     | Avatar 256                     | `binary`    |     |       |                         |
| `avatar_512`                     | Avatar 512                     | `binary`    |     |       |                         |
| `badge_ids`                      | Badge                          | `one2many`  |     |       | gamification.badge.user |
| `birthday_public_display_string` | Public Date of Birth           | `char`      |     |       |                         |
| `certification_ids`              | Certification                  | `one2many`  |     |       | hr.employee.skill       |
| `child_all_count`                | Child All Count                | `integer`   |     |       |                         |
| `child_count`                    | Child Count                    | `integer`   |     |       |                         |
| `child_ids`                      | Direct subordinates            | `one2many`  |     | ✅    | hr.employee.public      |
| `coach_id`                       | Coach                          | `many2one`  |     | ✅    | hr.employee.public      |
| `color`                          | Color                          | `integer`   |     | ✅    |                         |
| `company_id`                     | Company                        | `many2one`  |     | ✅    | res.company             |
| `country_code`                   | Country Code                   | `char`      |     |       |                         |
| `create_date`                    | Create Date                    | `datetime`  |     | ✅    |                         |
| `create_uid`                     | Created by                     | `many2one`  |     | ✅    | res.users               |
| `current_employee_skill_ids`     | Current Employee Skill         | `one2many`  |     |       | hr.employee.skill       |
| `department_color`               | Department Color               | `integer`   |     |       |                         |
| `department_id`                  | Department                     | `many2one`  |     | ✅    | hr.department           |
| `display_certification_page`     | Display Certification Page     | `boolean`   |     |       |                         |
| `display_name`                   | Display Name                   | `char`      |     |       |                         |
| `email`                          | Email                          | `char`      |     |       |                         |
| `employee_id`                    | Employee                       | `many2one`  |     | ✅    | hr.employee             |
| `employee_skill_ids`             | Skills                         | `one2many`  |     | ✅    | hr.employee.skill       |
| `expense_manager_id`             | Expense Manager                | `many2one`  |     | ✅    | res.users               |
| `filter_for_expense`             | Filter For Expense             | `boolean`   |     |       |                         |
| `friday_location_id`             | Friday                         | `many2one`  |     | ✅    | hr.work.location        |
| `has_badges`                     | Has Badges                     | `boolean`   |     |       |                         |
| `hr_icon_display`                | Hr Icon Display                | `selection` |     |       |                         |
| `hr_presence_state`              | Hr Presence State              | `selection` |     |       |                         |
| `id`                             | ID                             | `integer`   |     | ✅    |                         |
| `image_1024`                     | Image 1024                     | `binary`    |     |       |                         |
| `image_128`                      | Image 128                      | `binary`    |     |       |                         |
| `image_1920`                     | Image                          | `binary`    |     |       |                         |
| `image_256`                      | Image 256                      | `binary`    |     |       |                         |
| `image_512`                      | Image 512                      | `binary`    |     |       |                         |
| `im_status`                      | IM Status                      | `char`      |     |       |                         |
| `is_absent`                      | Absent Today                   | `boolean`   |     |       |                         |
| `is_manager`                     | Is Manager                     | `boolean`   |     |       |                         |
| `is_subordinate`                 | Is Subordinate                 | `boolean`   |     |       |                         |
| `is_user`                        | Is User                        | `boolean`   |     |       |                         |
| `job_id`                         | Job                            | `many2one`  |     | ✅    | hr.job                  |
| `job_title`                      | Job Title                      | `char`      |     |       |                         |
| `last_activity`                  | Last Activity                  | `date`      |     |       |                         |
| `last_activity_time`             | Last Activity Time             | `char`      |     |       |                         |
| `leave_date_to`                  | To Date                        | `date`      |     |       |                         |
| `leave_manager_id`               | Time Off Approver              | `many2one`  |     | ✅    | res.users               |
| `member_of_department`           | Member Of Department           | `boolean`   |     |       |                         |
| `mobile_phone`                   | Mobile Phone                   | `char`      |     | ✅    |                         |
| `mobility_card`                  | Mobility Card                  | `char`      |     | ✅    |                         |
| `monday_location_id`             | Monday                         | `many2one`  |     | ✅    | hr.work.location        |
| `name`                           | Name                           | `char`      |     | ✅    |                         |
| `newly_hired`                    | Newly Hired                    | `boolean`   |     |       |                         |
| `parent_id`                      | Manager                        | `many2one`  |     | ✅    | hr.employee.public      |
| `phone`                          | Phone                          | `char`      |     |       |                         |
| `resource_calendar_id`           | Resource Calendar              | `many2one`  |     | ✅    | resource.calendar       |
| `resource_id`                    | Resource                       | `many2one`  |     | ✅    | resource.resource       |
| `resume_line_ids`                | Resume lines                   | `one2many`  |     | ✅    | hr.resume.line          |
| `saturday_location_id`           | Saturday                       | `many2one`  |     | ✅    | hr.work.location        |
| `share`                          | Share User                     | `boolean`   |     |       |                         |
| `show_hr_icon_display`           | Show Hr Icon Display           | `boolean`   |     |       |                         |
| `show_leaves`                    | Able to see Remaining Time Off | `boolean`   |     |       |                         |
| `subordinate_ids`                | Subordinates                   | `one2many`  |     |       | hr.employee             |
| `sunday_location_id`             | Sunday                         | `many2one`  |     | ✅    | hr.work.location        |
| `thursday_location_id`           | Thursday                       | `many2one`  |     | ✅    | hr.work.location        |
| `today_location_name`            | Today Location Name            | `char`      |     | ✅    |                         |
| `tuesday_location_id`            | Tuesday                        | `many2one`  |     | ✅    | hr.work.location        |
| `tz`                             | Timezone                       | `selection` |     |       |                         |
| `user_id`                        | User                           | `many2one`  |     | ✅    | res.users               |
| `user_partner_id`                | User's partner                 | `many2one`  |     |       | res.partner             |
| `wednesday_location_id`          | Wednesday                      | `many2one`  |     | ✅    | hr.work.location        |
| `work_contact_id`                | Work Contact                   | `many2one`  |     | ✅    | res.partner             |
| `work_email`                     | Work Email                     | `char`      |     | ✅    |                         |
| `work_location_id`               | Work Location                  | `many2one`  |     | ✅    | hr.work.location        |
| `work_location_name`             | Work Location Name             | `char`      |     |       |                         |
| `work_location_type`             | Work Location Type             | `selection` |     |       |                         |
| `work_phone`                     | Work Phone                     | `char`      |     | ✅    |                         |
| `write_date`                     | Last Updated on                | `datetime`  |     | ✅    |                         |
| `write_uid`                      | Last Updated by                | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name               | Group       | Perms |
| ------------------ | ----------- | ----- |
| hr.employee_public | Role / User | `R`   |

**Record Rules:**

- **Employee multi company rule** (Global) `R/W/C/D`
  - Domain:
    `['|', '|', '|',         ('company_id', 'in', company_ids + [False]),         ('parent_id.user_id', '=', user.id),         ('id', '=', user.employee_id.parent_id.id),         ('user_id', '=', user.id)     ]`

### 🗃️ `res.users` — User

Update of res.users class - add a preference about username for livechat purpose

**Fields:**

| Field                                       | Label                                                 | Type         | Req | Store | Relation                    |
| ------------------------------------------- | ----------------------------------------------------- | ------------ | --- | ----- | --------------------------- |
| `accesses_count`                            | # Access Rights                                       | `integer`    |     |       |                             |
| `access_token`                              | Access Token                                          | `char`       |     | ✅    |                             |
| `account_move_count`                        | Account Move Count                                    | `integer`    |     |       |                             |
| `action_id`                                 | Home Action                                           | `many2one`   |     | ✅    | ir.actions.actions          |
| `active`                                    | Active                                                | `boolean`    |     | ✅    |                             |
| `active_lang_count`                         | Active Lang Count                                     | `integer`    |     |       |                             |
| `active_partner`                            | Partner is Active                                     | `boolean`    |     |       |                             |
| `activity_calendar_event_id`                | Next Activity Calendar Event                          | `many2one`   |     |       | calendar.event              |
| `activity_date_deadline`                    | Next Activity Deadline                                | `date`       |     |       |                             |
| `activity_exception_decoration`             | Activity Exception Decoration                         | `selection`  |     |       |                             |
| `activity_exception_icon`                   | Icon                                                  | `char`       |     |       |                             |
| `activity_ids`                              | Activities                                            | `one2many`   |     |       | mail.activity               |
| `activity_state`                            | Activity State                                        | `selection`  |     |       |                             |
| `activity_summary`                          | Next Activity Summary                                 | `char`       |     |       |                             |
| `activity_type_icon`                        | Activity Type Icon                                    | `char`       |     |       |                             |
| `activity_type_id`                          | Next Activity Type                                    | `many2one`   |     |       | mail.activity.type          |
| `activity_user_id`                          | Responsible User                                      | `many2one`   |     |       | res.users                   |
| `additional_note`                           | Additional Note                                       | `text`       |     |       |                             |
| `all_group_ids`                             | Groups and implied groups                             | `many2many`  |     |       | res.groups                  |
| `api_key_ids`                               | API Keys                                              | `one2many`   |     | ✅    | res.users.apikeys           |
| `applicant_ids`                             | Applicants                                            | `one2many`   |     |       | hr.applicant                |
| `application_count`                         | Applications                                          | `integer`    |     |       |                             |
| `application_statistics`                    | Stats                                                 | `json`       |     |       |                             |
| `auth_passkey_key_ids`                      | Auth Passkey Key                                      | `one2many`   |     | ✅    | auth.passkey.key            |
| `autopost_bills`                            | Auto-post bills                                       | `selection`  | ✅  |       |                             |
| `available_invoice_template_pdf_report_ids` | Available Invoice Template Pdf Report                 | `one2many`   |     |       | ir.actions.report           |
| `available_peppol_eas`                      | Available Peppol Eas                                  | `json`       |     |       |                             |
| `avatar_1024`                               | Avatar 1024                                           | `binary`     |     |       |                             |
| `avatar_128`                                | Avatar 128                                            | `binary`     |     |       |                             |
| `avatar_1920`                               | Avatar                                                | `binary`     |     |       |                             |
| `avatar_256`                                | Avatar 256                                            | `binary`     |     |       |                             |
| `avatar_512`                                | Avatar 512                                            | `binary`     |     |       |                             |
| `badge_ids`                                 | Badges                                                | `one2many`   |     | ✅    | gamification.badge.user     |
| `bank_account_count`                        | Bank                                                  | `integer`    |     |       |                             |
| `bank_account_ids`                          | Bank Accounts                                         | `many2many`  |     |       | res.partner.bank            |
| `bank_ids`                                  | Banks                                                 | `one2many`   |     |       | res.partner.bank            |
| `barcode`                                   | Badge ID                                              | `char`       |     |       |                             |
| `bronze_badge`                              | Bronze badges count                                   | `integer`    |     |       |                             |
| `buyer_id`                                  | Buyer                                                 | `many2one`   |     |       | res.users                   |
| `calendar_default_privacy`                  | Calendar Default Privacy                              | `selection`  |     |       |                             |
| `calendar_last_notif_ack`                   | Last notification marked as read from base Calendar   | `datetime`   |     |       |                             |
| `can_edit_role`                             | Can Edit Role                                         | `boolean`    |     |       |                             |
| `can_publish`                               | Can Publish                                           | `boolean`    |     |       |                             |
| `category_id`                               | Tags                                                  | `many2many`  |     |       | res.partner.category        |
| `category_ids`                              | Employee Tags                                         | `many2many`  |     |       | hr.employee.category        |
| `certifications_company_count`              | Company Certifications Count                          | `integer`    |     |       |                             |
| `certifications_count`                      | Certifications Count                                  | `integer`    |     |       |                             |
| `channel_ids`                               | Channels                                              | `many2many`  |     |       | discuss.channel             |
| `channel_member_ids`                        | Channel Member                                        | `one2many`   |     |       | discuss.channel.member      |
| `chatbot_script_ids`                        | Chatbot Script                                        | `one2many`   |     |       | chatbot.script              |
| `chatter_position`                          | Chatter Position                                      | `selection`  |     | ✅    |                             |
| `child_ids`                                 | Childs                                                | `many2many`  |     | ✅    | res.users                   |
| `city`                                      | City                                                  | `char`       |     |       |                             |
| `client_id`                                 | Client ID                                             | `char`       |     | ✅    |                             |
| `client_secret`                             | Client Secret                                         | `char`       |     | ✅    |                             |
| `code`                                      | Company Code                                          | `char`       |     |       |                             |
| `color`                                     | Color Index                                           | `integer`    |     |       |                             |
| `comment`                                   | Notes                                                 | `html`       |     |       |                             |
| `commercial_company_name`                   | Company Name Entity                                   | `char`       |     |       |                             |
| `commercial_partner_id`                     | Commercial Entity                                     | `many2one`   |     |       | res.partner                 |
| `companies_count`                           | Number of Companies                                   | `integer`    |     |       |                             |
| `company_id`                                | Company                                               | `many2one`   | ✅  | ✅    | res.company                 |
| `company_ids`                               | Companies                                             | `many2many`  |     | ✅    | res.company                 |
| `company_name`                              | Company Name                                          | `char`       |     |       |                             |
| `company_registry`                          | Company ID                                            | `char`       |     |       |                             |
| `company_registry_label`                    | Company ID Label                                      | `char`       |     |       |                             |
| `company_registry_placeholder`              | Company Registry Placeholder                          | `char`       |     |       |                             |
| `company_type`                              | Company Type                                          | `selection`  |     |       |                             |
| `complete_name`                             | Complete Name                                         | `char`       |     |       |                             |
| `contact_address`                           | Complete Address                                      | `char`       |     |       |                             |
| `contact_address_inline`                    | Inlined Complete Address                              | `char`       |     |       |                             |
| `contract_ids`                              | Partner Contracts                                     | `one2many`   |     |       | account.analytic.account    |
| `country_code`                              | Country Code                                          | `char`       |     |       |                             |
| `country_id`                                | Country                                               | `many2one`   |     |       | res.country                 |
| `create_date`                               | Create Date                                           | `datetime`   |     | ✅    |                             |
| `create_employee`                           | Technical field, whether to create an employee        | `boolean`    |     |       |                             |
| `create_employee_id`                        | Technical field, bind user to this employee on create | `many2one`   |     |       | hr.employee                 |
| `create_uid`                                | Created by                                            | `many2one`   |     | ✅    | res.users                   |
| `credit`                                    | Total Receivable                                      | `monetary`   |     |       |                             |
| `credit_limit`                              | Credit Limit                                          | `float`      |     |       |                             |
| `credit_to_invoice`                         | Credit To Invoice                                     | `monetary`   |     |       |                             |
| `crm_team_ids`                              | Sales Teams                                           | `many2many`  |     |       | crm.team                    |
| `crm_team_member_ids`                       | Sales Team Members                                    | `one2many`   |     | ✅    | crm.team.member             |
| `currency_id`                               | Currency                                              | `many2one`   |     |       | res.currency                |
| `customer_rank`                             | Customer Rank                                         | `integer`    |     |       |                             |
| `dark_mode`                                 | Dark Mode                                             | `boolean`    |     | ✅    |                             |
| `days_sales_outstanding`                    | Days Sales Outstanding (DSO)                          | `float`      |     |       |                             |
| `debit`                                     | Total Payable                                         | `monetary`   |     |       |                             |
| `department_count`                          | Number of Departments                                 | `integer`    |     |       |                             |
| `department_ids`                            | Allowed Department                                    | `many2many`  |     | ✅    | op.department               |
| `dept_id`                                   | Department Name                                       | `many2one`   |     | ✅    | op.department               |
| `device_ids`                                | User devices                                          | `one2many`   |     | ✅    | res.device                  |
| `display_invoice_edi_format`                | Display Invoice Edi Format                            | `boolean`    |     |       |                             |
| `display_invoice_template_pdf_report_id`    | Display Invoice Template Pdf Report                   | `boolean`    |     |       |                             |
| `display_name`                              | Display Name                                          | `char`       |     |       |                             |
| `duplicate_bank_partner_ids`                | Duplicate Bank Partner                                | `many2many`  |     |       | res.partner                 |
| `email`                                     | Email                                                 | `char`       |     |       |                             |
| `email_domain_placeholder`                  | Email Domain Placeholder                              | `char`       |     |       |                             |
| `email_formatted`                           | Formatted Email                                       | `char`       |     |       |                             |
| `email_normalized`                          | Normalized Email                                      | `char`       |     |       |                             |
| `emergency_contact`                         | Emergency Contact                                     | `char`       |     |       |                             |
| `emergency_phone`                           | Emergency Phone                                       | `char`       |     |       |                             |
| `employee`                                  | Employee                                              | `boolean`    |     |       |                             |
| `employee_bank_account_ids`                 | Employee's Bank Accounts                              | `many2many`  |     |       | res.partner.bank            |
| `employee_count`                            | Employee Count                                        | `integer`    |     |       |                             |
| `employee_id`                               | Company employee                                      | `many2one`   |     |       | hr.employee                 |
| `employee_ids`                              | Related employee                                      | `one2many`   |     | ✅    | hr.employee                 |
| `employee_resource_calendar_id`             | Employee's Working Hours                              | `many2one`   |     |       | resource.calendar           |
| `employees_count`                           | Employees Count                                       | `integer`    |     |       |                             |
| `esign_initials`                            | Digitial Initials                                     | `binary`     |     | ✅    |                             |
| `esign_signature`                           | Digital Signature                                     | `binary`     |     | ✅    |                             |
| `event_count`                               | # Events                                              | `integer`    |     |       |                             |
| `fiscal_country_codes`                      | Fiscal Country Codes                                  | `char`       |     |       |                             |
| `fiscal_country_group_codes`                | Fiscal Country Group Codes                            | `json`       |     |       |                             |
| `friday_location_id`                        | Fridays                                               | `many2one`   |     |       | hr.work.location            |
| `function`                                  | Job Position                                          | `char`       |     |       |                             |
| `global_location_number`                    | GLN                                                   | `char`       |     |       |                             |
| `goal_ids`                                  | Goal                                                  | `one2many`   |     | ✅    | gamification.goal           |
| `gold_badge`                                | Gold badges count                                     | `integer`    |     |       |                             |
| `grievance_team_id`                         | Grievance Team                                        | `many2one`   |     | ✅    | grievance.team              |
| `group_ids`                                 | Groups                                                | `many2many`  |     | ✅    | res.groups                  |
| `group_on`                                  | Week Day                                              | `selection`  | ✅  |       |                             |
| `group_rfq`                                 | Group RFQ                                             | `selection`  | ✅  |       |                             |
| `groups_count`                              | # Groups                                              | `integer`    |     |       |                             |
| `has_access_livechat`                       | Has access to Livechat                                | `boolean`    |     |       |                             |
| `has_external_mail_server`                  | Has External Mail Server                              | `boolean`    |     |       |                             |
| `has_message`                               | Has Message                                           | `boolean`    |     |       |                             |
| `head_office`                               | Head Office                                           | `char`       |     |       |                             |
| `hr_contact`                                | HR Contact                                            | `char`       |     |       |                             |
| `hr_email`                                  | HR Email                                              | `char`       |     |       |                             |
| `hr_name`                                   | HR Name                                               | `char`       |     |       |                             |
| `id`                                        | ID                                                    | `integer`    |     | ✅    |                             |
| `ignore_abnormal_invoice_amount`            | Ignore Abnormal Invoice Amount                        | `boolean`    |     |       |                             |
| `ignore_abnormal_invoice_date`              | Ignore Abnormal Invoice Date                          | `boolean`    |     |       |                             |
| `image_1024`                                | Image 1024                                            | `binary`     |     |       |                             |
| `image_128`                                 | Image 128                                             | `binary`     |     |       |                             |
| `image_1920`                                | Image                                                 | `binary`     |     |       |                             |
| `image_256`                                 | Image 256                                             | `binary`     |     |       |                             |
| `image_512`                                 | Image 512                                             | `binary`     |     |       |                             |
| `im_status`                                 | IM Status                                             | `char`       |     |       |                             |
| `industry_id`                               | Industry                                              | `many2one`   |     |       | res.partner.industry        |
| `invoice_edi_format`                        | eInvoice format                                       | `selection`  |     |       |                             |
| `invoice_edi_format_store`                  | Invoice Edi Format Store                              | `char`       |     |       |                             |
| `invoice_ids`                               | Invoices                                              | `one2many`   |     |       | account.move                |
| `invoice_sending_method`                    | Invoice sending                                       | `selection`  |     |       |                             |
| `invoice_template_pdf_report_id`            | Invoice report                                        | `many2one`   |     |       | ir.actions.report           |
| `is_blacklisted`                            | Blacklist                                             | `boolean`    |     |       |                             |
| `is_company`                                | Is a Company                                          | `boolean`    |     |       |                             |
| `is_hr_user`                                | Is Hr User                                            | `boolean`    |     |       |                             |
| `is_in_call`                                | Is in call                                            | `boolean`    |     |       |                             |
| `is_out_of_office`                          | Out of Office                                         | `boolean`    |     |       |                             |
| `is_parent`                                 | Is a Parent                                           | `boolean`    |     |       |                             |
| `is_peppol_edi_format`                      | Is Peppol Edi Format                                  | `boolean`    |     |       |                             |
| `is_pickup_location`                        | Is Pickup Location                                    | `boolean`    |     |       |                             |
| `is_public`                                 | Is Public                                             | `boolean`    |     |       |                             |
| `is_published`                              | Is Published                                          | `boolean`    |     |       |                             |
| `is_seo_optimized`                          | SEO optimized                                         | `boolean`    |     |       |                             |
| `is_student`                                | Is a Student                                          | `boolean`    |     |       |                             |
| `is_system`                                 | Is System                                             | `boolean`    |     |       |                             |
| `is_ubl_format`                             | Is Ubl Format                                         | `boolean`    |     |       |                             |
| `is_venue`                                  | Venue                                                 | `boolean`    |     |       |                             |
| `job_title`                                 | Job Title                                             | `char`       |     |       |                             |
| `karma`                                     | Karma                                                 | `integer`    |     | ✅    |                             |
| `karma_tracking_ids`                        | Karma Changes                                         | `one2many`   |     | ✅    | gamification.karma.tracking |
| `km_home_work`                              | Home-Work Distance in Km                              | `integer`    |     |       |                             |
| `lang`                                      | Language                                              | `selection`  |     |       |                             |
| `leave_date_to`                             | To Date                                               | `date`       |     |       |                             |
| `livechat_channel_count`                    | Livechat Channel Count                                | `integer`    |     |       |                             |
| `livechat_channel_ids`                      | Livechat Channel                                      | `many2many`  |     | ✅    | im_livechat.channel         |
| `livechat_expertise_ids`                    | Live Chat Expertise                                   | `many2many`  |     |       | im_livechat.expertise       |
| `livechat_is_in_call`                       | Livechat Is In Call                                   | `boolean`    |     |       |                             |
| `livechat_lang_ids`                         | Livechat Languages                                    | `many2many`  |     |       | res.lang                    |
| `livechat_ongoing_session_count`            | Number of Ongoing sessions                            | `integer`    |     |       |                             |
| `livechat_username`                         | Livechat Username                                     | `char`       |     |       |                             |
| `log_ids`                                   | User log entries                                      | `one2many`   |     | ✅    | res.users.log               |
| `login`                                     | Login                                                 | `char`       | ✅  | ✅    |                             |
| `login_date`                                | Latest Login                                          | `datetime`   |     |       |                             |
| `logo_visible`                              | Show Company Logo in Sidebar                          | `boolean`    |     | ✅    |                             |
| `main_user_id`                              | Main User                                             | `many2one`   |     |       | res.users                   |
| `manual_im_status`                          | IM status manually set by the user                    | `selection`  |     | ✅    |                             |
| `meeting_count`                             | # Meetings                                            | `integer`    |     |       |                             |
| `meeting_ids`                               | Meetings                                              | `many2many`  |     |       | calendar.event              |
| `message_attachment_count`                  | Attachment Count                                      | `integer`    |     |       |                             |
| `message_bounce`                            | Bounce                                                | `integer`    |     |       |                             |
| `message_follower_ids`                      | Followers                                             | `one2many`   |     |       | mail.followers              |
| `message_has_error`                         | Message Delivery error                                | `boolean`    |     |       |                             |
| `message_has_error_counter`                 | Number of errors                                      | `integer`    |     |       |                             |
| `message_has_sms_error`                     | SMS Delivery error                                    | `boolean`    |     |       |                             |
| `message_ids`                               | Messages                                              | `one2many`   |     |       | mail.message                |
| `message_is_follower`                       | Is Follower                                           | `boolean`    |     |       |                             |
| `message_needaction`                        | Action Needed                                         | `boolean`    |     |       |                             |
| `message_needaction_counter`                | Number of Actions                                     | `integer`    |     |       |                             |
| `message_partner_ids`                       | Followers (Partners)                                  | `many2many`  |     |       | res.partner                 |
| `mobile_phone`                              | Work Mobile                                           | `char`       |     |       |                             |
| `monday_location_id`                        | Mondays                                               | `many2one`   |     |       | hr.work.location            |
| `my_activity_date_deadline`                 | My Activity Deadline                                  | `date`       |     |       |                             |
| `name`                                      | Name                                                  | `char`       |     |       |                             |
| `new_password`                              | Set Password                                          | `char`       |     |       |                             |
| `next_rank_id`                              | Next Rank                                             | `many2one`   |     | ✅    | gamification.karma.rank     |
| `notification_type`                         | Notification                                          | `selection`  | ✅  | ✅    |                             |
| `odoobot_failed`                            | Odoobot Failed                                        | `boolean`    |     | ✅    |                             |
| `odoobot_state`                             | OdooBot Status                                        | `selection`  |     | ✅    |                             |
| `offline_since`                             | Offline since                                         | `datetime`   |     |       |                             |
| `onesignal_device_id`                       | One Signal Device ID                                  | `char`       |     | ✅    |                             |
| `on_time_rate`                              | On-Time Delivery Rate                                 | `float`      |     |       |                             |
| `opportunity_count`                         | Opportunity Count                                     | `integer`    |     |       |                             |
| `opportunity_ids`                           | Opportunities                                         | `one2many`   |     |       | crm.lead                    |
| `outgoing_mail_server_id`                   | Outgoing Mail Server                                  | `many2one`   |     |       | ir.mail_server              |
| `outgoing_mail_server_type`                 | Outgoing Mail Server Type                             | `selection`  | ✅  |       |                             |
| `out_of_office_from`                        | Out Of Office From                                    | `datetime`   |     | ✅    |                             |
| `out_of_office_message`                     | Vacation Responder                                    | `html`       |     | ✅    |                             |
| `out_of_office_to`                          | Out Of Office To                                      | `datetime`   |     | ✅    |                             |
| `parent_id`                                 | Related Company                                       | `many2one`   |     |       | res.partner                 |
| `parent_name`                               | Parent name                                           | `char`       |     |       |                             |
| `partner_company_registry_placeholder`      | Partner Company Registry Placeholder                  | `char`       |     |       |                             |
| `partner_id`                                | Related Partner                                       | `many2one`   | ✅  | ✅    | res.partner                 |
| `partner_latitude`                          | Geo Latitude                                          | `float`      |     |       |                             |
| `partner_longitude`                         | Geo Longitude                                         | `float`      |     |       |                             |
| `partner_share`                             | Share Partner                                         | `boolean`    |     |       |                             |
| `partner_vat_placeholder`                   | Partner Vat Placeholder                               | `char`       |     |       |                             |
| `password`                                  | Password                                              | `char`       |     |       |                             |
| `payment_token_count`                       | Payment Token Count                                   | `integer`    |     |       |                             |
| `payment_token_ids`                         | Payment Tokens                                        | `one2many`   |     |       | payment.token               |
| `peppol_eas`                                | Peppol e-address (EAS)                                | `selection`  |     |       |                             |
| `peppol_endpoint`                           | Peppol Endpoint                                       | `char`       |     |       |                             |
| `phone`                                     | Phone                                                 | `char`       |     |       |                             |
| `phone_blacklisted`                         | Blacklisted Phone is Phone                            | `boolean`    |     |       |                             |
| `phone_mobile_search`                       | Phone Number                                          | `char`       |     |       |                             |
| `phone_sanitized`                           | Sanitized Number                                      | `char`       |     |       |                             |
| `phone_sanitized_blacklisted`               | Phone Blacklisted                                     | `boolean`    |     |       |                             |
| `picking_warn_msg`                          | Message for Stock Picking                             | `text`       |     |       |                             |
| `pin`                                       | PIN                                                   | `char`       |     |       |                             |
| `pin_whatsapp_contact_id`                   | Pin Whatsapp Contact                                  | `char`       |     | ✅    |                             |
| `placement_team_id`                         | Placement Team Members                                | `many2one`   |     | ✅    | op.placement.cell           |
| `presence_ids`                              | Presence                                              | `one2many`   |     | ✅    | mail.presence               |
| `private_city`                              | Private City                                          | `char`       |     |       |                             |
| `private_country_id`                        | Private Country                                       | `many2one`   |     |       | res.country                 |
| `private_email`                             | Private Email                                         | `char`       |     |       |                             |
| `private_phone`                             | Private Phone                                         | `char`       |     |       |                             |
| `private_state_id`                          | Private State                                         | `many2one`   |     |       | res.country.state           |
| `private_street`                            | Private Street                                        | `char`       |     |       |                             |
| `private_street2`                           | Private Street2                                       | `char`       |     |       |                             |
| `private_zip`                               | Private Zip                                           | `char`       |     |       |                             |
| `properties`                                | Properties                                            | `properties` |     |       |                             |
| `properties_base_definition_id`             | Properties Base Definition                            | `many2one`   |     |       | properties.base.definition  |
| `property_account_payable_id`               | Account Payable                                       | `many2one`   |     |       | account.account             |
| `property_account_position_id`              | Fiscal Position                                       | `many2one`   |     |       | account.fiscal.position     |
| `property_account_receivable_id`            | Account Receivable                                    | `many2one`   |     |       | account.account             |
| `property_delivery_carrier_id`              | Delivery Method                                       | `many2one`   |     |       | delivery.carrier            |
| `property_inbound_payment_method_line_id`   | Property Inbound Payment Method Line                  | `many2one`   |     |       | account.payment.method.line |
| `property_outbound_payment_method_line_id`  | Property Outbound Payment Method Line                 | `many2one`   |     |       | account.payment.method.line |
| `property_payment_term_id`                  | Customer Payment Terms                                | `many2one`   |     |       | account.payment.term        |
| `property_product_pricelist`                | Pricelist                                             | `many2one`   |     |       | product.pricelist           |
| `property_purchase_currency_id`             | Supplier Currency                                     | `many2one`   |     |       | res.currency                |
| `property_stock_customer`                   | Customer Location                                     | `many2one`   |     |       | stock.location              |
| `property_stock_supplier`                   | Vendor Location                                       | `many2one`   |     |       | stock.location              |
| `property_supplier_payment_term_id`         | Vendor Payment Terms                                  | `many2one`   |     |       | account.payment.term        |
| `property_warehouse_id`                     | Default Warehouse                                     | `many2one`   |     | ✅    | stock.warehouse             |
| `purchase_line_ids`                         | Purchase Lines                                        | `one2many`   |     |       | purchase.order.line         |
| `purchase_order_count`                      | Purchase Order Count                                  | `integer`    |     |       |                             |
| `purchase_warn_msg`                         | Message for Purchase Order                            | `text`       |     |       |                             |
| `rank_id`                                   | Rank                                                  | `many2one`   |     | ✅    | gamification.karma.rank     |
| `rating_ids`                                | Ratings                                               | `one2many`   |     |       | rating.rating               |
| `receipt_reminder_email`                    | Receipt Reminder                                      | `boolean`    |     |       |                             |
| `ref`                                       | Reference                                             | `char`       |     |       |                             |
| `ref_company_ids`                           | Companies that refers to partner                      | `one2many`   |     |       | res.company                 |
| `refresh_token`                             | Refresh Token                                         | `char`       |     | ✅    |                             |
| `reminder_date_before_receipt`              | Days Before Receipt                                   | `integer`    |     |       |                             |
| `resource_calendar_id`                      | Default Working Hours                                 | `many2one`   |     |       | resource.calendar           |
| `resource_ids`                              | Resources                                             | `one2many`   |     | ✅    | resource.resource           |
| `res_users_settings_id`                     | Settings                                              | `many2one`   |     |       | res.users.settings          |
| `res_users_settings_ids`                    | Res Users Settings                                    | `one2many`   |     | ✅    | res.users.settings          |
| `role`                                      | Role                                                  | `selection`  |     |       |                             |
| `role_ids`                                  | User Roles                                            | `many2many`  |     | ✅    | res.role                    |
| `role_line_ids`                             | Role lines                                            | `one2many`   |     | ✅    | res.users.role.line         |
| `rtc_session_ids`                           | Rtc Session                                           | `one2many`   |     |       | discuss.channel.rtc.session |
| `rules_count`                               | # Record Rules                                        | `integer`    |     |       |                             |
| `sale_order_count`                          | Sale Order Count                                      | `integer`    |     |       |                             |
| `sale_order_ids`                            | Sales Order                                           | `one2many`   |     |       | sale.order                  |
| `sale_team_id`                              | User Sales Team                                       | `many2one`   |     | ✅    | crm.team                    |
| `sale_warn_msg`                             | Message for Sales Order                               | `text`       |     |       |                             |
| `same_company_registry_partner_id`          | Partner with same Company Registry                    | `many2one`   |     |       | res.partner                 |
| `same_vat_partner_id`                       | Partner with same Tax ID                              | `many2one`   |     |       | res.partner                 |
| `saturday_location_id`                      | Saturdays                                             | `many2one`   |     |       | hr.work.location            |
| `self`                                      | Self                                                  | `many2one`   |     |       | res.partner                 |
| `seo_name`                                  | Seo name                                              | `char`       |     |       |                             |
| `share`                                     | Share User                                            | `boolean`    |     | ✅    |                             |
| `show_alert`                                | Show Alert                                            | `boolean`    |     |       |                             |
| `show_credit_limit`                         | Show Credit Limit                                     | `boolean`    |     |       |                             |
| `signature`                                 | Email Signature                                       | `html`       |     | ✅    |                             |
| `signup_type`                               | Signup Token Type                                     | `char`       |     |       |                             |
| `silver_badge`                              | Silver badges count                                   | `integer`    |     |       |                             |
| `specific_property_product_pricelist`       | Specific Property Product Pricelist                   | `many2one`   |     |       | product.pricelist           |
| `state`                                     | Status                                                | `selection`  |     |       |                             |
| `state_id`                                  | State                                                 | `many2one`   |     |       | res.country.state           |
| `static_map_url`                            | Static Map Url                                        | `char`       |     |       |                             |
| `static_map_url_is_valid`                   | Static Map Url Is Valid                               | `boolean`    |     |       |                             |
| `street`                                    | Street                                                | `char`       |     |       |                             |
| `street2`                                   | Street2                                               | `char`       |     |       |                             |
| `student_line`                              | Line                                                  | `many2one`   |     | ✅    | op.student                  |
| `suggest_based_on`                          | Suggest Based On                                      | `char`       |     |       |                             |
| `suggest_days`                              | Suggest Days                                          | `integer`    |     |       |                             |
| `suggest_percent`                           | Suggest Percent                                       | `integer`    |     |       |                             |
| `sunday_location_id`                        | Sundays                                               | `many2one`   |     |       | hr.work.location            |
| `supplier_invoice_count`                    | # Vendor Bills                                        | `integer`    |     |       |                             |
| `supplier_rank`                             | Supplier Rank                                         | `integer`    |     |       |                             |
| `thursday_location_id`                      | Thursdays                                             | `many2one`   |     |       | hr.work.location            |
| `ticket_count`                              | Ticket Count                                          | `integer`    |     |       |                             |
| `title`                                     | Title                                                 | `many2one`   |     |       | res.partner.title           |
| `total_invoiced`                            | Total Invoiced                                        | `monetary`   |     |       |                             |
| `totp_enabled`                              | Two-factor authentication                             | `boolean`    |     |       |                             |
| `totp_last_counter`                         | Totp Last Counter                                     | `integer`    |     | ✅    |                             |
| `totp_secret`                               | Totp Secret                                           | `char`       |     |       |                             |
| `totp_trusted_device_ids`                   | Trusted Devices                                       | `one2many`   |     | ✅    | auth_totp.device            |
| `tour_enabled`                              | Onboarding                                            | `boolean`    |     | ✅    |                             |
| `trust`                                     | Degree of trust you have in this debtor               | `selection`  |     |       |                             |
| `tuesday_location_id`                       | Tuesdays                                              | `many2one`   |     |       | hr.work.location            |
| `type`                                      | Address Type                                          | `selection`  |     |       |                             |
| `type_address_label`                        | Address Type Description                              | `char`       |     |       |                             |
| `tz`                                        | Timezone                                              | `selection`  |     |       |                             |
| `tz_offset`                                 | Timezone offset                                       | `char`       |     |       |                             |
| `use_partner_credit_limit`                  | Partner Limit                                         | `boolean`    |     |       |                             |
| `user_id`                                   | Salesperson                                           | `many2one`   |     |       | res.users                   |
| `user_ids`                                  | Users                                                 | `one2many`   |     |       | res.users                   |
| `user_line`                                 | User Line                                             | `one2many`   |     | ✅    | op.student                  |
| `user_livechat_username`                    | User Livechat Username                                | `char`       |     |       |                             |
| `vat`                                       | Tax ID                                                | `char`       |     |       |                             |
| `vat_label`                                 | Tax ID Label                                          | `char`       |     |       |                             |
| `view_group_hierarchy`                      | Technical field for user group setting                | `json`       |     |       |                             |
| `visa_expire`                               | Visa Expiration Date                                  | `date`       |     |       |                             |
| `visitor_ids`                               | Visitors                                              | `one2many`   |     |       | website.visitor             |
| `website`                                   | Website Link                                          | `char`       |     |       |                             |
| `website_absolute_url`                      | Website Absolute URL                                  | `char`       |     |       |                             |
| `website_description`                       | Website Partner Full Description                      | `html`       |     |       |                             |
| `website_id`                                | Website                                               | `many2one`   |     | ✅    | website                     |
| `website_message_ids`                       | Website Messages                                      | `one2many`   |     |       | mail.message                |
| `website_meta_description`                  | Website meta description                              | `text`       |     |       |                             |
| `website_meta_keywords`                     | Website meta keywords                                 | `char`       |     |       |                             |
| `website_meta_og_img`                       | Website opengraph image                               | `char`       |     |       |                             |
| `website_meta_title`                        | Website meta title                                    | `char`       |     |       |                             |
| `website_published`                         | Visible on current website                            | `boolean`    |     |       |                             |
| `website_short_description`                 | Website Partner Short Description                     | `text`       |     |       |                             |
| `website_url`                               | Website URL                                           | `char`       |     |       |                             |
| `wednesday_location_id`                     | Wednesdays                                            | `many2one`   |     |       | hr.work.location            |
| `wishlist_ids`                              | Wishlist                                              | `one2many`   |     |       | product.wishlist            |
| `work_contact_id`                           | Work Contact                                          | `many2one`   |     |       | res.partner                 |
| `work_email`                                | Work Email                                            | `char`       |     |       |                             |
| `work_location_id`                          | Work Location                                         | `many2one`   |     |       | hr.work.location            |
| `work_location_name`                        | Work Location Name                                    | `char`       |     |       |                             |
| `work_location_type`                        | Work Location Type                                    | `selection`  |     |       |                             |
| `work_phone`                                | Work Phone                                            | `char`       |     |       |                             |
| `write_date`                                | Last Updated on                                       | `datetime`   |     | ✅    |                             |
| `write_uid`                                 | Last Updated by                                       | `many2one`   |     | ✅    | res.users                   |
| `zip`                                       | Zip                                                   | `char`       |     |       |                             |

**Access Rights:**

| Name                             | Group            | Perms     |
| -------------------------------- | ---------------- | --------- |
| access_op_placement_cell_res     | Placement / User | `R/W/C`   |
| name_res_users_back_office_admin | Parent / Manager | `R/W/C/D` |
| res_users group_erp_manager      | Access Rights    | `R/W/C/D` |
| res_users all                    | Role / Portal    | `R`       |
| res_users all                    | Role / Public    | `R`       |
| res_users all                    | Role / User      | `R`       |

**Record Rules:**

- **user rule** (Global) `R/W/C/D`
  - Domain: `['|', ('share', '=', False), ('company_ids', 'in', company_ids)]`
- **portal user access** (10) `R/W/C/D`
  - Domain: `[('commercial_partner_id', '=', user.commercial_partner_id.id)]`

### 🗃️ `hr.work.location` — Work Location

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label           | Type        | Req | Store | Relation    |
| ----------------- | --------------- | ----------- | --- | ----- | ----------- |
| `active`          | Active          | `boolean`   |     | ✅    |             |
| `address_id`      | Work Address    | `many2one`  | ✅  | ✅    | res.partner |
| `company_id`      | Company         | `many2one`  | ✅  | ✅    | res.company |
| `create_date`     | Created on      | `datetime`  |     | ✅    |             |
| `create_uid`      | Created by      | `many2one`  |     | ✅    | res.users   |
| `display_name`    | Display Name    | `char`      |     |       |             |
| `id`              | ID              | `integer`   |     | ✅    |             |
| `location_number` | Location Number | `char`      |     | ✅    |             |
| `location_type`   | Cover Image     | `selection` | ✅  | ✅    |             |
| `name`            | Work Location   | `char`      | ✅  | ✅    |             |
| `write_date`      | Last Updated on | `datetime`  |     | ✅    |             |
| `write_uid`       | Last Updated by | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                            | Group                     | Perms     |
| ------------------------------- | ------------------------- | --------- |
| access_hr_work_location_manager | Employees / Administrator | `R/W/C/D` |
| access_hr_work_location_user    | Role / User               | `R`       |
