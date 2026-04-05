# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpAcademicPlanStages(models.Model):
    """Academic plan Stages
    """

    _inherit = ['op.academic.plan.stages', 'mail.thread', 'rating.mixin', 'website.published.mixin']
    _description = 'Academic plan Stages'

    # ── Fields ──────────────────────────────────────────────
    company_id = fields.Many2one('res.company', string='Company')
    is_approve = fields.Boolean(string='Is Approve')
    is_done = fields.Boolean(string='Is Done')
    name = fields.Char(string='Stage Name', required=True)
    sequence = fields.Integer(string='Sequence')
    state = fields.Selection(string='State', selection=[])

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, has_message, id, message_attachment_count, message_follower_ids, message_has_error, message_has_error_counter, message_has_sms_error ...

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
