# -*- coding: utf-8 -*-

from odoo import models, fields


class BiodataModel(models.Model):
    _inherit = 'biodata.model'

    # Kita mau Inherit, nambahin Umur dan Gender ke Modul Biodata

    umur = fields.Integer(string="Umur")
    gender = fields.Selection([('cwo', 'Pria'), ('cwe', 'Wanita')], required=True, default='cwo', string='Gender')
