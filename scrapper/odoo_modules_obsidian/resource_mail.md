---
title: "Resource Mail"
module: "resource_mail"
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

# 🟢 Resource Mail

> **Module:** `resource_mail` | **Version:** `19.0.1.0` **Category:** Technical |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[resource]] [[mail]]

## 📖 Description

Integrate features developped in Mail in use case involving resources instead of users

## 🖥️ UI Components

### Menus

_none_

### Views

_none_

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

### 🗃️ `resource.resource` — Resources

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label                | Type        | Req | Store | Relation          |
| ---------------------- | -------------------- | ----------- | --- | ----- | ----------------- |
| `active`               | Active               | `boolean`   |     | ✅    |                   |
| `avatar_128`           | Avatar 128           | `binary`    |     |       |                   |
| `calendar_id`          | Working Time         | `many2one`  |     | ✅    | resource.calendar |
| `color`                | Color                | `integer`   |     | ✅    |                   |
| `company_id`           | Company              | `many2one`  |     | ✅    | res.company       |
| `create_date`          | Created on           | `datetime`  |     | ✅    |                   |
| `create_uid`           | Created by           | `many2one`  |     | ✅    | res.users         |
| `department_id`        | Department           | `many2one`  |     |       | hr.department     |
| `display_name`         | Display Name         | `char`      |     |       |                   |
| `email`                | Email                | `char`      |     |       |                   |
| `employee_id`          | Employee             | `one2many`  |     | ✅    | hr.employee       |
| `employee_skill_ids`   | Skills               | `one2many`  |     |       | hr.employee.skill |
| `hr_icon_display`      | Hr Icon Display      | `selection` |     |       |                   |
| `id`                   | ID                   | `integer`   |     | ✅    |                   |
| `im_status`            | IM Status            | `char`      |     |       |                   |
| `job_title`            | Job Title            | `char`      |     |       |                   |
| `leave_date_to`        | To Date              | `date`      |     |       |                   |
| `name`                 | Name                 | `char`      | ✅  | ✅    |                   |
| `phone`                | Phone                | `char`      |     |       |                   |
| `resource_type`        | Type                 | `selection` | ✅  | ✅    |                   |
| `share`                | Share User           | `boolean`   |     |       |                   |
| `show_hr_icon_display` | Show Hr Icon Display | `boolean`   |     |       |                   |
| `time_efficiency`      | Efficiency Factor    | `float`     | ✅  | ✅    |                   |
| `tz`                   | Timezone             | `selection` | ✅  | ✅    |                   |
| `user_id`              | User                 | `many2one`  |     | ✅    | res.users         |
| `work_email`           | Work Email           | `char`      |     |       |                   |
| `work_location_id`     | Work Location        | `many2one`  |     |       | hr.work.location  |
| `work_phone`           | Work Phone           | `char`      |     |       |                   |
| `write_date`           | Last Updated on      | `datetime`  |     | ✅    |                   |
| `write_uid`            | Last Updated by      | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                                     | Group                                     | Perms     |
| ---------------------------------------- | ----------------------------------------- | --------- |
| resource.resource.user                   | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.employee.resource.manager             | Employees / Administrator                 | `R/W/C/D` |
| name_resource_resource_back_office_admin | OpenEduCat / Manager                      | `R/W/C`   |
| resource.resource                        | Role / Administrator                      | `R`       |
| resource.resource all                    | Role / User                               | `R`       |

**Record Rules:**

- **resource.resource multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
