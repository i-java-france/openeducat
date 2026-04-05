---
title: "Fleet"
module: "fleet"
state: "installed"
version: "19.0.0.1"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/app/fleet"
license: "LGPL-3"
category: "Fleet"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_____, odoo/app]
---

# 🟢 Fleet

> **Module:** `fleet` | **Version:** `19.0.0.1` **Category:** Fleet | **License:**
> `LGPL-3` **Author:** Odoo S.A. **Website:** https://www.odoo.com/app/fleet

## 🔗 Dependencies

[[base]] [[mail]]

## 📖 Description

# Vehicle, leasing, insurances, cost

With this module, Odoo helps you managing all your vehicles, the contracts associated to
those vehicle as well as services, costs and many other features necessary to the
management of your fleet of vehicle(s)

## Main Features

- Add vehicles to your fleet
- Manage contracts for vehicles
- Reminder when a contract reach its expiration date
- Add services, odometer values for all vehicles
- Show all costs associated to a vehicle or to a type of service
- Analysis graph for costs

## 🖥️ UI Components

### Menus

- `Fleet`
- `Fleet/Configuration`
- `Fleet/Configuration/Activity Types`
- `Fleet/Configuration/Models`
- `Fleet/Configuration/Models/Categories`
- `Fleet/Configuration/Models/Manufacturers`
- `Fleet/Configuration/Models/Models`
- `Fleet/Configuration/Services`
- `Fleet/Configuration/Services/Types`
- `Fleet/Configuration/Settings`
- `Fleet/Configuration/Vehicle`
- `Fleet/Configuration/Vehicle/Status`
- `Fleet/Configuration/Vehicle/Tags`
- `Fleet/Fleet`
- `Fleet/Fleet/Contracts`
- `Fleet/Fleet/Fleet`
- `Fleet/Fleet/Odometers`
- `Fleet/Fleet/Services`
- `Fleet/Reporting`
- `Fleet/Reporting/Costs`
- `Fleet/Reporting/Odometers`

### Views

- `* INHERIT res.config.settings.view.form.inherit.hr.fleet (form)`
- `fleet.service.type search (search)`
- `fleet.service.type.list (list)`
- `fleet.vehicle pivot (pivot)`
- `fleet.vehicle.activity (activity)`
- `fleet.vehicle.assignation.log.view.list (list)`
- `fleet.vehicle.cost.report.form (form)`
- `fleet.vehicle.cost.report.view.list (list)`
- `fleet.vehicle.cost.view.graph (graph)`
- `fleet.vehicle.cost.view.pivot (pivot)`
- `fleet.vehicle.cost.view.search (search)`
- `fleet.vehicle.form (form)`
- `fleet.vehicle.form.quick.create (form)`
- `fleet.vehicle.kanban (kanban)`
- `fleet.vehicle.list (list)`
- `fleet.vehicle.log.contract pivot (pivot)`
- `fleet.vehicle.log.contract.activity (activity)`
- `fleet.vehicle.log.contract.graph (graph)`
- `fleet.vehicle.log.contract.kanban (kanban)`
- `fleet.vehicle.log.contract.list (list)`
- `fleet.vehicle.log.contract.search (search)`
- `fleet.vehicle.log.services activity (activity)`
- `fleet.vehicle.log.services pivot (pivot)`
- `fleet.vehicle.log.services.form (form)`
- `fleet.vehicle.log.services.graph (graph)`
- `fleet.vehicle.log.services.kanban (kanban)`
- `fleet.vehicle.log.services.list (list)`
- `fleet.vehicle.log.services.search (search)`
- `fleet.vehicle.log_contract.form (form)`
- `fleet.vehicle.model.brand.form (form)`
- `fleet.vehicle.model.brand.list (list)`
- `fleet.vehicle.model.brand.view.search (search)`
- `fleet.vehicle.model.brandkanban (kanban)`
- `fleet.vehicle.model.category.view.form (form)`
- `fleet.vehicle.model.category.view.list (list)`
- `fleet.vehicle.model.form (form)`
- `fleet.vehicle.model.kanban (kanban)`
- `fleet.vehicle.model.list (list)`
- `fleet.vehicle.model.search (search)`
- `fleet.vehicle.odometer.form (form)`
- `fleet.vehicle.odometer.graph (graph)`
- `fleet.vehicle.odometer.list (list)`
- `fleet.vehicle.odometer.report.view.graph (graph)`
- `fleet.vehicle.odometer.report.view.search (search)`
- `fleet.vehicle.odometer.search (search)`
- `fleet.vehicle.search (search)`
- `fleet.vehicle.send.mail form (form)`
- `fleet.vehicle.state.form (form)`
- `fleet.vehicle.state.list (list)`
- `fleet.vehicle.tag.form (form)`
- `fleet.vehicle.tag.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**16 model(s) defined by this module:**

### 🗃️ `fleet.vehicle.model` — Model of a vehicle

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type                    | Req | Store | Relation                     |
| ------------------------------- | ----------------------------- | ----------------------- | --- | ----- | ---------------------------- |
| `active`                        | Active                        | `boolean`               |     | ✅    |                              |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`              |     |       | calendar.event               |
| `activity_date_deadline`        | Next Activity Deadline        | `date`                  |     |       |                              |
| `activity_exception_decoration` | Activity Exception Decoration | `selection`             |     |       |                              |
| `activity_exception_icon`       | Icon                          | `char`                  |     |       |                              |
| `activity_ids`                  | Activities                    | `one2many`              |     | ✅    | mail.activity                |
| `activity_state`                | Activity State                | `selection`             |     |       |                              |
| `activity_summary`              | Next Activity Summary         | `char`                  |     |       |                              |
| `activity_type_icon`            | Activity Type Icon            | `char`                  |     |       |                              |
| `activity_type_id`              | Next Activity Type            | `many2one`              |     |       | mail.activity.type           |
| `activity_user_id`              | Responsible User              | `many2one`              |     |       | res.users                    |
| `avatar_1024`                   | Avatar 1024                   | `binary`                |     |       |                              |
| `avatar_128`                    | Avatar 128                    | `binary`                |     |       |                              |
| `avatar_1920`                   | Avatar                        | `binary`                |     |       |                              |
| `avatar_256`                    | Avatar 256                    | `binary`                |     |       |                              |
| `avatar_512`                    | Avatar 512                    | `binary`                |     |       |                              |
| `brand_id`                      | Manufacturer                  | `many2one`              | ✅  | ✅    | fleet.vehicle.model.brand    |
| `category_id`                   | Category                      | `many2one`              |     | ✅    | fleet.vehicle.model.category |
| `co2_emission_unit`             | Co2 Emission Unit             | `selection`             | ✅  |       |                              |
| `co2_standard`                  | Emission Standard             | `char`                  |     | ✅    |                              |
| `color`                         | Color                         | `char`                  |     | ✅    |                              |
| `create_date`                   | Created on                    | `datetime`              |     | ✅    |                              |
| `create_uid`                    | Created by                    | `many2one`              |     | ✅    | res.users                    |
| `default_co2`                   | CO₂ Emissions                 | `float`                 |     | ✅    |                              |
| `default_fuel_type`             | Fuel Type                     | `selection`             |     | ✅    |                              |
| `display_name`                  | Display Name                  | `char`                  |     |       |                              |
| `doors`                         | Number of Doors               | `integer`               |     | ✅    |                              |
| `drive_type`                    | Drive Type                    | `selection`             |     | ✅    |                              |
| `electric_assistance`           | Electric Assistance           | `boolean`               |     | ✅    |                              |
| `has_message`                   | Has Message                   | `boolean`               |     |       |                              |
| `horsepower`                    | Horsepower                    | `float`                 |     | ✅    |                              |
| `horsepower_tax`                | Horsepower Taxation           | `float`                 |     | ✅    |                              |
| `id`                            | ID                            | `integer`               |     | ✅    |                              |
| `image_1024`                    | Image 1024                    | `binary`                |     | ✅    |                              |
| `image_128`                     | Image 128                     | `binary`                |     | ✅    |                              |
| `image_1920`                    | Image                         | `binary`                |     | ✅    |                              |
| `image_256`                     | Image 256                     | `binary`                |     | ✅    |                              |
| `image_512`                     | Image 512                     | `binary`                |     | ✅    |                              |
| `message_attachment_count`      | Attachment Count              | `integer`               |     |       |                              |
| `message_follower_ids`          | Followers                     | `one2many`              |     | ✅    | mail.followers               |
| `message_has_error`             | Message Delivery error        | `boolean`               |     |       |                              |
| `message_has_error_counter`     | Number of errors              | `integer`               |     |       |                              |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`               |     |       |                              |
| `message_ids`                   | Messages                      | `one2many`              |     | ✅    | mail.message                 |
| `message_is_follower`           | Is Follower                   | `boolean`               |     |       |                              |
| `message_needaction`            | Action Needed                 | `boolean`               |     |       |                              |
| `message_needaction_counter`    | Number of Actions             | `integer`               |     |       |                              |
| `message_partner_ids`           | Followers (Partners)          | `many2many`             |     |       | res.partner                  |
| `model_year`                    | Model Year                    | `selection`             |     | ✅    |                              |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`                  |     |       |                              |
| `name`                          | Model name                    | `char`                  | ✅  | ✅    |                              |
| `power`                         | Power                         | `float`                 |     | ✅    |                              |
| `power_unit`                    | Power Unit                    | `selection`             | ✅  | ✅    |                              |
| `range_unit`                    | Range Unit                    | `selection`             | ✅  | ✅    |                              |
| `rating_ids`                    | Ratings                       | `one2many`              |     | ✅    | rating.rating                |
| `seats`                         | Seating Capacity              | `integer`               |     | ✅    |                              |
| `trailer_hook`                  | Trailer Hitch                 | `boolean`               |     | ✅    |                              |
| `transmission`                  | Transmission                  | `selection`             |     | ✅    |                              |
| `vehicle_count`                 | Vehicle Count                 | `integer`               |     |       |                              |
| `vehicle_properties_definition` | Vehicle Properties            | `properties_definition` |     | ✅    |                              |
| `vehicle_range`                 | Range                         | `integer`               |     | ✅    |                              |
| `vehicle_type`                  | Vehicle Type                  | `selection`             | ✅  | ✅    |                              |
| `vendors`                       | Vendors                       | `many2many`             |     | ✅    | res.partner                  |
| `website_message_ids`           | Website Messages              | `one2many`              |     | ✅    | mail.message                 |
| `write_date`                    | Last Updated on               | `datetime`              |     | ✅    |                              |
| `write_uid`                     | Last Updated by               | `many2one`              |     | ✅    | res.users                    |

**Access Rights:**

| Name                             | Group                                | Perms     |
| -------------------------------- | ------------------------------------ | --------- |
| fleet_vehicle_model_access_right | Fleet / Officer: Manage all vehicles | `R`       |
| fleet_vehicle_model_access_right | Fleet / Administrator                | `R/W/C/D` |

### 🗃️ `fleet.vehicle.log.services` — Services for vehicles

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                  |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------- |
| `account_move_line_id`          | Account Move Line             | `many2one`  |     | ✅    | account.move.line         |
| `account_move_state`            | Status                        | `selection` |     |       |                           |
| `active`                        | Active                        | `boolean`   |     | ✅    |                           |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event            |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                           |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                           |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                           |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity             |
| `activity_state`                | Activity State                | `selection` |     |       |                           |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                           |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                           |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type        |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users                 |
| `amount`                        | Cost                          | `monetary`  |     | ✅    |                           |
| `brand_id`                      | Brand                         | `many2one`  |     | ✅    | fleet.vehicle.model.brand |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company               |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                           |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users                 |
| `currency_id`                   | Currency                      | `many2one`  |     |       | res.currency              |
| `date`                          | Date                          | `date`      |     | ✅    |                           |
| `description`                   | Description                   | `char`      |     | ✅    |                           |
| `display_name`                  | Display Name                  | `char`      |     |       |                           |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                           |
| `id`                            | ID                            | `integer`   |     | ✅    |                           |
| `inv_ref`                       | Vendor Reference              | `char`      |     | ✅    |                           |
| `manager_id`                    | Fleet Manager                 | `many2one`  |     | ✅    | res.users                 |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                           |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers            |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                           |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                           |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                           |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message              |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                           |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                           |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                           |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner               |
| `model_id`                      | Model                         | `many2one`  |     | ✅    | fleet.vehicle.model       |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                           |
| `notes`                         | Notes                         | `text`      |     | ✅    |                           |
| `odometer`                      | Odometer Value                | `float`     |     |       |                           |
| `odometer_id`                   | Odometer                      | `many2one`  |     | ✅    | fleet.vehicle.odometer    |
| `odometer_unit`                 | Unit                          | `selection` |     |       |                           |
| `purchaser_employee_id`         | Driver (Employee)             | `many2one`  |     | ✅    | hr.employee               |
| `purchaser_id`                  | Driver                        | `many2one`  |     | ✅    | res.partner               |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating             |
| `service_type_id`               | Service Type                  | `many2one`  | ✅  | ✅    | fleet.service.type        |
| `state`                         | Stage                         | `selection` |     | ✅    |                           |
| `vehicle_id`                    | Vehicle                       | `many2one`  | ✅  | ✅    | fleet.vehicle             |
| `vendor_id`                     | Vendor                        | `many2one`  |     | ✅    | res.partner               |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message              |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                           |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name                                    | Group                                | Perms     |
| --------------------------------------- | ------------------------------------ | --------- |
| fleet_vehicle_log_services_access_right | Fleet / Officer: Manage all vehicles | `R`       |
| fleet_vehicle_log_services_access_right | Fleet / Administrator                | `R/W/C/D` |

**Record Rules:**

- **Administrator has all rights on vehicle's services** (21) `R/W/C/D`
- **Fleet log services: Multi Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `fleet.vehicle` — Vehicle

> 📧 Mail Thread

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
| `acquisition_date`              | Registration Date             | `date`       |     | ✅    |                               |
| `active`                        | Active                        | `boolean`    |     | ✅    |                               |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`   |     |       | calendar.event                |
| `activity_date_deadline`        | Next Activity Deadline        | `date`       |     |       |                               |
| `activity_exception_decoration` | Activity Exception Decoration | `selection`  |     |       |                               |
| `activity_exception_icon`       | Icon                          | `char`       |     |       |                               |
| `activity_ids`                  | Activities                    | `one2many`   |     | ✅    | mail.activity                 |
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
| `brand_id`                      | Brand                         | `many2one`   |     | ✅    | fleet.vehicle.model.brand     |
| `car_value`                     | Catalog Value (VAT Incl.)     | `float`      |     | ✅    |                               |
| `category_id`                   | Category                      | `many2one`   |     | ✅    | fleet.vehicle.model.category  |
| `co2`                           | CO₂ Emissions                 | `float`      |     | ✅    |                               |
| `co2_emission_unit`             | Co2 Emission Unit             | `selection`  | ✅  | ✅    |                               |
| `co2_standard`                  | Emission Standard             | `char`       |     | ✅    |                               |
| `color`                         | Color                         | `char`       |     | ✅    |                               |
| `company_id`                    | Company                       | `many2one`   |     | ✅    | res.company                   |
| `contract_count`                | Contract Count                | `integer`    |     |       |                               |
| `contract_date_start`           | First Contract Date           | `date`       |     | ✅    |                               |
| `contract_renewal_due_soon`     | Has Contracts to renew        | `boolean`    |     |       |                               |
| `contract_renewal_overdue`      | Has Contracts Overdue         | `boolean`    |     |       |                               |
| `contract_state`                | Last Contract State           | `selection`  |     |       |                               |
| `country_code`                  | Country Code                  | `char`       |     |       |                               |
| `country_id`                    | Country                       | `many2one`   |     |       | res.country                   |
| `create_date`                   | Created on                    | `datetime`   |     | ✅    |                               |
| `create_uid`                    | Created by                    | `many2one`   |     | ✅    | res.users                     |
| `currency_id`                   | Currency                      | `many2one`   |     |       | res.currency                  |
| `description`                   | Vehicle Description           | `html`       |     | ✅    |                               |
| `display_name`                  | Display Name                  | `char`       |     |       |                               |
| `doors`                         | Number of Doors               | `integer`    |     | ✅    |                               |
| `driver_employee_id`            | Driver (Employee)             | `many2one`   |     | ✅    | hr.employee                   |
| `driver_employee_name`          | Employee Name                 | `char`       |     |       |                               |
| `driver_id`                     | Driver                        | `many2one`   |     | ✅    | res.partner                   |
| `electric_assistance`           | Electric Assistance           | `boolean`    |     | ✅    |                               |
| `frame_size`                    | Frame Size                    | `float`      |     | ✅    |                               |
| `frame_type`                    | Bike Frame Type               | `selection`  |     | ✅    |                               |
| `fuel_type`                     | Fuel Type                     | `selection`  |     | ✅    |                               |
| `future_driver_employee_id`     | Future Driver (Employee)      | `many2one`   |     | ✅    | hr.employee                   |
| `future_driver_id`              | Future Driver                 | `many2one`   |     | ✅    | res.partner                   |
| `has_message`                   | Has Message                   | `boolean`    |     |       |                               |
| `history_count`                 | Drivers History Count         | `integer`    |     |       |                               |
| `horsepower`                    | Horsepower                    | `float`      |     | ✅    |                               |
| `horsepower_tax`                | Horsepower Taxation           | `float`      |     | ✅    |                               |
| `id`                            | ID                            | `integer`    |     | ✅    |                               |
| `image_1024`                    | Image 1024                    | `binary`     |     | ✅    |                               |
| `image_128`                     | Image 128                     | `binary`     |     | ✅    |                               |
| `image_1920`                    | Image                         | `binary`     |     | ✅    |                               |
| `image_256`                     | Image 256                     | `binary`     |     | ✅    |                               |
| `image_512`                     | Image 512                     | `binary`     |     | ✅    |                               |
| `license_plate`                 | License Plate                 | `char`       |     | ✅    |                               |
| `location`                      | Location                      | `char`       |     | ✅    |                               |
| `log_contracts`                 | Contracts                     | `one2many`   |     | ✅    | fleet.vehicle.log.contract    |
| `log_drivers`                   | Assignment Logs               | `one2many`   |     | ✅    | fleet.vehicle.assignation.log |
| `log_services`                  | Services Logs                 | `one2many`   |     | ✅    | fleet.vehicle.log.services    |
| `manager_id`                    | Fleet Manager                 | `many2one`   |     | ✅    | res.users                     |
| `message_attachment_count`      | Attachment Count              | `integer`    |     |       |                               |
| `message_follower_ids`          | Followers                     | `one2many`   |     | ✅    | mail.followers                |
| `message_has_error`             | Message Delivery error        | `boolean`    |     |       |                               |
| `message_has_error_counter`     | Number of errors              | `integer`    |     |       |                               |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`    |     |       |                               |
| `message_ids`                   | Messages                      | `one2many`   |     | ✅    | mail.message                  |
| `message_is_follower`           | Is Follower                   | `boolean`    |     |       |                               |
| `message_needaction`            | Action Needed                 | `boolean`    |     |       |                               |
| `message_needaction_counter`    | Number of Actions             | `integer`    |     |       |                               |
| `message_partner_ids`           | Followers (Partners)          | `many2many`  |     |       | res.partner                   |
| `mobility_card`                 | Mobility Card                 | `char`       |     | ✅    |                               |
| `model_id`                      | Model                         | `many2one`   | ✅  | ✅    | fleet.vehicle.model           |
| `model_year`                    | Model Year                    | `selection`  |     | ✅    |                               |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`       |     |       |                               |
| `name`                          | Name                          | `char`       |     | ✅    |                               |
| `net_car_value`                 | Purchase Value                | `float`      |     | ✅    |                               |
| `next_assignation_date`         | Assignment Date               | `date`       |     | ✅    |                               |
| `odometer`                      | Last Odometer                 | `float`      |     |       |                               |
| `odometer_count`                | Odometer                      | `integer`    |     |       |                               |
| `odometer_unit`                 | Odometer Unit                 | `selection`  | ✅  | ✅    |                               |
| `order_date`                    | Order Date                    | `date`       |     | ✅    |                               |
| `plan_to_change_bike`           | Plan To Change Bike           | `boolean`    |     | ✅    |                               |
| `plan_to_change_car`            | Plan To Change Car            | `boolean`    |     | ✅    |                               |
| `power`                         | Power                         | `float`      |     | ✅    |                               |
| `power_unit`                    | Power Unit                    | `selection`  | ✅  | ✅    |                               |
| `range_unit`                    | Range Unit                    | `selection`  | ✅  | ✅    |                               |
| `rating_ids`                    | Ratings                       | `one2many`   |     | ✅    | rating.rating                 |
| `residual_value`                | Residual Value                | `float`      |     | ✅    |                               |
| `seats`                         | Seating Capacity              | `integer`    |     | ✅    |                               |
| `service_activity`              | Service Activity              | `selection`  |     |       |                               |
| `service_count`                 | Services                      | `integer`    |     |       |                               |
| `state_id`                      | State                         | `many2one`   |     | ✅    | fleet.vehicle.state           |
| `tag_ids`                       | Tags                          | `many2many`  |     | ✅    | fleet.vehicle.tag             |
| `trailer_hook`                  | Trailer Hitch                 | `boolean`    |     | ✅    |                               |
| `transmission`                  | Transmission                  | `selection`  |     | ✅    |                               |
| `vehicle_properties`            | Properties                    | `properties` |     | ✅    |                               |
| `vehicle_range`                 | Range                         | `integer`    |     | ✅    |                               |
| `vehicle_type`                  | Vehicle Type                  | `selection`  |     |       |                               |
| `vin_sn`                        | Chassis Number                | `char`       |     | ✅    |                               |
| `website_message_ids`           | Website Messages              | `one2many`   |     | ✅    | mail.message                  |
| `write_date`                    | Last Updated on               | `datetime`   |     | ✅    |                               |
| `write_off_date`                | Cancellation Date             | `date`       |     | ✅    |                               |
| `write_uid`                     | Last Updated by               | `many2one`   |     | ✅    | res.users                     |

**Access Rights:**

| Name                                     | Group                                     | Perms     |
| ---------------------------------------- | ----------------------------------------- | --------- |
| hr_fleet_vehicle_access_right_hr_officer | Employees / Officer: Manage all employees | `R`       |
| fleet_vehicle_access_right               | Fleet / Officer: Manage all vehicles      | `R/W/C/D` |
| fleet_vehicle_access_right               | Fleet / Administrator                     | `R/W/C/D` |
| name_fleet_vehicle_transport_user        | Transportation Privilege / User           | `R`       |

**Record Rules:**

- **Administrator has all rights on vehicle** (21) `R/W/C/D`
- **Fleet vehicle: Multi Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Hr Officer read rights on vehicle with employees assigned** (49) `R`
  - Domain:
    `['|', ('driver_employee_id', '!=', False), ('future_driver_employee_id', '!=', False)]`

### 🗃️ `fleet.vehicle.log.contract` — Vehicle Contract

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
| `amount`                        | Cost                          | `monetary`  |     | ✅    |                    |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company        |
| `cost_frequency`                | Recurring Cost Frequency      | `selection` | ✅  | ✅    |                    |
| `cost_generated`                | Recurring Cost                | `monetary`  |     | ✅    |                    |
| `cost_subtype_id`               | Type                          | `many2one`  |     | ✅    | fleet.service.type |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `currency_id`                   | Currency                      | `many2one`  |     |       | res.currency       |
| `date`                          | Date                          | `date`      |     | ✅    |                    |
| `days_left`                     | Warning Date                  | `integer`   |     |       |                    |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `expiration_date`               | Contract Expiration Date      | `date`      |     | ✅    |                    |
| `expires_today`                 | Expires Today                 | `boolean`   |     |       |                    |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `has_open_contract`             | Has Open Contract             | `boolean`   |     |       |                    |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
| `ins_ref`                       | Reference                     | `char`      |     | ✅    |                    |
| `insurer_id`                    | Vendor                        | `many2one`  |     | ✅    | res.partner        |
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
| `name`                          | Name                          | `char`      |     | ✅    |                    |
| `notes`                         | Terms and Conditions          | `html`      |     | ✅    |                    |
| `purchaser_employee_id`         | Driver (Employee)             | `many2one`  |     |       | hr.employee        |
| `purchaser_id`                  | Driver                        | `many2one`  |     |       | res.partner        |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `service_ids`                   | Included Services             | `many2many` |     | ✅    | fleet.service.type |
| `start_date`                    | Contract Start Date           | `date`      |     | ✅    |                    |
| `state`                         | Status                        | `selection` |     | ✅    |                    |
| `user_id`                       | Responsible                   | `many2one`  |     | ✅    | res.users          |
| `vehicle_id`                    | Vehicle                       | `many2one`  | ✅  | ✅    | fleet.vehicle      |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                    | Group                                | Perms     |
| --------------------------------------- | ------------------------------------ | --------- |
| fleet_vehicle_log_contract_access_right | Fleet / Officer: Manage all vehicles | `R/W/C/D` |
| fleet_vehicle_log_contract_access_right | Fleet / Administrator                | `R/W/C/D` |

**Record Rules:**

- **Administrator has all rights on vehicle's contracts** (21) `R/W/C/D`
- **Fleet vehicle log contract: Multi Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `mail.activity.type` — Activity Type

Activity Types are used to categorize activities. Each type is a different kind of
activity e.g. call, mail, meeting. An activity can be generic i.e. available for all
models using activities; or specific to a model in which case res_model field should be
used.

**Fields:**

| Field                     | Label                | Type        | Req | Store | Relation           |
| ------------------------- | -------------------- | ----------- | --- | ----- | ------------------ |
| `active`                  | Active               | `boolean`   |     | ✅    |                    |
| `category`                | Action               | `selection` |     | ✅    |                    |
| `chaining_type`           | Chaining Type        | `selection` | ✅  | ✅    |                    |
| `create_date`             | Created on           | `datetime`  |     | ✅    |                    |
| `create_uid`              | Create Uid           | `many2one`  |     | ✅    | res.users          |
| `decoration_type`         | Decoration Type      | `selection` |     | ✅    |                    |
| `default_note`            | Default Note         | `html`      |     | ✅    |                    |
| `default_user_id`         | Default User         | `many2one`  |     | ✅    | res.users          |
| `delay_count`             | Schedule             | `integer`   |     | ✅    |                    |
| `delay_from`              | Delay Type           | `selection` | ✅  | ✅    |                    |
| `delay_label`             | Delay Label          | `char`      |     |       |                    |
| `delay_unit`              | Delay units          | `selection` | ✅  | ✅    |                    |
| `display_name`            | Display Name         | `char`      |     |       |                    |
| `icon`                    | Icon                 | `char`      |     | ✅    |                    |
| `id`                      | ID                   | `integer`   |     | ✅    |                    |
| `initial_res_model`       | Initial model        | `selection` |     |       |                    |
| `mail_template_ids`       | Email templates      | `many2many` |     | ✅    | mail.template      |
| `name`                    | Name                 | `char`      | ✅  | ✅    |                    |
| `previous_type_ids`       | Preceding Activities | `many2many` |     | ✅    | mail.activity.type |
| `res_model`               | Model                | `selection` |     | ✅    |                    |
| `res_model_change`        | Model has change     | `boolean`   |     |       |                    |
| `sequence`                | Sequence             | `integer`   |     | ✅    |                    |
| `suggested_next_type_ids` | Suggest              | `many2many` |     | ✅    | mail.activity.type |
| `summary`                 | Default Summary      | `char`      |     | ✅    |                    |
| `triggered_next_type_id`  | Trigger              | `many2one`  |     | ✅    | mail.activity.type |
| `write_date`              | Last Updated on      | `datetime`  |     | ✅    |                    |
| `write_uid`               | Last Updated by      | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                | Group                    | Perms     |
| ----------------------------------- | ------------------------ | --------- |
| mail.activity.type.sale.manager     | Sales / Administrator    | `R/W/C/D` |
| mail.activity.type.sale.manager     | Sales / Administrator    | `R/W/C/D` |
| mail.activity.type.holidays.manager | Time Off / Administrator | `R/W/C/D` |
| mail.activity.type.expense.user     | Expenses / Administrator | `R/W/C/D` |
| mail.activity.type.fleet.manager    | Fleet / Administrator    | `R/W/C/D` |
| mail.activity.type.system           | Role / Administrator     | `R/W/C/D` |
| mail.activity.type.user             | Role / User              | `R`       |

### 🗃️ `fleet.vehicle.model.brand` — Brand of the vehicle

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation            |
| -------------- | --------------- | ---------- | --- | ----- | ------------------- |
| `active`       | Active          | `boolean`  |     | ✅    |                     |
| `create_date`  | Created on      | `datetime` |     | ✅    |                     |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users           |
| `display_name` | Display Name    | `char`     |     |       |                     |
| `id`           | ID              | `integer`  |     | ✅    |                     |
| `image_128`    | Logo            | `binary`   |     | ✅    |                     |
| `model_count`  | Model Count     | `integer`  |     | ✅    |                     |
| `model_ids`    | Model           | `one2many` |     | ✅    | fleet.vehicle.model |
| `name`         | Name            | `char`     | ✅  | ✅    |                     |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                     |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users           |

**Access Rights:**

| Name                                   | Group                                | Perms     |
| -------------------------------------- | ------------------------------------ | --------- |
| fleet_vehicle_model_brand_access_right | Fleet / Officer: Manage all vehicles | `R`       |
| fleet_vehicle_model_brand_access_right | Fleet / Administrator                | `R/W/C/D` |

### 🗃️ `fleet.vehicle.model.category` — Category of the model

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
| `name`         | Name            | `char`     | ✅  | ✅    |           |
| `sequence`     | Sequence        | `integer`  |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                                      | Group                                | Perms     |
| ----------------------------------------- | ------------------------------------ | --------- |
| fleet_vehicle_model_category_access_right | Fleet / Officer: Manage all vehicles | `R`       |
| fleet_vehicle_model_brand_category_right  | Fleet / Administrator                | `R/W/C/D` |

### 🗃️ `res.config.settings` — Config Settings

> ✳️ Transient (Wizard)

Enhanced configuration interface for exchange rate management

**Fields:**

| Field                                                | Label                                                                                           | Type        | Req | Store | Relation                         |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------- | --- | ----- | -------------------------------- |
| `access_token`                                       | Access Token                                                                                    | `char`      |     | ✅    |                                  |
| `account_cash_basis_base_account_id`                 | Base Tax Received Account                                                                       | `many2one`  |     |       | account.account                  |
| `account_default_credit_limit`                       | Default Credit Limit                                                                            | `monetary`  |     |       |                                  |
| `account_discount_expense_allocation_id`             | Customer Invoices Discounts Account                                                             | `many2one`  |     |       | account.account                  |
| `account_discount_income_allocation_id`              | Vendor Bills Discounts Account                                                                  | `many2one`  |     |       | account.account                  |
| `account_fiscal_country_id`                          | Fiscal Country Code                                                                             | `many2one`  |     |       | res.country                      |
| `account_journal_early_pay_discount_gain_account_id` | Early Discount Gain                                                                             | `many2one`  |     |       | account.account                  |
| `account_journal_early_pay_discount_loss_account_id` | Early Discount Loss                                                                             | `many2one`  |     |       | account.account                  |
| `account_journal_suspense_account_id`                | Bank Suspense                                                                                   | `many2one`  |     |       | account.account                  |
| `account_on_checkout`                                | Customer Accounts                                                                               | `selection` | ✅  |       |                                  |
| `account_price_include`                              | Default Sales Price Include                                                                     | `selection` | ✅  |       |                                  |
| `account_storno`                                     | Storno accounting                                                                               | `boolean`   |     |       |                                  |
| `account_use_credit_limit`                           | Sales Credit Limit                                                                              | `boolean`   |     |       |                                  |
| `active_provider_id`                                 | Active Provider                                                                                 | `many2one`  |     |       | payment.provider                 |
| `active_user_count`                                  | Number of Active Users                                                                          | `integer`   |     |       |                                  |
| `add_to_cart_action`                                 | Add To Cart Action                                                                              | `selection` |     |       |                                  |
| `alias_domain_id`                                    | Alias Domain                                                                                    | `many2one`  |     |       | mail.alias.domain                |
| `anglo_saxon_accounting`                             | Use anglo-saxon accounting                                                                      | `boolean`   |     |       |                                  |
| `annual_inventory_day`                               | Day of the month                                                                                | `integer`   |     |       |                                  |
| `annual_inventory_month`                             | Annual Inventory Month                                                                          | `selection` |     |       |                                  |
| `app_login_details_show`                             | Replace Login URL                                                                               | `boolean`   |     | ✅    |                                  |
| `app_login_name`                                     | Login Page Name                                                                                 | `char`      |     | ✅    |                                  |
| `app_login_url`                                      | Login Page URL                                                                                  | `char`      |     | ✅    |                                  |
| `app_ribbon_name`                                    | Show Demo Ribbon                                                                                | `char`      |     | ✅    |                                  |
| `app_ribbon_name_show`                               | Show Ribbon                                                                                     | `boolean`   |     | ✅    |                                  |
| `app_show_lang`                                      | Show Quick Language Switcher                                                                    | `boolean`   |     | ✅    |                                  |
| `app_system_name`                                    | System Name                                                                                     | `char`      |     | ✅    |                                  |
| `attendance_subject_generic`                         | Attendance Subject Generic                                                                      | `selection` |     | ✅    |                                  |
| `auth_signup_reset_password`                         | Enable password reset from Login page                                                           | `boolean`   |     | ✅    |                                  |
| `auth_signup_template_user_id`                       | Template user for new users created through signup                                              | `many2one`  |     | ✅    | res.users                        |
| `auth_signup_uninvited`                              | Customer Account                                                                                | `selection` |     |       |                                  |
| `auth_totp_enforce`                                  | Enforce two-factor authentication                                                               | `boolean`   |     | ✅    |                                  |
| `auth_totp_policy`                                   | Two-factor authentication enforcing policy                                                      | `selection` |     | ✅    |                                  |
| `automatic_email`                                    | Automatic Email                                                                                 | `boolean`   |     | ✅    |                                  |
| `automatic_invoice`                                  | Automatic Invoice                                                                               | `boolean`   |     | ✅    |                                  |
| `autopost_bills`                                     | Auto-validate bills                                                                             | `boolean`   |     |       |                                  |
| `barcode_nomenclature_id`                            | Nomenclature                                                                                    | `many2one`  |     |       | barcode.nomenclature             |
| `barcode_separator`                                  | Separator                                                                                       | `char`      |     | ✅    |                                  |
| `cart_abandoned_delay`                               | Abandoned Delay                                                                                 | `float`     |     |       |                                  |
| `cart_recovery_mail_template`                        | Cart Recovery Email                                                                             | `many2one`  |     |       | mail.template                    |
| `cdn_activated`                                      | Content Delivery Network (CDN)                                                                  | `boolean`   |     |       |                                  |
| `cdn_filters`                                        | CDN Filters                                                                                     | `text`      |     |       |                                  |
| `cdn_url`                                            | CDN Base URL                                                                                    | `char`      |     |       |                                  |
| `channel_id`                                         | Website Live Channel                                                                            | `many2one`  |     |       | im_livechat.channel              |
| `chart_template`                                     | Chart Template                                                                                  | `selection` |     | ✅    |                                  |
| `client_id`                                          | Client ID                                                                                       | `char`      |     | ✅    |                                  |
| `client_secret`                                      | Client Secret                                                                                   | `char`      |     | ✅    |                                  |
| `company_count`                                      | Number of Companies                                                                             | `integer`   |     |       |                                  |
| `company_country_code`                               | Company Country Code                                                                            | `char`      |     |       |                                  |
| `company_country_group_codes`                        | Country Group Codes                                                                             | `json`      |     |       |                                  |
| `company_currency_id`                                | Company Currency                                                                                | `many2one`  |     |       | res.currency                     |
| `company_expense_allowed_payment_method_line_ids`    | Payment methods available for expenses paid by company                                          | `many2many` |     |       | account.payment.method.line      |
| `company_id`                                         | Company                                                                                         | `many2one`  | ✅  | ✅    | res.company                      |
| `company_informations`                               | Company Informations                                                                            | `text`      |     |       |                                  |
| `company_name`                                       | Company Name                                                                                    | `char`      |     |       |                                  |
| `company_so_template_id`                             | Default Template                                                                                | `many2one`  |     |       | sale.order.template              |
| `confirmation_email_template_id`                     | Confirmation Email Template                                                                     | `many2one`  |     |       | mail.template                    |
| `contract_expiration_notice_period`                  | Contract Expiry Notice Period                                                                   | `integer`   |     |       |                                  |
| `country_code`                                       | Country Code                                                                                    | `char`      |     |       |                                  |
| `create_date`                                        | Created on                                                                                      | `datetime`  |     | ✅    |                                  |
| `create_uid`                                         | Created by                                                                                      | `many2one`  |     | ✅    | res.users                        |
| `crm_auto_assignment_action`                         | Auto Assignment Action                                                                          | `selection` |     | ✅    |                                  |
| `crm_auto_assignment_interval_number`                | Repeat every                                                                                    | `integer`   |     | ✅    |                                  |
| `crm_auto_assignment_interval_type`                  | Auto Assignment Interval Unit                                                                   | `selection` |     | ✅    |                                  |
| `crm_auto_assignment_run_datetime`                   | Auto Assignment Next Execution Date                                                             | `datetime`  |     | ✅    |                                  |
| `crm_use_auto_assignment`                            | Rule-Based Assignment                                                                           | `boolean`   |     | ✅    |                                  |
| `currency_exchange_journal_id`                       | Currency Exchange Journal                                                                       | `many2one`  |     |       | account.journal                  |
| `currency_id`                                        | Currency                                                                                        | `many2one`  | ✅  |       | res.currency                     |
| `days_to_purchase`                                   | Days to Purchase                                                                                | `float`     |     |       |                                  |
| `default_allow_out_of_stock_order`                   | Continue selling when out-of-stock                                                              | `boolean`   |     | ✅    |                                  |
| `default_available_threshold`                        | Show Threshold                                                                                  | `float`     |     | ✅    |                                  |
| `default_invoice_policy`                             | Invoicing Policy                                                                                | `selection` |     | ✅    |                                  |
| `default_picking_policy`                             | Picking Policy                                                                                  | `selection` | ✅  | ✅    |                                  |
| `default_show_availability`                          | Show availability Qty                                                                           | `boolean`   |     | ✅    |                                  |
| `delay_alert_contract`                               | Delay alert contract outdated                                                                   | `integer`   |     | ✅    |                                  |
| `digest_emails`                                      | Digest Emails                                                                                   | `boolean`   |     | ✅    |                                  |
| `digest_id`                                          | Digest Email                                                                                    | `many2one`  |     | ✅    | digest.digest                    |
| `display_account_storno`                             | Display Account Storno                                                                          | `boolean`   |     |       |                                  |
| `display_invoice_amount_total_words`                 | Total amount of invoice in letters                                                              | `boolean`   |     |       |                                  |
| `display_invoice_tax_company_currency`               | Taxes in company currency                                                                       | `boolean`   |     |       |                                  |
| `display_name`                                       | Display Name                                                                                    | `char`      |     |       |                                  |
| `documents_binary_max_size`                          | Size                                                                                            | `integer`   |     | ✅    |                                  |
| `documents_forbidden_extensions`                     | Extensions                                                                                      | `char`      |     | ✅    |                                  |
| `downpayment_account_id`                             | Downpayment Account                                                                             | `many2one`  |     |       | account.account                  |
| `ecommerce_access`                                   | Ecommerce Access                                                                                | `selection` |     |       |                                  |
| `email_primary_color`                                | Email Button Text                                                                               | `char`      |     |       |                                  |
| `email_secondary_color`                              | Email Button Color                                                                              | `char`      |     |       |                                  |
| `enable_academic_plan`                               | Academic Plan                                                                                   | `boolean`   |     | ✅    |                                  |
| `enable_create_student_user`                         | Create Student User                                                                             | `boolean`   |     | ✅    |                                  |
| `enable_exchange_rate_module`                        | Enable Exchange Rate Synchronization                                                            | `boolean`   |     | ✅    |                                  |
| `enable_recaptcha`                                   | Enable reCAPTCHA                                                                                | `boolean`   |     | ✅    |                                  |
| `expense_account_id`                                 | Expense Account                                                                                 | `many2one`  |     |       | account.account                  |
| `expense_currency_exchange_account_id`               | Loss Exchange Rate Account                                                                      | `many2one`  |     |       | account.account                  |
| `expense_journal_id`                                 | Default Expense Journal                                                                         | `many2one`  |     |       | account.journal                  |
| `external_email_server_default`                      | Use Custom Email Servers                                                                        | `boolean`   |     | ✅    |                                  |
| `external_report_layout_id`                          | Document Template                                                                               | `many2one`  |     |       | ir.ui.view                       |
| `fail_counter`                                       | Fail Mail                                                                                       | `integer`   |     |       |                                  |
| `favicon`                                            | Favicon                                                                                         | `binary`    |     |       |                                  |
| `fiscalyear_last_day`                                | Fiscalyear Last Day                                                                             | `integer`   |     |       |                                  |
| `fiscalyear_last_month`                              | Fiscalyear Last Month                                                                           | `selection` |     |       |                                  |
| `fiscalyear_lock_date`                               | Global Lock Date                                                                                | `date`      |     |       |                                  |
| `force_restrictive_audit_trail`                      | Forced Audit Trail                                                                              | `boolean`   |     |       |                                  |
| `global_calendar_user_id`                            | Calendar User                                                                                   | `many2one`  |     | ✅    | res.users                        |
| `google_analytics_key`                               | Google Analytics Key                                                                            | `char`      |     |       |                                  |
| `google_gmail_client_identifier`                     | Gmail Client Id                                                                                 | `char`      |     | ✅    |                                  |
| `google_gmail_client_secret`                         | Gmail Client Secret                                                                             | `char`      |     | ✅    |                                  |
| `google_maps_static_api_key`                         | Google Maps API key                                                                             | `char`      |     | ✅    |                                  |
| `google_maps_static_api_secret`                      | Google Maps API secret                                                                          | `char`      |     | ✅    |                                  |
| `google_search_console`                              | Google Search Console Key                                                                       | `char`      |     |       |                                  |
| `google_translate_api_key`                           | Message Translation API Key                                                                     | `char`      |     | ✅    |                                  |
| `group_analytic_accounting`                          | Analytic Accounting                                                                             | `boolean`   |     | ✅    |                                  |
| `group_auto_done_setting`                            | Lock Confirmed Sales                                                                            | `boolean`   |     | ✅    |                                  |
| `group_cash_rounding`                                | Cash Rounding                                                                                   | `boolean`   |     | ✅    |                                  |
| `group_discount_per_so_line`                         | Discounts                                                                                       | `boolean`   |     | ✅    |                                  |
| `group_fiscal_year`                                  | Fiscal Years                                                                                    | `boolean`   |     | ✅    |                                  |
| `group_gmc_feed`                                     | Google Merchant Center                                                                          | `boolean`   |     |       |                                  |
| `group_lot_on_delivery_slip`                         | Display Lots & Serial Numbers on Delivery Slips                                                 | `boolean`   |     | ✅    |                                  |
| `group_lot_on_invoice`                               | Display Lots & Serial Numbers on Invoices                                                       | `boolean`   |     | ✅    |                                  |
| `group_mass_mailing_campaign`                        | Mailing Campaigns                                                                               | `boolean`   |     | ✅    |                                  |
| `group_multi_currency`                               | Multi-Currencies                                                                                | `boolean`   |     | ✅    |                                  |
| `group_multi_website`                                | Multi-website                                                                                   | `boolean`   |     | ✅    |                                  |
| `group_product_price_comparison`                     | Comparison Price                                                                                | `boolean`   |     | ✅    |                                  |
| `group_product_pricelist`                            | Pricelists                                                                                      | `boolean`   |     | ✅    |                                  |
| `group_product_variant`                              | Variants                                                                                        | `boolean`   |     | ✅    |                                  |
| `group_proforma_sales`                               | Pro-Forma Invoice                                                                               | `boolean`   |     | ✅    |                                  |
| `group_sale_delivery_address`                        | Customer Addresses                                                                              | `boolean`   |     | ✅    |                                  |
| `group_sale_order_template`                          | Quotation Templates                                                                             | `boolean`   |     | ✅    |                                  |
| `group_send_reminder`                                | Receipt Reminder                                                                                | `boolean`   |     | ✅    |                                  |
| `group_show_uom_price`                               | Base Unit Price                                                                                 | `boolean`   |     | ✅    |                                  |
| `group_stock_adv_location`                           | Multi-Step Routes                                                                               | `boolean`   |     | ✅    |                                  |
| `group_stock_lot_print_gs1`                          | Print GS1 Barcodes for Lots & Serial Numbers                                                    | `boolean`   |     | ✅    |                                  |
| `group_stock_multi_locations`                        | Storage Locations                                                                               | `boolean`   |     | ✅    |                                  |
| `group_stock_production_lot`                         | Lots & Serial Numbers                                                                           | `boolean`   |     | ✅    |                                  |
| `group_stock_reception_report`                       | Reception Report                                                                                | `boolean`   |     | ✅    |                                  |
| `group_stock_sign_delivery`                          | Signature                                                                                       | `boolean`   |     | ✅    |                                  |
| `group_stock_tracking_lot`                           | Packages                                                                                        | `boolean`   |     | ✅    |                                  |
| `group_stock_tracking_owner`                         | Consignment                                                                                     | `boolean`   |     | ✅    |                                  |
| `group_uom`                                          | Units of Measure & Packagings                                                                   | `boolean`   |     | ✅    |                                  |
| `group_use_lead`                                     | Leads                                                                                           | `boolean`   |     | ✅    |                                  |
| `group_use_recurring_revenues`                       | Recurring Revenues                                                                              | `boolean`   |     | ✅    |                                  |
| `group_warning_purchase`                             | Purchase Warnings                                                                               | `boolean`   |     | ✅    |                                  |
| `group_warning_sale`                                 | Sale Order Warnings                                                                             | `boolean`   |     | ✅    |                                  |
| `group_warning_stock`                                | Warnings for Stock                                                                              | `boolean`   |     | ✅    |                                  |
| `hard_lock_date`                                     | Hard Lock Date                                                                                  | `date`      |     |       |                                  |
| `has_accounting_entries`                             | Has Accounting Entries                                                                          | `boolean`   |     |       |                                  |
| `has_chart_of_accounts`                              | Company has a chart of accounts                                                                 | `boolean`   |     |       |                                  |
| `has_default_share_image`                            | Use a image by default for sharing                                                              | `boolean`   |     |       |                                  |
| `has_enabled_provider`                               | Has Enabled Provider                                                                            | `boolean`   |     |       |                                  |
| `has_google_analytics`                               | Google Analytics                                                                                | `boolean`   |     |       |                                  |
| `has_google_search_console`                          | Google Search Console                                                                           | `boolean`   |     |       |                                  |
| `has_plausible_shared_key`                           | Plausible Analytics                                                                             | `boolean`   |     |       |                                  |
| `horizon_days`                                       | Replenishment Horizon                                                                           | `float`     |     |       |                                  |
| `hr_expense_alias_domain_id`                         | Hr Expense Alias Domain                                                                         | `many2one`  |     |       | mail.alias.domain                |
| `hr_expense_alias_prefix`                            | Default Alias Name for Expenses                                                                 | `char`      |     | ✅    |                                  |
| `hr_expense_use_mailgateway`                         | Let your employees record expenses by email                                                     | `boolean`   |     | ✅    |                                  |
| `hr_presence_control_email`                          | Based on number of emails sent                                                                  | `boolean`   |     |       |                                  |
| `hr_presence_control_email_amount`                   | # emails to send                                                                                | `integer`   |     |       |                                  |
| `hr_presence_control_ip`                             | Based on IP Address                                                                             | `boolean`   |     |       |                                  |
| `hr_presence_control_ip_list`                        | Valid IP addresses                                                                              | `char`      |     |       |                                  |
| `hr_presence_control_login`                          | Based on user status in system                                                                  | `boolean`   |     |       |                                  |
| `id`                                                 | ID                                                                                              | `integer`   |     | ✅    |                                  |
| `income_account_id`                                  | Income Account                                                                                  | `many2one`  |     |       | account.account                  |
| `income_currency_exchange_account_id`                | Gain Exchange Rate Account                                                                      | `many2one`  |     |       | account.account                  |
| `incoterm_id`                                        | Default incoterm                                                                                | `many2one`  |     |       | account.incoterms                |
| `invoice_mail_template_id`                           | Email Template                                                                                  | `many2one`  |     | ✅    | mail.template                    |
| `invoice_terms`                                      | Terms & Conditions                                                                              | `html`      |     |       |                                  |
| `invoice_terms_html`                                 | Terms & Conditions as a Web page                                                                | `html`      |     |       |                                  |
| `is_account_peppol_eligible`                         | PEPPOL eligible                                                                                 | `boolean`   |     |       |                                  |
| `is_batch_and_subject_constraint`                    | Batch and Subject Constraint                                                                    | `boolean`   |     | ✅    |                                  |
| `is_batch_constraint`                                | Batch Constraint                                                                                | `boolean`   |     | ✅    |                                  |
| `is_classroom_constraint`                            | Classroom Constraint                                                                            | `boolean`   |     | ✅    |                                  |
| `is_faculty_constraint`                              | Faculty Constraint                                                                              | `boolean`   |     | ✅    |                                  |
| `is_hash_verified`                                   | Is Hash Verified                                                                                | `boolean`   |     |       |                                  |
| `is_installed_sale`                                  | Is the Sale Module Installed                                                                    | `boolean`   |     | ✅    |                                  |
| `is_mail_sent`                                       | Is Mail Sent                                                                                    | `boolean`   |     |       |                                  |
| `is_membership_multi`                                | Multi Teams                                                                                     | `boolean`   |     | ✅    |                                  |
| `is_newsletter_enabled`                              | Is Newsletter Enabled                                                                           | `boolean`   |     | ✅    |                                  |
| `is_root_company`                                    | Is Root Company                                                                                 | `boolean`   |     |       |                                  |
| `language_count`                                     | Number of Languages                                                                             | `integer`   |     |       |                                  |
| `language_ids`                                       | Languages                                                                                       | `many2many` |     |       | res.lang                         |
| `lead_enrich_auto`                                   | Enrich lead automatically                                                                       | `selection` |     | ✅    |                                  |
| `lead_mining_in_pipeline`                            | Create a lead mining request directly from the opportunity pipeline.                            | `boolean`   |     | ✅    |                                  |
| `link_qr_code`                                       | Display Link QR-code                                                                            | `boolean`   |     |       |                                  |
| `lock_confirmed_po`                                  | Lock Confirmed Orders                                                                           | `boolean`   |     | ✅    |                                  |
| `mass_mailing_mail_server_id`                        | Mail Server                                                                                     | `many2one`  |     | ✅    | ir.mail_server                   |
| `mass_mailing_outgoing_mail_server`                  | Dedicated Server                                                                                | `boolean`   |     | ✅    |                                  |
| `mass_mailing_reports`                               | 24H Stat Mailing Reports                                                                        | `boolean`   |     | ✅    |                                  |
| `mass_mailing_split_contact_name`                    | Split First and Last Name                                                                       | `boolean`   |     | ✅    |                                  |
| `menu_bg_image`                                      | Apps Menu Footer Image                                                                          | `binary`    |     |       |                                  |
| `microsoft_outlook_client_identifier`                | Outlook Client Id                                                                               | `char`      |     | ✅    |                                  |
| `microsoft_outlook_client_secret`                    | Outlook Client Secret                                                                           | `char`      |     | ✅    |                                  |
| `module_account_3way_match`                          | 3-way matching: purchases, receptions and bills                                                 | `boolean`   |     | ✅    |                                  |
| `module_account_accountant`                          | Accounting                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_account_bank_statement_extract`              | Bank Statement Digitization                                                                     | `boolean`   |     | ✅    |                                  |
| `module_account_bank_statement_import_qif`           | Import .qif files                                                                               | `boolean`   |     | ✅    |                                  |
| `module_account_batch_payment`                       | Use batch payments                                                                              | `boolean`   |     | ✅    |                                  |
| `module_account_budget`                              | Budget Management                                                                               | `boolean`   |     | ✅    |                                  |
| `module_account_check_printing`                      | Allow check printing and deposits                                                               | `boolean`   |     | ✅    |                                  |
| `module_account_extract`                             | Document Digitization                                                                           | `boolean`   |     | ✅    |                                  |
| `module_account_inter_company_rules`                 | Manage Inter Company                                                                            | `boolean`   |     | ✅    |                                  |
| `module_account_intrastat`                           | Intrastat                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_account_invoice_extract`                     | Invoice Digitization                                                                            | `boolean`   |     | ✅    |                                  |
| `module_account_iso20022`                            | SEPA Credit Transfer / ISO20022                                                                 | `boolean`   |     | ✅    |                                  |
| `module_account_payment`                             | Invoice Online Payment                                                                          | `boolean`   |     | ✅    |                                  |
| `module_account_peppol`                              | PEPPOL Invoicing                                                                                | `boolean`   |     | ✅    |                                  |
| `module_account_reports`                             | Dynamic Reports                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_account_sepa_direct_debit`                   | Use SEPA Direct Debit                                                                           | `boolean`   |     | ✅    |                                  |
| `module_auth_ldap`                                   | LDAP Authentication                                                                             | `boolean`   |     | ✅    |                                  |
| `module_auth_oauth`                                  | Use external authentication providers (OAuth)                                                   | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup`                        | Database Backup to Local Server                                                                 | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_dropbox`                | Database Backup to Dropbox                                                                      | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_ftp`                    | Database Backup to Remote FTP Server                                                            | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_google_drive`           | Database Backup to Google Drive                                                                 | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_onedrive`               | Database Backup to Onedrive                                                                     | `boolean`   |     | ✅    |                                  |
| `module_auto_database_backup_sftp`                   | Database Backup to Remote SFTP Server                                                           | `boolean`   |     | ✅    |                                  |
| `module_backend_theme`                               | Backend Theme                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_base_geolocalize`                            | GeoLocalize                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_base_import`                                 | Allow users to import data from CSV/XLS/XLSX/ODS files                                          | `boolean`   |     | ✅    |                                  |
| `module_bigbluebutton`                               | Bigbluebutton Enterprise                                                                        | `boolean`   |     | ✅    |                                  |
| `module_crm_iap_enrich`                              | Enrich your leads automatically with company data based on their email address.                 | `boolean`   |     | ✅    |                                  |
| `module_crm_iap_mine`                                | Generate new leads based on their country, industries, size, etc.                               | `boolean`   |     | ✅    |                                  |
| `module_currency_rate_live`                          | Automatic Currency Rates                                                                        | `boolean`   |     | ✅    |                                  |
| `module_delivery`                                    | Delivery Methods                                                                                | `boolean`   |     | ✅    |                                  |
| `module_delivery_bpost`                              | bpost Connector                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_delivery_dhl`                                | DHL Express Connector                                                                           | `boolean`   |     | ✅    |                                  |
| `module_delivery_easypost`                           | Easypost Connector                                                                              | `boolean`   |     | ✅    |                                  |
| `module_delivery_envia`                              | Envia.com Connector                                                                             | `boolean`   |     | ✅    |                                  |
| `module_delivery_fedex_rest`                         | FedEx Connector                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_delivery_sendcloud`                          | Sendcloud Connector                                                                             | `boolean`   |     | ✅    |                                  |
| `module_delivery_shiprocket`                         | Shiprocket Connector                                                                            | `boolean`   |     | ✅    |                                  |
| `module_delivery_starshipit`                         | Starshipit Connector                                                                            | `boolean`   |     | ✅    |                                  |
| `module_delivery_ups_rest`                           | UPS Connector                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_delivery_usps_rest`                          | USPS Connector                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_event_booth`                                 | Booth Management                                                                                | `boolean`   |     | ✅    |                                  |
| `module_event_sale`                                  | Tickets with Sale                                                                               | `boolean`   |     | ✅    |                                  |
| `module_google_address_autocomplete`                 | Google Address Autocomplete                                                                     | `boolean`   |     | ✅    |                                  |
| `module_google_calendar`                             | Allow the users to synchronize their calendar with Google Calendar                              | `boolean`   |     | ✅    |                                  |
| `module_google_gmail`                                | Support Gmail Authentication                                                                    | `boolean`   |     | ✅    |                                  |
| `module_googlemeet`                                  | Google Meet                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_google_recaptcha`                            | reCAPTCHA                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_helpdesk_elearning`                          | E-Learning                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_helpdesk_forum`                              | Helpdesk Forum                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_helpdesk_project_ext`                        | Helpdesk project                                                                                | `boolean`   |     | ✅    |                                  |
| `module_hr_attendance`                               | Based on attendances                                                                            | `boolean`   |     |       |                                  |
| `module_hr_expense_extract`                          | Send bills to OCR to generate expenses                                                          | `boolean`   |     | ✅    |                                  |
| `module_hr_expense_stripe`                           | Link your stripe issuing account to manage company credit cards for your employees through Odoo | `boolean`   |     | ✅    |                                  |
| `module_hr_payroll_expense`                          | Reimburse Expenses in Payslip                                                                   | `boolean`   |     | ✅    |                                  |
| `module_hr_presence`                                 | Advanced Presence Control                                                                       | `boolean`   |     | ✅    |                                  |
| `module_hr_recruitment_extract`                      | Send CV to OCR to fill applications                                                             | `boolean`   |     | ✅    |                                  |
| `module_hr_recruitment_survey`                       | Interview Forms                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_hr_skills`                                   | Skills Management                                                                               | `boolean`   |     | ✅    |                                  |
| `module_loyalty`                                     | Promotions, Coupons, Gift Card & Loyalty Program                                                | `boolean`   |     | ✅    |                                  |
| `module_mail_plugin`                                 | Allow integration with the mail plugins                                                         | `boolean`   |     | ✅    |                                  |
| `module_microsoft_calendar`                          | Allow the users to synchronize their calendar with Outlook Calendar                             | `boolean`   |     | ✅    |                                  |
| `module_microsoft_outlook`                           | Support Outlook Authentication                                                                  | `boolean`   |     | ✅    |                                  |
| `module_online_appointment`                          | Online Appointment Enterprise                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_achievement_enterprise`           | Achievement Enterprise                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_activity`                         | Activity                                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_activity_enterprise`              | Activity Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_admission`                        | Admission                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_admission_enterprise`             | Admission Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_admission_grading_bridge`         | Admission Grading Bridge                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_blog_enterprise`           | Alumni Blog Enterprise                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_enterprise`                | Alumni Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_event_enterprise`          | Alumni Event Enterprise                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_alumni_job_enterprise`            | Alumni Job Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_asset_request_enterprise`         | Asset Request Enterprise                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment`                       | Assignment                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_enterprise`            | Assignment Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_grading_bridge`        | Assignment Gradebook Bridge                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_grading_enterprise`    | Assignment Grading Enterprise                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_assignment_rubrics`               | Assignment Rubrics                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance`                       | Attendance                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance_enterprise`            | Attendance Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance_face_recognition`      | Attendance Face Recognition                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_attendance_report_xlsx`           | Attendance Xlsx Report                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_campus_enterprise`                | Campus Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_classroom`                        | Classroom                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_classroom_enterprise`             | Classroom Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_convocation`                      | Convocation                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_crm_enterprise`                   | CRM Enterprise                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_dashboard_kpi`                    | Dashboard KPI                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_digital_library`                  | Digital Library                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_openeducat_discipline`                       | Discipline Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_dynamic_admission`                | Dynamic Admission                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_event_enterprise`                 | Event Enterprise                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam`                             | Exam                                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_enterprise`                  | Exam Enterprise                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_gpa_enterprise`              | Exam GPA Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_grading_bridge`              | Exam Grading Bridge                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_exam_migration_bridge`            | Student Migration Exam Bridge                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_facility`                         | Facility                                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_facility_enterprise`              | Facility Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_fees`                             | Fees                                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_fees_parent_bridge`               | Fees Parent Bridge                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_fees_plan`                        | Fees Plan                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_grading`                          | Grading                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_grading_migration_bridge`         | Student Migration Grading Bridge                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_grievance_enterprise`             | Grievance                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_health_enterprise`                | Health Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_jitsi_enterprise`                 | Jitsi Enterprise                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_job_enterprise`                   | Job Enterprise                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lesson`                           | Lesson Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_library`                          | Library                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_library_barcode`                  | Library Barcode Enterprise                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_library_enterprise`               | Library Enterprise                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live`                             | Live Meeting                                                                                    | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live_assignment`                  | Live Meeting Assignment                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live_attendance`                  | Live Meeting Attendance                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_live_attentiveness`               | Live Meeting Attentiveness                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms`                              | LMS Enterprise                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_admission`                    | LMS Admission                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_blog`                         | LMS Blog Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_forum`                        | LMS Forum Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_gamification`                 | LMS Gamification Enterprise                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_h5p`                          | LMS H5P Enterprise                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_sale`                         | LMS Sale Enterprise                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_lms_survey`                       | LMS Survey Enterprise                                                                           | `boolean`   |     | ✅    |                                  |
| `module_openeducat_mass_subject_registration`        | Mass Subject Registration                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_meeting_enterprise`               | Meeting Enterprise                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_notice_board_enterprise`          | Notice Board Enterprise                                                                         | `boolean`   |     | ✅    |                                  |
| `module_openeducat_omr`                              | OMR                                                                                             | `boolean`   |     | ✅    |                                  |
| `module_openeducat_parent`                           | Parent                                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_parent_enterprise`                | Parent Enterprise                                                                               | `boolean`   |     | ✅    |                                  |
| `module_openeducat_placement_enterprise`             | Placement Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_placement_job_enterprise`         | Placement Job Enterprise                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_quiz`                             | Quiz Enterprise                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_openeducat_quiz_anti_cheating`               | Quiz Anti Cheating                                                                              | `boolean`   |     | ✅    |                                  |
| `module_openeducat_scholarship_enterprise`           | Scholarship Enterprise                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_secure`                           | Secure QR                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_skill_enterprise`                 | Skill Enterprise                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_skypemeet`                        | Skype Meet                                                                                      | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_attendance_enterprise`    | Student Attendance Kiosk                                                                        | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_feedback_management`      | Student Feedback                                                                                | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_leave_enterprise`         | Student Leave                                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_mentor`                   | Student Mentor                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_progress_enterprise`      | Student Progress Enterprise                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_skill_assessment`         | Skill Assessment Enterprise                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_student_withdrawal_mgmt`          | Student Withdrawal Management                                                                   | `boolean`   |     | ✅    |                                  |
| `module_openeducat_subject_material_allocation`      | Subject Material Allocation                                                                     | `boolean`   |     | ✅    |                                  |
| `module_openeducat_thesis`                           | Thesis                                                                                          | `boolean`   |     | ✅    |                                  |
| `module_openeducat_timetable`                        | Timetable                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_openeducat_timetable_enterprise`             | Timetable Enterprise                                                                            | `boolean`   |     | ✅    |                                  |
| `module_openeducat_transportation_enterprise`        | Transportation Enterprise                                                                       | `boolean`   |     | ✅    |                                  |
| `module_partner_autocomplete`                        | Partner Autocomplete                                                                            | `boolean`   |     | ✅    |                                  |
| `module_partnership`                                 | Membership / Partnership                                                                        | `boolean`   |     | ✅    |                                  |
| `module_pos_event`                                   | Tickets with PoS                                                                                | `boolean`   |     | ✅    |                                  |
| `module_product_email_template`                      | Specific Email                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_product_expiry`                              | Expiration Dates                                                                                | `boolean`   |     | ✅    |                                  |
| `module_product_margin`                              | Allow Product Margin                                                                            | `boolean`   |     | ✅    |                                  |
| `module_purchase_product_matrix`                     | Purchase Grid Entry                                                                             | `boolean`   |     | ✅    |                                  |
| `module_purchase_requisition`                        | Purchase Agreements                                                                             | `boolean`   |     | ✅    |                                  |
| `module_quality_control`                             | Quality                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_quality_control_worksheet`                   | Quality Worksheet                                                                               | `boolean`   |     | ✅    |                                  |
| `module_sale_amazon`                                 | Amazon Sync                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_sale_commission`                             | Commissions                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_sale_gelato`                                 | Gelato                                                                                          | `boolean`   |     | ✅    |                                  |
| `module_sale_loyalty`                                | Coupons & Loyalty                                                                               | `boolean`   |     | ✅    |                                  |
| `module_sale_margin`                                 | Margins                                                                                         | `boolean`   |     | ✅    |                                  |
| `module_sale_pdf_quote_builder`                      | PDF Quote builder                                                                               | `boolean`   |     | ✅    |                                  |
| `module_sale_product_matrix`                         | Sales Grid Entry                                                                                | `boolean`   |     | ✅    |                                  |
| `module_sale_shopee`                                 | Shopee Sync                                                                                     | `boolean`   |     | ✅    |                                  |
| `module_sms`                                         | SMS                                                                                             | `boolean`   |     | ✅    |                                  |
| `module_snailmail_account`                           | Snailmail                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_stock_barcode`                               | Barcode Scanner                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_stock_barcode_barcodelookup`                 | Stock Barcode Database                                                                          | `boolean`   |     | ✅    |                                  |
| `module_stock_dropshipping`                          | Dropshipping                                                                                    | `boolean`   |     | ✅    |                                  |
| `module_stock_fleet`                                 | Dispatch Management System                                                                      | `boolean`   |     | ✅    |                                  |
| `module_stock_landed_costs`                          | Landed Costs                                                                                    | `boolean`   |     | ✅    |                                  |
| `module_stock_picking_batch`                         | Batch, Wave & Cluster Transfers                                                                 | `boolean`   |     | ✅    |                                  |
| `module_stock_sms`                                   | SMS Confirmation                                                                                | `boolean`   |     | ✅    |                                  |
| `module_teams`                                       | Teams                                                                                           | `boolean`   |     | ✅    |                                  |
| `module_voip`                                        | Phone                                                                                           | `boolean`   |     | ✅    |                                  |
| `module_website_cf_turnstile`                        | Cloudflare Turnstile                                                                            | `boolean`   |     | ✅    |                                  |
| `module_website_crm_iap_reveal`                      | Create Leads/Opportunities from your website's traffic                                          | `boolean`   |     | ✅    |                                  |
| `module_website_event_exhibitor`                     | Advanced Sponsors                                                                               | `boolean`   |     | ✅    |                                  |
| `module_website_event_sale`                          | Online Ticketing                                                                                | `boolean`   |     | ✅    |                                  |
| `module_website_event_track`                         | Tracks and Agenda                                                                               | `boolean`   |     | ✅    |                                  |
| `module_website_event_track_live`                    | Live Mode                                                                                       | `boolean`   |     | ✅    |                                  |
| `module_website_event_track_quiz`                    | Quiz on Tracks                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_website_helpdesk_mgmt`                       | Helpdesk Website                                                                                | `boolean`   |     | ✅    |                                  |
| `module_website_hr_recruitment`                      | Online Posting                                                                                  | `boolean`   |     | ✅    |                                  |
| `module_website_livechat`                            | Module Website Livechat                                                                         | `boolean`   |     | ✅    |                                  |
| `module_website_sale_autocomplete`                   | Address Autocomplete                                                                            | `boolean`   |     | ✅    |                                  |
| `module_website_sale_collect`                        | Click & Collect                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_web_unsplash`                                | Unsplash Image Library                                                                          | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_account_templates`                  | Account Templates                                                                               | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_ecommerce_templates`                | Whatsapp Ecommerce Templates                                                                    | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_education_templates`                | Education Templates                                                                             | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_other_templates`                    | Other Templates                                                                                 | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_services_templates`                 | Services Templates                                                                              | `boolean`   |     | ✅    |                                  |
| `module_whatsapp_special_occasions_template`         | Special Occasions Templates                                                                     | `boolean`   |     | ✅    |                                  |
| `module_zoom`                                        | Zoom                                                                                            | `boolean`   |     | ✅    |                                  |
| `newsletter_id`                                      | Newsletter List                                                                                 | `many2one`  |     |       | mailing.list                     |
| `next_execution_timestamp`                           | Next Execution Time                                                                             | `datetime`  |     |       |                                  |
| `onboarding_payment_module`                          | Onboarding Payment Module                                                                       | `selection` |     |       |                                  |
| `openeducat_instance_hash_key`                       | OpenEducat Instance Hash Key                                                                    | `char`      |     |       |                                  |
| `openeducat_instance_hash_msg`                       | Instance Hash Key Message                                                                       | `char`      |     |       |                                  |
| `openeducat_instance_key`                            | OpenEducat Instance Key                                                                         | `char`      |     |       |                                  |
| `parent_qrcode`                                      | QR Code                                                                                         | `boolean`   |     | ✅    |                                  |
| `partner_autocomplete_insufficient_credit`           | Insufficient credit                                                                             | `boolean`   |     |       |                                  |
| `pay_invoices_online`                                | Pay Invoices Online                                                                             | `boolean`   |     | ✅    |                                  |
| `plausible_shared_key`                               | Plausible auth Key                                                                              | `char`      |     |       |                                  |
| `plausible_site`                                     | Plausible Site (e.g. domain.com)                                                                | `char`      |     |       |                                  |
| `po_double_validation`                               | Levels of Approvals \*                                                                          | `selection` |     |       |                                  |
| `po_double_validation_amount`                        | Minimum Amount                                                                                  | `monetary`  |     |       |                                  |
| `po_lock`                                            | Purchase Order Modification \*                                                                  | `selection` |     |       |                                  |
| `po_order_approval`                                  | Purchase Order Approval                                                                         | `boolean`   |     | ✅    |                                  |
| `portal_allow_api_keys`                              | Customer API Keys                                                                               | `boolean`   |     |       |                                  |
| `portal_confirmation_pay`                            | Online Payment                                                                                  | `boolean`   |     |       |                                  |
| `portal_confirmation_sign`                           | Online Signature                                                                                | `boolean`   |     |       |                                  |
| `predictive_lead_scoring_field_labels`               | Predictive Lead Scoring Field Labels                                                            | `char`      |     |       |                                  |
| `predictive_lead_scoring_fields`                     | Lead Scoring Frequency Fields                                                                   | `many2many` |     |       | crm.lead.scoring.frequency.field |
| `predictive_lead_scoring_fields_str`                 | Lead Scoring Frequency Fields in String                                                         | `char`      |     | ✅    |                                  |
| `predictive_lead_scoring_start_date`                 | Lead Scoring Starting Date                                                                      | `date`      |     |       |                                  |
| `predictive_lead_scoring_start_date_str`             | Lead Scoring Starting Date in String                                                            | `char`      |     | ✅    |                                  |
| `prepayment_percent`                                 | Prepayment percentage                                                                           | `float`     |     |       |                                  |
| `preview_ready`                                      | Display preview button                                                                          | `boolean`   |     |       |                                  |
| `product_volume_volume_in_cubic_feet`                | Volume unit of measure                                                                          | `selection` |     | ✅    |                                  |
| `product_weight_in_lbs`                              | Weight unit of measure                                                                          | `selection` |     | ✅    |                                  |
| `profiling_enabled_until`                            | Profiling enabled until                                                                         | `datetime`  |     | ✅    |                                  |
| `purchase_lock_date`                                 | Purchases Lock Date                                                                             | `date`      |     |       |                                  |
| `purchase_tax_id`                                    | Default Purchase Tax                                                                            | `many2one`  |     |       | account.tax                      |
| `qr_code`                                            | Display SEPA QR-code                                                                            | `boolean`   |     |       |                                  |
| `quick_edit_mode`                                    | Quick encoding                                                                                  | `selection` |     |       |                                  |
| `quotation_validity_days`                            | Default Quotation Validity                                                                      | `integer`   |     |       |                                  |
| `rate_provider_selection`                            | Exchange Rate Provider                                                                          | `selection` |     |       |                                  |
| `recaptcha_min_score`                                | Minimum score                                                                                   | `float`     |     | ✅    |                                  |
| `recaptcha_private_key`                              | Secret Key                                                                                      | `char`      |     | ✅    |                                  |
| `recaptcha_public_key`                               | Site Key                                                                                        | `char`      |     | ✅    |                                  |
| `refresh_token`                                      | Refresh Token                                                                                   | `char`      |     | ✅    |                                  |
| `replenish_on_order`                                 | Replenish on Order (MTO)                                                                        | `boolean`   |     |       |                                  |
| `report_footer`                                      | Custom Report Footer                                                                            | `html`      |     |       |                                  |
| `resource_calendar_id`                               | Company Working Hours                                                                           | `many2one`  |     |       | resource.calendar                |
| `restrictive_audit_trail`                            | Restricted Audit Trail                                                                          | `boolean`   |     |       |                                  |
| `restrict_template_rendering`                        | Restrict Template Rendering                                                                     | `boolean`   |     | ✅    |                                  |
| `sale_lock_date`                                     | Sales Lock Date                                                                                 | `date`      |     |       |                                  |
| `salesperson_id`                                     | Salesperson                                                                                     | `many2one`  |     |       | res.users                        |
| `salesteam_id`                                       | Sales Team                                                                                      | `many2one`  |     |       | crm.team                         |
| `sale_tax_id`                                        | Default Sale Tax                                                                                | `many2one`  |     |       | account.tax                      |
| `secure_qr_code`                                     | Secure Qr Code                                                                                  | `selection` |     | ✅    |                                  |
| `security_lead`                                      | Security Lead Time                                                                              | `float`     |     |       |                                  |
| `send_abandoned_cart_email`                          | Abandoned Email                                                                                 | `boolean`   |     |       |                                  |
| `sfu_server_key`                                     | SFU Server key                                                                                  | `char`      |     | ✅    |                                  |
| `sfu_server_url`                                     | SFU Server URL                                                                                  | `char`      |     | ✅    |                                  |
| `shared_user_account`                                | Shared Customer Accounts                                                                        | `boolean`   |     |       |                                  |
| `show_blacklist_buttons`                             | Blacklist Option when Unsubscribing                                                             | `boolean`   |     | ✅    |                                  |
| `show_branding_in_footer`                            | Show Branding In Footer                                                                         | `boolean`   |     | ✅    |                                  |
| `show_effect`                                        | Show Effect                                                                                     | `boolean`   |     | ✅    |                                  |
| `show_line_subtotals_tax_selection`                  | Line Subtotals Tax Display                                                                      | `selection` |     |       |                                  |
| `show_sale_receipts`                                 | Sale Receipt                                                                                    | `boolean`   |     | ✅    |                                  |
| `snailmail_color`                                    | Print In Color                                                                                  | `boolean`   |     |       |                                  |
| `snailmail_cover`                                    | Add a Cover Page                                                                                | `boolean`   |     |       |                                  |
| `snailmail_cover_readonly`                           | Snailmail Cover Readonly                                                                        | `boolean`   |     |       |                                  |
| `snailmail_duplex`                                   | Print Both sides                                                                                | `boolean`   |     |       |                                  |
| `social_default_image`                               | Default Social Share Image                                                                      | `binary`    |     |       |                                  |
| `stock_confirmation_type`                            | Stock Text Validation type                                                                      | `selection` |     |       |                                  |
| `stock_move_email_validation`                        | Email Confirmation picking                                                                      | `boolean`   |     |       |                                  |
| `stock_sms_confirmation_template_id`                 | SMS Template                                                                                    | `many2one`  |     |       | sms.template                     |
| `stock_text_confirmation`                            | Stock Text Validation with stock move                                                           | `boolean`   |     |       |                                  |
| `synchronization_batch_size`                         | Batch Size                                                                                      | `integer`   |     |       |                                  |
| `synchronization_frequency`                          | Synchronization Frequency                                                                       | `selection` |     |       |                                  |
| `tax_calculation_rounding_method`                    | Tax calculation rounding method                                                                 | `selection` |     |       |                                  |
| `tax_cash_basis_journal_id`                          | Tax Cash Basis Journal                                                                          | `many2one`  |     |       | account.journal                  |
| `tax_exigibility`                                    | Cash Basis                                                                                      | `boolean`   |     |       |                                  |
| `tax_lock_date`                                      | Tax Lock Date                                                                                   | `date`      |     |       |                                  |
| `tenor_api_key`                                      | Tenor API key                                                                                   | `char`      |     | ✅    |                                  |
| `terms_type`                                         | Terms & Conditions format                                                                       | `selection` |     |       |                                  |
| `transfer_account_id`                                | Internal Transfer                                                                               | `many2one`  |     |       | account.account                  |
| `twilio_account_sid`                                 | Account SID                                                                                     | `char`      |     | ✅    |                                  |
| `twilio_account_token`                               | Account Auth Token                                                                              | `char`      |     | ✅    |                                  |
| `unsplash_access_key`                                | Access Key                                                                                      | `char`      |     | ✅    |                                  |
| `unsplash_app_id`                                    | Application ID                                                                                  | `char`      |     | ✅    |                                  |
| `use_event_barcode`                                  | Use Event Barcode                                                                               | `boolean`   |     | ✅    |                                  |
| `use_google_maps_static_api`                         | Google Maps static API                                                                          | `boolean`   |     | ✅    |                                  |
| `use_invoice_terms`                                  | Default Terms & Conditions                                                                      | `boolean`   |     | ✅    |                                  |
| `use_project`                                        | Use Projects                                                                                    | `boolean`   |     | ✅    |                                  |
| `use_security_lead`                                  | Security Lead Time for Sales                                                                    | `boolean`   |     | ✅    |                                  |
| `use_sfu_server`                                     | Use SFU server                                                                                  | `boolean`   |     | ✅    |                                  |
| `use_twilio_rtc_servers`                             | Use Twilio ICE servers                                                                          | `boolean`   |     | ✅    |                                  |
| `use_website_form`                                   | Website Form                                                                                    | `boolean`   |     | ✅    |                                  |
| `verify_date`                                        | Verify Date                                                                                     | `char`      |     |       |                                  |
| `web_app_name`                                       | Web App Name                                                                                    | `char`      |     | ✅    |                                  |
| `website_block_third_party_domains`                  | Block 3rd-party domains                                                                         | `boolean`   |     |       |                                  |
| `website_company_id`                                 | Website Company                                                                                 | `many2one`  |     |       | res.company                      |
| `website_cookies_bar`                                | Cookies Bar                                                                                     | `boolean`   |     |       |                                  |
| `website_default_lang_code`                          | Default language code                                                                           | `char`      |     |       |                                  |
| `website_default_lang_id`                            | Default language                                                                                | `many2one`  |     |       | res.lang                         |
| `website_domain`                                     | Website Domain                                                                                  | `char`      |     |       |                                  |
| `website_homepage_url`                               | Homepage Url                                                                                    | `char`      |     |       |                                  |
| `website_id`                                         | website                                                                                         | `many2one`  |     | ✅    | website                          |
| `website_language_count`                             | Number of languages                                                                             | `integer`   |     |       |                                  |
| `website_logo`                                       | Website Logo                                                                                    | `binary`    |     |       |                                  |
| `website_name`                                       | Website Name                                                                                    | `char`      |     |       |                                  |
| `website_sale_contact_us_button_url`                 | Button Url                                                                                      | `char`      |     |       |                                  |
| `website_sale_prevent_zero_price_sale`               | Prevent Sale of Zero Priced Product                                                             | `boolean`   |     |       |                                  |
| `website_warehouse_id`                               | Warehouse                                                                                       | `many2one`  |     |       | stock.warehouse                  |
| `whatsapp_business_id`                               | Business Account                                                                                | `many2one`  |     | ✅    | whatsapp.business                |
| `work_permit_expiration_notice_period`               | Work Permit Expiry Notice Period                                                                | `integer`   |     |       |                                  |
| `write_date`                                         | Last Updated on                                                                                 | `datetime`  |     | ✅    |                                  |
| `write_uid`                                          | Last Updated by                                                                                 | `many2one`  |     | ✅    | res.users                        |

**Access Rights:**

| Name                       | Group                | Perms   |
| -------------------------- | -------------------- | ------- |
| access.res.config.settings | Role / Administrator | `R/W/C` |

### 🗃️ `fleet.vehicle.assignation.log` — Drivers history on a vehicle

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label                 | Type       | Req | Store | Relation      |
| -------------------- | --------------------- | ---------- | --- | ----- | ------------- |
| `attachment_number`  | Number of Attachments | `integer`  |     |       |               |
| `create_date`        | Created on            | `datetime` |     | ✅    |               |
| `create_uid`         | Created by            | `many2one` |     | ✅    | res.users     |
| `date_end`           | End Date              | `date`     |     | ✅    |               |
| `date_start`         | Start Date            | `date`     |     | ✅    |               |
| `display_name`       | Display Name          | `char`     |     |       |               |
| `driver_employee_id` | Driver (Employee)     | `many2one` |     | ✅    | hr.employee   |
| `driver_id`          | Driver                | `many2one` | ✅  | ✅    | res.partner   |
| `id`                 | ID                    | `integer`  |     | ✅    |               |
| `vehicle_id`         | Vehicle               | `many2one` | ✅  | ✅    | fleet.vehicle |
| `write_date`         | Last Updated on       | `datetime` |     | ✅    |               |
| `write_uid`          | Last Updated by       | `many2one` |     | ✅    | res.users     |

**Access Rights:**

| Name                                           | Group                                | Perms     |
| ---------------------------------------------- | ------------------------------------ | --------- |
| fleet_vehicle_assignation_log fleet_group_user | Fleet / Officer: Manage all vehicles | `R/W/C/D` |

### 🗃️ `fleet.vehicle.cost.report` — Fleet Analysis Report

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label        | Type        | Req | Store | Relation      |
| -------------- | ------------ | ----------- | --- | ----- | ------------- |
| `company_id`   | Company      | `many2one`  |     | ✅    | res.company   |
| `cost`         | Cost         | `float`     |     | ✅    |               |
| `cost_type`    | Cost Type    | `selection` |     | ✅    |               |
| `date_start`   | Date         | `date`      |     | ✅    |               |
| `display_name` | Display Name | `char`      |     |       |               |
| `driver_id`    | Driver       | `many2one`  |     | ✅    | res.partner   |
| `fuel_type`    | Fuel         | `char`      |     | ✅    |               |
| `id`           | ID           | `integer`   |     | ✅    |               |
| `name`         | Vehicle Name | `char`      |     | ✅    |               |
| `vehicle_id`   | Vehicle      | `many2one`  |     | ✅    | fleet.vehicle |
| `vehicle_type` | Vehicle Type | `selection` |     | ✅    |               |

**Access Rights:**

| Name                                   | Group                 | Perms |
| -------------------------------------- | --------------------- | ----- |
| fleet_vehicle_cost_report_access_right | Fleet / Administrator | `R`   |

**Record Rules:**

- **Costs Analysis: Multi Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `fleet.vehicle.odometer.report` — Fleet Odometer Analysis Report

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label          | Type        | Req | Store | Relation                     |
| ---------------- | -------------- | ----------- | --- | ----- | ---------------------------- |
| `category_id`    | Category       | `many2one`  |     |       | fleet.vehicle.model.category |
| `display_name`   | Display Name   | `char`      |     |       |                              |
| `fuel_type`      | Fuel Type      | `selection` |     |       |                              |
| `id`             | ID             | `integer`   |     | ✅    |                              |
| `mileage_delta`  | Mileage Delta  | `float`     |     | ✅    |                              |
| `model_id`       | Model          | `many2one`  |     |       | fleet.vehicle.model          |
| `odometer_value` | Odometer Value | `float`     |     | ✅    |                              |
| `recorded_date`  | Date           | `date`      |     | ✅    |                              |
| `vehicle_id`     | Vehicle        | `many2one`  |     | ✅    | fleet.vehicle                |

**Access Rights:**

| Name                                       | Group                 | Perms     |
| ------------------------------------------ | --------------------- | --------- |
| fleet_vehicle_odometer_report_access_right | Fleet / Administrator | `R/W/C/D` |

### 🗃️ `fleet.service.type` — Fleet Service Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation  |
| -------------- | --------------- | ----------- | --- | ----- | --------- |
| `category`     | Category        | `selection` | ✅  | ✅    |           |
| `create_date`  | Created on      | `datetime`  |     | ✅    |           |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users |
| `display_name` | Display Name    | `char`      |     |       |           |
| `id`           | ID              | `integer`   |     | ✅    |           |
| `name`         | Name            | `char`      | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                            | Group                                | Perms     |
| ------------------------------- | ------------------------------------ | --------- |
| fleet_service_type_access_right | Fleet / Officer: Manage all vehicles | `R`       |
| fleet_service_type_access_right | Fleet / Administrator                | `R/W/C/D` |

### 🗃️ `fleet.vehicle.odometer` — Odometer log for a vehicle

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label             | Type        | Req | Store | Relation      |
| -------------------- | ----------------- | ----------- | --- | ----- | ------------- |
| `create_date`        | Created on        | `datetime`  |     | ✅    |               |
| `create_uid`         | Created by        | `many2one`  |     | ✅    | res.users     |
| `date`               | Date              | `date`      |     | ✅    |               |
| `display_name`       | Display Name      | `char`      |     |       |               |
| `driver_employee_id` | Driver (Employee) | `many2one`  |     |       | hr.employee   |
| `driver_id`          | Driver            | `many2one`  |     | ✅    | res.partner   |
| `id`                 | ID                | `integer`   |     | ✅    |               |
| `name`               | Name              | `char`      |     | ✅    |               |
| `unit`               | Unit              | `selection` |     |       |               |
| `value`              | Odometer Value    | `float`     |     | ✅    |               |
| `vehicle_id`         | Vehicle           | `many2one`  | ✅  | ✅    | fleet.vehicle |
| `write_date`         | Last Updated on   | `datetime`  |     | ✅    |               |
| `write_uid`          | Last Updated by   | `many2one`  |     | ✅    | res.users     |

**Access Rights:**

| Name                                | Group                                | Perms     |
| ----------------------------------- | ------------------------------------ | --------- |
| fleet_vehicle_odometer_access_right | Fleet / Officer: Manage all vehicles | `R/W/C/D` |

**Record Rules:**

- **Administrator has all rights on vehicle's vehicle's odometer** (21) `R/W/C/D`
- **Fleet odometer: Multi Company** (Global) `R/W/C/D`
  - Domain: `[('vehicle_id.company_id', 'in', company_ids + [False])]`

### 🗃️ `fleet.vehicle.send.mail` — Send mails to Drivers

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                     | Label                                    | Type        | Req | Store | Relation      |
| ------------------------- | ---------------------------------------- | ----------- | --- | ----- | ------------- |
| `attachment_ids`          | Attachments                              | `many2many` |     | ✅    | ir.attachment |
| `author_id`               | Author                                   | `many2one`  | ✅  | ✅    | res.partner   |
| `body`                    | Contents                                 | `html`      |     | ✅    |               |
| `body_has_template_value` | Body content is the same as the template | `boolean`   |     |       |               |
| `can_edit_body`           | Can Edit Body                            | `boolean`   |     |       |               |
| `create_date`             | Created on                               | `datetime`  |     | ✅    |               |
| `create_uid`              | Created by                               | `many2one`  |     | ✅    | res.users     |
| `display_name`            | Display Name                             | `char`      |     |       |               |
| `id`                      | ID                                       | `integer`   |     | ✅    |               |
| `is_mail_template_editor` | Is Editor                                | `boolean`   |     |       |               |
| `lang`                    | Language                                 | `char`      |     | ✅    |               |
| `render_model`            | Rendering Model                          | `char`      |     |       |               |
| `subject`                 | Subject                                  | `char`      |     | ✅    |               |
| `template_id`             | Mail Template                            | `many2one`  |     | ✅    | mail.template |
| `vehicle_ids`             | Vehicles                                 | `many2many` | ✅  | ✅    | fleet.vehicle |
| `write_date`              | Last Updated on                          | `datetime`  |     | ✅    |               |
| `write_uid`               | Last Updated by                          | `many2one`  |     | ✅    | res.users     |

**Access Rights:**

| Name                           | Group                 | Perms   |
| ------------------------------ | --------------------- | ------- |
| access.fleet.vehicle.send.mail | Fleet / Administrator | `R/W/C` |

### 🗃️ `fleet.vehicle.state` — Vehicle Status

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label            | Type       | Req | Store | Relation  |
| -------------- | ---------------- | ---------- | --- | ----- | --------- |
| `create_date`  | Created on       | `datetime` |     | ✅    |           |
| `create_uid`   | Created by       | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name     | `char`     |     |       |           |
| `fold`         | Folded in Kanban | `boolean`  |     | ✅    |           |
| `id`           | ID               | `integer`  |     | ✅    |           |
| `name`         | Name             | `char`     | ✅  | ✅    |           |
| `sequence`     | Sequence         | `integer`  |     | ✅    |           |
| `write_date`   | Last Updated on  | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by  | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                             | Group                                | Perms     |
| -------------------------------- | ------------------------------------ | --------- |
| fleet_vehicle_state_access_right | Fleet / Officer: Manage all vehicles | `R`       |
| fleet_vehicle_state_access_right | Fleet / Administrator                | `R/W/C/D` |

### 🗃️ `fleet.vehicle.tag` — Vehicle Tag

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `color`        | Color           | `integer`  |     | ✅    |           |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `name`         | Tag Name        | `char`     | ✅  | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                           | Group                                | Perms     |
| ------------------------------ | ------------------------------------ | --------- |
| fleet_vehicle_tag_access_right | Fleet / Officer: Manage all vehicles | `R`       |
| fleet_vehicle_tag_access_right | Fleet / Administrator                | `R/W/C/D` |
