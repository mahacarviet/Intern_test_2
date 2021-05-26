from odoo import fields, models, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class UpdateProductWarrantyWizard(models.TransientModel):
    _name = 'update.product.warranty.wizard'

