# -*- coding: utf-8 -*-
# from odoo import http


# class PragtechTailoringManagement(http.Controller):
#     @http.route('/pragtech_tailoring_management/pragtech_tailoring_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pragtech_tailoring_management/pragtech_tailoring_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pragtech_tailoring_management.listing', {
#             'root': '/pragtech_tailoring_management/pragtech_tailoring_management',
#             'objects': http.request.env['pragtech_tailoring_management.pragtech_tailoring_management'].search([]),
#         })

#     @http.route('/pragtech_tailoring_management/pragtech_tailoring_management/objects/<model("pragtech_tailoring_management.pragtech_tailoring_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pragtech_tailoring_management.object', {
#             'object': obj
#         })
