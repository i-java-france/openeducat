---
title: "Link Tracker"
module: "website_links"
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

# 🟢 Link Tracker

> **Module:** `website_links` | **Version:** `19.0.1.0` **Category:** Website |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[website]] [[link_tracker]]

## 📖 Description

Generate short links with analytics trackers (UTM) to share your pages through marketing
campaigns. Those trackers can be used in Google Analytics to track clicks and visitors,
or in Odoo reports to analyze the efficiency of those campaigns in terms of lead
generation, related revenues (sales orders), recruitment, etc.

## 🖥️ UI Components

### Menus

- `Website/Site/This page/Link Tracker`

### Views

- `* INHERIT link.tracker.view.list.inherit.website.links (list)`
- `Link Statistics (qweb)`
- `Link Tracker (qweb)`
- `create_shorten_url (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

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
