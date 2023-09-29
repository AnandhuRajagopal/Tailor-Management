from odoo import models, fields, api

class assigningTailorWizard(models.TransientModel):
    _name = 'tailoring.wizard'
    _description = 'tailoring_wizard'

    tailor_id = fields.Many2one('res.users', string='Select Tailor')

    def assign(self):
        sale_order = self.env['sale.order'].browse(self._context.get('active_id'))
        tailor = self.env['tailoring.tailor'].search([])

        if tailor or (sale_order and sale_order.state != 'tailor assigned'):

            sale_order.write({
                'state': 'tailor assigned',
            })

            tailor.create({
                'product' : sale_order.name,
                'name': self.tailor_id.name,
            })

        return {'type': 'ir.actions.act_window_close'}
