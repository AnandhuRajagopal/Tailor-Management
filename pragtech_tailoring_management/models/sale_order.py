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


    def current_driver_record(self):
        # action = self.env['ir.actions.actions']._for_xml_id('pragtech_tailoring_management.tailor_driver_action')
        # action['domain'] = [('customer_name', '=', self.id)]
        # form_view = [(self.env.ref('pragtech_tailoring_management.tailor_driver_form').id, 'form')]
        # print('1111111111111111111111111111111111',form_view)
        # action['views'] = form_view
        # action['res_id'] = self.id
        # print('1111111111111111111111111111', action)

        # return action

        return{
                'type': 'ir.actions.act_window',
                'name': 'Driver',
                'res_model': 'tailoring.driver',
                'domain' : [('customer_name', '=', self.id)],
                'view_mode' : 'kanban,tree,form',
                'target': 'current',
        }


# not complete
    def current_tailor_record(self):
        print('***************')
    
