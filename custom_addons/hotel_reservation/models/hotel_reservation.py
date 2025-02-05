# models/hotel_reservation.py

from odoo import models, fields, api
from odoo.exceptions import UserError

class HotelReservation(models.Model):
    _name = 'hotel.reservation'
    _description = 'Hotel Reservation'
    _order = 'check_in_date desc'

    name = fields.Char(string='Reservation Reference', required=True, copy=False, readonly=True,
                       default=lambda self: self.env['ir.sequence'].next_by_code('hotel.reservation'))
    guest_name = fields.Char(string='Guest Name', required=True)
    room_id = fields.Many2one('hotel.room', string='Room', required=True)
    check_in_date = fields.Datetime(string='Check-In', required=True)
    check_out_date = fields.Datetime(string='Check-Out', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('in_stay', 'In Stay'),
        ('checked_out', 'Checked Out'),
        ('cancel', 'Canceled'),
    ], default='draft', string='Status')

    # Optional deposit or prepayment
    deposit_amount = fields.Float(string='Deposit Amount')
    # Could integrate with Accounting/Payments if needed

    # Example: compute total price (basic example without advanced pricing rules)
    total_price = fields.Float(string='Total Price', compute='_compute_total_price', store=True)

    @api.depends('room_id', 'check_in_date', 'check_out_date')
    def _compute_total_price(self):
        for rec in self:
            if rec.room_id and rec.check_in_date and rec.check_out_date:
                # Simple example: base_price * number_of_nights
                delta = rec.check_out_date - rec.check_in_date
                nights = delta.days + (delta.seconds / 86400.0)
                rec.total_price = rec.room_id.base_price * nights
            else:
                rec.total_price = 0.0

    # State transitions
    def action_confirm(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError("Reservation can only be confirmed from Draft state.")
            rec.state = 'confirm'
            # Optionally mark the room as occupied
            if rec.room_id:
                rec.room_id.is_occupied = True

    def action_in_stay(self):
        for rec in self:
            if rec.state != 'confirm':
                raise UserError("Reservation must be Confirmed before 'In Stay'.")
            rec.state = 'in_stay'

    def action_check_out(self):
        for rec in self:
            if rec.state != 'in_stay':
                raise UserError("Reservation must be 'In Stay' to check out.")
            rec.state = 'checked_out'
            # Mark the room as not occupied
            if rec.room_id:
                rec.room_id.is_occupied = False

    def action_cancel(self):
        for rec in self:
            if rec.state == 'checked_out':
                raise UserError("Cannot cancel a reservation that has already been checked out.")
            rec.state = 'cancel'
            # Free the room if it was occupied
            if rec.room_id:
                rec.room_id.is_occupied = False
