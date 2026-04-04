---
title: "Online Appointments CRM"
module: "online_appointment_crm"
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

# 🟢 Online Appointments CRM

> **Module:** `online_appointment_crm` | **Version:** `19.0.1.0` **Category:** Website |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[online_appointment]] [[crm]]

## 📖 Description

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT calendar.online.appointment.crm.form (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**2 model(s) defined by this module:**

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
