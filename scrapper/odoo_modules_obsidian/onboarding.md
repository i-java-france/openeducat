---
title: "Onboarding Toolbox"
module: "onboarding"
state: "installed"
version: "19.0.1.2"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Technical"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 Onboarding Toolbox

> **Module:** `onboarding` | **Version:** `19.0.1.2` **Category:** Technical |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[web]]

## 📖 Description

# This module allows to manage onboardings and their progress

## 🖥️ UI Components

### Menus

- `Settings/Technical/User Interface/Onboardings`
- `Settings/Technical/User Interface/Onboardings Steps`

### Views

- `onboarding.onboarding.step.view.form (form)`
- `onboarding.onboarding.step.view.list (list)`
- `onboarding.onboarding.view.form (form)`
- `onboarding.onboarding.view.list (list)`
- `onboarding_container (qweb)`
- `onboarding_panel (qweb)`
- `onboarding_step (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**4 model(s) defined by this module:**

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

### 🗃️ `onboarding.progress.step` — Onboarding Progress Step Tracker

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label                               | Type        | Req | Store | Relation                   |
| -------------- | ----------------------------------- | ----------- | --- | ----- | -------------------------- |
| `company_id`   | Company                             | `many2one`  |     | ✅    | res.company                |
| `create_date`  | Created on                          | `datetime`  |     | ✅    |                            |
| `create_uid`   | Created by                          | `many2one`  |     | ✅    | res.users                  |
| `display_name` | Display Name                        | `char`      |     |       |                            |
| `id`           | ID                                  | `integer`   |     | ✅    |                            |
| `progress_ids` | Related Onboarding Progress Tracker | `many2many` |     | ✅    | onboarding.progress        |
| `step_id`      | Onboarding Step                     | `many2one`  | ✅  | ✅    | onboarding.onboarding.step |
| `step_state`   | Onboarding Step Progress            | `selection` |     | ✅    |                            |
| `write_date`   | Last Updated on                     | `datetime`  |     | ✅    |                            |
| `write_uid`    | Last Updated by                     | `many2one`  |     | ✅    | res.users                  |

**Access Rights:**

| Name                             | Group                | Perms     |
| -------------------------------- | -------------------- | --------- |
| onboarding.progress.step.manager | Role / Administrator | `R/W/C/D` |
| onboarding.progress.step.user    | Role / User          | `-`       |
| onboarding.progress.step.all     | Everyone             | `-`       |

### 🗃️ `onboarding.progress` — Onboarding Progress Tracker

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label                      | Type        | Req | Store | Relation                 |
| ---------------------- | -------------------------- | ----------- | --- | ----- | ------------------------ |
| `company_id`           | Company                    | `many2one`  |     | ✅    | res.company              |
| `create_date`          | Created on                 | `datetime`  |     | ✅    |                          |
| `create_uid`           | Created by                 | `many2one`  |     | ✅    | res.users                |
| `display_name`         | Display Name               | `char`      |     |       |                          |
| `id`                   | ID                         | `integer`   |     | ✅    |                          |
| `is_onboarding_closed` | Was panel closed?          | `boolean`   |     | ✅    |                          |
| `onboarding_id`        | Related onboarding tracked | `many2one`  | ✅  | ✅    | onboarding.onboarding    |
| `onboarding_state`     | Onboarding progress        | `selection` |     | ✅    |                          |
| `progress_step_ids`    | Progress Steps Trackers    | `many2many` |     | ✅    | onboarding.progress.step |
| `write_date`           | Last Updated on            | `datetime`  |     | ✅    |                          |
| `write_uid`            | Last Updated by            | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                        | Group                | Perms     |
| --------------------------- | -------------------- | --------- |
| onboarding.progress.manager | Role / Administrator | `R/W/C/D` |
| onboarding.progress.user    | Role / User          | `-`       |
| onboarding.progress.all     | Everyone             | `-`       |

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
