from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Building(models.Model):
    _name = 'building'
    _description = 'building numbers'
    _rec_name = "buiding_name"
    
    buiding_name = fields.Char(string='اسم المبنى')  
    property_ids = fields.One2many('estate.property', 'building_id', string='Properties') 

    @api.constrains('buiding_name')
    def _check_buiding_name(self):
        # Search for any records that have the same building name as the current one
        existing_buildings = self.search([('buiding_name', '=', self.buiding_name), ('id', '!=', self.id)])
        # If any records are found, raise a validation error
        if existing_buildings:
            raise ValidationError('هذا المبنى موجود بالفعل')

    

