---
title: "Mass mailing on attendees"
module: "mass_mailing_event"
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

# 🟢 Mass mailing on attendees

> **Module:** `mass_mailing_event` | **Version:** `19.0.1.0` **Category:** Email
> Marketing | **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[event]] [[mass_mailing]]

## 📖 Description

# Mass mail event attendees

Bridge module adding UX requirements to ease mass mailing of event attendees.

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT event.event.view.form.inherit.mass.mailing (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**2 model(s) defined by this module:**

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
