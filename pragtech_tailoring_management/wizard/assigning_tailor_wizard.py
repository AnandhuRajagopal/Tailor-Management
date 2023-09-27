from odoo import models, fields, api


class assigningTailorWizard(models.TransientModel):
    _name = 'tailoring.wizard'
    _description = 'tailoring_wizard'


    tailor_id = fields.Char(string='Select Tailor')
    products_ids = fields.Char(string='Product Name')