---
title: "Discuss"
module: "mail"
state: "installed"
version: "19.0.1.19"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/app/discuss"
license: "LGPL-3"
category: "Discuss"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_______, odoo/app]
---

# 🟢 Discuss

> **Module:** `mail` | **Version:** `19.0.1.19` **Category:** Discuss | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** https://www.odoo.com/app/discuss

## 🔗 Dependencies

[[base]] [[base_setup]] [[bus]] [[web_tour]] [[html_editor]]

## 📖 Description

# Chat, mail gateway and private channel.

Communicate with your colleagues/customers/guest within Odoo.

## Discuss/Chat

User-friendly "Discuss" features that allows one 2 one or group communication (text
chat/voice call/video call), invite guests and share documents with them, all real-time.

## Mail gateway

Sending information and documents made simplified. You can send emails from Odoo itself,
and that too with great possibilities. For example, design a beautiful email template
for the invoices, and use the same for all your customers, no need to do the same
exercise every time.

## Chatter

Do all the contextual conversation on a document. For example on an applicant, directly
post an update to send email to the applicant, schedule the next interview call, attach
the contract, add HR officer to the follower list to notify them for important
events(with help of subtypes),...

# Retrieve incoming email on POP/IMAP servers.

Enter the parameters of your POP/IMAP account(s), and any incoming emails on these
accounts will be automatically downloaded into your Odoo system. All
POP3/IMAP-compatible servers are supported, included those that require an encrypted
SSL/TLS connection. This can be used to easily create email-based workflows for many
email-enabled Odoo documents, such as:

---

> - CRM Leads/Opportunities
> - CRM Claims
> - Project Issues
> - Project Tasks
> - Human Resource Recruitment (Applicants)

Just install the relevant application, and you can assign any of these document types
(Leads, Project Issues) to your incoming email accounts. New emails will automatically
spawn new documents of the chosen type, so it's a snap to create a mailbox-to-Odoo
integration. Even better: these documents directly act as mini conversations
synchronized by email. You can reply from within Odoo, and the answers will
automatically be collected when they come back, and attached to the same _conversation_
document. For more specific needs, you may also assign custom-defined actions
(technically: Server Actions) to be triggered for each incoming mail.

## 🖥️ UI Components

### Menus

- `Discuss`
- `Discuss/Channels`
- `Discuss/Configuration`
- `Discuss/Configuration/Canned Responses`
- `Discuss/Configuration/Notifications`
- `Discuss/Configuration/Roles`
- `Discuss/Configuration/Voice & Video`
- `Discuss/Discuss`
- `Discuss/Integrations`
- `Discuss/Technical`
- `Discuss/Technical/Call History`
- `Settings/Technical/Activities`
- `Settings/Technical/Activities/Activity Overview`
- `Settings/Technical/Activities/Activity Plans`
- `Settings/Technical/Activities/Activity Types`
- `Settings/Technical/Discuss`
- `Settings/Technical/Discuss/Email Blacklist`
- `Settings/Technical/Discuss/Followers`
- `Settings/Technical/Discuss/GIF favorite`
- `Settings/Technical/Discuss/Guests`
- `Settings/Technical/Discuss/ICE Servers`
- `Settings/Technical/Discuss/Link Previews`
- `Settings/Technical/Discuss/Message Reactions`
- `Settings/Technical/Discuss/Messages`
- `Settings/Technical/Discuss/Notifications`
- `Settings/Technical/Discuss/RTC sessions`
- `Settings/Technical/Discuss/Scheduled Messages`
- `Settings/Technical/Discuss/Subtypes`
- `Settings/Technical/Discuss/Tracking Values`
- `Settings/Technical/Discuss/User Settings`
- `Settings/Technical/Email/Alias Domains`
- `Settings/Technical/Email/Aliases`
- `Settings/Technical/Email/Channels`
- `Settings/Technical/Email/Channels/Members`
- `Settings/Technical/Email/Email Templates`
- `Settings/Technical/Email/Emails`
- `Settings/Technical/Email/Incoming Mail Servers`
- `Settings/Technical/Email/Mail Gateway Allowed`

### Views

- `* INHERIT Mail: mail notification layout with responsible signature (user_id of the record) (qweb)`
- `* INHERIT ir.actions.server.form (form)`
- `* INHERIT ir.cron.view.form.inherit (form)`
- `* INHERIT ir.filters.view.form.inherit (form)`
- `* INHERIT ir.filters.view.tree.inherit (list)`
- `* INHERIT ir.mail_server.view.form.inherit.mail (form)`
- `* INHERIT ir.model form (form)`
- `* INHERIT ir.model search (search)`
- `* INHERIT ir.model.fields form (form)`
- `* INHERIT mail.activity.plan.view.form.fixed.model (form)`
- `* INHERIT mail.activity.plan.view.list.detailed (list)`
- `* INHERIT mail.activity.view.form (form)`
- `* INHERIT mail.activity.view.list.open.target (list)`
- `* INHERIT mail.activity.view.list.without.record.access (list)`
- `* INHERIT mail.followers.list.edit.form (form)`
- `* INHERIT mail_notification_invite (qweb)`
- `* INHERIT mail_notification_multi_invite (qweb)`
- `* INHERIT res.company.view.form.inherit.mail (form)`
- `* INHERIT res.config.settings.view.form.inherit.mail (form)`
- `* INHERIT res.partner.view.form.inherit.mail (form)`
- `* INHERIT res.partner.view.kanban.inherit.mail (kanban)`
- `* INHERIT res.partner.view.list.inherit.mail (list)`
- `* INHERIT res.partner.view.search.inherit.mail (search)`
- `* INHERIT res.users.form.mail (form)`
- `* INHERIT res.users.preferences.form.mail (form)`
- `Activity schedule (form)`
- `Alert Security Update (qweb)`
- `Attachment links (qweb)`
- `Discuss Public Template (qweb)`
- `Mail: mail notification layout template (qweb)`
- `discuss.call.history.view.form (form)`
- `discuss.call.history.view.list (list)`
- `discuss.channel.form (form)`
- `discuss.channel.kanban (kanban)`
- `discuss.channel.list (list)`
- `discuss.channel.list (list)`
- `discuss.channel.member.form (form)`
- `discuss.channel.member.list (list)`
- `discuss.channel.rtc.session.form (form)`
- `discuss.channel.rtc.session.list (list)`
- `discuss.channel.rtc.session.search (search)`
- `discuss.channel.search (search)`
- `discuss.gif.favorite.form (form)`
- `discuss.gif.favorite.list (list)`
- `discuss_channel_invitation_template (qweb)`
- `email.template.form (form)`
- `email.template.list (list)`
- `email.template.search (search)`
- `fetchmail.server.form (form)`
- `fetchmail.server.list (list)`
- `fetchmail.server.search (search)`
- `ir.attachment kanban (kanban)`
- `mail.activity.plan.template.view.form (form)`
- `mail.activity.plan.template.view.list (list)`
- `mail.activity.plan.view.form (form)`
- `mail.activity.plan.view.kanban (kanban)`
- `mail.activity.plan.view.list (list)`
- `mail.activity.plan.view.search (search)`
- `mail.activity.type.search (search)`
- `mail.activity.type.view.form (form)`
- `mail.activity.type.view.kanban (kanban)`
- `mail.activity.type.view.list (list)`
- `mail.activity.view.calendar (calendar)`
- `mail.activity.view.form.popup (form)`
- `mail.activity.view.form.without.record.access (form)`
- `mail.activity.view.kanban.open.target (kanban)`
- `mail.activity.view.list (list)`
- `mail.activity.view.search (search)`
- `mail.alias.domain.view.form (form)`
- `mail.alias.domain.view.list (list)`
- `mail.alias.domain.view.search (search)`
- `mail.alias.view.form (form)`
- `mail.alias.view.list (list)`
- `mail.alias.view.search (search)`
- `mail.blacklist.remove.form (form)`
- `mail.blacklist.view.form (form)`
- `mail.blacklist.view.list (list)`
- `mail.blacklist.view.search (search)`
- `mail.canned.response.form (form)`
- `mail.canned.response.kanban (kanban)`
- `mail.canned.response.list (list)`
- `mail.canned.response.view.search (search)`
- `mail.compose.message.form (form)`
- `mail.compose.message.view.form.template.save (form)`
- `mail.followers.edit.form (form)`
- `mail.followers.form (form)`
- `mail.followers.list (list)`
- `mail.gateway.allowed.view.list (list)`
- `mail.gateway.allowed.view.search (search)`
- `mail.guest.form (form)`
- `mail.guest.list (list)`
- `mail.ice.server.form (form)`
- `mail.ice.server.kanban (kanban)`
- `mail.ice.server.list (list)`
- `mail.ice.server.search (search)`
- `mail.link.preview.form (form)`
- `mail.link.preview.list (list)`
- `mail.mail.form (form)`
- `mail.mail.list (list)`
- `mail.mail.search (search)`
- `mail.message.link.preview.list (list)`
- `mail.message.list (list)`
- `mail.message.reaction.form (form)`
- `mail.message.reaction.list (list)`
- `mail.message.schedule.view.form (form)`
- `mail.message.schedule.view.list (list)`
- `mail.message.schedule.view.search (search)`
- `mail.message.search (search)`
- `mail.message.subtype.form (form)`
- `mail.message.subtype.list (list)`
- `mail.message.subtype.view.search (search)`
- `mail.message.view.form (form)`
- `mail.message_document_unfollowed (qweb)`
- `mail.notification.view.form (form)`
- `mail.notification.view.list (list)`
- `mail.public_layout (qweb)`
- `mail.scheduled.message.view.form (form)`
- `mail.template.preview.view.form (form)`
- `mail.template.reset.view.form (form)`
- `mail.tracking.value.form (form)`
- `mail.tracking.value.list (list)`
- `mail_bounce_alias_security (qweb)`
- `mail_bounce_catchall (qweb)`
- `mail_notification_light (qweb)`
- `message_activity_assigned (qweb)`
- `message_activity_done (qweb)`
- `message_notification_limit_email (qweb)`
- `message_notification_out_of_office (qweb)`
- `message_origin_link (qweb)`
- `message_user_assigned (qweb)`
- `notification_preview (qweb)`
- `res.partner.activity (activity)`
- `res.role.form (form)`
- `res.role.list (list)`
- `res.role.view.search (search)`
- `res.users.settings.form (form)`
- `res.users.settings.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**78 model(s) defined by this module:**

### 🗃️ `res.company` — Companies

> 📧 Mail Thread

Advanced orchestration layer for exchange rate management

**Fields:**

| Field                                                | Label                                                  | Type                    | Req | Store | Relation                    |
| ---------------------------------------------------- | ------------------------------------------------------ | ----------------------- | --- | ----- | --------------------------- |
| `account_cash_basis_base_account_id`                 | Base Tax Received Account                              | `many2one`              |     | ✅    | account.account             |
| `account_default_pos_receivable_account_id`          | Default PoS Receivable Account                         | `many2one`              |     | ✅    | account.account             |
| `account_discount_expense_allocation_id`             | Separate account for expense discount                  | `many2one`              |     | ✅    | account.account             |
| `account_discount_income_allocation_id`              | Separate account for income discount                   | `many2one`              |     | ✅    | account.account             |
| `account_enabled_tax_country_ids`                    | l10n-used countries                                    | `many2many`             |     |       | res.country                 |
| `account_fiscal_country_group_codes`                 | Account Fiscal Country Group Codes                     | `json`                  |     |       |                             |
| `account_fiscal_country_id`                          | Fiscal Country                                         | `many2one`              |     | ✅    | res.country                 |
| `account_journal_early_pay_discount_gain_account_id` | Cash Discount Write-Off Gain Account                   | `many2one`              |     | ✅    | account.account             |
| `account_journal_early_pay_discount_loss_account_id` | Cash Discount Write-Off Loss Account                   | `many2one`              |     | ✅    | account.account             |
| `account_journal_suspense_account_id`                | Journal Suspense Account                               | `many2one`              |     | ✅    | account.account             |
| `account_opening_date`                               | Opening Entry                                          | `date`                  |     | ✅    |                             |
| `account_opening_journal_id`                         | Opening Journal                                        | `many2one`              |     |       | account.journal             |
| `account_opening_move_id`                            | Opening Journal Entry                                  | `many2one`              |     | ✅    | account.move                |
| `account_price_include`                              | Default Sales Price Include                            | `selection`             | ✅  | ✅    |                             |
| `account_production_wip_account_id`                  | Production WIP Account                                 | `many2one`              |     | ✅    | account.account             |
| `account_production_wip_overhead_account_id`         | Production WIP Overhead Account                        | `many2one`              |     | ✅    | account.account             |
| `account_purchase_receipt_fiscal_position_id`        | Default Purchase Receipt Fiscal Position               | `many2one`              |     | ✅    | account.fiscal.position     |
| `account_purchase_tax_id`                            | Default Purchase Tax                                   | `many2one`              |     | ✅    | account.tax                 |
| `account_sale_tax_id`                                | Default Sale Tax                                       | `many2one`              |     | ✅    | account.tax                 |
| `account_stock_journal_id`                           | Stock Journal                                          | `many2one`              |     | ✅    | account.journal             |
| `account_stock_valuation_id`                         | Stock Valuation Account                                | `many2one`              |     | ✅    | account.account             |
| `account_storno`                                     | Storno accounting                                      | `boolean`               |     | ✅    |                             |
| `account_use_credit_limit`                           | Sales Credit Limit                                     | `boolean`               |     | ✅    |                             |
| `accreditation`                                      | Accreditation                                          | `text`                  |     | ✅    |                             |
| `active`                                             | Active                                                 | `boolean`               |     | ✅    |                             |
| `affiliation_ids`                                    | Affiliation Board                                      | `one2many`              |     | ✅    | op.board.affiliation        |
| `alias_domain_id`                                    | Email Domain                                           | `many2one`              |     | ✅    | mail.alias.domain           |
| `all_child_ids`                                      | All Child                                              | `one2many`              |     | ✅    | res.company                 |
| `anglo_saxon_accounting`                             | Use anglo-saxon accounting                             | `boolean`               |     | ✅    |                             |
| `annual_inventory_day`                               | Day of the month                                       | `integer`               |     | ✅    |                             |
| `annual_inventory_month`                             | Annual Inventory Month                                 | `selection`             |     | ✅    |                             |
| `approval_authority`                                 | Approval Authority                                     | `text`                  |     | ✅    |                             |
| `automatic_entry_default_journal_id`                 | Automatic Entry Default Journal                        | `many2one`              |     | ✅    | account.journal             |
| `autopost_bills`                                     | Auto-validate bills                                    | `boolean`               |     | ✅    |                             |
| `bank_account_code_prefix`                           | Prefix of the bank accounts                            | `char`                  |     | ✅    |                             |
| `bank_ids`                                           | Banks                                                  | `one2many`              |     |       | res.partner.bank            |
| `bank_journal_ids`                                   | Bank Journals                                          | `one2many`              |     | ✅    | account.journal             |
| `batch_payment_sequence_id`                          | Batch Payment Sequence                                 | `many2one`              |     | ✅    | ir.sequence                 |
| `bounce_email`                                       | Bounce Email                                           | `char`                  |     |       |                             |
| `bounce_formatted`                                   | Bounce                                                 | `char`                  |     |       |                             |
| `cash_account_code_prefix`                           | Prefix of the cash accounts                            | `char`                  |     | ✅    |                             |
| `catchall_email`                                     | Catchall Email                                         | `char`                  |     |       |                             |
| `catchall_formatted`                                 | Catchall                                               | `char`                  |     |       |                             |
| `chart_template`                                     | Chart Template                                         | `selection`             |     | ✅    |                             |
| `child_company_count`                                | Child Company Count                                    | `integer`               |     |       |                             |
| `child_ids`                                          | Branches                                               | `one2many`              |     | ✅    | res.company                 |
| `city`                                               | City                                                   | `char`                  |     |       |                             |
| `color`                                              | Color Index                                            | `integer`               |     |       |                             |
| `company_batch_count`                                | Company Batch Count                                    | `integer`               |     |       |                             |
| `company_course_count`                               | Company Course Count                                   | `integer`               |     |       |                             |
| `company_details`                                    | Company Details                                        | `html`                  |     | ✅    |                             |
| `company_expense_allowed_payment_method_line_ids`    | Payment methods available for expenses paid by company | `many2many`             |     | ✅    | account.payment.method.line |
| `company_registry`                                   | Company ID                                             | `char`                  |     |       |                             |
| `company_registry_placeholder`                       | Company Registry Placeholder                           | `char`                  |     |       |                             |
| `company_student_count`                              | Company Student Count                                  | `integer`               |     |       |                             |
| `company_subject_count`                              | Company Subject Count                                  | `integer`               |     |       |                             |
| `company_vat_placeholder`                            | Company Vat Placeholder                                | `char`                  |     |       |                             |
| `contract_expiration_notice_period`                  | Contract Expiry Notice Period                          | `integer`               |     | ✅    |                             |
| `cost_method`                                        | Cost Method                                            | `selection`             | ✅  | ✅    |                             |
| `country_code`                                       | Country Code                                           | `char`                  |     |       |                             |
| `country_id`                                         | Country                                                | `many2one`              |     |       | res.country                 |
| `create_date`                                        | Created on                                             | `datetime`              |     | ✅    |                             |
| `create_uid`                                         | Created by                                             | `many2one`              |     | ✅    | res.users                   |
| `currency_exchange_journal_id`                       | Exchange Gain or Loss Journal                          | `many2one`              |     | ✅    | account.journal             |
| `currency_id`                                        | Currency                                               | `many2one`              | ✅  | ✅    | res.currency                |
| `custom_bg_image`                                    | Custom Background Image                                | `binary`                |     | ✅    |                             |
| `dashboard_background`                               | Dashboard Background                                   | `binary`                |     | ✅    |                             |
| `days_to_purchase`                                   | Days to Purchase                                       | `float`                 |     | ✅    |                             |
| `default_cash_difference_expense_account_id`         | Cash Difference Expense                                | `many2one`              |     | ✅    | account.account             |
| `default_cash_difference_income_account_id`          | Cash Difference Income                                 | `many2one`              |     | ✅    | account.account             |
| `default_from_email`                                 | Default From                                           | `char`                  |     |       |                             |
| `display_account_storno`                             | Display Account Storno                                 | `boolean`               |     |       |                             |
| `display_invoice_amount_total_words`                 | Total amount of invoice in letters                     | `boolean`               |     | ✅    |                             |
| `display_invoice_tax_company_currency`               | Taxes in company currency                              | `boolean`               |     | ✅    |                             |
| `display_name`                                       | Display Name                                           | `char`                  |     |       |                             |
| `domestic_fiscal_position_id`                        | Domestic Fiscal Position                               | `many2one`              |     | ✅    | account.fiscal.position     |
| `downpayment_account_id`                             | Downpayment Account                                    | `many2one`              |     | ✅    | account.account             |
| `email`                                              | Email                                                  | `char`                  |     | ✅    |                             |
| `email_formatted`                                    | Formatted Email                                        | `char`                  |     |       |                             |
| `email_primary_color`                                | Email Button Text                                      | `char`                  |     | ✅    |                             |
| `email_secondary_color`                              | Email Button Color                                     | `char`                  |     | ✅    |                             |
| `employee_properties_definition`                     | Employee Properties                                    | `properties_definition` |     | ✅    |                             |
| `error_tolerance_threshold`                          | Error Tolerance                                        | `float`                 |     | ✅    |                             |
| `expects_chart_of_accounts`                          | Expects a Chart of Accounts                            | `boolean`               |     | ✅    |                             |
| `expense_account_id`                                 | Expense Account                                        | `many2one`              |     | ✅    | account.account             |
| `expense_accrual_account_id`                         | Expense Accrual Account                                | `many2one`              |     | ✅    | account.account             |
| `expense_currency_exchange_account_id`               | Loss Exchange Rate Account                             | `many2one`              |     | ✅    | account.account             |
| `expense_journal_id`                                 | Default Expense Journal                                | `many2one`              |     | ✅    | account.journal             |
| `external_report_layout_id`                          | Document Template                                      | `many2one`              |     | ✅    | ir.ui.view                  |
| `fiscal_position_ids`                                | Fiscal Position                                        | `one2many`              |     | ✅    | account.fiscal.position     |
| `fiscalyear_last_day`                                | Fiscalyear Last Day                                    | `integer`               | ✅  | ✅    |                             |
| `fiscalyear_last_month`                              | Fiscalyear Last Month                                  | `selection`             | ✅  | ✅    |                             |
| `fiscalyear_lock_date`                               | Global Lock Date                                       | `date`                  |     | ✅    |                             |
| `font`                                               | Font                                                   | `selection`             |     | ✅    |                             |
| `force_restrictive_audit_trail`                      | Force Audit Trail                                      | `boolean`               |     |       |                             |
| `google_font`                                        | Google Font                                            | `char`                  |     | ✅    |                             |
| `hard_lock_date`                                     | Hard Lock Date                                         | `date`                  |     | ✅    |                             |
| `has_message`                                        | Has Message                                            | `boolean`               |     |       |                             |
| `has_received_warning_stock_sms`                     | Has Received Warning Stock Sms                         | `boolean`               |     | ✅    |                             |
| `horizon_days`                                       | Replenishment Horizon                                  | `float`                 | ✅  | ✅    |                             |
| `hr_presence_control_attendance`                     | Based on attendances                                   | `boolean`               |     | ✅    |                             |
| `hr_presence_control_email`                          | Based on number of emails sent                         | `boolean`               |     | ✅    |                             |
| `hr_presence_control_email_amount`                   | # emails to send                                       | `integer`               |     | ✅    |                             |
| `hr_presence_control_ip`                             | Based on IP Address                                    | `boolean`               |     | ✅    |                             |
| `hr_presence_control_ip_list`                        | Valid IP addresses                                     | `char`                  |     | ✅    |                             |
| `hr_presence_control_login`                          | Based on user status in system                         | `boolean`               |     | ✅    |                             |
| `iap_enrich_auto_done`                               | Enrich Done                                            | `boolean`               |     | ✅    |                             |
| `id`                                                 | ID                                                     | `integer`               |     | ✅    |                             |
| `income_account_id`                                  | Income Account                                         | `many2one`              |     | ✅    | account.account             |
| `income_currency_exchange_account_id`                | Gain Exchange Rate Account                             | `many2one`              |     | ✅    | account.account             |
| `incoterm_id`                                        | Default incoterm                                       | `many2one`              |     | ✅    | account.incoterms           |
| `internal_transit_location_id`                       | Internal Transit Location                              | `many2one`              |     | ✅    | stock.location              |
| `inventory_period`                                   | Inventory Period                                       | `selection`             | ✅  | ✅    |                             |
| `inventory_valuation`                                | Valuation                                              | `selection`             |     | ✅    |                             |
| `invoice_terms`                                      | Default Terms and Conditions                           | `html`                  |     | ✅    |                             |
| `invoice_terms_html`                                 | Default Terms and Conditions as a Web page             | `html`                  |     | ✅    |                             |
| `is_company_details_empty`                           | Is Company Details Empty                               | `boolean`               |     |       |                             |
| `is_hash_verified`                                   | Is Hash Verified                                       | `boolean`               |     | ✅    |                             |
| `is_mail_sent`                                       | Is Mail Sent                                           | `boolean`               |     | ✅    |                             |
| `job_properties_definition`                          | Job Properties                                         | `properties_definition` |     | ✅    |                             |
| `layout_background`                                  | Layout Background                                      | `selection`             | ✅  | ✅    |                             |
| `layout_background_image`                            | Background Image                                       | `binary`                |     | ✅    |                             |
| `link_qr_code`                                       | Display Link QR-code                                   | `boolean`               |     | ✅    |                             |
| `logo`                                               | Company Logo                                           | `binary`                |     |       |                             |
| `logo_web`                                           | Logo Web                                               | `binary`                |     | ✅    |                             |
| `meeting_enterprise_onboard_panel`                   | State of the meeting onboarding step                   | `selection`             |     | ✅    |                             |
| `menu_bg_image`                                      | Apps Menu Footer Image                                 | `binary`                |     | ✅    |                             |
| `message_attachment_count`                           | Attachment Count                                       | `integer`               |     |       |                             |
| `message_follower_ids`                               | Followers                                              | `one2many`              |     | ✅    | mail.followers              |
| `message_has_error`                                  | Message Delivery error                                 | `boolean`               |     |       |                             |
| `message_has_error_counter`                          | Number of errors                                       | `integer`               |     |       |                             |
| `message_has_sms_error`                              | SMS Delivery error                                     | `boolean`               |     |       |                             |
| `message_ids`                                        | Messages                                               | `one2many`              |     | ✅    | mail.message                |
| `message_is_follower`                                | Is Follower                                            | `boolean`               |     |       |                             |
| `message_needaction`                                 | Action Needed                                          | `boolean`               |     |       |                             |
| `message_needaction_counter`                         | Number of Actions                                      | `integer`               |     |       |                             |
| `message_partner_ids`                                | Followers (Partners)                                   | `many2many`             |     |       | res.partner                 |
| `multi_vat_foreign_country_ids`                      | Foreign VAT countries                                  | `many2many`             |     |       | res.country                 |
| `name`                                               | Company Name                                           | `char`                  | ✅  | ✅    |                             |
| `next_execution_timestamp`                           | Next Execution Time                                    | `datetime`              |     | ✅    |                             |
| `nomenclature_id`                                    | Nomenclature                                           | `many2one`              |     | ✅    | barcode.nomenclature        |
| `onboarding_meeting_layout_state`                    | State of the onboarding meeting layout step            | `selection`             |     | ✅    |                             |
| `openeducat_instance_hash_key`                       | OpenEducat Instance Hash Key                           | `char`                  |     | ✅    |                             |
| `openeducat_instance_hash_msg`                       | Instance Hash Key Message                              | `char`                  |     | ✅    |                             |
| `openeducat_instance_key`                            | OpenEducat Instance Key                                | `char`                  |     | ✅    |                             |
| `paperformat_id`                                     | Paper format                                           | `many2one`              |     | ✅    | report.paperformat          |
| `parent_company_id`                                  | Company                                                | `many2one`              |     | ✅    | res.company                 |
| `parent_id`                                          | Parent Company                                         | `many2one`              |     | ✅    | res.company                 |
| `parent_ids`                                         | Parent                                                 | `many2many`             |     |       | res.company                 |
| `parent_path`                                        | Parent Path                                            | `char`                  |     | ✅    |                             |
| `partner_id`                                         | Partner                                                | `many2one`              | ✅  | ✅    | res.partner                 |
| `phone`                                              | Phone                                                  | `char`                  |     | ✅    |                             |
| `po_double_validation`                               | Levels of Approvals                                    | `selection`             |     | ✅    |                             |
| `po_double_validation_amount`                        | Double validation amount                               | `monetary`              |     | ✅    |                             |
| `po_lock`                                            | Purchase Order Modification                            | `selection`             |     | ✅    |                             |
| `portal_confirmation_pay`                            | Online Payment                                         | `boolean`               |     | ✅    |                             |
| `portal_confirmation_sign`                           | Online Signature                                       | `boolean`               |     | ✅    |                             |
| `preloader_option`                                   | Preloader Option                                       | `selection`             |     | ✅    |                             |
| `prepayment_percent`                                 | Prepayment percentage                                  | `float`                 |     | ✅    |                             |
| `price_difference_account_id`                        | Price Difference Account                               | `many2one`              |     | ✅    | account.account             |
| `primary_color`                                      | Primary Color                                          | `char`                  |     | ✅    |                             |
| `purchase_lock_date`                                 | Purchase Lock date                                     | `date`                  |     | ✅    |                             |
| `qr_code`                                            | Display QR-code on invoices                            | `boolean`               |     | ✅    |                             |
| `quick_edit_mode`                                    | Quick encoding                                         | `selection`             |     | ✅    |                             |
| `quotation_validity_days`                            | Default Quotation Validity                             | `integer`               |     | ✅    |                             |
| `rate_provider_selection`                            | Exchange Rate Provider                                 | `selection`             |     | ✅    |                             |
| `rating_ids`                                         | Ratings                                                | `one2many`              |     | ✅    | rating.rating               |
| `report_footer`                                      | Report Footer                                          | `html`                  |     | ✅    |                             |
| `report_header`                                      | Company Tagline                                        | `html`                  |     | ✅    |                             |
| `resource_calendar_id`                               | Default Working Hours                                  | `many2one`              |     | ✅    | resource.calendar           |
| `resource_calendar_ids`                              | Working Hours                                          | `one2many`              |     | ✅    | resource.calendar           |
| `restrictive_audit_trail`                            | Restrictive Audit Trail                                | `boolean`               |     | ✅    |                             |
| `revenue_accrual_account_id`                         | Revenue Accrual Account                                | `many2one`              |     | ✅    | account.account             |
| `root_id`                                            | Root                                                   | `many2one`              |     |       | res.company                 |
| `sale_discount_product_id`                           | Discount Product                                       | `many2one`              |     | ✅    | product.product             |
| `sale_lock_date`                                     | Sales Lock Date                                        | `date`                  |     | ✅    |                             |
| `sale_onboarding_payment_method`                     | Sale onboarding selected payment method                | `selection`             |     | ✅    |                             |
| `sale_order_template_id`                             | Default Sale Template                                  | `many2one`              |     | ✅    | sale.order.template         |
| `secondary_color`                                    | Secondary Color                                        | `char`                  |     | ✅    |                             |
| `security_lead`                                      | Sales Safety Days                                      | `float`                 | ✅  | ✅    |                             |
| `sequence`                                           | Sequence                                               | `integer`               |     | ✅    |                             |
| `sidebar_bg_image`                                   | Sidebar Background                                     | `binary`                |     | ✅    |                             |
| `sidebar_company_logo`                               | Sidebar Logo                                           | `binary`                |     | ✅    |                             |
| `signature`                                          | Signature                                              | `binary`                |     | ✅    |                             |
| `snailmail_color`                                    | Snailmail Color                                        | `boolean`               |     | ✅    |                             |
| `snailmail_cover`                                    | Add a Cover Page                                       | `boolean`               |     | ✅    |                             |
| `snailmail_duplex`                                   | Both sides                                             | `boolean`               |     | ✅    |                             |
| `social_discord`                                     | Discord Account                                        | `char`                  |     | ✅    |                             |
| `social_facebook`                                    | Facebook Account                                       | `char`                  |     | ✅    |                             |
| `social_github`                                      | GitHub Account                                         | `char`                  |     | ✅    |                             |
| `social_instagram`                                   | Instagram Account                                      | `char`                  |     | ✅    |                             |
| `social_linkedin`                                    | LinkedIn Account                                       | `char`                  |     | ✅    |                             |
| `social_tiktok`                                      | TikTok Account                                         | `char`                  |     | ✅    |                             |
| `social_twitter`                                     | X Account                                              | `char`                  |     | ✅    |                             |
| `social_youtube`                                     | Youtube Account                                        | `char`                  |     | ✅    |                             |
| `state_id`                                           | Fed. State                                             | `many2one`              |     |       | res.country.state           |
| `stock_confirmation_type`                            | Stock Confirmation Type                                | `selection`             |     | ✅    |                             |
| `stock_mail_confirmation_template_id`                | Email Template confirmation picking                    | `many2one`              |     | ✅    | mail.template               |
| `stock_move_email_validation`                        | Email Confirmation picking                             | `boolean`               |     | ✅    |                             |
| `stock_sms_confirmation_template_id`                 | SMS Template                                           | `many2one`              |     | ✅    | sms.template                |
| `stock_text_confirmation`                            | Stock Text Confirmation                                | `boolean`               |     | ✅    |                             |
| `street`                                             | Street                                                 | `char`                  |     |       |                             |
| `street2`                                            | Street2                                                | `char`                  |     |       |                             |
| `synchronization_batch_size`                         | Batch Size                                             | `integer`               |     | ✅    |                             |
| `synchronization_frequency`                          | Synchronization Frequency                              | `selection`             |     | ✅    |                             |
| `tax_calculation_rounding_method`                    | Tax Calculation Rounding Method                        | `selection`             |     | ✅    |                             |
| `tax_cash_basis_journal_id`                          | Cash Basis Journal                                     | `many2one`              |     | ✅    | account.journal             |
| `tax_exigibility`                                    | Use Cash Basis                                         | `boolean`               |     | ✅    |                             |
| `tax_lock_date`                                      | Tax Return Lock Date                                   | `date`                  |     | ✅    |                             |
| `terms_type`                                         | Terms & Conditions format                              | `selection`             |     | ✅    |                             |
| `theme_background_color`                             | Theme Background Color                                 | `char`                  |     | ✅    |                             |
| `theme_color_brand`                                  | Theme Brand Color                                      | `char`                  |     | ✅    |                             |
| `theme_font_name`                                    | Select Font                                            | `selection`             |     | ✅    |                             |
| `theme_menu_style`                                   | Menu Style                                             | `selection`             |     | ✅    |                             |
| `theme_sidebar_color`                                | Theme Sidebar Color                                    | `char`                  |     | ✅    |                             |
| `theme_sidebar_text_color`                           | Sidebar Text Color                                     | `char`                  |     | ✅    |                             |
| `transfer_account_code_prefix`                       | Prefix of the transfer accounts                        | `char`                  |     | ✅    |                             |
| `transfer_account_id`                                | Inter-Banks Transfer Account                           | `many2one`              |     | ✅    | account.account             |
| `uninstalled_l10n_module_ids`                        | Uninstalled L10N Module                                | `many2many`             |     |       | ir.module.module            |
| `user_fiscalyear_lock_date`                          | User Fiscalyear Lock Date                              | `date`                  |     |       |                             |
| `user_hard_lock_date`                                | User Hard Lock Date                                    | `date`                  |     |       |                             |
| `user_ids`                                           | Accepted Users                                         | `many2many`             |     | ✅    | res.users                   |
| `user_purchase_lock_date`                            | User Purchase Lock Date                                | `date`                  |     |       |                             |
| `user_sale_lock_date`                                | User Sale Lock Date                                    | `date`                  |     |       |                             |
| `user_tax_lock_date`                                 | User Tax Lock Date                                     | `date`                  |     |       |                             |
| `uses_default_logo`                                  | Uses Default Logo                                      | `boolean`               |     | ✅    |                             |
| `vat`                                                | Tax ID                                                 | `char`                  |     |       |                             |
| `verify_date`                                        | Verify Date                                            | `char`                  |     | ✅    |                             |
| `website`                                            | Website Link                                           | `char`                  |     |       |                             |
| `website_id`                                         | Website                                                | `many2one`              |     | ✅    | website                     |
| `website_message_ids`                                | Website Messages                                       | `one2many`              |     | ✅    | mail.message                |
| `work_permit_expiration_notice_period`               | Work Permit Expiry Notice Period                       | `integer`               |     | ✅    |                             |
| `write_date`                                         | Last Updated on                                        | `datetime`              |     | ✅    |                             |
| `write_uid`                                          | Last Updated by                                        | `many2one`              |     | ✅    | res.users                   |
| `zip`                                                | Zip                                                    | `char`                  |     |       |                             |

**Access Rights:**

| Name                          | Group         | Perms     |
| ----------------------------- | ------------- | --------- |
| res_company group_erp_manager | Access Rights | `R/W/C/D` |
| res_company group_user        | Role / Portal | `R`       |
| res_company group_user        | Role / Public | `R`       |
| res_company group_user        | Role / User   | `R`       |

**Record Rules:**

- **company rule portal** (10) `R/W/C/D`
  - Domain: `[('id','in', company_ids)]`
- **company rule employee** (1) `R/W/C/D`
  - Domain: `[('id','in', company_ids)]`
- **company rule public** (11) `R/W/C/D`
  - Domain: `[('id','in', company_ids)]`
- **company rule erp manager** (2) `R/W/C/D`
  - Domain: `[(1,'=',1)]`

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

### 🗃️ `mail.thread.cc` — Email CC management

> 📧 Mail Thread

Update MailThread to add the support of bounce management in mass mailing traces.

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `email_cc`                   | Email cc               | `char`      |     | ✅    |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |

### 🗃️ `mail.thread` — Email Thread

> 📧 Mail Thread

Update MailThread to add the support of bounce management in mass mailing traces.

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |

### 🗃️ `mail.blacklist` — Mail Blacklist

> 📧 Mail Thread

Model of blacklisted email addresses to stop sending emails.

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation                    |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | --------------------------- |
| `active`                     | Active                 | `boolean`   |     | ✅    |                             |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                             |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users                   |
| `display_name`               | Display Name           | `char`      |     |       |                             |
| `email`                      | Email Address          | `char`      | ✅  | ✅    |                             |
| `has_message`                | Has Message            | `boolean`   |     |       |                             |
| `id`                         | ID                     | `integer`   |     | ✅    |                             |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                             |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers              |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                             |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                             |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                             |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message                |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                             |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                             |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                             |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner                 |
| `opt_out_reason_id`          | Opt-out Reason         | `many2one`  |     | ✅    | mailing.subscription.optout |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating               |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message                |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                             |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                                    | Group                  | Perms     |
| --------------------------------------- | ---------------------- | --------- |
| access.mail.blacklist.mass_mailing_user | Email Marketing / User | `R/W/C/D` |
| access_mail_blacklist_system            | Role / Administrator   | `R/W/C/D` |

### 🗃️ `mail.thread.blacklist` — Mail Blacklist mixin

> 📧 Mail Thread

Mixin that is inherited by all model with opt out. This mixin stores a normalized email
based on primary_email field.

    A normalized email is considered as :
        - having a left part + @ + a right part (the domain can be without '.something')
        - being lower case
        - having no name before the address. Typically, having no 'Name <>'
    Ex:
        - Formatted Email : 'Name <NaMe@DoMaIn.CoM>'
        - Normalized Email : 'name@domain.com'

    The primary email field can be specified on the parent model, if it differs from the default one ('email')
    The email_normalized field can than be used on that model to search quickly on emails (by simple comparison
    and not using time consuming regex anymore).

    Using this email_normalized field, blacklist status is computed.

    Mail Thread capabilities are required for this mixin.

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `email_normalized`           | Normalized Email       | `char`      |     | ✅    |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `is_blacklisted`             | Blacklist              | `boolean`   |     |       |                |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_bounce`             | Bounce                 | `integer`   |     | ✅    |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |

### 🗃️ `mail.thread.main.attachment` — Mail Main Attachment management

> 📧 Mail Thread

Mixin that adds main attachment support to the MailThread class.

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_main_attachment_id` | Main Attachment        | `many2one`  |     | ✅    | ir.attachment  |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |

### 🗃️ `mail.tracking.duration.mixin` — Mixin to compute the time a record has spent in each value a many2one field can take

> 📧 Mail Thread

Update MailThread to add the support of bounce management in mass mailing traces.

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `duration_tracking`          | Status time            | `json`      |     |       |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `is_rotting`                 | Rotting                | `boolean`   |     |       |                |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `rotting_days`               | Days Rotting           | `integer`   |     |       |                |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |

### 🗃️ `ir.cron` — Scheduled Actions

> 📧 Mail Thread

Model describing cron jobs (also called actions or tasks).

**Fields:**

| Field                               | Label                         | Type        | Req | Store | Relation                  |
| ----------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------- |
| `action_class`                      | Action Class                  | `char`      |     |       |                           |
| `active`                            | Active                        | `boolean`   |     | ✅    |                           |
| `activity_calendar_event_id`        | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event            |
| `activity_date_deadline`            | Next Activity Deadline        | `date`      |     |       |                           |
| `activity_date_deadline_range`      | Due Date In                   | `integer`   |     |       |                           |
| `activity_date_deadline_range_type` | Due type                      | `selection` |     |       |                           |
| `activity_exception_decoration`     | Activity Exception Decoration | `selection` |     |       |                           |
| `activity_exception_icon`           | Icon                          | `char`      |     |       |                           |
| `activity_ids`                      | Activities                    | `one2many`  |     | ✅    | mail.activity             |
| `activity_note`                     | Note                          | `html`      |     |       |                           |
| `activity_state`                    | Activity State                | `selection` |     |       |                           |
| `activity_summary`                  | Next Activity Summary         | `char`      |     |       |                           |
| `activity_type_icon`                | Activity Type Icon            | `char`      |     |       |                           |
| `activity_type_id`                  | Next Activity Type            | `many2one`  |     |       | mail.activity.type        |
| `activity_user_field_name`          | User Field                    | `char`      |     |       |                           |
| `activity_user_id`                  | Responsible User              | `many2one`  |     |       | res.users                 |
| `activity_user_type`                | User Type                     | `selection` |     |       |                           |
| `allowed_states`                    | Allowed states                | `json`      |     |       |                           |
| `automated_name`                    | Automated Name                | `char`      |     |       |                           |
| `available_model_ids`               | Available Models              | `many2many` |     |       | ir.model                  |
| `base_automation_id`                | Automation Rule               | `many2one`  |     |       | base.automation           |
| `binding_model_id`                  | Binding Model                 | `many2one`  |     |       | ir.model                  |
| `binding_type`                      | Binding Type                  | `selection` | ✅  |       |                           |
| `binding_view_types`                | Binding View Types            | `char`      |     |       |                           |
| `child_ids`                         | Child Actions                 | `one2many`  |     |       | ir.actions.server         |
| `code`                              | Python Code                   | `text`      |     |       |                           |
| `create_date`                       | Created on                    | `datetime`  |     | ✅    |                           |
| `create_uid`                        | Created by                    | `many2one`  |     | ✅    | res.users                 |
| `cron_name`                         | Name                          | `char`      |     | ✅    |                           |
| `crud_model_id`                     | Record to Create              | `many2one`  |     |       | ir.model                  |
| `crud_model_name`                   | Target Model Name             | `char`      |     |       |                           |
| `display_name`                      | Display Name                  | `char`      |     |       |                           |
| `evaluation_type`                   | Value Type                    | `selection` |     |       |                           |
| `failure_count`                     | Failure Count                 | `integer`   |     | ✅    |                           |
| `first_failure_date`                | First Failure Date            | `datetime`  |     | ✅    |                           |
| `followers_partner_field_name`      | Followers Field               | `char`      |     |       |                           |
| `followers_type`                    | Followers Type                | `selection` |     |       |                           |
| `group_ids`                         | Allowed Groups                | `many2many` |     |       | res.groups                |
| `has_message`                       | Has Message                   | `boolean`   |     |       |                           |
| `help`                              | Action Description            | `html`      |     |       |                           |
| `html_value`                        | Html Value                    | `html`      |     |       |                           |
| `icon`                              | Icon                          | `char`      |     |       |                           |
| `id`                                | ID                            | `integer`   |     | ✅    |                           |
| `interval_number`                   | Interval Number               | `integer`   | ✅  | ✅    |                           |
| `interval_type`                     | Interval Unit                 | `selection` | ✅  | ✅    |                           |
| `ir_actions_server_id`              | Server action                 | `many2one`  | ✅  | ✅    | ir.actions.server         |
| `ir_cron_ids`                       | Scheduled Action              | `one2many`  |     |       | ir.cron                   |
| `lastcall`                          | Last Execution Date           | `datetime`  |     | ✅    |                           |
| `link_field_id`                     | Link Field                    | `many2one`  |     |       | ir.model.fields           |
| `mail_post_autofollow`              | Subscribe Recipients          | `boolean`   |     |       |                           |
| `mail_post_method`                  | Send Email As                 | `selection` |     |       |                           |
| `message_attachment_count`          | Attachment Count              | `integer`   |     |       |                           |
| `message_follower_ids`              | Followers                     | `one2many`  |     | ✅    | mail.followers            |
| `message_has_error`                 | Message Delivery error        | `boolean`   |     |       |                           |
| `message_has_error_counter`         | Number of errors              | `integer`   |     |       |                           |
| `message_has_sms_error`             | SMS Delivery error            | `boolean`   |     |       |                           |
| `message_ids`                       | Messages                      | `one2many`  |     | ✅    | mail.message              |
| `message_is_follower`               | Is Follower                   | `boolean`   |     |       |                           |
| `message_needaction`                | Action Needed                 | `boolean`   |     |       |                           |
| `message_needaction_counter`        | Number of Actions             | `integer`   |     |       |                           |
| `message_partner_ids`               | Followers (Partners)          | `many2many` |     |       | res.partner               |
| `model_id`                          | Model                         | `many2one`  | ✅  |       | ir.model                  |
| `model_name`                        | Model Name                    | `char`      |     |       |                           |
| `my_activity_date_deadline`         | My Activity Deadline          | `date`      |     |       |                           |
| `name`                              | Action Name                   | `char`      | ✅  |       |                           |
| `nextcall`                          | Next Execution Date           | `datetime`  | ✅  | ✅    |                           |
| `parent_id`                         | Parent Action                 | `many2one`  |     |       | ir.actions.server         |
| `partner_ids`                       | Partner                       | `many2many` |     |       | res.partner               |
| `path`                              | Path to show in the URL       | `char`      |     |       |                           |
| `priority`                          | Priority                      | `integer`   |     | ✅    |                           |
| `rating_ids`                        | Ratings                       | `one2many`  |     | ✅    | rating.rating             |
| `resource_ref`                      | Record                        | `reference` |     |       |                           |
| `selection_value`                   | Custom Value                  | `many2one`  |     |       | ir.model.fields.selection |
| `sequence`                          | Sequence                      | `integer`   |     |       |                           |
| `sequence_id`                       | Sequence to use               | `many2one`  |     |       | ir.sequence               |
| `show_code_history`                 | Show Code History             | `boolean`   |     |       |                           |
| `sms_method`                        | Send SMS As                   | `selection` |     |       |                           |
| `sms_template_id`                   | SMS Template                  | `many2one`  |     |       | sms.template              |
| `state`                             | Type                          | `selection` | ✅  |       |                           |
| `template_id`                       | Email Template                | `many2one`  |     |       | mail.template             |
| `type`                              | Action Type                   | `char`      | ✅  |       |                           |
| `update_boolean_value`              | Boolean Value                 | `selection` |     |       |                           |
| `update_field_id`                   | Field to Update               | `many2one`  |     |       | ir.model.fields           |
| `update_field_type`                 | Field Type                    | `selection` |     |       |                           |
| `update_m2m_operation`              | Many2many Operations          | `selection` |     |       |                           |
| `update_path`                       | Field to Update Path          | `char`      |     |       |                           |
| `update_related_model_id`           | Update Related Model          | `many2one`  |     |       | ir.model                  |
| `usage`                             | Usage                         | `selection` | ✅  |       |                           |
| `user_id`                           | Scheduler User                | `many2one`  | ✅  | ✅    | res.users                 |
| `value`                             | Value                         | `text`      |     |       |                           |
| `value_field_to_show`               | Value Field To Show           | `selection` |     |       |                           |
| `warning`                           | Warning                       | `text`      |     |       |                           |
| `webhook_field_ids`                 | Webhook Fields                | `many2many` |     |       | ir.model.fields           |
| `webhook_sample_payload`            | Sample Payload                | `text`      |     |       |                           |
| `webhook_url`                       | Webhook URL                   | `char`      |     |       |                           |
| `website_message_ids`               | Website Messages              | `one2many`  |     | ✅    | mail.message              |
| `website_path`                      | Website Path                  | `char`      |     |       |                           |
| `website_published`                 | Available on the Website      | `boolean`   |     |       |                           |
| `website_url`                       | Website Url                   | `char`      |     |       |                           |
| `write_date`                        | Last Updated on               | `datetime`  |     | ✅    |                           |
| `write_uid`                         | Last Updated by               | `many2one`  |     | ✅    | res.users                 |
| `xml_id`                            | External ID                   | `char`      |     |       |                           |

**Access Rights:**

| Name               | Group                | Perms     |
| ------------------ | -------------------- | --------- |
| ir_cron group_cron | Role / Administrator | `R/W/C/D` |

### 🗃️ `ir.actions.server` — Server Action

> 📧 Mail Thread

Add website option in server actions.

**Fields:**

| Field                               | Label                         | Type        | Req | Store | Relation                  |
| ----------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------- |
| `action_class`                      | Action Class                  | `char`      |     | ✅    |                           |
| `activity_calendar_event_id`        | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event            |
| `activity_date_deadline`            | Next Activity Deadline        | `date`      |     |       |                           |
| `activity_date_deadline_range`      | Due Date In                   | `integer`   |     | ✅    |                           |
| `activity_date_deadline_range_type` | Due type                      | `selection` |     | ✅    |                           |
| `activity_exception_decoration`     | Activity Exception Decoration | `selection` |     |       |                           |
| `activity_exception_icon`           | Icon                          | `char`      |     |       |                           |
| `activity_ids`                      | Activities                    | `one2many`  |     | ✅    | mail.activity             |
| `activity_note`                     | Note                          | `html`      |     | ✅    |                           |
| `activity_state`                    | Activity State                | `selection` |     |       |                           |
| `activity_summary`                  | Title                         | `char`      |     | ✅    |                           |
| `activity_type_icon`                | Activity Type Icon            | `char`      |     |       |                           |
| `activity_type_id`                  | Activity Type                 | `many2one`  |     | ✅    | mail.activity.type        |
| `activity_user_field_name`          | User Field                    | `char`      |     | ✅    |                           |
| `activity_user_id`                  | Responsible                   | `many2one`  |     | ✅    | res.users                 |
| `activity_user_type`                | User Type                     | `selection` |     | ✅    |                           |
| `allowed_states`                    | Allowed states                | `json`      |     |       |                           |
| `automated_name`                    | Automated Name                | `char`      |     | ✅    |                           |
| `available_model_ids`               | Available Models              | `many2many` |     |       | ir.model                  |
| `base_automation_id`                | Automation Rule               | `many2one`  |     | ✅    | base.automation           |
| `binding_model_id`                  | Binding Model                 | `many2one`  |     | ✅    | ir.model                  |
| `binding_type`                      | Binding Type                  | `selection` | ✅  | ✅    |                           |
| `binding_view_types`                | Binding View Types            | `char`      |     | ✅    |                           |
| `child_ids`                         | Child Actions                 | `one2many`  |     | ✅    | ir.actions.server         |
| `code`                              | Python Code                   | `text`      |     | ✅    |                           |
| `create_date`                       | Created on                    | `datetime`  |     | ✅    |                           |
| `create_uid`                        | Created by                    | `many2one`  |     | ✅    | res.users                 |
| `crud_model_id`                     | Record to Create              | `many2one`  |     | ✅    | ir.model                  |
| `crud_model_name`                   | Target Model Name             | `char`      |     |       |                           |
| `display_name`                      | Display Name                  | `char`      |     |       |                           |
| `evaluation_type`                   | Value Type                    | `selection` |     | ✅    |                           |
| `followers_partner_field_name`      | Followers Field               | `char`      |     | ✅    |                           |
| `followers_type`                    | Followers Type                | `selection` |     | ✅    |                           |
| `group_ids`                         | Allowed Groups                | `many2many` |     | ✅    | res.groups                |
| `has_message`                       | Has Message                   | `boolean`   |     |       |                           |
| `help`                              | Action Description            | `html`      |     | ✅    |                           |
| `html_value`                        | Html Value                    | `html`      |     | ✅    |                           |
| `icon`                              | Icon                          | `char`      |     | ✅    |                           |
| `id`                                | ID                            | `integer`   |     | ✅    |                           |
| `ir_cron_ids`                       | Scheduled Action              | `one2many`  |     | ✅    | ir.cron                   |
| `link_field_id`                     | Link Field                    | `many2one`  |     | ✅    | ir.model.fields           |
| `mail_post_autofollow`              | Subscribe Recipients          | `boolean`   |     | ✅    |                           |
| `mail_post_method`                  | Send Email As                 | `selection` |     | ✅    |                           |
| `message_attachment_count`          | Attachment Count              | `integer`   |     |       |                           |
| `message_follower_ids`              | Followers                     | `one2many`  |     | ✅    | mail.followers            |
| `message_has_error`                 | Message Delivery error        | `boolean`   |     |       |                           |
| `message_has_error_counter`         | Number of errors              | `integer`   |     |       |                           |
| `message_has_sms_error`             | SMS Delivery error            | `boolean`   |     |       |                           |
| `message_ids`                       | Messages                      | `one2many`  |     | ✅    | mail.message              |
| `message_is_follower`               | Is Follower                   | `boolean`   |     |       |                           |
| `message_needaction`                | Action Needed                 | `boolean`   |     |       |                           |
| `message_needaction_counter`        | Number of Actions             | `integer`   |     |       |                           |
| `message_partner_ids`               | Followers (Partners)          | `many2many` |     |       | res.partner               |
| `model_id`                          | Model                         | `many2one`  | ✅  | ✅    | ir.model                  |
| `model_name`                        | Model Name                    | `char`      |     |       |                           |
| `my_activity_date_deadline`         | My Activity Deadline          | `date`      |     |       |                           |
| `name`                              | Action Name                   | `char`      | ✅  | ✅    |                           |
| `parent_id`                         | Parent Action                 | `many2one`  |     | ✅    | ir.actions.server         |
| `partner_ids`                       | Partner                       | `many2many` |     | ✅    | res.partner               |
| `path`                              | Path to show in the URL       | `char`      |     | ✅    |                           |
| `rating_ids`                        | Ratings                       | `one2many`  |     | ✅    | rating.rating             |
| `resource_ref`                      | Record                        | `reference` |     | ✅    |                           |
| `selection_value`                   | Custom Value                  | `many2one`  |     | ✅    | ir.model.fields.selection |
| `sequence`                          | Sequence                      | `integer`   |     | ✅    |                           |
| `sequence_id`                       | Sequence to use               | `many2one`  |     | ✅    | ir.sequence               |
| `show_code_history`                 | Show Code History             | `boolean`   |     |       |                           |
| `sms_method`                        | Send SMS As                   | `selection` |     | ✅    |                           |
| `sms_template_id`                   | SMS Template                  | `many2one`  |     | ✅    | sms.template              |
| `state`                             | Type                          | `selection` | ✅  | ✅    |                           |
| `template_id`                       | Email Template                | `many2one`  |     | ✅    | mail.template             |
| `type`                              | Action Type                   | `char`      | ✅  | ✅    |                           |
| `update_boolean_value`              | Boolean Value                 | `selection` |     | ✅    |                           |
| `update_field_id`                   | Field to Update               | `many2one`  |     | ✅    | ir.model.fields           |
| `update_field_type`                 | Field Type                    | `selection` |     |       |                           |
| `update_m2m_operation`              | Many2many Operations          | `selection` |     | ✅    |                           |
| `update_path`                       | Field to Update Path          | `char`      |     | ✅    |                           |
| `update_related_model_id`           | Update Related Model          | `many2one`  |     | ✅    | ir.model                  |
| `usage`                             | Usage                         | `selection` | ✅  | ✅    |                           |
| `value`                             | Value                         | `text`      |     | ✅    |                           |
| `value_field_to_show`               | Value Field To Show           | `selection` |     |       |                           |
| `warning`                           | Warning                       | `text`      |     |       |                           |
| `webhook_field_ids`                 | Webhook Fields                | `many2many` |     | ✅    | ir.model.fields           |
| `webhook_sample_payload`            | Sample Payload                | `text`      |     |       |                           |
| `webhook_url`                       | Webhook URL                   | `char`      |     | ✅    |                           |
| `website_message_ids`               | Website Messages              | `one2many`  |     | ✅    | mail.message              |
| `website_path`                      | Website Path                  | `char`      |     | ✅    |                           |
| `website_published`                 | Available on the Website      | `boolean`   |     | ✅    |                           |
| `website_url`                       | Website Url                   | `char`      |     |       |                           |
| `write_date`                        | Last Updated on               | `datetime`  |     | ✅    |                           |
| `write_uid`                         | Last Updated by               | `many2one`  |     | ✅    | res.users                 |
| `xml_id`                            | External ID                   | `char`      |     |       |                           |

**Access Rights:**

| Name                           | Group                | Perms     |
| ------------------------------ | -------------------- | --------- |
| ir_actions_server_group_system | Role / Administrator | `R/W/C/D` |

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

### 🗃️ `ir.actions.act_window.view` — Action Window View

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label            | Type        | Req | Store | Relation              |
| --------------- | ---------------- | ----------- | --- | ----- | --------------------- |
| `act_window_id` | Action           | `many2one`  |     | ✅    | ir.actions.act_window |
| `create_date`   | Created on       | `datetime`  |     | ✅    |                       |
| `create_uid`    | Created by       | `many2one`  |     | ✅    | res.users             |
| `display_name`  | Display Name     | `char`      |     |       |                       |
| `id`            | ID               | `integer`   |     | ✅    |                       |
| `multi`         | On Multiple Doc. | `boolean`   |     | ✅    |                       |
| `sequence`      | Sequence         | `integer`   |     | ✅    |                       |
| `view_id`       | View             | `many2one`  |     | ✅    | ir.ui.view            |
| `view_mode`     | View Type        | `selection` | ✅  | ✅    |                       |
| `write_date`    | Last Updated on  | `datetime`  |     | ✅    |                       |
| `write_uid`     | Last Updated by  | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                                    | Group                | Perms     |
| --------------------------------------- | -------------------- | --------- |
| ir_actions_act_window_view_group_system | Role / Administrator | `R/W/C/D` |

### 🗃️ `mail.activity` — Activity

An actual activity to perform. Activities are linked to documents using res_id and
res_model_id fields. Activities have a deadline that can be used in kanban view to
display a status. Once done activities are unlinked and a message is posted. This
message has a new activity_type_id field that indicates the activity linked to the
message.

**Fields:**

| Field                          | Label                     | Type                 | Req | Store | Relation           |
| ------------------------------ | ------------------------- | -------------------- | --- | ----- | ------------------ |
| `active`                       | Active                    | `boolean`            |     | ✅    |                    |
| `activity_category`            | Action                    | `selection`          |     |       |                    |
| `activity_decoration`          | Decoration Type           | `selection`          |     |       |                    |
| `activity_type_id`             | Activity Type             | `many2one`           |     | ✅    | mail.activity.type |
| `attachment_ids`               | Attachments               | `many2many`          |     | ✅    | ir.attachment      |
| `automated`                    | Automated activity        | `boolean`            |     | ✅    |                    |
| `calendar_event_id`            | Calendar Meeting          | `many2one`           |     | ✅    | calendar.event     |
| `can_write`                    | Can Write                 | `boolean`            |     |       |                    |
| `chaining_type`                | Chaining Type             | `selection`          |     |       |                    |
| `create_date`                  | Created on                | `datetime`           |     | ✅    |                    |
| `create_uid`                   | Created by                | `many2one`           |     | ✅    | res.users          |
| `date_deadline`                | Due Date                  | `date`               | ✅  | ✅    |                    |
| `date_done`                    | Done Date                 | `date`               |     | ✅    |                    |
| `display_name`                 | Display Name              | `char`               |     |       |                    |
| `feedback`                     | Feedback                  | `text`               |     | ✅    |                    |
| `has_recommended_activities`   | Next activities available | `boolean`            |     |       |                    |
| `icon`                         | Icon                      | `char`               |     |       |                    |
| `id`                           | ID                        | `integer`            |     | ✅    |                    |
| `mail_template_ids`            | Email templates           | `many2many`          |     |       | mail.template      |
| `note`                         | Note                      | `html`               |     | ✅    |                    |
| `previous_activity_type_id`    | Previous Activity Type    | `many2one`           |     | ✅    | mail.activity.type |
| `recommended_activity_type_id` | Recommended Activity Type | `many2one`           |     | ✅    | mail.activity.type |
| `res_id`                       | Related Document ID       | `many2one_reference` |     | ✅    |                    |
| `res_model`                    | Related Document Model    | `char`               |     | ✅    |                    |
| `res_model_id`                 | Document Model            | `many2one`           |     | ✅    | ir.model           |
| `res_name`                     | Document Name             | `char`               |     | ✅    |                    |
| `state`                        | State                     | `selection`          |     |       |                    |
| `summary`                      | Summary                   | `char`               |     | ✅    |                    |
| `user_id`                      | Assigned to               | `many2one`           |     | ✅    | res.users          |
| `user_tz`                      | Timezone                  | `selection`          |     | ✅    |                    |
| `write_date`                   | Last Updated on           | `datetime`           |     | ✅    |                    |
| `write_uid`                    | Last Updated by           | `many2one`           |     | ✅    | res.users          |

**Access Rights:**

| Name               | Group       | Perms     |
| ------------------ | ----------- | --------- |
| mail.activity.user | Role / User | `R/W/C/D` |

**Record Rules:**

- **mail.activity: user: write/unlink only (created or assigned)** (1) `W/D`
  - Domain: `['|', ('user_id', '=', user.id), ('create_uid', '=', user.id)]`

### 🗃️ `mail.activity.mixin` — Activity Mixin

Mail Activity Mixin is a mixin class to use if you want to add activities management on
a model. It works like the mail.thread mixin. It defines an activity_ids one2many field
toward activities using res_id and res_model_id. Various related / computed fields are
also added to have a global status of activities on documents.

    Activities come with a new JS widget for the form view. It is integrated in the
    Chatter widget although it is a separate widget. It displays activities linked
    to the current record and allow to schedule, edit and mark done activities.

    There is also a kanban widget defined. It defines a small widget to integrate
    in kanban vignettes. It allow to manage activities directly from the kanban
    view. Use widget="kanban_activity" on activitiy_ids field in kanban view to
    use it.

    Some context keys allow to control the mixin behavior. Use those in some
    specific cases like import

     * ``mail_activity_automation_skip``: skip activities automation; it means
       no automated activities will be generated, updated or unlinked, allowing
       to save computation and avoid generating unwanted activities;

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation           |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------ |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event     |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                    |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                    |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                    |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity      |
| `activity_state`                | Activity State                | `selection` |     |       |                    |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                    |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                    |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users          |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                    |

### 🗃️ `mail.activity.plan` — Activity Plan

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                   | Label                     | Type        | Req | Store | Relation                    |
| ----------------------- | ------------------------- | ----------- | --- | ----- | --------------------------- |
| `active`                | Active                    | `boolean`   |     | ✅    |                             |
| `company_id`            | Company                   | `many2one`  |     | ✅    | res.company                 |
| `create_date`           | Created on                | `datetime`  |     | ✅    |                             |
| `create_uid`            | Created by                | `many2one`  |     | ✅    | res.users                   |
| `department_assignable` | Department Assignable     | `boolean`   |     |       |                             |
| `department_id`         | Department                | `many2one`  |     | ✅    | hr.department               |
| `display_name`          | Display Name              | `char`      |     |       |                             |
| `has_user_on_demand`    | Has on demand responsible | `boolean`   |     |       |                             |
| `id`                    | ID                        | `integer`   |     | ✅    |                             |
| `name`                  | Name                      | `char`      | ✅  | ✅    |                             |
| `res_model`             | Model                     | `selection` | ✅  | ✅    |                             |
| `res_model_id`          | Applies to                | `many2one`  | ✅  | ✅    | ir.model                    |
| `steps_count`           | Steps Count               | `integer`   |     |       |                             |
| `template_ids`          | Activities                | `one2many`  |     | ✅    | mail.activity.plan.template |
| `write_date`            | Last Updated on           | `datetime`  |     | ✅    |                             |
| `write_uid`             | Last Updated by           | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                                      | Group                       | Perms     |
| ----------------------------------------- | --------------------------- | --------- |
| mail.activity.plan.sale.manager           | Sales / Administrator       | `R/W/C/D` |
| mail.activity.plan.sale.manager           | Sales / Administrator       | `R/W/C/D` |
| mail.activity.plan.hr.manager             | Employees / Administrator   | `R/W/C/D` |
| mail.activity.plan.hr.recruitment.manager | Recruitment / Administrator | `R/W/C/D` |
| mail.activity.plan.system                 | Role / Administrator        | `R/W/C/D` |
| mail.activity.plan.user                   | Role / User                 | `R`       |

**Record Rules:**

- **Administrators can access all activity plans.** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Manager can manage lead plans** (27) `W/C/D`
  - Domain: `[('res_model', '=', 'crm.lead')]`
- **Manager can edit employee plan** (50) `W/C/D`
  - Domain: `[('res_model', '=', 'hr.employee')]`
- **Manager can manage applicant plans** (84) `W/C/D`
  - Domain: `[('res_model', '=', 'hr.applicant')]`
- **Manager can manage sale order plans** (27) `W/C/D`
  - Domain: `[('res_model', '=', 'sale.order')]`

### 🗃️ `mail.activity.plan.template` — Activity plan template

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label           | Type        | Req | Store | Relation           |
| ------------------- | --------------- | ----------- | --- | ----- | ------------------ |
| `activity_type_id`  | Activity Type   | `many2one`  | ✅  | ✅    | mail.activity.type |
| `company_id`        | Company         | `many2one`  |     |       | res.company        |
| `create_date`       | Created on      | `datetime`  |     | ✅    |                    |
| `create_uid`        | Created by      | `many2one`  |     | ✅    | res.users          |
| `delay_count`       | Interval        | `integer`   |     | ✅    |                    |
| `delay_from`        | Trigger         | `selection` | ✅  | ✅    |                    |
| `delay_unit`        | Delay units     | `selection` | ✅  | ✅    |                    |
| `display_name`      | Display Name    | `char`      |     |       |                    |
| `icon`              | Icon            | `char`      |     |       |                    |
| `id`                | ID              | `integer`   |     | ✅    |                    |
| `next_activity_ids` | Next Activities | `many2many` |     | ✅    | mail.activity.type |
| `note`              | Note            | `html`      |     | ✅    |                    |
| `plan_id`           | Plan            | `many2one`  | ✅  | ✅    | mail.activity.plan |
| `res_model`         | Model           | `selection` |     |       |                    |
| `responsible_id`    | Assigned to     | `many2one`  |     | ✅    | res.users          |
| `responsible_type`  | Assignment      | `selection` | ✅  | ✅    |                    |
| `sequence`          | Sequence        | `integer`   |     | ✅    |                    |
| `summary`           | Summary         | `char`      |     | ✅    |                    |
| `write_date`        | Last Updated on | `datetime`  |     | ✅    |                    |
| `write_uid`         | Last Updated by | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                               | Group                       | Perms     |
| -------------------------------------------------- | --------------------------- | --------- |
| mail.activity.plan.template.sale.manager           | Sales / Administrator       | `R/W/C/D` |
| mail.activity.plan.template.sale.manager           | Sales / Administrator       | `R/W/C/D` |
| mail.activity.plan.template.hr.manager             | Employees / Administrator   | `R/W/C/D` |
| mail.activity.plan.template.hr.recruitment.manager | Recruitment / Administrator | `R/W/C/D` |
| mail.activity.plan.template.system                 | Role / Administrator        | `R/W/C/D` |
| mail.activity.plan.template.user                   | Role / User                 | `R`       |

**Record Rules:**

- **Administrators can access all activity plan templates.** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Manager can manage lead plan templates** (27) `W/C/D`
  - Domain: `[('plan_id.res_model', '=', 'crm.lead')]`
- **Manager can edit employee plan template** (50) `W/C/D`
  - Domain: `[('plan_id.res_model', '=', 'hr.employee')]`
- **Manager can manage applicant plan templates** (84) `W/C/D`
  - Domain: `[('plan_id.res_model', '=', 'hr.applicant')]`
- **Manager can manage sale order plan templates** (27) `W/C/D`
  - Domain: `[('plan_id.res_model', '=', 'sale.order')]`

### 🗃️ `mail.activity.schedule` — Activity schedule plan Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                        | Label                      | Type        | Req | Store | Relation                    |
| ---------------------------- | -------------------------- | ----------- | --- | ----- | --------------------------- |
| `activity_category`          | Action                     | `selection` |     |       |                             |
| `activity_type_id`           | Activity Type              | `many2one`  |     | ✅    | mail.activity.type          |
| `activity_user_id`           | Assigned to                | `many2one`  |     | ✅    | res.users                   |
| `chaining_type`              | Chaining Type              | `selection` |     |       |                             |
| `company_id`                 | Company                    | `many2one`  |     |       | res.company                 |
| `create_date`                | Created on                 | `datetime`  |     | ✅    |                             |
| `create_uid`                 | Created by                 | `many2one`  |     | ✅    | res.users                   |
| `date_deadline`              | Due Date                   | `date`      |     | ✅    |                             |
| `department_id`              | Department                 | `many2one`  |     |       | hr.department               |
| `display_name`               | Display Name               | `char`      |     |       |                             |
| `error`                      | Error                      | `html`      |     |       |                             |
| `has_error`                  | Has Error                  | `boolean`   |     |       |                             |
| `has_warning`                | Has Warning                | `boolean`   |     |       |                             |
| `id`                         | ID                         | `integer`   |     | ✅    |                             |
| `is_batch_mode`              | Use in batch               | `boolean`   |     |       |                             |
| `note`                       | Note                       | `html`      |     | ✅    |                             |
| `plan_available_ids`         | Plan Available             | `many2many` |     | ✅    | mail.activity.plan          |
| `plan_date`                  | Plan Date                  | `date`      |     | ✅    |                             |
| `plan_department_filterable` | Plan Department Filterable | `boolean`   |     |       |                             |
| `plan_has_user_on_demand`    | Has on demand responsible  | `boolean`   |     |       |                             |
| `plan_id`                    | Plan                       | `many2one`  |     | ✅    | mail.activity.plan          |
| `plan_on_demand_user_id`     | Assigned To                | `many2one`  |     | ✅    | res.users                   |
| `plan_schedule_line_ids`     | Schedule Lines             | `one2many`  |     |       | mail.activity.schedule.line |
| `res_ids`                    | Document IDs               | `text`      |     | ✅    |                             |
| `res_model`                  | Model                      | `char`      |     | ✅    |                             |
| `res_model_id`               | Applies to                 | `many2one`  |     | ✅    | ir.model                    |
| `summary`                    | Summary                    | `char`      |     | ✅    |                             |
| `warning`                    | Warning                    | `html`      |     |       |                             |
| `write_date`                 | Last Updated on            | `datetime`  |     | ✅    |                             |
| `write_uid`                  | Last Updated by            | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                        | Group       | Perms   |
| --------------------------- | ----------- | ------- |
| mail.activity.schedule.user | Role / User | `R/W/C` |

### 🗃️ `mail.activity.type` — Activity Type

Activity Types are used to categorize activities. Each type is a different kind of
activity e.g. call, mail, meeting. An activity can be generic i.e. available for all
models using activities; or specific to a model in which case res_model field should be
used.

**Fields:**

| Field                     | Label                | Type        | Req | Store | Relation           |
| ------------------------- | -------------------- | ----------- | --- | ----- | ------------------ |
| `active`                  | Active               | `boolean`   |     | ✅    |                    |
| `category`                | Action               | `selection` |     | ✅    |                    |
| `chaining_type`           | Chaining Type        | `selection` | ✅  | ✅    |                    |
| `create_date`             | Created on           | `datetime`  |     | ✅    |                    |
| `create_uid`              | Create Uid           | `many2one`  |     | ✅    | res.users          |
| `decoration_type`         | Decoration Type      | `selection` |     | ✅    |                    |
| `default_note`            | Default Note         | `html`      |     | ✅    |                    |
| `default_user_id`         | Default User         | `many2one`  |     | ✅    | res.users          |
| `delay_count`             | Schedule             | `integer`   |     | ✅    |                    |
| `delay_from`              | Delay Type           | `selection` | ✅  | ✅    |                    |
| `delay_label`             | Delay Label          | `char`      |     |       |                    |
| `delay_unit`              | Delay units          | `selection` | ✅  | ✅    |                    |
| `display_name`            | Display Name         | `char`      |     |       |                    |
| `icon`                    | Icon                 | `char`      |     | ✅    |                    |
| `id`                      | ID                   | `integer`   |     | ✅    |                    |
| `initial_res_model`       | Initial model        | `selection` |     |       |                    |
| `mail_template_ids`       | Email templates      | `many2many` |     | ✅    | mail.template      |
| `name`                    | Name                 | `char`      | ✅  | ✅    |                    |
| `previous_type_ids`       | Preceding Activities | `many2many` |     | ✅    | mail.activity.type |
| `res_model`               | Model                | `selection` |     | ✅    |                    |
| `res_model_change`        | Model has change     | `boolean`   |     |       |                    |
| `sequence`                | Sequence             | `integer`   |     | ✅    |                    |
| `suggested_next_type_ids` | Suggest              | `many2many` |     | ✅    | mail.activity.type |
| `summary`                 | Default Summary      | `char`      |     | ✅    |                    |
| `triggered_next_type_id`  | Trigger              | `many2one`  |     | ✅    | mail.activity.type |
| `write_date`              | Last Updated on      | `datetime`  |     | ✅    |                    |
| `write_uid`               | Last Updated by      | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                | Group                    | Perms     |
| ----------------------------------- | ------------------------ | --------- |
| mail.activity.type.sale.manager     | Sales / Administrator    | `R/W/C/D` |
| mail.activity.type.sale.manager     | Sales / Administrator    | `R/W/C/D` |
| mail.activity.type.holidays.manager | Time Off / Administrator | `R/W/C/D` |
| mail.activity.type.expense.user     | Expenses / Administrator | `R/W/C/D` |
| mail.activity.type.fleet.manager    | Fleet / Administrator    | `R/W/C/D` |
| mail.activity.type.system           | Role / Administrator     | `R/W/C/D` |
| mail.activity.type.user             | Role / User              | `R`       |

### 🗃️ `ir.attachment` — Attachment

Attachments are used to link binary files or url to any openerp document.

    External attachment storage
    ---------------------------

    The computed field ``datas`` is implemented using ``_file_read``,
    ``_file_write`` and ``_file_delete``, which can be overridden to implement
    other storage engines. Such methods should check for other location pseudo
    uri (example: hdfs://hadoopserver).

    The default implementation is the file:dirname location that stores files
    on the local filesystem using name based on their sha1 hash

**Fields:**

| Field               | Label                                        | Type                 | Req | Store | Relation               |
| ------------------- | -------------------------------------------- | -------------------- | --- | ----- | ---------------------- |
| `access_token`      | Access Token                                 | `char`               |     | ✅    |                        |
| `checksum`          | Checksum/SHA1                                | `char`               |     | ✅    |                        |
| `company_id`        | Company                                      | `many2one`           |     | ✅    | res.company            |
| `create_date`       | Created on                                   | `datetime`           |     | ✅    |                        |
| `create_uid`        | Created by                                   | `many2one`           |     | ✅    | res.users              |
| `datas`             | File Content (base64)                        | `binary`             |     |       |                        |
| `db_datas`          | Database Data                                | `binary`             |     | ✅    |                        |
| `description`       | Description                                  | `text`               |     | ✅    |                        |
| `display_name`      | Display Name                                 | `char`               |     |       |                        |
| `file_size`         | File Size                                    | `integer`            |     | ✅    |                        |
| `has_thumbnail`     | Has Thumbnail                                | `boolean`            |     |       |                        |
| `id`                | ID                                           | `integer`            |     | ✅    |                        |
| `image_height`      | Image Height                                 | `integer`            |     |       |                        |
| `image_src`         | Image Src                                    | `char`               |     |       |                        |
| `image_width`       | Image Width                                  | `integer`            |     |       |                        |
| `index_content`     | Indexed Content                              | `text`               |     | ✅    |                        |
| `key`               | Key                                          | `char`               |     | ✅    |                        |
| `local_url`         | Attachment URL                               | `char`               |     |       |                        |
| `media_link`        | Media Link                                   | `char`               |     | ✅    |                        |
| `mimetype`          | Mime Type                                    | `char`               |     | ✅    |                        |
| `name`              | Name                                         | `char`               | ✅  | ✅    |                        |
| `original_id`       | Original (unoptimized, unresized) attachment | `many2one`           |     | ✅    | ir.attachment          |
| `public`            | Is public document                           | `boolean`            |     | ✅    |                        |
| `raw`               | File Content (raw)                           | `binary`             |     |       |                        |
| `res_field`         | Resource Field                               | `char`               |     | ✅    |                        |
| `res_id`            | Resource ID                                  | `many2one_reference` |     | ✅    |                        |
| `res_model`         | Resource Model                               | `char`               |     | ✅    |                        |
| `res_name`          | Resource Name                                | `char`               |     |       |                        |
| `store_fname`       | Stored Filename                              | `char`               |     | ✅    |                        |
| `theme_template_id` | Theme Template                               | `many2one`           |     | ✅    | theme.ir.attachment    |
| `thumbnail`         | Thumbnail                                    | `binary`             |     | ✅    |                        |
| `type`              | Type                                         | `selection`          | ✅  | ✅    |                        |
| `url`               | Url                                          | `char`               |     | ✅    |                        |
| `voice_ids`         | Voice                                        | `one2many`           |     | ✅    | discuss.voice.metadata |
| `website_id`        | Website                                      | `many2one`           |     | ✅    | website                |
| `whatsapp_media_id` | whatsapp Media Id                            | `char`               |     | ✅    |                        |
| `write_date`        | Last Updated on                              | `datetime`           |     | ✅    |                        |
| `write_uid`         | Last Updated by                              | `many2one`           |     | ✅    | res.users              |

**Access Rights:**

| Name                              | Group       | Perms     |
| --------------------------------- | ----------- | --------- |
| ir_attachment group_user          | Role / User | `R/W/C/D` |
| ir_attachment group_portal_public | Everyone    | `-`       |

### 🗃️ `base` — Base

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `mail.canned.response` — Canned Response

Canned Response: content that automatically replaces shortcuts of your choosing. This
content can still be adapted before sending your message.

**Fields:**

| Field          | Label                                                                  | Type        | Req | Store | Relation   |
| -------------- | ---------------------------------------------------------------------- | ----------- | --- | ----- | ---------- |
| `create_date`  | Created on                                                             | `datetime`  |     | ✅    |            |
| `create_uid`   | Created by                                                             | `many2one`  |     | ✅    | res.users  |
| `display_name` | Display Name                                                           | `char`      |     |       |            |
| `group_ids`    | Authorized Groups                                                      | `many2many` |     | ✅    | res.groups |
| `id`           | ID                                                                     | `integer`   |     | ✅    |            |
| `is_editable`  | Determines if the canned response can be edited by the current user    | `boolean`   |     |       |            |
| `is_shared`    | Determines if the canned_response is currently shared with other users | `boolean`   |     | ✅    |            |
| `last_used`    | Last Used                                                              | `datetime`  |     | ✅    |            |
| `source`       | Shortcut                                                               | `char`      | ✅  | ✅    |            |
| `substitution` | Substitution                                                           | `text`      | ✅  | ✅    |            |
| `write_date`   | Last Updated on                                                        | `datetime`  |     | ✅    |            |
| `write_uid`    | Last Updated by                                                        | `many2one`  |     | ✅    | res.users  |

**Access Rights:**

| Name                 | Group       | Perms     |
| -------------------- | ----------- | --------- |
| mail.canned.response | Role / User | `R/W/C/D` |

**Record Rules:**

- **Canned response: admin has all access on shared canned response** (16) `R/W/D`
  - Domain: `[('is_shared', '=', True)]`
- **Canned response: User read: own or in groups** (1) `R`
  - Domain:
    `['|', ('create_uid', '=', user.id), ('group_ids', 'in', user.all_group_ids.ids)]`
- **Canned response: User write/unlink: own only** (1) `W/D`
  - Domain: `[('create_uid', '=', user.id)]`

### 🗃️ `bus.listener.mixin` — Can send messages via bus.bus

Allow sending messages related to the current model via as a bus.bus channel.

    The model needs to be allowed as a valid channel for the bus in `_build_bus_channel_list`.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

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

### 🗃️ `res.config.settings` — Config Settings

> ✳️ Transient (Wizard)

Enhanced configuration interface for exchange rate management

**Fields:**

| Field                                                | Label                                                                                           | Type        | Req | Store | Relation                         |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------- | --- | ----- | -------------------------------- |
| `access_token`                                       | Access Token                                                                                    | `char`      |     | ✅    |                                  |
| `account_cash_basis_base_account_id`                 | Base Tax Received Account                                                                       | `many2one`  |     |       | account.account                  |
| `account_default_credit_limit`                       | Default Credit Limit                                                                            | `monetary`  |     |       |                                  |
| `account_discount_expense_allocation_id`             | Customer Invoices Discounts Account                                                             | `many2one`  |     |       | account.account                  |
| `account_discount_income_allocation_id`              | Vendor Bills Discounts Account                                                                  | `many2one`  |     |       | account.account                  |
| `account_fiscal_country_id`                          | Fiscal Country Code                                                                             | `many2one`  |     |       | res.country                      |
| `account_journal_early_pay_discount_gain_account_id` | Early Discount Gain                                                                             | `many2one`  |     |       | account.account                  |
| `account_journal_early_pay_discount_loss_account_id` | Early Discount Loss                                                                             | `many2one`  |     |       | account.account                  |
| `account_journal_suspense_account_id`                | Bank Suspense                                                                                   | `many2one`  |     |       | account.account                  |
| `account_on_checkout`                                | Customer Accounts                                                                               | `selection` | ✅  |       |                                  |
| `account_price_include`                              | Default Sales Price Include                                                                     | `selection` | ✅  |       |                                  |
| `account_storno`                                     | Storno accounting                                                                               | `boolean`   |     |       |                                  |
| `account_use_credit_limit`                           | Sales Credit Limit                                                                              | `boolean`   |     |       |                                  |
| `active_provider_id`                                 | Active Provider                                                                                 | `many2one`  |     |       | payment.provider                 |
| `active_user_count`                                  | Number of Active Users                                                                          | `integer`   |     |       |                                  |
| `add_to_cart_action`                                 | Add To Cart Action                                                                              | `selection` |     |       |                                  |
| `alias_domain_id`                                    | Alias Domain                                                                                    | `many2one`  |     |       | mail.alias.domain                |
| `anglo_saxon_accounting`                             | Use anglo-saxon accounting                                                                      | `boolean`   |     |       |                                  |
| `annual_inventory_day`                               | Day of the month                                                                                | `integer`   |     |       |                                  |
| `annual_inventory_month`                             | Annual Inventory Month                                                                          | `selection` |     |       |                                  |
| `app_login_details_show`                             | Replace Login URL                                                                               | `boolean`   |     | ✅    |                                  |
| `app_login_name`                                     | Login Page Name                                                                                 | `char`      |     | ✅    |                                  |
| `app_login_url`                                      | Login Page URL                                                                                  | `char`      |     | ✅    |                                  |
| `app_ribbon_name`                                    | Show Demo Ribbon                                                                                | `char`      |     | ✅    |                                  |
| `app_ribbon_name_show`                               | Show Ribbon                                                                                     | `boolean`   |     | ✅    |                                  |
| `app_show_lang`                                      | Show Quick Language Switcher                                                                    | `boolean`   |     | ✅    |                                  |
| `app_system_name`                                    | System Name                                                                                     | `char`      |     | ✅    |                                  |
| `attendance_subject_generic`                         | Attendance Subject Generic                                                                      | `selection` |     | ✅    |                                  |
| `auth_signup_reset_password`                         | Enable password reset from Login page                                                           | `boolean`   |     | ✅    |                                  |
| `auth_signup_template_user_id`                       | Template user for new users created through signup                                              | `many2one`  |     | ✅    | res.users                        |
| `auth_signup_uninvited`                              | Customer Account                                                                                | `selection` |     |       |                                  |
| `auth_totp_enforce`                                  | Enforce two-factor authentication                                                               | `boolean`   |     | ✅    |                                  |
| `auth_totp_policy`                                   | Two-factor authentication enforcing policy                                                      | `selection` |     | ✅    |                                  |
| `automatic_email`                                    | Automatic Email                                                                                 | `boolean`   |     | ✅    |                                  |
| `automatic_invoice`                                  | Automatic Invoice                                                                               | `boolean`   |     | ✅    |                                  |
| `autopost_bills`                                     | Auto-validate bills                                                                             | `boolean`   |     |       |                                  |
| `barcode_nomenclature_id`                            | Nomenclature                                                                                    | `many2one`  |     |       | barcode.nomenclature             |
| `barcode_separator`                                  | Separator                                                                                       | `char`      |     | ✅    |                                  |
| `cart_abandoned_delay`                               | Abandoned Delay                                                                                 | `float`     |     |       |                                  |
| `cart_recovery_mail_template`                        | Cart Recovery Email                                                                             | `many2one`  |     |       | mail.template                    |
| `cdn_activated`                                      | Content Delivery Network (CDN)                                                                  | `boolean`   |     |       |                                  |
| `cdn_filters`                                        | CDN Filters                                                                                     | `text`      |     |       |                                  |
| `cdn_url`                                            | CDN Base URL                                                                                    | `char`      |     |       |                                  |
| `channel_id`                                         | Website Live Channel                                                                            | `many2one`  |     |       | im_livechat.channel              |
| `chart_template`                                     | Chart Template                                                                                  | `selection` |     | ✅    |                                  |
| `client_id`                                          | Client ID                                                                                       | `char`      |     | ✅    |                                  |
| `client_secret`                                      | Client Secret                                                                                   | `char`      |     | ✅    |                                  |
| `company_count`                                      | Number of Companies                                                                             | `integer`   |     |       |                                  |
| `company_country_code`                               | Company Country Code                                                                            | `char`      |     |       |                                  |
| `company_country_group_codes`                        | Country Group Codes                                                                             | `json`      |     |       |                                  |
| `company_currency_id`                                | Company Currency                                                                                | `many2one`  |     |       | res.currency                     |
| `company_expense_allowed_payment_method_line_ids`    | Payment methods available for expenses paid by company                                          | `many2many` |     |       | account.payment.method.line      |
| `company_id`                                         | Company                                                                                         | `many2one`  | ✅  | ✅    | res.company                      |
| `company_informations`                               | Company Informations                                                                            | `text`      |     |       |                                  |
| `company_name`                                       | Company Name                                                                                    | `char`      |     |       |                                  |
| `company_so_template_id`                             | Default Template                                                                                | `many2one`  |     |       | sale.order.template              |
| `confirmation_email_template_id`                     | Confirmation Email Template                                                                     | `many2one`  |     |       | mail.template                    |
| `contract_expiration_notice_period`                  | Contract Expiry Notice Period                                                                   | `integer`   |     |       |                                  |
| `country_code`                                       | Country Code                                                                                    | `char`      |     |       |                                  |
| `create_date`                                        | Created on                                                                                      | `datetime`  |     | ✅    |                                  |
| `create_uid`                                         | Created by                                                                                      | `many2one`  |     | ✅    | res.users                        |
| `crm_auto_assignment_action`                         | Auto Assignment Action                                                                          | `selection` |     | ✅    |                                  |
| `crm_auto_assignment_interval_number`                | Repeat every                                                                                    | `integer`   |     | ✅    |                                  |
| `crm_auto_assignment_interval_type`                  | Auto Assignment Interval Unit                                                                   | `selection` |     | ✅    |                                  |
| `crm_auto_assignment_run_datetime`                   | Auto Assignment Next Execution Date                                                             | `datetime`  |     | ✅    |                                  |
| `crm_use_auto_assignment`                            | Rule-Based Assignment                                                                           | `boolean`   |     | ✅    |                                  |
| `currency_exchange_journal_id`                       | Currency Exchange Journal                                                                       | `many2one`  |     |       | account.journal                  |
| `currency_id`                                        | Currency                                                                                        | `many2one`  | ✅  |       | res.currency                     |
| `days_to_purchase`                                   | Days to Purchase                                                                                | `float`     |     |       |                                  |
| `default_allow_out_of_stock_order`                   | Continue selling when out-of-stock                                                              | `boolean`   |     | ✅    |                                  |
| `default_available_threshold`                        | Show Threshold                                                                                  | `float`     |     | ✅    |                                  |
| `default_invoice_policy`                             | Invoicing Policy                                                                                | `selection` |     | ✅    |                                  |
| `default_picking_policy`                             | Picking Policy                                                                                  | `selection` | ✅  | ✅    |                                  |
| `default_show_availability`                          | Show availability Qty                                                                           | `boolean`   |     | ✅    |                                  |
| `delay_alert_contract`                               | Delay alert contract outdated                                                                   | `integer`   |     | ✅    |                                  |
| `digest_emails`                                      | Digest Emails                                                                                   | `boolean`   |     | ✅    |                                  |
| `digest_id`                                          | Digest Email                                                                                    | `many2one`  |     | ✅    | digest.digest                    |
| `display_account_storno`                             | Display Account Storno                                                                          | `boolean`   |     |       |                                  |
| `display_invoice_amount_total_words`                 | Total amount of invoice in letters                                                              | `boolean`   |     |       |                                  |
| `display_invoice_tax_company_currency`               | Taxes in company currency                                                                       | `boolean`   |     |       |                                  |
| `display_name`                                       | Display Name                                                                                    | `char`      |     |       |                                  |
| `documents_binary_max_size`                          | Size                                                                                            | `integer`   |     | ✅    |                                  |
| `documents_forbidden_extensions`                     | Extensions                                                                                      | `char`      |     | ✅    |                                  |
| `downpayment_account_id`                             | Downpayment Account                                                                             | `many2one`  |     |       | account.account                  |
| `ecommerce_access`                                   | Ecommerce Access                                                                                | `selection` |     |       |                                  |
| `email_primary_color`                                | Email Button Text                                                                               | `char`      |     |       |                                  |
| `email_secondary_color`                              | Email Button Color                                                                              | `char`      |     |       |                                  |
| `enable_academic_plan`                               | Academic Plan                                                                                   | `boolean`   |     | ✅    |                                  |
| `enable_create_student_user`                         | Create Student User                                                                             | `boolean`   |     | ✅    |                                  |
| `enable_exchange_rate_module`                        | Enable Exchange Rate Synchronization                                                            | `boolean`   |     | ✅    |                                  |
| `enable_recaptcha`                                   | Enable reCAPTCHA                                                                                | `boolean`   |     | ✅    |                                  |
| `expense_account_id`                                 | Expense Account                                                                                 | `many2one`  |     |       | account.account                  |
| `expense_currency_exchange_account_id`               | Loss Exchange Rate Account                                                                      | `many2one`  |     |       | account.account                  |
| `expense_journal_id`                                 | Default Expense Journal                                                                         | `many2one`  |     |       | account.journal                  |
| `external_email_server_default`                      | Use Custom Email Servers                                                                        | `boolean`   |     | ✅    |                                  |
| `external_report_layout_id`                          | Document Template                                                                               | `many2one`  |     |       | ir.ui.view                       |
| `fail_counter`                                       | Fail Mail                                                                                       | `integer`   |     |       |                                  |
| `favicon`                                            | Favicon                                                                                         | `binary`    |     |       |                                  |
| `fiscalyear_last_day`                                | Fiscalyear Last Day                                                                             | `integer`   |     |       |                                  |
| `fiscalyear_last_month`                              | Fiscalyear Last Month                                                                           | `selection` |     |       |                                  |
| `fiscalyear_lock_date`                               | Global Lock Date                                                                                | `date`      |     |       |                                  |
| `force_restrictive_audit_trail`                      | Forced Audit Trail                                                                              | `boolean`   |     |       |                                  |
| `global_calendar_user_id`                            | Calendar User                                                                                   | `many2one`  |     | ✅    | res.users                        |
| `google_analytics_key`                               | Google Analytics Key                                                                            | `char`      |     |       |                                  |
| `google_gmail_client_identifier`                     | Gmail Client Id                                                                                 | `char`      |     | ✅    |                                  |
| `google_gmail_client_secret`                         | Gmail Client Secret                                                                             | `char`      |     | ✅    |                                  |
| `google_maps_static_api_key`                         | Google Maps API key                                                                             | `char`      |     | ✅    |                                  |
| `google_maps_static_api_secret`                      | Google Maps API secret                                                                          | `char`      |     | ✅    |                                  |
| `google_search_console`                              | Google Search Console Key                                                                       | `char`      |     |       |                                  |
| `google_translate_api_key`                           | Message Translation API Key                                                                     | `char`      |     | ✅    |                                  |
| `group_analytic_accounting`                          | Analytic Accounting                                                                             | `boolean`   |     | ✅    |                                  |
| `group_auto_done_setting`                            | Lock Confirmed Sales                                                                            | `boolean`   |     | ✅    |                                  |
| `group_cash_rounding`                                | Cash Rounding                                                                                   | `boolean`   |     | ✅    |                                  |
| `group_discount_per_so_line`                         | Discounts                                                                                       | `boolean`   |     | ✅    |                                  |
| `group_fiscal_year`                                  | Fiscal Years                                                                                    | `boolean`   |     | ✅    |                                  |
| `group_gmc_feed`                                     | Google Merchant Center                                                                          | `boolean`   |     |       |                                  |
| `group_lot_on_delivery_slip`                         | Display Lots & Serial Numbers on Delivery Slips                                                 | `boolean`   |     | ✅    |                                  |
| `group_lot_on_invoice`                               | Display Lots & Serial Numbers on Invoices                                                       | `boolean`   |     | ✅    |                                  |
| `group_mass_mailing_campaign`                        | Mailing Campaigns                                                                               | `boolean`   |     | ✅    |                                  |
| `group_multi_currency`                               | Multi-Currencies                                                                                | `boolean`   |     | ✅    |                                  |
| `group_multi_website`                                | Multi-website                                                                                   | `boolean`   |     | ✅    |                                  |
| `group_product_price_comparison`                     | Comparison Price                                                                                | `boolean`   |     | ✅    |                                  |
| `group_product_pricelist`                            | Pricelists                                                                                      | `boolean`   |     | ✅    |                                  |
| `group_product_variant`                              | Variants                                                                                        | `boolean`   |     | ✅    |                                  |
| `group_proforma_sales`                               | Pro-Forma Invoice                                                                               | `boolean`   |     | ✅    |                                  |
| `group_sale_delivery_address`                        | Customer Addresses                                                                              | `boolean`   |     | ✅    |                                  |
| `group_sale_order_template`                          | Quotation Templates                                                                             | `boolean`   |     | ✅    |                                  |
| `group_send_reminder`                                | Receipt Reminder                                                                                | `boolean`   |     | ✅    |                                  |
| `group_show_uom_price`                               | Base Unit Price                                                                                 | `boolean`   |     | ✅    |                                  |
| `group_stock_adv_location`                           | Multi-Step Routes                                                                               | `boolean`   |     | ✅    |                                  |
| `group_stock_lot_print_gs1`                          | Print GS1 Barcodes for Lots & Serial Numbers                                                    | `boolean`   |     | ✅    |                                  |
| `group_stock_multi_locations`                        | Storage Locations                                                                               | `boolean`   |     | ✅    |                                  |
| `group_stock_production_lot`                         | Lots & Serial Numbers                                                                           | `boolean`   |     | ✅    |                                  |
| `group_stock_reception_report`                       | Reception Report                                                                                | `boolean`   |     | ✅    |                                  |
| `group_stock_sign_delivery`                          | Signature                                                                                       | `boolean`   |     | ✅    |                                  |
| `group_stock_tracking_lot`                           | Packages                                                                                        | `boolean`   |     | ✅    |                                  |
| `group_stock_tracking_owner`                         | Consignment                                                                                     | `boolean`   |     | ✅    |                                  |
| `group_uom`                                          | Units of Measure & Packagings                                                                   | `boolean`   |     | ✅    |                                  |
| `group_use_lead`                                     | Leads                                                                                           | `boolean`   |     | ✅    |                                  |
| `group_use_recurring_revenues`                       | Recurring Revenues                                                                              | `boolean`   |     | ✅    |                                  |
| `group_warning_purchase`                             | Purchase Warnings                                                                               | `boolean`   |     | ✅    |                                  |
| `group_warning_sale`                                 | Sale Order Warnings                                                                             | `boolean`   |     | ✅    |                                  |
| `group_warning_stock`                                | Warnings for Stock                                                                              | `boolean`   |     | ✅    |                                  |
| `hard_lock_date`                                     | Hard Lock Date                                                                                  | `date`      |     |       |                                  |
| `has_accounting_entries`                             | Has Accounting Entries                                                                          | `boolean`   |     |       |                                  |
| `has_chart_of_accounts`                              | Company has a chart of accounts                                                                 | `boolean`   |     |       |                                  |
| `has_default_share_image`                            | Use a image by default for sharing                                                              | `boolean`   |     |       |                                  |
| `has_enabled_provider`                               | Has Enabled Provider                                                                            | `boolean`   |     |       |                                  |
| `has_google_analytics`                               | Google Analytics                                                                                | `boolean`   |     |       |                                  |
| `has_google_search_console`                          | Google Search Console                                                                           | `boolean`   |     |       |                                  |
| `has_plausible_shared_key`                           | Plausible Analytics                                                                             | `boolean`   |     |       |                                  |
| `horizon_days`                                       | Replenishment Horizon                                                                           | `float`     |     |       |                                  |
| `hr_expense_alias_domain_id`                         | Hr Expense Alias Domain                                                                         | `many2one`  |     |       | mail.alias.domain                |
| `hr_expense_alias_prefix`                            | Default Alias Name for Expenses                                                                 | `char`      |     | ✅    |                                  |
| `hr_expense_use_mailgateway`                         | Let your employees record expenses by email                                                     | `boolean`   |     | ✅    |                                  |
| `hr_presence_control_email`                          | Based on number of emails sent                                                                  | `boolean`   |     |       |                                  |
| `hr_presence_control_email_amount`                   | # emails to send                                                                                | `integer`   |     |       |                                  |
| `hr_presence_control_ip`                             | Based on IP Address                                                                             | `boolean`   |     |       |                                  |
| `hr_presence_control_ip_list`                        | Valid IP addresses                                                                              | `char`      |     |       |                                  |
| `hr_presence_control_login`                          | Based on user status in system                                                                  | `boolean`   |     |       |                                  |
| `id`                                                 | ID                                                                                              | `integer`   |     | ✅    |                                  |
| `income_account_id`                                  | Income Account                                                                                  | `many2one`  |     |       | account.account                  |
| `income_currency_exchange_account_id`                | Gain Exchange Rate Account                                                                      | `many2one`  |     |       | account.account                  |
| `incoterm_id`                                        | Default incoterm                                                                                | `many2one`  |     |       | account.incoterms                |
| `invoice_mail_template_id`                           | Email Template                                                                                  | `many2one`  |     | ✅    | mail.template                    |
| `invoice_terms`                                      | Terms & Conditions                                                                              | `html`      |     |       |                                  |
| `invoice_terms_html`                                 | Terms & Conditions as a Web page                                                                | `html`      |     |       |                                  |
| `is_account_peppol_eligible`                         | PEPPOL eligible                                                                                 | `boolean`   |     |       |                                  |
| `is_batch_and_subject_constraint`                    | Batch and Subject Constraint                                                                    | `boolean`   |     | ✅    |                                  |
| `is_batch_constraint`                                | Batch Constraint                                                                                | `boolean`   |     | ✅    |                                  |
| `is_classroom_constraint`                            | Classroom Constraint                                                                            | `boolean`   |     | ✅    |                                  |
| `is_faculty_constraint`                              | Faculty Constraint                                                                              | `boolean`   |     | ✅    |                                  |
| `is_hash_verified`                                   | Is Hash Verified                                                                                | `boolean`   |     |       |                                  |
| `is_installed_sale`                                  | Is the Sale Module Installed                                                                    | `boolean`   |     | ✅    |                                  |
| `is_mail_sent`                                       | Is Mail Sent                                                                                    | `boolean`   |     |       |                                  |
| `is_membership_multi`                                | Multi Teams                                                                                     | `boolean`   |     | ✅    |                                  |
| `is_newsletter_enabled`                              | Is Newsletter Enabled                                                                           | `boolean`   |     | ✅    |                                  |
| `is_root_company`                                    | Is Root Company                                                                                 | `boolean`   |     |       |                                  |
| `language_count`                                     | Number of Languages                                                                             | `integer`   |     |       |                                  |
| `language_ids`                                       | Languages                                                                                       | `many2many` |     |       | res.lang                         |
| `lead_enrich_auto`                                   | Enrich lead automatically                                                                       | `selection` |     | ✅    |                                  |
| `lead_mining_in_pipeline`                            | Create a lead mining request directly from the opportunity pipeline.                            | `boolean`   |     | ✅    |                                  |
| `link_qr_code`                                       | Display Link QR-code                                                                            | `boolean`   |     |       |                                  |
| `lock_confirmed_po`                                  | Lock Confirmed Orders                                                                           | `boolean`   |     | ✅    |                                  |
| `mass_mailing_mail_server_id`                        | Mail Server                                                                                     | `many2one`  |     | ✅    | ir.mail_server                   |
| `mass_mailing_outgoing_mail_server`                  | Dedicated Server                                                                                | `boolean`   |     | ✅    |                                  |
| `mass_mailing_reports`                               | 24H Stat Mailing Reports                                                                        | `boolean`   |     | ✅    |                                  |
| `mass_mailing_split_contact_name`                    | Split First and Last Name                                                                       | `boolean`   |     | ✅    |                                  |
| `menu_bg_image`                                      | Apps Menu Footer Image                                                                          | `binary`    |     |       |                                  |
| `microsoft_outlook_client_identifier`                | Outlook Client Id                                                                               | `char`      |     | ✅    |                                  |
| `microsoft_outlook_client_secret`                    | Outlook Client Secret                                                                           | `char`      |     | ✅    |                                  |
| `module_account_3way_match`                          | 3-way matching: purchases, receptions and bills                                                 | `boolean`   |     | ✅    |                                  |
| `module_account_accountant`                          | Accounting                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_account_bank_statement_extract`              | Bank Statement Digitization                                                                     | `boolean`   |     | ✅    |                                  |
| `module_account_bank_statement_import_qif`           | Import .qif files                                                                               | `boolean`   |     | ✅    |                                  |
| `module_account_batch_payment`                       | Use batch payments                                                                              | `boolean`   |     | ✅    |                                  |
| `module_account_budget`                              | Budget Management                                                                               | `boolean`   |     | ✅    |                                  |
| `module_account_check_printing`                      | Allow check printing and deposits                                                               | `boolean`   |     | ✅    |                                  |
| `module_account_extract`                             | Document Digitization                                                                           | `boolean`   |     | ✅    |                                  |
| `module_account_inter_company_rules`                 | Manage Inter Company                                                                            | `boolean`   |     | ✅    |                                  |
| `module_account_intrastat`                           | Intrastat                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_account_invoice_extract`                     | Invoice Digitization                                                                            | `boolean`   |     | ✅    |                                  |
| `module_account_iso20022`                            | SEPA Credit Transfer / ISO20022                                                                 | `boolean`   |     | ✅    |                                  |
| `module_account_payment`                             | Invoice Online Payment                                                                          | `boolean`   |     | ✅    |                                  |
| `module_account_peppol`                              | PEPPOL Invoicing                                                                                | `boolean`   |     | ✅    |                                  |
| `module_account_reports`                             | Dynamic Reports                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_account_sepa_direct_debit`                   | Use SEPA Direct Debit                                                                           | `boolean`   |     | ✅    |                                  |
| `module_auth_ldap`                                   | LDAP Authentication                                                                             | `boolean`   |     | ✅    |                                  |
| `module_auth_oauth`                                  | Use external authentication providers (OAuth)                                                   | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup`                        | Database Backup to Local Server                                                                 | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_dropbox`                | Database Backup to Dropbox                                                                      | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_ftp`                    | Database Backup to Remote FTP Server                                                            | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_google_drive`           | Database Backup to Google Drive                                                                 | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_onedrive`               | Database Backup to Onedrive                                                                     | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_sftp`                   | Database Backup to Remote SFTP Server                                                           | `boolean`   |     | ✅    |                                  |
| `module_backend_theme`                               | Backend Theme                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_base_geolocalize`                            | GeoLocalize                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_base_import`                                 | Allow users to import data from CSV/XLS/XLSX/ODS files                                          | `boolean`   |     | ✅    |                                  |
| `module_bigbluebutton`                               | Bigbluebutton Enterprise                                                                        | `boolean`   |     | ✅    |                                  |
| `module_crm_iap_enrich`                              | Enrich your leads automatically with company data based on their email address.                 | `boolean`   |     | ✅    |                                  |
| `module_crm_iap_mine`                                | Generate new leads based on their country, industries, size, etc.                               | `boolean`   |     | ✅    |                                  |
| `module_currency_rate_live`                          | Automatic Currency Rates                                                                        | `boolean`   |     | ✅    |                                  |
| `module_delivery`                                    | Delivery Methods                                                                                | `boolean`   |     | ✅    |                                  |
| `module_delivery_bpost`                              | bpost Connector                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_delivery_dhl`                                | DHL Express Connector                                                                           | `boolean`   |     | ✅    |                                  |
| `module_delivery_easypost`                           | Easypost Connector                                                                              | `boolean`   |     | ✅    |                                  |
| `module_delivery_envia`                              | Envia.com Connector                                                                             | `boolean`   |     | ✅    |                                  |
| `module_delivery_fedex_rest`                         | FedEx Connector                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_delivery_sendcloud`                          | Sendcloud Connector                                                                             | `boolean`   |     | ✅    |                                  |
| `module_delivery_shiprocket`                         | Shiprocket Connector                                                                            | `boolean`   |     | ✅    |                                  |
| `module_delivery_starshipit`                         | Starshipit Connector                                                                            | `boolean`   |     | ✅    |                                  |
| `module_delivery_ups_rest`                           | UPS Connector                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_delivery_usps_rest`                          | USPS Connector                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_event_booth`                                 | Booth Management                                                                                | `boolean`   |     | ✅    |                                  |
| `module_event_sale`                                  | Tickets with Sale                                                                               | `boolean`   |     | ✅    |                                  |
| `module_google_address_autocomplete`                 | Google Address Autocomplete                                                                     | `boolean`   |     | ✅    |                                  |
| `module_google_calendar`                             | Allow the users to synchronize their calendar with Google Calendar                              | `boolean`   |     | ✅    |                                  |
| `module_google_gmail`                                | Support Gmail Authentication                                                                    | `boolean`   |     | ✅    |                                  |
| `module_googlemeet`                                  | Google Meet                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_google_recaptcha`                            | reCAPTCHA                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_helpdesk_elearning`                          | E-Learning                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_helpdesk_forum`                              | Helpdesk Forum                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_helpdesk_project_ext`                        | Helpdesk project                                                                                | `boolean`   |     | ✅    |                                  |
| `module_hr_attendance`                               | Based on attendances                                                                            | `boolean`   |     |       |                                  |
| `module_hr_expense_extract`                          | Send bills to OCR to generate expenses                                                          | `boolean`   |     | ✅    |                                  |
| `module_hr_expense_stripe`                           | Link your stripe issuing account to manage company credit cards for your employees through Odoo | `boolean`   |     | ✅    |                                  |
| `module_hr_payroll_expense`                          | Reimburse Expenses in Payslip                                                                   | `boolean`   |     | ✅    |                                  |
| `module_hr_presence`                                 | Advanced Presence Control                                                                       | `boolean`   |     | ✅    |                                  |
| `module_hr_recruitment_extract`                      | Send CV to OCR to fill applications                                                             | `boolean`   |     | ✅    |                                  |
| `module_hr_recruitment_survey`                       | Interview Forms                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_hr_skills`                                   | Skills Management                                                                               | `boolean`   |     | ✅    |                                  |
| `module_loyalty`                                     | Promotions, Coupons, Gift Card & Loyalty Program                                                | `boolean`   |     | ✅    |                                  |
| `module_mail_plugin`                                 | Allow integration with the mail plugins                                                         | `boolean`   |     | ✅    |                                  |
| `module_microsoft_calendar`                          | Allow the users to synchronize their calendar with Outlook Calendar                             | `boolean`   |     | ✅    |                                  |
| `module_microsoft_outlook`                           | Support Outlook Authentication                                                                  | `boolean`   |     | ✅    |                                  |
| `module_online_appointment`                          | Online Appointment Enterprise                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_achievement_enterprise`           | Achievement Enterprise                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_activity`                         | Activity                                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_activity_enterprise`              | Activity Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_admission`                        | Admission                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_admission_enterprise`             | Admission Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_admission_grading_bridge`         | Admission Grading Bridge                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_blog_enterprise`           | Alumni Blog Enterprise                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_enterprise`                | Alumni Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_event_enterprise`          | Alumni Event Enterprise                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_job_enterprise`            | Alumni Job Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_asset_request_enterprise`         | Asset Request Enterprise                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment`                       | Assignment                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_enterprise`            | Assignment Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_grading_bridge`        | Assignment Gradebook Bridge                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_grading_enterprise`    | Assignment Grading Enterprise                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_rubrics`               | Assignment Rubrics                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance`                       | Attendance                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance_enterprise`            | Attendance Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance_face_recognition`      | Attendance Face Recognition                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance_report_xlsx`           | Attendance Xlsx Report                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_campus_enterprise`                | Campus Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_classroom`                        | Classroom                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_classroom_enterprise`             | Classroom Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_convocation`                      | Convocation                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_crm_enterprise`                   | CRM Enterprise                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_dashboard_kpi`                    | Dashboard KPI                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_digital_library`                  | Digital Library                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_openeducat_discipline`                       | Discipline Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_dynamic_admission`                | Dynamic Admission                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_event_enterprise`                 | Event Enterprise                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam`                             | Exam                                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_enterprise`                  | Exam Enterprise                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_gpa_enterprise`              | Exam GPA Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_grading_bridge`              | Exam Grading Bridge                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_migration_bridge`            | Student Migration Exam Bridge                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_facility`                         | Facility                                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_facility_enterprise`              | Facility Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_fees`                             | Fees                                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_fees_parent_bridge`               | Fees Parent Bridge                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_fees_plan`                        | Fees Plan                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_grading`                          | Grading                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_grading_migration_bridge`         | Student Migration Grading Bridge                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_grievance_enterprise`             | Grievance                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_health_enterprise`                | Health Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_jitsi_enterprise`                 | Jitsi Enterprise                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_job_enterprise`                   | Job Enterprise                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lesson`                           | Lesson Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_library`                          | Library                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_library_barcode`                  | Library Barcode Enterprise                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_library_enterprise`               | Library Enterprise                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live`                             | Live Meeting                                                                                    | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live_assignment`                  | Live Meeting Assignment                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live_attendance`                  | Live Meeting Attendance                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live_attentiveness`               | Live Meeting Attentiveness                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms`                              | LMS Enterprise                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_admission`                    | LMS Admission                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_blog`                         | LMS Blog Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_forum`                        | LMS Forum Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_gamification`                 | LMS Gamification Enterprise                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_h5p`                          | LMS H5P Enterprise                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_sale`                         | LMS Sale Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_survey`                       | LMS Survey Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_mass_subject_registration`        | Mass Subject Registration                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_meeting_enterprise`               | Meeting Enterprise                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_notice_board_enterprise`          | Notice Board Enterprise                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_omr`                              | OMR                                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_parent`                           | Parent                                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_parent_enterprise`                | Parent Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_placement_enterprise`             | Placement Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_placement_job_enterprise`         | Placement Job Enterprise                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_quiz`                             | Quiz Enterprise                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_openeducat_quiz_anti_cheating`               | Quiz Anti Cheating                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_scholarship_enterprise`           | Scholarship Enterprise                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_secure`                           | Secure QR                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_skill_enterprise`                 | Skill Enterprise                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_skypemeet`                        | Skype Meet                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_attendance_enterprise`    | Student Attendance Kiosk                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_feedback_management`      | Student Feedback                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_leave_enterprise`         | Student Leave                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_mentor`                   | Student Mentor                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_progress_enterprise`      | Student Progress Enterprise                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_skill_assessment`         | Skill Assessment Enterprise                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_withdrawal_mgmt`          | Student Withdrawal Management                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_subject_material_allocation`      | Subject Material Allocation                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_thesis`                           | Thesis                                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_timetable`                        | Timetable                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_timetable_enterprise`             | Timetable Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_transportation_enterprise`        | Transportation Enterprise                                                                       | `boolean`   |     | ✅    |                                  |
| `module_partner_autocomplete`                        | Partner Autocomplete                                                                            | `boolean`   |     | ✅    |                                  |
| `module_partnership`                                 | Membership / Partnership                                                                        | `boolean`   |     | ✅    |                                  |
| `module_pos_event`                                   | Tickets with PoS                                                                                | `boolean`   |     | ✅    |                                  |
| `module_product_email_template`                      | Specific Email                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_product_expiry`                              | Expiration Dates                                                                                | `boolean`   |     | ✅    |                                  |
| `module_product_margin`                              | Allow Product Margin                                                                            | `boolean`   |     | ✅    |                                  |
| `module_purchase_product_matrix`                     | Purchase Grid Entry                                                                             | `boolean`   |     | ✅    |                                  |
| `module_purchase_requisition`                        | Purchase Agreements                                                                             | `boolean`   |     | ✅    |                                  |
| `module_quality_control`                             | Quality                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_quality_control_worksheet`                   | Quality Worksheet                                                                               | `boolean`   |     | ✅    |                                  |
| `module_sale_amazon`                                 | Amazon Sync                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_sale_commission`                             | Commissions                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_sale_gelato`                                 | Gelato                                                                                          | `boolean`   |     | ✅    |                                  |
| `module_sale_loyalty`                                | Coupons & Loyalty                                                                               | `boolean`   |     | ✅    |                                  |
| `module_sale_margin`                                 | Margins                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_sale_pdf_quote_builder`                      | PDF Quote builder                                                                               | `boolean`   |     | ✅    |                                  |
| `module_sale_product_matrix`                         | Sales Grid Entry                                                                                | `boolean`   |     | ✅    |                                  |
| `module_sale_shopee`                                 | Shopee Sync                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_sms`                                         | SMS                                                                                             | `boolean`   |     | ✅    |                                  |
| `module_snailmail_account`                           | Snailmail                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_stock_barcode`                               | Barcode Scanner                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_stock_barcode_barcodelookup`                 | Stock Barcode Database                                                                          | `boolean`   |     | ✅    |                                  |
| `module_stock_dropshipping`                          | Dropshipping                                                                                    | `boolean`   |     | ✅    |                                  |
| `module_stock_fleet`                                 | Dispatch Management System                                                                      | `boolean`   |     | ✅    |                                  |
| `module_stock_landed_costs`                          | Landed Costs                                                                                    | `boolean`   |     | ✅    |                                  |
| `module_stock_picking_batch`                         | Batch, Wave & Cluster Transfers                                                                 | `boolean`   |     | ✅    |                                  |
| `module_stock_sms`                                   | SMS Confirmation                                                                                | `boolean`   |     | ✅    |                                  |
| `module_teams`                                       | Teams                                                                                           | `boolean`   |     | ✅    |                                  |
| `module_voip`                                        | Phone                                                                                           | `boolean`   |     | ✅    |                                  |
| `module_website_cf_turnstile`                        | Cloudflare Turnstile                                                                            | `boolean`   |     | ✅    |                                  |
| `module_website_crm_iap_reveal`                      | Create Leads/Opportunities from your website's traffic                                          | `boolean`   |     | ✅    |                                  |
| `module_website_event_exhibitor`                     | Advanced Sponsors                                                                               | `boolean`   |     | ✅    |                                  |
| `module_website_event_sale`                          | Online Ticketing                                                                                | `boolean`   |     | ✅    |                                  |
| `module_website_event_track`                         | Tracks and Agenda                                                                               | `boolean`   |     | ✅    |                                  |
| `module_website_event_track_live`                    | Live Mode                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_website_event_track_quiz`                    | Quiz on Tracks                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_website_helpdesk_mgmt`                       | Helpdesk Website                                                                                | `boolean`   |     | ✅    |                                  |
| `module_website_hr_recruitment`                      | Online Posting                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_website_livechat`                            | Module Website Livechat                                                                         | `boolean`   |     | ✅    |                                  |
| `module_website_sale_autocomplete`                   | Address Autocomplete                                                                            | `boolean`   |     | ✅    |                                  |
| `module_website_sale_collect`                        | Click & Collect                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_web_unsplash`                                | Unsplash Image Library                                                                          | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_account_templates`                  | Account Templates                                                                               | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_ecommerce_templates`                | Whatsapp Ecommerce Templates                                                                    | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_education_templates`                | Education Templates                                                                             | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_other_templates`                    | Other Templates                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_services_templates`                 | Services Templates                                                                              | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_special_occasions_template`         | Special Occasions Templates                                                                     | `boolean`   |     | ✅    |                                  |
| `module_zoom`                                        | Zoom                                                                                            | `boolean`   |     | ✅    |                                  |
| `newsletter_id`                                      | Newsletter List                                                                                 | `many2one`  |     |       | mailing.list                     |
| `next_execution_timestamp`                           | Next Execution Time                                                                             | `datetime`  |     |       |                                  |
| `onboarding_payment_module`                          | Onboarding Payment Module                                                                       | `selection` |     |       |                                  |
| `openeducat_instance_hash_key`                       | OpenEducat Instance Hash Key                                                                    | `char`      |     |       |                                  |
| `openeducat_instance_hash_msg`                       | Instance Hash Key Message                                                                       | `char`      |     |       |                                  |
| `openeducat_instance_key`                            | OpenEducat Instance Key                                                                         | `char`      |     |       |                                  |
| `parent_qrcode`                                      | QR Code                                                                                         | `boolean`   |     | ✅    |                                  |
| `partner_autocomplete_insufficient_credit`           | Insufficient credit                                                                             | `boolean`   |     |       |                                  |
| `pay_invoices_online`                                | Pay Invoices Online                                                                             | `boolean`   |     | ✅    |                                  |
| `plausible_shared_key`                               | Plausible auth Key                                                                              | `char`      |     |       |                                  |
| `plausible_site`                                     | Plausible Site (e.g. domain.com)                                                                | `char`      |     |       |                                  |
| `po_double_validation`                               | Levels of Approvals \*                                                                          | `selection` |     |       |                                  |
| `po_double_validation_amount`                        | Minimum Amount                                                                                  | `monetary`  |     |       |                                  |
| `po_lock`                                            | Purchase Order Modification \*                                                                  | `selection` |     |       |                                  |
| `po_order_approval`                                  | Purchase Order Approval                                                                         | `boolean`   |     | ✅    |                                  |
| `portal_allow_api_keys`                              | Customer API Keys                                                                               | `boolean`   |     |       |                                  |
| `portal_confirmation_pay`                            | Online Payment                                                                                  | `boolean`   |     |       |                                  |
| `portal_confirmation_sign`                           | Online Signature                                                                                | `boolean`   |     |       |                                  |
| `predictive_lead_scoring_field_labels`               | Predictive Lead Scoring Field Labels                                                            | `char`      |     |       |                                  |
| `predictive_lead_scoring_fields`                     | Lead Scoring Frequency Fields                                                                   | `many2many` |     |       | crm.lead.scoring.frequency.field |
| `predictive_lead_scoring_fields_str`                 | Lead Scoring Frequency Fields in String                                                         | `char`      |     | ✅    |                                  |
| `predictive_lead_scoring_start_date`                 | Lead Scoring Starting Date                                                                      | `date`      |     |       |                                  |
| `predictive_lead_scoring_start_date_str`             | Lead Scoring Starting Date in String                                                            | `char`      |     | ✅    |                                  |
| `prepayment_percent`                                 | Prepayment percentage                                                                           | `float`     |     |       |                                  |
| `preview_ready`                                      | Display preview button                                                                          | `boolean`   |     |       |                                  |
| `product_volume_volume_in_cubic_feet`                | Volume unit of measure                                                                          | `selection` |     | ✅    |                                  |
| `product_weight_in_lbs`                              | Weight unit of measure                                                                          | `selection` |     | ✅    |                                  |
| `profiling_enabled_until`                            | Profiling enabled until                                                                         | `datetime`  |     | ✅    |                                  |
| `purchase_lock_date`                                 | Purchases Lock Date                                                                             | `date`      |     |       |                                  |
| `purchase_tax_id`                                    | Default Purchase Tax                                                                            | `many2one`  |     |       | account.tax                      |
| `qr_code`                                            | Display SEPA QR-code                                                                            | `boolean`   |     |       |                                  |
| `quick_edit_mode`                                    | Quick encoding                                                                                  | `selection` |     |       |                                  |
| `quotation_validity_days`                            | Default Quotation Validity                                                                      | `integer`   |     |       |                                  |
| `rate_provider_selection`                            | Exchange Rate Provider                                                                          | `selection` |     |       |                                  |
| `recaptcha_min_score`                                | Minimum score                                                                                   | `float`     |     | ✅    |                                  |
| `recaptcha_private_key`                              | Secret Key                                                                                      | `char`      |     | ✅    |                                  |
| `recaptcha_public_key`                               | Site Key                                                                                        | `char`      |     | ✅    |                                  |
| `refresh_token`                                      | Refresh Token                                                                                   | `char`      |     | ✅    |                                  |
| `replenish_on_order`                                 | Replenish on Order (MTO)                                                                        | `boolean`   |     |       |                                  |
| `report_footer`                                      | Custom Report Footer                                                                            | `html`      |     |       |                                  |
| `resource_calendar_id`                               | Company Working Hours                                                                           | `many2one`  |     |       | resource.calendar                |
| `restrictive_audit_trail`                            | Restricted Audit Trail                                                                          | `boolean`   |     |       |                                  |
| `restrict_template_rendering`                        | Restrict Template Rendering                                                                     | `boolean`   |     | ✅    |                                  |
| `sale_lock_date`                                     | Sales Lock Date                                                                                 | `date`      |     |       |                                  |
| `salesperson_id`                                     | Salesperson                                                                                     | `many2one`  |     |       | res.users                        |
| `salesteam_id`                                       | Sales Team                                                                                      | `many2one`  |     |       | crm.team                         |
| `sale_tax_id`                                        | Default Sale Tax                                                                                | `many2one`  |     |       | account.tax                      |
| `secure_qr_code`                                     | Secure Qr Code                                                                                  | `selection` |     | ✅    |                                  |
| `security_lead`                                      | Security Lead Time                                                                              | `float`     |     |       |                                  |
| `send_abandoned_cart_email`                          | Abandoned Email                                                                                 | `boolean`   |     |       |                                  |
| `sfu_server_key`                                     | SFU Server key                                                                                  | `char`      |     | ✅    |                                  |
| `sfu_server_url`                                     | SFU Server URL                                                                                  | `char`      |     | ✅    |                                  |
| `shared_user_account`                                | Shared Customer Accounts                                                                        | `boolean`   |     |       |                                  |
| `show_blacklist_buttons`                             | Blacklist Option when Unsubscribing                                                             | `boolean`   |     | ✅    |                                  |
| `show_branding_in_footer`                            | Show Branding In Footer                                                                         | `boolean`   |     | ✅    |                                  |
| `show_effect`                                        | Show Effect                                                                                     | `boolean`   |     | ✅    |                                  |
| `show_line_subtotals_tax_selection`                  | Line Subtotals Tax Display                                                                      | `selection` |     |       |                                  |
| `show_sale_receipts`                                 | Sale Receipt                                                                                    | `boolean`   |     | ✅    |                                  |
| `snailmail_color`                                    | Print In Color                                                                                  | `boolean`   |     |       |                                  |
| `snailmail_cover`                                    | Add a Cover Page                                                                                | `boolean`   |     |       |                                  |
| `snailmail_cover_readonly`                           | Snailmail Cover Readonly                                                                        | `boolean`   |     |       |                                  |
| `snailmail_duplex`                                   | Print Both sides                                                                                | `boolean`   |     |       |                                  |
| `social_default_image`                               | Default Social Share Image                                                                      | `binary`    |     |       |                                  |
| `stock_confirmation_type`                            | Stock Text Validation type                                                                      | `selection` |     |       |                                  |
| `stock_move_email_validation`                        | Email Confirmation picking                                                                      | `boolean`   |     |       |                                  |
| `stock_sms_confirmation_template_id`                 | SMS Template                                                                                    | `many2one`  |     |       | sms.template                     |
| `stock_text_confirmation`                            | Stock Text Validation with stock move                                                           | `boolean`   |     |       |                                  |
| `synchronization_batch_size`                         | Batch Size                                                                                      | `integer`   |     |       |                                  |
| `synchronization_frequency`                          | Synchronization Frequency                                                                       | `selection` |     |       |                                  |
| `tax_calculation_rounding_method`                    | Tax calculation rounding method                                                                 | `selection` |     |       |                                  |
| `tax_cash_basis_journal_id`                          | Tax Cash Basis Journal                                                                          | `many2one`  |     |       | account.journal                  |
| `tax_exigibility`                                    | Cash Basis                                                                                      | `boolean`   |     |       |                                  |
| `tax_lock_date`                                      | Tax Lock Date                                                                                   | `date`      |     |       |                                  |
| `tenor_api_key`                                      | Tenor API key                                                                                   | `char`      |     | ✅    |                                  |
| `terms_type`                                         | Terms & Conditions format                                                                       | `selection` |     |       |                                  |
| `transfer_account_id`                                | Internal Transfer                                                                               | `many2one`  |     |       | account.account                  |
| `twilio_account_sid`                                 | Account SID                                                                                     | `char`      |     | ✅    |                                  |
| `twilio_account_token`                               | Account Auth Token                                                                              | `char`      |     | ✅    |                                  |
| `unsplash_access_key`                                | Access Key                                                                                      | `char`      |     | ✅    |                                  |
| `unsplash_app_id`                                    | Application ID                                                                                  | `char`      |     | ✅    |                                  |
| `use_event_barcode`                                  | Use Event Barcode                                                                               | `boolean`   |     | ✅    |                                  |
| `use_google_maps_static_api`                         | Google Maps static API                                                                          | `boolean`   |     | ✅    |                                  |
| `use_invoice_terms`                                  | Default Terms & Conditions                                                                      | `boolean`   |     | ✅    |                                  |
| `use_project`                                        | Use Projects                                                                                    | `boolean`   |     | ✅    |                                  |
| `use_security_lead`                                  | Security Lead Time for Sales                                                                    | `boolean`   |     | ✅    |                                  |
| `use_sfu_server`                                     | Use SFU server                                                                                  | `boolean`   |     | ✅    |                                  |
| `use_twilio_rtc_servers`                             | Use Twilio ICE servers                                                                          | `boolean`   |     | ✅    |                                  |
| `use_website_form`                                   | Website Form                                                                                    | `boolean`   |     | ✅    |                                  |
| `verify_date`                                        | Verify Date                                                                                     | `char`      |     |       |                                  |
| `web_app_name`                                       | Web App Name                                                                                    | `char`      |     | ✅    |                                  |
| `website_block_third_party_domains`                  | Block 3rd-party domains                                                                         | `boolean`   |     |       |                                  |
| `website_company_id`                                 | Website Company                                                                                 | `many2one`  |     |       | res.company                      |
| `website_cookies_bar`                                | Cookies Bar                                                                                     | `boolean`   |     |       |                                  |
| `website_default_lang_code`                          | Default language code                                                                           | `char`      |     |       |                                  |
| `website_default_lang_id`                            | Default language                                                                                | `many2one`  |     |       | res.lang                         |
| `website_domain`                                     | Website Domain                                                                                  | `char`      |     |       |                                  |
| `website_homepage_url`                               | Homepage Url                                                                                    | `char`      |     |       |                                  |
| `website_id`                                         | website                                                                                         | `many2one`  |     | ✅    | website                          |
| `website_language_count`                             | Number of languages                                                                             | `integer`   |     |       |                                  |
| `website_logo`                                       | Website Logo                                                                                    | `binary`    |     |       |                                  |
| `website_name`                                       | Website Name                                                                                    | `char`      |     |       |                                  |
| `website_sale_contact_us_button_url`                 | Button Url                                                                                      | `char`      |     |       |                                  |
| `website_sale_prevent_zero_price_sale`               | Prevent Sale of Zero Priced Product                                                             | `boolean`   |     |       |                                  |
| `website_warehouse_id`                               | Warehouse                                                                                       | `many2one`  |     |       | stock.warehouse                  |
| `whatsapp_business_id`                               | Business Account                                                                                | `many2one`  |     | ✅    | whatsapp.business                |
| `work_permit_expiration_notice_period`               | Work Permit Expiry Notice Period                                                                | `integer`   |     |       |                                  |
| `write_date`                                         | Last Updated on                                                                                 | `datetime`  |     | ✅    |                                  |
| `write_uid`                                          | Last Updated by                                                                                 | `many2one`  |     | ✅    | res.users                        |

**Access Rights:**

| Name                       | Group                | Perms   |
| -------------------------- | -------------------- | ------- |
| access.res.config.settings | Role / Administrator | `R/W/C` |

### 🗃️ `mail.followers` — Document Followers

mail_followers holds the data related to the follow mechanism inside Odoo. Partners can
choose to follow documents (records) of any kind that inherits from mail.thread.
Following documents allow to receive notifications for new messages. A subscription is
characterized by:

    :param: res_model: model of the followed objects
    :param: res_id: ID of resource (may be 0 for every objects)

**Fields:**

| Field          | Label                       | Type                 | Req | Store | Relation             |
| -------------- | --------------------------- | -------------------- | --- | ----- | -------------------- |
| `display_name` | Display Name                | `char`               |     |       |                      |
| `email`        | Email                       | `char`               |     |       |                      |
| `id`           | ID                          | `integer`            |     | ✅    |                      |
| `is_active`    | Is Active                   | `boolean`            |     |       |                      |
| `name`         | Name                        | `char`               |     |       |                      |
| `partner_id`   | Related Partner             | `many2one`           | ✅  | ✅    | res.partner          |
| `res_id`       | Related Document ID         | `many2one_reference` |     | ✅    |                      |
| `res_model`    | Related Document Model Name | `char`               | ✅  | ✅    |                      |
| `subtype_ids`  | Subtype                     | `many2many`          |     | ✅    | mail.message.subtype |

**Access Rights:**

| Name                  | Group                | Perms     |
| --------------------- | -------------------- | --------- |
| mail.followers.system | Role / Administrator | `R/W/C/D` |
| mail.followers.user   | Role / User          | `R`       |

### 🗃️ `mail.alias` — Email Aliases

A Mail Alias is a mapping of an email address with a given Odoo Document model. It is
used by Odoo's mail gateway when processing incoming emails sent to the system. If the
recipient address (To) of the message matches a Mail MailAlias, the message will be
either processed following the rules of that alias. If the message is a reply it will be
attached to the existing discussion on the corresponding record, otherwise a new record
of the corresponding model will be created.

       This is meant to be used in combination with a catch-all email configuration
       on the company's mail server, so that as soon as a new mail.alias is
       created, it becomes immediately usable and Odoo will accept email for it.


**Fields:**

| Field                    | Label                               | Type        | Req | Store | Relation          |
| ------------------------ | ----------------------------------- | ----------- | --- | ----- | ----------------- |
| `alias_bounced_content`  | Custom Bounced Message              | `html`      |     | ✅    |                   |
| `alias_contact`          | Alias Contact Security              | `selection` | ✅  | ✅    |                   |
| `alias_defaults`         | Default Values                      | `text`      | ✅  | ✅    |                   |
| `alias_domain`           | Alias domain name                   | `char`      |     |       |                   |
| `alias_domain_id`        | Alias Domain                        | `many2one`  |     | ✅    | mail.alias.domain |
| `alias_force_thread_id`  | Record Thread ID                    | `integer`   |     | ✅    |                   |
| `alias_full_name`        | Alias Email                         | `char`      |     | ✅    |                   |
| `alias_incoming_local`   | Local-part based incoming detection | `boolean`   |     | ✅    |                   |
| `alias_model_id`         | Aliased Model                       | `many2one`  | ✅  | ✅    | ir.model          |
| `alias_name`             | Alias Name                          | `char`      |     | ✅    |                   |
| `alias_parent_model_id`  | Parent Model                        | `many2one`  |     | ✅    | ir.model          |
| `alias_parent_thread_id` | Parent Record Thread ID             | `integer`   |     | ✅    |                   |
| `alias_status`           | Alias Status                        | `selection` |     | ✅    |                   |
| `create_date`            | Created on                          | `datetime`  |     | ✅    |                   |
| `create_uid`             | Created by                          | `many2one`  |     | ✅    | res.users         |
| `display_name`           | Display Name                        | `char`      |     |       |                   |
| `id`                     | ID                                  | `integer`   |     | ✅    |                   |
| `write_date`             | Last Updated on                     | `datetime`  |     | ✅    |                   |
| `write_uid`              | Last Updated by                     | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name              | Group                | Perms     |
| ----------------- | -------------------- | --------- |
| mail.alias.system | Role / Administrator | `R/W/C/D` |
| mail.alias.user   | Role / User          | `R`       |

### 🗃️ `mail.alias.mixin` — Email Aliases Mixin

A mixin for models that inherits mail.alias to have a one-to-one relation between the
model and its alias.

**Fields:**

| Field             | Label             | Type       | Req | Store | Relation          |
| ----------------- | ----------------- | ---------- | --- | ----- | ----------------- |
| `alias_defaults`  | Default Values    | `text`     | ✅  |       |                   |
| `alias_domain`    | Alias Domain Name | `char`     |     |       |                   |
| `alias_domain_id` | Alias Domain      | `many2one` |     |       | mail.alias.domain |
| `alias_email`     | Email Alias       | `char`     |     |       |                   |
| `alias_id`        | Alias             | `many2one` | ✅  | ✅    | mail.alias        |
| `alias_name`      | Alias Name        | `char`     |     |       |                   |
| `display_name`    | Display Name      | `char`     |     |       |                   |
| `id`              | ID                | `integer`  |     | ✅    |                   |

### 🗃️ `mail.alias.mixin.optional` — Email Aliases Mixin (light)

A mixin for models that handles underlying 'mail.alias' records to use the mail gateway.
Field is not mandatory and its creation is done dynamically based on given 'alias_name',
allowing to gradually populate the alias table without having void aliases as when used
with an inherits-like implementation.

**Fields:**

| Field             | Label             | Type       | Req | Store | Relation          |
| ----------------- | ----------------- | ---------- | --- | ----- | ----------------- |
| `alias_defaults`  | Default Values    | `text`     |     |       |                   |
| `alias_domain`    | Alias Domain Name | `char`     |     |       |                   |
| `alias_domain_id` | Alias Domain      | `many2one` |     |       | mail.alias.domain |
| `alias_email`     | Email Alias       | `char`     |     |       |                   |
| `alias_id`        | Alias             | `many2one` |     | ✅    | mail.alias        |
| `alias_name`      | Alias Name        | `char`     |     |       |                   |
| `display_name`    | Display Name      | `char`     |     |       |                   |
| `id`              | ID                | `integer`  |     | ✅    |                   |

### 🗃️ `mail.compose.message` — Email composition wizard

> ✳️ Transient (Wizard)

Generic message composition wizard. You may inherit from this wizard at model and view
levels to provide specific features.

        The behavior of the wizard depends on the composition_mode field:
        - 'comment': post on a record.
        - 'mass_mail': wizard in mass mailing mode where the mail details can
            contain template placeholders that will be merged with actual data
            before being sent to each recipient.

**Fields:**

| Field                         | Label                                            | Type        | Req | Store | Relation             |
| ----------------------------- | ------------------------------------------------ | ----------- | --- | ----- | -------------------- |
| `attachment_ids`              | Attachments                                      | `many2many` |     | ✅    | ir.attachment        |
| `author_id`                   | Author                                           | `many2one`  |     | ✅    | res.partner          |
| `auto_delete`                 | Delete Emails                                    | `boolean`   |     | ✅    |                      |
| `auto_delete_keep_log`        | Keep Message Copy                                | `boolean`   |     | ✅    |                      |
| `body`                        | Contents                                         | `html`      |     | ✅    |                      |
| `body_has_template_value`     | Body content is the same as the template         | `boolean`   |     |       |                      |
| `campaign_id`                 | Mass Mailing Campaign                            | `many2one`  |     | ✅    | utm.campaign         |
| `can_edit_body`               | Can Edit Body                                    | `boolean`   |     |       |                      |
| `composition_batch`           | Batch composition                                | `boolean`   |     |       |                      |
| `composition_comment_option`  | Comment Options                                  | `selection` |     | ✅    |                      |
| `composition_mode`            | Composition mode                                 | `selection` |     | ✅    |                      |
| `create_date`                 | Created on                                       | `datetime`  |     | ✅    |                      |
| `create_uid`                  | Created by                                       | `many2one`  |     | ✅    | res.users            |
| `display_name`                | Display Name                                     | `char`      |     |       |                      |
| `email_add_signature`         | Add signature                                    | `boolean`   |     | ✅    |                      |
| `email_from`                  | From                                             | `char`      |     | ✅    |                      |
| `email_layout_xmlid`          | Email Notification Layout                        | `char`      |     | ✅    |                      |
| `force_send`                  | Send mailing or notifications directly           | `boolean`   |     | ✅    |                      |
| `id`                          | ID                                               | `integer`   |     | ✅    |                      |
| `is_mail_template_editor`     | Is Editor                                        | `boolean`   |     |       |                      |
| `lang`                        | Language                                         | `char`      |     | ✅    |                      |
| `mail_activity_type_id`       | Mail Activity Type                               | `many2one`  |     | ✅    | mail.activity.type   |
| `mailing_list_ids`            | Mailing List                                     | `many2many` |     | ✅    | mailing.list         |
| `mail_server_id`              | Outgoing mail server                             | `many2one`  |     | ✅    | ir.mail_server       |
| `marketing_activity_id`       | Marketing Activity                               | `many2one`  |     | ✅    | marketing.activity   |
| `mass_mailing_id`             | Mass Mailing                                     | `many2one`  |     | ✅    | mailing.mailing      |
| `mass_mailing_name`           | Mass Mailing Name                                | `char`      |     | ✅    |                      |
| `message_type`                | Type                                             | `selection` | ✅  | ✅    |                      |
| `model`                       | Related Document Model                           | `char`      |     | ✅    |                      |
| `model_is_thread`             | Thread-Enabled                                   | `boolean`   |     |       |                      |
| `notified_bcc_contains_share` | Is an external partner follower of the document? | `boolean`   |     |       |                      |
| `notify_author`               | Notify Author                                    | `boolean`   |     | ✅    |                      |
| `notify_author_mention`       | Notify Author Mention                            | `boolean`   |     | ✅    |                      |
| `notify_skip_followers`       | Notify Skip Followers                            | `boolean`   |     | ✅    |                      |
| `parent_id`                   | Parent Message                                   | `many2one`  |     | ✅    | mail.message         |
| `partner_ids`                 | Additional Contacts                              | `many2many` |     | ✅    | res.partner          |
| `partner_ids_all_have_email`  | Partner Ids All Have Email                       | `boolean`   |     |       |                      |
| `record_alias_domain_id`      | Alias Domain                                     | `many2one`  |     | ✅    | mail.alias.domain    |
| `record_company_id`           | Company                                          | `many2one`  |     | ✅    | res.company          |
| `render_model`                | Rendering Model                                  | `char`      |     |       |                      |
| `reply_to`                    | Reply To                                         | `char`      |     | ✅    |                      |
| `reply_to_force_new`          | Considers answers as new thread                  | `boolean`   |     | ✅    |                      |
| `reply_to_mode`               | Replies                                          | `selection` |     |       |                      |
| `res_domain`                  | Active domain                                    | `text`      |     | ✅    |                      |
| `res_domain_user_id`          | Responsible                                      | `many2one`  |     | ✅    | res.users            |
| `res_ids`                     | Related Document IDs                             | `text`      |     | ✅    |                      |
| `scheduled_date`              | Scheduled Date                                   | `char`      |     | ✅    |                      |
| `subject`                     | Subject                                          | `char`      |     | ✅    |                      |
| `subtype_id`                  | Subtype                                          | `many2one`  |     | ✅    | mail.message.subtype |
| `subtype_is_log`              | Is a log                                         | `boolean`   |     |       |                      |
| `template_id`                 | Use template                                     | `many2one`  |     | ✅    | mail.template        |
| `template_name`               | Template Name                                    | `char`      |     | ✅    |                      |
| `use_exclusion_list`          | Use Exclusion List                               | `boolean`   |     | ✅    |                      |
| `write_date`                  | Last Updated on                                  | `datetime`  |     | ✅    |                      |
| `write_uid`                   | Last Updated by                                  | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                        | Group       | Perms   |
| --------------------------- | ----------- | ------- |
| access.mail.compose.message | Role / User | `R/W/C` |

**Record Rules:**

- **Mail Compose Message Rule** (Global) `R/W`
  - Domain: `[('create_uid', '=', user.id)]`

### 🗃️ `mail.alias.domain` — Email Domain

Model alias domains, now company-specific. Alias domains are email domains used to
receive emails through catchall and bounce aliases, as well as using mail.alias records
to redirect email replies.

    This replaces ``mail.alias.domain`` configuration parameter use until v16.

**Fields:**

| Field                | Label              | Type       | Req | Store | Relation    |
| -------------------- | ------------------ | ---------- | --- | ----- | ----------- |
| `bounce_alias`       | Bounce Alias       | `char`     | ✅  | ✅    |             |
| `bounce_email`       | Bounce Email       | `char`     |     |       |             |
| `catchall_alias`     | Catchall Alias     | `char`     | ✅  | ✅    |             |
| `catchall_email`     | Catchall Email     | `char`     |     |       |             |
| `company_ids`        | Companies          | `one2many` |     | ✅    | res.company |
| `create_date`        | Created on         | `datetime` |     | ✅    |             |
| `create_uid`         | Created by         | `many2one` |     | ✅    | res.users   |
| `default_from`       | Default From Alias | `char`     |     | ✅    |             |
| `default_from_email` | Default From       | `char`     |     |       |             |
| `display_name`       | Display Name       | `char`     |     |       |             |
| `id`                 | ID                 | `integer`  |     | ✅    |             |
| `name`               | Name               | `char`     | ✅  | ✅    |             |
| `sequence`           | Sequence           | `integer`  |     | ✅    |             |
| `write_date`         | Last Updated on    | `datetime` |     | ✅    |             |
| `write_uid`          | Last Updated by    | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                     | Group         | Perms     |
| ------------------------ | ------------- | --------- |
| mail.alias.domain.system | Access Rights | `R/W/C/D` |
| mail.alias.domain.user   | Role / User   | `R`       |

### 🗃️ `mail.template.preview` — Email Template Preview

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                             | Label                           | Type        | Req | Store | Relation      |
| --------------------------------- | ------------------------------- | ----------- | --- | ----- | ------------- |
| `attachment_ids`                  | Attachments                     | `many2many` |     |       | ir.attachment |
| `body_html`                       | Body                            | `html`      |     |       |               |
| `create_date`                     | Created on                      | `datetime`  |     | ✅    |               |
| `create_uid`                      | Created by                      | `many2one`  |     | ✅    | res.users     |
| `display_name`                    | Display Name                    | `char`      |     |       |               |
| `email_cc`                        | Cc                              | `char`      |     |       |               |
| `email_from`                      | From                            | `char`      |     |       |               |
| `email_to`                        | To                              | `char`      |     |       |               |
| `error_msg`                       | Error Message                   | `char`      |     |       |               |
| `has_attachments`                 | Has Attachments                 | `boolean`   |     |       |               |
| `has_several_languages_installed` | Has Several Languages Installed | `boolean`   |     |       |               |
| `id`                              | ID                              | `integer`   |     | ✅    |               |
| `lang`                            | Template Preview Language       | `selection` |     | ✅    |               |
| `mail_template_id`                | Related Mail Template           | `many2one`  | ✅  | ✅    | mail.template |
| `model_id`                        | Targeted model                  | `many2one`  |     |       | ir.model      |
| `no_record`                       | No Record                       | `boolean`   |     |       |               |
| `partner_ids`                     | Recipients                      | `many2many` |     |       | res.partner   |
| `reply_to`                        | Reply-To                        | `char`      |     |       |               |
| `resource_ref`                    | Record                          | `reference` |     | ✅    |               |
| `scheduled_date`                  | Scheduled Date                  | `char`      |     |       |               |
| `subject`                         | Subject                         | `char`      |     |       |               |
| `write_date`                      | Last Updated on                 | `datetime`  |     | ✅    |               |
| `write_uid`                       | Last Updated by                 | `many2one`  |     | ✅    | res.users     |

**Access Rights:**

| Name                         | Group       | Perms   |
| ---------------------------- | ----------- | ------- |
| access.mail.template.preview | Role / User | `R/W/C` |

### 🗃️ `mail.template` — Email Templates

Templates for sending email

**Fields:**

| Field                 | Label                     | Type        | Req | Store | Relation              |
| --------------------- | ------------------------- | ----------- | --- | ----- | --------------------- |
| `active`              | Active                    | `boolean`   |     | ✅    |                       |
| `attachment_ids`      | Attachments               | `many2many` |     | ✅    | ir.attachment         |
| `auto_delete`         | Auto Delete               | `boolean`   |     | ✅    |                       |
| `body_html`           | Body                      | `html`      |     | ✅    |                       |
| `can_write`           | Can Write                 | `boolean`   |     |       |                       |
| `create_date`         | Created on                | `datetime`  |     | ✅    |                       |
| `create_uid`          | Created by                | `many2one`  |     | ✅    | res.users             |
| `description`         | Template Description      | `text`      |     | ✅    |                       |
| `display_name`        | Display Name              | `char`      |     |       |                       |
| `email_cc`            | Cc                        | `char`      |     | ✅    |                       |
| `email_from`          | Send From                 | `char`      |     | ✅    |                       |
| `email_layout_xmlid`  | Email Notification Layout | `char`      |     | ✅    |                       |
| `email_to`            | To (Emails)               | `char`      |     | ✅    |                       |
| `has_dynamic_reports` | Has Dynamic Reports       | `boolean`   |     |       |                       |
| `has_mail_server`     | Has Mail Server           | `boolean`   |     |       |                       |
| `id`                  | ID                        | `integer`   |     | ✅    |                       |
| `is_template_editor`  | Is Template Editor        | `boolean`   |     |       |                       |
| `lang`                | Language                  | `char`      |     | ✅    |                       |
| `mail_server_id`      | Outgoing Mail Server      | `many2one`  |     | ✅    | ir.mail_server        |
| `model`               | Related Document Model    | `char`      |     | ✅    |                       |
| `model_id`            | Applies to                | `many2one`  |     | ✅    | ir.model              |
| `name`                | Name                      | `char`      |     | ✅    |                       |
| `partner_to`          | To (Partners)             | `char`      |     | ✅    |                       |
| `ref_ir_act_window`   | Sidebar action            | `many2one`  |     | ✅    | ir.actions.act_window |
| `render_model`        | Rendering Model           | `char`      |     |       |                       |
| `reply_to`            | Reply To                  | `char`      |     | ✅    |                       |
| `report_template_ids` | Dynamic Reports           | `many2many` |     | ✅    | ir.actions.report     |
| `scheduled_date`      | Scheduled Date            | `char`      |     | ✅    |                       |
| `subject`             | Subject                   | `char`      |     | ✅    |                       |
| `template_category`   | Template Category         | `selection` |     |       |                       |
| `template_fs`         | Template Filename         | `char`      |     | ✅    |                       |
| `use_default_to`      | Default Recipients        | `boolean`   |     | ✅    |                       |
| `user_id`             | Owner                     | `many2one`  |     | ✅    | res.users             |
| `write_date`          | Last Updated on           | `datetime`  |     | ✅    |                       |
| `write_uid`           | Last Updated by           | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                        | Group                | Perms     |
| --------------------------- | -------------------- | --------- |
| mail.template_editor        | Mail Template Editor | `R/W/C/D` |
| mail.template_system        | Role / Administrator | `R/W/C/D` |
| access_mail_template_portal | Role / Portal        | `R/W/C/D` |
| access_mail_template_public | Role / Public        | `R/W/C/D` |
| mail.template               | Role / User          | `R/W/C/D` |

**Record Rules:**

- **Employees can only modify templates they have created or been assigned** (1) `W/C/D`
  - Domain: `['|', ('create_uid', '=', user.id), ('user_id', '=', user.id)]`
- **Mail Template Editors - Edit All Templates** (17, 4) `W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `ir.model.fields` — Fields

fields configuration for form builder

**Fields:**

| Field                      | Label                          | Type        | Req | Store | Relation                  |
| -------------------------- | ------------------------------ | ----------- | --- | ----- | ------------------------- |
| `column1`                  | Column 1                       | `char`      |     | ✅    |                           |
| `column2`                  | Column 2                       | `char`      |     | ✅    |                           |
| `company_dependent`        | Company Dependent              | `boolean`   |     | ✅    |                           |
| `compute`                  | Compute                        | `text`      |     | ✅    |                           |
| `copied`                   | Copied                         | `boolean`   |     | ✅    |                           |
| `create_date`              | Created on                     | `datetime`  |     | ✅    |                           |
| `create_uid`               | Created by                     | `many2one`  |     | ✅    | res.users                 |
| `currency_field`           | Currency field                 | `char`      |     | ✅    |                           |
| `depends`                  | Dependencies                   | `char`      |     | ✅    |                           |
| `display_name`             | Display Name                   | `char`      |     |       |                           |
| `domain`                   | Domain                         | `char`      |     | ✅    |                           |
| `field_description`        | Field Label                    | `char`      | ✅  | ✅    |                           |
| `group_expand`             | Expand Groups                  | `boolean`   |     | ✅    |                           |
| `groups`                   | Groups                         | `many2many` |     | ✅    | res.groups                |
| `help`                     | Field Help                     | `text`      |     | ✅    |                           |
| `id`                       | ID                             | `integer`   |     | ✅    |                           |
| `index`                    | Indexed                        | `boolean`   |     | ✅    |                           |
| `model`                    | Model Name                     | `char`      | ✅  | ✅    |                           |
| `model_id`                 | Model                          | `many2one`  | ✅  | ✅    | ir.model                  |
| `modules`                  | In Apps                        | `char`      |     |       |                           |
| `name`                     | Field Name                     | `char`      | ✅  | ✅    |                           |
| `on_delete`                | On Delete                      | `selection` |     | ✅    |                           |
| `readonly`                 | Readonly                       | `boolean`   |     | ✅    |                           |
| `related`                  | Related Field Definition       | `char`      |     | ✅    |                           |
| `related_field_id`         | Related Field                  | `many2one`  |     | ✅    | ir.model.fields           |
| `relation`                 | Related Model                  | `char`      |     | ✅    |                           |
| `relation_field`           | Relation Field                 | `char`      |     | ✅    |                           |
| `relation_field_id`        | Relation field                 | `many2one`  |     | ✅    | ir.model.fields           |
| `relation_table`           | Relation Table                 | `char`      |     | ✅    |                           |
| `required`                 | Required                       | `boolean`   |     | ✅    |                           |
| `sanitize`                 | Sanitize HTML                  | `boolean`   |     | ✅    |                           |
| `sanitize_attributes`      | Sanitize HTML Attributes       | `boolean`   |     | ✅    |                           |
| `sanitize_form`            | Sanitize HTML Form             | `boolean`   |     | ✅    |                           |
| `sanitize_overridable`     | Sanitize HTML overridable      | `boolean`   |     | ✅    |                           |
| `sanitize_style`           | Sanitize HTML Style            | `boolean`   |     | ✅    |                           |
| `sanitize_tags`            | Sanitize HTML Tags             | `boolean`   |     | ✅    |                           |
| `secure`                   | Secure                         | `boolean`   |     | ✅    |                           |
| `selectable`               | Selectable                     | `boolean`   |     | ✅    |                           |
| `selection`                | Selection Options (Deprecated) | `char`      |     |       |                           |
| `selection_ids`            | Selection Options              | `one2many`  |     | ✅    | ir.model.fields.selection |
| `serialization_field_id`   | Serialization Field            | `many2one`  |     | ✅    | ir.model.fields           |
| `size`                     | Size                           | `integer`   |     | ✅    |                           |
| `state`                    | Type                           | `selection` | ✅  | ✅    |                           |
| `store`                    | Stored                         | `boolean`   |     | ✅    |                           |
| `strip_classes`            | Strip Class Attribute          | `boolean`   |     | ✅    |                           |
| `strip_style`              | Strip Style Attribute          | `boolean`   |     | ✅    |                           |
| `tracking`                 | Enable Ordered Tracking        | `integer`   |     | ✅    |                           |
| `translate`                | Translatable                   | `selection` |     | ✅    |                           |
| `ttype`                    | Field Type                     | `selection` | ✅  | ✅    |                           |
| `website_form_blacklisted` | Blacklisted in web forms       | `boolean`   |     | ✅    |                           |
| `write_date`               | Last Updated on                | `datetime`  |     | ✅    |                           |
| `write_uid`                | Last Updated by                | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name                              | Group         | Perms     |
| --------------------------------- | ------------- | --------- |
| ir_model_fields group_erp_manager | Access Rights | `R/W/C/D` |
| ir_model_fields all               | Role / User   | `-`       |

### 🗃️ `mail.followers.edit` — Followers edit wizard

> ✳️ Transient (Wizard)

Wizard to edit partners (or channels) to add/remove them to/from followers list.

**Fields:**

| Field          | Label                  | Type        | Req | Store | Relation    |
| -------------- | ---------------------- | ----------- | --- | ----- | ----------- |
| `create_date`  | Created on             | `datetime`  |     | ✅    |             |
| `create_uid`   | Created by             | `many2one`  |     | ✅    | res.users   |
| `display_name` | Display Name           | `char`      |     |       |             |
| `id`           | ID                     | `integer`   |     | ✅    |             |
| `message`      | Message                | `html`      |     | ✅    |             |
| `notify`       | Notify Recipients      | `boolean`   |     | ✅    |             |
| `operation`    | Operation              | `selection` | ✅  | ✅    |             |
| `partner_ids`  | Followers              | `many2many` | ✅  | ✅    | res.partner |
| `res_ids`      | Related Document IDs   | `char`      |     | ✅    |             |
| `res_model`    | Related Document Model | `char`      | ✅  | ✅    |             |
| `write_date`   | Last Updated on        | `datetime`  |     | ✅    |             |
| `write_uid`    | Last Updated by        | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                       | Group       | Perms   |
| -------------------------- | ----------- | ------- |
| access.mail.followers.edit | Role / User | `R/W/C` |

### 🗃️ `mail.guest` — Guest

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label           | Type        | Req | Store | Relation        |
| --------------- | --------------- | ----------- | --- | ----- | --------------- |
| `access_token`  | Access Token    | `char`      | ✅  | ✅    |                 |
| `avatar_1024`   | Avatar 1024     | `binary`    |     |       |                 |
| `avatar_128`    | Avatar 128      | `binary`    |     |       |                 |
| `avatar_1920`   | Avatar          | `binary`    |     |       |                 |
| `avatar_256`    | Avatar 256      | `binary`    |     |       |                 |
| `avatar_512`    | Avatar 512      | `binary`    |     |       |                 |
| `channel_ids`   | Channels        | `many2many` |     | ✅    | discuss.channel |
| `country_id`    | Country         | `many2one`  |     | ✅    | res.country     |
| `create_date`   | Created on      | `datetime`  |     | ✅    |                 |
| `create_uid`    | Created by      | `many2one`  |     | ✅    | res.users       |
| `display_name`  | Display Name    | `char`      |     |       |                 |
| `email`         | Email           | `char`      |     | ✅    |                 |
| `id`            | ID              | `integer`   |     | ✅    |                 |
| `image_1024`    | Image 1024      | `binary`    |     | ✅    |                 |
| `image_128`     | Image 128       | `binary`    |     | ✅    |                 |
| `image_1920`    | Image           | `binary`    |     | ✅    |                 |
| `image_256`     | Image 256       | `binary`    |     | ✅    |                 |
| `image_512`     | Image 512       | `binary`    |     | ✅    |                 |
| `im_status`     | IM Status       | `char`      |     |       |                 |
| `lang`          | Language        | `selection` |     | ✅    |                 |
| `name`          | Name            | `char`      | ✅  | ✅    |                 |
| `offline_since` | Offline since   | `datetime`  |     |       |                 |
| `presence_ids`  | Presence        | `one2many`  |     | ✅    | mail.presence   |
| `timezone`      | Timezone        | `selection` |     | ✅    |                 |
| `write_date`    | Last Updated on | `datetime`  |     | ✅    |                 |
| `write_uid`     | Last Updated by | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name       | Group                | Perms     |
| ---------- | -------------------- | --------- |
| mail.guest | Role / Administrator | `R/W/C/D` |
| mail.guest | Role / User          | `R`       |

### 🗃️ `ir.http` — HTTP Routing

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `mail.ice.server` — ICE Server

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation  |
| -------------- | --------------- | ----------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime`  |     | ✅    |           |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users |
| `credential`   | Credential      | `char`      |     | ✅    |           |
| `display_name` | Display Name    | `char`      |     |       |           |
| `id`           | ID              | `integer`   |     | ✅    |           |
| `server_type`  | Type            | `selection` | ✅  | ✅    |           |
| `uri`          | URI             | `char`      | ✅  | ✅    |           |
| `username`     | Username        | `char`      |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                   | Group                | Perms     |
| ---------------------- | -------------------- | --------- |
| mail.ice.server.system | Role / Administrator | `R/W/C/D` |

### 🗃️ `fetchmail.server` — Incoming Mail Server

Add the Outlook OAuth authentication on the incoming mail servers.

**Fields:**

| Field                                       | Label                                     | Type        | Req | Store | Relation  |
| ------------------------------------------- | ----------------------------------------- | ----------- | --- | ----- | --------- |
| `active`                                    | Active                                    | `boolean`   |     | ✅    |           |
| `attach`                                    | Keep Attachments                          | `boolean`   |     | ✅    |           |
| `configuration`                             | Configuration                             | `text`      |     | ✅    |           |
| `create_date`                               | Created on                                | `datetime`  |     | ✅    |           |
| `create_uid`                                | Created by                                | `many2one`  |     | ✅    | res.users |
| `date`                                      | Last Fetch Date                           | `datetime`  |     | ✅    |           |
| `display_name`                              | Display Name                              | `char`      |     |       |           |
| `error_date`                                | Last Error Date                           | `datetime`  |     | ✅    |           |
| `error_message`                             | Last Error Message                        | `text`      |     | ✅    |           |
| `google_gmail_access_token`                 | Access Token                              | `char`      |     | ✅    |           |
| `google_gmail_access_token_expiration`      | Access Token Expiration Timestamp         | `integer`   |     | ✅    |           |
| `google_gmail_refresh_token`                | Refresh Token                             | `char`      |     | ✅    |           |
| `google_gmail_uri`                          | URI                                       | `char`      |     |       |           |
| `id`                                        | ID                                        | `integer`   |     | ✅    |           |
| `is_ssl`                                    | SSL/TLS                                   | `boolean`   |     | ✅    |           |
| `message_ids`                               | Messages                                  | `one2many`  |     | ✅    | mail.mail |
| `microsoft_outlook_access_token`            | Outlook Access Token                      | `char`      |     | ✅    |           |
| `microsoft_outlook_access_token_expiration` | Outlook Access Token Expiration Timestamp | `integer`   |     | ✅    |           |
| `microsoft_outlook_refresh_token`           | Outlook Refresh Token                     | `char`      |     | ✅    |           |
| `microsoft_outlook_uri`                     | Authentication URI                        | `char`      |     |       |           |
| `name`                                      | Name                                      | `char`      | ✅  | ✅    |           |
| `object_id`                                 | Create a New Record                       | `many2one`  |     | ✅    | ir.model  |
| `original`                                  | Keep Original                             | `boolean`   |     | ✅    |           |
| `password`                                  | Password                                  | `char`      |     | ✅    |           |
| `port`                                      | Port                                      | `integer`   |     | ✅    |           |
| `priority`                                  | Server Priority                           | `integer`   |     | ✅    |           |
| `script`                                    | Script                                    | `char`      |     | ✅    |           |
| `server`                                    | Server Name                               | `char`      |     | ✅    |           |
| `server_type`                               | Server Type                               | `selection` | ✅  | ✅    |           |
| `server_type_info`                          | Server Type Info                          | `text`      |     |       |           |
| `state`                                     | Status                                    | `selection` |     | ✅    |           |
| `user`                                      | Username                                  | `char`      |     | ✅    |           |
| `write_date`                                | Last Updated on                           | `datetime`  |     | ✅    |           |
| `write_uid`                                 | Last Updated by                           | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name             | Group                | Perms     |
| ---------------- | -------------------- | --------- |
| fetchmail.server | Role / Administrator | `R/W/C/D` |

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

### 🗃️ `mail.message.link.preview` — Link between link previews and messages

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label           | Type       | Req | Store | Relation          |
| ----------------- | --------------- | ---------- | --- | ----- | ----------------- |
| `author_id`       | Author          | `many2one` |     |       | res.partner       |
| `create_date`     | Created on      | `datetime` |     | ✅    |                   |
| `create_uid`      | Created by      | `many2one` |     | ✅    | res.users         |
| `display_name`    | Display Name    | `char`     |     |       |                   |
| `id`              | ID              | `integer`  |     | ✅    |                   |
| `is_hidden`       | Is Hidden       | `boolean`  |     | ✅    |                   |
| `link_preview_id` | Link Preview    | `many2one` | ✅  | ✅    | mail.link.preview |
| `message_id`      | Message         | `many2one` | ✅  | ✅    | mail.message      |
| `sequence`        | Sequence        | `integer`  |     | ✅    |                   |
| `write_date`      | Last Updated on | `datetime` |     | ✅    |                   |
| `write_uid`       | Last Updated by | `many2one` |     | ✅    | res.users         |

**Access Rights:**

| Name                          | Group         | Perms     |
| ----------------------------- | ------------- | --------- |
| mail.link.preview.erp_manager | Access Rights | `R/W/C/D` |

### 🗃️ `mail.activity.schedule.line` — Mail Activity Schedule Line

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                  | Label             | Type       | Req | Store | Relation               |
| ---------------------- | ----------------- | ---------- | --- | ----- | ---------------------- |
| `activity_schedule_id` | Activity Schedule | `many2one` | ✅  | ✅    | mail.activity.schedule |
| `create_date`          | Created on        | `datetime` |     | ✅    |                        |
| `create_uid`           | Created by        | `many2one` |     | ✅    | res.users              |
| `display_name`         | Display Name      | `char`     |     |       |                        |
| `id`                   | ID                | `integer`  |     | ✅    |                        |
| `line_date_deadline`   | Date Deadline     | `date`     |     | ✅    |                        |
| `line_description`     | Line Description  | `char`     |     | ✅    |                        |
| `responsible_user_id`  | Responsible User  | `many2one` |     | ✅    | res.users              |
| `write_date`           | Last Updated on   | `datetime` |     | ✅    |                        |
| `write_uid`            | Last Updated by   | `many2one` |     | ✅    | res.users              |

**Access Rights:**

| Name                             | Group       | Perms   |
| -------------------------------- | ----------- | ------- |
| mail.activity.schedule.line.user | Role / User | `R/W/C` |

### 🗃️ `mail.composer.mixin` — Mail Composer Mixin

Mixin used to edit and render some fields used when sending emails or notifications
based on a mail template.

    Main current purpose is to hide details related to subject and body computation
    and rendering based on a mail.template. It also give the base tools to control
    who is allowed to edit body, notably when dealing with templating language
    like inline_template or qweb.

    It is meant to evolve in a near future with upcoming support of qweb and fine
    grain control of rendering access.

**Fields:**

| Field                     | Label                                    | Type       | Req | Store | Relation      |
| ------------------------- | ---------------------------------------- | ---------- | --- | ----- | ------------- |
| `body`                    | Contents                                 | `html`     |     | ✅    |               |
| `body_has_template_value` | Body content is the same as the template | `boolean`  |     |       |               |
| `can_edit_body`           | Can Edit Body                            | `boolean`  |     |       |               |
| `display_name`            | Display Name                             | `char`     |     |       |               |
| `id`                      | ID                                       | `integer`  |     | ✅    |               |
| `is_mail_template_editor` | Is Editor                                | `boolean`  |     |       |               |
| `lang`                    | Language                                 | `char`     |     | ✅    |               |
| `render_model`            | Rendering Model                          | `char`     |     |       |               |
| `subject`                 | Subject                                  | `char`     |     | ✅    |               |
| `template_id`             | Mail Template                            | `many2one` |     | ✅    | mail.template |

### 🗃️ `mail.gateway.allowed` — Mail Gateway Allowed

List of trusted email address which won't have the quota restriction.

    The incoming emails have a restriction of the number of records they can
    create with alias, defined by the 2 systems parameters;
    - mail.gateway.loop.minutes
    - mail.gateway.loop.threshold

    But we might have some legit use cases for which we want to receive a ton of emails
    from an automated-source. This model stores those trusted source and this restriction
    won't apply to them.

**Fields:**

| Field              | Label            | Type       | Req | Store | Relation  |
| ------------------ | ---------------- | ---------- | --- | ----- | --------- |
| `create_date`      | Created on       | `datetime` |     | ✅    |           |
| `create_uid`       | Created by       | `many2one` |     | ✅    | res.users |
| `display_name`     | Display Name     | `char`     |     |       |           |
| `email`            | Email Address    | `char`     | ✅  | ✅    |           |
| `email_normalized` | Normalized Email | `char`     |     | ✅    |           |
| `id`               | ID               | `integer`  |     | ✅    |           |
| `write_date`       | Last Updated on  | `datetime` |     | ✅    |           |
| `write_uid`        | Last Updated by  | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                        | Group                | Perms     |
| --------------------------- | -------------------- | --------- |
| mail.gateway.allowed.system | Role / Administrator | `R/W/C/D` |

### 🗃️ `mail.render.mixin` — Mail Render Mixin

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label           | Type      | Req | Store | Relation |
| -------------- | --------------- | --------- | --- | ----- | -------- |
| `display_name` | Display Name    | `char`    |     |       |          |
| `id`           | ID              | `integer` |     | ✅    |          |
| `lang`         | Language        | `char`    |     | ✅    |          |
| `render_model` | Rendering Model | `char`    |     |       |          |

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

### 🗃️ `ir.mail_server` — Mail Server

Add the Outlook OAuth authentication on the outgoing mail servers.

**Fields:**

| Field                                       | Label                                     | Type        | Req | Store | Relation        |
| ------------------------------------------- | ----------------------------------------- | ----------- | --- | ----- | --------------- |
| `active`                                    | Active                                    | `boolean`   |     | ✅    |                 |
| `active_mailing_ids`                        | Active mailing using this mail server     | `one2many`  |     | ✅    | mailing.mailing |
| `create_date`                               | Created on                                | `datetime`  |     | ✅    |                 |
| `create_uid`                                | Created by                                | `many2one`  |     | ✅    | res.users       |
| `display_name`                              | Display Name                              | `char`      |     |       |                 |
| `from_filter`                               | FROM Filtering                            | `char`      |     | ✅    |                 |
| `google_gmail_access_token`                 | Access Token                              | `char`      |     | ✅    |                 |
| `google_gmail_access_token_expiration`      | Access Token Expiration Timestamp         | `integer`   |     | ✅    |                 |
| `google_gmail_refresh_token`                | Refresh Token                             | `char`      |     | ✅    |                 |
| `google_gmail_uri`                          | URI                                       | `char`      |     |       |                 |
| `id`                                        | ID                                        | `integer`   |     | ✅    |                 |
| `mail_template_ids`                         | Mail template using this mail server      | `one2many`  |     | ✅    | mail.template   |
| `max_email_size`                            | Max Email Size                            | `float`     |     | ✅    |                 |
| `microsoft_outlook_access_token`            | Outlook Access Token                      | `char`      |     | ✅    |                 |
| `microsoft_outlook_access_token_expiration` | Outlook Access Token Expiration Timestamp | `integer`   |     | ✅    |                 |
| `microsoft_outlook_refresh_token`           | Outlook Refresh Token                     | `char`      |     | ✅    |                 |
| `microsoft_outlook_uri`                     | Authentication URI                        | `char`      |     |       |                 |
| `name`                                      | Name                                      | `char`      | ✅  | ✅    |                 |
| `owner_limit_count`                         | Owner Limit Count                         | `integer`   |     | ✅    |                 |
| `owner_limit_time`                          | Owner Limit Time                          | `datetime`  |     | ✅    |                 |
| `owner_user_id`                             | Owner                                     | `many2one`  |     | ✅    | res.users       |
| `sequence`                                  | Priority                                  | `integer`   |     | ✅    |                 |
| `smtp_authentication`                       | Authenticate with                         | `selection` | ✅  | ✅    |                 |
| `smtp_authentication_info`                  | Authentication Info                       | `text`      |     |       |                 |
| `smtp_debug`                                | Debugging                                 | `boolean`   |     | ✅    |                 |
| `smtp_encryption`                           | Connection Encryption                     | `selection` | ✅  | ✅    |                 |
| `smtp_host`                                 | SMTP Server                               | `char`      |     | ✅    |                 |
| `smtp_pass`                                 | Password                                  | `char`      |     | ✅    |                 |
| `smtp_port`                                 | SMTP Port                                 | `integer`   |     | ✅    |                 |
| `smtp_ssl_certificate`                      | SSL Certificate                           | `binary`    |     | ✅    |                 |
| `smtp_ssl_private_key`                      | SSL Private Key                           | `binary`    |     | ✅    |                 |
| `smtp_user`                                 | Username                                  | `char`      |     | ✅    |                 |
| `write_date`                                | Last Updated on                           | `datetime`  |     | ✅    |                 |
| `write_uid`                                 | Last Updated by                           | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                  | Group                  | Perms     |
| --------------------- | ---------------------- | --------- |
| access_ir_mail_server | Email Marketing / User | `R`       |
| ir_mail_server        | Role / Administrator   | `R/W/C/D` |

### 🗃️ `mail.template.reset` — Mail Template Reset

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation      |
| -------------- | --------------- | ----------- | --- | ----- | ------------- |
| `create_date`  | Created on      | `datetime`  |     | ✅    |               |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users     |
| `display_name` | Display Name    | `char`      |     |       |               |
| `id`           | ID              | `integer`   |     | ✅    |               |
| `template_ids` | Template        | `many2many` |     | ✅    | mail.template |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |               |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users     |

**Access Rights:**

| Name                       | Group                | Perms     |
| -------------------------- | -------------------- | --------- |
| access.mail.template.reset | Mail Template Editor | `R/W/C/D` |

### 🗃️ `mail.tracking.value` — Mail Tracking Value

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label                     | Type       | Req | Store | Relation        |
| -------------------- | ------------------------- | ---------- | --- | ----- | --------------- |
| `create_date`        | Created on                | `datetime` |     | ✅    |                 |
| `create_uid`         | Created by                | `many2one` |     | ✅    | res.users       |
| `currency_id`        | Currency                  | `many2one` |     | ✅    | res.currency    |
| `display_name`       | Display Name              | `char`     |     |       |                 |
| `field_id`           | Field                     | `many2one` |     | ✅    | ir.model.fields |
| `field_info`         | Removed field information | `json`     |     | ✅    |                 |
| `id`                 | ID                        | `integer`  |     | ✅    |                 |
| `mail_message_id`    | Message ID                | `many2one` | ✅  | ✅    | mail.message    |
| `new_value_char`     | New Value Char            | `char`     |     | ✅    |                 |
| `new_value_datetime` | New Value Datetime        | `datetime` |     | ✅    |                 |
| `new_value_float`    | New Value Float           | `float`    |     | ✅    |                 |
| `new_value_integer`  | New Value Integer         | `integer`  |     | ✅    |                 |
| `new_value_text`     | New Value Text            | `text`     |     | ✅    |                 |
| `old_value_char`     | Old Value Char            | `char`     |     | ✅    |                 |
| `old_value_datetime` | Old Value DateTime        | `datetime` |     | ✅    |                 |
| `old_value_float`    | Old Value Float           | `float`    |     | ✅    |                 |
| `old_value_integer`  | Old Value Integer         | `integer`  |     | ✅    |                 |
| `old_value_text`     | Old Value Text            | `text`     |     | ✅    |                 |
| `write_date`         | Last Updated on           | `datetime` |     | ✅    |                 |
| `write_uid`          | Last Updated by           | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                       | Group                | Perms     |
| -------------------------- | -------------------- | --------- |
| mail.tracking.value.system | Role / Administrator | `R/W/C/D` |

### 🗃️ `ir.ui.menu` — Menu

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label           | Type        | Req | Store | Relation   |
| --------------- | --------------- | ----------- | --- | ----- | ---------- |
| `action`        | Action          | `reference` |     | ✅    |            |
| `active`        | Active          | `boolean`   |     | ✅    |            |
| `child_id`      | Child IDs       | `one2many`  |     | ✅    | ir.ui.menu |
| `complete_name` | Full Path       | `char`      |     |       |            |
| `create_date`   | Created on      | `datetime`  |     | ✅    |            |
| `create_uid`    | Created by      | `many2one`  |     | ✅    | res.users  |
| `display_name`  | Display Name    | `char`      |     |       |            |
| `group_ids`     | Groups          | `many2many` |     | ✅    | res.groups |
| `id`            | ID              | `integer`   |     | ✅    |            |
| `name`          | Menu            | `char`      | ✅  | ✅    |            |
| `parent_id`     | Parent Menu     | `many2one`  |     | ✅    | ir.ui.menu |
| `parent_path`   | Parent Path     | `char`      |     | ✅    |            |
| `sequence`      | Sequence        | `integer`   |     | ✅    |            |
| `web_icon`      | Web Icon File   | `char`      |     | ✅    |            |
| `web_icon_data` | Web Icon Image  | `binary`    |     | ✅    |            |
| `write_date`    | Last Updated on | `datetime`  |     | ✅    |            |
| `write_uid`     | Last Updated by | `many2one`  |     | ✅    | res.users  |

**Access Rights:**

| Name                    | Group                | Perms     |
| ----------------------- | -------------------- | --------- |
| ir_ui_menu group_system | Role / Administrator | `R/W/C/D` |
| ir_ui_menu group_user   | Role / User          | `R`       |

### 🗃️ `base.partner.merge.automatic.wizard` — Merge Partner Wizard

> ✳️ Transient (Wizard)

        The idea behind this wizard is to create a list of potential partners to
        merge. We use two objects, the first one is the wizard for the end-user.
        And the second will contain the partner list to merge.

**Fields:**

| Field                  | Label                                   | Type        | Req | Store | Relation                |
| ---------------------- | --------------------------------------- | ----------- | --- | ----- | ----------------------- |
| `create_date`          | Created on                              | `datetime`  |     | ✅    |                         |
| `create_uid`           | Created by                              | `many2one`  |     | ✅    | res.users               |
| `current_line_id`      | Current Line                            | `many2one`  |     | ✅    | base.partner.merge.line |
| `display_name`         | Display Name                            | `char`      |     |       |                         |
| `dst_partner_id`       | Destination Contact                     | `many2one`  |     | ✅    | res.partner             |
| `exclude_contact`      | A user associated to the contact        | `boolean`   |     | ✅    |                         |
| `exclude_journal_item` | Journal Items associated to the contact | `boolean`   |     | ✅    |                         |
| `group_by_email`       | Email                                   | `boolean`   |     | ✅    |                         |
| `group_by_is_company`  | Is Company                              | `boolean`   |     | ✅    |                         |
| `group_by_name`        | Name                                    | `boolean`   |     | ✅    |                         |
| `group_by_parent_id`   | Parent Company                          | `boolean`   |     | ✅    |                         |
| `group_by_vat`         | VAT                                     | `boolean`   |     | ✅    |                         |
| `id`                   | ID                                      | `integer`   |     | ✅    |                         |
| `line_ids`             | Lines                                   | `one2many`  |     | ✅    | base.partner.merge.line |
| `maximum_group`        | Maximum of Group of Contacts            | `integer`   |     | ✅    |                         |
| `number_group`         | Group of Contacts                       | `integer`   |     | ✅    |                         |
| `partner_ids`          | Contacts                                | `many2many` |     | ✅    | res.partner             |
| `state`                | State                                   | `selection` | ✅  | ✅    |                         |
| `write_date`           | Last Updated on                         | `datetime`  |     | ✅    |                         |
| `write_uid`            | Last Updated by                         | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name                                       | Group              | Perms   |
| ------------------------------------------ | ------------------ | ------- |
| access.base.partner.merge.automatic.wizard | Contact / Creation | `R/W/C` |

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

### 🗃️ `mail.notification` — Message Notifications

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                 | Label              | Type        | Req | Store | Relation         |
| --------------------- | ------------------ | ----------- | --- | ----- | ---------------- |
| `author_id`           | Author             | `many2one`  |     | ✅    | res.partner      |
| `display_name`        | Display Name       | `char`      |     |       |                  |
| `failure_reason`      | Failure reason     | `text`      |     | ✅    |                  |
| `failure_type`        | Failure type       | `selection` |     | ✅    |                  |
| `id`                  | ID                 | `integer`   |     | ✅    |                  |
| `is_read`             | Is Read            | `boolean`   |     | ✅    |                  |
| `letter_id`           | Snailmail Letter   | `many2one`  |     | ✅    | snailmail.letter |
| `mail_email_address`  | Mail Email Address | `char`      |     | ✅    |                  |
| `mail_mail_id`        | Mail               | `many2one`  |     | ✅    | mail.mail        |
| `mail_message_id`     | Message            | `many2one`  | ✅  | ✅    | mail.message     |
| `notification_status` | Status             | `selection` |     | ✅    |                  |
| `notification_type`   | Notification Type  | `selection` | ✅  | ✅    |                  |
| `read_date`           | Read Date          | `datetime`  |     | ✅    |                  |
| `res_partner_id`      | Recipient          | `many2one`  |     | ✅    | res.partner      |
| `sms_id`              | SMS                | `many2one`  |     |       | sms.sms          |
| `sms_id_int`          | SMS ID             | `integer`   |     | ✅    |                  |
| `sms_number`          | SMS Number         | `char`      |     | ✅    |                  |
| `sms_tracker_ids`     | SMS Trackers       | `one2many`  |     | ✅    | sms.tracker      |

**Access Rights:**

| Name                     | Group                | Perms     |
| ------------------------ | -------------------- | --------- |
| mail.notification.system | Role / Administrator | `R/W/C/D` |
| mail.notification.portal | Role / Portal        | `R`       |
| mail.notification.user   | Role / User          | `R/W/C`   |

**Record Rules:**

- **mail.notifications: group_user: write its own entries** (10, 1) `W`
  - Domain: `[('res_partner_id', '=', user.partner_id.id)]`
- **mail.notifications: group_portal: own entries** (10) `R/W/C/D`
  - Domain:
    `['|', ('res_partner_id', '=', user.partner_id.id), ('author_id', '=', user.partner_id.id)]`

### 🗃️ `mail.message.reaction` — Message Reaction

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label            | Type       | Req | Store | Relation     |
| -------------- | ---------------- | ---------- | --- | ----- | ------------ |
| `content`      | Content          | `char`     | ✅  | ✅    |              |
| `display_name` | Display Name     | `char`     |     |       |              |
| `guest_id`     | Reacting Guest   | `many2one` |     | ✅    | mail.guest   |
| `id`           | ID               | `integer`  |     | ✅    |              |
| `message_id`   | Message          | `many2one` | ✅  | ✅    | mail.message |
| `partner_id`   | Reacting Partner | `many2one` |     | ✅    | res.partner  |

**Access Rights:**

| Name                         | Group                | Perms     |
| ---------------------------- | -------------------- | --------- |
| mail.message.reaction.system | Role / Administrator | `R/W/C/D` |

### 🗃️ `mail.message.subtype` — Message subtypes

Class holding subtype definition for messages. Subtypes allow to tune the follower
subscription, allowing only some subtypes to be pushed on the Wall.

**Fields:**

| Field              | Label            | Type       | Req | Store | Relation             |
| ------------------ | ---------------- | ---------- | --- | ----- | -------------------- |
| `create_date`      | Created on       | `datetime` |     | ✅    |                      |
| `create_uid`       | Created by       | `many2one` |     | ✅    | res.users            |
| `default`          | Default          | `boolean`  |     | ✅    |                      |
| `description`      | Description      | `text`     |     | ✅    |                      |
| `display_name`     | Display Name     | `char`     |     |       |                      |
| `hidden`           | Hidden           | `boolean`  |     | ✅    |                      |
| `id`               | ID               | `integer`  |     | ✅    |                      |
| `internal`         | Internal Only    | `boolean`  |     | ✅    |                      |
| `name`             | Message Type     | `char`     | ✅  | ✅    |                      |
| `parent_id`        | Parent           | `many2one` |     | ✅    | mail.message.subtype |
| `relation_field`   | Relation field   | `char`     |     | ✅    |                      |
| `res_model`        | Model            | `char`     |     | ✅    |                      |
| `sequence`         | Sequence         | `integer`  |     | ✅    |                      |
| `track_recipients` | Track Recipients | `boolean`  |     | ✅    |                      |
| `write_date`       | Last Updated on  | `datetime` |     | ✅    |                      |
| `write_uid`        | Last Updated by  | `many2one` |     | ✅    | res.users            |

**Access Rights:**

| Name                        | Group                | Perms     |
| --------------------------- | -------------------- | --------- |
| mail.message.subtype.system | Role / Administrator | `R/W/C/D` |
| mail.message.subtype.all    | Role / Portal        | `R`       |
| mail.message.subtype.all    | Role / Public        | `R`       |
| mail.message.subtype.user   | Role / User          | `R`       |

**Record Rules:**

- **mail.message.subtype: portal/public: read public subtypes** (10, 11) `R/W/C/D`
  - Domain: `[('internal', '=', False)]`

### 🗃️ `mail.message.translation` — Message Translation

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label            | Type       | Req | Store | Relation     |
| -------------- | ---------------- | ---------- | --- | ----- | ------------ |
| `body`         | Translation Body | `html`     | ✅  | ✅    |              |
| `create_date`  | Create Date      | `datetime` |     | ✅    |              |
| `create_uid`   | Created by       | `many2one` |     | ✅    | res.users    |
| `display_name` | Display Name     | `char`     |     |       |              |
| `id`           | ID               | `integer`  |     | ✅    |              |
| `message_id`   | Message          | `many2one` | ✅  | ✅    | mail.message |
| `source_lang`  | Source Language  | `char`     | ✅  | ✅    |              |
| `target_lang`  | Target Language  | `char`     | ✅  | ✅    |              |
| `write_date`   | Last Updated on  | `datetime` |     | ✅    |              |
| `write_uid`    | Last Updated by  | `many2one` |     | ✅    | res.users    |

**Access Rights:**

| Name                     | Group                | Perms     |
| ------------------------ | -------------------- | --------- |
| mail.message.translation | Role / Administrator | `R/W/C/D` |

### 🗃️ `discuss.voice.metadata` — Metadata for voice attachments

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label           | Type       | Req | Store | Relation      |
| --------------- | --------------- | ---------- | --- | ----- | ------------- |
| `attachment_id` | Attachment      | `many2one` |     | ✅    | ir.attachment |
| `create_date`   | Created on      | `datetime` |     | ✅    |               |
| `create_uid`    | Created by      | `many2one` |     | ✅    | res.users     |
| `display_name`  | Display Name    | `char`     |     |       |               |
| `id`            | ID              | `integer`  |     | ✅    |               |
| `write_date`    | Last Updated on | `datetime` |     | ✅    |               |
| `write_uid`     | Last Updated by | `many2one` |     | ✅    | res.users     |

**Access Rights:**

| Name                        | Group                | Perms     |
| --------------------------- | -------------------- | --------- |
| discuss.voice.metadata.user | Role / Administrator | `R/W/C/D` |

### 🗃️ `ir.model` — Models

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                      | Type        | Req | Store | Relation        |
| ------------------------------- | -------------------------- | ----------- | --- | ----- | --------------- |
| `abstract`                      | Abstract Model             | `boolean`   |     | ✅    |                 |
| `access_ids`                    | Access                     | `one2many`  |     | ✅    | ir.model.access |
| `count`                         | Count (Incl. Archived)     | `integer`   |     |       |                 |
| `create_date`                   | Created on                 | `datetime`  |     | ✅    |                 |
| `create_uid`                    | Created by                 | `many2one`  |     | ✅    | res.users       |
| `display_name`                  | Display Name               | `char`      |     |       |                 |
| `field_id`                      | Fields                     | `one2many`  | ✅  | ✅    | ir.model.fields |
| `fold_name`                     | Fold Field                 | `char`      |     | ✅    |                 |
| `id`                            | ID                         | `integer`   |     | ✅    |                 |
| `info`                          | Information                | `text`      |     | ✅    |                 |
| `inherited_model_ids`           | Inherited models           | `many2many` |     |       | ir.model        |
| `is_mail_activity`              | Has Mail Activity          | `boolean`   |     | ✅    |                 |
| `is_mail_blacklist`             | Has Mail Blacklist         | `boolean`   |     | ✅    |                 |
| `is_mailing_enabled`            | Mailing Enabled            | `boolean`   |     |       |                 |
| `is_mail_thread`                | Has Mail Thread            | `boolean`   |     | ✅    |                 |
| `is_mail_thread_sms`            | Mail Thread SMS            | `boolean`   |     |       |                 |
| `is_phone_whatsapp`             | Whatsapp Contact           | `boolean`   |     |       |                 |
| `model`                         | Model                      | `char`      | ✅  | ✅    |                 |
| `modules`                       | In Apps                    | `char`      |     |       |                 |
| `name`                          | Model Description          | `char`      | ✅  | ✅    |                 |
| `order`                         | Order                      | `char`      | ✅  | ✅    |                 |
| `rule_ids`                      | Record Rules               | `one2many`  |     | ✅    | ir.rule         |
| `state`                         | Type                       | `selection` |     | ✅    |                 |
| `transient`                     | Transient Model            | `boolean`   |     | ✅    |                 |
| `view_ids`                      | Views                      | `one2many`  |     |       | ir.ui.view      |
| `website_form_access`           | Allowed to use in forms    | `boolean`   |     | ✅    |                 |
| `website_form_default_field_id` | Field for custom form data | `many2one`  |     | ✅    | ir.model.fields |
| `website_form_key`              | Website Form Key           | `char`      |     | ✅    |                 |
| `website_form_label`            | Label for form action      | `char`      |     | ✅    |                 |
| `write_date`                    | Last Updated on            | `datetime`  |     | ✅    |                 |
| `write_uid`                     | Last Updated by            | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                       | Group                  | Perms     |
| -------------------------- | ---------------------- | --------- |
| access_ir_model            | Email Marketing / User | `R`       |
| ir_model group_erp_manager | Access Rights          | `R/W/C/D` |
| ir_model_all               | Role / User            | `-`       |

### 🗃️ `base.module.uninstall` — Module Uninstall

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                 | Label                | Type        | Req | Store | Relation         |
| --------------------- | -------------------- | ----------- | --- | ----- | ---------------- |
| `create_date`         | Created on           | `datetime`  |     | ✅    |                  |
| `create_uid`          | Created by           | `many2one`  |     | ✅    | res.users        |
| `display_name`        | Display Name         | `char`      |     |       |                  |
| `id`                  | ID                   | `integer`   |     | ✅    |                  |
| `impacted_module_ids` | Impacted modules     | `many2many` |     |       | ir.module.module |
| `model_ids`           | Impacted data models | `many2many` |     |       | ir.model         |
| `module_ids`          | Module(s)            | `many2many` | ✅  | ✅    | ir.module.module |
| `show_all`            | Show All             | `boolean`   |     | ✅    |                  |
| `write_date`          | Last Updated on      | `datetime`  |     | ✅    |                  |
| `write_uid`           | Last Updated by      | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                         | Group                | Perms   |
| ---------------------------- | -------------------- | ------- |
| access.base.module.uninstall | Role / Administrator | `R/W/C` |

### 🗃️ `mail.mail` — Outgoing Mails

Add the mass mailing campaign data to mail

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
| `attachment_ids`                  | Attachments                        | `many2many`          |     |       | ir.attachment             |
| `author_avatar`                   | Author's avatar                    | `binary`             |     |       |                           |
| `author_guest_id`                 | Guest                              | `many2one`           |     |       | mail.guest                |
| `author_id`                       | Author                             | `many2one`           |     |       | res.partner               |
| `auto_delete`                     | Auto Delete                        | `boolean`            |     | ✅    |                           |
| `body`                            | Contents                           | `html`               |     |       |                           |
| `body_content`                    | Rich-text Contents                 | `html`               |     |       |                           |
| `body_html`                       | Text Contents                      | `text`               |     | ✅    |                           |
| `call_history_ids`                | Call History                       | `one2many`           |     |       | discuss.call.history      |
| `channel_id`                      | Channel                            | `many2one`           |     |       | discuss.channel           |
| `child_ids`                       | Child Messages                     | `one2many`           |     |       | mail.message              |
| `create_date`                     | Created on                         | `datetime`           |     | ✅    |                           |
| `create_uid`                      | Created by                         | `many2one`           |     | ✅    | res.users                 |
| `date`                            | Date                               | `datetime`           |     |       |                           |
| `display_name`                    | Display Name                       | `char`               |     |       |                           |
| `email_add_signature`             | Email Add Signature                | `boolean`            |     |       |                           |
| `email_cc`                        | Cc                                 | `char`               |     | ✅    |                           |
| `email_from`                      | From                               | `char`               |     |       |                           |
| `email_layout_xmlid`              | Layout                             | `char`               |     |       |                           |
| `email_to`                        | To                                 | `text`               |     | ✅    |                           |
| `failure_reason`                  | Failure Reason                     | `text`               |     | ✅    |                           |
| `failure_type`                    | Failure type                       | `selection`          |     | ✅    |                           |
| `fetchmail_server_id`             | Inbound Mail Server                | `many2one`           |     | ✅    | fetchmail.server          |
| `has_error`                       | Has error                          | `boolean`            |     |       |                           |
| `has_sms_error`                   | Has SMS error                      | `boolean`            |     |       |                           |
| `headers`                         | Headers                            | `text`               |     | ✅    |                           |
| `id`                              | ID                                 | `integer`            |     | ✅    |                           |
| `incoming_email_cc`               | Emails Cc                          | `char`               |     |       |                           |
| `incoming_email_to`               | Emails To                          | `text`               |     |       |                           |
| `is_current_user_or_guest_author` | Is Current User Or Guest Author    | `boolean`            |     |       |                           |
| `is_internal`                     | Employee Only                      | `boolean`            |     |       |                           |
| `is_notification`                 | Notification Email                 | `boolean`            |     | ✅    |                           |
| `letter_ids`                      | Letter                             | `one2many`           |     |       | snailmail.letter          |
| `linked_message_ids`              | Linked Message                     | `many2many`          |     |       | mail.message              |
| `mail_activity_type_id`           | Mail Activity Type                 | `many2one`           |     |       | mail.activity.type        |
| `mail_ids`                        | Mails                              | `one2many`           |     |       | mail.mail                 |
| `mailing_id`                      | Mass Mailing                       | `many2one`           |     | ✅    | mailing.mailing           |
| `mailing_trace_ids`               | Statistics                         | `one2many`           |     | ✅    | mailing.trace             |
| `mail_message_id`                 | Message                            | `many2one`           | ✅  | ✅    | mail.message              |
| `mail_message_id_int`             | Mail Message Id Int                | `integer`            |     |       |                           |
| `mail_server_id`                  | Outgoing mail server               | `many2one`           |     |       | ir.mail_server            |
| `message_id`                      | Message-Id                         | `char`               |     |       |                           |
| `message_link_preview_ids`        | Message Link Preview               | `one2many`           |     |       | mail.message.link.preview |
| `message_type`                    | Type                               | `selection`          | ✅  |       |                           |
| `model`                           | Related Document Model             | `char`               |     |       |                           |
| `needaction`                      | Need Action                        | `boolean`            |     |       |                           |
| `notification_ids`                | Notifications                      | `one2many`           |     |       | mail.notification         |
| `notified_partner_ids`            | Partners with Need Action          | `many2many`          |     |       | res.partner               |
| `outgoing_email_to`               | emails To                          | `char`               |     |       |                           |
| `parent_id`                       | Parent Message                     | `many2one`           |     |       | mail.message              |
| `partner_ids`                     | Recipients                         | `many2many`          |     |       | res.partner               |
| `pinned_at`                       | Pinned                             | `datetime`           |     |       |                           |
| `preview`                         | Preview                            | `char`               |     |       |                           |
| `rating_id`                       | Rating                             | `many2one`           |     |       | rating.rating             |
| `rating_ids`                      | Related ratings                    | `one2many`           |     |       | rating.rating             |
| `rating_value`                    | Rating Value                       | `float`              |     |       |                           |
| `reaction_ids`                    | Reactions                          | `one2many`           |     |       | mail.message.reaction     |
| `recipient_ids`                   | To (Partners)                      | `many2many`          |     | ✅    | res.partner               |
| `record_alias_domain_id`          | Alias Domain                       | `many2one`           |     |       | mail.alias.domain         |
| `record_company_id`               | Company                            | `many2one`           |     |       | res.company               |
| `record_name`                     | Message Record Name                | `char`               |     |       |                           |
| `references`                      | References                         | `text`               |     | ✅    |                           |
| `reply_to`                        | Reply-To                           | `char`               |     |       |                           |
| `reply_to_force_new`              | No threading for answers           | `boolean`            |     |       |                           |
| `res_id`                          | Related Document ID                | `many2one_reference` |     |       |                           |
| `restricted_attachment_count`     | Restricted attachments             | `integer`            |     |       |                           |
| `scheduled_date`                  | Scheduled Send Date                | `datetime`           |     | ✅    |                           |
| `snailmail_error`                 | Snailmail message in error         | `boolean`            |     |       |                           |
| `starred`                         | Starred                            | `boolean`            |     |       |                           |
| `starred_partner_ids`             | Favorited By                       | `many2many`          |     |       | res.partner               |
| `state`                           | Status                             | `selection`          |     | ✅    |                           |
| `subject`                         | Subject                            | `char`               |     |       |                           |
| `subtype_id`                      | Subtype                            | `many2one`           |     |       | mail.message.subtype      |
| `tracking_value_ids`              | Tracking values                    | `one2many`           |     |       | mail.tracking.value       |
| `unrestricted_attachment_ids`     | Unrestricted Attachments           | `many2many`          |     |       | ir.attachment             |
| `write_date`                      | Last Updated on                    | `datetime`           |     | ✅    |                           |
| `write_uid`                       | Last Updated by                    | `many2one`           |     | ✅    | res.users                 |

**Access Rights:**

| Name                  | Group                | Perms     |
| --------------------- | -------------------- | --------- |
| mail.mail.system      | Role / Administrator | `R/W/C/D` |
| access_mail_mail_user | Role / User          | `R/W/C/D` |

### 🗃️ `publisher_warranty.contract` — Publisher Warranty Contract

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

**Access Rights:**

| Name                            | Group                | Perms     |
| ------------------------------- | -------------------- | --------- |
| publisher.warranty.contract.all | Role / Administrator | `R/W/C/D` |

### 🗃️ `mail.push.device` — Push Notification Device

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label                 | Type       | Req | Store | Relation    |
| ----------------- | --------------------- | ---------- | --- | ----- | ----------- |
| `create_date`     | Created on            | `datetime` |     | ✅    |             |
| `create_uid`      | Created by            | `many2one` |     | ✅    | res.users   |
| `display_name`    | Display Name          | `char`     |     |       |             |
| `endpoint`        | Browser endpoint      | `char`     | ✅  | ✅    |             |
| `expiration_time` | Expiration Token Date | `datetime` |     | ✅    |             |
| `id`              | ID                    | `integer`  |     | ✅    |             |
| `keys`            | Browser keys          | `char`     | ✅  | ✅    |             |
| `partner_id`      | Partner               | `many2one` | ✅  | ✅    | res.partner |
| `write_date`      | Last Updated on       | `datetime` |     | ✅    |             |
| `write_uid`       | Last Updated by       | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                           | Group                | Perms     |
| ------------------------------ | -------------------- | --------- |
| access.mail.push.device.system | Role / Administrator | `R/W/C/D` |

### 🗃️ `mail.push` — Push Notifications

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                 | Label           | Type       | Req | Store | Relation         |
| --------------------- | --------------- | ---------- | --- | ----- | ---------------- |
| `create_date`         | Created on      | `datetime` |     | ✅    |                  |
| `create_uid`          | Created by      | `many2one` |     | ✅    | res.users        |
| `display_name`        | Display Name    | `char`     |     |       |                  |
| `id`                  | ID              | `integer`  |     | ✅    |                  |
| `mail_push_device_id` | devices         | `many2one` | ✅  | ✅    | mail.push.device |
| `payload`             | Payload         | `text`     |     | ✅    |                  |
| `write_date`          | Last Updated on | `datetime` |     | ✅    |                  |
| `write_uid`           | Last Updated by | `many2one` |     | ✅    | res.users        |

**Access Rights:**

| Name                    | Group                | Perms     |
| ----------------------- | -------------------- | --------- |
| access.mail.push.system | Role / Administrator | `R/W/C/D` |

### 🗃️ `ir.qweb` — Qweb

IrQweb object for rendering stuff in the website context

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `mail.blacklist.remove` — Remove email from blacklist wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `email`        | Email           | `char`     | ✅  | ✅    |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `reason`       | Reason          | `char`     |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                                           | Group                  | Perms     |
| ---------------------------------------------- | ---------------------- | --------- |
| acesss.mail.blacklist.remove.mass_mailing_user | Email Marketing / User | `R/W/C/D` |
| acesss.mail.blacklist.remove.system            | Role / Administrator   | `R/W/C/D` |

### 🗃️ `res.role` — Represents a role in the system used to categorize users. Each role has a unique name and can be associated with multiple users. Roles can be mentioned in messages to notify all associated users.

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation  |
| -------------- | --------------- | ----------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime`  |     | ✅    |           |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users |
| `display_name` | Display Name    | `char`      |     |       |           |
| `id`           | ID              | `integer`   |     | ✅    |           |
| `name`         | Name            | `char`      | ✅  | ✅    |           |
| `user_ids`     | Users           | `many2many` |     | ✅    | res.users |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name           | Group         | Perms     |
| -------------- | ------------- | --------- |
| res.role.admin | Access Rights | `R/W/C/D` |
| res.role.user  | Role / User   | `R`       |

### 🗃️ `discuss.gif.favorite` — Save favorite GIF from Tenor API

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label             | Type       | Req | Store | Relation  |
| -------------- | ----------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on        | `datetime` |     | ✅    |           |
| `create_uid`   | Created by        | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name      | `char`     |     |       |           |
| `id`           | ID                | `integer`  |     | ✅    |           |
| `tenor_gif_id` | GIF id from Tenor | `char`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on   | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by   | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                 | Group       | Perms     |
| -------------------- | ----------- | --------- |
| discuss.gif.favorite | Role / User | `R/W/C/D` |

**Record Rules:**

- **Discuss.gif.favorite: User access** (1) `R/W/C/D`
  - Domain: `[('create_uid', '=', user.id)]`
- **Discuss.gif.favorite: admin full access** (2) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `mail.scheduled.message` — Scheduled Message

Scheduled message model (holds post values generated by the composer to delay the
posting of the message). Different from mail.message.schedule that posts the message but
delays the notification process.

    Todo: when adding support for scheduling messages in mass_mail mode, could add a reference to
    the "parent" composer (by making 'mail.compose.message' not transient anymore). This reference
    could then be used to cancel every message scheduled "at the same time" (from one composer),
    and to get the static 'notification parameters' (mail_server_id, auto_delete,...) instead of
    duplicating them for each scheduled message.
    Currently as scheduling is allowed in monocomment only, we don't have duplicates and we only
    have static notification parameters, but some will become dynamic when adding mass_mail support
    such as 'email_from' and 'force_email_lang'.

**Fields:**

| Field                        | Label                   | Type                 | Req | Store | Relation      |
| ---------------------------- | ----------------------- | -------------------- | --- | ----- | ------------- |
| `attachment_ids`             | Attachments             | `many2many`          |     | ✅    | ir.attachment |
| `author_id`                  | Author                  | `many2one`           | ✅  | ✅    | res.partner   |
| `body`                       | Contents                | `html`               |     | ✅    |               |
| `composition_comment_option` | Comment Options         | `selection`          |     | ✅    |               |
| `create_date`                | Created on              | `datetime`           |     | ✅    |               |
| `create_uid`                 | Created by              | `many2one`           |     | ✅    | res.users     |
| `display_name`               | Display Name            | `char`               |     |       |               |
| `id`                         | ID                      | `integer`            |     | ✅    |               |
| `is_note`                    | Is a note               | `boolean`            |     | ✅    |               |
| `model`                      | Related Document Model  | `char`               | ✅  | ✅    |               |
| `notification_parameters`    | Notification parameters | `text`               |     | ✅    |               |
| `partner_ids`                | Recipients              | `many2many`          |     | ✅    | res.partner   |
| `res_id`                     | Related Document Id     | `many2one_reference` | ✅  | ✅    |               |
| `scheduled_date`             | Scheduled Date          | `datetime`           | ✅  | ✅    |               |
| `send_context`               | Sending Context         | `json`               |     | ✅    |               |
| `subject`                    | Subject                 | `char`               |     | ✅    |               |
| `write_date`                 | Last Updated on         | `datetime`           |     | ✅    |               |
| `write_uid`                  | Last Updated by         | `many2one`           |     | ✅    | res.users     |

**Access Rights:**

| Name                          | Group       | Perms     |
| ----------------------------- | ----------- | --------- |
| access.mail.scheduled.message | Role / User | `R/W/C/D` |

**Record Rules:**

- **False** (Global) `W/C`
  - Domain: `[('create_uid', '=', user.id)]`

### 🗃️ `mail.message.schedule` — Scheduled Messages

Mail message notification schedule queue.

    This model is used to store the mail messages scheduled. So we can
    delay the sending of the notifications. A scheduled date field already
    exists on the <mail.mail> but it does not allow us to delay the sending
    of the <bus.bus> notifications.

**Fields:**

| Field                     | Label                  | Type       | Req | Store | Relation     |
| ------------------------- | ---------------------- | ---------- | --- | ----- | ------------ |
| `create_date`             | Created on             | `datetime` |     | ✅    |              |
| `create_uid`              | Created by             | `many2one` |     | ✅    | res.users    |
| `display_name`            | Display Name           | `char`     |     |       |              |
| `id`                      | ID                     | `integer`  |     | ✅    |              |
| `mail_message_id`         | Message                | `many2one` | ✅  | ✅    | mail.message |
| `notification_parameters` | Notification Parameter | `text`     |     | ✅    |              |
| `scheduled_datetime`      | Scheduled Send Date    | `datetime` | ✅  | ✅    |              |
| `write_date`              | Last Updated on        | `datetime` |     | ✅    |              |
| `write_uid`               | Last Updated by        | `many2one` |     | ✅    | res.users    |

**Access Rights:**

| Name                          | Group                | Perms     |
| ----------------------------- | -------------------- | --------- |
| mail.message.scheduled.system | Role / Administrator | `R/W/C/D` |

### 🗃️ `mail.link.preview` — Store link preview data

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label                | Type       | Req | Store | Relation                  |
| -------------------------- | -------------------- | ---------- | --- | ----- | ------------------------- |
| `create_date`              | Create Date          | `datetime` |     | ✅    |                           |
| `create_uid`               | Created by           | `many2one` |     | ✅    | res.users                 |
| `display_name`             | Display Name         | `char`     |     |       |                           |
| `id`                       | ID                   | `integer`  |     | ✅    |                           |
| `image_mimetype`           | Image MIME type      | `char`     |     | ✅    |                           |
| `message_link_preview_ids` | Message Link Preview | `one2many` |     | ✅    | mail.message.link.preview |
| `og_description`           | Description          | `text`     |     | ✅    |                           |
| `og_image`                 | Image                | `char`     |     | ✅    |                           |
| `og_mimetype`              | MIME type            | `char`     |     | ✅    |                           |
| `og_site_name`             | Site name            | `char`     |     | ✅    |                           |
| `og_title`                 | Title                | `char`     |     | ✅    |                           |
| `og_type`                  | Type                 | `char`     |     | ✅    |                           |
| `source_url`               | URL                  | `char`     | ✅  | ✅    |                           |
| `write_date`               | Last Updated on      | `datetime` |     | ✅    |                           |
| `write_uid`                | Last Updated by      | `many2one` |     | ✅    | res.users                 |

**Access Rights:**

| Name                    | Group         | Perms     |
| ----------------------- | ------------- | --------- |
| mail.link.preview.admin | Access Rights | `R/W/C/D` |

### 🗃️ `ir.config_parameter` — System Parameter

Per-database storage of configuration key-value pairs.

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `key`          | Key             | `char`     | ✅  | ✅    |           |
| `value`        | Value           | `text`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                       | Group                | Perms     |
| -------------------------- | -------------------- | --------- |
| access_ir_config_parameter | Category / Manager   | `R`       |
| ir_config_parameter_system | Role / Administrator | `R/W/C/D` |

### 🗃️ `template.reset.mixin` — Template Reset Mixin

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label             | Type      | Req | Store | Relation |
| -------------- | ----------------- | --------- | --- | ----- | -------- |
| `display_name` | Display Name      | `char`    |     |       |          |
| `id`           | ID                | `integer` |     | ✅    |          |
| `template_fs`  | Template Filename | `char`    |     | ✅    |          |

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

### 🗃️ `mail.presence` — User/Guest Presence

User/Guest Presence Its status is 'online', 'away' or 'offline'. This model should be a
one2one, but is not attached to res_users to avoid database concurrency errors.

**Fields:**

| Field           | Label         | Type        | Req | Store | Relation   |
| --------------- | ------------- | ----------- | --- | ----- | ---------- |
| `display_name`  | Display Name  | `char`      |     |       |            |
| `guest_id`      | Guest         | `many2one`  |     | ✅    | mail.guest |
| `id`            | ID            | `integer`   |     | ✅    |            |
| `last_poll`     | Last Poll     | `datetime`  |     | ✅    |            |
| `last_presence` | Last Presence | `datetime`  |     | ✅    |            |
| `status`        | IM Status     | `selection` |     | ✅    |            |
| `user_id`       | Users         | `many2one`  |     | ✅    | res.users  |

**Access Rights:**

| Name          | Group                | Perms     |
| ------------- | -------------------- | --------- |
| mail.presence | Role / Administrator | `R/W/C/D` |

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

### 🗃️ `res.users.settings.volumes` — User Settings Volumes

Represents the volume of the sound that the user of user_setting_id will receive from
partner_id.

**Fields:**

| Field             | Label           | Type       | Req | Store | Relation           |
| ----------------- | --------------- | ---------- | --- | ----- | ------------------ |
| `create_date`     | Created on      | `datetime` |     | ✅    |                    |
| `create_uid`      | Created by      | `many2one` |     | ✅    | res.users          |
| `display_name`    | Display Name    | `char`     |     |       |                    |
| `guest_id`        | Guest           | `many2one` |     | ✅    | res.partner        |
| `id`              | ID              | `integer`  |     | ✅    |                    |
| `partner_id`      | Partner         | `many2one` |     | ✅    | res.partner        |
| `user_setting_id` | User Setting    | `many2one` | ✅  | ✅    | res.users.settings |
| `volume`          | Volume          | `float`    |     | ✅    |                    |
| `write_date`      | Last Updated on | `datetime` |     | ✅    |                    |
| `write_uid`       | Last Updated by | `many2one` |     | ✅    | res.users          |

**Access Rights:**

| Name                       | Group       | Perms     |
| -------------------------- | ----------- | --------- |
| res.users.settings.volumes | Role / User | `R/W/C/D` |

**Record Rules:**

- **res.users.settings.volumes: access their own entries** (1) `R/W/C/D`
  - Domain: `[('user_setting_id.user_id', '=', user.id)]`
- **Administrators can access all User Settings volumes.** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `ir.ui.view` — View

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                             | Type        | Req | Store | Relation                |
| ----------------------------- | --------------------------------- | ----------- | --- | ----- | ----------------------- |
| `active`                      | Active                            | `boolean`   |     | ✅    |                         |
| `arch`                        | View Architecture                 | `text`      |     |       |                         |
| `arch_base`                   | Base View Architecture            | `text`      |     |       |                         |
| `arch_db`                     | Arch Blob                         | `text`      |     | ✅    |                         |
| `arch_fs`                     | Arch Filename                     | `char`      |     | ✅    |                         |
| `arch_prev`                   | Previous View Architecture        | `text`      |     | ✅    |                         |
| `arch_updated`                | Modified Architecture             | `boolean`   |     | ✅    |                         |
| `controller_page_ids`         | Controller Page                   | `one2many`  |     | ✅    | website.controller.page |
| `create_date`                 | Created on                        | `datetime`  |     | ✅    |                         |
| `create_uid`                  | Created by                        | `many2one`  |     | ✅    | res.users               |
| `customize_show`              | Show As Optional Inherit          | `boolean`   |     | ✅    |                         |
| `display_name`                | Display Name                      | `char`      |     |       |                         |
| `first_page_id`               | Website Page                      | `many2one`  |     |       | website.page            |
| `group_ids`                   | Groups                            | `many2many` |     | ✅    | res.groups              |
| `id`                          | ID                                | `integer`   |     | ✅    |                         |
| `inherit_children_ids`        | Views which inherit from this one | `one2many`  |     | ✅    | ir.ui.view              |
| `inherit_id`                  | Inherited View                    | `many2one`  |     | ✅    | ir.ui.view              |
| `invalid_locators`            | Invalid Locators                  | `json`      |     |       |                         |
| `is_seo_optimized`            | SEO optimized                     | `boolean`   |     | ✅    |                         |
| `key`                         | Key                               | `char`      |     | ✅    |                         |
| `mode`                        | View inheritance mode             | `selection` | ✅  | ✅    |                         |
| `model`                       | Model                             | `char`      |     | ✅    |                         |
| `model_data_id`               | Model Data                        | `many2one`  |     |       | ir.model.data           |
| `model_id`                    | Model of the view                 | `many2one`  |     |       | ir.model                |
| `name`                        | View Name                         | `char`      | ✅  | ✅    |                         |
| `page_ids`                    | Page                              | `one2many`  |     | ✅    | website.page            |
| `priority`                    | Sequence                          | `integer`   | ✅  | ✅    |                         |
| `seo_name`                    | Seo name                          | `char`      |     | ✅    |                         |
| `theme_template_id`           | Theme Template                    | `many2one`  |     | ✅    | theme.ir.ui.view        |
| `track`                       | Track                             | `boolean`   |     | ✅    |                         |
| `type`                        | View Type                         | `selection` |     | ✅    |                         |
| `visibility`                  | Visibility                        | `selection` |     | ✅    |                         |
| `visibility_password`         | Visibility Password               | `char`      |     | ✅    |                         |
| `visibility_password_display` | Visibility Password Display       | `char`      |     |       |                         |
| `warning_info`                | Warning information               | `html`      |     |       |                         |
| `website_id`                  | Website                           | `many2one`  |     | ✅    | website                 |
| `website_meta_description`    | Website meta description          | `text`      |     | ✅    |                         |
| `website_meta_keywords`       | Website meta keywords             | `char`      |     | ✅    |                         |
| `website_meta_og_img`         | Website opengraph image           | `char`      |     | ✅    |                         |
| `website_meta_title`          | Website meta title                | `char`      |     | ✅    |                         |
| `write_date`                  | Last Updated on                   | `datetime`  |     | ✅    |                         |
| `write_uid`                   | Last Updated by                   | `many2one`  |     | ✅    | res.users               |
| `xml_id`                      | External ID                       | `char`      |     |       |                         |

**Access Rights:**

| Name                                        | Group                         | Perms     |
| ------------------------------------------- | ----------------------------- | --------- |
| access_website_ir_ui_view_restricted_editor | Website / Restricted Editor   | `R`       |
| access_website_ir_ui_view_designer          | Website / Editor and Designer | `R/W/C/D` |
| ir_ui_view group_system                     | Role / Administrator          | `R/W/C/D` |
| ir_ui_view group_user                       | Everyone                      | `-`       |

**Record Rules:**

- **website_designer: Manage Website and qWeb view** (72) `R/W/C/D`
  - Domain: `[('type', '=', 'qweb')]`
- **website_designer: global view** (72) `R`
  - Domain: `[('type', '!=', 'qweb')]`
- **Administration Settings: Manage all views** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Website View Visibility Public** (11) `R`
  - Domain: `['|', ('type', '!=', 'qweb'), ('visibility', 'in', ('public', False))]`
- **Website View Visibility Connected** (10) `R`
  - Domain:
    `['|', ('type', '!=', 'qweb'), ('visibility', 'in', ('public', 'connected', False))]`

### 🗃️ `ir.websocket` — websocket message handling

Override to handle discuss specific features (channel in particular).

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |
