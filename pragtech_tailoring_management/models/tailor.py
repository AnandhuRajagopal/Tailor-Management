from odoo import fields,models,api,_



class Tailor(models.Model):

    _name = 'tailoring.tailor'
    _description = 'Tailor'
    _inherit = ['mail.thread','mail.activity.mixin']



    order_id = fields.Many2one('sale.order',string='Order Number', readonly=1, tracking=True)
    product = fields.Char()
    name = fields.Char(string="Tailor", tracking=True)
    state = fields.Selection([('pending','PENDING'),('in progress','IN PROGRESS'),('finished','FINISHED')],default="pending", tracking=True)


    def start(self):
        self.write({
            'state' : 'in progress'
        })

    def finish(self):
        
        self.write({
            'state' : 'finished'
        }) 

        sale_order = self.env['sale.order'].search([])

        if self.state == 'finished' or sale_order:

            sale_order.write({
                'state' : 'ready to deliver'
            })
         

        
