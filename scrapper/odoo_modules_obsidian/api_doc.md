---
title: "API Documentation"
module: "api_doc"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Technical"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 API Documentation

> **Module:** `api_doc` | **Version:** `19.0.1.0` **Category:** Technical | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[web]]

## 📖 Description

# Odoo Dynamic API Documentation

This module provides a dynamic documentation page for developpers at the /doc URL. The
documentation is generated using the database to list the models and their fields and
methods. It also provides a playground to run the methods over HTTP, with examples in
various programming languages.

## 🖥️ UI Components

### Menus

_none_

### Views

- `api_doc.docclient (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

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
