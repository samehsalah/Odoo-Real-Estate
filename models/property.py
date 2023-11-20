# -*- coding: utf-8 -*-
from odoo import fields, models, api


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Property"
    _rec_name = 'unit_number'
    unit_number = fields.Char("رقم الوحدة", required=True)
    #reservation_date = fields.Date(string="ناريخ الحجز")
    notes = fields.Text(string="ملاحظات")
    total_amount = fields.Float(string="التميز")
    total_area = fields.Float(string=" المساحة الكلية")
    building_id = fields.Many2one(comodel_name ='building', string='رقم العمارة',required=True, ondelete='cascade')
    installment_ids = fields.One2many(comodel_name='installment', inverse_name='property_id', string='الاقساط')
    ownerhip_ids = fields.One2many(comodel_name='ownership', inverse_name="property_unit_ids")
    garage_number = fields.Char("رقم الباكيه")
    is_development_garage = fields.Selection(
        [('yes', 'نعم'), ('no', 'لا')],
        string='باكيات المطور',
        default='no'
    )
    owner_names = fields.Char(compute='_compute_owner_names', string='أسماء المالكين')
    
    dedication_date = fields.Date(string='تاريخ التخصيص')


    def print_installment(self):
        # Generate the report and return the action
        # You can use the existing report function or create a new one
        report = self.env.ref('estate.installment_copy').report_action(self.installments_ids.ids)
        return report
    
        
    def _compute_owner_names(self):
        for record in self:
            owners = []
            owners.extend(record.ownerhip_ids.filtered(lambda x: x.is_current).name_owner_ids.mapped('customer_name'))
            record.owner_names = ' و '.join(owners)
    


 

