# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpBoardAffiliation(models.Model):
    """Board Affiliation
    """

    _name = 'op.board.affiliation'
    _description = 'Board Affiliation'

    # ── Fields ──────────────────────────────────────────────
    code = fields.Char(string='Code')
    company_id = fields.Many2one('res.company', string='Company')
    name = fields.Char(string='Board Name')
    note = fields.Text(string='Description')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

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
