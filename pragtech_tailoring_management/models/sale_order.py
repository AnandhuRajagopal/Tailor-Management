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


    def action_print(self):
        print(".....")



    def action_send_mail(self):
        active_id = self.env.context.get('active_id')
        sale_order = self.env['sale.order'].browse(active_id)
        print("---------------active model--------------------", active_id)
        email_values = {
        'email_from': self.company_id.email,
        'email_to': self.partner_id.email,
        'subject': 'Assigned Product Details'
        }
        template = self.env.ref('pragtech_tailoring_management.mail_template_ready_to_delivery')
        template.send_mail(sale_order.id, force_send=True, email_values=email_values)




    
