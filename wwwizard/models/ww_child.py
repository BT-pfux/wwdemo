from odoo import api, models, fields


class WWInsurance(models.Model):
    _name = "ww.child"

    insurance_id = fields.Many2one("ww.insurance")
    birthday = fields.Date()
    start_date = fields.Date()
