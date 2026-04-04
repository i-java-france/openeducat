# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import fields, models


class OpActivityType(models.Model):
    """Activity Type"""

    _name = "op.activity.type"
    _description = "Activity Type"

    # ── Fields ──────────────────────────────────────────────
    active = fields.Boolean(string="Active")
    company_id = fields.Many2one("res.company", string="Company")
    name = fields.Char(string="Name", required=True)

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   Openeducat Activity Privilege / Manager: read, write, create, unlink
    #   Openeducat Activity Privilege / User: read

    # Record Rules:
    #   Activity Type multi-company: ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
