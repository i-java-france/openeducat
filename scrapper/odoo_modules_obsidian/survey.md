---
title: "Surveys"
module: "survey"
state: "installed"
version: "19.0.3.7"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/app/surveys"
license: "LGPL-3"
category: "Surveys"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_______, odoo/app]
---

# 🟢 Surveys

> **Module:** `survey` | **Version:** `19.0.3.7` **Category:** Surveys | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** https://www.odoo.com/app/surveys

## 🔗 Dependencies

[[auth_signup]] [[http_routing]] [[mail]] [[web_tour]] [[gamification]]

## 📖 Description

# Create beautiful surveys and visualize answers

It depends on the answers or reviews of some questions by different users. A survey may
have multiple pages. Each page may contain multiple questions and each question may have
multiple answers. Different users may give different answers of question and according
to that survey is done. Partners are also sent mails with personal token for the
invitation of the survey.

## 🖥️ UI Components

### Menus

- `Surveys`
- `Surveys/Participants`
- `Surveys/Questions & Answers`
- `Surveys/Questions & Answers/Detailed Answers`
- `Surveys/Questions & Answers/Questions`
- `Surveys/Questions & Answers/Suggested Values`
- `Surveys/Surveys`

### Views

- `* INHERIT Survey Layout (qweb)`
- `* INHERIT Survey User Input Session (qweb)`
- `* INHERIT res.partner.view.form.inherit.survey (form)`
- `Form view for survey question (form)`
- `Image from the question suggested answer (qweb)`
- `List view for survey question (list)`
- `Question: choice result (simple_choice, multiple_choice, scale) (qweb)`
- `Question: comments (qweb)`
- `Question: date box (qweb)`
- `Question: datetime box (qweb)`
- `Question: free text box (qweb)`
- `Question: matrix (qweb)`
- `Question: matrix result (matrix) (qweb)`
- `Question: multiple choice (qweb)`
- `Question: number or date (and time) result (numerical_box or date or datetime) (qweb)`
- `Question: numerical box (qweb)`
- `Question: result statistics (qweb)`
- `Question: scale (qweb)`
- `Question: simple choice (qweb)`
- `Question: text box (qweb)`
- `Question: text result (text_box, char_box) (qweb)`
- `Search view for survey question (search)`
- `Survey User Input Leaderboard (qweb)`
- `Survey User Input Session Manage (qweb)`
- `Survey: Access Code page (qweb)`
- `Survey: Filter results (qweb)`
- `Survey: Manage Session (qweb)`
- `Survey: Navigation (qweb)`
- `Survey: Open Session (qweb)`
- `Survey: Progression (qweb)`
- `Survey: access error (qweb)`
- `Survey: back to form view (qweb)`
- `Survey: custom 403 page (qweb)`
- `Survey: expired (qweb)`
- `Survey: finished (qweb)`
- `Survey: form with questions (qweb)`
- `Survey: login required (qweb)`
- `Survey: main page (take survey) (qweb)`
- `Survey: main page content (qweb)`
- `Survey: main page header (qweb)`
- `Survey: print page (qweb)`
- `Survey: question container (qweb)`
- `Survey: remove .0 (qweb)`
- `Survey: result statistics content (qweb)`
- `Survey: result statistics header (qweb)`
- `Survey: result statistics page (qweb)`
- `Survey: retake button (qweb)`
- `Survey: start form content (qweb)`
- `Survey: statistics table pagination (qweb)`
- `Survey: void content (qweb)`
- `certification_preview (qweb)`
- `certification_report_view (qweb)`
- `certification_report_view_general (qweb)`
- `gamification.badge.form.view.simplified (form)`
- `survey.invite.view.form (form)`
- `survey.question.answer.view.form (form)`
- `survey.question.answer.view.list (list)`
- `survey.question.answer.view.search (search)`
- `survey.survey.search (search)`
- `survey.survey.view.activity (activity)`
- `survey.survey.view.form (form)`
- `survey.survey.view.graph (graph)`
- `survey.survey.view.kanban (kanban)`
- `survey.survey.view.list (list)`
- `survey.survey.view.pivot (pivot)`
- `survey.user_input.line.view.form (form)`
- `survey.user_input.line.view.list (list)`
- `survey.user_input.line.view.search (search)`
- `survey.user_input.view.form (form)`
- `survey.user_input.view.kanban (kanban)`
- `survey.user_input.view.list (list)`
- `survey.user_input.view.search (search)`
- `survey_selection_key (qweb)`

### Reports

- `Certifications`

## 🛠️ Technical Documentation

**11 model(s) defined by this module:**

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

### 🗃️ `gamification.badge` — Gamification Badge

> 📧 Mail Thread

Badge object that users can send and receive

**Fields:**

| Field                        | Label                      | Type        | Req | Store | Relation                     |
| ---------------------------- | -------------------------- | ----------- | --- | ----- | ---------------------------- |
| `active`                     | Active                     | `boolean`   |     | ✅    |                              |
| `can_publish`                | Can Publish                | `boolean`   |     |       |                              |
| `challenge_ids`              | Reward of Challenges       | `one2many`  |     | ✅    | gamification.challenge       |
| `create_date`                | Created on                 | `datetime`  |     | ✅    |                              |
| `create_uid`                 | Created by                 | `many2one`  |     | ✅    | res.users                    |
| `description`                | Description                | `html`      |     | ✅    |                              |
| `display_name`               | Display Name               | `char`      |     |       |                              |
| `goal_definition_ids`        | Rewarded by                | `many2many` |     | ✅    | gamification.goal.definition |
| `granted_count`              | Total                      | `integer`   |     |       |                              |
| `granted_employees_count`    | Granted Employees Count    | `integer`   |     |       |                              |
| `granted_users_count`        | Number of users            | `integer`   |     |       |                              |
| `has_message`                | Has Message                | `boolean`   |     |       |                              |
| `id`                         | ID                         | `integer`   |     | ✅    |                              |
| `image_1024`                 | Image 1024                 | `binary`    |     | ✅    |                              |
| `image_128`                  | Image 128                  | `binary`    |     | ✅    |                              |
| `image_1920`                 | Image                      | `binary`    |     | ✅    |                              |
| `image_256`                  | Image 256                  | `binary`    |     | ✅    |                              |
| `image_512`                  | Image 512                  | `binary`    |     | ✅    |                              |
| `is_published`               | Is Published               | `boolean`   |     | ✅    |                              |
| `level`                      | Forum Badge Level          | `selection` |     | ✅    |                              |
| `message_attachment_count`   | Attachment Count           | `integer`   |     |       |                              |
| `message_follower_ids`       | Followers                  | `one2many`  |     | ✅    | mail.followers               |
| `message_has_error`          | Message Delivery error     | `boolean`   |     |       |                              |
| `message_has_error_counter`  | Number of errors           | `integer`   |     |       |                              |
| `message_has_sms_error`      | SMS Delivery error         | `boolean`   |     |       |                              |
| `message_ids`                | Messages                   | `one2many`  |     | ✅    | mail.message                 |
| `message_is_follower`        | Is Follower                | `boolean`   |     |       |                              |
| `message_needaction`         | Action Needed              | `boolean`   |     |       |                              |
| `message_needaction_counter` | Number of Actions          | `integer`   |     |       |                              |
| `message_partner_ids`        | Followers (Partners)       | `many2many` |     |       | res.partner                  |
| `name`                       | Badge                      | `char`      | ✅  | ✅    |                              |
| `owner_ids`                  | Owners                     | `one2many`  |     | ✅    | gamification.badge.user      |
| `rating_ids`                 | Ratings                    | `one2many`  |     | ✅    | rating.rating                |
| `remaining_sending`          | Remaining Sending Allowed  | `integer`   |     |       |                              |
| `rule_auth`                  | Allowance to Grant         | `selection` | ✅  | ✅    |                              |
| `rule_auth_badge_ids`        | Required Badges            | `many2many` |     | ✅    | gamification.badge           |
| `rule_auth_user_ids`         | Authorized Users           | `many2many` |     | ✅    | res.users                    |
| `rule_max`                   | Monthly Limited Sending    | `boolean`   |     | ✅    |                              |
| `rule_max_number`            | Limitation Number          | `integer`   |     | ✅    |                              |
| `stat_my`                    | My Total                   | `integer`   |     |       |                              |
| `stat_my_monthly_sending`    | My Monthly Sending Total   | `integer`   |     |       |                              |
| `stat_my_this_month`         | My Monthly Total           | `integer`   |     |       |                              |
| `stat_this_month`            | Monthly total              | `integer`   |     |       |                              |
| `survey_id`                  | Survey                     | `many2one`  |     | ✅    | survey.survey                |
| `survey_ids`                 | Survey Ids                 | `one2many`  |     | ✅    | survey.survey                |
| `unique_owner_ids`           | Unique Owners              | `many2many` |     |       | res.users                    |
| `website_absolute_url`       | Website Absolute URL       | `char`      |     |       |                              |
| `website_message_ids`        | Website Messages           | `one2many`  |     | ✅    | mail.message                 |
| `website_published`          | Visible on current website | `boolean`   |     |       |                              |
| `website_url`                | Website URL                | `char`      |     |       |                              |
| `write_date`                 | Last Updated on            | `datetime`  |     | ✅    |                              |
| `write_uid`                  | Last Updated by            | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                           | Group                                     | Perms     |
| ------------------------------ | ----------------------------------------- | --------- |
| Badge Officer                  | Employees / Officer: Manage all employees | `R/W/C/D` |
| student_gamifiction_badge      | OpenEduCat / User                         | `R/W/C/D` |
| gamification.badge.survey.user | Surveys / User                            | `R/W/C/D` |
| Badge Manager                  | Access Rights                             | `R/W/C/D` |
| Badge Portal                   | Role / Portal                             | `R`       |
| Badge Public                   | Role / Public                             | `R`       |
| Badge Employee                 | Role / User                               | `R`       |

### 🗃️ `gamification.challenge` — Gamification Challenge

> 📧 Mail Thread

Gamification challenge

    Set of predifined objectives assigned to people with rules for recurrence and
    rewards

    If 'user_ids' is defined and 'period' is different than 'one', the set will
    be assigned to the users for each period (eg: every 1st of each month if
    'monthly' is selected)

**Fields:**

| Field                        | Label                                           | Type        | Req | Store | Relation                    |
| ---------------------------- | ----------------------------------------------- | ----------- | --- | ----- | --------------------------- |
| `challenge_category`         | Appears in                                      | `selection` | ✅  | ✅    |                             |
| `create_date`                | Created on                                      | `datetime`  |     | ✅    |                             |
| `create_uid`                 | Created by                                      | `many2one`  |     | ✅    | res.users                   |
| `description`                | Description                                     | `text`      |     | ✅    |                             |
| `display_name`               | Display Name                                    | `char`      |     |       |                             |
| `end_date`                   | End Date                                        | `date`      |     | ✅    |                             |
| `has_message`                | Has Message                                     | `boolean`   |     |       |                             |
| `id`                         | ID                                              | `integer`   |     | ✅    |                             |
| `invited_user_ids`           | Suggest to users                                | `many2many` |     | ✅    | res.users                   |
| `last_report_date`           | Last Report Date                                | `date`      |     | ✅    |                             |
| `line_ids`                   | Lines                                           | `one2many`  | ✅  | ✅    | gamification.challenge.line |
| `manager_id`                 | Responsible                                     | `many2one`  |     | ✅    | res.users                   |
| `message_attachment_count`   | Attachment Count                                | `integer`   |     |       |                             |
| `message_follower_ids`       | Followers                                       | `one2many`  |     | ✅    | mail.followers              |
| `message_has_error`          | Message Delivery error                          | `boolean`   |     |       |                             |
| `message_has_error_counter`  | Number of errors                                | `integer`   |     |       |                             |
| `message_has_sms_error`      | SMS Delivery error                              | `boolean`   |     |       |                             |
| `message_ids`                | Messages                                        | `one2many`  |     | ✅    | mail.message                |
| `message_is_follower`        | Is Follower                                     | `boolean`   |     |       |                             |
| `message_needaction`         | Action Needed                                   | `boolean`   |     |       |                             |
| `message_needaction_counter` | Number of Actions                               | `integer`   |     |       |                             |
| `message_partner_ids`        | Followers (Partners)                            | `many2many` |     |       | res.partner                 |
| `name`                       | Challenge Name                                  | `char`      | ✅  | ✅    |                             |
| `next_report_date`           | Next Report Date                                | `date`      |     | ✅    |                             |
| `period`                     | Periodicity                                     | `selection` | ✅  | ✅    |                             |
| `rating_ids`                 | Ratings                                         | `one2many`  |     | ✅    | rating.rating               |
| `remind_update_delay`        | Non-updated manual goals will be reminded after | `integer`   |     | ✅    |                             |
| `report_message_frequency`   | Report Frequency                                | `selection` | ✅  | ✅    |                             |
| `report_message_group_id`    | Send a copy to                                  | `many2one`  |     | ✅    | discuss.channel             |
| `report_template_id`         | Report Template                                 | `many2one`  | ✅  | ✅    | mail.template               |
| `reward_failure`             | Reward Bests if not Succeeded?                  | `boolean`   |     | ✅    |                             |
| `reward_first_id`            | For 1st user                                    | `many2one`  |     | ✅    | gamification.badge          |
| `reward_id`                  | For Every Succeeding User                       | `many2one`  |     | ✅    | gamification.badge          |
| `reward_realtime`            | Reward as soon as every goal is reached         | `boolean`   |     | ✅    |                             |
| `reward_second_id`           | For 2nd user                                    | `many2one`  |     | ✅    | gamification.badge          |
| `reward_third_id`            | For 3rd user                                    | `many2one`  |     | ✅    | gamification.badge          |
| `start_date`                 | Start Date                                      | `date`      |     | ✅    |                             |
| `state`                      | State                                           | `selection` | ✅  | ✅    |                             |
| `user_count`                 | # Users                                         | `integer`   |     |       |                             |
| `user_domain`                | User domain                                     | `char`      |     | ✅    |                             |
| `user_ids`                   | Participants                                    | `many2many` |     | ✅    | res.users                   |
| `visibility_mode`            | Display Mode                                    | `selection` | ✅  | ✅    |                             |
| `website_message_ids`        | Website Messages                                | `one2many`  |     | ✅    | mail.message                |
| `write_date`                 | Last Updated on                                 | `datetime`  |     | ✅    |                             |
| `write_uid`                  | Last Updated by                                 | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                    | Group                                     | Perms     |
| ----------------------- | ----------------------------------------- | --------- |
| Challenge Officer       | Employees / Officer: Manage all employees | `R/W/C/D` |
| Goal Challenge Manager  | Access Rights                             | `R/W/C/D` |
| Goal Challenge Portal   | Role / Portal                             | `R`       |
| Goal Challenge Employee | Role / User                               | `R`       |

### 🗃️ `survey.survey` — Survey

> 📧 Mail Thread

Add the new 'Lead Qualification' survey template to the templates that can be selected
in the helper screen.

**Fields:**

| Field                             | Label                          | Type        | Req | Store | Relation           |
| --------------------------------- | ------------------------------ | ----------- | --- | ----- | ------------------ |
| `access_mode`                     | Access Mode                    | `selection` | ✅  | ✅    |                    |
| `access_token`                    | Access Token                   | `char`      |     | ✅    |                    |
| `active`                          | Active                         | `boolean`   |     | ✅    |                    |
| `activity_calendar_event_id`      | Next Activity Calendar Event   | `many2one`  |     |       | calendar.event     |
| `activity_date_deadline`          | Next Activity Deadline         | `date`      |     |       |                    |
| `activity_exception_decoration`   | Activity Exception Decoration  | `selection` |     |       |                    |
| `activity_exception_icon`         | Icon                           | `char`      |     |       |                    |
| `activity_ids`                    | Activities                     | `one2many`  |     | ✅    | mail.activity      |
| `activity_state`                  | Activity State                 | `selection` |     |       |                    |
| `activity_summary`                | Next Activity Summary          | `char`      |     |       |                    |
| `activity_type_icon`              | Activity Type Icon             | `char`      |     |       |                    |
| `activity_type_id`                | Next Activity Type             | `many2one`  |     |       | mail.activity.type |
| `activity_user_id`                | Responsible User               | `many2one`  |     |       | res.users          |
| `allowed_survey_types`            | Allowed survey types           | `json`      |     |       |                    |
| `answer_count`                    | Registered                     | `integer`   |     |       |                    |
| `answer_done_count`               | Attempts                       | `integer`   |     |       |                    |
| `answer_duration_avg`             | Average Duration               | `float`     |     |       |                    |
| `answer_score_avg`                | Avg Score (%)                  | `float`     |     |       |                    |
| `attempts_limit`                  | Number of attempts             | `integer`   |     | ✅    |                    |
| `background_image`                | Background Image               | `binary`    |     | ✅    |                    |
| `background_image_url`            | Background Url                 | `char`      |     |       |                    |
| `certification`                   | Is a Certification             | `boolean`   |     | ✅    |                    |
| `certification_badge_id`          | Certification Badge            | `many2one`  |     | ✅    | gamification.badge |
| `certification_badge_id_dummy`    | Certification Badge            | `many2one`  |     |       | gamification.badge |
| `certification_give_badge`        | Give Badge                     | `boolean`   |     | ✅    |                    |
| `certification_mail_template_id`  | Certified Email Template       | `many2one`  |     | ✅    | mail.template      |
| `certification_report_layout`     | Certification template         | `selection` |     | ✅    |                    |
| `certification_validity_months`   | Validity                       | `integer`   |     | ✅    |                    |
| `color`                           | Color Index                    | `integer`   |     | ✅    |                    |
| `course_id`                       | Course                         | `many2one`  |     | ✅    | op.course          |
| `create_date`                     | Created on                     | `datetime`  |     | ✅    |                    |
| `create_uid`                      | Created by                     | `many2one`  |     | ✅    | res.users          |
| `description`                     | Description                    | `html`      |     | ✅    |                    |
| `description_done`                | End Message                    | `html`      |     | ✅    |                    |
| `display_name`                    | Display Name                   | `char`      |     |       |                    |
| `generate_lead`                   | Lead Generating                | `boolean`   |     | ✅    |                    |
| `has_conditional_questions`       | Contains conditional questions | `boolean`   |     |       |                    |
| `has_message`                     | Has Message                    | `boolean`   |     |       |                    |
| `id`                              | ID                             | `integer`   |     | ✅    |                    |
| `is_attempts_limited`             | Limited number of attempts     | `boolean`   |     | ✅    |                    |
| `is_time_limited`                 | The survey is limited in time  | `boolean`   |     | ✅    |                    |
| `lang_ids`                        | Languages                      | `many2many` |     | ✅    | res.lang           |
| `lead_count`                      | Leads                          | `integer`   |     |       |                    |
| `lead_ids`                        | Lead                           | `one2many`  |     | ✅    | crm.lead           |
| `message_attachment_count`        | Attachment Count               | `integer`   |     |       |                    |
| `message_follower_ids`            | Followers                      | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`               | Message Delivery error         | `boolean`   |     |       |                    |
| `message_has_error_counter`       | Number of errors               | `integer`   |     |       |                    |
| `message_has_sms_error`           | SMS Delivery error             | `boolean`   |     |       |                    |
| `message_ids`                     | Messages                       | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`             | Is Follower                    | `boolean`   |     |       |                    |
| `message_needaction`              | Action Needed                  | `boolean`   |     |       |                    |
| `message_needaction_counter`      | Number of Actions              | `integer`   |     |       |                    |
| `message_partner_ids`             | Followers (Partners)           | `many2many` |     |       | res.partner        |
| `my_activity_date_deadline`       | My Activity Deadline           | `date`      |     |       |                    |
| `page_ids`                        | Pages                          | `one2many`  |     |       | survey.question    |
| `progression_mode`                | Display Progress as            | `selection` |     | ✅    |                    |
| `question_and_page_ids`           | Sections and Questions         | `one2many`  |     | ✅    | survey.question    |
| `question_count`                  | # Questions                    | `integer`   |     |       |                    |
| `question_ids`                    | Questions                      | `one2many`  |     |       | survey.question    |
| `questions_layout`                | Pagination                     | `selection` | ✅  | ✅    |                    |
| `questions_selection`             | Question Selection             | `selection` | ✅  | ✅    |                    |
| `rating_ids`                      | Ratings                        | `one2many`  |     | ✅    | rating.rating      |
| `restrict_user_ids`               | Restricted to                  | `many2many` |     | ✅    | res.users          |
| `scoring_max_obtainable`          | Maximum obtainable score       | `float`     |     |       |                    |
| `scoring_success_min`             | Required Score (%)             | `float`     |     | ✅    |                    |
| `scoring_type`                    | Scoring                        | `selection` | ✅  | ✅    |                    |
| `session_answer_count`            | Answers Count                  | `integer`   |     |       |                    |
| `session_available`               | Live session available         | `boolean`   |     |       |                    |
| `session_code`                    | Session Code                   | `char`      |     | ✅    |                    |
| `session_link`                    | Session Link                   | `char`      |     |       |                    |
| `session_question_answer_count`   | Question Answers Count         | `integer`   |     |       |                    |
| `session_question_id`             | Current Question               | `many2one`  |     | ✅    | survey.question    |
| `session_question_start_time`     | Current Question Start Time    | `datetime`  |     | ✅    |                    |
| `session_show_leaderboard`        | Show Session Leaderboard       | `boolean`   |     |       |                    |
| `session_speed_rating`            | Reward quick answers           | `boolean`   |     | ✅    |                    |
| `session_speed_rating_time_limit` | Time limit (seconds)           | `integer`   |     | ✅    |                    |
| `session_start_time`              | Current Session Start Time     | `datetime`  |     | ✅    |                    |
| `session_state`                   | Session State                  | `selection` |     | ✅    |                    |
| `success_count`                   | Success                        | `integer`   |     |       |                    |
| `success_ratio`                   | Success Ratio (%)              | `integer`   |     |       |                    |
| `survey_type`                     | Survey Type                    | `selection` | ✅  | ✅    |                    |
| `team_id`                         | Assign Leads to                | `many2one`  |     | ✅    | crm.team           |
| `time_limit`                      | Time limit (minutes)           | `float`     |     | ✅    |                    |
| `title`                           | Survey Title                   | `char`      | ✅  | ✅    |                    |
| `user_id`                         | Responsible                    | `many2one`  |     | ✅    | res.users          |
| `user_input_ids`                  | User responses                 | `one2many`  |     | ✅    | survey.user_input  |
| `users_can_go_back`               | Users can go back              | `boolean`   |     | ✅    |                    |
| `users_can_signup`                | Users can signup               | `boolean`   |     |       |                    |
| `users_login_required`            | Require Login                  | `boolean`   |     | ✅    |                    |
| `website_message_ids`             | Website Messages               | `one2many`  |     | ✅    | mail.message       |
| `write_date`                      | Last Updated on                | `datetime`  |     | ✅    |                    |
| `write_uid`                       | Last Updated by                | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                         | Group                   | Perms     |
| ---------------------------- | ----------------------- | --------- |
| survey.survey.survey.user    | Surveys / User          | `R/W/C/D` |
| survey.survey.survey.manager | Surveys / Administrator | `R/W/C/D` |
| survey.survey.user           | Role / User             | `-`       |
| survey.survey.all            | Everyone                | `-`       |

**Record Rules:**

- **Survey: manager: all** (29) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Survey: officer: unrestricted survey or in restricted users** (28) `R/W/C/D`
  - Domain:
    `[             '|', ('restrict_user_ids', 'in', user.id), ('restrict_user_ids', '=', False)]`

### 🗃️ `survey.user_input` — Survey User Input

> 📧 Mail Thread

Metadata for a set of one user's answers to a particular survey

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation               |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ---------------------- |
| `access_token`                  | Identification token          | `char`      | ✅  | ✅    |                        |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event         |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                        |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                        |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                        |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity          |
| `activity_state`                | Activity State                | `selection` |     |       |                        |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                        |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                        |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type     |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users              |
| `attempts_count`                | Attempts Count                | `integer`   |     |       |                        |
| `attempts_limit`                | Number of attempts            | `integer`   |     |       |                        |
| `attempts_number`               | Attempt n°                    | `integer`   |     |       |                        |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                        |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users              |
| `deadline`                      | Deadline                      | `datetime`  |     | ✅    |                        |
| `display_name`                  | Display Name                  | `char`      |     |       |                        |
| `email`                         | Email                         | `char`      |     | ✅    |                        |
| `end_datetime`                  | End date and time             | `datetime`  |     | ✅    |                        |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                        |
| `id`                            | ID                            | `integer`   |     | ✅    |                        |
| `invite_token`                  | Invite token                  | `char`      |     | ✅    |                        |
| `is_attempts_limited`           | Limited number of attempts    | `boolean`   |     |       |                        |
| `is_session_answer`             | Is in a Session               | `boolean`   |     | ✅    |                        |
| `lang_id`                       | Language                      | `many2one`  |     | ✅    | res.lang               |
| `last_displayed_page_id`        | Last displayed question/page  | `many2one`  |     | ✅    | survey.question        |
| `lead_id`                       | Lead                          | `many2one`  |     | ✅    | crm.lead               |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                        |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers         |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                        |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                        |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                        |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message           |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                        |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                        |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                        |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner            |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                        |
| `nickname`                      | Nickname                      | `char`      |     | ✅    |                        |
| `partner_id`                    | Contact                       | `many2one`  |     | ✅    | res.partner            |
| `predefined_question_ids`       | Predefined Questions          | `many2many` |     | ✅    | survey.question        |
| `question_time_limit_reached`   | Question Time Limit Reached   | `boolean`   |     |       |                        |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating          |
| `scoring_percentage`            | Score (%)                     | `float`     |     | ✅    |                        |
| `scoring_success`               | Quiz Passed                   | `boolean`   |     | ✅    |                        |
| `scoring_total`                 | Total Score                   | `float`     |     | ✅    |                        |
| `scoring_type`                  | Scoring                       | `selection` |     |       |                        |
| `start_datetime`                | Start date and time           | `datetime`  |     | ✅    |                        |
| `state`                         | Status                        | `selection` |     | ✅    |                        |
| `survey_first_submitted`        | Survey First Submitted        | `boolean`   |     | ✅    |                        |
| `survey_id`                     | Survey                        | `many2one`  | ✅  | ✅    | survey.survey          |
| `survey_time_limit_reached`     | Survey Time Limit Reached     | `boolean`   |     |       |                        |
| `test_entry`                    | Test Entry                    | `boolean`   |     | ✅    |                        |
| `user_input_line_ids`           | Answers                       | `one2many`  |     | ✅    | survey.user_input.line |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message           |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                        |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                             | Group                   | Perms     |
| -------------------------------- | ----------------------- | --------- |
| survey.user_input.survey.user    | Surveys / User          | `R/W/C/D` |
| survey.user_input.survey.manager | Surveys / Administrator | `R/W/C/D` |
| survey.user_input.user           | Role / User             | `-`       |
| survey.user_input.all            | Everyone                | `-`       |

**Record Rules:**

- **Survey user input: manager: all non specialized surveys** (29) `R/W/C/D`
  - Domain:
    `[('survey_id.survey_type', 'in', ('assessment', 'custom', 'live_session', 'survey'))]`
- **Survey user input: officer: unrestricted survey or in restricted users** (28)
  `R/W/C/D`
  - Domain:
    `[             '&', ('survey_id.survey_type', 'in', ('assessment', 'custom', 'live_session', 'survey')),             '|', ('survey_id.restrict_user_ids', 'in', user.id),                  ('survey_id.restrict_user_ids', '=', False)]`

### 🗃️ `ir.http` — HTTP Routing

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `res.lang` — Languages

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label               | Type        | Req | Store | Relation  |
| ---------------- | ------------------- | ----------- | --- | ----- | --------- |
| `active`         | Active              | `boolean`   |     | ✅    |           |
| `code`           | Locale Code         | `char`      | ✅  | ✅    |           |
| `create_date`    | Created on          | `datetime`  |     | ✅    |           |
| `create_uid`     | Created by          | `many2one`  |     | ✅    | res.users |
| `date_format`    | Date Format         | `selection` | ✅  | ✅    |           |
| `decimal_point`  | Decimal Separator   | `char`      | ✅  | ✅    |           |
| `direction`      | Direction           | `selection` | ✅  | ✅    |           |
| `display_name`   | Display Name        | `char`      |     |       |           |
| `flag_image`     | Image               | `binary`    |     | ✅    |           |
| `flag_image_url` | Flag Image Url      | `char`      |     |       |           |
| `grouping`       | Separator Format    | `selection` | ✅  | ✅    |           |
| `id`             | ID                  | `integer`   |     | ✅    |           |
| `iso_code`       | ISO code            | `char`      |     | ✅    |           |
| `name`           | Name                | `char`      | ✅  | ✅    |           |
| `thousands_sep`  | Thousands Separator | `char`      |     | ✅    |           |
| `time_format`    | Time Format         | `selection` | ✅  | ✅    |           |
| `url_code`       | URL Code            | `char`      | ✅  | ✅    |           |
| `week_start`     | First Day of Week   | `selection` | ✅  | ✅    |           |
| `write_date`     | Last Updated on     | `datetime`  |     | ✅    |           |
| `write_uid`      | Last Updated by     | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                | Group                | Perms     |
| ------------------- | -------------------- | --------- |
| res_lang group_user | Role / Administrator | `R/W/C/D` |
| res_lang group_all  | Role / Portal        | `R`       |
| res_lang group_all  | Role / Public        | `R`       |
| res_lang group_all  | Role / User          | `R`       |

### 🗃️ `survey.invite` — Survey Invitation Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                         | Label                                    | Type        | Req | Store | Relation       |
| ----------------------------- | ---------------------------------------- | ----------- | --- | ----- | -------------- |
| `attachment_ids`              | Attachments                              | `many2many` |     | ✅    | ir.attachment  |
| `author_id`                   | Author                                   | `many2one`  |     | ✅    | res.partner    |
| `body`                        | Contents                                 | `html`      |     | ✅    |                |
| `body_has_template_value`     | Body content is the same as the template | `boolean`   |     |       |                |
| `can_edit_body`               | Can Edit Body                            | `boolean`   |     |       |                |
| `create_date`                 | Created on                               | `datetime`  |     | ✅    |                |
| `create_uid`                  | Created by                               | `many2one`  |     | ✅    | res.users      |
| `deadline`                    | Answer deadline                          | `datetime`  |     | ✅    |                |
| `display_name`                | Display Name                             | `char`      |     |       |                |
| `emails`                      | Additional emails                        | `text`      |     | ✅    |                |
| `existing_emails`             | Existing emails                          | `text`      |     |       |                |
| `existing_mode`               | Handle existing                          | `selection` | ✅  | ✅    |                |
| `existing_partner_ids`        | Existing Partner                         | `many2many` |     |       | res.partner    |
| `existing_text`               | Resend Comment                           | `text`      |     |       |                |
| `id`                          | ID                                       | `integer`   |     | ✅    |                |
| `is_mail_template_editor`     | Is Editor                                | `boolean`   |     |       |                |
| `lang`                        | Language                                 | `char`      |     | ✅    |                |
| `mail_server_id`              | Outgoing mail server                     | `many2one`  |     | ✅    | ir.mail_server |
| `partner_ids`                 | Recipients                               | `many2many` |     | ✅    | res.partner    |
| `render_model`                | Rendering Model                          | `char`      |     |       |                |
| `send_email`                  | Send Email                               | `boolean`   |     |       |                |
| `subject`                     | Subject                                  | `char`      |     | ✅    |                |
| `survey_access_mode`          | Access Mode                              | `selection` |     |       |                |
| `survey_id`                   | Survey                                   | `many2one`  | ✅  | ✅    | survey.survey  |
| `survey_start_url`            | Survey URL                               | `char`      |     |       |                |
| `survey_users_can_signup`     | Users can signup                         | `boolean`   |     |       |                |
| `survey_users_login_required` | Require Login                            | `boolean`   |     |       |                |
| `template_id`                 | Mail Template                            | `many2one`  |     | ✅    | mail.template  |
| `write_date`                  | Last Updated on                          | `datetime`  |     | ✅    |                |
| `write_uid`                   | Last Updated by                          | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                 | Group          | Perms   |
| -------------------- | -------------- | ------- |
| access.survey.invite | Surveys / User | `R/W/C` |

**Record Rules:**

- **Survey invite: officer: unrestricted or in restricted users** (28) `R/W/C`
  - Domain:
    `['|',  ('survey_id.restrict_user_ids', 'in', user.id),             ('survey_id.restrict_user_ids', '=', False)]`
- **Survey invite: manager: all** (29) `R/W/C`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `survey.question.answer` — Survey Label

A preconfigured answer for a question. This model stores values used for

      * simple choice, multiple choice: proposed values for the selection /
        radio;
      * matrix: row and column values;

**Fields:**

| Field                  | Label                    | Type        | Req | Store | Relation        |
| ---------------------- | ------------------------ | ----------- | --- | ----- | --------------- |
| `answer_score`         | Score                    | `float`     |     | ✅    |                 |
| `create_date`          | Created on               | `datetime`  |     | ✅    |                 |
| `create_uid`           | Created by               | `many2one`  |     | ✅    | res.users       |
| `display_name`         | Display Name             | `char`      |     |       |                 |
| `generate_lead`        | Lead creation            | `boolean`   |     | ✅    |                 |
| `id`                   | ID                       | `integer`   |     | ✅    |                 |
| `is_correct`           | Correct                  | `boolean`   |     | ✅    |                 |
| `matrix_question_id`   | Question (as matrix row) | `many2one`  |     | ✅    | survey.question |
| `question_id`          | Question                 | `many2one`  |     | ✅    | survey.question |
| `question_type`        | Question Type            | `selection` |     |       |                 |
| `scoring_type`         | Scoring Type             | `selection` |     |       |                 |
| `sequence`             | Label Sequence order     | `integer`   |     | ✅    |                 |
| `value`                | Suggested value          | `char`      |     | ✅    |                 |
| `value_image`          | Image                    | `binary`    |     | ✅    |                 |
| `value_image_filename` | Image Filename           | `char`      |     | ✅    |                 |
| `value_label`          | Value Label              | `char`      |     |       |                 |
| `write_date`           | Last Updated on          | `datetime`  |     | ✅    |                 |
| `write_uid`            | Last Updated by          | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                                  | Group                   | Perms     |
| ------------------------------------- | ----------------------- | --------- |
| survey.question.answer.survey.user    | Surveys / User          | `R/W/C/D` |
| survey.question.answer.survey.manager | Surveys / Administrator | `R/W/C/D` |
| survey.question.answer.user           | Role / User             | `-`       |
| survey.question.answer.all            | Everyone                | `-`       |

**Record Rules:**

- **Survey question answer: manager: all** (29) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Survey question answer: officer: unrestricted survey or in restricted users** (28)
  `R/W/C/D`
  - Domain:
    `[             '|',                 '|', ('question_id.survey_id.restrict_user_ids', 'in', user.id), ('matrix_question_id.survey_id.restrict_user_ids', 'in', user.id),                 '|', ('question_id.survey_id.restrict_user_ids', '=', False), ('matrix_question_id.survey_id.restrict_user_ids', '=', False)]         `

### 🗃️ `survey.question` — Survey Question

Questions that will be asked in a survey.

        Each question can have one of more suggested answers (eg. in case of
        multi-answer checkboxes, radio buttons...).

        Technical note:

        survey.question is also the model used for the survey's pages (with the "is_page" field set to True).

        A page corresponds to a "section" in the interface, and the fact that it separates the survey in
        actual pages in the interface depends on the "questions_layout" parameter on the survey.survey model.
        Pages are also used when randomizing questions. The randomization can happen within a "page".

        Using the same model for questions and pages allows to put all the pages and questions together in a o2m field
        (see survey.survey.question_and_page_ids) on the view side and easily reorganize your survey by dragging the
        items around.

        It also removes on level of encoding by directly having 'Add a page' and 'Add a question'
        links on the list view of questions, enabling a faster encoding.

        However, this has the downside of making the code reading a little bit more complicated.
        Efforts were made at the model level to create computed fields so that the use of these models
        still seems somewhat logical. That means:
        - A survey still has "page_ids" (question_and_page_ids filtered on is_page = True)
        - These "page_ids" still have question_ids (questions located between this page and the next)
        - These "question_ids" still have a "page_id"

        That makes the use and display of these information at view and controller levels easier to understand.

**Fields:**

| Field                                    | Label                           | Type        | Req | Store | Relation               |
| ---------------------------------------- | ------------------------------- | ----------- | --- | ----- | ---------------------- |
| `allowed_triggering_question_ids`        | Allowed Triggering Questions    | `many2many` |     |       | survey.question        |
| `answer_date`                            | Correct date answer             | `date`      |     | ✅    |                        |
| `answer_datetime`                        | Correct datetime answer         | `datetime`  |     | ✅    |                        |
| `answer_numerical_box`                   | Correct numerical answer        | `float`     |     | ✅    |                        |
| `answer_score`                           | Score                           | `float`     |     | ✅    |                        |
| `background_image`                       | Background Image                | `binary`    |     | ✅    |                        |
| `background_image_url`                   | Background Url                  | `char`      |     |       |                        |
| `comment_count_as_answer`                | Comment is an answer            | `boolean`   |     | ✅    |                        |
| `comments_allowed`                       | Show Comments Field             | `boolean`   |     | ✅    |                        |
| `comments_message`                       | Comment Message                 | `char`      |     | ✅    |                        |
| `constr_error_msg`                       | Error message                   | `char`      |     | ✅    |                        |
| `constr_mandatory`                       | Mandatory Answer                | `boolean`   |     | ✅    |                        |
| `create_date`                            | Created on                      | `datetime`  |     | ✅    |                        |
| `create_uid`                             | Created by                      | `many2one`  |     | ✅    | res.users              |
| `description`                            | Description                     | `html`      |     | ✅    |                        |
| `display_name`                           | Display Name                    | `char`      |     |       |                        |
| `generate_lead`                          | Lead Generating                 | `boolean`   |     |       |                        |
| `has_image_only_suggested_answer`        | Has image only suggested answer | `boolean`   |     |       |                        |
| `id`                                     | ID                              | `integer`   |     | ✅    |                        |
| `is_page`                                | Is a page?                      | `boolean`   |     | ✅    |                        |
| `is_placed_before_trigger`               | Is misplaced?                   | `boolean`   |     |       |                        |
| `is_scored_question`                     | Scored                          | `boolean`   |     | ✅    |                        |
| `is_time_customized`                     | Customized speed rewards        | `boolean`   |     | ✅    |                        |
| `is_time_limited`                        | The question is limited in time | `boolean`   |     | ✅    |                        |
| `matrix_row_ids`                         | Matrix Rows                     | `one2many`  |     | ✅    | survey.question.answer |
| `matrix_subtype`                         | Matrix Type                     | `selection` |     | ✅    |                        |
| `page_id`                                | Page                            | `many2one`  |     | ✅    | survey.question        |
| `question_ids`                           | Questions                       | `one2many`  |     |       | survey.question        |
| `question_placeholder`                   | Placeholder                     | `char`      |     | ✅    |                        |
| `questions_selection`                    | Question Selection              | `selection` |     |       |                        |
| `question_type`                          | Question Type                   | `selection` |     | ✅    |                        |
| `random_questions_count`                 | # Questions Randomly Picked     | `integer`   |     | ✅    |                        |
| `save_as_email`                          | Save as user email              | `boolean`   |     | ✅    |                        |
| `save_as_nickname`                       | Save as user nickname           | `boolean`   |     | ✅    |                        |
| `scale_max`                              | Scale Maximum Value             | `integer`   |     | ✅    |                        |
| `scale_max_label`                        | Scale Maximum Label             | `char`      |     | ✅    |                        |
| `scale_mid_label`                        | Scale Middle Label              | `char`      |     | ✅    |                        |
| `scale_min`                              | Scale Minimum Value             | `integer`   |     | ✅    |                        |
| `scale_min_label`                        | Scale Minimum Label             | `char`      |     | ✅    |                        |
| `scoring_type`                           | Scoring Type                    | `selection` |     |       |                        |
| `sequence`                               | Sequence                        | `integer`   |     | ✅    |                        |
| `session_available`                      | Live Session available          | `boolean`   |     |       |                        |
| `suggested_answer_ids`                   | Types of answers                | `one2many`  |     | ✅    | survey.question.answer |
| `survey_id`                              | Survey                          | `many2one`  |     | ✅    | survey.survey          |
| `survey_session_speed_rating`            | Reward quick answers            | `boolean`   |     |       |                        |
| `survey_session_speed_rating_time_limit` | General Time limit (seconds)    | `integer`   |     |       |                        |
| `survey_type`                            | Survey Type                     | `selection` |     |       |                        |
| `time_limit`                             | Time limit (seconds)            | `integer`   |     | ✅    |                        |
| `title`                                  | Title                           | `char`      | ✅  | ✅    |                        |
| `triggering_answer_ids`                  | Triggering Answers              | `many2many` |     | ✅    | survey.question.answer |
| `triggering_question_ids`                | Triggering Questions            | `many2many` |     |       | survey.question        |
| `user_input_line_ids`                    | Answers                         | `one2many`  |     | ✅    | survey.user_input.line |
| `validation_email`                       | Input must be an email          | `boolean`   |     | ✅    |                        |
| `validation_error_msg`                   | Validation Error                | `char`      |     | ✅    |                        |
| `validation_length_max`                  | Maximum Text Length             | `integer`   |     | ✅    |                        |
| `validation_length_min`                  | Minimum Text Length             | `integer`   |     | ✅    |                        |
| `validation_max_date`                    | Maximum Date                    | `date`      |     | ✅    |                        |
| `validation_max_datetime`                | Maximum Datetime                | `datetime`  |     | ✅    |                        |
| `validation_max_float_value`             | Maximum value                   | `float`     |     | ✅    |                        |
| `validation_min_date`                    | Minimum Date                    | `date`      |     | ✅    |                        |
| `validation_min_datetime`                | Minimum Datetime                | `datetime`  |     | ✅    |                        |
| `validation_min_float_value`             | Minimum value                   | `float`     |     | ✅    |                        |
| `validation_required`                    | Validate entry                  | `boolean`   |     | ✅    |                        |
| `write_date`                             | Last Updated on                 | `datetime`  |     | ✅    |                        |
| `write_uid`                              | Last Updated by                 | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                           | Group                   | Perms     |
| ------------------------------ | ----------------------- | --------- |
| survey.question.survey.user    | Surveys / User          | `R/W/C/D` |
| survey.question.survey.manager | Surveys / Administrator | `R/W/C/D` |
| survey.question.user           | Role / User             | `-`       |
| survey.question.all            | Everyone                | `-`       |

**Record Rules:**

- **Survey question: manager: all** (29) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Survey question: officer: unrestricted survey or in restricted users** (28)
  `R/W/C/D`
  - Domain:
    `[             '|', ('survey_id.restrict_user_ids', 'in', user.id), ('survey_id.restrict_user_ids', '=', False)]`

### 🗃️ `survey.user_input.line` — Survey User Input Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                 | Label            | Type        | Req | Store | Relation               |
| --------------------- | ---------------- | ----------- | --- | ----- | ---------------------- |
| `answer_is_correct`   | Correct          | `boolean`   |     | ✅    |                        |
| `answer_score`        | Score            | `float`     |     | ✅    |                        |
| `answer_type`         | Answer Type      | `selection` |     | ✅    |                        |
| `create_date`         | Created on       | `datetime`  |     | ✅    |                        |
| `create_uid`          | Created by       | `many2one`  |     | ✅    | res.users              |
| `display_name`        | Display Name     | `char`      |     |       |                        |
| `id`                  | ID               | `integer`   |     | ✅    |                        |
| `lang_id`             | Language         | `many2one`  |     |       | res.lang               |
| `matrix_row_id`       | Row answer       | `many2one`  |     | ✅    | survey.question.answer |
| `page_id`             | Section          | `many2one`  |     |       | survey.question        |
| `question_id`         | Question         | `many2one`  | ✅  | ✅    | survey.question        |
| `question_sequence`   | Sequence         | `integer`   |     | ✅    |                        |
| `skipped`             | Skipped          | `boolean`   |     | ✅    |                        |
| `suggested_answer_id` | Suggested answer | `many2one`  |     | ✅    | survey.question.answer |
| `survey_id`           | Survey           | `many2one`  |     | ✅    | survey.survey          |
| `user_input_id`       | User Input       | `many2one`  | ✅  | ✅    | survey.user_input      |
| `value_char_box`      | Text answer      | `char`      |     | ✅    |                        |
| `value_date`          | Date answer      | `date`      |     | ✅    |                        |
| `value_datetime`      | Datetime answer  | `datetime`  |     | ✅    |                        |
| `value_numerical_box` | Numerical answer | `float`     |     | ✅    |                        |
| `value_scale`         | Scale value      | `integer`   |     | ✅    |                        |
| `value_text_box`      | Free Text answer | `text`      |     | ✅    |                        |
| `write_date`          | Last Updated on  | `datetime`  |     | ✅    |                        |
| `write_uid`           | Last Updated by  | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                                  | Group                   | Perms     |
| ------------------------------------- | ----------------------- | --------- |
| survey.user_input.line.survey.user    | Surveys / User          | `R`       |
| survey.user_input.line.survey.manager | Surveys / Administrator | `R/W/C/D` |
| survey.user_input.line.user           | Role / User             | `-`       |
| survey.user_input.line.all            | Everyone                | `-`       |

**Record Rules:**

- **Survey user input line: manager: all non specialized surveys** (29) `R/W/C/D`
  - Domain:
    `[('survey_id.survey_type', 'in', ('assessment', 'custom', 'live_session', 'survey'))]`
- **Survey user input line: officer: unrestricted survey or in restricted users** (28)
  `R/W/C/D`
  - Domain:
    `[             '&', ('survey_id.survey_type', 'in', ('assessment', 'custom', 'live_session', 'survey')),             '|', ('survey_id.restrict_user_ids', 'in', user.id),                  ('survey_id.restrict_user_ids', '=', False)]`
