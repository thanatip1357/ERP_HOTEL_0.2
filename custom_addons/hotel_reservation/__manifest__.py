# __manifest__.py
{
    'name': 'Hotel Reservation',
    'version': '16.0.1.0.0',
    'summary': 'Manage hotel room reservations and related workflows',
    'category': 'Hotel Management',
    'author': 'Your Company Name',
    'website': 'https://yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        # If you plan to use accounting or other Odoo modules, add them here
        # 'account',
        # 'sale',
    ],
    'data': [
        # Views
        'views/hotel_room_views.xml',
        'views/hotel_reservation_views.xml',
        'views/menus.xml',
        
        'data/model_data.xml',
        # Security
        'security/security_rules.xml',
        'security/ir.model.access.csv',

         # Sequences
        'data/sequence.xml',

        

        # Demo data (optional)
        # 'data/demo_data.xml',
    ],
     'demo': [
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
