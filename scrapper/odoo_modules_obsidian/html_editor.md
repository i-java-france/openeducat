---
title: "HTML Editor"
module: "html_editor"
state: "installed"
version: "19.0.1.0"
author: "odoo"
maintainer: "N/A"
website: "https://www.odoo.com"
license: "LGPL-3"
category: "Technical"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 HTML Editor

> **Module:** `html_editor` | **Version:** `19.0.1.0` **Category:** Technical |
> **License:** `LGPL-3` **Author:** odoo **Website:** https://www.odoo.com

## 🔗 Dependencies

[[base]] [[bus]] [[web]]

## 📖 Description

# Html Editor

This addon provides an extensible, maintainable editor.

## 🖥️ UI Components

### Menus

_none_

### Views

_none_

### Reports

_none_

## 🛠️ Technical Documentation

**24 model(s) defined by this module:**

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

### 🗃️ `base` — Base

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `html.field.history.mixin` — Field html History

The base model, which is implicitly inherited by all models.

**Fields:**

| Field                         | Label            | Type      | Req | Store | Relation |
| ----------------------------- | ---------------- | --------- | --- | ----- | -------- |
| `display_name`                | Display Name     | `char`    |     |       |          |
| `html_field_history`          | History data     | `json`    |     | ✅    |          |
| `html_field_history_metadata` | History metadata | `json`    |     |       |          |
| `id`                          | ID               | `integer` |     | ✅    |          |

### 🗃️ `html_editor.converter.test.sub` — Html Editor Converter Subtest

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Name            | `char`     |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                                  | Group                | Perms     |
| ------------------------------------- | -------------------- | --------- |
| access_html_editor_converter_test_sub | Role / Administrator | `R/W/C/D` |

### 🗃️ `html_editor.converter.test` — Html Editor Converter Test

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label                                                                                                            | Type        | Req | Store | Relation                       |
| --------------- | ---------------------------------------------------------------------------------------------------------------- | ----------- | --- | ----- | ------------------------------ |
| `binary`        | Binary                                                                                                           | `binary`    |     | ✅    |                                |
| `char`          | Char                                                                                                             | `char`      |     | ✅    |                                |
| `create_date`   | Created on                                                                                                       | `datetime`  |     | ✅    |                                |
| `create_uid`    | Created by                                                                                                       | `many2one`  |     | ✅    | res.users                      |
| `date`          | Date                                                                                                             | `date`      |     | ✅    |                                |
| `datetime`      | Datetime                                                                                                         | `datetime`  |     | ✅    |                                |
| `display_name`  | Display Name                                                                                                     | `char`      |     |       |                                |
| `float`         | Float                                                                                                            | `float`     |     | ✅    |                                |
| `html`          | Html                                                                                                             | `html`      |     | ✅    |                                |
| `id`            | ID                                                                                                               | `integer`   |     | ✅    |                                |
| `integer`       | Integer                                                                                                          | `integer`   |     | ✅    |                                |
| `many2one`      | Many2One                                                                                                         | `many2one`  |     | ✅    | html_editor.converter.test.sub |
| `numeric`       | Numeric                                                                                                          | `float`     |     | ✅    |                                |
| `selection_str` | Lorsqu'un pancake prend l'avion à destination de Toronto et qu'il fait une escale technique à St Claude, on dit: | `selection` |     | ✅    |                                |
| `text`          | Text                                                                                                             | `text`      |     | ✅    |                                |
| `write_date`    | Last Updated on                                                                                                  | `datetime`  |     | ✅    |                                |
| `write_uid`     | Last Updated by                                                                                                  | `many2one`  |     | ✅    | res.users                      |

**Access Rights:**

| Name                              | Group                | Perms     |
| --------------------------------- | -------------------- | --------- |
| access_html_editor_converter_test | Role / Administrator | `R/W/C/D` |

### 🗃️ `ir.http` — HTTP Routing

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb` — Qweb

IrQweb object for rendering stuff in the website context

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field` — Qweb Field

Used to convert a t-field specification into an output HTML field.

    :meth:`~.to_html` is the entry point of this conversion from QWeb, it:

    * converts the record value to html using :meth:`~.record_to_html`
    * generates the metadata attributes (``data-oe-``) to set on the root
      result node
    * generates the root result node itself through :meth:`~.render_element`

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.contact` — Qweb Field Contact

Used to convert a t-field specification into an output HTML field.

    :meth:`~.to_html` is the entry point of this conversion from QWeb, it:

    * converts the record value to html using :meth:`~.record_to_html`
    * generates the metadata attributes (``data-oe-``) to set on the root
      result node
    * generates the root result node itself through :meth:`~.render_element`

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.date` — Qweb Field Date

Used to convert a t-field specification into an output HTML field.

    :meth:`~.to_html` is the entry point of this conversion from QWeb, it:

    * converts the record value to html using :meth:`~.record_to_html`
    * generates the metadata attributes (``data-oe-``) to set on the root
      result node
    * generates the root result node itself through :meth:`~.render_element`

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.datetime` — Qweb Field Datetime

Used to convert a t-field specification into an output HTML field.

    :meth:`~.to_html` is the entry point of this conversion from QWeb, it:

    * converts the record value to html using :meth:`~.record_to_html`
    * generates the metadata attributes (``data-oe-``) to set on the root
      result node
    * generates the root result node itself through :meth:`~.render_element`

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.duration` — Qweb Field Duration

`duration` converter, to display integral or fractional values as human-readable time
spans (e.g. 1.5 as "1 hour 30 minutes").

    Can be used on any numerical field.

    Has an option ``unit`` which can be one of ``second``, ``minute``,
    ``hour``, ``day``, ``week`` or ``year``, used to interpret the numerical
    field value before converting it. By default use ``second``.

    Has an option ``round``. By default use ``second``.

    Has an option ``digital`` to display 01:00 instead of 1 hour

    Sub-second values will be ignored.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.float` — Qweb Field Float

Used to convert a t-field specification into an output HTML field.

    :meth:`~.to_html` is the entry point of this conversion from QWeb, it:

    * converts the record value to html using :meth:`~.record_to_html`
    * generates the metadata attributes (``data-oe-``) to set on the root
      result node
    * generates the root result node itself through :meth:`~.render_element`

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.html` — Qweb Field HTML

Used to convert a t-field specification into an output HTML field.

    :meth:`~.to_html` is the entry point of this conversion from QWeb, it:

    * converts the record value to html using :meth:`~.record_to_html`
    * generates the metadata attributes (``data-oe-``) to set on the root
      result node
    * generates the root result node itself through :meth:`~.render_element`

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.image` — Qweb Field Image

    Widget options:

    ``class``
        set as attribute on the generated <img> tag

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.integer` — Qweb Field Integer

Used to convert a t-field specification into an output HTML field.

    :meth:`~.to_html` is the entry point of this conversion from QWeb, it:

    * converts the record value to html using :meth:`~.record_to_html`
    * generates the metadata attributes (``data-oe-``) to set on the root
      result node
    * generates the root result node itself through :meth:`~.render_element`

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.many2one` — Qweb Field Many to One

Used to convert a t-field specification into an output HTML field.

    :meth:`~.to_html` is the entry point of this conversion from QWeb, it:

    * converts the record value to html using :meth:`~.record_to_html`
    * generates the metadata attributes (``data-oe-``) to set on the root
      result node
    * generates the root result node itself through :meth:`~.render_element`

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.monetary` — Qweb Field Monetary

`monetary` converter, has a mandatory option `display_currency` only if field is not of
type Monetary. Otherwise, if we are in presence of a monetary field, the field
definition must have a currency_field attribute set.

    The currency is used for formatting *and rounding* of the float value. It
    is assumed that the linked res_currency has a non-empty rounding value and
    res.currency's ``round`` method is used to perform rounding.

    .. note:: the monetary converter internally adds the qweb context to its
              options mapping, so that the context is available to callees.
              It's set under the ``_values`` key.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.qweb` — Qweb Field qweb

Used to convert a t-field specification into an output HTML field.

    :meth:`~.to_html` is the entry point of this conversion from QWeb, it:

    * converts the record value to html using :meth:`~.record_to_html`
    * generates the metadata attributes (``data-oe-``) to set on the root
      result node
    * generates the root result node itself through :meth:`~.render_element`

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.relative` — Qweb Field Relative

Used to convert a t-field specification into an output HTML field.

    :meth:`~.to_html` is the entry point of this conversion from QWeb, it:

    * converts the record value to html using :meth:`~.record_to_html`
    * generates the metadata attributes (``data-oe-``) to set on the root
      result node
    * generates the root result node itself through :meth:`~.render_element`

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.selection` — Qweb Field Selection

Used to convert a t-field specification into an output HTML field.

    :meth:`~.to_html` is the entry point of this conversion from QWeb, it:

    * converts the record value to html using :meth:`~.record_to_html`
    * generates the metadata attributes (``data-oe-``) to set on the root
      result node
    * generates the root result node itself through :meth:`~.render_element`

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.qweb.field.text` — Qweb Field Text

Used to convert a t-field specification into an output HTML field.

    :meth:`~.to_html` is the entry point of this conversion from QWeb, it:

    * converts the record value to html using :meth:`~.record_to_html`
    * generates the metadata attributes (``data-oe-``) to set on the root
      result node
    * generates the root result node itself through :meth:`~.render_element`

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `ir.ui.view` — View

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                             | Type        | Req | Store | Relation                |
| ----------------------------- | --------------------------------- | ----------- | --- | ----- | ----------------------- |
| `active`                      | Active                            | `boolean`   |     | ✅    |                         |
| `arch`                        | View Architecture                 | `text`      |     |       |                         |
| `arch_base`                   | Base View Architecture            | `text`      |     |       |                         |
| `arch_db`                     | Arch Blob                         | `text`      |     | ✅    |                         |
| `arch_fs`                     | Arch Filename                     | `char`      |     | ✅    |                         |
| `arch_prev`                   | Previous View Architecture        | `text`      |     | ✅    |                         |
| `arch_updated`                | Modified Architecture             | `boolean`   |     | ✅    |                         |
| `controller_page_ids`         | Controller Page                   | `one2many`  |     | ✅    | website.controller.page |
| `create_date`                 | Created on                        | `datetime`  |     | ✅    |                         |
| `create_uid`                  | Created by                        | `many2one`  |     | ✅    | res.users               |
| `customize_show`              | Show As Optional Inherit          | `boolean`   |     | ✅    |                         |
| `display_name`                | Display Name                      | `char`      |     |       |                         |
| `first_page_id`               | Website Page                      | `many2one`  |     |       | website.page            |
| `group_ids`                   | Groups                            | `many2many` |     | ✅    | res.groups              |
| `id`                          | ID                                | `integer`   |     | ✅    |                         |
| `inherit_children_ids`        | Views which inherit from this one | `one2many`  |     | ✅    | ir.ui.view              |
| `inherit_id`                  | Inherited View                    | `many2one`  |     | ✅    | ir.ui.view              |
| `invalid_locators`            | Invalid Locators                  | `json`      |     |       |                         |
| `is_seo_optimized`            | SEO optimized                     | `boolean`   |     | ✅    |                         |
| `key`                         | Key                               | `char`      |     | ✅    |                         |
| `mode`                        | View inheritance mode             | `selection` | ✅  | ✅    |                         |
| `model`                       | Model                             | `char`      |     | ✅    |                         |
| `model_data_id`               | Model Data                        | `many2one`  |     |       | ir.model.data           |
| `model_id`                    | Model of the view                 | `many2one`  |     |       | ir.model                |
| `name`                        | View Name                         | `char`      | ✅  | ✅    |                         |
| `page_ids`                    | Page                              | `one2many`  |     | ✅    | website.page            |
| `priority`                    | Sequence                          | `integer`   | ✅  | ✅    |                         |
| `seo_name`                    | Seo name                          | `char`      |     | ✅    |                         |
| `theme_template_id`           | Theme Template                    | `many2one`  |     | ✅    | theme.ir.ui.view        |
| `track`                       | Track                             | `boolean`   |     | ✅    |                         |
| `type`                        | View Type                         | `selection` |     | ✅    |                         |
| `visibility`                  | Visibility                        | `selection` |     | ✅    |                         |
| `visibility_password`         | Visibility Password               | `char`      |     | ✅    |                         |
| `visibility_password_display` | Visibility Password Display       | `char`      |     |       |                         |
| `warning_info`                | Warning information               | `html`      |     |       |                         |
| `website_id`                  | Website                           | `many2one`  |     | ✅    | website                 |
| `website_meta_description`    | Website meta description          | `text`      |     | ✅    |                         |
| `website_meta_keywords`       | Website meta keywords             | `char`      |     | ✅    |                         |
| `website_meta_og_img`         | Website opengraph image           | `char`      |     | ✅    |                         |
| `website_meta_title`          | Website meta title                | `char`      |     | ✅    |                         |
| `write_date`                  | Last Updated on                   | `datetime`  |     | ✅    |                         |
| `write_uid`                   | Last Updated by                   | `many2one`  |     | ✅    | res.users               |
| `xml_id`                      | External ID                       | `char`      |     |       |                         |

**Access Rights:**

| Name                                        | Group                         | Perms     |
| ------------------------------------------- | ----------------------------- | --------- |
| access_website_ir_ui_view_restricted_editor | Website / Restricted Editor   | `R`       |
| access_website_ir_ui_view_designer          | Website / Editor and Designer | `R/W/C/D` |
| ir_ui_view group_system                     | Role / Administrator          | `R/W/C/D` |
| ir_ui_view group_user                       | Everyone                      | `-`       |

**Record Rules:**

- **website_designer: Manage Website and qWeb view** (72) `R/W/C/D`
  - Domain: `[('type', '=', 'qweb')]`
- **website_designer: global view** (72) `R`
  - Domain: `[('type', '!=', 'qweb')]`
- **Administration Settings: Manage all views** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Website View Visibility Public** (11) `R`
  - Domain: `['|', ('type', '!=', 'qweb'), ('visibility', 'in', ('public', False))]`
- **Website View Visibility Connected** (10) `R`
  - Domain:
    `['|', ('type', '!=', 'qweb'), ('visibility', 'in', ('public', 'connected', False))]`

### 🗃️ `ir.websocket` — websocket message handling

Override to handle discuss specific features (channel in particular).

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |
