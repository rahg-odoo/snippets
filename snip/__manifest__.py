# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'snip',
    'sequence': 50,
    'version': '1.1',
    'depends': ['website', 'helpdesk'],
    'data': [
        'views/snippets/ticket_data.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            '/snip/static/src/scss/ticket_data.scss',
            '/snip/static/src/xml/tickets_card.xml',
            '/snip/static/src/js/ticket_data.js'
        ]
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
