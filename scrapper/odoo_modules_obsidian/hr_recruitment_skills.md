---
title: "Recruitment - Skills Management"
module: "hr_recruitment_skills"
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

# 🟢 Recruitment - Skills Management

> **Module:** `hr_recruitment_skills` | **Version:** `19.0.1.0` **Category:**
> Recruitment | **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[hr_skills]] [[hr_recruitment]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `Recruitment/Configuration/Employees/Skill Types`

### Views

- `* INHERIT hr.applicant.view.form.inherit.hr.recruitment.skills (form)`
- `* INHERIT hr.applicant.view.list.inherit.hr.recruitment.skills (list)`
- `* INHERIT hr.applicant.view.search.inherit.skills (search)`
- `* INHERIT hr.applicant.view.search.inherit.skills.bis (search)`
- `* INHERIT hr.applicant.view.tree.inherit.skills (list)`
- `* INHERIT hr.job.view.form.inherit.hr.recruitment.skills (form)`
- `* INHERIT hr.job.view.list.inherit (list)`
- `hr.applicant.skill.view.form (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

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

### 🗃️ `hr.applicant.skill` — Skill level for an applicant

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                          | Type       | Req | Store | Relation       |
| -------------------------------- | ------------------------------ | ---------- | --- | ----- | -------------- |
| `applicant_id`                   | Applicant                      | `many2one` | ✅  | ✅    | hr.applicant   |
| `certification_skill_type_count` | Certification Skill Type Count | `integer`  |     |       |                |
| `color`                          | Color                          | `integer`  |     |       |                |
| `create_date`                    | Created on                     | `datetime` |     | ✅    |                |
| `create_uid`                     | Created by                     | `many2one` |     | ✅    | res.users      |
| `display_name`                   | Display Name                   | `char`     |     |       |                |
| `display_warning_message`        | Display Warning Message        | `boolean`  |     | ✅    |                |
| `id`                             | ID                             | `integer`  |     | ✅    |                |
| `is_certification`               | Certification                  | `boolean`  |     |       |                |
| `level_progress`                 | Progress                       | `integer`  |     |       |                |
| `levels_count`                   | Levels Count                   | `integer`  |     |       |                |
| `skill_id`                       | Skill                          | `many2one` | ✅  | ✅    | hr.skill       |
| `skill_level_id`                 | Skill Level                    | `many2one` | ✅  | ✅    | hr.skill.level |
| `skill_type_id`                  | Skill Type                     | `many2one` | ✅  | ✅    | hr.skill.type  |
| `valid_from`                     | Validity Start                 | `date`     |     | ✅    |                |
| `valid_to`                       | Validity Stop                  | `date`     |     | ✅    |                |
| `write_date`                     | Last Updated on                | `datetime` |     | ✅    |                |
| `write_uid`                      | Last Updated by                | `many2one` |     | ✅    | res.users      |

**Access Rights:**

| Name                                  | Group                     | Perms     |
| ------------------------------------- | ------------------------- | --------- |
| access_hr_applicant_skill_interviewer | Recruitment / Interviewer | `R/W/C/D` |

**Record Rules:**

- **Applicant Skill: Interviewer** (82) `R/W/C/D`
  - Domain:
    `[         '|',             ('applicant_id.job_id.interviewer_ids', 'in', user.id),             ('applicant_id.interviewer_ids', 'in', user.id),     ]`
- **Applicant Skill: Officer** (83) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
