---
title: "OpenEduCat OMR"
module: "openeducat_omr"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Uncategorized"
application: true
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_____________, odoo/app]
---

# 🟢 OpenEduCat OMR

> **Module:** `openeducat_omr` | **Version:** `19.0.1.0` **Category:** Uncategorized |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[base]] [[website]] [[mail]] [[portal]] [[openeducat_core_enterprise]]
[[openeducat_web]] [[openeducat_subject_material_allocation]]

## 📖 Description

## OpenEduCat OMR

### OMR Scanner

[![](/openeducat_omr/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module adds the feature of Omr scanner to OpenEduCat. You can print Omr for exam &
scan omr with your mobile and get result.

[Contact Us](https://www.openeducat.org/contactus/)

## Generate OMR Sheet

Generate 20, 50, 100 question OMR sheet with 4 or 5 mcq option for exam.

![](/openeducat_omr/static/description/omr_sheet_generate.png)

## Paper Set

![](/openeducat_omr/static/description/paper_set.png)

Create answer sheet for particular subject with multiple paper set option.

## OMR Exam

Create OMR Exam to scan OMR sheets with template and answer key.

![](/openeducat_omr/static/description/omr_exam.png)

## Scan OMR Sheet

![](/openeducat_omr/static/description/scan_image.png)

Scan OMR Exam sheets with your mobile or high resolution Camera.

## Get Result

Get result of scanned OMR with student Name, Roll number, Paper set and Score.

![](/openeducat_omr/static/description/answer_sheets.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

- `OMR`
- `OMR/Configuration`
- `OMR/Configuration/Answer Sheet`
- `OMR/Configuration/Settings`
- `OMR/Exam`
- `OMR/Generate Sheet`
- `OMR/Reporting`
- `OMR/Reporting/Answer Sheets`

### Views

- `* INHERIT Portal layout : OMR Exam (qweb)`
- `* INHERIT Portal layout : OMR Exam Result (qweb)`
- `* INHERIT Show OMR (qweb)`
- `* INHERIT Show OMR Result (qweb)`
- `OMR Exam Kanban (kanban)`
- `answer_set_form_view (form)`
- `answer_set_list_view (list)`
- `answer_sheets_form_view (form)`
- `answer_sheets_list_view (list)`
- `answer_sheets_pivot_view (pivot)`
- `answersheet_configuration_form_view (form)`
- `answersheet_configuration_list_view (list)`
- `omr_exam_form_view (form)`
- `omr_exam_list_view (list)`
- `omr_exam_pivot_view (pivot)`
- `omr_exam_result (qweb)`
- `omr_exam_student_portal (qweb)`
- `omr_image_form_view (form)`
- `omr_image_list_view (list)`
- `omr_template_form_view (form)`
- `omr_template_list_view (list)`
- `op_omr_template_wizard (form)`
- `question_answer_form_view (form)`
- `question_answer_import_wizard_form (form)`
- `question_answer_list_view (list)`
- `report_layout_hundred (qweb)`

### Reports

- `Generate Templates`

## 🛠️ Technical Documentation

**10 model(s) defined by this module:**

### 🗃️ `op.answer.set` — Answer Sets

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                          | Label                     | Type        | Req | Store | Relation                     |
| ------------------------------ | ------------------------- | ----------- | --- | ----- | ---------------------------- |
| `answersheet_configuration_id` | Answersheet Configuration | `many2one`  |     | ✅    | op.answersheet.configuration |
| `create_date`                  | Created on                | `datetime`  |     | ✅    |                              |
| `create_uid`                   | Created by                | `many2one`  |     | ✅    | res.users                    |
| `display_name`                 | Display Name              | `char`      |     |       |                              |
| `has_message`                  | Has Message               | `boolean`   |     |       |                              |
| `id`                           | ID                        | `integer`   |     | ✅    |                              |
| `message_attachment_count`     | Attachment Count          | `integer`   |     |       |                              |
| `message_follower_ids`         | Followers                 | `one2many`  |     | ✅    | mail.followers               |
| `message_has_error`            | Message Delivery error    | `boolean`   |     |       |                              |
| `message_has_error_counter`    | Number of errors          | `integer`   |     |       |                              |
| `message_has_sms_error`        | SMS Delivery error        | `boolean`   |     |       |                              |
| `message_ids`                  | Messages                  | `one2many`  |     | ✅    | mail.message                 |
| `message_is_follower`          | Is Follower               | `boolean`   |     |       |                              |
| `message_needaction`           | Action Needed             | `boolean`   |     |       |                              |
| `message_needaction_counter`   | Number of Actions         | `integer`   |     |       |                              |
| `message_partner_ids`          | Followers (Partners)      | `many2many` |     |       | res.partner                  |
| `omr_exam_id`                  | OMR Exam                  | `many2one`  |     | ✅    | op.omr.exam                  |
| `paper_set`                    | Paper Set                 | `char`      | ✅  | ✅    |                              |
| `question_answer_line`         | Question Answer Line      | `one2many`  |     | ✅    | op.question.answer           |
| `rating_ids`                   | Ratings                   | `one2many`  |     | ✅    | rating.rating                |
| `website_message_ids`          | Website Messages          | `one2many`  |     | ✅    | mail.message                 |
| `write_date`                   | Last Updated on           | `datetime`  |     | ✅    |                              |
| `write_uid`                    | Last Updated by           | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                      | Group         | Perms     |
| ------------------------- | ------------- | --------- |
| access_op_answer_set      | OMR / Manager | `R/W/C/D` |
| access_op_answer_set_user | OMR / User    | `R/W`     |

### 🗃️ `op.answersheet.configuration` — Answer Sheet Configuration

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `answer_set_line`            | Answer Set Line        | `one2many`  |     | ✅    | op.answer.set  |
| `company_id`                 | Company                | `many2one`  |     | ✅    | res.company    |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users      |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `name`                       | Answer Sheet Name      | `char`      | ✅  | ✅    |                |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `subject_id`                 | Subject                | `many2one`  | ✅  | ✅    | op.subject     |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                                     | Group         | Perms     |
| ---------------------------------------- | ------------- | --------- |
| access_op_answersheet_configuration      | OMR / Manager | `R/W/C/D` |
| access_op_answersheet_configuration_user | OMR / User    | `R/W`     |

**Record Rules:**

- **OMR Answersheet Configuration multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `

### 🗃️ `op.question.answer` — Answer Sheet Question-Answer

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation         |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ---------------- |
| `answer`                     | Answer                 | `char`      | ✅  | ✅    |                  |
| `answer_set_id`              | Answer Set             | `many2one`  |     | ✅    | op.answer.set    |
| `answer_sheet_id`            | Answer Sheet           | `many2one`  |     | ✅    | op.answer.sheets |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                  |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users        |
| `display_name`               | Display Name           | `char`      |     |       |                  |
| `has_message`                | Has Message            | `boolean`   |     |       |                  |
| `id`                         | ID                     | `integer`   |     | ✅    |                  |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                  |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers   |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                  |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                  |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                  |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message     |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                  |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                  |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                  |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner      |
| `question`                   | Question Number        | `integer`   | ✅  | ✅    |                  |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating    |
| `state`                      | Status                 | `selection` |     | ✅    |                  |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message     |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                  |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users        |

**Access Rights:**

| Name                           | Group         | Perms     |
| ------------------------------ | ------------- | --------- |
| access_op_question_answer      | OMR / Manager | `R/W/C/D` |
| access_op_question_answer_user | OMR / User    | `R/W`     |

### 🗃️ `op.answer.sheets` — Answer Sheets

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation           |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | ------------------ |
| `access_token`               | Security Token         | `char`      |     | ✅    |                    |
| `access_url`                 | Portal Access URL      | `char`      |     |       |                    |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                    |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users          |
| `date_time`                  | Created Date           | `date`      |     | ✅    |                    |
| `display_name`               | Display Name           | `char`      |     |       |                    |
| `has_message`                | Has Message            | `boolean`   |     |       |                    |
| `id`                         | ID                     | `integer`   |     | ✅    |                    |
| `image`                      | OMR Image              | `binary`    |     | ✅    |                    |
| `image_id`                   | Image                  | `many2one`  |     | ✅    | op.omr.image       |
| `key_type`                   | Paper Set              | `char`      |     | ✅    |                    |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                    |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers     |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                    |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                    |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                    |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message       |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                    |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                    |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                    |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner        |
| `not_attampted`              | Not Attampted          | `integer`   |     | ✅    |                    |
| `omr_exam_id`                | Exam                   | `many2one`  |     | ✅    | op.omr.exam        |
| `question_answer_line`       | Question Answer Line   | `one2many`  |     | ✅    | op.question.answer |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating      |
| `result_json`                | Result                 | `text`      |     | ✅    |                    |
| `right_answer`               | Right Answers          | `integer`   |     | ✅    |                    |
| `roll_number`                | Roll Number            | `char`      |     | ✅    |                    |
| `score`                      | Total Score            | `integer`   |     | ✅    |                    |
| `state`                      | Status                 | `selection` |     | ✅    |                    |
| `student_id`                 | Student                | `many2one`  |     | ✅    | op.student         |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message       |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                    |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users          |
| `wrong_answer`               | Wrong Answer           | `integer`   |     | ✅    |                    |

**Access Rights:**

| Name                         | Group         | Perms     |
| ---------------------------- | ------------- | --------- |
| access_op_answer_sheets      | OMR / Manager | `R/W/C/D` |
| access_op_answer_sheets_user | OMR / User    | `R/W`     |

### 🗃️ `op.omr.exam` — Omr Exam

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                          | Label                         | Type        | Req | Store | Relation                     |
| ------------------------------ | ----------------------------- | ----------- | --- | ----- | ---------------------------- |
| `answersheet_configuration_id` | Answer Sheet                  | `many2one`  | ✅  | ✅    | op.answersheet.configuration |
| `answersheet_count`            | Answer Sheet Count            | `integer`   |     | ✅    |                              |
| `answer_sheets_line`           | Answer Sheets Line            | `one2many`  |     | ✅    | op.answer.sheets             |
| `create_date`                  | Created on                    | `datetime`  |     | ✅    |                              |
| `create_uid`                   | Created by                    | `many2one`  |     | ✅    | res.users                    |
| `display_name`                 | Display Name                  | `char`      |     |       |                              |
| `display_result`               | Display OMR Result To Student | `boolean`   |     | ✅    |                              |
| `has_message`                  | Has Message                   | `boolean`   |     |       |                              |
| `id`                           | ID                            | `integer`   |     | ✅    |                              |
| `is_student_upload_omr`        | Allow Student to Upload OMR   | `boolean`   |     | ✅    |                              |
| `message_attachment_count`     | Attachment Count              | `integer`   |     |       |                              |
| `message_follower_ids`         | Followers                     | `one2many`  |     | ✅    | mail.followers               |
| `message_has_error`            | Message Delivery error        | `boolean`   |     |       |                              |
| `message_has_error_counter`    | Number of errors              | `integer`   |     |       |                              |
| `message_has_sms_error`        | SMS Delivery error            | `boolean`   |     |       |                              |
| `message_ids`                  | Messages                      | `one2many`  |     | ✅    | mail.message                 |
| `message_is_follower`          | Is Follower                   | `boolean`   |     |       |                              |
| `message_needaction`           | Action Needed                 | `boolean`   |     |       |                              |
| `message_needaction_counter`   | Number of Actions             | `integer`   |     |       |                              |
| `message_partner_ids`          | Followers (Partners)          | `many2many` |     |       | res.partner                  |
| `name`                         | Exam Name                     | `char`      | ✅  | ✅    |                              |
| `omr_image_line`               | Omr Images                    | `one2many`  |     | ✅    | op.omr.image                 |
| `rating_ids`                   | Ratings                       | `one2many`  |     | ✅    | rating.rating                |
| `state`                        | Status                        | `selection` |     | ✅    |                              |
| `subject_id`                   | Subject                       | `many2one`  | ✅  | ✅    | op.subject                   |
| `template_id`                  | Template                      | `many2one`  | ✅  | ✅    | op.omr.template              |
| `website_message_ids`          | Website Messages              | `one2many`  |     | ✅    | mail.message                 |
| `write_date`                   | Last Updated on               | `datetime`  |     | ✅    |                              |
| `write_uid`                    | Last Updated by               | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                    | Group         | Perms     |
| ----------------------- | ------------- | --------- |
| access_op_omr_exam      | OMR / Manager | `R/W/C/D` |
| access_op_omr_exam_user | OMR / User    | `R`       |

**Record Rules:**

- **OMR Exam multi-company** (Global) `R/W/C/D`
  - Domain:
    `         ['|',('answersheet_configuration_id.company_id','=',False),'&',('answersheet_configuration_id.company_id','in',company_ids),'|',('answersheet_configuration_id.company_id','child_of',[user.company_id.id]),('answersheet_configuration_id.company_id','in',user.company_ids.ids)]     `

### 🗃️ `op.omr.image` — Omr Images

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users      |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `image`                      | Image                  | `binary`    |     | ✅    |                |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `name`                       | Name                   | `char`      |     | ✅    |                |
| `omr_exam_id`                | Omr Exam               | `many2one`  |     | ✅    | op.omr.exam    |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                       | Group         | Perms     |
| -------------------------- | ------------- | --------- |
| access_op_omr_image        | OMR / Manager | `R/W/C`   |
| access_op_omr_image_user   | OMR / User    | `R/W`     |
| access_op_omr_image_portal | Role / Portal | `R/W/C/D` |

### 🗃️ `op.omr.template` — Omr Template

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation       |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | -------------- |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users      |
| `display_name`               | Display Name           | `char`      |     |       |                |
| `has_message`                | Has Message            | `boolean`   |     |       |                |
| `id`                         | ID                     | `integer`   |     | ✅    |                |
| `json_data`                  | json data              | `char`      |     | ✅    |                |
| `message_attachment_count`   | Attachment Count       | `integer`   |     |       |                |
| `message_follower_ids`       | Followers              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors       | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error     | `boolean`   |     |       |                |
| `message_ids`                | Messages               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower            | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed          | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions      | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)   | `many2many` |     |       | res.partner    |
| `name`                       | Template Name          | `char`      |     | ✅    |                |
| `question_option`            | Question Options       | `selection` |     | ✅    |                |
| `rating_ids`                 | Ratings                | `one2many`  |     | ✅    | rating.rating  |
| `website_message_ids`        | Website Messages       | `one2many`  |     | ✅    | mail.message   |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                        | Group         | Perms     |
| --------------------------- | ------------- | --------- |
| access_op_omr_template      | OMR / Manager | `R/W/C/D` |
| access_op_omr_template_user | OMR / User    | `R/W`     |

### 🗃️ `report.openeducat_omr.report_layout_hundred` — 100 Omr Sheet Layout

The base model, which is implicitly inherited by all models.

**Fields:**

| Field          | Label        | Type      | Req | Store | Relation |
| -------------- | ------------ | --------- | --- | ----- | -------- |
| `display_name` | Display Name | `char`    |     |       |          |
| `id`           | ID           | `integer` |     | ✅    |          |

### 🗃️ `question.answer.import.wizard` — Import Question Answers from Excel

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field           | Label           | Type       | Req | Store | Relation      |
| --------------- | --------------- | ---------- | --- | ----- | ------------- |
| `answer_set_id` | Answer Set      | `many2one` | ✅  | ✅    | op.answer.set |
| `create_date`   | Created on      | `datetime` |     | ✅    |               |
| `create_uid`    | Created by      | `many2one` |     | ✅    | res.users     |
| `display_name`  | Display Name    | `char`     |     |       |               |
| `filename`      | Filename        | `char`     |     | ✅    |               |
| `id`            | ID              | `integer`  |     | ✅    |               |
| `upload_file`   | Excel File      | `binary`   | ✅  | ✅    |               |
| `write_date`    | Last Updated on | `datetime` |     | ✅    |               |
| `write_uid`     | Last Updated by | `many2one` |     | ✅    | res.users     |

**Access Rights:**

| Name                                 | Group      | Perms     |
| ------------------------------------ | ---------- | --------- |
| access_question_answer_import_wizard | OMR / User | `R/W/C/D` |

### 🗃️ `op.omr.template.wizard` — Omr Sheet Generate

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field          | Label             | Type        | Req | Store | Relation  |
| -------------- | ----------------- | ----------- | --- | ----- | --------- |
| `batch`        | Batch Field       | `boolean`   |     | ✅    |           |
| `create_date`  | Created on        | `datetime`  |     | ✅    |           |
| `create_uid`   | Created by        | `many2one`  |     | ✅    | res.users |
| `date`         | Date              | `boolean`   |     | ✅    |           |
| `display_name` | Display Name      | `char`      |     |       |           |
| `id`           | ID                | `integer`   |     | ✅    |           |
| `instruction`  | Instruction Block | `boolean`   |     | ✅    |           |
| `mobile_no`    | Mobile No         | `boolean`   |     | ✅    |           |
| `no_option`    | No of Options     | `selection` | ✅  | ✅    |           |
| `no_que`       | No of Questions   | `selection` | ✅  | ✅    |           |
| `signature`    | Signature Block   | `boolean`   |     | ✅    |           |
| `write_date`   | Last Updated on   | `datetime`  |     | ✅    |           |
| `write_uid`    | Last Updated by   | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                               | Group         | Perms     |
| ---------------------------------- | ------------- | --------- |
| access_op_omr_template_wizard      | OMR / Manager | `R/W/C/D` |
| access_op_omr_template_wizard_user | OMR / User    | `R/W`     |
