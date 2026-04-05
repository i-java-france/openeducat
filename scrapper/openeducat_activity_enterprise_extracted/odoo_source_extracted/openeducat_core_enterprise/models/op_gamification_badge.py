# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpGamificationBadge(models.Model):
    """Gamification Badge
    """

    _name = 'op.gamification.badge'
    _description = 'Gamification Badge'

    # ── Fields ──────────────────────────────────────────────
    active = fields.Boolean(string='Active')
    description = fields.Text(string='Description')
    image = fields.Binary(string='Image', help='This field holds the image         used for the badge, limited to 256x256')
    name = fields.Char(string='Badge', required=True)

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read, write, create

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
