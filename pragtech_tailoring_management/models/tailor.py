from odoo import fields,models,api,_



class Tailor(models.Model):

    _name = 'tailoring.tailor'
    _description = 'tailoring_tailor'

   
    order_id = fields.Many2one('sale.order',string='Order Number', readonly=1)
    product = fields.Char()
    name = fields.Char(string="Tailor", readonly=1)
    state = fields.Selection([('pending','PENDING'),('in_progress','IN PROGRESS'),('finished','FINISHED')],default="pending")
    

    def start(self):
        self.write({
            'state' : 'in_progress'
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
         

        

