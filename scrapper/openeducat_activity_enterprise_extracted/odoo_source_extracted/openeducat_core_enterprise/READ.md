# 🐍 OpenEduCat Core Enterprise — Python Skeleton

**Module:** `openeducat_core_enterprise`
**Generated from:** Odoo database metadata (ir.model, ir.model.fields, ir.rule, ir.model.access)

## ⚠️ Important Notes

- This is a **reconstructed skeleton** — not the original source code
- Field definitions are accurate (name, type, required, relation, store)
- Mixin detection (mail.thread, activity.mixin) is based on field presence
- Computed field stubs are generated but logic is **not** recoverable from DB
- `_sql_constraints`, `@api.constrains`, `@api.onchange` must be added manually
- Controller routes (`/web`, `http.route`) are **not** in the DB — add manually

## Structure

```
openeducat_core_enterprise/
├── __manifest__.py     ← reconstructed from module metadata
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── op_academic_plan_stages.py
│   ├── calendar_event.py
│   ├── res_company.py
│   ├── op_course.py
│   ├── op_course_plan.py
│   ├── hr_employee.py
│   ├── op_academic_plan.py
│   ├── op_area.py
│   ├── op_batch.py
│   ├── op_faculty.py
│   ├── op_intake_year.py
│   ├── op_specialization.py
│   ├── op_student.py
│   ├── op_student_course.py
│   ├── op_subject.py
│   ├── op_subject_registration.py
│   ├── op_program.py
│   ├── op_assessment_type.py
│   ├── op_badge_student_wizard.py
│   ├── op_board_affiliation.py
│   ├── res_config_settings.py
│   ├── op_course_category.py
│   ├── wizard_course_allocation.py
│   ├── op_gamification_badge.py
│   ├── op_badge_student.py
│   ├── op_marks_line.py
│   ├── ir_module_module.py
│   ├── onboarding_onboarding.py
│   ├── onboarding_onboarding_step.py
│   ├── op_department.py
│   ├── publisher_warranty_contract.py
│   ├── op_section.py
│   ├── op_subject_faculty.py
│   ├── op_topics.py
│   ├── res_users.py
│   ├── website.py
│   ├── website_configurator_feature.py
└── controllers/
    └── __init__.py     ← placeholder only
```

## Models (37)

| Model | Class | Fields |
|-------|-------|--------|
| `op.academic.plan.stages` | `OpAcademicPlanStages` | see file |
| `calendar.event` | `CalendarEvent` | see file |
| `res.company` | `ResCompany` | see file |
| `op.course` | `OpCourse` | see file |
| `op.course.plan` | `OpCoursePlan` | see file |
| `hr.employee` | `HrEmployee` | see file |
| `op.academic.plan` | `OpAcademicPlan` | see file |
| `op.area` | `OpArea` | see file |
| `op.batch` | `OpBatch` | see file |
| `op.faculty` | `OpFaculty` | see file |
| `op.intake.year` | `OpIntakeYear` | see file |
| `op.specialization` | `OpSpecialization` | see file |
| `op.student` | `OpStudent` | see file |
| `op.student.course` | `OpStudentCourse` | see file |
| `op.subject` | `OpSubject` | see file |
| `op.subject.registration` | `OpSubjectRegistration` | see file |
| `op.program` | `OpProgram` | see file |
| `op.assessment.type` | `OpAssessmentType` | see file |
| `op.badge.student.wizard` | `OpBadgeStudentWizard` | see file |
| `op.board.affiliation` | `OpBoardAffiliation` | see file |
| `res.config.settings` | `ResConfigSettings` | see file |
| `op.course.category` | `OpCourseCategory` | see file |
| `wizard.course.allocation` | `WizardCourseAllocation` | see file |
| `op.gamification.badge` | `OpGamificationBadge` | see file |
| `op.badge.student` | `OpBadgeStudent` | see file |
| `op.marks.line` | `OpMarksLine` | see file |
| `ir.module.module` | `IrModuleModule` | see file |
| `onboarding.onboarding` | `OnboardingOnboarding` | see file |
| `onboarding.onboarding.step` | `OnboardingOnboardingStep` | see file |
| `op.department` | `OpDepartment` | see file |
| `publisher_warranty.contract` | `PublisherWarrantyContract` | see file |
| `op.section` | `OpSection` | see file |
| `op.subject.faculty` | `OpSubjectFaculty` | see file |
| `op.topics` | `OpTopics` | see file |
| `res.users` | `ResUsers` | see file |
| `website` | `Website` | see file |
| `website.configurator.feature` | `WebsiteConfiguratorFeature` | see file |
