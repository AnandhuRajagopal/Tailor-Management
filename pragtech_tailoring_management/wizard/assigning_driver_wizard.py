from odoo import models, fields, api


class assigningDriverWizard(models.TransientModel):
    _name = 'driver.wizard'
    _description = 'driver_wizard'

    driver_id = fields.Many2one('hr.employee',string="Driver")
    order_id = fields.Many2one('sale.order', string="Order Number",default=lambda self: self.get_active_id())
    # location = fields.Char(string ="Location", related='order_id.')
    date = fields.Datetime(string="Date",related='order_id.date_order')
    state = fields.Selection(related="order_id.state")
    

    @api.model
    def get_active_id(self):
        active_id = self.env.context.get('active_id')
        if active_id:
            return self.env['sale.order'].browse(active_id)



    def driver_wizard_pickup_action(self):
        active_id = self.env.context.get("active_id")
        sale_order = self.env['sale.order'].browse(self._context.get('active_id'))
        re = self.env['tailoring.driver'].browse([active_id])
        if re or (sale_order and sale_order.state != 'pickup'):
            self.env['tailoring.driver'].create({
                'name':self.driver_id.id,
                'order_id':self.order_id.id,
                'product' : sale_order,
                'date':self.date,
                'type': 'Pickup',
            })

            sale_order.write({
                'state' : 'pickup'
            })

    def driver_wizard_delivery_action(self):
        active_id = self.env.context.get("active_id")
        sale_order = self.env['sale.order'].browse(self._context.get('active_id'))
        re = self.env['tailoring.driver'].browse([active_id])
        if re or (sale_order and sale_order.state != 'pickup'):
            self.env['tailoring.driver'].create({
                'name':self.driver_id.id,
                'order_id':self.order_id.id,
                'product' : sale_order,
                'date':self.date,
                'type': 'Delivery',
            })
            sale_order.write({
                'state' : 'delivery'
            })

            


      
       

    