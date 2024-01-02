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
    
    office = fields.Many2one('cd.office')
    ddo = fields.Char(related='office.ddo', readonly=True)
    office_name = fields.Char(related='office.office_name', readonly=True)
    dao = fields.Char(related='office.dao', readonly=True)
    ddo_office = fields.Char(related='office.ddo_office', readonly=True)

    date = fields.Date('Date', default=fields.Date.context_today)

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
    total = fields.Integer(compute='compute_total_amount')

    @api.depends('amount')
    def compute_total_amount(self):
        for record in self:
            record.total = record.amount
    