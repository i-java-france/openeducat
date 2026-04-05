# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpAcademicPlan(models.Model):
    """OpenEduCat Academic Plan
    """

    _inherit = ['op.academic.plan', 'mail.thread', 'mail.activity.mixin', 'rating.mixin', 'website.published.mixin']
    _description = 'OpenEduCat Academic Plan'

    # ── Fields ──────────────────────────────────────────────
    academic_session_count = fields.Integer(string='Academic Session count', store=False)
    academic_year_id = fields.Many2one('op.academic.year', string='Academic Year', required=True)
    active = fields.Boolean(string='Active')
    attendance_sheet_count = fields.Integer(string='Attendance Sheet', store=False)
    code = fields.Char(string='Code', required=True)
    color = fields.Integer(string='Color Index')
    company_id = fields.Many2one('res.company', string='Company')
    course_configure_count = fields.Integer(string='Course Configure Count', store=False)
    course_id = fields.Many2one('op.course', string='Course')
    course_plan_line = fields.One2many('op.course.plan', 'academic_plan_id', string='Configure Course')
    duration_tracking = fields.Json(string='Status time', store=False, help='JSON that maps ids from a many2one field to seconds spent')
    end_date = fields.Date(string='End Date', store=False)
    fees_plan_count = fields.Integer(string='Student Fees Plan count', store=False)
    final_approve_user_id = fields.Many2one('res.users', string='Final Approve User')
    first_approve_user_id = fields.Many2one('res.users', string='First Approve User')
    intake_year_ids = fields.Many2many('op.intake.year', string='Intake Year')
    is_rotting = fields.Boolean(string='Rotting', store=False)
    name = fields.Char(string='Name', store=False)
    program_id = fields.Many2one('op.program', string='Program', required=True)
    rotting_days = fields.Integer(string='Days Rotting', store=False, help='Day count since this resource was last updated')
    sequence = fields.Char(string='Sequence')
    stages_id = fields.Many2one('op.academic.plan.stages', string='Stage')
    start_date = fields.Date(string='Start Date', store=False)
    state = fields.Selection(string='State', selection=[])
    student_count = fields.Integer(string='Student Count', store=False)
    student_course_ids = fields.One2many('op.student.course', 'academic_plan_id', string='Students')
    subject_count = fields.Integer(string='Subject Count', store=False)
    topics_line = fields.One2many('op.topics', 'academic_plan_id', string='Topics Line')

    # Mixin-inherited fields (not redeclared): activity_calendar_event_id, activity_date_deadline, activity_exception_decoration, activity_exception_icon, activity_ids, activity_state, activity_summary, activity_type_icon, activity_type_id, activity_user_id ...

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read
    #   Role / Portal: read, write

    # Record Rules:
    #   Academic Plan multi-company: ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_academic_session_count(self):
        for rec in self:
            rec.academic_session_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_attendance_sheet_count(self):
        for rec in self:
            rec.attendance_sheet_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_course_configure_count(self):
        for rec in self:
            rec.course_configure_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_duration_tracking(self):
        for rec in self:
            rec.duration_tracking = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_end_date(self):
        for rec in self:
            rec.end_date = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_fees_plan_count(self):
        for rec in self:
            rec.fees_plan_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_is_rotting(self):
        for rec in self:
            rec.is_rotting = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_name(self):
        for rec in self:
            rec.name = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_rotting_days(self):
        for rec in self:
            rec.rotting_days = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_start_date(self):
        for rec in self:
            rec.start_date = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
