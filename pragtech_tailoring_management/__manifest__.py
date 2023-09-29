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

    'depends': ['base','product','sale','website_sale','website'],


    # always loaded
    'data': [

        'security/ir.model.access.csv',
        'views/fabrics.xml',
        'views/view_cloth_type.xml',
        'views/sequence_measurment.xml',
        'views/view_measurement.xml',
        'views/fabrics.xml',
        'views/sale_order.xml',
        'views/tailor.xml',
        'views/product_page_inherit.xml',
        'views/view_customer_measurement.xml',
        'wizard/assigning_tailor_wizard.xml',
        'views/menu.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
