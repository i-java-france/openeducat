# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class Website(models.Model):
    """Website
    """

    _name = 'website'
    _description = 'Website'

    # ── Fields ──────────────────────────────────────────────
    account_on_checkout = fields.Selection(string='Customer Accounts', selection=[])
    add_to_cart_action = fields.Selection(string='Add To Cart Action', selection=[])
    auth_signup_uninvited = fields.Selection(string='Customer Account', selection=[])
    auto_redirect_lang = fields.Boolean(string='Autoredirect Language', help='Should users be redirected to their browser\'s language')
    block_third_party_domains = fields.Boolean(string='Block 3rd-party domains', help='Block 3rd-party domains that may track users (YouTube, Google Maps, etc.).')
    blocked_third_party_domains = fields.Text(string='List of blocked 3rd-party domains', store=False)
    cart_abandoned_delay = fields.Float(string='Abandoned Delay')
    cart_recovery_mail_template_id = fields.Many2one('mail.template', string='Cart Recovery Email')
    cdn_activated = fields.Boolean(string='Content Delivery Network (CDN)')
    cdn_filters = fields.Text(string='CDN Filters', help='URL matching those filters will be rewritten using the CDN Base URL')
    cdn_url = fields.Char(string='CDN Base URL')
    channel_id = fields.Many2one('im_livechat.channel', string='Website Live Chat Channel')
    company_id = fields.Many2one('res.company', string='Company', required=True)
    configurator_done = fields.Boolean(string='Configurator Done', help='True if configurator has been completed or ignored')
    confirmation_email_template_id = fields.Many2one('mail.template', string='Confirmation Email Template')
    contact_us_button_url = fields.Char(string='Contact Us Button URL')
    cookies_bar = fields.Boolean(string='Cookies Bar', help='Display a customizable cookies bar on your website.')
    crm_default_team_id = fields.Many2one('crm.team', string='Default Sales Teams', help='Default Sales Team for new leads created through the Contact Us form.')
    crm_default_user_id = fields.Many2one('res.users', string='Default Salesperson', help='Default salesperson for new leads created through the Contact Us form.')
    currency_id = fields.Many2one('res.currency', string='Default Currency', store=False)
    custom_blocked_third_party_domains = fields.Text(string='User list of blocked 3rd-party domains')
    custom_code_footer = fields.Html(string='Custom end of <body> code')
    custom_code_head = fields.Html(string='Custom <head> code')
    default_lang_id = fields.Many2one('res.lang', string='Default Language', required=True)
    domain = fields.Char(string='Website Domain', help='E.g. https://www.mydomain.com')
    domain_punycode = fields.Char(string='Punycode Domain', store=False)
    ecommerce_access = fields.Selection(string='Ecommerce Access', required=True, selection=[])
    enabled_gmc_src = fields.Boolean(string='Google Merchant Center')
    favicon = fields.Binary(string='Website Favicon', help='This field holds the image used to display a favicon on the website.')
    forum_count = fields.Integer(string='Forum Count')
    google_analytics_key = fields.Char(string='Google Analytics Key')
    google_maps_api_key = fields.Char(string='Google Maps API Key')
    google_search_console = fields.Char(string='Google Search Console', help='Google key, or Enable to access first reply')
    has_social_default_image = fields.Boolean(string='Has Social Default Image')
    homepage_url = fields.Char(string='Homepage Url', help='E.g. /contactus or /shop')
    karma_profile_min = fields.Integer(string='Minimal karma to see other user's profile')
    language_count = fields.Integer(string='Number of languages', store=False)
    language_ids = fields.Many2many('res.lang', string='Languages', required=True)
    logo = fields.Binary(string='Website Logo', help='Display this logo on the website.')
    menu_id = fields.Many2one('website.menu', string='Main Menu', store=False)
    name = fields.Char(string='Website Name', required=True)
    newsletter_id = fields.Many2one('mailing.list', string='Newsletter List')
    partner_id = fields.Many2one('res.partner', string='Public Partner', store=False, help='Partner-related data of the user')
    plausible_shared_key = fields.Char(string='Plausible Shared Key')
    plausible_site = fields.Char(string='Plausible Site')
    prevent_zero_price_sale = fields.Boolean(string='Hide 'Add To Cart' when price = 0')
    pricelist_ids = fields.One2many('product.pricelist', 'False', string='Price list available for this Ecommerce/Website')
    product_page_cols_order = fields.Selection(string='Product Page main columns order', selection=[])
    product_page_container = fields.Selection(string='Product Page Container', selection=[])
    product_page_grid_columns = fields.Integer(string='Product Page Grid Columns')
    product_page_image_layout = fields.Selection(string='Product Page Image Layout', required=True, selection=[])
    product_page_image_ratio = fields.Selection(string='Product Page Image Ratio', required=True, selection=[])
    product_page_image_ratio_mobile = fields.Selection(string='Product Page Image Ratio Mobile', required=True, selection=[])
    product_page_image_roundness = fields.Selection(string='Product Page Image Roundness', required=True, selection=[])
    product_page_image_spacing = fields.Selection(string='Product Page Image Spacing', required=True, selection=[])
    product_page_image_width = fields.Selection(string='Product Page Image Width', required=True, selection=[])
    robots_txt = fields.Html(string='Robots.txt')
    salesperson_id = fields.Many2one('res.users', string='Salesperson')
    salesteam_id = fields.Many2one('crm.team', string='Sales Team')
    send_abandoned_cart_email = fields.Boolean(string='Send email to customers who abandoned their cart.')
    send_abandoned_cart_email_activation_time = fields.Datetime(string='Time when the 'Send abandoned cart email' feature was activated.')
    sequence = fields.Integer(string='Sequence')
    shop_default_sort = fields.Selection(string='Shop Default Sort', required=True, selection=[])
    shop_extra_field_ids = fields.One2many('website.sale.extra.field', 'website_id', string='E-Commerce Extra Fields')
    shop_gap = fields.Char(string='Grid-gap on the shop')
    shop_opt_products_design_classes = fields.Char(string='Shop Design Class', help='CSS class for shop products design')
    shop_page_container = fields.Selection(string='Shop Page Container', selection=[])
    shop_ppg = fields.Integer(string='Number of products in the grid on the shop')
    shop_ppr = fields.Integer(string='Number of grid columns on the shop')
    show_line_subtotals_tax_selection = fields.Selection(string='Line Subtotals Tax Display', selection=[])
    social_default_image = fields.Binary(string='Default Social Share Image', help='If set, replaces the website logo as the default social share image.')
    social_discord = fields.Char(string='Discord Account')
    social_facebook = fields.Char(string='Facebook Account')
    social_github = fields.Char(string='GitHub Account')
    social_instagram = fields.Char(string='Instagram Account')
    social_linkedin = fields.Char(string='LinkedIn Account')
    social_tiktok = fields.Char(string='TikTok Account')
    social_twitter = fields.Char(string='X Account')
    social_youtube = fields.Char(string='Youtube Account')
    specific_user_account = fields.Boolean(string='Specific User Account', help='If True, new accounts will be associated to the current website')
    theme_id = fields.Many2one('ir.module.module', string='Theme', help='Installed theme')
    user_id = fields.Many2one('res.users', string='Public User', required=True)
    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse')
    wishlist_gap = fields.Char(string='Wishlist Grid Gap', help='Gap between products on the wishlist page')
    wishlist_grid_columns = fields.Integer(string='Wishlist Grid Columns', help='Number of columns to display on the wishlist page')
    wishlist_mobile_columns = fields.Integer(string='Wishlist Mobile Columns', help='Number of columns to display on mobile for the wishlist page (1 or 2)')
    wishlist_opt_products_design_classes = fields.Char(string='Wishlist Page Design Class', help='CSS class for wishlist page design')

    # Mixin-inherited fields (not redeclared): create_date, create_uid, display_name, id, write_date, write_uid

    # Access Rights:
    #   Website / Editor and Designer: read, write, create, unlink
    #   Role / Portal: read
    #   Role / Public: read
    #   Role / User: read

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_blocked_third_party_domains(self):
        for rec in self:
            rec.blocked_third_party_domains = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_currency_id(self):
        for rec in self:
            rec.currency_id = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_domain_punycode(self):
        for rec in self:
            rec.domain_punycode = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_language_count(self):
        for rec in self:
            rec.language_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_menu_id(self):
        for rec in self:
            rec.menu_id = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_partner_id(self):
        for rec in self:
            rec.partner_id = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
