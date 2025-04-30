from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    notes = fields.Text(string="Notas", copy=False)
    
    def _action_confirm(self):
        res = super(SaleOrder, self)._action_confirm()
        for order in self:
            pickings = order.picking_ids.filtered(lambda p: p.state != 'cancel')
            if pickings:
                pickings.write({'notes': order.notes})
        return res