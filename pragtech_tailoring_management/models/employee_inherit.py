from odoo import models, fields,api
from odoo.exceptions import UserError
class MyEmployee(models.Model):
    _inherit = 'hr.employee'

    jobdata = fields.Many2one('tailoring.job',string='Job Positions')
    password = fields.Char('Password')

    def create_user_from_employee(self):
        for employee in self:
            user = self.env['res.users']
            if employee.job_title == 'Driver':
                driver_login_group = [
                    self.env.ref('base.group_user').id,
                    self.env.ref('pragtech_tailoring_management.group_driver').id,]
                user = user.create({
                    'name': employee.name,
                    'login': employee.work_email,
                    'email': employee.work_email,
                    'password': employee.password,
                    'groups_id': [(6,0,driver_login_group)],

                })
            elif employee.job_title == 'Tailor':
                tailor_login_group = [
                    self.env.ref('base.group_user').id,
                    self.env.ref('pragtech_tailoring_management.group_tailor').id,]
                user = user.create({
                    'name': employee.name,
                    'login': employee.work_email,
                    'email': employee.work_email,
                    'password': employee.password,
                    'groups_id': [(6,0,tailor_login_group)]

                })
            elif employee.job_title == 'Admin':
                tailor_login_group = [
                    self.env.ref('base.group_user').id,
                    self.env.ref('pragtech_tailoring_management.group_admin').id,]
                user = user.create({
                    'name': employee.name,
                    'login': employee.work_email,
                    'email': employee.work_email,
                    'password': employee.password,
                    'groups_id': [(6,0,tailor_login_group.id)]
                })
            return user

