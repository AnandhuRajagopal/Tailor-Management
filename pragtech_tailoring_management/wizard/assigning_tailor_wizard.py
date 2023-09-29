from odoo import models, fields, api


class assigningTailorWizard(models.TransientModel):
    _name = 'tailoring.assign.tailors'
    _description = 'tailoring_assign_tailors'


    tailor_id = fields.Char(string='Select Tailor')
    products_ids = fields.Char(string='Product Name')