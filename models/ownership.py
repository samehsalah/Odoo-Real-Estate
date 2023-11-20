from odoo import models, fields, api

class ownership(models.Model):
    _name = "ownership"
    _description = "to track ownership for property and store"

    start_date = fields.Date(string="بداية الملكية", required=True)
    end_date = fields.Date( string='نهاية الملكية')
    is_current = fields.Boolean(string="المالك الحالى", default=True)
    name_owner_ids = fields.Many2one(comodel_name='estate.contact', string="اسم المالك",ondelete='cascade', required=True)
    #sotre_unit_ids = fields.Many2one(comodel_name='store', string="الوحدة التجارية")
    property_unit_ids = fields.Many2one(comodel_name='estate.property', string="الوحدة السكنية", ondelete='cascade')

    ownership_building = fields.Many2one(comodel_name='building', string="رقم العمارة", required=True,ondelete='cascade')
    #ownership_mall = fields.Many2one(comodel_name='mall', string="المبنى التجارى")
    ownership_files = fields.Binary(string='الملف')
    
    
        











