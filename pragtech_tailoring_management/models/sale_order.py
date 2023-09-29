from odoo import models,fields,api,_



class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    
    cloth_type_id = fields.Many2one('tailoring.cloth_type')
    


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def measurement(self):
        print("measurement")


    def assign_driver(self):
        print("assigning driver")  

    def assign_tailor(self):
        print("assigning tailor")    