# -*- coding: utf-8 -*-
from odoo import api, fields, models

class CDSalaryCode(models.Model):
    _name = "cd.salary.code"
    _description = "Salary Code"

    code = fields.Char("Salary Code", required=True)
    description = fields.Char("Salary Description", required=True)
    active = fields.Boolean("active", default=True)
    source_id = fields.Many2one('cd.source.ii', string='Source')