from odoo import http, _
from odoo.http import request

class TailoringController(http.Controller):
    @http.route('/', type='http', auth="public", website=True)
    def tailor_page(self, **kw):
        return request.render('pragtech_tailoring_management.home_page_template')



