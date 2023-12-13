# -*- coding: utf-8 -*-
from odoo import api, fields, models

class CDEmployee(models.Model):
    _name = 'cd.employee'
    _description = 'Employee Information'
    # _rec_name = 'personal_name'
    _order = 'name desc'

    personal = fields.Char('Personal #', required=True)
    name = fields.Char('Name', required=True)
    father_name = fields.Char('Father Name')
    cnic = fields.Char('CNIC #', required=True)
    date_of_birth = fields.Date('Date of Birth')
    joining_date = fields.Date('Joining Date')
    mobile1 = fields.Char('Mobile # 1')
    mobile2 = fields.Char('Mobile # 2')
    vendor = fields.Char('Vendor #')
    bank_name = fields.Char('Bank Name')
    account = fields.Char('Account #')
    branch_code = fields.Char('Branch Code')
    branch_address = fields.Char('Branch Address')
    email = fields.Char("Email Address")
    nationality = fields.Char("Nationality", default="Pakistani")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', default='male')
    status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('widow', 'Widow'),
        ('divorced', 'Divorced'),
    ], string='Marital Status')
    address = fields.Text('Address')
    image = fields.Image()
    designation_id = fields.Many2one('cd.position', string='Designation', required=True)
    bps = fields.Char('BPS', related='designation_id.bps')
    children = fields.Char('Number of Children')

    _sql_constraints = [
        ("personal_uni", "unique(personal)", "This Employee already exits"),
    ]

    # personal_name = fields.Char(compute='_compute_personal_name')

    # @api.depends('personal', 'name')
    # def _compute_personal_name(self):
    #     for per_name in self:
    #         per_name.personal_name = str(per_name.personal) + ' ' + str(per_name.name)

    @api.onchange('name')
    def name_in_caps(self):
        if self.name:
            self.name = str(self.name).title()

    @api.onchange('father_name')
    def father_name_in_caps(self):
        if self.father_name:
            self.father_name = str(self.father_name).title()
