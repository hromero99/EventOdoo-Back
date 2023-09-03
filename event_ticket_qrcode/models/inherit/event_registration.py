from odoo import fields, api, models
import logging
import qrcode
import uuid
import io
import base64
_logger = logging.getLogger(__name__)


class EventRegistration(models.Model):
    _inherit = "event.registration"
    qr_img = fields.Binary(attachment=True)
    qr_code = fields.Char()
    qr_img64 = fields.Text()

    def compute_qrcode(self):
        """
            Compute unique qrcode for one event
            Assign qr_code field the value of the final code
        """
        self.qr_code = f"{self.event_id.id}{uuid.uuid4().hex}{self.id}"
        img = qrcode.make(self.qr_code)
        image_io_stream = io.BytesIO()
        img.save(image_io_stream, format="JPEG")
        bytes = image_io_stream.getvalue()
        self.qr_img = bytes
        self.qr_img64 = base64.b64encode(bytes)
        _logger.info(self.qr_code)
        _logger.info(self.qr_img)

    @api.model
    def create(self, vals):
        rec = super(EventRegistration, self).create(vals)
        rec.compute_qrcode()
        return rec
