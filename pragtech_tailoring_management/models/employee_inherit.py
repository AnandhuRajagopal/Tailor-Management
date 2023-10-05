from odoo import models, fields

class MyEmployee(models.Model):
    _inherit = 'hr.employee'

    jobdata = fields.Many2one('tailoring.job',string='Job Positions')
