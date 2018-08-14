from odoo import api, models, fields
from odoo.http import request
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from datetime import date, datetime


class WWInsuranceWizard(models.TransientModel):
    _name = "ww.insurance.wizard"

    start_date = fields.Date()
    overnight_rate_1 = fields.Float()
    
    def create(self, vals):
        if not vals:
            vals = {}

        insurance = self.env['ww.insurance'].create({})


        child_1 = False
        if vals['child_birth_1']:
            child_1 = self.env['ww.child'].create({
                'insurance_id': insurance.id,
                'overnight': vals['overnight_rate_1']
            })

        if child_1:
            insurance.write({
                'child_ids': [(4, child_1.id)]
            })

        vals.update({
            'ww_insurance_id': insurance.id,
            'partner_id': self.env.user.id
        })

        sale_order = self.env['sale.order'].create(vals)

        insurance.write({
            'sale_order_id': sale_order.id
        })
        request.session['insurance_id'] = insurance.id
        request.session['overnight_1'] = vals['overnight_rate_1']

        signature_template = self.env['signature.request.template'].browse(8)
        signature_template_copy = signature_template.copy()

        request.session['link'] = signature_template_copy.share(signature_template_copy.id)
        return super(WWInsuranceWizard, self).create(vals)
