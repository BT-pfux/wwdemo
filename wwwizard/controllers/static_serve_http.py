from odoo import http
from odoo.http import request

class StaticServeHttp(http.Controller):

    @http.route('/agreements/<string:filename>',type='http', auth='public', website=True)
    def get_agreements(self, filename):
        attachment = request.env['ir.attachment'].search([('name', '=', filename)])
        if attachment:
            return attachment.datas
        else:
            return request.render('website.layout')
