from odoo import api, models, fields
from odoo.http import request


class WWSaleOrderExt(models.Model):
    _inherit = "sale.order"

    ww_insurance_id = fields.Many2one("ww.insurance")

    @api.model
    def create(self, vals):
        if not vals:
            vals = {}

        product = self.env['product.product'].search([('name', '=', 'Pflegetagegeldversicherung')])
        if not product:
            product = self.env['product.product'].create({
            'name': 'Pflegetagegeldversicherung',
            'categ_id': self.env.ref('product.product_category_all').id,
            'uom_id': self.env.ref('product.product_uom_unit').id,
            'uom_po_id': self.env.ref('product.product_uom_unit').id,
        })
        vals.update({'state': 'draft',
                     'order_line': [],
                     'payment_tx_ids': [],
                     'activity_ids': [],
                     'website_order_line': [],})
        rec = super(WWSaleOrderExt, self).create(vals)
        order_line = self.env['sale.order.line'].create({'order_id': rec.id,
                                                         'product_id': product.id,
                                                         'product_uom_qty': 1,
                                                         'price_unit': float(vals['overnight_rate_1']) * 30,
                                                         })
        vals.update({'order_line': [(0, 0, {'id': order_line.id,
                                            'order_id': self.id})]})

        request.session['sale_order_id'] = rec.id
        rec.write({'state': 'sent'})
        return rec
