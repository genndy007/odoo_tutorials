from odoo import fields, models


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Real Estate Property Offer'

    price = fields.Float('Price')
    status = fields.Selection(
        string='Status',
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ],
        copy=False,
    )
    partner_id = fields.Many2one('res.partner', 'Partner', required=True, index=True)
    property_id = fields.Many2one('estate.property', 'Property', required=True, index=True)
