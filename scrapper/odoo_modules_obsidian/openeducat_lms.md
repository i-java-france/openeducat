---
title: "OpenEduCat LMS"
module: "openeducat_lms"
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

# 🟢 OpenEduCat LMS

> **Module:** `openeducat_lms` | **Version:** `19.0.1.0` **Category:** Education |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_core_enterprise]] [[website]] [[portal_rating]] [[openeducat_quiz]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `LMS`
- `LMS/Configuration`
- `LMS/Configuration/Category`
- `LMS/Configuration/Tags`
- `LMS/Dashboard`
- `LMS/Reporting`
- `LMS/Reporting/Course Participation`
- `LMS/Reporting/Course Profile Report`
- `LMS/Reporting/Quiz Participation Report`
- `LMS/Reporting/Quiz Statistics`
- `LMS/Reporting/Summary`

### Views

- `* INHERIT Course Announcement Tab (qweb)`
- `* INHERIT Course Author (qweb)`
- `* INHERIT Course Author (qweb)`
- `* INHERIT Course Curriculum Tab (qweb)`
- `* INHERIT Course Description Tab (qweb)`
- `* INHERIT Course Includes (qweb)`
- `* INHERIT Course Instructor Tab (qweb)`
- `* INHERIT Course Layout Option One (qweb)`
- `* INHERIT Course Module (qweb)`
- `* INHERIT Course Module (qweb)`
- `* INHERIT Course Price (qweb)`
- `* INHERIT Course Rating (qweb)`
- `* INHERIT Course Rating (qweb)`
- `* INHERIT Course Review Tab (qweb)`
- `* INHERIT Course Social Icons (qweb)`
- `* INHERIT Course Student (qweb)`
- `* INHERIT Course Students (qweb)`
- `* INHERIT Course Tags (qweb)`
- `* INHERIT Course Time (qweb)`
- `* INHERIT Course Total Duration (qweb)`
- `* INHERIT Course Update Date (qweb)`
- `* INHERIT List View (by default) (qweb)`
- `* INHERIT Portal layout : Certificate (qweb)`
- `* INHERIT Show Certificate (qweb)`
- `* INHERIT Show Courses (qweb)`
- `* INHERIT Toggle Description (qweb)`
- `* INHERIT lms_course_detail_template_style_default (qweb)`
- `* INHERIT lms_course_detail_template_style_one (qweb)`
- `* INHERIT lms_course_detail_template_style_two (qweb)`
- `* INHERIT op.faculty.lms.form (form)`
- `* INHERIT op.faculty.lms.tree.inherited (list)`
- `* INHERIT op.quiz.form (form)`
- `* INHERIT op.quiz.lms.tree.inherited (list)`
- `Certificates (qweb)`
- `Course (qweb)`
- `Course Detail (qweb)`
- `Courses (qweb)`
- `Embedded Slide Page (qweb)`
- `Enable Search (qweb)`
- `Forbidden Embedded Slide (qweb)`
- `Grid or List button (qweb)`
- `My Courses (qweb)`
- `Private Presentation (qweb)`
- `Sort-by Template (qweb)`
- `certi_data (qweb)`
- `certification_report_view (qweb)`
- `course.report.graph (graph)`
- `course_content_module_preview_document (qweb)`
- `course_content_module_type_image (qweb)`
- `lms.dashboard.view.kanban (kanban)`
- `op.course.enrollment.lms.form (form)`
- `op.course.enrollment.lms.list (list)`
- `op.course.lms.form (form)`
- `op.course.lms.list (list)`
- `op.course.module.lms.form (form)`
- `op.course.module.lms.tree (list)`
- `op.course.pivot (pivot)`
- `op.course.question.view.form (form)`
- `op.course.tag.lms.list (list)`
- `op.course.view.form.add (form)`
- `op.quiz.result.graph (graph)`
- `op.quiz.result.tree.custom (list)`
- `op.quiz.tree (list)`
- `openeducat_lms.lms_course_attributes (qweb)`
- `openeducat_lms.lms_course_attributes_top (qweb)`

### Reports

- `Certifications`

## 🛠️ Technical Documentation

**12 model(s) defined by this module:**

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

### 🗃️ `op.course.module` — Course Module

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                                     | Type        | Req | Store | Relation           |
| ---------------------------- | ----------------------------------------- | ----------- | --- | ----- | ------------------ |
| `active`                     | Active                                    | `boolean`   |     | ✅    |                    |
| `allow_download`             | Allow Download?                           | `boolean`   |     | ✅    |                    |
| `binary_content`             | File                                      | `binary`    |     | ✅    |                    |
| `can_publish`                | Can Publish                               | `boolean`   |     |       |                    |
| `company_id`                 | Company                                   | `many2one`  |     | ✅    | res.company        |
| `completion_time`            | Duration                                  | `float`     |     | ✅    |                    |
| `course_id`                  | Course                                    | `many2one`  |     | ✅    | op.course          |
| `create_date`                | Created on                                | `datetime`  |     | ✅    |                    |
| `create_uid`                 | Created by                                | `many2one`  |     | ✅    | res.users          |
| `datas`                      | Content                                   | `binary`    |     | ✅    |                    |
| `display_name`               | Display Name                              | `char`      |     |       |                    |
| `document_binary_content`    | PDF Content                               | `binary`    |     | ✅    |                    |
| `document_binary_mimetype`   | Content Mimetype                          | `char`      |     | ✅    |                    |
| `document_google_url`        | Document Link                             | `char`      |     |       |                    |
| `document_id`                | Document ID                               | `char`      |     | ✅    |                    |
| `document_name`              | Document Filename                         | `char`      |     | ✅    |                    |
| `document_url`               | Document URL                              | `char`      |     | ✅    |                    |
| `embed_code`                 | Embed Code                                | `text`      |     |       |                    |
| `embed_code_external`        | External Embed Code                       | `html`      |     |       |                    |
| `file`                       | File                                      | `binary`    |     | ✅    |                    |
| `file_name`                  | File Name                                 | `char`      |     | ✅    |                    |
| `has_message`                | Has Message                               | `boolean`   |     |       |                    |
| `html_content`               | HTML Content                              | `html`      |     | ✅    |                    |
| `id`                         | ID                                        | `integer`   |     | ✅    |                    |
| `image_1024`                 | Image 1024                                | `binary`    |     | ✅    |                    |
| `image_128`                  | Image 128                                 | `binary`    |     | ✅    |                    |
| `image_1920`                 | Image                                     | `binary`    |     | ✅    |                    |
| `image_256`                  | Image 256                                 | `binary`    |     | ✅    |                    |
| `image_512`                  | Image 512                                 | `binary`    |     | ✅    |                    |
| `image_binary_content`       | Image Content                             | `binary`    |     |       |                    |
| `image_google_url`           | Image Link                                | `char`      |     |       |                    |
| `is_module`                  | Is a module                               | `boolean`   |     | ✅    |                    |
| `is_published`               | Is Published                              | `boolean`   |     | ✅    |                    |
| `is_seo_optimized`           | SEO optimized                             | `boolean`   |     | ✅    |                    |
| `message_attachment_count`   | Attachment Count                          | `integer`   |     |       |                    |
| `message_follower_ids`       | Followers                                 | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`          | Message Delivery error                    | `boolean`   |     |       |                    |
| `message_has_error_counter`  | Number of errors                          | `integer`   |     |       |                    |
| `message_has_sms_error`      | SMS Delivery error                        | `boolean`   |     |       |                    |
| `message_ids`                | Messages                                  | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`        | Is Follower                               | `boolean`   |     |       |                    |
| `message_needaction`         | Action Needed                             | `boolean`   |     |       |                    |
| `message_needaction_counter` | Number of Actions                         | `integer`   |     |       |                    |
| `message_partner_ids`        | Followers (Partners)                      | `many2many` |     |       | res.partner        |
| `module_category`            | Content Type                              | `selection` | ✅  | ✅    |                    |
| `module_id`                  | Module                                    | `many2one`  |     | ✅    | op.course.module   |
| `module_lines`               | Contents                                  | `one2many`  |     | ✅    | op.course.module   |
| `name`                       | Title                                     | `char`      | ✅  | ✅    |                    |
| `question_ids`               | Questions                                 | `one2many`  |     | ✅    | op.course.question |
| `quiz_first_attempt_reward`  | Reward: first attempt                     | `integer`   |     | ✅    |                    |
| `quiz_fourth_attempt_reward` | Reward: every attempt after the third try | `integer`   |     | ✅    |                    |
| `quiz_id`                    | Quiz                                      | `many2one`  |     | ✅    | op.quiz            |
| `quiz_second_attempt_reward` | Reward: second attempt                    | `integer`   |     | ✅    |                    |
| `quiz_third_attempt_reward`  | Reward: third attempt                     | `integer`   |     | ✅    |                    |
| `rating_ids`                 | Ratings                                   | `one2many`  |     | ✅    | rating.rating      |
| `seo_name`                   | Seo name                                  | `char`      |     | ✅    |                    |
| `sequence`                   | Sequence                                  | `integer`   |     | ✅    |                    |
| `source_type`                | Source Type                               | `selection` | ✅  | ✅    |                    |
| `url`                        | External URL                              | `char`      |     | ✅    |                    |
| `user_id`                    | Uploaded by                               | `many2one`  |     | ✅    | res.users          |
| `video_source_type`          | Video Source                              | `selection` |     |       |                    |
| `video_type`                 | Video Type                                | `selection` |     | ✅    |                    |
| `video_url`                  | Video Link                                | `char`      |     |       |                    |
| `vimeo_id`                   | Video Vimeo ID                            | `char`      |     |       |                    |
| `website_absolute_url`       | Website Absolute URL                      | `char`      |     |       |                    |
| `website_message_ids`        | Website Messages                          | `one2many`  |     | ✅    | mail.message       |
| `website_meta_description`   | Website meta description                  | `text`      |     | ✅    |                    |
| `website_meta_keywords`      | Website meta keywords                     | `char`      |     | ✅    |                    |
| `website_meta_og_img`        | Website opengraph image                   | `char`      |     | ✅    |                    |
| `website_meta_title`         | Website meta title                        | `char`      |     | ✅    |                    |
| `website_published`          | Visible on current website                | `boolean`   |     |       |                    |
| `website_url`                | Website URL                               | `char`      |     |       |                    |
| `write_date`                 | Last Updated on                           | `datetime`  |     | ✅    |                    |
| `write_uid`                  | Last Updated by                           | `many2one`  |     | ✅    | res.users          |
| `youtube_id`                 | Video YouTube ID                          | `char`      |     |       |                    |

**Access Rights:**

| Name                           | Group         | Perms     |
| ------------------------------ | ------------- | --------- |
| access_op_course_module        | LMS / Manager | `R/W/C/D` |
| access_op_course_module_user   | LMS / User    | `R/W/C`   |
| access_op_course_module_portal | Role / Portal | `R`       |
| access_op_course_module_public | Role / Public | `R`       |

**Record Rules:**

- **Course Module multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

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

### 🗃️ `op.quiz` — Quiz

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                                  | Type        | Req | Store | Relation               |
| -------------------------------- | -------------------------------------- | ----------- | --- | ----- | ---------------------- |
| `active`                         | Active                                 | `boolean`   |     | ✅    |                        |
| `allow_shuffle`                  | Allow Shuffle                          | `boolean`   |     | ✅    |                        |
| `assigned_to`                    | Assigned To                            | `selection` | ✅  | ✅    |                        |
| `batch_ids`                      | Batches                                | `many2many` |     | ✅    | op.batch               |
| `categ_id`                       | Category                               | `many2one`  |     | ✅    | op.quiz.category       |
| `challenge_ids`                  | Challenges                             | `many2many` |     | ✅    | gamification.challenge |
| `company_id`                     | Company                                | `many2one`  |     | ✅    | res.company            |
| `config_ids`                     | Quiz Configuration                     | `one2many`  |     | ✅    | op.quiz.config         |
| `copy_paste_allow`               | Copy/Paste Allow                       | `boolean`   |     | ✅    |                        |
| `course_ids`                     | Courses                                | `many2many` |     | ✅    | op.course              |
| `create_date`                    | Created on                             | `datetime`  |     | ✅    |                        |
| `create_uid`                     | Created by                             | `many2one`  |     | ✅    | res.users              |
| `description`                    | Short Description                      | `char`      |     | ✅    |                        |
| `display_name`                   | Display Name                           | `char`      |     |       |                        |
| `display_result`                 | Display On Portal                      | `boolean`   |     | ✅    |                        |
| `exit_allow`                     | Allow Exit                             | `boolean`   |     | ✅    |                        |
| `face_sensitivity`               | Sensitivity                            | `float`     |     | ✅    |                        |
| `face_tracking`                  | Face Tracking                          | `boolean`   |     | ✅    |                        |
| `grace_period`                   | Grace Period                           | `boolean`   |     | ✅    |                        |
| `grace_period_hr`                | Submission Grace Period                | `integer`   |     | ✅    |                        |
| `grace_period_minute`            | Grace Minutes                          | `integer`   |     | ✅    |                        |
| `has_message`                    | Has Message                            | `boolean`   |     |       |                        |
| `id`                             | ID                                     | `integer`   |     | ✅    |                        |
| `is_attached_reference_material` | Allow Attached Reference Material      | `boolean`   |     | ✅    |                        |
| `line_ids`                       | Questions                              | `one2many`  |     | ✅    | op.quiz.line           |
| `lms`                            | LMS                                    | `boolean`   |     | ✅    |                        |
| `manual`                         | Manual                                 | `boolean`   |     | ✅    |                        |
| `message_attachment_count`       | Attachment Count                       | `integer`   |     |       |                        |
| `message_follower_ids`           | Followers                              | `one2many`  |     | ✅    | mail.followers         |
| `message_has_error`              | Message Delivery error                 | `boolean`   |     |       |                        |
| `message_has_error_counter`      | Number of errors                       | `integer`   |     |       |                        |
| `message_has_sms_error`          | SMS Delivery error                     | `boolean`   |     |       |                        |
| `message_ids`                    | Messages                               | `one2many`  |     | ✅    | mail.message           |
| `message_is_follower`            | Is Follower                            | `boolean`   |     |       |                        |
| `message_needaction`             | Action Needed                          | `boolean`   |     |       |                        |
| `message_needaction_counter`     | Number of Actions                      | `integer`   |     |       |                        |
| `message_partner_ids`            | Followers (Partners)                   | `many2many` |     |       | res.partner            |
| `multiple_person`                | Multiple Person                        | `boolean`   |     | ✅    |                        |
| `name`                           | Name                                   | `char`      |     | ✅    |                        |
| `no_of_attempt`                  | No of Attempt                          | `integer`   |     | ✅    |                        |
| `no_of_question`                 | No of Question from each Question Bank | `integer`   |     | ✅    |                        |
| `no_person`                      | No Person                              | `boolean`   |     | ✅    |                        |
| `not_attempt_ans`                | Display Not Attempted Answer           | `boolean`   |     | ✅    |                        |
| `parent_id`                      | Parent Quiz                            | `many2one`  |     | ✅    | op.quiz                |
| `particular_interval`            | Take Screenshots                       | `integer`   |     | ✅    |                        |
| `prev_allow`                     | Previous Question Allowed              | `boolean`   |     | ✅    |                        |
| `prev_readonly`                  | Only One Time Answer                   | `boolean`   |     | ✅    |                        |
| `que_required`                   | All Question are Required              | `boolean`   |     | ✅    |                        |
| `question_count`                 | Question Count                         | `integer`   |     |       |                        |
| `question_time_out`              | Question Time Out                      | `integer`   |     | ✅    |                        |
| `quiz_audio`                     | Audio File                             | `binary`    |     | ✅    |                        |
| `quiz_config`                    | Configuration                          | `selection` |     | ✅    |                        |
| `quiz_html`                      | HTML Content                           | `html`      |     | ✅    |                        |
| `quiz_message_ids`               | Message                                | `one2many`  |     | ✅    | op.quiz.result.message |
| `quiz_video`                     | Video File                             | `binary`    |     | ✅    |                        |
| `random_end`                     | End                                    | `integer`   |     | ✅    |                        |
| `random_start`                   | Start                                  | `integer`   |     | ✅    |                        |
| `rating_ids`                     | Ratings                                | `one2many`  |     | ✅    | rating.rating          |
| `right_ans`                      | Display Right Answer                   | `boolean`   |     | ✅    |                        |
| `show_header`                    | Show Header                            | `boolean`   |     | ✅    |                        |
| `show_result`                    | Display Result                         | `boolean`   |     | ✅    |                        |
| `shuffle`                        | Shuffle the Choices                    | `boolean`   |     | ✅    |                        |
| `single_que`                     | Single Question Per Page               | `boolean`   |     | ✅    |                        |
| `start_view`                     | Starting View                          | `selection` |     | ✅    |                        |
| `state`                          | Status                                 | `selection` |     | ✅    |                        |
| `student_ids`                    | Students                               | `many2many` |     | ✅    | op.student             |
| `take_screenshot`                | Take Screenshot                        | `selection` |     | ✅    |                        |
| `time_config`                    | Time Configuration                     | `boolean`   |     | ✅    |                        |
| `time_expire`                    | When Time Expires                      | `selection` |     | ✅    |                        |
| `time_limit_hr`                  | Hour                                   | `integer`   |     | ✅    |                        |
| `time_limit_minute`              | Minutes                                | `integer`   |     | ✅    |                        |
| `total_marks`                    | Total Marks                            | `float`     |     | ✅    |                        |
| `total_quiz_count`               | Total Quiz                             | `integer`   |     |       |                        |
| `warning_limit`                  | Warning Limit                          | `integer`   |     | ✅    |                        |
| `warning_state`                  | Warning State                          | `selection` |     | ✅    |                        |
| `website_message_ids`            | Website Messages                       | `one2many`  |     | ✅    | mail.message           |
| `write_date`                     | Last Updated on                        | `datetime`  |     | ✅    |                        |
| `write_uid`                      | Last Updated by                        | `many2one`  |     | ✅    | res.users              |
| `wrong_ans`                      | Display Wrong Answer                   | `boolean`   |     | ✅    |                        |

**Access Rights:**

| Name                             | Group          | Perms     |
| -------------------------------- | -------------- | --------- |
| access_op_quiz_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_quiz_portal            | Role / Portal  | `R`       |

**Record Rules:**

- **Quiz multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.course.question` — Content Quiz Question

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation         |
| -------------- | --------------- | ---------- | --- | ----- | ---------------- |
| `answer_ids`   | Answer          | `one2many` |     | ✅    | op.course.answer |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company      |
| `create_date`  | Created on      | `datetime` |     | ✅    |                  |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users        |
| `display_name` | Display Name    | `char`     |     |       |                  |
| `id`           | ID              | `integer`  |     | ✅    |                  |
| `question`     | Question Name   | `char`     | ✅  | ✅    |                  |
| `sequence`     | Sequence        | `integer`  |     | ✅    |                  |
| `slide_id`     | Content         | `many2one` | ✅  | ✅    | op.course.module |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                  |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users        |

**Access Rights:**

| Name                           | Group         | Perms     |
| ------------------------------ | ------------- | --------- |
| access_op_course_question      | LMS / Manager | `R/W/C/D` |
| access_op_course_question_user | LMS / User    | `R/W/C`   |

**Record Rules:**

- **Course Question multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.course.announcement` — Course Announcement

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label           | Type       | Req | Store | Relation  |
| ------------------- | --------------- | ---------- | --- | ----- | --------- |
| `announcement_html` | Description     | `html`     |     | ✅    |           |
| `course_id`         | Course          | `many2one` |     | ✅    | op.course |
| `create_date`       | Created on      | `datetime` |     | ✅    |           |
| `create_uid`        | Created by      | `many2one` |     | ✅    | res.users |
| `display_name`      | Display Name    | `char`     |     |       |           |
| `id`                | ID              | `integer`  |     | ✅    |           |
| `name`              | Title           | `char`     |     | ✅    |           |
| `user_id`           | User            | `many2one` |     | ✅    | res.users |
| `write_date`        | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`         | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                                 | Group         | Perms     |
| ------------------------------------ | ------------- | --------- |
| access_op_course_announcement        | LMS / Manager | `R/W/C/D` |
| access_op_course_announcement_user   | LMS / User    | `R/W/C`   |
| access_op_course_announcement_portal | Role / Portal | `R`       |
| access_op_course_announcementpublic  | Role / Public | `R`       |

### 🗃️ `op.course.enrollment.line` — Course Enrollment Lines

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label           | Type       | Req | Store | Relation             |
| ----------------- | --------------- | ---------- | --- | ----- | -------------------- |
| `completion_date` | Completion Date | `datetime` |     | ✅    |                      |
| `course_id`       | Course          | `many2one` |     |       | op.course            |
| `create_date`     | Created on      | `datetime` |     | ✅    |                      |
| `create_uid`      | Created by      | `many2one` |     | ✅    | res.users            |
| `display_name`    | Display Name    | `char`     |     |       |                      |
| `enrollment_id`   | Enrollment      | `many2one` |     | ✅    | op.course.enrollment |
| `id`              | ID              | `integer`  |     | ✅    |                      |
| `is_completed`    | Is Completed    | `boolean`  |     | ✅    |                      |
| `module_id`       | Module          | `many2one` |     | ✅    | op.course.module     |
| `quiz_result_id`  | Quiz Result     | `many2one` |     | ✅    | op.quiz.result       |
| `write_date`      | Last Updated on | `datetime` |     | ✅    |                      |
| `write_uid`       | Last Updated by | `many2one` |     | ✅    | res.users            |

**Access Rights:**

| Name                                    | Group         | Perms     |
| --------------------------------------- | ------------- | --------- |
| access_op_course_enrollment_line        | LMS / Manager | `R/W/C/D` |
| access_op_course_enrollment_line_user   | LMS / User    | `R/W/C`   |
| access_op_course_enrollment_line_portal | Role / Portal | `R/W/C`   |

### 🗃️ `op.course.tag` — Course Tag

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Tag             | `char`     |     | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                        | Group         | Perms     |
| --------------------------- | ------------- | --------- |
| access_op_course_tag        | LMS / Manager | `R/W/C/D` |
| access_op_course_tag_user   | LMS / User    | `R/W/C`   |
| access_op_course_tag_portal | Role / Portal | `R`       |
| access_op_course_tag_public | Role / Public | `R`       |

**Record Rules:**

- **course enrollment material multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.course.enrollment` — LMS Course Enrollment

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label                | Type        | Req | Store | Relation                  |
| ----------------- | -------------------- | ----------- | --- | ----- | ------------------------- |
| `access_token`    | Access Token         | `char`      |     | ✅    |                           |
| `access_url`      | Portal Access URL    | `char`      |     |       |                           |
| `company_id`      | Company              | `many2one`  |     | ✅    | res.company               |
| `completion_date` | Completion Date      | `datetime`  |     | ✅    |                           |
| `course_id`       | Course               | `many2one`  | ✅  | ✅    | op.course                 |
| `create_date`     | Created on           | `datetime`  |     | ✅    |                           |
| `create_uid`      | Created by           | `many2one`  |     | ✅    | res.users                 |
| `display_name`    | Display Name         | `char`      |     |       |                           |
| `enrollment_date` | Enrollment Date      | `datetime`  | ✅  | ✅    |                           |
| `enrollment_line` | Module Content       | `one2many`  |     | ✅    | op.course.enrollment.line |
| `id`              | ID                   | `integer`   |     | ✅    |                           |
| `index`           | Index                | `char`      |     | ✅    |                           |
| `last_module_id`  | Last Accessed Module | `many2one`  |     | ✅    | op.course.module          |
| `order_id`        | Order                | `many2one`  |     | ✅    | sale.order                |
| `progress`        | Progress             | `integer`   |     | ✅    |                           |
| `state`           | Status               | `selection` |     | ✅    |                           |
| `user_id`         | User                 | `many2one`  | ✅  | ✅    | res.users                 |
| `write_date`      | Last Updated on      | `datetime`  |     | ✅    |                           |
| `write_uid`       | Last Updated by      | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name                               | Group         | Perms     |
| ---------------------------------- | ------------- | --------- |
| access_op_course_enrollment        | LMS / Manager | `R/W/C/D` |
| access_op_course_enrollment_user   | LMS / User    | `R/W/C`   |
| access_op_course_enrollment_portal | Role / Portal | `R/W/C`   |
| access_op_course_enrollment_public | Role / Public | `R`       |

**Record Rules:**

- **Course Enrollment multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `lms.stats` — LMS Stats

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
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name             | Group       | Perms |
| ---------------- | ----------- | ----- |
| access_lms_stats | Role / User | `R`   |

### 🗃️ `op.course.answer` — Slide Question's Answer

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label             | Type       | Req | Store | Relation           |
| -------------- | ----------------- | ---------- | --- | ----- | ------------------ |
| `comment`      | Comment           | `text`     |     | ✅    |                    |
| `create_date`  | Created on        | `datetime` |     | ✅    |                    |
| `create_uid`   | Created by        | `many2one` |     | ✅    | res.users          |
| `display_name` | Display Name      | `char`     |     |       |                    |
| `id`           | ID                | `integer`  |     | ✅    |                    |
| `is_correct`   | Is correct answer | `boolean`  |     | ✅    |                    |
| `question_id`  | Question          | `many2one` | ✅  | ✅    | op.course.question |
| `sequence`     | Sequence          | `integer`  |     | ✅    |                    |
| `text_value`   | Answer            | `char`     | ✅  | ✅    |                    |
| `write_date`   | Last Updated on   | `datetime` |     | ✅    |                    |
| `write_uid`    | Last Updated by   | `many2one` |     | ✅    | res.users          |

**Access Rights:**

| Name                         | Group         | Perms     |
| ---------------------------- | ------------- | --------- |
| access_op_course_answer      | LMS / Manager | `R/W/C/D` |
| access_op_course_answer_user | LMS / User    | `R/W/C`   |

### 🗃️ `website` — Website

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                       | Label                                                            | Type        | Req | Store | Relation                 |
| ------------------------------------------- | ---------------------------------------------------------------- | ----------- | --- | ----- | ------------------------ |
| `account_on_checkout`                       | Customer Accounts                                                | `selection` |     | ✅    |                          |
| `add_to_cart_action`                        | Add To Cart Action                                               | `selection` |     | ✅    |                          |
| `auth_signup_uninvited`                     | Customer Account                                                 | `selection` |     | ✅    |                          |
| `auto_redirect_lang`                        | Autoredirect Language                                            | `boolean`   |     | ✅    |                          |
| `blocked_third_party_domains`               | List of blocked 3rd-party domains                                | `text`      |     |       |                          |
| `block_third_party_domains`                 | Block 3rd-party domains                                          | `boolean`   |     | ✅    |                          |
| `cart_abandoned_delay`                      | Abandoned Delay                                                  | `float`     |     | ✅    |                          |
| `cart_recovery_mail_template_id`            | Cart Recovery Email                                              | `many2one`  |     | ✅    | mail.template            |
| `cdn_activated`                             | Content Delivery Network (CDN)                                   | `boolean`   |     | ✅    |                          |
| `cdn_filters`                               | CDN Filters                                                      | `text`      |     | ✅    |                          |
| `cdn_url`                                   | CDN Base URL                                                     | `char`      |     | ✅    |                          |
| `channel_id`                                | Website Live Chat Channel                                        | `many2one`  |     | ✅    | im_livechat.channel      |
| `company_id`                                | Company                                                          | `many2one`  | ✅  | ✅    | res.company              |
| `configurator_done`                         | Configurator Done                                                | `boolean`   |     | ✅    |                          |
| `confirmation_email_template_id`            | Confirmation Email Template                                      | `many2one`  |     | ✅    | mail.template            |
| `contact_us_button_url`                     | Contact Us Button URL                                            | `char`      |     | ✅    |                          |
| `cookies_bar`                               | Cookies Bar                                                      | `boolean`   |     | ✅    |                          |
| `create_date`                               | Created on                                                       | `datetime`  |     | ✅    |                          |
| `create_uid`                                | Created by                                                       | `many2one`  |     | ✅    | res.users                |
| `crm_default_team_id`                       | Default Sales Teams                                              | `many2one`  |     | ✅    | crm.team                 |
| `crm_default_user_id`                       | Default Salesperson                                              | `many2one`  |     | ✅    | res.users                |
| `currency_id`                               | Default Currency                                                 | `many2one`  |     |       | res.currency             |
| `custom_blocked_third_party_domains`        | User list of blocked 3rd-party domains                           | `text`      |     | ✅    |                          |
| `custom_code_footer`                        | Custom end of <body> code                                        | `html`      |     | ✅    |                          |
| `custom_code_head`                          | Custom <head> code                                               | `html`      |     | ✅    |                          |
| `default_lang_id`                           | Default Language                                                 | `many2one`  | ✅  | ✅    | res.lang                 |
| `display_name`                              | Display Name                                                     | `char`      |     |       |                          |
| `domain`                                    | Website Domain                                                   | `char`      |     | ✅    |                          |
| `domain_punycode`                           | Punycode Domain                                                  | `char`      |     |       |                          |
| `ecommerce_access`                          | Ecommerce Access                                                 | `selection` | ✅  | ✅    |                          |
| `enabled_gmc_src`                           | Google Merchant Center                                           | `boolean`   |     | ✅    |                          |
| `favicon`                                   | Website Favicon                                                  | `binary`    |     | ✅    |                          |
| `forum_count`                               | Forum Count                                                      | `integer`   |     | ✅    |                          |
| `google_analytics_key`                      | Google Analytics Key                                             | `char`      |     | ✅    |                          |
| `google_maps_api_key`                       | Google Maps API Key                                              | `char`      |     | ✅    |                          |
| `google_search_console`                     | Google Search Console                                            | `char`      |     | ✅    |                          |
| `has_social_default_image`                  | Has Social Default Image                                         | `boolean`   |     | ✅    |                          |
| `homepage_url`                              | Homepage Url                                                     | `char`      |     | ✅    |                          |
| `id`                                        | ID                                                               | `integer`   |     | ✅    |                          |
| `karma_profile_min`                         | Minimal karma to see other user's profile                        | `integer`   |     | ✅    |                          |
| `language_count`                            | Number of languages                                              | `integer`   |     |       |                          |
| `language_ids`                              | Languages                                                        | `many2many` | ✅  | ✅    | res.lang                 |
| `logo`                                      | Website Logo                                                     | `binary`    |     | ✅    |                          |
| `menu_id`                                   | Main Menu                                                        | `many2one`  |     |       | website.menu             |
| `name`                                      | Website Name                                                     | `char`      | ✅  | ✅    |                          |
| `newsletter_id`                             | Newsletter List                                                  | `many2one`  |     | ✅    | mailing.list             |
| `partner_id`                                | Public Partner                                                   | `many2one`  |     |       | res.partner              |
| `plausible_shared_key`                      | Plausible Shared Key                                             | `char`      |     | ✅    |                          |
| `plausible_site`                            | Plausible Site                                                   | `char`      |     | ✅    |                          |
| `prevent_zero_price_sale`                   | Hide 'Add To Cart' when price = 0                                | `boolean`   |     | ✅    |                          |
| `pricelist_ids`                             | Price list available for this Ecommerce/Website                  | `one2many`  |     |       | product.pricelist        |
| `product_page_cols_order`                   | Product Page main columns order                                  | `selection` |     | ✅    |                          |
| `product_page_container`                    | Product Page Container                                           | `selection` |     | ✅    |                          |
| `product_page_grid_columns`                 | Product Page Grid Columns                                        | `integer`   |     | ✅    |                          |
| `product_page_image_layout`                 | Product Page Image Layout                                        | `selection` | ✅  | ✅    |                          |
| `product_page_image_ratio`                  | Product Page Image Ratio                                         | `selection` | ✅  | ✅    |                          |
| `product_page_image_ratio_mobile`           | Product Page Image Ratio Mobile                                  | `selection` | ✅  | ✅    |                          |
| `product_page_image_roundness`              | Product Page Image Roundness                                     | `selection` | ✅  | ✅    |                          |
| `product_page_image_spacing`                | Product Page Image Spacing                                       | `selection` | ✅  | ✅    |                          |
| `product_page_image_width`                  | Product Page Image Width                                         | `selection` | ✅  | ✅    |                          |
| `robots_txt`                                | Robots.txt                                                       | `html`      |     | ✅    |                          |
| `salesperson_id`                            | Salesperson                                                      | `many2one`  |     | ✅    | res.users                |
| `salesteam_id`                              | Sales Team                                                       | `many2one`  |     | ✅    | crm.team                 |
| `send_abandoned_cart_email`                 | Send email to customers who abandoned their cart.                | `boolean`   |     | ✅    |                          |
| `send_abandoned_cart_email_activation_time` | Time when the 'Send abandoned cart email' feature was activated. | `datetime`  |     | ✅    |                          |
| `sequence`                                  | Sequence                                                         | `integer`   |     | ✅    |                          |
| `shop_default_sort`                         | Shop Default Sort                                                | `selection` | ✅  | ✅    |                          |
| `shop_extra_field_ids`                      | E-Commerce Extra Fields                                          | `one2many`  |     | ✅    | website.sale.extra.field |
| `shop_gap`                                  | Grid-gap on the shop                                             | `char`      |     | ✅    |                          |
| `shop_opt_products_design_classes`          | Shop Design Class                                                | `char`      |     | ✅    |                          |
| `shop_page_container`                       | Shop Page Container                                              | `selection` |     | ✅    |                          |
| `shop_ppg`                                  | Number of products in the grid on the shop                       | `integer`   |     | ✅    |                          |
| `shop_ppr`                                  | Number of grid columns on the shop                               | `integer`   |     | ✅    |                          |
| `show_line_subtotals_tax_selection`         | Line Subtotals Tax Display                                       | `selection` |     | ✅    |                          |
| `social_default_image`                      | Default Social Share Image                                       | `binary`    |     | ✅    |                          |
| `social_discord`                            | Discord Account                                                  | `char`      |     | ✅    |                          |
| `social_facebook`                           | Facebook Account                                                 | `char`      |     | ✅    |                          |
| `social_github`                             | GitHub Account                                                   | `char`      |     | ✅    |                          |
| `social_instagram`                          | Instagram Account                                                | `char`      |     | ✅    |                          |
| `social_linkedin`                           | LinkedIn Account                                                 | `char`      |     | ✅    |                          |
| `social_tiktok`                             | TikTok Account                                                   | `char`      |     | ✅    |                          |
| `social_twitter`                            | X Account                                                        | `char`      |     | ✅    |                          |
| `social_youtube`                            | Youtube Account                                                  | `char`      |     | ✅    |                          |
| `specific_user_account`                     | Specific User Account                                            | `boolean`   |     | ✅    |                          |
| `theme_id`                                  | Theme                                                            | `many2one`  |     | ✅    | ir.module.module         |
| `user_id`                                   | Public User                                                      | `many2one`  | ✅  | ✅    | res.users                |
| `warehouse_id`                              | Warehouse                                                        | `many2one`  |     | ✅    | stock.warehouse          |
| `wishlist_gap`                              | Wishlist Grid Gap                                                | `char`      |     | ✅    |                          |
| `wishlist_grid_columns`                     | Wishlist Grid Columns                                            | `integer`   |     | ✅    |                          |
| `wishlist_mobile_columns`                   | Wishlist Mobile Columns                                          | `integer`   |     | ✅    |                          |
| `wishlist_opt_products_design_classes`      | Wishlist Page Design Class                                       | `char`      |     | ✅    |                          |
| `write_date`                                | Last Updated on                                                  | `datetime`  |     | ✅    |                          |
| `write_uid`                                 | Last Updated by                                                  | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                     | Group                         | Perms     |
| ------------------------ | ----------------------------- | --------- |
| website.website.designer | Website / Editor and Designer | `R/W/C/D` |
| website.public           | Role / Portal                 | `R`       |
| website.public           | Role / Public                 | `R`       |
| website.public           | Role / User                   | `R`       |
