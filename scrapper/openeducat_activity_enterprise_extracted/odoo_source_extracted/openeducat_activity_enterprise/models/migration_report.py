# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import fields, models


class MigrationReport(models.Model):
    """Migration Report"""

    _name = "migration.report"
    _description = "Migration Report"

    # ── Fields ──────────────────────────────────────────────
    date = fields.Date(string="Date")
    faculty_id = fields.Many2one("op.faculty", string="Faculty")
    student_id = fields.Many2one("op.student", string="Student")

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   Role / User: read

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
