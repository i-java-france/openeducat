# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpCourseCategory(models.Model):
    """Course Category
    """

    _name = 'op.course.category'
    _description = 'Course Category'

    # ── Fields ──────────────────────────────────────────────
    active = fields.Boolean(string='Active')
    code = fields.Char(string='Code', required=True)
    company_id = fields.Many2one('res.company', string='Company')
    desc = fields.Text(string='Description')
    icon = fields.Char(string='Icon')
    name = fields.Char(string='Name', required=True)
    parent_id = fields.Many2one('op.course.category', string='Parent Category')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read, write, create
    #   Role / Portal: read
    #   Role / Public: read
    #   Role / User: read

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
