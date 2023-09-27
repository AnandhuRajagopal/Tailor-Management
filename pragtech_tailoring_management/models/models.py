# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pragtech_tailoring_management(models.Model):
#     _name = 'pragtech_tailoring_management.pragtech_tailoring_management'
#     _description = 'pragtech_tailoring_management.pragtech_tailoring_management'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
