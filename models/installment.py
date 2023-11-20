# -*- coding: utf-8 -*-
from odoo import fields, models, api
from num2words import num2words


class Installment(models.Model):
    _name = 'installment'
    _description = 'to manage installments'

    name = fields.Char(string='الغرض')
    amount = fields.Float(string='المبلغ')
    due_date = fields.Date(string='تاريخ الأستحقاق')
    paid_date = fields.Date(string='تاريخ الدفع')
    bank_date = fields.Date(string='تاريخ - البنك')
    installment_copy = fields.Binary(string='رفع الايصال')
    amount_in_words_arabic = fields.Text(string='المبلغ بالاحرف', compute='_compute_amount_in_words_arabic')
    property_id = fields.Many2one(comodel_name ='estate.property', string='الوحدة', ondelete='cascade')
    store_id_installment = fields.Many2one(comodel_name ='store', string='تجارى-الوحدة', ondelete='cascade')

    owner_names = fields.Char(compute='_compute_owner_names', string='أسماء المالكين')

    unit_number = fields.Char(compute='_compute_unit_number', string='رقم الوحدة')
    building_number = fields.Char(compute='_compute_building_number', string='المبنى')
    notes = fields.Text(string="ملاحظات")

    @api.depends('property_id', 'store_id_installment')
    def _compute_unit_number(self):
        for record in self:
            if record.property_id:
                record.unit_number = record.property_id.unit_number
            elif record.store_id_installment:
                record.unit_number = record.store_id_installment.unit_number

    @api.depends('property_id', 'store_id_installment')
    def _compute_building_number(self):
        for record in self:
            if record.property_id:
                record.building_number = record.property_id.building_id.buiding_name
            elif record.store_id_installment:
                record.building_number = record.store_id_installment.mall_ids.mall_name





    @api.depends('property_id', 'store_id_installment')
    def _compute_owner_names(self):
        for record in self:
            owners = []
            if record.property_id:
                owners.extend(record.property_id.ownerhip_ids.filtered(lambda x: x.is_current).name_owner_ids.mapped('customer_name'))
            elif record.store_id_installment :
                owners.extend(record.store_id_installment.ownerhip_ids.filtered(lambda x: x.is_current).name_owner_commerce_ids.mapped('customer_name'))
            record.owner_names = ' و '.join(owners)





    def _compute_amount_in_words_arabic(self):
        for record in self:
            number = int(record.amount)
            amount_words = num2words(number, lang='ar')
            record.amount_in_words_arabic = amount_words





