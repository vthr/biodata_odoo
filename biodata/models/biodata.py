# -*- coding: utf-8 -*-

from odoo import models, fields


class BiodataModel(models.Model):
    _name = 'biodata.model'

    name = fields.Char(string="Nama")
    alamat = fields.Char(string="Alamat")
