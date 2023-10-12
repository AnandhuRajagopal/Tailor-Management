from odoo import fields,models,api,_
from datetime import date



class Tailor(models.Model):

    _name = 'tailoring.tailor'
    _description = 'Tailor'
    _inherit = ['mail.thread','mail.activity.mixin']

    order_id = fields.Many2one('sale.order',string='Order Number', readonly=1, tracking=True)
    product = fields.Char()
    name = fields.Many2one("res.users",readonly=1,tracking=True,string='Tailor')
    assigned_date = fields.Datetime(string="Assigned Date",related='order_id.date_order',readonly=1)
    started_date = fields.Datetime(string="Started Date",readonly=1)
    finished_date = fields.Datetime(string="Finished Date",readonly=1)
    state = fields.Selection([('pending','Pending'),('in_progress','In Progress'),
                              ('finished','Finished')],default="pending", tracking=True)


    # ...........................................Tailor Work Start Datetime..........................................
    def start(self):
        self.started_date = fields.Datetime.now()
        self.write({
            'state' : 'in_progress'
        })

    # ...........................................Tailor Work Finished Datetime..........................................
    def finish(self):
        self.finished_date = fields.Datetime.now()
        self.write({
            'state': 'finished'
        })
    # ........................................... send delivery mail..........................................

        if self.state == 'finished' or self.order_id.state == 'sale':
            self.order_id.state = 'ready to deliver'
            email_values = {
            'email_from': self.order_id.company_id.email,
            'email_to': self.order_id.partner_id.email,
            'subject': 'Product Delivery'
        }
        template = self.env.ref('pragtech_tailoring_management.mail_template_ready_to_delivery')
        template.send_mail(self.id, force_send=True, email_values=email_values)
        

    # ...........................................Specific Measrement Record Form View..........................................
    def current_measurement_record(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Measurement',
            'domain': [('order_id', '=', self.order_id.id)],
            'res_model': 'tailoring.customer.measurement',
            'view_mode': 'tree,form',
            'target': 'current',
        }
