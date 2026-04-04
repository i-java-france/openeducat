---
title: "OpenEduCat Library Enterprise"
module: "openeducat_library_enterprise"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Education"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________, odoo/app]
---

# 🟢 OpenEduCat Library Enterprise

> **Module:** `openeducat_library_enterprise` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_library]] [[openeducat_core_enterprise]]

## 📖 Description

## OpenEduCat Library

### Library Management

[![](/openeducat_library_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module adds the feature of library management to OpenEduCat. You can print media
barcode & library id card.

[Contact Us](https://www.openeducat.org/contactus/)

## Medias

Manage all details for media like author, publisher, ISBN code & other details. You can
see movements & requests related to that.

![](/openeducat_library_enterprise/static/description/media.png)

## Media Units

![](/openeducat_library_enterprise/static/description/media_unit.png)

You can create media unit to manage details for each copy of a media.

## Media Movements

Librarian can track media units by media movements and issues, return and actual return
dates.

![](/openeducat_library_enterprise/static/description/media_movements.png)

## Media Queue Request

![](/openeducat_library_enterprise/static/description/media_queue_request.png)

User can make request to get a media. If media is not there in library you can make
purchase request.

## Author

You can manage authors with his medias & other details.

![](/openeducat_library_enterprise/static/description/authors.png)

## Publisher

![](/openeducat_library_enterprise/static/description/publisher.png)

You can manage publisher with its medias & other details.

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Library/All Media/Issue Media`
- `Library/Dashboard`
- `Library/Reporting`
- `Library/Reporting/Media Analysis`
- `Library/Reporting/Media Movement Analysis`
- `Library/Reporting/Media Purchase Analysis`
- `Library/Reporting/Media Queue Analysis`
- `Library/Reporting/Media Unit Analysis`

### Views

- `* INHERIT Portal layout : Library Media (qweb)`
- `* INHERIT Portal layout : Media Purchase (qweb)`
- `* INHERIT Portal layout : Media Purchase Req Form (qweb)`
- `* INHERIT Portal layout : Media Queue Req Form (qweb)`
- `* INHERIT Portal layout : Media queue (qweb)`
- `* INHERIT Portal layout : Meida Movement (qweb)`
- `* INHERIT Portal layout : Submited Purchase Req (qweb)`
- `* INHERIT Portal layout : Submited Queue Req (qweb)`
- `* INHERIT Show Library (qweb)`
- `* INHERIT op.author.inherited.form (form)`
- `* INHERIT op.author.inherited.list (list)`
- `* INHERIT op.library.card.inherited.form (form)`
- `* INHERIT op.library.card.inherited.list (list)`
- `* INHERIT op.library.card.type.inherited.form (form)`
- `* INHERIT op.library.card.type.inherited.list (list)`
- `* INHERIT op.media.form (form)`
- `* INHERIT op.media.inherited.search.view (search)`
- `* INHERIT op.media.inherited.view (list)`
- `* INHERIT op.media.movement.form (form)`
- `* INHERIT op.media.movement.inherited.search.view (search)`
- `* INHERIT op.media.movement.inherited.view (list)`
- `* INHERIT op.media.purchase.inherited.form.view (form)`
- `* INHERIT op.media.purchase.inherited.tree.view (list)`
- `* INHERIT op.media.queue.inherited.form.view (form)`
- `* INHERIT op.media.queue.inherited.search.view (search)`
- `* INHERIT op.media.queue.inherited.tree.view (list)`
- `* INHERIT op.media.type.inherited.form (form)`
- `* INHERIT op.media.type.inherited.list (list)`
- `* INHERIT op.media.unit.form (form)`
- `* INHERIT op.media.unit_inherited.search.view (search)`
- `* INHERIT op.media.unit_inherited.view (list)`
- `* INHERIT op.publisher.inherited.form (form)`
- `* INHERIT op.publisher.inherited.list (list)`
- `* INHERIT student_portal_library (qweb)`
- `barcode.issue.media.form (form)`
- `op.author.form (form)`
- `op.library.card.form (form)`
- `op.library.card.type.form (form)`
- `op.media.movement.pivot (pivot)`
- `op.media.type.dashboard.kanban (kanban)`
- `op.media.type.form (form)`
- `op.publisher.form (form)`
- `openeducat_library_media_data (qweb)`
- `openeducat_library_media_purchase (qweb)`
- `openeducat_library_media_queue (qweb)`
- `openeducat_library_midia_portal (qweb)`
- `portal_student_media_movement_information (qweb)`
- `portal_student_media_movement_list (qweb)`
- `portal_submited_purchase_request_list (qweb)`
- `portal_submited_purchases_request (qweb)`
- `portal_submited_queue_request (qweb)`
- `portal_submited_queue_request_list (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**15 model(s) defined by this module:**

### 🗃️ `op.media` — Media Details

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation          |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ----------------- |
| `active`                     | Active                 | `boolean`   |     | ✅    |                   |
| `author_ids`                 | Author(s)              | `many2many` | ✅  | ✅    | op.author         |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company       |
| `course_ids`                 | Course                 | `many2many` |     | ✅    | op.course         |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                   |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users         |
| `description`                | Description            | `text`      |     | ✅    |                   |
| `display_name`               | Display Name           | `char`      |     |       |                   |
| `edition`                    | Edition                | `char`      |     | ✅    |                   |
| `has_message`                | Has Message            | `boolean`   |     |       |                   |
| `id`                         | ID                     | `integer`   |     | ✅    |                   |
| `internal_code`              | Internal Code          | `char`      |     | ✅    |                   |
| `isbn`                       | ISBN Code              | `char`      |     | ✅    |                   |
| `media_type_id`              | Media Type             | `many2one`  |     | ✅    | op.media.type     |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                   |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers    |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                   |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                   |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                   |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message      |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                   |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                   |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                   |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner       |
| `movement_line`              | Movements              | `one2many`  |     | ✅    | op.media.movement |
| `name`                       | Title                  | `char`      | ✅  | ✅    |                   |
| `publisher_ids`              | Publisher(s)           | `many2many` | ✅  | ✅    | op.publisher      |
| `queue_ids`                  | Media Queue            | `one2many`  |     | ✅    | op.media.queue    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating     |
| `subject_ids`                | Subjects               | `many2many` |     | ✅    | op.subject        |
| `tags`                       | Tag(s)                 | `many2many` |     | ✅    | op.tag            |
| `total_media_queue_req`      | Media Queue Requests   | `integer`   |     |       |                   |
| `total_units`                | Total Units            | `integer`   |     |       |                   |
| `unit_ids`                   | Units                  | `one2many`  |     | ✅    | op.media.unit     |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message      |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                   |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                  | Group             | Perms     |
| --------------------- | ----------------- | --------- |
| name_op_media_library | Library / Manager | `R/W/C/D` |
| name_op_media_faculty | Library / User    | `R`       |

**Record Rules:**

- **Media multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.media.movement` — Media Movement

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation          |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ----------------- |
| `active`                     | Active                 | `boolean`   |     | ✅    |                   |
| `actual_return_date`         | Actual Return Date     | `date`      |     | ✅    |                   |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company       |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                   |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users         |
| `display_name`               | Display Name           | `char`      |     |       |                   |
| `faculty_id`                 | Faculty                | `many2one`  |     | ✅    | op.faculty        |
| `has_message`                | Has Message            | `boolean`   |     |       |                   |
| `id`                         | ID                     | `integer`   |     | ✅    |                   |
| `invoice_id`                 | Invoice                | `many2one`  |     | ✅    | account.move      |
| `is_renew`                   | Renew                  | `boolean`   |     | ✅    |                   |
| `issued_date`                | Issued Date            | `date`      | ✅  | ✅    |                   |
| `library_card_id`            | Library Card           | `many2one`  | ✅  | ✅    | op.library.card   |
| `media_id`                   | Media                  | `many2one`  | ✅  | ✅    | op.media          |
| `media_movement_id`          | Parent Media Movement  | `many2one`  |     | ✅    | op.media.movement |
| `media_type_id`              | Media Type             | `many2one`  |     | ✅    | op.media.type     |
| `media_unit_id`              | Media Unit             | `many2one`  | ✅  | ✅    | op.media.unit     |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                   |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers    |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                   |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                   |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                   |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message      |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                   |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                   |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                   |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner       |
| `partner_id`                 | Person                 | `many2one`  |     | ✅    | res.partner       |
| `penalty`                    | Penalty                | `float`     |     | ✅    |                   |
| `queue_count`                | Media Queue Count      | `float`     |     |       |                   |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating     |
| `renew_ids`                  | Renew Details          | `one2many`  |     | ✅    | op.media.renew    |
| `reserver_name`              | Person Name            | `char`      |     | ✅    |                   |
| `return_date`                | Due Date               | `date`      | ✅  | ✅    |                   |
| `state`                      | Status                 | `selection` |     | ✅    |                   |
| `student_id`                 | Student                | `many2one`  |     | ✅    | op.student        |
| `type`                       | Student/Faculty        | `selection` | ✅  | ✅    |                   |
| `user_id`                    | Users                  | `many2one`  |     | ✅    | res.users         |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message      |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                   |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                           | Group             | Perms     |
| ------------------------------ | ----------------- | --------- |
| name_op_media_movement_library | Library / Manager | `R/W/C/D` |
| name_op_media_movement_faculty | Library / User    | `R`       |

**Record Rules:**

- **Media Movement For Group Student** (130, 129) `R/W/C/D`
  - Domain:
    `['|', ('user_id','=',user.id), ('user_id', 'in', user.child_ids.ids),             ('state','in',['issue'])]         `
- **Media Movement For Group Library** (130) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Media Movement multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.media.purchase` — Media Purchase Request

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `active`                     | Active                 | `boolean`   |     | ✅    |                |
| `author`                     | Author(s)              | `char`      | ✅  | ✅    |                |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company    |
| `course_ids`                 | Course                 | `many2one`  | ✅  | ✅    | op.course      |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users      |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `edition`                    | Edition                | `char`      |     | ✅    |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `media_type_id`              | Media Type             | `many2one`  |     | ✅    | op.media.type  |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `name`                       | Title                  | `char`      | ✅  | ✅    |                |
| `publisher`                  | Publisher(s)           | `char`      |     | ✅    |                |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `request_date`               | Request Date           | `date`      |     | ✅    |                |
| `requested_id`               | Requested By           | `many2one`  |     | ✅    | res.partner    |
| `request_no`                 | Request No.            | `char`      |     | ✅    |                |
| `state`                      | State                  | `selection` |     | ✅    |                |
| `subject_ids`                | Subject                | `many2one`  | ✅  | ✅    | op.subject     |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                           | Group             | Perms     |
| ------------------------------ | ----------------- | --------- |
| name_op_media_purchase_library | Library / Manager | `R/W/C/D` |
| name_op_media_purchase_faculty | Library / User    | `R/W/C`   |

### 🗃️ `op.media.queue` — Media Queue Request

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `active`                     | Active                 | `boolean`   |     | ✅    |                |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company    |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users      |
| `date_from`                  | From Date              | `date`      | ✅  | ✅    |                |
| `date_to`                    | To Date                | `date`      | ✅  | ✅    |                |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `is_read`                    | Read?                  | `boolean`   |     | ✅    |                |
| `media_id`                   | Media                  | `many2one`  | ✅  | ✅    | op.media       |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `name`                       | Sequence No            | `char`      |     | ✅    |                |
| `partner_id`                 | Student/Faculty        | `many2one`  |     | ✅    | res.partner    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `state`                      | Status                 | `selection` |     | ✅    |                |
| `user_id`                    | User                   | `many2one`  |     | ✅    | res.users      |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                        | Group             | Perms     |
| --------------------------- | ----------------- | --------- |
| op_media_queue_library      | Library / Manager | `R/W/C/D` |
| name_op_media_queue_faculty | Library / User    | `R/W/C`   |

**Record Rules:**

- **See Own media Queue Request** (130) `R/W/C/D`
  - Domain: `['|', ('user_id','=',user.id), ('user_id', 'in', user.child_ids.ids)]`
- **View Media Queue** (129) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Media Queue multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.media.unit` — Media Unit

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation          |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ----------------- |
| `active`                     | Active                 | `boolean`   |     | ✅    |                   |
| `barcode`                    | Barcode                | `char`      |     | ✅    |                   |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company       |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                   |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users         |
| `display_name`               | Display Name           | `char`      |     |       |                   |
| `has_message`                | Has Message            | `boolean`   |     |       |                   |
| `id`                         | ID                     | `integer`   |     | ✅    |                   |
| `media_id`                   | Media                  | `many2one`  | ✅  | ✅    | op.media          |
| `media_type_id`              | Media Type             | `many2one`  |     | ✅    | op.media.type     |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                   |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers    |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                   |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                   |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                   |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message      |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                   |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                   |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                   |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner       |
| `movement_lines`             | Movements              | `one2many`  |     | ✅    | op.media.movement |
| `name`                       | Name                   | `char`      | ✅  | ✅    |                   |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating     |
| `state`                      | State                  | `selection` |     | ✅    |                   |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message      |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                   |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                       | Group             | Perms     |
| -------------------------- | ----------------- | --------- |
| name_op_media_unit_library | Library / Manager | `R/W/C/D` |
| name_op_media_unit_faculty | Library / User    | `R`       |

**Record Rules:**

- **Media Unit multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `barcode.issue.media` — Barcode Issue Media Wizard

> ✳️ Transient (Wizard)

Issue Media

**Fields:**

| Field                 | Label               | Type        | Req | Store | Relation  |
| --------------------- | ------------------- | ----------- | --- | ----- | --------- |
| `create_date`         | Created on          | `datetime`  |     | ✅    |           |
| `create_uid`          | Created by          | `many2one`  |     | ✅    | res.users |
| `display_name`        | Display Name        | `char`      |     |       |           |
| `id`                  | ID                  | `integer`   |     | ✅    |           |
| `library_card_number` | Library Card Number | `char`      |     | ✅    |           |
| `media_unit_number`   | Media Unit Number   | `char`      |     | ✅    |           |
| `transaction_type`    | Transaction Type    | `selection` |     | ✅    |           |
| `write_date`          | Last Updated on     | `datetime`  |     | ✅    |           |
| `write_uid`           | Last Updated by     | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                     | Group             | Perms     |
| ------------------------ | ----------------- | --------- |
| name_barcode_issue_media | Library / Manager | `R/W/C/D` |

### 🗃️ `op.library.card` — Library Card

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label           | Type        | Req | Store | Relation             |
| ---------------------- | --------------- | ----------- | --- | ----- | -------------------- |
| `active`               | Active          | `boolean`   |     | ✅    |                      |
| `company_id`           | Company         | `many2one`  |     | ✅    | res.company          |
| `create_date`          | Created on      | `datetime`  |     | ✅    |                      |
| `create_uid`           | Created by      | `many2one`  |     | ✅    | res.users            |
| `display_name`         | Display Name    | `char`      |     |       |                      |
| `faculty_id`           | Faculty         | `many2one`  |     | ✅    | op.faculty           |
| `id`                   | ID              | `integer`   |     | ✅    |                      |
| `issue_date`           | Issue Date      | `date`      | ✅  | ✅    |                      |
| `library_card_type_id` | Card Type       | `many2one`  | ✅  | ✅    | op.library.card.type |
| `number`               | Number          | `char`      |     | ✅    |                      |
| `partner_id`           | Student/Faculty | `many2one`  | ✅  | ✅    | res.partner          |
| `student_id`           | Student         | `many2one`  |     | ✅    | op.student           |
| `type`                 | Type            | `selection` | ✅  | ✅    |                      |
| `write_date`           | Last Updated on | `datetime`  |     | ✅    |                      |
| `write_uid`            | Last Updated by | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                         | Group             | Perms     |
| ---------------------------- | ----------------- | --------- |
| name_op_library_card_library | Library / Manager | `R/W/C/D` |
| name_op_library_card_faculty | Library / User    | `R/W/C/D` |

**Record Rules:**

- **Library Card multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.library.card.type` — Library Card Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                 | Label               | Type       | Req | Store | Relation    |
| --------------------- | ------------------- | ---------- | --- | ----- | ----------- |
| `allow_media`         | No of Media Allowed | `integer`  | ✅  | ✅    |             |
| `company_id`          | Company             | `many2one` |     | ✅    | res.company |
| `create_date`         | Created on          | `datetime` |     | ✅    |             |
| `create_uid`          | Created by          | `many2one` |     | ✅    | res.users   |
| `display_name`        | Display Name        | `char`     |     |       |             |
| `duration`            | Duration            | `integer`  | ✅  | ✅    |             |
| `id`                  | ID                  | `integer`  |     | ✅    |             |
| `name`                | Name                | `char`     | ✅  | ✅    |             |
| `penalty_amt_per_day` | Penalty Amount/Day  | `float`    | ✅  | ✅    |             |
| `write_date`          | Last Updated on     | `datetime` |     | ✅    |             |
| `write_uid`           | Last Updated by     | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                                        | Group             | Perms     |
| ------------------------------------------- | ----------------- | --------- |
| name_op_library_card_type_back_office_admin | Library / Manager | `R/W/C/D` |
| name_op_library_card_type_library           | Library / Manager | `R/W/C/D` |
| name_op_library_card_type_faculty           | Library / User    | `R/W/C/D` |

**Record Rules:**

- **Library Card Type multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.media.renew` — Library Media Renewal

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation          |
| -------------- | --------------- | ---------- | --- | ----- | ----------------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |                   |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users         |
| `display_name` | Display Name    | `char`     |     |       |                   |
| `id`           | ID              | `integer`  |     | ✅    |                   |
| `librarian_id` | Librarian       | `many2one` |     | ✅    | res.users         |
| `movement_id`  | Media Movement  | `many2one` |     | ✅    | op.media.movement |
| `renew_date`   | Renew Date      | `date`     |     | ✅    |                   |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                   |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users         |

**Access Rights:**

| Name                                | Group             | Perms     |
| ----------------------------------- | ----------------- | --------- |
| name_op_media_renew_library         | Library / Manager | `R/W/C/D` |
| name_op_media_renew_student_faculty | Library / User    | `R`       |

### 🗃️ `op.author` — Media Author

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation    |
| -------------- | --------------- | ----------- | --- | ----- | ----------- |
| `company_id`   | Company         | `many2one`  |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime`  |     | ✅    |             |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`      |     |       |             |
| `id`           | ID              | `integer`   |     | ✅    |             |
| `media_ids`    | Media(s)        | `many2many` |     | ✅    | op.media    |
| `name`         | Name            | `char`      | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                   | Group             | Perms     |
| ---------------------- | ----------------- | --------- |
| name_op_author_library | Library / Manager | `R/W/C/D` |
| name_op_author_faculty | Library / User    | `R`       |

**Record Rules:**

- **Author multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.tag` — Media Tags

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Name            | `char`     | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                | Group             | Perms     |
| ------------------- | ----------------- | --------- |
| name_op_tag_library | Library / Manager | `R/W/C/D` |
| name_op_tag_faculty | Library / User    | `R`       |

**Record Rules:**

- **Tag multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.media.type` — Media Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label              | Type       | Req | Store | Relation    |
| ----------------- | ------------------ | ---------- | --- | ----- | ----------- |
| `available`       | Available          | `integer`  |     |       |             |
| `code`            | Code               | `char`     | ✅  | ✅    |             |
| `color`           | Color Index        | `integer`  |     | ✅    |             |
| `company_id`      | Company            | `many2one` |     | ✅    | res.company |
| `create_date`     | Created on         | `datetime` |     | ✅    |             |
| `create_uid`      | Created by         | `many2one` |     | ✅    | res.users   |
| `display_name`    | Display Name       | `char`     |     |       |             |
| `due_media_month` | Due Media of Month | `integer`  |     |       |             |
| `due_media_today` | Due Media of Today | `integer`  |     |       |             |
| `id`              | ID                 | `integer`  |     | ✅    |             |
| `issued`          | Issued             | `integer`  |     |       |             |
| `name`            | Name               | `char`     | ✅  | ✅    |             |
| `total_copies`    | Total Copies       | `integer`  |     |       |             |
| `write_date`      | Last Updated on    | `datetime` |     | ✅    |             |
| `write_uid`       | Last Updated by    | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                       | Group             | Perms     |
| -------------------------- | ----------------- | --------- |
| name_op_media_type_library | Library / Manager | `R/W/C/D` |
| name_op_media_type_faculty | Library / User    | `R/W`     |

**Record Rules:**

- **Media Type multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `onboarding.onboarding` — Onboarding

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label                       | Type        | Req | Store | Relation                   |
| -------------------------- | --------------------------- | ----------- | --- | ----- | -------------------------- |
| `create_date`              | Created on                  | `datetime`  |     | ✅    |                            |
| `create_uid`               | Created by                  | `many2one`  |     | ✅    | res.users                  |
| `current_onboarding_state` | Completion State            | `selection` |     |       |                            |
| `current_progress_id`      | Onboarding Progress         | `many2one`  |     |       | onboarding.progress        |
| `display_name`             | Display Name                | `char`      |     |       |                            |
| `id`                       | ID                          | `integer`   |     | ✅    |                            |
| `is_onboarding_closed`     | Was panel closed?           | `boolean`   |     |       |                            |
| `is_per_company`           | Should be done per company? | `boolean`   |     |       |                            |
| `name`                     | Name of the onboarding      | `char`      |     | ✅    |                            |
| `panel_close_action_name`  | Closing action              | `char`      |     | ✅    |                            |
| `progress_ids`             | Onboarding Progress Records | `one2many`  |     | ✅    | onboarding.progress        |
| `route_name`               | One word name               | `char`      | ✅  | ✅    |                            |
| `sequence`                 | Sequence                    | `integer`   |     | ✅    |                            |
| `step_ids`                 | Onboarding steps            | `many2many` |     | ✅    | onboarding.onboarding.step |
| `text_completed`           | Message at completion       | `char`      |     | ✅    |                            |
| `write_date`               | Last Updated on             | `datetime`  |     | ✅    |                            |
| `write_uid`                | Last Updated by             | `many2one`  |     | ✅    | res.users                  |

**Access Rights:**

| Name                          | Group                | Perms     |
| ----------------------------- | -------------------- | --------- |
| onboarding.onboarding.manager | Role / Administrator | `R/W/C/D` |
| onboarding.onboarding.user    | Role / User          | `-`       |
| onboarding.onboarding.all     | Everyone             | `-`       |

### 🗃️ `onboarding.onboarding.step` — Onboarding Step

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                               | Type        | Req | Store | Relation                 |
| ----------------------------- | ----------------------------------- | ----------- | --- | ----- | ------------------------ |
| `button_text`                 | Button text                         | `char`      | ✅  | ✅    |                          |
| `create_date`                 | Created on                          | `datetime`  |     | ✅    |                          |
| `create_uid`                  | Created by                          | `many2one`  |     | ✅    | res.users                |
| `current_progress_step_id`    | Step Progress                       | `many2one`  |     |       | onboarding.progress.step |
| `current_step_state`          | Completion State                    | `selection` |     |       |                          |
| `description`                 | Description                         | `char`      |     | ✅    |                          |
| `display_name`                | Display Name                        | `char`      |     |       |                          |
| `done_icon`                   | Font Awesome Icon when completed    | `char`      |     | ✅    |                          |
| `done_text`                   | Text to show when step is completed | `char`      |     | ✅    |                          |
| `id`                          | ID                                  | `integer`   |     | ✅    |                          |
| `is_per_company`              | Is per company                      | `boolean`   |     | ✅    |                          |
| `onboarding_ids`              | Onboardings                         | `many2many` |     | ✅    | onboarding.onboarding    |
| `panel_step_open_action_name` | Opening action                      | `char`      |     | ✅    |                          |
| `progress_ids`                | Onboarding Progress Step Records    | `one2many`  |     | ✅    | onboarding.progress.step |
| `sequence`                    | Sequence                            | `integer`   |     | ✅    |                          |
| `step_image`                  | Step Image                          | `binary`    |     | ✅    |                          |
| `step_image_alt`              | Alt Text for the Step Image         | `char`      |     | ✅    |                          |
| `step_image_filename`         | Step Image Filename                 | `char`      |     | ✅    |                          |
| `title`                       | Title                               | `char`      |     | ✅    |                          |
| `write_date`                  | Last Updated on                     | `datetime`  |     | ✅    |                          |
| `write_uid`                   | Last Updated by                     | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                               | Group                | Perms     |
| ---------------------------------- | -------------------- | --------- |
| onboarding.onboarding.step.manager | Role / Administrator | `R/W/C/D` |
| onboarding.onboarding.step.user    | Role / User          | `-`       |
| onboarding.onboarding.step.all     | Everyone             | `-`       |

### 🗃️ `op.publisher` — Publisher

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation    |
| -------------- | --------------- | ----------- | --- | ----- | ----------- |
| `company_id`   | Company         | `many2one`  |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime`  |     | ✅    |             |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`      |     |       |             |
| `id`           | ID              | `integer`   |     | ✅    |             |
| `media_ids`    | Media(s)        | `many2many` |     | ✅    | op.media    |
| `name`         | Name            | `char`      | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                      | Group             | Perms     |
| ------------------------- | ----------------- | --------- |
| name_op_publisher_library | Library / Manager | `R/W/C/D` |
| name_op_publisher_faculty | Library / User    | `R`       |

**Record Rules:**

- **Publisher multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`
