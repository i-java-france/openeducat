---
title: "Send SMS to Visitor"
module: "website_sms"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Website"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/w______]
---

# 🟢 Send SMS to Visitor

> **Module:** `website_sms` | **Version:** `19.0.1.0` **Category:** Website |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[website]] [[sms]]

## 📖 Description

Allows to send sms to website visitor if the visitor is linked to a partner.

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT website.visitor.view.form.inherit.website.mass.mailing.sms (form)`
- `* INHERIT website.visitor.view.kanban.inherit.website.sms (kanban)`
- `* INHERIT website.visitor.view.list.inherit.website.sms (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

### 🗃️ `website.visitor` — Website Visitor

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label                       | Type        | Req | Store | Relation           |
| -------------------------- | --------------------------- | ----------- | --- | ----- | ------------------ |
| `access_token`             | Access Token                | `char`      | ✅  | ✅    |                    |
| `country_flag`             | Country Flag                | `char`      |     |       |                    |
| `country_id`               | Country                     | `many2one`  |     | ✅    | res.country        |
| `create_date`              | First Connection            | `datetime`  |     | ✅    |                    |
| `create_uid`               | Created by                  | `many2one`  |     | ✅    | res.users          |
| `discuss_channel_ids`      | Visitor's livechat channels | `one2many`  |     | ✅    | discuss.channel    |
| `display_name`             | Display Name                | `char`      |     |       |                    |
| `email`                    | Email                       | `char`      |     |       |                    |
| `event_registered_ids`     | Registered Events           | `many2many` |     |       | event.event        |
| `event_registration_count` | # Registrations             | `integer`   |     |       |                    |
| `event_registration_ids`   | Event Registrations         | `one2many`  |     | ✅    | event.registration |
| `id`                       | ID                          | `integer`   |     | ✅    |                    |
| `is_connected`             | Is connected?               | `boolean`   |     |       |                    |
| `lang_id`                  | Language                    | `many2one`  |     | ✅    | res.lang           |
| `last_connection_datetime` | Last Connection             | `datetime`  |     | ✅    |                    |
| `last_visited_page_id`     | Last Visited Page           | `many2one`  |     |       | website.page       |
| `lead_count`               | # Leads                     | `integer`   |     |       |                    |
| `lead_ids`                 | Leads                       | `many2many` |     | ✅    | crm.lead           |
| `livechat_operator_id`     | Speaking with               | `many2one`  |     | ✅    | res.partner        |
| `livechat_operator_name`   | Operator Name               | `char`      |     |       |                    |
| `mobile`                   | Mobile                      | `char`      |     |       |                    |
| `name`                     | Name                        | `char`      |     |       |                    |
| `page_count`               | # Visited Pages             | `integer`   |     |       |                    |
| `page_ids`                 | Visited Pages               | `many2many` |     |       | website.page       |
| `partner_id`               | Contact                     | `many2one`  |     | ✅    | res.partner        |
| `partner_image`            | Image                       | `binary`    |     |       |                    |
| `product_count`            | Products Views              | `integer`   |     |       |                    |
| `product_ids`              | Visited Products            | `many2many` |     |       | product.product    |
| `session_count`            | # Sessions                  | `integer`   |     |       |                    |
| `time_since_last_action`   | Last action                 | `char`      |     |       |                    |
| `timezone`                 | Timezone                    | `selection` |     | ✅    |                    |
| `visit_count`              | # Visits                    | `integer`   |     | ✅    |                    |
| `visitor_page_count`       | Page Views                  | `integer`   |     |       |                    |
| `visitor_product_count`    | Product Views               | `integer`   |     |       |                    |
| `website_id`               | Website                     | `many2one`  |     | ✅    | website            |
| `website_track_ids`        | Visited Pages History       | `one2many`  |     | ✅    | website.track      |
| `write_date`               | Last Updated on             | `datetime`  |     | ✅    |                    |
| `write_uid`                | Last Updated by             | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                            | Group                            | Perms   |
| ------------------------------- | -------------------------------- | ------- |
| access_website_visitor_salesman | Sales / User: Own Documents Only | `R`     |
| website.visitor.user            | Events / Registration Desk       | `R/W`   |
| website.visitor.livechat.users  | Live Chat / User                 | `R`     |
| access_website_visitor_designer | Website / Editor and Designer    | `R/W/D` |
| access_website_visitor_system   | Role / Administrator             | `R/W/D` |
