from odoo import fields,models,api,_



class Tailor(models.Model):

    _name = 'tailoring.tailor'

    product = fields.Char(string="Product")
    name = fields.Char(string="Tailor")
    state = fields.Selection([('pending','PENDING'),('in progress','IN PROGRESS'),('finished','FINISHED')],default="pending")


    def start(self):
        self.write({
            'state' : 'in progress'
        })

    def finish(self):
        self.write({
            'state' : 'finished'
        })    

        sale_order = self.env['sale.order'].search([('name', '=', self.product)])

        if self.state == 'finished' or sale_order:

            sale_order.write({
                'state' : 'ready to deliver'
            })

        
