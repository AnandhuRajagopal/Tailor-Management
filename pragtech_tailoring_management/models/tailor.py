from odoo import fields,models,api,_



class Tailor(models.Model):

    _name = 'tailoring.tailor'

    product = fields.Char(string="Product")
    name = fields.Char(string="Tailor")