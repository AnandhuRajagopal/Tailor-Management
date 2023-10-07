from odoo import models, fields

class Feedback(models.Model):
    _name = 'tailoring.feedback'
    _description = 'Feedback'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    feedback = fields.Text(string='Feedback', required=True)
