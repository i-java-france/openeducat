# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class IrUiView(models.Model):
    _inherit = "ir.ui.view"

    customize_show = fields.Boolean("Show As Optional Inherit", default=False)
