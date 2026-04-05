# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OnboardingOnboarding(models.Model):
    """Onboarding
    """

    _name = 'onboarding.onboarding'
    _description = 'Onboarding'

    # ── Fields ──────────────────────────────────────────────
    current_onboarding_state = fields.Selection(string='Completion State', store=False, selection=[])
    current_progress_id = fields.Many2one('onboarding.progress', string='Onboarding Progress', store=False, help='Onboarding Progress for the current context (company).')
    is_onboarding_closed = fields.Boolean(string='Was panel closed?', store=False)
    is_per_company = fields.Boolean(string='Should be done per company?', store=False)
    name = fields.Char(string='Name of the onboarding')
    panel_close_action_name = fields.Char(string='Closing action', help='Name of the onboarding model action to execute when closing the panel.')
    progress_ids = fields.One2many('onboarding.progress', 'onboarding_id', string='Onboarding Progress Records', help='All Onboarding Progress Records (across companies).')
    route_name = fields.Char(string='One word name', required=True)
    sequence = fields.Integer(string='Sequence')
    step_ids = fields.Many2many('onboarding.onboarding.step', string='Onboarding steps')
    text_completed = fields.Char(string='Message at completion', help='Text shown on onboarding when completed')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   Role / Administrator: read, write, create, unlink
    #   Role / User: 
    #   Everyone:

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_current_onboarding_state(self):
        for rec in self:
            rec.current_onboarding_state = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_current_progress_id(self):
        for rec in self:
            rec.current_progress_id = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_is_onboarding_closed(self):
        for rec in self:
            rec.is_onboarding_closed = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_is_per_company(self):
        for rec in self:
            rec.is_per_company = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
