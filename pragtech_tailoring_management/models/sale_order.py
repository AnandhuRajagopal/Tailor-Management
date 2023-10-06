from odoo import models,fields,api,_


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    cloth_type_id = fields.Many2one(related='product_template_id.cloth_type', string="Cloth Type")

    def wizard_value_pass(self):
        # ctx = self.env.context.copy()
        # ctx.update({"cloth_category_id": self.cloth_type_id.id})

        print("111111111111111111111111112222222211111111111",self.product_template_id.cloth_type.measurement_ids.measurement_id)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Measurement',
            'res_model': 'measurement.wizard',
            'view_mode': 'form',
            'target': 'new',
            'view_id': self.env.ref('pragtech_tailoring_management.view_measurement_wizard_form').id,
            'context': {
                'default_cloth_category_id': self.cloth_type_id.id,

            },
        }



class SaleOrder(models.Model):
    _inherit = "sale.order"

    state = fields.Selection(selection_add=[ ('pickup','PICKUP'),('material collected', 'MATERIAL COLLECTED'),('tailor assigned','TAILOR ASSIGNED'),('ready to deliver','READY TO DELIVER'),('finished','FINISHED')])


    def measurement(self):
        print("measurement")


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


    # ...........................................Action send mail..........................................
    def action_send_mail(self):
        active_id = self.env.context.get('active_id')
        sale_order = self.env['sale.order'].browse(self.id)
        email_values = {
        'email_from': self.company_id.email,
        'email_to': self.partner_id.email,
        'subject': 'Assigned Product Details'
        }
        template = self.env.ref('pragtech_tailoring_management.mail_template_ready_to_delivery')
        template.send_mail(sale_order.id, force_send=True, email_values=email_values)
