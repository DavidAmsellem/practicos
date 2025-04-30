from odoo import models, fields, api, _
from odoo.exceptions import AccessError

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    def write(self, vals):
        """Proporcionar un mensaje de error más claro cuando se intentan editar contactos de compañía"""
        # Verificar contactos de compañía
        company_partners = self.env['res.company'].search([('partner_id', 'in', self.ids)])
        
        if company_partners and not self.env.user.has_group('base.group_system'):
            raise AccessError(_(
                "Solo los usuarios con permisos de Administración / Configuración pueden modificar "
                "los contactos asociados a compañías. Por favor, contacte con su administrador."
            ))
            
        return super(ResPartner, self).write(vals)