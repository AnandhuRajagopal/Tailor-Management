from odoo import fields,models,api


class Driver(models.Model):
    _name = "tailoring.driver"
    _description = "tailoring_driver"
    _rec_name = "name"


    name = fields.Char(string="Name")
    location = fields.Char()
    customer_name = fields.Char()
    date = fields.Date()



