---
title: "OpenEduCat LMS Sale"
module: "openeducat_lms_sale"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "https://www.openeducat.org"
license: "Other proprietary"
category: "Education"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_________]
---

# 🟢 OpenEduCat LMS Sale

> **Module:** `openeducat_lms_sale` | **Version:** `19.0.1.0` **Category:** Education |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> https://www.openeducat.org

## 🔗 Dependencies

[[website_sale]] [[openeducat_lms]] [[payment_demo]]

## 📖 Description

## OpenEduCat LMS Sale

[![](/openeducat_lms_sale/static/description/openeducat_logo.png)](https://www.openeducat.org/demo)

Online Demo

This module adds the feature in OpenEduCat LMS to sell courses online.

[Contact Us](https://www.openeducat.org/contactus/)

## Sell Your Course

### Create your paid course and sell it online.

![](/openeducat_lms_sale/static/description/course_with_price.png)

## Course Type

You can set course type as free or paid. If paid then just set your price and sell it.

![](/openeducat_lms_sale/static/description/lms_sale_type.png)

## Cart

### User will enroll for course and it will be added in shopping cart.

![](/openeducat_lms_sale/static/description/course_shoping_cart.png)

## Order Confirmation and Pay Now

### Confirm your order and pay now for that.

![](/openeducat_lms_sale/static/description/lms_sale_payment.png)

## My Courses

After successful payment and order confirmation you will get it in my course.

![](/openeducat_lms_sale/static/description/sale_course_my_course.png)

## Need Any Help?

[Email](mailto:support@openeducat.org)
[Contact Us](https://www.openeducat.org/page/contactus)
[Request Customization](https://www.openeducat.org/page/contactus)
[Returns and Refunds Policy](https://www.openeducat.org/page/return-and-refund-policy)

## 🖥️ UI Components

### Menus

_none_

### Views

- `* INHERIT lms_course_attributes_sale (qweb)`
- `* INHERIT op.course.add.form.inherit (form)`
- `* INHERIT op.course.enrollment.form (form)`
- `* INHERIT op.course.enrollment.sale.list (list)`
- `* INHERIT op.course.form.inherit (form)`

### Reports

_none_

## 🛠️ Technical Documentation

**3 model(s) defined by this module:**

### 🗃️ `op.course` — Course

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                         | Type        | Req | Store | Relation               |
| -------------------------------- | ----------------------------- | ----------- | --- | ----- | ---------------------- |
| `active`                         | Active                        | `boolean`   |     | ✅    |                        |
| `activity_calendar_event_id`     | Next Activity Calendar Event  | `many2one`  |     |       | calendar.event         |
| `activity_date_deadline`         | Next Activity Deadline        | `date`      |     |       |                        |
| `activity_exception_decoration`  | Activity Exception Decoration | `selection` |     |       |                        |
| `activity_exception_icon`        | Icon                          | `char`      |     |       |                        |
| `activity_ids`                   | Activities                    | `one2many`  |     | ✅    | mail.activity          |
| `activity_state`                 | Activity State                | `selection` |     |       |                        |
| `activity_summary`               | Next Activity Summary         | `char`      |     |       |                        |
| `activity_type_icon`             | Activity Type Icon            | `char`      |     |       |                        |
| `activity_type_id`               | Next Activity Type            | `many2one`  |     |       | mail.activity.type     |
| `activity_user_id`               | Responsible User              | `many2one`  |     |       | res.users              |
| `admission_count`                | Admission Count               | `integer`   |     |       |                        |
| `allow_reviews`                  | Allow Reviews                 | `boolean`   |     | ✅    |                        |
| `announcement_line`              | Announcements                 | `one2many`  |     | ✅    | op.course.announcement |
| `area_id`                        | Area                          | `many2one`  |     |       | op.area                |
| `assignment_count`               | Assignment Count              | `integer`   |     |       |                        |
| `avg_progress`                   | Avg. Progress (%)             | `float`     |     | ✅    |                        |
| `background`                     | Background Image              | `binary`    |     | ✅    |                        |
| `batch_count`                    | Batch Count                   | `integer`   |     |       |                        |
| `can_publish`                    | Can Publish                   | `boolean`   |     |       |                        |
| `category_ids`                   | Categories                    | `many2many` |     | ✅    | op.course.category     |
| `certi_date`                     | Certificate Date              | `boolean`   |     | ✅    |                        |
| `certi_title`                    | Certificate Title             | `char`      |     | ✅    |                        |
| `child_course_count`             | Child Course Count            | `integer`   |     |       |                        |
| `code`                           | Code                          | `char`      | ✅  | ✅    |                        |
| `color`                          | Color Index                   | `integer`   |     | ✅    |                        |
| `company_id`                     | Company                       | `many2one`  |     | ✅    | res.company            |
| `completion_count`               | Completions                   | `integer`   |     | ✅    |                        |
| `content_category_ids`           | Content Modules               | `one2many`  |     |       | op.course.module       |
| `content_content_ids`            | Content                       | `one2many`  |     |       | op.course.module       |
| `course_change_fees`             | Course Change Fees            | `boolean`   |     | ✅    |                        |
| `course_image`                   | Course Image                  | `binary`    |     | ✅    |                        |
| `cover_properties`               | Cover Properties              | `text`      |     | ✅    |                        |
| `create_date`                    | Created on                    | `datetime`  |     | ✅    |                        |
| `create_uid`                     | Created by                    | `many2one`  |     | ✅    | res.users              |
| `credit`                         | Course Credit                 | `float`     |     | ✅    |                        |
| `department_id`                  | Department                    | `many2one`  |     | ✅    | op.department          |
| `description`                    | Description                   | `html`      |     | ✅    |                        |
| `display_name`                   | Display Name                  | `char`      |     |       |                        |
| `display_style`                  | Display Style                 | `selection` |     | ✅    |                        |
| `enrollment_line`                | Enrollment                    | `one2many`  |     | ✅    | op.course.enrollment   |
| `evaluation_type`                | Evaluation Type               | `selection` | ✅  | ✅    |                        |
| `faculty_count`                  | Faculty Count                 | `integer`   |     |       |                        |
| `faculty_ids`                    | Instructor                    | `many2many` |     | ✅    | op.faculty             |
| `fees_term_id`                   | Fees Term                     | `many2one`  |     | ✅    | op.fees.terms          |
| `forum_count`                    | Forum Count                   | `integer`   |     | ✅    |                        |
| `forum_id`                       | Forum                         | `many2one`  |     | ✅    | forum.forum            |
| `forum_post_count`               | Forum Post Count              | `integer`   |     | ✅    |                        |
| `forum_post_ids`                 | Forum Post                    | `one2many`  |     | ✅    | forum.post             |
| `forum_reply_count`              | Forum Reply Count             | `integer`   |     | ✅    |                        |
| `full_description`               | Full Description              | `html`      |     | ✅    |                        |
| `grade_scale_id`                 | Final Grade                   | `many2one`  |     | ✅    | op.grade.scale         |
| `grade_template_ids`             | Grade Template                | `many2many` | ✅  | ✅    | op.grade.template      |
| `has_message`                    | Has Message                   | `boolean`   |     |       |                        |
| `id`                             | ID                            | `integer`   |     | ✅    |                        |
| `image_1024`                     | Image 1024                    | `binary`    |     | ✅    |                        |
| `image_128`                      | Image 128                     | `binary`    |     | ✅    |                        |
| `image_1920`                     | Image                         | `binary`    |     | ✅    |                        |
| `image_256`                      | Image 256                     | `binary`    |     | ✅    |                        |
| `image_512`                      | Image 512                     | `binary`    |     | ✅    |                        |
| `invited_users_ids`              | Invited Users                 | `many2many` |     | ✅    | res.users              |
| `is_certificate`                 | Certificate Of Completion?    | `boolean`   |     | ✅    |                        |
| `is_enroll_user`                 | Enroll User                   | `boolean`   |     | ✅    |                        |
| `is_paid`                        | Paid Course?                  | `boolean`   |     | ✅    |                        |
| `is_published`                   | Is Published                  | `boolean`   |     | ✅    |                        |
| `list_price`                     | Price                         | `float`     |     |       |                        |
| `lms_course_count`               | LMS course count              | `char`      |     | ✅    |                        |
| `lms_course_type`                | Course type                   | `selection` | ✅  | ✅    |                        |
| `max_unit_load`                  | Maximum Unit Load             | `float`     |     | ✅    |                        |
| `message_attachment_count`       | Attachment Count              | `integer`   |     |       |                        |
| `message_follower_ids`           | Followers                     | `one2many`  |     | ✅    | mail.followers         |
| `message_has_error`              | Message Delivery error        | `boolean`   |     |       |                        |
| `message_has_error_counter`      | Number of errors              | `integer`   |     |       |                        |
| `message_has_sms_error`          | SMS Delivery error            | `boolean`   |     |       |                        |
| `message_ids`                    | Messages                      | `one2many`  |     | ✅    | mail.message           |
| `message_is_follower`            | Is Follower                   | `boolean`   |     |       |                        |
| `message_needaction`             | Action Needed                 | `boolean`   |     |       |                        |
| `message_needaction_counter`     | Number of Actions             | `integer`   |     |       |                        |
| `message_partner_ids`            | Followers (Partners)          | `many2many` |     |       | res.partner            |
| `min_unit_load`                  | Minimum Unit Load             | `float`     |     | ✅    |                        |
| `module_lines`                   | Module                        | `one2many`  |     | ✅    | op.course.module       |
| `my_activity_date_deadline`      | My Activity Deadline          | `date`      |     |       |                        |
| `name`                           | Name                          | `char`      | ✅  | ✅    |                        |
| `navigation_policy`              | Navigation Policy             | `selection` | ✅  | ✅    |                        |
| `notice_group_id`                | Notice Group                  | `many2one`  |     | ✅    | op.notice.group        |
| `online_course`                  | Online Course                 | `boolean`   |     | ✅    |                        |
| `online_course_created`          | Online Course Created         | `boolean`   |     | ✅    |                        |
| `parent_id`                      | Parent Course                 | `many2one`  |     | ✅    | op.course              |
| `price`                          | Computed Price                | `float`     |     |       |                        |
| `product_id`                     | Product                       | `many2one`  |     | ✅    | product.product        |
| `program_id`                     | Program                       | `many2one`  |     | ✅    | op.program             |
| `rating_avg`                     | Average Rating                | `float`     |     |       |                        |
| `rating_avg_stars`               | Rating Average (Stars)        | `float`     |     |       |                        |
| `rating_avg_text`                | Rating Avg Text               | `selection` |     |       |                        |
| `rating_count`                   | Rating count                  | `integer`   |     |       |                        |
| `rating_ids`                     | Ratings                       | `one2many`  |     | ✅    | rating.rating          |
| `rating_last_feedback`           | Rating Last Feedback          | `text`      |     |       |                        |
| `rating_last_image`              | Rating Last Image             | `binary`    |     |       |                        |
| `rating_last_text`               | Rating Text                   | `selection` |     |       |                        |
| `rating_last_value`              | Rating Last Value             | `float`     |     | ✅    |                        |
| `rating_percentage_satisfaction` | Rating Satisfaction           | `float`     |     |       |                        |
| `reg_fees`                       | Registration Fees             | `boolean`   |     | ✅    |                        |
| `sequence`                       | Sequence                      | `integer`   |     | ✅    |                        |
| `short_desc`                     | Short Description             | `text`      |     | ✅    |                        |
| `specialization_id`              | Specialization                | `many2one`  |     | ✅    | op.specialization      |
| `state`                          | State                         | `selection` |     | ✅    |                        |
| `student_count`                  | Student Count                 | `integer`   |     |       |                        |
| `subject_count`                  | Subject Count                 | `integer`   |     |       |                        |
| `subject_counts`                 | Subject Counts                | `integer`   |     |       |                        |
| `subject_ids`                    | Subject(s)                    | `many2many` |     | ✅    | op.subject             |
| `subject_selection_option`       | Subject Selection             | `selection` |     | ✅    |                        |
| `suggested_course_ids`           | Suggested Course              | `many2many` |     | ✅    | op.course              |
| `survey_ids`                     | Survey                        | `one2many`  |     | ✅    | survey.survey          |
| `tag_ids`                        | Tags                          | `many2many` |     | ✅    | op.course.tag          |
| `timetable_count`                | Timetable Count               | `integer`   |     |       |                        |
| `timing_course_count`            | Timing Course Count           | `integer`   |     |       |                        |
| `total_enrollment`               | Total Enrollment              | `integer`   |     | ✅    |                        |
| `total_modules`                  | Number of Contents            | `integer`   |     | ✅    |                        |
| `total_time`                     | Duration                      | `float`     |     | ✅    |                        |
| `user_id`                        | Responsible                   | `many2one`  |     | ✅    | res.users              |
| `visibility`                     | Visibility Policy             | `selection` | ✅  | ✅    |                        |
| `website_absolute_url`           | Website Absolute URL          | `char`      |     |       |                        |
| `website_id`                     | Website                       | `many2one`  |     | ✅    | website                |
| `website_message_ids`            | Website Messages              | `one2many`  |     | ✅    | mail.message           |
| `website_published`              | Visible on current website    | `boolean`   |     |       |                        |
| `website_url`                    | Website URL                   | `char`      |     |       |                        |
| `write_date`                     | Last Updated on               | `datetime`  |     | ✅    |                        |
| `write_uid`                      | Last Updated by               | `many2one`  |     | ✅    | res.users              |

**Access Rights:**

| Name                             | Group                | Perms     |
| -------------------------------- | -------------------- | --------- |
| name_op_course_back_office_admin | OpenEduCat / Manager | `R/W/C/D` |
| name_op_course_faculty           | OpenEduCat / User    | `R/W/C`   |
| name_op_course_library           | Library / Manager    | `R`       |
| access_op_course                 | LMS / Manager        | `R/W/C/D` |
| access_op_course_user            | LMS / User           | `R/W/C`   |
| access_op_course_portal          | Role / Portal        | `R/W`     |
| name_op_course_parent            | Role / Portal        | `R`       |
| access_op_course_public          | Role / Public        | `R`       |
| name_op_dynamic_admission_course | Role / Public        | `R`       |

**Record Rules:**

- **Course multi-company** (1) `R/W/C/D`
  - Domain:
    `         ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]     `
- **Course multi-department** (1) `R/W/C/D`
  - Domain:
    `         ['|','|',('department_id','=',False),('department_id','child_of',[user.dept_id.id]),('department_id','in',user.department_ids.ids)]     `
- **course multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `

### 🗃️ `sale.order` — Sales Order

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                              | Label                              | Type        | Req | Store | Relation                    |
| ---------------------------------- | ---------------------------------- | ----------- | --- | ----- | --------------------------- |
| `access_token`                     | Security Token                     | `char`      |     | ✅    |                             |
| `access_url`                       | Portal Access URL                  | `char`      |     |       |                             |
| `access_warning`                   | Access warning                     | `text`      |     |       |                             |
| `activity_calendar_event_id`       | Next Activity Calendar Event       | `many2one`  |     |       | calendar.event              |
| `activity_date_deadline`           | Next Activity Deadline             | `date`      |     |       |                             |
| `activity_exception_decoration`    | Activity Exception Decoration      | `selection` |     |       |                             |
| `activity_exception_icon`          | Icon                               | `char`      |     |       |                             |
| `activity_ids`                     | Activities                         | `one2many`  |     | ✅    | mail.activity               |
| `activity_state`                   | Activity State                     | `selection` |     |       |                             |
| `activity_summary`                 | Next Activity Summary              | `char`      |     |       |                             |
| `activity_type_icon`               | Activity Type Icon                 | `char`      |     |       |                             |
| `activity_type_id`                 | Next Activity Type                 | `many2one`  |     |       | mail.activity.type          |
| `activity_user_id`                 | Responsible User                   | `many2one`  |     |       | res.users                   |
| `amount_delivery`                  | Delivery Amount                    | `monetary`  |     |       |                             |
| `amount_invoiced`                  | Already invoiced                   | `monetary`  |     |       |                             |
| `amount_paid`                      | Payment Transactions Amount        | `float`     |     |       |                             |
| `amount_tax`                       | Taxes                              | `monetary`  |     | ✅    |                             |
| `amount_to_invoice`                | Un-invoiced Balance                | `monetary`  |     |       |                             |
| `amount_total`                     | Total                              | `monetary`  |     | ✅    |                             |
| `amount_undiscounted`              | Amount Before Discount             | `float`     |     |       |                             |
| `amount_untaxed`                   | Untaxed Amount                     | `monetary`  |     | ✅    |                             |
| `attendee_count`                   | Attendee Count                     | `integer`   |     |       |                             |
| `authorized_transaction_ids`       | Authorized Transactions            | `many2many` |     |       | payment.transaction         |
| `available_quotation_document_ids` | Available Quotation Documents      | `many2many` |     |       | quotation.document          |
| `campaign_id`                      | Campaign                           | `many2one`  |     | ✅    | utm.campaign                |
| `carrier_id`                       | Delivery Method                    | `many2one`  |     | ✅    | delivery.carrier            |
| `cart_quantity`                    | Cart Quantity                      | `integer`   |     |       |                             |
| `cart_recovery_email_sent`         | Cart recovery email already sent   | `boolean`   |     | ✅    |                             |
| `client_order_ref`                 | Customer Reference                 | `char`      |     | ✅    |                             |
| `commitment_date`                  | Delivery Date                      | `datetime`  |     | ✅    |                             |
| `company_id`                       | Company                            | `many2one`  | ✅  | ✅    | res.company                 |
| `company_price_include`            | Default Sales Price Include        | `selection` |     |       |                             |
| `country_code`                     | Country code                       | `char`      |     |       |                             |
| `create_date`                      | Creation Date                      | `datetime`  |     | ✅    |                             |
| `create_uid`                       | Created by                         | `many2one`  |     | ✅    | res.users                   |
| `currency_id`                      | Currency                           | `many2one`  |     | ✅    | res.currency                |
| `currency_rate`                    | Currency Rate                      | `float`     |     | ✅    |                             |
| `customizable_pdf_form_fields`     | Customizable PDF Form Fields       | `json`      |     | ✅    |                             |
| `date_order`                       | Order Date                         | `datetime`  | ✅  | ✅    |                             |
| `delivery_count`                   | Delivery Orders                    | `integer`   |     |       |                             |
| `delivery_message`                 | Delivery Message                   | `char`      |     | ✅    |                             |
| `delivery_set`                     | Delivery Set                       | `boolean`   |     |       |                             |
| `delivery_status`                  | Delivery Status                    | `selection` |     | ✅    |                             |
| `display_name`                     | Display Name                       | `char`      |     |       |                             |
| `duplicated_order_ids`             | Duplicated Order                   | `many2many` |     |       | sale.order                  |
| `effective_date`                   | Effective Date                     | `datetime`  |     | ✅    |                             |
| `expected_date`                    | Expected Date                      | `datetime`  |     |       |                             |
| `expense_count`                    | # of Expenses                      | `integer`   |     |       |                             |
| `expense_ids`                      | Expenses                           | `one2many`  |     | ✅    | hr.expense                  |
| `fiscal_position_id`               | Fiscal Position                    | `many2one`  |     | ✅    | account.fiscal.position     |
| `has_active_pricelist`             | Has Active Pricelist               | `boolean`   |     |       |                             |
| `has_archived_products`            | Has Archived Products              | `boolean`   |     |       |                             |
| `has_authorized_transaction_ids`   | Has Authorized Transactions        | `boolean`   |     |       |                             |
| `has_message`                      | Has Message                        | `boolean`   |     |       |                             |
| `id`                               | ID                                 | `integer`   |     | ✅    |                             |
| `incoterm`                         | Incoterm                           | `many2one`  |     | ✅    | account.incoterms           |
| `incoterm_location`                | Incoterm Location                  | `char`      |     | ✅    |                             |
| `invoice_count`                    | Invoice Count                      | `integer`   |     |       |                             |
| `invoice_ids`                      | Invoices                           | `many2many` |     |       | account.move                |
| `invoice_status`                   | Invoice Status                     | `selection` |     | ✅    |                             |
| `is_abandoned_cart`                | Abandoned Cart                     | `boolean`   |     |       |                             |
| `is_all_service`                   | Service Product                    | `boolean`   |     |       |                             |
| `is_expired`                       | Is Expired                         | `boolean`   |     |       |                             |
| `is_pdf_quote_builder_available`   | Is Pdf Quote Builder Available     | `boolean`   |     |       |                             |
| `journal_id`                       | Invoicing Journal                  | `many2one`  |     | ✅    | account.journal             |
| `json_popover`                     | JSON data for the popover widget   | `char`      |     |       |                             |
| `late_availability`                | Late Availability                  | `boolean`   |     |       |                             |
| `locked`                           | Locked                             | `boolean`   |     | ✅    |                             |
| `medium_id`                        | Medium                             | `many2one`  |     | ✅    | utm.medium                  |
| `message_attachment_count`         | Attachment Count                   | `integer`   |     |       |                             |
| `message_follower_ids`             | Followers                          | `one2many`  |     | ✅    | mail.followers              |
| `message_has_error`                | Message Delivery error             | `boolean`   |     |       |                             |
| `message_has_error_counter`        | Number of errors                   | `integer`   |     |       |                             |
| `message_has_sms_error`            | SMS Delivery error                 | `boolean`   |     |       |                             |
| `message_ids`                      | Messages                           | `one2many`  |     | ✅    | mail.message                |
| `message_is_follower`              | Is Follower                        | `boolean`   |     |       |                             |
| `message_needaction`               | Action Needed                      | `boolean`   |     |       |                             |
| `message_needaction_counter`       | Number of Actions                  | `integer`   |     |       |                             |
| `message_partner_ids`              | Followers (Partners)               | `many2many` |     |       | res.partner                 |
| `my_activity_date_deadline`        | My Activity Deadline               | `date`      |     |       |                             |
| `name`                             | Order Reference                    | `char`      | ✅  | ✅    |                             |
| `note`                             | Terms and conditions               | `html`      |     | ✅    |                             |
| `only_services`                    | Only Services                      | `boolean`   |     |       |                             |
| `opportunity_id`                   | Opportunity                        | `many2one`  |     | ✅    | crm.lead                    |
| `order_line`                       | Order Lines                        | `one2many`  |     | ✅    | sale.order.line             |
| `origin`                           | Source Document                    | `char`      |     | ✅    |                             |
| `partner_credit_warning`           | Partner Credit Warning             | `text`      |     |       |                             |
| `partner_id`                       | Customer                           | `many2one`  | ✅  | ✅    | res.partner                 |
| `partner_invoice_id`               | Invoice Address                    | `many2one`  | ✅  | ✅    | res.partner                 |
| `partner_shipping_id`              | Delivery Address                   | `many2one`  | ✅  | ✅    | res.partner                 |
| `payment_term_id`                  | Payment Terms                      | `many2one`  |     | ✅    | account.payment.term        |
| `pending_email_template_id`        | Pending Email Template             | `many2one`  |     | ✅    | mail.template               |
| `picking_ids`                      | Transfers                          | `one2many`  |     | ✅    | stock.picking               |
| `picking_policy`                   | Shipping Policy                    | `selection` | ✅  | ✅    |                             |
| `pickup_location_data`             | Pickup Location Data               | `json`      |     | ✅    |                             |
| `preferred_payment_method_line_id` | Payment Method                     | `many2one`  |     | ✅    | account.payment.method.line |
| `prepayment_percent`               | Prepayment percentage              | `float`     |     | ✅    |                             |
| `pricelist_id`                     | Pricelist                          | `many2one`  |     | ✅    | product.pricelist           |
| `purchase_order_count`             | Number of Purchase Order Generated | `integer`   |     |       |                             |
| `quotation_document_ids`           | Headers/Footers                    | `many2many` |     | ✅    | quotation.document          |
| `rating_ids`                       | Ratings                            | `one2many`  |     | ✅    | rating.rating               |
| `recompute_delivery_price`         | Delivery cost should be recomputed | `boolean`   |     | ✅    |                             |
| `reference`                        | Payment Ref.                       | `char`      |     | ✅    |                             |
| `require_payment`                  | Online payment                     | `boolean`   |     | ✅    |                             |
| `require_signature`                | Online signature                   | `boolean`   |     | ✅    |                             |
| `sale_order_template_id`           | Quotation Template                 | `many2one`  |     | ✅    | sale.order.template         |
| `sale_warning_text`                | Sale Warning                       | `text`      |     |       |                             |
| `shipping_weight`                  | Shipping Weight                    | `float`     |     | ✅    |                             |
| `shop_warning`                     | Warning                            | `char`      |     | ✅    |                             |
| `show_json_popover`                | Has late picking                   | `boolean`   |     |       |                             |
| `show_update_fpos`                 | Has Fiscal Position Changed        | `boolean`   |     |       |                             |
| `show_update_pricelist`            | Has Pricelist Changed              | `boolean`   |     |       |                             |
| `signature`                        | Signature                          | `binary`    |     | ✅    |                             |
| `signed_by`                        | Signed By                          | `char`      |     | ✅    |                             |
| `signed_on`                        | Signed On                          | `datetime`  |     | ✅    |                             |
| `source_id`                        | Source                             | `many2one`  |     | ✅    | utm.source                  |
| `state`                            | Status                             | `selection` |     | ✅    |                             |
| `stock_reference_ids`              | References                         | `many2many` |     | ✅    | stock.reference             |
| `tag_ids`                          | Tags                               | `many2many` |     | ✅    | crm.tag                     |
| `tax_calculation_rounding_method`  | Tax Calculation Rounding Method    | `selection` |     |       |                             |
| `tax_country_id`                   | Tax Country                        | `many2one`  |     |       | res.country                 |
| `tax_totals`                       | Tax Totals                         | `binary`    |     |       |                             |
| `team_id`                          | Sales Team                         | `many2one`  |     | ✅    | crm.team                    |
| `terms_type`                       | Terms & Conditions format          | `selection` |     |       |                             |
| `transaction_ids`                  | Transactions                       | `many2many` |     | ✅    | payment.transaction         |
| `type_name`                        | Type Name                          | `char`      |     |       |                             |
| `user_id`                          | Salesperson                        | `many2one`  |     | ✅    | res.users                   |
| `validity_date`                    | Expiration                         | `date`      |     | ✅    |                             |
| `warehouse_id`                     | Warehouse                          | `many2one`  |     | ✅    | stock.warehouse             |
| `website_id`                       | Website                            | `many2one`  |     | ✅    | website                     |
| `website_message_ids`              | Website Messages                   | `one2many`  |     | ✅    | mail.message                |
| `website_order_line`               | Order Lines displayed on Website   | `one2many`  |     |       | sale.order.line             |
| `write_date`                       | Last Updated on                    | `datetime`  |     | ✅    |                             |
| `write_uid`                        | Last Updated by                    | `many2one`  |     | ✅    | res.users                   |

**Access Rights:**

| Name                    | Group                            | Perms     |
| ----------------------- | -------------------------------- | --------- |
| sale.order              | Sales / User: Own Documents Only | `R/W/C`   |
| sale.order.manager      | Sales / Administrator            | `R/W/C/D` |
| sale.order              | Accounting / Invoicing           | `R/W`     |
| sale.order.accountant   | Contact / Accountant             | `R/W`     |
| sale.order stock worker | Inventory / User                 | `R/W`     |
| sale.order.accountant   | Auditor                          | `R`       |
| sale.order.portal       | Role / Portal                    | `R`       |

**Record Rules:**

- **Sales Order multi-company** (Global) `R/W/C/D`
  - Domain: `[('company_id', 'in', company_ids)]`
- **Portal Personal Quotations/Sales Orders** (10) `R/W/D`
  - Domain: `[('partner_id','child_of',[user.commercial_partner_id.id])]`
- **Personal Orders** (25) `R/W/C/D`
  - Domain: `['|',('user_id','=',user.id),('user_id','=',False)]`
- **All Orders** (26) `R/W/C/D`
  - Domain: `[(1,'=',1)]`

### 🗃️ `op.course.enrollment` — LMS Course Enrollment

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field             | Label                | Type        | Req | Store | Relation                  |
| ----------------- | -------------------- | ----------- | --- | ----- | ------------------------- |
| `access_token`    | Access Token         | `char`      |     | ✅    |                           |
| `access_url`      | Portal Access URL    | `char`      |     |       |                           |
| `company_id`      | Company              | `many2one`  |     | ✅    | res.company               |
| `completion_date` | Completion Date      | `datetime`  |     | ✅    |                           |
| `course_id`       | Course               | `many2one`  | ✅  | ✅    | op.course                 |
| `create_date`     | Created on           | `datetime`  |     | ✅    |                           |
| `create_uid`      | Created by           | `many2one`  |     | ✅    | res.users                 |
| `display_name`    | Display Name         | `char`      |     |       |                           |
| `enrollment_date` | Enrollment Date      | `datetime`  | ✅  | ✅    |                           |
| `enrollment_line` | Module Content       | `one2many`  |     | ✅    | op.course.enrollment.line |
| `id`              | ID                   | `integer`   |     | ✅    |                           |
| `index`           | Index                | `char`      |     | ✅    |                           |
| `last_module_id`  | Last Accessed Module | `many2one`  |     | ✅    | op.course.module          |
| `order_id`        | Order                | `many2one`  |     | ✅    | sale.order                |
| `progress`        | Progress             | `integer`   |     | ✅    |                           |
| `state`           | Status               | `selection` |     | ✅    |                           |
| `user_id`         | User                 | `many2one`  | ✅  | ✅    | res.users                 |
| `write_date`      | Last Updated on      | `datetime`  |     | ✅    |                           |
| `write_uid`       | Last Updated by      | `many2one`  |     | ✅    | res.users                 |

**Access Rights:**

| Name                               | Group         | Perms     |
| ---------------------------------- | ------------- | --------- |
| access_op_course_enrollment        | LMS / Manager | `R/W/C/D` |
| access_op_course_enrollment_user   | LMS / User    | `R/W/C`   |
| access_op_course_enrollment_portal | Role / Portal | `R/W/C`   |
| access_op_course_enrollment_public | Role / Public | `R`       |

**Record Rules:**

- **Course Enrollment multi-company** (Global) `R/W/C/D`
  - Domain:
    `             ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]         `
