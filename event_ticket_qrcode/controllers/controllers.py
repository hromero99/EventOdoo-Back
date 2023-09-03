# -*- coding: utf-8 -*-
# from odoo import http


# class EventTicketQrcode(http.Controller):
#     @http.route('/event_ticket_qrcode/event_ticket_qrcode', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_ticket_qrcode/event_ticket_qrcode/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_ticket_qrcode.listing', {
#             'root': '/event_ticket_qrcode/event_ticket_qrcode',
#             'objects': http.request.env['event_ticket_qrcode.event_ticket_qrcode'].search([]),
#         })

#     @http.route('/event_ticket_qrcode/event_ticket_qrcode/objects/<model("event_ticket_qrcode.event_ticket_qrcode"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_ticket_qrcode.object', {
#             'object': obj
#         })
