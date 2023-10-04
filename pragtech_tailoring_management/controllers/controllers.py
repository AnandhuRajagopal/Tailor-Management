# from odoo import http, _
# from odoo.http import request


# class CustomerMeasurementController(http.Controller):

#     @http.route('/measurement/page/', type='http', auth='user',website="True")
#     def measurement_page(self):
#         return request.render('pragtech_tailoring_management.measurement_details_template')



# class MeasurementController(http.Controller):

#     @http.route('/measurement/details/<int:measurement_id>', type='http', auth='user', website=True)
#     def display_measurement_details(self, measurement_id):
#         measurement = request.env['tailoring.customer.measurement'].browse(measurement_id)
#         return http.request.render('pragtech_tailoring_management.measurement_details_template', {
#             'measurement': measurement
#         })

