from odoo import fields,models,api,_
from datetime import date



class Tailor(models.Model):

    _name = 'tailoring.tailor'
    _description = 'Tailor'
    _inherit = ['mail.thread','mail.activity.mixin']

    order_id = fields.Many2one('sale.order',string='Order Number', readonly=1, tracking=True)
    product = fields.Char()
    name = fields.Many2one("res.users",readonly=1,tracking=True)
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
            'state' : 'finished'
        })
        
        sale_order = self.env['sale.order'].search([])

        if self.state == 'finished' or sale_order:

            sale_order.write({
                'state' : 'ready to deliver'
            })

    
         

        

