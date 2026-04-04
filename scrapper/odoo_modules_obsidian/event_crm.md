---
title: "Event CRM"
module: "event_crm"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/app/events"
license: "LGPL-3"
category: "Events"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/______]
---

# 🟢 Event CRM

> **Module:** `event_crm` | **Version:** `19.0.1.0` **Category:** Events | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** https://www.odoo.com/app/events

## 🔗 Dependencies

[[event]] [[crm]]

## 📖 Description

Create leads from event registrations.

## 🖥️ UI Components

### Menus

- `Events/Configuration/Lead Generation`

### Views

- `* INHERIT crm.lead.view.form.inherit.event.crm (form)`
- `* INHERIT crm_lead_merge_summary_inherit_event_crm (qweb)`
- `* INHERIT event.event.form.inherit.event.crm (form)`
- `* INHERIT event.event.list.inherit.event.crm (list)`
- `* INHERIT event.question.view.form (form)`
- `* INHERIT event.registration.form.inherit.event.crm (form)`
- `event.lead.rule.view.form (form)`
- `event.lead.rule.view.list (list)`
- `event.lead.rule.view.search (search)`

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

### 🗃️ `crm.lead` — Lead

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                | Label                                     | Type         | Req | Store | Relation                    |
| ------------------------------------ | ----------------------------------------- | ------------ | --- | ----- | --------------------------- |
| `active`                             | Active                                    | `boolean`    |     | ✅    |                             |
| `activity_calendar_event_id`         | Next Activity Calendar Event              | `many2one`   |     |       | calendar.event              |
| `activity_date_deadline`             | Next Activity Deadline                    | `date`       |     |       |                             |
| `activity_exception_decoration`      | Activity Exception Decoration             | `selection`  |     |       |                             |
| `activity_exception_icon`            | Icon                                      | `char`       |     |       |                             |
| `activity_ids`                       | Activities                                | `one2many`   |     | ✅    | mail.activity               |
| `activity_state`                     | Activity State                            | `selection`  |     |       |                             |
| `activity_summary`                   | Next Activity Summary                     | `char`       |     |       |                             |
| `activity_type_icon`                 | Activity Type Icon                        | `char`       |     |       |                             |
| `activity_type_id`                   | Next Activity Type                        | `many2one`   |     |       | mail.activity.type          |
| `activity_user_id`                   | Responsible User                          | `many2one`   |     |       | res.users                   |
| `automated_probability`              | Automated Probability                     | `float`      |     | ✅    |                             |
| `calendar_event_ids`                 | Meetings                                  | `one2many`   |     | ✅    | calendar.event              |
| `campaign_id`                        | Campaign                                  | `many2one`   |     | ✅    | utm.campaign                |
| `city`                               | City                                      | `char`       |     | ✅    |                             |
| `color`                              | Color Index                               | `integer`    |     | ✅    |                             |
| `commercial_partner_id`              | Customer Company                          | `many2one`   |     |       | res.partner                 |
| `company_currency`                   | Currency                                  | `many2one`   |     |       | res.currency                |
| `company_id`                         | Company                                   | `many2one`   |     | ✅    | res.company                 |
| `contact_name`                       | Contact Name                              | `char`       |     | ✅    |                             |
| `country_id`                         | Country                                   | `many2one`   |     | ✅    | res.country                 |
| `create_date`                        | Created on                                | `datetime`   |     | ✅    |                             |
| `create_uid`                         | Created by                                | `many2one`   |     | ✅    | res.users                   |
| `date_automation_last`               | Last Action                               | `datetime`   |     | ✅    |                             |
| `date_closed`                        | Closed Date                               | `datetime`   |     | ✅    |                             |
| `date_conversion`                    | Conversion Date                           | `datetime`   |     | ✅    |                             |
| `date_deadline`                      | Expected Closing                          | `date`       |     | ✅    |                             |
| `date_last_stage_update`             | Last Stage Update                         | `datetime`   |     | ✅    |                             |
| `date_open`                          | Assignment Date                           | `datetime`   |     | ✅    |                             |
| `day_close`                          | Days to Close                             | `float`      |     | ✅    |                             |
| `day_open`                           | Days to Assign                            | `float`      |     | ✅    |                             |
| `description`                        | Notes                                     | `html`       |     | ✅    |                             |
| `display_name`                       | Display Name                              | `char`       |     |       |                             |
| `duplicate_lead_count`               | Potential Duplicate Lead Count            | `integer`    |     |       |                             |
| `duplicate_lead_ids`                 | Potential Duplicate Lead                  | `many2many`  |     |       | crm.lead                    |
| `duration_tracking`                  | Status time                               | `json`       |     |       |                             |
| `email_cc`                           | Email cc                                  | `char`       |     | ✅    |                             |
| `email_domain_criterion`             | Email Domain Criterion                    | `char`       |     | ✅    |                             |
| `email_from`                         | Email                                     | `char`       |     | ✅    |                             |
| `email_normalized`                   | Normalized Email                          | `char`       |     | ✅    |                             |
| `email_state`                        | Email Quality                             | `selection`  |     | ✅    |                             |
| `event_id`                           | Source Event                              | `many2one`   |     | ✅    | event.event                 |
| `event_lead_rule_id`                 | Registration Rule                         | `many2one`   |     | ✅    | event.lead.rule             |
| `expected_revenue`                   | Expected Revenue                          | `monetary`   |     | ✅    |                             |
| `function`                           | Job Position                              | `char`       |     | ✅    |                             |
| `has_message`                        | Has Message                               | `boolean`    |     |       |                             |
| `iap_enrich_done`                    | Enrichment done                           | `boolean`    |     | ✅    |                             |
| `id`                                 | ID                                        | `integer`    |     | ✅    |                             |
| `is_automated_probability`           | Is automated probability?                 | `boolean`    |     |       |                             |
| `is_blacklisted`                     | Blacklist                                 | `boolean`    |     |       |                             |
| `is_partner_visible`                 | Is Partner Visible                        | `boolean`    |     |       |                             |
| `is_rotting`                         | Rotting                                   | `boolean`    |     |       |                             |
| `lang_active_count`                  | Lang Active Count                         | `integer`    |     |       |                             |
| `lang_code`                          | Locale Code                               | `char`       |     |       |                             |
| `lang_id`                            | Language                                  | `many2one`   |     | ✅    | res.lang                    |
| `lead_mining_request_id`             | Lead Mining Request                       | `many2one`   |     | ✅    | crm.iap.lead.mining.request |
| `lead_properties`                    | Properties                                | `properties` |     | ✅    |                             |
| `lost_reason_id`                     | Lost Reason                               | `many2one`   |     | ✅    | crm.lost.reason             |
| `medium_id`                          | Medium                                    | `many2one`   |     | ✅    | utm.medium                  |
| `meeting_display_date`               | Meeting Display Date                      | `date`       |     |       |                             |
| `meeting_display_label`              | Meeting Display Label                     | `char`       |     |       |                             |
| `message_attachment_count`           | Attachment Count                          | `integer`    |     |       |                             |
| `message_bounce`                     | Bounce                                    | `integer`    |     | ✅    |                             |
| `message_follower_ids`               | Followers                                 | `one2many`   |     | ✅    | mail.followers              |
| `message_has_error`                  | Message Delivery error                    | `boolean`    |     |       |                             |
| `message_has_error_counter`          | Number of errors                          | `integer`    |     |       |                             |
| `message_has_sms_error`              | SMS Delivery error                        | `boolean`    |     |       |                             |
| `message_ids`                        | Messages                                  | `one2many`   |     | ✅    | mail.message                |
| `message_is_follower`                | Is Follower                               | `boolean`    |     |       |                             |
| `message_needaction`                 | Action Needed                             | `boolean`    |     |       |                             |
| `message_needaction_counter`         | Number of Actions                         | `integer`    |     |       |                             |
| `message_partner_ids`                | Followers (Partners)                      | `many2many`  |     |       | res.partner                 |
| `my_activity_date_deadline`          | My Activity Deadline                      | `date`       |     |       |                             |
| `name`                               | Opportunity                               | `char`       | ✅  | ✅    |                             |
| `order_ids`                          | Orders                                    | `one2many`   |     | ✅    | sale.order                  |
| `origin_channel_id`                  | Live chat from which the lead was created | `many2one`   |     | ✅    | discuss.channel             |
| `origin_survey_id`                   | Survey                                    | `many2one`   |     | ✅    | survey.survey               |
| `partner_email_update`               | Partner Email will Update                 | `boolean`    |     |       |                             |
| `partner_id`                         | Contact                                   | `many2one`   |     | ✅    | res.partner                 |
| `partner_is_blacklisted`             | Partner is blacklisted                    | `boolean`    |     |       |                             |
| `partner_name`                       | Company Name                              | `char`       |     | ✅    |                             |
| `partner_phone_update`               | Partner Phone will Update                 | `boolean`    |     |       |                             |
| `phone`                              | Phone                                     | `char`       |     | ✅    |                             |
| `phone_blacklisted`                  | Blacklisted Phone is Phone                | `boolean`    |     |       |                             |
| `phone_mobile_search`                | Phone Number                              | `char`       |     |       |                             |
| `phone_sanitized`                    | Sanitized Number                          | `char`       |     | ✅    |                             |
| `phone_sanitized_blacklisted`        | Phone Blacklisted                         | `boolean`    |     |       |                             |
| `phone_state`                        | Phone Quality                             | `selection`  |     | ✅    |                             |
| `priority`                           | Priority                                  | `selection`  |     | ✅    |                             |
| `probability`                        | Probability                               | `float`      |     | ✅    |                             |
| `prorated_revenue`                   | Prorated Revenue                          | `monetary`   |     | ✅    |                             |
| `quotation_count`                    | Number of Quotations                      | `integer`    |     |       |                             |
| `rating_ids`                         | Ratings                                   | `one2many`   |     | ✅    | rating.rating               |
| `recurring_plan`                     | Recurring Plan                            | `many2one`   |     | ✅    | crm.recurring.plan          |
| `recurring_revenue`                  | Recurring Revenues                        | `monetary`   |     | ✅    |                             |
| `recurring_revenue_monthly`          | Expected MRR                              | `monetary`   |     | ✅    |                             |
| `recurring_revenue_monthly_prorated` | Prorated MRR                              | `monetary`   |     | ✅    |                             |
| `recurring_revenue_prorated`         | Prorated Recurring Revenues               | `monetary`   |     | ✅    |                             |
| `referred`                           | Referred By                               | `char`       |     | ✅    |                             |
| `registration_count`                 | # Registrations                           | `integer`    |     |       |                             |
| `registration_ids`                   | Source Registrations                      | `many2many`  |     | ✅    | event.registration          |
| `reveal_id`                          | Reveal ID                                 | `char`       |     | ✅    |                             |
| `rotting_days`                       | Days Rotting                              | `integer`    |     |       |                             |
| `sale_amount_total`                  | Sum of Orders                             | `monetary`   |     |       |                             |
| `sale_order_count`                   | Number of Sale Orders                     | `integer`    |     |       |                             |
| `show_enrich_button`                 | Allow manual enrich                       | `boolean`    |     |       |                             |
| `source_id`                          | Source                                    | `many2one`   |     | ✅    | utm.source                  |
| `stage_id`                           | Stage                                     | `many2one`   |     | ✅    | crm.stage                   |
| `stage_id_color`                     | Stage Color                               | `integer`    |     |       |                             |
| `state_id`                           | State                                     | `many2one`   |     | ✅    | res.country.state           |
| `street`                             | Street                                    | `char`       |     | ✅    |                             |
| `street2`                            | Street2                                   | `char`       |     | ✅    |                             |
| `student_id`                         | Student                                   | `many2one`   |     | ✅    | op.student                  |
| `tag_ids`                            | Tags                                      | `many2many`  |     | ✅    | crm.tag                     |
| `team_id`                            | Sales Team                                | `many2one`   |     | ✅    | crm.team                    |
| `type`                               | Type                                      | `selection`  | ✅  | ✅    |                             |
| `user_company_ids`                   | User Company                              | `many2many`  |     |       | res.company                 |
| `user_id`                            | Salesperson                               | `many2one`   |     | ✅    | res.users                   |
| `visitor_ids`                        | Web Visitors                              | `many2many`  |     | ✅    | website.visitor             |
| `visitor_page_count`                 | # Page Views                              | `integer`    |     |       |                             |
| `visitor_sessions_count`             | # Sessions                                | `integer`    |     |       |                             |
| `website`                            | Website                                   | `char`       |     | ✅    |                             |
| `website_message_ids`                | Website Messages                          | `one2many`   |     | ✅    | mail.message                |
| `won_status`                         | Won/Lost                                  | `selection`  |     | ✅    |                             |
| `write_date`                         | Last Updated on                           | `datetime`   |     | ✅    |                             |
| `write_uid`                          | Last Updated by                           | `many2one`   |     | ✅    | res.users                   |
| `zip`                                | Zip                                       | `char`       |     | ✅    |                             |

**Access Rights:**

| Name             | Group                            | Perms     |
| ---------------- | -------------------------------- | --------- |
| crm.lead         | Sales / User: Own Documents Only | `R/W/C`   |
| crm.lead.manager | Sales / Administrator            | `R/W/C/D` |

**Record Rules:**

- **Personal Leads** (25) `R/W/C/D`
  - Domain: `['|',('user_id','=',user.id),('user_id','=',False)]`
- **CRM Lead Multi-Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **All Leads** (26) `R/W/C/D`
  - Domain: `[(1,'=',1)]`

### 🗃️ `event.lead.request` — Event Lead Request

Technical model created when a user requests 'leads generation' on an event based on all
existing event.lead.rules (see event#action_generate_leads).

    As an event can hold a lot of registrations, we use a batch approach with a separate model that
    contains the batching logic method and the field to retain progress.

    To benefit from a background processing, we use a CRON that calls itself with a CRON trigger
    until the batch is completed, which unlinks this technical generation record.

**Fields:**

| Field                       | Label                  | Type        | Req | Store | Relation        |
| --------------------------- | ---------------------- | ----------- | --- | ----- | --------------- |
| `display_name`              | Display Name           | `char`      |     |       |                 |
| `event_id`                  | Event                  | `many2one`  | ✅  | ✅    | event.event     |
| `event_lead_rule_ids`       | Lead Rules             | `many2many` |     | ✅    | event.lead.rule |
| `id`                        | ID                     | `integer`   |     | ✅    |                 |
| `processed_registration_id` | Processed Registration | `integer`   |     | ✅    |                 |

**Access Rights:**

| Name                      | Group                | Perms     |
| ------------------------- | -------------------- | --------- |
| event.lead.request.system | Role / Administrator | `R/W/C/D` |

### 🗃️ `event.lead.rule` — Event Lead Rules

Rule model for creating / updating leads from event registrations.

    SPECIFICATIONS: CREATION TYPE

    There are two types of lead creation:

      * per attendee: create a lead for each registration;
      * per order: create a lead for a group of registrations;

    The last one is only available through interface if it is possible to register
    a group of attendees in one action (when event_sale or website_event are
    installed). Behavior itself is implemented directly in event_crm.

    Basically a group is either a list of registrations belonging to the same
    event and created in batch (website_event flow). With event_sale this
    definition will be improved to be based on sale_order.

    SPECIFICATIONS: CREATION TRIGGERS

    There are three options to trigger lead creation. We consider basically that
    lead quality increases if attendees confirmed or went to the event. Triggers
    allow therefore to run rules:

      * at attendee creation;
      * at attendee confirmation;
      * at attendee venue;

    This trigger defines when the rule will run.

    SPECIFICATIONS: FILTERING REGISTRATIONS

    When a batch of registrations matches the rule trigger we filter them based
    on conditions and rules defines on event_lead_rule model. Heuristic is the
    following:

      * the rule is active;
      * if a filter is set: filter registrations based on this filter. This is
        done like a search, and filter is a domain;
      * if a company is set on the rule, it must match event's company. Note
        that multi-company rules apply on event_lead_rule;
      * if an event category it set, it must match;
      * if an event is set, it must match;
      * if both event and category are set, one of them must match (OR). If none
        of those are set, it is considered as OK;

    If conditions are met, leads are created with pre-filled informations defined
    on the rule (type, user_id, team_id). Contact information coming from the
    registrations are computed (customer, name, email, phone, contact_name).

    SPECIFICATIONS: OTHER POINTS

    Note that all rules matching their conditions are applied. This means more
    than one lead can be created depending on the configuration. This is
    intended in order to give more freedom to the user using the automatic
    lead generation.

**Fields:**

| Field                       | Label                | Type        | Req | Store | Relation    |
| --------------------------- | -------------------- | ----------- | --- | ----- | ----------- |
| `active`                    | Active               | `boolean`   |     | ✅    |             |
| `company_id`                | Company              | `many2one`  |     | ✅    | res.company |
| `create_date`               | Created on           | `datetime`  |     | ✅    |             |
| `create_uid`                | Created by           | `many2one`  |     | ✅    | res.users   |
| `display_name`              | Display Name         | `char`      |     |       |             |
| `event_id`                  | Event                | `many2one`  |     | ✅    | event.event |
| `event_registration_filter` | Registrations Domain | `text`      |     | ✅    |             |
| `event_type_ids`            | Event Templates      | `many2many` |     | ✅    | event.type  |
| `id`                        | ID                   | `integer`   |     | ✅    |             |
| `lead_creation_basis`       | Create               | `selection` | ✅  | ✅    |             |
| `lead_creation_trigger`     | When                 | `selection` | ✅  | ✅    |             |
| `lead_ids`                  | Created Leads        | `one2many`  |     | ✅    | crm.lead    |
| `lead_sales_team_id`        | Sales Team           | `many2one`  |     | ✅    | crm.team    |
| `lead_tag_ids`              | Tags                 | `many2many` |     | ✅    | crm.tag     |
| `lead_type`                 | Lead Type            | `selection` | ✅  | ✅    |             |
| `lead_user_id`              | Salesperson          | `many2one`  |     | ✅    | res.users   |
| `name`                      | Rule Name            | `char`      | ✅  | ✅    |             |
| `write_date`                | Last Updated on      | `datetime`  |     | ✅    |             |
| `write_uid`                 | Last Updated by      | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                     | Group                            | Perms     |
| ------------------------ | -------------------------------- | --------- |
| event.lead.rule.salesman | Sales / User: Own Documents Only | `R`       |
| event.lead.rule.user     | Events / Registration Desk       | `R`       |
| event.lead.rule.user     | Events / User                    | `R`       |
| event.lead.rule.manager  | Events / Administrator           | `R/W/C/D` |

**Record Rules:**

- **Event CRM: Multi Company** (5) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `event.question.answer` — Event Question Answer

Contains suggested answers to a 'simple_choice' event.question.

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation       |
| -------------- | --------------- | ---------- | --- | ----- | -------------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |                |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users      |
| `display_name` | Display Name    | `char`     |     |       |                |
| `id`           | ID              | `integer`  |     | ✅    |                |
| `name`         | Answer          | `char`     | ✅  | ✅    |                |
| `question_id`  | Question        | `many2one` | ✅  | ✅    | event.question |
| `sequence`     | Sequence        | `integer`  |     | ✅    |                |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users      |

**Access Rights:**

| Name                               | Group                      | Perms     |
| ---------------------------------- | -------------------------- | --------- |
| event.question.answer.registration | Events / Registration Desk | `R/W`     |
| event.question.answer              | Events / User              | `R/W/C/D` |
| event.question.answer.user         | Events / User              | `R/W/C/D` |
| event.question.answer              | Role / Portal              | `R`       |
| event.question.answer              | Role / Public              | `R`       |
| event.question.answer              | Role / User                | `R`       |

**Record Rules:**

- **Event Question Answer: not event groups: event published read** (10, 11, 1) `R`
  - Domain: `[('question_id.event_ids', 'any', [('is_published', '=', True)])]`
- **Event Question Answer: event user: read all** (32) `R`
  - Domain: `[(1, '=', 1)]`
