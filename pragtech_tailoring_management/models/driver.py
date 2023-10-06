from odoo import fields,models,api


class Driver(models.Model):
    _name = "tailoring.driver"
    _description = "Driver"
    _rec_name = "name"
    _inherit = ['mail.thread','mail.activity.mixin']


    name = fields.Many2one('res.users',string="Driver", readonly=1 )
    location = fields.Char()
    order_id = fields.Many2one('sale.order',string='Order Number', readonly=1,tracking=True)
    product = fields.Char(string="Product")
    date = fields.Datetime(string="Date",related='order_id.date_order',readonly=1,tracking=True)
    state = fields.Selection([('pending','PENDING'),('in_progress','IN PROGRESS'),('material_collected','Material Collected')],default="pending",tracking=True)


    def start(self):
        self.write({
            'state' : 'in_progress'
        })

    def finish(self):
        self.write({
            'state' : 'material_collected'
        })    

        sale_order = self.env['sale.order'].search([])

        if self.state == 'material_collected' or sale_order:

            sale_order.write({
                'state' : 'material_collected'
            })


      
   


