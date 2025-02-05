# models/hotel_room.py

from odoo import models, fields, api

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'

    name = fields.Char(string='Room Name', required=True)
    room_number = fields.Char(string='Room Number', required=True)
    room_type = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ], string='Room Type', default='single')
    base_price = fields.Float(string='Base Price')
    # You can add more fields (floor, capacity, etc.)

    # Example: to check if a room is currently occupied or not
    is_occupied = fields.Boolean(string='Occupied', default=False)

    # If you have advanced logic for availability,
    # you can add helper methods here
