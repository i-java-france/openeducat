# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpBadgeStudent(models.Model):
    """Gamification Student badge
    """

    _name = 'op.badge.student'
    _description = 'Gamification Student badge'

    # ── Fields ──────────────────────────────────────────────
    badge_id = fields.Many2one('op.gamification.badge', string='Badge', required=True)
    badge_name = fields.Char(string='Badge Name', store=False)
    comment = fields.Text(string='Comment')
    sender_id = fields.Many2one('res.users', string='Sender', help='The user who has send the badge')
    student_id = fields.Many2one('op.student', string='Student', required=True)

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read, write, create

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_badge_name(self):
        for rec in self:
            rec.badge_name = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
