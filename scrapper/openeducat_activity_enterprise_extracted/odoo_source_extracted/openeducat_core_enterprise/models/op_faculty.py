# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpFaculty(models.Model):
    """OpenEduCat Faculty
    """

    _inherit = ['op.faculty', 'mail.thread', 'mail.activity.mixin', 'rating.mixin', 'website.published.mixin']
    _description = 'OpenEduCat Faculty'

    # ── Fields ──────────────────────────────────────────────
    account_move_count = fields.Integer(string='Account Move Count', store=False)
    active = fields.Boolean(string='Active')
    active_lang_count = fields.Integer(string='Active Lang Count', store=False)
    allowed_department_ids = fields.Many2many('op.department', string='Allowed Department')
    applicant_ids = fields.One2many('hr.applicant', 'False', string='Applicants')
    application_count = fields.Integer(string='Applications', store=False)
    application_statistics = fields.Json(string='Stats', store=False)
    assignment_count = fields.Integer(string='Assignment Count', store=False)
    autopost_bills = fields.Selection(string='Auto-post bills', required=True, store=False, selection=[], help='Automatically post bills for this trusted partner')
    available_invoice_template_pdf_report_ids = fields.One2many('ir.actions.report', 'False', string='Available Invoice Template Pdf Report')
    available_peppol_eas = fields.Json(string='Available Peppol Eas', store=False)
    avatar_1024 = fields.Binary(string='Avatar 1024', store=False)
    avatar_128 = fields.Binary(string='Avatar 128', store=False)
    avatar_1920 = fields.Binary(string='Avatar', store=False)
    avatar_256 = fields.Binary(string='Avatar 256', store=False)
    avatar_512 = fields.Binary(string='Avatar 512', store=False)
    bank_account_count = fields.Integer(string='Bank', store=False)
    bank_ids = fields.One2many('res.partner.bank', 'False', string='Banks')
    barcode = fields.Char(string='Barcode', store=False, help='Use a barcode to identify this contact.')
    bio_data = fields.Html(string='Bio Data')
    birth_date = fields.Date(string='Birth Date', required=True)
    blood_group = fields.Selection(string='Blood Group', selection=[])
    buyer_id = fields.Many2one('res.users', string='Buyer', store=False)
    calendar_last_notif_ack = fields.Datetime(string='Last notification marked as read from base Calendar', store=False)
    can_publish = fields.Boolean(string='Can Publish', store=False)
    category_id = fields.Many2many('res.partner.category', string='Tags')
    certifications_company_count = fields.Integer(string='Company Certifications Count', store=False)
    certifications_count = fields.Integer(string='Certifications Count', store=False)
    channel_ids = fields.Many2many('discuss.channel', string='Channels')
    channel_member_ids = fields.One2many('discuss.channel.member', 'False', string='Channel Member')
    chatbot_script_ids = fields.One2many('chatbot.script', 'False', string='Chatbot Script')
    child_ids = fields.One2many('res.partner', 'False', string='Contact')
    city = fields.Char(string='City', store=False)
    code = fields.Char(string='Company Code', store=False)
    color = fields.Integer(string='Color Index', store=False)
    comment = fields.Html(string='Notes', store=False)
    commercial_company_name = fields.Char(string='Company Name Entity', store=False)
    commercial_partner_id = fields.Many2one('res.partner', string='Commercial Entity', store=False)
    company_id = fields.Many2one('res.company', string='Company')
    company_name = fields.Char(string='Company Name', store=False)
    company_registry = fields.Char(string='Company ID', store=False, help='The registry number of the company. Use it if it is different from the Tax ID. It must be unique across all partners of ')
    company_registry_label = fields.Char(string='Company ID Label', store=False)
    company_registry_placeholder = fields.Char(string='Company Registry Placeholder', store=False)
    company_type = fields.Selection(string='Company Type', store=False, selection=[])
    complete_name = fields.Char(string='Complete Name', store=False)
    contact_address = fields.Char(string='Complete Address', store=False)
    contact_address_inline = fields.Char(string='Inlined Complete Address', store=False)
    contract_ids = fields.One2many('account.analytic.account', 'False', string='Partner Contracts')
    country_code = fields.Char(string='Country Code', store=False, help='The ISO country code in two chars.  You can use this field for quick search.')
    country_id = fields.Many2one('res.country', string='Country', store=False)
    course_count = fields.Integer(string='Course Count', store=False)
    credit = fields.Monetary(string='Total Receivable', store=False, help='Total amount this customer owes you.')
    credit_limit = fields.Float(string='Credit Limit', store=False, help='Credit limit specific to this partner.')
    credit_to_invoice = fields.Monetary(string='Credit To Invoice', store=False)
    currency_id = fields.Many2one('res.currency', string='Currency', store=False)
    customer_rank = fields.Integer(string='Customer Rank', store=False)
    days_sales_outstanding = fields.Float(string='Days Sales Outstanding (DSO)', store=False, help='[(Total Receivable/Total Revenue) * number of days since the first invoice] for this customer')
    debit = fields.Monetary(string='Total Payable', store=False, help='Total amount you have to pay to this vendor.')
    designation = fields.Char(string='Designation')
    display_invoice_edi_format = fields.Boolean(string='Display Invoice Edi Format', store=False)
    display_invoice_template_pdf_report_id = fields.Boolean(string='Display Invoice Template Pdf Report', store=False)
    duplicate_bank_partner_ids = fields.Many2many('res.partner', string='Duplicate Bank Partner')
    email = fields.Char(string='Email', store=False)
    email_formatted = fields.Char(string='Formatted Email', store=False, help='Format email address "Name <email@domain>"')
    email_normalized = fields.Char(string='Normalized Email', store=False, help='This field is used to search on email address as the primary email field can contain more than strictly an email address')
    emergency_contact = fields.Many2one('res.partner', string='Emergency Contact')
    emp_id = fields.Many2one('hr.employee', string='HR Employee')
    employee = fields.Boolean(string='Employee', store=False, help='Whether this contact is an Employee.')
    employee_ids = fields.One2many('hr.employee', 'False', string='Employees', help='Related employees based on their private address')
    employees_count = fields.Integer(string='Employees Count', store=False)
    event_count = fields.Integer(string='# Events', store=False)
    faculty_subject_ids = fields.Many2many('op.subject', string='Subject(s)')
    first_name = fields.Char(string='First Name', required=True)
    fiscal_country_codes = fields.Char(string='Fiscal Country Codes', store=False)
    fiscal_country_group_codes = fields.Json(string='Fiscal Country Group Codes', store=False)
    function = fields.Char(string='Job Position', store=False)
    gender = fields.Selection(string='Gender', required=True, selection=[])
    global_location_number = fields.Char(string='GLN', store=False, help='Global Location Number')
    group_on = fields.Selection(string='Week Day', required=True, store=False, selection=[])
    group_rfq = fields.Selection(string='Group RFQ', required=True, store=False, selection=[], help='Define if RFQ should be grouped         together based on expected arrival, except for dropship operations.          On ')
    head_office = fields.Char(string='Head Office', store=False)
    health_faculty_count = fields.Integer(string='Health Faculty Count', store=False)
    health_faculty_lines = fields.One2many('op.health', 'faculty_id', string='Health Detail')
    hr_contact = fields.Char(string='HR Contact', store=False)
    hr_email = fields.Char(string='HR Email', store=False)
    hr_name = fields.Char(string='HR Name', store=False)
    id_number = fields.Char(string='ID Card Number')
    ignore_abnormal_invoice_amount = fields.Boolean(string='Ignore Abnormal Invoice Amount', store=False)
    ignore_abnormal_invoice_date = fields.Boolean(string='Ignore Abnormal Invoice Date', store=False)
    im_status = fields.Char(string='IM Status', store=False)
    image_1024 = fields.Binary(string='Image 1024', store=False)
    image_128 = fields.Binary(string='Image 128', store=False)
    image_1920 = fields.Binary(string='Image', store=False)
    image_256 = fields.Binary(string='Image 256', store=False)
    image_512 = fields.Binary(string='Image 512', store=False)
    industry_id = fields.Many2one('res.partner.industry', string='Industry', store=False)
    invoice_edi_format = fields.Selection(string='eInvoice format', store=False, selection=[])
    invoice_edi_format_store = fields.Char(string='Invoice Edi Format Store', store=False)
    invoice_ids = fields.One2many('account.move', 'False', string='Invoices')
    invoice_sending_method = fields.Selection(string='Invoice sending', store=False, selection=[])
    invoice_template_pdf_report_id = fields.Many2one('ir.actions.report', string='Invoice report', store=False)
    is_blacklisted = fields.Boolean(string='Blacklist', store=False, help='If the email address is on the blacklist, the contact won\'t receive mass mailing anymore, from any list')
    is_company = fields.Boolean(string='Is a Company', store=False, help='Check if the contact is a company, otherwise it is a person')
    is_in_call = fields.Boolean(string='Is In Call', store=False)
    is_parent = fields.Boolean(string='Is a Parent', store=False)
    is_peppol_edi_format = fields.Boolean(string='Is Peppol Edi Format', store=False)
    is_pickup_location = fields.Boolean(string='Is Pickup Location', store=False)
    is_public = fields.Boolean(string='Is Public', store=False)
    is_published = fields.Boolean(string='Is Published', store=False)
    is_seo_optimized = fields.Boolean(string='SEO optimized', store=False)
    is_student = fields.Boolean(string='Is a Student', store=False)
    is_ubl_format = fields.Boolean(string='Is Ubl Format', store=False)
    is_venue = fields.Boolean(string='Venue', store=False)
    lang = fields.Selection(string='Language', store=False, selection=[], help='All the emails and documents sent to this contact will be translated in this language.')
    last_login = fields.Datetime(string='Latest Connection', store=False)
    last_name = fields.Char(string='Last Name', required=True)
    leave_date_to = fields.Date(string='Leave Date To', store=False)
    library_card_id = fields.Many2one('op.library.card', string='Library Card')
    livechat_channel_count = fields.Integer(string='Livechat Channel Count', store=False)
    login = fields.Char(string='Login', store=False, help='Used to log into the system')
    main_department_id = fields.Many2one('op.department', string='Main Department')
    main_user_id = fields.Many2one('res.users', string='Main User', store=False, help='There can be several users related to the same partner. When a single user is needed, this field attempts to find the mo')
    media_movement_lines = fields.One2many('op.media.movement', 'faculty_id', string='Movements')
    media_movement_lines_count = fields.Integer(string='Media Movement Lines Count', store=False)
    meeting_count = fields.Integer(string='# Meetings', store=False)
    meeting_ids = fields.Many2many('calendar.event', string='Meetings')
    message_bounce = fields.Integer(string='Bounce', store=False, help='Counter of the number of bounced emails for this contact')
    middle_name = fields.Char(string='Middle Name')
    name = fields.Char(string='Name', store=False)
    nationality = fields.Many2one('res.country', string='Nationality')
    offline_since = fields.Datetime(string='Offline since', store=False)
    on_time_rate = fields.Float(string='On-Time Delivery Rate', store=False, help='Over the past x days; the number of products received on time divided by the number of ordered products.x is either the ')
    opportunity_count = fields.Integer(string='Opportunity Count', store=False)
    opportunity_ids = fields.One2many('crm.lead', 'False', string='Opportunities')
    parent_id = fields.Many2one('res.partner', string='Related Company', store=False)
    parent_name = fields.Char(string='Parent name', store=False)
    partner_company_registry_placeholder = fields.Char(string='Partner Company Registry Placeholder', store=False)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    partner_latitude = fields.Float(string='Geo Latitude', store=False)
    partner_longitude = fields.Float(string='Geo Longitude', store=False)
    partner_share = fields.Boolean(string='Share Partner', store=False, help='Either customer (not a user), either shared user. Indicated the current partner is a customer without access or with a l')
    partner_vat_placeholder = fields.Char(string='Partner Vat Placeholder', store=False)
    payment_token_count = fields.Integer(string='Payment Token Count', store=False)
    payment_token_ids = fields.One2many('payment.token', 'False', string='Payment Tokens')
    peppol_eas = fields.Selection(string='Peppol e-address (EAS)', store=False, selection=[], help='Code used to identify the Endpoint for BIS Billing 3.0 and its derivatives.              List available at https://docs.')
    peppol_endpoint = fields.Char(string='Peppol Endpoint', store=False, help='Unique identifier used by the BIS Billing 3.0 and its derivatives, also known as \'Endpoint ID\'.')
    phone = fields.Char(string='Phone', store=False)
    phone_blacklisted = fields.Boolean(string='Blacklisted Phone is Phone', store=False, help='Indicates if a blacklisted sanitized phone number is a phone number. Helps distinguish which number is blacklisted      ')
    phone_mobile_search = fields.Char(string='Phone Number', store=False)
    phone_sanitized = fields.Char(string='Sanitized Number', store=False, help='Field used to store sanitized phone number. Helps speeding up searches and comparisons.')
    phone_sanitized_blacklisted = fields.Boolean(string='Phone Blacklisted', store=False, help='If the sanitized phone number is on the blacklist, the contact won\'t receive mass mailing sms anymore, from any list')
    picking_warn_msg = fields.Text(string='Message for Stock Picking', store=False)
    properties = fields.Properties(string='Properties', store=False)
    properties_base_definition_id = fields.Many2one('properties.base.definition', string='Properties Base Definition', store=False)
    property_account_payable_id = fields.Many2one('account.account', string='Account Payable', store=False)
    property_account_position_id = fields.Many2one('account.fiscal.position', string='Fiscal Position', store=False, help='The fiscal position determines the taxes/accounts used for this contact.')
    property_account_receivable_id = fields.Many2one('account.account', string='Account Receivable', store=False)
    property_delivery_carrier_id = fields.Many2one('delivery.carrier', string='Delivery Method', store=False, help='Used in sales orders.')
    property_inbound_payment_method_line_id = fields.Many2one('account.payment.method.line', string='Property Inbound Payment Method Line', store=False)
    property_outbound_payment_method_line_id = fields.Many2one('account.payment.method.line', string='Property Outbound Payment Method Line', store=False)
    property_payment_term_id = fields.Many2one('account.payment.term', string='Customer Payment Terms', store=False)
    property_product_pricelist = fields.Many2one('product.pricelist', string='Pricelist', store=False, help='Used for sales to the current partner')
    property_purchase_currency_id = fields.Many2one('res.currency', string='Supplier Currency', store=False, help='This currency will be used for purchases from the current partner')
    property_stock_customer = fields.Many2one('stock.location', string='Customer Location', store=False, help='The stock location used as destination when sending goods to this contact.')
    property_stock_supplier = fields.Many2one('stock.location', string='Vendor Location', store=False, help='The stock location used as source when receiving goods from this contact.')
    property_supplier_payment_term_id = fields.Many2one('account.payment.term', string='Vendor Payment Terms', store=False)
    purchase_line_ids = fields.One2many('purchase.order.line', 'False', string='Purchase Lines')
    purchase_order_count = fields.Integer(string='Purchase Order Count', store=False)
    purchase_warn_msg = fields.Text(string='Message for Purchase Order', store=False)
    receipt_reminder_email = fields.Boolean(string='Receipt Reminder', store=False, help='Automatically send a confirmation email to the vendor X days before the expected receipt date, asking him to confirm the')
    ref = fields.Char(string='Reference', store=False)
    ref_company_ids = fields.One2many('res.company', 'False', string='Companies that refers to partner')
    reminder_date_before_receipt = fields.Integer(string='Days Before Receipt', store=False, help='Number of days to send reminder email before the promised receipt date')
    rtc_session_ids = fields.One2many('discuss.channel.rtc.session', 'False', string='Rtc Session')
    sale_order_count = fields.Integer(string='Sale Order Count', store=False)
    sale_order_ids = fields.One2many('sale.order', 'False', string='Sales Order')
    sale_warn_msg = fields.Text(string='Message for Sales Order', store=False)
    same_company_registry_partner_id = fields.Many2one('res.partner', string='Partner with same Company Registry', store=False)
    same_vat_partner_id = fields.Many2one('res.partner', string='Partner with same Tax ID', store=False)
    self = fields.Many2one('res.partner', string='Self', store=False)
    seo_name = fields.Char(string='Seo name', store=False)
    session_count = fields.Integer(string='Session Count', store=False)
    session_ids = fields.One2many('op.session', 'faculty_id', string='Sessions')
    show_credit_limit = fields.Boolean(string='Show Credit Limit', store=False)
    signup_type = fields.Char(string='Signup Token Type', store=False)
    specific_property_product_pricelist = fields.Many2one('product.pricelist', string='Specific Property Product Pricelist', store=False)
    state_id = fields.Many2one('res.country.state', string='State', store=False)
    static_map_url = fields.Char(string='Static Map Url', store=False)
    static_map_url_is_valid = fields.Boolean(string='Static Map Url Is Valid', store=False)
    street = fields.Char(string='Street', store=False)
    street2 = fields.Char(string='Street2', store=False)
    subject_cost_ids = fields.One2many('op.subject.cost', 'faculty_id', string='Subject Cost')
    subject_count = fields.Integer(string='Subject Count', store=False)
    suggest_based_on = fields.Char(string='Suggest Based On', store=False)
    suggest_days = fields.Integer(string='Suggest Days', store=False)
    suggest_percent = fields.Integer(string='Suggest Percent', store=False)
    supplier_invoice_count = fields.Integer(string='# Vendor Bills', store=False)
    supplier_rank = fields.Integer(string='Supplier Rank', store=False)
    ticket_count = fields.Integer(string='Ticket Count', store=False)
    timetable_count = fields.Integer(string='Timetable Count', store=False)
    title = fields.Many2one('res.partner.title', string='Title', store=False)
    total_invoiced = fields.Monetary(string='Total Invoiced', store=False)
    trust = fields.Selection(string='Degree of trust you have in this debtor', store=False, selection=[])
    type = fields.Selection(string='Address Type', store=False, selection=[])
    type_address_label = fields.Char(string='Address Type Description', store=False)
    tz = fields.Selection(string='Timezone', store=False, selection=[], help='When printing documents and exporting/importing data, time values are computed according to this timezone. If the timezo')
    tz_offset = fields.Char(string='Timezone offset', store=False)
    use_partner_credit_limit = fields.Boolean(string='Partner Limit', store=False, help='Set a value greater than 0.0 to activate a credit limit check')
    user_id = fields.Many2one('res.users', string='Salesperson', store=False, help='The internal user in charge of this contact.')
    user_ids = fields.One2many('res.users', 'False', string='Users')
    user_livechat_username = fields.Char(string='User Livechat Username', store=False)
    vat = fields.Char(string='Tax ID', store=False, help='The Tax Identification Number. Values here will be validated based on the country format. You can use \'/\' to indicate ')
    vat_label = fields.Char(string='Tax ID Label', store=False)
    visa_info = fields.Char(string='Visa Info')
    visitor_ids = fields.One2many('website.visitor', 'False', string='Visitors')
    website = fields.Char(string='Website Link', store=False)
    website_absolute_url = fields.Char(string='Website Absolute URL', store=False, help='The full absolute URL to access the document through the website.')
    website_description = fields.Html(string='Website Partner Full Description', store=False)
    website_id = fields.Many2one('website', string='Website', store=False, help='Restrict to a specific website.')
    website_meta_description = fields.Text(string='Website meta description', store=False)
    website_meta_keywords = fields.Char(string='Website meta keywords', store=False)
    website_meta_og_img = fields.Char(string='Website opengraph image', store=False)
    website_meta_title = fields.Char(string='Website meta title', store=False)
    website_published = fields.Boolean(string='Visible on current website', store=False)
    website_short_description = fields.Text(string='Website Partner Short Description', store=False)
    website_url = fields.Char(string='Website URL', store=False, help='The full relative URL to access the document through the website.')
    wishlist_ids = fields.One2many('product.wishlist', 'False', string='Wishlist')
    zip = fields.Char(string='Zip', store=False)

    # Mixin-inherited fields (not redeclared): activity_calendar_event_id, activity_date_deadline, activity_exception_decoration, activity_exception_icon, activity_ids, activity_state, activity_summary, activity_type_icon, activity_type_id, activity_user_id ...

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read
    #   Library / Manager: read
    #   Role / Portal: read

    # Record Rules:
    #   Faculty Login rule: ['|',('user_id','=',user.id),('emp_id.user_id','=',user.id)]
    #   View Faculties: [(1,'=',1)]
    #   Faculty multi-company: ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]
    #   Faculty multi-department: ['|','|','|','|',('user_id','=',user.id),('emp_id.user_id','=',user.id),('main_department_id','=',False),('main_department_id','child_of',[user.dept_id.id]),('main_department_id','in',user.department_ids.ids)]
    #   Gradebook Faculty Login rule: [(1,'=',1)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_account_move_count(self):
        for rec in self:
            rec.account_move_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_active_lang_count(self):
        for rec in self:
            rec.active_lang_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_application_count(self):
        for rec in self:
            rec.application_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_application_statistics(self):
        for rec in self:
            rec.application_statistics = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_assignment_count(self):
        for rec in self:
            rec.assignment_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_autopost_bills(self):
        for rec in self:
            rec.autopost_bills = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_available_peppol_eas(self):
        for rec in self:
            rec.available_peppol_eas = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_avatar_1024(self):
        for rec in self:
            rec.avatar_1024 = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_avatar_128(self):
        for rec in self:
            rec.avatar_128 = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_avatar_1920(self):
        for rec in self:
            rec.avatar_1920 = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
