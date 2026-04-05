---
title: "SMS on Events"
module: "event_sms"
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

# 🟢 SMS on Events

> **Module:** `event_sms` | **Version:** `19.0.1.0` **Category:** Events | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[event]] [[sms]]

## 📖 Description

Schedule SMS in event management

## 🖥️ UI Components

### Menus

_none_

### Views

_none_

### Reports

_none_

## 🛠️ Technical Documentation

**4 model(s) defined by this module:**

### 🗃️ `event.mail` — Event Automated Mailing

Event automated mailing. This model replaces all existing fields and configuration
allowing to send emails on events since Odoo 9. A cron exists that periodically checks
for mailing to run.

**Fields:**

| Field                   | Label                       | Type        | Req | Store | Relation                |
| ----------------------- | --------------------------- | ----------- | --- | ----- | ----------------------- |
| `create_date`           | Created on                  | `datetime`  |     | ✅    |                         |
| `create_uid`            | Created by                  | `many2one`  |     | ✅    | res.users               |
| `display_name`          | Display Name                | `char`      |     |       |                         |
| `error_datetime`        | Last Error                  | `datetime`  |     | ✅    |                         |
| `event_id`              | Event                       | `many2one`  | ✅  | ✅    | event.event             |
| `id`                    | ID                          | `integer`   |     | ✅    |                         |
| `interval_nbr`          | Interval                    | `integer`   |     | ✅    |                         |
| `interval_type`         | Trigger                     | `selection` | ✅  | ✅    |                         |
| `interval_unit`         | Unit                        | `selection` | ✅  | ✅    |                         |
| `last_registration_id`  | Last Attendee               | `many2one`  |     | ✅    | event.registration      |
| `mail_count_done`       | # Sent                      | `integer`   |     | ✅    |                         |
| `mail_done`             | Sent                        | `boolean`   |     | ✅    |                         |
| `mail_registration_ids` | Mail Registration           | `one2many`  |     | ✅    | event.mail.registration |
| `mail_slot_ids`         | Mail Slot                   | `one2many`  |     | ✅    | event.mail.slot         |
| `mail_state`            | Global communication Status | `selection` |     |       |                         |
| `notification_type`     | Send                        | `selection` |     |       |                         |
| `scheduled_date`        | Schedule Date               | `datetime`  |     | ✅    |                         |
| `sequence`              | Display order               | `integer`   |     | ✅    |                         |
| `template_ref`          | Template                    | `reference` | ✅  | ✅    |                         |
| `write_date`            | Last Updated on             | `datetime`  |     | ✅    |                         |
| `write_uid`             | Last Updated by             | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name                    | Group                      | Perms     |
| ----------------------- | -------------------------- | --------- |
| event.mail.registration | Events / Registration Desk | `R`       |
| event.mail.user         | Events / User              | `R/W/C/D` |

### 🗃️ `event.type.mail` — Mail Scheduling on Event Category

Template of event.mail to attach to event.type. Those will be copied upon all events
created in that type to ease event creation.

**Fields:**

| Field               | Label           | Type        | Req | Store | Relation   |
| ------------------- | --------------- | ----------- | --- | ----- | ---------- |
| `create_date`       | Created on      | `datetime`  |     | ✅    |            |
| `create_uid`        | Created by      | `many2one`  |     | ✅    | res.users  |
| `display_name`      | Display Name    | `char`      |     |       |            |
| `event_type_id`     | Event Type      | `many2one`  | ✅  | ✅    | event.type |
| `id`                | ID              | `integer`   |     | ✅    |            |
| `interval_nbr`      | Interval        | `integer`   |     | ✅    |            |
| `interval_type`     | Trigger         | `selection` | ✅  | ✅    |            |
| `interval_unit`     | Unit            | `selection` | ✅  | ✅    |            |
| `notification_type` | Send            | `selection` |     |       |            |
| `template_ref`      | Template        | `reference` | ✅  | ✅    |            |
| `write_date`        | Last Updated on | `datetime`  |     | ✅    |            |
| `write_uid`         | Last Updated by | `many2one`  |     | ✅    | res.users  |

**Access Rights:**

| Name                         | Group                      | Perms     |
| ---------------------------- | -------------------------- | --------- |
| event.type.mail.registration | Events / Registration Desk | `R`       |
| event.type.mail.manager      | Events / Administrator     | `R/W/C/D` |

### 🗃️ `event.mail.registration` — Registration Mail Scheduler

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label           | Type       | Req | Store | Relation           |
| ----------------- | --------------- | ---------- | --- | ----- | ------------------ |
| `create_date`     | Created on      | `datetime` |     | ✅    |                    |
| `create_uid`      | Created by      | `many2one` |     | ✅    | res.users          |
| `display_name`    | Display Name    | `char`     |     |       |                    |
| `id`              | ID              | `integer`  |     | ✅    |                    |
| `mail_sent`       | Mail Sent       | `boolean`  |     | ✅    |                    |
| `registration_id` | Attendee        | `many2one` | ✅  | ✅    | event.registration |
| `scheduled_date`  | Scheduled Time  | `datetime` |     | ✅    |                    |
| `scheduler_id`    | Mail Scheduler  | `many2one` | ✅  | ✅    | event.mail         |
| `write_date`      | Last Updated on | `datetime` |     | ✅    |                    |
| `write_uid`       | Last Updated by | `many2one` |     | ✅    | res.users          |

**Access Rights:**

| Name                                 | Group                      | Perms     |
| ------------------------------------ | -------------------------- | --------- |
| event.mail.registration.registration | Events / Registration Desk | `R`       |
| event.mail.registration.manager      | Events / Administrator     | `R/W/C/D` |

### 🗃️ `sms.template` — SMS Templates

Templates for sending SMS

**Fields:**

| Field               | Label                  | Type       | Req | Store | Relation              |
| ------------------- | ---------------------- | ---------- | --- | ----- | --------------------- |
| `body`              | Body                   | `char`     | ✅  | ✅    |                       |
| `create_date`       | Created on             | `datetime` |     | ✅    |                       |
| `create_uid`        | Created by             | `many2one` |     | ✅    | res.users             |
| `display_name`      | Display Name           | `char`     |     |       |                       |
| `id`                | ID                     | `integer`  |     | ✅    |                       |
| `lang`              | Language               | `char`     |     | ✅    |                       |
| `model`             | Related Document Model | `char`     |     | ✅    |                       |
| `model_id`          | Applies to             | `many2one` | ✅  | ✅    | ir.model              |
| `name`              | Name                   | `char`     |     | ✅    |                       |
| `render_model`      | Rendering Model        | `char`     |     |       |                       |
| `sidebar_action_id` | Sidebar action         | `many2one` |     | ✅    | ir.actions.act_window |
| `template_fs`       | Template Filename      | `char`     |     | ✅    |                       |
| `write_date`        | Last Updated on        | `datetime` |     | ✅    |                       |
| `write_uid`         | Last Updated by        | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                              | Group                     | Perms     |
| --------------------------------- | ------------------------- | --------- |
| access.sms.template.sale.manager  | Sales / Administrator     | `R/W/C/D` |
| access.sms.template.sale.manager  | Sales / Administrator     | `R/W/C/D` |
| access.sms.template.event.manager | Events / Administrator    | `R/W/C/D` |
| access.sms.template.stock.manager | Inventory / Administrator | `R/W/C/D` |
| access.sms.template.system        | Role / Administrator      | `R/W/C/D` |
| access.sms.template.user          | Role / User               | `R`       |
| access.sms.template.all           | Everyone                  | `-`       |

**Record Rules:**

- **SMS Template: system group granted all** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **SMS Template: event manager CUD on event / registrations templates** (34) `W/C/D`
  - Domain: `[('model_id.model', 'in', ('event.event', 'event.registration'))]`
- **SMS Template: sale manager CUD on opportunity / partner templates** (27) `W/C/D`
  - Domain: `[('model_id.model', 'in', ('crm.lead', 'res.partner'))]`
- **SMS Template: stock manager CUD on stock picking templates** (59) `W/C/D`
  - Domain: `[('model_id.model', '=', 'stock.picking')]`
- **SMS Template: sale manager CUD on sale orders** (27) `W/C/D`
  - Domain: `[('model_id.model', 'in', ('sale.order', 'res.partner'))]`
