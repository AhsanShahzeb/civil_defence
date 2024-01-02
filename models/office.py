# -*- coding: utf-8 -*-
from odoo import fields, models, api

class CDOffice(models.Model):
    _name = 'cd.office'
    _description = 'Office Information'
    _rec_name = 'ddo_office'
    _order = 'ddo, office_name desc'

    ddo = fields.Char("DDO Code", required=True)
    office_name = fields.Char("Office Name", required=True)
    dao = fields.Char("Accounts Office", required=True)
    active = fields.Boolean('Active', default=True)
    ddo_office = fields.Char("Select Office", compute='_compute_ddo_office')

    _sql_constraints = [
        ("ddo_uni", "unique(ddo)", "This DDO is already exits"),
        ("office_name_uni", "unique(office_name)", "This Office is already exits"),
        ("dao_uni", "unique(dao)", "This Accounts Office is already exits"),
    ]

    @api.depends('ddo','office_name')
    def _compute_ddo_office(self):
        for rec in self:
            rec.ddo_office = f"{rec.ddo} - {rec.office_name}"


    @api.onchange('ddo')
    def caps_ddo(self):
        if self.ddo:
            self.ddo = str(self.ddo).upper()

    @api.onchange('office_name')
    def caps_office_name(self):
        if self.office_name:
            self.office_name = str(self.office_name).title()

    @api.onchange('dao')
    def caps_dao(self):
        if self.dao:
            self.dao = str(self.dao).title()