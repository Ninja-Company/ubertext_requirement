# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AjusteInventarioUbertex(models.Model):
    _inherit = 'stock.inventory.line'

    barcode2 = fields.Char(related='product_id.barcode',string="Código de Barras")
