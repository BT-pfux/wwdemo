from odoo import api, models, fields


class WWInsurance(models.Model):
    _name = "ww.insurance"

    sale_order_id = fields.Many2one("sale.order")
    ww_childs_ids = fields.One2many("ww.child", "insurance_id")
    start_date = fields.Date()
