---
title: "Gamification"
module: "gamification"
state: "installed"
version: "19.0.1.0"
author: "Odoo S.A."
maintainer: "N/A"
website: ""
license: "LGPL-3"
category: "Human Resources"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_______________]
---

# 🟢 Gamification

> **Module:** `gamification` | **Version:** `19.0.1.0` **Category:** Human Resources |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:** _N/A_

## 🔗 Dependencies

[[mail]]

## 📖 Description

# Gamification process

The Gamification module provides ways to evaluate and motivate the users of Odoo.

The users can be evaluated using goals and numerical objectives to reach. **Goals** are
assigned through **challenges** to evaluate and compare members of a team with each
others and through time.

For non-numerical achievements, **badges** can be granted to users. From a simple "thank
you" to an exceptional achievement, a badge is an easy way to exprimate gratitude to a
user for their good work.

Both goals and badges are flexibles and can be adapted to a large range of modules and
actions. When installed, this module creates easy goals to help new users to discover
Odoo and configure their user profile.

## 🖥️ UI Components

### Menus

- `Settings/Gamification Tools`
- `Settings/Gamification Tools/Badges`
- `Settings/Gamification Tools/Challenges`
- `Settings/Gamification Tools/Goal Definitions`
- `Settings/Gamification Tools/Goals`
- `Settings/Gamification Tools/Karma Tracking`
- `Settings/Gamification Tools/Ranks`

### Views

- `* INHERIT res.users.view.form.inherit.gamification (form)`
- `Badge Form (form)`
- `Badge Kanban View (kanban)`
- `Badge List (list)`
- `Badge User Kanban View (kanban)`
- `Challenge Form (form)`
- `Challenge Kanban (kanban)`
- `Challenge Search (search)`
- `Challenge line list (list)`
- `Challenges List (list)`
- `Goal Definition Search (search)`
- `Goal Definitions Form (form)`
- `Goal Definitions List (list)`
- `Goal Form (form)`
- `Goal Kanban View (kanban)`
- `Goal List (list)`
- `Goal Search (search)`
- `Grant Badge User Form (form)`
- `Update the current value of the Goal (form)`
- `gamification.badge.view.search (search)`
- `gamification.karma.rank.view.form (form)`
- `gamification.karma.ranks.view.list (list)`
- `gamification.karma.ranks.view.search (search)`
- `gamification.karma.tracking.view.form (form)`
- `gamification.karma.tracking.view.list (list)`
- `gamification.karma.tracking.view.search (search)`

### Reports

_none_

## 🛠️ Technical Documentation

**11 model(s) defined by this module:**

### 🗃️ `gamification.badge` — Gamification Badge

> 📧 Mail Thread

Badge object that users can send and receive

**Fields:**

| Field                        | Label                      | Type        | Req | Store | Relation                     |
| ---------------------------- | -------------------------- | ----------- | --- | ----- | ---------------------------- |
| `active`                     | Active                     | `boolean`   |     | ✅    |                              |
| `can_publish`                | Can Publish                | `boolean`   |     |       |                              |
| `challenge_ids`              | Reward of Challenges       | `one2many`  |     | ✅    | gamification.challenge       |
| `create_date`                | Created on                 | `datetime`  |     | ✅    |                              |
| `create_uid`                 | Created by                 | `many2one`  |     | ✅    | res.users                    |
| `description`                | Description                | `html`      |     | ✅    |                              |
| `display_name`               | Display Name               | `char`      |     |       |                              |
| `goal_definition_ids`        | Rewarded by                | `many2many` |     | ✅    | gamification.goal.definition |
| `granted_count`              | Total                      | `integer`   |     |       |                              |
| `granted_employees_count`    | Granted Employees Count    | `integer`   |     |       |                              |
| `granted_users_count`        | Number of users            | `integer`   |     |       |                              |
| `has_message`                | Has Message                | `boolean`   |     |       |                              |
| `id`                         | ID                         | `integer`   |     | ✅    |                              |
| `image_1024`                 | Image 1024                 | `binary`    |     | ✅    |                              |
| `image_128`                  | Image 128                  | `binary`    |     | ✅    |                              |
| `image_1920`                 | Image                      | `binary`    |     | ✅    |                              |
| `image_256`                  | Image 256                  | `binary`    |     | ✅    |                              |
| `image_512`                  | Image 512                  | `binary`    |     | ✅    |                              |
| `is_published`               | Is Published               | `boolean`   |     | ✅    |                              |
| `level`                      | Forum Badge Level          | `selection` |     | ✅    |                              |
| `message_attachment_count`   | Attachment Count           | `integer`   |     |       |                              |
| `message_follower_ids`       | Followers                  | `one2many`  |     | ✅    | mail.followers               |
| `message_has_error`          | Message Delivery error     | `boolean`   |     |       |                              |
| `message_has_error_counter`  | Number of errors           | `integer`   |     |       |                              |
| `message_has_sms_error`      | SMS Delivery error         | `boolean`   |     |       |                              |
| `message_ids`                | Messages                   | `one2many`  |     | ✅    | mail.message                 |
| `message_is_follower`        | Is Follower                | `boolean`   |     |       |                              |
| `message_needaction`         | Action Needed              | `boolean`   |     |       |                              |
| `message_needaction_counter` | Number of Actions          | `integer`   |     |       |                              |
| `message_partner_ids`        | Followers (Partners)       | `many2many` |     |       | res.partner                  |
| `name`                       | Badge                      | `char`      | ✅  | ✅    |                              |
| `owner_ids`                  | Owners                     | `one2many`  |     | ✅    | gamification.badge.user      |
| `rating_ids`                 | Ratings                    | `one2many`  |     | ✅    | rating.rating                |
| `remaining_sending`          | Remaining Sending Allowed  | `integer`   |     |       |                              |
| `rule_auth`                  | Allowance to Grant         | `selection` | ✅  | ✅    |                              |
| `rule_auth_badge_ids`        | Required Badges            | `many2many` |     | ✅    | gamification.badge           |
| `rule_auth_user_ids`         | Authorized Users           | `many2many` |     | ✅    | res.users                    |
| `rule_max`                   | Monthly Limited Sending    | `boolean`   |     | ✅    |                              |
| `rule_max_number`            | Limitation Number          | `integer`   |     | ✅    |                              |
| `stat_my`                    | My Total                   | `integer`   |     |       |                              |
| `stat_my_monthly_sending`    | My Monthly Sending Total   | `integer`   |     |       |                              |
| `stat_my_this_month`         | My Monthly Total           | `integer`   |     |       |                              |
| `stat_this_month`            | Monthly total              | `integer`   |     |       |                              |
| `survey_id`                  | Survey                     | `many2one`  |     | ✅    | survey.survey                |
| `survey_ids`                 | Survey Ids                 | `one2many`  |     | ✅    | survey.survey                |
| `unique_owner_ids`           | Unique Owners              | `many2many` |     |       | res.users                    |
| `website_absolute_url`       | Website Absolute URL       | `char`      |     |       |                              |
| `website_message_ids`        | Website Messages           | `one2many`  |     | ✅    | mail.message                 |
| `website_published`          | Visible on current website | `boolean`   |     |       |                              |
| `website_url`                | Website URL                | `char`      |     |       |                              |
| `write_date`                 | Last Updated on            | `datetime`  |     | ✅    |                              |
| `write_uid`                  | Last Updated by            | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                           | Group                                     | Perms     |
| ------------------------------ | ----------------------------------------- | --------- |
| Badge Officer                  | Employees / Officer: Manage all employees | `R/W/C/D` |
| student_gamifiction_badge      | OpenEduCat / User                         | `R/W/C/D` |
| gamification.badge.survey.user | Surveys / User                            | `R/W/C/D` |
| Badge Manager                  | Access Rights                             | `R/W/C/D` |
| Badge Portal                   | Role / Portal                             | `R`       |
| Badge Public                   | Role / Public                             | `R`       |
| Badge Employee                 | Role / User                               | `R`       |

### 🗃️ `gamification.challenge` — Gamification Challenge

> 📧 Mail Thread

Gamification challenge

    Set of predifined objectives assigned to people with rules for recurrence and
    rewards

    If 'user_ids' is defined and 'period' is different than 'one', the set will
    be assigned to the users for each period (eg: every 1st of each month if
    'monthly' is selected)

**Fields:**

| Field                        | Label                                           | Type        | Req | Store | Relation                    |
| ---------------------------- | ----------------------------------------------- | ----------- | --- | ----- | --------------------------- |
| `challenge_category`         | Appears in                                      | `selection` | ✅  | ✅    |                             |
| `create_date`                | Created on                                      | `datetime`  |     | ✅    |                             |
| `create_uid`                 | Created by                                      | `many2one`  |     | ✅    | res.users                   |
| `description`                | Description                                     | `text`      |     | ✅    |                             |
| `display_name`               | Display Name                                    | `char`      |     |       |                             |
| `end_date`                   | End Date                                        | `date`      |     | ✅    |                             |
| `has_message`                | Has Message                                     | `boolean`   |     |       |                             |
| `id`                         | ID                                              | `integer`   |     | ✅    |                             |
| `invited_user_ids`           | Suggest to users                                | `many2many` |     | ✅    | res.users                   |
| `last_report_date`           | Last Report Date                                | `date`      |     | ✅    |                             |
| `line_ids`                   | Lines                                           | `one2many`  | ✅  | ✅    | gamification.challenge.line |
| `manager_id`                 | Responsible                                     | `many2one`  |     | ✅    | res.users                   |
| `message_attachment_count`   | Attachment Count                                | `integer`   |     |       |                             |
| `message_follower_ids`       | Followers                                       | `one2many`  |     | ✅    | mail.followers              |
| `message_has_error`          | Message Delivery error                          | `boolean`   |     |       |                             |
| `message_has_error_counter`  | Number of errors                                | `integer`   |     |       |                             |
| `message_has_sms_error`      | SMS Delivery error                              | `boolean`   |     |       |                             |
| `message_ids`                | Messages                                        | `one2many`  |     | ✅    | mail.message                |
| `message_is_follower`        | Is Follower                                     | `boolean`   |     |       |                             |
| `message_needaction`         | Action Needed                                   | `boolean`   |     |       |                             |
| `message_needaction_counter` | Number of Actions                               | `integer`   |     |       |                             |
| `message_partner_ids`        | Followers (Partners)                            | `many2many` |     |       | res.partner                 |
| `name`                       | Challenge Name                                  | `char`      | ✅  | ✅    |                             |
| `next_report_date`           | Next Report Date                                | `date`      |     | ✅    |                             |
| `period`                     | Periodicity                                     | `selection` | ✅  | ✅    |                             |
| `rating_ids`                 | Ratings                                         | `one2many`  |     | ✅    | rating.rating               |
| `remind_update_delay`        | Non-updated manual goals will be reminded after | `integer`   |     | ✅    |                             |
| `report_message_frequency`   | Report Frequency                                | `selection` | ✅  | ✅    |                             |
| `report_message_group_id`    | Send a copy to                                  | `many2one`  |     | ✅    | discuss.channel             |
| `report_template_id`         | Report Template                                 | `many2one`  | ✅  | ✅    | mail.template               |
| `reward_failure`             | Reward Bests if not Succeeded?                  | `boolean`   |     | ✅    |                             |
| `reward_first_id`            | For 1st user                                    | `many2one`  |     | ✅    | gamification.badge          |
| `reward_id`                  | For Every Succeeding User                       | `many2one`  |     | ✅    | gamification.badge          |
| `reward_realtime`            | Reward as soon as every goal is reached         | `boolean`   |     | ✅    |                             |
| `reward_second_id`           | For 2nd user                                    | `many2one`  |     | ✅    | gamification.badge          |
| `reward_third_id`            | For 3rd user                                    | `many2one`  |     | ✅    | gamification.badge          |
| `start_date`                 | Start Date                                      | `date`      |     | ✅    |                             |
| `state`                      | State                                           | `selection` | ✅  | ✅    |                             |
| `user_count`                 | # Users                                         | `integer`   |     |       |                             |
| `user_domain`                | User domain                                     | `char`      |     | ✅    |                             |
| `user_ids`                   | Participants                                    | `many2many` |     | ✅    | res.users                   |
| `visibility_mode`            | Display Mode                                    | `selection` | ✅  | ✅    |                             |
| `website_message_ids`        | Website Messages                                | `one2many`  |     | ✅    | mail.message                |
| `write_date`                 | Last Updated on                                 | `datetime`  |     | ✅    |                             |
| `write_uid`                  | Last Updated by                                 | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                    | Group                                     | Perms     |
| ----------------------- | ----------------------------------------- | --------- |
| Challenge Officer       | Employees / Officer: Manage all employees | `R/W/C/D` |
| Goal Challenge Manager  | Access Rights                             | `R/W/C/D` |
| Goal Challenge Portal   | Role / Portal                             | `R`       |
| Goal Challenge Employee | Role / User                               | `R`       |

### 🗃️ `gamification.badge.user` — Gamification User Badge

> 📧 Mail Thread

User having received a badge

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation               |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ---------------------- |
| `badge_id`                   | Badge                  | `many2one`  | ✅  | ✅    | gamification.badge     |
| `badge_name`                 | Badge Name             | `char`      |     |       |                        |
| `challenge_id`               | Challenge              | `many2one`  |     | ✅    | gamification.challenge |
| `comment`                    | Comment                | `text`      |     | ✅    |                        |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                        |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users              |
| `display_name`               | Display Name           | `char`      |     |       |                        |
| `employee_id`                | Employee               | `many2one`  |     | ✅    | hr.employee            |
| `has_edit_delete_access`     | Has Edit Delete Access | `boolean`   |     |       |                        |
| `has_message`                | Has Message            | `boolean`   |     |       |                        |
| `id`                         | ID                     | `integer`   |     | ✅    |                        |
| `level`                      | Badge Level            | `selection` |     | ✅    |                        |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                        |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers         |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                        |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                        |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                        |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message           |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                        |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                        |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                        |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner            |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating          |
| `sender_id`                  | Sender                 | `many2one`  |     | ✅    | res.users              |
| `user_id`                    | User                   | `many2one`  | ✅  | ✅    | res.users              |
| `user_partner_id`            | Related Partner        | `many2one`  |     |       | res.partner            |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message           |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                        |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                | Group                                     | Perms     |
| ------------------- | ----------------------------------------- | --------- |
| Badge-user Officer  | Employees / Officer: Manage all employees | `R/W/C/D` |
| Badge-user Manager  | Access Rights                             | `R/W/C/D` |
| Badge-user Portal   | Role / Portal                             | `R/W/C`   |
| Badge-user Public   | Role / Public                             | `R`       |
| Badge-user Employee | Role / User                               | `R/W/C`   |
| Badge-user Employee | Role / User                               | `R/W/C/D` |

**Record Rules:**

- **Base group user granted badge write/unlink access** (1) `R/W/C/D`
  - Domain: `[('create_uid', '=', user.id)]`
- **Base group user not granted badge write/unlink access** (1) `R/C`
  - Domain: `[('create_uid', '!=', user.id)]`
- **Officer: Manage all employees- Badge Access** (49) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `gamification.challenge.line` — Gamification generic goal for challenge

Gamification challenge line

    Predefined goal for 'gamification_challenge'
    These are generic list of goals with only the target goal defined
    Should only be created for the gamification.challenge object

**Fields:**

| Field                    | Label                 | Type        | Req | Store | Relation                     |
| ------------------------ | --------------------- | ----------- | --- | ----- | ---------------------------- |
| `challenge_id`           | Challenge             | `many2one`  | ✅  | ✅    | gamification.challenge       |
| `condition`              | Condition             | `selection` |     |       |                              |
| `create_date`            | Created on            | `datetime`  |     | ✅    |                              |
| `create_uid`             | Created by            | `many2one`  |     | ✅    | res.users                    |
| `definition_full_suffix` | Suffix                | `char`      |     |       |                              |
| `definition_id`          | Goal Definition       | `many2one`  | ✅  | ✅    | gamification.goal.definition |
| `definition_monetary`    | Monetary              | `boolean`   |     |       |                              |
| `definition_suffix`      | Unit                  | `char`      |     |       |                              |
| `display_name`           | Display Name          | `char`      |     |       |                              |
| `id`                     | ID                    | `integer`   |     | ✅    |                              |
| `name`                   | Name                  | `char`      |     |       |                              |
| `sequence`               | Sequence              | `integer`   |     | ✅    |                              |
| `target_goal`            | Target Value to Reach | `float`     | ✅  | ✅    |                              |
| `write_date`             | Last Updated on       | `datetime`  |     | ✅    |                              |
| `write_uid`              | Last Updated by       | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                    | Group                                     | Perms     |
| ----------------------- | ----------------------------------------- | --------- |
| Challenge Line Officer  | Employees / Officer: Manage all employees | `R/W/C/D` |
| Challenge Line Manager  | Access Rights                             | `R/W/C/D` |
| Challenge Line Portal   | Role / Portal                             | `R`       |
| Challenge Line Employee | Role / User                               | `R`       |

### 🗃️ `gamification.goal` — Gamification Goal

Goal instance for a user

    An individual goal for a user on a specified time period

**Fields:**

| Field                    | Label                  | Type        | Req | Store | Relation                     |
| ------------------------ | ---------------------- | ----------- | --- | ----- | ---------------------------- |
| `challenge_id`           | Challenge              | `many2one`  |     | ✅    | gamification.challenge       |
| `closed`                 | Closed goal            | `boolean`   |     | ✅    |                              |
| `color`                  | Color Index            | `integer`   |     |       |                              |
| `completeness`           | Completeness           | `float`     |     |       |                              |
| `computation_mode`       | Computation Mode       | `selection` |     |       |                              |
| `create_date`            | Created on             | `datetime`  |     | ✅    |                              |
| `create_uid`             | Created by             | `many2one`  |     | ✅    | res.users                    |
| `current`                | Current Value          | `float`     | ✅  | ✅    |                              |
| `definition_condition`   | Definition Condition   | `selection` |     |       |                              |
| `definition_description` | Definition Description | `text`      |     |       |                              |
| `definition_display`     | Display Mode           | `selection` |     |       |                              |
| `definition_id`          | Goal Definition        | `many2one`  | ✅  | ✅    | gamification.goal.definition |
| `definition_suffix`      | Suffix                 | `char`      |     |       |                              |
| `display_name`           | Display Name           | `char`      |     |       |                              |
| `end_date`               | End Date               | `date`      |     | ✅    |                              |
| `id`                     | ID                     | `integer`   |     | ✅    |                              |
| `last_update`            | Last Update            | `date`      |     | ✅    |                              |
| `line_id`                | Challenge Line         | `many2one`  |     | ✅    | gamification.challenge.line  |
| `remind_update_delay`    | Remind delay           | `integer`   |     | ✅    |                              |
| `start_date`             | Start Date             | `date`      |     | ✅    |                              |
| `state`                  | State                  | `selection` | ✅  | ✅    |                              |
| `target_goal`            | To Reach               | `float`     | ✅  | ✅    |                              |
| `to_update`              | To update              | `boolean`   |     | ✅    |                              |
| `user_id`                | User                   | `many2one`  | ✅  | ✅    | res.users                    |
| `user_partner_id`        | Related Partner        | `many2one`  |     |       | res.partner                  |
| `write_date`             | Last Updated on        | `datetime`  |     | ✅    |                              |
| `write_uid`              | Last Updated by        | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name          | Group         | Perms     |
| ------------- | ------------- | --------- |
| Goal Manager  | Access Rights | `R/W/C/D` |
| Goal Portal   | Role / Portal | `R/W`     |
| Goal Employee | Role / User   | `R/W`     |

**Record Rules:**

- **User can only see his/her goals or goal from the same challenge in board
  visibility** (10, 1) `R/W`
  - Domain:
    `[             '|',                 ('user_id','=',user.id),                 '&',                     ('challenge_id.user_ids','in',user.id),                     ('challenge_id.visibility_mode','=','ranking')]`
- **Manager can see any goal** (2) `R/W`
  - Domain: `[(1, '=', 1)]`
- **Multicompany rule on challenges** (Global) `R/W/C/D`
  - Domain: `[('user_id.company_id', 'in', company_ids)]`
- **HR Officer can see any goal** (49) `R/W`

### 🗃️ `gamification.goal.definition` — Gamification Goal Definition

Goal definition

    A goal definition contains the way to evaluate an objective
    Each module wanting to be able to set goals to the users needs to create
    a new gamification_goal_definition

**Fields:**

| Field                     | Label                               | Type        | Req | Store | Relation              |
| ------------------------- | ----------------------------------- | ----------- | --- | ----- | --------------------- |
| `action_id`               | Action                              | `many2one`  |     | ✅    | ir.actions.act_window |
| `batch_distinctive_field` | Distinctive field for batch user    | `many2one`  |     | ✅    | ir.model.fields       |
| `batch_mode`              | Batch Mode                          | `boolean`   |     | ✅    |                       |
| `batch_user_expression`   | Evaluated expression for batch mode | `char`      |     | ✅    |                       |
| `computation_mode`        | Computation Mode                    | `selection` | ✅  | ✅    |                       |
| `compute_code`            | Python Code                         | `text`      |     | ✅    |                       |
| `condition`               | Goal Performance                    | `selection` | ✅  | ✅    |                       |
| `create_date`             | Created on                          | `datetime`  |     | ✅    |                       |
| `create_uid`              | Created by                          | `many2one`  |     | ✅    | res.users             |
| `description`             | Goal Description                    | `text`      |     | ✅    |                       |
| `display_mode`            | Displayed as                        | `selection` | ✅  | ✅    |                       |
| `display_name`            | Display Name                        | `char`      |     |       |                       |
| `domain`                  | Filter Domain                       | `char`      | ✅  | ✅    |                       |
| `field_date_id`           | Date Field                          | `many2one`  |     | ✅    | ir.model.fields       |
| `field_id`                | Field to Sum                        | `many2one`  |     | ✅    | ir.model.fields       |
| `full_suffix`             | Full Suffix                         | `char`      |     |       |                       |
| `id`                      | ID                                  | `integer`   |     | ✅    |                       |
| `model_id`                | Model                               | `many2one`  |     | ✅    | ir.model              |
| `model_inherited_ids`     | Inherited models                    | `many2many` |     |       | ir.model              |
| `monetary`                | Monetary Value                      | `boolean`   |     | ✅    |                       |
| `name`                    | Goal Definition                     | `char`      | ✅  | ✅    |                       |
| `res_id_field`            | ID Field of user                    | `char`      |     | ✅    |                       |
| `suffix`                  | Suffix                              | `char`      |     | ✅    |                       |
| `write_date`              | Last Updated on                     | `datetime`  |     | ✅    |                       |
| `write_uid`               | Last Updated by                     | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                     | Group         | Perms     |
| ------------------------ | ------------- | --------- |
| Goal Definition Manager  | Access Rights | `R/W/C/D` |
| Goal Definition Portal   | Role / Portal | `R`       |
| Goal Definition Employee | Role / User   | `R`       |

### 🗃️ `gamification.goal.wizard` — Gamification Goal Wizard

> ✳️ Transient (Wizard)

Wizard to update a manual goal

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation          |
| -------------- | --------------- | ---------- | --- | ----- | ----------------- |
| `create_date`  | Created on      | `datetime` |     | ✅    |                   |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users         |
| `current`      | Current         | `float`    |     | ✅    |                   |
| `display_name` | Display Name    | `char`     |     |       |                   |
| `goal_id`      | Goal            | `many2one` | ✅  | ✅    | gamification.goal |
| `id`           | ID              | `integer`  |     | ✅    |                   |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                   |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users         |

**Access Rights:**

| Name                            | Group       | Perms   |
| ------------------------------- | ----------- | ------- |
| access.gamification.goal.wizard | Role / User | `R/W/C` |

### 🗃️ `gamification.badge.user.wizard` — Gamification User Badge Wizard

> ✳️ Transient (Wizard)

Wizard allowing to grant a badge to a user

**Fields:**

| Field          | Label           | Type       | Req | Store | Relation           |
| -------------- | --------------- | ---------- | --- | ----- | ------------------ |
| `badge_id`     | Badge           | `many2one` | ✅  | ✅    | gamification.badge |
| `comment`      | Comment         | `text`     |     | ✅    |                    |
| `create_date`  | Created on      | `datetime` |     | ✅    |                    |
| `create_uid`   | Created by      | `many2one` |     | ✅    | res.users          |
| `display_name` | Display Name    | `char`     |     |       |                    |
| `employee_id`  | Employee        | `many2one` |     | ✅    | hr.employee        |
| `id`           | ID              | `integer`  |     | ✅    |                    |
| `user_id`      | User            | `many2one` | ✅  | ✅    | res.users          |
| `write_date`   | Last Updated on | `datetime` |     | ✅    |                    |
| `write_uid`    | Last Updated by | `many2one` |     | ✅    | res.users          |

**Access Rights:**

| Name                                  | Group       | Perms   |
| ------------------------------------- | ----------- | ------- |
| access.gamification.badge.user.wizard | Role / User | `R/W/C` |

### 🗃️ `gamification.karma.rank` — Rank based on karma

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                      | Label           | Type       | Req | Store | Relation  |
| -------------------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`              | Created on      | `datetime` |     | ✅    |           |
| `create_uid`               | Created by      | `many2one` |     | ✅    | res.users |
| `description`              | Description     | `html`     |     | ✅    |           |
| `description_motivational` | Motivational    | `html`     |     | ✅    |           |
| `display_name`             | Display Name    | `char`     |     |       |           |
| `id`                       | ID              | `integer`  |     | ✅    |           |
| `image_1024`               | Image 1024      | `binary`   |     | ✅    |           |
| `image_128`                | Image 128       | `binary`   |     | ✅    |           |
| `image_1920`               | Image           | `binary`   |     | ✅    |           |
| `image_256`                | Image 256       | `binary`   |     | ✅    |           |
| `image_512`                | Image 512       | `binary`   |     | ✅    |           |
| `karma_min`                | Required Karma  | `integer`  | ✅  | ✅    |           |
| `name`                     | Rank Name       | `text`     | ✅  | ✅    |           |
| `rank_users_count`         | # Users         | `integer`  |     |       |           |
| `user_ids`                 | Users           | `one2many` |     | ✅    | res.users |
| `write_date`               | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`                | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                                                     | Group                       | Perms     |
| -------------------------------------------------------- | --------------------------- | --------- |
| gamification.karma.rank.access.website.restricted_editor | Website / Restricted Editor | `R/W/C/D` |
| gamification.karma.rank.access.user.manager              | Role / Administrator        | `R/W/C/D` |
| gamification.karma.rank.access.all                       | Role / Portal               | `R`       |
| gamification.karma.rank.access.all                       | Role / Public               | `R`       |
| gamification.karma.rank.access.all                       | Role / User                 | `R`       |

### 🗃️ `gamification.karma.tracking` — Track Karma Changes

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                   | Label           | Type        | Req | Store | Relation  |
| ----------------------- | --------------- | ----------- | --- | ----- | --------- |
| `consolidated`          | Consolidated    | `boolean`   |     | ✅    |           |
| `create_date`           | Created on      | `datetime`  |     | ✅    |           |
| `create_uid`            | Created by      | `many2one`  |     | ✅    | res.users |
| `display_name`          | Display Name    | `char`      |     |       |           |
| `gain`                  | Gain            | `integer`   |     |       |           |
| `id`                    | ID              | `integer`   |     | ✅    |           |
| `new_value`             | New Karma Value | `integer`   | ✅  | ✅    |           |
| `old_value`             | Old Karma Value | `integer`   |     | ✅    |           |
| `origin_ref`            | Source          | `reference` |     | ✅    |           |
| `origin_ref_model_name` | Source Type     | `selection` |     | ✅    |           |
| `reason`                | Description     | `text`      |     | ✅    |           |
| `tracking_date`         | Tracking Date   | `datetime`  |     | ✅    |           |
| `user_id`               | User            | `many2one`  | ✅  | ✅    | res.users |
| `write_date`            | Last Updated on | `datetime`  |     | ✅    |           |
| `write_uid`             | Last Updated by | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                                            | Group                | Perms     |
| ----------------------------------------------- | -------------------- | --------- |
| gamification.karma.tracking.access.user.manager | Role / Administrator | `R/W/C/D` |
| gamification.karma.tracking.access.all          | Everyone             | `-`       |

### 🗃️ `res.users` — User

Update of res.users class - add a preference about username for livechat purpose

**Fields:**

| Field                                       | Label                                                 | Type         | Req | Store | Relation                    |
| ------------------------------------------- | ----------------------------------------------------- | ------------ | --- | ----- | --------------------------- |
| `accesses_count`                            | # Access Rights                                       | `integer`    |     |       |                             |
| `access_token`                              | Access Token                                          | `char`       |     | ✅    |                             |
| `account_move_count`                        | Account Move Count                                    | `integer`    |     |       |                             |
| `action_id`                                 | Home Action                                           | `many2one`   |     | ✅    | ir.actions.actions          |
| `active`                                    | Active                                                | `boolean`    |     | ✅    |                             |
| `active_lang_count`                         | Active Lang Count                                     | `integer`    |     |       |                             |
| `active_partner`                            | Partner is Active                                     | `boolean`    |     |       |                             |
| `activity_calendar_event_id`                | Next Activity Calendar Event                          | `many2one`   |     |       | calendar.event              |
| `activity_date_deadline`                    | Next Activity Deadline                                | `date`       |     |       |                             |
| `activity_exception_decoration`             | Activity Exception Decoration                         | `selection`  |     |       |                             |
| `activity_exception_icon`                   | Icon                                                  | `char`       |     |       |                             |
| `activity_ids`                              | Activities                                            | `one2many`   |     |       | mail.activity               |
| `activity_state`                            | Activity State                                        | `selection`  |     |       |                             |
| `activity_summary`                          | Next Activity Summary                                 | `char`       |     |       |                             |
| `activity_type_icon`                        | Activity Type Icon                                    | `char`       |     |       |                             |
| `activity_type_id`                          | Next Activity Type                                    | `many2one`   |     |       | mail.activity.type          |
| `activity_user_id`                          | Responsible User                                      | `many2one`   |     |       | res.users                   |
| `additional_note`                           | Additional Note                                       | `text`       |     |       |                             |
| `all_group_ids`                             | Groups and implied groups                             | `many2many`  |     |       | res.groups                  |
| `api_key_ids`                               | API Keys                                              | `one2many`   |     | ✅    | res.users.apikeys           |
| `applicant_ids`                             | Applicants                                            | `one2many`   |     |       | hr.applicant                |
| `application_count`                         | Applications                                          | `integer`    |     |       |                             |
| `application_statistics`                    | Stats                                                 | `json`       |     |       |                             |
| `auth_passkey_key_ids`                      | Auth Passkey Key                                      | `one2many`   |     | ✅    | auth.passkey.key            |
| `autopost_bills`                            | Auto-post bills                                       | `selection`  | ✅  |       |                             |
| `available_invoice_template_pdf_report_ids` | Available Invoice Template Pdf Report                 | `one2many`   |     |       | ir.actions.report           |
| `available_peppol_eas`                      | Available Peppol Eas                                  | `json`       |     |       |                             |
| `avatar_1024`                               | Avatar 1024                                           | `binary`     |     |       |                             |
| `avatar_128`                                | Avatar 128                                            | `binary`     |     |       |                             |
| `avatar_1920`                               | Avatar                                                | `binary`     |     |       |                             |
| `avatar_256`                                | Avatar 256                                            | `binary`     |     |       |                             |
| `avatar_512`                                | Avatar 512                                            | `binary`     |     |       |                             |
| `badge_ids`                                 | Badges                                                | `one2many`   |     | ✅    | gamification.badge.user     |
| `bank_account_count`                        | Bank                                                  | `integer`    |     |       |                             |
| `bank_account_ids`                          | Bank Accounts                                         | `many2many`  |     |       | res.partner.bank            |
| `bank_ids`                                  | Banks                                                 | `one2many`   |     |       | res.partner.bank            |
| `barcode`                                   | Badge ID                                              | `char`       |     |       |                             |
| `bronze_badge`                              | Bronze badges count                                   | `integer`    |     |       |                             |
| `buyer_id`                                  | Buyer                                                 | `many2one`   |     |       | res.users                   |
| `calendar_default_privacy`                  | Calendar Default Privacy                              | `selection`  |     |       |                             |
| `calendar_last_notif_ack`                   | Last notification marked as read from base Calendar   | `datetime`   |     |       |                             |
| `can_edit_role`                             | Can Edit Role                                         | `boolean`    |     |       |                             |
| `can_publish`                               | Can Publish                                           | `boolean`    |     |       |                             |
| `category_id`                               | Tags                                                  | `many2many`  |     |       | res.partner.category        |
| `category_ids`                              | Employee Tags                                         | `many2many`  |     |       | hr.employee.category        |
| `certifications_company_count`              | Company Certifications Count                          | `integer`    |     |       |                             |
| `certifications_count`                      | Certifications Count                                  | `integer`    |     |       |                             |
| `channel_ids`                               | Channels                                              | `many2many`  |     |       | discuss.channel             |
| `channel_member_ids`                        | Channel Member                                        | `one2many`   |     |       | discuss.channel.member      |
| `chatbot_script_ids`                        | Chatbot Script                                        | `one2many`   |     |       | chatbot.script              |
| `chatter_position`                          | Chatter Position                                      | `selection`  |     | ✅    |                             |
| `child_ids`                                 | Childs                                                | `many2many`  |     | ✅    | res.users                   |
| `city`                                      | City                                                  | `char`       |     |       |                             |
| `client_id`                                 | Client ID                                             | `char`       |     | ✅    |                             |
| `client_secret`                             | Client Secret                                         | `char`       |     | ✅    |                             |
| `code`                                      | Company Code                                          | `char`       |     |       |                             |
| `color`                                     | Color Index                                           | `integer`    |     |       |                             |
| `comment`                                   | Notes                                                 | `html`       |     |       |                             |
| `commercial_company_name`                   | Company Name Entity                                   | `char`       |     |       |                             |
| `commercial_partner_id`                     | Commercial Entity                                     | `many2one`   |     |       | res.partner                 |
| `companies_count`                           | Number of Companies                                   | `integer`    |     |       |                             |
| `company_id`                                | Company                                               | `many2one`   | ✅  | ✅    | res.company                 |
| `company_ids`                               | Companies                                             | `many2many`  |     | ✅    | res.company                 |
| `company_name`                              | Company Name                                          | `char`       |     |       |                             |
| `company_registry`                          | Company ID                                            | `char`       |     |       |                             |
| `company_registry_label`                    | Company ID Label                                      | `char`       |     |       |                             |
| `company_registry_placeholder`              | Company Registry Placeholder                          | `char`       |     |       |                             |
| `company_type`                              | Company Type                                          | `selection`  |     |       |                             |
| `complete_name`                             | Complete Name                                         | `char`       |     |       |                             |
| `contact_address`                           | Complete Address                                      | `char`       |     |       |                             |
| `contact_address_inline`                    | Inlined Complete Address                              | `char`       |     |       |                             |
| `contract_ids`                              | Partner Contracts                                     | `one2many`   |     |       | account.analytic.account    |
| `country_code`                              | Country Code                                          | `char`       |     |       |                             |
| `country_id`                                | Country                                               | `many2one`   |     |       | res.country                 |
| `create_date`                               | Create Date                                           | `datetime`   |     | ✅    |                             |
| `create_employee`                           | Technical field, whether to create an employee        | `boolean`    |     |       |                             |
| `create_employee_id`                        | Technical field, bind user to this employee on create | `many2one`   |     |       | hr.employee                 |
| `create_uid`                                | Created by                                            | `many2one`   |     | ✅    | res.users                   |
| `credit`                                    | Total Receivable                                      | `monetary`   |     |       |                             |
| `credit_limit`                              | Credit Limit                                          | `float`      |     |       |                             |
| `credit_to_invoice`                         | Credit To Invoice                                     | `monetary`   |     |       |                             |
| `crm_team_ids`                              | Sales Teams                                           | `many2many`  |     |       | crm.team                    |
| `crm_team_member_ids`                       | Sales Team Members                                    | `one2many`   |     | ✅    | crm.team.member             |
| `currency_id`                               | Currency                                              | `many2one`   |     |       | res.currency                |
| `customer_rank`                             | Customer Rank                                         | `integer`    |     |       |                             |
| `dark_mode`                                 | Dark Mode                                             | `boolean`    |     | ✅    |                             |
| `days_sales_outstanding`                    | Days Sales Outstanding (DSO)                          | `float`      |     |       |                             |
| `debit`                                     | Total Payable                                         | `monetary`   |     |       |                             |
| `department_count`                          | Number of Departments                                 | `integer`    |     |       |                             |
| `department_ids`                            | Allowed Department                                    | `many2many`  |     | ✅    | op.department               |
| `dept_id`                                   | Department Name                                       | `many2one`   |     | ✅    | op.department               |
| `device_ids`                                | User devices                                          | `one2many`   |     | ✅    | res.device                  |
| `display_invoice_edi_format`                | Display Invoice Edi Format                            | `boolean`    |     |       |                             |
| `display_invoice_template_pdf_report_id`    | Display Invoice Template Pdf Report                   | `boolean`    |     |       |                             |
| `display_name`                              | Display Name                                          | `char`       |     |       |                             |
| `duplicate_bank_partner_ids`                | Duplicate Bank Partner                                | `many2many`  |     |       | res.partner                 |
| `email`                                     | Email                                                 | `char`       |     |       |                             |
| `email_domain_placeholder`                  | Email Domain Placeholder                              | `char`       |     |       |                             |
| `email_formatted`                           | Formatted Email                                       | `char`       |     |       |                             |
| `email_normalized`                          | Normalized Email                                      | `char`       |     |       |                             |
| `emergency_contact`                         | Emergency Contact                                     | `char`       |     |       |                             |
| `emergency_phone`                           | Emergency Phone                                       | `char`       |     |       |                             |
| `employee`                                  | Employee                                              | `boolean`    |     |       |                             |
| `employee_bank_account_ids`                 | Employee's Bank Accounts                              | `many2many`  |     |       | res.partner.bank            |
| `employee_count`                            | Employee Count                                        | `integer`    |     |       |                             |
| `employee_id`                               | Company employee                                      | `many2one`   |     |       | hr.employee                 |
| `employee_ids`                              | Related employee                                      | `one2many`   |     | ✅    | hr.employee                 |
| `employee_resource_calendar_id`             | Employee's Working Hours                              | `many2one`   |     |       | resource.calendar           |
| `employees_count`                           | Employees Count                                       | `integer`    |     |       |                             |
| `esign_initials`                            | Digitial Initials                                     | `binary`     |     | ✅    |                             |
| `esign_signature`                           | Digital Signature                                     | `binary`     |     | ✅    |                             |
| `event_count`                               | # Events                                              | `integer`    |     |       |                             |
| `fiscal_country_codes`                      | Fiscal Country Codes                                  | `char`       |     |       |                             |
| `fiscal_country_group_codes`                | Fiscal Country Group Codes                            | `json`       |     |       |                             |
| `friday_location_id`                        | Fridays                                               | `many2one`   |     |       | hr.work.location            |
| `function`                                  | Job Position                                          | `char`       |     |       |                             |
| `global_location_number`                    | GLN                                                   | `char`       |     |       |                             |
| `goal_ids`                                  | Goal                                                  | `one2many`   |     | ✅    | gamification.goal           |
| `gold_badge`                                | Gold badges count                                     | `integer`    |     |       |                             |
| `grievance_team_id`                         | Grievance Team                                        | `many2one`   |     | ✅    | grievance.team              |
| `group_ids`                                 | Groups                                                | `many2many`  |     | ✅    | res.groups                  |
| `group_on`                                  | Week Day                                              | `selection`  | ✅  |       |                             |
| `group_rfq`                                 | Group RFQ                                             | `selection`  | ✅  |       |                             |
| `groups_count`                              | # Groups                                              | `integer`    |     |       |                             |
| `has_access_livechat`                       | Has access to Livechat                                | `boolean`    |     |       |                             |
| `has_external_mail_server`                  | Has External Mail Server                              | `boolean`    |     |       |                             |
| `has_message`                               | Has Message                                           | `boolean`    |     |       |                             |
| `head_office`                               | Head Office                                           | `char`       |     |       |                             |
| `hr_contact`                                | HR Contact                                            | `char`       |     |       |                             |
| `hr_email`                                  | HR Email                                              | `char`       |     |       |                             |
| `hr_name`                                   | HR Name                                               | `char`       |     |       |                             |
| `id`                                        | ID                                                    | `integer`    |     | ✅    |                             |
| `ignore_abnormal_invoice_amount`            | Ignore Abnormal Invoice Amount                        | `boolean`    |     |       |                             |
| `ignore_abnormal_invoice_date`              | Ignore Abnormal Invoice Date                          | `boolean`    |     |       |                             |
| `image_1024`                                | Image 1024                                            | `binary`     |     |       |                             |
| `image_128`                                 | Image 128                                             | `binary`     |     |       |                             |
| `image_1920`                                | Image                                                 | `binary`     |     |       |                             |
| `image_256`                                 | Image 256                                             | `binary`     |     |       |                             |
| `image_512`                                 | Image 512                                             | `binary`     |     |       |                             |
| `im_status`                                 | IM Status                                             | `char`       |     |       |                             |
| `industry_id`                               | Industry                                              | `many2one`   |     |       | res.partner.industry        |
| `invoice_edi_format`                        | eInvoice format                                       | `selection`  |     |       |                             |
| `invoice_edi_format_store`                  | Invoice Edi Format Store                              | `char`       |     |       |                             |
| `invoice_ids`                               | Invoices                                              | `one2many`   |     |       | account.move                |
| `invoice_sending_method`                    | Invoice sending                                       | `selection`  |     |       |                             |
| `invoice_template_pdf_report_id`            | Invoice report                                        | `many2one`   |     |       | ir.actions.report           |
| `is_blacklisted`                            | Blacklist                                             | `boolean`    |     |       |                             |
| `is_company`                                | Is a Company                                          | `boolean`    |     |       |                             |
| `is_hr_user`                                | Is Hr User                                            | `boolean`    |     |       |                             |
| `is_in_call`                                | Is in call                                            | `boolean`    |     |       |                             |
| `is_out_of_office`                          | Out of Office                                         | `boolean`    |     |       |                             |
| `is_parent`                                 | Is a Parent                                           | `boolean`    |     |       |                             |
| `is_peppol_edi_format`                      | Is Peppol Edi Format                                  | `boolean`    |     |       |                             |
| `is_pickup_location`                        | Is Pickup Location                                    | `boolean`    |     |       |                             |
| `is_public`                                 | Is Public                                             | `boolean`    |     |       |                             |
| `is_published`                              | Is Published                                          | `boolean`    |     |       |                             |
| `is_seo_optimized`                          | SEO optimized                                         | `boolean`    |     |       |                             |
| `is_student`                                | Is a Student                                          | `boolean`    |     |       |                             |
| `is_system`                                 | Is System                                             | `boolean`    |     |       |                             |
| `is_ubl_format`                             | Is Ubl Format                                         | `boolean`    |     |       |                             |
| `is_venue`                                  | Venue                                                 | `boolean`    |     |       |                             |
| `job_title`                                 | Job Title                                             | `char`       |     |       |                             |
| `karma`                                     | Karma                                                 | `integer`    |     | ✅    |                             |
| `karma_tracking_ids`                        | Karma Changes                                         | `one2many`   |     | ✅    | gamification.karma.tracking |
| `km_home_work`                              | Home-Work Distance in Km                              | `integer`    |     |       |                             |
| `lang`                                      | Language                                              | `selection`  |     |       |                             |
| `leave_date_to`                             | To Date                                               | `date`       |     |       |                             |
| `livechat_channel_count`                    | Livechat Channel Count                                | `integer`    |     |       |                             |
| `livechat_channel_ids`                      | Livechat Channel                                      | `many2many`  |     | ✅    | im_livechat.channel         |
| `livechat_expertise_ids`                    | Live Chat Expertise                                   | `many2many`  |     |       | im_livechat.expertise       |
| `livechat_is_in_call`                       | Livechat Is In Call                                   | `boolean`    |     |       |                             |
| `livechat_lang_ids`                         | Livechat Languages                                    | `many2many`  |     |       | res.lang                    |
| `livechat_ongoing_session_count`            | Number of Ongoing sessions                            | `integer`    |     |       |                             |
| `livechat_username`                         | Livechat Username                                     | `char`       |     |       |                             |
| `log_ids`                                   | User log entries                                      | `one2many`   |     | ✅    | res.users.log               |
| `login`                                     | Login                                                 | `char`       | ✅  | ✅    |                             |
| `login_date`                                | Latest Login                                          | `datetime`   |     |       |                             |
| `logo_visible`                              | Show Company Logo in Sidebar                          | `boolean`    |     | ✅    |                             |
| `main_user_id`                              | Main User                                             | `many2one`   |     |       | res.users                   |
| `manual_im_status`                          | IM status manually set by the user                    | `selection`  |     | ✅    |                             |
| `meeting_count`                             | # Meetings                                            | `integer`    |     |       |                             |
| `meeting_ids`                               | Meetings                                              | `many2many`  |     |       | calendar.event              |
| `message_attachment_count`                  | Attachment Count                                      | `integer`    |     |       |                             |
| `message_bounce`                            | Bounce                                                | `integer`    |     |       |                             |
| `message_follower_ids`                      | Followers                                             | `one2many`   |     |       | mail.followers              |
| `message_has_error`                         | Message Delivery error                                | `boolean`    |     |       |                             |
| `message_has_error_counter`                 | Number of errors                                      | `integer`    |     |       |                             |
| `message_has_sms_error`                     | SMS Delivery error                                    | `boolean`    |     |       |                             |
| `message_ids`                               | Messages                                              | `one2many`   |     |       | mail.message                |
| `message_is_follower`                       | Is Follower                                           | `boolean`    |     |       |                             |
| `message_needaction`                        | Action Needed                                         | `boolean`    |     |       |                             |
| `message_needaction_counter`                | Number of Actions                                     | `integer`    |     |       |                             |
| `message_partner_ids`                       | Followers (Partners)                                  | `many2many`  |     |       | res.partner                 |
| `mobile_phone`                              | Work Mobile                                           | `char`       |     |       |                             |
| `monday_location_id`                        | Mondays                                               | `many2one`   |     |       | hr.work.location            |
| `my_activity_date_deadline`                 | My Activity Deadline                                  | `date`       |     |       |                             |
| `name`                                      | Name                                                  | `char`       |     |       |                             |
| `new_password`                              | Set Password                                          | `char`       |     |       |                             |
| `next_rank_id`                              | Next Rank                                             | `many2one`   |     | ✅    | gamification.karma.rank     |
| `notification_type`                         | Notification                                          | `selection`  | ✅  | ✅    |                             |
| `odoobot_failed`                            | Odoobot Failed                                        | `boolean`    |     | ✅    |                             |
| `odoobot_state`                             | OdooBot Status                                        | `selection`  |     | ✅    |                             |
| `offline_since`                             | Offline since                                         | `datetime`   |     |       |                             |
| `onesignal_device_id`                       | One Signal Device ID                                  | `char`       |     | ✅    |                             |
| `on_time_rate`                              | On-Time Delivery Rate                                 | `float`      |     |       |                             |
| `opportunity_count`                         | Opportunity Count                                     | `integer`    |     |       |                             |
| `opportunity_ids`                           | Opportunities                                         | `one2many`   |     |       | crm.lead                    |
| `outgoing_mail_server_id`                   | Outgoing Mail Server                                  | `many2one`   |     |       | ir.mail_server              |
| `outgoing_mail_server_type`                 | Outgoing Mail Server Type                             | `selection`  | ✅  |       |                             |
| `out_of_office_from`                        | Out Of Office From                                    | `datetime`   |     | ✅    |                             |
| `out_of_office_message`                     | Vacation Responder                                    | `html`       |     | ✅    |                             |
| `out_of_office_to`                          | Out Of Office To                                      | `datetime`   |     | ✅    |                             |
| `parent_id`                                 | Related Company                                       | `many2one`   |     |       | res.partner                 |
| `parent_name`                               | Parent name                                           | `char`       |     |       |                             |
| `partner_company_registry_placeholder`      | Partner Company Registry Placeholder                  | `char`       |     |       |                             |
| `partner_id`                                | Related Partner                                       | `many2one`   | ✅  | ✅    | res.partner                 |
| `partner_latitude`                          | Geo Latitude                                          | `float`      |     |       |                             |
| `partner_longitude`                         | Geo Longitude                                         | `float`      |     |       |                             |
| `partner_share`                             | Share Partner                                         | `boolean`    |     |       |                             |
| `partner_vat_placeholder`                   | Partner Vat Placeholder                               | `char`       |     |       |                             |
| `password`                                  | Password                                              | `char`       |     |       |                             |
| `payment_token_count`                       | Payment Token Count                                   | `integer`    |     |       |                             |
| `payment_token_ids`                         | Payment Tokens                                        | `one2many`   |     |       | payment.token               |
| `peppol_eas`                                | Peppol e-address (EAS)                                | `selection`  |     |       |                             |
| `peppol_endpoint`                           | Peppol Endpoint                                       | `char`       |     |       |                             |
| `phone`                                     | Phone                                                 | `char`       |     |       |                             |
| `phone_blacklisted`                         | Blacklisted Phone is Phone                            | `boolean`    |     |       |                             |
| `phone_mobile_search`                       | Phone Number                                          | `char`       |     |       |                             |
| `phone_sanitized`                           | Sanitized Number                                      | `char`       |     |       |                             |
| `phone_sanitized_blacklisted`               | Phone Blacklisted                                     | `boolean`    |     |       |                             |
| `picking_warn_msg`                          | Message for Stock Picking                             | `text`       |     |       |                             |
| `pin`                                       | PIN                                                   | `char`       |     |       |                             |
| `pin_whatsapp_contact_id`                   | Pin Whatsapp Contact                                  | `char`       |     | ✅    |                             |
| `placement_team_id`                         | Placement Team Members                                | `many2one`   |     | ✅    | op.placement.cell           |
| `presence_ids`                              | Presence                                              | `one2many`   |     | ✅    | mail.presence               |
| `private_city`                              | Private City                                          | `char`       |     |       |                             |
| `private_country_id`                        | Private Country                                       | `many2one`   |     |       | res.country                 |
| `private_email`                             | Private Email                                         | `char`       |     |       |                             |
| `private_phone`                             | Private Phone                                         | `char`       |     |       |                             |
| `private_state_id`                          | Private State                                         | `many2one`   |     |       | res.country.state           |
| `private_street`                            | Private Street                                        | `char`       |     |       |                             |
| `private_street2`                           | Private Street2                                       | `char`       |     |       |                             |
| `private_zip`                               | Private Zip                                           | `char`       |     |       |                             |
| `properties`                                | Properties                                            | `properties` |     |       |                             |
| `properties_base_definition_id`             | Properties Base Definition                            | `many2one`   |     |       | properties.base.definition  |
| `property_account_payable_id`               | Account Payable                                       | `many2one`   |     |       | account.account             |
| `property_account_position_id`              | Fiscal Position                                       | `many2one`   |     |       | account.fiscal.position     |
| `property_account_receivable_id`            | Account Receivable                                    | `many2one`   |     |       | account.account             |
| `property_delivery_carrier_id`              | Delivery Method                                       | `many2one`   |     |       | delivery.carrier            |
| `property_inbound_payment_method_line_id`   | Property Inbound Payment Method Line                  | `many2one`   |     |       | account.payment.method.line |
| `property_outbound_payment_method_line_id`  | Property Outbound Payment Method Line                 | `many2one`   |     |       | account.payment.method.line |
| `property_payment_term_id`                  | Customer Payment Terms                                | `many2one`   |     |       | account.payment.term        |
| `property_product_pricelist`                | Pricelist                                             | `many2one`   |     |       | product.pricelist           |
| `property_purchase_currency_id`             | Supplier Currency                                     | `many2one`   |     |       | res.currency                |
| `property_stock_customer`                   | Customer Location                                     | `many2one`   |     |       | stock.location              |
| `property_stock_supplier`                   | Vendor Location                                       | `many2one`   |     |       | stock.location              |
| `property_supplier_payment_term_id`         | Vendor Payment Terms                                  | `many2one`   |     |       | account.payment.term        |
| `property_warehouse_id`                     | Default Warehouse                                     | `many2one`   |     | ✅    | stock.warehouse             |
| `purchase_line_ids`                         | Purchase Lines                                        | `one2many`   |     |       | purchase.order.line         |
| `purchase_order_count`                      | Purchase Order Count                                  | `integer`    |     |       |                             |
| `purchase_warn_msg`                         | Message for Purchase Order                            | `text`       |     |       |                             |
| `rank_id`                                   | Rank                                                  | `many2one`   |     | ✅    | gamification.karma.rank     |
| `rating_ids`                                | Ratings                                               | `one2many`   |     |       | rating.rating               |
| `receipt_reminder_email`                    | Receipt Reminder                                      | `boolean`    |     |       |                             |
| `ref`                                       | Reference                                             | `char`       |     |       |                             |
| `ref_company_ids`                           | Companies that refers to partner                      | `one2many`   |     |       | res.company                 |
| `refresh_token`                             | Refresh Token                                         | `char`       |     | ✅    |                             |
| `reminder_date_before_receipt`              | Days Before Receipt                                   | `integer`    |     |       |                             |
| `resource_calendar_id`                      | Default Working Hours                                 | `many2one`   |     |       | resource.calendar           |
| `resource_ids`                              | Resources                                             | `one2many`   |     | ✅    | resource.resource           |
| `res_users_settings_id`                     | Settings                                              | `many2one`   |     |       | res.users.settings          |
| `res_users_settings_ids`                    | Res Users Settings                                    | `one2many`   |     | ✅    | res.users.settings          |
| `role`                                      | Role                                                  | `selection`  |     |       |                             |
| `role_ids`                                  | User Roles                                            | `many2many`  |     | ✅    | res.role                    |
| `role_line_ids`                             | Role lines                                            | `one2many`   |     | ✅    | res.users.role.line         |
| `rtc_session_ids`                           | Rtc Session                                           | `one2many`   |     |       | discuss.channel.rtc.session |
| `rules_count`                               | # Record Rules                                        | `integer`    |     |       |                             |
| `sale_order_count`                          | Sale Order Count                                      | `integer`    |     |       |                             |
| `sale_order_ids`                            | Sales Order                                           | `one2many`   |     |       | sale.order                  |
| `sale_team_id`                              | User Sales Team                                       | `many2one`   |     | ✅    | crm.team                    |
| `sale_warn_msg`                             | Message for Sales Order                               | `text`       |     |       |                             |
| `same_company_registry_partner_id`          | Partner with same Company Registry                    | `many2one`   |     |       | res.partner                 |
| `same_vat_partner_id`                       | Partner with same Tax ID                              | `many2one`   |     |       | res.partner                 |
| `saturday_location_id`                      | Saturdays                                             | `many2one`   |     |       | hr.work.location            |
| `self`                                      | Self                                                  | `many2one`   |     |       | res.partner                 |
| `seo_name`                                  | Seo name                                              | `char`       |     |       |                             |
| `share`                                     | Share User                                            | `boolean`    |     | ✅    |                             |
| `show_alert`                                | Show Alert                                            | `boolean`    |     |       |                             |
| `show_credit_limit`                         | Show Credit Limit                                     | `boolean`    |     |       |                             |
| `signature`                                 | Email Signature                                       | `html`       |     | ✅    |                             |
| `signup_type`                               | Signup Token Type                                     | `char`       |     |       |                             |
| `silver_badge`                              | Silver badges count                                   | `integer`    |     |       |                             |
| `specific_property_product_pricelist`       | Specific Property Product Pricelist                   | `many2one`   |     |       | product.pricelist           |
| `state`                                     | Status                                                | `selection`  |     |       |                             |
| `state_id`                                  | State                                                 | `many2one`   |     |       | res.country.state           |
| `static_map_url`                            | Static Map Url                                        | `char`       |     |       |                             |
| `static_map_url_is_valid`                   | Static Map Url Is Valid                               | `boolean`    |     |       |                             |
| `street`                                    | Street                                                | `char`       |     |       |                             |
| `street2`                                   | Street2                                               | `char`       |     |       |                             |
| `student_line`                              | Line                                                  | `many2one`   |     | ✅    | op.student                  |
| `suggest_based_on`                          | Suggest Based On                                      | `char`       |     |       |                             |
| `suggest_days`                              | Suggest Days                                          | `integer`    |     |       |                             |
| `suggest_percent`                           | Suggest Percent                                       | `integer`    |     |       |                             |
| `sunday_location_id`                        | Sundays                                               | `many2one`   |     |       | hr.work.location            |
| `supplier_invoice_count`                    | # Vendor Bills                                        | `integer`    |     |       |                             |
| `supplier_rank`                             | Supplier Rank                                         | `integer`    |     |       |                             |
| `thursday_location_id`                      | Thursdays                                             | `many2one`   |     |       | hr.work.location            |
| `ticket_count`                              | Ticket Count                                          | `integer`    |     |       |                             |
| `title`                                     | Title                                                 | `many2one`   |     |       | res.partner.title           |
| `total_invoiced`                            | Total Invoiced                                        | `monetary`   |     |       |                             |
| `totp_enabled`                              | Two-factor authentication                             | `boolean`    |     |       |                             |
| `totp_last_counter`                         | Totp Last Counter                                     | `integer`    |     | ✅    |                             |
| `totp_secret`                               | Totp Secret                                           | `char`       |     |       |                             |
| `totp_trusted_device_ids`                   | Trusted Devices                                       | `one2many`   |     | ✅    | auth_totp.device            |
| `tour_enabled`                              | Onboarding                                            | `boolean`    |     | ✅    |                             |
| `trust`                                     | Degree of trust you have in this debtor               | `selection`  |     |       |                             |
| `tuesday_location_id`                       | Tuesdays                                              | `many2one`   |     |       | hr.work.location            |
| `type`                                      | Address Type                                          | `selection`  |     |       |                             |
| `type_address_label`                        | Address Type Description                              | `char`       |     |       |                             |
| `tz`                                        | Timezone                                              | `selection`  |     |       |                             |
| `tz_offset`                                 | Timezone offset                                       | `char`       |     |       |                             |
| `use_partner_credit_limit`                  | Partner Limit                                         | `boolean`    |     |       |                             |
| `user_id`                                   | Salesperson                                           | `many2one`   |     |       | res.users                   |
| `user_ids`                                  | Users                                                 | `one2many`   |     |       | res.users                   |
| `user_line`                                 | User Line                                             | `one2many`   |     | ✅    | op.student                  |
| `user_livechat_username`                    | User Livechat Username                                | `char`       |     |       |                             |
| `vat`                                       | Tax ID                                                | `char`       |     |       |                             |
| `vat_label`                                 | Tax ID Label                                          | `char`       |     |       |                             |
| `view_group_hierarchy`                      | Technical field for user group setting                | `json`       |     |       |                             |
| `visa_expire`                               | Visa Expiration Date                                  | `date`       |     |       |                             |
| `visitor_ids`                               | Visitors                                              | `one2many`   |     |       | website.visitor             |
| `website`                                   | Website Link                                          | `char`       |     |       |                             |
| `website_absolute_url`                      | Website Absolute URL                                  | `char`       |     |       |                             |
| `website_description`                       | Website Partner Full Description                      | `html`       |     |       |                             |
| `website_id`                                | Website                                               | `many2one`   |     | ✅    | website                     |
| `website_message_ids`                       | Website Messages                                      | `one2many`   |     |       | mail.message                |
| `website_meta_description`                  | Website meta description                              | `text`       |     |       |                             |
| `website_meta_keywords`                     | Website meta keywords                                 | `char`       |     |       |                             |
| `website_meta_og_img`                       | Website opengraph image                               | `char`       |     |       |                             |
| `website_meta_title`                        | Website meta title                                    | `char`       |     |       |                             |
| `website_published`                         | Visible on current website                            | `boolean`    |     |       |                             |
| `website_short_description`                 | Website Partner Short Description                     | `text`       |     |       |                             |
| `website_url`                               | Website URL                                           | `char`       |     |       |                             |
| `wednesday_location_id`                     | Wednesdays                                            | `many2one`   |     |       | hr.work.location            |
| `wishlist_ids`                              | Wishlist                                              | `one2many`   |     |       | product.wishlist            |
| `work_contact_id`                           | Work Contact                                          | `many2one`   |     |       | res.partner                 |
| `work_email`                                | Work Email                                            | `char`       |     |       |                             |
| `work_location_id`                          | Work Location                                         | `many2one`   |     |       | hr.work.location            |
| `work_location_name`                        | Work Location Name                                    | `char`       |     |       |                             |
| `work_location_type`                        | Work Location Type                                    | `selection`  |     |       |                             |
| `work_phone`                                | Work Phone                                            | `char`       |     |       |                             |
| `write_date`                                | Last Updated on                                       | `datetime`   |     | ✅    |                             |
| `write_uid`                                 | Last Updated by                                       | `many2one`   |     | ✅    | res.users                   |
| `zip`                                       | Zip                                                   | `char`       |     |       |                             |

**Access Rights:**

| Name                             | Group            | Perms     |
| -------------------------------- | ---------------- | --------- |
| access_op_placement_cell_res     | Placement / User | `R/W/C`   |
| name_res_users_back_office_admin | Parent / Manager | `R/W/C/D` |
| res_users group_erp_manager      | Access Rights    | `R/W/C/D` |
| res_users all                    | Role / Portal    | `R`       |
| res_users all                    | Role / Public    | `R`       |
| res_users all                    | Role / User      | `R`       |

**Record Rules:**

- **user rule** (Global) `R/W/C/D`
  - Domain: `['|', ('share', '=', False), ('company_ids', 'in', company_ids)]`
- **portal user access** (10) `R/W/C/D`
  - Domain: `[('commercial_partner_id', '=', user.commercial_partner_id.id)]`
