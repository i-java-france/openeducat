from odoo import fields, models


class TestTask(models.Model):
    _name = "test.task"
    _description = "Test Task"

    name = fields.Char(required=True)
    description = fields.Text()
    is_done = fields.Boolean(default=False)
    active = fields.Boolean(default=True)
