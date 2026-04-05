# -*- coding: utf-8 -*-
# AUTO-GENERATED SKELETON — reconstructed from Odoo database metadata
# Real Python source lives on the server filesystem, not in the database.
# This skeleton reflects field definitions, mixins, ACL and record rules.

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class OpCourse(models.Model):
    """Course
    """

    _inherit = ['op.course', 'mail.thread', 'mail.activity.mixin', 'rating.mixin', 'website.published.mixin']
    _description = 'Course'

    # ── Fields ──────────────────────────────────────────────
    active = fields.Boolean(string='Active')
    admission_count = fields.Integer(string='Admission Count', store=False)
    allow_reviews = fields.Boolean(string='Allow Reviews')
    announcement_line = fields.One2many('op.course.announcement', 'course_id', string='Announcements')
    area_id = fields.Many2one('op.area', string='Area', store=False)
    assignment_count = fields.Integer(string='Assignment Count', store=False)
    avg_progress = fields.Float(string='Avg. Progress (%)')
    background = fields.Binary(string='Background Image')
    batch_count = fields.Integer(string='Batch Count', store=False)
    can_publish = fields.Boolean(string='Can Publish', store=False)
    category_ids = fields.Many2many('op.course.category', string='Categories')
    certi_date = fields.Boolean(string='Certificate Date')
    certi_title = fields.Char(string='Certificate Title')
    child_course_count = fields.Integer(string='Child Course Count', store=False)
    code = fields.Char(string='Code', required=True)
    color = fields.Integer(string='Color Index')
    company_id = fields.Many2one('res.company', string='Company')
    completion_count = fields.Integer(string='Completions')
    content_category_ids = fields.One2many('op.course.module', 'False', string='Content Modules')
    content_content_ids = fields.One2many('op.course.module', 'False', string='Content')
    course_change_fees = fields.Boolean(string='Course Change Fees')
    course_image = fields.Binary(string='Course Image')
    cover_properties = fields.Text(string='Cover Properties')
    credit = fields.Float(string='Course Credit')
    department_id = fields.Many2one('op.department', string='Department')
    description = fields.Html(string='Description')
    display_style = fields.Selection(string='Display Style', selection=[])
    enrollment_line = fields.One2many('op.course.enrollment', 'course_id', string='Enrollment')
    evaluation_type = fields.Selection(string='Evaluation Type', required=True, selection=[])
    faculty_count = fields.Integer(string='Faculty Count', store=False)
    faculty_ids = fields.Many2many('op.faculty', string='Instructor')
    fees_term_id = fields.Many2one('op.fees.terms', string='Fees Term')
    forum_count = fields.Integer(string='Forum Count')
    forum_id = fields.Many2one('forum.forum', string='Forum')
    forum_post_count = fields.Integer(string='Forum Post Count')
    forum_post_ids = fields.One2many('forum.post', 'course_id', string='Forum Post')
    forum_reply_count = fields.Integer(string='Forum Reply Count')
    full_description = fields.Html(string='Full Description')
    grade_scale_id = fields.Many2one('op.grade.scale', string='Final Grade')
    grade_template_ids = fields.Many2many('op.grade.template', string='Grade Template', required=True)
    image_1024 = fields.Binary(string='Image 1024')
    image_128 = fields.Binary(string='Image 128')
    image_1920 = fields.Binary(string='Image')
    image_256 = fields.Binary(string='Image 256')
    image_512 = fields.Binary(string='Image 512')
    invited_users_ids = fields.Many2many('res.users', string='Invited Users')
    is_certificate = fields.Boolean(string='Certificate Of Completion?')
    is_enroll_user = fields.Boolean(string='Enroll User')
    is_paid = fields.Boolean(string='Paid Course?')
    is_published = fields.Boolean(string='Is Published')
    list_price = fields.Float(string='Price', store=False, help='Price at which the product is sold to customers.')
    lms_course_count = fields.Char(string='LMS course count')
    lms_course_type = fields.Selection(string='Course type', required=True, selection=[])
    max_unit_load = fields.Float(string='Maximum Unit Load')
    min_unit_load = fields.Float(string='Minimum Unit Load')
    module_lines = fields.One2many('op.course.module', 'course_id', string='Module')
    name = fields.Char(string='Name', required=True)
    navigation_policy = fields.Selection(string='Navigation Policy', required=True, selection=[])
    notice_group_id = fields.Many2one('op.notice.group', string='Notice Group')
    online_course = fields.Boolean(string='Online Course')
    online_course_created = fields.Boolean(string='Online Course Created')
    parent_id = fields.Many2one('op.course', string='Parent Course')
    price = fields.Float(string='Computed Price', store=False, help='The sale price is managed from the product template. Click on the \'Configure Variants\' button to set the extra attribu')
    product_id = fields.Many2one('product.product', string='Product')
    program_id = fields.Many2one('op.program', string='Program')
    rating_avg_stars = fields.Float(string='Rating Average (Stars)', store=False)
    rating_avg_text = fields.Selection(string='Rating Avg Text', store=False, selection=[])
    rating_last_feedback = fields.Text(string='Rating Last Feedback', store=False)
    rating_last_image = fields.Binary(string='Rating Last Image', store=False)
    rating_last_text = fields.Selection(string='Rating Text', store=False, selection=[])
    rating_percentage_satisfaction = fields.Float(string='Rating Satisfaction', store=False)
    reg_fees = fields.Boolean(string='Registration Fees')
    sequence = fields.Integer(string='Sequence', help='Display order')
    short_desc = fields.Text(string='Short Description')
    specialization_id = fields.Many2one('op.specialization', string='Specialization')
    state = fields.Selection(string='State', selection=[])
    student_count = fields.Integer(string='Student Count', store=False)
    subject_count = fields.Integer(string='Subject Count', store=False)
    subject_counts = fields.Integer(string='Subject Counts', store=False)
    subject_ids = fields.Many2many('op.subject', string='Subject(s)')
    subject_selection_option = fields.Selection(string='Subject Selection', selection=[])
    suggested_course_ids = fields.Many2many('op.course', string='Suggested Course')
    survey_ids = fields.One2many('survey.survey', 'course_id', string='Survey')
    tag_ids = fields.Many2many('op.course.tag', string='Tags')
    timetable_count = fields.Integer(string='Timetable Count', store=False)
    timing_course_count = fields.Integer(string='Timing Course Count', store=False)
    total_enrollment = fields.Integer(string='Total Enrollment')
    total_modules = fields.Integer(string='Number of Contents')
    total_time = fields.Float(string='Duration')
    user_id = fields.Many2one('res.users', string='Responsible')
    visibility = fields.Selection(string='Visibility Policy', required=True, selection=[], help='Defines who can access your courses and their content.')
    website_absolute_url = fields.Char(string='Website Absolute URL', store=False, help='The full absolute URL to access the document through the website.')
    website_id = fields.Many2one('website', string='Website', help='Restrict to a specific website.')
    website_published = fields.Boolean(string='Visible on current website', store=False)
    website_url = fields.Char(string='Website URL', store=False, help='The full relative URL to access the document through the website.')

    # Mixin-inherited fields (not redeclared): activity_calendar_event_id, activity_date_deadline, activity_exception_decoration, activity_exception_icon, activity_ids, activity_state, activity_summary, activity_type_icon, activity_type_id, activity_user_id ...

    # Access Rights:
    #   OpenEduCat / Manager: read, write, create, unlink
    #   OpenEduCat / User: read, write, create
    #   Library / Manager: read
    #   LMS / Manager: read, write, create, unlink
    #   LMS / User: read, write, create
    #   Role / Portal: read, write
    #   Role / Portal: read
    #   Role / Public: read
    #   Role / Public: read

    # Record Rules:
    #   Course multi-company: ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]
    #   Course multi-department: ['|','|',('department_id','=',False),('department_id','child_of',[user.dept_id.id]),('department_id','in',user.department_ids.ids)]
    #   course multi-company: ['|',('company_id','=',False),'&',('company_id','in',company_ids),'|',('company_id','child_of',[user.company_id.id]),('company_id','in',user.company_ids.ids)]

    # ── Computed / onchange methods (reconstructed stubs) ───────────

    @api.depends()  # TODO: add real dependencies
    def _compute_admission_count(self):
        for rec in self:
            rec.admission_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_area_id(self):
        for rec in self:
            rec.area_id = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_assignment_count(self):
        for rec in self:
            rec.assignment_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_batch_count(self):
        for rec in self:
            rec.batch_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_can_publish(self):
        for rec in self:
            rec.can_publish = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_child_course_count(self):
        for rec in self:
            rec.child_course_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_faculty_count(self):
        for rec in self:
            rec.faculty_count = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_list_price(self):
        for rec in self:
            rec.list_price = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_price(self):
        for rec in self:
            rec.price = False  # TODO: implement

    @api.depends()  # TODO: add real dependencies
    def _compute_rating_avg_stars(self):
        for rec in self:
            rec.rating_avg_stars = False  # TODO: implement

    # ── CRUD overrides (if any) ──────────────────────────────────────

    # def create(self, vals):
    #     return super().create(vals)

    # def write(self, vals):
    #     return super().write(vals)

    # ── Business logic ───────────────────────────────────────────────

    # TODO: add action methods found in ir.actions.server for this model
