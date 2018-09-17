from odoo import http
from odoo.http import request

import base64


class StaticServeHttp(http.Controller):

    @http.route('/agreements/<string:filename>', type='http', auth='public', website=True)
    def get_agreements(self, filename):
        attachment = request.env['ir.attachment'].search([('name', '=', filename)])
        if attachment:
            headers = [('Content-type', 'application/pdf')]
            data = base64.b64decode(attachment.datas)
            return request.make_response(data, headers)
        else:
            return request.render('website.layout')
