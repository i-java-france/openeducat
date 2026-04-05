# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OeOnboardingSteps(models.Model):
    """Onboarding Steps
    """

    _name = 'oe.onboarding.steps'
    _description = 'Onboarding Steps'

    # ── Fields ──────────────────────────────────────────────
    action_id = fields.Many2one('ir.actions.act_window', string='Action')
    doc_link = fields.Text(string='Doc Link')
    image = fields.Binary(string='Image')
    is_done = fields.Boolean(string='Done ?')
    is_start = fields.Boolean(string='Is Start')
    name = fields.Char(string='Sequence')
    plan_id = fields.Many2one('oe.onboarding.plan', string='Plan')
    step_name = fields.Char(string='Steps Name')
    youtube_link = fields.Text(string='Youtube Link')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    def open_action_view(self):
        """Called by the start button in kanban view."""
        # TODO: implement
        pass

    def step_done(self):
        """Called by the Mark as done button in kanban view."""
        # TODO: implement
        pass
