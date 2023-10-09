from odoo import models, fields

class MyEmployee(models.Model):
    _inherit = 'hr.employee'

    job_data = fields.Many2one('tailoring.job',string='Job Positions')
