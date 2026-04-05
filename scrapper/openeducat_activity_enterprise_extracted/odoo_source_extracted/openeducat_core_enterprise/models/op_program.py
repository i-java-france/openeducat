# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpProgram(models.Model):
    """Thesis Program
    """

    _inherit = ['op.program', 'mail.thread', 'rating.mixin', 'website.published.mixin']
    _description = 'Thesis Program'

    # ── Fields ──────────────────────────────────────────────
    active = fields.Boolean(string='Active')
    admission_count = fields.Integer(string='Admission Count', store=False)
    area_id = fields.Many2one('op.area', string='Area')
    batch_count = fields.Integer(string='Batch Count', store=False)
    code = fields.Char(string='Code', required=True)
    color = fields.Integer(string='Color Index')
    company_id = fields.Many2one('res.company', string='Company')
    course_count = fields.Integer(string='Course Count', store=False)
    department_id = fields.Many2one('op.department', string='Department')
    evaluation_template_id = fields.Many2one('op.thesis.evaluation.template', string='Evaluation Template')
    full_description = fields.Html(string='Full Description')
    image_1920 = fields.Binary(string='Image')
    max_unit_load = fields.Float(string='Maximum Unit Load')
    min_unit_load = fields.Float(string='Minimum Unit Load')
    name = fields.Char(string='Name', required=True)
    program_level_id = fields.Many2one('op.program.level', string='Program Level', required=True)
    program_sessions_count = fields.Integer(string='Session Count', store=False)
    required_thesis = fields.Boolean(string='Required Thesis')
    short_desc = fields.Text(string='Short Description')
    student_count = fields.Integer(string='Student Count', store=False)
    subject_count = fields.Integer(string='Subject Count', store=False)
    thesis_duration = fields.Integer(string='Thesis Duration (months)')
    thesis_guidelines = fields.Html(string='Thesis Guidelines')
    user_id = fields.Many2one('res.users', string='User')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, has_message, id, message_attachment_count, message_follower_ids, message_has_error, message_has_error_counter, message_has_sms_error ...

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read

    # Record Rules:
    #   Program multi-company: ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_admission_count(self):
        for rec in self:
            rec.admission_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_batch_count(self):
        for rec in self:
            rec.batch_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_course_count(self):
        for rec in self:
            rec.course_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_program_sessions_count(self):
        for rec in self:
            rec.program_sessions_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_student_count(self):
        for rec in self:
            rec.student_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_subject_count(self):
        for rec in self:
            rec.subject_count = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
