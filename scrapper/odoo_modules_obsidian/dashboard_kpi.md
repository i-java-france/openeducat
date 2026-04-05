---
title: "Dashboard KPI"
module: "dashboard_kpi"
state: "installed"
version: "19.0.1.0"
author: "OpenEduCat Inc"
maintainer: "N/A"
website: "http://www.openeducat.org"
license: "Other proprietary"
category: "Tools"
application: false
auto_install: false
tags: [odoo/module, odoo/state/installed, odoo/category/_____]
---

# 🟢 Dashboard KPI

> **Module:** `dashboard_kpi` | **Version:** `19.0.1.0` **Category:** Tools |
> **License:** `Other proprietary` **Author:** OpenEduCat Inc **Website:**
> http://www.openeducat.org

## 🔗 Dependencies

[[base]] [[web]] [[base_setup]]

## 📖 Description

## Dashboard Pro

### Dashboard Pro is a Responsive Dashboard with customizable And Easy Configurable Item Settings. Dashboard Pro Helps You Make Eye On Your Important Data Easily. It Contains Multiple Tile View, Kpi View, List View, Multiple Chart View.

[![](/dashboard_kpi/static/description/Dashboard_01.png)](#)

Dashboard Anywhere

Editable Layout

Copy Or Move Item To Any Dashboard

Dashboard Filtering

Multi Company Support

## Chart View

![](/dashboard_kpi/static/description/Dashboard_07.png)

- Dashboard Pro Provide Multiple Types Of Charts Like Bar, Horizontal Bar, Line, Area,
  Pie, Doughnut, Polar Area.
- It Let You Choose Which Model & Field Value You Want In Chart. There Is Also Filtering
  & Sorting Feature
- You Can Export Chart As Excel, Csv, PDF, Image And Json. Json File Can Be Imported In
  Dashboard Later.
- Dashboard Pro Features 4 Different Colouring Options.

## Great Chart Features

Configure Data And Keep Track Of Your Data.

Multiple Color Selection For Chart Like Cool, Warm, Neon And Default.

Import Chart As CSV, Image, Excel, PDF And JSON

## Tile & KPI

- Dashboard Pro Provides Different Elements Like Tile View & KPI View. There Is 6
  Stunning And Good Looking Tile Layouts.
- It Provides To Select Different Icon From Font Awesome And Also Let You Select Your
  Favourite Color.It Also Let You Select Color For Font And Background From Display Tab.
- Dashboard Pro Let You Customize Menu Title And It's Value From Different Models In
  Data Tab. In KPI View You Can Select Between Progress Bar Or Percent In Target Tab.
  Also You Can Compare With Another Model in Sum , Ratio And Percentage.

![](/dashboard_kpi/static/description/Dashboard_05.png)

## Beautiful List & KPI Features

Predefined 6 Beautiful And Responsive Tile Layouts

Favourite Icon Font And Color Selection.

Compare Different Data Or Set Your Target To Achieve.

## List View

![](/dashboard_kpi/static/description/Dashboard_06.png)

- Dashboard Pro Also Provides List View. Which Let You Add Different Fields In List.
  Dashboard Pro Also Let You Customize Individual Record From List In Dashboard.
- Add Field From Any Model Into Column Of List View With Un-Grouped And Grouped Options.

## Features Of List

Edit Record Directly From List.

Add Your Column To Keep Track.

## Filtering!!

- Dashboard Pro Let You Filter Elements By Date With Multiple Date Filter Options Like
  This Week, Next Week, Last Week, Last 7 Days. Dashboard Pro Also Feature Custom Date
  Filter.

- Dashboard Pro Provide Filtering In Record By Limiting Records.

![](/dashboard_kpi/static/description/Dashboard_08.png)

## Filtering Is Time Saver

Get Specific Time Related Data With Filtering.

Filter From Dashboard Or From Individual Item.

## Choose The Rights!

![](/dashboard_kpi/static/description/Dashboard_04.png)

- Dashboard Pro Provide Feature To Choose Who Can Get All Feature Like Add New Element
  To Dashboard & Who Can Mess With Your Layout Of Dashboard.

## Privacy Is Important

Choose Who Can Access Features Of Dashboard Pro.

Access Right So Not EveryOne Can Play With Your Dashboard.

## Dashboard Under Any Menu!!

- Dashboard List And Configuration. Dashboard Pro Allow To Add As Many Dashboard AS You
  Want. Dashboard Can Be Created And Added Under Any Menu With Customizable Menu Name
  And Dashboard Name.

![](/dashboard_kpi/static/description/Dashboard_03.png)

## Dashboard Anywhere

Get Dashboard Under Any Of Your Favourite Menu.

Create Dashboard With Simple And Easy Filling Data.

## 🖥️ UI Components

### Menus

- `KPI Dashboard`
- `KPI Dashboard/Create Dashboard`
- `KPI Dashboard/My Dashboard`

### Views

- `dashboard_pro Theme View (form)`
- `dashboard_pro View (form)`
- `dashboard_pro theme tree (list)`
- `dashboard_pro tree (list)`
- `dashboard_pro_element form (form)`
- `dashboard_pro_element tree (list)`

### Reports

_none_

## 🛠️ Technical Documentation

**8 model(s) defined by this module:**

### 🗃️ `dashboard_pro.element_action` — Dashboard Element Action Model

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                  | Type        | Req | Store | Relation              |
| ---------------------------- | ---------------------- | ----------- | --- | ----- | --------------------- |
| `chart_type`                 | Item Type              | `selection` |     | ✅    |                       |
| `create_date`                | Created on             | `datetime`  |     | ✅    |                       |
| `create_uid`                 | Created by             | `many2one`  |     | ✅    | res.users             |
| `dashboard_item_id`          | Dashboard Item         | `many2one`  |     | ✅    | dashboard_pro.element |
| `display_name`               | Display Name           | `char`      |     |       |                       |
| `id`                         | ID                     | `integer`   |     | ✅    |                       |
| `item_action_date_groupby`   | Group By Date          | `selection` |     | ✅    |                       |
| `item_action_field`          | Action Group By        | `many2one`  |     | ✅    | ir.model.fields       |
| `item_action_field_type`     | Item Action Field Type | `char`      |     |       |                       |
| `model_id`                   | Model                  | `many2one`  |     |       | ir.model              |
| `record_limit`               | Record Limit           | `integer`   |     | ✅    |                       |
| `sequence`                   | Sequence               | `integer`   |     | ✅    |                       |
| `sorting_selection`          | Sort Order             | `selection` |     | ✅    |                       |
| `sorting_selection_by_field` | Sort By Field          | `many2one`  |     | ✅    | ir.model.fields       |
| `write_date`                 | Last Updated on        | `datetime`  |     | ✅    |                       |
| `write_uid`                  | Last Updated by        | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                                       | Group         | Perms     |
| ------------------------------------------ | ------------- | --------- |
| access_dashboard_pro_element_action_portal | Role / Portal | `R`       |
| access_dashboard_pro_element_action_public | Role / Public | `R`       |
| access_dashboard_pro_element_action        | Role / User   | `R/W/C/D` |

### 🗃️ `dashboard_pro.element` — Dashboard Element Model And object

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                            | Label                                  | Type        | Req | Store | Relation                     |
| -------------------------------- | -------------------------------------- | ----------- | --- | ----- | ---------------------------- |
| `action_lines`                   | Action Lines                           | `one2many`  |     | ✅    | dashboard_pro.element_action |
| `actions`                        | Actions                                | `many2one`  |     | ✅    | ir.actions.act_window        |
| `add_divider_line`               | Add Divider Line                       | `selection` |     | ✅    |                              |
| `add_image_image`                | Image                                  | `binary`    |     | ✅    |                              |
| `add_link_content`               | Link                                   | `char`      |     | ✅    |                              |
| `add_link_preview`               | Link Preview                           | `integer`   |     | ✅    |                              |
| `add_link_title`                 | Add Name As Title?                     | `boolean`   |     | ✅    |                              |
| `add_text_align`                 | Add Text Align                         | `selection` |     | ✅    |                              |
| `add_text_custom_bold`           | Bold Text                              | `boolean`   |     | ✅    |                              |
| `add_text_custom_font_size`      | Font Size                              | `integer`   |     | ✅    |                              |
| `add_text_custom_italic`         | Italic Text                            | `boolean`   |     | ✅    |                              |
| `add_text_font_style`            | Add Text Font Style                    | `selection` |     | ✅    |                              |
| `add_text_main_content`          | Text Content                           | `text`      |     | ✅    |                              |
| `add_text_preview`               | Text Preview                           | `integer`   |     | ✅    |                              |
| `background_color`               | Background Color                       | `char`      |     | ✅    |                              |
| `bar_chart_stacked`              | Stacked Bar Chart                      | `boolean`   |     | ✅    |                              |
| `chart_data`                     | Chart Data in string form              | `char`      |     |       |                              |
| `chart_data_calculation_field`   | Measure 1                              | `many2many` |     | ✅    | ir.model.fields              |
| `chart_data_calculation_field_2` | Line Measure                           | `many2many` |     | ✅    | ir.model.fields              |
| `chart_group_field`              | Dashboard Item Chart Group By Type     | `selection` |     | ✅    |                              |
| `chart_sub_field`                | Sub Group By                           | `many2one`  |     | ✅    | ir.model.fields              |
| `chart_sub_field_date`           | Dashboard Item Chart Sub Group By Type | `selection` |     | ✅    |                              |
| `chart_theme_selection`          | Chart Chart Theme                      | `selection` |     | ✅    |                              |
| `chart_unit`                     | Enter Unit                             | `char`      |     | ✅    |                              |
| `company_id`                     | Company                                | `many2one`  |     | ✅    | res.company                  |
| `create_date`                    | Created on                             | `datetime`  |     | ✅    |                              |
| `create_uid`                     | Created by                             | `many2one`  |     | ✅    | res.users                    |
| `dashboard_pro_dashboard_id`     | Dashboard                              | `many2one`  |     | ✅    | dashboard_pro.main_dashboard |
| `data_calculation_type`          | Record Type                            | `selection` |     | ✅    |                              |
| `data_calculation_type_chart`    | Data Type                              | `selection` |     | ✅    |                              |
| `data_calculation_value`         | Record Count                           | `float`     |     |       |                              |
| `date_domain_fields`             | Date Filter Selection                  | `selection` | ✅  | ✅    |                              |
| `date_filter_field`              | Date Filter Field                      | `many2one`  |     | ✅    | ir.model.fields              |
| `date_filter_field_2`            | Kpi Date Filter Field                  | `many2one`  |     | ✅    | ir.model.fields              |
| `date_filter_selection_2`        | Kpi Date Filter Selection              | `selection` | ✅  | ✅    |                              |
| `default_icon`                   | Icon                                   | `char`      |     | ✅    |                              |
| `default_icon_color`             | Icon Color                             | `char`      |     | ✅    |                              |
| `display_name`                   | Display Name                           | `char`      |     |       |                              |
| `domain`                         | Domain                                 | `char`      |     | ✅    |                              |
| `domain_2`                       | Kpi Domain                             | `char`      |     | ✅    |                              |
| `element_end_date`               | End Date                               | `datetime`  |     | ✅    |                              |
| `element_start_date`             | Start Date                             | `datetime`  |     | ✅    |                              |
| `element_theme`                  | Theme                                  | `char`      |     | ✅    |                              |
| `ending_date_kpi_2`              | Kpi End Date                           | `datetime`  |     | ✅    |                              |
| `filter_limit`                   | Record Limit                           | `integer`   |     | ✅    |                              |
| `font_color`                     | Font Color                             | `char`      |     | ✅    |                              |
| `goal_line_field`                | Show Target As Line                    | `boolean`   |     | ✅    |                              |
| `goal_lines`                     | Target Lines                           | `one2many`  |     | ✅    | dashboard_pro.element_target |
| `goal_value_field`               | Standard Target                        | `float`     |     | ✅    |                              |
| `graph_preview`                  | Graph Preview                          | `char`      |     | ✅    |                              |
| `group_chart_field`              | Chart GroupBy                          | `char`      |     |       |                              |
| `group_chart_relation`           | Group By                               | `many2one`  |     | ✅    | ir.model.fields              |
| `icon`                           | Upload Icon                            | `binary`    |     | ✅    |                              |
| `id`                             | ID                                     | `integer`   |     | ✅    |                              |
| `ir_model_field_2`               | Model                                  | `many2one`  |     | ✅    | ir.model                     |
| `ir_model_field_2_name`          | Model Name                             | `char`      |     |       |                              |
| `is_goal_enable`                 | Enable Target                          | `boolean`   |     | ✅    |                              |
| `json_list_data`                 | List View Data in JSon                 | `char`      |     |       |                              |
| `json_todo_list_data`            | To-Do Data In Json                     | `char`      |     |       |                              |
| `kpi_compare_field`              | Kpi Data Type                          | `char`      |     | ✅    |                              |
| `kpi_data`                       | KPI Data                               | `char`      |     |       |                              |
| `kpi_preview`                    | Kpi Preview                            | `char`      |     | ✅    |                              |
| `layout`                         | Layout                                 | `selection` | ✅  | ✅    |                              |
| `list_data_grouping`             | List View Grouped Fields               | `many2many` |     | ✅    | ir.model.fields              |
| `list_fields_data`               | Fields to show in list                 | `many2many` |     | ✅    | ir.model.fields              |
| `list_goal_field`                | list_field_id                          | `many2one`  |     | ✅    | ir.model.fields              |
| `list_preview`                   | List View Preview                      | `char`      |     | ✅    |                              |
| `list_view_type`                 | List View Type                         | `selection` | ✅  | ✅    |                              |
| `many2many_field_ordering`       | Many2Many Field Ordering               | `char`      |     | ✅    |                              |
| `model_id`                       | Model                                  | `many2one`  |     | ✅    | ir.model                     |
| `model_name`                     | Model Name                             | `char`      |     |       |                              |
| `name`                           | Name:                                  | `char`      | ✅  | ✅    |                              |
| `preview`                        | Preview                                | `integer`   |     | ✅    |                              |
| `previous_data_field`            | Previous Period                        | `boolean`   |     | ✅    |                              |
| `record_count_2`                 | KPI Record Count                       | `float`     |     |       |                              |
| `selection_icon_field`           | Icon Option                            | `char`      |     | ✅    |                              |
| `semi_circle_chart`              | Semi Circle Chart                      | `boolean`   |     | ✅    |                              |
| `show_data_value`                | Show Data Value                        | `boolean`   |     | ✅    |                              |
| `show_records`                   | Show Records                           | `boolean`   |     | ✅    |                              |
| `sorting_selection`              | Sort Order                             | `selection` |     | ✅    |                              |
| `sorting_selection_by_field`     | Sort By Field                          | `many2one`  |     | ✅    | ir.model.fields              |
| `starting_date_kpi_2`            | Kpi Start Date                         | `datetime`  |     | ✅    |                              |
| `state_layout_state`             | State                                  | `selection` |     | ✅    |                              |
| `state_layout_state_1`           | State                                  | `selection` |     | ✅    |                              |
| `store_field_data`               | Record Field                           | `many2one`  |     | ✅    | ir.model.fields              |
| `store_field_data_2`             | Kpi Record Field                       | `many2one`  |     | ✅    | ir.model.fields              |
| `sub_group_chart_field`          | Sub Group Chart Field                  | `char`      |     |       |                              |
| `target_view`                    | View                                   | `char`      |     | ✅    |                              |
| `time_of_comparation`            | Include Period                         | `integer`   |     | ✅    |                              |
| `time_of_comparation_2`          | Include Period                         | `integer`   |     | ✅    |                              |
| `to_do_list_count`               | Total Of To Do List                    | `char`      |     |       |                              |
| `to_do_list_line`                | To Do List                             | `one2many`  |     | ✅    | to_do.list                   |
| `to_do_list_preview`             | To-Do List Preview                     | `char`      |     | ✅    |                              |
| `type_of_element`                | Dashboard Item Type                    | `selection` | ✅  | ✅    |                              |
| `unit`                           | Show Custom Unit                       | `boolean`   |     | ✅    |                              |
| `unit_selection`                 | Select Unit Type                       | `selection` |     | ✅    |                              |
| `update_element_data_time`       | Item Update Interval                   | `selection` |     | ✅    |                              |
| `write_date`                     | Last Updated on                        | `datetime`  |     | ✅    |                              |
| `write_uid`                      | Last Updated by                        | `many2one`  |     | ✅    | res.users                    |
| `year_period`                    | Same Period Previous Years             | `integer`   |     | ✅    |                              |
| `year_period_2`                  | Same Period Previous Years             | `integer`   |     | ✅    |                              |

**Access Rights:**

| Name                                | Group         | Perms     |
| ----------------------------------- | ------------- | --------- |
| access_dashboard_pro_element_portal | Role / Portal | `R`       |
| access_dashboard_pro_element_public | Role / Public | `R`       |
| access_dashboard_pro_element        | Role / User   | `R/W/C/D` |

**Record Rules:**

- **Dashboard Item Company Restriction: User Can only view their company and sub
  companies items. ** (Global) `R/W/C/D`
  - Domain:
    `             ['|','|',('company_id','=',False),('company_id','=',user.company_id.id),('company_id','child_of',[user.company_id.id])]         `

### 🗃️ `dashboard_pro.element_target` — Dashboard Element Target Object And Model.

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field               | Label           | Type       | Req | Store | Relation              |
| ------------------- | --------------- | ---------- | --- | ----- | --------------------- |
| `create_date`       | Created on      | `datetime` |     | ✅    |                       |
| `create_uid`        | Created by      | `many2one` |     | ✅    | res.users             |
| `dashboard_element` | Dashboard Item  | `many2one` |     | ✅    | dashboard_pro.element |
| `display_name`      | Display Name    | `char`     |     |       |                       |
| `goal_date`         | Date            | `date`     |     | ✅    |                       |
| `goal_value`        | Value           | `float`    |     | ✅    |                       |
| `id`                | ID              | `integer`  |     | ✅    |                       |
| `write_date`        | Last Updated on | `datetime` |     | ✅    |                       |
| `write_uid`         | Last Updated by | `many2one` |     | ✅    | res.users             |

**Access Rights:**

| Name                                       | Group         | Perms     |
| ------------------------------------------ | ------------- | --------- |
| access_dashboard_pro_element_target_portal | Role / Portal | `R`       |
| access_dashboard_pro_element_target_public | Role / Public | `R`       |
| access_dashboard_pro_element_target        | Role / User   | `R/W/C/D` |

### 🗃️ `pro_dashboard_pro.item_action` — Dashboard Item Action

> ✳️ Transient (Wizard)

Model super-class for transient records, meant to be temporarily persistent, and
regularly vacuum-cleaned.

    A TransientModel has a simplified access rights management, all users can
    create new records, and may only access the records they created. The
    superuser has unrestricted access to all TransientModel records.

**Fields:**

| Field                | Label             | Type        | Req | Store | Relation                     |
| -------------------- | ----------------- | ----------- | --- | ----- | ---------------------------- |
| `action`             | Action            | `selection` |     | ✅    |                              |
| `create_date`        | Created on        | `datetime`  |     | ✅    |                              |
| `create_uid`         | Created by        | `many2one`  |     | ✅    | res.users                    |
| `dashboard_item_ids` | Dashboard Items   | `many2many` |     | ✅    | dashboard_pro.element        |
| `dashboard_pro_id`   | Select Dashboard  | `many2one`  |     | ✅    | dashboard_pro.main_dashboard |
| `dashboard_pro_ids`  | Select Dashboards | `many2many` |     | ✅    | dashboard_pro.main_dashboard |
| `display_name`       | Display Name      | `char`      |     |       |                              |
| `id`                 | ID                | `integer`   |     | ✅    |                              |
| `name`               | Name              | `char`      |     | ✅    |                              |
| `write_date`         | Last Updated on   | `datetime`  |     | ✅    |                              |
| `write_uid`          | Last Updated by   | `many2one`  |     | ✅    | res.users                    |

**Access Rights:**

| Name                                        | Group         | Perms     |
| ------------------------------------------- | ------------- | --------- |
| access_pro_dashboard_pro_item_action_portal | Role / Portal | `R`       |
| access_pro_dashboard_pro_item_action_public | Role / Public | `R`       |
| access_pro_dashboard_pro_item_action        | Role / User   | `R/W/C/D` |

### 🗃️ `dashboard_pro.dashboard_template` — Dashboard Template

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label              | Type       | Req | Store | Relation  |
| -------------------- | ------------------ | ---------- | --- | ----- | --------- |
| `create_date`        | Created on         | `datetime` |     | ✅    |           |
| `create_uid`         | Created by         | `many2one` |     | ✅    | res.users |
| `display_name`       | Display Name       | `char`     |     |       |           |
| `grid_configuration` | Grid Configuration | `char`     |     | ✅    |           |
| `id`                 | ID                 | `integer`  |     | ✅    |           |
| `item_count`         | Item Count         | `integer`  |     | ✅    |           |
| `name`               | Name               | `char`     |     | ✅    |           |
| `write_date`         | Last Updated on    | `datetime` |     | ✅    |           |
| `write_uid`          | Last Updated by    | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                                           | Group         | Perms     |
| ---------------------------------------------- | ------------- | --------- |
| access_dashboard_pro_dashboard_template_portal | Role / Portal | `R`       |
| access_dashboard_pro_dashboard_template_public | Role / Public | `R`       |
| access_dashboard_pro_dashboard_template        | Role / User   | `R/W/C/D` |

### 🗃️ `dashboard_pro.main_dashboard` — Main Dashboard Model And Objects

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                        | Label                | Type        | Req | Store | Relation                         |
| ---------------------------- | -------------------- | ----------- | --- | ----- | -------------------------------- |
| `client_action`              | Client Action        | `many2one`  |     | ✅    | ir.actions.client                |
| `create_date`                | Created on           | `datetime`  |     | ✅    |                                  |
| `create_uid`                 | Created by           | `many2one`  |     | ✅    | res.users                        |
| `dashboard_active`           | Active               | `boolean`   |     | ✅    |                                  |
| `dashboard_default_template` | Dashboard Template   | `many2one`  |     | ✅    | dashboard_pro.dashboard_template |
| `dashboard_group_access`     | Group Access         | `many2many` |     | ✅    | res.groups                       |
| `dashboard_item_ids`         | Dashboard Items      | `one2many`  |     | ✅    | dashboard_pro.element            |
| `dashboard_menu_id`          | Dashboard Menu       | `many2one`  |     | ✅    | ir.ui.menu                       |
| `dashboard_menu_sequence`    | Menu Sequence        | `integer`   |     | ✅    |                                  |
| `dashboard_state`            | Dashboard State      | `char`      |     | ✅    |                                  |
| `dashboard_theme_id`         | Dashboard Theme      | `many2one`  |     | ✅    | dashboard_pro.theme              |
| `dashboard_top_menu_id`      | Show Under Menu      | `many2one`  |     | ✅    | ir.ui.menu                       |
| `date_domain_fields`         | Default Date Filter  | `selection` |     | ✅    |                                  |
| `display_name`               | Display Name         | `char`      |     |       |                                  |
| `ending_date_dashboard`      | End Date             | `datetime`  |     | ✅    |                                  |
| `grid_configuration`         | Item Configurations  | `char`      |     | ✅    |                                  |
| `id`                         | ID                   | `integer`   |     | ✅    |                                  |
| `interval_time`              | Update Interval Time | `selection` |     | ✅    |                                  |
| `menu_name_dashboard`        | Menu Name            | `char`      |     | ✅    |                                  |
| `name`                       | Dashboard Name       | `char`      | ✅  | ✅    |                                  |
| `starting_date_dashboard`    | Start Date           | `datetime`  |     | ✅    |                                  |
| `write_date`                 | Last Updated on      | `datetime`  |     | ✅    |                                  |
| `write_uid`                  | Last Updated by      | `many2one`  |     | ✅    | res.users                        |

**Access Rights:**

| Name                                       | Group         | Perms     |
| ------------------------------------------ | ------------- | --------- |
| access_dashboard_pro_main_dashboard_portal | Role / Portal | `R`       |
| access_dashboard_pro_main_dashboard_public | Role / Public | `R`       |
| access_dashboard_pro_main_dashboard        | Role / User   | `R/W/C/D` |

### 🗃️ `to_do.list` — Model For To Do List

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                | Label           | Type        | Req | Store | Relation              |
| -------------------- | --------------- | ----------- | --- | ----- | --------------------- |
| `create_date`        | Created on      | `datetime`  |     | ✅    |                       |
| `create_uid`         | Created by      | `many2one`  |     | ✅    | res.users             |
| `dashboard_to_do_id` | Dashboard To Do | `many2one`  |     | ✅    | dashboard_pro.element |
| `display_name`       | Display Name    | `char`      |     |       |                       |
| `id`                 | ID              | `integer`   |     | ✅    |                       |
| `name`               | Name:           | `char`      |     | ✅    |                       |
| `sequence`           | Sequence        | `integer`   | ✅  | ✅    |                       |
| `to_do_state`        | To Do State     | `selection` |     | ✅    |                       |
| `write_date`         | Last Updated on | `datetime`  |     | ✅    |                       |
| `write_uid`          | Last Updated by | `many2one`  |     | ✅    | res.users             |

**Access Rights:**

| Name                     | Group         | Perms     |
| ------------------------ | ------------- | --------- |
| access_to_do_list_portal | Role / Portal | `R`       |
| access_to_do_list_public | Role / Public | `R`       |
| access_to_do_list        | Role / User   | `R/W/C/D` |

### 🗃️ `dashboard_pro.theme` — Theme Of Dashboard

Main super-class for regular database-persisted Odoo models.

    Odoo models are created by inheriting from this class::

        class ResUsers(Model):
            ...

    The system will later instantiate the class once per database (on
    which the class' module is installed).

**Fields:**

| Field                             | Label           | Type       | Req | Store | Relation  |
| --------------------------------- | --------------- | ---------- | --- | ----- | --------- |
| `create_date`                     | Created on      | `datetime` |     | ✅    |           |
| `create_uid`                      | Created by      | `many2one` |     | ✅    | res.users |
| `dashboard_theme_font_color`      | Font Color      | `char`     |     | ✅    |           |
| `dashboard_theme_primary_color`   | Primary Color   | `char`     |     | ✅    |           |
| `dashboard_theme_secondary_color` | Secondary Color | `char`     |     | ✅    |           |
| `display_name`                    | Display Name    | `char`     |     |       |           |
| `id`                              | ID              | `integer`  |     | ✅    |           |
| `name`                            | Name            | `char`     |     | ✅    |           |
| `write_date`                      | Last Updated on | `datetime` |     | ✅    |           |
| `write_uid`                       | Last Updated by | `many2one` |     | ✅    | res.users |

**Access Rights:**

| Name                              | Group         | Perms     |
| --------------------------------- | ------------- | --------- |
| access_dashboard_pro_theme_portal | Role / Portal | `R`       |
| access_dashboard_pro_theme_public | Role / Public | `R`       |
| access_dashboard_pro_theme        | Role / User   | `R/W/C/D` |
