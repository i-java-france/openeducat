# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpSubjectFaculty(models.Model):
    """Subject Faculty Line
    """

    _name = 'op.subject.faculty'
    _description = 'Subject Faculty Line'

    # ── Fields ──────────────────────────────────────────────
    academic_plan_id = fields.Many2one('op.academic.plan', string='Academic Plan')
    company_id = fields.Many2one('res.company', string='Company', store=False)
    course_plan_id = fields.Many2one('op.course.plan', string='Course Plan')
    credit = fields.Float(string='Credit')
    faculty_id = fields.Many2one('op.faculty', string='Faculty')
    marks_line = fields.One2many('op.marks.line', 'subject_faculty_id', string='Marks Line')
    marks_line_count = fields.Integer(string='Marks Line Count', store=False)
    sequence = fields.Char(string='Sequence')
    subject_id = fields.Many2one('op.subject', string='Subject', required=True)
    subject_ids = fields.Many2many('op.subject', string='Subjects')
    subject_type = fields.Selection(string='Subject Type', required=True, selection=[])
    topics_count = fields.Integer(string='Topics Count', store=False)
    topics_line = fields.One2many('op.topics', 'subject_faculty_id', string='Topics Line')
    total_lab = fields.Integer(string='Total Lab')
    total_lectures = fields.Integer(string='Total Lectures')
    total_marks = fields.Float(string='Total Marks', store=False)
    tuition = fields.Integer(string='Tuition')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_company_id(self):
        for rec in self:
            rec.company_id = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_marks_line_count(self):
        for rec in self:
            rec.marks_line_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_topics_count(self):
        for rec in self:
            rec.topics_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_total_marks(self):
        for rec in self:
            rec.total_marks = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
