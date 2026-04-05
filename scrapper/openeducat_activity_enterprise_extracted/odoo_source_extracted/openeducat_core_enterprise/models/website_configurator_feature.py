# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class WebsiteConfiguratorFeature(models.Model):
    """Website Configurator Feature
    """

    _name = 'website.configurator.feature'
    _description = 'Website Configurator Feature'

    # ── Fields ──────────────────────────────────────────────
    active = fields.Boolean(string='Active')
    description = fields.Char(string='Description')
    feature_url = fields.Char(string='Feature Url')
    iap_page_code = fields.Char(string='Iap Page Code', help='Page code used to tell IAP website_service for which page a snippet list should be generated')
    icon = fields.Char(string='Icon')
    image = fields.Binary(string='Image')
    is_openeducat = fields.Boolean(string='Is Openeducat')
    menu_company = fields.Boolean(string='Menu Company', help='If set, add the menu as a second level menu, as a child of "Company" menu.')
    menu_sequence = fields.Integer(string='Menu Sequence', help='If set, a website menu will be created for the feature.')
    module_id = fields.Many2one('ir.module.module', string='Module')
    name = fields.Char(string='Name')
    page_view_id = fields.Many2one('ir.ui.view', string='Page View')
    sequence = fields.Integer(string='Sequence')
    website_config_preselection = fields.Char(string='Website Config Preselection', help='Comma-separated list of website type/purpose for which this feature should be pre-selected')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   Website / Editor and Designer: read, write, create, unlink

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
