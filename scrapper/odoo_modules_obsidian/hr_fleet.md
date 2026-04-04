---
title: "Fleet History"
module: "hr_fleet"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Human Resources"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_______________]
---

# 🟢 Fleet History

> **Module:** `hr_fleet` | **Version:** `19.0.1.0` **Category:** Human Resources |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[hr]] [[fleet]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT fleet.vehicle list (list)`
- `* INHERIT fleet.vehicle.assignation.log.view.list.inherit.hr.fleet (list)`
- `* INHERIT fleet.vehicle.assignation.log.view.list.inherit.hr.fleet (list)`
- `* INHERIT fleet.vehicle.form.inherit.hr (form)`
- `* INHERIT fleet.vehicle.log.contract.form.inherit.hr (form)`
- `* INHERIT fleet.vehicle.log.contract.form.inherit.hr (form)`
- `* INHERIT fleet.vehicle.log.contract.list.inherit.hr (list)`
- `* INHERIT fleet.vehicle.log.contract.search.inherit.hr (search)`
- `* INHERIT fleet.vehicle.log.services.kanban.inherit.hr (kanban)`
- `* INHERIT fleet.vehicle.log.services.list.inherit.hr (list)`
- `* INHERIT fleet.vehicle.odometer.view.list.inherit.hr.fleet (list)`
- `* INHERIT fleet.vehicle.search.inherit.hr (search)`
- `* INHERIT hr.departure.wizard.view.form.extend2 (form)`
- `* INHERIT hr.employee.filter.inherit.hr.fleet (search)`
- `* INHERIT hr.employee.form.inherit.hr.fleet (form)`
- `* INHERIT ir.attachment.kanban.inherit.hr (kanban)`

### Reports

_none_

## 🛠️ Technical Documentation

**10 model(s) defined by this module:**

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

### 🗃️ `fleet.vehicle.log.services` — Services for vehicles

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type        | Req | Store | Relation                  |
| ------------------------------- | ----------------------------- | ----------- | --- | ----- | ------------------------- |
| `account_move_line_id`          | Account Move Line             | `many2one`  |     | ✅    | account.move.line         |
| `account_move_state`            | Status                        | `selection` |     |       |                           |
| `active`                        | Active                        | `boolean`   |     | ✅    |                           |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event            |
| `activity_date_deadline`        | Next Activity Deadline        | `date`      |     |       |                           |
| `activity_exception_decoration` | Activity Exception Decoration | `selection` |     |       |                           |
| `activity_exception_icon`       | Icon                          | `char`      |     |       |                           |
| `activity_ids`                  | Activities                    | `one2many`  |     | ✅    | mail.activity             |
| `activity_state`                | Activity State                | `selection` |     |       |                           |
| `activity_summary`              | Next Activity Summary         | `char`      |     |       |                           |
| `activity_type_icon`            | Activity Type Icon            | `char`      |     |       |                           |
| `activity_type_id`              | Next Activity Type            | `many2one`  |     |       | mail.activity.type        |
| `activity_user_id`              | Responsible User              | `many2one`  |     |       | res.users                 |
| `amount`                        | Cost                          | `monetary`  |     | ✅    |                           |
| `brand_id`                      | Brand                         | `many2one`  |     | ✅    | fleet.vehicle.model.brand |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company               |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                           |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users                 |
| `currency_id`                   | Currency                      | `many2one`  |     |       | res.currency              |
| `date`                          | Date                          | `date`      |     | ✅    |                           |
| `description`                   | Description                   | `char`      |     | ✅    |                           |
| `display_name`                  | Display Name                  | `char`      |     |       |                           |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                           |
| `id`                            | ID                            | `integer`   |     | ✅    |                           |
| `inv_ref`                       | Vendor Reference              | `char`      |     | ✅    |                           |
| `manager_id`                    | Fleet Manager                 | `many2one`  |     | ✅    | res.users                 |
| `message_attachment_count`      | Attachment Count              | `integer`   |     |       |                           |
| `message_follower_ids`          | Followers                     | `one2many`  |     | ✅    | mail.followers            |
| `message_has_error`             | Message Delivery error        | `boolean`   |     |       |                           |
| `message_has_error_counter`     | Number of errors              | `integer`   |     |       |                           |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`   |     |       |                           |
| `message_ids`                   | Messages                      | `one2many`  |     | ✅    | mail.message              |
| `message_is_follower`           | Is Follower                   | `boolean`   |     |       |                           |
| `message_needaction`            | Action Needed                 | `boolean`   |     |       |                           |
| `message_needaction_counter`    | Number of Actions             | `integer`   |     |       |                           |
| `message_partner_ids`           | Followers (Partners)          | `many2many` |     |       | res.partner               |
| `model_id`                      | Model                         | `many2one`  |     | ✅    | fleet.vehicle.model       |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`      |     |       |                           |
| `notes`                         | Notes                         | `text`      |     | ✅    |                           |
| `odometer`                      | Odometer Value                | `float`     |     |       |                           |
| `odometer_id`                   | Odometer                      | `many2one`  |     | ✅    | fleet.vehicle.odometer    |
| `odometer_unit`                 | Unit                          | `selection` |     |       |                           |
| `purchaser_employee_id`         | Driver (Employee)             | `many2one`  |     | ✅    | hr.employee               |
| `purchaser_id`                  | Driver                        | `many2one`  |     | ✅    | res.partner               |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating             |
| `service_type_id`               | Service Type                  | `many2one`  | ✅  | ✅    | fleet.service.type        |
| `state`                         | Stage                         | `selection` |     | ✅    |                           |
| `vehicle_id`                    | Vehicle                       | `many2one`  | ✅  | ✅    | fleet.vehicle             |
| `vendor_id`                     | Vendor                        | `many2one`  |     | ✅    | res.partner               |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message              |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                           |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name                                    | Group                                | Perms     |
| --------------------------------------- | ------------------------------------ | --------- |
| fleet_vehicle_log_services_access_right | Fleet / Officer: Manage all vehicles | `R`       |
| fleet_vehicle_log_services_access_right | Fleet / Administrator                | `R/W/C/D` |

**Record Rules:**

- **Administrator has all rights on vehicle's services** (21) `R/W/C/D`
- **Fleet log services: Multi Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `fleet.vehicle` — Vehicle

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                           | Label                         | Type         | Req | Store | Relation                      |
| ------------------------------- | ----------------------------- | ------------ | --- | ----- | ----------------------------- |
| `account_move_ids`              | Account Move                  | `one2many`   |     |       | account.move                  |
| `acquisition_date`              | Registration Date             | `date`       |     | ✅    |                               |
| `active`                        | Active                        | `boolean`    |     | ✅    |                               |
| `activity_calendar_event_id`    | Next Activity Calendar Event  | `many2one`   |     |       | calendar.event                |
| `activity_date_deadline`        | Next Activity Deadline        | `date`       |     |       |                               |
| `activity_exception_decoration` | Activity Exception Decoration | `selection`  |     |       |                               |
| `activity_exception_icon`       | Icon                          | `char`       |     |       |                               |
| `activity_ids`                  | Activities                    | `one2many`   |     | ✅    | mail.activity                 |
| `activity_state`                | Activity State                | `selection`  |     |       |                               |
| `activity_summary`              | Next Activity Summary         | `char`       |     |       |                               |
| `activity_type_icon`            | Activity Type Icon            | `char`       |     |       |                               |
| `activity_type_id`              | Next Activity Type            | `many2one`   |     |       | mail.activity.type            |
| `activity_user_id`              | Responsible User              | `many2one`   |     |       | res.users                     |
| `avatar_1024`                   | Avatar 1024                   | `binary`     |     |       |                               |
| `avatar_128`                    | Avatar 128                    | `binary`     |     |       |                               |
| `avatar_1920`                   | Avatar                        | `binary`     |     |       |                               |
| `avatar_256`                    | Avatar 256                    | `binary`     |     |       |                               |
| `avatar_512`                    | Avatar 512                    | `binary`     |     |       |                               |
| `bill_count`                    | Bills Count                   | `integer`    |     |       |                               |
| `brand_id`                      | Brand                         | `many2one`   |     | ✅    | fleet.vehicle.model.brand     |
| `car_value`                     | Catalog Value (VAT Incl.)     | `float`      |     | ✅    |                               |
| `category_id`                   | Category                      | `many2one`   |     | ✅    | fleet.vehicle.model.category  |
| `co2`                           | CO₂ Emissions                 | `float`      |     | ✅    |                               |
| `co2_emission_unit`             | Co2 Emission Unit             | `selection`  | ✅  | ✅    |                               |
| `co2_standard`                  | Emission Standard             | `char`       |     | ✅    |                               |
| `color`                         | Color                         | `char`       |     | ✅    |                               |
| `company_id`                    | Company                       | `many2one`   |     | ✅    | res.company                   |
| `contract_count`                | Contract Count                | `integer`    |     |       |                               |
| `contract_date_start`           | First Contract Date           | `date`       |     | ✅    |                               |
| `contract_renewal_due_soon`     | Has Contracts to renew        | `boolean`    |     |       |                               |
| `contract_renewal_overdue`      | Has Contracts Overdue         | `boolean`    |     |       |                               |
| `contract_state`                | Last Contract State           | `selection`  |     |       |                               |
| `country_code`                  | Country Code                  | `char`       |     |       |                               |
| `country_id`                    | Country                       | `many2one`   |     |       | res.country                   |
| `create_date`                   | Created on                    | `datetime`   |     | ✅    |                               |
| `create_uid`                    | Created by                    | `many2one`   |     | ✅    | res.users                     |
| `currency_id`                   | Currency                      | `many2one`   |     |       | res.currency                  |
| `description`                   | Vehicle Description           | `html`       |     | ✅    |                               |
| `display_name`                  | Display Name                  | `char`       |     |       |                               |
| `doors`                         | Number of Doors               | `integer`    |     | ✅    |                               |
| `driver_employee_id`            | Driver (Employee)             | `many2one`   |     | ✅    | hr.employee                   |
| `driver_employee_name`          | Employee Name                 | `char`       |     |       |                               |
| `driver_id`                     | Driver                        | `many2one`   |     | ✅    | res.partner                   |
| `electric_assistance`           | Electric Assistance           | `boolean`    |     | ✅    |                               |
| `frame_size`                    | Frame Size                    | `float`      |     | ✅    |                               |
| `frame_type`                    | Bike Frame Type               | `selection`  |     | ✅    |                               |
| `fuel_type`                     | Fuel Type                     | `selection`  |     | ✅    |                               |
| `future_driver_employee_id`     | Future Driver (Employee)      | `many2one`   |     | ✅    | hr.employee                   |
| `future_driver_id`              | Future Driver                 | `many2one`   |     | ✅    | res.partner                   |
| `has_message`                   | Has Message                   | `boolean`    |     |       |                               |
| `history_count`                 | Drivers History Count         | `integer`    |     |       |                               |
| `horsepower`                    | Horsepower                    | `float`      |     | ✅    |                               |
| `horsepower_tax`                | Horsepower Taxation           | `float`      |     | ✅    |                               |
| `id`                            | ID                            | `integer`    |     | ✅    |                               |
| `image_1024`                    | Image 1024                    | `binary`     |     | ✅    |                               |
| `image_128`                     | Image 128                     | `binary`     |     | ✅    |                               |
| `image_1920`                    | Image                         | `binary`     |     | ✅    |                               |
| `image_256`                     | Image 256                     | `binary`     |     | ✅    |                               |
| `image_512`                     | Image 512                     | `binary`     |     | ✅    |                               |
| `license_plate`                 | License Plate                 | `char`       |     | ✅    |                               |
| `location`                      | Location                      | `char`       |     | ✅    |                               |
| `log_contracts`                 | Contracts                     | `one2many`   |     | ✅    | fleet.vehicle.log.contract    |
| `log_drivers`                   | Assignment Logs               | `one2many`   |     | ✅    | fleet.vehicle.assignation.log |
| `log_services`                  | Services Logs                 | `one2many`   |     | ✅    | fleet.vehicle.log.services    |
| `manager_id`                    | Fleet Manager                 | `many2one`   |     | ✅    | res.users                     |
| `message_attachment_count`      | Attachment Count              | `integer`    |     |       |                               |
| `message_follower_ids`          | Followers                     | `one2many`   |     | ✅    | mail.followers                |
| `message_has_error`             | Message Delivery error        | `boolean`    |     |       |                               |
| `message_has_error_counter`     | Number of errors              | `integer`    |     |       |                               |
| `message_has_sms_error`         | SMS Delivery error            | `boolean`    |     |       |                               |
| `message_ids`                   | Messages                      | `one2many`   |     | ✅    | mail.message                  |
| `message_is_follower`           | Is Follower                   | `boolean`    |     |       |                               |
| `message_needaction`            | Action Needed                 | `boolean`    |     |       |                               |
| `message_needaction_counter`    | Number of Actions             | `integer`    |     |       |                               |
| `message_partner_ids`           | Followers (Partners)          | `many2many`  |     |       | res.partner                   |
| `mobility_card`                 | Mobility Card                 | `char`       |     | ✅    |                               |
| `model_id`                      | Model                         | `many2one`   | ✅  | ✅    | fleet.vehicle.model           |
| `model_year`                    | Model Year                    | `selection`  |     | ✅    |                               |
| `my_activity_date_deadline`     | My Activity Deadline          | `date`       |     |       |                               |
| `name`                          | Name                          | `char`       |     | ✅    |                               |
| `net_car_value`                 | Purchase Value                | `float`      |     | ✅    |                               |
| `next_assignation_date`         | Assignment Date               | `date`       |     | ✅    |                               |
| `odometer`                      | Last Odometer                 | `float`      |     |       |                               |
| `odometer_count`                | Odometer                      | `integer`    |     |       |                               |
| `odometer_unit`                 | Odometer Unit                 | `selection`  | ✅  | ✅    |                               |
| `order_date`                    | Order Date                    | `date`       |     | ✅    |                               |
| `plan_to_change_bike`           | Plan To Change Bike           | `boolean`    |     | ✅    |                               |
| `plan_to_change_car`            | Plan To Change Car            | `boolean`    |     | ✅    |                               |
| `power`                         | Power                         | `float`      |     | ✅    |                               |
| `power_unit`                    | Power Unit                    | `selection`  | ✅  | ✅    |                               |
| `range_unit`                    | Range Unit                    | `selection`  | ✅  | ✅    |                               |
| `rating_ids`                    | Ratings                       | `one2many`   |     | ✅    | rating.rating                 |
| `residual_value`                | Residual Value                | `float`      |     | ✅    |                               |
| `seats`                         | Seating Capacity              | `integer`    |     | ✅    |                               |
| `service_activity`              | Service Activity              | `selection`  |     |       |                               |
| `service_count`                 | Services                      | `integer`    |     |       |                               |
| `state_id`                      | State                         | `many2one`   |     | ✅    | fleet.vehicle.state           |
| `tag_ids`                       | Tags                          | `many2many`  |     | ✅    | fleet.vehicle.tag             |
| `trailer_hook`                  | Trailer Hitch                 | `boolean`    |     | ✅    |                               |
| `transmission`                  | Transmission                  | `selection`  |     | ✅    |                               |
| `vehicle_properties`            | Properties                    | `properties` |     | ✅    |                               |
| `vehicle_range`                 | Range                         | `integer`    |     | ✅    |                               |
| `vehicle_type`                  | Vehicle Type                  | `selection`  |     |       |                               |
| `vin_sn`                        | Chassis Number                | `char`       |     | ✅    |                               |
| `website_message_ids`           | Website Messages              | `one2many`   |     | ✅    | mail.message                  |
| `write_date`                    | Last Updated on               | `datetime`   |     | ✅    |                               |
| `write_off_date`                | Cancellation Date             | `date`       |     | ✅    |                               |
| `write_uid`                     | Last Updated by               | `many2one`   |     | ✅    | res.users                     |

**Access Rights:**

| Name                                     | Group                                     | Perms     |
| ---------------------------------------- | ----------------------------------------- | --------- |
| hr_fleet_vehicle_access_right_hr_officer | Employees / Officer: Manage all employees | `R`       |
| fleet_vehicle_access_right               | Fleet / Officer: Manage all vehicles      | `R/W/C/D` |
| fleet_vehicle_access_right               | Fleet / Administrator                     | `R/W/C/D` |
| name_fleet_vehicle_transport_user        | Transportation Privilege / User           | `R`       |

**Record Rules:**

- **Administrator has all rights on vehicle** (21) `R/W/C/D`
- **Fleet vehicle: Multi Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`
- **Hr Officer read rights on vehicle with employees assigned** (49) `R`
  - Domain:
    `['|', ('driver_employee_id', '!=', False), ('future_driver_employee_id', '!=', False)]`

### 🗃️ `fleet.vehicle.log.contract` — Vehicle Contract

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
| `amount`                        | Cost                          | `monetary`  |     | ✅    |                    |
| `company_id`                    | Company                       | `many2one`  |     | ✅    | res.company        |
| `cost_frequency`                | Recurring Cost Frequency      | `selection` | ✅  | ✅    |                    |
| `cost_generated`                | Recurring Cost                | `monetary`  |     | ✅    |                    |
| `cost_subtype_id`               | Type                          | `many2one`  |     | ✅    | fleet.service.type |
| `create_date`                   | Created on                    | `datetime`  |     | ✅    |                    |
| `create_uid`                    | Created by                    | `many2one`  |     | ✅    | res.users          |
| `currency_id`                   | Currency                      | `many2one`  |     |       | res.currency       |
| `date`                          | Date                          | `date`      |     | ✅    |                    |
| `days_left`                     | Warning Date                  | `integer`   |     |       |                    |
| `display_name`                  | Display Name                  | `char`      |     |       |                    |
| `expiration_date`               | Contract Expiration Date      | `date`      |     | ✅    |                    |
| `expires_today`                 | Expires Today                 | `boolean`   |     |       |                    |
| `has_message`                   | Has Message                   | `boolean`   |     |       |                    |
| `has_open_contract`             | Has Open Contract             | `boolean`   |     |       |                    |
| `id`                            | ID                            | `integer`   |     | ✅    |                    |
| `ins_ref`                       | Reference                     | `char`      |     | ✅    |                    |
| `insurer_id`                    | Vendor                        | `many2one`  |     | ✅    | res.partner        |
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
| `name`                          | Name                          | `char`      |     | ✅    |                    |
| `notes`                         | Terms and Conditions          | `html`      |     | ✅    |                    |
| `purchaser_employee_id`         | Driver (Employee)             | `many2one`  |     |       | hr.employee        |
| `purchaser_id`                  | Driver                        | `many2one`  |     |       | res.partner        |
| `rating_ids`                    | Ratings                       | `one2many`  |     | ✅    | rating.rating      |
| `service_ids`                   | Included Services             | `many2many` |     | ✅    | fleet.service.type |
| `start_date`                    | Contract Start Date           | `date`      |     | ✅    |                    |
| `state`                         | Status                        | `selection` |     | ✅    |                    |
| `user_id`                       | Responsible                   | `many2one`  |     | ✅    | res.users          |
| `vehicle_id`                    | Vehicle                       | `many2one`  | ✅  | ✅    | fleet.vehicle      |
| `website_message_ids`           | Website Messages              | `one2many`  |     | ✅    | mail.message       |
| `write_date`                    | Last Updated on               | `datetime`  |     | ✅    |                    |
| `write_uid`                     | Last Updated by               | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                    | Group                                | Perms     |
| --------------------------------------- | ------------------------------------ | --------- |
| fleet_vehicle_log_contract_access_right | Fleet / Officer: Manage all vehicles | `R/W/C/D` |
| fleet_vehicle_log_contract_access_right | Fleet / Administrator                | `R/W/C/D` |

**Record Rules:**

- **Administrator has all rights on vehicle's contracts** (21) `R/W/C/D`
- **Fleet vehicle log contract: Multi Company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids + [False])]`

### 🗃️ `mail.activity.plan.template` — Activity plan template

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label           | Type        | Req | Store | Relation           |
| ------------------- | --------------- | ----------- | --- | ----- | ------------------ |
| `activity_type_id`  | Activity Type   | `many2one`  | ✅  | ✅    | mail.activity.type |
| `company_id`        | Company         | `many2one`  |     |       | res.company        |
| `create_date`       | Created on      | `datetime`  |     | ✅    |                    |
| `create_uid`        | Created by      | `many2one`  |     | ✅    | res.users          |
| `delay_count`       | Interval        | `integer`   |     | ✅    |                    |
| `delay_from`        | Trigger         | `selection` | ✅  | ✅    |                    |
| `delay_unit`        | Delay units     | `selection` | ✅  | ✅    |                    |
| `display_name`      | Display Name    | `char`      |     |       |                    |
| `icon`              | Icon            | `char`      |     |       |                    |
| `id`                | ID              | `integer`   |     | ✅    |                    |
| `next_activity_ids` | Next Activities | `many2many` |     | ✅    | mail.activity.type |
| `note`              | Note            | `html`      |     | ✅    |                    |
| `plan_id`           | Plan            | `many2one`  | ✅  | ✅    | mail.activity.plan |
| `res_model`         | Model           | `selection` |     |       |                    |
| `responsible_id`    | Assigned to     | `many2one`  |     | ✅    | res.users          |
| `responsible_type`  | Assignment      | `selection` | ✅  | ✅    |                    |
| `sequence`          | Sequence        | `integer`   |     | ✅    |                    |
| `summary`           | Summary         | `char`      |     | ✅    |                    |
| `write_date`        | Last Updated on | `datetime`  |     | ✅    |                    |
| `write_uid`         | Last Updated by | `many2one`  |     | ✅    | res.users          |

**Access Rights:**

| Name                                               | Group                       | Perms     |
| -------------------------------------------------- | --------------------------- | --------- |
| mail.activity.plan.template.sale.manager           | Sales / Administrator       | `R/W/C/D` |
| mail.activity.plan.template.sale.manager           | Sales / Administrator       | `R/W/C/D` |
| mail.activity.plan.template.hr.manager             | Employees / Administrator   | `R/W/C/D` |
| mail.activity.plan.template.hr.recruitment.manager | Recruitment / Administrator | `R/W/C/D` |
| mail.activity.plan.template.system                 | Role / Administrator        | `R/W/C/D` |
| mail.activity.plan.template.user                   | Role / User                 | `R`       |

**Record Rules:**

- **Administrators can access all activity plan templates.** (4) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Manager can manage lead plan templates** (27) `W/C/D`
  - Domain: `[('plan_id.res_model', '=', 'crm.lead')]`
- **Manager can edit employee plan template** (50) `W/C/D`
  - Domain: `[('plan_id.res_model', '=', 'hr.employee')]`
- **Manager can manage applicant plan templates** (84) `W/C/D`
  - Domain: `[('plan_id.res_model', '=', 'hr.applicant')]`
- **Manager can manage sale order plan templates** (27) `W/C/D`
  - Domain: `[('plan_id.res_model', '=', 'sale.order')]`

### 🗃️ `ir.attachment` — Attachment

Attachments are used to link binary files or url to any openerp document.

    External attachment storage
    ---------------------------

    The computed field ``datas`` is implemented using ``_file_read``,
    ``_file_write`` and ``_file_delete``, which can be overridden to implement
    other storage engines. Such methods should check for other location pseudo
    uri (example: hdfs://hadoopserver).

    The default implementation is the file:dirname location that stores files
    on the local filesystem using name based on their sha1 hash

**Fields:**

| Field               | Label                                        | Type                 | Req | Store | Relation               |
| ------------------- | -------------------------------------------- | -------------------- | --- | ----- | ---------------------- |
| `access_token`      | Access Token                                 | `char`               |     | ✅    |                        |
| `checksum`          | Checksum/SHA1                                | `char`               |     | ✅    |                        |
| `company_id`        | Company                                      | `many2one`           |     | ✅    | res.company            |
| `create_date`       | Created on                                   | `datetime`           |     | ✅    |                        |
| `create_uid`        | Created by                                   | `many2one`           |     | ✅    | res.users              |
| `datas`             | File Content (base64)                        | `binary`             |     |       |                        |
| `db_datas`          | Database Data                                | `binary`             |     | ✅    |                        |
| `description`       | Description                                  | `text`               |     | ✅    |                        |
| `display_name`      | Display Name                                 | `char`               |     |       |                        |
| `file_size`         | File Size                                    | `integer`            |     | ✅    |                        |
| `has_thumbnail`     | Has Thumbnail                                | `boolean`            |     |       |                        |
| `id`                | ID                                           | `integer`            |     | ✅    |                        |
| `image_height`      | Image Height                                 | `integer`            |     |       |                        |
| `image_src`         | Image Src                                    | `char`               |     |       |                        |
| `image_width`       | Image Width                                  | `integer`            |     |       |                        |
| `index_content`     | Indexed Content                              | `text`               |     | ✅    |                        |
| `key`               | Key                                          | `char`               |     | ✅    |                        |
| `local_url`         | Attachment URL                               | `char`               |     |       |                        |
| `media_link`        | Media Link                                   | `char`               |     | ✅    |                        |
| `mimetype`          | Mime Type                                    | `char`               |     | ✅    |                        |
| `name`              | Name                                         | `char`               | ✅  | ✅    |                        |
| `original_id`       | Original (unoptimized, unresized) attachment | `many2one`           |     | ✅    | ir.attachment          |
| `public`            | Is public document                           | `boolean`            |     | ✅    |                        |
| `raw`               | File Content (raw)                           | `binary`             |     |       |                        |
| `res_field`         | Resource Field                               | `char`               |     | ✅    |                        |
| `res_id`            | Resource ID                                  | `many2one_reference` |     | ✅    |                        |
| `res_model`         | Resource Model                               | `char`               |     | ✅    |                        |
| `res_name`          | Resource Name                                | `char`               |     |       |                        |
| `store_fname`       | Stored Filename                              | `char`               |     | ✅    |                        |
| `theme_template_id` | Theme Template                               | `many2one`           |     | ✅    | theme.ir.attachment    |
| `thumbnail`         | Thumbnail                                    | `binary`             |     | ✅    |                        |
| `type`              | Type                                         | `selection`          | ✅  | ✅    |                        |
| `url`               | Url                                          | `char`               |     | ✅    |                        |
| `voice_ids`         | Voice                                        | `one2many`           |     | ✅    | discuss.voice.metadata |
| `website_id`        | Website                                      | `many2one`           |     | ✅    | website                |
| `whatsapp_media_id` | whatsapp Media Id                            | `char`               |     | ✅    |                        |
| `write_date`        | Last Updated on                              | `datetime`           |     | ✅    |                        |
| `write_uid`         | Last Updated by                              | `many2one`           |     | ✅    | res.users              |

**Access Rights:**

| Name                              | Group       | Perms     |
| --------------------------------- | ----------- | --------- |
| ir_attachment group_user          | Role / User | `R/W/C/D` |
| ir_attachment group_portal_public | Everyone    | `-`       |

### 🗃️ `hr.departure.wizard` — Departure Wizard

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                   | Label                  | Type        | Req | Store | Relation            |
| ----------------------- | ---------------------- | ----------- | --- | ----- | ------------------- |
| `create_date`           | Created on             | `datetime`  |     | ✅    |                     |
| `create_uid`            | Created by             | `many2one`  |     | ✅    | res.users           |
| `departure_date`        | Contract End Date      | `date`      | ✅  | ✅    |                     |
| `departure_description` | Additional Information | `html`      |     | ✅    |                     |
| `departure_reason_id`   | Departure Reason       | `many2one`  | ✅  | ✅    | hr.departure.reason |
| `display_name`          | Display Name           | `char`      |     |       |                     |
| `employee_ids`          | Employees              | `many2many` | ✅  | ✅    | hr.employee         |
| `id`                    | ID                     | `integer`   |     | ✅    |                     |
| `is_user_employee`      | User Employee          | `boolean`   |     |       |                     |
| `release_campany_car`   | Release Company Car    | `boolean`   |     | ✅    |                     |
| `remove_related_user`   | Related User           | `boolean`   |     | ✅    |                     |
| `set_date_end`          | Set Contract End Date  | `boolean`   |     | ✅    |                     |
| `write_date`            | Last Updated on        | `datetime`  |     | ✅    |                     |
| `write_uid`             | Last Updated by        | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                       | Group                                     | Perms   |
| -------------------------- | ----------------------------------------- | ------- |
| access.hr.departure.wizard | Employees / Officer: Manage all employees | `R/W/C` |

### 🗃️ `fleet.vehicle.assignation.log` — Drivers history on a vehicle

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label                 | Type       | Req | Store | Relation      |
| -------------------- | --------------------- | ---------- | --- | ----- | ------------- |
| `attachment_number`  | Number of Attachments | `integer`  |     |       |               |
| `create_date`        | Created on            | `datetime` |     | ✅    |               |
| `create_uid`         | Created by            | `many2one` |     | ✅    | res.users     |
| `date_end`           | End Date              | `date`     |     | ✅    |               |
| `date_start`         | Start Date            | `date`     |     | ✅    |               |
| `display_name`       | Display Name          | `char`     |     |       |               |
| `driver_employee_id` | Driver (Employee)     | `many2one` |     | ✅    | hr.employee   |
| `driver_id`          | Driver                | `many2one` | ✅  | ✅    | res.partner   |
| `id`                 | ID                    | `integer`  |     | ✅    |               |
| `vehicle_id`         | Vehicle               | `many2one` | ✅  | ✅    | fleet.vehicle |
| `write_date`         | Last Updated on       | `datetime` |     | ✅    |               |
| `write_uid`          | Last Updated by       | `many2one` |     | ✅    | res.users     |

**Access Rights:**

| Name                                           | Group                                | Perms     |
| ---------------------------------------------- | ------------------------------------ | --------- |
| fleet_vehicle_assignation_log fleet_group_user | Fleet / Officer: Manage all vehicles | `R/W/C/D` |

### 🗃️ `fleet.vehicle.odometer` — Odometer log for a vehicle

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label             | Type        | Req | Store | Relation      |
| -------------------- | ----------------- | ----------- | --- | ----- | ------------- |
| `create_date`        | Created on        | `datetime`  |     | ✅    |               |
| `create_uid`         | Created by        | `many2one`  |     | ✅    | res.users     |
| `date`               | Date              | `date`      |     | ✅    |               |
| `display_name`       | Display Name      | `char`      |     |       |               |
| `driver_employee_id` | Driver (Employee) | `many2one`  |     |       | hr.employee   |
| `driver_id`          | Driver            | `many2one`  |     | ✅    | res.partner   |
| `id`                 | ID                | `integer`   |     | ✅    |               |
| `name`               | Name              | `char`      |     | ✅    |               |
| `unit`               | Unit              | `selection` |     |       |               |
| `value`              | Odometer Value    | `float`     |     | ✅    |               |
| `vehicle_id`         | Vehicle           | `many2one`  | ✅  | ✅    | fleet.vehicle |
| `write_date`         | Last Updated on   | `datetime`  |     | ✅    |               |
| `write_uid`          | Last Updated by   | `many2one`  |     | ✅    | res.users     |

**Access Rights:**

| Name                                | Group                                | Perms     |
| ----------------------------------- | ------------------------------------ | --------- |
| fleet_vehicle_odometer_access_right | Fleet / Officer: Manage all vehicles | `R/W/C/D` |

**Record Rules:**

- **Administrator has all rights on vehicle's vehicle's odometer** (21) `R/W/C/D`
- **Fleet odometer: Multi Company** (Global) `R/W/C/D`
  - Domain: `[('vehicle_id.company_id', 'in', company_ids + [False])]`

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
