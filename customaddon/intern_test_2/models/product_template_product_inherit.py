from odoo import fields, models, api
import datetime

class ProductTemplateProductInherit(models.Model):
    _inherit = 'product.template.product'

    date_to = fields.Date()
    date_from = fields.Date()
    to_date = fields.Char(date_to.strftime("%d%m%y"))
    from_date = fields.Char(date_from.strftime("%d%m%y"))
    product_warranty = fields.Text(compute="_compute_product_warranty", store=True)
    check_product_warranty = fields.Boolean(compute="_compute_check_product_warranty", store=True)

    @api.depends('date_to', 'date_from')
    def _compute_check_discount_code(self):
        for rec in self:
            if (rec.date_to == '') or (rec.date_from == ''):
                if rec.date_from < rec.date_to:
                    rec.product_warranty = "PWR/" + rec.from_date + "/" + rec.to_date
                else:
                    rec.product_warranty = ''
            else:
                rec.product_warranty = ''

    @api.depends('product_warranty')
    def _compute_check_product_warranty(self):
        for rec in self:
            if rec.product_warranty != '':
                rec.check_discount_code = True
            else:
                rec.check_discount_code = False




