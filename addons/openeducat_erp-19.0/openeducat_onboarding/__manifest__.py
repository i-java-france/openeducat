# -*- coding: utf-8 -*-
# AUTO-GENERATED — reconstructed from Odoo database metadata
{
    'name': 'OpenEduCat Onboarding',
    'version': '19.0.1.0',
    'summary': 'OpenEduCat Onboarding',
    'description': """
        OpenEduCat Onboarding
    """,
    'author': 'OpenEduCat Inc',
    'website': 'https://www.openeducat.org',
    'license': 'Other proprietary',
    'category': 'Tool',
    'depends': [
        'base',
        'openeducat_core'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/views_list.xml',
        'views/views_kanban.xml',
        'actions/act_window.xml',
        'menus/menus.xml',
    ],
    'demo': [
        'demo/openeducat_onboarding_demo.xml',
    ],
    
    'installable': True,
    'application': False,
    'auto_install': False,
}
