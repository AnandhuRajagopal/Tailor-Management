from odoo import models, fields, api



class CustomerMeasurments(models.Model):
    _name = "tailoring.customer.measurement"
    _description = "tailoring_customermeasurement"

    order_id = fields.Many2one( "sale.order", string= "Order Id")
    name = fields.Char(string="Name",required=True)
    measurement = fields.Float(string="Measurement",required=True)