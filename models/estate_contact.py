from odoo import fields, models


class EsateContact(models.Model):
    _name = "estate.contact"
    _description = "to store customer contacts"
    _rec_name = "customer_name"
    customer_name = fields.Char(string="الأسم")
    job= fields.Char(string="الوظيفة")
    customer_address = fields.Text(string="العنوان")
    id_number = fields.Char(string='رقم البطاقة')
    cutomer_notes = fields.Text(string="ملاحظات")

    phone_ids = fields.One2many(comodel_name="customer.phones", inverse_name="customer_ids")
    files_ids = fields.One2many(comodel_name="personal.files", inverse_name="customer_files_ids")
    ownerhip_ids = fields.One2many(comodel_name='ownership', inverse_name="name_owner_ids")
    ownerhip_commerce_ids = fields.One2many(comodel_name='ownership.commerce', inverse_name="name_owner_commerce_ids")



class CustomerPhones(models.Model):
    _name = "customer.phones"
    _description = "to save phones"
    customer_phone = fields.Char(string="رقم التليفون")
    customer_ids = fields.Many2one(comodel_name= "estate.contact", ondelete='cascade')
    
    
class PersonalFiles(models.Model):
    _name = "personal.files"
    _description = "to add association files to the customer"
    files_name = fields.Char(string="اسم الملف")
    file_upload = fields.Binary(string=" الملف")
    customer_files_ids = fields.Many2one(comodel_name= "estate.contact", ondelete='cascade')
    
