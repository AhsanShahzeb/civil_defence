# -*- coding: utf-8 -*-
from odoo import api, fields, models

class CDSourceII(models.Model):
    _name = "cd.source.ii"
    _description = "Source II"
    _rec_name = 'name'

    employee_id = fields.Many2one('cd.employee', string='Employee', copy=False)
    name = fields.Char(related='employee_id.name', readonly=True)
    personal = fields.Char(related='employee_id.personal')
    grade = fields.Char(related='employee_id.bps')
    dsignation = fields.Char(related='employee_id.designation_id.designation')
    cnic = fields.Char(related='employee_id.cnic')
    remarks = fields.Text('Remarks')
    salaries_ids = fields.One2many('cd.source.salary', 'source_id', string='Select Salary Head')

    @api.onchange('remarks')
    def onchange_remarks_title(self):
        if self.remarks:
            self.remarks = str(self.remarks).title()


class CDSourceSalary(models.Model):
    _name = 'cd.source.salary'
    _description = 'Source Salary'

    salary_id = fields.Many2one('cd.salary.code', string='Salary')
    amount = fields.Integer('Amount')
    source_id = fields.Many2one('cd.source.ii', string='Source')
