from odoo import http, _
from odoo.http import request
import json


class TailoringController(http.Controller):
    @http.route('/', type='http', auth="public", website=True)
    def tailor_page(self, **kw):
        return request.render('pragtech_tailoring_management.home_page_template')

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



     
    
        
    



