# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class IrModuleModule(models.Model):
    """Module
    """

    _name = 'ir.module.module'
    _description = 'Module'

    # ── Fields ──────────────────────────────────────────────
    account_templates = fields.Binary(string='Account Templates', store=False)
    application = fields.Boolean(string='Application')
    author = fields.Char(string='Author')
    auto_install = fields.Boolean(string='Automatic Installation', help='An auto-installable module is automatically installed by the system when all its dependencies are satisfied. If the modu')
    category_id = fields.Many2one('ir.module.category', string='Category')
    contributors = fields.Text(string='Contributors')
    country_ids = fields.Many2many('res.country', string='Country')
    demo = fields.Boolean(string='Demo Data')
    dependencies_id = fields.One2many('ir.module.module.dependency', 'module_id', string='Dependencies')
    description = fields.Text(string='Description')
    description_html = fields.Html(string='Description HTML', store=False)
    exclusion_ids = fields.One2many('ir.module.module.exclusion', 'module_id', string='Exclusions')
    has_iap = fields.Boolean(string='Has Iap', store=False)
    icon = fields.Char(string='Icon URL')
    icon_flag = fields.Char(string='Flag', store=False)
    icon_image = fields.Binary(string='Icon', store=False)
    image_ids = fields.One2many('ir.attachment', 'res_id', string='Screenshots')
    imported = fields.Boolean(string='Imported Module')
    installed_version = fields.Char(string='Latest Version', store=False)
    is_installed_on_current_website = fields.Boolean(string='Is Installed On Current Website', store=False)
    latest_version = fields.Char(string='Installed Version')
    license = fields.Selection(string='License', selection=[])
    maintainer = fields.Char(string='Maintainer')
    menus_by_module = fields.Text(string='Menus')
    module_type = fields.Selection(string='Module Type', selection=[])
    name = fields.Char(string='Technical Name', required=True)
    published_version = fields.Char(string='Published Version')
    reports_by_module = fields.Text(string='Reports')
    sequence = fields.Integer(string='Sequence')
    shortdesc = fields.Char(string='Module Name')
    state = fields.Selection(string='Status', selection=[])
    summary = fields.Char(string='Summary')
    to_buy = fields.Boolean(string='Odoo Enterprise Module')
    url = fields.Char(string='URL')
    views_by_module = fields.Text(string='Views')
    website = fields.Char(string='Website')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   Role / Administrator: read, write, create, unlink
    #   Role / User: read

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_account_templates(self):
        for rec in self:
            rec.account_templates = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_description_html(self):
        for rec in self:
            rec.description_html = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_has_iap(self):
        for rec in self:
            rec.has_iap = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_icon_flag(self):
        for rec in self:
            rec.icon_flag = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_icon_image(self):
        for rec in self:
            rec.icon_image = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_installed_version(self):
        for rec in self:
            rec.installed_version = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_is_installed_on_current_website(self):
        for rec in self:
            rec.is_installed_on_current_website = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
