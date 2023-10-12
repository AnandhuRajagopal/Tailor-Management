from odoo import fields, models,api
from odoo.exceptions import MissingError

class StockPickup(models.Model):
    _inherit = 'stock.picking'

    driver_id = fields.Many2one('res.users', string="Driver")
    product_image = fields.Binary(string="Product Image")
    image_filename = fields.Char(string="Image Filename")
    state = fields.Selection(selection_add=[('delivered', 'DELIVERED')])
    is_delivery = fields.Boolean(default = False, compute = 'is_delivery_funct')
    photo_req = fields.Boolean(default = False, compute = 'photo_req_funct')

    # ...........................................Stock Validate Button..........................................
    def button_validate(self):
        if any(move.quantity_done <= 0 for move in self.move_ids):
            raise MissingError("Done Quantities Cannot be Zero")

        pic = super(StockPickup, self).button_validate()

        if self.state == 'done':
            sale_order = self.env['sale.order'].browse(self.sale_id.id)
            print("2222222222222222222222222222222222222222222222222222222",self.sale_id)
            email_values = {
                'email_from': sale_order.company_id.email,
                'email_to': sale_order.partner_id.email,
                'subject': 'Shipped'
            }
            template = self.env.ref('pragtech_tailoring_management.mail_template_ready_to_shipped')
            template.send_mail(sale_order.id, force_send=True, email_values=email_values)
            sale_orders = self.env['sale.order'].search([('picking_ids', 'in', self.ids)])
            for sale_order in sale_orders:
                if sale_order.state != 'shipped':
                    sale_order.write({'state': 'shipped'})
            print("1111111111111111111111111111111",sale_orders.state)
        return pic

    # ...........................................Product Deliverd Button..........................................
    def delivered(self):
        if not self.product_image and self.is_delivery:
            raise MissingError("Add the Product Image")

        if self.state == 'done':
            sale_orders = self.env['sale.order'].search([('picking_ids', 'in', self.ids)])
            for sale_order in sale_orders:
                if sale_order.state != 'delivered':
                    sale_order.state = 'delivered'
            print("222222222222222222222222222222222222222222222", sale_orders.state)
            self.state = 'delivered'


    @api.depends('is_delivery')
    def is_delivery_funct(self):
        if self.picking_type_id.code == 'outgoing':
            self.is_delivery = True
        elif self.picking_type_id.code == 'incoming':
            self.is_delivery = False
            
    @api.depends('state', 'picking_type_id', 'photo_req')
    def photo_req_funct(self):
        for record in self:
            if record.state in ('done', 'delivered') and record.picking_type_id.code == 'outgoing':
                record.photo_req = True
            else:
                record.photo_req = False





            