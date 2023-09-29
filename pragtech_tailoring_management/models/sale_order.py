from odoo import models,fields,api,_



class SaleOrder(models.Model):
    _inherit = 'sale.order.line'
    
    
    cloth_type_id = fields.Many2one('tailoring.cloth_type')

    


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _rec_name = 'partner_id'

    state = fields.Selection(selection_add=[('pickup', 'PICKUP'), ('material collected', 'MATERIAL COLLECTED'),('tailor assigned','TAILOR ASSIGNED'),('ready to deliver','READY TO DELIVER'),('finished','FINISHED')]) 




    def measurement(self):
        print("measurement")


    def assign_driver(self):
        self.filtered(lambda order: order.state != 'Pickup').write({'state': 'pickup'})


    
