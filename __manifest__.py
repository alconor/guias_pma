# -*- coding: utf-8 -*-
{
    'name': "guias_pma",

    'summary': """
        Adecuación de fincas para Panamá y módulos de compras y ventas para
        almnacenar dos datos de las guias de cañas de un ingenio de azúcar""",

    'description': """
        Herencia en los modelos y vistas de.
        - compras (compra de caña)
        - ventas (venta de servicio de gestion de fincas)
        Para ver la información que proviene de las 
    """,

    'author': "Alconsoft",
    'website': "http://www.alconsoft.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2020-12-21 - 14:00',

    # any module necessary for this one to work correctly
    'depends': ['base', 'fincas_pma'],

    # always loaded: Aqui se cargan los formularios de vista.
    # IMPORTANTE: SE QUITA EL CARACTER "#" PARA QUE SE PUEDA CARGAR ARCHIVO CON LA LISTA DE ACCESO DE SEGURIDAD
    'data': [
        ####### ESTO IMPEDIA QUE SE PUDIERA VER EL MENU ########################
        #'security/ir.model.access.csv',
        ###############################
        #'views/views_compras.xml',
        #'views/views_ventas.xml',
        #'views/templates.xml',
        ####### CARGA AUTOMATICA AL INSTALAR DE DATOS ESTATICOS ########################
        #'static/xls/guias_pma.fincas_pma.csv',
        ###############################
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # Aplicacion:  si aparace cierto (true) esta modulo sera una aplicacion que aprecera en el listado de aplicaciones de odoo.
    'application': True,
}
