# -*- coding: utf-8 -*-
from odoo import fields, models, api

class CDOffice(models.Model):
    _name = 'cd.office'
    _description = 'Office Information'
    _rec_name = 'office_name'
    _order = 'ddo desc'

    ddo = fields.Char("DDO Code", required=True)
    office_name = fields.Char("Office Name", required=True)
    active = fields.Boolean('Active', default=True)

    _sql_constraints = [
        ("ddo_uni", "UNIQUE (ddo)", "This DDO is already exists"),
        ("office_name_uni", "UNIQUE (office_name)", "This Office is already exists"),
    ]

    @api.onchange('ddo')
    def caps_ddo(self):
        if self.ddo:
            self.ddo = str(self.ddo).upper()

    @api.onchange('office_name')
    def caps_office_name(self):
        if self.office_name:
            self.office_name = str(self.office_name).title()
