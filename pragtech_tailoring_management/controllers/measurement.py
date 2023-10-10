from odoo import http, _,api
from odoo.http import request


class MeasurementController(http.Controller):

    @http.route('/store_measurements', type='http', auth="public", csrf=True, website=True, method=['POST'])
    def measurement(self, **kw):
        product_id = int(kw.get('product_id'))
        cloth_type = int(kw.get('cloth_type'))
        
        
        user = request.env.user

        sale_order = request.website.sale_get_order()
        print(",,,,,,,,,,,,,,,,,,,",sale_order.name)


        existing_measurement_record = request.env['tailoring.customer.measurement'].sudo().search([
            ('order_id', '=', sale_order.name),
            ('cloth_type', '=', cloth_type),
            ('state', '=', 'draft'),
            ('customer_id', '=', user.id),  
        ])

        measurement_data = []

        for field_name, value in kw.items():
            if field_name.startswith('measurement_'):
                measurement_name = field_name.replace('measurement_', '')
                measure_value = float(value)
                measurement_data.append((0, 0, {
                    'name': measurement_name,
                    'measures': measure_value,
                    'uom_id': request.env.ref('uom.product_uom_cm').id,
                }))

        if existing_measurement_record:
            existing_measurement_record.write({'measurement_ids': [(5, 0, 0)]})

            existing_measurement_record.write({'measurement_ids': measurement_data})
            
            existing_measurement_record.write({
                'state': 'draft'
            })
        else:
            request.env['tailoring.customer.measurement'].sudo().create({
                'order_id' : sale_order.id,
                'cloth_type': cloth_type,
                'measurement_ids': measurement_data,
                'customer_id': user.id,
                'state': 'draft',
            })


        return request.redirect(request.httprequest.referrer or '/')
    
