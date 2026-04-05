# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpSubject(models.Model):
    """Subject Material Allocation
    """

    _inherit = ['op.subject', 'mail.thread', 'rating.mixin', 'website.published.mixin']
    _description = 'Subject Material Allocation'

    # ── Fields ──────────────────────────────────────────────
    active = fields.Boolean(string='Active')
    assignment_count = fields.Integer(string='Assignment Count', store=False)
    attachment_ids = fields.One2many('ir.attachment', 'res_id', string='Attachments')
    attempted_units = fields.Selection(string='Attempted Units', selection=[])
    code = fields.Char(string='Code', required=True)
    company_id = fields.Many2one('res.company', string='Company')
    course_id = fields.Many2one('op.course', string='Course')
    credit_point = fields.Float(string='Credit')
    default_template = fields.Boolean(string='Use Default Course Template')
    department_id = fields.Many2one('op.department', string='Department')
    grade_template_ids = fields.Many2many('op.grade.template', string='Grade Template', required=True)
    grade_weightage = fields.Float(string='Grade Weightage')
    name = fields.Char(string='Name', required=True)
    parent_sub_id = fields.Many2one('op.subject', string='Parent Subject')
    subject_credit = fields.Float(string='Credit Hours')
    subject_type = fields.Selection(string='Subject Type', required=True, selection=[])
    timetable_count = fields.Integer(string='Timetable Count', store=False)
    type = fields.Selection(string='Type', required=True, selection=[])

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, has_message, id, message_attachment_count, message_follower_ids, message_has_error, message_has_error_counter, message_has_sms_error ...

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read
    #   Library / Manager: read
    #   Role / Portal: read

    # Record Rules:
    #   Subject multi-company: ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]
    #   Subject multi-department: ['|','|',('department_id','=',False),('department_id','child_of',[user.dept_id.id]),('department_id','in',user.department_ids.ids)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_assignment_count(self):
        for rec in self:
            rec.assignment_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_timetable_count(self):
        for rec in self:
            rec.timetable_count = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
