# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpTopics(models.Model):
    """Topics
    """

    _name = 'op.topics'
    _description = 'Topics'

    # ── Fields ──────────────────────────────────────────────
    academic_plan_id = fields.Many2one('op.academic.plan', string='Academic Plan')
    description = fields.Text(string='Description')
    name = fields.Char(string='Name')
    parent_id = fields.Many2one('op.topics', string='Parent')
    subject_faculty_id = fields.Many2one('op.subject.faculty', string='Subject Faculty')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read, write

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
