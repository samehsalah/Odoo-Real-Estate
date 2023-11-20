# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{

    "name": "كمبوند العاصمة",

    "summary": "Real Eastate Management",

    "author": "Sameh Salah",

    "license": "AGPL-3",

    "website": "https://azharclub.com",

    "version": "16.0.1.0.0",

    "depends": ['base'],

    'data': [
        'reports/installment_report.xml',
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        'views/building_view.xml',
        'views/customer_phones_view.xml',
        'views/estate_contact_view.xml',
        'views/estate_menu.xml',
        'views/installment_view.xml',
        'views/mall_view.xml',
        'views/ownership_commerce_view.xml',
        'views/ownership_view.xml',
        'views/property_view.xml',
        'views/store_view.xml'
    ],

    "application": True,


}