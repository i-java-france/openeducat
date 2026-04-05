---
title: "Online Jobs"
module: "website_hr_recruitment"
state: "installed"
version: "19.0.1.1"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Website"
application: true
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/w______, odoo/app]
---

# 🟢 Online Jobs

> **Module:** `website_hr_recruitment` | **Version:** `19.0.1.1` **Category:** Website |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[hr_recruitment]] [[website_mail]]

## 📖 Description

This module allows to publish your available job positions on your website and keep
track of application submissions easily.

## 🖥️ UI Components

### Menus

- `Website/Site/Content/Jobs`

### Views

- `* INHERIT Job Pages Kanban (kanban)`
- `* INHERIT Job Pages List (list)`
- `* INHERIT Right Side Bar (qweb)`
- `* INHERIT hr.job search (search)`
- `* INHERIT hr.job.form (form)`
- `* INHERIT hr.job.form.inherit (form)`
- `* INHERIT hr.job.form.inherit.published.button (form)`
- `* INHERIT hr.job.kanban.inherit (kanban)`
- `* INHERIT hr.job.list (list)`
- `* INHERIT hr.job.view.kanban (kanban)`
- `* INHERIT hr.recruitment.list.inherit.url (list)`
- `* INHERIT job_filter_by_countries (qweb)`
- `* INHERIT job_filter_by_departments (qweb)`
- `* INHERIT job_filter_by_employment_type (qweb)`
- `* INHERIT job_filter_by_industries (qweb)`
- `* INHERIT job_filter_by_offices (qweb)`
- `* INHERIT job_reset_filters (qweb)`
- `* INHERIT job_search_bar (qweb)`
- `Job Detail (qweb)`
- `Jobs (qweb)`
- `Thank you (Recruitment) (qweb)`
- `Topbar (qweb)`
- `apply (qweb)`
- `default_website_description (qweb)`
- `job_filter_base (qweb)`
- `job_filter_base_mobile (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**6 model(s) defined by this module:**

### 🗃️ `hr.applicant` — Applicant

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type         | Req | Store | Relation                   |
| ------------------------------- | ----------------------------- | ------------ | --- | ----- | -------------------------- |
| `active`                        | Active                        | `boolean`    |     | ✅    |                            |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`   |     |       | calendar.event             |
| `activity_date_deadline`        | Next Activity Deadline        | `date`       |     |       |                            |
| `activity_exception_decoration` | Activity Exception Decoration | `selection`  |     |       |                            |
| `activity_exception_icon`       | Icon                          | `char`       |     |       |                            |
| `activity_ids`                  | Activities                    | `one2many`   |     | ✅    | mail.activity              |
| `activity_state`                | Activity State                | `selection`  |     |       |                            |
| `activity_summary`              | Next Activity Summary         | `char`       |     |       |                            |
| `activity_type_icon`            | Activity Type Icon            | `char`       |     |       |                            |
| `activity_type_id`              | Next Activity Type            | `many2one`   |     |       | mail.activity.type         |
| `activity_user_id`              | Responsible User              | `many2one`   |     |       | res.users                  |
| `applicant_notes`               | Applicant Notes               | `html`       |     | ✅    |                            |
| `applicant_properties`          | Properties                    | `properties` |     | ✅    |                            |
| `applicant_skill_ids`           | Skills                        | `one2many`   |     | ✅    | hr.applicant.skill         |
| `application_count`             | Application Count             | `integer`    |     |       |                            |
| `application_status`            | Application Status            | `selection`  |     |       |                            |
| `attachment_ids`                | Attachments                   | `one2many`   |     | ✅    | ir.attachment              |
| `attachment_number`             | Number of Attachments         | `integer`    |     |       |                            |
| `availability`                  | Availability                  | `date`       |     | ✅    |                            |
| `campaign_id`                   | Campaign                      | `many2one`   |     | ✅    | utm.campaign               |
| `categ_ids`                     | Tags                          | `many2many`  |     | ✅    | hr.applicant.category      |
| `color`                         | Color Index                   | `integer`    |     | ✅    |                            |
| `company_id`                    | Company                       | `many2one`   |     | ✅    | res.company                |
| `create_date`                   | Applied on                    | `datetime`   |     | ✅    |                            |
| `create_uid`                    | Created by                    | `many2one`   |     | ✅    | res.users                  |
| `current_applicant_skill_ids`   | Current Applicant Skill       | `one2many`   |     |       | hr.applicant.skill         |
| `date_closed`                   | Hire Date                     | `datetime`   |     | ✅    |                            |
| `date_last_stage_update`        | Last Stage Update             | `datetime`   |     | ✅    |                            |
| `date_open`                     | Assigned                      | `datetime`   |     | ✅    |                            |
| `day_close`                     | Days to Close                 | `float`      |     |       |                            |
| `day_open`                      | Days to Open                  | `float`      |     |       |                            |
| `delay_close`                   | Delay to Close                | `float`      |     | ✅    |                            |
| `department_id`                 | Department                    | `many2one`   |     | ✅    | hr.department              |
| `display_name`                  | Display Name                  | `char`       |     |       |                            |
| `duration_tracking`             | Status time                   | `json`       |     |       |                            |
| `email_cc`                      | Email cc                      | `char`       |     | ✅    |                            |
| `email_from`                    | Email                         | `char`       |     | ✅    |                            |
| `email_normalized`              | Normalized Email              | `char`       |     | ✅    |                            |
| `emp_is_active`                 | Employee Active               | `boolean`    |     |       |                            |
| `employee_id`                   | Employee                      | `many2one`   |     | ✅    | hr.employee                |
| `employee_name`                 | Employee Name                 | `char`       |     |       |                            |
| `has_message`                   | Has Message                   | `boolean`    |     |       |                            |
| `id`                            | ID                            | `integer`    |     | ✅    |                            |
| `interviewer_ids`               | Interviewers                  | `many2many`  |     | ✅    | res.users                  |
| `is_applicant_in_pool`          | Is Applicant In Pool          | `boolean`    |     |       |                            |
| `is_blacklisted`                | Blacklist                     | `boolean`    |     |       |                            |
| `is_pool_applicant`             | Is Pool Applicant             | `boolean`    |     |       |                            |
| `is_rotting`                    | Rotting                       | `boolean`    |     |       |                            |
| `job_id`                        | Job Position                  | `many2one`   |     | ✅    | hr.job                     |
| `kanban_state`                  | Kanban State                  | `selection`  | ✅  | ✅    |                            |
| `last_stage_id`                 | Last Stage                    | `many2one`   |     | ✅    | hr.recruitment.stage       |
| `legend_blocked`                | Kanban Blocked                | `char`       |     |       |                            |
| `legend_done`                   | Kanban Valid                  | `char`       |     |       |                            |
| `legend_normal`                 | Kanban Ongoing                | `char`       |     |       |                            |
| `legend_waiting`                | Kanban Waiting                | `char`       |     |       |                            |
| `linkedin_profile`              | LinkedIn Profile              | `char`       |     | ✅    |                            |
| `matching_score`                | Matching Score                | `integer`    |     |       |                            |
| `matching_skill_ids`            | Matching Skills               | `many2many`  |     |       | hr.skill                   |
| `medium_id`                     | Medium                        | `many2one`   |     | ✅    | utm.medium                 |
| `meeting_display_date`          | Meeting Display Date          | `date`       |     |       |                            |
| `meeting_display_text`          | Meeting Display Text          | `char`       |     |       |                            |
| `meeting_ids`                   | Meetings                      | `one2many`   |     | ✅    | calendar.event             |
| `message_attachment_count`      | Attachment Count              | `integer`    |     |       |                            |
| `message_bounce`                | Bounce                        | `integer`    |     | ✅    |                            |
| `message_follower_ids`          | Followers                     | `one2many`   |     | ✅    | mail.followers             |
| `message_has_error`             | Message Delivery error        | `boolean`    |     |       |                            |
| `message_has_error_counter`     | Number of errors              | `integer`    |     |       |                            |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`    |     |       |                            |
| `message_ids`                   | Messages                      | `one2many`   |     | ✅    | mail.message               |
| `message_is_follower`           | Is Follower                   | `boolean`    |     |       |                            |
| `message_main_attachment_id`    | Main Attachment               | `many2one`   |     | ✅    | ir.attachment              |
| `message_needaction`            | Action Needed                 | `boolean`    |     |       |                            |
| `message_needaction_counter`    | Number of Actions             | `integer`    |     |       |                            |
| `message_partner_ids`           | Followers (Partners)          | `many2many`  |     |       | res.partner                |
| `missing_skill_ids`             | Missing Skills                | `many2many`  |     |       | hr.skill                   |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`       |     |       |                            |
| `partner_id`                    | Contact                       | `many2one`   |     | ✅    | res.partner                |
| `partner_name`                  | Applicant's Name              | `char`       |     | ✅    |                            |
| `partner_phone`                 | Phone                         | `char`       |     | ✅    |                            |
| `partner_phone_sanitized`       | Sanitized Phone Number        | `char`       |     | ✅    |                            |
| `phone_blacklisted`             | Blacklisted Phone is Phone    | `boolean`    |     |       |                            |
| `phone_mobile_search`           | Phone Number                  | `char`       |     |       |                            |
| `phone_sanitized`               | Sanitized Number              | `char`       |     | ✅    |                            |
| `phone_sanitized_blacklisted`   | Phone Blacklisted             | `boolean`    |     |       |                            |
| `pool_applicant_id`             | Pool Applicant                | `many2one`   |     | ✅    | hr.applicant               |
| `priority`                      | Evaluation                    | `selection`  |     | ✅    |                            |
| `probability`                   | Probability                   | `float`      |     | ✅    |                            |
| `rating_ids`                    | Ratings                       | `one2many`   |     | ✅    | rating.rating              |
| `refuse_date`                   | Refuse Date                   | `datetime`   |     | ✅    |                            |
| `refuse_reason_id`              | Refuse Reason                 | `many2one`   |     | ✅    | hr.applicant.refuse.reason |
| `rotting_days`                  | Days Rotting                  | `integer`    |     |       |                            |
| `salary_expected`               | Expected                      | `float`      |     | ✅    |                            |
| `salary_expected_extra`         | Expected Salary Extra         | `char`       |     | ✅    |                            |
| `salary_proposed`               | Proposed                      | `float`      |     | ✅    |                            |
| `salary_proposed_extra`         | Proposed Salary Extra         | `char`       |     | ✅    |                            |
| `sequence`                      | Sequence                      | `integer`    |     | ✅    |                            |
| `skill_ids`                     | Skill                         | `many2many`  |     | ✅    | hr.skill                   |
| `source_id`                     | Source                        | `many2one`   |     | ✅    | utm.source                 |
| `stage_id`                      | Stage                         | `many2one`   |     | ✅    | hr.recruitment.stage       |
| `talent_pool_count`             | Talent Pool Count             | `integer`    |     |       |                            |
| `talent_pool_ids`               | Talent Pools                  | `many2many`  |     | ✅    | hr.talent.pool             |
| `type_id`                       | Degree                        | `many2one`   |     | ✅    | hr.recruitment.degree      |
| `user_email`                    | User Email                    | `char`       |     |       |                            |
| `user_id`                       | Recruiter                     | `many2one`   |     | ✅    | res.users                  |
| `website_message_ids`           | Website Messages              | `one2many`   |     | ✅    | mail.message               |
| `write_date`                    | Last Updated on               | `datetime`   |     | ✅    |                            |
| `write_uid`                     | Last Updated by               | `many2one`   |     | ✅    | res.users                  |

**Access Rights:**

| Name                     | Group                                        | Perms     |
| ------------------------ | -------------------------------------------- | --------- |
| hr.applicant.interviewer | Recruitment / Interviewer                    | `R/W`     |
| hr.applicant.user        | Recruitment / Officer: Manage all applicants | `R/W/C/D` |

**Record Rules:**

- **Applicant multi company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Applicant Interviewer** (82) `R/W`
  - Domain:
    `[         '|',             ('job_id.interviewer_ids', 'in', user.id),             ('interviewer_ids', 'in', user.id),     ]`
- **User: All Applicants** (83) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `hr.department` — Department

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
| `absence_of_today`              | Absence by Today              | `integer`   |     |       |                    |
| `active`                        | Active                        | `boolean`   |     | ✅    |                    |
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
| `allocation_to_approve_count`   | Allocation to Approve         | `integer`   |     |       |                    |
| `child_ids`                     | Child Departments             | `one2many`  |     | ✅    | hr.department      |
| `color`                         | Color Index                   | `integer`   |     | ✅    |                    |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company        |
| `complete_name`                 | Complete Name                 | `char`      |     |       |                    |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `expected_employee`             | Expected Employee             | `integer`   |     |       |                    |
| `expenses_to_approve_count`     | Expenses to Approve           | `integer`   |     |       |                    |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `has_read_access`               | Has Read Access               | `boolean`   |     |       |                    |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
| `jobs_ids`                      | Jobs                          | `one2many`  |     | ✅    | hr.job             |
| `leave_to_approve_count`        | Time Off to Approve           | `integer`   |     |       |                    |
| `manager_id`                    | Manager                       | `many2one`  |     | ✅    | hr.employee        |
| `master_department_id`          | Master Department             | `many2one`  |     | ✅    | hr.department      |
| `member_ids`                    | Members                       | `one2many`  |     | ✅    | hr.employee        |
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
| `name`                          | Department Name               | `char`      | ✅  | ✅    |                    |
| `new_applicant_count`           | New Applicant                 | `integer`   |     |       |                    |
| `new_hired_employee`            | New Hired Employee            | `integer`   |     |       |                    |
| `note`                          | Note                          | `text`      |     | ✅    |                    |
| `parent_id`                     | Parent Department             | `many2one`  |     | ✅    | hr.department      |
| `parent_path`                   | Parent Path                   | `char`      |     | ✅    |                    |
| `plan_ids`                      | Plan                          | `one2many`  |     | ✅    | mail.activity.plan |
| `plans_count`                   | Plans Count                   | `integer`   |     |       |                    |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `total_employee`                | Total Employee                | `integer`   |     |       |                    |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                   | Group                                     | Perms     |
| ---------------------- | ----------------------------------------- | --------- |
| hr.department.user     | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.department.public   | Role / Public                             | `R`       |
| hr.department.employee | Role / User                               | `R`       |

**Record Rules:**

- **Department multi company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Job department: Public** (11) `R`
  - Domain:
    `['|', ('jobs_ids.website_published', '=', True), ('child_ids', 'not in', [])]`

### 🗃️ `hr.job` — Job Position

> 📧 Mail Thread

A mixin for models that inherits mail.alias to have a one-to-one relation between the
model and its alias.

**Fields:**

| Field                             | Label                               | Type                    | Req | Store | Relation              |
| --------------------------------- | ----------------------------------- | ----------------------- | --- | ----- | --------------------- |
| `active`                          | Active                              | `boolean`               |     | ✅    |                       |
| `activity_calendar_event_id`      | Next Activity Calendar Event        | `many2one`              |     |       | calendar.event        |
| `activity_count`                  | Activity Count                      | `integer`               |     |       |                       |
| `activity_date_deadline`          | Next Activity Deadline              | `date`                  |     |       |                       |
| `activity_exception_decoration`   | Activity Exception Decoration       | `selection`             |     |       |                       |
| `activity_exception_icon`         | Icon                                | `char`                  |     |       |                       |
| `activity_ids`                    | Activities                          | `one2many`              |     | ✅    | mail.activity         |
| `activity_state`                  | Activity State                      | `selection`             |     |       |                       |
| `activity_summary`                | Next Activity Summary               | `char`                  |     |       |                       |
| `activity_type_icon`              | Activity Type Icon                  | `char`                  |     |       |                       |
| `activity_type_id`                | Next Activity Type                  | `many2one`              |     |       | mail.activity.type    |
| `activity_user_id`                | Responsible User                    | `many2one`              |     |       | res.users             |
| `address_id`                      | Job Location                        | `many2one`              |     | ✅    | res.partner           |
| `alias_bounced_content`           | Custom Bounced Message              | `html`                  |     |       |                       |
| `alias_contact`                   | Alias Contact Security              | `selection`             | ✅  |       |                       |
| `alias_defaults`                  | Default Values                      | `text`                  | ✅  |       |                       |
| `alias_domain`                    | Alias Domain Name                   | `char`                  |     |       |                       |
| `alias_domain_id`                 | Alias Domain                        | `many2one`              |     |       | mail.alias.domain     |
| `alias_email`                     | Email Alias                         | `char`                  |     |       |                       |
| `alias_force_thread_id`           | Record Thread ID                    | `integer`               |     |       |                       |
| `alias_full_name`                 | Alias Email                         | `char`                  |     |       |                       |
| `alias_id`                        | Alias                               | `many2one`              | ✅  | ✅    | mail.alias            |
| `alias_incoming_local`            | Local-part based incoming detection | `boolean`               |     |       |                       |
| `alias_model_id`                  | Aliased Model                       | `many2one`              | ✅  |       | ir.model              |
| `alias_name`                      | Alias Name                          | `char`                  |     |       |                       |
| `alias_parent_model_id`           | Parent Model                        | `many2one`              |     |       | ir.model              |
| `alias_parent_thread_id`          | Parent Record Thread ID             | `integer`               |     |       |                       |
| `alias_status`                    | Alias Status                        | `selection`             |     |       |                       |
| `all_application_count`           | All Application Count               | `integer`               |     |       |                       |
| `allowed_user_ids`                | Allowed User                        | `many2many`             |     |       | res.users             |
| `applicant_hired`                 | Applicants Hired                    | `integer`               |     |       |                       |
| `applicant_matching_score`        | Matching Score(%)                   | `float`                 |     |       |                       |
| `applicant_properties_definition` | Applicant Properties                | `properties_definition` |     | ✅    |                       |
| `application_count`               | Application Count                   | `integer`               |     |       |                       |
| `application_ids`                 | Job Applications                    | `one2many`              |     | ✅    | hr.applicant          |
| `can_publish`                     | Can Publish                         | `boolean`               |     |       |                       |
| `color`                           | Color Index                         | `integer`               |     | ✅    |                       |
| `company_id`                      | Company                             | `many2one`              |     | ✅    | res.company           |
| `contract_type_id`                | Employment Type                     | `many2one`              |     | ✅    | hr.contract.type      |
| `create_date`                     | Created on                          | `datetime`              |     | ✅    |                       |
| `create_uid`                      | Created by                          | `many2one`              |     | ✅    | res.users             |
| `current_job_skill_ids`           | Current Job Skill                   | `one2many`              |     |       | hr.job.skill          |
| `department_id`                   | Department                          | `many2one`              |     | ✅    | hr.department         |
| `description`                     | Job Description                     | `html`                  |     | ✅    |                       |
| `display_name`                    | Display Name                        | `char`                  |     |       |                       |
| `document_ids`                    | Documents                           | `one2many`              |     |       | ir.attachment         |
| `documents_count`                 | Document Count                      | `integer`               |     |       |                       |
| `employee_count`                  | Employee Count                      | `integer`               |     |       |                       |
| `employee_ids`                    | Employees                           | `one2many`              |     | ✅    | hr.employee           |
| `expected_degree`                 | Expected Degree                     | `many2one`              |     | ✅    | hr.recruitment.degree |
| `expected_employees`              | Total Forecasted Employees          | `integer`               |     |       |                       |
| `extended_interviewer_ids`        | Extended Interviewer                | `many2many`             |     | ✅    | res.users             |
| `favorite_user_ids`               | Favorite User                       | `many2many`             |     | ✅    | res.users             |
| `full_url`                        | job URL                             | `char`                  |     |       |                       |
| `has_message`                     | Has Message                         | `boolean`               |     |       |                       |
| `id`                              | ID                                  | `integer`               |     | ✅    |                       |
| `industry_id`                     | Industry                            | `many2one`              |     | ✅    | res.partner.industry  |
| `interviewer_ids`                 | Interviewers                        | `many2many`             |     | ✅    | res.users             |
| `is_favorite`                     | Is Favorite                         | `boolean`               |     |       |                       |
| `is_published`                    | Is Published                        | `boolean`               |     | ✅    |                       |
| `is_seo_optimized`                | SEO optimized                       | `boolean`               |     | ✅    |                       |
| `job_details`                     | Process Details                     | `html`                  |     | ✅    |                       |
| `job_properties`                  | Properties                          | `properties`            |     | ✅    |                       |
| `job_skill_ids`                   | Skills                              | `one2many`              |     | ✅    | hr.job.skill          |
| `job_source_ids`                  | Job Source                          | `one2many`              |     | ✅    | hr.recruitment.source |
| `manager_id`                      | Department Manager                  | `many2one`              |     | ✅    | hr.employee           |
| `message_attachment_count`        | Attachment Count                    | `integer`               |     |       |                       |
| `message_follower_ids`            | Followers                           | `one2many`              |     | ✅    | mail.followers        |
| `message_has_error`               | Message Delivery error              | `boolean`               |     |       |                       |
| `message_has_error_counter`       | Number of errors                    | `integer`               |     |       |                       |
| `message_has_sms_error`           | SMS Delivery error                  | `boolean`               |     |       |                       |
| `message_ids`                     | Messages                            | `one2many`              |     | ✅    | mail.message          |
| `message_is_follower`             | Is Follower                         | `boolean`               |     |       |                       |
| `message_needaction`              | Action Needed                       | `boolean`               |     |       |                       |
| `message_needaction_counter`      | Number of Actions                   | `integer`               |     |       |                       |
| `message_partner_ids`             | Followers (Partners)                | `many2many`             |     |       | res.partner           |
| `my_activity_date_deadline`       | My Activity Deadline                | `date`                  |     |       |                       |
| `name`                            | Job Position                        | `char`                  | ✅  | ✅    |                       |
| `new_application_count`           | New Application                     | `integer`               |     |       |                       |
| `no_of_employee`                  | Current Number of Employees         | `integer`               |     |       |                       |
| `no_of_hired_employee`            | Hired                               | `integer`               |     | ✅    |                       |
| `no_of_recruitment`               | Target                              | `integer`               |     | ✅    |                       |
| `old_application_count`           | Old Application                     | `integer`               |     |       |                       |
| `open_application_count`          | Open Application Count              | `integer`               |     |       |                       |
| `published_date`                  | Published Date                      | `date`                  |     | ✅    |                       |
| `rating_ids`                      | Ratings                             | `one2many`              |     | ✅    | rating.rating         |
| `requirements`                    | Requirements                        | `text`                  |     | ✅    |                       |
| `seo_name`                        | Seo name                            | `char`                  |     | ✅    |                       |
| `sequence`                        | Sequence                            | `integer`               |     | ✅    |                       |
| `skill_ids`                       | Skill                               | `many2many`             |     | ✅    | hr.skill              |
| `user_id`                         | Recruiter                           | `many2one`              |     | ✅    | res.users             |
| `website_absolute_url`            | Website Absolute URL                | `char`                  |     |       |                       |
| `website_description`             | Website description                 | `html`                  |     | ✅    |                       |
| `website_id`                      | Website                             | `many2one`              |     | ✅    | website               |
| `website_message_ids`             | Website Messages                    | `one2many`              |     | ✅    | mail.message          |
| `website_meta_description`        | Website meta description            | `text`                  |     | ✅    |                       |
| `website_meta_keywords`           | Website meta keywords               | `char`                  |     | ✅    |                       |
| `website_meta_og_img`             | Website opengraph image             | `char`                  |     | ✅    |                       |
| `website_meta_title`              | Website meta title                  | `char`                  |     | ✅    |                       |
| `website_published`               | Visible on current website          | `boolean`               |     |       |                       |
| `website_url`                     | Website URL                         | `char`                  |     |       |                       |
| `write_date`                      | Last Updated on                     | `datetime`              |     | ✅    |                       |
| `write_uid`                       | Last Updated by                     | `many2one`              |     | ✅    | res.users             |

**Access Rights:**

| Name               | Group                                        | Perms     |
| ------------------ | -------------------------------------------- | --------- |
| hr.job user        | Employees / Officer: Manage all employees    | `R`       |
| hr.job.interviewer | Recruitment / Interviewer                    | `R`       |
| hr.job user        | Recruitment / Officer: Manage all applicants | `R/W/C/D` |
| hr.job.public      | Role / Portal                                | `R`       |
| hr.job.public      | Role / Public                                | `R`       |
| hr.job.employee    | Role / User                                  | `R`       |
| hr.job.public      | Role / User                                  | `R`       |

**Record Rules:**

- **Job multi company rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **User: All Applicants** (83) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Job Positions: Public** (11) `R`
  - Domain: `[('website_published', '=', True)]`
- **Job Positions: Portal** (10) `R`
  - Domain: `[('website_published', '=', True)]`
- **Job Positions: HR Officer** (83) `R`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `website.page` — Page

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                         | Label                             | Type        | Req | Store | Relation                |
| ----------------------------- | --------------------------------- | ----------- | --- | ----- | ----------------------- |
| `active`                      | Active                            | `boolean`   |     |       |                         |
| `arch`                        | View Architecture                 | `text`      |     |       |                         |
| `arch_base`                   | Base View Architecture            | `text`      |     |       |                         |
| `arch_db`                     | Arch Blob                         | `text`      |     |       |                         |
| `arch_fs`                     | Arch Filename                     | `char`      |     |       |                         |
| `arch_prev`                   | Previous View Architecture        | `text`      |     |       |                         |
| `arch_updated`                | Modified Architecture             | `boolean`   |     |       |                         |
| `can_publish`                 | Can Publish                       | `boolean`   |     |       |                         |
| `controller_page_ids`         | Controller Page                   | `one2many`  |     |       | website.controller.page |
| `create_date`                 | Created on                        | `datetime`  |     | ✅    |                         |
| `create_uid`                  | Created by                        | `many2one`  |     | ✅    | res.users               |
| `customize_show`              | Show As Optional Inherit          | `boolean`   |     |       |                         |
| `date_publish`                | Publishing Date                   | `datetime`  |     | ✅    |                         |
| `display_name`                | Display Name                      | `char`      |     |       |                         |
| `first_page_id`               | Website Page                      | `many2one`  |     |       | website.page            |
| `footer_visible`              | Footer Visible                    | `boolean`   |     | ✅    |                         |
| `group_ids`                   | Groups                            | `many2many` |     |       | res.groups              |
| `header_color`                | Header Color                      | `char`      |     | ✅    |                         |
| `header_overlay`              | Header Overlay                    | `boolean`   |     | ✅    |                         |
| `header_text_color`           | Header Text Color                 | `char`      |     | ✅    |                         |
| `header_visible`              | Header Visible                    | `boolean`   |     | ✅    |                         |
| `id`                          | ID                                | `integer`   |     | ✅    |                         |
| `inherit_children_ids`        | Views which inherit from this one | `one2many`  |     |       | ir.ui.view              |
| `inherit_id`                  | Inherited View                    | `many2one`  |     |       | ir.ui.view              |
| `invalid_locators`            | Invalid Locators                  | `json`      |     |       |                         |
| `is_homepage`                 | Homepage                          | `boolean`   |     |       |                         |
| `is_in_menu`                  | Is In Menu                        | `boolean`   |     |       |                         |
| `is_new_page_template`        | New Page Template                 | `boolean`   |     | ✅    |                         |
| `is_published`                | Is Published                      | `boolean`   |     | ✅    |                         |
| `is_seo_optimized`            | SEO optimized                     | `boolean`   |     |       |                         |
| `is_visible`                  | Is Visible                        | `boolean`   |     |       |                         |
| `key`                         | Key                               | `char`      |     |       |                         |
| `menu_ids`                    | Related Menus                     | `one2many`  |     | ✅    | website.menu            |
| `mode`                        | View inheritance mode             | `selection` | ✅  |       |                         |
| `model`                       | Model                             | `char`      |     |       |                         |
| `model_data_id`               | Model Data                        | `many2one`  |     |       | ir.model.data           |
| `model_id`                    | Model of the view                 | `many2one`  |     |       | ir.model                |
| `name`                        | View Name                         | `char`      | ✅  |       |                         |
| `page_ids`                    | Page                              | `one2many`  |     |       | website.page            |
| `priority`                    | Sequence                          | `integer`   | ✅  |       |                         |
| `seo_name`                    | Seo name                          | `char`      |     |       |                         |
| `theme_template_id`           | Theme Template                    | `many2one`  |     | ✅    | theme.website.page      |
| `track`                       | Track                             | `boolean`   |     |       |                         |
| `type`                        | View Type                         | `selection` |     |       |                         |
| `url`                         | Page URL                          | `char`      | ✅  | ✅    |                         |
| `view_id`                     | View                              | `many2one`  | ✅  | ✅    | ir.ui.view              |
| `view_write_date`             | Last Content Update on            | `datetime`  |     |       |                         |
| `view_write_uid`              | Last Content Update by            | `many2one`  |     |       | res.users               |
| `visibility`                  | Visibility                        | `selection` |     |       |                         |
| `visibility_password`         | Visibility Password               | `char`      |     |       |                         |
| `visibility_password_display` | Visibility Password Display       | `char`      |     |       |                         |
| `warning_info`                | Warning information               | `html`      |     |       |                         |
| `website_absolute_url`        | Website Absolute URL              | `char`      |     |       |                         |
| `website_id`                  | Website                           | `many2one`  |     | ✅    | website                 |
| `website_indexed`             | Is Indexed                        | `boolean`   |     | ✅    |                         |
| `website_meta_description`    | Website meta description          | `text`      |     |       |                         |
| `website_meta_keywords`       | Website meta keywords             | `char`      |     |       |                         |
| `website_meta_og_img`         | Website opengraph image           | `char`      |     |       |                         |
| `website_meta_title`          | Website meta title                | `char`      |     |       |                         |
| `website_published`           | Visible on current website        | `boolean`   |     |       |                         |
| `website_url`                 | Website URL                       | `char`      |     |       |                         |
| `write_date`                  | Last Updated on                   | `datetime`  |     | ✅    |                         |
| `write_uid`                   | Last Updated by                   | `many2one`  |     | ✅    | res.users               |
| `xml_id`                      | External ID                       | `char`      |     |       |                         |

**Access Rights:**

| Name             | Group                         | Perms     |
| ---------------- | ----------------------------- | --------- |
| Web Page Manager | Website / Editor and Designer | `R/W/C/D` |

**Record Rules:**

- **website.page: portal/public: read published pages** (10, 11) `R/W/C/D`
  - Domain: `[('website_published', '=', True)]`

### 🗃️ `hr.recruitment.source` — Source of Applicants

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation     |
| -------------- | --------------- | ---------- | --- | ----- | ------------ |
| `alias_id`     | Alias ID        | `many2one` |     | ✅    | mail.alias   |
| `campaign_id`  | Campaign        | `many2one` |     | ✅    | utm.campaign |
| `create_date`  | Created on      | `datetime` |     | ✅    |              |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users    |
| `display_name` | Display Name    | `char`     |     |       |              |
| `email`        | Email           | `char`     |     |       |              |
| `has_domain`   | Has Domain      | `char`     |     |       |              |
| `id`           | ID              | `integer`  |     | ✅    |              |
| `job_id`       | Job             | `many2one` |     | ✅    | hr.job       |
| `medium_id`    | Medium          | `many2one` |     | ✅    | utm.medium   |
| `name`         | Name            | `char`     |     |       |              |
| `source_id`    | Source          | `many2one` | ✅  | ✅    | utm.source   |
| `url`          | Tracker URL     | `char`     |     |       |              |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |              |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users    |

**Access Rights:**

| Name                  | Group                                        | Perms     |
| --------------------- | -------------------------------------------- | --------- |
| hr.recruitment.source | Recruitment / Officer: Manage all applicants | `R/W/C/D` |
| hr.recruitment.source | Role / User                                  | `R`       |

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
