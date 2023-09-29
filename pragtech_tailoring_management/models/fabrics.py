from odoo import fields,models,api


class TailoringFabric (models.Model):
    _name = "tailoring.fabric"
    _description = "tailoring.fabric"

    name = fields.Char('Name of Fabric')
