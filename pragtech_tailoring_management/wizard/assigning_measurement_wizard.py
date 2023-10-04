from odoo import models, fields, api


class assigningMeasurementWizard(models.TransientModel):
    _name = 'measurement.wizard'
    _description = 'measurement.wizard'

    name = fields.Char('name')

    def measurement_assign_action(self):
        self.env['tailoring.measurement'].create({
            'name': self.name,
        })
        return {'type': 'ir.actions.act_window_close'}
