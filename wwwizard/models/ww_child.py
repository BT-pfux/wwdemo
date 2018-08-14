from odoo import api, models, fields


class WWChild(models.Model):
    _name = "ww.child"

    insurance_id = fields.Many2one("ww.insurance")
    birthday = fields.Date()
    overnight = fields.Float()