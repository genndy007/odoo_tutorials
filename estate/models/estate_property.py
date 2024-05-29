from odoo import fields, models


class Property(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    postcode = fields.Char('Post Code')
    date_availability = fields.Date('Date of Availability')
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('# Bedrooms')
    living_area = fields.Integer('Living Area (m2)')
    facades = fields.Integer('# Facades')
    garage = fields.Boolean('Has Garage')
    garden = fields.Boolean('Has Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('west', 'West'),
            ('east', 'East'),
        ],
        help='Geo Orient of Garden',
    )
