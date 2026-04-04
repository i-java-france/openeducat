---
title: "Events Product"
module: "event_product"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Events"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/______]
---

# 🟢 Events Product

> **Module:** `event_product` | **Version:** `19.0.1.0` **Category:** Events |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[event]] [[product]] [[account]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT event.event.ticket.view.form.from.event.inherit.event.product (form)`
- `* INHERIT event.event.ticket.view.form.inherit.event.product (form)`
- `* INHERIT event.event.ticket.view.kanban.from.event.product (kanban)`
- `* INHERIT event.event.ticket.view.list.from.event.inherit.event.product (list)`
- `* INHERIT event.registration.form.inherit (form)`
- `* INHERIT event.registration.graph.inherit.event.sale (graph)`
- `* INHERIT event.registration.list.inherit (list)`
- `* INHERIT event.type.ticket.view.form.inherit.event.product (form)`
- `* INHERIT event.type.ticket.view.list.inherit.event.product (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**6 model(s) defined by this module:**

### 🗃️ `event.event` — Event

> 📧 Mail Thread

Event Model for Training and Placement.

**Fields:**

| Field                                | Label                                       | Type                    | Req | Store | Relation                |
| ------------------------------------ | ------------------------------------------- | ----------------------- | --- | ----- | ----------------------- |
| `active`                             | Active                                      | `boolean`               |     | ✅    |                         |
| `activity_calendar_event_id`         | Next Activity Calendar Event                | `many2one`              |     |       | calendar.event          |
| `activity_date_deadline`             | Next Activity Deadline                      | `date`                  |     |       |                         |
| `activity_exception_decoration`      | Activity Exception Decoration               | `selection`             |     |       |                         |
| `activity_exception_icon`            | Icon                                        | `char`                  |     |       |                         |
| `activity_ids`                       | Activities                                  | `one2many`              |     | ✅    | mail.activity           |
| `activity_state`                     | Activity State                              | `selection`             |     |       |                         |
| `activity_summary`                   | Next Activity Summary                       | `char`                  |     |       |                         |
| `activity_type_icon`                 | Activity Type Icon                          | `char`                  |     |       |                         |
| `activity_type_id`                   | Next Activity Type                          | `many2one`              |     |       | mail.activity.type      |
| `activity_user_id`                   | Responsible User                            | `many2one`              |     |       | res.users               |
| `address_id`                         | Venue                                       | `many2one`              |     | ✅    | res.partner             |
| `address_inline`                     | Venue (formatted for one line uses)         | `char`                  |     |       |                         |
| `address_name`                       | Name                                        | `char`                  |     |       |                         |
| `address_search`                     | Address                                     | `many2one`              |     |       | res.partner             |
| `alumni_event_id`                    | Alumni Group                                | `many2one`              |     | ✅    | op.alumni.group         |
| `badge_format`                       | Badge Dimension                             | `selection`             | ✅  | ✅    |                         |
| `badge_image`                        | Badge Background                            | `binary`                |     | ✅    |                         |
| `can_publish`                        | Can Publish                                 | `boolean`               |     |       |                         |
| `ceremony_id`                        | Convocation Ceremony                        | `many2one`              |     | ✅    | op.convocation.ceremony |
| `community_menu`                     | Community Menu                              | `boolean`               |     | ✅    |                         |
| `community_menu_ids`                 | Event Community Menus                       | `one2many`              |     | ✅    | website.event.menu      |
| `company_id`                         | Company                                     | `many2one`              |     | ✅    | res.company             |
| `country_id`                         | Country                                     | `many2one`              |     | ✅    | res.country             |
| `cover_properties`                   | Cover Properties                            | `text`                  |     | ✅    |                         |
| `create_date`                        | Created on                                  | `datetime`              |     | ✅    |                         |
| `create_uid`                         | Created by                                  | `many2one`              |     | ✅    | res.users               |
| `currency_id`                        | Currency                                    | `many2one`              |     |       | res.currency            |
| `date_begin`                         | Start Date                                  | `datetime`              | ✅  | ✅    |                         |
| `date_end`                           | End Date                                    | `datetime`              | ✅  | ✅    |                         |
| `date_tz`                            | Display Timezone                            | `selection`             | ✅  | ✅    |                         |
| `description`                        | Description                                 | `html`                  |     | ✅    |                         |
| `display_name`                       | Display Name                                | `char`                  |     |       |                         |
| `event_mail_ids`                     | Mail Schedule                               | `one2many`              |     | ✅    | event.mail              |
| `event_register_url`                 | Event Registration Link                     | `char`                  |     |       |                         |
| `event_registrations_open`           | Registration open                           | `boolean`               |     |       |                         |
| `event_registrations_sold_out`       | Sold Out                                    | `boolean`               |     |       |                         |
| `event_registrations_started`        | Registrations started                       | `boolean`               |     |       |                         |
| `event_share_url`                    | Event Share URL                             | `char`                  |     |       |                         |
| `event_slot_count`                   | Slots Count                                 | `integer`               |     |       |                         |
| `event_slot_ids`                     | Slots                                       | `one2many`              |     | ✅    | event.slot              |
| `event_ticket_ids`                   | Event Ticket                                | `one2many`              |     | ✅    | event.event.ticket      |
| `event_type_id`                      | Template                                    | `many2one`              |     | ✅    | event.type              |
| `event_url`                          | Online Event URL                            | `char`                  |     | ✅    |                         |
| `footer_visible`                     | Footer Visible                              | `boolean`               |     | ✅    |                         |
| `general_question_ids`               | General Questions                           | `many2many`             |     | ✅    | event.question          |
| `has_message`                        | Has Message                                 | `boolean`               |     |       |                         |
| `header_visible`                     | Header Visible                              | `boolean`               |     | ✅    |                         |
| `id`                                 | ID                                          | `integer`               |     | ✅    |                         |
| `introduction_menu`                  | Introduction Menu                           | `boolean`               |     | ✅    |                         |
| `introduction_menu_ids`              | Introduction Menus                          | `one2many`              |     | ✅    | website.event.menu      |
| `is_convocation`                     | Is Convocation                              | `boolean`               |     | ✅    |                         |
| `is_done`                            | Is Done                                     | `boolean`               |     |       |                         |
| `is_finished`                        | Is Finished                                 | `boolean`               |     |       |                         |
| `is_multi_slots`                     | Is Multi Slots                              | `boolean`               |     | ✅    |                         |
| `is_one_day`                         | Is One Day                                  | `boolean`               |     |       |                         |
| `is_ongoing`                         | Is Ongoing                                  | `boolean`               |     |       |                         |
| `is_participating`                   | Is Participating                            | `boolean`               |     |       |                         |
| `is_published`                       | Is Published                                | `boolean`               |     | ✅    |                         |
| `is_seo_optimized`                   | SEO optimized                               | `boolean`               |     | ✅    |                         |
| `is_visible_on_website`              | Visible On Website                          | `boolean`               |     |       |                         |
| `kanban_state`                       | Kanban State                                | `selection`             |     | ✅    |                         |
| `lang`                               | Language                                    | `selection`             |     | ✅    |                         |
| `lead_count`                         | # Leads                                     | `integer`               |     |       |                         |
| `lead_ids`                           | Leads                                       | `one2many`              |     | ✅    | crm.lead                |
| `menu_id`                            | Event Menu                                  | `many2one`              |     | ✅    | website.menu            |
| `message_attachment_count`           | Attachment Count                            | `integer`               |     |       |                         |
| `message_follower_ids`               | Followers                                   | `one2many`              |     | ✅    | mail.followers          |
| `message_has_error`                  | Message Delivery error                      | `boolean`               |     |       |                         |
| `message_has_error_counter`          | Number of errors                            | `integer`               |     |       |                         |
| `message_has_sms_error`              | SMS Delivery error                          | `boolean`               |     |       |                         |
| `message_ids`                        | Messages                                    | `one2many`              |     | ✅    | mail.message            |
| `message_is_follower`                | Is Follower                                 | `boolean`               |     |       |                         |
| `message_needaction`                 | Action Needed                               | `boolean`               |     |       |                         |
| `message_needaction_counter`         | Number of Actions                           | `integer`               |     |       |                         |
| `message_partner_ids`                | Followers (Partners)                        | `many2many`             |     |       | res.partner             |
| `my_activity_date_deadline`          | My Activity Deadline                        | `date`                  |     |       |                         |
| `name`                               | Event                                       | `char`                  | ✅  | ✅    |                         |
| `note`                               | Note                                        | `html`                  |     | ✅    |                         |
| `organizer_id`                       | Organizer                                   | `many2one`              |     | ✅    | res.partner             |
| `other_menu_ids`                     | Other Menus                                 | `one2many`              |     | ✅    | website.event.menu      |
| `question_ids`                       | Questions                                   | `many2many`             |     | ✅    | event.question          |
| `rating_ids`                         | Ratings                                     | `one2many`              |     | ✅    | rating.rating           |
| `register_menu`                      | Register Menu                               | `boolean`               |     | ✅    |                         |
| `register_menu_ids`                  | Register Menus                              | `one2many`              |     | ✅    | website.event.menu      |
| `registration_ids`                   | Attendees                                   | `one2many`              |     | ✅    | event.registration      |
| `registration_properties_definition` | Registration Properties                     | `properties_definition` |     | ✅    |                         |
| `sale_order_lines_ids`               | All sale order lines pointing to this event | `one2many`              |     | ✅    | sale.order.line         |
| `sale_price_total`                   | Sales (Tax Included)                        | `monetary`              |     |       |                         |
| `seats_available`                    | Available Seats                             | `integer`               |     |       |                         |
| `seats_limited`                      | Limit Attendees                             | `boolean`               | ✅  | ✅    |                         |
| `seats_max`                          | Maximum Attendees                           | `integer`               |     | ✅    |                         |
| `seats_reserved`                     | Number of Registrations                     | `integer`               |     |       |                         |
| `seats_taken`                        | Number of Taken Seats                       | `integer`               |     |       |                         |
| `seats_used`                         | Number of Attendees                         | `integer`               |     |       |                         |
| `seo_name`                           | Seo name                                    | `char`                  |     | ✅    |                         |
| `specific_question_ids`              | Specific Questions                          | `many2many`             |     | ✅    | event.question          |
| `stage_id`                           | Stage                                       | `many2one`              |     | ✅    | event.stage             |
| `start_remaining`                    | Remaining before start                      | `integer`               |     |       |                         |
| `start_sale_datetime`                | Start sale date                             | `datetime`              |     |       |                         |
| `start_today`                        | Start Today                                 | `boolean`               |     |       |                         |
| `subtitle`                           | Event Subtitle                              | `char`                  |     | ✅    |                         |
| `tag_ids`                            | Tags                                        | `many2many`             |     | ✅    | event.tag               |
| `ticket_instructions`                | Ticket Instructions                         | `html`                  |     | ✅    |                         |
| `training_event`                     | Training Event                              | `boolean`               |     | ✅    |                         |
| `use_barcode`                        | Use Barcode                                 | `boolean`               |     |       |                         |
| `user_id`                            | Responsible                                 | `many2one`              |     | ✅    | res.users               |
| `website_absolute_url`               | Website Absolute URL                        | `char`                  |     |       |                         |
| `website_id`                         | Website                                     | `many2one`              |     | ✅    | website                 |
| `website_menu`                       | Website Menu                                | `boolean`               |     | ✅    |                         |
| `website_message_ids`                | Website Messages                            | `one2many`              |     | ✅    | mail.message            |
| `website_meta_description`           | Website meta description                    | `text`                  |     | ✅    |                         |
| `website_meta_keywords`              | Website meta keywords                       | `char`                  |     | ✅    |                         |
| `website_meta_og_img`                | Website opengraph image                     | `char`                  |     | ✅    |                         |
| `website_meta_title`                 | Website meta title                          | `char`                  |     | ✅    |                         |
| `website_published`                  | Visible on current website                  | `boolean`               |     |       |                         |
| `website_url`                        | Website URL                                 | `char`                  |     |       |                         |
| `website_visibility`                 | Website Visibility                          | `selection`             | ✅  | ✅    |                         |
| `write_date`                         | Last Updated on                             | `datetime`              |     | ✅    |                         |
| `write_uid`                          | Last Updated by                             | `many2one`              |     | ✅    | res.users               |

**Access Rights:**

| Name                     | Group                      | Perms     |
| ------------------------ | -------------------------- | --------- |
| event.event.registration | Events / Registration Desk | `R`       |
| event.event.user         | Events / User              | `R/W/C`   |
| event.event.manager      | Events / Administrator     | `R/W/C/D` |
| event.event              | Role / Portal              | `R`       |
| event.event              | Role / Public              | `R`       |
| event.event              | Role / User                | `R`       |

**Record Rules:**

- **Event: multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Event: public/portal: published read** (10, 11) `R`
  - Domain: `[('website_published', '=', True)]`

### 🗃️ `event.registration` — Event Registration

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                         | Type         | Req | Store | Relation                    |
| -------------------------------- | ----------------------------- | ------------ | --- | ----- | --------------------------- |
| `active`                         | Active                        | `boolean`    |     | ✅    |                             |
| `activity_calendar_event_id`     | Next Activity Calendar Event  | `many2one`   |     |       | calendar.event              |
| `activity_date_deadline`         | Next Activity Deadline        | `date`       |     |       |                             |
| `activity_exception_decoration`  | Activity Exception Decoration | `selection`  |     |       |                             |
| `activity_exception_icon`        | Icon                          | `char`       |     |       |                             |
| `activity_ids`                   | Activities                    | `one2many`   |     | ✅    | mail.activity               |
| `activity_state`                 | Activity State                | `selection`  |     |       |                             |
| `activity_summary`               | Next Activity Summary         | `char`       |     |       |                             |
| `activity_type_icon`             | Activity Type Icon            | `char`       |     |       |                             |
| `activity_type_id`               | Next Activity Type            | `many2one`   |     |       | mail.activity.type          |
| `activity_user_id`               | Responsible User              | `many2one`   |     |       | res.users                   |
| `barcode`                        | Barcode                       | `char`       |     | ✅    |                             |
| `ceremony_id`                    | Ceremony                      | `many2one`   |     | ✅    | op.convocation.ceremony     |
| `company_id`                     | Company                       | `many2one`   |     | ✅    | res.company                 |
| `company_name`                   | Company Name                  | `char`       |     | ✅    |                             |
| `convocation_guest_id`           | Convocation Guest             | `many2one`   |     | ✅    | op.convocation.guest        |
| `convocation_registration_id`    | Convocation Registration      | `many2one`   |     | ✅    | op.convocation.registration |
| `create_date`                    | Created on                    | `datetime`   |     | ✅    |                             |
| `create_uid`                     | Created by                    | `many2one`   |     | ✅    | res.users                   |
| `date_closed`                    | Attended Date                 | `datetime`   |     | ✅    |                             |
| `display_name`                   | Display Name                  | `char`       |     |       |                             |
| `email`                          | Email                         | `char`       |     | ✅    |                             |
| `event_begin_date`               | Event Start Date              | `datetime`   |     |       |                             |
| `event_date_range`               | Date Range                    | `char`       |     |       |                             |
| `event_end_date`                 | Event End Date                | `datetime`   |     |       |                             |
| `event_id`                       | Event                         | `many2one`   | ✅  | ✅    | event.event                 |
| `event_organizer_id`             | Event Organizer               | `many2one`   |     |       | res.partner                 |
| `event_slot_id`                  | Slot                          | `many2one`   |     | ✅    | event.slot                  |
| `event_ticket_id`                | Ticket Type                   | `many2one`   |     | ✅    | event.event.ticket          |
| `event_user_id`                  | Event Responsible             | `many2one`   |     |       | res.users                   |
| `has_message`                    | Has Message                   | `boolean`    |     |       |                             |
| `id`                             | ID                            | `integer`    |     | ✅    |                             |
| `is_convocation`                 | Is Convocation                | `boolean`    |     |       |                             |
| `is_multi_slots`                 | Is Event Multi Slots          | `boolean`    |     |       |                             |
| `lead_count`                     | # Leads                       | `integer`    |     |       |                             |
| `lead_ids`                       | Leads                         | `many2many`  |     | ✅    | crm.lead                    |
| `mail_registration_ids`          | Scheduler Emails              | `one2many`   |     | ✅    | event.mail.registration     |
| `message_attachment_count`       | Attachment Count              | `integer`    |     |       |                             |
| `message_follower_ids`           | Followers                     | `one2many`   |     | ✅    | mail.followers              |
| `message_has_error`              | Message Delivery error        | `boolean`    |     |       |                             |
| `message_has_error_counter`      | Number of errors              | `integer`    |     |       |                             |
| `message_has_sms_error`          | SMS Delivery error            | `boolean`    |     |       |                             |
| `message_ids`                    | Messages                      | `one2many`   |     | ✅    | mail.message                |
| `message_is_follower`            | Is Follower                   | `boolean`    |     |       |                             |
| `message_needaction`             | Action Needed                 | `boolean`    |     |       |                             |
| `message_needaction_counter`     | Number of Actions             | `integer`    |     |       |                             |
| `message_partner_ids`            | Followers (Partners)          | `many2many`  |     |       | res.partner                 |
| `my_activity_date_deadline`      | My Activity Deadline          | `date`       |     |       |                             |
| `name`                           | Attendee Name                 | `char`       |     | ✅    |                             |
| `partner_id`                     | Booked by                     | `many2one`   |     | ✅    | res.partner                 |
| `phone`                          | Phone                         | `char`       |     | ✅    |                             |
| `program_id`                     | Program                       | `many2one`   |     | ✅    | op.program                  |
| `rating_ids`                     | Ratings                       | `one2many`   |     | ✅    | rating.rating               |
| `registration_answer_choice_ids` | Attendee Selection Answers    | `one2many`   |     | ✅    | event.registration.answer   |
| `registration_answer_ids`        | Attendee Answers              | `one2many`   |     | ✅    | event.registration.answer   |
| `registration_properties`        | Properties                    | `properties` |     | ✅    |                             |
| `sale_order_id`                  | Sales Order                   | `many2one`   |     | ✅    | sale.order                  |
| `sale_order_line_id`             | Sales Order Line              | `many2one`   |     | ✅    | sale.order.line             |
| `sale_status`                    | Sale Status                   | `selection`  |     | ✅    |                             |
| `state`                          | Status                        | `selection`  |     | ✅    |                             |
| `utm_campaign_id`                | Campaign                      | `many2one`   |     | ✅    | utm.campaign                |
| `utm_medium_id`                  | Medium                        | `many2one`   |     | ✅    | utm.medium                  |
| `utm_source_id`                  | Source                        | `many2one`   |     | ✅    | utm.source                  |
| `visitor_id`                     | Visitor                       | `many2one`   |     | ✅    | website.visitor             |
| `website_message_ids`            | Website Messages              | `one2many`   |     | ✅    | mail.message                |
| `write_date`                     | Last Updated on               | `datetime`   |     | ✅    |                             |
| `write_uid`                      | Last Updated by               | `many2one`   |     | ✅    | res.users                   |

**Access Rights:**

| Name                            | Group                      | Perms     |
| ------------------------------- | -------------------------- | --------- |
| event.registration.registration | Events / Registration Desk | `R/W/C`   |
| event.registration.manager      | Events / Administrator     | `R/W/C/D` |
| event.registration              | Everyone                   | `-`       |

**Record Rules:**

- **Event/Registration: multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

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

### 🗃️ `event.type.ticket` — Event Template Ticket

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label             | Type       | Req | Store | Relation        |
| --------------- | ----------------- | ---------- | --- | ----- | --------------- |
| `create_date`   | Created on        | `datetime` |     | ✅    |                 |
| `create_uid`    | Created by        | `many2one` |     | ✅    | res.users       |
| `currency_id`   | Currency          | `many2one` |     |       | res.currency    |
| `description`   | Description       | `text`     |     | ✅    |                 |
| `display_name`  | Display Name      | `char`     |     |       |                 |
| `event_type_id` | Event Category    | `many2one` | ✅  | ✅    | event.type      |
| `id`            | ID                | `integer`  |     | ✅    |                 |
| `name`          | Name              | `char`     | ✅  | ✅    |                 |
| `price`         | Price             | `float`    |     | ✅    |                 |
| `price_reduce`  | Price Reduce      | `float`    |     |       |                 |
| `product_id`    | Product           | `many2one` | ✅  | ✅    | product.product |
| `seats_limited` | Limit Attendees   | `boolean`  |     | ✅    |                 |
| `seats_max`     | Maximum Attendees | `integer`  |     | ✅    |                 |
| `sequence`      | Sequence          | `integer`  |     | ✅    |                 |
| `write_date`    | Last Updated on   | `datetime` |     | ✅    |                 |
| `write_uid`     | Last Updated by   | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                           | Group                      | Perms     |
| ------------------------------ | -------------------------- | --------- |
| event.type.ticket.registration | Events / Registration Desk | `R`       |
| event.type.ticket.manager      | Events / Administrator     | `R/W/C/D` |

### 🗃️ `event.event.ticket` — Event Ticket

Ticket model allowing to have different kind of registrations for a given event. Ticket
are based on ticket type as they share some common fields and behavior. Those models
come from <= v13 Odoo event.event.ticket that modeled both concept: tickets for event
templates, and tickets for events.

**Fields:**

| Field                  | Label                | Type       | Req | Store | Relation           |
| ---------------------- | -------------------- | ---------- | --- | ----- | ------------------ |
| `color`                | Color                | `char`     |     | ✅    |                    |
| `company_id`           | Company              | `many2one` |     |       | res.company        |
| `create_date`          | Created on           | `datetime` |     | ✅    |                    |
| `create_uid`           | Created by           | `many2one` |     | ✅    | res.users          |
| `currency_id`          | Currency             | `many2one` |     |       | res.currency       |
| `description`          | Description          | `text`     |     | ✅    |                    |
| `display_name`         | Display Name         | `char`     |     |       |                    |
| `end_sale_datetime`    | Registration End     | `datetime` |     | ✅    |                    |
| `event_id`             | Event                | `many2one` | ✅  | ✅    | event.event        |
| `event_type_id`        | Event Category       | `many2one` |     | ✅    | event.type         |
| `id`                   | ID                   | `integer`  |     | ✅    |                    |
| `is_expired`           | Is Expired           | `boolean`  |     |       |                    |
| `is_guest_ticket`      | Guest Ticket         | `boolean`  |     | ✅    |                    |
| `is_launched`          | Are sales launched   | `boolean`  |     |       |                    |
| `is_sold_out`          | Sold Out             | `boolean`  |     |       |                    |
| `is_student_ticket`    | Student Ticket       | `boolean`  |     | ✅    |                    |
| `limit_max_per_order`  | Limit per Order      | `integer`  |     | ✅    |                    |
| `max_booking_attendee` | Max Booking Attendee | `integer`  |     | ✅    |                    |
| `name`                 | Name                 | `char`     | ✅  | ✅    |                    |
| `price`                | Price                | `float`    |     | ✅    |                    |
| `price_incl`           | Price include        | `float`    |     |       |                    |
| `price_reduce`         | Price Reduce         | `float`    |     |       |                    |
| `price_reduce_taxinc`  | Price Reduce Tax inc | `float`    |     |       |                    |
| `product_id`           | Product              | `many2one` | ✅  | ✅    | product.product    |
| `registration_ids`     | Registrations        | `one2many` |     | ✅    | event.registration |
| `sale_available`       | Is Available         | `boolean`  |     |       |                    |
| `seats_available`      | Available Seats      | `integer`  |     |       |                    |
| `seats_limited`        | Limit Attendees      | `boolean`  |     | ✅    |                    |
| `seats_max`            | Maximum Attendees    | `integer`  |     | ✅    |                    |
| `seats_reserved`       | Reserved Seats       | `integer`  |     |       |                    |
| `seats_taken`          | Taken Seats          | `integer`  |     |       |                    |
| `seats_used`           | Used Seats           | `integer`  |     |       |                    |
| `sequence`             | Sequence             | `integer`  |     | ✅    |                    |
| `start_sale_datetime`  | Registration Start   | `datetime` |     | ✅    |                    |
| `write_date`           | Last Updated on      | `datetime` |     | ✅    |                    |
| `write_uid`            | Last Updated by      | `many2one` |     | ✅    | res.users          |

**Access Rights:**

| Name                            | Group                      | Perms     |
| ------------------------------- | -------------------------- | --------- |
| event.event.ticket.registration | Events / Registration Desk | `R`       |
| event.event.ticket.user         | Events / User              | `R/W/C/D` |
| event.event.ticket              | Role / Portal              | `R`       |
| event.event.ticket              | Role / Public              | `R`       |
| event.event.ticket              | Role / User                | `R`       |
| event.event.ticket              | Everyone                   | `-`       |

**Record Rules:**

- **Event/Ticket: multi-company** (Global) `R/W/C/D`
  - Domain: `[('event_id.company_id', 'in', company_ids + [False])]`
- **Event Ticket: public/portal: published read** (10, 11) `R`
  - Domain: `[('event_id.website_published', '=', True)]`
