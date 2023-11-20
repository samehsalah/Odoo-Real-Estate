from odoo import models, fields

class Mall(models.Model):
    _name = 'mall'
    _description = 'malls'
    _rec_name = 'mall_name'
    
    mall_name = fields.Char(string='اسم المول') 
    store_ids = fields.One2many('store', 'mall_ids', string='الواحدات التجارية')