{
    "name": "Test Module",
    "version": "19.0.1.0.0",
    "license": "LGPL-3",
    "summary": "A simple test module for Odoo 19",
    "author": "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/oca-addons-repo-template",
    "category": "Uncategorized",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/test_model_views.xml",
        "views/test_task_views.xml",
    ],
    "installable": True,
    "application": True,
}
