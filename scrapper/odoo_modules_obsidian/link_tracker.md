---
title: "Link Tracker"
module: "link_tracker"
state: "installed"
version: "19.0.1.1"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Marketing"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 Link Tracker

> **Module:** `link_tracker` | **Version:** `19.0.1.1` **Category:** Marketing |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[utm]] [[mail]]

## 📖 Description

Shorten URLs and use them to track clicks and UTMs

## 🖥️ UI Components

### Menus

- `Link Tracker/Link Tracker`

### Views

- `* INHERIT utm.campaign.view.form (form)`
- `* INHERIT utm.campaign.view.form (kanban)`
- `link.tracker.click.view.form (form)`
- `link.tracker.click.view.graph (graph)`
- `link.tracker.click.view.list (list)`
- `link.tracker.click.view.search (search)`
- `link.tracker.view.form (form)`
- `link.tracker.view.graph (graph)`
- `link.tracker.view.list (list)`
- `link.tracker.view.search (search)`

### Reports

_none_

## 🛠️ Technical Documentation

**5 model(s) defined by this module:**

### 🗃️ `link.tracker` — Link Tracker

Link trackers allow users to wrap any URL into a short URL that can be tracked by Odoo.
Clicks are counter on each link. A tracker is linked to UTMs allowing to analyze
marketing actions.

    This model is also used in mass_mailing where each link in html body is
    automatically converted into a short link that is tracked and integrates
    UTMs.

**Fields:**

| Field             | Label                 | Type       | Req | Store | Relation           |
| ----------------- | --------------------- | ---------- | --- | ----- | ------------------ |
| `absolute_url`    | Absolute URL          | `char`     |     |       |                    |
| `campaign_id`     | Campaign              | `many2one` |     | ✅    | utm.campaign       |
| `code`            | Short URL code        | `char`     |     |       |                    |
| `count`           | Number of Clicks      | `integer`  |     | ✅    |                    |
| `create_date`     | Created on            | `datetime` |     | ✅    |                    |
| `create_uid`      | Created by            | `many2one` |     | ✅    | res.users          |
| `display_name`    | Display Name          | `char`     |     |       |                    |
| `id`              | ID                    | `integer`  |     | ✅    |                    |
| `label`           | Button label          | `char`     |     | ✅    |                    |
| `link_click_ids`  | Clicks                | `one2many` |     | ✅    | link.tracker.click |
| `link_code_ids`   | Codes                 | `one2many` |     | ✅    | link.tracker.code  |
| `mass_mailing_id` | Mass Mailing          | `many2one` |     | ✅    | mailing.mailing    |
| `medium_id`       | Medium                | `many2one` |     | ✅    | utm.medium         |
| `redirected_url`  | Redirected URL        | `char`     |     |       |                    |
| `short_url`       | Tracked URL           | `char`     |     |       |                    |
| `short_url_host`  | Host of the short URL | `char`     |     |       |                    |
| `source_id`       | Source                | `many2one` |     | ✅    | utm.source         |
| `title`           | Page Title            | `char`     |     | ✅    |                    |
| `url`             | Target URL            | `char`     | ✅  | ✅    |                    |
| `write_date`      | Last Updated on       | `datetime` |     | ✅    |                    |
| `write_uid`       | Last Updated by       | `many2one` |     | ✅    | res.users          |

**Access Rights:**

| Name                        | Group                         | Perms     |
| --------------------------- | ----------------------------- | --------- |
| access.link.tracker.mailing | Email Marketing / User        | `R/W/C/D` |
| link.tracker                | Website / Editor and Designer | `R/W/C/D` |
| access.link.tracker.system  | Role / Administrator          | `R/W/C/D` |
| access.link.tracker.public  | Role / Public                 | `-`       |
| access.link.tracker.user    | Role / User                   | `R`       |

### 🗃️ `link.tracker.click` — Link Tracker Click

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field              | Label             | Type       | Req | Store | Relation        |
| ------------------ | ----------------- | ---------- | --- | ----- | --------------- |
| `campaign_id`      | UTM Campaign      | `many2one` |     | ✅    | utm.campaign    |
| `country_id`       | Country           | `many2one` |     | ✅    | res.country     |
| `create_date`      | Created on        | `datetime` |     | ✅    |                 |
| `create_uid`       | Created by        | `many2one` |     | ✅    | res.users       |
| `display_name`     | Display Name      | `char`     |     |       |                 |
| `id`               | ID                | `integer`  |     | ✅    |                 |
| `ip`               | Internet Protocol | `char`     |     | ✅    |                 |
| `link_id`          | Link              | `many2one` | ✅  | ✅    | link.tracker    |
| `mailing_trace_id` | Mail Statistics   | `many2one` |     | ✅    | mailing.trace   |
| `mass_mailing_id`  | Mass Mailing      | `many2one` |     | ✅    | mailing.mailing |
| `write_date`       | Last Updated on   | `datetime` |     | ✅    |                 |
| `write_uid`        | Last Updated by   | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                             | Group                         | Perms     |
| -------------------------------- | ----------------------------- | --------- |
| link.tracker.click               | Website / Editor and Designer | `R/W/C/D` |
| access.link.tracker.click.system | Role / Administrator          | `R/W/C/D` |
| access.link.tracker.click.public | Role / Public                 | `-`       |
| access.link.tracker.click.user   | Role / User                   | `R`       |

### 🗃️ `link.tracker.code` — Link Tracker Code

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation     |
| -------------- | --------------- | ---------- | --- | ----- | ------------ |
| `code`         | Short URL Code  | `char`     | ✅  | ✅    |              |
| `create_date`  | Created on      | `datetime` |     | ✅    |              |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users    |
| `display_name` | Display Name    | `char`     |     |       |              |
| `id`           | ID              | `integer`  |     | ✅    |              |
| `link_id`      | Link            | `many2one` | ✅  | ✅    | link.tracker |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |              |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users    |

**Access Rights:**

| Name                            | Group                         | Perms     |
| ------------------------------- | ----------------------------- | --------- |
| link.tracker.code               | Website / Editor and Designer | `R/W/C/D` |
| access.link.tracker.code.system | Role / Administrator          | `R/W/C/D` |
| access.link.tracker.code.public | Role / Public                 | `-`       |
| access.link.tracker.code.user   | Role / User                   | `R`       |

### 🗃️ `mail.render.mixin` — Mail Render Mixin

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label           | Type      | Req | Store | Relation |
| -------------- | --------------- | --------- | --- | ----- | -------- |
| `display_name` | Display Name    | `char`    |     |       |          |
| `id`           | ID              | `integer` |     | ✅    |          |
| `lang`         | Language        | `char`    |     | ✅    |          |
| `render_model` | Rendering Model | `char`    |     |       |          |

### 🗃️ `utm.campaign` — UTM Campaign

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                                      | Type        | Req | Store | Relation        |
| ------------------------------- | ------------------------------------------ | ----------- | --- | ----- | --------------- |
| `ab_testing_completed`          | A/B Testing Campaign Finished              | `boolean`   |     | ✅    |                 |
| `ab_testing_mailings_count`     | A/B Test Mailings #                        | `integer`   |     |       |                 |
| `ab_testing_schedule_datetime`  | Send Final On                              | `datetime`  |     | ✅    |                 |
| `ab_testing_winner_mailing_id`  | A/B Campaign Winner Mailing                | `many2one`  |     | ✅    | mailing.mailing |
| `ab_testing_winner_selection`   | Winner Selection                           | `selection` |     | ✅    |                 |
| `active`                        | Active                                     | `boolean`   |     | ✅    |                 |
| `bounced_ratio`                 | Bounced Ratio                              | `float`     |     |       |                 |
| `click_count`                   | Number of clicks generated by the campaign | `integer`   |     |       |                 |
| `color`                         | Color Index                                | `integer`   |     | ✅    |                 |
| `company_id`                    | Company                                    | `many2one`  |     | ✅    | res.company     |
| `create_date`                   | Created on                                 | `datetime`  |     | ✅    |                 |
| `create_uid`                    | Created by                                 | `many2one`  |     | ✅    | res.users       |
| `crm_lead_count`                | Leads/Opportunities count                  | `integer`   |     |       |                 |
| `currency_id`                   | Currency                                   | `many2one`  |     |       | res.currency    |
| `display_name`                  | Display Name                               | `char`      |     |       |                 |
| `id`                            | ID                                         | `integer`   |     | ✅    |                 |
| `invoiced_amount`               | Revenues generated by the campaign         | `integer`   |     |       |                 |
| `is_auto_campaign`              | Automatically Generated Campaign           | `boolean`   |     | ✅    |                 |
| `is_mailing_campaign_activated` | Is Mailing Campaign Activated              | `boolean`   |     |       |                 |
| `mailing_mail_count`            | Number of Mass Mailing                     | `integer`   |     |       |                 |
| `mailing_mail_ids`              | Mass Mailings                              | `one2many`  |     | ✅    | mailing.mailing |
| `name`                          | Campaign Identifier                        | `char`      | ✅  | ✅    |                 |
| `opened_ratio`                  | Opened Ratio                               | `float`     |     |       |                 |
| `quotation_count`               | Quotation Count                            | `integer`   |     |       |                 |
| `received_ratio`                | Received Ratio                             | `float`     |     |       |                 |
| `replied_ratio`                 | Replied Ratio                              | `float`     |     |       |                 |
| `stage_id`                      | Stage                                      | `many2one`  | ✅  | ✅    | utm.stage       |
| `tag_ids`                       | Tags                                       | `many2many` |     | ✅    | utm.tag         |
| `title`                         | Campaign Name                              | `char`      | ✅  | ✅    |                 |
| `use_leads`                     | Use Leads                                  | `boolean`   |     |       |                 |
| `user_id`                       | Responsible                                | `many2one`  | ✅  | ✅    | res.users       |
| `write_date`                    | Last Updated on                            | `datetime`  |     | ✅    |                 |
| `write_uid`                     | Last Updated by                            | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                     | Group                  | Perms     |
| ------------------------ | ---------------------- | --------- |
| utm.campaign             | Email Marketing / User | `R/W/C/D` |
| utm.campaign.system      | Role / Administrator   | `R/W/C/D` |
| access_utm_campaign_user | Role / User            | `R/W/C`   |
