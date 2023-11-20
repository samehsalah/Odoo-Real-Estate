from odoo import models, fields, api

class ownership(models.Model):
    _name = "ownership.commerce"
    _description = "to track ownership for property and store"

    start_date = fields.Date(string="بداية الملكية")
    end_date = fields.Date( string='نهاية الملكية')
    is_current = fields.Boolean(string="المالك الحالى")

    name_owner_commerce_ids = fields.Many2one(comodel_name='estate.contact', string="اسم المالك")
    store_unit_ids = fields.Many2one(comodel_name='store', string="الوحدة التجارية", ondelete='cascade')
    ownership_mall = fields.Many2one(comodel_name='mall', string="المبنى التجارى",ondelete='cascade')

    ownership_files = fields.Binary(string='الملف')


    @api.depends('store_unit_ids')
    def _compute_ownership_mall(self):
        for record in self:
            record.ownership_mall = record.store_unit_ids.mall_name










