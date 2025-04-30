
from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    notes = fields.Text(string="Notas", copy=False)