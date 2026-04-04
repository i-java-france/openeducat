---
title: "OpenEduCat Alumni Blog Enterprise"
module: "openeducat_alumni_blog_enterprise"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Education"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 OpenEduCat Alumni Blog Enterprise

> **Module:** `openeducat_alumni_blog_enterprise` | **Version:** `19.0.1.0`
> **Category:** Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc
> **Website:** https://www.openeducat.org

## 🔗 Dependencies

[[base]] [[website_blog]] [[openeducat_alumni_enterprise]]

## 📖 Description

## OpenEduCat Alumni Blog

[![](/openeducat_alumni_blog_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module adds the feature of blog in alumni management system to OpenEduCat. You can
create blog and post it online.

[Contact Us](https://www.openeducat.org/contactus/)

## Blog post

### Create blog. Create blog post and publish it online.

![](/openeducat_alumni_blog_enterprise/static/description/online_blog.png)

## Blog

### Create blog under that blog and publish it.

![](/openeducat_alumni_blog_enterprise/static/description/create_blog.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Alumni Blog`

### Views

- `* INHERIT Blog Post Detail (qweb)`
- `* INHERIT op.alumni.blog.form (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**2 model(s) defined by this module:**

### 🗃️ `op.alumni.group` — Alumni Group

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                      | Type        | Req | Store | Relation        |
| ---------------------------- | -------------------------- | ----------- | --- | ----- | --------------- |
| `active`                     | Active                     | `boolean`   |     | ✅    |                 |
| `alumni_fees_amount`         | Fees Amount                | `float`     |     | ✅    |                 |
| `alumni_student_line`        | Students                   | `one2many`  |     | ✅    | op.student      |
| `blog_post_ids`              | Blog                       | `one2many`  |     | ✅    | blog.post       |
| `can_publish`                | Can Publish                | `boolean`   |     |       |                 |
| `company_id`                 | Company                    | `many2one`  |     | ✅    | res.company     |
| `create_date`                | Created on                 | `datetime`  |     | ✅    |                 |
| `create_uid`                 | Created by                 | `many2one`  |     | ✅    | res.users       |
| `description`                | Description                | `html`      |     | ✅    |                 |
| `display_name`               | Display Name               | `char`      |     |       |                 |
| `event_count`                | Total_events_record        | `integer`   |     |       |                 |
| `event_ids`                  | Events                     | `one2many`  |     | ✅    | event.event     |
| `fees_id`                    | Fees                       | `many2one`  |     | ✅    | product.product |
| `forum_id`                   | Forum                      | `many2one`  |     | ✅    | forum.forum     |
| `has_message`                | Has Message                | `boolean`   |     |       |                 |
| `id`                         | ID                         | `integer`   |     | ✅    |                 |
| `image`                      | Image                      | `binary`    |     | ✅    |                 |
| `is_published`               | Is Published               | `boolean`   |     | ✅    |                 |
| `is_seo_optimized`           | SEO optimized              | `boolean`   |     | ✅    |                 |
| `message_attachment_count`   | Attachment Count           | `integer`   |     |       |                 |
| `message_follower_ids`       | Followers                  | `one2many`  |     | ✅    | mail.followers  |
| `message_has_error`          | Message Delivery error     | `boolean`   |     |       |                 |
| `message_has_error_counter`  | Number of errors           | `integer`   |     |       |                 |
| `message_has_sms_error`      | SMS Delivery error         | `boolean`   |     |       |                 |
| `message_ids`                | Messages                   | `one2many`  |     | ✅    | mail.message    |
| `message_is_follower`        | Is Follower                | `boolean`   |     |       |                 |
| `message_needaction`         | Action Needed              | `boolean`   |     |       |                 |
| `message_needaction_counter` | Number of Actions          | `integer`   |     |       |                 |
| `message_partner_ids`        | Followers (Partners)       | `many2many` |     |       | res.partner     |
| `name`                       | Name                       | `char`      | ✅  | ✅    |                 |
| `rating_ids`                 | Ratings                    | `one2many`  |     | ✅    | rating.rating   |
| `seo_name`                   | Seo name                   | `char`      |     | ✅    |                 |
| `website_absolute_url`       | Website Absolute URL       | `char`      |     |       |                 |
| `website_id`                 | Website                    | `many2one`  |     | ✅    | website         |
| `website_message_ids`        | Website Messages           | `one2many`  |     | ✅    | mail.message    |
| `website_meta_description`   | Website meta description   | `text`      |     | ✅    |                 |
| `website_meta_keywords`      | Website meta keywords      | `char`      |     | ✅    |                 |
| `website_meta_og_img`        | Website opengraph image    | `char`      |     | ✅    |                 |
| `website_meta_title`         | Website meta title         | `char`      |     | ✅    |                 |
| `website_published`          | Visible on current website | `boolean`   |     |       |                 |
| `website_url`                | Website URL                | `char`      |     |       |                 |
| `write_date`                 | Last Updated on            | `datetime`  |     | ✅    |                 |
| `write_uid`                  | Last Updated by            | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                                | Group            | Perms     |
| ----------------------------------- | ---------------- | --------- |
| access_op_alumni_group_manager      | Alumni / Manager | `R/W/C/D` |
| access_op_alumni_group              | Alumni / User    | `R/W`     |
| access_op_alumni_group_admin_portal | Role / Portal    | `R`       |
| access_op_alumni_group_admin_public | Role / Public    | `R`       |

**Record Rules:**

- **Alumni Group multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `blog.post` — Blog Post

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                      | Type        | Req | Store | Relation        |
| ---------------------------- | -------------------------- | ----------- | --- | ----- | --------------- |
| `active`                     | Active                     | `boolean`   |     | ✅    |                 |
| `alumni_group_id`            | Alumni Group               | `many2one`  |     | ✅    | op.alumni.group |
| `author_avatar`              | Avatar                     | `binary`    |     |       |                 |
| `author_id`                  | Author                     | `many2one`  |     | ✅    | res.partner     |
| `author_name`                | Author Name                | `char`      |     | ✅    |                 |
| `blog_id`                    | Blog                       | `many2one`  | ✅  | ✅    | blog.blog       |
| `can_publish`                | Can Publish                | `boolean`   |     |       |                 |
| `content`                    | Content                    | `html`      |     | ✅    |                 |
| `cover_properties`           | Cover Properties           | `text`      |     | ✅    |                 |
| `create_date`                | Created on                 | `datetime`  |     | ✅    |                 |
| `create_uid`                 | Created by                 | `many2one`  |     | ✅    | res.users       |
| `display_name`               | Display Name               | `char`      |     |       |                 |
| `footer_visible`             | Footer Visible             | `boolean`   |     | ✅    |                 |
| `has_message`                | Has Message                | `boolean`   |     |       |                 |
| `header_visible`             | Header Visible             | `boolean`   |     | ✅    |                 |
| `id`                         | ID                         | `integer`   |     | ✅    |                 |
| `is_published`               | Is Published               | `boolean`   |     | ✅    |                 |
| `is_seo_optimized`           | SEO optimized              | `boolean`   |     | ✅    |                 |
| `message_attachment_count`   | Attachment Count           | `integer`   |     |       |                 |
| `message_follower_ids`       | Followers                  | `one2many`  |     | ✅    | mail.followers  |
| `message_has_error`          | Message Delivery error     | `boolean`   |     |       |                 |
| `message_has_error_counter`  | Number of errors           | `integer`   |     |       |                 |
| `message_has_sms_error`      | SMS Delivery error         | `boolean`   |     |       |                 |
| `message_ids`                | Messages                   | `one2many`  |     | ✅    | mail.message    |
| `message_is_follower`        | Is Follower                | `boolean`   |     |       |                 |
| `message_needaction`         | Action Needed              | `boolean`   |     |       |                 |
| `message_needaction_counter` | Number of Actions          | `integer`   |     |       |                 |
| `message_partner_ids`        | Followers (Partners)       | `many2many` |     |       | res.partner     |
| `name`                       | Title                      | `char`      | ✅  | ✅    |                 |
| `post_date`                  | Publishing date            | `datetime`  |     | ✅    |                 |
| `published_date`             | Published Date             | `datetime`  |     | ✅    |                 |
| `rating_ids`                 | Ratings                    | `one2many`  |     | ✅    | rating.rating   |
| `seo_name`                   | Seo name                   | `char`      |     | ✅    |                 |
| `subtitle`                   | Sub Title                  | `char`      |     | ✅    |                 |
| `tag_ids`                    | Tags                       | `many2many` |     | ✅    | blog.tag        |
| `teaser`                     | Teaser                     | `text`      |     |       |                 |
| `teaser_manual`              | Teaser Content             | `text`      |     | ✅    |                 |
| `visits`                     | No of Views                | `integer`   |     | ✅    |                 |
| `website_absolute_url`       | Website Absolute URL       | `char`      |     |       |                 |
| `website_id`                 | Website                    | `many2one`  |     | ✅    | website         |
| `website_message_ids`        | Website Messages           | `one2many`  |     | ✅    | mail.message    |
| `website_meta_description`   | Website meta description   | `text`      |     | ✅    |                 |
| `website_meta_keywords`      | Website meta keywords      | `char`      |     | ✅    |                 |
| `website_meta_og_img`        | Website opengraph image    | `char`      |     | ✅    |                 |
| `website_meta_title`         | Website meta title         | `char`      |     | ✅    |                 |
| `website_published`          | Visible on current website | `boolean`   |     |       |                 |
| `website_url`                | Website URL                | `char`      |     |       |                 |
| `write_date`                 | Last Updated on            | `datetime`  |     | ✅    |                 |
| `write_uid`                  | Last Contributor           | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name      | Group                         | Perms     |
| --------- | ----------------------------- | --------- |
| blog.post | Website / Editor and Designer | `R/W/C/D` |
| blog.post | Role / Portal                 | `R`       |
| blog.post | Role / Public                 | `R`       |
| blog.post | Role / User                   | `R`       |

**Record Rules:**

- **Blog Post: public: published only** (10, 11) `R/W/C/D`
  - Domain: `[('website_published', '=', True)]`
