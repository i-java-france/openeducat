# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpSection(models.Model):
    """Section
    """

    _name = 'op.section'
    _description = 'Section'

    # ── Fields ──────────────────────────────────────────────
    batch_ids = fields.Many2many('op.batch', string='Batch')
    color = fields.Integer(string='Color Index')
    company_id = fields.Many2one('res.company', string='Company')
    course_ids = fields.Many2many('op.course', string='Course')
    name = fields.Char(string='Name', required=True)
    student_count = fields.Integer(string='Student Count', store=False)
    student_course_ids = fields.Many2many('op.student.course', string='Student')
    subject_id = fields.Many2one('op.subject', string='Subject')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read, write

    # Record Rules:
    #   Section Multi  Company: ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_student_count(self):
        for rec in self:
            rec.student_count = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
