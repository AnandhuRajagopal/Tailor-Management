from odoo import models, fields

class CustomerMeasurements(models.Model):
    _name = "tailoring.customer.measurement"
    _description = "Customer Measurements"

    order_id = fields.Many2one("sale.order", string="Order Id")
    name = fields.Char(string="Name", required=True)
    measurement_value = fields.Float(string="Measurement", required=True)
    measurement_type_id = fields.Many2one(
        "tailoring.cloth_type.measurement_ids",
        string="Measurement Type",
    )