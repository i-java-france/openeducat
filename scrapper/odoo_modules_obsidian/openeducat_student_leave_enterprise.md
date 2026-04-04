---
title: "OpenEduCat Student Leave Enterprise"
module: "openeducat_student_leave_enterprise"
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

# 🟢 OpenEduCat Student Leave Enterprise

> **Module:** `openeducat_student_leave_enterprise` | **Version:** `19.0.1.0`
> **Category:** Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc
> **Website:** https://www.openeducat.org

## 🔗 Dependencies

[[mail]] [[openeducat_core_enterprise]] [[openeducat_web]]

## 📖 Description

## OpenEduCat Student Leave Request

### Track Student Leave

[![](/openeducat_student_leave_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module aims to manage student's leave requests and keeps account of the leaves of
the students.

[Contact Us](https://www.openeducat.org/contactus/)

## Student Side Leave Request

### Student Leave Request

Student can request leave to a specific Faculty.

![](/openeducat_student_leave_enterprise/static/description/student_leave_request.png)

### Student Leave Request List

![](/openeducat_student_leave_enterprise/static/description/student_leave_request_list.png)

Student can see their Leave Requests with Status.

## Parent Side Leave Request

### Child's Leave Request

Parents can request leave on behalf of their child to a specific faculty.

![](/openeducat_student_leave_enterprise/static/description/parent_leave_request.png)

### Child's Leave Request List

![](/openeducat_student_leave_enterprise/static/description/parent_leave_request_list.png)

Parents can see their children's Leave Requests with Status.

## Admin Side Leave Request

### Leave Type Configure

Only Admin can configure Leave Types.

![](/openeducat_student_leave_enterprise/static/description/leave_type.png)

### Create Leave Request

![](/openeducat_student_leave_enterprise/static/description/admin_leave_request.png)

Admin can create leave request for any student.

### Admin Action

Admin can Approve, Cancel or Take Action on all leave requests.

![](/openeducat_student_leave_enterprise/static/description/admin_request_action.png)

## Faculty Side Leave Request

### Faculty Action

![](/openeducat_student_leave_enterprise/static/description/faculty_action.png)

Faculty can only Approve, Cancel or Take Action on those request to which he/she
assigned to.

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Students/Configuration/Leave Type`
- `Students/General/Student Leave Request`

### Views

- `* INHERIT Portal layout : Subject Registration Form (qweb)`
- `* INHERIT Show Time off (qweb)`
- `* INHERIT notice_notification_inherit (qweb)`
- `Portal layout : Student Leave Request (qweb)`
- `Student Leave Request (qweb)`
- `Student Leave Request Submitted (qweb)`
- `student.leave.request.calender.view (calendar)`
- `student.leave.request.form.view (form)`
- `student.leave.request.kanban.view (kanban)`
- `student.leave.request.search.view (search)`
- `student.leave.request.tree.view (list)`
- `student.leave.type.form (form)`
- `student.leave.type.list (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**2 model(s) defined by this module:**

### 🗃️ `student.leave.request` — Student Leave Request

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
| `approve_date`                  | Approve Date                  | `date`      |     | ✅    |                    |
| `approved_by_id`                | Approved By                   | `many2one`  |     | ✅    | res.users          |
| `attachment_ids`                | Attachments                   | `one2many`  |     | ✅    | ir.attachment      |
| `color`                         | Color Index                   | `char`      |     |       |                    |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company        |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `description`                   | Description                   | `text`      | ✅  | ✅    |                    |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `duration`                      | Duration                      | `char`      |     |       |                    |
| `email_cc`                      | Email cc                      | `char`      |     | ✅    |                    |
| `end_date`                      | End Date                      | `datetime`  | ✅  | ✅    |                    |
| `end_date_only`                 | End Date Only                 | `date`      |     |       |                    |
| `faculty_id`                    | Faculty                       | `many2one`  | ✅  | ✅    | op.faculty         |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
| `image_1920`                    | Image                         | `binary`    |     |       |                    |
| `leave_type`                    | Leave Type                    | `many2one`  | ✅  | ✅    | student.leave.type |
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
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `request_number`                | Request Number                | `char`      |     | ✅    |                    |
| `start_date`                    | Start Date                    | `datetime`  | ✅  | ✅    |                    |
| `start_date_only`               | Start Date Only               | `date`      |     |       |                    |
| `state`                         | Status                        | `selection` |     | ✅    |                    |
| `student_id`                    | Student                       | `many2one`  |     | ✅    | op.student         |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                        | Group                   | Perms     |
| ------------------------------------------- | ----------------------- | --------- |
| access_student_leave_type_back_office_admin | Student Leave / Manager | `R/W/C/D` |
| access_student_leave_request_faculty        | Student Leave / User    | `R/W`     |

**Record Rules:**

- **Faculty Time Off View** (92) `R/W/C/D`
  - Domain: `[('faculty_id.user_id.id', '=', user.id)]`
- **Admin Time Off View** (2) `R/W/C/D`
  - Domain: `[(1, '=',1)]`
- **Student Leave Request line multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `student.leave.type` — Student Leave Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `code`         | code            | `char`     | ✅  | ✅    |             |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Type            | `char`     | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                                        | Group                   | Perms     |
| ------------------------------------------- | ----------------------- | --------- |
| access_student_leave_type_back_office_admin | Student Leave / Manager | `R/W/C/D` |
| access_student_leave_type_faculty           | Student Leave / User    | `R/W`     |

**Record Rules:**

- **Student Leave Type multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `
