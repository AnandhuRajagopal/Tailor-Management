from odoo import fields,models



class StockPickup(models.Model):
    _inherit = 'stock.picking'


    driver_id = fields.Many2one('hr.employee',string="Driver")


