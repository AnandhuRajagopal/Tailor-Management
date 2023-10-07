from odoo import fields, models
from odoo.exceptions import MissingError

class StockPickup(models.Model):
    _inherit = 'stock.picking'

    driver_id = fields.Many2one('hr.employee', string="Driver")
    product_image = fields.Binary(string="Product Image")
    state = fields.Selection(selection_add=[('delivered','DELIVERED')])


    def button_validate(self):
        if any(move.quantity_done <= 0 for move in self.move_ids):
            raise MissingError("Done Quantities Cannot be Zero")

        super(StockPickup, self).button_validate()

        if self.state == 'done':
            sale_orders = self.env['sale.order'].search([('picking_ids', 'in', self.ids)])
            for sale_order in sale_orders:
                if sale_order.state != 'shipped':
                    sale_order.write({'state': 'shipped'})

    def delivered(self):
        if not self.product_image:
            raise MissingError("Add the Product Image")

        if self.state == 'done':
            sale_orders = self.env['sale.order'].search([('picking_ids', 'in', self.ids)])
            for sale_order in sale_orders:
                if sale_order.state != 'delivered':
                    sale_order.write({'state': 'delivered'})  
            self.write({
                'state' : 'delivered'
            })                  
