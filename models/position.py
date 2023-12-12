# -*- coding: utf-8 -*-
from odoo import fields, models, api

class CDPosition(models.Model):
    _name = 'cd.position'
    _description = 'Position Information'
    _rec_name = 'designation'
    _order = 'bps desc'

    designation = fields.Char("Designation", required=True)
    bps = fields.Char("BPS", required=True)
    active = fields.Boolean('Active', default=True)

    @api.onchange('designation')
    def caps_designation(self):
        if self.designation:
            self.designation = str(self.designation).title()
