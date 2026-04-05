---
title: "OpenEduCat Timetable Enterprise"
module: "openeducat_timetable_enterprise"
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

# 🟢 OpenEduCat Timetable Enterprise

> **Module:** `openeducat_timetable_enterprise` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_lesson]] [[openeducat_timetable]] [[openeducat_core_enterprise]]

## 📖 Description

## OpenEduCat Timetable Enterprise

### Timetable Management

[![](/openeducat_timetable_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module adds feature to manage the session to OpenEduCat.

[Contact Us](https://www.openeducat.org/contactus/)

## Generate Sessions

![](/openeducat_timetable_enterprise/static/description/generate_session.png)

Session contains all details of course, subject, time, day & else. Kanban & calandar
view gives you better look to check it. You can have report for faculty & student for
lectures in the week.

## Sessions

With Generate Session wizard you can easily create session for specific course & batch
with vast date range.

![](/openeducat_timetable_enterprise/static/description/session.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT Portal layout : Timetable (qweb)`
- `* INHERIT Show Timetable (qweb)`
- `* INHERIT generate.time.table.form.inherit (form)`
- `* INHERIT op.academic.plan.form.session (form)`
- `* INHERIT op.batch.form (form)`
- `* INHERIT op.batch.timetable.dashboard.kanban (kanban)`
- `* INHERIT op.course.admission.dashboard.kanban (kanban)`
- `* INHERIT op.course.form (form)`
- `* INHERIT op.department.form (form)`
- `* INHERIT op.faculty.form (form)`
- `* INHERIT op.program.session.dashboard.kanban (kanban)`
- `* INHERIT op.student.course.form.inherit (form)`
- `* INHERIT op.subject.form (form)`
- `* INHERIT op.timetable.inherited.form (form)`
- `* INHERIT op.timetable.inherited.list (list)`
- `* INHERIT op.timetable.inherited.search (search)`
- `* INHERIT op.timetable.onboard (kanban)`
- `* INHERIT op.timing.inherited.list (list)`
- `Timetable (qweb)`
- `op.timing.form (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**14 model(s) defined by this module:**

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

### 🗃️ `op.academic.plan` — OpenEduCat Academic Plan

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ----------------------- |
| `academic_session_count`        | Academic Session count        | `integer`   |     |       |                         |
| `academic_year_id`              | Academic Year                 | `many2one`  | ✅  | ✅    | op.academic.year        |
| `active`                        | Active                        | `boolean`   |     | ✅    |                         |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event          |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                         |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                         |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                         |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity           |
| `activity_state`                | Activity State                | `selection` |     |       |                         |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                         |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                         |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type      |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users               |
| `attendance_sheet_count`        | Attendance Sheet              | `integer`   |     |       |                         |
| `code`                          | Code                          | `char`      | ✅  | ✅    |                         |
| `color`                         | Color Index                   | `integer`   |     | ✅    |                         |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company             |
| `course_configure_count`        | Course Configure Count        | `integer`   |     |       |                         |
| `course_id`                     | Course                        | `many2one`  |     | ✅    | op.course               |
| `course_plan_line`              | Configure Course              | `one2many`  |     | ✅    | op.course.plan          |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                         |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users               |
| `display_name`                  | Display Name                  | `char`      |     |       |                         |
| `duration_tracking`             | Status time                   | `json`      |     |       |                         |
| `end_date`                      | End Date                      | `date`      |     |       |                         |
| `fees_plan_count`               | Student Fees Plan count       | `integer`   |     |       |                         |
| `final_approve_user_id`         | Final Approve User            | `many2one`  |     | ✅    | res.users               |
| `first_approve_user_id`         | First Approve User            | `many2one`  |     | ✅    | res.users               |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                         |
| `id`                            | ID                            | `integer`   |     | ✅    |                         |
| `intake_year_ids`               | Intake Year                   | `many2many` |     | ✅    | op.intake.year          |
| `is_rotting`                    | Rotting                       | `boolean`   |     |       |                         |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                         |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers          |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                         |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                         |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                         |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message            |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                         |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                         |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                         |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner             |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                         |
| `name`                          | Name                          | `char`      |     |       |                         |
| `program_id`                    | Program                       | `many2one`  | ✅  | ✅    | op.program              |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating           |
| `rotting_days`                  | Days Rotting                  | `integer`   |     |       |                         |
| `sequence`                      | Sequence                      | `char`      |     | ✅    |                         |
| `stages_id`                     | Stage                         | `many2one`  |     | ✅    | op.academic.plan.stages |
| `start_date`                    | Start Date                    | `date`      |     |       |                         |
| `state`                         | State                         | `selection` |     | ✅    |                         |
| `student_count`                 | Student Count                 | `integer`   |     |       |                         |
| `student_course_ids`            | Students                      | `one2many`  |     | ✅    | op.student.course       |
| `subject_count`                 | Subject Count                 | `integer`   |     |       |                         |
| `topics_line`                   | Topics Line                   | `one2many`  |     | ✅    | op.topics               |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message            |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                         |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name                                      | Group                | Perms     |
| ----------------------------------------- | -------------------- | --------- |
| access_op_academic_plan_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_op_academic_plan_faculty           | OpenEduCat / User    | `R`       |
| access_op_academic_plan_portal_user       | Role / Portal        | `R/W`     |

**Record Rules:**

- **Academic Plan multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

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

### 🗃️ `op.faculty` — OpenEduCat Faculty

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                       | Label                                               | Type         | Req | Store | Relation                    |
| ------------------------------------------- | --------------------------------------------------- | ------------ | --- | ----- | --------------------------- |
| `account_move_count`                        | Account Move Count                                  | `integer`    |     |       |                             |
| `active`                                    | Active                                              | `boolean`    |     | ✅    |                             |
| `active_lang_count`                         | Active Lang Count                                   | `integer`    |     |       |                             |
| `activity_calendar_event_id`                | Next Activity Calendar Event                        | `many2one`   |     |       | calendar.event              |
| `activity_date_deadline`                    | Next Activity Deadline                              | `date`       |     |       |                             |
| `activity_exception_decoration`             | Activity Exception Decoration                       | `selection`  |     |       |                             |
| `activity_exception_icon`                   | Icon                                                | `char`       |     |       |                             |
| `activity_ids`                              | Activities                                          | `one2many`   |     | ✅    | mail.activity               |
| `activity_state`                            | Activity State                                      | `selection`  |     |       |                             |
| `activity_summary`                          | Next Activity Summary                               | `char`       |     |       |                             |
| `activity_type_icon`                        | Activity Type Icon                                  | `char`       |     |       |                             |
| `activity_type_id`                          | Next Activity Type                                  | `many2one`   |     |       | mail.activity.type          |
| `activity_user_id`                          | Responsible User                                    | `many2one`   |     |       | res.users                   |
| `allowed_department_ids`                    | Allowed Department                                  | `many2many`  |     | ✅    | op.department               |
| `applicant_ids`                             | Applicants                                          | `one2many`   |     |       | hr.applicant                |
| `application_count`                         | Applications                                        | `integer`    |     |       |                             |
| `application_statistics`                    | Stats                                               | `json`       |     |       |                             |
| `assignment_count`                          | Assignment Count                                    | `integer`    |     |       |                             |
| `autopost_bills`                            | Auto-post bills                                     | `selection`  | ✅  |       |                             |
| `available_invoice_template_pdf_report_ids` | Available Invoice Template Pdf Report               | `one2many`   |     |       | ir.actions.report           |
| `available_peppol_eas`                      | Available Peppol Eas                                | `json`       |     |       |                             |
| `avatar_1024`                               | Avatar 1024                                         | `binary`     |     |       |                             |
| `avatar_128`                                | Avatar 128                                          | `binary`     |     |       |                             |
| `avatar_1920`                               | Avatar                                              | `binary`     |     |       |                             |
| `avatar_256`                                | Avatar 256                                          | `binary`     |     |       |                             |
| `avatar_512`                                | Avatar 512                                          | `binary`     |     |       |                             |
| `bank_account_count`                        | Bank                                                | `integer`    |     |       |                             |
| `bank_ids`                                  | Banks                                               | `one2many`   |     |       | res.partner.bank            |
| `barcode`                                   | Barcode                                             | `char`       |     |       |                             |
| `bio_data`                                  | Bio Data                                            | `html`       |     | ✅    |                             |
| `birth_date`                                | Birth Date                                          | `date`       | ✅  | ✅    |                             |
| `blood_group`                               | Blood Group                                         | `selection`  |     | ✅    |                             |
| `buyer_id`                                  | Buyer                                               | `many2one`   |     |       | res.users                   |
| `calendar_last_notif_ack`                   | Last notification marked as read from base Calendar | `datetime`   |     |       |                             |
| `can_publish`                               | Can Publish                                         | `boolean`    |     |       |                             |
| `category_id`                               | Tags                                                | `many2many`  |     |       | res.partner.category        |
| `certifications_company_count`              | Company Certifications Count                        | `integer`    |     |       |                             |
| `certifications_count`                      | Certifications Count                                | `integer`    |     |       |                             |
| `channel_ids`                               | Channels                                            | `many2many`  |     |       | discuss.channel             |
| `channel_member_ids`                        | Channel Member                                      | `one2many`   |     |       | discuss.channel.member      |
| `chatbot_script_ids`                        | Chatbot Script                                      | `one2many`   |     |       | chatbot.script              |
| `child_ids`                                 | Contact                                             | `one2many`   |     |       | res.partner                 |
| `city`                                      | City                                                | `char`       |     |       |                             |
| `code`                                      | Company Code                                        | `char`       |     |       |                             |
| `color`                                     | Color Index                                         | `integer`    |     |       |                             |
| `comment`                                   | Notes                                               | `html`       |     |       |                             |
| `commercial_company_name`                   | Company Name Entity                                 | `char`       |     |       |                             |
| `commercial_partner_id`                     | Commercial Entity                                   | `many2one`   |     |       | res.partner                 |
| `company_id`                                | Company                                             | `many2one`   |     | ✅    | res.company                 |
| `company_name`                              | Company Name                                        | `char`       |     |       |                             |
| `company_registry`                          | Company ID                                          | `char`       |     |       |                             |
| `company_registry_label`                    | Company ID Label                                    | `char`       |     |       |                             |
| `company_registry_placeholder`              | Company Registry Placeholder                        | `char`       |     |       |                             |
| `company_type`                              | Company Type                                        | `selection`  |     |       |                             |
| `complete_name`                             | Complete Name                                       | `char`       |     |       |                             |
| `contact_address`                           | Complete Address                                    | `char`       |     |       |                             |
| `contact_address_inline`                    | Inlined Complete Address                            | `char`       |     |       |                             |
| `contract_ids`                              | Partner Contracts                                   | `one2many`   |     |       | account.analytic.account    |
| `country_code`                              | Country Code                                        | `char`       |     |       |                             |
| `country_id`                                | Country                                             | `many2one`   |     |       | res.country                 |
| `course_count`                              | Course Count                                        | `integer`    |     |       |                             |
| `create_date`                               | Created on                                          | `datetime`   |     | ✅    |                             |
| `create_uid`                                | Created by                                          | `many2one`   |     | ✅    | res.users                   |
| `credit`                                    | Total Receivable                                    | `monetary`   |     |       |                             |
| `credit_limit`                              | Credit Limit                                        | `float`      |     |       |                             |
| `credit_to_invoice`                         | Credit To Invoice                                   | `monetary`   |     |       |                             |
| `currency_id`                               | Currency                                            | `many2one`   |     |       | res.currency                |
| `customer_rank`                             | Customer Rank                                       | `integer`    |     |       |                             |
| `days_sales_outstanding`                    | Days Sales Outstanding (DSO)                        | `float`      |     |       |                             |
| `debit`                                     | Total Payable                                       | `monetary`   |     |       |                             |
| `designation`                               | Designation                                         | `char`       |     | ✅    |                             |
| `display_invoice_edi_format`                | Display Invoice Edi Format                          | `boolean`    |     |       |                             |
| `display_invoice_template_pdf_report_id`    | Display Invoice Template Pdf Report                 | `boolean`    |     |       |                             |
| `display_name`                              | Display Name                                        | `char`       |     |       |                             |
| `duplicate_bank_partner_ids`                | Duplicate Bank Partner                              | `many2many`  |     |       | res.partner                 |
| `email`                                     | Email                                               | `char`       |     |       |                             |
| `email_formatted`                           | Formatted Email                                     | `char`       |     |       |                             |
| `email_normalized`                          | Normalized Email                                    | `char`       |     |       |                             |
| `emergency_contact`                         | Emergency Contact                                   | `many2one`   |     | ✅    | res.partner                 |
| `emp_id`                                    | HR Employee                                         | `many2one`   |     | ✅    | hr.employee                 |
| `employee`                                  | Employee                                            | `boolean`    |     |       |                             |
| `employee_ids`                              | Employees                                           | `one2many`   |     |       | hr.employee                 |
| `employees_count`                           | Employees Count                                     | `integer`    |     |       |                             |
| `event_count`                               | # Events                                            | `integer`    |     |       |                             |
| `faculty_subject_ids`                       | Subject(s)                                          | `many2many`  |     | ✅    | op.subject                  |
| `first_name`                                | First Name                                          | `char`       | ✅  | ✅    |                             |
| `fiscal_country_codes`                      | Fiscal Country Codes                                | `char`       |     |       |                             |
| `fiscal_country_group_codes`                | Fiscal Country Group Codes                          | `json`       |     |       |                             |
| `function`                                  | Job Position                                        | `char`       |     |       |                             |
| `gender`                                    | Gender                                              | `selection`  | ✅  | ✅    |                             |
| `global_location_number`                    | GLN                                                 | `char`       |     |       |                             |
| `group_on`                                  | Week Day                                            | `selection`  | ✅  |       |                             |
| `group_rfq`                                 | Group RFQ                                           | `selection`  | ✅  |       |                             |
| `has_message`                               | Has Message                                         | `boolean`    |     |       |                             |
| `head_office`                               | Head Office                                         | `char`       |     |       |                             |
| `health_faculty_count`                      | Health Faculty Count                                | `integer`    |     |       |                             |
| `health_faculty_lines`                      | Health Detail                                       | `one2many`   |     | ✅    | op.health                   |
| `hr_contact`                                | HR Contact                                          | `char`       |     |       |                             |
| `hr_email`                                  | HR Email                                            | `char`       |     |       |                             |
| `hr_name`                                   | HR Name                                             | `char`       |     |       |                             |
| `id`                                        | ID                                                  | `integer`    |     | ✅    |                             |
| `id_number`                                 | ID Card Number                                      | `char`       |     | ✅    |                             |
| `ignore_abnormal_invoice_amount`            | Ignore Abnormal Invoice Amount                      | `boolean`    |     |       |                             |
| `ignore_abnormal_invoice_date`              | Ignore Abnormal Invoice Date                        | `boolean`    |     |       |                             |
| `image_1024`                                | Image 1024                                          | `binary`     |     |       |                             |
| `image_128`                                 | Image 128                                           | `binary`     |     |       |                             |
| `image_1920`                                | Image                                               | `binary`     |     |       |                             |
| `image_256`                                 | Image 256                                           | `binary`     |     |       |                             |
| `image_512`                                 | Image 512                                           | `binary`     |     |       |                             |
| `im_status`                                 | IM Status                                           | `char`       |     |       |                             |
| `industry_id`                               | Industry                                            | `many2one`   |     |       | res.partner.industry        |
| `invoice_edi_format`                        | eInvoice format                                     | `selection`  |     |       |                             |
| `invoice_edi_format_store`                  | Invoice Edi Format Store                            | `char`       |     |       |                             |
| `invoice_ids`                               | Invoices                                            | `one2many`   |     |       | account.move                |
| `invoice_sending_method`                    | Invoice sending                                     | `selection`  |     |       |                             |
| `invoice_template_pdf_report_id`            | Invoice report                                      | `many2one`   |     |       | ir.actions.report           |
| `is_blacklisted`                            | Blacklist                                           | `boolean`    |     |       |                             |
| `is_company`                                | Is a Company                                        | `boolean`    |     |       |                             |
| `is_in_call`                                | Is In Call                                          | `boolean`    |     |       |                             |
| `is_parent`                                 | Is a Parent                                         | `boolean`    |     |       |                             |
| `is_peppol_edi_format`                      | Is Peppol Edi Format                                | `boolean`    |     |       |                             |
| `is_pickup_location`                        | Is Pickup Location                                  | `boolean`    |     |       |                             |
| `is_public`                                 | Is Public                                           | `boolean`    |     |       |                             |
| `is_published`                              | Is Published                                        | `boolean`    |     |       |                             |
| `is_seo_optimized`                          | SEO optimized                                       | `boolean`    |     |       |                             |
| `is_student`                                | Is a Student                                        | `boolean`    |     |       |                             |
| `is_ubl_format`                             | Is Ubl Format                                       | `boolean`    |     |       |                             |
| `is_venue`                                  | Venue                                               | `boolean`    |     |       |                             |
| `lang`                                      | Language                                            | `selection`  |     |       |                             |
| `last_login`                                | Latest Connection                                   | `datetime`   |     |       |                             |
| `last_name`                                 | Last Name                                           | `char`       | ✅  | ✅    |                             |
| `leave_date_to`                             | Leave Date To                                       | `date`       |     |       |                             |
| `library_card_id`                           | Library Card                                        | `many2one`   |     | ✅    | op.library.card             |
| `livechat_channel_count`                    | Livechat Channel Count                              | `integer`    |     |       |                             |
| `login`                                     | Login                                               | `char`       |     |       |                             |
| `main_department_id`                        | Main Department                                     | `many2one`   |     | ✅    | op.department               |
| `main_user_id`                              | Main User                                           | `many2one`   |     |       | res.users                   |
| `media_movement_lines`                      | Movements                                           | `one2many`   |     | ✅    | op.media.movement           |
| `media_movement_lines_count`                | Media Movement Lines Count                          | `integer`    |     |       |                             |
| `meeting_count`                             | # Meetings                                          | `integer`    |     |       |                             |
| `meeting_ids`                               | Meetings                                            | `many2many`  |     |       | calendar.event              |
| `message_attachment_count`                  | Attachment Count                                    | `integer`    |     |       |                             |
| `message_bounce`                            | Bounce                                              | `integer`    |     |       |                             |
| `message_follower_ids`                      | Followers                                           | `one2many`   |     | ✅    | mail.followers              |
| `message_has_error`                         | Message Delivery error                              | `boolean`    |     |       |                             |
| `message_has_error_counter`                 | Number of errors                                    | `integer`    |     |       |                             |
| `message_has_sms_error`                     | SMS Delivery error                                  | `boolean`    |     |       |                             |
| `message_ids`                               | Messages                                            | `one2many`   |     | ✅    | mail.message                |
| `message_is_follower`                       | Is Follower                                         | `boolean`    |     |       |                             |
| `message_needaction`                        | Action Needed                                       | `boolean`    |     |       |                             |
| `message_needaction_counter`                | Number of Actions                                   | `integer`    |     |       |                             |
| `message_partner_ids`                       | Followers (Partners)                                | `many2many`  |     |       | res.partner                 |
| `middle_name`                               | Middle Name                                         | `char`       |     | ✅    |                             |
| `my_activity_date_deadline`                 | My Activity Deadline                                | `date`       |     |       |                             |
| `name`                                      | Name                                                | `char`       |     |       |                             |
| `nationality`                               | Nationality                                         | `many2one`   |     | ✅    | res.country                 |
| `offline_since`                             | Offline since                                       | `datetime`   |     |       |                             |
| `on_time_rate`                              | On-Time Delivery Rate                               | `float`      |     |       |                             |
| `opportunity_count`                         | Opportunity Count                                   | `integer`    |     |       |                             |
| `opportunity_ids`                           | Opportunities                                       | `one2many`   |     |       | crm.lead                    |
| `parent_id`                                 | Related Company                                     | `many2one`   |     |       | res.partner                 |
| `parent_name`                               | Parent name                                         | `char`       |     |       |                             |
| `partner_company_registry_placeholder`      | Partner Company Registry Placeholder                | `char`       |     |       |                             |
| `partner_id`                                | Partner                                             | `many2one`   | ✅  | ✅    | res.partner                 |
| `partner_latitude`                          | Geo Latitude                                        | `float`      |     |       |                             |
| `partner_longitude`                         | Geo Longitude                                       | `float`      |     |       |                             |
| `partner_share`                             | Share Partner                                       | `boolean`    |     |       |                             |
| `partner_vat_placeholder`                   | Partner Vat Placeholder                             | `char`       |     |       |                             |
| `payment_token_count`                       | Payment Token Count                                 | `integer`    |     |       |                             |
| `payment_token_ids`                         | Payment Tokens                                      | `one2many`   |     |       | payment.token               |
| `peppol_eas`                                | Peppol e-address (EAS)                              | `selection`  |     |       |                             |
| `peppol_endpoint`                           | Peppol Endpoint                                     | `char`       |     |       |                             |
| `phone`                                     | Phone                                               | `char`       |     |       |                             |
| `phone_blacklisted`                         | Blacklisted Phone is Phone                          | `boolean`    |     |       |                             |
| `phone_mobile_search`                       | Phone Number                                        | `char`       |     |       |                             |
| `phone_sanitized`                           | Sanitized Number                                    | `char`       |     |       |                             |
| `phone_sanitized_blacklisted`               | Phone Blacklisted                                   | `boolean`    |     |       |                             |
| `picking_warn_msg`                          | Message for Stock Picking                           | `text`       |     |       |                             |
| `properties`                                | Properties                                          | `properties` |     |       |                             |
| `properties_base_definition_id`             | Properties Base Definition                          | `many2one`   |     |       | properties.base.definition  |
| `property_account_payable_id`               | Account Payable                                     | `many2one`   |     |       | account.account             |
| `property_account_position_id`              | Fiscal Position                                     | `many2one`   |     |       | account.fiscal.position     |
| `property_account_receivable_id`            | Account Receivable                                  | `many2one`   |     |       | account.account             |
| `property_delivery_carrier_id`              | Delivery Method                                     | `many2one`   |     |       | delivery.carrier            |
| `property_inbound_payment_method_line_id`   | Property Inbound Payment Method Line                | `many2one`   |     |       | account.payment.method.line |
| `property_outbound_payment_method_line_id`  | Property Outbound Payment Method Line               | `many2one`   |     |       | account.payment.method.line |
| `property_payment_term_id`                  | Customer Payment Terms                              | `many2one`   |     |       | account.payment.term        |
| `property_product_pricelist`                | Pricelist                                           | `many2one`   |     |       | product.pricelist           |
| `property_purchase_currency_id`             | Supplier Currency                                   | `many2one`   |     |       | res.currency                |
| `property_stock_customer`                   | Customer Location                                   | `many2one`   |     |       | stock.location              |
| `property_stock_supplier`                   | Vendor Location                                     | `many2one`   |     |       | stock.location              |
| `property_supplier_payment_term_id`         | Vendor Payment Terms                                | `many2one`   |     |       | account.payment.term        |
| `purchase_line_ids`                         | Purchase Lines                                      | `one2many`   |     |       | purchase.order.line         |
| `purchase_order_count`                      | Purchase Order Count                                | `integer`    |     |       |                             |
| `purchase_warn_msg`                         | Message for Purchase Order                          | `text`       |     |       |                             |
| `rating_ids`                                | Ratings                                             | `one2many`   |     | ✅    | rating.rating               |
| `receipt_reminder_email`                    | Receipt Reminder                                    | `boolean`    |     |       |                             |
| `ref`                                       | Reference                                           | `char`       |     |       |                             |
| `ref_company_ids`                           | Companies that refers to partner                    | `one2many`   |     |       | res.company                 |
| `reminder_date_before_receipt`              | Days Before Receipt                                 | `integer`    |     |       |                             |
| `rtc_session_ids`                           | Rtc Session                                         | `one2many`   |     |       | discuss.channel.rtc.session |
| `sale_order_count`                          | Sale Order Count                                    | `integer`    |     |       |                             |
| `sale_order_ids`                            | Sales Order                                         | `one2many`   |     |       | sale.order                  |
| `sale_warn_msg`                             | Message for Sales Order                             | `text`       |     |       |                             |
| `same_company_registry_partner_id`          | Partner with same Company Registry                  | `many2one`   |     |       | res.partner                 |
| `same_vat_partner_id`                       | Partner with same Tax ID                            | `many2one`   |     |       | res.partner                 |
| `self`                                      | Self                                                | `many2one`   |     |       | res.partner                 |
| `seo_name`                                  | Seo name                                            | `char`       |     |       |                             |
| `session_count`                             | Session Count                                       | `integer`    |     |       |                             |
| `session_ids`                               | Sessions                                            | `one2many`   |     | ✅    | op.session                  |
| `show_credit_limit`                         | Show Credit Limit                                   | `boolean`    |     |       |                             |
| `signup_type`                               | Signup Token Type                                   | `char`       |     |       |                             |
| `specific_property_product_pricelist`       | Specific Property Product Pricelist                 | `many2one`   |     |       | product.pricelist           |
| `state_id`                                  | State                                               | `many2one`   |     |       | res.country.state           |
| `static_map_url`                            | Static Map Url                                      | `char`       |     |       |                             |
| `static_map_url_is_valid`                   | Static Map Url Is Valid                             | `boolean`    |     |       |                             |
| `street`                                    | Street                                              | `char`       |     |       |                             |
| `street2`                                   | Street2                                             | `char`       |     |       |                             |
| `subject_cost_ids`                          | Subject Cost                                        | `one2many`   |     | ✅    | op.subject.cost             |
| `subject_count`                             | Subject Count                                       | `integer`    |     |       |                             |
| `suggest_based_on`                          | Suggest Based On                                    | `char`       |     |       |                             |
| `suggest_days`                              | Suggest Days                                        | `integer`    |     |       |                             |
| `suggest_percent`                           | Suggest Percent                                     | `integer`    |     |       |                             |
| `supplier_invoice_count`                    | # Vendor Bills                                      | `integer`    |     |       |                             |
| `supplier_rank`                             | Supplier Rank                                       | `integer`    |     |       |                             |
| `ticket_count`                              | Ticket Count                                        | `integer`    |     |       |                             |
| `timetable_count`                           | Timetable Count                                     | `integer`    |     |       |                             |
| `title`                                     | Title                                               | `many2one`   |     |       | res.partner.title           |
| `total_invoiced`                            | Total Invoiced                                      | `monetary`   |     |       |                             |
| `trust`                                     | Degree of trust you have in this debtor             | `selection`  |     |       |                             |
| `type`                                      | Address Type                                        | `selection`  |     |       |                             |
| `type_address_label`                        | Address Type Description                            | `char`       |     |       |                             |
| `tz`                                        | Timezone                                            | `selection`  |     |       |                             |
| `tz_offset`                                 | Timezone offset                                     | `char`       |     |       |                             |
| `use_partner_credit_limit`                  | Partner Limit                                       | `boolean`    |     |       |                             |
| `user_id`                                   | Salesperson                                         | `many2one`   |     |       | res.users                   |
| `user_ids`                                  | Users                                               | `one2many`   |     |       | res.users                   |
| `user_livechat_username`                    | User Livechat Username                              | `char`       |     |       |                             |
| `vat`                                       | Tax ID                                              | `char`       |     |       |                             |
| `vat_label`                                 | Tax ID Label                                        | `char`       |     |       |                             |
| `visa_info`                                 | Visa Info                                           | `char`       |     | ✅    |                             |
| `visitor_ids`                               | Visitors                                            | `one2many`   |     |       | website.visitor             |
| `website`                                   | Website Link                                        | `char`       |     |       |                             |
| `website_absolute_url`                      | Website Absolute URL                                | `char`       |     |       |                             |
| `website_description`                       | Website Partner Full Description                    | `html`       |     |       |                             |
| `website_id`                                | Website                                             | `many2one`   |     |       | website                     |
| `website_message_ids`                       | Website Messages                                    | `one2many`   |     | ✅    | mail.message                |
| `website_meta_description`                  | Website meta description                            | `text`       |     |       |                             |
| `website_meta_keywords`                     | Website meta keywords                               | `char`       |     |       |                             |
| `website_meta_og_img`                       | Website opengraph image                             | `char`       |     |       |                             |
| `website_meta_title`                        | Website meta title                                  | `char`       |     |       |                             |
| `website_published`                         | Visible on current website                          | `boolean`    |     |       |                             |
| `website_short_description`                 | Website Partner Short Description                   | `text`       |     |       |                             |
| `website_url`                               | Website URL                                         | `char`       |     |       |                             |
| `wishlist_ids`                              | Wishlist                                            | `one2many`   |     |       | product.wishlist            |
| `write_date`                                | Last Updated on                                     | `datetime`   |     | ✅    |                             |
| `write_uid`                                 | Last Updated by                                     | `many2one`   |     | ✅    | res.users                   |
| `zip`                                       | Zip                                                 | `char`       |     |       |                             |

**Access Rights:**

| Name                              | Group                | Perms     |
| --------------------------------- | -------------------- | --------- |
| name_op_faculty_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| op_faculty_faculty                | OpenEduCat / User    | `R`       |
| name_op_faculty_library           | Library / Manager    | `R`       |
| op_faculty_parent                 | Role / Portal        | `R`       |

**Record Rules:**

- **Faculty Login rule** (92) `R/W/C/D`
  - Domain: `['|',('user_id','=',user.id),('emp_id.user_id','=',user.id)]`
- **View Faculties** (93) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **Faculty multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`
- **Faculty multi-department** (Global) `R/W/C/D`
  - Domain:
    `['|','|','|','|',('user_id','=',user.id),('emp_id.user_id','=',user.id),('main_department_id','=',False),('main_department_id','child_of',[user.dept_id.id]),('main_department_id','in',user.department_ids.ids)]`
- **Gradebook Faculty Login rule** (182) `R/W/C/D`
  - Domain: `[(1,'=',1)]`

### 🗃️ `op.session` — Sessions

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation            |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ------------------- |
| `academic_plan_id`           | Academic Plan          | `many2one`  |     | ✅    | op.academic.plan    |
| `active`                     | Active                 | `boolean`   |     | ✅    |                     |
| `attendance_sheet`           | Session                | `one2many`  |     | ✅    | op.attendance.sheet |
| `batch_id`                   | Batch                  | `many2one`  |     | ✅    | op.batch            |
| `classroom_id`               | Classroom              | `many2one`  |     | ✅    | op.classroom        |
| `color`                      | Color Index            | `integer`   |     | ✅    |                     |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company         |
| `course_id`                  | Course                 | `many2one`  |     | ✅    | op.course           |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                     |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users           |
| `days`                       | Days                   | `selection` |     | ✅    |                     |
| `display_name`               | Display Name           | `char`      |     |       |                     |
| `end_datetime`               | End Time               | `datetime`  | ✅  | ✅    |                     |
| `faculty_id`                 | Faculty                | `many2one`  | ✅  | ✅    | op.faculty          |
| `has_message`                | Has Message            | `boolean`   |     |       |                     |
| `id`                         | ID                     | `integer`   |     | ✅    |                     |
| `lesson_ids`                 | Lesson                 | `many2many` |     | ✅    | op.lesson           |
| `meeting_count`              | Meeting Count          | `integer`   |     |       |                     |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                     |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers      |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                     |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                     |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                     |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message        |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                     |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                     |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                     |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner         |
| `name`                       | Name                   | `char`      |     | ✅    |                     |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating       |
| `required_field`             | Required Field         | `boolean`   |     | ✅    |                     |
| `section_ids`                | Section                | `many2many` |     | ✅    | op.section          |
| `start_datetime`             | Start Time             | `datetime`  | ✅  | ✅    |                     |
| `state`                      | Status                 | `selection` |     | ✅    |                     |
| `student_count`              | Student Count          | `integer`   |     |       |                     |
| `subject_id`                 | Subject                | `many2one`  | ✅  | ✅    | op.subject          |
| `timing`                     | Session timing         | `char`      |     |       |                     |
| `timing_id`                  | Timing                 | `many2one`  |     | ✅    | op.timing           |
| `type`                       | Day                    | `char`      |     | ✅    |                     |
| `user_id`                    | User                   | `many2one`  |     | ✅    | res.users           |
| `user_ids`                   | Users                  | `many2many` |     | ✅    | res.users           |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message        |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                     |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                           | Group               | Perms     |
| ------------------------------ | ------------------- | --------- |
| name_op_session_student        | Timetable / Manager | `R/W/C/D` |
| name_op_session_timetable_user | Timetable / User    | `R/W/C`   |

**Record Rules:**

- **Student Session rule** (160) `R/W/C/D`
  - Domain: `['|', ('user_ids','in',user.id), ('user_ids','in',user.child_ids.ids)]`
- **Manager Session Rule** (161) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **User Session Rule** (160) `R/W/C/D`
  - Domain: `[('faculty_id.user_id','=',user.id)]`
- **Timetable multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.student.course` — Student Course Details

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation              |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | --------------------- |
| `academic_plan_id`           | Academic Plan          | `many2one`  |     | ✅    | op.academic.plan      |
| `academic_term_id`           | Terms                  | `many2one`  |     | ✅    | op.academic.term      |
| `academic_years_id`          | Academic Year          | `many2one`  |     | ✅    | op.academic.year      |
| `batch_id`                   | Batch                  | `many2one`  |     | ✅    | op.batch              |
| `course_id`                  | Course                 | `many2one`  | ✅  | ✅    | op.course             |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                       |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users             |
| `display_name`               | Display Name           | `char`      |     |       |                       |
| `expires_after`              | Invoice Cycles         | `integer`   |     | ✅    |                       |
| `faculty_advisor_id`         | Faculty Advisor        | `many2one`  |     | ✅    | op.faculty            |
| `fees_plan_id`               | Fees Term Plan         | `many2one`  |     | ✅    | op.fees.plan          |
| `fees_start_date`            | Fees Start Date        | `date`      |     | ✅    |                       |
| `fees_term_id`               | Fees Term              | `many2one`  |     | ✅    | op.fees.terms         |
| `generated_invoices`         | Generated Invoices     | `integer`   |     | ✅    |                       |
| `has_message`                | Has Message            | `boolean`   |     |       |                       |
| `id`                         | ID                     | `integer`   |     | ✅    |                       |
| `intake_year_id`             | Intake Year            | `many2one`  |     | ✅    | op.intake.year        |
| `is_withdrawal`              | Withdrawal             | `boolean`   |     | ✅    |                       |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                       |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers        |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                       |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                       |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                       |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message          |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                       |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                       |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                       |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner           |
| `next_invoice_date`          | Next Invoice Date      | `date`      |     | ✅    |                       |
| `prev_invoice_date`          | Previous Invoice Date  | `date`      |     | ✅    |                       |
| `product_id`                 | Course Fees            | `many2one`  |     | ✅    | product.product       |
| `program_id`                 | Program                | `many2one`  |     |       | op.program            |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating         |
| `required_field`             | Required Field         | `boolean`   |     | ✅    |                       |
| `roll_number`                | Roll Number            | `char`      |     | ✅    |                       |
| `session_count`              | Session Count          | `integer`   |     |       |                       |
| `state`                      | Status                 | `selection` |     | ✅    |                       |
| `student_id`                 | Student                | `many2one`  |     | ✅    | op.student            |
| `subject_ids`                | Subjects               | `many2many` |     | ✅    | op.subject            |
| `user_id`                    | User                   | `many2one`  |     | ✅    | res.users             |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message          |
| `withdrawal_id`              | Withdrawal Details     | `many2one`  |     | ✅    | op.student.withdrawal |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                       |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                                     | Group                | Perms     |
| ---------------------------------------- | -------------------- | --------- |
| name_op_student_course_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| name_op_student_course_faculty           | OpenEduCat / User    | `R/W/C`   |
| op_student_course_parent                 | Library / Manager    | `R`       |
| op_student_course_parent                 | Role / Portal        | `R`       |

**Record Rules:**

- **Student Course multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|','|',('student_id.company_id','=',False),('student_id.company_id','child_of',[user.company_id.id]),('student_id.company_id','in',user.company_ids.ids),('student_id.company_id','in', company_ids)]`

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

### 🗃️ `op.program` — Thesis Program

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                    | Type        | Req | Store | Relation                      |
| ---------------------------- | ------------------------ | ----------- | --- | ----- | ----------------------------- |
| `active`                     | Active                   | `boolean`   |     | ✅    |                               |
| `admission_count`            | Admission Count          | `integer`   |     |       |                               |
| `area_id`                    | Area                     | `many2one`  |     | ✅    | op.area                       |
| `batch_count`                | Batch Count              | `integer`   |     |       |                               |
| `code`                       | Code                     | `char`      | ✅  | ✅    |                               |
| `color`                      | Color Index              | `integer`   |     | ✅    |                               |
| `company_id`                 | Company                  | `many2one`  |     | ✅    | res.company                   |
| `course_count`               | Course Count             | `integer`   |     |       |                               |
| `create_date`                | Created on               | `datetime`  |     | ✅    |                               |
| `create_uid`                 | Created by               | `many2one`  |     | ✅    | res.users                     |
| `department_id`              | Department               | `many2one`  |     | ✅    | op.department                 |
| `display_name`               | Display Name             | `char`      |     |       |                               |
| `evaluation_template_id`     | Evaluation Template      | `many2one`  |     | ✅    | op.thesis.evaluation.template |
| `full_description`           | Full Description         | `html`      |     | ✅    |                               |
| `has_message`                | Has Message              | `boolean`   |     |       |                               |
| `id`                         | ID                       | `integer`   |     | ✅    |                               |
| `image_1920`                 | Image                    | `binary`    |     | ✅    |                               |
| `max_unit_load`              | Maximum Unit Load        | `float`     |     | ✅    |                               |
| `message_attachment_count`   | Attachment Count         | `integer`   |     |       |                               |
| `message_follower_ids`       | Followers                | `one2many`  |     | ✅    | mail.followers                |
| `message_has_error`          | Message Delivery error   | `boolean`   |     |       |                               |
| `message_has_error_counter`  | Number of errors         | `integer`   |     |       |                               |
| `message_has_sms_error`      | SMS Delivery error       | `boolean`   |     |       |                               |
| `message_ids`                | Messages                 | `one2many`  |     | ✅    | mail.message                  |
| `message_is_follower`        | Is Follower              | `boolean`   |     |       |                               |
| `message_needaction`         | Action Needed            | `boolean`   |     |       |                               |
| `message_needaction_counter` | Number of Actions        | `integer`   |     |       |                               |
| `message_partner_ids`        | Followers (Partners)     | `many2many` |     |       | res.partner                   |
| `min_unit_load`              | Minimum Unit Load        | `float`     |     | ✅    |                               |
| `name`                       | Name                     | `char`      | ✅  | ✅    |                               |
| `program_level_id`           | Program Level            | `many2one`  | ✅  | ✅    | op.program.level              |
| `program_sessions_count`     | Session Count            | `integer`   |     |       |                               |
| `rating_ids`                 | Ratings                  | `one2many`  |     | ✅    | rating.rating                 |
| `required_thesis`            | Required Thesis          | `boolean`   |     | ✅    |                               |
| `short_desc`                 | Short Description        | `text`      |     | ✅    |                               |
| `student_count`              | Student Count            | `integer`   |     |       |                               |
| `subject_count`              | Subject Count            | `integer`   |     |       |                               |
| `thesis_duration`            | Thesis Duration (months) | `integer`   |     | ✅    |                               |
| `thesis_guidelines`          | Thesis Guidelines        | `html`      |     | ✅    |                               |
| `user_id`                    | User                     | `many2one`  |     | ✅    | res.users                     |
| `website_message_ids`        | Website Messages         | `one2many`  |     | ✅    | mail.message                  |
| `write_date`                 | Last Updated on          | `datetime`  |     | ✅    |                               |
| `write_uid`                  | Last Updated by          | `many2one`  |     | ✅    | res.users                     |

**Access Rights:**

| Name                                | Group                | Perms     |
| ----------------------------------- | -------------------- | --------- |
| access_op_program_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| access_op_program_faculty           | OpenEduCat / User    | `R`       |

**Record Rules:**

- **Program multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `generate.time.table` — Generate Sessions

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                | Label             | Type       | Req | Store | Relation            |
| -------------------- | ----------------- | ---------- | --- | ----- | ------------------- |
| `batch_id`           | Batch             | `many2one` | ✅  | ✅    | op.batch            |
| `course_id`          | Course            | `many2one` | ✅  | ✅    | op.course           |
| `create_date`        | Created on        | `datetime` |     | ✅    |                     |
| `create_uid`         | Created by        | `many2one` |     | ✅    | res.users           |
| `display_name`       | Display Name      | `char`     |     |       |                     |
| `end_date`           | End Date          | `date`     | ✅  | ✅    |                     |
| `id`                 | ID                | `integer`  |     | ✅    |                     |
| `name`               | name              | `char`     |     | ✅    |                     |
| `start_date`         | Start Date        | `date`     | ✅  | ✅    |                     |
| `time_table_lines`   | Time Table Lines  | `one2many` |     | ✅    | gen.time.table.line |
| `time_table_lines_1` | Time Table Lines1 | `one2many` |     | ✅    | gen.time.table.line |
| `time_table_lines_2` | Time Table Lines2 | `one2many` |     | ✅    | gen.time.table.line |
| `time_table_lines_3` | Time Table Lines3 | `one2many` |     | ✅    | gen.time.table.line |
| `time_table_lines_4` | Time Table Lines4 | `one2many` |     | ✅    | gen.time.table.line |
| `time_table_lines_5` | Time Table Lines5 | `one2many` |     | ✅    | gen.time.table.line |
| `time_table_lines_6` | Time Table Lines6 | `one2many` |     | ✅    | gen.time.table.line |
| `time_table_lines_7` | Time Table Lines7 | `one2many` |     | ✅    | gen.time.table.line |
| `write_date`         | Last Updated on   | `datetime` |     | ✅    |                     |
| `write_uid`          | Last Updated by   | `many2one` |     | ✅    | res.users           |

**Access Rights:**

| Name                          | Group               | Perms     |
| ----------------------------- | ------------------- | --------- |
| name_generate_time_table      | Timetable / Manager | `R/W/C/D` |
| name_generate_time_table_user | Timetable / User    | `R/W/C`   |

### 🗃️ `gen.time.table.line` — Generate Time Table Lines

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                | Label           | Type        | Req | Store | Relation            |
| -------------------- | --------------- | ----------- | --- | ----- | ------------------- |
| `classroom_id`       | Classroom       | `many2one`  |     | ✅    | op.classroom        |
| `create_date`        | Created on      | `datetime`  |     | ✅    |                     |
| `create_uid`         | Created by      | `many2one`  |     | ✅    | res.users           |
| `day`                | Day             | `selection` | ✅  | ✅    |                     |
| `display_name`       | Display Name    | `char`      |     |       |                     |
| `faculty_id`         | Faculty         | `many2one`  | ✅  | ✅    | op.faculty          |
| `gen_time_table`     | Time Table      | `many2one`  |     | ✅    | generate.time.table |
| `id`                 | ID              | `integer`   |     | ✅    |                     |
| `session_end_time`   | End Time        | `float`     |     | ✅    |                     |
| `session_start_time` | Start Time      | `float`     |     | ✅    |                     |
| `subject_id`         | Subject         | `many2one`  | ✅  | ✅    | op.subject          |
| `timing_id`          | Timing          | `many2one`  |     | ✅    | op.timing           |
| `write_date`         | Last Updated on | `datetime`  |     | ✅    |                     |
| `write_uid`          | Last Updated by | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                          | Group               | Perms     |
| ----------------------------- | ------------------- | --------- |
| name_gen_time_table_line      | Timetable / Manager | `R/W/C/D` |
| name_gen_time_table_line_user | Timetable / User    | `R/W/C`   |

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

### 🗃️ `op.department` — OpenEduCat Department

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label             | Type       | Req | Store | Relation      |
| --------------- | ----------------- | ---------- | --- | ----- | ------------- |
| `batch_count`   | Batch Count       | `integer`  |     |       |               |
| `code`          | Code              | `char`     | ✅  | ✅    |               |
| `color`         | Color Index       | `integer`  |     | ✅    |               |
| `company_id`    | Company           | `many2one` | ✅  | ✅    | res.company   |
| `course_count`  | Course Count      | `integer`  |     |       |               |
| `create_date`   | Created on        | `datetime` |     | ✅    |               |
| `create_uid`    | Created by        | `many2one` |     | ✅    | res.users     |
| `display_name`  | Display Name      | `char`     |     |       |               |
| `faculty_count` | Faculty Count     | `integer`  |     |       |               |
| `id`            | ID                | `integer`  |     | ✅    |               |
| `name`          | Name              | `char`     | ✅  | ✅    |               |
| `parent_id`     | Parent Department | `many2one` |     | ✅    | op.department |
| `program_count` | Program Count     | `integer`  |     |       |               |
| `session_count` | Session Count     | `integer`  |     |       |               |
| `student_count` | Student Count     | `integer`  |     |       |               |
| `subject_count` | Subject Count     | `integer`  |     |       |               |
| `user_id`       | User              | `many2one` |     | ✅    | res.users     |
| `write_date`    | Last Updated on   | `datetime` |     | ✅    |               |
| `write_uid`     | Last Updated by   | `many2one` |     | ✅    | res.users     |

**Access Rights:**

| Name                 | Group                | Perms     |
| -------------------- | -------------------- | --------- |
| access_op_department | OpenEduCat / Manager | `R/W/C/D` |
| access_op_department | OpenEduCat / User    | `R`       |

**Record Rules:**

- **Department multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

### 🗃️ `op.timing` — Period

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation    |
| -------------- | --------------- | ----------- | --- | ----- | ----------- |
| `am_pm`        | AM/PM           | `selection` | ✅  | ✅    |             |
| `company_id`   | Company         | `many2one`  |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime`  |     | ✅    |             |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`      |     |       |             |
| `duration`     | Duration        | `float`     |     | ✅    |             |
| `hour`         | Hours           | `selection` | ✅  | ✅    |             |
| `id`           | ID              | `integer`   |     | ✅    |             |
| `minute`       | Minute          | `selection` | ✅  | ✅    |             |
| `name`         | Name            | `char`      | ✅  | ✅    |             |
| `sequence`     | Sequence        | `integer`   |     | ✅    |             |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                             | Group               | Perms     |
| -------------------------------- | ------------------- | --------- |
| name_op_timing_timetable_manager | Timetable / Manager | `R/W/C/D` |
| name_op_timing_timetable_user    | Timetable / User    | `R/W`     |

**Record Rules:**

- **Period multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`
