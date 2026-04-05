---
title: "OpenEduCat Convocation"
module: "openeducat_convocation"
state: "installed"
version: "19.0.1.0.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "http://www.openeducat.org"
license: "Other proprietary"
category: "Education"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________, odoo/app]
---

# 🟢 OpenEduCat Convocation

> **Module:** `openeducat_convocation` | **Version:** `19.0.1.0.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> http://www.openeducat.org

## 🔗 Dependencies

[[openeducat_core_enterprise]] [[openeducat_event_enterprise]]
[[openeducat_parent_enterprise]] [[web]] [[event]] [[website_event]] [[event_sale]]
[[website_event_sale]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `SIS/Configuration/General Management/Convocation Documents`
- `SIS/Convocation`
- `SIS/Convocation/Ceremonies`
- `SIS/Convocation/Operations`
- `SIS/Convocation/Registrations`
- `SIS/Dashboard/Convocation`

### Views

- `* INHERIT event.event.form.inherit.convocation (form)`
- `* INHERIT event.event.ticket.view.list.from.event (list)`
- `* INHERIT event.question.form.inherit.convocation (form)`
- `* INHERIT event.registration.form.inherit.convocation (form)`
- `* INHERIT modal_ticket_registration_inherit (qweb)`
- `* INHERIT registration_attendee_details_inherit (qweb)`
- `* INHERIT registration_event_question_inherit (qweb)`
- `op.convocation.ceremony.form (form)`
- `op.convocation.ceremony.kanban (kanban)`
- `op.convocation.ceremony.list (list)`
- `op.convocation.ceremony.search (search)`
- `op.convocation.dashboard (kanban)`
- `op.convocation.document.form (form)`
- `op.convocation.document.list (list)`
- `op.convocation.document.search (search)`
- `op.convocation.guest.form (form)`
- `op.convocation.guest.list (list)`
- `op.convocation.guest.search (search)`
- `op.convocation.registration.form (form)`
- `op.convocation.registration.kanban (kanban)`
- `op.convocation.registration.list (list)`
- `op.convocation.registration.search (search)`
- `report_op_convocation_award (qweb)`
- `report_op_convocation_ceremony (qweb)`
- `report_op_convocation_registration (qweb)`

### Reports

- `Convocation Ceremony`
- `Convocation Registration`

## 🛠️ Technical Documentation

**10 model(s) defined by this module:**

### 🗃️ `op.convocation.ceremony` — Convocation Ceremony

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                    |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | --------------------------- |
| `academic_year_id`              | Academic Year                 | `many2one`  | ✅  | ✅    | op.academic.year            |
| `active`                        | Active                        | `boolean`   |     | ✅    |                             |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event              |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                             |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                             |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                             |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity               |
| `activity_state`                | Activity State                | `selection` |     |       |                             |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                             |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                             |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type          |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users                   |
| `address_id`                    | Venue                         | `many2one`  |     | ✅    | res.partner                 |
| `code`                          | Code                          | `char`      | ✅  | ✅    |                             |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company                 |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                             |
| `create_event`                  | Create Event                  | `boolean`   |     | ✅    |                             |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users                   |
| `currency_id`                   | Currency                      | `many2one`  |     |       | res.currency                |
| `date`                          | Date                          | `datetime`  | ✅  | ✅    |                             |
| `display_name`                  | Display Name                  | `char`      |     |       |                             |
| `event_id`                      | Related Event                 | `many2one`  |     | ✅    | event.event                 |
| `event_ticket_ids`              | Event Tickets                 | `one2many`  |     |       | event.event.ticket          |
| `formatted_month`               | Month Year                    | `char`      |     |       |                             |
| `guest_document_ids`            | Guest Documents               | `many2many` |     | ✅    | op.convocation.document     |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                             |
| `id`                            | ID                            | `integer`   |     | ✅    |                             |
| `max_guests_per_student`        | Max Guests per Student        | `integer`   |     | ✅    |                             |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                             |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers              |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                             |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                             |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                             |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message                |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                             |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                             |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                             |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner                 |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                             |
| `name`                          | Name                          | `char`      | ✅  | ✅    |                             |
| `note`                          | Note                          | `text`      |     | ✅    |                             |
| `program_ids`                   | Programs                      | `many2many` | ✅  | ✅    | op.program                  |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating               |
| `registration_ids`              | Registrations                 | `one2many`  |     | ✅    | op.convocation.registration |
| `student_document_ids`          | Student Documents             | `many2many` |     | ✅    | op.convocation.document     |
| `total_guests`                  | Total Guests                  | `integer`   |     |       |                             |
| `total_registrations`           | Total Registrations           | `integer`   |     |       |                             |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message                |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                             |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                         | Group                               | Perms     |
| ---------------------------- | ----------------------------------- | --------- |
| convocation.ceremony.manager | Convocation / Convocation / Manager | `R/W/C/D` |
| convocation.ceremony.user    | Convocation / Convocation / User    | `R`       |

**Record Rules:**

- **Convocation Ceremony: User Access** (170) `R`
- **Convocation Ceremony: Manager Access** (171) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Convocation Ceremony: multi-company rule** (Global) `R/W/C/D`
  - Domain: `['|', ('company_id', '=', False), ('company_id', 'in', company_ids)]`

### 🗃️ `op.convocation.document` — Convocation Document

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation           |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------ |
| `active`                        | Active                        | `boolean`   |     | ✅    |                    |
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
| `code`                          | Code                          | `char`      | ✅  | ✅    |                    |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company        |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `document_type`                 | Document Type                 | `selection` | ✅  | ✅    |                    |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                    |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                    |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                    |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                    |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                    |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                    |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                    |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner        |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                    |
| `name`                          | Name                          | `char`      | ✅  | ✅    |                    |
| `note`                          | Note                          | `text`      |     | ✅    |                    |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                         | Group                               | Perms     |
| ---------------------------- | ----------------------------------- | --------- |
| convocation.document.manager | Convocation / Convocation / Manager | `R/W/C/D` |
| convocation.document.user    | Convocation / Convocation / User    | `R/W/C`   |

**Record Rules:**

- **Convocation Document: multi-company rule** (Global) `R/W/C/D`
  - Domain: `['|', ('company_id', '=', False), ('company_id', 'in', company_ids)]`

### 🗃️ `op.convocation.document.line` — Convocation Document Line

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation                    |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | --------------------------- |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company                 |
| `convocation_document_id`    | Convocation Documents  | `many2one`  |     | ✅    | op.convocation.document     |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                             |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users                   |
| `display_name`               | Display Name           | `char`      |     |       |                             |
| `document_type`              | Document Type          | `selection` |     |       |                             |
| `file`                       | File                   | `binary`    | ✅  | ✅    |                             |
| `file_name`                  | File Name              | `char`      |     | ✅    |                             |
| `guest_registration_id`      | Guest Registration     | `many2one`  |     | ✅    | op.convocation.guest        |
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
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating               |
| `registration_id`            | Registration           | `many2one`  |     | ✅    | op.convocation.registration |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message                |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                             |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                                             | Group                               | Perms     |
| ------------------------------------------------ | ----------------------------------- | --------- |
| convocation.op.convocation.document.line.manager | Convocation / Convocation / Manager | `R/W/C/D` |
| convocation.op.convocation.document.line.user    | Convocation / Convocation / User    | `R`       |

### 🗃️ `op.convocation.guest` — Convocation Guest

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                     |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ---------------------------- |
| `active`                        | Active                        | `boolean`   |     | ✅    |                              |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event               |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                              |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                              |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                              |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity                |
| `activity_state`                | Activity State                | `selection` |     |       |                              |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                              |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                              |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type           |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users                    |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company                  |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                              |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users                    |
| `currency_id`                   | Currency                      | `many2one`  |     |       | res.currency                 |
| `display_name`                  | Display Name                  | `char`      |     |       |                              |
| `email`                         | Email                         | `char`      |     | ✅    |                              |
| `event_registration_id`         | Event Registration            | `many2one`  |     | ✅    | event.registration           |
| `guest_document_line_ids`       | Guest Documents               | `one2many`  |     | ✅    | op.convocation.document.line |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                              |
| `id`                            | ID                            | `integer`   |     | ✅    |                              |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                              |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers               |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                              |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                              |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                              |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message                 |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                              |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                              |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                              |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner                  |
| `mobile`                        | Mobile                        | `char`      |     | ✅    |                              |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                              |
| `name`                          | Name                          | `char`      | ✅  | ✅    |                              |
| `note`                          | Notes                         | `text`      |     | ✅    |                              |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating                |
| `registration_id`               | Registration                  | `many2one`  | ✅  | ✅    | op.convocation.registration  |
| `relationship`                  | Relationship                  | `selection` | ✅  | ✅    |                              |
| `state`                         | Status                        | `selection` |     | ✅    |                              |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message                 |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                              |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                      | Group                               | Perms     |
| ------------------------- | ----------------------------------- | --------- |
| convocation.guest.manager | Convocation / Convocation / Manager | `R/W/C/D` |
| convocation.guest.user    | Convocation / Convocation / User    | `R/W/C`   |

**Record Rules:**

- **Convocation Guest: multi-company rule** (Global) `R/W/C/D`
  - Domain: `['|', ('company_id', '=', False), ('company_id', 'in', company_ids)]`

### 🗃️ `op.convocation.registration` — Convocation Registration

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                     |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ---------------------------- |
| `active`                        | Active                        | `boolean`   |     | ✅    |                              |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event               |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                              |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                              |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                              |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity                |
| `activity_state`                | Activity State                | `selection` |     |       |                              |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                              |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                              |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type           |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users                    |
| `attendance`                    | Will Attend                   | `boolean`   |     | ✅    |                              |
| `ceremony_id`                   | Ceremony                      | `many2one`  | ✅  | ✅    | op.convocation.ceremony      |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company                  |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                              |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users                    |
| `currency_id`                   | Currency                      | `many2one`  |     |       | res.currency                 |
| `display_name`                  | Display Name                  | `char`      |     |       |                              |
| `email`                         | Email                         | `char`      |     | ✅    |                              |
| `event_registration_id`         | Event Registration            | `many2one`  |     | ✅    | event.registration           |
| `guest_ids`                     | Guests                        | `one2many`  |     | ✅    | op.convocation.guest         |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                              |
| `id`                            | ID                            | `integer`   |     | ✅    |                              |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                              |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers               |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                              |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                              |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                              |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message                 |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                              |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                              |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                              |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner                  |
| `mobile`                        | Mobile                        | `char`      |     | ✅    |                              |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                              |
| `name`                          | Name                          | `char`      | ✅  | ✅    |                              |
| `note`                          | Note                          | `text`      |     | ✅    |                              |
| `parent_id`                     | Parent                        | `many2one`  |     | ✅    | op.parent                    |
| `program_id`                    | Program                       | `many2one`  | ✅  | ✅    | op.program                   |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating                |
| `registration_date`             | Registration Date             | `datetime`  |     | ✅    |                              |
| `state`                         | Status                        | `selection` |     | ✅    |                              |
| `student_document_line_ids`     | Student Documents             | `one2many`  |     | ✅    | op.convocation.document.line |
| `student_id`                    | Student                       | `many2one`  | ✅  | ✅    | op.student                   |
| `total_guests`                  | Total Guests                  | `integer`   |     |       |                              |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message                 |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                              |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                             | Group                               | Perms     |
| -------------------------------- | ----------------------------------- | --------- |
| convocation.registration.manager | Convocation / Convocation / Manager | `R/W/C/D` |
| convocation.registration.user    | Convocation / Convocation / User    | `R/W/C`   |

**Record Rules:**

- **Convocation Registration: multi-company rule** (Global) `R/W/C/D`
  - Domain: `['|', ('company_id', '=', False), ('company_id', 'in', company_ids)]`

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

### 🗃️ `event.question` — Event Question

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label                | Type        | Req | Store | Relation              |
| ---------------------- | -------------------- | ----------- | --- | ----- | --------------------- |
| `active`               | Active               | `boolean`   |     | ✅    |                       |
| `answer_ids`           | Answers              | `one2many`  |     | ✅    | event.question.answer |
| `create_date`          | Created on           | `datetime`  |     | ✅    |                       |
| `create_uid`           | Created by           | `many2one`  |     | ✅    | res.users             |
| `display_name`         | Display Name         | `char`      |     |       |                       |
| `document_type`        | Document Type        | `selection` |     | ✅    |                       |
| `event_count`          | # Events             | `integer`   |     |       |                       |
| `event_ids`            | Events               | `many2many` |     | ✅    | event.event           |
| `event_type_ids`       | Event Types          | `many2many` |     | ✅    | event.type            |
| `id`                   | ID                   | `integer`   |     | ✅    |                       |
| `is_default`           | Default question     | `boolean`   |     | ✅    |                       |
| `is_document_question` | Is Document Question | `boolean`   |     | ✅    |                       |
| `is_mandatory_answer`  | Mandatory Answer     | `boolean`   |     | ✅    |                       |
| `is_reusable`          | Is Reusable          | `boolean`   |     | ✅    |                       |
| `once_per_order`       | Ask once per order   | `boolean`   |     | ✅    |                       |
| `question_type`        | Question Type        | `selection` | ✅  | ✅    |                       |
| `sequence`             | Sequence             | `integer`   |     | ✅    |                       |
| `title`                | Title                | `char`      | ✅  | ✅    |                       |
| `write_date`           | Last Updated on      | `datetime`  |     | ✅    |                       |
| `write_uid`            | Last Updated by      | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                | Group                  | Perms     |
| ------------------- | ---------------------- | --------- |
| event.question.user | Events / User          | `R/W/C/D` |
| event.question      | Events / Administrator | `R/W/C/D` |
| event.question      | Role / Portal          | `R`       |
| event.question      | Role / Public          | `R`       |
| event.question      | Role / User            | `R`       |

**Record Rules:**

- **Event Question: not event groups: event published read** (10, 11, 1) `R`
  - Domain: `[('event_ids', 'any', [('is_published', '=', True)])]`
- **Event Question: event user: read all** (32) `R`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `event.registration.answer` — Event Registration Answer

Represents the user input answer for a single event.question

**Fields:**

| Field             | Label            | Type        | Req | Store | Relation              |
| ----------------- | ---------------- | ----------- | --- | ----- | --------------------- |
| `create_date`     | Created on       | `datetime`  |     | ✅    |                       |
| `create_uid`      | Created by       | `many2one`  |     | ✅    | res.users             |
| `display_name`    | Display Name     | `char`      |     |       |                       |
| `event_id`        | Event            | `many2one`  |     |       | event.event           |
| `file`            | File             | `binary`    | ✅  | ✅    |                       |
| `file_name`       | File Name        | `char`      |     | ✅    |                       |
| `id`              | ID               | `integer`   |     | ✅    |                       |
| `partner_id`      | Booked by        | `many2one`  |     |       | res.partner           |
| `question_id`     | Question         | `many2one`  | ✅  | ✅    | event.question        |
| `question_type`   | Question Type    | `selection` |     |       |                       |
| `registration_id` | Registration     | `many2one`  | ✅  | ✅    | event.registration    |
| `value_answer_id` | Suggested answer | `many2one`  |     | ✅    | event.question.answer |
| `value_text_box`  | Text answer      | `text`      |     | ✅    |                       |
| `write_date`      | Last Updated on  | `datetime`  |     | ✅    |                       |
| `write_uid`       | Last Updated by  | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                      | Group                      | Perms     |
| ------------------------- | -------------------------- | --------- |
| event.registration.answer | Events / Registration Desk | `R/W/C/D` |

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
