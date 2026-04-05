---
title: "OpenEduCat Subject Material Allocation"
module: "openeducat_subject_material_allocation"
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

# 🟢 OpenEduCat Subject Material Allocation

> **Module:** `openeducat_subject_material_allocation` | **Version:** `19.0.1.0`
> **Category:** Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc
> **Website:** https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_core_enterprise]]

## 📖 Description

## OpenEduCat Subject Material Allocation

### Manage Subject Material Allocation

[![](/openeducat_subject_material_allocation/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module provides the facility of the specific subject material allocation which help
the admin and faculty to add material to the subject so that the student has can
download the material and see their study material by logging into their account.

[Contact Us](https://www.openeducat.org/contactus/)

## Subject Material Allocation

Admin or faculty can Add material to specific subject for the particular student.

![](/openeducat_subject_material_allocation/static/description/adding_study_material.png)

## Study Material

![](/openeducat_subject_material_allocation/static/description/study_material.png)

Admin or faculty can add material of subjects for, make sure student's have the access
of that subject. admin & faculty can add attachments and student can view and download
by the portal.

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT Portal layout : Study Material (qweb)`
- `* INHERIT Show Study Material (qweb)`
- `portal_student_subject_details (qweb)`
- `portal_student_subject_material_details (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

### 🗃️ `op.subject` — Subject Material Allocation

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                       | Type        | Req | Store | Relation          |
| ---------------------------- | --------------------------- | ----------- | --- | ----- | ----------------- |
| `active`                     | Active                      | `boolean`   |     | ✅    |                   |
| `assignment_count`           | Assignment Count            | `integer`   |     |       |                   |
| `attachment_ids`             | Attachments                 | `one2many`  |     | ✅    | ir.attachment     |
| `attempted_units`            | Attempted Units             | `selection` |     | ✅    |                   |
| `code`                       | Code                        | `char`      | ✅  | ✅    |                   |
| `company_id`                 | Company                     | `many2one`  |     | ✅    | res.company       |
| `course_id`                  | Course                      | `many2one`  |     | ✅    | op.course         |
| `create_date`                | Created on                  | `datetime`  |     | ✅    |                   |
| `create_uid`                 | Created by                  | `many2one`  |     | ✅    | res.users         |
| `credit_point`               | Credit                      | `float`     |     | ✅    |                   |
| `default_template`           | Use Default Course Template | `boolean`   |     | ✅    |                   |
| `department_id`              | Department                  | `many2one`  |     | ✅    | op.department     |
| `display_name`               | Display Name                | `char`      |     |       |                   |
| `grade_template_ids`         | Grade Template              | `many2many` | ✅  | ✅    | op.grade.template |
| `grade_weightage`            | Grade Weightage             | `float`     |     | ✅    |                   |
| `has_message`                | Has Message                 | `boolean`   |     |       |                   |
| `id`                         | ID                          | `integer`   |     | ✅    |                   |
| `message_attachment_count`   | Attachment Count            | `integer`   |     |       |                   |
| `message_follower_ids`       | Followers                   | `one2many`  |     | ✅    | mail.followers    |
| `message_has_error`          | Message Delivery error      | `boolean`   |     |       |                   |
| `message_has_error_counter`  | Number of errors            | `integer`   |     |       |                   |
| `message_has_sms_error`      | SMS Delivery error          | `boolean`   |     |       |                   |
| `message_ids`                | Messages                    | `one2many`  |     | ✅    | mail.message      |
| `message_is_follower`        | Is Follower                 | `boolean`   |     |       |                   |
| `message_needaction`         | Action Needed               | `boolean`   |     |       |                   |
| `message_needaction_counter` | Number of Actions           | `integer`   |     |       |                   |
| `message_partner_ids`        | Followers (Partners)        | `many2many` |     |       | res.partner       |
| `name`                       | Name                        | `char`      | ✅  | ✅    |                   |
| `parent_sub_id`              | Parent Subject              | `many2one`  |     | ✅    | op.subject        |
| `rating_ids`                 | Ratings                     | `one2many`  |     | ✅    | rating.rating     |
| `subject_credit`             | Credit Hours                | `float`     |     | ✅    |                   |
| `subject_type`               | Subject Type                | `selection` | ✅  | ✅    |                   |
| `timetable_count`            | Timetable Count             | `integer`   |     |       |                   |
| `type`                       | Type                        | `selection` | ✅  | ✅    |                   |
| `website_message_ids`        | Website Messages            | `one2many`  |     | ✅    | mail.message      |
| `write_date`                 | Last Updated on             | `datetime`  |     | ✅    |                   |
| `write_uid`                  | Last Updated by             | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                              | Group                | Perms     |
| --------------------------------- | -------------------- | --------- |
| name_op_subject_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| name_op_subject_faculty           | OpenEduCat / User    | `R`       |
| name_op_subject_library           | Library / Manager    | `R`       |
| name_op_subject_parent            | Role / Portal        | `R`       |

**Record Rules:**

- **Subject multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`
- **Subject multi-department** (Global) `R/W/C/D`
  - Domain:
    `['|','|',('department_id','=',False),('department_id','child_of',[user.dept_id.id]),('department_id','in',user.department_ids.ids)]`
