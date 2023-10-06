from odoo import fields,models,api


class Driver(models.Model):
    _name = "tailoring.driver"
    _description = "tailoring_driver"
    _rec_name = "name"


    name = fields.Many2one('res.users',string="Driver", readonly=1)
    location = fields.Char()
    order_id = fields.Many2one('sale.order',string='Order Number', readonly=1)
    product = fields.Char(string="Product")
    date = fields.Datetime(string="Date",related='order_id.date_order',readonly=1)
    state = fields.Selection([('pending','PENDING'),('in_progress','IN PROGRESS'),('material collected','MATERIAL COLLECTED')],default="pending")


    def start(self):
        self.write({
            'state' : 'in_progress'
        })

    def finish(self):
        self.write({
            'state' : 'material collected'
        })    

        sale_order = self.env['sale.order'].search([])

        if self.state == 'material collected' or sale_order:

            sale_order.write({
                'state' : 'material collected'
            })


      
   


