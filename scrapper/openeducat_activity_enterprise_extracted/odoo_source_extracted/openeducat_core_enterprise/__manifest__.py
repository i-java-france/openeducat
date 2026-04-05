# -*- coding: utf-8 -*-
# AUTO-GENERATED — reconstructed from Odoo database metadata
{
    'name': 'OpenEduCat Core Enterprise',
    'version': '19.0.1.0',
    'summary': 'Based on best of class enterprise level architecture,
    OpenEduCat is ready to be used from local infrastructure
    to a highly scalable cloud environment.',
    'description': """
        Based on best of class enterprise level architecture,
    OpenEduCat is ready to be used from local infrastructure
    to a highly scalable cloud environment.
    """,
    'author': 'OpenEduCat Inc',
    'website': 'https://www.openeducat.org',
    'license': 'Other proprietary',
    'category': 'Education',
    'depends': [
        'calendar',
        'website',
        'gamification',
        'openeducat_core',
        'openeducat_web',
        'openeducat_onboarding',
        'onboarding',
        'base_user_role_company'
    ],
    'data': [
        # TODO: list XML files
        # 'security/ir.model.access.csv',
        # 'views/views_form.xml',
        # 'data/sequences.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
