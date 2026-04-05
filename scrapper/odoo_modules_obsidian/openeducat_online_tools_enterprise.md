---
title: "OpenEduCat Online Tools Base Enterprise"
module: "openeducat_online_tools_enterprise"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Education"
application: false
auto_install: true
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 OpenEduCat Online Tools Base Enterprise

> **Module:** `openeducat_online_tools_enterprise` | **Version:** `19.0.1.0`
> **Category:** Education | **License:** `Other proprietary` **Author:** OpenEduCat Inc
> **Website:** https://www.openeducat.org

## 🔗 Dependencies

[[calendar]] [[online_tools_intg]] [[openeducat_core_enterprise]]
[[openeducat_timetable_enterprise]]

## 📖 Description

## OpenEduCat Online Tool

### Manage Online Meeting

[![](/openeducat_online_tools_enterprise/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module allows you to manage online meeting. This module adds feature to manage the
online meeting of session in OpenEduCat.

[Contact Us](https://www.openeducat.org/contactus/)

## Openeducat Online Tool

Openeducat Online Tool helps to manage the online meetings of sessions.

![](/openeducat_online_tools_enterprise/static/description/online_tool_1.png)

![](/openeducat_online_tools_enterprise/static/description/online_tool_2.png)

By Clicking on smart button Online Meeting at the top, we can create the online meeting
of particular session in calender

Again going back to the session, you can see the online meeting is created for that
session

![](/openeducat_online_tools_enterprise/static/description/online_tool_3.png)

![](/openeducat_online_tools_enterprise/static/description/online_tool_4.png)

By clicking on the smart button, calendar view gives you the better look to check the
online meeting.

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT Portal layout : Online Meeting (qweb)`
- `* INHERIT calendar.event.online.tools (list)`
- `* INHERIT calendar.online.meeting.form (form)`
- `* INHERIT op.session.online.tools.form (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**2 model(s) defined by this module:**

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

### 🗃️ `op.session` — Sessions

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation            |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ------------------- |
| `academic_plan_id`           | Academic Plan          | `many2one`  |     | ✅    | op.academic.plan    |
| `active`                     | Active                 | `boolean`   |     | ✅    |                     |
| `attendance_sheet`           | Session                | `one2many`  |     | ✅    | op.attendance.sheet |
| `batch_id`                   | Batch                  | `many2one`  |     | ✅    | op.batch            |
| `classroom_id`               | Classroom              | `many2one`  |     | ✅    | op.classroom        |
| `color`                      | Color Index            | `integer`   |     | ✅    |                     |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company         |
| `course_id`                  | Course                 | `many2one`  |     | ✅    | op.course           |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                     |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users           |
| `days`                       | Days                   | `selection` |     | ✅    |                     |
| `display_name`               | Display Name           | `char`      |     |       |                     |
| `end_datetime`               | End Time               | `datetime`  | ✅  | ✅    |                     |
| `faculty_id`                 | Faculty                | `many2one`  | ✅  | ✅    | op.faculty          |
| `has_message`                | Has Message            | `boolean`   |     |       |                     |
| `id`                         | ID                     | `integer`   |     | ✅    |                     |
| `lesson_ids`                 | Lesson                 | `many2many` |     | ✅    | op.lesson           |
| `meeting_count`              | Meeting Count          | `integer`   |     |       |                     |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                     |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers      |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                     |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                     |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                     |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message        |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                     |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                     |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                     |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner         |
| `name`                       | Name                   | `char`      |     | ✅    |                     |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating       |
| `required_field`             | Required Field         | `boolean`   |     | ✅    |                     |
| `section_ids`                | Section                | `many2many` |     | ✅    | op.section          |
| `start_datetime`             | Start Time             | `datetime`  | ✅  | ✅    |                     |
| `state`                      | Status                 | `selection` |     | ✅    |                     |
| `student_count`              | Student Count          | `integer`   |     |       |                     |
| `subject_id`                 | Subject                | `many2one`  | ✅  | ✅    | op.subject          |
| `timing`                     | Session timing         | `char`      |     |       |                     |
| `timing_id`                  | Timing                 | `many2one`  |     | ✅    | op.timing           |
| `type`                       | Day                    | `char`      |     | ✅    |                     |
| `user_id`                    | User                   | `many2one`  |     | ✅    | res.users           |
| `user_ids`                   | Users                  | `many2many` |     | ✅    | res.users           |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message        |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                     |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users           |

**Access Rights:**

| Name                           | Group               | Perms     |
| ------------------------------ | ------------------- | --------- |
| name_op_session_student        | Timetable / Manager | `R/W/C/D` |
| name_op_session_timetable_user | Timetable / User    | `R/W/C`   |

**Record Rules:**

- **Student Session rule** (160) `R/W/C/D`
  - Domain: `['|', ('user_ids','in',user.id), ('user_ids','in',user.child_ids.ids)]`
- **Manager Session Rule** (161) `R/W/C/D`
  - Domain: `[(1,'=',1)]`
- **User Session Rule** (160) `R/W/C/D`
  - Domain: `[('faculty_id.user_id','=',user.id)]`
- **Timetable multi-company** (Global) `R/W/C/D`
  - Domain:
    `['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]`
