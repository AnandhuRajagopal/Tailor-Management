from odoo import models, fields, api


class productInherit(models.Model):
    _inherit = 'product.template'
    _description = 'product.template'

    cloth_type = fields.Many2one('tailoring.cloth_type','Cloth type')
    categories = fields.Selection([('gents', 'Gents'),('ladies', 'Laies'),('kids', 'Kids')])
    description = fields.Text('Description')
    fabric = fields.Char(string="Fabric type",related='cloth_type.name')