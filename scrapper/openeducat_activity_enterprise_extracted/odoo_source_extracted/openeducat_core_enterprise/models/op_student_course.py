# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpStudentCourse(models.Model):
    """Student Course Details
    """

    _inherit = ['op.student.course', 'mail.thread', 'rating.mixin', 'website.published.mixin']
    _description = 'Student Course Details'

    # ── Fields ──────────────────────────────────────────────
    academic_plan_id = fields.Many2one('op.academic.plan', string='Academic Plan')
    academic_term_id = fields.Many2one('op.academic.term', string='Terms')
    academic_years_id = fields.Many2one('op.academic.year', string='Academic Year')
    batch_id = fields.Many2one('op.batch', string='Batch')
    course_id = fields.Many2one('op.course', string='Course', required=True)
    expires_after = fields.Integer(string='Invoice Cycles', help='Expires after number of Invoices')
    faculty_advisor_id = fields.Many2one('op.faculty', string='Faculty Advisor')
    fees_plan_id = fields.Many2one('op.fees.plan', string='Fees Term Plan')
    fees_start_date = fields.Date(string='Fees Start Date')
    fees_term_id = fields.Many2one('op.fees.terms', string='Fees Term')
    generated_invoices = fields.Integer(string='Generated Invoices', help='Number of Invoices Generated')
    intake_year_id = fields.Many2one('op.intake.year', string='Intake Year')
    is_withdrawal = fields.Boolean(string='Withdrawal')
    next_invoice_date = fields.Date(string='Next Invoice Date')
    prev_invoice_date = fields.Date(string='Previous Invoice Date')
    product_id = fields.Many2one('product.product', string='Course Fees')
    program_id = fields.Many2one('op.program', string='Program', store=False)
    required_field = fields.Boolean(string='Required Field')
    roll_number = fields.Char(string='Roll Number')
    session_count = fields.Integer(string='Session Count', store=False)
    state = fields.Selection(string='Status', selection=[])
    student_id = fields.Many2one('op.student', string='Student')
    subject_ids = fields.Many2many('op.subject', string='Subjects')
    user_id = fields.Many2one('res.users', string='User')
    withdrawal_id = fields.Many2one('op.student.withdrawal', string='Withdrawal Details')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, has_message, id, message_attachment_count, message_follower_ids, message_has_error, message_has_error_counter, message_has_sms_error ...

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read, write, create
    #   Library / Manager: read
    #   Role / Portal: read

    # Record Rules:
    #   Student Course multi-company: ['|','|',('student_id.company_id','=',False),('student_id.company_id','child_of',[user.company_id.id]),('student_id.company_id','in',user.company_ids.ids),('student_id.company_id','in', company_ids)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_program_id(self):
        for rec in self:
            rec.program_id = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_session_count(self):
        for rec in self:
            rec.session_count = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
