from odoo import models, fields,api,_

class Measurement(models.Model):
    _name = 'tailoring.measurement'
    _description = 'Tailoring Measurement'

    sequence_no = fields.Char(string="Sequence No.", readonly=True, default="New")
    name = fields.Char(string="Name", required=True)
    value = fields.Float(string="Measurement Value")
    product_id = fields.Many2one('product.template', string="Product")


    # ...........................................Measurement Sequence..........................................
    @api.model
    def create(self, vals):
        vals['sequence_no'] = self.env['ir.sequence'].next_by_code('measurment.seq') or ('New')
        res = super(Measurement, self).create(vals)
        return res


class MeasurementRelative(models.Model):
    _name = "tailoring.measurement_relative"
    _description = "tailoring_measurement_relative"
    _rec_name = 'measurement_id'

    cloth_id = fields.Many2one('tailoring.cloth_type')
    measurement_id = fields.Many2one('tailoring.measurement', string="Name")


    def _default_cloth_id(self):
        product = self.env['product.product'].browse(self.env.context.get('product_id'))
        if product:
            cloth_type = product.cloth_type
            return cloth_type
        
    # ...........................................Compute Measurement Name..........................................
    @api.depends('measurement_id')
    def _compute_measurement_name(self):
        for record in self:
            record.measurement_name = record.measurement_id.name
