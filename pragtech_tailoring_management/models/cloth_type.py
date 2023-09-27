from odoo import models, fields, api


class clothtype(models.Model):
    _name = 'tailoring.cloth'
    _description = 'tailoring_cloth'

    name = fields.Char()
    # fabric = fields.Many2one()
    # measurement = fields.One2many()
