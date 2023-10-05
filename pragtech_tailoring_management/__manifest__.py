# -*- coding: utf-8 -*-
{
    'name': "pragtech_tailoring_management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','sale','hr','mail','contacts','website','website_sale'],


    # always loaded
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/assigning_driver_wizard.xml',
        'wizard/assigning_tailor_wizard.xml',
        'wizard/assigning_measurement_wizard.xml',
        'views/view_fabrics.xml',
        'views/view_cloth_type.xml',
        'views/view_driver.xml',
        'views/view_measurement.xml',
        'views/view_tailor.xml',
        'views/view_customer_measurement.xml',
        'views/template_delivery_email.xml',
        'data/job_positions.xml',
        'views/inherit_sale_order.xml',
        'views/inherit_product_page.xml',
        'views/inherit_employee.xml',
        'views/menu.xml',



    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
