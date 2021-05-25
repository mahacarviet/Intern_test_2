from odoo import fields, models, api
from datetime import datetime

class ProductTemplateProductInherit(models.Model):
    _inherit = 'product.template'

    date_to = fields.Date()
    date_from = fields.Date()
    product_warranty = fields.Text(compute="_compute_product_warranty", store=True)
    check_product_warranty = fields.Boolean(compute="_compute_check_product_warranty", store=True)

    @api.depends('date_to', 'date_from')
    def _compute_product_warranty(self):
        for rec in self:
            if (rec.date_to == '') or (rec.date_from == ''):
                if rec.date_from < rec.date_to:
                    rec.product_warranty = "PWR/" + rec.date_from.strftime("%d%m%y") + "/" + rec.date_to.strftime("%d%m%y")
                else:
                    rec.product_warranty = ''
            else:
                rec.product_warranty = ''

    @api.depends('product_warranty')
    def _compute_check_product_warranty(self):
        for rec in self:
            if rec.product_warranty != '':
                rec.check_product_warranty = True
            else:
                rec.check_product_warranty = False




