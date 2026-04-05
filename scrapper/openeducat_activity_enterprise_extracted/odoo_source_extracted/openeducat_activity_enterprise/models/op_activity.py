# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import fields, models


class OpActivity(models.Model):
    """Student Activity"""

    _inherit = [
        "op.activity",
        "mail.thread",
        "mail.activity.mixin",
        "rating.mixin",
        "website.published.mixin",
    ]
    _description = "Student Activity"

    # ── Fields ──────────────────────────────────────────────
    active = fields.Boolean(string="Active")
    company_id = fields.Many2one("res.company", string="Company")
    date = fields.Date(string="Date")
    description = fields.Text(string="Description")
    faculty_id = fields.Many2one("op.faculty", string="Faculty")
    progression_id = fields.Many2one("op.student.progression", string="Progression No")
    student_id = fields.Many2one("op.student", string="Student", required=True)
    type_id = fields.Many2one("op.activity.type", string="Activity Type")

    # Mixin-inherited fields (not redeclared): activity_calendar_event_id, activity_date_deadline, activity_exception_decoration, activity_exception_icon, activity_ids, activity_state, activity_summary, activity_type_icon, activity_type_id, activity_user_id ...

    # Access Rights:
    #   Openeducat Activity Privilege / Manager: read, write, create, unlink
    #   Openeducat Activity Privilege / User: read, write

    # Record Rules:
    #   Student Activity Logs: ['|', ('student_id.user_id','=',user.id), ('student_id.user_id','in',user.child_ids.ids)]
    #   Faculty Activity Logs: ['|', ('faculty_id.user_id','=',user.id), ('faculty_id.user_id','in',user.child_ids.ids)]
    #   Back Office Activity Logs: [(1,'=',1)]
    #   Activity multi-company: ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
