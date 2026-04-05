---
title: "Forum"
module: "website_forum"
state: "installed"
version: "19.0.1.2"
author: "Odoo S.A."
maintainer: "N/A"
website: "https://www.odoo.com/app/forum"
license: "LGPL-3"
category: "Website"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/w______]
---

# 🟢 Forum

> **Module:** `website_forum` | **Version:** `19.0.1.2` **Category:** Website |
> **License:** `LGPL-3` **Author:** Odoo S.A. **Website:**
> https://www.odoo.com/app/forum

## 🔗 Dependencies

[[auth_signup]] [[website_mail]] [[website_profile]]

## 📖 Description

Ask questions, get answers, no distractions

## 🖥️ UI Components

### Menus

- `Website/Configuration/Forum`
- `Website/Configuration/Forum/Badges`
- `Website/Configuration/Forum/Close Reasons`
- `Website/Configuration/Forum/Forums`
- `Website/Configuration/Forum/Ranks`
- `Website/Configuration/Forum/Tags`
- `Website/Site/Content/Forum Posts`

### Views

- `* INHERIT Forum Contact Widget (qweb)`
- `* INHERIT Forum Layout (qweb)`
- `* INHERIT Forum Navigation (oe_structure_forum_all_top) (qweb)`
- `* INHERIT Forum Welcome Message (oe_structure_forum_top) (qweb)`
- `* INHERIT List View (qweb)`
- `* INHERIT Show Last Post (qweb)`
- `* INHERIT Show Post Count (qweb)`
- `* INHERIT gamification.karma.tracking.view.search.inherit.website.forum (search)`
- `* INHERIT profile_access_denied (qweb)`
- `* INHERIT user_profile_content (qweb)`
- `404 (qweb)`
- `Close Post (qweb)`
- `Edit Post (qweb)`
- `Faq Accordion (qweb)`
- `Filtering Forum Tag (qweb)`
- `Forum (qweb)`
- `Forum Index (qweb)`
- `Forum Moderation Queue (qweb)`
- `Forum Navigation (qweb)`
- `Forum Post Pages Kanban (kanban)`
- `Forum Profile Activities (qweb)`
- `Forum Tags (qweb)`
- `Forum User Votes (qweb)`
- `Frequently Asked Questions (qweb)`
- `Karma (qweb)`
- `New Post (qweb)`
- `Question Navigation (qweb)`
- `Related Posts (qweb)`
- `Sign-Up Call to Action (qweb)`
- `author_box (qweb)`
- `display_post (qweb)`
- `display_post_answer (qweb)`
- `display_post_question_block (qweb)`
- `follow (qweb)`
- `forum.forum.view.form (form)`
- `forum.forum.view.form.add (form)`
- `forum.forum.view.list (list)`
- `forum.forum.view.search (search)`
- `forum.post.reason.list (list)`
- `forum.post.view.form (form)`
- `forum.post.view.graph (graph)`
- `forum.post.view.list (list)`
- `forum.post.view.search (search)`
- `forum.tag.view.form (form)`
- `forum.tag.view.list (list)`
- `forum_all_all_entries (qweb)`
- `forum_model_nav (qweb)`
- `forum_post_template_new_answer (qweb)`
- `forum_post_template_new_question (qweb)`
- `forum_post_template_validation (qweb)`
- `link_button (qweb)`
- `mark_as_offensive (qweb)`
- `moderation_display_post_question_block (qweb)`
- `no_results_message (qweb)`
- `post_answer (qweb)`
- `post_comment (qweb)`
- `post_display (qweb)`
- `post_dropdown (qweb)`
- `post_stats (qweb)`
- `show_flag_validator (qweb)`
- `user_sidebar (qweb)`
- `user_sidebar_body (qweb)`
- `user_sidebar_header (qweb)`
- `user_sidebar_mobile (qweb)`
- `vote (qweb)`

### Reports

_none_

## 🛠️ Technical Documentation

**10 model(s) defined by this module:**

### 🗃️ `forum.forum` — Forum

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                                  | Type        | Req | Store | Relation       |
| -------------------------------- | -------------------------------------- | ----------- | --- | ----- | -------------- |
| `active`                         | Active                                 | `boolean`   |     | ✅    |                |
| `allow_share`                    | Sharing Options                        | `boolean`   |     | ✅    |                |
| `authorized_group_id`            | Authorized Group                       | `many2one`  |     | ✅    | res.groups     |
| `can_moderate`                   | Is a moderator                         | `boolean`   |     |       |                |
| `count_flagged_posts`            | Number of flagged posts                | `integer`   |     |       |                |
| `count_posts_waiting_validation` | Number of posts waiting for validation | `integer`   |     |       |                |
| `course_id`                      | Course                                 | `many2one`  |     | ✅    | op.course      |
| `create_date`                    | Created on                             | `datetime`  |     | ✅    |                |
| `create_uid`                     | Created by                             | `many2one`  |     | ✅    | res.users      |
| `default_order`                  | Default                                | `selection` | ✅  | ✅    |                |
| `description`                    | Description                            | `text`      |     | ✅    |                |
| `display_name`                   | Display Name                           | `char`      |     |       |                |
| `faq`                            | Guidelines                             | `html`      |     | ✅    |                |
| `has_message`                    | Has Message                            | `boolean`   |     |       |                |
| `has_pending_post`               | Has pending post                       | `boolean`   |     |       |                |
| `id`                             | ID                                     | `integer`   |     | ✅    |                |
| `image_1024`                     | Image 1024                             | `binary`    |     | ✅    |                |
| `image_128`                      | Image 128                              | `binary`    |     | ✅    |                |
| `image_1920`                     | Image                                  | `binary`    |     | ✅    |                |
| `image_256`                      | Image 256                              | `binary`    |     | ✅    |                |
| `image_512`                      | Image 512                              | `binary`    |     | ✅    |                |
| `is_seo_optimized`               | SEO optimized                          | `boolean`   |     | ✅    |                |
| `karma_answer`                   | Answer questions                       | `integer`   |     | ✅    |                |
| `karma_answer_accept_all`        | Accept an answer to all questions      | `integer`   |     | ✅    |                |
| `karma_answer_accept_own`        | Accept an answer on own questions      | `integer`   |     | ✅    |                |
| `karma_ask`                      | Ask questions                          | `integer`   |     | ✅    |                |
| `karma_close_all`                | Close all posts                        | `integer`   |     | ✅    |                |
| `karma_close_own`                | Close own posts                        | `integer`   |     | ✅    |                |
| `karma_comment_all`              | Comment all posts                      | `integer`   |     | ✅    |                |
| `karma_comment_convert_all`      | Convert all comments to answers        | `integer`   |     | ✅    |                |
| `karma_comment_convert_own`      | Convert own comments to answers        | `integer`   |     | ✅    |                |
| `karma_comment_own`              | Comment own posts                      | `integer`   |     | ✅    |                |
| `karma_comment_unlink_all`       | Delete all comments                    | `integer`   |     | ✅    |                |
| `karma_comment_unlink_own`       | Delete own comments                    | `integer`   |     | ✅    |                |
| `karma_dofollow`                 | Nofollow links                         | `integer`   |     | ✅    |                |
| `karma_downvote`                 | Downvote                               | `integer`   |     | ✅    |                |
| `karma_edit_all`                 | Edit all posts                         | `integer`   |     | ✅    |                |
| `karma_editor`                   | Editor Features: image and links       | `integer`   |     | ✅    |                |
| `karma_edit_own`                 | Edit own posts                         | `integer`   |     | ✅    |                |
| `karma_edit_retag`               | Change question tags                   | `integer`   |     | ✅    |                |
| `karma_flag`                     | Flag a post as offensive               | `integer`   |     | ✅    |                |
| `karma_gen_answer_accept`        | Accepting an answer                    | `integer`   |     | ✅    |                |
| `karma_gen_answer_accepted`      | Answer accepted                        | `integer`   |     | ✅    |                |
| `karma_gen_answer_downvote`      | Answer downvoted                       | `integer`   |     | ✅    |                |
| `karma_gen_answer_flagged`       | Answer flagged                         | `integer`   |     | ✅    |                |
| `karma_gen_answer_upvote`        | Answer upvoted                         | `integer`   |     | ✅    |                |
| `karma_gen_question_downvote`    | Question downvoted                     | `integer`   |     | ✅    |                |
| `karma_gen_question_new`         | Asking a question                      | `integer`   |     | ✅    |                |
| `karma_gen_question_upvote`      | Question upvoted                       | `integer`   |     | ✅    |                |
| `karma_moderate`                 | Moderate posts                         | `integer`   |     | ✅    |                |
| `karma_post`                     | Ask questions without validation       | `integer`   |     | ✅    |                |
| `karma_tag_create`               | Create new tags                        | `integer`   |     | ✅    |                |
| `karma_unlink_all`               | Delete all posts                       | `integer`   |     | ✅    |                |
| `karma_unlink_own`               | Delete own posts                       | `integer`   |     | ✅    |                |
| `karma_upvote`                   | Upvote                                 | `integer`   |     | ✅    |                |
| `karma_user_bio`                 | Display detailed user biography        | `integer`   |     | ✅    |                |
| `last_post_id`                   | Last Post                              | `many2one`  |     |       | forum.post     |
| `message_attachment_count`       | Attachment Count                       | `integer`   |     |       |                |
| `message_follower_ids`           | Followers                              | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`              | Message Delivery error                 | `boolean`   |     |       |                |
| `message_has_error_counter`      | Number of errors                       | `integer`   |     |       |                |
| `message_has_sms_error`          | SMS Delivery error                     | `boolean`   |     |       |                |
| `message_ids`                    | Messages                               | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`            | Is Follower                            | `boolean`   |     |       |                |
| `message_needaction`             | Action Needed                          | `boolean`   |     |       |                |
| `message_needaction_counter`     | Number of Actions                      | `integer`   |     |       |                |
| `message_partner_ids`            | Followers (Partners)                   | `many2many` |     |       | res.partner    |
| `mode`                           | Mode                                   | `selection` | ✅  | ✅    |                |
| `name`                           | Forum Name                             | `char`      | ✅  | ✅    |                |
| `post_ids`                       | Posts                                  | `one2many`  |     | ✅    | forum.post     |
| `privacy`                        | Privacy                                | `selection` |     | ✅    |                |
| `rating_ids`                     | Ratings                                | `one2many`  |     | ✅    | rating.rating  |
| `relevancy_post_vote`            | First Relevance Parameter              | `float`     |     | ✅    |                |
| `relevancy_time_decay`           | Second Relevance Parameter             | `float`     |     | ✅    |                |
| `seo_name`                       | Seo name                               | `char`      |     | ✅    |                |
| `sequence`                       | Sequence                               | `integer`   |     | ✅    |                |
| `tag_ids`                        | Tags                                   | `one2many`  |     | ✅    | forum.tag      |
| `tag_most_used_ids`              | Most used tags                         | `one2many`  |     |       | forum.tag      |
| `tag_unused_ids`                 | Unused tags                            | `one2many`  |     |       | forum.tag      |
| `total_answers`                  | # Answers                              | `integer`   |     |       |                |
| `total_favorites`                | # Favorites                            | `integer`   |     |       |                |
| `total_posts`                    | # Posts                                | `integer`   |     |       |                |
| `total_views`                    | # Views                                | `integer`   |     |       |                |
| `website_id`                     | Website                                | `many2one`  |     | ✅    | website        |
| `website_message_ids`            | Website Messages                       | `one2many`  |     | ✅    | mail.message   |
| `website_meta_description`       | Website meta description               | `text`      |     | ✅    |                |
| `website_meta_keywords`          | Website meta keywords                  | `char`      |     | ✅    |                |
| `website_meta_og_img`            | Website opengraph image                | `char`      |     | ✅    |                |
| `website_meta_title`             | Website meta title                     | `char`      |     | ✅    |                |
| `welcome_message`                | Welcome Message                        | `html`      |     | ✅    |                |
| `write_date`                     | Last Updated on                        | `datetime`  |     | ✅    |                |
| `write_uid`                      | Last Updated by                        | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name                | Group         | Perms     |
| ------------------- | ------------- | --------- |
| forum.forum.maanger | Access Rights | `R/W/C/D` |
| forum.forum         | Role / Portal | `R`       |
| forum.forum         | Role / Public | `R`       |
| forum.forum         | Role / User   | `R`       |

**Record Rules:**

- **Website forum: Public user can only access to public forum** (11) `R/W/C/D`
  - Domain: `[('privacy', '=', 'public')]`
- **Website forum: User can only access to public (or authorized) forum** (10, 1)
  `R/W/C/D`
  - Domain:
    `[         '|',             ('privacy', 'in', ['public', 'connected']),             '&',                 ('privacy', '=', 'private'),                 ('authorized_group_id', 'in', user.all_group_ids.ids)]`
- **Website forum: Website designer can create private forum** (72) `C`
  - Domain: `[(1, '=', 1)]`
- **Website forum: All access for manager** (2) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `forum.post` — Forum Post

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                                           | Type        | Req | Store | Relation          |
| ---------------------------- | ----------------------------------------------- | ----------- | --- | ----- | ----------------- |
| `active`                     | Active                                          | `boolean`   |     | ✅    |                   |
| `can_accept`                 | Can Accept                                      | `boolean`   |     |       |                   |
| `can_answer`                 | Can Answer                                      | `boolean`   |     |       |                   |
| `can_ask`                    | Can Ask                                         | `boolean`   |     |       |                   |
| `can_close`                  | Can Close                                       | `boolean`   |     |       |                   |
| `can_comment`                | Can Comment                                     | `boolean`   |     |       |                   |
| `can_comment_convert`        | Can Convert to Comment                          | `boolean`   |     |       |                   |
| `can_display_biography`      | Is the author's biography visible from his post | `boolean`   |     |       |                   |
| `can_downvote`               | Can Downvote                                    | `boolean`   |     |       |                   |
| `can_edit`                   | Can Edit                                        | `boolean`   |     |       |                   |
| `can_flag`                   | Can Flag                                        | `boolean`   |     |       |                   |
| `can_moderate`               | Can Moderate                                    | `boolean`   |     |       |                   |
| `can_post`                   | Can Automatically be Validated                  | `boolean`   |     |       |                   |
| `can_unlink`                 | Can Unlink                                      | `boolean`   |     |       |                   |
| `can_upvote`                 | Can Upvote                                      | `boolean`   |     |       |                   |
| `can_use_full_editor`        | Can Use Full Editor                             | `boolean`   |     |       |                   |
| `can_view`                   | Can View                                        | `boolean`   |     |       |                   |
| `child_count`                | Answers                                         | `integer`   |     | ✅    |                   |
| `child_ids`                  | Post Answers                                    | `one2many`  |     | ✅    | forum.post        |
| `closed_date`                | Closed on                                       | `datetime`  |     | ✅    |                   |
| `closed_reason_id`           | Reason                                          | `many2one`  |     | ✅    | forum.post.reason |
| `closed_uid`                 | Closed by                                       | `many2one`  |     | ✅    | res.users         |
| `content`                    | Content                                         | `html`      |     | ✅    |                   |
| `course_id`                  | Course                                          | `many2one`  |     | ✅    | op.course         |
| `create_date`                | Asked on                                        | `datetime`  |     | ✅    |                   |
| `create_uid`                 | Created by                                      | `many2one`  |     | ✅    | res.users         |
| `display_name`               | Display Name                                    | `char`      |     |       |                   |
| `favourite_count`            | Favorite                                        | `integer`   |     | ✅    |                   |
| `favourite_ids`              | Favourite                                       | `many2many` |     | ✅    | res.users         |
| `flag_user_id`               | Flagged by                                      | `many2one`  |     | ✅    | res.users         |
| `forum_id`                   | Forum                                           | `many2one`  | ✅  | ✅    | forum.forum       |
| `has_message`                | Has Message                                     | `boolean`   |     |       |                   |
| `has_validated_answer`       | Is answered                                     | `boolean`   |     | ✅    |                   |
| `id`                         | ID                                              | `integer`   |     | ✅    |                   |
| `is_correct`                 | Correct                                         | `boolean`   |     | ✅    |                   |
| `is_seo_optimized`           | SEO optimized                                   | `boolean`   |     | ✅    |                   |
| `karma_accept`               | Convert comment to answer                       | `integer`   |     |       |                   |
| `karma_close`                | Karma to close                                  | `integer`   |     |       |                   |
| `karma_comment`              | Karma to comment                                | `integer`   |     |       |                   |
| `karma_comment_convert`      | Karma to convert comment to answer              | `integer`   |     |       |                   |
| `karma_edit`                 | Karma to edit                                   | `integer`   |     |       |                   |
| `karma_flag`                 | Flag a post as offensive                        | `integer`   |     |       |                   |
| `karma_unlink`               | Karma to unlink                                 | `integer`   |     |       |                   |
| `last_activity_date`         | Last activity on                                | `datetime`  | ✅  | ✅    |                   |
| `message_attachment_count`   | Attachment Count                                | `integer`   |     |       |                   |
| `message_follower_ids`       | Followers                                       | `one2many`  |     | ✅    | mail.followers    |
| `message_has_error`          | Message Delivery error                          | `boolean`   |     |       |                   |
| `message_has_error_counter`  | Number of errors                                | `integer`   |     |       |                   |
| `message_has_sms_error`      | SMS Delivery error                              | `boolean`   |     |       |                   |
| `message_ids`                | Messages                                        | `one2many`  |     | ✅    | mail.message      |
| `message_is_follower`        | Is Follower                                     | `boolean`   |     |       |                   |
| `message_needaction`         | Action Needed                                   | `boolean`   |     |       |                   |
| `message_needaction_counter` | Number of Actions                               | `integer`   |     |       |                   |
| `message_partner_ids`        | Followers (Partners)                            | `many2many` |     |       | res.partner       |
| `moderator_id`               | Reviewed by                                     | `many2one`  |     | ✅    | res.users         |
| `name`                       | Title                                           | `char`      |     | ✅    |                   |
| `parent_id`                  | Question                                        | `many2one`  |     | ✅    | forum.post        |
| `plain_content`              | Plain Content                                   | `text`      |     | ✅    |                   |
| `rating_ids`                 | Ratings                                         | `one2many`  |     | ✅    | rating.rating     |
| `relevancy`                  | Relevance                                       | `float`     |     | ✅    |                   |
| `self_reply`                 | Reply to own question                           | `boolean`   |     | ✅    |                   |
| `seo_name`                   | Seo name                                        | `char`      |     | ✅    |                   |
| `state`                      | Status                                          | `selection` |     | ✅    |                   |
| `tag_ids`                    | Tags                                            | `many2many` |     | ✅    | forum.tag         |
| `uid_has_answered`           | Has Answered                                    | `boolean`   |     |       |                   |
| `user_favourite`             | Is Favourite                                    | `boolean`   |     |       |                   |
| `user_vote`                  | My Vote                                         | `integer`   |     |       |                   |
| `views`                      | Views                                           | `integer`   |     | ✅    |                   |
| `vote_count`                 | Total Votes                                     | `integer`   |     | ✅    |                   |
| `vote_ids`                   | Votes                                           | `one2many`  |     | ✅    | forum.post.vote   |
| `website_id`                 | Website                                         | `many2one`  |     |       | website           |
| `website_message_ids`        | Website Messages                                | `one2many`  |     | ✅    | mail.message      |
| `website_meta_description`   | Website meta description                        | `text`      |     | ✅    |                   |
| `website_meta_keywords`      | Website meta keywords                           | `char`      |     | ✅    |                   |
| `website_meta_og_img`        | Website opengraph image                         | `char`      |     | ✅    |                   |
| `website_meta_title`         | Website meta title                              | `char`      |     | ✅    |                   |
| `website_url`                | Website URL                                     | `char`      |     |       |                   |
| `write_date`                 | Updated on                                      | `datetime`  |     | ✅    |                   |
| `write_uid`                  | Updated by                                      | `many2one`  |     | ✅    | res.users         |

**Access Rights:**

| Name                          | Group         | Perms     |
| ----------------------------- | ------------- | --------- |
| access_op_material_op_faculty | LMS / User    | `R/W/C/D` |
| forum.post.portal             | Role / Portal | `R/W/C/D` |
| forum.post.public             | Role / Public | `R`       |
| forum.post.user               | Role / User   | `R/W/C/D` |

**Record Rules:**

- **Website forum post: Public user can only access to public post** (11) `R/W/C/D`
  - Domain: `[('forum_id.privacy', '=', 'public')]`
- **Website forum post: User can only access to public (or authorized) post** (10, 1)
  `R/W/C/D`
  - Domain:
    `['|', ('forum_id.privacy', 'in', ['public', 'connected']), '&', ('forum_id.privacy', '=', 'private'), ('forum_id.authorized_group_id', 'in', user.all_group_ids.ids)]`
- **Website forum post : All access for manager** (2) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

### 🗃️ `forum.tag` — Forum Tag

> 📧 Mail Thread

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                          | Type        | Req | Store | Relation       |
| ---------------------------- | ------------------------------ | ----------- | --- | ----- | -------------- |
| `color`                      | Color                          | `integer`   |     | ✅    |                |
| `create_date`                | Created on                     | `datetime`  |     | ✅    |                |
| `create_uid`                 | Created by                     | `many2one`  |     | ✅    | res.users      |
| `display_name`               | Display Name                   | `char`      |     |       |                |
| `forum_id`                   | Forum                          | `many2one`  | ✅  | ✅    | forum.forum    |
| `has_message`                | Has Message                    | `boolean`   |     |       |                |
| `id`                         | ID                             | `integer`   |     | ✅    |                |
| `is_seo_optimized`           | SEO optimized                  | `boolean`   |     | ✅    |                |
| `message_attachment_count`   | Attachment Count               | `integer`   |     |       |                |
| `message_follower_ids`       | Followers                      | `one2many`  |     | ✅    | mail.followers |
| `message_has_error`          | Message Delivery error         | `boolean`   |     |       |                |
| `message_has_error_counter`  | Number of errors               | `integer`   |     |       |                |
| `message_has_sms_error`      | SMS Delivery error             | `boolean`   |     |       |                |
| `message_ids`                | Messages                       | `one2many`  |     | ✅    | mail.message   |
| `message_is_follower`        | Is Follower                    | `boolean`   |     |       |                |
| `message_needaction`         | Action Needed                  | `boolean`   |     |       |                |
| `message_needaction_counter` | Number of Actions              | `integer`   |     |       |                |
| `message_partner_ids`        | Followers (Partners)           | `many2many` |     |       | res.partner    |
| `name`                       | Name                           | `char`      | ✅  | ✅    |                |
| `post_ids`                   | Posts                          | `many2many` |     | ✅    | forum.post     |
| `posts_count`                | Number of Posts                | `integer`   |     | ✅    |                |
| `rating_ids`                 | Ratings                        | `one2many`  |     | ✅    | rating.rating  |
| `seo_name`                   | Seo name                       | `char`      |     | ✅    |                |
| `website_message_ids`        | Website Messages               | `one2many`  |     | ✅    | mail.message   |
| `website_meta_description`   | Website meta description       | `text`      |     | ✅    |                |
| `website_meta_keywords`      | Website meta keywords          | `char`      |     | ✅    |                |
| `website_meta_og_img`        | Website opengraph image        | `char`      |     | ✅    |                |
| `website_meta_title`         | Website meta title             | `char`      |     | ✅    |                |
| `website_url`                | Link to questions with the tag | `char`      |     |       |                |
| `write_date`                 | Last Updated on                | `datetime`  |     | ✅    |                |
| `write_uid`                  | Last Updated by                | `many2one`  |     | ✅    | res.users      |

**Access Rights:**

| Name             | Group         | Perms     |
| ---------------- | ------------- | --------- |
| forum.tag.portal | Role / Portal | `R/C`     |
| forum.tag.public | Role / Public | `R/C`     |
| forum.tag.user   | Role / User   | `R/W/C/D` |

**Record Rules:**

- **Website forum tag: Public user can only access to tag linked to public forum** (11)
  `R/W/C/D`
  - Domain: `[('forum_id.privacy', '=', 'public')]`
- **Website forum tag: User can only access to tag linked to public (or authorized)
  forum** (10, 1) `R/W/C/D`
  - Domain:
    `['|', ('forum_id.privacy', 'in', ['public', 'connected']), '&', ('forum_id.privacy', '=', 'private'), ('forum_id.authorized_group_id', 'in', user.all_group_ids.ids)]`
- **Website forum tag : Manager user can access to all tags** (2) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

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

### 🗃️ `forum.post.reason` — Post Closing Reason

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation  |
| -------------- | --------------- | ----------- | --- | ----- | --------- |
| `create_date`  | Created on      | `datetime`  |     | ✅    |           |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users |
| `display_name` | Display Name    | `char`      |     |       |           |
| `id`           | ID              | `integer`   |     | ✅    |           |
| `name`         | Closing Reason  | `char`      | ✅  | ✅    |           |
| `reason_type`  | Reason Type     | `selection` |     | ✅    |           |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |           |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users |

**Access Rights:**

| Name                     | Group         | Perms     |
| ------------------------ | ------------- | --------- |
| forum.post.reason.portal | Role / Portal | `R`       |
| forum.post.reason.public | Role / Public | `R`       |
| forum.post.reason.user   | Role / User   | `R/W/C/D` |

### 🗃️ `forum.post.vote` — Post Vote

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field          | Label           | Type        | Req | Store | Relation    |
| -------------- | --------------- | ----------- | --- | ----- | ----------- |
| `create_date`  | Create Date     | `datetime`  |     | ✅    |             |
| `create_uid`   | Created by      | `many2one`  |     | ✅    | res.users   |
| `display_name` | Display Name    | `char`      |     |       |             |
| `forum_id`     | Forum           | `many2one`  |     | ✅    | forum.forum |
| `id`           | ID              | `integer`   |     | ✅    |             |
| `post_id`      | Post            | `many2one`  | ✅  | ✅    | forum.post  |
| `recipient_id` | To              | `many2one`  |     | ✅    | res.users   |
| `user_id`      | User            | `many2one`  | ✅  | ✅    | res.users   |
| `vote`         | Vote            | `selection` | ✅  | ✅    |             |
| `write_date`   | Last Updated on | `datetime`  |     | ✅    |             |
| `write_uid`    | Last Updated by | `many2one`  |     | ✅    | res.users   |

**Access Rights:**

| Name                  | Group         | Perms     |
| --------------------- | ------------- | --------- |
| orum.post.vote.portal | Role / Portal | `R/W/C`   |
| forum.post.vote.user  | Role / User   | `R/W/C/D` |

**Record Rules:**

- **Website forum vote: own votes only** (10, 1) `R/W/C/D`
  - Domain: `[('user_id', '=', user.id)]`
- **Website forum vote: all votes** (2) `R/W/C/D`
  - Domain: `[(1, '=', 1)]`

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

### 🗃️ `website` — Website

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                                       | Label                                                            | Type        | Req | Store | Relation                 |
| ------------------------------------------- | ---------------------------------------------------------------- | ----------- | --- | ----- | ------------------------ |
| `account_on_checkout`                       | Customer Accounts                                                | `selection` |     | ✅    |                          |
| `add_to_cart_action`                        | Add To Cart Action                                               | `selection` |     | ✅    |                          |
| `auth_signup_uninvited`                     | Customer Account                                                 | `selection` |     | ✅    |                          |
| `auto_redirect_lang`                        | Autoredirect Language                                            | `boolean`   |     | ✅    |                          |
| `blocked_third_party_domains`               | List of blocked 3rd-party domains                                | `text`      |     |       |                          |
| `block_third_party_domains`                 | Block 3rd-party domains                                          | `boolean`   |     | ✅    |                          |
| `cart_abandoned_delay`                      | Abandoned Delay                                                  | `float`     |     | ✅    |                          |
| `cart_recovery_mail_template_id`            | Cart Recovery Email                                              | `many2one`  |     | ✅    | mail.template            |
| `cdn_activated`                             | Content Delivery Network (CDN)                                   | `boolean`   |     | ✅    |                          |
| `cdn_filters`                               | CDN Filters                                                      | `text`      |     | ✅    |                          |
| `cdn_url`                                   | CDN Base URL                                                     | `char`      |     | ✅    |                          |
| `channel_id`                                | Website Live Chat Channel                                        | `many2one`  |     | ✅    | im_livechat.channel      |
| `company_id`                                | Company                                                          | `many2one`  | ✅  | ✅    | res.company              |
| `configurator_done`                         | Configurator Done                                                | `boolean`   |     | ✅    |                          |
| `confirmation_email_template_id`            | Confirmation Email Template                                      | `many2one`  |     | ✅    | mail.template            |
| `contact_us_button_url`                     | Contact Us Button URL                                            | `char`      |     | ✅    |                          |
| `cookies_bar`                               | Cookies Bar                                                      | `boolean`   |     | ✅    |                          |
| `create_date`                               | Created on                                                       | `datetime`  |     | ✅    |                          |
| `create_uid`                                | Created by                                                       | `many2one`  |     | ✅    | res.users                |
| `crm_default_team_id`                       | Default Sales Teams                                              | `many2one`  |     | ✅    | crm.team                 |
| `crm_default_user_id`                       | Default Salesperson                                              | `many2one`  |     | ✅    | res.users                |
| `currency_id`                               | Default Currency                                                 | `many2one`  |     |       | res.currency             |
| `custom_blocked_third_party_domains`        | User list of blocked 3rd-party domains                           | `text`      |     | ✅    |                          |
| `custom_code_footer`                        | Custom end of <body> code                                        | `html`      |     | ✅    |                          |
| `custom_code_head`                          | Custom <head> code                                               | `html`      |     | ✅    |                          |
| `default_lang_id`                           | Default Language                                                 | `many2one`  | ✅  | ✅    | res.lang                 |
| `display_name`                              | Display Name                                                     | `char`      |     |       |                          |
| `domain`                                    | Website Domain                                                   | `char`      |     | ✅    |                          |
| `domain_punycode`                           | Punycode Domain                                                  | `char`      |     |       |                          |
| `ecommerce_access`                          | Ecommerce Access                                                 | `selection` | ✅  | ✅    |                          |
| `enabled_gmc_src`                           | Google Merchant Center                                           | `boolean`   |     | ✅    |                          |
| `favicon`                                   | Website Favicon                                                  | `binary`    |     | ✅    |                          |
| `forum_count`                               | Forum Count                                                      | `integer`   |     | ✅    |                          |
| `google_analytics_key`                      | Google Analytics Key                                             | `char`      |     | ✅    |                          |
| `google_maps_api_key`                       | Google Maps API Key                                              | `char`      |     | ✅    |                          |
| `google_search_console`                     | Google Search Console                                            | `char`      |     | ✅    |                          |
| `has_social_default_image`                  | Has Social Default Image                                         | `boolean`   |     | ✅    |                          |
| `homepage_url`                              | Homepage Url                                                     | `char`      |     | ✅    |                          |
| `id`                                        | ID                                                               | `integer`   |     | ✅    |                          |
| `karma_profile_min`                         | Minimal karma to see other user's profile                        | `integer`   |     | ✅    |                          |
| `language_count`                            | Number of languages                                              | `integer`   |     |       |                          |
| `language_ids`                              | Languages                                                        | `many2many` | ✅  | ✅    | res.lang                 |
| `logo`                                      | Website Logo                                                     | `binary`    |     | ✅    |                          |
| `menu_id`                                   | Main Menu                                                        | `many2one`  |     |       | website.menu             |
| `name`                                      | Website Name                                                     | `char`      | ✅  | ✅    |                          |
| `newsletter_id`                             | Newsletter List                                                  | `many2one`  |     | ✅    | mailing.list             |
| `partner_id`                                | Public Partner                                                   | `many2one`  |     |       | res.partner              |
| `plausible_shared_key`                      | Plausible Shared Key                                             | `char`      |     | ✅    |                          |
| `plausible_site`                            | Plausible Site                                                   | `char`      |     | ✅    |                          |
| `prevent_zero_price_sale`                   | Hide 'Add To Cart' when price = 0                                | `boolean`   |     | ✅    |                          |
| `pricelist_ids`                             | Price list available for this Ecommerce/Website                  | `one2many`  |     |       | product.pricelist        |
| `product_page_cols_order`                   | Product Page main columns order                                  | `selection` |     | ✅    |                          |
| `product_page_container`                    | Product Page Container                                           | `selection` |     | ✅    |                          |
| `product_page_grid_columns`                 | Product Page Grid Columns                                        | `integer`   |     | ✅    |                          |
| `product_page_image_layout`                 | Product Page Image Layout                                        | `selection` | ✅  | ✅    |                          |
| `product_page_image_ratio`                  | Product Page Image Ratio                                         | `selection` | ✅  | ✅    |                          |
| `product_page_image_ratio_mobile`           | Product Page Image Ratio Mobile                                  | `selection` | ✅  | ✅    |                          |
| `product_page_image_roundness`              | Product Page Image Roundness                                     | `selection` | ✅  | ✅    |                          |
| `product_page_image_spacing`                | Product Page Image Spacing                                       | `selection` | ✅  | ✅    |                          |
| `product_page_image_width`                  | Product Page Image Width                                         | `selection` | ✅  | ✅    |                          |
| `robots_txt`                                | Robots.txt                                                       | `html`      |     | ✅    |                          |
| `salesperson_id`                            | Salesperson                                                      | `many2one`  |     | ✅    | res.users                |
| `salesteam_id`                              | Sales Team                                                       | `many2one`  |     | ✅    | crm.team                 |
| `send_abandoned_cart_email`                 | Send email to customers who abandoned their cart.                | `boolean`   |     | ✅    |                          |
| `send_abandoned_cart_email_activation_time` | Time when the 'Send abandoned cart email' feature was activated. | `datetime`  |     | ✅    |                          |
| `sequence`                                  | Sequence                                                         | `integer`   |     | ✅    |                          |
| `shop_default_sort`                         | Shop Default Sort                                                | `selection` | ✅  | ✅    |                          |
| `shop_extra_field_ids`                      | E-Commerce Extra Fields                                          | `one2many`  |     | ✅    | website.sale.extra.field |
| `shop_gap`                                  | Grid-gap on the shop                                             | `char`      |     | ✅    |                          |
| `shop_opt_products_design_classes`          | Shop Design Class                                                | `char`      |     | ✅    |                          |
| `shop_page_container`                       | Shop Page Container                                              | `selection` |     | ✅    |                          |
| `shop_ppg`                                  | Number of products in the grid on the shop                       | `integer`   |     | ✅    |                          |
| `shop_ppr`                                  | Number of grid columns on the shop                               | `integer`   |     | ✅    |                          |
| `show_line_subtotals_tax_selection`         | Line Subtotals Tax Display                                       | `selection` |     | ✅    |                          |
| `social_default_image`                      | Default Social Share Image                                       | `binary`    |     | ✅    |                          |
| `social_discord`                            | Discord Account                                                  | `char`      |     | ✅    |                          |
| `social_facebook`                           | Facebook Account                                                 | `char`      |     | ✅    |                          |
| `social_github`                             | GitHub Account                                                   | `char`      |     | ✅    |                          |
| `social_instagram`                          | Instagram Account                                                | `char`      |     | ✅    |                          |
| `social_linkedin`                           | LinkedIn Account                                                 | `char`      |     | ✅    |                          |
| `social_tiktok`                             | TikTok Account                                                   | `char`      |     | ✅    |                          |
| `social_twitter`                            | X Account                                                        | `char`      |     | ✅    |                          |
| `social_youtube`                            | Youtube Account                                                  | `char`      |     | ✅    |                          |
| `specific_user_account`                     | Specific User Account                                            | `boolean`   |     | ✅    |                          |
| `theme_id`                                  | Theme                                                            | `many2one`  |     | ✅    | ir.module.module         |
| `user_id`                                   | Public User                                                      | `many2one`  | ✅  | ✅    | res.users                |
| `warehouse_id`                              | Warehouse                                                        | `many2one`  |     | ✅    | stock.warehouse          |
| `wishlist_gap`                              | Wishlist Grid Gap                                                | `char`      |     | ✅    |                          |
| `wishlist_grid_columns`                     | Wishlist Grid Columns                                            | `integer`   |     | ✅    |                          |
| `wishlist_mobile_columns`                   | Wishlist Mobile Columns                                          | `integer`   |     | ✅    |                          |
| `wishlist_opt_products_design_classes`      | Wishlist Page Design Class                                       | `char`      |     | ✅    |                          |
| `write_date`                                | Last Updated on                                                  | `datetime`  |     | ✅    |                          |
| `write_uid`                                 | Last Updated by                                                  | `many2one`  |     | ✅    | res.users                |

**Access Rights:**

| Name                     | Group                         | Perms     |
| ------------------------ | ----------------------------- | --------- |
| website.website.designer | Website / Editor and Designer | `R/W/C/D` |
| website.public           | Role / Portal                 | `R`       |
| website.public           | Role / Public                 | `R`       |
| website.public           | Role / User                   | `R`       |
