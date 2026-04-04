---
title: "OpenEduCat Transportation Enterprise"
module: "openeducat_transportation_enterprise"
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

# 🟢 OpenEduCat Transportation Enterprise

> **Module:** `openeducat_transportation_enterprise` | **Version:** `19.0.1.0`
> **Category:** Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc
> **Website:** https://www.openeducat.org

## 🔗 Dependencies

[[fleet]] [[openeducat_core_enterprise]] [[account]]

## 📖 Description

## OpenEduCat Transportation Enterprise

### Manage Vehicles, Stops & Transportations

[![](/openeducat_transportation_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module adds feature to manage transportation to OpenEduCat.

[Contact Us](https://www.openeducat.org/contactus/)

## Routes

Manage the details for routes available at institute for students. You can specify
vehicle that is used for that.

![](/openeducat_transportation_enterprise/static/description/route.png)

## Stops

![](/openeducat_transportation_enterprise/static/description/stops.png)

Create stops used by vehicles with the sequence.

## Trips

Create trips of route for everyday and route related passengers and stops. Set present
or abset for that passengers.

![](/openeducat_transportation_enterprise/static/description/trip.png)

## Vehicle

![](/openeducat_transportation_enterprise/static/description/vehicle.png)

Manage vehicles used for student's transportation. You can maintain registration,
capacity & driver details.

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Transportation`
- `Transportation/Agreements`
- `Transportation/Configuration`
- `Transportation/Configuration/Plan`
- `Transportation/Configuration/Routes`
- `Transportation/Configuration/Settings`
- `Transportation/Configuration/Stops`
- `Transportation/Configuration/Vehicles`
- `Transportation/Reporting`
- `Transportation/Reporting/Trips Analysis`
- `Transportation/Route Register`
- `Transportation/Trips`

### Views

- `op.cost.plan.form (form)`
- `op.cost.plan.list (list)`
- `op.route.form (form)`
- `op.route.form (form)`
- `op.route.line.form (form)`
- `op.route.line.form (form)`
- `op.route.line.graph (graph)`
- `op.route.line.list (list)`
- `op.route.line.pivot (pivot)`
- `op.route.line.search (search)`
- `op.route.list (list)`
- `op.route.register.form (form)`
- `op.route.register.kanban (kanban)`
- `op.route.register.list (list)`
- `op.route.search (search)`
- `op.route.stop.line.form (form)`
- `op.route.stop.line.list (list)`
- `op.route.stop.line.search (search)`
- `op.stop.form (form)`
- `op.stop.form (form)`
- `op.stop.graph (graph)`
- `op.stop.pivot (pivot)`
- `op.stop.search (search)`
- `op.stops.list (list)`
- `op.transportation.agreement.calendar (calendar)`
- `op.transportation.agreement.form (form)`
- `op.transportation.agreement.list (list)`
- `op.transportation.agreement.pivot (pivot)`
- `op.vehicle.form (form)`
- `op.vehicle.form (form)`
- `op.vehicle.list (list)`
- `op.vehicle.search (search)`

### Reports

_none_

## 🛠️ Technical Documentation

**12 model(s) defined by this module:**

### 🗃️ `cost.plan` — Plan for Cost

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
| `bill`                          | Bill Every                    | `integer`   |     | ✅    |                    |
| `bill_selection`                | Bill Type                     | `selection` |     | ✅    |                    |
| `code`                          | Plan Code                     | `char`      | ✅  | ✅    |                    |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company        |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `email_cc`                      | Email cc                      | `char`      |     | ✅    |                    |
| `expires_after`                 | Expires After                 | `integer`   |     | ✅    |                    |
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
| `plan_description`              | Plan Desription               | `text`      |     | ✅    |                    |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                               | Group                              | Perms     |
| ---------------------------------- | ---------------------------------- | --------- |
| access_cost_plan_transport_manager | Transportation Privilege / Manager | `R/W/C/D` |

**Record Rules:**

- **Cost Plan multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.transportation.agreement` — Transportation Agreement

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                                  | Type        | Req | Store | Relation                               |
| -------------------------------- | -------------------------------------- | ----------- | --- | ----- | -------------------------------------- |
| `activity_calendar_event_id`     | Next Activity Calendar Event           | `many2one`  |     |       | calendar.event                         |
| `activity_date_deadline`         | Next Activity Deadline                 | `date`      |     |       |                                        |
| `activity_exception_decoration`  | Activity Exception Decoration          | `selection` |     |       |                                        |
| `activity_exception_icon`        | Icon                                   | `char`      |     |       |                                        |
| `activity_ids`                   | Activities                             | `one2many`  |     | ✅    | mail.activity                          |
| `activity_state`                 | Activity State                         | `selection` |     |       |                                        |
| `activity_summary`               | Next Activity Summary                  | `char`      |     |       |                                        |
| `activity_type_icon`             | Activity Type Icon                     | `char`      |     |       |                                        |
| `activity_type_id`               | Next Activity Type                     | `many2one`  |     |       | mail.activity.type                     |
| `activity_user_id`               | Responsible User                       | `many2one`  |     |       | res.users                              |
| `bill`                           | Bill Every                             | `integer`   |     | ✅    |                                        |
| `bill_selection`                 | Bill Type                              | `selection` |     | ✅    |                                        |
| `company_id`                     | Company                                | `many2one`  |     | ✅    | res.company                            |
| `create_date`                    | Created on                             | `datetime`  |     | ✅    |                                        |
| `create_uid`                     | Created by                             | `many2one`  |     | ✅    | res.users                              |
| `date`                           | Agreement Date                         | `date`      | ✅  | ✅    |                                        |
| `display_name`                   | Display Name                           | `char`      |     |       |                                        |
| `email_cc`                       | Email cc                               | `char`      |     | ✅    |                                        |
| `end_date`                       | End Date                               | `date`      |     | ✅    |                                        |
| `expires_after`                  | Expires After                          | `integer`   |     | ✅    |                                        |
| `has_message`                    | Has Message                            | `boolean`   |     |       |                                        |
| `id`                             | ID                                     | `integer`   |     | ✅    |                                        |
| `invoice_count`                  | Bill Count                             | `integer`   |     | ✅    |                                        |
| `message_attachment_count`       | Attachment Count                       | `integer`   |     |       |                                        |
| `message_follower_ids`           | Followers                              | `one2many`  |     | ✅    | mail.followers                         |
| `message_has_error`              | Message Delivery error                 | `boolean`   |     |       |                                        |
| `message_has_error_counter`      | Number of errors                       | `integer`   |     |       |                                        |
| `message_has_sms_error`          | SMS Delivery error                     | `boolean`   |     |       |                                        |
| `message_ids`                    | Messages                               | `one2many`  |     | ✅    | mail.message                           |
| `message_is_follower`            | Is Follower                            | `boolean`   |     |       |                                        |
| `message_needaction`             | Action Needed                          | `boolean`   |     |       |                                        |
| `message_needaction_counter`     | Number of Actions                      | `integer`   |     |       |                                        |
| `message_partner_ids`            | Followers (Partners)                   | `many2many` |     |       | res.partner                            |
| `my_activity_date_deadline`      | My Activity Deadline                   | `date`      |     |       |                                        |
| `next_invoice_date`              | Next Invoice Date                      | `date`      |     | ✅    |                                        |
| `partner_id`                     | Student/Faculty                        | `many2one`  | ✅  | ✅    | res.partner                            |
| `plan_id`                        | Plan                                   | `many2one`  |     | ✅    | cost.plan                              |
| `prev_invoice_date`              | Previous Invoice Date                  | `date`      |     | ✅    |                                        |
| `rating_ids`                     | Ratings                                | `one2many`  |     | ✅    | rating.rating                          |
| `route_id`                       | Route                                  | `many2one`  | ✅  | ✅    | op.route                               |
| `route_register_id`              | Route Register                         | `many2one`  | ✅  | ✅    | op.route.register                      |
| `state`                          | State                                  | `selection` |     | ✅    |                                        |
| `stop_id`                        | Stop                                   | `many2one`  | ✅  | ✅    | op.stop                                |
| `transportation_fees_detail_ids` | Transportation Fees Collection Details | `one2many`  |     | ✅    | op.partner.transportation.fees.details |
| `website_message_ids`            | Website Messages                       | `one2many`  |     | ✅    | mail.message                           |
| `write_date`                     | Last Updated on                        | `datetime`  |     | ✅    |                                        |
| `write_uid`                      | Last Updated by                        | `many2one`  |     | ✅    | res.users                              |

**Access Rights:**

| Name                                                 | Group                              | Perms     |
| ---------------------------------------------------- | ---------------------------------- | --------- |
| access_op_transportation_agreement_transport_manager | Transportation Privilege / Manager | `R/W/C/D` |

**Record Rules:**

- **transportation enterprise multi comp rule** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.route.line` — Transportation Route Line

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation           |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ------------------ |
| `active`                     | Active                 | `boolean`   |     | ✅    |                    |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company        |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                    |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users          |
| `display_name`               | Display Name           | `char`      |     |       |                    |
| `driver_id`                  | Driver                 | `many2one`  | ✅  |       | res.partner        |
| `has_message`                | Has Message            | `boolean`   |     |       |                    |
| `id`                         | ID                     | `integer`   |     | ✅    |                    |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                    |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                    |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                    |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                    |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                    |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                    |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                    |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner        |
| `name`                       | Name                   | `char`      |     | ✅    |                    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating      |
| `route_date`                 | Date                   | `date`      | ✅  | ✅    |                    |
| `route_id`                   | Route                  | `many2one`  | ✅  | ✅    | op.route           |
| `route_passenger_ids`        | Passenger              | `one2many`  |     | ✅    | op.route.passenger |
| `route_stop_ids`             | Stops                  | `one2many`  |     | ✅    | op.route.stop.line |
| `route_type`                 | Route Type             | `selection` | ✅  | ✅    |                    |
| `start_time`                 | Start Time             | `float`     | ✅  | ✅    |                    |
| `state`                      | State                  | `selection` |     | ✅    |                    |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message       |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                    |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                 | Group                              | Perms     |
| ------------------------------------ | ---------------------------------- | --------- |
| name_op_route_line_transport_manager | Transportation Privilege / Manager | `R/W/C/D` |
| name_op_route_line_transport_user    | Transportation Privilege / User    | `R/W/C`   |

**Record Rules:**

- **Route line multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

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

### 🗃️ `op.partner.transportation.fees.details` — Partner Transportation Fees Details

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label               | Type        | Req | Store | Relation                    |
| --------------- | ------------------- | ----------- | --- | ----- | --------------------------- |
| `agreement_id`  | Transport Agreement | `many2one`  |     | ✅    | op.transportation.agreement |
| `amount`        | Fees Amount         | `monetary`  |     | ✅    |                             |
| `company_id`    | Company             | `many2one`  |     | ✅    | res.company                 |
| `create_date`   | Created on          | `datetime`  |     | ✅    |                             |
| `create_uid`    | Created by          | `many2one`  |     | ✅    | res.users                   |
| `currency_id`   | Currency            | `many2one`  |     |       | res.currency                |
| `date`          | Submit Date         | `date`      |     | ✅    |                             |
| `display_name`  | Display Name        | `char`      |     |       |                             |
| `id`            | ID                  | `integer`   |     | ✅    |                             |
| `invoice_id`    | Invoice ID          | `many2one`  |     | ✅    | account.move                |
| `invoice_state` | Invoice             | `selection` |     |       |                             |
| `product_id`    | Product             | `many2one`  |     | ✅    | product.product             |
| `state`         | State               | `selection` |     | ✅    |                             |
| `write_date`    | Last Updated on     | `datetime`  |     | ✅    |                             |
| `write_uid`     | Last Updated by     | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                                                            | Group                              | Perms     |
| --------------------------------------------------------------- | ---------------------------------- | --------- |
| access_op_partner_transportation_fees_details_transport_manager | Transportation Privilege / Manager | `R/W/C/D` |

### 🗃️ `op.route.register` — Route Register

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label                    | Type        | Req | Store | Relation                    |
| ----------------- | ------------------------ | ----------- | --- | ----- | --------------------------- |
| `color`           | Color Index              | `integer`   |     | ✅    |                             |
| `cost`            | Cost                     | `float`     |     | ✅    |                             |
| `create_date`     | Created on               | `datetime`  |     | ✅    |                             |
| `create_uid`      | Created by               | `many2one`  |     | ✅    | res.users                   |
| `display_name`    | Display Name             | `char`      |     |       |                             |
| `end_date`        | End Date                 | `date`      | ✅  | ✅    |                             |
| `id`              | ID                       | `integer`   |     | ✅    |                             |
| `name`            | Name                     | `char`      | ✅  | ✅    |                             |
| `plan_id`         | Plan                     | `many2one`  |     | ✅    | cost.plan                   |
| `product_id`      | Product                  | `many2one`  | ✅  | ✅    | product.product             |
| `route_id`        | Route                    | `many2one`  | ✅  | ✅    | op.route                    |
| `start_date`      | Start Date               | `date`      | ✅  | ✅    |                             |
| `state`           | Status                   | `selection` |     | ✅    |                             |
| `student_count`   | Student Count            | `integer`   |     |       |                             |
| `transport_lines` | Transportation Agreement | `one2many`  |     | ✅    | op.transportation.agreement |
| `write_date`      | Last Updated on          | `datetime`  |     | ✅    |                             |
| `write_uid`       | Last Updated by          | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                                       | Group                              | Perms     |
| ------------------------------------------ | ---------------------------------- | --------- |
| access_op_route_register_transport_manager | Transportation Privilege / Manager | `R/W/C/D` |

**Record Rules:**

- **Route Register multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('route_id.company_id','=',False),'&',('route_id.company_id','in',company_ids),'|',('route_id.company_id','child_of',[user.company_id.id]),('route_id.company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.route` — Transportation Route

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation        |
| -------------- | --------------- | ---------- | --- | ----- | --------------- |
| `active`       | Active          | `boolean`  |     | ✅    |                 |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company     |
| `cost`         | Cost            | `float`    |     | ✅    |                 |
| `create_date`  | Created on      | `datetime` |     | ✅    |                 |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users       |
| `display_name` | Display Name    | `char`     |     |       |                 |
| `id`           | ID              | `integer`  |     | ✅    |                 |
| `name`         | Name            | `char`     | ✅  | ✅    |                 |
| `product_id`   | Product         | `many2one` |     | ✅    | product.product |
| `stop_ids`     | Stops           | `one2many` |     | ✅    | op.stop         |
| `vehicle_id`   | Vehicle         | `many2one` | ✅  | ✅    | op.vehicle      |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                 |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                            | Group                              | Perms     |
| ------------------------------- | ---------------------------------- | --------- |
| name_op_route_transport_manager | Transportation Privilege / Manager | `R/W/C/D` |
| name_op_route_transport_user    | Transportation Privilege / User    | `R/W`     |

**Record Rules:**

- **Transportation multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.route.passenger` — Transportation Route Passenger

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label           | Type       | Req | Store | Relation      |
| --------------- | --------------- | ---------- | --- | ----- | ------------- |
| `company_id`    | Company         | `many2one` |     | ✅    | res.company   |
| `create_date`   | Created on      | `datetime` |     | ✅    |               |
| `create_uid`    | Created by      | `many2one` |     | ✅    | res.users     |
| `display_name`  | Display Name    | `char`     |     |       |               |
| `id`            | ID              | `integer`  |     | ✅    |               |
| `partner_id`    | Passenger       | `many2one` | ✅  | ✅    | res.partner   |
| `present`       | Present/Absent  | `boolean`  |     | ✅    |               |
| `route_line_id` | Route Line      | `many2one` | ✅  | ✅    | op.route.line |
| `stop_id`       | Stop            | `many2one` | ✅  | ✅    | op.stop       |
| `write_date`    | Last Updated on | `datetime` |     | ✅    |               |
| `write_uid`     | Last Updated by | `many2one` |     | ✅    | res.users     |

**Access Rights:**

| Name                                      | Group                              | Perms     |
| ----------------------------------------- | ---------------------------------- | --------- |
| name_op_route_passenger_transport_manager | Transportation Privilege / Manager | `R/W/C/D` |
| name_op_route_passenger_transport_user    | Transportation Privilege / User    | `R/W/C`   |

**Record Rules:**

- **Route Passenger multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.route.stop.line` — Transportation Route Stop Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label             | Type       | Req | Store | Relation      |
| ---------------- | ----------------- | ---------- | --- | ----- | ------------- |
| `company_id`     | Company           | `many2one` |     | ✅    | res.company   |
| `create_date`    | Created on        | `datetime` |     | ✅    |               |
| `create_uid`     | Created by        | `many2one` |     | ✅    | res.users     |
| `display_name`   | Display Name      | `char`     |     |       |               |
| `estimated_time` | Estimated Arrival | `float`    |     |       |               |
| `id`             | ID                | `integer`  |     | ✅    |               |
| `route_line_id`  | Route Line        | `many2one` |     | ✅    | op.route.line |
| `sequence`       | Sequence          | `integer`  |     |       |               |
| `stop_id`        | Stop              | `many2one` |     | ✅    | op.stop       |
| `write_date`     | Last Updated on   | `datetime` |     | ✅    |               |
| `write_uid`      | Last Updated by   | `many2one` |     | ✅    | res.users     |

**Access Rights:**

| Name                                      | Group                              | Perms     |
| ----------------------------------------- | ---------------------------------- | --------- |
| name_op_route_stop_line_transport_manager | Transportation Privilege / Manager | `R/W/C/D` |
| name_op_route_stop_line_transport_user    | Transportation Privilege / User    | `R/W/C`   |

**Record Rules:**

- **Route stop line multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.stop` — Transportation Stop

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                    | Label                  | Type        | Req | Store | Relation    |
| ------------------------ | ---------------------- | ----------- | --- | ----- | ----------- |
| `active`                 | Active                 | `boolean`   |     | ✅    |             |
| `company_id`             | Company                | `many2one`  |     | ✅    | res.company |
| `create_date`            | Created on             | `datetime`  |     | ✅    |             |
| `create_uid`             | Created by             | `many2one`  |     | ✅    | res.users   |
| `display_name`           | Display Name           | `char`      |     |       |             |
| `estimated_arrival_conf` | Estimated Arrival Time | `float`     |     | ✅    |             |
| `id`                     | ID                     | `integer`   |     | ✅    |             |
| `name`                   | Name                   | `char`      | ✅  | ✅    |             |
| `partner_ids`            | Person(s)              | `many2many` |     | ✅    | res.partner |
| `route_id`               | Route                  | `many2one`  | ✅  | ✅    | op.route    |
| `sequence`               | Sequence               | `integer`   |     | ✅    |             |
| `write_date`             | Last Updated on        | `datetime`  |     | ✅    |             |
| `write_uid`              | Last Updated by        | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                           | Group                              | Perms     |
| ------------------------------ | ---------------------------------- | --------- |
| name_op_stop_transport_manager | Transportation Privilege / Manager | `R/W/C/D` |
| name_op_stop_transport_user    | Transportation Privilege / User    | `R/W`     |

**Record Rules:**

- **Stop multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.vehicle` — Transportation Vehicle

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type         | Req | Store | Relation                      |
| ------------------------------- | ----------------------------- | ------------ | --- | ----- | ----------------------------- |
| `account_move_ids`              | Account Move                  | `one2many`   |     |       | account.move                  |
| `acquisition_date`              | Registration Date             | `date`       |     |       |                               |
| `active`                        | Active                        | `boolean`    |     | ✅    |                               |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`   |     |       | calendar.event                |
| `activity_date_deadline`        | Next Activity Deadline        | `date`       |     |       |                               |
| `activity_exception_decoration` | Activity Exception Decoration | `selection`  |     |       |                               |
| `activity_exception_icon`       | Icon                          | `char`       |     |       |                               |
| `activity_ids`                  | Activities                    | `one2many`   |     |       | mail.activity                 |
| `activity_state`                | Activity State                | `selection`  |     |       |                               |
| `activity_summary`              | Next Activity Summary         | `char`       |     |       |                               |
| `activity_type_icon`            | Activity Type Icon            | `char`       |     |       |                               |
| `activity_type_id`              | Next Activity Type            | `many2one`   |     |       | mail.activity.type            |
| `activity_user_id`              | Responsible User              | `many2one`   |     |       | res.users                     |
| `avatar_1024`                   | Avatar 1024                   | `binary`     |     |       |                               |
| `avatar_128`                    | Avatar 128                    | `binary`     |     |       |                               |
| `avatar_1920`                   | Avatar                        | `binary`     |     |       |                               |
| `avatar_256`                    | Avatar 256                    | `binary`     |     |       |                               |
| `avatar_512`                    | Avatar 512                    | `binary`     |     |       |                               |
| `bill_count`                    | Bills Count                   | `integer`    |     |       |                               |
| `brand_id`                      | Brand                         | `many2one`   |     |       | fleet.vehicle.model.brand     |
| `capacity`                      | Capacity                      | `integer`    | ✅  | ✅    |                               |
| `car_value`                     | Catalog Value (VAT Incl.)     | `float`      |     |       |                               |
| `category_id`                   | Category                      | `many2one`   |     |       | fleet.vehicle.model.category  |
| `co2`                           | CO₂ Emissions                 | `float`      |     |       |                               |
| `co2_emission_unit`             | Co2 Emission Unit             | `selection`  | ✅  |       |                               |
| `co2_standard`                  | Emission Standard             | `char`       |     |       |                               |
| `color`                         | Color                         | `char`       |     |       |                               |
| `company_id`                    | Company                       | `many2one`   |     | ✅    | res.company                   |
| `contract_count`                | Contract Count                | `integer`    |     |       |                               |
| `contract_date_start`           | First Contract Date           | `date`       |     |       |                               |
| `contract_renewal_due_soon`     | Has Contracts to renew        | `boolean`    |     |       |                               |
| `contract_renewal_overdue`      | Has Contracts Overdue         | `boolean`    |     |       |                               |
| `contract_state`                | Last Contract State           | `selection`  |     |       |                               |
| `country_code`                  | Country Code                  | `char`       |     |       |                               |
| `country_id`                    | Country                       | `many2one`   |     |       | res.country                   |
| `create_date`                   | Created on                    | `datetime`   |     | ✅    |                               |
| `create_uid`                    | Created by                    | `many2one`   |     | ✅    | res.users                     |
| `currency_id`                   | Currency                      | `many2one`   |     |       | res.currency                  |
| `description`                   | Vehicle Description           | `html`       |     |       |                               |
| `display_name`                  | Display Name                  | `char`       |     |       |                               |
| `doors`                         | Number of Doors               | `integer`    |     |       |                               |
| `driver_employee_id`            | Driver (Employee)             | `many2one`   |     |       | hr.employee                   |
| `driver_employee_name`          | Employee Name                 | `char`       |     |       |                               |
| `driver_id`                     | Driver                        | `many2one`   |     |       | res.partner                   |
| `electric_assistance`           | Electric Assistance           | `boolean`    |     |       |                               |
| `frame_size`                    | Frame Size                    | `float`      |     |       |                               |
| `frame_type`                    | Bike Frame Type               | `selection`  |     |       |                               |
| `fuel_type`                     | Fuel Type                     | `selection`  |     |       |                               |
| `future_driver_employee_id`     | Future Driver (Employee)      | `many2one`   |     |       | hr.employee                   |
| `future_driver_id`              | Future Driver                 | `many2one`   |     |       | res.partner                   |
| `has_message`                   | Has Message                   | `boolean`    |     |       |                               |
| `history_count`                 | Drivers History Count         | `integer`    |     |       |                               |
| `horsepower`                    | Horsepower                    | `float`      |     |       |                               |
| `horsepower_tax`                | Horsepower Taxation           | `float`      |     |       |                               |
| `id`                            | ID                            | `integer`    |     | ✅    |                               |
| `image_1024`                    | Image 1024                    | `binary`     |     |       |                               |
| `image_128`                     | Image 128                     | `binary`     |     |       |                               |
| `image_1920`                    | Image                         | `binary`     |     |       |                               |
| `image_256`                     | Image 256                     | `binary`     |     |       |                               |
| `image_512`                     | Image 512                     | `binary`     |     |       |                               |
| `license_plate`                 | License Plate                 | `char`       |     |       |                               |
| `location`                      | Location                      | `char`       |     |       |                               |
| `log_contracts`                 | Contracts                     | `one2many`   |     |       | fleet.vehicle.log.contract    |
| `log_drivers`                   | Assignment Logs               | `one2many`   |     |       | fleet.vehicle.assignation.log |
| `log_services`                  | Services Logs                 | `one2many`   |     |       | fleet.vehicle.log.services    |
| `manager_id`                    | Fleet Manager                 | `many2one`   |     |       | res.users                     |
| `message_attachment_count`      | Attachment Count              | `integer`    |     |       |                               |
| `message_follower_ids`          | Followers                     | `one2many`   |     |       | mail.followers                |
| `message_has_error`             | Message Delivery error        | `boolean`    |     |       |                               |
| `message_has_error_counter`     | Number of errors              | `integer`    |     |       |                               |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`    |     |       |                               |
| `message_ids`                   | Messages                      | `one2many`   |     |       | mail.message                  |
| `message_is_follower`           | Is Follower                   | `boolean`    |     |       |                               |
| `message_needaction`            | Action Needed                 | `boolean`    |     |       |                               |
| `message_needaction_counter`    | Number of Actions             | `integer`    |     |       |                               |
| `message_partner_ids`           | Followers (Partners)          | `many2many`  |     |       | res.partner                   |
| `mobility_card`                 | Mobility Card                 | `char`       |     |       |                               |
| `model_id`                      | Model                         | `many2one`   | ✅  |       | fleet.vehicle.model           |
| `model_year`                    | Model Year                    | `selection`  |     |       |                               |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`       |     |       |                               |
| `name`                          | Name                          | `char`       |     |       |                               |
| `net_car_value`                 | Purchase Value                | `float`      |     |       |                               |
| `next_assignation_date`         | Assignment Date               | `date`       |     |       |                               |
| `odometer`                      | Last Odometer                 | `float`      |     |       |                               |
| `odometer_count`                | Odometer                      | `integer`    |     |       |                               |
| `odometer_unit`                 | Odometer Unit                 | `selection`  | ✅  |       |                               |
| `order_date`                    | Order Date                    | `date`       |     |       |                               |
| `plan_to_change_bike`           | Plan To Change Bike           | `boolean`    |     |       |                               |
| `plan_to_change_car`            | Plan To Change Car            | `boolean`    |     |       |                               |
| `power`                         | Power                         | `float`      |     |       |                               |
| `power_unit`                    | Power Unit                    | `selection`  | ✅  |       |                               |
| `range_unit`                    | Range Unit                    | `selection`  | ✅  |       |                               |
| `rating_ids`                    | Ratings                       | `one2many`   |     |       | rating.rating                 |
| `residual_value`                | Residual Value                | `float`      |     |       |                               |
| `seats`                         | Seating Capacity              | `integer`    |     |       |                               |
| `service_activity`              | Service Activity              | `selection`  |     |       |                               |
| `service_count`                 | Services                      | `integer`    |     |       |                               |
| `state_id`                      | State                         | `many2one`   |     |       | fleet.vehicle.state           |
| `tag_ids`                       | Tags                          | `many2many`  |     |       | fleet.vehicle.tag             |
| `trailer_hook`                  | Trailer Hitch                 | `boolean`    |     |       |                               |
| `transmission`                  | Transmission                  | `selection`  |     |       |                               |
| `vehicle_id`                    | Vehicle                       | `many2one`   | ✅  | ✅    | fleet.vehicle                 |
| `vehicle_properties`            | Properties                    | `properties` |     |       |                               |
| `vehicle_range`                 | Range                         | `integer`    |     |       |                               |
| `vehicle_type`                  | Vehicle Type                  | `selection`  |     |       |                               |
| `vin_sn`                        | Chassis Number                | `char`       |     |       |                               |
| `website_message_ids`           | Website Messages              | `one2many`   |     |       | mail.message                  |
| `write_date`                    | Last Updated on               | `datetime`   |     | ✅    |                               |
| `write_off_date`                | Cancellation Date             | `date`       |     |       |                               |
| `write_uid`                     | Last Updated by               | `many2one`   |     | ✅    | res.users                     |

**Access Rights:**

| Name                              | Group                              | Perms     |
| --------------------------------- | ---------------------------------- | --------- |
| name_op_vehicle_transport_manager | Transportation Privilege / Manager | `R/W/C/D` |
| name_op_vehicle_transport_user    | Transportation Privilege / User    | `R/W`     |

**Record Rules:**

- **Vehicle multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `
