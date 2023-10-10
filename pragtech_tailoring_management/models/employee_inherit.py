from odoo import models, fields,api


class MyEmployee(models.Model):
    _inherit = 'hr.employee'

    jobdata = fields.Many2one('tailoring.job',string='Job Positions')
    password = fields.Char('Password')
    done = fields.Boolean('Done')


    def create_user_from_employee(self):
        for employee in self:
            user = self.env['res.users']
            if employee.job_title == 'Driver':
                driver_login_group = [
                    self.env.ref('sales_team.group_sale_salesman').id,
                    self.env.ref('base.group_user').id,
                    self.env.ref('pragtech_tailoring_management.group_driver').id,]
                user = user.create({
                    'name': employee.name,
                    'login': employee.work_email,
                    'email': employee.work_email,
                    'password': employee.password,
                    'groups_id': [(6,0,driver_login_group)],

                })
                user.partner_id.function = 'Driver'

                
            elif employee.job_title == 'Tailor':
                tailor_login_group = [
                    self.env.ref('sales_team.group_sale_salesman').id,
                    self.env.ref('base.group_user').id,
                    self.env.ref('pragtech_tailoring_management.group_tailor').id,]
                user = user.create({
                    'name': employee.name,
                    'login': employee.work_email,
                    'email': employee.work_email,
                    'password': employee.password,
                    'groups_id': [(6,0,tailor_login_group)]

                })
                user.partner_id.function = 'Tailor'
            elif employee.job_title == 'Admin':
                admin_login_group = [
                    self.env.ref('sales_team.group_sale_salesman').id,
                    self.env.ref('base.group_user').id,
                    self.env.ref('pragtech_tailoring_management.group_admin').id,]
                user = user.create({
                    'name': employee.name,
                    'login': employee.work_email,
                    'email': employee.work_email,
                    'password': employee.password,
                    'groups_id': [(6,0,admin_login_group)]
                })
                user.partner_id.function = 'Admin'
                
            employee.done = True
            return user

