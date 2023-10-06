from odoo import models, fields, api


class assigningMeasurementWizard(models.TransientModel):
    _name = 'measurement.wizard'
    _description = 'measurement_wizard'

    cloth_category_id = fields.Many2one('tailoring.cloth_type')
    measurement_lines_ids = fields.One2many('measurement.wizard.line', 'wizard_id', string="Measurements")

    def default_get(self,vals):
        res = super(assigningMeasurementWizard, self).default_get(vals)
        list_measurement = []
        # measurement = self.env['tailoring.measurement_relative'].search([('cloth_id', '=', 'cloth_category_id')])
        from_cloth_table = self.env['tailoring.cloth_type'].browse(res.get('cloth_category_id'))
        for rec in from_cloth_table.measurement_ids:
            vals = {
                'measurement_id': rec.id
            }
            # measurement = self.env['measurement.wizard.line'].create(
            #     {
            #         'measurement_id': rec.id,
            #     })
            list_measurement.append((0,0,vals))
        # self.measurement_lines_ids = [(6, 0, lis)]
        res.update({'measurement_lines_ids':list_measurement})
        return res

    def measurement_assign_action(self):
        self.env['tailoring.measurement'].create({
            'name': self.cloth_category_id,
        })
        return {'type': 'ir.actions.act_window_close'}
