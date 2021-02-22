# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

class AccountMove(models.Model):

    _inherit = "account.move"

    boleto = fields.Many2many('payment.boleto', string='Boletos', help="Boletos")

    @api.model
    def post(self):
        super().write(vals)
        raise Warning(_('teste super method'))

class BoletoApi(models.Model):

    _name = 'payment.boleto'
