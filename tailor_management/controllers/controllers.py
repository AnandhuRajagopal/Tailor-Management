# -*- coding: utf-8 -*-
# from odoo import http


# class TailorManagement(http.Controller):
#     @http.route('/tailor_management/tailor_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tailor_management/tailor_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tailor_management.listing', {
#             'root': '/tailor_management/tailor_management',
#             'objects': http.request.env['tailor_management.tailor_management'].search([]),
#         })

#     @http.route('/tailor_management/tailor_management/objects/<model("tailor_management.tailor_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tailor_management.object', {
#             'object': obj
#         })
