---
title: "OpenEduCat Notice Board Enterprise"
module: "openeducat_notice_board_enterprise"
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

# 🟢 OpenEduCat Notice Board Enterprise

> **Module:** `openeducat_notice_board_enterprise` | **Version:** `19.0.1.0`
> **Category:** Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc
> **Website:** https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_core_enterprise]] [[openeducat_parent]]

## 📖 Description

## OpenEduCat Notice Board

### Create Notices/Circulars, Publish it

[![](/openeducat_notice_board_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module allows you to manage the notices/circulars easily. Admin/Faculty can create
notice/circular, publish it & students and parents can view that on their portal.

[Contact Us](https://www.openeducat.org/contactus/)

## Create Group

Admin and Faculty can make group of Students,Parents and Faculties for send Notice or
Circular easily.

![](/openeducat_notice_board_enterprise/static/description/notice_group.png)

## Create Circular

![](/openeducat_notice_board_enterprise/static/description/create_circular.png)

Admin can create a circular for students , Faculties or Parents and can send them via
email and sms. Faculty can Create and send circular to particular group of students ,
Course, batch and class about their academics through system.

## Create Notice

Admin can create notices for students, Faculties or Parents and can send them via email
and sms. Faculty can Create and Send notices to particular group of students , Course,
batch and class about their academics through system .

![](/openeducat_notice_board_enterprise/static/description/create_notice.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Notice Board`
- `Notice Board/Configuration`
- `Notice Board/Configuration/Circular Types`
- `Notice Board/Configuration/Groups`
- `Notice Board/Configuration/Settings`
- `Notice Board/My Circular`
- `Notice Board/My Circular/Circulars`
- `Notice Board/My Notice`
- `Notice Board/My Notice/Notices`

### Views

- `* INHERIT Portal layout : Notice Board (qweb)`
- `* INHERIT Show Notice Board (qweb)`
- `* INHERIT notice_notification_inherit (qweb)`
- `* INHERIT op.batch.notice.board.list (list)`
- `* INHERIT op.course.notice.board.list (list)`
- `Circular Type Form View (form)`
- `Circular Type Tree View (list)`
- `Notice Group Form View (form)`
- `Notice Group Tree View (list)`
- `OP Notice Form View (form)`
- `OP Notice Kanban View (kanban)`
- `OP Notice Tree View (list)`
- `Op Circular Form View (form)`
- `Op Circular Kanban View (kanban)`
- `Op Circular Tree View (list)`
- `Portal layout : Student Notice Board (qweb)`
- `Portal layout : Student Notice Board (qweb)`
- `Portal layout : Student Notice Board (qweb)`
- `Portal layout : Student Notice Board (qweb)`
- `circular.pivot (pivot)`
- `notice.pivot (pivot)`

### Reports

_none_

## 🛠️ Technical Documentation

**8 model(s) defined by this module:**

### 🗃️ `op.circular` — Circular

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
| `academic_term_id`              | Academic Terms                | `many2one`  | ✅  | ✅    | op.academic.term   |
| `academic_year_id`              | Academic Year                 | `many2one`  | ✅  | ✅    | op.academic.year   |
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
| `circular_number`               | Circular Number               | `char`      |     | ✅    |                    |
| `circular_type_id`              | Circular Type                 | `many2one`  |     | ✅    | op.circular.type   |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company        |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `created_by`                    | Created By                    | `many2one`  |     | ✅    | res.users          |
| `created_date`                  | Created Date                  | `date`      |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `description`                   | Description                   | `html`      | ✅  | ✅    |                    |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `email_cc`                      | Email cc                      | `char`      |     | ✅    |                    |
| `end_date`                      | End Date                      | `date`      |     | ✅    |                    |
| `group_id`                      | Group                         | `many2one`  |     | ✅    | op.notice.group    |
| `group_ids`                     | Groups                        | `many2many` |     | ✅    | op.notice.group    |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `high_priority`                 | Priority                      | `selection` |     | ✅    |                    |
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
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `start_date`                    | Start Date                    | `date`      | ✅  | ✅    |                    |
| `state`                         | Status                        | `selection` |     | ✅    |                    |
| `subject`                       | Subject                       | `char`      | ✅  | ✅    |                    |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                    | Group                  | Perms     |
| ----------------------- | ---------------------- | --------- |
| access_op_circular      | Notice Board / Manager | `R/W/C/D` |
| access_op_circular_user | Notice Board / User    | `R/W`     |

**Record Rules:**

- **Faculty Circular View** (145) `R/W/C/D`
  - Domain:
    `['|', ('created_by', '=', user.id),('group_ids.faculty_ids.emp_id.user_id', '=', user.id)]`
- **Admin Circular View** (2) `R/W/C/D`
  - Domain: `[(1, '=',1)]`
- **Circular multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('group_ids.company_id','=',False),'&',('group_ids.company_id','in',company_ids),'|',('group_ids.company_id','child_of',[user.company_id.id]),('group_ids.company_id','in',user.company_ids.ids)]     `

### 🗃️ `op.course` — Course

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                         | Type        | Req | Store | Relation               |
| -------------------------------- | ----------------------------- | ----------- | --- | ----- | ---------------------- |
| `active`                         | Active                        | `boolean`   |     | ✅    |                        |
| `activity_calendar_event_id`     | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event         |
| `activity_date_deadline`         | Next Activity Deadline        | `date`      |     |       |                        |
| `activity_exception_decoration`  | Activity Exception Decoration | `selection` |     |       |                        |
| `activity_exception_icon`        | Icon                          | `char`      |     |       |                        |
| `activity_ids`                   | Activities                    | `one2many`  |     | ✅    | mail.activity          |
| `activity_state`                 | Activity State                | `selection` |     |       |                        |
| `activity_summary`               | Next Activity Summary         | `char`      |     |       |                        |
| `activity_type_icon`             | Activity Type Icon            | `char`      |     |       |                        |
| `activity_type_id`               | Next Activity Type            | `many2one`  |     |       | mail.activity.type     |
| `activity_user_id`               | Responsible User              | `many2one`  |     |       | res.users              |
| `admission_count`                | Admission Count               | `integer`   |     |       |                        |
| `allow_reviews`                  | Allow Reviews                 | `boolean`   |     | ✅    |                        |
| `announcement_line`              | Announcements                 | `one2many`  |     | ✅    | op.course.announcement |
| `area_id`                        | Area                          | `many2one`  |     |       | op.area                |
| `assignment_count`               | Assignment Count              | `integer`   |     |       |                        |
| `avg_progress`                   | Avg. Progress (%)             | `float`     |     | ✅    |                        |
| `background`                     | Background Image              | `binary`    |     | ✅    |                        |
| `batch_count`                    | Batch Count                   | `integer`   |     |       |                        |
| `can_publish`                    | Can Publish                   | `boolean`   |     |       |                        |
| `category_ids`                   | Categories                    | `many2many` |     | ✅    | op.course.category     |
| `certi_date`                     | Certificate Date              | `boolean`   |     | ✅    |                        |
| `certi_title`                    | Certificate Title             | `char`      |     | ✅    |                        |
| `child_course_count`             | Child Course Count            | `integer`   |     |       |                        |
| `code`                           | Code                          | `char`      | ✅  | ✅    |                        |
| `color`                          | Color Index                   | `integer`   |     | ✅    |                        |
| `company_id`                     | Company                       | `many2one`  |     | ✅    | res.company            |
| `completion_count`               | Completions                   | `integer`   |     | ✅    |                        |
| `content_category_ids`           | Content Modules               | `one2many`  |     |       | op.course.module       |
| `content_content_ids`            | Content                       | `one2many`  |     |       | op.course.module       |
| `course_change_fees`             | Course Change Fees            | `boolean`   |     | ✅    |                        |
| `course_image`                   | Course Image                  | `binary`    |     | ✅    |                        |
| `cover_properties`               | Cover Properties              | `text`      |     | ✅    |                        |
| `create_date`                    | Created on                    | `datetime`  |     | ✅    |                        |
| `create_uid`                     | Created by                    | `many2one`  |     | ✅    | res.users              |
| `credit`                         | Course Credit                 | `float`     |     | ✅    |                        |
| `department_id`                  | Department                    | `many2one`  |     | ✅    | op.department          |
| `description`                    | Description                   | `html`      |     | ✅    |                        |
| `display_name`                   | Display Name                  | `char`      |     |       |                        |
| `display_style`                  | Display Style                 | `selection` |     | ✅    |                        |
| `enrollment_line`                | Enrollment                    | `one2many`  |     | ✅    | op.course.enrollment   |
| `evaluation_type`                | Evaluation Type               | `selection` | ✅  | ✅    |                        |
| `faculty_count`                  | Faculty Count                 | `integer`   |     |       |                        |
| `faculty_ids`                    | Instructor                    | `many2many` |     | ✅    | op.faculty             |
| `fees_term_id`                   | Fees Term                     | `many2one`  |     | ✅    | op.fees.terms          |
| `forum_count`                    | Forum Count                   | `integer`   |     | ✅    |                        |
| `forum_id`                       | Forum                         | `many2one`  |     | ✅    | forum.forum            |
| `forum_post_count`               | Forum Post Count              | `integer`   |     | ✅    |                        |
| `forum_post_ids`                 | Forum Post                    | `one2many`  |     | ✅    | forum.post             |
| `forum_reply_count`              | Forum Reply Count             | `integer`   |     | ✅    |                        |
| `full_description`               | Full Description              | `html`      |     | ✅    |                        |
| `grade_scale_id`                 | Final Grade                   | `many2one`  |     | ✅    | op.grade.scale         |
| `grade_template_ids`             | Grade Template                | `many2many` | ✅  | ✅    | op.grade.template      |
| `has_message`                    | Has Message                   | `boolean`   |     |       |                        |
| `id`                             | ID                            | `integer`   |     | ✅    |                        |
| `image_1024`                     | Image 1024                    | `binary`    |     | ✅    |                        |
| `image_128`                      | Image 128                     | `binary`    |     | ✅    |                        |
| `image_1920`                     | Image                         | `binary`    |     | ✅    |                        |
| `image_256`                      | Image 256                     | `binary`    |     | ✅    |                        |
| `image_512`                      | Image 512                     | `binary`    |     | ✅    |                        |
| `invited_users_ids`              | Invited Users                 | `many2many` |     | ✅    | res.users              |
| `is_certificate`                 | Certificate Of Completion?    | `boolean`   |     | ✅    |                        |
| `is_enroll_user`                 | Enroll User                   | `boolean`   |     | ✅    |                        |
| `is_paid`                        | Paid Course?                  | `boolean`   |     | ✅    |                        |
| `is_published`                   | Is Published                  | `boolean`   |     | ✅    |                        |
| `list_price`                     | Price                         | `float`     |     |       |                        |
| `lms_course_count`               | LMS course count              | `char`      |     | ✅    |                        |
| `lms_course_type`                | Course type                   | `selection` | ✅  | ✅    |                        |
| `max_unit_load`                  | Maximum Unit Load             | `float`     |     | ✅    |                        |
| `message_attachment_count`       | Attachment Count              | `integer`   |     |       |                        |
| `message_follower_ids`           | Followers                     | `one2many`  |     | ✅    | mail.followers         |
| `message_has_error`              | Message Delivery error        | `boolean`   |     |       |                        |
| `message_has_error_counter`      | Number of errors              | `integer`   |     |       |                        |
| `message_has_sms_error`          | SMS Delivery error            | `boolean`   |     |       |                        |
| `message_ids`                    | Messages                      | `one2many`  |     | ✅    | mail.message           |
| `message_is_follower`            | Is Follower                   | `boolean`   |     |       |                        |
| `message_needaction`             | Action Needed                 | `boolean`   |     |       |                        |
| `message_needaction_counter`     | Number of Actions             | `integer`   |     |       |                        |
| `message_partner_ids`            | Followers (Partners)          | `many2many` |     |       | res.partner            |
| `min_unit_load`                  | Minimum Unit Load             | `float`     |     | ✅    |                        |
| `module_lines`                   | Module                        | `one2many`  |     | ✅    | op.course.module       |
| `my_activity_date_deadline`      | My Activity Deadline          | `date`      |     |       |                        |
| `name`                           | Name                          | `char`      | ✅  | ✅    |                        |
| `navigation_policy`              | Navigation Policy             | `selection` | ✅  | ✅    |                        |
| `notice_group_id`                | Notice Group                  | `many2one`  |     | ✅    | op.notice.group        |
| `online_course`                  | Online Course                 | `boolean`   |     | ✅    |                        |
| `online_course_created`          | Online Course Created         | `boolean`   |     | ✅    |                        |
| `parent_id`                      | Parent Course                 | `many2one`  |     | ✅    | op.course              |
| `price`                          | Computed Price                | `float`     |     |       |                        |
| `product_id`                     | Product                       | `many2one`  |     | ✅    | product.product        |
| `program_id`                     | Program                       | `many2one`  |     | ✅    | op.program             |
| `rating_avg`                     | Average Rating                | `float`     |     |       |                        |
| `rating_avg_stars`               | Rating Average (Stars)        | `float`     |     |       |                        |
| `rating_avg_text`                | Rating Avg Text               | `selection` |     |       |                        |
| `rating_count`                   | Rating count                  | `integer`   |     |       |                        |
| `rating_ids`                     | Ratings                       | `one2many`  |     | ✅    | rating.rating          |
| `rating_last_feedback`           | Rating Last Feedback          | `text`      |     |       |                        |
| `rating_last_image`              | Rating Last Image             | `binary`    |     |       |                        |
| `rating_last_text`               | Rating Text                   | `selection` |     |       |                        |
| `rating_last_value`              | Rating Last Value             | `float`     |     | ✅    |                        |
| `rating_percentage_satisfaction` | Rating Satisfaction           | `float`     |     |       |                        |
| `reg_fees`                       | Registration Fees             | `boolean`   |     | ✅    |                        |
| `sequence`                       | Sequence                      | `integer`   |     | ✅    |                        |
| `short_desc`                     | Short Description             | `text`      |     | ✅    |                        |
| `specialization_id`              | Specialization                | `many2one`  |     | ✅    | op.specialization      |
| `state`                          | State                         | `selection` |     | ✅    |                        |
| `student_count`                  | Student Count                 | `integer`   |     |       |                        |
| `subject_count`                  | Subject Count                 | `integer`   |     |       |                        |
| `subject_counts`                 | Subject Counts                | `integer`   |     |       |                        |
| `subject_ids`                    | Subject(s)                    | `many2many` |     | ✅    | op.subject             |
| `subject_selection_option`       | Subject Selection             | `selection` |     | ✅    |                        |
| `suggested_course_ids`           | Suggested Course              | `many2many` |     | ✅    | op.course              |
| `survey_ids`                     | Survey                        | `one2many`  |     | ✅    | survey.survey          |
| `tag_ids`                        | Tags                          | `many2many` |     | ✅    | op.course.tag          |
| `timetable_count`                | Timetable Count               | `integer`   |     |       |                        |
| `timing_course_count`            | Timing Course Count           | `integer`   |     |       |                        |
| `total_enrollment`               | Total Enrollment              | `integer`   |     | ✅    |                        |
| `total_modules`                  | Number of Contents            | `integer`   |     | ✅    |                        |
| `total_time`                     | Duration                      | `float`     |     | ✅    |                        |
| `user_id`                        | Responsible                   | `many2one`  |     | ✅    | res.users              |
| `visibility`                     | Visibility Policy             | `selection` | ✅  | ✅    |                        |
| `website_absolute_url`           | Website Absolute URL          | `char`      |     |       |                        |
| `website_id`                     | Website                       | `many2one`  |     | ✅    | website                |
| `website_message_ids`            | Website Messages              | `one2many`  |     | ✅    | mail.message           |
| `website_published`              | Visible on current website    | `boolean`   |     |       |                        |
| `website_url`                    | Website URL                   | `char`      |     |       |                        |
| `write_date`                     | Last Updated on               | `datetime`  |     | ✅    |                        |
| `write_uid`                      | Last Updated by               | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                             | Group                | Perms     |
| -------------------------------- | -------------------- | --------- |
| name_op_course_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| name_op_course_faculty           | OpenEduCat / User    | `R/W/C`   |
| name_op_course_library           | Library / Manager    | `R`       |
| access_op_course                 | LMS / Manager        | `R/W/C/D` |
| access_op_course_user            | LMS / User           | `R/W/C`   |
| access_op_course_portal          | Role / Portal        | `R/W`     |
| name_op_course_parent            | Role / Portal        | `R`       |
| access_op_course_public          | Role / Public        | `R`       |
| name_op_dynamic_admission_course | Role / Public        | `R`       |

**Record Rules:**

- **Course multi-company** (1) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `
- **Course multi-department** (1) `R/W/C/D`
  - Domain:
    `         ['|','|',('department_id','=',False),('department_id','child_of',[user.dept_id.id]),('department_id','in',user.department_ids.ids)]     `
- **course multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.notice` — Notice Board

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
| `academic_term_id`              | Academic Terms                | `many2one`  | ✅  | ✅    | op.academic.term   |
| `academic_year_id`              | Academic Year                 | `many2one`  | ✅  | ✅    | op.academic.year   |
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
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company        |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `created_by`                    | Created By                    | `many2one`  |     | ✅    | res.users          |
| `created_date`                  | Created Date                  | `date`      |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `description`                   | Description                   | `html`      | ✅  | ✅    |                    |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `email_cc`                      | Email cc                      | `char`      |     | ✅    |                    |
| `end_date`                      | End Date                      | `date`      |     | ✅    |                    |
| `group_id`                      | Group                         | `many2one`  |     | ✅    | op.notice.group    |
| `group_ids`                     | Groups                        | `many2many` |     | ✅    | op.notice.group    |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `high_priority`                 | Priority                      | `selection` |     | ✅    |                    |
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
| `notice_number`                 | Notice Number                 | `char`      |     | ✅    |                    |
| `notice_template_id`            | Notice Template               | `many2one`  |     | ✅    | mail.template      |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `start_date`                    | Start Date                    | `date`      | ✅  | ✅    |                    |
| `state`                         | Status                        | `selection` |     | ✅    |                    |
| `subject`                       | Subject                       | `char`      | ✅  | ✅    |                    |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                  | Group                  | Perms     |
| --------------------- | ---------------------- | --------- |
| access_op_notice      | Notice Board / Manager | `R/W/C/D` |
| access_op_notice_user | Notice Board / User    | `R/W`     |

**Record Rules:**

- **Faculty Notice View** (145) `R/W/C/D`
  - Domain:
    `['|',('created_by', '=', user.id),('group_ids.faculty_ids.emp_id.user_id', '=', user.id)]`
- **Admin Notice View** (2) `R/W/C/D`
  - Domain: `[(1, '=',1)]`
- **Notice multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('group_ids.company_id','=',False),'&',('group_ids.company_id','in',company_ids),'|',('group_ids.company_id','child_of',[user.company_id.id]),('group_ids.company_id','in',user.company_ids.ids)]     `

### 🗃️ `op.batch` — OpenEduCat Batch

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation        |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | --------------- |
| `active`                     | Active                 | `boolean`   |     | ✅    |                 |
| `code`                       | Code                   | `char`      | ✅  | ✅    |                 |
| `color`                      | Color Index            | `integer`   |     | ✅    |                 |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company     |
| `course_id`                  | Course                 | `many2one`  | ✅  | ✅    | op.course       |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                 |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users       |
| `display_name`               | Display Name           | `char`      |     |       |                 |
| `end_date`                   | End Date               | `date`      | ✅  | ✅    |                 |
| `has_message`                | Has Message            | `boolean`   |     |       |                 |
| `id`                         | ID                     | `integer`   |     | ✅    |                 |
| `kanban_dashboard_graph`     | Kanban Dashboard Graph | `text`      |     |       |                 |
| `lectures_count`             | Lectures Count         | `integer`   |     |       |                 |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                 |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers  |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                 |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                 |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                 |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message    |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                 |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                 |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                 |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner     |
| `name`                       | Name                   | `char`      | ✅  | ✅    |                 |
| `notice_group_id`            | Notice Group           | `many2one`  |     | ✅    | op.notice.group |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating   |
| `start_date`                 | Start Date             | `date`      | ✅  | ✅    |                 |
| `student_count`              | Student Count          | `integer`   |     |       |                 |
| `total_absent_student`       | Total Absent           | `integer`   |     |       |                 |
| `total_present_student`      | Total Present          | `integer`   |     |       |                 |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message    |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                 |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users       |

**Access Rights:**

| Name                            | Group                | Perms     |
| ------------------------------- | -------------------- | --------- |
| name_op_batch_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| name_op_batch_faculty           | OpenEduCat / User    | `R/W/C`   |
| name_op_batch_parent            | Role / Portal        | `R`       |

**Record Rules:**

- **Batch multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.circular.type` — Circular Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `code`         | Code            | `char`     | ✅  | ✅    |             |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Name            | `char`     | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                         | Group                  | Perms     |
| ---------------------------- | ---------------------- | --------- |
| access_op_circular_type      | Notice Board / Manager | `R/W/C/D` |
| access_op_circular_type_user | Notice Board / User    | `R/W`     |

**Record Rules:**

- **Op Circular Type Multi Comp Rule** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `mail.compose.message` — Email composition wizard

> ✳️ Transient (Wizard)

Generic message composition wizard. You may inherit from this wizard at model and view
levels to provide specific features.

        The behavior of the wizard depends on the composition_mode field:
        - 'comment': post on a record.
        - 'mass_mail': wizard in mass mailing mode where the mail details can
            contain template placeholders that will be merged with actual data
            before being sent to each recipient.

**Fields:**

| Field                         | Label                                            | Type        | Req | Store | Relation             |
| ----------------------------- | ------------------------------------------------ | ----------- | --- | ----- | -------------------- |
| `attachment_ids`              | Attachments                                      | `many2many` |     | ✅    | ir.attachment        |
| `author_id`                   | Author                                           | `many2one`  |     | ✅    | res.partner          |
| `auto_delete`                 | Delete Emails                                    | `boolean`   |     | ✅    |                      |
| `auto_delete_keep_log`        | Keep Message Copy                                | `boolean`   |     | ✅    |                      |
| `body`                        | Contents                                         | `html`      |     | ✅    |                      |
| `body_has_template_value`     | Body content is the same as the template         | `boolean`   |     |       |                      |
| `campaign_id`                 | Mass Mailing Campaign                            | `many2one`  |     | ✅    | utm.campaign         |
| `can_edit_body`               | Can Edit Body                                    | `boolean`   |     |       |                      |
| `composition_batch`           | Batch composition                                | `boolean`   |     |       |                      |
| `composition_comment_option`  | Comment Options                                  | `selection` |     | ✅    |                      |
| `composition_mode`            | Composition mode                                 | `selection` |     | ✅    |                      |
| `create_date`                 | Created on                                       | `datetime`  |     | ✅    |                      |
| `create_uid`                  | Created by                                       | `many2one`  |     | ✅    | res.users            |
| `display_name`                | Display Name                                     | `char`      |     |       |                      |
| `email_add_signature`         | Add signature                                    | `boolean`   |     | ✅    |                      |
| `email_from`                  | From                                             | `char`      |     | ✅    |                      |
| `email_layout_xmlid`          | Email Notification Layout                        | `char`      |     | ✅    |                      |
| `force_send`                  | Send mailing or notifications directly           | `boolean`   |     | ✅    |                      |
| `id`                          | ID                                               | `integer`   |     | ✅    |                      |
| `is_mail_template_editor`     | Is Editor                                        | `boolean`   |     |       |                      |
| `lang`                        | Language                                         | `char`      |     | ✅    |                      |
| `mail_activity_type_id`       | Mail Activity Type                               | `many2one`  |     | ✅    | mail.activity.type   |
| `mailing_list_ids`            | Mailing List                                     | `many2many` |     | ✅    | mailing.list         |
| `mail_server_id`              | Outgoing mail server                             | `many2one`  |     | ✅    | ir.mail_server       |
| `marketing_activity_id`       | Marketing Activity                               | `many2one`  |     | ✅    | marketing.activity   |
| `mass_mailing_id`             | Mass Mailing                                     | `many2one`  |     | ✅    | mailing.mailing      |
| `mass_mailing_name`           | Mass Mailing Name                                | `char`      |     | ✅    |                      |
| `message_type`                | Type                                             | `selection` | ✅  | ✅    |                      |
| `model`                       | Related Document Model                           | `char`      |     | ✅    |                      |
| `model_is_thread`             | Thread-Enabled                                   | `boolean`   |     |       |                      |
| `notified_bcc_contains_share` | Is an external partner follower of the document? | `boolean`   |     |       |                      |
| `notify_author`               | Notify Author                                    | `boolean`   |     | ✅    |                      |
| `notify_author_mention`       | Notify Author Mention                            | `boolean`   |     | ✅    |                      |
| `notify_skip_followers`       | Notify Skip Followers                            | `boolean`   |     | ✅    |                      |
| `parent_id`                   | Parent Message                                   | `many2one`  |     | ✅    | mail.message         |
| `partner_ids`                 | Additional Contacts                              | `many2many` |     | ✅    | res.partner          |
| `partner_ids_all_have_email`  | Partner Ids All Have Email                       | `boolean`   |     |       |                      |
| `record_alias_domain_id`      | Alias Domain                                     | `many2one`  |     | ✅    | mail.alias.domain    |
| `record_company_id`           | Company                                          | `many2one`  |     | ✅    | res.company          |
| `render_model`                | Rendering Model                                  | `char`      |     |       |                      |
| `reply_to`                    | Reply To                                         | `char`      |     | ✅    |                      |
| `reply_to_force_new`          | Considers answers as new thread                  | `boolean`   |     | ✅    |                      |
| `reply_to_mode`               | Replies                                          | `selection` |     |       |                      |
| `res_domain`                  | Active domain                                    | `text`      |     | ✅    |                      |
| `res_domain_user_id`          | Responsible                                      | `many2one`  |     | ✅    | res.users            |
| `res_ids`                     | Related Document IDs                             | `text`      |     | ✅    |                      |
| `scheduled_date`              | Scheduled Date                                   | `char`      |     | ✅    |                      |
| `subject`                     | Subject                                          | `char`      |     | ✅    |                      |
| `subtype_id`                  | Subtype                                          | `many2one`  |     | ✅    | mail.message.subtype |
| `subtype_is_log`              | Is a log                                         | `boolean`   |     |       |                      |
| `template_id`                 | Use template                                     | `many2one`  |     | ✅    | mail.template        |
| `template_name`               | Template Name                                    | `char`      |     | ✅    |                      |
| `use_exclusion_list`          | Use Exclusion List                               | `boolean`   |     | ✅    |                      |
| `write_date`                  | Last Updated on                                  | `datetime`  |     | ✅    |                      |
| `write_uid`                   | Last Updated by                                  | `many2one`  |     | ✅    | res.users            |

**Access Rights:**

| Name                        | Group       | Perms   |
| --------------------------- | ----------- | ------- |
| access.mail.compose.message | Role / User | `R/W/C` |

**Record Rules:**

- **Mail Compose Message Rule** (Global) `R/W`
  - Domain: `[('create_uid', '=', user.id)]`

### 🗃️ `op.notice.group` — Groups

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label              | Type        | Req | Store | Relation    |
| -------------------- | ------------------ | ----------- | --- | ----- | ----------- |
| `batch_ids`          | Batches            | `many2many` |     | ✅    | op.batch    |
| `company_id`         | Company            | `many2one`  |     | ✅    | res.company |
| `course_ids`         | Courses            | `many2many` |     | ✅    | op.course   |
| `create_date`        | Created on         | `datetime`  |     | ✅    |             |
| `created_by`         | Created By         | `many2one`  |     | ✅    | res.users   |
| `created_date`       | Created Date       | `date`      |     | ✅    |             |
| `create_uid`         | Created by         | `many2one`  |     | ✅    | res.users   |
| `display_name`       | Display Name       | `char`      |     |       |             |
| `faculty_ids`        | Faculties          | `many2many` |     | ✅    | op.faculty  |
| `faculty_visibility` | Faculty Visibility | `selection` |     | ✅    |             |
| `id`                 | ID                 | `integer`   |     | ✅    |             |
| `name`               | Name               | `char`      | ✅  | ✅    |             |
| `parent_batch_ids`   | Parent Batch       | `many2many` |     | ✅    | op.batch    |
| `parent_course_ids`  | Parent Course      | `many2many` |     | ✅    | op.course   |
| `parent_ids`         | Parents            | `many2many` |     | ✅    | op.parent   |
| `parent_visibility`  | Parent Visibility  | `selection` |     | ✅    |             |
| `student_ids`        | Students           | `many2many` |     | ✅    | op.student  |
| `student_visibility` | Student Visibility | `selection` |     | ✅    |             |
| `write_date`         | Last Updated on    | `datetime`  |     | ✅    |             |
| `write_uid`          | Last Updated by    | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                        | Group                  | Perms     |
| --------------------------- | ---------------------- | --------- |
| access_op_notice_group      | Notice Board / Manager | `R/W/C/D` |
| access_op_notice_group_user | Notice Board / User    | `R/W`     |

**Record Rules:**

- **Notice Group multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `student.notice.circular.read` — Student Notice Read

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `circular_id`  | Circular        | `many2one` |     | ✅    | op.circular |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `is_read`      | Is Read         | `boolean`  |     | ✅    |             |
| `notice_id`    | Notice          | `many2one` |     | ✅    | op.notice   |
| `student_id`   | Student         | `many2one` |     | ✅    | op.student  |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                                     | Group                  | Perms     |
| ---------------------------------------- | ---------------------- | --------- |
| access_student_notice_circular_read      | Notice Board / Manager | `R/W/C/D` |
| access_student_notice_circular_read_user | Notice Board / User    | `R/W`     |
