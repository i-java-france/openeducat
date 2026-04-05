---
title: "Online Appointments"
module: "online_appointment"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Website"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/w______, odoo/app]
---

# 🟢 Online Appointments

> **Module:** `online_appointment` | **Version:** `19.0.1.0` **Category:** Website |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[calendar]] [[hr]] [[website]] [[qna_mixin]] [[resource]] [[portal]]

## 📖 Description

## 🖥️ UI Components

### Menus

- `Calendar/Configuration/Online Appointment Resource`
- `Calendar/Online Appointment`
- `Calendar/Reporting`

### Views

- `* INHERIT calendar.event.form (form)`
- `* INHERIT calendar.event.search.inherit (search)`
- `* INHERIT calendar.event.tree.inherited (list)`
- `* INHERIT hr.employee.appointment.tree (list)`
- `Booking (qweb)`
- `Confirmation (qweb)`
- `Events (graph)`
- `Services (qweb)`
- `calendar.appointment.resource.form (form)`
- `calendar.appointment.resource.tree (list)`
- `calendar.event.pivot (pivot)`
- `calendar.online.appointment.form (form)`
- `calendar.online.appointment.kanban (kanban)`
- `calendar.online.appointment.search (search)`
- `calendar.online.appointment.tree (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**6 model(s) defined by this module:**

### 🗃️ `calendar.online.appointment` — Booking calendar Appointment

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                             | Label                        | Type        | Req | Store | Relation                      |
| --------------------------------- | ---------------------------- | ----------- | --- | ----- | ----------------------------- |
| `allow_other_members`             | Allow Other Member           | `boolean`   |     | ✅    |                               |
| `appointment_based_on`            | Appointment Based on         | `selection` |     | ✅    |                               |
| `appointment_date`                | Appointment Date             | `date`      |     | ✅    |                               |
| `appointment_resource_ids`        | Appointment Resources        | `many2many` |     | ✅    | calendar.appointment.resource |
| `appointment_schedule`            | Appointment Schedule         | `selection` |     | ✅    |                               |
| `assign_method`                   | Assignation                  | `selection` |     | ✅    |                               |
| `calendar_reminder_ids`           | Reminders                    | `many2many` |     | ✅    | calendar.alarm                |
| `cancel_type`                     | Cancel In                    | `selection` |     | ✅    |                               |
| `can_publish`                     | Can Publish                  | `boolean`   |     |       |                               |
| `code`                            | Unique Code                  | `char`      |     | ✅    |                               |
| `company_id`                      | Company                      | `many2one`  |     | ✅    | res.company                   |
| `count_appointment`               | appointment                  | `integer`   |     |       |                               |
| `create_crm_lead`                 | Create Opportunities         | `boolean`   |     | ✅    |                               |
| `create_date`                     | Created on                   | `datetime`  |     | ✅    |                               |
| `create_uid`                      | Created by                   | `many2one`  |     | ✅    | res.users                     |
| `crm_lead_count`                  | Crm Leads Count              | `integer`   |     |       |                               |
| `crm_lead_ids`                    | Leads/Opportunity            | `many2many` |     | ✅    | crm.lead                      |
| `default_timezone`                | Default Timezone             | `selection` |     | ✅    |                               |
| `description`                     | Descriptions                 | `html`      |     | ✅    |                               |
| `display_name`                    | Display Name                 | `char`      |     |       |                               |
| `duration`                        | Duration                     | `float`     |     | ✅    |                               |
| `employee_ids`                    | Staff                        | `many2many` |     | ✅    | hr.employee                   |
| `end_date`                        | End Date                     | `datetime`  |     | ✅    |                               |
| `event_ids`                       | Calender Events              | `one2many`  |     | ✅    | calendar.event                |
| `from_date`                       | From Date                    | `datetime`  |     | ✅    |                               |
| `has_message`                     | Has Message                  | `boolean`   |     |       |                               |
| `id`                              | ID                           | `integer`   |     | ✅    |                               |
| `image_1920`                      | Image                        | `binary`    |     | ✅    |                               |
| `is_cancel`                       | Allow Cancellation           | `boolean`   |     | ✅    |                               |
| `is_published`                    | Is Published                 | `boolean`   |     | ✅    |                               |
| `is_seo_optimized`                | SEO optimized                | `boolean`   |     | ✅    |                               |
| `location`                        | Appointment Location         | `char`      |     | ✅    |                               |
| `manual_confirm`                  | Manual Confirmation          | `boolean`   |     | ✅    |                               |
| `max_appointment_days`            | Appointment not after (days) | `integer`   |     | ✅    |                               |
| `message_attachment_count`        | Attachment Count             | `integer`   |     |       |                               |
| `message_follower_ids`            | Followers                    | `one2many`  |     | ✅    | mail.followers                |
| `message_has_error`               | Message Delivery error       | `boolean`   |     |       |                               |
| `message_has_error_counter`       | Number of errors             | `integer`   |     |       |                               |
| `message_has_sms_error`           | SMS Delivery error           | `boolean`   |     |       |                               |
| `message_ids`                     | Messages                     | `one2many`  |     | ✅    | mail.message                  |
| `message_is_follower`             | Is Follower                  | `boolean`   |     |       |                               |
| `message_needaction`              | Action Needed                | `boolean`   |     |       |                               |
| `message_needaction_counter`      | Number of Actions            | `integer`   |     |       |                               |
| `message_partner_ids`             | Followers (Partners)         | `many2many` |     |       | res.partner                   |
| `min_appointment_cancel_duration` | Cancel Appointment Before    | `integer`   |     | ✅    |                               |
| `min_appointment_hours`           | Pre-Booking Time             | `float`     |     | ✅    |                               |
| `name`                            | Name                         | `char`      |     | ✅    |                               |
| `not_after_type`                  | not_after_type               | `selection` |     | ✅    |                               |
| `question_ids`                    | Questions                    | `one2many`  |     | ✅    | question.single               |
| `questions`                       | Appointment Question         | `one2many`  |     | ✅    | calendar.appointment.question |
| `rating_ids`                      | Ratings                      | `one2many`  |     | ✅    | rating.rating                 |
| `resource_ids`                    | Resources                    | `many2many` |     | ✅    | resource.calendar.attendance  |
| `resource_location_id`            | Location                     | `many2one`  |     | ✅    | res.partner                   |
| `seo_name`                        | Seo name                     | `char`      |     | ✅    |                               |
| `short_description`               | Description                  | `text`      |     | ✅    |                               |
| `slots`                           | Appointment Slots            | `one2many`  |     | ✅    | calendar.appointment.slot     |
| `user_id`                         | Team Leader                  | `many2one`  | ✅  | ✅    | res.users                     |
| `website_absolute_url`            | Website Absolute URL         | `char`      |     |       |                               |
| `website_id`                      | Website                      | `many2one`  |     | ✅    | website                       |
| `website_message_ids`             | Website Messages             | `one2many`  |     | ✅    | mail.message                  |
| `website_meta_description`        | Website meta description     | `text`      |     | ✅    |                               |
| `website_meta_keywords`           | Website meta keywords        | `char`      |     | ✅    |                               |
| `website_meta_og_img`             | Website opengraph image      | `char`      |     | ✅    |                               |
| `website_meta_title`              | Website meta title           | `char`      |     | ✅    |                               |
| `website_published`               | Visible on current website   | `boolean`   |     |       |                               |
| `website_url`                     | Website URL                  | `char`      |     |       |                               |
| `write_date`                      | Last Updated on              | `datetime`  |     | ✅    |                               |
| `write_uid`                       | Last Updated by              | `many2one`  |     | ✅    | res.users                     |

**Access Rights:**

| Name                               | Group       | Perms     |
| ---------------------------------- | ----------- | --------- |
| access_calendar_appointment        | Role / User | `R/W/C/D` |
| access_calendar_online_appointment | Role / User | `R/W/C/D` |

**Record Rules:**

- **Calendar Online Appointment multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `calendar.event` — Calendar Event

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                             | Label                        | Type                 | Req | Store | Relation                      |
| --------------------------------- | ---------------------------- | -------------------- | --- | ----- | ----------------------------- |
| `academic_calendar`               | Academic Calendar?           | `boolean`            |     | ✅    |                               |
| `accepted_count`                  | Accepted Count               | `integer`            |     |       |                               |
| `access_token`                    | Invitation Token             | `char`               |     | ✅    |                               |
| `active`                          | Active                       | `boolean`            |     | ✅    |                               |
| `activity_ids`                    | Activities                   | `one2many`           |     | ✅    | mail.activity                 |
| `alarm_ids`                       | Reminders                    | `many2many`          |     | ✅    | calendar.alarm                |
| `allday`                          | All Day                      | `boolean`            |     | ✅    |                               |
| `applicant_id`                    | Applicant                    | `many2one`           |     | ✅    | hr.applicant                  |
| `appointment_id`                  | Online Appointment           | `many2one`           |     | ✅    | calendar.online.appointment   |
| `attendee_ids`                    | Participant                  | `one2many`           |     | ✅    | calendar.attendee             |
| `attendees_count`                 | Attendees Count              | `integer`            |     |       |                               |
| `automatic_email`                 | Automatic Email              | `boolean`            |     | ✅    |                               |
| `awaiting_count`                  | Awaiting Count               | `integer`            |     |       |                               |
| `batch_ids`                       | Batches                      | `many2many`          |     | ✅    | op.batch                      |
| `booking_status`                  | Booking Status               | `selection`          |     | ✅    |                               |
| `byday`                           | By day                       | `selection`          |     |       |                               |
| `categ_ids`                       | Tags                         | `many2many`          |     | ✅    | calendar.event.type           |
| `count`                           | Number of Repetitions        | `integer`            |     |       |                               |
| `course_ids`                      | Courses                      | `many2many`          |     | ✅    | op.course                     |
| `create_date`                     | Created on                   | `datetime`           |     | ✅    |                               |
| `create_uid`                      | Created by                   | `many2one`           |     | ✅    | res.users                     |
| `current_attendee`                | Current Attendee             | `many2one`           |     |       | calendar.attendee             |
| `current_status`                  | Attending?                   | `selection`          |     |       |                               |
| `day`                             | Date of month                | `integer`            |     |       |                               |
| `declined_count`                  | Declined Count               | `integer`            |     |       |                               |
| `description`                     | Description                  | `html`               |     | ✅    |                               |
| `display_description`             | Display Description          | `boolean`            |     |       |                               |
| `display_name`                    | Display Name                 | `char`               |     |       |                               |
| `display_time`                    | Event Time                   | `char`               |     |       |                               |
| `duration`                        | Duration                     | `float`              |     | ✅    |                               |
| `effective_privacy`               | Effective Privacy            | `selection`          |     |       |                               |
| `end_type`                        | Recurrence Termination       | `selection`          |     |       |                               |
| `event_tz`                        | Timezone                     | `selection`          |     |       |                               |
| `follow_recurrence`               | Follow Recurrence            | `boolean`            |     | ✅    |                               |
| `fri`                             | Fri                          | `boolean`            |     |       |                               |
| `has_message`                     | Has Message                  | `boolean`            |     |       |                               |
| `id`                              | ID                           | `integer`            |     | ✅    |                               |
| `interval`                        | Repeat On                    | `integer`            |     |       |                               |
| `invalid_email_partner_ids`       | Invalid Email Partner        | `many2many`          |     |       | res.partner                   |
| `is_highlighted`                  | Is the Event Highlighted     | `boolean`            |     |       |                               |
| `is_organizer_alone`              | Is the Organizer Alone       | `boolean`            |     |       |                               |
| `location`                        | Location                     | `char`               |     | ✅    |                               |
| `meeting_url`                     | URL                          | `char`               |     | ✅    |                               |
| `meet_url`                        | Google Meet URL              | `char`               |     | ✅    |                               |
| `message_attachment_count`        | Attachment Count             | `integer`            |     |       |                               |
| `message_follower_ids`            | Followers                    | `one2many`           |     | ✅    | mail.followers                |
| `message_has_error`               | Message Delivery error       | `boolean`            |     |       |                               |
| `message_has_error_counter`       | Number of errors             | `integer`            |     |       |                               |
| `message_has_sms_error`           | SMS Delivery error           | `boolean`            |     |       |                               |
| `message_ids`                     | Messages                     | `one2many`           |     | ✅    | mail.message                  |
| `message_is_follower`             | Is Follower                  | `boolean`            |     |       |                               |
| `message_needaction`              | Action Needed                | `boolean`            |     |       |                               |
| `message_needaction_counter`      | Number of Actions            | `integer`            |     |       |                               |
| `message_partner_ids`             | Followers (Partners)         | `many2many`          |     |       | res.partner                   |
| `mon`                             | Mon                          | `boolean`            |     |       |                               |
| `month_by`                        | Option                       | `selection`          |     |       |                               |
| `mpw`                             | Moderator Password           | `char`               |     | ✅    |                               |
| `name`                            | Meeting Subject              | `char`               | ✅  | ✅    |                               |
| `notes`                           | Notes                        | `html`               |     | ✅    |                               |
| `online_appointment_resource_ids` | Online Appointment Resources | `many2one`           |     | ✅    | calendar.appointment.resource |
| `online_meeting`                  | Online Meeting               | `boolean`            |     | ✅    |                               |
| `opportunity_id`                  | Crm Opportunity              | `many2one`           |     | ✅    | crm.lead                      |
| `op_session_id`                   | Session                      | `many2one`           |     | ✅    | op.session                    |
| `partner_id`                      | Scheduled by                 | `many2one`           |     |       | res.partner                   |
| `partner_ids`                     | Attendees                    | `many2many`          |     | ✅    | res.partner                   |
| `privacy`                         | Privacy                      | `selection`          |     | ✅    |                               |
| `rating_ids`                      | Ratings                      | `one2many`           |     | ✅    | rating.rating                 |
| `recurrence_id`                   | Recurrence Rule              | `many2one`           |     | ✅    | calendar.recurrence           |
| `recurrence_update`               | Recurrence Update            | `selection`          |     |       |                               |
| `recurrency`                      | Recurrent                    | `boolean`            |     | ✅    |                               |
| `res_id`                          | Document ID                  | `many2one_reference` |     | ✅    |                               |
| `res_model`                       | Document Model Name          | `char`               |     | ✅    |                               |
| `res_model_id`                    | Document Model               | `many2one`           |     | ✅    | ir.model                      |
| `res_model_name`                  | Model Description            | `char`               |     |       |                               |
| `rrule`                           | Recurrent Rule               | `char`               |     |       |                               |
| `rrule_type`                      | Recurrence                   | `selection`          |     |       |                               |
| `rrule_type_ui`                   | Repeat                       | `selection`          |     |       |                               |
| `sat`                             | Sat                          | `boolean`            |     |       |                               |
| `should_show_status`              | Should Show Status           | `boolean`            |     |       |                               |
| `show_as`                         | Show as                      | `selection`          | ✅  | ✅    |                               |
| `start`                           | Start                        | `datetime`           | ✅  | ✅    |                               |
| `start_date`                      | Start Date                   | `date`               |     | ✅    |                               |
| `stop`                            | Stop                         | `datetime`           | ✅  | ✅    |                               |
| `stop_date`                       | End Date                     | `date`               |     | ✅    |                               |
| `sun`                             | Sun                          | `boolean`            |     |       |                               |
| `tentative_count`                 | Tentative Count              | `integer`            |     |       |                               |
| `thu`                             | Thu                          | `boolean`            |     |       |                               |
| `tue`                             | Tue                          | `boolean`            |     |       |                               |
| `unavailable_partner_ids`         | Unavailable Attendees        | `many2many`          |     |       | res.partner                   |
| `until`                           | Until                        | `date`               |     |       |                               |
| `user_can_edit`                   | User Can Edit                | `boolean`            |     |       |                               |
| `user_id`                         | Organizer                    | `many2one`           |     | ✅    | res.users                     |
| `videocall_channel_id`            | Discuss Channel              | `many2one`           |     | ✅    | discuss.channel               |
| `videocall_location`              | Meeting URL                  | `char`               |     | ✅    |                               |
| `videocall_source`                | Videocall Source             | `selection`          |     |       |                               |
| `website_message_ids`             | Website Messages             | `one2many`           |     | ✅    | mail.message                  |
| `wed`                             | Wed                          | `boolean`            |     |       |                               |
| `weekday`                         | Weekday                      | `selection`          |     |       |                               |
| `write_date`                      | Last Updated on              | `datetime`           |     | ✅    |                               |
| `write_uid`                       | Last Updated by              | `many2one`           |     | ✅    | res.users                     |

**Access Rights:**

| Name                           | Group                                        | Perms     |
| ------------------------------ | -------------------------------------------- | --------- |
| calendar.event                 | Sales / User: Own Documents Only             | `R/W/C`   |
| calendar.event.manager         | Sales / Administrator                        | `R/W/C/D` |
| calendar.event.hr.user         | Time Off / Officer: Manage all requests      | `R/W/C/D` |
| calendar.event.hruser          | Recruitment / Officer: Manage all applicants | `R/W/C/D` |
| calendar.event.partner.manager | Contact / Creation                           | `R/W/C/D` |
| calendar.event_all_user        | Role / Portal                                | `R`       |
| calendar.event_all_employee    | Role / User                                  | `R/W/C/D` |

**Record Rules:**

- **Own events** (10) `R/W/C/D`
  - Domain: `[('partner_ids', 'in', user.partner_id.id)]`
- **All Calendar Event for employees** (1) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`
- **Private events** (Global) `W/C/D`
  - Domain:
    `['|', ('privacy', '!=', 'private'), '&', ('privacy', '=', 'private'), '|', ('user_id', '=', user.id), ('partner_ids', 'in', user.partner_id.id)]`

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

### 🗃️ `calendar.appointment.question` — Appointment Question

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label              | Type        | Req | Store | Relation                    |
| ----------------- | ------------------ | ----------- | --- | ----- | --------------------------- |
| `appointment_id`  | Online Appointment | `many2one`  |     | ✅    | calendar.online.appointment |
| `create_date`     | Created on         | `datetime`  |     | ✅    |                             |
| `create_uid`      | Created by         | `many2one`  |     | ✅    | res.users                   |
| `display_name`    | Display Name       | `char`      |     |       |                             |
| `id`              | ID                 | `integer`   |     | ✅    |                             |
| `placeholder`     | Placeholder        | `char`      |     | ✅    |                             |
| `question`        | Question           | `char`      |     | ✅    |                             |
| `question_type`   | Question Type      | `selection` |     | ✅    |                             |
| `required_answer` | Required Answer    | `boolean`   |     | ✅    |                             |
| `write_date`      | Last Updated on    | `datetime`  |     | ✅    |                             |
| `write_uid`       | Last Updated by    | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                                 | Group       | Perms     |
| ------------------------------------ | ----------- | --------- |
| access_calendar_appointment_question | Role / User | `R/W/C/D` |

### 🗃️ `calendar.appointment.slot` — Booking Slot

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field            | Label                | Type        | Req | Store | Relation                    |
| ---------------- | -------------------- | ----------- | --- | ----- | --------------------------- |
| `appointment_id` | Calendar Appointment | `many2one`  |     | ✅    | calendar.online.appointment |
| `create_date`    | Created on           | `datetime`  |     | ✅    |                             |
| `create_uid`     | Created by           | `many2one`  |     | ✅    | res.users                   |
| `display_name`   | Display Name         | `char`      |     |       |                             |
| `hour`           | Starting Hour        | `float`     |     | ✅    |                             |
| `id`             | ID                   | `integer`   |     | ✅    |                             |
| `week`           | Week Day             | `selection` |     | ✅    |                             |
| `write_date`     | Last Updated on      | `datetime`  |     | ✅    |                             |
| `write_uid`      | Last Updated by      | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                             | Group       | Perms     |
| -------------------------------- | ----------- | --------- |
| access_calendar_appointment_slot | Role / User | `R/W/C/D` |

### 🗃️ `calendar.appointment.resource` — Calendar Appointment Resource

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                  | Label            | Type        | Req | Store | Relation                      |
| ---------------------- | ---------------- | ----------- | --- | ----- | ----------------------------- |
| `active`               | Active           | `boolean`   |     | ✅    |                               |
| `avatar_1024`          | Avatar 1024      | `binary`    |     |       |                               |
| `avatar_128`           | Avatar 128       | `binary`    |     |       |                               |
| `avatar_1920`          | Avatar           | `binary`    |     |       |                               |
| `avatar_256`           | Avatar 256       | `binary`    |     |       |                               |
| `avatar_512`           | Avatar 512       | `binary`    |     |       |                               |
| `company_id`           | Company          | `many2one`  |     | ✅    | res.company                   |
| `create_date`          | Created on       | `datetime`  |     | ✅    |                               |
| `create_uid`           | Created by       | `many2one`  |     | ✅    | res.users                     |
| `default_timezone`     | Default Timezone | `selection` |     | ✅    |                               |
| `display_name`         | Display Name     | `char`      |     |       |                               |
| `id`                   | ID               | `integer`   |     | ✅    |                               |
| `image_1024`           | Image 1024       | `binary`    |     | ✅    |                               |
| `image_128`            | Image 128        | `binary`    |     | ✅    |                               |
| `image_1920`           | Image            | `binary`    |     | ✅    |                               |
| `image_256`            | Image 256        | `binary`    |     | ✅    |                               |
| `image_512`            | Image 512        | `binary`    |     | ✅    |                               |
| `linked_resource_ids`  | Linked Resource  | `many2many` |     | ✅    | calendar.appointment.resource |
| `name`                 | Resource Name    | `char`      | ✅  | ✅    |                               |
| `resource_calendar_id` | Working Hours    | `many2one`  |     | ✅    | resource.calendar             |
| `resource_capacity`    | Capacity         | `integer`   | ✅  | ✅    |                               |
| `resource_description` | Description      | `html`      |     | ✅    |                               |
| `resource_id`          | Resource         | `many2one`  | ✅  | ✅    | resource.resource             |
| `sequence`             | Sequence         | `integer`   | ✅  | ✅    |                               |
| `tz`                   | Timezone         | `selection` |     |       |                               |
| `write_date`           | Last Updated on  | `datetime`  |     | ✅    |                               |
| `write_uid`            | Last Updated by  | `many2one`  |     | ✅    | res.users                     |

**Access Rights:**

| Name                                 | Group       | Perms     |
| ------------------------------------ | ----------- | --------- |
| access_calendar_appointment_resource | Role / User | `R/W/C/D` |
