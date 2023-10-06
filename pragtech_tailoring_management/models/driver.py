from odoo import fields,models,api


class Driver(models.Model):
    _name = "tailoring.driver"
    _description = "Driver"
    _rec_name = "name"
    _inherit = ['mail.thread','mail.activity.mixin']


    name = fields.Many2one('hr.employee',string="Driver", readonly=1 )
    location = fields.Char()
    order_id = fields.Many2one('sale.order',string='Order Number', readonly=1,tracking=True)
    product = fields.Char(string="Product")
    date = fields.Datetime(string="Date",related='order_id.date_order',readonly=1,tracking=True)
    state = fields.Selection([('pending','PENDING'),('in progress','IN PROGRESS'),('material collected','MATERIAL COLLECTED'),('delivered','DELIVERED')],default="pending",tracking=True)
    type = fields.Char(string="Type" ,readonly="1")


    def start(self):
        self.write({
            'state' : 'in progress'
        })

    def finish(self):
        if self.type == 'Pickup':
            self.write({
                'state' : 'material collected'
            })    
            sale_order = self.env['sale.order'].search([])

            if self.state == 'material collected' or sale_order:

                sale_order.write({
                    'state' : 'material collected'
                })
        elif self.type == 'Delivery':
            self.write({
                'state' : 'delivered'
            })    
            sale_order = self.env['sale.order'].search([])

            if self.state == 'material collected' or sale_order:

                sale_order.write({
                    'state' : 'finished'
                })



      
   


