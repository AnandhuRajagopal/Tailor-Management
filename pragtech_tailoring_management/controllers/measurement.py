from odoo import http, _
from odoo.http import request


class MeasurementController(http.Controller):

   @http.route('/store_measurements', type='http', auth="public", csrf=True, website=True, method=['POST'])
   def measurement(self, **kw):
        print(kw)
        product_id = int(kw.get('product_id'))
        cloth_type = int(kw.get('cloth_type'))

        measurement_data = []

        for field_name, value in kw.items():
            if field_name.startswith('measurement_'):
                measurement_name = field_name.replace('measurement_', '')
                measure_value = float(value)
                measurement_data.append((0, 0, {
                    'name': measurement_name,
                    'measures': measure_value,
                    'uom_id': request.env.ref('uom.product_uom_cm').id
                }))
        
        measurement_record = request.env['tailoring.customer.measurement'].sudo().create({
            'order_id': product_id,
            'cloth_type': cloth_type,
            'measurement_ids': measurement_data
        })
        measurement_record.write({'state': 'draft'})
        return request.redirect('/')  