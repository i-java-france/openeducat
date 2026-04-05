# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpMarksLine(models.Model):
    """Marks Line
    """

    _name = 'op.marks.line'
    _description = 'Marks Line'

    # ── Fields ──────────────────────────────────────────────
    assessment_type_id = fields.Many2one('op.assessment.type', string='Assessment Type')
    maximum_marks = fields.Float(string='Maximum Marks')
    passing_marks = fields.Float(string='Passing Marks')
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
