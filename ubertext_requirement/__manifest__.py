# -*- coding: utf-8 -*-
{
    'name': "ubertext_requirement",

    'summary': """
        Reports and views Requirements for ubertext """,

    'description': """
        This module implements new features for reports and views, 
        1-add signatures to invoices
        2-Modify invoice format to add brand at invoice description 
        3-Input Reports, Output Reports, Stock Reports 
        4-Modify inventory adjustment view to add barcode, add to report of inventory adjustment
        theoretical inventory quantities, and diferences between cost of adquisition with real inventory
        quantities
    """,

    'author': "Fausto Jesús De La Cruz Caminero",
    'website': "http://www.ubertex.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'account',
                'stock',
                'point_of_sale',
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/ajustesfactura.xml',
        'views/ajuste_inventario.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}