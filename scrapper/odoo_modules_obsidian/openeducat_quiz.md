---
title: "OpenEduCat Quiz Management"
module: "openeducat_quiz"
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

# 🟢 OpenEduCat Quiz Management

> **Module:** `openeducat_quiz` | **Version:** `19.0.1.0` **Category:** Education |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[base]] [[portal]] [[gamification]] [[openeducat_core_enterprise]] [[openeducat_web]]
[[openeducat_onboarding]]

## 📖 Description

## OpenEduCat Quiz / Exam

### OpenEduCat Quiz module provides facility to conduct online exam platform

[![](/openeducat_quiz/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

Based on best of class enterprise level architecture, OpenEduCat is ready to be used
from local infrastructure to a highly scalable cloud environment.

[Contact Us](https://www.openeducat.org/contactus/)

## Question Bank Type

User can add multiple question bank types.

![](/openeducat_quiz/static/description/question_bank_type.png)

## Question Bank

![](/openeducat_quiz/static/description/question_bank.png)

Question Bank is a collection of different questions and answers.

## Quiz Category

User can define multiple quiz category.

![](/openeducat_quiz/static/description/quiz_category.png)

## Quiz / Exam

![](/openeducat_quiz/static/description/quiz.png)

User can create a quiz / exam with different configuration and also set exams timing.

## Quiz Configuration

User can modified exam view with different configurations

![](/openeducat_quiz/static/description/quiz_config.png)

## Exam Attempt

![](/openeducat_quiz/static/description/Exam_main_view.png)

User can attempt multiple exams

## Exam View

User can jump any question while exam if configured

![](/openeducat_quiz/static/description/single_page_question_quiz.png)

## Result Overview

![](/openeducat_quiz/static/description/result_overview.png)

User can see their results anytime

## Results

Faculty can see all attempted results

![](/openeducat_quiz/static/description/results.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Quiz`
- `Quiz/Configuration`
- `Quiz/Configuration/Grades`
- `Quiz/Configuration/Question Bank Type`
- `Quiz/Configuration/Quiz Category`
- `Quiz/Configuration/Settings`
- `Quiz/Question Bank`
- `Quiz/Question Bank/Question Bank`
- `Quiz/Quiz`
- `Quiz/Quiz/Quiz`
- `Quiz/Quiz/Results`
- `Quiz/Reporting`
- `Quiz/Reporting/Quiz Result Analysis`

### Views

- `* INHERIT Portal layout : Quiz (qweb)`
- `* INHERIT Show Quiz Result (qweb)`
- `* INHERIT quiz_notification_inherit (qweb)`
- `Embedded Material Page (qweb)`
- `Exam Main View (qweb)`
- `Exam Main View (qweb)`
- `Exam Results (qweb)`
- `Exam View (qweb)`
- `Forbidden Embedded Slide (qweb)`
- `Quiz Attempt Form (qweb)`
- `Quiz Attempt Form (qweb)`
- `Quiz Completed (qweb)`
- `Quiz Questions (qweb)`
- `Quiz Questions (qweb)`
- `Quiz Questions (qweb)`
- `Quiz Questions (qweb)`
- `Quiz Questions Form View (qweb)`
- `Quiz Questions Form View (qweb)`
- `Quiz Results (qweb)`
- `Quiz Results Form (qweb)`
- `Quiz Starting Page (qweb)`
- `Users Profile (qweb)`
- `Website slides embed assets (qweb)`
- `my_result (qweb)`
- `op.answer.grade.form (form)`
- `op.answer.grade.list (list)`
- `op.answer.grade.search (search)`
- `op.override.mark.wizard.form (form)`
- `op.question.bank.form (form)`
- `op.question.bank.form (form)`
- `op.question.bank.list (list)`
- `op.question.bank.search (search)`
- `op.question.bank.type.form (form)`
- `op.question.bank.type.list (list)`
- `op.question.bank.type.search (search)`
- `op.question.wizard.form (form)`
- `op.quiz.category.form (form)`
- `op.quiz.category.list (list)`
- `op.quiz.category.search (search)`
- `op.quiz.form (form)`
- `op.quiz.form (form)`
- `op.quiz.list (list)`
- `op.quiz.result.form (form)`
- `op.quiz.result.list (list)`
- `op.quiz.result.pivot (pivot)`
- `op.quiz.result.search (search)`
- `op.quiz.search (search)`
- `op.update.mark.wizard.form (form)`
- `quiz_first_question (qweb)`
- `quiz_last_question (qweb)`
- `quiz_middle_question (qweb)`
- `quiz_render_single_form_view (qweb)`
- `quiz_render_single_form_view_fullscreen (qweb)`
- `quiz_web_page_fullscreen_template (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**31 model(s) defined by this module:**

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

### 🗃️ `op.quiz.result` — Quiz Results

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation               |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ---------------------- |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event         |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                        |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                        |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                        |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity          |
| `activity_state`                | Activity State                | `selection` |     |       |                        |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                        |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                        |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type     |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users              |
| `answered_question_count`       | Answered Question Count       | `integer`   |     | ✅    |                        |
| `categ_id`                      | Quiz Category                 | `many2one`  |     | ✅    | op.quiz.category       |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company            |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                        |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users              |
| `display_name`                  | Display Name                  | `char`      |     |       |                        |
| `finish_date`                   | Finished On                   | `datetime`  |     | ✅    |                        |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                        |
| `id`                            | ID                            | `integer`   |     | ✅    |                        |
| `index`                         | Index                         | `char`      | ✅  | ✅    |                        |
| `is_read`                       | Read?                         | `boolean`   |     | ✅    |                        |
| `line_ids`                      | Result Line                   | `one2many`  |     | ✅    | op.quiz.result.line    |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                        |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers         |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                        |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                        |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                        |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message           |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                        |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                        |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                        |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner            |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                        |
| `name`                          | Name                          | `char`      |     | ✅    |                        |
| `not_answered_question_count`   | Not Answered Question Count   | `integer`   |     | ✅    |                        |
| `override`                      | Override                      | `boolean`   |     | ✅    |                        |
| `quiz_id`                       | Quiz                          | `many2one`  |     | ✅    | op.quiz                |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating          |
| `received_marks`                | Received Marks                | `float`     |     | ✅    |                        |
| `score`                         | Score (%)                     | `float`     |     | ✅    |                        |
| `state`                         | Status                        | `selection` |     | ✅    |                        |
| `submit_date`                   | Submitted On                  | `datetime`  |     | ✅    |                        |
| `time_spent_hr`                 | Spent Hours                   | `integer`   |     | ✅    |                        |
| `time_spent_minute`             | Spent Minutes                 | `integer`   |     | ✅    |                        |
| `time_spent_second`             | Spent Seconds                 | `integer`   |     | ✅    |                        |
| `total_correct`                 | Total Correct                 | `integer`   |     | ✅    |                        |
| `total_incorrect`               | Total Incorrect               | `integer`   |     | ✅    |                        |
| `total_marks`                   | Total Marks                   | `float`     |     | ✅    |                        |
| `total_not_attempt`             | Total Not Attempt             | `float`     |     | ✅    |                        |
| `total_question`                | Total Question                | `integer`   |     | ✅    |                        |
| `user_id`                       | User                          | `many2one`  |     | ✅    | res.users              |
| `warning_line_ids`              | Warning Line                  | `one2many`  |     | ✅    | op.quiz.result.warning |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message           |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                        |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                                    | Group          | Perms     |
| --------------------------------------- | -------------- | --------- |
| access_op_quiz_result_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_result_faculty           | Quiz / User    | `R/W/C`   |
| access_op_quiz_result_portal            | Role / Portal  | `R`       |

**Record Rules:**

- **Quiz result multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

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

### 🗃️ `op.override.mark` — Override Mark Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field            | Label           | Type       | Req | Store | Relation  |
| ---------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`    | Created on      | `datetime` |     | ✅    |           |
| `create_uid`     | Created by      | `many2one` |     | ✅    | res.users |
| `display_name`   | Display Name    | `char`     |     |       |           |
| `id`             | ID              | `integer`  |     | ✅    |           |
| `override`       | Override        | `boolean`  |     | ✅    |           |
| `override_marks` | Override Marks  | `float`    |     | ✅    |           |
| `write_date`     | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`      | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                    | Group          | Perms     |
| ----------------------- | -------------- | --------- |
| access_op_override_mark | Quiz / Manager | `R/W/C/D` |

### 🗃️ `op.quiz.line` — Questions

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                       | Label                          | Type        | Req | Store | Relation                        |
| --------------------------- | ------------------------------ | ----------- | --- | ----- | ------------------------------- |
| `answer`                    | Answer                         | `char`      |     | ✅    |                                 |
| `case_sensitive`            | Case Sensitive                 | `boolean`   |     | ✅    |                                 |
| `company_id`                | Company                        | `many2one`  |     | ✅    | res.company                     |
| `create_date`               | Created on                     | `datetime`  |     | ✅    |                                 |
| `create_uid`                | Created by                     | `many2one`  |     | ✅    | res.users                       |
| `datas`                     | Content                        | `binary`    |     | ✅    |                                 |
| `display_name`              | Display Name                   | `char`      |     |       |                                 |
| `display_type`              | Display Type                   | `selection` |     | ✅    |                                 |
| `document_id`               | Document ID                    | `char`      |     | ✅    |                                 |
| `embed_code`                | Embed Code                     | `text`      |     |       |                                 |
| `following_images_line_ids` | Follwing Images Answers        | `one2many`  |     | ✅    | op.quiz.answer.following.images |
| `following_line_ids`        | Following Answers              | `one2many`  |     | ✅    | op.quiz.answer.following        |
| `grade_false_id`            | Grade for wrongly given answer | `many2one`  |     | ✅    | op.answer.grade                 |
| `grade_true_id`             | Grade for truly given answer   | `many2one`  |     | ✅    | op.answer.grade                 |
| `id`                        | ID                             | `integer`   |     | ✅    |                                 |
| `line_ids`                  | Answers                        | `one2many`  |     | ✅    | op.quiz.answer                  |
| `mark`                      | Marks                          | `float`     |     | ✅    |                                 |
| `material_type`             | Material Type                  | `selection` |     | ✅    |                                 |
| `multiple_choice_line_ids`  | Multiple Choice Answers        | `one2many`  |     | ✅    | op.quiz.answer.multiple.choice  |
| `multiple_choice_que_type`  | Multiple Choice Question Type  | `selection` |     | ✅    |                                 |
| `name`                      | Question                       | `char`      |     | ✅    |                                 |
| `numeric_answer`            | Numeric Answer                 | `float`     |     | ✅    |                                 |
| `que_id`                    | question                       | `many2one`  |     | ✅    | op.question.bank.line           |
| `que_type`                  | Question Type                  | `selection` |     | ✅    |                                 |
| `quiz_id`                   | Quiz                           | `many2one`  |     | ✅    | op.quiz                         |
| `reference_material`        | Reference Material             | `text`      |     | ✅    |                                 |
| `sequence`                  | Sequence                       | `integer`   |     | ✅    |                                 |
| `sort_paragraphs_line_ids`  | Sort the Paragraphs Answers    | `one2many`  |     | ✅    | op.quiz.answer.sort.paragraphs  |
| `url`                       | Document URL                   | `char`      |     | ✅    |                                 |
| `video_type`                | Video Type                     | `selection` |     | ✅    |                                 |
| `write_date`                | Last Updated on                | `datetime`  |     | ✅    |                                 |
| `write_uid`                 | Last Updated by                | `many2one`  |     | ✅    | res.users                       |

**Access Rights:**

| Name                                  | Group          | Perms     |
| ------------------------------------- | -------------- | --------- |
| access_op_quiz_line_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_line_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_quiz_line_portal            | Role / Portal  | `R`       |

**Record Rules:**

- **Quiz line multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.answer.grade` — Quiz Answer Grades

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `active`       | Active          | `boolean`  |     | ✅    |             |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Name            | `char`     |     | ✅    |             |
| `value`        | Grade (%)       | `float`    |     | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                                     | Group          | Perms     |
| ---------------------------------------- | -------------- | --------- |
| access_op_answer_grade_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_answer_grade_faculty           | Quiz / User    | `R`       |
| access_op_answer_grade_portal            | Role / Portal  | `R`       |

**Record Rules:**

- **Answer grade multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.quiz.answer` — Quiz Answers

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation        |
| -------------- | --------------- | ---------- | --- | ----- | --------------- |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company     |
| `create_date`  | Created on      | `datetime` |     | ✅    |                 |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users       |
| `display_name` | Display Name    | `char`     |     |       |                 |
| `grade_id`     | Grade           | `many2one` | ✅  | ✅    | op.answer.grade |
| `id`           | ID              | `integer`  |     | ✅    |                 |
| `line_id`      | Questions       | `many2one` |     | ✅    | op.quiz.line    |
| `name`         | Answer          | `char`     | ✅  | ✅    |                 |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                 |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                                    | Group          | Perms     |
| --------------------------------------- | -------------- | --------- |
| access_op_quiz_answer_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_answer_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_quiz_answer_portal            | Role / Portal  | `R`       |

**Record Rules:**

- **Quiz answer multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.quiz.answer.following` — Quiz Answers match the following

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label           | Type       | Req | Store | Relation        |
| ------------------- | --------------- | ---------- | --- | ----- | --------------- |
| `answer`            | Answer          | `char`     | ✅  | ✅    |                 |
| `company_id`        | Company         | `many2one` |     | ✅    | res.company     |
| `create_date`       | Created on      | `datetime` |     | ✅    |                 |
| `create_uid`        | Created by      | `many2one` |     | ✅    | res.users       |
| `default_answer`    | default Answer  | `char`     |     | ✅    |                 |
| `display_name`      | Display Name    | `char`     |     |       |                 |
| `following_line_id` | question        | `many2one` |     | ✅    | op.quiz.line    |
| `grade_id`          | Grade           | `many2one` |     | ✅    | op.answer.grade |
| `id`                | ID              | `integer`  |     | ✅    |                 |
| `image`             | Image           | `binary`   |     | ✅    |                 |
| `question`          | Question        | `char`     |     | ✅    |                 |
| `write_date`        | Last Updated on | `datetime` |     | ✅    |                 |
| `write_uid`         | Last Updated by | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                                              | Group          | Perms     |
| ------------------------------------------------- | -------------- | --------- |
| access_op_quiz_answer_following_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_answer_following_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_quiz_answer_following_public            | Role / Portal  | `R`       |

### 🗃️ `op.question.bank.answer.following` — Quiz Answers match the following

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label           | Type       | Req | Store | Relation              |
| ------------------- | --------------- | ---------- | --- | ----- | --------------------- |
| `answer`            | Answer          | `char`     |     | ✅    |                       |
| `company_id`        | Company         | `many2one` |     | ✅    | res.company           |
| `create_date`       | Created on      | `datetime` |     | ✅    |                       |
| `create_uid`        | Created by      | `many2one` |     | ✅    | res.users             |
| `display_name`      | Display Name    | `char`     |     |       |                       |
| `following_line_id` | question        | `many2one` |     | ✅    | op.question.bank.line |
| `id`                | ID              | `integer`  |     | ✅    |                       |
| `image`             | Image           | `binary`   |     | ✅    |                       |
| `question`          | Question        | `char`     |     | ✅    |                       |
| `write_date`        | Last Updated on | `datetime` |     | ✅    |                       |
| `write_uid`         | Last Updated by | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                                                       | Group          | Perms     |
| ---------------------------------------------------------- | -------------- | --------- |
| access_op_question_bank_answer_following_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_question_bank_answer_following_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_question_bank_answer_following_public            | Role / Portal  | `R`       |

### 🗃️ `op.question.bank.answer.following.images` — Quiz Answers match the following images

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label           | Type       | Req | Store | Relation              |
| -------------------------- | --------------- | ---------- | --- | ----- | --------------------- |
| `company_id`               | Company         | `many2one` |     | ✅    | res.company           |
| `create_date`              | Created on      | `datetime` |     | ✅    |                       |
| `create_uid`               | Created by      | `many2one` |     | ✅    | res.users             |
| `default_answer`           | Default Answer  | `binary`   | ✅  | ✅    |                       |
| `display_name`             | Display Name    | `char`     |     |       |                       |
| `following_images_line_id` | question        | `many2one` |     | ✅    | op.question.bank.line |
| `given_answer`             | Given Answer    | `binary`   |     | ✅    |                       |
| `id`                       | ID              | `integer`  |     | ✅    |                       |
| `image`                    | Question        | `binary`   | ✅  | ✅    |                       |
| `write_date`               | Last Updated on | `datetime` |     | ✅    |                       |
| `write_uid`                | Last Updated by | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                                                              | Group          | Perms     |
| ----------------------------------------------------------------- | -------------- | --------- |
| access_op_question_bank_answer_following_images_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_question_bank_answer_following_images_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_question_bank_answer_following_images_public            | Role / Portal  | `R`       |

### 🗃️ `op.quiz.answer.following.images` — Quiz Answers match the following images

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label           | Type       | Req | Store | Relation        |
| -------------------------- | --------------- | ---------- | --- | ----- | --------------- |
| `company_id`               | Company         | `many2one` |     | ✅    | res.company     |
| `create_date`              | Created on      | `datetime` |     | ✅    |                 |
| `create_uid`               | Created by      | `many2one` |     | ✅    | res.users       |
| `default_answer`           | Default Answer  | `binary`   | ✅  | ✅    |                 |
| `display_name`             | Display Name    | `char`     |     |       |                 |
| `following_images_line_id` | question        | `many2one` |     | ✅    | op.quiz.line    |
| `given_answer`             | Given Answer    | `binary`   |     | ✅    |                 |
| `grade_id`                 | Grade           | `many2one` |     | ✅    | op.answer.grade |
| `id`                       | ID              | `integer`  |     | ✅    |                 |
| `image`                    | Images          | `binary`   | ✅  | ✅    |                 |
| `write_date`               | Last Updated on | `datetime` |     | ✅    |                 |
| `write_uid`                | Last Updated by | `many2one` |     | ✅    | res.users       |

**Access Rights:**

| Name                                                     | Group          | Perms     |
| -------------------------------------------------------- | -------------- | --------- |
| access_op_quiz_answer_following_images_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_answer_following_images_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_quiz_answer_following_images_public            | Role / Portal  | `R`       |

### 🗃️ `op.quiz.answer.multiple.choice` — Quiz Answers multiple choice

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label            | Type       | Req | Store | Relation     |
| ------------------------- | ---------------- | ---------- | --- | ----- | ------------ |
| `company_id`              | Company          | `many2one` |     | ✅    | res.company  |
| `create_date`             | Created on       | `datetime` |     | ✅    |              |
| `create_uid`              | Created by       | `many2one` |     | ✅    | res.users    |
| `default_answer`          | Grade            | `boolean`  |     | ✅    |              |
| `display_name`            | Display Name     | `char`     |     |       |              |
| `id`                      | ID               | `integer`  |     | ✅    |              |
| `multiple_choice_line_id` | question         | `many2one` |     | ✅    | op.quiz.line |
| `que_given_answer`        | Default Answer   | `binary`   |     | ✅    |              |
| `que_image`               | Image Answer     | `binary`   |     | ✅    |              |
| `que_text`                | Text Answer      | `char`     |     | ✅    |              |
| `que_text_answer`         | Quiz Text Answer | `char`     |     | ✅    |              |
| `write_date`              | Last Updated on  | `datetime` |     | ✅    |              |
| `write_uid`               | Last Updated by  | `many2one` |     | ✅    | res.users    |

**Access Rights:**

| Name                                                    | Group          | Perms     |
| ------------------------------------------------------- | -------------- | --------- |
| access_op_quiz_answer_multiple_choice_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_answer_multiple_choice_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_quiz_answer_multiple_choice_public            | Role / Portal  | `R`       |

### 🗃️ `op.quiz.answer.sort.paragraphs` — Quiz Answers sort paragraphs

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label           | Type       | Req | Store | Relation     |
| ------------------------- | --------------- | ---------- | --- | ----- | ------------ |
| `answer`                  | Answer          | `char`     |     | ✅    |              |
| `company_id`              | Company         | `many2one` |     | ✅    | res.company  |
| `create_date`             | Created on      | `datetime` |     | ✅    |              |
| `create_uid`              | Created by      | `many2one` |     | ✅    | res.users    |
| `display_name`            | Display Name    | `char`     |     |       |              |
| `id`                      | ID              | `integer`  |     | ✅    |              |
| `question`                | Correct Answers | `char`     |     | ✅    |              |
| `sort_paragraphs_line_id` | question Line   | `many2one` |     | ✅    | op.quiz.line |
| `write_date`              | Last Updated on | `datetime` |     | ✅    |              |
| `write_uid`               | Last Updated by | `many2one` |     | ✅    | res.users    |

**Access Rights:**

| Name                                                    | Group          | Perms     |
| ------------------------------------------------------- | -------------- | --------- |
| access_op_quiz_answer_sort_paragraphs_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_answer_sort_paragraphs_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_quiz_answer_sort_paragraphs_public            | Role / Portal  | `R`       |

### 🗃️ `op.quiz.category` — Quiz Category

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `active`       | Active          | `boolean`  |     | ✅    |             |
| `code`         | Code            | `char`     |     | ✅    |             |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `description`  | Description     | `text`     |     | ✅    |             |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Name            | `char`     |     | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                                      | Group          | Perms     |
| ----------------------------------------- | -------------- | --------- |
| access_op_quiz_category_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_category_faculty           | Quiz / User    | `R`       |
| access_op_quiz_category_portal            | Role / Portal  | `R`       |

**Record Rules:**

- **Quiz Category multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.quiz.config` — Quiz Configuration

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label              | Type       | Req | Store | Relation         |
| ---------------- | ------------------ | ---------- | --- | ----- | ---------------- |
| `bank_id`        | Question Bank      | `many2one` |     | ✅    | op.question.bank |
| `company_id`     | Company            | `many2one` |     | ✅    | res.company      |
| `create_date`    | Created on         | `datetime` |     | ✅    |                  |
| `create_uid`     | Created by         | `many2one` |     | ✅    | res.users        |
| `display_name`   | Display Name       | `char`     |     |       |                  |
| `id`             | ID                 | `integer`  |     | ✅    |                  |
| `no_of_question` | Number of Question | `integer`  |     | ✅    |                  |
| `quiz_id`        | Quiz               | `many2one` |     | ✅    | op.quiz          |
| `write_date`     | Last Updated on    | `datetime` |     | ✅    |                  |
| `write_uid`      | Last Updated by    | `many2one` |     | ✅    | res.users        |

**Access Rights:**

| Name                                    | Group          | Perms     |
| --------------------------------------- | -------------- | --------- |
| access_op_quiz_config_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_config_faculty           | Quiz / User    | `R/W/C`   |
| access_op_quiz_config_portal            | Role / Portal  | `R`       |

**Record Rules:**

- **Quiz config multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.quiz.result.line.multiple.choice` — quiz multiple choice result

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label           | Type        | Req | Store | Relation            |
| ------------------------- | --------------- | ----------- | --- | ----- | ------------------- |
| `company_id`              | Company         | `many2one`  |     | ✅    | res.company         |
| `create_date`             | Created on      | `datetime`  |     | ✅    |                     |
| `create_uid`              | Created by      | `many2one`  |     | ✅    | res.users           |
| `default_answer`          | Default Answer  | `boolean`   |     | ✅    |                     |
| `display_name`            | Display Name    | `char`      |     |       |                     |
| `given_answer`            | Given Answer    | `boolean`   |     | ✅    |                     |
| `id`                      | ID              | `integer`   |     | ✅    |                     |
| `multiple_choice_line_id` | Question line   | `many2one`  |     | ✅    | op.quiz.result.line |
| `que_image`               | Image           | `binary`    |     | ✅    |                     |
| `que_text`                | Text Question   | `char`      |     | ✅    |                     |
| `que_type`                | Question Type   | `selection` |     | ✅    |                     |
| `write_date`              | Last Updated on | `datetime`  |     | ✅    |                     |
| `write_uid`               | Last Updated by | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                                                         | Group          | Perms     |
| ------------------------------------------------------------ | -------------- | --------- |
| access_op_quiz_result_line_multiple_choice_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_result_line_multiple_choice_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_quiz_result_line_multiple_choice_public            | Role / Portal  | `R`       |

### 🗃️ `op.question.bank` — Quiz Question Bank

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation              |
| -------------- | --------------- | ---------- | --- | ----- | --------------------- |
| `active`       | Active          | `boolean`  |     | ✅    |                       |
| `bank_type_id` | Type            | `many2one` |     | ✅    | op.question.bank.type |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company           |
| `create_date`  | Created on      | `datetime` |     | ✅    |                       |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users             |
| `description`  | Description     | `text`     |     | ✅    |                       |
| `display_name` | Display Name    | `char`     |     |       |                       |
| `id`           | ID              | `integer`  |     | ✅    |                       |
| `line_ids`     | Questions       | `one2many` |     | ✅    | op.question.bank.line |
| `name`         | Name            | `char`     |     | ✅    |                       |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                       |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                                      | Group          | Perms     |
| ----------------------------------------- | -------------- | --------- |
| access_op_question_bank_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_question_bank_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_question_bank_portal            | Role / Portal  | `R`       |

**Record Rules:**

- **Question bank multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.question.bank.answer` — Quiz Question Bank Answers

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation              |
| -------------- | --------------- | ---------- | --- | ----- | --------------------- |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company           |
| `create_date`  | Created on      | `datetime` |     | ✅    |                       |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users             |
| `display_name` | Display Name    | `char`     |     |       |                       |
| `grade_id`     | Grade           | `many2one` |     | ✅    | op.answer.grade       |
| `id`           | ID              | `integer`  |     | ✅    |                       |
| `name`         | Answer          | `char`     | ✅  | ✅    |                       |
| `question_id`  | Question        | `many2one` |     | ✅    | op.question.bank.line |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                       |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                                             | Group          | Perms     |
| ------------------------------------------------ | -------------- | --------- |
| access_op_question_bank_answer_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_question_bank_answer_faculty           | Quiz / User    | `R/W/C/D` |

**Record Rules:**

- **Question bank answer multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.question.bank.answer.sort.paragraphs` — Quiz Question Bank Answers multiple choice

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label           | Type       | Req | Store | Relation              |
| ------------------------- | --------------- | ---------- | --- | ----- | --------------------- |
| `answer`                  | Answer          | `char`     |     | ✅    |                       |
| `company_id`              | Company         | `many2one` |     | ✅    | res.company           |
| `create_date`             | Created on      | `datetime` |     | ✅    |                       |
| `create_uid`              | Created by      | `many2one` |     | ✅    | res.users             |
| `display_name`            | Display Name    | `char`     |     |       |                       |
| `id`                      | ID              | `integer`  |     | ✅    |                       |
| `question`                | Correct Answers | `char`     |     | ✅    |                       |
| `sort_paragraphs_line_id` | question Line   | `many2one` |     | ✅    | op.question.bank.line |
| `write_date`              | Last Updated on | `datetime` |     | ✅    |                       |
| `write_uid`               | Last Updated by | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                                                                | Group          | Perms     |
| ------------------------------------------------------------------- | -------------- | --------- |
| access_op_op_question_bank_answer_sort_paragraphs_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_op_question_bank_answer_sort_paragraphs_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_op_question_bank_answer_sort_paragraphs_public            | Role / Portal  | `R`       |

### 🗃️ `op.question.bank.answer.multiple.choice` — Quiz Question Bank Answers multiple choice

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                     | Label           | Type        | Req | Store | Relation              |
| ------------------------- | --------------- | ----------- | --- | ----- | --------------------- |
| `company_id`              | Company         | `many2one`  |     | ✅    | res.company           |
| `create_date`             | Created on      | `datetime`  |     | ✅    |                       |
| `create_uid`              | Created by      | `many2one`  |     | ✅    | res.users             |
| `default_answer`          | Grade           | `boolean`   |     | ✅    |                       |
| `display_name`            | Display Name    | `char`      |     |       |                       |
| `given_answer`            | Given Answer    | `boolean`   |     | ✅    |                       |
| `id`                      | ID              | `integer`   |     | ✅    |                       |
| `multiple_choice_line_id` | Question line   | `many2one`  |     | ✅    | op.question.bank.line |
| `que_image`               | Image           | `binary`    |     | ✅    |                       |
| `que_text`                | Text Answers    | `char`      |     | ✅    |                       |
| `que_type`                | Question Type   | `selection` |     | ✅    |                       |
| `write_date`              | Last Updated on | `datetime`  |     | ✅    |                       |
| `write_uid`               | Last Updated by | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                                                             | Group          | Perms     |
| ---------------------------------------------------------------- | -------------- | --------- |
| access_op_question_bank_answer_multiple_choice_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_question_bank_answer_multiple_choice_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_question_bank_answer_multiple_choice_public            | Role / Portal  | `R`       |

### 🗃️ `op.question.bank.type` — Quiz Question Bank Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation    |
| -------------- | --------------- | ---------- | --- | ----- | ----------- |
| `active`       | Active          | `boolean`  |     | ✅    |             |
| `company_id`   | Company         | `many2one` |     | ✅    | res.company |
| `create_date`  | Created on      | `datetime` |     | ✅    |             |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users   |
| `description`  | Description     | `text`     |     | ✅    |             |
| `display_name` | Display Name    | `char`     |     |       |             |
| `id`           | ID              | `integer`  |     | ✅    |             |
| `name`         | Name            | `char`     |     | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                                           | Group          | Perms     |
| ---------------------------------------------- | -------------- | --------- |
| access_op_question_bank_type_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_question_bank_type_faculty           | Quiz / User    | `R`       |
| access_op_question_bank_type_portal            | Role / Portal  | `R`       |

**Record Rules:**

- **Question bank type multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.question.bank.line` — Quiz Question Lines

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                       | Label                          | Type        | Req | Store | Relation                                 |
| --------------------------- | ------------------------------ | ----------- | --- | ----- | ---------------------------------------- |
| `answer`                    | Answer                         | `char`      |     | ✅    |                                          |
| `bank_id`                   | Question Bank                  | `many2one`  |     | ✅    | op.question.bank                         |
| `case_sensitive`            | Case Sensitive                 | `boolean`   |     | ✅    |                                          |
| `company_id`                | Company                        | `many2one`  |     | ✅    | res.company                              |
| `create_date`               | Created on                     | `datetime`  |     | ✅    |                                          |
| `create_uid`                | Created by                     | `many2one`  |     | ✅    | res.users                                |
| `datas`                     | Content                        | `binary`    |     | ✅    |                                          |
| `display_name`              | Display Name                   | `char`      |     |       |                                          |
| `document_id`               | Document ID                    | `char`      |     | ✅    |                                          |
| `following_images_line_ids` | Following Images Answers       | `one2many`  |     | ✅    | op.question.bank.answer.following.images |
| `following_line_ids`        | Following Answers              | `one2many`  |     | ✅    | op.question.bank.answer.following        |
| `grade_false_id`            | Grade for wrongly given answer | `many2one`  |     | ✅    | op.answer.grade                          |
| `grade_true_id`             | Grade for truly given answer   | `many2one`  |     | ✅    | op.answer.grade                          |
| `id`                        | ID                             | `integer`   |     | ✅    |                                          |
| `line_ids`                  | Answers                        | `one2many`  |     | ✅    | op.question.bank.answer                  |
| `mark`                      | Marks                          | `float`     |     | ✅    |                                          |
| `material_type`             | Material Type                  | `selection` |     | ✅    |                                          |
| `multiple_choice_line_ids`  | Multiple Choice Answers        | `one2many`  |     | ✅    | op.question.bank.answer.multiple.choice  |
| `multiple_choice_que_type`  | Multiple Choice Question Type  | `selection` |     | ✅    |                                          |
| `name`                      | Question                       | `char`      |     | ✅    |                                          |
| `numeric_answer`            | Numeric Answer                 | `float`     |     | ✅    |                                          |
| `que_type`                  | Question Type                  | `selection` |     | ✅    |                                          |
| `sort_paragraphs_line_ids`  | Sort the Paragraphs Answers    | `one2many`  |     | ✅    | op.question.bank.answer.sort.paragraphs  |
| `url`                       | Document URL                   | `char`      |     | ✅    |                                          |
| `video_type`                | Video Type                     | `selection` |     | ✅    |                                          |
| `write_date`                | Last Updated on                | `datetime`  |     | ✅    |                                          |
| `write_uid`                 | Last Updated by                | `many2one`  |     | ✅    | res.users                                |

**Access Rights:**

| Name                                           | Group          | Perms     |
| ---------------------------------------------- | -------------- | --------- |
| access_op_question_bank_line_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_question_bank_line_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_question_bank_line_portal            | Role / Portal  | `R`       |

**Record Rules:**

- **Question bank line multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.question.wizard` — Quiz Question Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation              |
| -------------- | --------------- | ----------- | --- | ----- | --------------------- |
| `bank_id`      | Question Bank   | `many2one`  |     | ✅    | op.question.bank      |
| `create_date`  | Created on      | `datetime`  |     | ✅    |                       |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users             |
| `display_name` | Display Name    | `char`      |     |       |                       |
| `id`           | ID              | `integer`   |     | ✅    |                       |
| `question_ids` | Questions       | `many2many` |     | ✅    | op.question.bank.line |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |                       |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                              | Group          | Perms     |
| --------------------------------- | -------------- | --------- |
| access_op_question_wizard         | Quiz / Manager | `R/W/C/D` |
| access_op_question_wizard_faculty | Quiz / User    | `R/W/C`   |

### 🗃️ `op.quiz.result.line` — Quiz Result Line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                       | Label                          | Type        | Req | Store | Relation                             |
| --------------------------- | ------------------------------ | ----------- | --- | ----- | ------------------------------------ |
| `answer`                    | Correct Answer                 | `text`      |     | ✅    |                                      |
| `bank_line`                 | Question Reference             | `many2one`  |     | ✅    | op.quiz.line                         |
| `case_sensitive`            | Case Sensitive                 | `boolean`   |     | ✅    |                                      |
| `company_id`                | Company                        | `many2one`  |     | ✅    | res.company                          |
| `create_date`               | Created on                     | `datetime`  |     | ✅    |                                      |
| `create_uid`                | Created by                     | `many2one`  |     | ✅    | res.users                            |
| `display_name`              | Display Name                   | `char`      |     |       |                                      |
| `display_type`              | Display Type                   | `selection` |     | ✅    |                                      |
| `following_images_line_ids` | Following Images               | `one2many`  |     | ✅    | op.quiz.result.line.following.images |
| `following_line_ids`        | Following Answer               | `one2many`  |     | ✅    | op.quiz.result.line.answers          |
| `given_answer`              | User Answer                    | `text`      |     | ✅    |                                      |
| `grade_false_id`            | Grade for wrongly given answer | `many2one`  |     | ✅    | op.answer.grade                      |
| `grade_true_id`             | Grade for truly given answer   | `many2one`  |     | ✅    | op.answer.grade                      |
| `id`                        | ID                             | `integer`   |     | ✅    |                                      |
| `line_ids`                  | Answers                        | `one2many`  |     | ✅    | op.quiz.result.line.answers          |
| `mark`                      | Received Marks                 | `float`     |     | ✅    |                                      |
| `multiple_choice_line_ids`  | Multiple Choice                | `one2many`  |     | ✅    | op.quiz.result.line.multiple.choice  |
| `multiple_choice_que_type`  | multiple choice Question Type  | `selection` |     | ✅    |                                      |
| `name`                      | Question                       | `text`      |     | ✅    |                                      |
| `question_mark`             | Actual Marks                   | `float`     |     | ✅    |                                      |
| `que_type`                  | Question Type                  | `selection` |     | ✅    |                                      |
| `reference_material`        | Answer Reference Material      | `text`      |     | ✅    |                                      |
| `result_id`                 | Result                         | `many2one`  |     | ✅    | op.quiz.result                       |
| `sequence`                  | Sequence                       | `integer`   |     | ✅    |                                      |
| `sort_paragraphs_line_ids`  | Sort Paragraphs Answer         | `one2many`  |     | ✅    | op.quiz.result.line.sort.paragraphs  |
| `write_date`                | Last Updated on                | `datetime`  |     | ✅    |                                      |
| `write_uid`                 | Last Updated by                | `many2one`  |     | ✅    | res.users                            |

**Access Rights:**

| Name                                         | Group          | Perms     |
| -------------------------------------------- | -------------- | --------- |
| access_op_quiz_result_line_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_result_line_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_quiz_result_line_portal            | Role / Portal  | `R`       |

**Record Rules:**

- **Quiz result line multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.quiz.result.line.answers` — Quiz Result Line Answer

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label           | Type       | Req | Store | Relation            |
| ---------------- | --------------- | ---------- | --- | ----- | ------------------- |
| `company_id`     | Company         | `many2one` |     | ✅    | res.company         |
| `create_date`    | Created on      | `datetime` |     | ✅    |                     |
| `create_uid`     | Created by      | `many2one` |     | ✅    | res.users           |
| `default_answer` | Default Answer  | `char`     |     | ✅    |                     |
| `display_name`   | Display Name    | `char`     |     |       |                     |
| `grade_id`       | Grade           | `many2one` |     | ✅    | op.answer.grade     |
| `id`             | ID              | `integer`  |     | ✅    |                     |
| `image`          | Image           | `binary`   |     | ✅    |                     |
| `line_id`        | Questions       | `many2one` |     | ✅    | op.quiz.result.line |
| `name`           | Given Answer    | `char`     | ✅  | ✅    |                     |
| `question`       | Question        | `char`     |     | ✅    |                     |
| `write_date`     | Last Updated on | `datetime` |     | ✅    |                     |
| `write_uid`      | Last Updated by | `many2one` |     | ✅    | res.users           |

**Access Rights:**

| Name                                                 | Group          | Perms     |
| ---------------------------------------------------- | -------------- | --------- |
| access_op_quiz_result_line_answers_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_result_line_answers_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_quiz_result_line_answers_portal            | Role / Portal  | `R`       |

**Record Rules:**

- **Quiz result line answers multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.quiz.result.line.following.images` — Quiz Result Line Following Images

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label           | Type       | Req | Store | Relation            |
| -------------------------- | --------------- | ---------- | --- | ----- | ------------------- |
| `company_id`               | Company         | `many2one` |     | ✅    | res.company         |
| `create_date`              | Created on      | `datetime` |     | ✅    |                     |
| `create_uid`               | Created by      | `many2one` |     | ✅    | res.users           |
| `default_answer`           | Default Answer  | `binary`   |     | ✅    |                     |
| `display_name`             | Display Name    | `char`     |     |       |                     |
| `following_images_line_id` | Question line   | `many2one` |     | ✅    | op.quiz.result.line |
| `given_answer`             | Given Answer    | `binary`   |     | ✅    |                     |
| `grade_id`                 | Grade           | `many2one` |     | ✅    | op.answer.grade     |
| `id`                       | ID              | `integer`  |     | ✅    |                     |
| `image`                    | Image           | `binary`   |     | ✅    |                     |
| `write_date`               | Last Updated on | `datetime` |     | ✅    |                     |
| `write_uid`                | Last Updated by | `many2one` |     | ✅    | res.users           |

**Access Rights:**

| Name                                                          | Group          | Perms     |
| ------------------------------------------------------------- | -------------- | --------- |
| access_op_quiz_result_line_following_images_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_result_line_following_images_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_quiz_result_line_following_images_public            | Role / Portal  | `R`       |

### 🗃️ `op.quiz.result.message` — Quiz Result Message

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
| `message`      | Message         | `html`     |     | ✅    |             |
| `quiz_id`      | Quiz            | `many2one` |     | ✅    | op.quiz     |
| `result_from`  | Result From (%) | `float`    |     | ✅    |             |
| `result_to`    | Result To (%)   | `float`    |     | ✅    |             |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users   |

**Access Rights:**

| Name                                            | Group          | Perms     |
| ----------------------------------------------- | -------------- | --------- |
| access_op_quiz_result_message_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_result_message_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_quiz_result_message_portal            | Role / Portal  | `R`       |

**Record Rules:**

- **Quiz result message multi-company** (1) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `op.quiz.result.line.sort.paragraphs` — Quiz result sort paragraphs

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label           | Type       | Req | Store | Relation            |
| ---------------- | --------------- | ---------- | --- | ----- | ------------------- |
| `create_date`    | Created on      | `datetime` |     | ✅    |                     |
| `create_uid`     | Created by      | `many2one` |     | ✅    | res.users           |
| `default_answer` | Default Answer  | `char`     |     | ✅    |                     |
| `display_name`   | Display Name    | `char`     |     |       |                     |
| `given_answer`   | Given Answer    | `char`     |     | ✅    |                     |
| `id`             | ID              | `integer`  |     | ✅    |                     |
| `line_id`        | Questions       | `many2one` |     | ✅    | op.quiz.result.line |
| `write_date`     | Last Updated on | `datetime` |     | ✅    |                     |
| `write_uid`      | Last Updated by | `many2one` |     | ✅    | res.users           |

**Access Rights:**

| Name                                                         | Group          | Perms     |
| ------------------------------------------------------------ | -------------- | --------- |
| access_op_quiz_result_line_sort_paragraphs_back_office_admin | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_result_line_sort_paragraphs_faculty           | Quiz / User    | `R/W/C/D` |
| access_op_quiz_result_line_sort_paragraphs_public            | Role / Portal  | `R`       |

### 🗃️ `op.update.mark` — Update Mark Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation  |
| -------------- | --------------- | ---------- | --- | ----- | --------- |
| `answer`       | Given Answer    | `text`     |     | ✅    |           |
| `create_date`  | Created on      | `datetime` |     | ✅    |           |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users |
| `display_name` | Display Name    | `char`     |     |       |           |
| `id`           | ID              | `integer`  |     | ✅    |           |
| `mark`         | Received Marks  | `float`    |     | ✅    |           |
| `name`         | Question        | `text`     |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                  | Group          | Perms     |
| --------------------- | -------------- | --------- |
| access_op_update_mark | Quiz / Manager | `R/W/C/D` |

### 🗃️ `ir.ui.view` — View

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                             | Type        | Req | Store | Relation                |
| ----------------------------- | --------------------------------- | ----------- | --- | ----- | ----------------------- |
| `active`                      | Active                            | `boolean`   |     | ✅    |                         |
| `arch`                        | View Architecture                 | `text`      |     |       |                         |
| `arch_base`                   | Base View Architecture            | `text`      |     |       |                         |
| `arch_db`                     | Arch Blob                         | `text`      |     | ✅    |                         |
| `arch_fs`                     | Arch Filename                     | `char`      |     | ✅    |                         |
| `arch_prev`                   | Previous View Architecture        | `text`      |     | ✅    |                         |
| `arch_updated`                | Modified Architecture             | `boolean`   |     | ✅    |                         |
| `controller_page_ids`         | Controller Page                   | `one2many`  |     | ✅    | website.controller.page |
| `create_date`                 | Created on                        | `datetime`  |     | ✅    |                         |
| `create_uid`                  | Created by                        | `many2one`  |     | ✅    | res.users               |
| `customize_show`              | Show As Optional Inherit          | `boolean`   |     | ✅    |                         |
| `display_name`                | Display Name                      | `char`      |     |       |                         |
| `first_page_id`               | Website Page                      | `many2one`  |     |       | website.page            |
| `group_ids`                   | Groups                            | `many2many` |     | ✅    | res.groups              |
| `id`                          | ID                                | `integer`   |     | ✅    |                         |
| `inherit_children_ids`        | Views which inherit from this one | `one2many`  |     | ✅    | ir.ui.view              |
| `inherit_id`                  | Inherited View                    | `many2one`  |     | ✅    | ir.ui.view              |
| `invalid_locators`            | Invalid Locators                  | `json`      |     |       |                         |
| `is_seo_optimized`            | SEO optimized                     | `boolean`   |     | ✅    |                         |
| `key`                         | Key                               | `char`      |     | ✅    |                         |
| `mode`                        | View inheritance mode             | `selection` | ✅  | ✅    |                         |
| `model`                       | Model                             | `char`      |     | ✅    |                         |
| `model_data_id`               | Model Data                        | `many2one`  |     |       | ir.model.data           |
| `model_id`                    | Model of the view                 | `many2one`  |     |       | ir.model                |
| `name`                        | View Name                         | `char`      | ✅  | ✅    |                         |
| `page_ids`                    | Page                              | `one2many`  |     | ✅    | website.page            |
| `priority`                    | Sequence                          | `integer`   | ✅  | ✅    |                         |
| `seo_name`                    | Seo name                          | `char`      |     | ✅    |                         |
| `theme_template_id`           | Theme Template                    | `many2one`  |     | ✅    | theme.ir.ui.view        |
| `track`                       | Track                             | `boolean`   |     | ✅    |                         |
| `type`                        | View Type                         | `selection` |     | ✅    |                         |
| `visibility`                  | Visibility                        | `selection` |     | ✅    |                         |
| `visibility_password`         | Visibility Password               | `char`      |     | ✅    |                         |
| `visibility_password_display` | Visibility Password Display       | `char`      |     |       |                         |
| `warning_info`                | Warning information               | `html`      |     |       |                         |
| `website_id`                  | Website                           | `many2one`  |     | ✅    | website                 |
| `website_meta_description`    | Website meta description          | `text`      |     | ✅    |                         |
| `website_meta_keywords`       | Website meta keywords             | `char`      |     | ✅    |                         |
| `website_meta_og_img`         | Website opengraph image           | `char`      |     | ✅    |                         |
| `website_meta_title`          | Website meta title                | `char`      |     | ✅    |                         |
| `write_date`                  | Last Updated on                   | `datetime`  |     | ✅    |                         |
| `write_uid`                   | Last Updated by                   | `many2one`  |     | ✅    | res.users               |
| `xml_id`                      | External ID                       | `char`      |     |       |                         |

**Access Rights:**

| Name                                        | Group                         | Perms     |
| ------------------------------------------- | ----------------------------- | --------- |
| access_website_ir_ui_view_restricted_editor | Website / Restricted Editor   | `R`       |
| access_website_ir_ui_view_designer          | Website / Editor and Designer | `R/W/C/D` |
| ir_ui_view group_system                     | Role / Administrator          | `R/W/C/D` |
| ir_ui_view group_user                       | Everyone                      | `-`       |

**Record Rules:**

- **website_designer: Manage Website and qWeb view** (72) `R/W/C/D`
  - Domain: `[('type', '=', 'qweb')]`
- **website_designer: global view** (72) `R`
  - Domain: `[('type', '!=', 'qweb')]`
- **Administration Settings: Manage all views** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Website View Visibility Public** (11) `R`
  - Domain: `['|', ('type', '!=', 'qweb'), ('visibility', 'in', ('public', False))]`
- **Website View Visibility Connected** (10) `R`
  - Domain:
    `['|', ('type', '!=', 'qweb'), ('visibility', 'in', ('public', 'connected', False))]`
