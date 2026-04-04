---
title: "Recruitment - SMS"
module: "hr_recruitment_sms"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Recruitment"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/___________]
---

# 🟢 Recruitment - SMS

> **Module:** `hr_recruitment_sms` | **Version:** `19.0.1.0` **Category:** Recruitment |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[hr_recruitment]] [[sms]]

## 📖 Description

Mass mailing sms to job applicants

## 🖥️ UI Components

### Menus

_none_

### Views

_none_

### Reports

_none_

## 🛠️ Technical Documentation

**1 model(s) defined by this module:**

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
