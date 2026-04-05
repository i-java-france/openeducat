# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class CalendarEvent(models.Model):
    """Calendar Event
    """

    _inherit = ['calendar.event', 'mail.thread', 'mail.activity.mixin', 'rating.mixin', 'website.published.mixin']
    _description = 'Calendar Event'

    # ── Fields ──────────────────────────────────────────────
    academic_calendar = fields.Boolean(string='Academic Calendar?')
    accepted_count = fields.Integer(string='Accepted Count', store=False)
    access_token = fields.Char(string='Invitation Token')
    active = fields.Boolean(string='Active', help='If the active field is set to false, it will allow you to hide the event alarm information without removing it.')
    alarm_ids = fields.Many2many('calendar.alarm', string='Reminders', help='Notifications sent to all attendees to remind of the meeting.')
    allday = fields.Boolean(string='All Day')
    applicant_id = fields.Many2one('hr.applicant', string='Applicant')
    appointment_id = fields.Many2one('calendar.online.appointment', string='Online Appointment')
    attendee_ids = fields.One2many('calendar.attendee', 'event_id', string='Participant')
    attendees_count = fields.Integer(string='Attendees Count', store=False)
    automatic_email = fields.Boolean(string='Automatic Email')
    awaiting_count = fields.Integer(string='Awaiting Count', store=False)
    batch_ids = fields.Many2many('op.batch', string='Batches')
    booking_status = fields.Selection(string='Booking Status', selection=[])
    byday = fields.Selection(string='By day', store=False, selection=[])
    categ_ids = fields.Many2many('calendar.event.type', string='Tags')
    count = fields.Integer(string='Number of Repetitions', store=False, help='Repeat x times')
    course_ids = fields.Many2many('op.course', string='Courses')
    current_attendee = fields.Many2one('calendar.attendee', string='Current Attendee', store=False)
    current_status = fields.Selection(string='Attending?', store=False, selection=[])
    day = fields.Integer(string='Date of month', store=False)
    declined_count = fields.Integer(string='Declined Count', store=False)
    description = fields.Html(string='Description', help='When synchronization with an external calendar is active, this description is synchronized         with the one of the a')
    display_description = fields.Boolean(string='Display Description', store=False)
    display_time = fields.Char(string='Event Time', store=False)
    duration = fields.Float(string='Duration')
    effective_privacy = fields.Selection(string='Effective Privacy', store=False, selection=[], help='Whether the event is private, considering the user privacy')
    end_type = fields.Selection(string='Recurrence Termination', store=False, selection=[])
    event_tz = fields.Selection(string='Timezone', store=False, selection=[])
    follow_recurrence = fields.Boolean(string='Follow Recurrence')
    fri = fields.Boolean(string='Fri', store=False)
    interval = fields.Integer(string='Repeat On', store=False, help='Repeat every (Days/Week/Month/Year)')
    invalid_email_partner_ids = fields.Many2many('res.partner', string='Invalid Email Partner')
    is_highlighted = fields.Boolean(string='Is the Event Highlighted', store=False)
    is_organizer_alone = fields.Boolean(string='Is the Organizer Alone', store=False, help='Check if the organizer is alone in the event, i.e. if the organizer is the only one that hasn\'t declined         the ev')
    location = fields.Char(string='Location')
    meet_url = fields.Char(string='Google Meet URL')
    meeting_url = fields.Char(string='URL')
    mon = fields.Boolean(string='Mon', store=False)
    month_by = fields.Selection(string='Option', store=False, selection=[])
    mpw = fields.Char(string='Moderator Password')
    name = fields.Char(string='Meeting Subject', required=True)
    notes = fields.Html(string='Notes')
    online_appointment_resource_ids = fields.Many2one('calendar.appointment.resource', string='Online Appointment Resources')
    online_meeting = fields.Boolean(string='Online Meeting')
    op_session_id = fields.Many2one('op.session', string='Session')
    opportunity_id = fields.Many2one('crm.lead', string='Crm Opportunity')
    partner_id = fields.Many2one('res.partner', string='Scheduled by', store=False, help='Partner-related data of the user')
    partner_ids = fields.Many2many('res.partner', string='Attendees')
    privacy = fields.Selection(string='Privacy', selection=[], help='People to whom this event will be visible.')
    recurrence_id = fields.Many2one('calendar.recurrence', string='Recurrence Rule')
    recurrence_update = fields.Selection(string='Recurrence Update', store=False, selection=[], help='Choose what to do with other events in the recurrence. Updating All Events is not allowed when dates or time is modified')
    recurrency = fields.Boolean(string='Recurrent')
    res_id = fields.Char(string='Document ID')
    res_model = fields.Char(string='Document Model Name')
    res_model_id = fields.Many2one('ir.model', string='Document Model')
    res_model_name = fields.Char(string='Model Description', store=False)
    rrule = fields.Char(string='Recurrent Rule', store=False)
    rrule_type = fields.Selection(string='Recurrence', store=False, selection=[], help='Let the event automatically repeat at that interval')
    rrule_type_ui = fields.Selection(string='Repeat', store=False, selection=[], help='Let the event automatically repeat at that interval')
    sat = fields.Boolean(string='Sat', store=False)
    should_show_status = fields.Boolean(string='Should Show Status', store=False)
    show_as = fields.Selection(string='Show as', required=True, selection=[], help='If the time is shown as \'busy\', this event will be visible to other people with either the full         information or')
    start = fields.Datetime(string='Start', required=True, help='Start date of an event, without time for full days events')
    start_date = fields.Date(string='Start Date')
    stop = fields.Datetime(string='Stop', required=True, help='Stop date of an event, without time for full days events')
    stop_date = fields.Date(string='End Date')
    sun = fields.Boolean(string='Sun', store=False)
    tentative_count = fields.Integer(string='Tentative Count', store=False)
    thu = fields.Boolean(string='Thu', store=False)
    tue = fields.Boolean(string='Tue', store=False)
    unavailable_partner_ids = fields.Many2many('res.partner', string='Unavailable Attendees')
    until = fields.Date(string='Until', store=False)
    user_can_edit = fields.Boolean(string='User Can Edit', store=False)
    user_id = fields.Many2one('res.users', string='Organizer')
    videocall_channel_id = fields.Many2one('discuss.channel', string='Discuss Channel')
    videocall_location = fields.Char(string='Meeting URL')
    videocall_source = fields.Selection(string='Videocall Source', store=False, selection=[])
    wed = fields.Boolean(string='Wed', store=False)
    weekday = fields.Selection(string='Weekday', store=False, selection=[])

    # Mixin-inherited fields (not redeclared): activity_ids, create_date, create_uid, display_name, has_message, id, message_attachment_count, message_follower_ids, message_has_error, message_has_error_counter ...

    # Access Rights:
    #   Sales / User: Own Documents Only: read, write, create
    #   Sales / Administrator: read, write, create, unlink
    #   Time Off / Officer: Manage all requests: read, write, create, unlink
    #   Recruitment / Officer: Manage all applicants: read, write, create, unlink
    #   Contact / Creation: read, write, create, unlink
    #   Role / Portal: read
    #   Role / User: read, write, create, unlink

    # Record Rules:
    #   Own events: [('partner_ids', 'in', user.partner_id.id)]
    #   All Calendar Event for employees: [(1, '=', 1)]
    #   Private events: ['|', ('privacy', '!=', 'private'), '&', ('privacy', '=', 'private'), '|', ('user_id', '=', user.id), ('partner_ids', 'in', user.partner_id.id)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_accepted_count(self):
        for rec in self:
            rec.accepted_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_attendees_count(self):
        for rec in self:
            rec.attendees_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_awaiting_count(self):
        for rec in self:
            rec.awaiting_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_byday(self):
        for rec in self:
            rec.byday = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_count(self):
        for rec in self:
            rec.count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_current_attendee(self):
        for rec in self:
            rec.current_attendee = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_current_status(self):
        for rec in self:
            rec.current_status = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_day(self):
        for rec in self:
            rec.day = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_declined_count(self):
        for rec in self:
            rec.declined_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_display_description(self):
        for rec in self:
            rec.display_description = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
