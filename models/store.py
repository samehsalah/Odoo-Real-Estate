# -*- coding: utf-8 -*-
from odoo import fields, models, api


class store(models.Model):
    _name = "store"
    _description = "To save store information"
    _rec_name = 'unit_number'
    unit_number = fields.Char("رقم الوحدة", required=True)
    notes = fields.Text(string="ملاحظات")
    total_amount = fields.Float(string="القيمة البيعية")
    total_area = fields.Float(string=" المساحة الكلية")
    outside_area = fields.Float(string=" المساحة الخارجيه")
    activity = fields.Char(string="النشاط")
    installment_ids = fields.One2many(comodel_name='installment', inverse_name='store_id_installment', string='الاقساط')
    mall_ids = fields.Many2one('mall', string='تجارى', required=True, ondelete='cascade')
    #mall_name = fields.Char(string='اسم المول', compute='compute_mall_name', store=True, required=True)

    ownerhip_ids = fields.One2many(comodel_name='ownership.commerce', inverse_name="store_unit_ids")
    
    owner_names = fields.Char(compute='_compute_owner_names', string='أسماء المالكين')

    dedication_date = fields.Date(string='تاريخ التخصيص')

    @api.depends('mall_ids')
    def compute_mall_name(self):
        for store in self:
            store.mall_name = store.mall_ids.mall_name 

    



    def print_installment(self):
        # Generate the report and return the action
        # You can use the existing report function or create a new one
        report = self.env.ref('estate.installment_copy').report_action(self.installments_ids.ids)
        return report
    
    
    
    def _compute_owner_names(self):
        for record in self:
            owners = []
            owners.extend(record.ownerhip_ids.filtered(lambda x: x.is_current).name_owner_commerce_ids.mapped('customer_name'))
            record.owner_names = ' و '.join(owners)
    


 

