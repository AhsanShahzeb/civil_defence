# -*- coding: utf-8 -*-
from odoo import api, fields, models

class CDSourceII(models.Model):
    _name = "cd.source.ii"
    _description = "Source II"

    employee_id = fields.Many2one('cd.employee', string='Employee', copy=False)
    personal = fields.Char(related='employee_id.personal')
    grade = fields.Char(related='employee_id.bps')
    dsignation = fields.Char(related='employee_id.designation_id.designation')
    cnic = fields.Char(related='employee_id.cnic')
    salary_ids = fields.One2many('cd.salary.code', 'source_id', compute='_compute_salary_ids' ,string='Salary')


    @api.depends('employee_id')
    def _compute_salary_ids(self):
        for order in self:
            order.salary_ids = order.employee_id.salary_ids

    # @api.depends('salary_ids')
    # def _compute_salary_ids(self):
    #     for i in self.salary_ids:

    # @api.onchange('salary_ids')
    # def _onchange_salary_ids(self):
    #     for i in self.salary_ids:
    #         i
