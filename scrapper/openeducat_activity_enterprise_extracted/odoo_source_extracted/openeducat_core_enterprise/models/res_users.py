# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class ResUsers(models.Model):
    """User

    Update of res.users class
        - add a preference about username for livechat purpose
    """

    _inherit = ['res.users', 'mail.thread', 'mail.activity.mixin', 'rating.mixin', 'website.published.mixin']
    _description = 'User'

    # ── Fields ──────────────────────────────────────────────
    access_token = fields.Char(string='Access Token')
    accesses_count = fields.Integer(string='# Access Rights', store=False, help='Number of access rights that apply to the current user')
    account_move_count = fields.Integer(string='Account Move Count', store=False)
    action_id = fields.Many2one('ir.actions.actions', string='Home Action', help='If specified, this action will be opened at log on for this user, in addition to the standard menu.')
    active = fields.Boolean(string='Active')
    active_lang_count = fields.Integer(string='Active Lang Count', store=False)
    active_partner = fields.Boolean(string='Partner is Active', store=False)
    additional_note = fields.Text(string='Additional Note', store=False)
    all_group_ids = fields.Many2many('res.groups', string='Groups and implied groups')
    api_key_ids = fields.One2many('res.users.apikeys', 'user_id', string='API Keys')
    applicant_ids = fields.One2many('hr.applicant', 'False', string='Applicants')
    application_count = fields.Integer(string='Applications', store=False)
    application_statistics = fields.Json(string='Stats', store=False)
    auth_passkey_key_ids = fields.One2many('auth.passkey.key', 'create_uid', string='Auth Passkey Key')
    autopost_bills = fields.Selection(string='Auto-post bills', required=True, store=False, selection=[], help='Automatically post bills for this trusted partner')
    available_invoice_template_pdf_report_ids = fields.One2many('ir.actions.report', 'False', string='Available Invoice Template Pdf Report')
    available_peppol_eas = fields.Json(string='Available Peppol Eas', store=False)
    avatar_1024 = fields.Binary(string='Avatar 1024', store=False)
    avatar_128 = fields.Binary(string='Avatar 128', store=False)
    avatar_1920 = fields.Binary(string='Avatar', store=False)
    avatar_256 = fields.Binary(string='Avatar 256', store=False)
    avatar_512 = fields.Binary(string='Avatar 512', store=False)
    badge_ids = fields.One2many('gamification.badge.user', 'user_id', string='Badges')
    bank_account_count = fields.Integer(string='Bank', store=False)
    bank_account_ids = fields.Many2many('res.partner.bank', string='Bank Accounts', help='Employee bank accounts to pay salaries')
    bank_ids = fields.One2many('res.partner.bank', 'False', string='Banks')
    barcode = fields.Char(string='Badge ID', store=False, help='ID used for employee identification.')
    bronze_badge = fields.Integer(string='Bronze badges count', store=False)
    buyer_id = fields.Many2one('res.users', string='Buyer', store=False)
    calendar_default_privacy = fields.Selection(string='Calendar Default Privacy', store=False, selection=[])
    calendar_last_notif_ack = fields.Datetime(string='Last notification marked as read from base Calendar', store=False)
    can_edit_role = fields.Boolean(string='Can Edit Role', store=False)
    can_publish = fields.Boolean(string='Can Publish', store=False)
    category_id = fields.Many2many('res.partner.category', string='Tags')
    category_ids = fields.Many2many('hr.employee.category', string='Employee Tags')
    certifications_company_count = fields.Integer(string='Company Certifications Count', store=False)
    certifications_count = fields.Integer(string='Certifications Count', store=False)
    channel_ids = fields.Many2many('discuss.channel', string='Channels')
    channel_member_ids = fields.One2many('discuss.channel.member', 'False', string='Channel Member')
    chatbot_script_ids = fields.One2many('chatbot.script', 'False', string='Chatbot Script')
    chatter_position = fields.Selection(string='Chatter Position', selection=[])
    child_ids = fields.Many2many('res.users', string='Childs')
    city = fields.Char(string='City', store=False)
    client_id = fields.Char(string='Client ID')
    client_secret = fields.Char(string='Client Secret')
    code = fields.Char(string='Company Code', store=False)
    color = fields.Integer(string='Color Index', store=False)
    comment = fields.Html(string='Notes', store=False)
    commercial_company_name = fields.Char(string='Company Name Entity', store=False)
    commercial_partner_id = fields.Many2one('res.partner', string='Commercial Entity', store=False)
    companies_count = fields.Integer(string='Number of Companies', store=False)
    company_id = fields.Many2one('res.company', string='Company', required=True, help='The default company for this user.')
    company_ids = fields.Many2many('res.company', string='Companies')
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
    create_employee = fields.Boolean(string='Technical field, whether to create an employee', store=False)
    create_employee_id = fields.Many2one('hr.employee', string='Technical field, bind user to this employee on create', store=False)
    credit = fields.Monetary(string='Total Receivable', store=False, help='Total amount this customer owes you.')
    credit_limit = fields.Float(string='Credit Limit', store=False, help='Credit limit specific to this partner.')
    credit_to_invoice = fields.Monetary(string='Credit To Invoice', store=False)
    crm_team_ids = fields.Many2many('crm.team', string='Sales Teams')
    crm_team_member_ids = fields.One2many('crm.team.member', 'user_id', string='Sales Team Members')
    currency_id = fields.Many2one('res.currency', string='Currency', store=False)
    customer_rank = fields.Integer(string='Customer Rank', store=False)
    dark_mode = fields.Boolean(string='Dark Mode')
    days_sales_outstanding = fields.Float(string='Days Sales Outstanding (DSO)', store=False, help='[(Total Receivable/Total Revenue) * number of days since the first invoice] for this customer')
    debit = fields.Monetary(string='Total Payable', store=False, help='Total amount you have to pay to this vendor.')
    department_count = fields.Integer(string='Number of Departments', store=False)
    department_ids = fields.Many2many('op.department', string='Allowed Department')
    dept_id = fields.Many2one('op.department', string='Department Name')
    device_ids = fields.One2many('res.device', 'user_id', string='User devices')
    display_invoice_edi_format = fields.Boolean(string='Display Invoice Edi Format', store=False)
    display_invoice_template_pdf_report_id = fields.Boolean(string='Display Invoice Template Pdf Report', store=False)
    duplicate_bank_partner_ids = fields.Many2many('res.partner', string='Duplicate Bank Partner')
    email = fields.Char(string='Email', store=False)
    email_domain_placeholder = fields.Char(string='Email Domain Placeholder', store=False)
    email_formatted = fields.Char(string='Formatted Email', store=False, help='Format email address "Name <email@domain>"')
    email_normalized = fields.Char(string='Normalized Email', store=False, help='This field is used to search on email address as the primary email field can contain more than strictly an email address')
    emergency_contact = fields.Char(string='Emergency Contact', store=False)
    emergency_phone = fields.Char(string='Emergency Phone', store=False)
    employee = fields.Boolean(string='Employee', store=False, help='Whether this contact is an Employee.')
    employee_bank_account_ids = fields.Many2many('res.partner.bank', string='Employee's Bank Accounts', help='Employee bank accounts to pay salaries')
    employee_count = fields.Integer(string='Employee Count', store=False)
    employee_id = fields.Many2one('hr.employee', string='Company employee', store=False)
    employee_ids = fields.One2many('hr.employee', 'user_id', string='Related employee')
    employee_resource_calendar_id = fields.Many2one('resource.calendar', string='Employee's Working Hours', store=False, help='Working hour of week')
    employees_count = fields.Integer(string='Employees Count', store=False)
    esign_initials = fields.Binary(string='Digitial Initials')
    esign_signature = fields.Binary(string='Digital Signature')
    event_count = fields.Integer(string='# Events', store=False)
    fiscal_country_codes = fields.Char(string='Fiscal Country Codes', store=False)
    fiscal_country_group_codes = fields.Json(string='Fiscal Country Group Codes', store=False)
    friday_location_id = fields.Many2one('hr.work.location', string='Fridays', store=False)
    function = fields.Char(string='Job Position', store=False)
    global_location_number = fields.Char(string='GLN', store=False, help='Global Location Number')
    goal_ids = fields.One2many('gamification.goal', 'user_id', string='Goal')
    gold_badge = fields.Integer(string='Gold badges count', store=False)
    grievance_team_id = fields.Many2one('grievance.team', string='Grievance Team')
    group_ids = fields.Many2many('res.groups', string='Groups', help='Groups explicitly assigned to the user')
    group_on = fields.Selection(string='Week Day', required=True, store=False, selection=[])
    group_rfq = fields.Selection(string='Group RFQ', required=True, store=False, selection=[], help='Define if RFQ should be grouped         together based on expected arrival, except for dropship operations.          On ')
    groups_count = fields.Integer(string='# Groups', store=False, help='Number of groups that apply to the current user')
    has_access_livechat = fields.Boolean(string='Has access to Livechat', store=False)
    has_external_mail_server = fields.Boolean(string='Has External Mail Server', store=False)
    head_office = fields.Char(string='Head Office', store=False)
    hr_contact = fields.Char(string='HR Contact', store=False)
    hr_email = fields.Char(string='HR Email', store=False)
    hr_name = fields.Char(string='HR Name', store=False)
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
    is_hr_user = fields.Boolean(string='Is Hr User', store=False)
    is_in_call = fields.Boolean(string='Is in call', store=False)
    is_out_of_office = fields.Boolean(string='Out of Office', store=False)
    is_parent = fields.Boolean(string='Is a Parent', store=False)
    is_peppol_edi_format = fields.Boolean(string='Is Peppol Edi Format', store=False)
    is_pickup_location = fields.Boolean(string='Is Pickup Location', store=False)
    is_public = fields.Boolean(string='Is Public', store=False)
    is_published = fields.Boolean(string='Is Published', store=False)
    is_seo_optimized = fields.Boolean(string='SEO optimized', store=False)
    is_student = fields.Boolean(string='Is a Student', store=False)
    is_system = fields.Boolean(string='Is System', store=False)
    is_ubl_format = fields.Boolean(string='Is Ubl Format', store=False)
    is_venue = fields.Boolean(string='Venue', store=False)
    job_title = fields.Char(string='Job Title', store=False)
    karma = fields.Integer(string='Karma')
    karma_tracking_ids = fields.One2many('gamification.karma.tracking', 'user_id', string='Karma Changes')
    km_home_work = fields.Integer(string='Home-Work Distance in Km', store=False)
    lang = fields.Selection(string='Language', store=False, selection=[], help='All the emails and documents sent to this contact will be translated in this language.')
    leave_date_to = fields.Date(string='To Date', store=False)
    livechat_channel_count = fields.Integer(string='Livechat Channel Count', store=False)
    livechat_channel_ids = fields.Many2many('im_livechat.channel', string='Livechat Channel')
    livechat_expertise_ids = fields.Many2many('im_livechat.expertise', string='Live Chat Expertise', help='When forwarding live chat conversations, the chatbot will prioritize users with matching expertise.')
    livechat_is_in_call = fields.Boolean(string='Livechat Is In Call', store=False, help='Whether the user is in a call, only available if the user is in a live chat agent')
    livechat_lang_ids = fields.Many2many('res.lang', string='Livechat Languages')
    livechat_ongoing_session_count = fields.Integer(string='Number of Ongoing sessions', store=False)
    livechat_username = fields.Char(string='Livechat Username', store=False)
    log_ids = fields.One2many('res.users.log', 'create_uid', string='User log entries')
    login = fields.Char(string='Login', required=True, help='Used to log into the system')
    login_date = fields.Datetime(string='Latest Login', store=False)
    logo_visible = fields.Boolean(string='Show Company Logo in Sidebar')
    main_user_id = fields.Many2one('res.users', string='Main User', store=False, help='There can be several users related to the same partner. When a single user is needed, this field attempts to find the mo')
    manual_im_status = fields.Selection(string='IM status manually set by the user', selection=[])
    meeting_count = fields.Integer(string='# Meetings', store=False)
    meeting_ids = fields.Many2many('calendar.event', string='Meetings')
    message_bounce = fields.Integer(string='Bounce', store=False, help='Counter of the number of bounced emails for this contact')
    mobile_phone = fields.Char(string='Work Mobile', store=False)
    monday_location_id = fields.Many2one('hr.work.location', string='Mondays', store=False)
    name = fields.Char(string='Name', store=False)
    new_password = fields.Char(string='Set Password', store=False, help='Specify a value only when creating a user or if you\'re changing the user\'s password, otherwise leave empty. After a ch')
    next_rank_id = fields.Many2one('gamification.karma.rank', string='Next Rank')
    notification_type = fields.Selection(string='Notification', required=True, selection=[], help='Policy on how to handle Chatter notifications: - By Emails: notifications are sent to your email address - In Odoo: noti')
    odoobot_failed = fields.Boolean(string='Odoobot Failed')
    odoobot_state = fields.Selection(string='OdooBot Status', selection=[])
    offline_since = fields.Datetime(string='Offline since', store=False)
    on_time_rate = fields.Float(string='On-Time Delivery Rate', store=False, help='Over the past x days; the number of products received on time divided by the number of ordered products.x is either the ')
    onesignal_device_id = fields.Char(string='One Signal Device ID')
    opportunity_count = fields.Integer(string='Opportunity Count', store=False)
    opportunity_ids = fields.One2many('crm.lead', 'False', string='Opportunities')
    out_of_office_from = fields.Datetime(string='Out Of Office From')
    out_of_office_message = fields.Html(string='Vacation Responder')
    out_of_office_to = fields.Datetime(string='Out Of Office To')
    outgoing_mail_server_id = fields.Many2one('ir.mail_server', string='Outgoing Mail Server', store=False)
    outgoing_mail_server_type = fields.Selection(string='Outgoing Mail Server Type', required=True, store=False, selection=[])
    parent_id = fields.Many2one('res.partner', string='Related Company', store=False)
    parent_name = fields.Char(string='Parent name', store=False)
    partner_company_registry_placeholder = fields.Char(string='Partner Company Registry Placeholder', store=False)
    partner_id = fields.Many2one('res.partner', string='Related Partner', required=True, help='Partner-related data of the user')
    partner_latitude = fields.Float(string='Geo Latitude', store=False)
    partner_longitude = fields.Float(string='Geo Longitude', store=False)
    partner_share = fields.Boolean(string='Share Partner', store=False, help='Either customer (not a user), either shared user. Indicated the current partner is a customer without access or with a l')
    partner_vat_placeholder = fields.Char(string='Partner Vat Placeholder', store=False)
    password = fields.Char(string='Password', store=False, help='Keep empty if you don\'t want the user to be able to connect on the system.')
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
    pin = fields.Char(string='PIN', store=False, help='PIN used to Check In/Out in the Kiosk Mode of the Attendance application (if enabled in Configuration) and to change the')
    pin_whatsapp_contact_id = fields.Char(string='Pin Whatsapp Contact')
    placement_team_id = fields.Many2one('op.placement.cell', string='Placement Team Members')
    presence_ids = fields.One2many('mail.presence', 'user_id', string='Presence')
    private_city = fields.Char(string='Private City', store=False)
    private_country_id = fields.Many2one('res.country', string='Private Country', store=False)
    private_email = fields.Char(string='Private Email', store=False)
    private_phone = fields.Char(string='Private Phone', store=False)
    private_state_id = fields.Many2one('res.country.state', string='Private State', store=False)
    private_street = fields.Char(string='Private Street', store=False)
    private_street2 = fields.Char(string='Private Street2', store=False)
    private_zip = fields.Char(string='Private Zip', store=False)
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
    property_warehouse_id = fields.Many2one('stock.warehouse', string='Default Warehouse')
    purchase_line_ids = fields.One2many('purchase.order.line', 'False', string='Purchase Lines')
    purchase_order_count = fields.Integer(string='Purchase Order Count', store=False)
    purchase_warn_msg = fields.Text(string='Message for Purchase Order', store=False)
    rank_id = fields.Many2one('gamification.karma.rank', string='Rank')
    receipt_reminder_email = fields.Boolean(string='Receipt Reminder', store=False, help='Automatically send a confirmation email to the vendor X days before the expected receipt date, asking him to confirm the')
    ref = fields.Char(string='Reference', store=False)
    ref_company_ids = fields.One2many('res.company', 'False', string='Companies that refers to partner')
    refresh_token = fields.Char(string='Refresh Token')
    reminder_date_before_receipt = fields.Integer(string='Days Before Receipt', store=False, help='Number of days to send reminder email before the promised receipt date')
    res_users_settings_id = fields.Many2one('res.users.settings', string='Settings', store=False)
    res_users_settings_ids = fields.One2many('res.users.settings', 'user_id', string='Res Users Settings')
    resource_calendar_id = fields.Many2one('resource.calendar', string='Default Working Hours', store=False, help='Define the working schedule of the resource. If not set, the resource will have fully flexible working hours.')
    resource_ids = fields.One2many('resource.resource', 'user_id', string='Resources')
    role = fields.Selection(string='Role', store=False, selection=[])
    role_ids = fields.Many2many('res.role', string='User Roles', help='Users are notified whenever one of their roles is @-mentioned in a conversation.')
    role_line_ids = fields.One2many('res.users.role.line', 'user_id', string='Role lines')
    rtc_session_ids = fields.One2many('discuss.channel.rtc.session', 'False', string='Rtc Session')
    rules_count = fields.Integer(string='# Record Rules', store=False, help='Number of record rules that apply to the current user')
    sale_order_count = fields.Integer(string='Sale Order Count', store=False)
    sale_order_ids = fields.One2many('sale.order', 'False', string='Sales Order')
    sale_team_id = fields.Many2one('crm.team', string='User Sales Team', help='Main user sales team. Used notably for pipeline, or to set sales team in invoicing or subscription.')
    sale_warn_msg = fields.Text(string='Message for Sales Order', store=False)
    same_company_registry_partner_id = fields.Many2one('res.partner', string='Partner with same Company Registry', store=False)
    same_vat_partner_id = fields.Many2one('res.partner', string='Partner with same Tax ID', store=False)
    saturday_location_id = fields.Many2one('hr.work.location', string='Saturdays', store=False)
    self = fields.Many2one('res.partner', string='Self', store=False)
    seo_name = fields.Char(string='Seo name', store=False)
    share = fields.Boolean(string='Share User', help='External user with limited access, created only for the purpose of sharing data.')
    show_alert = fields.Boolean(string='Show Alert', store=False)
    show_credit_limit = fields.Boolean(string='Show Credit Limit', store=False)
    signature = fields.Html(string='Email Signature')
    signup_type = fields.Char(string='Signup Token Type', store=False)
    silver_badge = fields.Integer(string='Silver badges count', store=False)
    specific_property_product_pricelist = fields.Many2one('product.pricelist', string='Specific Property Product Pricelist', store=False)
    state = fields.Selection(string='Status', store=False, selection=[])
    state_id = fields.Many2one('res.country.state', string='State', store=False)
    static_map_url = fields.Char(string='Static Map Url', store=False)
    static_map_url_is_valid = fields.Boolean(string='Static Map Url Is Valid', store=False)
    street = fields.Char(string='Street', store=False)
    street2 = fields.Char(string='Street2', store=False)
    student_line = fields.Many2one('op.student', string='Line')
    suggest_based_on = fields.Char(string='Suggest Based On', store=False)
    suggest_days = fields.Integer(string='Suggest Days', store=False)
    suggest_percent = fields.Integer(string='Suggest Percent', store=False)
    sunday_location_id = fields.Many2one('hr.work.location', string='Sundays', store=False)
    supplier_invoice_count = fields.Integer(string='# Vendor Bills', store=False)
    supplier_rank = fields.Integer(string='Supplier Rank', store=False)
    thursday_location_id = fields.Many2one('hr.work.location', string='Thursdays', store=False)
    ticket_count = fields.Integer(string='Ticket Count', store=False)
    title = fields.Many2one('res.partner.title', string='Title', store=False)
    total_invoiced = fields.Monetary(string='Total Invoiced', store=False)
    totp_enabled = fields.Boolean(string='Two-factor authentication', store=False)
    totp_last_counter = fields.Integer(string='Totp Last Counter')
    totp_secret = fields.Char(string='Totp Secret', store=False)
    totp_trusted_device_ids = fields.One2many('auth_totp.device', 'user_id', string='Trusted Devices')
    tour_enabled = fields.Boolean(string='Onboarding')
    trust = fields.Selection(string='Degree of trust you have in this debtor', store=False, selection=[])
    tuesday_location_id = fields.Many2one('hr.work.location', string='Tuesdays', store=False)
    type = fields.Selection(string='Address Type', store=False, selection=[])
    type_address_label = fields.Char(string='Address Type Description', store=False)
    tz = fields.Selection(string='Timezone', store=False, selection=[], help='When printing documents and exporting/importing data, time values are computed according to this timezone. If the timezo')
    tz_offset = fields.Char(string='Timezone offset', store=False)
    use_partner_credit_limit = fields.Boolean(string='Partner Limit', store=False, help='Set a value greater than 0.0 to activate a credit limit check')
    user_id = fields.Many2one('res.users', string='Salesperson', store=False, help='The internal user in charge of this contact.')
    user_ids = fields.One2many('res.users', 'False', string='Users')
    user_line = fields.One2many('op.student', 'user_id', string='User Line')
    user_livechat_username = fields.Char(string='User Livechat Username', store=False)
    vat = fields.Char(string='Tax ID', store=False, help='The Tax Identification Number. Values here will be validated based on the country format. You can use \'/\' to indicate ')
    vat_label = fields.Char(string='Tax ID Label', store=False)
    view_group_hierarchy = fields.Json(string='Technical field for user group setting', store=False)
    visa_expire = fields.Date(string='Visa Expiration Date', store=False)
    visitor_ids = fields.One2many('website.visitor', 'False', string='Visitors')
    website = fields.Char(string='Website Link', store=False)
    website_absolute_url = fields.Char(string='Website Absolute URL', store=False, help='The full absolute URL to access the document through the website.')
    website_description = fields.Html(string='Website Partner Full Description', store=False)
    website_id = fields.Many2one('website', string='Website', help='Restrict to a specific website.')
    website_meta_description = fields.Text(string='Website meta description', store=False)
    website_meta_keywords = fields.Char(string='Website meta keywords', store=False)
    website_meta_og_img = fields.Char(string='Website opengraph image', store=False)
    website_meta_title = fields.Char(string='Website meta title', store=False)
    website_published = fields.Boolean(string='Visible on current website', store=False)
    website_short_description = fields.Text(string='Website Partner Short Description', store=False)
    website_url = fields.Char(string='Website URL', store=False, help='The full relative URL to access the document through the website.')
    wednesday_location_id = fields.Many2one('hr.work.location', string='Wednesdays', store=False)
    wishlist_ids = fields.One2many('product.wishlist', 'False', string='Wishlist')
    work_contact_id = fields.Many2one('res.partner', string='Work Contact', store=False)
    work_email = fields.Char(string='Work Email', store=False)
    work_location_id = fields.Many2one('hr.work.location', string='Work Location', store=False)
    work_location_name = fields.Char(string='Work Location Name', store=False)
    work_location_type = fields.Selection(string='Work Location Type', store=False, selection=[])
    work_phone = fields.Char(string='Work Phone', store=False)
    zip = fields.Char(string='Zip', store=False)

    # Mixin-inherited fields (not redeclared): activity_calendar_event_id, activity_date_deadline, activity_exception_decoration, activity_exception_icon, activity_ids, activity_state, activity_summary, activity_type_icon, activity_type_id, activity_user_id ...

    # Access Rights:
    #   Placement / User: read, write, create
    #   Parent / Manager: read, write, create, unlink
    #   Access Rights: read, write, create, unlink
    #   Role / Portal: read
    #   Role / Public: read
    #   Role / User: read

    # Record Rules:
    #   user rule: ['|', ('share', '=', False), ('company_ids', 'in', company_ids)]
    #   portal user access: [('commercial_partner_id', '=', user.commercial_partner_id.id)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_accesses_count(self):
        for rec in self:
            rec.accesses_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_account_move_count(self):
        for rec in self:
            rec.account_move_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_active_lang_count(self):
        for rec in self:
            rec.active_lang_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_active_partner(self):
        for rec in self:
            rec.active_partner = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_additional_note(self):
        for rec in self:
            rec.additional_note = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_application_count(self):
        for rec in self:
            rec.application_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_application_statistics(self):
        for rec in self:
            rec.application_statistics = False  # TODO: implement

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

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
