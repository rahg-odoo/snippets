from odoo import http
from odoo.http import request
import json


class TicketData(http.Controller):
    @http.route('/ticket-data-all', type='json', auth="public")
    def sold_total(self):
        ticket_obj = request.env['helpdesk.ticket'].sudo().search_read([
            ('kanban_state', 'in', ['normal', 'done', 'blocked']),
        ])
        return ticket_obj
