from odoo import api, models


class WWUsersExt(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        if not vals:
            vals = {}

        portal = self.env.ref('base.group_portal')
        if vals['groups_id']:
            groups = vals['groups_id']
        else:
            groups = [(6,0,[])]

        groups[0][2].append(portal.id)

        vals.update({'groups_id': groups})

        return super(WWUsersExt, self).create(vals)

