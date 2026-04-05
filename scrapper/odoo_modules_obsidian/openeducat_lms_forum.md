---
title: "OpenEduCat LMS Forum"
module: "openeducat_lms_forum"
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

# 🟢 OpenEduCat LMS Forum

> **Module:** `openeducat_lms_forum` | **Version:** `19.0.1.0` **Category:** Education |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[website_forum]] [[openeducat_lms]] [[base]]

## 📖 Description

## OpenEduCat LMS Forum

[![](/openeducat_lms_forum/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module adds the feature of forum in learning management system to OpenEduCat. You
can create forum of course and post it online.

[Contact Us](https://www.openeducat.org/contactus/)

## Forum

### Create forum for your course. Create forum post and publish it online.

![](/openeducat_lms_forum/static/description/lms_forum_tab.png)

## Forum Post

### Create forum post under that forum and publish it.

![](/openeducat_lms_forum/static/description/lms_forum_posts.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `LMS/Reporting/Forum Participation`

### Views

- `* INHERIT course_detail_inherit (qweb)`
- `* INHERIT course_detail_inherit_one (qweb)`
- `* INHERIT course_detail_inherit_two (qweb)`
- `* INHERIT lms.forum.forum.form (form)`
- `* INHERIT lms.forum.post.list (list)`
- `* INHERIT op.course.form.forum.inherit (form)`
- `* INHERIT op.course.lms.forum.list (list)`
- `lms.course.forum.graph (graph)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

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

### 🗃️ `forum.forum` — Forum

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                                  | Type        | Req | Store | Relation       |
| -------------------------------- | -------------------------------------- | ----------- | --- | ----- | -------------- |
| `active`                         | Active                                 | `boolean`   |     | ✅    |                |
| `allow_share`                    | Sharing Options                        | `boolean`   |     | ✅    |                |
| `authorized_group_id`            | Authorized Group                       | `many2one`  |     | ✅    | res.groups     |
| `can_moderate`                   | Is a moderator                         | `boolean`   |     |       |                |
| `count_flagged_posts`            | Number of flagged posts                | `integer`   |     |       |                |
| `count_posts_waiting_validation` | Number of posts waiting for validation | `integer`   |     |       |                |
| `course_id`                      | Course                                 | `many2one`  |     | ✅    | op.course      |
| `create_date`                    | Created on                             | `datetime`  |     | ✅    |                |
| `create_uid`                     | Created by                             | `many2one`  |     | ✅    | res.users      |
| `default_order`                  | Default                                | `selection` | ✅  | ✅    |                |
| `description`                    | Description                            | `text`      |     | ✅    |                |
| `display_name`                   | Display Name                           | `char`      |     |       |                |
| `faq`                            | Guidelines                             | `html`      |     | ✅    |                |
| `has_message`                    | Has Message                            | `boolean`   |     |       |                |
| `has_pending_post`               | Has pending post                       | `boolean`   |     |       |                |
| `id`                             | ID                                     | `integer`   |     | ✅    |                |
| `image_1024`                     | Image 1024                             | `binary`    |     | ✅    |                |
| `image_128`                      | Image 128                              | `binary`    |     | ✅    |                |
| `image_1920`                     | Image                                  | `binary`    |     | ✅    |                |
| `image_256`                      | Image 256                              | `binary`    |     | ✅    |                |
| `image_512`                      | Image 512                              | `binary`    |     | ✅    |                |
| `is_seo_optimized`               | SEO optimized                          | `boolean`   |     | ✅    |                |
| `karma_answer`                   | Answer questions                       | `integer`   |     | ✅    |                |
| `karma_answer_accept_all`        | Accept an answer to all questions      | `integer`   |     | ✅    |                |
| `karma_answer_accept_own`        | Accept an answer on own questions      | `integer`   |     | ✅    |                |
| `karma_ask`                      | Ask questions                          | `integer`   |     | ✅    |                |
| `karma_close_all`                | Close all posts                        | `integer`   |     | ✅    |                |
| `karma_close_own`                | Close own posts                        | `integer`   |     | ✅    |                |
| `karma_comment_all`              | Comment all posts                      | `integer`   |     | ✅    |                |
| `karma_comment_convert_all`      | Convert all comments to answers        | `integer`   |     | ✅    |                |
| `karma_comment_convert_own`      | Convert own comments to answers        | `integer`   |     | ✅    |                |
| `karma_comment_own`              | Comment own posts                      | `integer`   |     | ✅    |                |
| `karma_comment_unlink_all`       | Delete all comments                    | `integer`   |     | ✅    |                |
| `karma_comment_unlink_own`       | Delete own comments                    | `integer`   |     | ✅    |                |
| `karma_dofollow`                 | Nofollow links                         | `integer`   |     | ✅    |                |
| `karma_downvote`                 | Downvote                               | `integer`   |     | ✅    |                |
| `karma_edit_all`                 | Edit all posts                         | `integer`   |     | ✅    |                |
| `karma_editor`                   | Editor Features: image and links       | `integer`   |     | ✅    |                |
| `karma_edit_own`                 | Edit own posts                         | `integer`   |     | ✅    |                |
| `karma_edit_retag`               | Change question tags                   | `integer`   |     | ✅    |                |
| `karma_flag`                     | Flag a post as offensive               | `integer`   |     | ✅    |                |
| `karma_gen_answer_accept`        | Accepting an answer                    | `integer`   |     | ✅    |                |
| `karma_gen_answer_accepted`      | Answer accepted                        | `integer`   |     | ✅    |                |
| `karma_gen_answer_downvote`      | Answer downvoted                       | `integer`   |     | ✅    |                |
| `karma_gen_answer_flagged`       | Answer flagged                         | `integer`   |     | ✅    |                |
| `karma_gen_answer_upvote`        | Answer upvoted                         | `integer`   |     | ✅    |                |
| `karma_gen_question_downvote`    | Question downvoted                     | `integer`   |     | ✅    |                |
| `karma_gen_question_new`         | Asking a question                      | `integer`   |     | ✅    |                |
| `karma_gen_question_upvote`      | Question upvoted                       | `integer`   |     | ✅    |                |
| `karma_moderate`                 | Moderate posts                         | `integer`   |     | ✅    |                |
| `karma_post`                     | Ask questions without validation       | `integer`   |     | ✅    |                |
| `karma_tag_create`               | Create new tags                        | `integer`   |     | ✅    |                |
| `karma_unlink_all`               | Delete all posts                       | `integer`   |     | ✅    |                |
| `karma_unlink_own`               | Delete own posts                       | `integer`   |     | ✅    |                |
| `karma_upvote`                   | Upvote                                 | `integer`   |     | ✅    |                |
| `karma_user_bio`                 | Display detailed user biography        | `integer`   |     | ✅    |                |
| `last_post_id`                   | Last Post                              | `many2one`  |     |       | forum.post     |
| `message_attachment_count`       | Attachment Count                       | `integer`   |     |       |                |
| `message_follower_ids`           | Followers                              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`              | Message Delivery error                 | `boolean`   |     |       |                |
| `message_has_error_counter`      | Number of errors                       | `integer`   |     |       |                |
| `message_has_sms_error`          | SMS Delivery error                     | `boolean`   |     |       |                |
| `message_ids`                    | Messages                               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`            | Is Follower                            | `boolean`   |     |       |                |
| `message_needaction`             | Action Needed                          | `boolean`   |     |       |                |
| `message_needaction_counter`     | Number of Actions                      | `integer`   |     |       |                |
| `message_partner_ids`            | Followers (Partners)                   | `many2many` |     |       | res.partner    |
| `mode`                           | Mode                                   | `selection` | ✅  | ✅    |                |
| `name`                           | Forum Name                             | `char`      | ✅  | ✅    |                |
| `post_ids`                       | Posts                                  | `one2many`  |     | ✅    | forum.post     |
| `privacy`                        | Privacy                                | `selection` |     | ✅    |                |
| `rating_ids`                     | Ratings                                | `one2many`  |     | ✅    | rating.rating  |
| `relevancy_post_vote`            | First Relevance Parameter              | `float`     |     | ✅    |                |
| `relevancy_time_decay`           | Second Relevance Parameter             | `float`     |     | ✅    |                |
| `seo_name`                       | Seo name                               | `char`      |     | ✅    |                |
| `sequence`                       | Sequence                               | `integer`   |     | ✅    |                |
| `tag_ids`                        | Tags                                   | `one2many`  |     | ✅    | forum.tag      |
| `tag_most_used_ids`              | Most used tags                         | `one2many`  |     |       | forum.tag      |
| `tag_unused_ids`                 | Unused tags                            | `one2many`  |     |       | forum.tag      |
| `total_answers`                  | # Answers                              | `integer`   |     |       |                |
| `total_favorites`                | # Favorites                            | `integer`   |     |       |                |
| `total_posts`                    | # Posts                                | `integer`   |     |       |                |
| `total_views`                    | # Views                                | `integer`   |     |       |                |
| `website_id`                     | Website                                | `many2one`  |     | ✅    | website        |
| `website_message_ids`            | Website Messages                       | `one2many`  |     | ✅    | mail.message   |
| `website_meta_description`       | Website meta description               | `text`      |     | ✅    |                |
| `website_meta_keywords`          | Website meta keywords                  | `char`      |     | ✅    |                |
| `website_meta_og_img`            | Website opengraph image                | `char`      |     | ✅    |                |
| `website_meta_title`             | Website meta title                     | `char`      |     | ✅    |                |
| `welcome_message`                | Welcome Message                        | `html`      |     | ✅    |                |
| `write_date`                     | Last Updated on                        | `datetime`  |     | ✅    |                |
| `write_uid`                      | Last Updated by                        | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                | Group         | Perms     |
| ------------------- | ------------- | --------- |
| forum.forum.maanger | Access Rights | `R/W/C/D` |
| forum.forum         | Role / Portal | `R`       |
| forum.forum         | Role / Public | `R`       |
| forum.forum         | Role / User   | `R`       |

**Record Rules:**

- **Website forum: Public user can only access to public forum** (11) `R/W/C/D`
  - Domain: `[('privacy', '=', 'public')]`
- **Website forum: User can only access to public (or authorized) forum** (10, 1)
  `R/W/C/D`
  - Domain:
    `[         '|',             ('privacy', 'in', ['public', 'connected']),             '&',                 ('privacy', '=', 'private'),                 ('authorized_group_id', 'in', user.all_group_ids.ids)]`
- **Website forum: Website designer can create private forum** (72) `C`
  - Domain: `[(1, '=', 1)]`
- **Website forum: All access for manager** (2) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `forum.post` — Forum Post

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                                           | Type        | Req | Store | Relation          |
| ---------------------------- | ----------------------------------------------- | ----------- | --- | ----- | ----------------- |
| `active`                     | Active                                          | `boolean`   |     | ✅    |                   |
| `can_accept`                 | Can Accept                                      | `boolean`   |     |       |                   |
| `can_answer`                 | Can Answer                                      | `boolean`   |     |       |                   |
| `can_ask`                    | Can Ask                                         | `boolean`   |     |       |                   |
| `can_close`                  | Can Close                                       | `boolean`   |     |       |                   |
| `can_comment`                | Can Comment                                     | `boolean`   |     |       |                   |
| `can_comment_convert`        | Can Convert to Comment                          | `boolean`   |     |       |                   |
| `can_display_biography`      | Is the author's biography visible from his post | `boolean`   |     |       |                   |
| `can_downvote`               | Can Downvote                                    | `boolean`   |     |       |                   |
| `can_edit`                   | Can Edit                                        | `boolean`   |     |       |                   |
| `can_flag`                   | Can Flag                                        | `boolean`   |     |       |                   |
| `can_moderate`               | Can Moderate                                    | `boolean`   |     |       |                   |
| `can_post`                   | Can Automatically be Validated                  | `boolean`   |     |       |                   |
| `can_unlink`                 | Can Unlink                                      | `boolean`   |     |       |                   |
| `can_upvote`                 | Can Upvote                                      | `boolean`   |     |       |                   |
| `can_use_full_editor`        | Can Use Full Editor                             | `boolean`   |     |       |                   |
| `can_view`                   | Can View                                        | `boolean`   |     |       |                   |
| `child_count`                | Answers                                         | `integer`   |     | ✅    |                   |
| `child_ids`                  | Post Answers                                    | `one2many`  |     | ✅    | forum.post        |
| `closed_date`                | Closed on                                       | `datetime`  |     | ✅    |                   |
| `closed_reason_id`           | Reason                                          | `many2one`  |     | ✅    | forum.post.reason |
| `closed_uid`                 | Closed by                                       | `many2one`  |     | ✅    | res.users         |
| `content`                    | Content                                         | `html`      |     | ✅    |                   |
| `course_id`                  | Course                                          | `many2one`  |     | ✅    | op.course         |
| `create_date`                | Asked on                                        | `datetime`  |     | ✅    |                   |
| `create_uid`                 | Created by                                      | `many2one`  |     | ✅    | res.users         |
| `display_name`               | Display Name                                    | `char`      |     |       |                   |
| `favourite_count`            | Favorite                                        | `integer`   |     | ✅    |                   |
| `favourite_ids`              | Favourite                                       | `many2many` |     | ✅    | res.users         |
| `flag_user_id`               | Flagged by                                      | `many2one`  |     | ✅    | res.users         |
| `forum_id`                   | Forum                                           | `many2one`  | ✅  | ✅    | forum.forum       |
| `has_message`                | Has Message                                     | `boolean`   |     |       |                   |
| `has_validated_answer`       | Is answered                                     | `boolean`   |     | ✅    |                   |
| `id`                         | ID                                              | `integer`   |     | ✅    |                   |
| `is_correct`                 | Correct                                         | `boolean`   |     | ✅    |                   |
| `is_seo_optimized`           | SEO optimized                                   | `boolean`   |     | ✅    |                   |
| `karma_accept`               | Convert comment to answer                       | `integer`   |     |       |                   |
| `karma_close`                | Karma to close                                  | `integer`   |     |       |                   |
| `karma_comment`              | Karma to comment                                | `integer`   |     |       |                   |
| `karma_comment_convert`      | Karma to convert comment to answer              | `integer`   |     |       |                   |
| `karma_edit`                 | Karma to edit                                   | `integer`   |     |       |                   |
| `karma_flag`                 | Flag a post as offensive                        | `integer`   |     |       |                   |
| `karma_unlink`               | Karma to unlink                                 | `integer`   |     |       |                   |
| `last_activity_date`         | Last activity on                                | `datetime`  | ✅  | ✅    |                   |
| `message_attachment_count`   | Attachment Count                                | `integer`   |     |       |                   |
| `message_follower_ids`       | Followers                                       | `one2many`  |     | ✅    | mail.followers    |
| `message_has_error`          | Message Delivery error                          | `boolean`   |     |       |                   |
| `message_has_error_counter`  | Number of errors                                | `integer`   |     |       |                   |
| `message_has_sms_error`      | SMS Delivery error                              | `boolean`   |     |       |                   |
| `message_ids`                | Messages                                        | `one2many`  |     | ✅    | mail.message      |
| `message_is_follower`        | Is Follower                                     | `boolean`   |     |       |                   |
| `message_needaction`         | Action Needed                                   | `boolean`   |     |       |                   |
| `message_needaction_counter` | Number of Actions                               | `integer`   |     |       |                   |
| `message_partner_ids`        | Followers (Partners)                            | `many2many` |     |       | res.partner       |
| `moderator_id`               | Reviewed by                                     | `many2one`  |     | ✅    | res.users         |
| `name`                       | Title                                           | `char`      |     | ✅    |                   |
| `parent_id`                  | Question                                        | `many2one`  |     | ✅    | forum.post        |
| `plain_content`              | Plain Content                                   | `text`      |     | ✅    |                   |
| `rating_ids`                 | Ratings                                         | `one2many`  |     | ✅    | rating.rating     |
| `relevancy`                  | Relevance                                       | `float`     |     | ✅    |                   |
| `self_reply`                 | Reply to own question                           | `boolean`   |     | ✅    |                   |
| `seo_name`                   | Seo name                                        | `char`      |     | ✅    |                   |
| `state`                      | Status                                          | `selection` |     | ✅    |                   |
| `tag_ids`                    | Tags                                            | `many2many` |     | ✅    | forum.tag         |
| `uid_has_answered`           | Has Answered                                    | `boolean`   |     |       |                   |
| `user_favourite`             | Is Favourite                                    | `boolean`   |     |       |                   |
| `user_vote`                  | My Vote                                         | `integer`   |     |       |                   |
| `views`                      | Views                                           | `integer`   |     | ✅    |                   |
| `vote_count`                 | Total Votes                                     | `integer`   |     | ✅    |                   |
| `vote_ids`                   | Votes                                           | `one2many`  |     | ✅    | forum.post.vote   |
| `website_id`                 | Website                                         | `many2one`  |     |       | website           |
| `website_message_ids`        | Website Messages                                | `one2many`  |     | ✅    | mail.message      |
| `website_meta_description`   | Website meta description                        | `text`      |     | ✅    |                   |
| `website_meta_keywords`      | Website meta keywords                           | `char`      |     | ✅    |                   |
| `website_meta_og_img`        | Website opengraph image                         | `char`      |     | ✅    |                   |
| `website_meta_title`         | Website meta title                              | `char`      |     | ✅    |                   |
| `website_url`                | Website URL                                     | `char`      |     |       |                   |
| `write_date`                 | Updated on                                      | `datetime`  |     | ✅    |                   |
| `write_uid`                  | Updated by                                      | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                          | Group         | Perms     |
| ----------------------------- | ------------- | --------- |
| access_op_material_op_faculty | LMS / User    | `R/W/C/D` |
| forum.post.portal             | Role / Portal | `R/W/C/D` |
| forum.post.public             | Role / Public | `R`       |
| forum.post.user               | Role / User   | `R/W/C/D` |

**Record Rules:**

- **Website forum post: Public user can only access to public post** (11) `R/W/C/D`
  - Domain: `[('forum_id.privacy', '=', 'public')]`
- **Website forum post: User can only access to public (or authorized) post** (10, 1)
  `R/W/C/D`
  - Domain:
    `['|', ('forum_id.privacy', 'in', ['public', 'connected']), '&', ('forum_id.privacy', '=', 'private'), ('forum_id.authorized_group_id', 'in', user.all_group_ids.ids)]`
- **Website forum post : All access for manager** (2) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
