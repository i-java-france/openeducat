---
title: "OpenEduCat Cbcs"
module: "openeducat_cbcs"
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

# 🟢 OpenEduCat Cbcs

> **Module:** `openeducat_cbcs` | **Version:** `19.0.1.0` **Category:** Education |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_admission]] [[openeducat_admission_enterprise]]
[[openeducat_core_enterprise]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `SIS/Configuration/Course Management/Course Credit`

### Views

- `* INHERIT course_registration_form_inherit_credit (qweb)`
- `* INHERIT op.course.optional.inherited.form (form)`
- `course.credit.form (form)`
- `course.credit.list (list)`
- `course.credit.search (search)`
- `sem.credit.form (form)`
- `sem.credit.list (list)`
- `sem.credit.search (search)`
- `subject.credit.form (form)`
- `subject.credit.list (list)`
- `subject.credit.search (search)`

### Reports

_none_

## 🛠️ Technical Documentation

**5 model(s) defined by this module:**

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

### 🗃️ `course.credit` — Course Credit

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation         |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ---------------- |
| `academic_year_id`           | Academic Year          | `many2one`  |     | ✅    | op.academic.year |
| `all_academic`               | Credit System          | `selection` |     | ✅    |                  |
| `course_id`                  | Course                 | `many2one`  | ✅  | ✅    | op.course        |
| `course_plan_id`             | Course Plan            | `many2one`  |     | ✅    | op.course.plan   |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                  |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users        |
| `display_name`               | Display Name           | `char`      |     |       |                  |
| `has_message`                | Has Message            | `boolean`   |     |       |                  |
| `id`                         | ID                     | `integer`   |     | ✅    |                  |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                  |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers   |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                  |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                  |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                  |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message     |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                  |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                  |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                  |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner      |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating    |
| `sem_credit_line_id`         | Semester Credit        | `one2many`  |     | ✅    | sem.credit       |
| `subject_credit`             | Subject Credit         | `one2many`  |     | ✅    | subject.credit   |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message     |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                  |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                 | Group               | Perms     |
| -------------------- | ------------------- | --------- |
| access_course_credit | Admission / Manager | `R/W/C/D` |
| access_course_credit | Admission / User    | `R/W/C`   |

### 🗃️ `op.course.plan` — Course Plan

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                   | Type        | Req | Store | Relation           |
| ---------------------------- | ----------------------- | ----------- | --- | ----- | ------------------ |
| `academic_plan_id`           | Academic Plan           | `many2one`  |     | ✅    | op.academic.plan   |
| `academic_term_id`           | Academic Term           | `many2one`  | ✅  | ✅    | op.academic.term   |
| `copo_line_ids`              | CO PO Lines             | `one2many`  |     | ✅    | copo.lines         |
| `copo_lines_count`           | CO PO Lines Count       | `integer`   |     |       |                    |
| `course_credit`              | Course Credit           | `one2many`  |     | ✅    | course.credit      |
| `course_id`                  | Course                  | `many2one`  | ✅  | ✅    | op.course          |
| `course_ids`                 | Courses                 | `many2many` |     | ✅    | op.course          |
| `create_date`                | Created on              | `datetime`  |     | ✅    |                    |
| `create_uid`                 | Created by              | `many2one`  |     | ✅    | res.users          |
| `display_name`               | Display Name            | `char`      |     |       |                    |
| `fees_term_id`               | Fees Term               | `many2one`  |     | ✅    | op.fees.terms      |
| `has_message`                | Has Message             | `boolean`   |     |       |                    |
| `id`                         | ID                      | `integer`   |     | ✅    |                    |
| `message_attachment_count`   | Attachment Count        | `integer`   |     |       |                    |
| `message_follower_ids`       | Followers               | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`          | Message Delivery error  | `boolean`   |     |       |                    |
| `message_has_error_counter`  | Number of errors        | `integer`   |     |       |                    |
| `message_has_sms_error`      | SMS Delivery error      | `boolean`   |     |       |                    |
| `message_ids`                | Messages                | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`        | Is Follower             | `boolean`   |     |       |                    |
| `message_needaction`         | Action Needed           | `boolean`   |     |       |                    |
| `message_needaction_counter` | Number of Actions       | `integer`   |     |       |                    |
| `message_partner_ids`        | Followers (Partners)    | `many2many` |     |       | res.partner        |
| `name`                       | Name                    | `char`      |     |       |                    |
| `rating_ids`                 | Ratings                 | `one2many`  |     | ✅    | rating.rating      |
| `subject_configure_count`    | Subject Configure Count | `integer`   |     |       |                    |
| `subject_faculty_line`       | Configure Subjects      | `one2many`  |     | ✅    | op.subject.faculty |
| `website_message_ids`        | Website Messages        | `one2many`  |     | ✅    | mail.message       |
| `write_date`                 | Last Updated on         | `datetime`  |     | ✅    |                    |
| `write_uid`                  | Last Updated by         | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                    | Group                | Perms     |
| --------------------------------------- | -------------------- | --------- |
| access_op_course_plan_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_op_course_plan_faculty           | OpenEduCat / User    | `R/W`     |

### 🗃️ `sem.credit` — Semester Credit

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation         |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ---------------- |
| `course_credit_id`           | Course Credit          | `many2one`  |     | ✅    | course.credit    |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                  |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users        |
| `display_name`               | Display Name           | `char`      |     |       |                  |
| `has_message`                | Has Message            | `boolean`   |     |       |                  |
| `id`                         | ID                     | `integer`   |     | ✅    |                  |
| `max_credit`                 | Maximum Credit         | `float`     |     | ✅    |                  |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                  |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers   |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                  |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                  |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                  |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message     |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                  |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                  |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                  |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner      |
| `min_credit`                 | Minimum Credit         | `float`     |     | ✅    |                  |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating    |
| `semester_id`                | Semester               | `many2one`  |     | ✅    | op.academic.term |
| `subject_credit`             | Subject Credit         | `one2many`  |     | ✅    | subject.credit   |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message     |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                  |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name              | Group               | Perms     |
| ----------------- | ------------------- | --------- |
| access_sem_credit | Admission / Manager | `R/W/C/D` |
| access_sem_credit | Admission / User    | `R/W/C`   |

### 🗃️ `subject.credit` — Subject Credit

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field              | Label           | Type       | Req | Store | Relation      |
| ------------------ | --------------- | ---------- | --- | ----- | ------------- |
| `course_credit_id` | Course Credit   | `many2one` |     | ✅    | course.credit |
| `create_date`      | Created on      | `datetime` |     | ✅    |               |
| `create_uid`       | Created by      | `many2one` |     | ✅    | res.users     |
| `credit`           | Credit          | `float`    |     | ✅    |               |
| `display_name`     | Display Name    | `char`     |     |       |               |
| `id`               | ID              | `integer`  |     | ✅    |               |
| `sem_credit_id`    | semester Credit | `many2one` |     | ✅    | sem.credit    |
| `subject_id`       | Subject         | `many2one` |     | ✅    | op.subject    |
| `write_date`       | Last Updated on | `datetime` |     | ✅    |               |
| `write_uid`        | Last Updated by | `many2one` |     | ✅    | res.users     |

**Access Rights:**

| Name                  | Group               | Perms     |
| --------------------- | ------------------- | --------- |
| access_subject_credit | Admission / Manager | `R/W/C/D` |
| access_subject_credit | Admission / User    | `R/W/C`   |
