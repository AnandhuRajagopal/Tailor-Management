from odoo import models,fields,api,_



class SaleOrder(models.Model):
    _inherit = 'sale.order.line'
    
    
    cloth_type_id = fields.Many2one('tailoring.cloth_type')

class SaleOrder(models.Model):
    _inherit = "sale.order"

    state = fields.Selection(selection_add=[ ('pickup','PICKUP'),('material collected', 'MATERIAL COLLECTED'),('tailor assigned','TAILOR ASSIGNED'),('ready to deliver','READY TO DELIVER'),('finished','FINISHED')]) 


    def measurement(self):
        print("measurement")


    # def assign_driver(self):
    #     self.filtered(lambda order: order.state != 'Pickup').write({'state': 'pickup'})


    def action_print(self):
        print(".....")



    # def action_measurement(self):
    #     return{
    #     'name':'Measurement',
    #     'type':'ir.actions.act_window',
    #     'vieew_type':''


    def current_driver_record(self):
        driver_id = self.env['tailoring.driver'].search([('order_id','=',self.id)])
        return{
                'type': 'ir.actions.act_window',
                'name': 'Driver',
                'res_id': driver_id.id,
                'res_model': 'tailoring.driver',
                'view_mode' : 'form',
                'target': 'current',
                'view_id': self.env.ref('pragtech_tailoring_management.driver_form_view').id
        }

    def current_tailor_record(self):
        tailor_id = self.env['tailoring.tailor'].search([('order_id','=',self.id)])
        return{
                'type': 'ir.actions.act_window',
                'name': 'Tailor',
                'res_id': tailor_id.id,
                'res_model': 'tailoring.tailor',
                'view_mode' : 'form',
                'target': 'current',
                'view_id': self.env.ref('pragtech_tailoring_management.tailor_form_view').id
        }