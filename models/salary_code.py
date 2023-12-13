# -*- coding: utf-8 -*-
from odoo import api, fields, models

class CDSalaryCode(models.Model):
    _name = "cd.salary.code"

    code = fields.Char("Salary Code", required=True)
    description = fields.Char("Salary Description", required=True)