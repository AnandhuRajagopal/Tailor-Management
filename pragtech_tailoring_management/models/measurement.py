from odoo import models, fields, api


class Measurments(models.Model):
    _name = "tailoring.measurement"
    _description = "tailoring.measurement"

    sequence_no = fields.Char(string="Sequence_no", readonly=True, default="New")
    name = fields.Char(string="Name", required=True)

    @api.model
    def create(self, vals):
        vals['sequence_no'] = self.env['ir.sequence'].next_by_code('measurment.seq') or ('New')
        res = super(Measurments, self).create(vals)
        return res


class MeasurementRelative(models.Model):
    _name = "tailoring.measurement_relative"
    _description = "tailoring_measurement_relative"
    _rec_name = 'measurement_id'

    cloth_id = fields.Many2one('tailoring.cloth_type')
    measurement_id = fields.Many2one('tailoring.measurement', string="Name")


