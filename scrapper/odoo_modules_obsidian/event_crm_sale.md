---
title: "Event CRM Sale"
module: "event_crm_sale"
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

# 🟢 Event CRM Sale

> **Module:** `event_crm_sale` | **Version:** `19.0.1.0` **Category:** Events |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:**
> https://www.odoo.com/app/events

## 🔗 Dependencies

[[event_crm]] [[event_sale]]

## 📖 Description

Add information of sale order linked to the registration for the creation of the lead.

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT event.lead.rule.view.form.inherit.event.crm.sale (form)`
- `* INHERIT event.lead.rule.view.list.inherit.event.crm.sale (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

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
