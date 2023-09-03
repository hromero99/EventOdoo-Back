# -*- coding: utf-8 -*-
from odoo import http
import logging
import json
_logger = logging.getLogger()


class ApiTickets(http.Controller):
    @http.route("/api/v1/event",  auth='api_key', type="json")
    def get_event_for_user(self, *args, **kwargs):
        headers = http.request.httprequest.environ
        _logger.info(headers)
        data = []
        events = http.request.env["event.event"].search([])
        for event in events:
            data.append({
                "id": event.id,
                "name": event.name
            })
        _logger.info(data)
        return data

    @http.route("/api/v1/event/<int:event_id>/validate",  auth='api_key', type="json", method=["POST"])
    def check_ticket_code_is_valid(self, *args, **kwargs):
        data = kwargs
        if "ticketcode" not in data.keys():
            return "Invalid request"
        stringinput = data["ticketcode"]
        events = http.request.env["event.registration"].search(
            [("qr_code", "=", stringinput), ("state", "=", "draft")])
        if events:
            event = events[0]
            event.state = "open"
            return {"data": "true"}
        else:
            return {"data": "false"}
