{
    'name': 'Real Estate App',
    'version': '0.1.0',
    'category': 'Tutorials/RealEstateApp',
    'summary': 'Kochev Hennadii Tutorialed Real Estate App',
    'description': '29 May 2024 created tutorialed Estate App',
    'author': 'Hennadii Kochev',
    'website': 'https://github.com/genndy007',
    'license': 'GPL-3',

    'depends': [
        'base',
    ],
    'data': [
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_menus.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
    'installable': True,
}
