---
title: "Skills Management"
module: "hr_skills"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Employees"
application: true
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_________, odoo/app]
---

# 🟢 Skills Management

> **Module:** `hr_skills` | **Version:** `19.0.1.0` **Category:** Employees |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[hr]]

## 📖 Description

# Skills and Resume for HR

This module introduces skills and resume management for employees.

## 🖥️ UI Components

### Menus

- `Employees/Configuration/Employee/Skill Types`
- `Employees/Configuration/Resume`
- `Employees/Configuration/Resume/Sections`
- `Employees/Learning`
- `Employees/Learning/Certifications`
- `Employees/Learning/Training Attendances`
- `Employees/Reporting/Skills`
- `Employees/Reporting/Skills/Certifications`
- `Employees/Reporting/Skills/Skills Inventory`

### Views

- `* INHERIT hr.department.kanban.inherit.hr.skills (kanban)`
- `* INHERIT hr.employee.public.skill.search (search)`
- `* INHERIT hr.employee.public.view.form.inherit.resume (form)`
- `* INHERIT hr.employee.skill.search (search)`
- `* INHERIT hr.employee.view.form.inherit.resume (form)`
- `* INHERIT hr.employees.skill.inherit.certificate.form (form)`
- `* INHERIT hr.job.view.form.inherit.hr.skills (form)`
- `* INHERIT hr.resume.line.inherit.form (form)`
- `hr.employee.certification.report list (list)`
- `hr.employee.certification.report pivot (pivot)`
- `hr.employee.certification.report search (search)`
- `hr.employee.cv.wizard.view.form (form)`
- `hr.employee.skill.history.report graph (graph)`
- `hr.employee.skill.history.report search (search)`
- `hr.employee.skill.report graph (graph)`
- `hr.employee.skill.report list (list)`
- `hr.employee.skill.report pivot (pivot)`
- `hr.employee.skill.report search (search)`
- `hr.employee.skill.view.search (search)`
- `hr.employees.skill.form (form)`
- `hr.employees.skill.list (list)`
- `hr.job.skill.view.form (form)`
- `hr.resume.line.calendar.view (calendar)`
- `hr.resume.line.form (form)`
- `hr.resume.line.kanban.view (kanban)`
- `hr.resume.line.list.view (list)`
- `hr.resume.line.search (search)`
- `hr.resume.line.type.list.view (list)`
- `hr.skill.form (form)`
- `hr.skill.level.form (form)`
- `hr.skill.level.list (list)`
- `hr.skill.list (list)`
- `hr.skill.type.form (form)`
- `hr.skill.type.list (list)`
- `hr.skill.type.search (search)`
- `hr.skill.view.search (search)`
- `report_employee_cv (qweb)`
- `report_employee_cv_company (qweb)`
- `report_employee_cv_main_panel (qweb)`
- `report_employee_cv_sidepanel (qweb)`

### Reports

- `Employee Resume`

## 🛠️ Technical Documentation

**17 model(s) defined by this module:**

### 🗃️ `hr.employee` — Employee

> 📧 Mail Thread

    NB: Any field only available on the model hr.employee (i.e. not on the
    hr.employee.public model) should have `groups="hr.group_hr_user"` on its
    definition to avoid being prefetched when the user hasn't access to the
    hr.employee model. Indeed, the prefetch loads the data for all the fields
    that are available according to the group defined on them.

**Fields:**

| Field                            | Label                           | Type         | Req | Store | Relation                  |
| -------------------------------- | ------------------------------- | ------------ | --- | ----- | ------------------------- |
| `active`                         | Active                          | `boolean`    |     | ✅    |                           |
| `active_employee`                | Active Employee                 | `boolean`    |     |       |                           |
| `activity_calendar_event_id`     | Next Activity Calendar Event    | `many2one`   |     |       | calendar.event            |
| `activity_date_deadline`         | Next Activity Deadline          | `date`       |     |       |                           |
| `activity_exception_decoration`  | Activity Exception Decoration   | `selection`  |     |       |                           |
| `activity_exception_icon`        | Icon                            | `char`       |     |       |                           |
| `activity_ids`                   | Activities                      | `one2many`   |     | ✅    | mail.activity             |
| `activity_state`                 | Activity State                  | `selection`  |     |       |                           |
| `activity_summary`               | Next Activity Summary           | `char`       |     |       |                           |
| `activity_type_icon`             | Activity Type Icon              | `char`       |     |       |                           |
| `activity_type_id`               | Next Activity Type              | `many2one`   |     |       | mail.activity.type        |
| `activity_user_id`               | Responsible User                | `many2one`   |     |       | res.users                 |
| `additional_note`                | Additional Note                 | `text`       |     |       |                           |
| `address_id`                     | Work Address                    | `many2one`   |     |       | res.partner               |
| `allocation_count`               | Total number of days allocated. | `float`      |     |       |                           |
| `allocation_display`             | Allocation Display              | `char`       |     |       |                           |
| `allocation_remaining_display`   | Allocation Remaining Display    | `char`       |     |       |                           |
| `allocations_count`              | Total number of allocations     | `integer`    |     |       |                           |
| `allowed_country_state_ids`      | Allowed Country State           | `many2many`  |     |       | res.country.state         |
| `applicant_ids`                  | Applicants                      | `one2many`   |     | ✅    | hr.applicant              |
| `avatar_1024`                    | Avatar 1024                     | `binary`     |     |       |                           |
| `avatar_128`                     | Avatar 128                      | `binary`     |     |       |                           |
| `avatar_1920`                    | Avatar                          | `binary`     |     |       |                           |
| `avatar_256`                     | Avatar 256                      | `binary`     |     |       |                           |
| `avatar_512`                     | Avatar 512                      | `binary`     |     |       |                           |
| `badge_ids`                      | Employee Badges                 | `one2many`   |     |       | gamification.badge.user   |
| `bank_account_ids`               | Bank Accounts                   | `many2many`  |     | ✅    | res.partner.bank          |
| `barcode`                        | Badge ID                        | `char`       |     | ✅    |                           |
| `birthday`                       | Birthday                        | `date`       |     | ✅    |                           |
| `birthday_public_display`        | Show to all employees           | `boolean`    |     | ✅    |                           |
| `birthday_public_display_string` | Public Date of Birth            | `char`       |     |       |                           |
| `car_ids`                        | Vehicles (private)              | `one2many`   |     | ✅    | fleet.vehicle             |
| `category_ids`                   | Tags                            | `many2many`  |     | ✅    | hr.employee.category      |
| `certificate`                    | Certificate Level               | `selection`  |     | ✅    |                           |
| `certification_ids`              | Certification                   | `one2many`   |     |       | hr.employee.skill         |
| `child_all_count`                | Indirect Subordinates Count     | `integer`    |     |       |                           |
| `child_count`                    | Direct Subordinates Count       | `integer`    |     |       |                           |
| `child_ids`                      | Direct subordinates             | `one2many`   |     | ✅    | hr.employee               |
| `children`                       | Dependent Children              | `integer`    |     |       |                           |
| `coach_id`                       | Coach                           | `many2one`   |     | ✅    | hr.employee               |
| `color`                          | Color Index                     | `integer`    |     | ✅    |                           |
| `company_country_code`           | Company Country Code            | `char`       |     |       |                           |
| `company_country_id`             | Company Country                 | `many2one`   |     |       | res.country               |
| `company_id`                     | Company                         | `many2one`   | ✅  | ✅    | res.company               |
| `contract_date_end`              | Contract End Date               | `date`       |     |       |                           |
| `contract_date_start`            | Contract Start Date             | `date`       |     |       |                           |
| `contract_template_id`           | Contract Template               | `many2one`   |     |       | hr.version                |
| `contract_type_id`               | Contract Type                   | `many2one`   |     |       | hr.contract.type          |
| `contract_wage`                  | Contract Wage                   | `monetary`   |     |       |                           |
| `country_code`                   | Country Code                    | `char`       |     |       |                           |
| `country_id`                     | Nationality (Country)           | `many2one`   |     |       | res.country               |
| `country_of_birth`               | Country of Birth                | `many2one`   |     | ✅    | res.country               |
| `create_date`                    | Created on                      | `datetime`   |     | ✅    |                           |
| `create_uid`                     | Created by                      | `many2one`   |     | ✅    | res.users                 |
| `currency_id`                    | Currency                        | `many2one`   |     |       | res.currency              |
| `current_date_version`           | Current Date Version            | `date`       |     |       |                           |
| `current_employee_skill_ids`     | Current Employee Skill          | `one2many`   |     |       | hr.employee.skill         |
| `current_leave_id`               | Current Time Off Type           | `many2one`   |     |       | hr.leave.type             |
| `current_leave_state`            | Current Time Off Status         | `selection`  |     |       |                           |
| `current_version_id`             | Current Version                 | `many2one`   |     | ✅    | hr.version                |
| `date_end`                       | Date End                        | `date`       |     |       |                           |
| `date_start`                     | Date Start                      | `date`       |     |       |                           |
| `date_version`                   | Date Version                    | `date`       | ✅  |       |                           |
| `department_color`               | Department Color                | `integer`    |     |       |                           |
| `department_id`                  | Department                      | `many2one`   |     |       | hr.department             |
| `departure_date`                 | Departure Date                  | `date`       |     |       |                           |
| `departure_description`          | Additional Information          | `html`       |     |       |                           |
| `departure_reason_id`            | Departure Reason                | `many2one`   |     |       | hr.departure.reason       |
| `direct_badge_ids`               | Direct Badge                    | `one2many`   |     | ✅    | gamification.badge.user   |
| `display_certification_page`     | Display Certification Page      | `boolean`    |     |       |                           |
| `display_name`                   | Display Name                    | `char`       |     |       |                           |
| `distance_home_work`             | Home-Work Distance              | `integer`    |     |       |                           |
| `distance_home_work_unit`        | Home-Work Distance unit         | `selection`  | ✅  |       |                           |
| `driving_license`                | Driving License                 | `binary`     |     | ✅    |                           |
| `email`                          | Email                           | `char`       |     |       |                           |
| `emergency_contact`              | Emergency Contact               | `char`       |     | ✅    |                           |
| `emergency_phone`                | Emergency Phone                 | `char`       |     | ✅    |                           |
| `employee_cars_count`            | Cars                            | `integer`    |     |       |                           |
| `employee_id`                    | Employee                        | `many2one`   |     |       | hr.employee               |
| `employee_properties`            | Properties                      | `properties` |     | ✅    |                           |
| `employee_skill_ids`             | Skills                          | `one2many`   |     | ✅    | hr.employee.skill         |
| `employee_type`                  | Employee Type                   | `selection`  | ✅  |       |                           |
| `exceptional_location_id`        | Current                         | `many2one`   |     |       | hr.work.location          |
| `expense_manager_id`             | Expense Approver                | `many2one`   |     | ✅    | res.users                 |
| `filter_for_expense`             | Filter For Expense              | `boolean`    |     |       |                           |
| `friday_location_id`             | Friday                          | `many2one`   |     | ✅    | hr.work.location          |
| `goal_ids`                       | Employee HR Goals               | `one2many`   |     |       | gamification.goal         |
| `has_badges`                     | Has Badges                      | `boolean`    |     |       |                           |
| `has_message`                    | Has Message                     | `boolean`    |     |       |                           |
| `has_multiple_bank_accounts`     | Has Multiple Bank Accounts      | `boolean`    |     |       |                           |
| `has_work_permit`                | Work Permit                     | `binary`     |     | ✅    |                           |
| `hr_icon_display`                | Hr Icon Display                 | `selection`  |     |       |                           |
| `hr_presence_state`              | Hr Presence State               | `selection`  |     |       |                           |
| `hr_responsible_id`              | HR Responsible                  | `many2one`   | ✅  |       | res.users                 |
| `id`                             | ID                              | `integer`    |     | ✅    |                           |
| `id_card`                        | ID Card Copy                    | `binary`     |     | ✅    |                           |
| `identification_id`              | Identification No               | `char`       |     |       |                           |
| `image_1024`                     | Image 1024                      | `binary`     |     | ✅    |                           |
| `image_128`                      | Image 128                       | `binary`     |     | ✅    |                           |
| `image_1920`                     | Image                           | `binary`     |     | ✅    |                           |
| `image_256`                      | Image 256                       | `binary`     |     | ✅    |                           |
| `image_512`                      | Image 512                       | `binary`     |     | ✅    |                           |
| `im_status`                      | IM Status                       | `char`       |     |       |                           |
| `is_absent`                      | Absent Today                    | `boolean`    |     |       |                           |
| `is_current`                     | Is Current                      | `boolean`    |     |       |                           |
| `is_custom_job_title`            | Is Custom Job Title             | `boolean`    |     |       |                           |
| `is_flexible`                    | Is Flexible                     | `boolean`    |     |       |                           |
| `is_fully_flexible`              | Is Fully Flexible               | `boolean`    |     |       |                           |
| `is_future`                      | Is Future                       | `boolean`    |     |       |                           |
| `is_in_contract`                 | Is In Contract                  | `boolean`    |     |       |                           |
| `is_past`                        | Is Past                         | `boolean`    |     |       |                           |
| `is_subordinate`                 | Is Subordinate                  | `boolean`    |     |       |                           |
| `is_trusted_bank_account`        | Is Trusted Bank Account         | `boolean`    |     |       |                           |
| `is_user_active`                 | User's active                   | `boolean`    |     |       |                           |
| `job_id`                         | Job                             | `many2one`   |     |       | hr.job                    |
| `job_title`                      | Job Title                       | `char`       |     |       |                           |
| `km_home_work`                   | Home-Work Distance in Km        | `integer`    |     |       |                           |
| `lang`                           | Lang                            | `selection`  |     | ✅    |                           |
| `last_activity`                  | Last Activity                   | `date`       |     |       |                           |
| `last_activity_time`             | Last Activity Time              | `char`       |     |       |                           |
| `last_modified_date`             | Last Modified on                | `datetime`   | ✅  |       |                           |
| `last_modified_uid`              | Last Modified by                | `many2one`   | ✅  |       | res.users                 |
| `leave_date_from`                | From Date                       | `date`       |     |       |                           |
| `leave_date_to`                  | To Date                         | `date`       |     |       |                           |
| `leave_manager_id`               | Time Off Approver               | `many2one`   |     | ✅    | res.users                 |
| `legal_name`                     | Legal Name                      | `char`       |     | ✅    |                           |
| `license_plate`                  | License Plate                   | `char`       |     |       |                           |
| `marital`                        | Marital Status                  | `selection`  | ✅  |       |                           |
| `member_of_department`           | Member of department            | `boolean`    |     |       |                           |
| `message_attachment_count`       | Attachment Count                | `integer`    |     |       |                           |
| `message_follower_ids`           | Followers                       | `one2many`   |     | ✅    | mail.followers            |
| `message_has_error`              | Message Delivery error          | `boolean`    |     |       |                           |
| `message_has_error_counter`      | Number of errors                | `integer`    |     |       |                           |
| `message_has_sms_error`          | SMS Delivery error              | `boolean`    |     |       |                           |
| `message_ids`                    | Messages                        | `one2many`   |     | ✅    | mail.message              |
| `message_is_follower`            | Is Follower                     | `boolean`    |     |       |                           |
| `message_main_attachment_id`     | Main Attachment                 | `many2one`   |     | ✅    | ir.attachment             |
| `message_needaction`             | Action Needed                   | `boolean`    |     |       |                           |
| `message_needaction_counter`     | Number of Actions               | `integer`    |     |       |                           |
| `message_partner_ids`            | Followers (Partners)            | `many2many`  |     |       | res.partner               |
| `mobile_phone`                   | Work Mobile                     | `char`       |     | ✅    |                           |
| `mobility_card`                  | Mobility Card                   | `char`       |     | ✅    |                           |
| `monday_location_id`             | Monday                          | `many2one`   |     | ✅    | hr.work.location          |
| `my_activity_date_deadline`      | My Activity Deadline            | `date`       |     |       |                           |
| `name`                           | Employee Name                   | `char`       |     | ✅    |                           |
| `newly_hired`                    | Newly Hired                     | `boolean`    |     |       |                           |
| `parent_id`                      | Manager                         | `many2one`   |     | ✅    | hr.employee               |
| `passport_expiration_date`       | Passport Expiration Date        | `date`       |     |       |                           |
| `passport_id`                    | Passport No                     | `char`       |     |       |                           |
| `permit_no`                      | Work Permit No                  | `char`       |     | ✅    |                           |
| `phone`                          | Phone                           | `char`       |     |       |                           |
| `pin`                            | PIN                             | `char`       |     | ✅    |                           |
| `place_of_birth`                 | Place of Birth                  | `char`       |     | ✅    |                           |
| `primary_bank_account_id`        | Primary Bank Account            | `many2one`   |     |       | res.partner.bank          |
| `private_car_plate`              | Private Car Plate               | `char`       |     | ✅    |                           |
| `private_city`                   | Private City                    | `char`       |     |       |                           |
| `private_country_id`             | Private Country                 | `many2one`   |     |       | res.country               |
| `private_email`                  | Private Email                   | `char`       |     | ✅    |                           |
| `private_phone`                  | Private Phone                   | `char`       |     | ✅    |                           |
| `private_state_id`               | Private State                   | `many2one`   |     |       | res.country.state         |
| `private_street`                 | Private Street                  | `char`       |     |       |                           |
| `private_street2`                | Private Street2                 | `char`       |     |       |                           |
| `private_zip`                    | Private Zip                     | `char`       |     |       |                           |
| `rating_ids`                     | Ratings                         | `one2many`   |     | ✅    | rating.rating             |
| `related_partners_count`         | Related Partners Count          | `integer`    |     |       |                           |
| `resource_calendar_id`           | Default Working Hours           | `many2one`   |     |       | resource.calendar         |
| `resource_id`                    | Resource                        | `many2one`   | ✅  | ✅    | resource.resource         |
| `resume_line_ids`                | Resume lines                    | `one2many`   |     | ✅    | hr.resume.line            |
| `salary_distribution`            | Salary Distribution             | `json`       |     | ✅    |                           |
| `saturday_location_id`           | Saturday                        | `many2one`   |     | ✅    | hr.work.location          |
| `sex`                            | Gender                          | `selection`  |     |       |                           |
| `share`                          | Share User                      | `boolean`    |     |       |                           |
| `show_hr_icon_display`           | Show Hr Icon Display            | `boolean`    |     |       |                           |
| `show_leaves`                    | Able to see Remaining Time Off  | `boolean`    |     |       |                           |
| `skill_ids`                      | Skill                           | `many2many`  |     | ✅    | hr.skill                  |
| `spouse_birthdate`               | Spouse Birthdate                | `date`       |     |       |                           |
| `spouse_complete_name`           | Spouse Legal Name               | `char`       |     |       |                           |
| `ssnid`                          | SSN No                          | `char`       |     |       |                           |
| `structure_type_id`              | Salary Structure Type           | `many2one`   |     |       | hr.payroll.structure.type |
| `study_field`                    | Field of Study                  | `char`       |     | ✅    |                           |
| `study_school`                   | School                          | `char`       |     | ✅    |                           |
| `subordinate_ids`                | Subordinates                    | `one2many`   |     |       | hr.employee               |
| `sunday_location_id`             | Sunday                          | `many2one`   |     | ✅    | hr.work.location          |
| `thursday_location_id`           | Thursday                        | `many2one`   |     | ✅    | hr.work.location          |
| `today_location_name`            | Today Location Name             | `char`       |     | ✅    |                           |
| `trial_date_end`                 | End of Trial Period             | `date`       |     |       |                           |
| `tuesday_location_id`            | Tuesday                         | `many2one`   |     | ✅    | hr.work.location          |
| `tz`                             | Timezone                        | `selection`  |     |       |                           |
| `user_id`                        | User                            | `many2one`   |     | ✅    | res.users                 |
| `user_partner_id`                | User's partner                  | `many2one`   |     |       | res.partner               |
| `version_id`                     | Version                         | `many2one`   | ✅  |       | hr.version                |
| `version_ids`                    | Employee Versions               | `one2many`   | ✅  | ✅    | hr.version                |
| `versions_count`                 | Versions Count                  | `integer`    |     |       |                           |
| `visa_expire`                    | Visa Expiration Date            | `date`       |     | ✅    |                           |
| `visa_no`                        | Visa No                         | `char`       |     | ✅    |                           |
| `wage`                           | Wage                            | `monetary`   |     |       |                           |
| `website_message_ids`            | Website Messages                | `one2many`   |     | ✅    | mail.message              |
| `wednesday_location_id`          | Wednesday                       | `many2one`   |     | ✅    | hr.work.location          |
| `work_contact_id`                | Work Contact                    | `many2one`   |     | ✅    | res.partner               |
| `work_email`                     | Work Email                      | `char`       |     | ✅    |                           |
| `work_location_id`               | Work Location                   | `many2one`   |     |       | hr.work.location          |
| `work_location_name`             | Work Location Name              | `char`       |     |       |                           |
| `work_location_type`             | Work Location Type              | `selection`  |     |       |                           |
| `work_permit_expiration_date`    | Work Permit Expiration Date     | `date`       |     | ✅    |                           |
| `work_permit_name`               | work_permit_name                | `char`       |     |       |                           |
| `work_permit_scheduled_activity` | Work Permit Scheduled Activity  | `boolean`    |     | ✅    |                           |
| `work_phone`                     | Work Phone                      | `char`       |     | ✅    |                           |
| `write_date`                     | Last Updated on                 | `datetime`   |     | ✅    |                           |
| `write_uid`                      | Last Updated by                 | `many2one`   |     | ✅    | res.users                 |

**Access Rights:**

| Name                         | Group                                     | Perms     |
| ---------------------------- | ----------------------------------------- | --------- |
| hr.employee user             | Employees / Officer: Manage all employees | `R/W/C/D` |
| name_hr_employee_back_office | OpenEduCat / Manager                      | `R/W/C`   |
| name_hr_employee_student     | OpenEduCat / Manager                      | `R`       |
| hr.employee system user      | Role / Administrator                      | `R`       |

**Record Rules:**

- **Employee multi company rule** (Global) `R/W/C/D`
  - Domain:
    `['|', '|', '|',         ('company_id', 'in', company_ids + [False]),         ('parent_id.user_id', '=', user.id),         ('id', '=', user.employee_id.parent_id.id),         ('user_id', '=', user.id)     ]`
- **HR multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`

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

### 🗃️ `hr.employee.certification.report` — Employee Certification Report

The base model, which is implicitly inherited by all models.

**Fields:**

| Field                           | Label                         | Type       | Req | Store | Relation      |
| ------------------------------- | ----------------------------- | ---------- | --- | ----- | ------------- |
| `active`                        | Active                        | `boolean`  |     | ✅    |               |
| `company_id`                    | Company                       | `many2one` |     | ✅    | res.company   |
| `department_id`                 | Department                    | `many2one` |     | ✅    | hr.department |
| `display_name`                  | Display Name                  | `char`     |     |       |               |
| `employee_id`                   | Employee                      | `many2one` |     | ✅    | hr.employee   |
| `has_department_manager_access` | Has Department Manager Access | `boolean`  |     |       |               |
| `id`                            | ID                            | `integer`  |     | ✅    |               |
| `level_progress`                | Level Progress                | `float`    |     | ✅    |               |
| `skill_id`                      | Skill                         | `many2one` |     | ✅    | hr.skill      |
| `skill_level`                   | Skill Level                   | `char`     |     | ✅    |               |
| `skill_type_id`                 | Skill Type                    | `many2one` |     | ✅    | hr.skill.type |

**Access Rights:**

| Name                             | Group       | Perms |
| -------------------------------- | ----------- | ----- |
| hr.employee.certification.report | Role / User | `R`   |

### 🗃️ `report.hr_skills.report_employee_cv` — Employee Resume

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `hr.employee.skill.report` — Employee Skills Report

The base model, which is implicitly inherited by all models.

**Fields:**

| Field                           | Label                         | Type       | Req | Store | Relation      |
| ------------------------------- | ----------------------------- | ---------- | --- | ----- | ------------- |
| `active`                        | Active                        | `boolean`  |     |       |               |
| `company_id`                    | Company                       | `many2one` |     | ✅    | res.company   |
| `department_id`                 | Department                    | `many2one` |     | ✅    | hr.department |
| `display_name`                  | Display Name                  | `char`     |     |       |               |
| `employee_id`                   | Employee                      | `many2one` |     | ✅    | hr.employee   |
| `has_department_manager_access` | Has Department Manager Access | `boolean`  |     |       |               |
| `id`                            | ID                            | `integer`  |     | ✅    |               |
| `job_id`                        | Job                           | `many2one` |     | ✅    | hr.job        |
| `level_progress`                | Level Progress                | `float`    |     | ✅    |               |
| `skill_id`                      | Skill                         | `many2one` |     | ✅    | hr.skill      |
| `skill_level`                   | Skill Level                   | `char`     |     | ✅    |               |
| `skill_type_id`                 | Skill Type                    | `many2one` |     | ✅    | hr.skill.type |

**Access Rights:**

| Name                     | Group                                     | Perms |
| ------------------------ | ----------------------------------------- | ----- |
| hr.employee.skill.report | Employees / Officer: Manage all employees | `R`   |
| hr.employee.skill.report | Role / User                               | `R`   |

**Record Rules:**

- **Employee Skill Report: HR user** (49) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Employee Skill Report: employee's manager** (1) `R/W/C/D`
  - Domain: `[('has_department_manager_access', '=', True)]`
- **Employee Skill Report: Multi-Company Rule** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `hr.employee.skill.history.report` — Employee Skills Report

The base model, which is implicitly inherited by all models.

**Fields:**

| Field            | Label          | Type       | Req | Store | Relation      |
| ---------------- | -------------- | ---------- | --- | ----- | ------------- |
| `date`           | Date           | `date`     |     | ✅    |               |
| `display_name`   | Display Name   | `char`     |     |       |               |
| `employee_id`    | Employee       | `many2one` |     | ✅    | hr.employee   |
| `id`             | ID             | `integer`  |     | ✅    |               |
| `level_progress` | Level Progress | `float`    |     | ✅    |               |
| `skill_id`       | Skill          | `many2one` |     | ✅    | hr.skill      |
| `skill_type_id`  | Skill Type     | `many2one` |     | ✅    | hr.skill.type |

**Access Rights:**

| Name                             | Group                                     | Perms |
| -------------------------------- | ----------------------------------------- | ----- |
| hr.employee.skill.history.report | Employees / Officer: Manage all employees | `R`   |
| hr.employee.skill.history.report | Role / User                               | `R`   |

**Record Rules:**

- **Employee Skill History Report: HR user** (49) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Employee Skill History Report: employee's manager** (1) `R/W/C/D`
  - Domain: `[('employee_id', 'child_of', user.employee_ids.ids)]`

### 🗃️ `hr.employee.cv.wizard` — Print Resume

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field             | Label               | Type        | Req | Store | Relation    |
| ----------------- | ------------------- | ----------- | --- | ----- | ----------- |
| `can_show_others` | Can Show Others     | `boolean`   |     |       |             |
| `can_show_skills` | Can Show Skills     | `boolean`   |     |       |             |
| `color_primary`   | Primary Color       | `char`      | ✅  | ✅    |             |
| `color_secondary` | Secondary Color     | `char`      | ✅  | ✅    |             |
| `create_date`     | Created on          | `datetime`  |     | ✅    |             |
| `create_uid`      | Created by          | `many2one`  |     | ✅    | res.users   |
| `display_name`    | Display Name        | `char`      |     |       |             |
| `employee_ids`    | Employee            | `many2many` |     | ✅    | hr.employee |
| `id`              | ID                  | `integer`   |     | ✅    |             |
| `show_contact`    | Contact Information | `boolean`   |     | ✅    |             |
| `show_others`     | Others              | `boolean`   |     | ✅    |             |
| `show_skills`     | Skills              | `boolean`   |     | ✅    |             |
| `write_date`      | Last Updated on     | `datetime`  |     | ✅    |             |
| `write_uid`       | Last Updated by     | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                         | Group       | Perms   |
| ---------------------------- | ----------- | ------- |
| access_hr_employee_cv_wizard | Role / User | `R/W/C` |

### 🗃️ `hr.employee.public` — Public Employee

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                          | Type        | Req | Store | Relation                |
| -------------------------------- | ------------------------------ | ----------- | --- | ----- | ----------------------- |
| `active`                         | Active                         | `boolean`   |     | ✅    |                         |
| `address_id`                     | Address                        | `many2one`  |     | ✅    | res.partner             |
| `allocation_display`             | Allocation Display             | `char`      |     |       |                         |
| `allocation_remaining_display`   | Allocation Remaining Display   | `char`      |     |       |                         |
| `avatar_1024`                    | Avatar 1024                    | `binary`    |     |       |                         |
| `avatar_128`                     | Avatar 128                     | `binary`    |     |       |                         |
| `avatar_1920`                    | Avatar                         | `binary`    |     |       |                         |
| `avatar_256`                     | Avatar 256                     | `binary`    |     |       |                         |
| `avatar_512`                     | Avatar 512                     | `binary`    |     |       |                         |
| `badge_ids`                      | Badge                          | `one2many`  |     |       | gamification.badge.user |
| `birthday_public_display_string` | Public Date of Birth           | `char`      |     |       |                         |
| `certification_ids`              | Certification                  | `one2many`  |     |       | hr.employee.skill       |
| `child_all_count`                | Child All Count                | `integer`   |     |       |                         |
| `child_count`                    | Child Count                    | `integer`   |     |       |                         |
| `child_ids`                      | Direct subordinates            | `one2many`  |     | ✅    | hr.employee.public      |
| `coach_id`                       | Coach                          | `many2one`  |     | ✅    | hr.employee.public      |
| `color`                          | Color                          | `integer`   |     | ✅    |                         |
| `company_id`                     | Company                        | `many2one`  |     | ✅    | res.company             |
| `country_code`                   | Country Code                   | `char`      |     |       |                         |
| `create_date`                    | Create Date                    | `datetime`  |     | ✅    |                         |
| `create_uid`                     | Created by                     | `many2one`  |     | ✅    | res.users               |
| `current_employee_skill_ids`     | Current Employee Skill         | `one2many`  |     |       | hr.employee.skill       |
| `department_color`               | Department Color               | `integer`   |     |       |                         |
| `department_id`                  | Department                     | `many2one`  |     | ✅    | hr.department           |
| `display_certification_page`     | Display Certification Page     | `boolean`   |     |       |                         |
| `display_name`                   | Display Name                   | `char`      |     |       |                         |
| `email`                          | Email                          | `char`      |     |       |                         |
| `employee_id`                    | Employee                       | `many2one`  |     | ✅    | hr.employee             |
| `employee_skill_ids`             | Skills                         | `one2many`  |     | ✅    | hr.employee.skill       |
| `expense_manager_id`             | Expense Manager                | `many2one`  |     | ✅    | res.users               |
| `filter_for_expense`             | Filter For Expense             | `boolean`   |     |       |                         |
| `friday_location_id`             | Friday                         | `many2one`  |     | ✅    | hr.work.location        |
| `has_badges`                     | Has Badges                     | `boolean`   |     |       |                         |
| `hr_icon_display`                | Hr Icon Display                | `selection` |     |       |                         |
| `hr_presence_state`              | Hr Presence State              | `selection` |     |       |                         |
| `id`                             | ID                             | `integer`   |     | ✅    |                         |
| `image_1024`                     | Image 1024                     | `binary`    |     |       |                         |
| `image_128`                      | Image 128                      | `binary`    |     |       |                         |
| `image_1920`                     | Image                          | `binary`    |     |       |                         |
| `image_256`                      | Image 256                      | `binary`    |     |       |                         |
| `image_512`                      | Image 512                      | `binary`    |     |       |                         |
| `im_status`                      | IM Status                      | `char`      |     |       |                         |
| `is_absent`                      | Absent Today                   | `boolean`   |     |       |                         |
| `is_manager`                     | Is Manager                     | `boolean`   |     |       |                         |
| `is_subordinate`                 | Is Subordinate                 | `boolean`   |     |       |                         |
| `is_user`                        | Is User                        | `boolean`   |     |       |                         |
| `job_id`                         | Job                            | `many2one`  |     | ✅    | hr.job                  |
| `job_title`                      | Job Title                      | `char`      |     |       |                         |
| `last_activity`                  | Last Activity                  | `date`      |     |       |                         |
| `last_activity_time`             | Last Activity Time             | `char`      |     |       |                         |
| `leave_date_to`                  | To Date                        | `date`      |     |       |                         |
| `leave_manager_id`               | Time Off Approver              | `many2one`  |     | ✅    | res.users               |
| `member_of_department`           | Member Of Department           | `boolean`   |     |       |                         |
| `mobile_phone`                   | Mobile Phone                   | `char`      |     | ✅    |                         |
| `mobility_card`                  | Mobility Card                  | `char`      |     | ✅    |                         |
| `monday_location_id`             | Monday                         | `many2one`  |     | ✅    | hr.work.location        |
| `name`                           | Name                           | `char`      |     | ✅    |                         |
| `newly_hired`                    | Newly Hired                    | `boolean`   |     |       |                         |
| `parent_id`                      | Manager                        | `many2one`  |     | ✅    | hr.employee.public      |
| `phone`                          | Phone                          | `char`      |     |       |                         |
| `resource_calendar_id`           | Resource Calendar              | `many2one`  |     | ✅    | resource.calendar       |
| `resource_id`                    | Resource                       | `many2one`  |     | ✅    | resource.resource       |
| `resume_line_ids`                | Resume lines                   | `one2many`  |     | ✅    | hr.resume.line          |
| `saturday_location_id`           | Saturday                       | `many2one`  |     | ✅    | hr.work.location        |
| `share`                          | Share User                     | `boolean`   |     |       |                         |
| `show_hr_icon_display`           | Show Hr Icon Display           | `boolean`   |     |       |                         |
| `show_leaves`                    | Able to see Remaining Time Off | `boolean`   |     |       |                         |
| `subordinate_ids`                | Subordinates                   | `one2many`  |     |       | hr.employee             |
| `sunday_location_id`             | Sunday                         | `many2one`  |     | ✅    | hr.work.location        |
| `thursday_location_id`           | Thursday                       | `many2one`  |     | ✅    | hr.work.location        |
| `today_location_name`            | Today Location Name            | `char`      |     | ✅    |                         |
| `tuesday_location_id`            | Tuesday                        | `many2one`  |     | ✅    | hr.work.location        |
| `tz`                             | Timezone                       | `selection` |     |       |                         |
| `user_id`                        | User                           | `many2one`  |     | ✅    | res.users               |
| `user_partner_id`                | User's partner                 | `many2one`  |     |       | res.partner             |
| `wednesday_location_id`          | Wednesday                      | `many2one`  |     | ✅    | hr.work.location        |
| `work_contact_id`                | Work Contact                   | `many2one`  |     | ✅    | res.partner             |
| `work_email`                     | Work Email                     | `char`      |     | ✅    |                         |
| `work_location_id`               | Work Location                  | `many2one`  |     | ✅    | hr.work.location        |
| `work_location_name`             | Work Location Name             | `char`      |     |       |                         |
| `work_location_type`             | Work Location Type             | `selection` |     |       |                         |
| `work_phone`                     | Work Phone                     | `char`      |     | ✅    |                         |
| `write_date`                     | Last Updated on                | `datetime`  |     | ✅    |                         |
| `write_uid`                      | Last Updated by                | `many2one`  |     | ✅    | res.users               |

**Access Rights:**

| Name               | Group       | Perms |
| ------------------ | ----------- | ----- |
| hr.employee_public | Role / User | `R`   |

**Record Rules:**

- **Employee multi company rule** (Global) `R/W/C/D`
  - Domain:
    `['|', '|', '|',         ('company_id', 'in', company_ids + [False]),         ('parent_id.user_id', '=', user.id),         ('id', '=', user.employee_id.parent_id.id),         ('user_id', '=', user.id)     ]`

### 🗃️ `resource.resource` — Resources

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label                | Type        | Req | Store | Relation          |
| ---------------------- | -------------------- | ----------- | --- | ----- | ----------------- |
| `active`               | Active               | `boolean`   |     | ✅    |                   |
| `avatar_128`           | Avatar 128           | `binary`    |     |       |                   |
| `calendar_id`          | Working Time         | `many2one`  |     | ✅    | resource.calendar |
| `color`                | Color                | `integer`   |     | ✅    |                   |
| `company_id`           | Company              | `many2one`  |     | ✅    | res.company       |
| `create_date`          | Created on           | `datetime`  |     | ✅    |                   |
| `create_uid`           | Created by           | `many2one`  |     | ✅    | res.users         |
| `department_id`        | Department           | `many2one`  |     |       | hr.department     |
| `display_name`         | Display Name         | `char`      |     |       |                   |
| `email`                | Email                | `char`      |     |       |                   |
| `employee_id`          | Employee             | `one2many`  |     | ✅    | hr.employee       |
| `employee_skill_ids`   | Skills               | `one2many`  |     |       | hr.employee.skill |
| `hr_icon_display`      | Hr Icon Display      | `selection` |     |       |                   |
| `id`                   | ID                   | `integer`   |     | ✅    |                   |
| `im_status`            | IM Status            | `char`      |     |       |                   |
| `job_title`            | Job Title            | `char`      |     |       |                   |
| `leave_date_to`        | To Date              | `date`      |     |       |                   |
| `name`                 | Name                 | `char`      | ✅  | ✅    |                   |
| `phone`                | Phone                | `char`      |     |       |                   |
| `resource_type`        | Type                 | `selection` | ✅  | ✅    |                   |
| `share`                | Share User           | `boolean`   |     |       |                   |
| `show_hr_icon_display` | Show Hr Icon Display | `boolean`   |     |       |                   |
| `time_efficiency`      | Efficiency Factor    | `float`     | ✅  | ✅    |                   |
| `tz`                   | Timezone             | `selection` | ✅  | ✅    |                   |
| `user_id`              | User                 | `many2one`  |     | ✅    | res.users         |
| `work_email`           | Work Email           | `char`      |     |       |                   |
| `work_location_id`     | Work Location        | `many2one`  |     |       | hr.work.location  |
| `work_phone`           | Work Phone           | `char`      |     |       |                   |
| `write_date`           | Last Updated on      | `datetime`  |     | ✅    |                   |
| `write_uid`            | Last Updated by      | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                                     | Group                                     | Perms     |
| ---------------------------------------- | ----------------------------------------- | --------- |
| resource.resource.user                   | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.employee.resource.manager             | Employees / Administrator                 | `R/W/C/D` |
| name_resource_resource_back_office_admin | OpenEduCat / Manager                      | `R/W/C`   |
| resource.resource                        | Role / Administrator                      | `R`       |
| resource.resource all                    | Role / User                               | `R`       |

**Record Rules:**

- **resource.resource multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

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

### 🗃️ `hr.skill` — Skill

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field           | Label           | Type       | Req | Store | Relation      |
| --------------- | --------------- | ---------- | --- | ----- | ------------- |
| `color`         | Color           | `integer`  |     |       |               |
| `create_date`   | Created on      | `datetime` |     | ✅    |               |
| `create_uid`    | Created by      | `many2one` |     | ✅    | res.users     |
| `display_name`  | Display Name    | `char`     |     |       |               |
| `id`            | ID              | `integer`  |     | ✅    |               |
| `name`          | Name            | `char`     | ✅  | ✅    |               |
| `sequence`      | Sequence        | `integer`  |     | ✅    |               |
| `skill_type_id` | Skill Type      | `many2one` | ✅  | ✅    | hr.skill.type |
| `write_date`    | Last Updated on | `datetime` |     | ✅    |               |
| `write_uid`     | Last Updated by | `many2one` |     | ✅    | res.users     |

**Access Rights:**

| Name              | Group                                     | Perms     |
| ----------------- | ----------------------------------------- | --------- |
| hr.skill          | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.skill.employee | Role / User                               | `R/C`     |

### 🗃️ `hr.individual.skill.mixin` — Skill level

The base model, which is implicitly inherited by all models.

**Fields:**

| Field                            | Label                          | Type       | Req | Store | Relation       |
| -------------------------------- | ------------------------------ | ---------- | --- | ----- | -------------- |
| `certification_skill_type_count` | Certification Skill Type Count | `integer`  |     |       |                |
| `color`                          | Color                          | `integer`  |     |       |                |
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

### 🗃️ `hr.skill.level` — Skill Level

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label                    | Type       | Req | Store | Relation      |
| -------------------------- | ------------------------ | ---------- | --- | ----- | ------------- |
| `create_date`              | Created on               | `datetime` |     | ✅    |               |
| `create_uid`               | Created by               | `many2one` |     | ✅    | res.users     |
| `default_level`            | Default Level            | `boolean`  |     | ✅    |               |
| `display_name`             | Display Name             | `char`     |     |       |               |
| `id`                       | ID                       | `integer`  |     | ✅    |               |
| `level_progress`           | Progress                 | `integer`  |     | ✅    |               |
| `name`                     | Name                     | `char`     | ✅  | ✅    |               |
| `skill_type_id`            | Skill Type               | `many2one` |     | ✅    | hr.skill.type |
| `technical_is_new_default` | Technical Is New Default | `boolean`  |     |       |               |
| `write_date`               | Last Updated on          | `datetime` |     | ✅    |               |
| `write_uid`                | Last Updated by          | `many2one` |     | ✅    | res.users     |

**Access Rights:**

| Name                    | Group                                     | Perms     |
| ----------------------- | ----------------------------------------- | --------- |
| hr.skill.level          | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.skill.level.employee | Role / User                               | `R`       |

### 🗃️ `hr.employee.skill` — Skill level for employee

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                          | Type       | Req | Store | Relation       |
| -------------------------------- | ------------------------------ | ---------- | --- | ----- | -------------- |
| `certification_skill_type_count` | Certification Skill Type Count | `integer`  |     |       |                |
| `color`                          | Color                          | `integer`  |     |       |                |
| `create_date`                    | Created on                     | `datetime` |     | ✅    |                |
| `create_uid`                     | Created by                     | `many2one` |     | ✅    | res.users      |
| `display_name`                   | Display Name                   | `char`     |     |       |                |
| `display_warning_message`        | Display Warning Message        | `boolean`  |     | ✅    |                |
| `employee_id`                    | Employee                       | `many2one` | ✅  | ✅    | hr.employee    |
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

| Name              | Group                                     | Perms     |
| ----------------- | ----------------------------------------- | --------- |
| hr.employee.skill | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.employee.skill | Role / User                               | `R/W/C/D` |

**Record Rules:**

- **Employee skill: employee: read all** (1) `R`
  - Domain: `[(1, '=', 1)]`
- **Employee skill: HR user: read all** (49) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Employee skill: employee: create/write/unlink own** (1) `W/C/D`
  - Domain: `[('employee_id.user_id','=',user.id)]`

### 🗃️ `hr.job.skill` — Skills for job positions

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                          | Type       | Req | Store | Relation       |
| -------------------------------- | ------------------------------ | ---------- | --- | ----- | -------------- |
| `certification_skill_type_count` | Certification Skill Type Count | `integer`  |     |       |                |
| `color`                          | Color                          | `integer`  |     |       |                |
| `create_date`                    | Created on                     | `datetime` |     | ✅    |                |
| `create_uid`                     | Created by                     | `many2one` |     | ✅    | res.users      |
| `display_name`                   | Display Name                   | `char`     |     |       |                |
| `display_warning_message`        | Display Warning Message        | `boolean`  |     | ✅    |                |
| `id`                             | ID                             | `integer`  |     | ✅    |                |
| `is_certification`               | Certification                  | `boolean`  |     |       |                |
| `job_id`                         | Job                            | `many2one` | ✅  | ✅    | hr.job         |
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

| Name                          | Group                                        | Perms     |
| ----------------------------- | -------------------------------------------- | --------- |
| hr.job.skill                  | Employees / Officer: Manage all employees    | `R/W/C/D` |
| hr.job.skill.recruitment.user | Recruitment / Officer: Manage all applicants | `R/W/C/D` |
| hr.job.skill.employee         | Role / User                                  | `R`       |

### 🗃️ `hr.skill.type` — Skill Type

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field              | Label           | Type       | Req | Store | Relation       |
| ------------------ | --------------- | ---------- | --- | ----- | -------------- |
| `active`           | Active          | `boolean`  |     | ✅    |                |
| `color`            | Color           | `integer`  |     | ✅    |                |
| `create_date`      | Created on      | `datetime` |     | ✅    |                |
| `create_uid`       | Created by      | `many2one` |     | ✅    | res.users      |
| `display_name`     | Display Name    | `char`     |     |       |                |
| `id`               | ID              | `integer`  |     | ✅    |                |
| `is_certification` | Certification   | `boolean`  |     | ✅    |                |
| `levels_count`     | Levels Count    | `integer`  |     | ✅    |                |
| `name`             | Name            | `char`     | ✅  | ✅    |                |
| `sequence`         | Sequence        | `integer`  |     | ✅    |                |
| `skill_ids`        | Skills          | `one2many` |     | ✅    | hr.skill       |
| `skill_level_ids`  | Levels          | `one2many` |     | ✅    | hr.skill.level |
| `write_date`       | Last Updated on | `datetime` |     | ✅    |                |
| `write_uid`        | Last Updated by | `many2one` |     | ✅    | res.users      |

**Access Rights:**

| Name                   | Group                                     | Perms     |
| ---------------------- | ----------------------------------------- | --------- |
| hr.skill.type          | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.skill.type.employee | Role / User                               | `R`       |

### 🗃️ `hr.resume.line.type` — Type of a resume line

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                    | Label               | Type                    | Req | Store | Relation  |
| ---------------------------------------- | ------------------- | ----------------------- | --- | ----- | --------- |
| `create_date`                            | Created on          | `datetime`              |     | ✅    |           |
| `create_uid`                             | Created by          | `many2one`              |     | ✅    | res.users |
| `display_name`                           | Display Name        | `char`                  |     |       |           |
| `id`                                     | ID                  | `integer`               |     | ✅    |           |
| `is_course`                              | Course              | `boolean`               |     | ✅    |           |
| `name`                                   | Name                | `char`                  | ✅  | ✅    |           |
| `resume_line_type_properties_definition` | Sections Properties | `properties_definition` |     | ✅    |           |
| `sequence`                               | Sequence            | `integer`               |     | ✅    |           |
| `write_date`                             | Last Updated on     | `datetime`              |     | ✅    |           |
| `write_uid`                              | Last Updated by     | `many2one`              |     | ✅    | res.users |

**Access Rights:**

| Name                         | Group                                     | Perms     |
| ---------------------------- | ----------------------------------------- | --------- |
| hr.resume.line.type          | Employees / Officer: Manage all employees | `R/W/C/D` |
| hr.resume.line.type.employee | Role / User                               | `R`       |
