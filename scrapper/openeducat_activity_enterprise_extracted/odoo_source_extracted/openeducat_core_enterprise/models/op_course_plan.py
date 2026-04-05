# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpCoursePlan(models.Model):
    """Course Plan
    """

    _inherit = ['op.course.plan', 'mail.thread', 'rating.mixin', 'website.published.mixin']
    _description = 'Course Plan'

    # ── Fields ──────────────────────────────────────────────
    academic_plan_id = fields.Many2one('op.academic.plan', string='Academic Plan')
    academic_term_id = fields.Many2one('op.academic.term', string='Academic Term', required=True)
    copo_line_ids = fields.One2many('copo.lines', 'course_plan_id', string='CO PO Lines')
    copo_lines_count = fields.Integer(string='CO PO Lines Count', store=False)
    course_credit = fields.One2many('course.credit', 'course_plan_id', string='Course Credit')
    course_id = fields.Many2one('op.course', string='Course', required=True)
    course_ids = fields.Many2many('op.course', string='Courses')
    fees_term_id = fields.Many2one('op.fees.terms', string='Fees Term')
    name = fields.Char(string='Name', store=False)
    subject_configure_count = fields.Integer(string='Subject Configure Count', store=False)
    subject_faculty_line = fields.One2many('op.subject.faculty', 'course_plan_id', string='Configure Subjects')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, has_message, id, message_attachment_count, message_follower_ids, message_has_error, message_has_error_counter, message_has_sms_error ...

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read, write

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_copo_lines_count(self):
        for rec in self:
            rec.copo_lines_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_name(self):
        for rec in self:
            rec.name = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_subject_configure_count(self):
        for rec in self:
            rec.subject_configure_count = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
