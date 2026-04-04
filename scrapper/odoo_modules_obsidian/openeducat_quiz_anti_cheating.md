---
title: "OpenEduCat Quiz Anti Cheating Management"
module: "openeducat_quiz_anti_cheating"
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

# 🟢 OpenEduCat Quiz Anti Cheating Management

> **Module:** `openeducat_quiz_anti_cheating` | **Version:** `19.0.1.0` **Category:**
> Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[openeducat_quiz]]

## 📖 Description

## OpenEduCat Quiz / Exam With Anti Cheating

### OpenEduCat Anti Cheating Module provides facility to conduct online exam platform with Anti Cheating Feature

[![](/openeducat_quiz_anti_cheating/static/description/openeducat__logo.png)](https://www.openeducat.org/demo)

Online Demo

Based on best of class enterprise level architecture, OpenEduCat is ready to be used
from local infrastructure to a highly scalable cloud environment.

[Contact Us](https://www.openeducat.org/contactus/)

## Quiz Anti Cheating Configuration

Faculty can configure Face Tracking with warning limit and warning state like In
Progress After warning, Permission from admin and Submit.

![](/openeducat_quiz_anti_cheating/static/description/face_track.png)

![](/openeducat_quiz_anti_cheating/static/description/copy_question.png)

Faculty can configure Cope/Paste Allow or not and set the Question Time out in minutes.

Faculty can configure Take Screenshot field with Random. Also set the range of time in
start and end minutes fields.

![](/openeducat_quiz_anti_cheating/static/description/random.png)

![](/openeducat_quiz_anti_cheating/static/description/interval.png)

Faculty can configure Take Screenshot field with Time Interval and set the interval time
in minutes.

## Exam Description

When user give the access of camera then face tracking is on otherwise not allow to give
the exam.

![](/openeducat_quiz_anti_cheating/static/description/description_page.png)

## Exam View

![](/openeducat_quiz_anti_cheating/static/description/exam_view.png)

User's face is tracked. While any cheating during the exam, display the warning message
with counting warning. After the warning limit is finished then automatically current
exam in hold state. For Re-open the exam, contact to administration.

## Results

Faculty can see warning number, time and image, for what's the reason warning is given
and also reopen the exam. In attachment screenshots are stored.

![](/openeducat_quiz_anti_cheating/static/description/warning_line.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `Quiz Anti Cheating`

### Views

- `* INHERIT op.quiz.anti.cheating.list (list)`
- `* INHERIT op.quiz.result.anti.cheating.list (list)`
- `* INHERIT op.quiz.result.form (form)`
- `* INHERIT quiz.test (form)`
- `Quiz Hold (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

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

### 🗃️ `op.quiz.result.warning` — Warning data

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label           | Type       | Req | Store | Relation       |
| -------------------- | --------------- | ---------- | --- | ----- | -------------- |
| `create_date`        | Created on      | `datetime` |     | ✅    |                |
| `create_uid`         | Created by      | `many2one` |     | ✅    | res.users      |
| `display_name`       | Display Name    | `char`     |     |       |                |
| `id`                 | ID              | `integer`  |     | ✅    |                |
| `result_id`          | Result          | `many2one` |     | ✅    | op.quiz.result |
| `time`               | Time            | `char`     |     | ✅    |                |
| `warning_attachment` | Attachment      | `binary`   |     | ✅    |                |
| `warning_name`       | Name            | `char`     |     | ✅    |                |
| `warning_no`         | Warning Number  | `integer`  |     | ✅    |                |
| `write_date`         | Last Updated on | `datetime` |     | ✅    |                |
| `write_uid`          | Last Updated by | `many2one` |     | ✅    | res.users      |

**Access Rights:**

| Name                                  | Group          | Perms     |
| ------------------------------------- | -------------- | --------- |
| access_op_quiz_result_warning_manager | Quiz / Manager | `R/W/C/D` |
| access_op_quiz_result_warning_user    | Quiz / User    | `R/W`     |
