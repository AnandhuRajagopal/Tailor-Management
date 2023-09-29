from odoo import fields,models,api


class Driver(models.Model):
    _name = "tailoring.driver"
    _description = "tailoring_driver"
    _rec_name = "name"


    name = fields.Char(string="Name")
    location = fields.Char()
    customer_name = fields.Char()
    product = fields.Char(string="Product")
    date = fields.Date()
    state = fields.Selection([('pending','PENDING'),('in progress','IN PROGRESS'),('material collected','MATERIAL COLLECTED')],default="pending")


    def start(self):
        self.write({
            'state' : 'in progress'
        })

    def finish(self):
        self.write({
            'state' : 'material collected'
        })    

        sale_order = self.env['sale.order'].search([('name', '=', self.product)])

        if self.state == 'material collected' or sale_order:

            sale_order.write({
                'state' : 'material collected'
            })




