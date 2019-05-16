{
    'name': 'Library Management',
    'description': 'Manage library book catalogue and lending.',
    'author': 'Quan Bui',
    'depends': ['base'],
    'application': True ,
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/book_list_template.xml',
    ],
}