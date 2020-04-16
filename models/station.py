# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Station(models.Model):
    _name = 'iti.session1.station'

    name = fields.Char()
    calls = fields.One2many(comodel_name='iti.session1.calls', inverse_name='station')

