# -*- coding: utf-8 -*-
from odoo import api, fields, models

class CDSalaryCode(models.Model):
    _name = "cd.salary.code"
    _description = "Salary Code"
    _rec_name = 'code_description'

    code = fields.Char("Salary Code", required=True)
    description = fields.Char("Salary Description", required=True)
    active = fields.Boolean("active", default=True)
    code_description = fields.Char(compute='_compute_code_description', store=True)

    @api.depends('code', 'description')
    def _compute_code_description(self):
        for combine in self:
            combine.code_description = f"{combine.code} - {combine.description}"
    
    @api.onchange('description')
    def _onchange_description(self):
        if self.description:
            self.description = str(self.description).title()