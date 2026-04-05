# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpSpecialization(models.Model):
    """OpenEduCat Specializations
    """

    _inherit = ['op.specialization', 'mail.thread', 'rating.mixin', 'website.published.mixin']
    _description = 'OpenEduCat Specializations'

    # ── Fields ──────────────────────────────────────────────
    active = fields.Boolean(string='Active')
    area_id = fields.Many2one('op.area', string='Area', required=True)
    code = fields.Char(string='Code', required=True)
    company_id = fields.Many2one('res.company', string='Company')
    name = fields.Char(string='Name', required=True)

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, has_message, id, message_attachment_count, message_follower_ids, message_has_error, message_has_error_counter, message_has_sms_error ...

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read

    # Record Rules:
    #   Specialization multi-company: ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
