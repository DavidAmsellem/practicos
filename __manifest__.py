{
    'name': 'Notas en Pedidos y Albaranes',
    'version': '1.0',
    'summary': 'Añade campos de notas en pedidos de venta y albaranes',
    'description': """
        Este módulo añade un campo de notas tanto en pedidos de venta como en albaranes.
        Las notas se copian automáticamente del pedido al albarán cuando se confirma el pedido.
        También añade estos campos en los informes de impresión.
        Además, restringe la edición de contactos de compañía a usuarios con permisos adecuados.
    """,
    'category': 'Sales/Sales',
    'author': 'David Amsellem',
    'depends': ['sale_stock', 'stock'],
    'data': [
        'security/security.xml',
        'security/ir_rule.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'views/report_saleorder.xml',
        'views/report_deliveryslip.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}