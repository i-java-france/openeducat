# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpSubjectRegistration(models.Model):
    """Subject Registration Details
    """

    _inherit = ['op.subject.registration', 'mail.thread', 'rating.mixin', 'website.published.mixin']
    _description = 'Subject Registration Details'

    # ── Fields ──────────────────────────────────────────────
    academic_plan_id = fields.Many2one('op.academic.plan', string='Academic Plan')
    batch_id = fields.Many2one('op.batch', string='Batch')
    cl_subject_ids = fields.Many2many('op.subject', string='Cl Subject')
    company_id = fields.Many2one('res.company', string='Company')
    compulsory_subject_ids = fields.Many2many('op.subject', string='Compulsory Subjects')
    course_id = fields.Many2one('op.course', string='Course', required=True)
    el_subject_ids = fields.Many2many('op.subject', string='El Subject')
    elective_subject_ids = fields.Many2many('op.subject', string='Elective Subjects')
    is_elective_select = fields.Boolean(string='Is Elective subject submitted?')
    is_read = fields.Boolean(string='Read?')
    max_unit_load = fields.Float(string='Maximum Unit Load')
    min_unit_load = fields.Float(string='Minimum Unit Load')
    name = fields.Char(string='Name')
    required_field = fields.Boolean(string='Required Field')
    state = fields.Selection(string='Status', selection=[])
    student_id = fields.Many2one('op.student', string='Student')
    user_id = fields.Many2one('res.users', string='User')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, has_message, id, message_attachment_count, message_follower_ids, message_has_error, message_has_error_counter, message_has_sms_error ...

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read, write, create

    # Record Rules:
    #   Student Subject Registration Rule: ['|', ('student_id.user_id','=',user.id), ('student_id.user_id','in',
                user.child_ids.ids)]
    #   View Students Registration: [(1,'=',1)]
    #   Subject Registration Multi Company: ['|','|',('company_id','=',False),('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids),('company_id',
                'in', company_ids)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
