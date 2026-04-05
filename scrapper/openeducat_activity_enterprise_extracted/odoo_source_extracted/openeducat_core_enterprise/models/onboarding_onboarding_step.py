# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OnboardingOnboardingStep(models.Model):
    """Onboarding Step
    """

    _name = 'onboarding.onboarding.step'
    _description = 'Onboarding Step'

    # ── Fields ──────────────────────────────────────────────
    button_text = fields.Char(string='Button text', required=True, help='Text on the panel\'s button to start this step')
    current_progress_step_id = fields.Many2one('onboarding.progress.step', string='Step Progress', store=False, help='Onboarding Progress Step for the current context (company).')
    current_step_state = fields.Selection(string='Completion State', store=False, selection=[])
    description = fields.Char(string='Description')
    done_icon = fields.Char(string='Font Awesome Icon when completed')
    done_text = fields.Char(string='Text to show when step is completed')
    is_per_company = fields.Boolean(string='Is per company')
    onboarding_ids = fields.Many2many('onboarding.onboarding', string='Onboardings')
    panel_step_open_action_name = fields.Char(string='Opening action', help='Name of the onboarding step model action to execute when opening the step, e.g. action_open_onboarding_1_step_1')
    progress_ids = fields.One2many('onboarding.progress.step', 'step_id', string='Onboarding Progress Step Records', help='All related Onboarding Progress Step Records (across companies)')
    sequence = fields.Integer(string='Sequence')
    step_image = fields.Binary(string='Step Image')
    step_image_alt = fields.Char(string='Alt Text for the Step Image', help='Show when impossible to load the image')
    step_image_filename = fields.Char(string='Step Image Filename')
    title = fields.Char(string='Title')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   Role / Administrator: read, write, create, unlink
    #   Role / User: 
    #   Everyone:

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_current_progress_step_id(self):
        for rec in self:
            rec.current_progress_step_id = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_current_step_state(self):
        for rec in self:
            rec.current_step_state = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
