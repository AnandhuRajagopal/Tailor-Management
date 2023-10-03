from odoo import fields,models,api


class Driver(models.Model):
    _name = "tailoring.driver"
    _description = "tailoring_driver"
    _rec_name = "name"

    name = fields.Char(string="Name")
    location = fields.Char()
    customer_name = fields.Char()
    date = fields.Date()
    state = fields.Selection([
        ('pending','Pending'),
        ('measurment','Measurment Collected'),
    ])

    def measurment(self,vals):
        self.state = 'measurement'

        
      
   


