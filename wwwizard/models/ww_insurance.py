from odoo import api, models, fields


class WWInsurance(models.Model):
    _name = "ww.insurance"

    partner_id = fields.Many2one('res.partner', default=lambda s: s.env.user.partner_id.id)
    start_date = fields.Date()
    child_ids = fields.One2many('ww.child', 'insurance_id')
    sale_order_id = fields.Many2one('sale.order')



