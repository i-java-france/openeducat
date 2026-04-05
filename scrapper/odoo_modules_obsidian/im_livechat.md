---
title: "Live Chat"
module: "im_livechat"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/app/live-chat"
license: "LGPL-3"
category: "Live Chat"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________, odoo/app]
---

# 🟢 Live Chat

> **Module:** `im_livechat` | **Version:** `19.0.1.0` **Category:** Live Chat |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:**
> https://www.odoo.com/app/live-chat

## 🔗 Dependencies

[[mail]] [[rating]] [[digest]] [[utm]]

## 📖 Description

# Live Chat Support

Allow to drop instant messaging widgets on any web page that will communicate with the
current server and dispatch visitors request amongst several live chat operators. Help
your customers with this chat, and analyse their feedback.

## 🖥️ UI Components

### Menus

- `Live Chat`
- `Live Chat/Channels`
- `Live Chat/Configuration`
- `Live Chat/Configuration/Canned Responses`
- `Live Chat/Configuration/Chatbots`
- `Live Chat/Configuration/Expertise`
- `Live Chat/Configuration/Tags`
- `Live Chat/Reporting`
- `Live Chat/Reporting/Agents`
- `Live Chat/Reporting/Sessions`
- `Live Chat/Sessions`
- `Live Chat/Sessions/All Conversations`
- `Live Chat/Sessions/Looking for Help`
- `Live Chat/Technical`
- `Live Chat/Technical/Member History`

### Views

- `* INHERIT im.livechat.digest.digest.view.form.inherit (form)`
- `* INHERIT res.partner.view.buttons (form)`
- `* INHERIT res.users.form.im_livechat (form)`
- `* INHERIT res.users.preferences.form.im_livechat (form)`
- `Livechat : Javascript appending the livechat button (qweb)`
- `Livechat : Support Page (qweb)`
- `Livechat : external_script field of livechat channel (qweb)`
- `chatbot.script.answer.view.form (form)`
- `chatbot.script.answer.view.list (list)`
- `chatbot.script.step.view.form (form)`
- `chatbot.script.step.view.list (list)`
- `chatbot.script.view.form (form)`
- `chatbot.script.view.list (list)`
- `chatbot.script.view.search (search)`
- `chatbot_test_script_page (qweb)`
- `discuss.channel.form (form)`
- `discuss.channel.graph (graph)`
- `discuss.channel.kanban (kanban)`
- `discuss.channel.kanban (kanban)`
- `discuss.channel.list (list)`
- `discuss.channel.looking.for.help.list (list)`
- `discuss.channel.looking.for.help.view.search (search)`
- `discuss.channel.pivot (pivot)`
- `discuss.channel.search (search)`
- `im.livechat.channel.conversation.tag.form (form)`
- `im.livechat.channel.conversation.tag.list (list)`
- `im.livechat.channel.rule.list (list)`
- `im.livechat.channel.view.search (search)`
- `im.livechat.expertise.form (form)`
- `im.livechat.expertise.list (list)`
- `im_livechat.agent.history.graph (graph)`
- `im_livechat.agent.history.pivot (pivot)`
- `im_livechat.agent.history.search (search)`
- `im_livechat.channel.form (form)`
- `im_livechat.channel.kanban (kanban)`
- `im_livechat.channel.member.history.view.list (list)`
- `im_livechat.channel.member.history.view.search (search)`
- `im_livechat.channel.rule.form (form)`
- `im_livechat.channel.rule.kanban (kanban)`
- `im_livechat.report.channel.form (form)`
- `im_livechat.report.channel.graph (graph)`
- `im_livechat.report.channel.list (list)`
- `im_livechat.report.channel.pivot (pivot)`
- `im_livechat.report.channel.search (search)`
- `im_livechat.unit_embed_suite (qweb)`
- `livechat_email_template (qweb)`
- `report_livechat_conversation (qweb)`

### Reports

- `Live Chat Conversation`

## 🛠️ Technical Documentation

**23 model(s) defined by this module:**

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

### 🗃️ `discuss.channel` — Discussion Channel

> 📧 Mail Thread

Chat Session Reprensenting a conversation between users. It extends the base method for
anonymous usage.

**Fields:**

| Field                                    | Label                                                                                       | Type        | Req | Store | Relation                           |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- | ----------- | --- | ----- | ---------------------------------- |
| `active`                                 | Active                                                                                      | `boolean`   |     | ✅    |                                    |
| `avatar_128`                             | Avatar                                                                                      | `binary`    |     |       |                                    |
| `avatar_cache_key`                       | Avatar Cache Key                                                                            | `char`      |     |       |                                    |
| `calendar_event_ids`                     | Calendar Event                                                                              | `one2many`  |     | ✅    | calendar.event                     |
| `call_history_ids`                       | Call History                                                                                | `one2many`  |     | ✅    | discuss.call.history               |
| `channel_member_ids`                     | Members                                                                                     | `one2many`  |     | ✅    | discuss.channel.member             |
| `channel_name_member_ids`                | Channel Name Member                                                                         | `one2many`  |     |       | discuss.channel.member             |
| `channel_partner_ids`                    | Partners                                                                                    | `many2many` |     |       | res.partner                        |
| `channel_type`                           | Channel Type                                                                                | `selection` | ✅  | ✅    |                                    |
| `chatbot_current_step_id`                | Chatbot Current Step                                                                        | `many2one`  |     | ✅    | chatbot.script.step                |
| `chatbot_message_ids`                    | Chatbot Messages                                                                            | `one2many`  |     | ✅    | chatbot.message                    |
| `country_id`                             | Country                                                                                     | `many2one`  |     | ✅    | res.country                        |
| `create_date`                            | Created on                                                                                  | `datetime`  |     | ✅    |                                    |
| `create_uid`                             | Created by                                                                                  | `many2one`  |     | ✅    | res.users                          |
| `default_display_mode`                   | Default Display Mode                                                                        | `selection` |     | ✅    |                                    |
| `description`                            | Description                                                                                 | `text`      |     | ✅    |                                    |
| `display_name`                           | Display Name                                                                                | `char`      |     |       |                                    |
| `duration`                               | Duration                                                                                    | `float`     |     |       |                                    |
| `faculty_id`                             | Faculty                                                                                     | `many2one`  |     | ✅    | op.faculty                         |
| `from_message_id`                        | From Message                                                                                | `many2one`  |     | ✅    | mail.message                       |
| `group_ids`                              | Auto Subscription                                                                           | `many2many` |     | ✅    | res.groups                         |
| `group_public_id`                        | Authorized Group                                                                            | `many2one`  |     | ✅    | res.groups                         |
| `has_crm_lead`                           | Has Crm Lead                                                                                | `boolean`   |     | ✅    |                                    |
| `has_message`                            | Has Message                                                                                 | `boolean`   |     |       |                                    |
| `id`                                     | ID                                                                                          | `integer`   |     | ✅    |                                    |
| `image_128`                              | Image                                                                                       | `binary`    |     | ✅    |                                    |
| `invitation_url`                         | Invitation URL                                                                              | `char`      |     |       |                                    |
| `invited_member_ids`                     | Invited Member                                                                              | `one2many`  |     |       | discuss.channel.member             |
| `is_created_student`                     | Is Created Student                                                                          | `boolean`   |     | ✅    |                                    |
| `is_editable`                            | Is Editable                                                                                 | `boolean`   |     |       |                                    |
| `is_member`                              | Is Member                                                                                   | `boolean`   |     |       |                                    |
| `is_pending_chat_request`                | When created from an operator, whether the channel is yet to be opened on the visitor side. | `boolean`   |     | ✅    |                                    |
| `last_interest_dt`                       | Last Interest                                                                               | `datetime`  |     | ✅    |                                    |
| `lead_ids`                               | Leads                                                                                       | `one2many`  |     | ✅    | crm.lead                           |
| `livechat_agent_history_ids`             | Agents (History)                                                                            | `one2many`  |     |       | im_livechat.channel.member.history |
| `livechat_agent_partner_ids`             | Agents                                                                                      | `many2many` |     | ✅    | res.partner                        |
| `livechat_agent_providing_help_history`  | Help Provided (Agent)                                                                       | `many2one`  |     | ✅    | im_livechat.channel.member.history |
| `livechat_agent_requesting_help_history` | Help Requested (Agent)                                                                      | `many2one`  |     | ✅    | im_livechat.channel.member.history |
| `livechat_bot_history_ids`               | Bots (History)                                                                              | `one2many`  |     |       | im_livechat.channel.member.history |
| `livechat_bot_partner_ids`               | Bots                                                                                        | `many2many` |     | ✅    | res.partner                        |
| `livechat_channel_id`                    | Channel                                                                                     | `many2one`  |     | ✅    | im_livechat.channel                |
| `livechat_channel_member_history_ids`    | Livechat Channel Member History                                                             | `one2many`  |     | ✅    | im_livechat.channel.member.history |
| `livechat_conversation_tag_ids`          | Live Chat Conversation Tags                                                                 | `many2many` |     | ✅    | im_livechat.conversation.tag       |
| `livechat_customer_guest_ids`            | Customers (Guests)                                                                          | `many2many` |     |       | mail.guest                         |
| `livechat_customer_history_ids`          | Customers (History)                                                                         | `one2many`  |     |       | im_livechat.channel.member.history |
| `livechat_customer_partner_ids`          | Customers (Partners)                                                                        | `many2many` |     | ✅    | res.partner                        |
| `livechat_end_dt`                        | Session end date                                                                            | `datetime`  |     | ✅    |                                    |
| `livechat_expertise_ids`                 | Livechat Expertise                                                                          | `many2many` |     | ✅    | im_livechat.expertise              |
| `livechat_failure`                       | Live Chat Session Failure                                                                   | `selection` |     | ✅    |                                    |
| `livechat_is_escalated`                  | Is session escalated                                                                        | `boolean`   |     | ✅    |                                    |
| `livechat_lang_id`                       | Language                                                                                    | `many2one`  |     | ✅    | res.lang                           |
| `livechat_matches_self_expertise`        | Livechat Matches Self Expertise                                                             | `boolean`   |     |       |                                    |
| `livechat_matches_self_lang`             | Livechat Matches Self Lang                                                                  | `boolean`   |     |       |                                    |
| `livechat_note`                          | Live Chat Note                                                                              | `html`      |     | ✅    |                                    |
| `livechat_operator_id`                   | Operator                                                                                    | `many2one`  |     | ✅    | res.partner                        |
| `livechat_outcome`                       | Livechat Outcome                                                                            | `selection` |     | ✅    |                                    |
| `livechat_start_hour`                    | Session Start Hour                                                                          | `float`     |     | ✅    |                                    |
| `livechat_state`                         | Livechat State                                                                              | `selection` |     | ✅    |                                    |
| `livechat_status`                        | Livechat Status                                                                             | `selection` |     | ✅    |                                    |
| `livechat_visitor_id`                    | Visitor                                                                                     | `many2one`  |     | ✅    | website.visitor                    |
| `livechat_week_day`                      | Day of the Week                                                                             | `selection` |     | ✅    |                                    |
| `member_count`                           | Member Count                                                                                | `integer`   |     |       |                                    |
| `message_attachment_count`               | Attachment Count                                                                            | `integer`   |     |       |                                    |
| `message_count`                          | # Messages                                                                                  | `integer`   |     |       |                                    |
| `message_follower_ids`                   | Followers                                                                                   | `one2many`  |     | ✅    | mail.followers                     |
| `message_has_error`                      | Message Delivery error                                                                      | `boolean`   |     |       |                                    |
| `message_has_error_counter`              | Number of errors                                                                            | `integer`   |     |       |                                    |
| `message_has_sms_error`                  | SMS Delivery error                                                                          | `boolean`   |     |       |                                    |
| `message_ids`                            | Messages                                                                                    | `one2many`  |     | ✅    | mail.message                       |
| `message_is_follower`                    | Is Follower                                                                                 | `boolean`   |     |       |                                    |
| `message_needaction`                     | Action Needed                                                                               | `boolean`   |     |       |                                    |
| `message_needaction_counter`             | Number of Actions                                                                           | `integer`   |     |       |                                    |
| `message_partner_ids`                    | Followers (Partners)                                                                        | `many2many` |     |       | res.partner                        |
| `name`                                   | Name                                                                                        | `char`      | ✅  | ✅    |                                    |
| `parent_channel_id`                      | Parent Channel                                                                              | `many2one`  |     | ✅    | discuss.channel                    |
| `pinned_message_ids`                     | Pinned Messages                                                                             | `one2many`  |     | ✅    | mail.message                       |
| `rating_avg`                             | Average Rating                                                                              | `float`     |     |       |                                    |
| `rating_avg_text`                        | Rating Avg Text                                                                             | `selection` |     |       |                                    |
| `rating_count`                           | Rating count                                                                                | `integer`   |     |       |                                    |
| `rating_ids`                             | Ratings                                                                                     | `one2many`  |     | ✅    | rating.rating                      |
| `rating_last_feedback`                   | Rating Last Feedback                                                                        | `text`      |     |       |                                    |
| `rating_last_image`                      | Rating Last Image                                                                           | `binary`    |     |       |                                    |
| `rating_last_text`                       | Rating Text                                                                                 | `selection` |     | ✅    |                                    |
| `rating_last_value`                      | Rating Last Value                                                                           | `float`     |     | ✅    |                                    |
| `rating_percentage_satisfaction`         | Rating Satisfaction                                                                         | `float`     |     |       |                                    |
| `rtc_session_ids`                        | Rtc Session                                                                                 | `one2many`  |     | ✅    | discuss.channel.rtc.session        |
| `self_member_id`                         | Self Member                                                                                 | `many2one`  |     |       | discuss.channel.member             |
| `sfu_channel_uuid`                       | Sfu Channel Uuid                                                                            | `char`      |     | ✅    |                                    |
| `sfu_server_url`                         | Sfu Server Url                                                                              | `char`      |     | ✅    |                                    |
| `student_id`                             | Student                                                                                     | `many2one`  |     | ✅    | op.student                         |
| `sub_channel_ids`                        | Sub Channels                                                                                | `one2many`  |     | ✅    | discuss.channel                    |
| `subscription_department_ids`            | HR Departments                                                                              | `many2many` |     | ✅    | hr.department                      |
| `uuid`                                   | UUID                                                                                        | `char`      |     | ✅    |                                    |
| `website_message_ids`                    | Website Messages                                                                            | `one2many`  |     | ✅    | mail.message                       |
| `whatsapp_contact`                       | Whatsapp Contact                                                                            | `many2one`  |     | ✅    | whatsapp.contact                   |
| `write_date`                             | Last Updated on                                                                             | `datetime`  |     | ✅    |                                    |
| `write_uid`                              | Last Updated by                                                                             | `many2one`  |     | ✅    | res.users                          |

**Access Rights:**

| Name                   | Group                | Perms     |
| ---------------------- | -------------------- | --------- |
| discuss.channel.system | Role / Administrator | `R/W/C/D` |
| discuss.channel.portal | Role / Portal        | `R`       |
| discuss.channel.portal | Role / Portal        | `R/W/C/D` |
| discuss.channel.public | Role / Public        | `R`       |
| discuss.channel.user   | Role / User          | `R/W/C`   |

**Record Rules:**

- **discuss.channel: can access channels (as member or as group allowed)** (10, 11, 1)
  `R/W/C/D`
  - Domain:
    `             [                 "|",                     "&",                         ("channel_type", "!=", "channel"),                         "|",                             ("is_member", "=", True),                             ("parent_channel_id.is_member", "=", True),                     "&",                         ("channel_type", "=", "channel"),                         "|",                             ("group_public_id", "=", False),                             ("group_public_id", "in", user.all_group_ids.ids),             ]         `
- **discuss.channel: admin full access** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **discuss.channel: livechat users can read all livechat channels** (51) `R`
  - Domain: `[('channel_type', '=', 'livechat')]`
- **discuss.channel: sales users can read lead's origin channel** (25) `R`
  - Domain: `[("has_crm_lead", "=", True)]`

### 🗃️ `res.groups` — Access Groups

Update of res.users class - add a preference about username for livechat purpose

**Fields:**

| Field                  | Label                                     | Type        | Req | Store | Relation             |
| ---------------------- | ----------------------------------------- | ----------- | --- | ----- | -------------------- |
| `all_implied_by_ids`   | Transitively Implying Groups              | `many2many` |     |       | res.groups           |
| `all_implied_ids`      | Transitively Implied Groups               | `many2many` |     |       | res.groups           |
| `all_user_ids`         | Users and implied users                   | `many2many` |     |       | res.users            |
| `all_users_count`      | # Users                                   | `integer`   |     |       |                      |
| `api_key_duration`     | API Keys maximum duration days            | `float`     |     | ✅    |                      |
| `comment`              | Comment                                   | `text`      |     | ✅    |                      |
| `create_date`          | Created on                                | `datetime`  |     | ✅    |                      |
| `create_uid`           | Created by                                | `many2one`  |     | ✅    | res.users            |
| `disjoint_ids`         | Disjoint Groups                           | `many2many` |     |       | res.groups           |
| `display_name`         | Display Name                              | `char`      |     |       |                      |
| `full_name`            | Group Name                                | `char`      |     |       |                      |
| `id`                   | ID                                        | `integer`   |     | ✅    |                      |
| `implied_by_ids`       | Implying Groups                           | `many2many` |     | ✅    | res.groups           |
| `implied_ids`          | Implied Groups                            | `many2many` |     | ✅    | res.groups           |
| `menu_access`          | Access Menu                               | `many2many` |     | ✅    | ir.ui.menu           |
| `model_access`         | Access Controls                           | `one2many`  |     | ✅    | ir.model.access      |
| `name`                 | Name                                      | `char`      | ✅  | ✅    |                      |
| `parent_ids`           | Parents                                   | `many2many` |     | ✅    | res.groups           |
| `privilege_id`         | Privilege                                 | `many2one`  |     | ✅    | res.groups.privilege |
| `role_count`           | # Roles                                   | `integer`   |     |       |                      |
| `role_id`              | Role                                      | `one2many`  |     | ✅    | res.users.role       |
| `role_ids`             | Roles                                     | `many2many` |     |       | res.users.role       |
| `rule_groups`          | Rules                                     | `many2many` |     | ✅    | ir.rule              |
| `sequence`             | Sequence                                  | `integer`   |     | ✅    |                      |
| `share`                | Share Group                               | `boolean`   |     | ✅    |                      |
| `trans_parent_ids`     | Parent Groups                             | `many2many` |     |       | res.groups           |
| `user_ids`             | User                                      | `many2many` |     | ✅    | res.users            |
| `view_access`          | Views                                     | `many2many` |     | ✅    | ir.ui.view           |
| `view_group_hierarchy` | Technical field for default group setting | `json`      |     |       |                      |
| `write_date`           | Last Updated on                           | `datetime`  |     | ✅    |                      |
| `write_uid`            | Last Updated by                           | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                         | Group         | Perms     |
| ---------------------------- | ------------- | --------- |
| res_groups group_erp_manager | Access Rights | `R/W/C/D` |
| res_groups group_user        | Role / User   | `R`       |

### 🗃️ `discuss.channel.member` — Channel Member

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                      | Type        | Req | Store | Relation                           |
| ----------------------------- | -------------------------- | ----------- | --- | ----- | ---------------------------------- |
| `agent_expertise_ids`         | Agent Expertise            | `many2many` |     |       | im_livechat.expertise              |
| `channel_id`                  | Channel                    | `many2one`  | ✅  | ✅    | discuss.channel                    |
| `chatbot_script_id`           | Chatbot Script             | `many2one`  |     |       | chatbot.script                     |
| `create_date`                 | Created on                 | `datetime`  |     | ✅    |                                    |
| `create_uid`                  | Created by                 | `many2one`  |     | ✅    | res.users                          |
| `custom_channel_name`         | Custom channel name        | `char`      |     | ✅    |                                    |
| `custom_notifications`        | Customized Notifications   | `selection` |     | ✅    |                                    |
| `display_name`                | Display Name               | `char`      |     |       |                                    |
| `fetched_message_id`          | Last Fetched               | `many2one`  |     | ✅    | mail.message                       |
| `guest_id`                    | Guest                      | `many2one`  |     | ✅    | mail.guest                         |
| `id`                          | ID                         | `integer`   |     | ✅    |                                    |
| `is_pinned`                   | Is pinned on the interface | `boolean`   |     |       |                                    |
| `is_self`                     | Is Self                    | `boolean`   |     |       |                                    |
| `last_interest_dt`            | Last Interest              | `datetime`  |     | ✅    |                                    |
| `last_seen_dt`                | Last seen date             | `datetime`  |     | ✅    |                                    |
| `livechat_member_history_ids` | Livechat Member History    | `one2many`  |     | ✅    | im_livechat.channel.member.history |
| `livechat_member_type`        | Livechat Member Type       | `selection` |     |       |                                    |
| `message_unread_counter`      | Unread Messages Counter    | `integer`   |     |       |                                    |
| `mute_until_dt`               | Mute notifications until   | `datetime`  |     | ✅    |                                    |
| `new_message_separator`       | New Message Separator      | `integer`   | ✅  | ✅    |                                    |
| `partner_id`                  | Partner                    | `many2one`  |     | ✅    | res.partner                        |
| `rtc_inviting_session_id`     | Ringing session            | `many2one`  |     | ✅    | discuss.channel.rtc.session        |
| `rtc_session_ids`             | RTC Sessions               | `one2many`  |     | ✅    | discuss.channel.rtc.session        |
| `seen_message_id`             | Last Seen                  | `many2one`  |     | ✅    | mail.message                       |
| `unpin_dt`                    | Unpin date                 | `datetime`  |     | ✅    |                                    |
| `write_date`                  | Last Updated on            | `datetime`  |     | ✅    |                                    |
| `write_uid`                   | Last Updated by            | `many2one`  |     | ✅    | res.users                          |

**Access Rights:**

| Name                          | Group         | Perms     |
| ----------------------------- | ------------- | --------- |
| discuss.channel.member.portal | Role / Portal | `R/W/C/D` |
| discuss.channel.member.public | Role / Public | `R/W/C/D` |
| discuss.channel.member.user   | Role / User   | `R/W/C/D` |

**Record Rules:**

- **discuss.channel.member: access their own entries** (10, 11, 1) `W/D`
  - Domain:
    `             [                 ('is_self', '=', True),                 "|",                     ("channel_id.channel_type", "!=", "channel"),                     "|",                         ("channel_id.group_public_id", "=", False),                         ("channel_id.group_public_id", "in", user.all_group_ids.ids),             ]         `
- **discuss.channel.member: read members of accessible channels** (10, 11, 1) `R`
  - Domain:
    `             [                 "|",                     "&",                         ("channel_id.channel_type", "!=", "channel"),                         "|",                             ("channel_id.is_member", "=", True),                             ("channel_id.parent_channel_id.is_member", "=", True),                     "&",                         ("channel_id.channel_type", "=", "channel"),                         "|",                             ("channel_id.group_public_id", "=", False),                             ("channel_id.group_public_id", "in", user.all_group_ids.ids),             ]         `
- **discuss.channel.member: can join group restricted channels when group is matching**
  (10, 11, 1) `C`
  - Domain:
    `             [                 ('is_self', '=', True),                 ('channel_id.channel_type', '=', 'channel'),                 '|',                     ('channel_id.group_public_id', '=', False),                     ('channel_id.group_public_id', 'in', user.all_group_ids.ids)             ]         `
- **discuss.channel.member: internal users can invite others in group restricted
  channels when group is matching** (1) `C`
  - Domain:
    `             [                 ('is_self', '=', False),                 ('channel_id.channel_type', '=', 'channel'),                 '|',                     ('channel_id.group_public_id', '=', False),                     ('channel_id.group_public_id', 'in', user.all_group_ids.ids)             ]         `
- **discuss.channel.member: internal users can invite others in channels they are member
  of** (1) `C`
  - Domain:
    `             [                 ('is_self', '=', False),                 ('channel_id.channel_type', 'not in', ('channel', 'chat')),                 ('channel_id.is_member', '=', True)             ]         `
- **discuss.channel.member: admin can manipulate all entries** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **discuss.channel.member: livechat users can read all livechat channel members and can
  invite anyone** (51) `R/C`
  - Domain: `[('channel_id.channel_type', '=', 'livechat')]`
- **discuss.channel.member: sales users can read/create members on lead's origin
  channel** (25) `R/C`
  - Domain: `[("channel_id.has_crm_lead", "=", True)]`

### 🗃️ `chatbot.message` — Chatbot Message

Chatbot Mail Message We create a new model to store the related step to a mail.message
and the user's answer. We do this in a new model to avoid bloating the 'mail.message'
model.

**Fields:**

| Field                       | Label                  | Type       | Req | Store | Relation              |
| --------------------------- | ---------------------- | ---------- | --- | ----- | --------------------- |
| `create_date`               | Created on             | `datetime` |     | ✅    |                       |
| `create_uid`                | Created by             | `many2one` |     | ✅    | res.users             |
| `discuss_channel_id`        | Discussion Channel     | `many2one` | ✅  | ✅    | discuss.channel       |
| `display_name`              | Display Name           | `char`     |     |       |                       |
| `id`                        | ID                     | `integer`  |     | ✅    |                       |
| `mail_message_id`           | Related Mail Message   | `many2one` |     | ✅    | mail.message          |
| `script_step_id`            | Chatbot Step           | `many2one` |     | ✅    | chatbot.script.step   |
| `user_raw_answer`           | User's raw answer      | `html`     |     | ✅    |                       |
| `user_raw_script_answer_id` | User Raw Script Answer | `integer`  |     | ✅    |                       |
| `user_script_answer_id`     | User's answer          | `many2one` |     | ✅    | chatbot.script.answer |
| `write_date`                | Last Updated on        | `datetime` |     | ✅    |                       |
| `write_uid`                 | Last Updated by        | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                | Group                     | Perms     |
| ------------------- | ------------------------- | --------- |
| chatbot.script.user | Live Chat / Administrator | `R/W/C/D` |

### 🗃️ `chatbot.script` — Chatbot Script

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                    | Label                  | Type        | Req | Store | Relation            |
| ------------------------ | ---------------------- | ----------- | --- | ----- | ------------------- |
| `active`                 | Active                 | `boolean`   |     | ✅    |                     |
| `create_date`            | Created on             | `datetime`  |     | ✅    |                     |
| `create_uid`             | Created by             | `many2one`  |     | ✅    | res.users           |
| `display_name`           | Display Name           | `char`      |     |       |                     |
| `first_step_warning`     | First Step Warning     | `selection` |     |       |                     |
| `id`                     | ID                     | `integer`   |     | ✅    |                     |
| `image_1024`             | Image 1024             | `binary`    |     | ✅    |                     |
| `image_128`              | Image 128              | `binary`    |     | ✅    |                     |
| `image_1920`             | Image                  | `binary`    |     |       |                     |
| `image_256`              | Image 256              | `binary`    |     | ✅    |                     |
| `image_512`              | Image 512              | `binary`    |     | ✅    |                     |
| `lead_count`             | Generated Lead Count   | `integer`   |     |       |                     |
| `livechat_channel_count` | Livechat Channel Count | `integer`   |     |       |                     |
| `name`                   | Name                   | `char`      |     |       |                     |
| `operator_partner_id`    | Bot Operator           | `many2one`  | ✅  | ✅    | res.partner         |
| `script_step_ids`        | Script Steps           | `one2many`  |     | ✅    | chatbot.script.step |
| `source_id`              | Source                 | `many2one`  | ✅  | ✅    | utm.source          |
| `title`                  | Title                  | `char`      | ✅  | ✅    |                     |
| `write_date`             | Last Updated on        | `datetime`  |     | ✅    |                     |
| `write_uid`              | Last Updated by        | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                | Group                     | Perms     |
| ------------------- | ------------------------- | --------- |
| chatbot.script.user | Live Chat / Administrator | `R/W/C/D` |

### 🗃️ `chatbot.script.answer` — Chatbot Script Answer

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label           | Type       | Req | Store | Relation            |
| ------------------- | --------------- | ---------- | --- | ----- | ------------------- |
| `chatbot_script_id` | Chatbot         | `many2one` |     |       | chatbot.script      |
| `create_date`       | Created on      | `datetime` |     | ✅    |                     |
| `create_uid`        | Created by      | `many2one` |     | ✅    | res.users           |
| `display_name`      | Display Name    | `char`     |     |       |                     |
| `id`                | ID              | `integer`  |     | ✅    |                     |
| `name`              | Answer          | `char`     | ✅  | ✅    |                     |
| `redirect_link`     | Redirect Link   | `char`     |     | ✅    |                     |
| `script_step_id`    | Script Step     | `many2one` | ✅  | ✅    | chatbot.script.step |
| `sequence`          | Sequence        | `integer`  |     | ✅    |                     |
| `write_date`        | Last Updated on | `datetime` |     | ✅    |                     |
| `write_uid`         | Last Updated by | `many2one` |     | ✅    | res.users           |

**Access Rights:**

| Name                       | Group                     | Perms     |
| -------------------------- | ------------------------- | --------- |
| chatbot.script.answer.user | Live Chat / Administrator | `R/W/C/D` |
| chatbot.script.answer      | Everyone                  | `-`       |

### 🗃️ `chatbot.script.step` — Chatbot Script Step

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                       | Label                     | Type        | Req | Store | Relation              |
| --------------------------- | ------------------------- | ----------- | --- | ----- | --------------------- |
| `answer_ids`                | Answers                   | `one2many`  |     | ✅    | chatbot.script.answer |
| `chatbot_script_id`         | Chatbot                   | `many2one`  | ✅  | ✅    | chatbot.script        |
| `create_date`               | Created on                | `datetime`  |     | ✅    |                       |
| `create_uid`                | Created by                | `many2one`  |     | ✅    | res.users             |
| `crm_team_id`               | Sales Team                | `many2one`  |     | ✅    | crm.team              |
| `display_name`              | Display Name              | `char`      |     |       |                       |
| `id`                        | ID                        | `integer`   |     | ✅    |                       |
| `is_forward_operator`       | Is Forward Operator       | `boolean`   |     |       |                       |
| `is_forward_operator_child` | Is Forward Operator Child | `boolean`   |     |       |                       |
| `message`                   | Message                   | `html`      |     | ✅    |                       |
| `name`                      | Name                      | `char`      |     |       |                       |
| `operator_expertise_ids`    | Operator Expertise        | `many2many` |     | ✅    | im_livechat.expertise |
| `sequence`                  | Sequence                  | `integer`   |     | ✅    |                       |
| `step_type`                 | Step Type                 | `selection` | ✅  | ✅    |                       |
| `triggering_answer_ids`     | Only If                   | `many2many` |     | ✅    | chatbot.script.answer |
| `write_date`                | Last Updated on           | `datetime`  |     | ✅    |                       |
| `write_uid`                 | Last Updated by           | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                     | Group                     | Perms     |
| ------------------------ | ------------------------- | --------- |
| chatbot.script.step.user | Live Chat / Administrator | `R/W/C/D` |

### 🗃️ `digest.digest` — Digest

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                     | Label                                   | Type        | Req | Store | Relation     |
| ----------------------------------------- | --------------------------------------- | ----------- | --- | ----- | ------------ |
| `available_fields`                        | Available Fields                        | `char`      |     |       |              |
| `company_id`                              | Company                                 | `many2one`  |     | ✅    | res.company  |
| `create_date`                             | Created on                              | `datetime`  |     | ✅    |              |
| `create_uid`                              | Created by                              | `many2one`  |     | ✅    | res.users    |
| `currency_id`                             | Currency                                | `many2one`  |     |       | res.currency |
| `display_name`                            | Display Name                            | `char`      |     |       |              |
| `id`                                      | ID                                      | `integer`   |     | ✅    |              |
| `is_subscribed`                           | Is user subscribed                      | `boolean`   |     |       |              |
| `kpi_account_total_revenue`               | Revenue                                 | `boolean`   |     | ✅    |              |
| `kpi_account_total_revenue_value`         | Kpi Account Total Revenue Value         | `monetary`  |     |       |              |
| `kpi_all_sale_total`                      | All Sales                               | `boolean`   |     | ✅    |              |
| `kpi_all_sale_total_value`                | Kpi All Sale Total Value                | `monetary`  |     |       |              |
| `kpi_crm_lead_created`                    | New Leads                               | `boolean`   |     | ✅    |              |
| `kpi_crm_lead_created_value`              | Kpi Crm Lead Created Value              | `integer`   |     |       |              |
| `kpi_crm_opportunities_won`               | Opportunities Won                       | `boolean`   |     | ✅    |              |
| `kpi_crm_opportunities_won_value`         | Kpi Crm Opportunities Won Value         | `integer`   |     |       |              |
| `kpi_hr_recruitment_new_colleagues`       | New Employees                           | `boolean`   |     | ✅    |              |
| `kpi_hr_recruitment_new_colleagues_value` | Kpi Hr Recruitment New Colleagues Value | `integer`   |     |       |              |
| `kpi_livechat_conversations`              | Conversations handled                   | `boolean`   |     | ✅    |              |
| `kpi_livechat_conversations_value`        | Kpi Livechat Conversations Value        | `integer`   |     |       |              |
| `kpi_livechat_rating`                     | % of Happiness                          | `boolean`   |     | ✅    |              |
| `kpi_livechat_rating_value`               | Kpi Livechat Rating Value               | `float`     |     |       |              |
| `kpi_livechat_response`                   | Time to answer (sec)                    | `boolean`   |     | ✅    |              |
| `kpi_livechat_response_value`             | Kpi Livechat Response Value             | `float`     |     |       |              |
| `kpi_mail_message_total`                  | Messages Sent                           | `boolean`   |     | ✅    |              |
| `kpi_mail_message_total_value`            | Kpi Mail Message Total Value            | `integer`   |     |       |              |
| `kpi_res_users_connected`                 | Connected Users                         | `boolean`   |     | ✅    |              |
| `kpi_res_users_connected_value`           | Kpi Res Users Connected Value           | `integer`   |     |       |              |
| `kpi_website_sale_total`                  | eCommerce Sales                         | `boolean`   |     | ✅    |              |
| `kpi_website_sale_total_value`            | Kpi Website Sale Total Value            | `monetary`  |     |       |              |
| `name`                                    | Name                                    | `char`      | ✅  | ✅    |              |
| `next_run_date`                           | Next Mailing Date                       | `date`      |     | ✅    |              |
| `periodicity`                             | Periodicity                             | `selection` | ✅  | ✅    |              |
| `state`                                   | Status                                  | `selection` |     | ✅    |              |
| `user_ids`                                | Recipients                              | `many2many` |     | ✅    | res.users    |
| `write_date`                              | Last Updated on                         | `datetime`  |     | ✅    |              |
| `write_uid`                               | Last Updated by                         | `many2one`  |     | ✅    | res.users    |

**Access Rights:**

| Name                         | Group         | Perms     |
| ---------------------------- | ------------- | --------- |
| digest.digest.administration | Access Rights | `R/W/C/D` |
| digest.digest.user           | Role / User   | `R`       |

### 🗃️ `discuss.call.history` — Keep the call history

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                              | Label                        | Type        | Req | Store | Relation                           |
| ---------------------------------- | ---------------------------- | ----------- | --- | ----- | ---------------------------------- |
| `channel_id`                       | Channel                      | `many2one`  | ✅  | ✅    | discuss.channel                    |
| `create_date`                      | Created on                   | `datetime`  |     | ✅    |                                    |
| `create_uid`                       | Created by                   | `many2one`  |     | ✅    | res.users                          |
| `display_name`                     | Display Name                 | `char`      |     |       |                                    |
| `duration_hour`                    | Duration Hour                | `float`     |     |       |                                    |
| `end_dt`                           | End Dt                       | `datetime`  |     | ✅    |                                    |
| `id`                               | ID                           | `integer`   |     | ✅    |                                    |
| `livechat_participant_history_ids` | Livechat Participant History | `many2many` |     | ✅    | im_livechat.channel.member.history |
| `start_call_message_id`            | Start Call Message           | `many2one`  |     | ✅    | mail.message                       |
| `start_dt`                         | Start Dt                     | `datetime`  | ✅  | ✅    |                                    |
| `write_date`                       | Last Updated on              | `datetime`  |     | ✅    |                                    |
| `write_uid`                        | Last Updated by              | `many2one`  |     | ✅    | res.users                          |

**Access Rights:**

| Name                        | Group         | Perms |
| --------------------------- | ------------- | ----- |
| discuss.call.history.portal | Role / Portal | `R`   |
| discuss.call.history.public | Role / Public | `R`   |
| discuss.call.history.user   | Role / User   | `R`   |

**Record Rules:**

- **discuss.call.history: read call history of accessible channels** (10, 11, 1) `R`
  - Domain:
    `             [                 "|",                     "&",                         ("channel_id.channel_type", "!=", "channel"),                         "|",                             ("channel_id.is_member", "=", True),                             ("channel_id.parent_channel_id.is_member", "=", True),                     "&",                         ("channel_id.channel_type", "=", "channel"),                         "|",                             ("channel_id.group_public_id", "=", False),                             ("channel_id.group_public_id", "in", user.all_group_ids.ids),             ]         `
- **discuss.call.history: livechat users can access all call histories** (51) `R`
  - Domain: `[('channel_id.channel_type', '=', 'livechat')]`

### 🗃️ `im_livechat.channel.member.history` — Keep the channel member history

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                       | Type        | Req | Store | Relation                     |
| ----------------------------- | --------------------------- | ----------- | --- | ----- | ---------------------------- |
| `agent_expertise_ids`         | Agent Expertise             | `many2many` |     | ✅    | im_livechat.expertise        |
| `avatar_128`                  | Avatar 128                  | `binary`    |     |       |                              |
| `call_count`                  | # of Sessions with Calls    | `float`     |     |       |                              |
| `call_duration_hour`          | Call Duration               | `float`     |     | ✅    |                              |
| `call_history_ids`            | Call History                | `many2many` |     | ✅    | discuss.call.history         |
| `call_percentage`             | Session with Calls (%)      | `float`     |     |       |                              |
| `channel_id`                  | Channel                     | `many2one`  |     | ✅    | discuss.channel              |
| `chatbot_script_id`           | Chatbot Script              | `many2one`  |     | ✅    | chatbot.script               |
| `conversation_tag_ids`        | Live Chat Conversation Tags | `many2many` |     |       | im_livechat.conversation.tag |
| `create_date`                 | Created on                  | `datetime`  |     | ✅    |                              |
| `create_uid`                  | Created by                  | `many2one`  |     | ✅    | res.users                    |
| `display_name`                | Display Name                | `char`      |     |       |                              |
| `guest_id`                    | Guest                       | `many2one`  |     | ✅    | mail.guest                   |
| `has_call`                    | Has Call                    | `float`     |     | ✅    |                              |
| `help_status`                 | Help Status                 | `selection` |     | ✅    |                              |
| `id`                          | ID                          | `integer`   |     | ✅    |                              |
| `livechat_member_type`        | Livechat Member Type        | `selection` |     | ✅    |                              |
| `member_id`                   | Member                      | `many2one`  |     | ✅    | discuss.channel.member       |
| `message_count`               | # of Messages per Session   | `integer`   |     | ✅    |                              |
| `partner_id`                  | Partner                     | `many2one`  |     | ✅    | res.partner                  |
| `rating`                      | Rating Value                | `float`     |     |       |                              |
| `rating_id`                   | Rating                      | `many2one`  |     | ✅    | rating.rating                |
| `rating_text`                 | Rating text                 | `selection` |     |       |                              |
| `response_time_hour`          | Response Time               | `float`     |     | ✅    |                              |
| `session_country_id`          | Country                     | `many2one`  |     |       | res.country                  |
| `session_duration_hour`       | Session Duration            | `float`     |     | ✅    |                              |
| `session_livechat_channel_id` | Live chat channel           | `many2one`  |     |       | im_livechat.channel          |
| `session_outcome`             | Livechat Outcome            | `selection` |     |       |                              |
| `session_start_hour`          | Session Start Hour          | `float`     |     |       |                              |
| `session_week_day`            | Day of the Week             | `selection` |     |       |                              |
| `write_date`                  | Last Updated on             | `datetime`  |     | ✅    |                              |
| `write_uid`                   | Last Updated by             | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                               | Group            | Perms |
| ---------------------------------- | ---------------- | ----- |
| im_livechat.channel.member.history | Live Chat / User | `R`   |

### 🗃️ `im_livechat.channel` — Livechat Channel

Livechat Channel Define a communication channel, which can be accessed with
'script_external' (script tag to put on external website), 'script_internal' (code to be
integrated with odoo website) or via 'web_page' link. It provides rating tools, and
access rules for anonymous people.

**Fields:**

| Field                            | Label                      | Type        | Req | Store | Relation                 |
| -------------------------------- | -------------------------- | ----------- | --- | ----- | ------------------------ |
| `are_you_inside`                 | Are you inside the matrix? | `boolean`   |     |       |                          |
| `available_operator_ids`         | Available Operator         | `many2many` |     |       | res.users                |
| `block_assignment_during_call`   | No Chats During Call       | `boolean`   |     | ✅    |                          |
| `button_background_color`        | Button Background Color    | `char`      |     | ✅    |                          |
| `button_text`                    | Text of the Button         | `char`      |     | ✅    |                          |
| `button_text_color`              | Button Text Color          | `char`      |     | ✅    |                          |
| `channel_ids`                    | Sessions                   | `one2many`  |     | ✅    | discuss.channel          |
| `chatbot_script_count`           | Number of Chatbot          | `integer`   |     |       |                          |
| `create_date`                    | Created on                 | `datetime`  |     | ✅    |                          |
| `create_uid`                     | Created by                 | `many2one`  |     | ✅    | res.users                |
| `default_message`                | Welcome Message            | `char`      |     | ✅    |                          |
| `display_name`                   | Display Name               | `char`      |     |       |                          |
| `header_background_color`        | Header Background Color    | `char`      |     | ✅    |                          |
| `id`                             | ID                         | `integer`   |     | ✅    |                          |
| `max_sessions`                   | Maximum Sessions           | `integer`   |     | ✅    |                          |
| `max_sessions_mode`              | Sessions per Operator      | `selection` |     | ✅    |                          |
| `name`                           | Channel Name               | `char`      | ✅  | ✅    |                          |
| `nbr_channel`                    | Number of conversation     | `integer`   |     |       |                          |
| `ongoing_session_count`          | Number of Ongoing Sessions | `integer`   |     |       |                          |
| `rating_avg`                     | Average Rating             | `float`     |     |       |                          |
| `rating_avg_percentage`          | Average Rating (%)         | `float`     |     |       |                          |
| `rating_count`                   | # Ratings                  | `integer`   |     |       |                          |
| `rating_ids`                     | Ratings                    | `one2many`  |     | ✅    | rating.rating            |
| `rating_percentage_satisfaction` | Rating Satisfaction        | `integer`   |     |       |                          |
| `remaining_session_capacity`     | Remaining Session Capacity | `integer`   |     |       |                          |
| `review_link`                    | Review Link                | `char`      |     | ✅    |                          |
| `rule_ids`                       | Rules                      | `one2many`  |     | ✅    | im_livechat.channel.rule |
| `script_external`                | Script (external)          | `html`      |     |       |                          |
| `title_color`                    | Title Color                | `char`      |     | ✅    |                          |
| `user_ids`                       | Agents                     | `many2many` |     | ✅    | res.users                |
| `web_page`                       | Web Page                   | `char`      |     |       |                          |
| `write_date`                     | Last Updated on            | `datetime`  |     | ✅    |                          |
| `write_uid`                      | Last Updated by            | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                        | Group                     | Perms     |
| --------------------------- | ------------------------- | --------- |
| im_livechat.channel.user    | Live Chat / User          | `R`       |
| im_livechat.channel.manager | Live Chat / Administrator | `R/W/C/D` |

### 🗃️ `im_livechat.channel.rule` — Livechat Channel Rules

Channel Rules Rules defining access to the channel (countries, and url matching). It
also provide the 'auto pop' option to open automatically the conversation.

**Fields:**

| Field                       | Label            | Type        | Req | Store | Relation            |
| --------------------------- | ---------------- | ----------- | --- | ----- | ------------------- |
| `action`                    | Live Chat Button | `selection` | ✅  | ✅    |                     |
| `auto_popup_timer`          | Time to Open     | `integer`   |     | ✅    |                     |
| `channel_id`                | Channel          | `many2one`  |     | ✅    | im_livechat.channel |
| `chatbot_enabled_condition` | Enable ChatBot   | `selection` | ✅  | ✅    |                     |
| `chatbot_script_id`         | Chatbot          | `many2one`  |     | ✅    | chatbot.script      |
| `country_ids`               | Countries        | `many2many` |     | ✅    | res.country         |
| `create_date`               | Created on       | `datetime`  |     | ✅    |                     |
| `create_uid`                | Created by       | `many2one`  |     | ✅    | res.users           |
| `display_name`              | Display Name     | `char`      |     |       |                     |
| `id`                        | ID               | `integer`   |     | ✅    |                     |
| `regex_url`                 | URL Regex        | `char`      |     | ✅    |                     |
| `sequence`                  | Matching order   | `integer`   |     | ✅    |                     |
| `write_date`                | Last Updated on  | `datetime`  |     | ✅    |                     |
| `write_uid`                 | Last Updated by  | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                     | Group                     | Perms     |
| ------------------------ | ------------------------- | --------- |
| im_livechat.channel.rule | Live Chat / User          | `R/W/C`   |
| im_livechat.channel.rule | Live Chat / Administrator | `R/W/C/D` |

### 🗃️ `im_livechat.conversation.tag` — Live Chat Conversation Tags

Tags for Live Chat conversations.

**Fields:**

| Field              | Label            | Type        | Req | Store | Relation        |
| ------------------ | ---------------- | ----------- | --- | ----- | --------------- |
| `color`            | Color            | `integer`   |     | ✅    |                 |
| `conversation_ids` | Discuss Channels | `many2many` |     | ✅    | discuss.channel |
| `create_date`      | Created on       | `datetime`  |     | ✅    |                 |
| `create_uid`       | Created by       | `many2one`  |     | ✅    | res.users       |
| `display_name`     | Display Name     | `char`      |     |       |                 |
| `id`               | ID               | `integer`   |     | ✅    |                 |
| `name`             | Name             | `char`      | ✅  | ✅    |                 |
| `write_date`       | Last Updated on  | `datetime`  |     | ✅    |                 |
| `write_uid`        | Last Updated by  | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                                          | Group                     | Perms     |
| --------------------------------------------- | ------------------------- | --------- |
| im_livechat.conversation.tag.livechat.user    | Live Chat / User          | `R/W/C`   |
| im_livechat.conversation.tag.livechat.manager | Live Chat / Administrator | `R/W/C/D` |

### 🗃️ `im_livechat.expertise` — Live Chat Expertise

Expertise of Live Chat users.

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation  |
| -------------- | --------------- | ----------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime`  |     | ✅    |           |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users |
| `display_name` | Display Name    | `char`      |     |       |           |
| `id`           | ID              | `integer`   |     | ✅    |           |
| `name`         | Name            | `char`      | ✅  | ✅    |           |
| `user_ids`     | Operators       | `many2many` |     |       | res.users |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                                | Group                     | Perms     |
| ----------------------------------- | ------------------------- | --------- |
| im_livechat.expertise.manager       | Live Chat / Administrator | `R/W/C/D` |
| im_livechat.expertise.internal.user | Role / User               | `R`       |

### 🗃️ `im_livechat.report.channel` — Livechat Support Channel Report

Livechat Support Report on the Channels

**Fields:**

| Field                           | Label                                       | Type        | Req | Store | Relation                           |
| ------------------------------- | ------------------------------------------- | ----------- | --- | ----- | ---------------------------------- |
| `agent_providing_help_history`  | Help Provided (Agent)                       | `many2one`  |     |       | im_livechat.channel.member.history |
| `agent_requesting_help_history` | Help Requested (Agent)                      | `many2one`  |     |       | im_livechat.channel.member.history |
| `call_duration_hour`            | Call Duration                               | `float`     |     | ✅    |                                    |
| `channel_id`                    | Conversation                                | `many2one`  |     | ✅    | discuss.channel                    |
| `channel_name`                  | Channel Name                                | `char`      |     | ✅    |                                    |
| `chatbot_answers_path`          | Chatbot Answers                             | `char`      |     | ✅    |                                    |
| `chatbot_answers_path_str`      | Chatbot Answers (String)                    | `char`      |     | ✅    |                                    |
| `chatbot_script_id`             | Chatbot                                     | `many2one`  |     | ✅    | chatbot.script                     |
| `conversation_tag_ids`          | Tags used in this conversation              | `many2many` |     |       | im_livechat.conversation.tag       |
| `country_id`                    | Country of the visitor                      | `many2one`  |     | ✅    | res.country                        |
| `day_number`                    | Day of the Week                             | `selection` |     | ✅    |                                    |
| `display_name`                  | Display Name                                | `char`      |     |       |                                    |
| `duration`                      | Duration (min)                              | `float`     |     | ✅    |                                    |
| `handled_by_agent`              | Handled by Agent                            | `integer`   |     | ✅    |                                    |
| `handled_by_bot`                | Handled by Bot                              | `integer`   |     | ✅    |                                    |
| `has_call`                      | Whether the session had a call              | `float`     |     | ✅    |                                    |
| `id`                            | ID                                          | `integer`   |     | ✅    |                                    |
| `lang_id`                       | Language                                    | `many2one`  |     |       | res.lang                           |
| `leads_created`                 | Leads created                               | `integer`   |     | ✅    |                                    |
| `livechat_channel_id`           | Channel                                     | `many2one`  |     | ✅    | im_livechat.channel                |
| `nbr_message`                   | Messages per Session                        | `integer`   |     | ✅    |                                    |
| `number_of_calls`               | # of Sessions with calls                    | `float`     |     |       |                                    |
| `partner_id`                    | Agent                                       | `many2one`  |     | ✅    | res.partner                        |
| `percentage_of_calls`           | Session with Calls (%)                      | `float`     |     |       |                                    |
| `rating`                        | Rating                                      | `integer`   |     | ✅    |                                    |
| `rating_text`                   | Satisfaction Rate                           | `char`      |     | ✅    |                                    |
| `session_expertise_ids`         | Expertises used in this session             | `many2many` |     |       | im_livechat.expertise              |
| `session_expertises`            | Expertises used in this session (String)    | `char`      |     | ✅    |                                    |
| `session_outcome`               | Session Outcome                             | `selection` |     | ✅    |                                    |
| `start_date`                    | Start Date of session                       | `datetime`  |     | ✅    |                                    |
| `start_date_hour`               | Hour of start Date of session               | `char`      |     | ✅    |                                    |
| `start_date_minutes`            | Start Date of session, truncated to minutes | `char`      |     | ✅    |                                    |
| `start_hour`                    | Start Hour of session                       | `char`      |     | ✅    |                                    |
| `time_to_answer`                | Response Time                               | `float`     |     | ✅    |                                    |
| `uuid`                          | UUID                                        | `char`      |     | ✅    |                                    |
| `visitor_partner_id`            | Customer                                    | `many2one`  |     | ✅    | res.partner                        |

**Access Rights:**

| Name                       | Group                     | Perms |
| -------------------------- | ------------------------- | ----- |
| im_livechat.report.channel | Live Chat / Administrator | `R`   |

### 🗃️ `discuss.channel.rtc.session` — Mail RTC session

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label                       | Type       | Req | Store | Relation               |
| ---------------------- | --------------------------- | ---------- | --- | ----- | ---------------------- |
| `channel_id`           | Channel                     | `many2one` |     | ✅    | discuss.channel        |
| `channel_member_id`    | Channel Member              | `many2one` | ✅  | ✅    | discuss.channel.member |
| `create_date`          | Created on                  | `datetime` |     | ✅    |                        |
| `create_uid`           | Created by                  | `many2one` |     | ✅    | res.users              |
| `display_name`         | Display Name                | `char`     |     |       |                        |
| `guest_id`             | Guest                       | `many2one` |     |       | mail.guest             |
| `id`                   | ID                          | `integer`  |     | ✅    |                        |
| `is_camera_on`         | Is sending user video       | `boolean`  |     | ✅    |                        |
| `is_created_student`   | Has created student         | `boolean`  |     | ✅    |                        |
| `is_deaf`              | Has disabled incoming sound | `boolean`  |     | ✅    |                        |
| `is_muted`             | Is microphone muted         | `boolean`  |     | ✅    |                        |
| `is_screen_sharing_on` | Is sharing the screen       | `boolean`  |     | ✅    |                        |
| `partner_id`           | Partner                     | `many2one` |     | ✅    | res.partner            |
| `write_date`           | Last Updated On             | `datetime` |     | ✅    |                        |
| `write_uid`            | Last Updated by             | `many2one` |     | ✅    | res.users              |

**Access Rights:**

| Name                               | Group                | Perms     |
| ---------------------------------- | -------------------- | --------- |
| discuss.channel.rtc.session.system | Role / Administrator | `R/W/C/D` |

### 🗃️ `mail.message` — Message

Override MailMessage class in order to add a new type: SMS messages. Those messages
comes with their own notification method, using SMS gateway.

**Fields:**

| Field                             | Label                              | Type                 | Req | Store | Relation                  |
| --------------------------------- | ---------------------------------- | -------------------- | --- | ----- | ------------------------- |
| `account_audit_log_account_id`    | Account                            | `many2one`           |     |       | account.account           |
| `account_audit_log_company_id`    | Company                            | `many2one`           |     |       | res.company               |
| `account_audit_log_move_id`       | Journal Entry                      | `many2one`           |     |       | account.move              |
| `account_audit_log_partner_id`    | Partner                            | `many2one`           |     |       | res.partner               |
| `account_audit_log_preview`       | Description                        | `text`               |     |       |                           |
| `account_audit_log_restricted`    | Protected by restricted Audit Logs | `boolean`            |     |       |                           |
| `account_audit_log_tax_id`        | Tax                                | `many2one`           |     |       | account.tax               |
| `attachment_ids`                  | Attachments                        | `many2many`          |     | ✅    | ir.attachment             |
| `author_avatar`                   | Author's avatar                    | `binary`             |     |       |                           |
| `author_guest_id`                 | Guest                              | `many2one`           |     | ✅    | mail.guest                |
| `author_id`                       | Author                             | `many2one`           |     | ✅    | res.partner               |
| `body`                            | Contents                           | `html`               |     | ✅    |                           |
| `call_history_ids`                | Call History                       | `one2many`           |     | ✅    | discuss.call.history      |
| `channel_id`                      | Channel                            | `many2one`           |     |       | discuss.channel           |
| `child_ids`                       | Child Messages                     | `one2many`           |     | ✅    | mail.message              |
| `create_date`                     | Created on                         | `datetime`           |     | ✅    |                           |
| `create_uid`                      | Created by                         | `many2one`           |     | ✅    | res.users                 |
| `date`                            | Date                               | `datetime`           |     | ✅    |                           |
| `display_name`                    | Display Name                       | `char`               |     |       |                           |
| `email_add_signature`             | Email Add Signature                | `boolean`            |     | ✅    |                           |
| `email_from`                      | From                               | `char`               |     | ✅    |                           |
| `email_layout_xmlid`              | Layout                             | `char`               |     | ✅    |                           |
| `has_error`                       | Has error                          | `boolean`            |     |       |                           |
| `has_sms_error`                   | Has SMS error                      | `boolean`            |     |       |                           |
| `id`                              | ID                                 | `integer`            |     | ✅    |                           |
| `incoming_email_cc`               | Emails Cc                          | `char`               |     | ✅    |                           |
| `incoming_email_to`               | Emails To                          | `text`               |     | ✅    |                           |
| `is_current_user_or_guest_author` | Is Current User Or Guest Author    | `boolean`            |     |       |                           |
| `is_internal`                     | Employee Only                      | `boolean`            |     | ✅    |                           |
| `letter_ids`                      | Letter                             | `one2many`           |     | ✅    | snailmail.letter          |
| `linked_message_ids`              | Linked Message                     | `many2many`          |     |       | mail.message              |
| `mail_activity_type_id`           | Mail Activity Type                 | `many2one`           |     | ✅    | mail.activity.type        |
| `mail_ids`                        | Mails                              | `one2many`           |     | ✅    | mail.mail                 |
| `mail_server_id`                  | Outgoing mail server               | `many2one`           |     | ✅    | ir.mail_server            |
| `message_id`                      | Message-Id                         | `char`               |     | ✅    |                           |
| `message_link_preview_ids`        | Message Link Preview               | `one2many`           |     | ✅    | mail.message.link.preview |
| `message_type`                    | Type                               | `selection`          | ✅  | ✅    |                           |
| `model`                           | Related Document Model             | `char`               |     | ✅    |                           |
| `needaction`                      | Need Action                        | `boolean`            |     |       |                           |
| `notification_ids`                | Notifications                      | `one2many`           |     | ✅    | mail.notification         |
| `notified_partner_ids`            | Partners with Need Action          | `many2many`          |     | ✅    | res.partner               |
| `outgoing_email_to`               | emails To                          | `char`               |     | ✅    |                           |
| `parent_id`                       | Parent Message                     | `many2one`           |     | ✅    | mail.message              |
| `partner_ids`                     | Recipients                         | `many2many`          |     | ✅    | res.partner               |
| `pinned_at`                       | Pinned                             | `datetime`           |     | ✅    |                           |
| `preview`                         | Preview                            | `char`               |     |       |                           |
| `rating_id`                       | Rating                             | `many2one`           |     |       | rating.rating             |
| `rating_ids`                      | Related ratings                    | `one2many`           |     | ✅    | rating.rating             |
| `rating_value`                    | Rating Value                       | `float`              |     |       |                           |
| `reaction_ids`                    | Reactions                          | `one2many`           |     | ✅    | mail.message.reaction     |
| `record_alias_domain_id`          | Alias Domain                       | `many2one`           |     | ✅    | mail.alias.domain         |
| `record_company_id`               | Company                            | `many2one`           |     | ✅    | res.company               |
| `record_name`                     | Message Record Name                | `char`               |     |       |                           |
| `reply_to`                        | Reply-To                           | `char`               |     | ✅    |                           |
| `reply_to_force_new`              | No threading for answers           | `boolean`            |     | ✅    |                           |
| `res_id`                          | Related Document ID                | `many2one_reference` |     | ✅    |                           |
| `snailmail_error`                 | Snailmail message in error         | `boolean`            |     |       |                           |
| `starred`                         | Starred                            | `boolean`            |     |       |                           |
| `starred_partner_ids`             | Favorited By                       | `many2many`          |     | ✅    | res.partner               |
| `subject`                         | Subject                            | `char`               |     | ✅    |                           |
| `subtype_id`                      | Subtype                            | `many2one`           |     | ✅    | mail.message.subtype      |
| `tracking_value_ids`              | Tracking values                    | `one2many`           |     | ✅    | mail.tracking.value       |
| `write_date`                      | Last Updated on                    | `datetime`           |     | ✅    |                           |
| `write_uid`                       | Last Updated by                    | `many2one`           |     | ✅    | res.users                 |

**Access Rights:**

| Name                | Group         | Perms     |
| ------------------- | ------------- | --------- |
| mail.message.portal | Role / Portal | `R/W/C/D` |
| mail.message.all    | Role / Public | `R`       |
| mail.message.user   | Role / User   | `R/W/C/D` |

**Record Rules:**

- **User: All Chatter** (83) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `ir.qweb` — Qweb

IrQweb object for rendering stuff in the website context

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `rating.rating` — Rating

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                 | Label                         | Type                 | Req | Store | Relation     |
| --------------------- | ----------------------------- | -------------------- | --- | ----- | ------------ |
| `access_token`        | Security Token                | `char`               |     | ✅    |              |
| `consumed`            | Filled Rating                 | `boolean`            |     | ✅    |              |
| `create_date`         | Submitted on                  | `datetime`           |     | ✅    |              |
| `create_uid`          | Created by                    | `many2one`           |     | ✅    | res.users    |
| `display_name`        | Display Name                  | `char`               |     |       |              |
| `feedback`            | Comment                       | `text`               |     | ✅    |              |
| `id`                  | ID                            | `integer`            |     | ✅    |              |
| `is_internal`         | Visible Internally Only       | `boolean`            |     | ✅    |              |
| `message_id`          | Message                       | `many2one`           |     | ✅    | mail.message |
| `parent_ref`          | Parent Ref                    | `reference`          |     |       |              |
| `parent_res_id`       | Parent Document               | `integer`            |     | ✅    |              |
| `parent_res_model`    | Parent Document Model         | `char`               |     | ✅    |              |
| `parent_res_model_id` | Parent Related Document Model | `many2one`           |     | ✅    | ir.model     |
| `parent_res_name`     | Parent Document Name          | `char`               |     | ✅    |              |
| `partner_id`          | Customer                      | `many2one`           |     | ✅    | res.partner  |
| `publisher_comment`   | Publisher comment             | `text`               |     | ✅    |              |
| `publisher_datetime`  | Commented on                  | `datetime`           |     | ✅    |              |
| `publisher_id`        | Commented by                  | `many2one`           |     | ✅    | res.partner  |
| `rated_on`            | Rated On                      | `datetime`           |     | ✅    |              |
| `rated_partner_id`    | Rated Operator                | `many2one`           |     | ✅    | res.partner  |
| `rated_partner_name`  | Name                          | `char`               |     |       |              |
| `rating`              | Rating Value                  | `float`              |     | ✅    |              |
| `rating_image`        | Image                         | `binary`             |     |       |              |
| `rating_image_url`    | Image URL                     | `char`               |     |       |              |
| `rating_text`         | Rating                        | `selection`          |     | ✅    |              |
| `res_id`              | Document                      | `many2one_reference` | ✅  | ✅    |              |
| `res_model`           | Document Model                | `char`               |     | ✅    |              |
| `res_model_id`        | Related Document Model        | `many2one`           |     | ✅    | ir.model     |
| `res_name`            | Resource name                 | `char`               |     | ✅    |              |
| `resource_ref`        | Resource Ref                  | `reference`          |     |       |              |
| `write_date`          | Last Updated on               | `datetime`           |     | ✅    |              |
| `write_uid`           | Last Updated by               | `many2one`           |     | ✅    | res.users    |

**Access Rights:**

| Name                        | Group                | Perms     |
| --------------------------- | -------------------- | --------- |
| rating.rating.access.system | Role / Administrator | `R/W/C/D` |
| rating.rating.portal        | Role / Portal        | `-`       |
| rating.rating.public        | Role / Public        | `-`       |
| rating.rating.user          | Role / User          | `R/W/C`   |

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

### 🗃️ `res.users.settings` — User Settings

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                      | Label                                     | Type        | Req | Store | Relation                           |
| ------------------------------------------ | ----------------------------------------- | ----------- | --- | ----- | ---------------------------------- |
| `calendar_default_privacy`                 | Calendar Default Privacy                  | `selection` | ✅  | ✅    |                                    |
| `channel_notifications`                    | Channel Notifications                     | `selection` |     | ✅    |                                    |
| `create_date`                              | Created on                                | `datetime`  |     | ✅    |                                    |
| `create_uid`                               | Created by                                | `many2one`  |     | ✅    | res.users                          |
| `display_name`                             | Display Name                              | `char`      |     |       |                                    |
| `embedded_actions_config_ids`              | Embedded Actions Config                   | `one2many`  |     | ✅    | res.users.settings.embedded.action |
| `id`                                       | ID                                        | `integer`   |     | ✅    |                                    |
| `is_discuss_sidebar_category_channel_open` | Is discuss sidebar category channel open? | `boolean`   |     | ✅    |                                    |
| `is_discuss_sidebar_category_chat_open`    | Is discuss sidebar category chat open?    | `boolean`   |     | ✅    |                                    |
| `livechat_expertise_ids`                   | Live Chat Expertise                       | `many2many` |     | ✅    | im_livechat.expertise              |
| `livechat_lang_ids`                        | Livechat languages                        | `many2many` |     | ✅    | res.lang                           |
| `livechat_username`                        | Livechat Username                         | `char`      |     | ✅    |                                    |
| `push_to_talk_key`                         | Push-To-Talk shortcut                     | `char`      |     | ✅    |                                    |
| `use_push_to_talk`                         | Use the push to talk feature              | `boolean`   |     | ✅    |                                    |
| `user_id`                                  | User                                      | `many2one`  | ✅  | ✅    | res.users                          |
| `voice_active_duration`                    | Duration of voice activity in ms          | `integer`   |     | ✅    |                                    |
| `volume_settings_ids`                      | Volumes of other partners                 | `one2many`  |     | ✅    | res.users.settings.volumes         |
| `write_date`                               | Last Updated on                           | `datetime`  |     | ✅    |                                    |
| `write_uid`                                | Last Updated by                           | `many2one`  |     | ✅    | res.users                          |

**Access Rights:**

| Name               | Group       | Perms     |
| ------------------ | ----------- | --------- |
| res.users.settings | Role / User | `R/W/C/D` |
| res.users.settings | Everyone    | `-`       |

**Record Rules:**

- **Administrators can access all User Settings.** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **res.users.settings: access their own entries** (1) `R/W/C/D`
  - Domain: `[('user_id', '=', user.id)]`

### 🗃️ `ir.websocket` — websocket message handling

Override to handle discuss specific features (channel in particular).

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |
