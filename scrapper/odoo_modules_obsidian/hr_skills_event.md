---
title: "Skills Events"
module: "hr_skills_event"
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

# 🟢 Skills Events

> **Module:** `hr_skills_event` | **Version:** `19.0.1.0` **Category:** Technical |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[hr_skills]] [[event]]

## 📖 Description

# Events and Skills for HR

This module add completed course events to resume for employees.

## 🖥️ UI Components

### Menus

- `Employees/Learning/Courses/Onsite`

### Views

- `* INHERIT hr.resume.line.form (form)`
- `* INHERIT hr.resume.line.kanban.view.inherited (kanban)`
- `* INHERIT hr.resume.line.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

### 🗃️ `hr.resume.line` — Resume line of an employee

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                    | Label                | Type         | Req | Store | Relation            |
| ------------------------ | -------------------- | ------------ | --- | ----- | ------------------- |
| `avatar_128`             | Avatar 128           | `binary`     |     |       |                     |
| `certificate_file`       | Certificate          | `binary`     |     | ✅    |                     |
| `certificate_filename`   | Certificate Filename | `char`       |     | ✅    |                     |
| `color`                  | Color                | `char`       |     |       |                     |
| `company_id`             | Company              | `many2one`   |     |       | res.company         |
| `course_type`            | Course Type          | `selection`  | ✅  | ✅    |                     |
| `create_date`            | Created on           | `datetime`   |     | ✅    |                     |
| `create_uid`             | Created by           | `many2one`   |     | ✅    | res.users           |
| `date_end`               | Date End             | `date`       |     | ✅    |                     |
| `date_start`             | Date Start           | `date`       | ✅  | ✅    |                     |
| `department_id`          | Department           | `many2one`   |     | ✅    | hr.department       |
| `description`            | Description          | `html`       |     | ✅    |                     |
| `display_name`           | Display Name         | `char`       |     |       |                     |
| `duration`               | Duration             | `integer`    |     | ✅    |                     |
| `employee_id`            | Employee             | `many2one`   | ✅  | ✅    | hr.employee         |
| `event_id`               | Onsite Course        | `many2one`   |     | ✅    | event.event         |
| `expiration_status`      | Expiration Status    | `selection`  |     | ✅    |                     |
| `external_url`           | External URL         | `char`       |     | ✅    |                     |
| `id`                     | ID                   | `integer`    |     | ✅    |                     |
| `is_course`              | Course               | `boolean`    |     |       |                     |
| `line_type_id`           | Type                 | `many2one`   |     | ✅    | hr.resume.line.type |
| `name`                   | Name                 | `char`       | ✅  | ✅    |                     |
| `resume_line_properties` | Properties           | `properties` |     | ✅    |                     |
| `survey_id`              | Certification        | `many2one`   |     | ✅    | survey.survey       |
| `write_date`             | Last Updated on      | `datetime`   |     | ✅    |                     |
| `write_uid`              | Last Updated by      | `many2one`   |     | ✅    | res.users           |

**Access Rights:**

| Name                    | Group                                     | Perms     |
| ----------------------- | ----------------------------------------- | --------- |
| hr.resume.line          | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.resume.line.employee | Role / User                               | `R/W/C/D` |

**Record Rules:**

- **Resume: employee: read all** (1) `R`
  - Domain: `[(1, '=', 1)]`
- **Resume: HR user: all** (49) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Resume: employee: create/write/unlink own** (1) `W/C/D`
  - Domain: `[('employee_id.user_id','=',user.id)]`
