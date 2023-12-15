# -*- coding: utf-8 -*-
from odoo import api, fields, models

class CDSourceII(models.Model):
    _name = "cd.source.ii"
    _description = "Source II"

    employee_id = fields.Many2one('cd.employee', string='Employee')
    personal = fields.Char(related='employee_id.personal')
    grade = fields.Char(related='employee_id.bps')
    dsignation = fields.Char(related='employee_id.designation_id.designation')
    cnic = fields.Char(related='employee_id.cnic')
    salary_ids = fields.One2many('cd.salary.code', 'source_id', string='Salary')

