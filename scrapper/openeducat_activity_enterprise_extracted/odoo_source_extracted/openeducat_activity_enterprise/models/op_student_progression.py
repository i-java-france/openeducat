# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpStudentProgression(models.Model):
    """Student progression
    """

    _inherit = ['op.student.progression', 'mail.thread', 'rating.mixin', 'website.published.mixin']
    _description = 'Student progression'

    # ── Fields ──────────────────────────────────────────────
    achievement_lines = fields.One2many('op.achievement', 'progression_id', string='Progression Achivement')
    active = fields.Boolean(string='Active')
    activity_lines = fields.One2many('op.activity', 'progression_id', string='Progression Activities')
    assignment_lines = fields.One2many('op.assignment.sub.line', 'progression_id', string='Progression Assignment')
    attendance_lines = fields.One2many('op.attendance.line', 'progression_id', string='Progression Attendance')
    company_id = fields.Many2one('res.company', string='Company')
    created_by = fields.Many2one('res.users', string='Created By')
    date = fields.Date(string='Date', required=True)
    discipline_lines = fields.One2many('op.discipline', 'progression_id', string='Progression Discipline')
    grade_book = fields.Char(string='GradeBook')
    marksheet_lines = fields.One2many('op.marksheet.line', 'progression_id', string='Progression Marksheet')
    name = fields.Char(string='Sequence', required=True)
    state = fields.Selection(string='Status', selection=[]  # TODO: add selection values)
    student_id = fields.Many2one('op.student', string='Student', required=True)
    total_achievement = fields.Integer(string='Total Achievement')
    total_activity = fields.Integer(string='Total Activity')
    total_assignment = fields.Integer(string='Total Assignment')
    total_attendance = fields.Integer(string='Total Attendance')
    total_discipline = fields.Integer(string='Total Discipline')
    total_marksheet_line = fields.Integer(string='Total Marksheet')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, has_message, id, message_attachment_count, message_follower_ids, message_has_error, message_has_error_counter, message_has_sms_error ...

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read, write, create

    # Record Rules:
    #   Student progression multi-company: ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
