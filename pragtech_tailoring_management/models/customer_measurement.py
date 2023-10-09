from odoo import models, fields, api



class CustomerMeasurments(models.Model):
    _name = "tailoring.customer.measurement"
    _description = "tailoring_customermeasurement"

    order_id = fields.Char(string="Order_id")
    name = fields.Char(string="Name")
    measurement = fields.Float(string="Measurement")