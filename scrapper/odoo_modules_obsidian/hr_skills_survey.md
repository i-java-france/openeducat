---
title: "Skills Certification"
module: "hr_skills_survey"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Employees"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 Skills Certification

> **Module:** `hr_skills_survey` | **Version:** `19.0.1.0` **Category:** Employees |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[hr_skills]] [[survey]]

## 📖 Description

# Certification and Skills for HR

This module adds certification to resume for employees.

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT hr.resume.line.form (form)`
- `* INHERIT survey.survey.view.form.inherit.hr.skills (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

### 🗃️ `survey.survey` — Survey

> 📧 Mail Thread

Add the new 'Lead Qualification' survey template to the templates that can be selected
in the helper screen.

**Fields:**

| Field                             | Label                          | Type        | Req | Store | Relation           |
| --------------------------------- | ------------------------------ | ----------- | --- | ----- | ------------------ |
| `access_mode`                     | Access Mode                    | `selection` | ✅  | ✅    |                    |
| `access_token`                    | Access Token                   | `char`      |     | ✅    |                    |
| `active`                          | Active                         | `boolean`   |     | ✅    |                    |
| `activity_calendar_event_id`      | Next Activity Calendar Event   | `many2one`  |     |       | calendar.event     |
| `activity_date_deadline`          | Next Activity Deadline         | `date`      |     |       |                    |
| `activity_exception_decoration`   | Activity Exception Decoration  | `selection` |     |       |                    |
| `activity_exception_icon`         | Icon                           | `char`      |     |       |                    |
| `activity_ids`                    | Activities                     | `one2many`  |     | ✅    | mail.activity      |
| `activity_state`                  | Activity State                 | `selection` |     |       |                    |
| `activity_summary`                | Next Activity Summary          | `char`      |     |       |                    |
| `activity_type_icon`              | Activity Type Icon             | `char`      |     |       |                    |
| `activity_type_id`                | Next Activity Type             | `many2one`  |     |       | mail.activity.type |
| `activity_user_id`                | Responsible User               | `many2one`  |     |       | res.users          |
| `allowed_survey_types`            | Allowed survey types           | `json`      |     |       |                    |
| `answer_count`                    | Registered                     | `integer`   |     |       |                    |
| `answer_done_count`               | Attempts                       | `integer`   |     |       |                    |
| `answer_duration_avg`             | Average Duration               | `float`     |     |       |                    |
| `answer_score_avg`                | Avg Score (%)                  | `float`     |     |       |                    |
| `attempts_limit`                  | Number of attempts             | `integer`   |     | ✅    |                    |
| `background_image`                | Background Image               | `binary`    |     | ✅    |                    |
| `background_image_url`            | Background Url                 | `char`      |     |       |                    |
| `certification`                   | Is a Certification             | `boolean`   |     | ✅    |                    |
| `certification_badge_id`          | Certification Badge            | `many2one`  |     | ✅    | gamification.badge |
| `certification_badge_id_dummy`    | Certification Badge            | `many2one`  |     |       | gamification.badge |
| `certification_give_badge`        | Give Badge                     | `boolean`   |     | ✅    |                    |
| `certification_mail_template_id`  | Certified Email Template       | `many2one`  |     | ✅    | mail.template      |
| `certification_report_layout`     | Certification template         | `selection` |     | ✅    |                    |
| `certification_validity_months`   | Validity                       | `integer`   |     | ✅    |                    |
| `color`                           | Color Index                    | `integer`   |     | ✅    |                    |
| `course_id`                       | Course                         | `many2one`  |     | ✅    | op.course          |
| `create_date`                     | Created on                     | `datetime`  |     | ✅    |                    |
| `create_uid`                      | Created by                     | `many2one`  |     | ✅    | res.users          |
| `description`                     | Description                    | `html`      |     | ✅    |                    |
| `description_done`                | End Message                    | `html`      |     | ✅    |                    |
| `display_name`                    | Display Name                   | `char`      |     |       |                    |
| `generate_lead`                   | Lead Generating                | `boolean`   |     | ✅    |                    |
| `has_conditional_questions`       | Contains conditional questions | `boolean`   |     |       |                    |
| `has_message`                     | Has Message                    | `boolean`   |     |       |                    |
| `id`                              | ID                             | `integer`   |     | ✅    |                    |
| `is_attempts_limited`             | Limited number of attempts     | `boolean`   |     | ✅    |                    |
| `is_time_limited`                 | The survey is limited in time  | `boolean`   |     | ✅    |                    |
| `lang_ids`                        | Languages                      | `many2many` |     | ✅    | res.lang           |
| `lead_count`                      | Leads                          | `integer`   |     |       |                    |
| `lead_ids`                        | Lead                           | `one2many`  |     | ✅    | crm.lead           |
| `message_attachment_count`        | Attachment Count               | `integer`   |     |       |                    |
| `message_follower_ids`            | Followers                      | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`               | Message Delivery error         | `boolean`   |     |       |                    |
| `message_has_error_counter`       | Number of errors               | `integer`   |     |       |                    |
| `message_has_sms_error`           | SMS Delivery error             | `boolean`   |     |       |                    |
| `message_ids`                     | Messages                       | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`             | Is Follower                    | `boolean`   |     |       |                    |
| `message_needaction`              | Action Needed                  | `boolean`   |     |       |                    |
| `message_needaction_counter`      | Number of Actions              | `integer`   |     |       |                    |
| `message_partner_ids`             | Followers (Partners)           | `many2many` |     |       | res.partner        |
| `my_activity_date_deadline`       | My Activity Deadline           | `date`      |     |       |                    |
| `page_ids`                        | Pages                          | `one2many`  |     |       | survey.question    |
| `progression_mode`                | Display Progress as            | `selection` |     | ✅    |                    |
| `question_and_page_ids`           | Sections and Questions         | `one2many`  |     | ✅    | survey.question    |
| `question_count`                  | # Questions                    | `integer`   |     |       |                    |
| `question_ids`                    | Questions                      | `one2many`  |     |       | survey.question    |
| `questions_layout`                | Pagination                     | `selection` | ✅  | ✅    |                    |
| `questions_selection`             | Question Selection             | `selection` | ✅  | ✅    |                    |
| `rating_ids`                      | Ratings                        | `one2many`  |     | ✅    | rating.rating      |
| `restrict_user_ids`               | Restricted to                  | `many2many` |     | ✅    | res.users          |
| `scoring_max_obtainable`          | Maximum obtainable score       | `float`     |     |       |                    |
| `scoring_success_min`             | Required Score (%)             | `float`     |     | ✅    |                    |
| `scoring_type`                    | Scoring                        | `selection` | ✅  | ✅    |                    |
| `session_answer_count`            | Answers Count                  | `integer`   |     |       |                    |
| `session_available`               | Live session available         | `boolean`   |     |       |                    |
| `session_code`                    | Session Code                   | `char`      |     | ✅    |                    |
| `session_link`                    | Session Link                   | `char`      |     |       |                    |
| `session_question_answer_count`   | Question Answers Count         | `integer`   |     |       |                    |
| `session_question_id`             | Current Question               | `many2one`  |     | ✅    | survey.question    |
| `session_question_start_time`     | Current Question Start Time    | `datetime`  |     | ✅    |                    |
| `session_show_leaderboard`        | Show Session Leaderboard       | `boolean`   |     |       |                    |
| `session_speed_rating`            | Reward quick answers           | `boolean`   |     | ✅    |                    |
| `session_speed_rating_time_limit` | Time limit (seconds)           | `integer`   |     | ✅    |                    |
| `session_start_time`              | Current Session Start Time     | `datetime`  |     | ✅    |                    |
| `session_state`                   | Session State                  | `selection` |     | ✅    |                    |
| `success_count`                   | Success                        | `integer`   |     |       |                    |
| `success_ratio`                   | Success Ratio (%)              | `integer`   |     |       |                    |
| `survey_type`                     | Survey Type                    | `selection` | ✅  | ✅    |                    |
| `team_id`                         | Assign Leads to                | `many2one`  |     | ✅    | crm.team           |
| `time_limit`                      | Time limit (minutes)           | `float`     |     | ✅    |                    |
| `title`                           | Survey Title                   | `char`      | ✅  | ✅    |                    |
| `user_id`                         | Responsible                    | `many2one`  |     | ✅    | res.users          |
| `user_input_ids`                  | User responses                 | `one2many`  |     | ✅    | survey.user_input  |
| `users_can_go_back`               | Users can go back              | `boolean`   |     | ✅    |                    |
| `users_can_signup`                | Users can signup               | `boolean`   |     |       |                    |
| `users_login_required`            | Require Login                  | `boolean`   |     | ✅    |                    |
| `website_message_ids`             | Website Messages               | `one2many`  |     | ✅    | mail.message       |
| `write_date`                      | Last Updated on                | `datetime`  |     | ✅    |                    |
| `write_uid`                       | Last Updated by                | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                         | Group                   | Perms     |
| ---------------------------- | ----------------------- | --------- |
| survey.survey.survey.user    | Surveys / User          | `R/W/C/D` |
| survey.survey.survey.manager | Surveys / Administrator | `R/W/C/D` |
| survey.survey.user           | Role / User             | `-`       |
| survey.survey.all            | Everyone                | `-`       |

**Record Rules:**

- **Survey: manager: all** (29) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Survey: officer: unrestricted survey or in restricted users** (28) `R/W/C/D`
  - Domain:
    `[             '|', ('restrict_user_ids', 'in', user.id), ('restrict_user_ids', '=', False)]`

### 🗃️ `survey.user_input` — Survey User Input

> 📧 Mail Thread

Metadata for a set of one user's answers to a particular survey

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation               |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ---------------------- |
| `access_token`                  | Identification token          | `char`      | ✅  | ✅    |                        |
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
| `attempts_count`                | Attempts Count                | `integer`   |     |       |                        |
| `attempts_limit`                | Number of attempts            | `integer`   |     |       |                        |
| `attempts_number`               | Attempt n°                    | `integer`   |     |       |                        |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                        |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users              |
| `deadline`                      | Deadline                      | `datetime`  |     | ✅    |                        |
| `display_name`                  | Display Name                  | `char`      |     |       |                        |
| `email`                         | Email                         | `char`      |     | ✅    |                        |
| `end_datetime`                  | End date and time             | `datetime`  |     | ✅    |                        |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                        |
| `id`                            | ID                            | `integer`   |     | ✅    |                        |
| `invite_token`                  | Invite token                  | `char`      |     | ✅    |                        |
| `is_attempts_limited`           | Limited number of attempts    | `boolean`   |     |       |                        |
| `is_session_answer`             | Is in a Session               | `boolean`   |     | ✅    |                        |
| `lang_id`                       | Language                      | `many2one`  |     | ✅    | res.lang               |
| `last_displayed_page_id`        | Last displayed question/page  | `many2one`  |     | ✅    | survey.question        |
| `lead_id`                       | Lead                          | `many2one`  |     | ✅    | crm.lead               |
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
| `nickname`                      | Nickname                      | `char`      |     | ✅    |                        |
| `partner_id`                    | Contact                       | `many2one`  |     | ✅    | res.partner            |
| `predefined_question_ids`       | Predefined Questions          | `many2many` |     | ✅    | survey.question        |
| `question_time_limit_reached`   | Question Time Limit Reached   | `boolean`   |     |       |                        |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating          |
| `scoring_percentage`            | Score (%)                     | `float`     |     | ✅    |                        |
| `scoring_success`               | Quiz Passed                   | `boolean`   |     | ✅    |                        |
| `scoring_total`                 | Total Score                   | `float`     |     | ✅    |                        |
| `scoring_type`                  | Scoring                       | `selection` |     |       |                        |
| `start_datetime`                | Start date and time           | `datetime`  |     | ✅    |                        |
| `state`                         | Status                        | `selection` |     | ✅    |                        |
| `survey_first_submitted`        | Survey First Submitted        | `boolean`   |     | ✅    |                        |
| `survey_id`                     | Survey                        | `many2one`  | ✅  | ✅    | survey.survey          |
| `survey_time_limit_reached`     | Survey Time Limit Reached     | `boolean`   |     |       |                        |
| `test_entry`                    | Test Entry                    | `boolean`   |     | ✅    |                        |
| `user_input_line_ids`           | Answers                       | `one2many`  |     | ✅    | survey.user_input.line |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message           |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                        |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                             | Group                   | Perms     |
| -------------------------------- | ----------------------- | --------- |
| survey.user_input.survey.user    | Surveys / User          | `R/W/C/D` |
| survey.user_input.survey.manager | Surveys / Administrator | `R/W/C/D` |
| survey.user_input.user           | Role / User             | `-`       |
| survey.user_input.all            | Everyone                | `-`       |

**Record Rules:**

- **Survey user input: manager: all non specialized surveys** (29) `R/W/C/D`
  - Domain:
    `[('survey_id.survey_type', 'in', ('assessment', 'custom', 'live_session', 'survey'))]`
- **Survey user input: officer: unrestricted survey or in restricted users** (28)
  `R/W/C/D`
  - Domain:
    `[             '&', ('survey_id.survey_type', 'in', ('assessment', 'custom', 'live_session', 'survey')),             '|', ('survey_id.restrict_user_ids', 'in', user.id),                  ('survey_id.restrict_user_ids', '=', False)]`

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
