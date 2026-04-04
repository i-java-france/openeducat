# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import fields, models


class ActivityProgressWizard(models.TransientModel):
    """Activity Progress Wizard

    Progression Activity
    """

    _inherit = ["activity.progress.wizard", "mail.activity.mixin"]
    _description = "Activity Progress Wizard"

    # ── Fields ──────────────────────────────────────────────
    student_id = fields.Many2one("op.student", string="Student Name")

    # Mixin-inherited fields (not redeclared): activity_ids, create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   Openeducat Activity Privilege / Manager: read, write, create, unlink
    #   Openeducat Activity Privilege / User: read, write, create

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
