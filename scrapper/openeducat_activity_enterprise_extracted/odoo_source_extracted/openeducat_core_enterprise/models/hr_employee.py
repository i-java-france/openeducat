# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class HrEmployee(models.Model):
    """Employee

    NB: Any field only available on the model hr.employee (i.e. not on the
    hr.employee.public model) should have `groups="hr.group_hr_user"` on its
    definition to avoid being prefetched when the user hasn't access to the
    hr.employee model. Indeed, the prefetch loads the data for all the fields
    that are available according to the group defined on them.
    """

    _inherit = ['hr.employee', 'mail.thread', 'mail.activity.mixin', 'rating.mixin', 'website.published.mixin']
    _description = 'Employee'

    # ── Fields ──────────────────────────────────────────────
    active = fields.Boolean(string='Active', help='If the active field is set to False, it will allow you to hide the resource record without removing it.')
    active_employee = fields.Boolean(string='Active Employee', store=False, help='If the active field is set to False, it will allow you to hide the resource record without removing it.')
    additional_note = fields.Text(string='Additional Note', store=False)
    address_id = fields.Many2one('res.partner', string='Work Address', store=False)
    allocation_count = fields.Float(string='Total number of days allocated.', store=False)
    allocation_display = fields.Char(string='Allocation Display', store=False)
    allocation_remaining_display = fields.Char(string='Allocation Remaining Display', store=False)
    allocations_count = fields.Integer(string='Total number of allocations', store=False)
    allowed_country_state_ids = fields.Many2many('res.country.state', string='Allowed Country State')
    applicant_ids = fields.One2many('hr.applicant', 'employee_id', string='Applicants')
    avatar_1024 = fields.Binary(string='Avatar 1024', store=False)
    avatar_128 = fields.Binary(string='Avatar 128', store=False)
    avatar_1920 = fields.Binary(string='Avatar', store=False)
    avatar_256 = fields.Binary(string='Avatar 256', store=False)
    avatar_512 = fields.Binary(string='Avatar 512', store=False)
    badge_ids = fields.One2many('gamification.badge.user', 'False', string='Employee Badges', help='All employee badges, linked to the employee either directly or through the user')
    bank_account_ids = fields.Many2many('res.partner.bank', string='Bank Accounts', help='Employee bank accounts to pay salaries')
    barcode = fields.Char(string='Badge ID', help='ID used for employee identification.')
    birthday = fields.Date(string='Birthday')
    birthday_public_display = fields.Boolean(string='Show to all employees')
    birthday_public_display_string = fields.Char(string='Public Date of Birth', store=False)
    car_ids = fields.One2many('fleet.vehicle', 'driver_employee_id', string='Vehicles (private)')
    category_ids = fields.Many2many('hr.employee.category', string='Tags')
    certificate = fields.Selection(string='Certificate Level', selection=[])
    certification_ids = fields.One2many('hr.employee.skill', 'False', string='Certification')
    child_all_count = fields.Integer(string='Indirect Subordinates Count', store=False)
    child_count = fields.Integer(string='Direct Subordinates Count', store=False)
    child_ids = fields.One2many('hr.employee', 'parent_id', string='Direct subordinates')
    children = fields.Integer(string='Dependent Children', store=False)
    coach_id = fields.Many2one('hr.employee', string='Coach', help='Select the "Employee" who is the coach of this employee. The "Coach" has no specific rights or responsibilities by defau')
    color = fields.Integer(string='Color Index')
    company_country_code = fields.Char(string='Company Country Code', store=False, help='The ISO country code in two chars.  You can use this field for quick search.')
    company_country_id = fields.Many2one('res.country', string='Company Country', store=False)
    company_id = fields.Many2one('res.company', string='Company', required=True)
    contract_date_end = fields.Date(string='Contract End Date', store=False, help='End date of the contract (if it\'s a fixed-term contract).')
    contract_date_start = fields.Date(string='Contract Start Date', store=False)
    contract_template_id = fields.Many2one('hr.version', string='Contract Template', store=False, help='Select a contract template to auto-fill the contract form with predefined values. You can still edit the fields as neede')
    contract_type_id = fields.Many2one('hr.contract.type', string='Contract Type', store=False)
    contract_wage = fields.Monetary(string='Contract Wage', store=False)
    country_code = fields.Char(string='Country Code', store=False, help='The ISO country code in two chars.  You can use this field for quick search.')
    country_id = fields.Many2one('res.country', string='Nationality (Country)', store=False)
    country_of_birth = fields.Many2one('res.country', string='Country of Birth')
    currency_id = fields.Many2one('res.currency', string='Currency', store=False)
    current_date_version = fields.Date(string='Current Date Version', store=False)
    current_employee_skill_ids = fields.One2many('hr.employee.skill', 'False', string='Current Employee Skill')
    current_leave_id = fields.Many2one('hr.leave.type', string='Current Time Off Type', store=False)
    current_leave_state = fields.Selection(string='Current Time Off Status', store=False, selection=[])
    current_version_id = fields.Many2one('hr.version', string='Current Version')
    date_end = fields.Date(string='Date End', store=False)
    date_start = fields.Date(string='Date Start', store=False)
    date_version = fields.Date(string='Date Version', required=True, store=False)
    department_color = fields.Integer(string='Department Color', store=False)
    department_id = fields.Many2one('hr.department', string='Department', store=False)
    departure_date = fields.Date(string='Departure Date', store=False)
    departure_description = fields.Html(string='Additional Information', store=False)
    departure_reason_id = fields.Many2one('hr.departure.reason', string='Departure Reason', store=False)
    direct_badge_ids = fields.One2many('gamification.badge.user', 'employee_id', string='Direct Badge', help='Badges directly linked to the employee')
    display_certification_page = fields.Boolean(string='Display Certification Page', store=False)
    distance_home_work = fields.Integer(string='Home-Work Distance', store=False)
    distance_home_work_unit = fields.Selection(string='Home-Work Distance unit', required=True, store=False, selection=[])
    driving_license = fields.Binary(string='Driving License')
    email = fields.Char(string='Email', store=False)
    emergency_contact = fields.Char(string='Emergency Contact')
    emergency_phone = fields.Char(string='Emergency Phone')
    employee_cars_count = fields.Integer(string='Cars', store=False)
    employee_id = fields.Many2one('hr.employee', string='Employee', store=False)
    employee_properties = fields.Properties(string='Properties')
    employee_skill_ids = fields.One2many('hr.employee.skill', 'employee_id', string='Skills')
    employee_type = fields.Selection(string='Employee Type', required=True, store=False, selection=[])
    exceptional_location_id = fields.Many2one('hr.work.location', string='Current', store=False, help='This is the exceptional, non-weekly, location set for today.')
    expense_manager_id = fields.Many2one('res.users', string='Expense Approver', help='Select the user responsible for approving "Expenses" of this employee. If empty, the approval is done by an Administrato')
    filter_for_expense = fields.Boolean(string='Filter For Expense', store=False)
    friday_location_id = fields.Many2one('hr.work.location', string='Friday')
    goal_ids = fields.One2many('gamification.goal', 'False', string='Employee HR Goals')
    has_badges = fields.Boolean(string='Has Badges', store=False)
    has_multiple_bank_accounts = fields.Boolean(string='Has Multiple Bank Accounts', store=False)
    has_work_permit = fields.Binary(string='Work Permit')
    hr_icon_display = fields.Selection(string='Hr Icon Display', store=False, selection=[])
    hr_presence_state = fields.Selection(string='Hr Presence State', store=False, selection=[])
    hr_responsible_id = fields.Many2one('res.users', string='HR Responsible', required=True, store=False, help='Person responsible for validating the employee\'s contracts.')
    id_card = fields.Binary(string='ID Card Copy')
    identification_id = fields.Char(string='Identification No', store=False, help='Enter the employee\'s National Identification Number issued by the government (e.g., Aadhaar, SIN, NIN). This is used fo')
    im_status = fields.Char(string='IM Status', store=False)
    image_1024 = fields.Binary(string='Image 1024')
    image_128 = fields.Binary(string='Image 128')
    image_1920 = fields.Binary(string='Image')
    image_256 = fields.Binary(string='Image 256')
    image_512 = fields.Binary(string='Image 512')
    is_absent = fields.Boolean(string='Absent Today', store=False)
    is_current = fields.Boolean(string='Is Current', store=False)
    is_custom_job_title = fields.Boolean(string='Is Custom Job Title', store=False)
    is_flexible = fields.Boolean(string='Is Flexible', store=False)
    is_fully_flexible = fields.Boolean(string='Is Fully Flexible', store=False)
    is_future = fields.Boolean(string='Is Future', store=False)
    is_in_contract = fields.Boolean(string='Is In Contract', store=False)
    is_past = fields.Boolean(string='Is Past', store=False)
    is_subordinate = fields.Boolean(string='Is Subordinate', store=False)
    is_trusted_bank_account = fields.Boolean(string='Is Trusted Bank Account', store=False)
    is_user_active = fields.Boolean(string='User's active', store=False)
    job_id = fields.Many2one('hr.job', string='Job', store=False)
    job_title = fields.Char(string='Job Title', store=False)
    km_home_work = fields.Integer(string='Home-Work Distance in Km', store=False)
    lang = fields.Selection(string='Lang', selection=[])
    last_activity = fields.Date(string='Last Activity', store=False)
    last_activity_time = fields.Char(string='Last Activity Time', store=False)
    last_modified_date = fields.Datetime(string='Last Modified on', required=True, store=False)
    last_modified_uid = fields.Many2one('res.users', string='Last Modified by', required=True, store=False)
    leave_date_from = fields.Date(string='From Date', store=False)
    leave_date_to = fields.Date(string='To Date', store=False)
    leave_manager_id = fields.Many2one('res.users', string='Time Off Approver', help='Select the user responsible for approving "Time Off" of this employee. If empty, the approval is done by an Administrato')
    legal_name = fields.Char(string='Legal Name')
    license_plate = fields.Char(string='License Plate', store=False)
    marital = fields.Selection(string='Marital Status', required=True, store=False, selection=[])
    member_of_department = fields.Boolean(string='Member of department', store=False, help='Whether the employee is a member of the active user\'s department or one of it\'s child department.')
    message_main_attachment_id = fields.Many2one('ir.attachment', string='Main Attachment')
    mobile_phone = fields.Char(string='Work Mobile')
    mobility_card = fields.Char(string='Mobility Card')
    monday_location_id = fields.Many2one('hr.work.location', string='Monday')
    name = fields.Char(string='Employee Name')
    newly_hired = fields.Boolean(string='Newly Hired', store=False)
    parent_id = fields.Many2one('hr.employee', string='Manager')
    passport_expiration_date = fields.Date(string='Passport Expiration Date', store=False)
    passport_id = fields.Char(string='Passport No', store=False)
    permit_no = fields.Char(string='Work Permit No')
    phone = fields.Char(string='Phone', store=False)
    pin = fields.Char(string='PIN', help='PIN used to Check In/Out in the Kiosk Mode of the Attendance application (if enabled in Configuration) and to change the')
    place_of_birth = fields.Char(string='Place of Birth')
    primary_bank_account_id = fields.Many2one('res.partner.bank', string='Primary Bank Account', store=False)
    private_car_plate = fields.Char(string='Private Car Plate', help='If you have more than one car, just separate the plates by a space.')
    private_city = fields.Char(string='Private City', store=False)
    private_country_id = fields.Many2one('res.country', string='Private Country', store=False)
    private_email = fields.Char(string='Private Email')
    private_phone = fields.Char(string='Private Phone')
    private_state_id = fields.Many2one('res.country.state', string='Private State', store=False)
    private_street = fields.Char(string='Private Street', store=False)
    private_street2 = fields.Char(string='Private Street2', store=False)
    private_zip = fields.Char(string='Private Zip', store=False)
    related_partners_count = fields.Integer(string='Related Partners Count', store=False)
    resource_calendar_id = fields.Many2one('resource.calendar', string='Default Working Hours', store=False, help='Working hour of week')
    resource_id = fields.Many2one('resource.resource', string='Resource', required=True)
    resume_line_ids = fields.One2many('hr.resume.line', 'employee_id', string='Resume lines')
    salary_distribution = fields.Json(string='Salary Distribution')
    saturday_location_id = fields.Many2one('hr.work.location', string='Saturday')
    sex = fields.Selection(string='Gender', store=False, selection=[], help='This is the legal sex recognized by the state.')
    share = fields.Boolean(string='Share User', store=False, help='External user with limited access, created only for the purpose of sharing data.')
    show_hr_icon_display = fields.Boolean(string='Show Hr Icon Display', store=False)
    show_leaves = fields.Boolean(string='Able to see Remaining Time Off', store=False)
    skill_ids = fields.Many2many('hr.skill', string='Skill')
    spouse_birthdate = fields.Date(string='Spouse Birthdate', store=False)
    spouse_complete_name = fields.Char(string='Spouse Legal Name', store=False)
    ssnid = fields.Char(string='SSN No', store=False, help='Social Security Number')
    structure_type_id = fields.Many2one('hr.payroll.structure.type', string='Salary Structure Type', store=False)
    study_field = fields.Char(string='Field of Study')
    study_school = fields.Char(string='School')
    subordinate_ids = fields.One2many('hr.employee', 'False', string='Subordinates', help='Direct and indirect subordinates')
    sunday_location_id = fields.Many2one('hr.work.location', string='Sunday')
    thursday_location_id = fields.Many2one('hr.work.location', string='Thursday')
    today_location_name = fields.Char(string='Today Location Name')
    trial_date_end = fields.Date(string='End of Trial Period', store=False, help='End date of the trial period (if there is one).')
    tuesday_location_id = fields.Many2one('hr.work.location', string='Tuesday')
    tz = fields.Selection(string='Timezone', store=False, selection=[], help='This field is used in order to define in which timezone the resources will work.')
    user_id = fields.Many2one('res.users', string='User', help='Related user name for the resource to manage its access.')
    user_partner_id = fields.Many2one('res.partner', string='User's partner', store=False, help='Partner-related data of the user')
    version_id = fields.Many2one('hr.version', string='Version', required=True, store=False)
    version_ids = fields.One2many('hr.version', 'employee_id', string='Employee Versions', required=True)
    versions_count = fields.Integer(string='Versions Count', store=False)
    visa_expire = fields.Date(string='Visa Expiration Date')
    visa_no = fields.Char(string='Visa No')
    wage = fields.Monetary(string='Wage', store=False, help='Employee\'s monthly gross wage.')
    wednesday_location_id = fields.Many2one('hr.work.location', string='Wednesday')
    work_contact_id = fields.Many2one('res.partner', string='Work Contact')
    work_email = fields.Char(string='Work Email')
    work_location_id = fields.Many2one('hr.work.location', string='Work Location', store=False)
    work_location_name = fields.Char(string='Work Location Name', store=False)
    work_location_type = fields.Selection(string='Work Location Type', store=False, selection=[])
    work_permit_expiration_date = fields.Date(string='Work Permit Expiration Date')
    work_permit_name = fields.Char(string='work_permit_name', store=False)
    work_permit_scheduled_activity = fields.Boolean(string='Work Permit Scheduled Activity')
    work_phone = fields.Char(string='Work Phone')

    # Mixin-inherited fields (not redeclared): activity_calendar_event_id, activity_date_deadline, activity_exception_decoration, activity_exception_icon, activity_ids, activity_state, activity_summary, activity_type_icon, activity_type_id, activity_user_id ...

    # Access Rights:
    #   Employees / Officer: Manage all employees: read, write, create, unlink
    #   OpenEduCat / Manager: read, write, create
    #   OpenEduCat / Manager: read
    #   Role / Administrator: read

    # Record Rules:
    #   Employee multi company rule: ['|', '|', '|',
            ('company_id', 'in', company_ids + [False]),
            ('parent_id.user_id', '=', user.id),
            ('id', '=', user.employee_id.parent_id.id),
            ('user_id', '=', user.id)
        ]
    #   HR multi-company: ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_active_employee(self):
        for rec in self:
            rec.active_employee = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_additional_note(self):
        for rec in self:
            rec.additional_note = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_address_id(self):
        for rec in self:
            rec.address_id = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_allocation_count(self):
        for rec in self:
            rec.allocation_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_allocation_display(self):
        for rec in self:
            rec.allocation_display = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_allocation_remaining_display(self):
        for rec in self:
            rec.allocation_remaining_display = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_allocations_count(self):
        for rec in self:
            rec.allocations_count = False  # TODO: implement

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
