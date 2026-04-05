# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class PublisherWarrantyContract(models.Model):
    """Publisher Warranty Contract

    The base model, which is implicitly inherited by all models.
    """

    _name = 'publisher_warranty.contract'
    _description = 'Publisher Warranty Contract'


    # Mixin-inherited fields (not redeclared): display_name, id

    # Access Rights:
    #   Role / Administrator: read, write, create, unlink

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
