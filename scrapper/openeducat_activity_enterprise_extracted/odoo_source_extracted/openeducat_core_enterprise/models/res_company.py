# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class ResCompany(models.Model):
    """Companies

    Advanced orchestration layer for exchange rate management
    """

    _inherit = ['res.company', 'mail.thread', 'rating.mixin', 'website.published.mixin']
    _description = 'Companies'

    # ── Fields ──────────────────────────────────────────────
    account_cash_basis_base_account_id = fields.Many2one('account.account', string='Base Tax Received Account', help='Account that will be set on lines created in cash basis journal entry and used to keep track of the tax base amount.')
    account_default_pos_receivable_account_id = fields.Many2one('account.account', string='Default PoS Receivable Account')
    account_discount_expense_allocation_id = fields.Many2one('account.account', string='Separate account for expense discount')
    account_discount_income_allocation_id = fields.Many2one('account.account', string='Separate account for income discount')
    account_enabled_tax_country_ids = fields.Many2many('res.country', string='l10n-used countries', help='Technical field containing the countries for which this company is using tax-related features(hence the ones for which l')
    account_fiscal_country_group_codes = fields.Json(string='Account Fiscal Country Group Codes', store=False)
    account_fiscal_country_id = fields.Many2one('res.country', string='Fiscal Country', help='The country to use the tax reports from for this company')
    account_journal_early_pay_discount_gain_account_id = fields.Many2one('account.account', string='Cash Discount Write-Off Gain Account')
    account_journal_early_pay_discount_loss_account_id = fields.Many2one('account.account', string='Cash Discount Write-Off Loss Account')
    account_journal_suspense_account_id = fields.Many2one('account.account', string='Journal Suspense Account')
    account_opening_date = fields.Date(string='Opening Entry', help='That is the date of the opening entry.')
    account_opening_journal_id = fields.Many2one('account.journal', string='Opening Journal', store=False, help='Journal where the opening entry of this company\'s accounting has been posted.')
    account_opening_move_id = fields.Many2one('account.move', string='Opening Journal Entry', help='The journal entry containing the initial balance of all this company\'s accounts.')
    account_price_include = fields.Selection(string='Default Sales Price Include', required=True, selection=[], help='Default on whether the sales price used on the product and invoices with this Company includes its taxes.')
    account_production_wip_account_id = fields.Many2one('account.account', string='Production WIP Account')
    account_production_wip_overhead_account_id = fields.Many2one('account.account', string='Production WIP Overhead Account')
    account_purchase_receipt_fiscal_position_id = fields.Many2one('account.fiscal.position', string='Default Purchase Receipt Fiscal Position')
    account_purchase_tax_id = fields.Many2one('account.tax', string='Default Purchase Tax')
    account_sale_tax_id = fields.Many2one('account.tax', string='Default Sale Tax')
    account_stock_journal_id = fields.Many2one('account.journal', string='Stock Journal')
    account_stock_valuation_id = fields.Many2one('account.account', string='Stock Valuation Account')
    account_storno = fields.Boolean(string='Storno accounting')
    account_use_credit_limit = fields.Boolean(string='Sales Credit Limit', help='Enable the use of credit limit on partners.')
    accreditation = fields.Text(string='Accreditation')
    active = fields.Boolean(string='Active')
    affiliation_ids = fields.One2many('op.board.affiliation', 'company_id', string='Affiliation Board')
    alias_domain_id = fields.Many2one('mail.alias.domain', string='Email Domain')
    all_child_ids = fields.One2many('res.company', 'parent_id', string='All Child')
    anglo_saxon_accounting = fields.Boolean(string='Use anglo-saxon accounting')
    annual_inventory_day = fields.Integer(string='Day of the month', help='Day of the month when the annual inventory should occur. If zero or negative, then the first day of the month will be se')
    annual_inventory_month = fields.Selection(string='Annual Inventory Month', selection=[], help='Annual inventory month for products not in a location with a cyclic inventory date. Set to no month if no automatic annu')
    approval_authority = fields.Text(string='Approval Authority')
    automatic_entry_default_journal_id = fields.Many2one('account.journal', string='Automatic Entry Default Journal', help='Journal used by default for moving the period of an entry')
    autopost_bills = fields.Boolean(string='Auto-validate bills')
    bank_account_code_prefix = fields.Char(string='Prefix of the bank accounts')
    bank_ids = fields.One2many('res.partner.bank', 'False', string='Banks')
    bank_journal_ids = fields.One2many('account.journal', 'company_id', string='Bank Journals')
    batch_payment_sequence_id = fields.Many2one('ir.sequence', string='Batch Payment Sequence')
    bounce_email = fields.Char(string='Bounce Email', store=False)
    bounce_formatted = fields.Char(string='Bounce', store=False)
    cash_account_code_prefix = fields.Char(string='Prefix of the cash accounts')
    catchall_email = fields.Char(string='Catchall Email', store=False)
    catchall_formatted = fields.Char(string='Catchall', store=False)
    chart_template = fields.Selection(string='Chart Template', selection=[])
    child_company_count = fields.Integer(string='Child Company Count', store=False)
    child_ids = fields.One2many('res.company', 'parent_id', string='Branches')
    city = fields.Char(string='City', store=False)
    color = fields.Integer(string='Color Index', store=False)
    company_batch_count = fields.Integer(string='Company Batch Count', store=False)
    company_course_count = fields.Integer(string='Company Course Count', store=False)
    company_details = fields.Html(string='Company Details', help='Header text displayed at the top of all reports.')
    company_expense_allowed_payment_method_line_ids = fields.Many2many('account.payment.method.line', string='Payment methods available for expenses paid by company')
    company_registry = fields.Char(string='Company ID', store=False, help='The registry number of the company. Use it if it is different from the Tax ID. It must be unique across all partners of ')
    company_registry_placeholder = fields.Char(string='Company Registry Placeholder', store=False)
    company_student_count = fields.Integer(string='Company Student Count', store=False)
    company_subject_count = fields.Integer(string='Company Subject Count', store=False)
    company_vat_placeholder = fields.Char(string='Company Vat Placeholder', store=False)
    contract_expiration_notice_period = fields.Integer(string='Contract Expiry Notice Period')
    cost_method = fields.Selection(string='Cost Method', required=True, selection=[])
    country_code = fields.Char(string='Country Code', store=False, help='The ISO country code in two chars.  You can use this field for quick search.')
    country_id = fields.Many2one('res.country', string='Country', store=False)
    currency_exchange_journal_id = fields.Many2one('account.journal', string='Exchange Gain or Loss Journal')
    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    custom_bg_image = fields.Binary(string='Custom Background Image')
    dashboard_background = fields.Binary(string='Dashboard Background')
    days_to_purchase = fields.Float(string='Days to Purchase', help='Days needed to confirm a PO, define when a PO should be validated')
    default_cash_difference_expense_account_id = fields.Many2one('account.account', string='Cash Difference Expense')
    default_cash_difference_income_account_id = fields.Many2one('account.account', string='Cash Difference Income')
    default_from_email = fields.Char(string='Default From', store=False)
    display_account_storno = fields.Boolean(string='Display Account Storno', store=False)
    display_invoice_amount_total_words = fields.Boolean(string='Total amount of invoice in letters')
    display_invoice_tax_company_currency = fields.Boolean(string='Taxes in company currency')
    domestic_fiscal_position_id = fields.Many2one('account.fiscal.position', string='Domestic Fiscal Position')
    downpayment_account_id = fields.Many2one('account.account', string='Downpayment Account', help='This account will be used on Downpayment invoices.')
    email = fields.Char(string='Email')
    email_formatted = fields.Char(string='Formatted Email', store=False)
    email_primary_color = fields.Char(string='Email Button Text')
    email_secondary_color = fields.Char(string='Email Button Color')
    employee_properties_definition = fields.Char(string='Employee Properties')
    error_tolerance_threshold = fields.Float(string='Error Tolerance', help='Maximum acceptable rate variation before triggering validation alerts')
    expects_chart_of_accounts = fields.Boolean(string='Expects a Chart of Accounts')
    expense_account_id = fields.Many2one('account.account', string='Expense Account', help='The expense is accounted for when a vendor bill is validated, except in anglo-saxon accounting with perpetual inventory ')
    expense_accrual_account_id = fields.Many2one('account.account', string='Expense Accrual Account', help='Account used to move the period of an expense')
    expense_currency_exchange_account_id = fields.Many2one('account.account', string='Loss Exchange Rate Account')
    expense_journal_id = fields.Many2one('account.journal', string='Default Expense Journal', help='The company\'s default journal used when an employee expense is created.')
    external_report_layout_id = fields.Many2one('ir.ui.view', string='Document Template')
    fiscal_position_ids = fields.One2many('account.fiscal.position', 'company_id', string='Fiscal Position')
    fiscalyear_last_day = fields.Integer(string='Fiscalyear Last Day', required=True)
    fiscalyear_last_month = fields.Selection(string='Fiscalyear Last Month', required=True, selection=[])
    fiscalyear_lock_date = fields.Date(string='Global Lock Date', help='Any entry up to and including that date will be postponed to a later time, in accordance with its journal\'s sequence.')
    font = fields.Selection(string='Font', selection=[])
    force_restrictive_audit_trail = fields.Boolean(string='Force Audit Trail', store=False)
    google_font = fields.Char(string='Google Font')
    hard_lock_date = fields.Date(string='Hard Lock Date', help='Any entry up to and including that date will be postponed to a later time, in accordance with its journal sequence. This')
    has_received_warning_stock_sms = fields.Boolean(string='Has Received Warning Stock Sms')
    horizon_days = fields.Float(string='Replenishment Horizon', required=True, help='Configure your horizon to trigger reordering rules earlier to get                                 a head start on replen')
    hr_presence_control_attendance = fields.Boolean(string='Based on attendances')
    hr_presence_control_email = fields.Boolean(string='Based on number of emails sent')
    hr_presence_control_email_amount = fields.Integer(string='# emails to send')
    hr_presence_control_ip = fields.Boolean(string='Based on IP Address')
    hr_presence_control_ip_list = fields.Char(string='Valid IP addresses')
    hr_presence_control_login = fields.Boolean(string='Based on user status in system')
    iap_enrich_auto_done = fields.Boolean(string='Enrich Done')
    income_account_id = fields.Many2one('account.account', string='Income Account', help='This account will be used when validating a customer invoice.')
    income_currency_exchange_account_id = fields.Many2one('account.account', string='Gain Exchange Rate Account')
    incoterm_id = fields.Many2one('account.incoterms', string='Default incoterm', help='International Commercial Terms are a series of predefined commercial terms used in international transactions.')
    internal_transit_location_id = fields.Many2one('stock.location', string='Internal Transit Location')
    inventory_period = fields.Selection(string='Inventory Period', required=True, selection=[])
    inventory_valuation = fields.Selection(string='Valuation', selection=[])
    invoice_terms = fields.Html(string='Default Terms and Conditions')
    invoice_terms_html = fields.Html(string='Default Terms and Conditions as a Web page')
    is_company_details_empty = fields.Boolean(string='Is Company Details Empty', store=False)
    is_hash_verified = fields.Boolean(string='Is Hash Verified')
    is_mail_sent = fields.Boolean(string='Is Mail Sent')
    job_properties_definition = fields.Char(string='Job Properties')
    layout_background = fields.Selection(string='Layout Background', required=True, selection=[])
    layout_background_image = fields.Binary(string='Background Image')
    link_qr_code = fields.Boolean(string='Display Link QR-code')
    logo = fields.Binary(string='Company Logo', store=False)
    logo_web = fields.Binary(string='Logo Web')
    meeting_enterprise_onboard_panel = fields.Selection(string='State of the meeting onboarding step', selection=[])
    menu_bg_image = fields.Binary(string='Apps Menu Footer Image')
    multi_vat_foreign_country_ids = fields.Many2many('res.country', string='Foreign VAT countries', help='Countries for which the company has a VAT number')
    name = fields.Char(string='Company Name', required=True)
    next_execution_timestamp = fields.Datetime(string='Next Execution Time')
    nomenclature_id = fields.Many2one('barcode.nomenclature', string='Nomenclature')
    onboarding_meeting_layout_state = fields.Selection(string='State of the onboarding meeting layout  step', selection=[])
    openeducat_instance_hash_key = fields.Char(string='OpenEducat Instance Hash Key', help='Instance Hash key is correspondence to instance key which you get in mail.')
    openeducat_instance_hash_msg = fields.Char(string='Instance Hash Key Message')
    openeducat_instance_key = fields.Char(string='OpenEducat Instance Key')
    paperformat_id = fields.Many2one('report.paperformat', string='Paper format')
    parent_company_id = fields.Many2one('res.company', string='Company')
    parent_id = fields.Many2one('res.company', string='Parent Company')
    parent_ids = fields.Many2many('res.company', string='Parent')
    parent_path = fields.Char(string='Parent Path')
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    phone = fields.Char(string='Phone')
    po_double_validation = fields.Selection(string='Levels of Approvals', selection=[], help='Provide a double validation mechanism for purchases')
    po_double_validation_amount = fields.Monetary(string='Double validation amount', help='Minimum amount for which a double validation is required')
    po_lock = fields.Selection(string='Purchase Order Modification', selection=[], help='Purchase Order Modification used when you want to purchase order editable after confirm')
    portal_confirmation_pay = fields.Boolean(string='Online Payment')
    portal_confirmation_sign = fields.Boolean(string='Online Signature')
    preloader_option = fields.Selection(string='Preloader Option', selection=[])
    prepayment_percent = fields.Float(string='Prepayment percentage', help='The percentage of the amount needed to be paid to confirm quotations.')
    price_difference_account_id = fields.Many2one('account.account', string='Price Difference Account', help='During perpetual valuation, this account will hold the price difference between the standard price and the bill price.')
    primary_color = fields.Char(string='Primary Color')
    purchase_lock_date = fields.Date(string='Purchase Lock date', help='Any purchase entry prior to and including this date will be postponed to a later date, in accordance with its journal\'s')
    qr_code = fields.Boolean(string='Display QR-code on invoices')
    quick_edit_mode = fields.Selection(string='Quick encoding', selection=[])
    quotation_validity_days = fields.Integer(string='Default Quotation Validity', help='Days between quotation proposal and expiration. 0 days means automatic expiration is disabled')
    rate_provider_selection = fields.Selection(string='Exchange Rate Provider', selection=[])
    report_footer = fields.Html(string='Report Footer', help='Footer text displayed at the bottom of all reports.')
    report_header = fields.Html(string='Company Tagline', help='Company tagline, which is included in a printed document\'s header or footer (depending on the selected layout).')
    resource_calendar_id = fields.Many2one('resource.calendar', string='Default Working Hours')
    resource_calendar_ids = fields.One2many('resource.calendar', 'company_id', string='Working Hours')
    restrictive_audit_trail = fields.Boolean(string='Restrictive Audit Trail', help='Enable this option to prevent deletion of journal item related logs')
    revenue_accrual_account_id = fields.Many2one('account.account', string='Revenue Accrual Account', help='Account used to move the period of a revenue')
    root_id = fields.Many2one('res.company', string='Root', store=False)
    sale_discount_product_id = fields.Many2one('product.product', string='Discount Product', help='Default product used for discounts')
    sale_lock_date = fields.Date(string='Sales Lock Date', help='Any sales entry prior to and including this date will be postponed to a later date, in accordance with its journal\'s se')
    sale_onboarding_payment_method = fields.Selection(string='Sale onboarding selected payment method', selection=[])
    sale_order_template_id = fields.Many2one('sale.order.template', string='Default Sale Template')
    secondary_color = fields.Char(string='Secondary Color')
    security_lead = fields.Float(string='Sales Safety Days', required=True, help='Margin of error for dates promised to customers. Products will be scheduled for procurement and delivery that many days ')
    sequence = fields.Integer(string='Sequence', help='Used to order Companies in the company switcher')
    sidebar_bg_image = fields.Binary(string='Sidebar Background')
    sidebar_company_logo = fields.Binary(string='Sidebar Logo')
    signature = fields.Binary(string='Signature')
    snailmail_color = fields.Boolean(string='Snailmail Color')
    snailmail_cover = fields.Boolean(string='Add a Cover Page')
    snailmail_duplex = fields.Boolean(string='Both sides')
    social_discord = fields.Char(string='Discord Account')
    social_facebook = fields.Char(string='Facebook Account')
    social_github = fields.Char(string='GitHub Account')
    social_instagram = fields.Char(string='Instagram Account')
    social_linkedin = fields.Char(string='LinkedIn Account')
    social_tiktok = fields.Char(string='TikTok Account')
    social_twitter = fields.Char(string='X Account')
    social_youtube = fields.Char(string='Youtube Account')
    state_id = fields.Many2one('res.country.state', string='Fed. State', store=False)
    stock_confirmation_type = fields.Selection(string='Stock Confirmation Type', selection=[])
    stock_mail_confirmation_template_id = fields.Many2one('mail.template', string='Email Template confirmation picking', help='Email sent to the customer once the order is done.')
    stock_move_email_validation = fields.Boolean(string='Email Confirmation picking')
    stock_sms_confirmation_template_id = fields.Many2one('sms.template', string='SMS Template', help='SMS sent to the customer once the order is delivered.')
    stock_text_confirmation = fields.Boolean(string='Stock Text Confirmation')
    street = fields.Char(string='Street', store=False)
    street2 = fields.Char(string='Street2', store=False)
    synchronization_batch_size = fields.Integer(string='Batch Size', help='Number of currencies to process in each synchronization batch')
    synchronization_frequency = fields.Selection(string='Synchronization Frequency', selection=[])
    tax_calculation_rounding_method = fields.Selection(string='Tax Calculation Rounding Method', selection=[])
    tax_cash_basis_journal_id = fields.Many2one('account.journal', string='Cash Basis Journal')
    tax_exigibility = fields.Boolean(string='Use Cash Basis')
    tax_lock_date = fields.Date(string='Tax Return Lock Date', help='Any entry with taxes up to and including that date will be postponed to a later time, in accordance with its journal\'s ')
    terms_type = fields.Selection(string='Terms & Conditions format', selection=[])
    theme_background_color = fields.Char(string='Theme Background Color')
    theme_color_brand = fields.Char(string='Theme Brand Color')
    theme_font_name = fields.Selection(string='Select Font', selection=[])
    theme_menu_style = fields.Selection(string='Menu Style', selection=[])
    theme_sidebar_color = fields.Char(string='Theme Sidebar Color')
    theme_sidebar_text_color = fields.Char(string='Sidebar Text Color')
    transfer_account_code_prefix = fields.Char(string='Prefix of the transfer accounts')
    transfer_account_id = fields.Many2one('account.account', string='Inter-Banks Transfer Account', help='Intermediary account used when moving money from a liquidity account to another')
    uninstalled_l10n_module_ids = fields.Many2many('ir.module.module', string='Uninstalled L10N Module')
    user_fiscalyear_lock_date = fields.Date(string='User Fiscalyear Lock Date', store=False)
    user_hard_lock_date = fields.Date(string='User Hard Lock Date', store=False)
    user_ids = fields.Many2many('res.users', string='Accepted Users')
    user_purchase_lock_date = fields.Date(string='User Purchase Lock Date', store=False)
    user_sale_lock_date = fields.Date(string='User Sale Lock Date', store=False)
    user_tax_lock_date = fields.Date(string='User Tax Lock Date', store=False)
    uses_default_logo = fields.Boolean(string='Uses Default Logo')
    vat = fields.Char(string='Tax ID', store=False, help='The Tax Identification Number. Values here will be validated based on the country format. You can use \'/\' to indicate ')
    verify_date = fields.Char(string='Verify Date')
    website = fields.Char(string='Website Link', store=False)
    website_id = fields.Many2one('website', string='Website')
    work_permit_expiration_notice_period = fields.Integer(string='Work Permit Expiry Notice Period')
    zip = fields.Char(string='Zip', store=False)

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, has_message, id, message_attachment_count, message_follower_ids, message_has_error, message_has_error_counter, message_has_sms_error ...

    # Access Rights:
    #   Access Rights: read, write, create, unlink
    #   Role / Portal: read
    #   Role / Public: read
    #   Role / User: read

    # Record Rules:
    #   company rule portal: [('id','in', company_ids)]
    #   company rule employee: [('id','in', company_ids)]
    #   company rule public: [('id','in', company_ids)]
    #   company rule erp manager: [(1,'=',1)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_account_fiscal_country_group_codes(self):
        for rec in self:
            rec.account_fiscal_country_group_codes = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_account_opening_journal_id(self):
        for rec in self:
            rec.account_opening_journal_id = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_bounce_email(self):
        for rec in self:
            rec.bounce_email = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_bounce_formatted(self):
        for rec in self:
            rec.bounce_formatted = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_catchall_email(self):
        for rec in self:
            rec.catchall_email = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_catchall_formatted(self):
        for rec in self:
            rec.catchall_formatted = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_child_company_count(self):
        for rec in self:
            rec.child_company_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_city(self):
        for rec in self:
            rec.city = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_color(self):
        for rec in self:
            rec.color = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_company_batch_count(self):
        for rec in self:
            rec.company_batch_count = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
