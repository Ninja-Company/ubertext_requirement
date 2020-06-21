# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ajustefacturaubertex(models.Model):
    _name ='ajusteubertex'

class AccountInvoiceUbertex(models.Model):
    _inherit='account.invoice.line'

    marca = fields.Many2one(related='product_id.pos_categ_id')

