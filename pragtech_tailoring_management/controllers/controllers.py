from odoo import http, _
from odoo.http import request
import json


class TailoringController(http.Controller):
    @http.route('/', type='http', auth="public", website=True)
    def tailor_page(self, **kw):
        return request.render('pragtech_tailoring_management.home_page_template')

    @http.route('/submit_measurement', auth='public', type='http', website=True)
    def submit_measurement(self, **post):
        # Get the order_id from the form data
        order_id = int(post.get('order_id', 0))

        # Get the list of measurement names as a comma-separated string
        measurement_names = post.get('measurement.name')
        measurement_values = [name.strip() for name in measurement_names.split(',')]

        # Iterate through the measurements and create records
        measurement_model = http.request.env['tailoring.customer.measurement']
        for name in measurement_values:
            measurement_value = post.get(f'measurement_value_{name}', '')
            if measurement_value:
                measurement_data = {
                    'order_id': order_id,
                    'name': name,
                    'measurement_value': float(measurement_value),
                }
                measurement_model.create(measurement_data)

        # Redirect back to the form or another page
        return http.request.redirect('/')
   
    

class FeedbackController(http.Controller):

    @http.route('/feedback/page/', type='http', auth="public", website=True)
    def feedback_page(self, **kw):
        return request.render('pragtech_tailoring_management.feedback_page_template')

    @http.route('/feedback/submit', type='http', auth="public", website=True)
    def submit_feedback(self, **post):
        Feedback = request.env['tailoring.feedback']
        Feedback.create({
            'name': post.get('name'),
            'email': post.get('email'),
            'feedback': post.get('feedback')
        })
        return request.render('pragtech_tailoring_management.feedback_page_template')
    
    
class TestimonialController(http.Controller):

    @http.route('/fetch_testimonials', type='http', auth="public", website=True, csrf=False)
    def fetch_testimonials(self, **kw):
        testimonials = request.env['tailoring.feedback'].search([])
        testimonial_data = []

        for testimonial in testimonials:
            testimonial_data.append({
                'name': testimonial.name,
                'feedback': testimonial.feedback
            })

        return json.dumps(testimonial_data)
    



