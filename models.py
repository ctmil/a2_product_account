from odoo import tools, models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date,datetime
from odoo.tools.safe_eval import safe_eval

ACCOUNT_DOMAIN = "['&', '&', ('deprecated', '=', False), ('company_id', '=', current_company_id), ('is_off_balance', '=', False)]"

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    property_account_income_id = fields.Many2one('account.account', company_dependent=True,
        string="Income Account",
        domain=ACCOUNT_DOMAIN,
        help="Keep this field empty to use the default value from the product category.")
    property_account_expense_id = fields.Many2one('account.account', company_dependent=True,
        string="Expense Account",
        domain=ACCOUNT_DOMAIN,
        help="Keep this field empty to use the default value from the product category. If anglo-saxon accounting with automated valuation method is configured, the expense account on the product category will be used.")

