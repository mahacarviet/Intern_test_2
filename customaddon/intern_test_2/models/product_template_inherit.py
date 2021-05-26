from odoo import fields, models, api
from datetime import *

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    date_to = fields.Date(string="Warranty From")
    date_from = fields.Date(string="Warranty To")
    product_warranty = fields.Char(compute="_compute_product_warranty", string="Product Warranty")
    check_product_warranty = fields.Boolean(compute="_compute_check_product_warranty")
    check_product_time = fields.Boolean(compute="_compute_check_product_time")

    # @api.depends('date_to')
    def _compute_check_product_time(self):
        for rec in self:
            if rec.check_product_warranty == True:
                if (rec.date_to == '') or (rec.date_from == ''):
                    rec.check_product_time = False
                else:
                    if date.today() < rec.date_to:
                        rec.check_product_time = True
                    else:
                        rec.check_product_time = False
            else:
                rec.check_product_time = False

    # @api.depends('date_to', 'date_from')
    def _compute_product_warranty(self):
        for rec in self:
            if (rec.date_to == '') or (rec.date_from == ''):
                rec.product_warranty = ''
            else:
                if rec.date_from < rec.date_to:
                    print(rec.date_to > rec.date_from)
                    rec.product_warranty = "PWR/" + rec.date_from.strftime("%d%m%y") + "/" + rec.date_to.strftime("%d%m%y")
                else:
                    rec.product_warranty = ''

    @api.depends('product_warranty')
    def _compute_check_product_warranty(self):
        for rec in self:
            if rec.product_warranty != '':
                rec.check_product_warranty = True
            else:
                rec.check_product_warranty = False

