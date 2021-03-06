{
    'name': 'Purchase Order Enhancement',
    'description' : 'Custom Purchase App',
    'author ' : 'Quan Bui',
    'depends' : ['purchase'],
    'application' : True,
    'data' : [
        'views/purchase_views.xml',
        'views/purchase_assets.xml',
        'views/res_config_settings_views.xml',
        'views/purchase_cron.xml',
        'views/purchase_order_template.xml',
        'wizard/purchase_archive_multiple_wizard_view.xml',
        'reports/purchase_order_templates.xml',
    ],
}
