# Jira Scrum Architecture for Odoo ERP Implementation

## Executive Summary

This document outlines the recommended Jira Scrum architecture for implementing a
comprehensive Odoo ERP system with 51 modules across Academic, HR, Business Operations,
and Communication domains.

---

## 1. PROJECT STRUCTURE OVERVIEW

### 1.1 Recommended Approach: Multi-Project Structure

**Strategy:** Create separate Jira projects for major functional domains with
cross-project dependencies

**Project Key Naming Convention:**

- **ODOO-EDU** - Education Management System
- **ODOO-HR** - Human Resources & Recruitment
- **ODOO-BUS** - Business Operations (Sales, Finance, Inventory)
- **ODOO-COMM** - Communication & Marketing
- **ODOO-CORE** - Core Infrastructure & Platform

---

## 2. PROJECT BREAKDOWN

### **Project 1: ODOO-EDU (Education Management System)**

**Project Key:** ODOO-EDU **Board Type:** Scrum Board **Sprint Duration:** 2 weeks

#### Epics Structure:

1. **ODOO-EDU-E01: Student Lifecycle Management**
   - Admissions
   - Students
   - SIS (Student Information System)

2. **ODOO-EDU-E02: Academic Delivery**
   - LMS (Learning Management System)
   - Time Table
   - Class Attendances
   - Assignments

3. **ODOO-EDU-E03: Assessment & Evaluation**
   - Exams
   - Grade Book
   - Quiz
   - Thesis
   - OMR

4. **ODOO-EDU-E04: Campus Operations**
   - Campus Management
   - Transportation
   - Library
   - Digital Library
   - Events

5. **ODOO-EDU-E05: Career Services**
   - Placements
   - Alumni

---

### **Project 2: ODOO-HR (Human Resources & Recruitment)**

**Project Key:** ODOO-HR **Board Type:** Scrum Board **Sprint Duration:** 2 weeks

#### Epics Structure:

1. **ODOO-HR-E01: Talent Acquisition**
   - Fleet (if related to employee transportation)
   - Recruitment
   - Job Postings
   - OnBoarding

2. **ODOO-HR-E02: Employee Management**
   - Human Resources Core
   - Time Off
   - Expenses
   - Approvals

---

### **Project 3: ODOO-BUS (Business Operations)**

**Project Key:** ODOO-BUS **Board Type:** Scrum Board **Sprint Duration:** 2 weeks

#### Epics Structure:

1. **ODOO-BUS-E01: Revenue Management**
   - Sales
   - CRM
   - Email Marketing

2. **ODOO-BUS-E02: Financial Operations**
   - Accounting
   - Purchase
   - Inventory

3. **ODOO-BUS-E03: Customer Support**
   - Helpdesk
   - Live Chat
   - Surveys

---

### **Project 4: ODOO-COMM (Communication & Marketing)**

**Project Key:** ODOO-COMM **Board Type:** Kanban Board (Continuous Flow) **Reason:**
Marketing and communication tasks often don't fit into fixed sprints

#### Epics Structure:

1. **ODOO-COMM-E01: Digital Presence**
   - Website
   - Email Marketing
   - WhatsApp Integration

2. **ODOO-COMM-E02: Engagement & Automation**
   - Live Chat
   - Automated Marketing
   - Surveys

3. **ODOO-COMM-E03: Internal Communication**
   - Discuss
   - Notice Board

---

### **Project 5: ODOO-CORE (Core Infrastructure & Platform)**

**Project Key:** ODOO-CORE **Board Type:** Scrum Board **Sprint Duration:** 2 weeks

#### Epics Structure:

1. **ODOO-CORE-E01: Platform Foundation**
   - Multi Campus Support
   - Settings
   - Apps Marketplace

2. **ODOO-CORE-E02: Collaboration Tools**
   - Calendar
   - Documents
   - E-sign
   - Spreadsheets

3. **ODOO-CORE-E03: Analytics & Reporting**
   - Dashboards
   - KPI Dashboard

4. **ODOO-CORE-E04: Master Data**
   - Contacts

---

## 3. JIRA HIERARCHY STRUCTURE

```
Initiative (Portfolio Level)
    └── Epic (Feature/Module Level)
        └── Story (User Requirement)
            └── Task (Development Work)
                └── Sub-task (Granular Activities)
```

### Hierarchy Example:

```
Initiative: Odoo ERP Digital Transformation
  ├── Epic: Student Lifecycle Management (ODOO-EDU-E01)
  │   ├── Story: As an admin, I want to manage student admissions
  │   │   ├── Task: Design admission form UI
  │   │   │   ├── Sub-task: Create wireframes
  │   │   │   └── Sub-task: Review with stakeholders
  │   │   ├── Task: Develop admission workflow
  │   │   └── Task: Integrate payment gateway
  │   └── Story: As a student, I want to track my application status
  │       └── Task: Create student portal
```

---

## 4. ISSUE TYPE CONFIGURATION

### Recommended Issue Types per Project:

| Issue Type     | Usage                     | Example                                     |
| -------------- | ------------------------- | ------------------------------------------- |
| **Initiative** | Program-level objectives  | "Phase 1: Academic Modules Implementation"  |
| **Epic**       | Large features/modules    | "Admissions Management System"              |
| **Story**      | User-facing functionality | "As a teacher, I want to record attendance" |
| **Task**       | Technical implementation  | "Setup database schema for attendance"      |
| **Sub-task**   | Granular work items       | "Write unit tests for attendance API"       |
| **Bug**        | Defects found             | "Attendance report shows wrong count"       |
| **Spike**      | Research/Investigation    | "Evaluate OMR scanning libraries"           |

---

## 5. WORKFLOW DESIGN

### Standard Workflow for All Projects:

```
TO DO → IN PROGRESS → CODE REVIEW → QA TESTING → UAT → DONE
```

### Detailed Workflow States:

1. **TO DO** (Backlog)
   - Requirements defined
   - Ready for development

2. **IN PROGRESS**
   - Active development
   - WIP limit: 3-5 per developer

3. **CODE REVIEW**
   - Pull request created
   - Peer review in progress

4. **QA TESTING**
   - Functional testing
   - Integration testing
   - Performance testing

5. **UAT (User Acceptance Testing)**
   - Business stakeholder review
   - User testing

6. **DONE**
   - Deployed to production
   - Documentation complete
   - Acceptance criteria met

---

## 6. SPRINT STRUCTURE

### Sprint Planning Strategy

#### Sprint Cadence:

- **Duration:** 2 weeks
- **Sprint Start:** Monday
- **Sprint End:** Friday (2 weeks later)

#### Sprint Ceremonies:

| Ceremony                 | Duration  | Participants             | Frequency       |
| ------------------------ | --------- | ------------------------ | --------------- |
| **Sprint Planning**      | 2-4 hours | Scrum Team, PO           | Start of sprint |
| **Daily Standup**        | 15 min    | Development Team         | Daily           |
| **Sprint Review**        | 1-2 hours | Scrum Team, Stakeholders | End of sprint   |
| **Sprint Retrospective** | 1 hour    | Scrum Team               | End of sprint   |
| **Backlog Refinement**   | 1 hour    | Scrum Team               | Mid-sprint      |

---

## 7. TEAM STRUCTURE

### Recommended Scrum Teams:

#### Team 1: Education Squad

- **Focus:** ODOO-EDU project
- **Size:** 5-7 members
- **Modules:** Admissions, Students, SIS, LMS, Timetable, Attendance, Exams, Grades

#### Team 2: HR & Talent Squad

- **Focus:** ODOO-HR project
- **Size:** 4-6 members
- **Modules:** Recruitment, Onboarding, HR Core, Time Off, Expenses

#### Team 3: Business Operations Squad

- **Focus:** ODOO-BUS project
- **Size:** 5-7 members
- **Modules:** Sales, Accounting, Purchase, Inventory, CRM

#### Team 4: Platform & Infrastructure Squad

- **Focus:** ODOO-CORE project
- **Size:** 4-5 members
- **Modules:** Multi-Campus, Settings, Dashboards, Documents, Calendar

#### Team 5: Communication & Marketing Squad

- **Focus:** ODOO-COMM project
- **Size:** 3-4 members
- **Board:** Kanban
- **Modules:** Website, Email Marketing, WhatsApp, Live Chat

---

## 8. ESTIMATION & VELOCITY TRACKING

### Story Point Scale (Fibonacci):

- **1 point:** Very simple, <4 hours
- **2 points:** Simple, <1 day
- **3 points:** Medium, 1-2 days
- **5 points:** Complex, 2-3 days
- **8 points:** Very complex, 3-5 days
- **13 points:** Epic size, needs breakdown
- **21+ points:** Too large, must split

### Velocity Tracking:

- Track completed story points per sprint
- Calculate average velocity after 3-4 sprints
- Use for sprint planning and release forecasting
- Monitor burndown charts daily

---

## 9. BACKLOG MANAGEMENT

### Backlog Hierarchy:

1. **Product Backlog** (All projects combined)
2. **Sprint Backlog** (Current sprint only)
3. **Icebox** (Future ideas, low priority)

### Prioritization Framework (MoSCoW):

- **Must Have:** Critical for go-live
- **Should Have:** Important but not critical
- **Could Have:** Nice to have
- **Won't Have:** Future consideration

### Backlog Refinement Rules:

- Top 2-3 sprints worth of stories should be refined
- Stories must have acceptance criteria
- Technical dependencies identified
- Story points estimated
- Ready for sprint planning

---

## 10. COMPONENT CONFIGURATION

### Create Components for Cross-Cutting Concerns:

**Technical Components:**

- Frontend/UI
- Backend/API
- Database
- Integration
- Infrastructure
- Security
- Performance

**Functional Components:**

- Reporting
- Notifications
- Workflows
- User Management
- Permissions
- Data Migration
- Training/Documentation

---

## 11. LABELS STRATEGY

### Recommended Labels:

**Priority:**

- `critical`
- `high-priority`
- `medium-priority`
- `low-priority`

**Type:**

- `feature`
- `enhancement`
- `bug`
- `technical-debt`
- `documentation`

**Domain:**

- `academic`
- `finance`
- `hr`
- `operations`
- `infrastructure`

**Status:**

- `blocked`
- `needs-review`
- `waiting-qa`
- `ready-for-uat`

**Modules (Examples):**

- `module:admissions`
- `module:lms`
- `module:accounting`
- `module:crm`

---

## 12. EPIC STRUCTURE TEMPLATE

### Epic Template:

```
Epic Name: [Module Name] - [Feature]
Epic Link: ODOO-XXX-E##

Summary:
[Brief description of the epic]

Business Value:
[Why this is important]

Scope:
- Feature 1
- Feature 2
- Feature 3

Success Criteria:
- [ ] Criterion 1
- [ ] Criterion 2

Dependencies:
- Epic: ODOO-XXX-E##
- External: [System/Team]

Target Release: Q#/YYYY
Team: [Squad Name]
```

---

## 13. STORY TEMPLATE

### User Story Template:

```
Title: As a [user role], I want to [action] so that [benefit]

Description:
[Detailed description]

Acceptance Criteria:
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]

Technical Notes:
- API endpoints needed
- Database changes
- UI components

Definition of Done:
- [ ] Code complete and reviewed
- [ ] Unit tests written (>80% coverage)
- [ ] QA testing passed
- [ ] Documentation updated
- [ ] Deployed to staging
- [ ] UAT approved

Dependencies:
- Story: ODOO-XXX-###
```

---

## 14. BOARD CONFIGURATION

### Scrum Board Setup:

**Columns:**

1. Backlog
2. Selected for Development
3. In Progress
4. Code Review
5. QA Testing
6. UAT
7. Done

**Swimlanes:**

- Group by: Assignee
- Or by: Epic
- Or by: Priority

**Quick Filters:**

- My Issues
- Current Sprint
- Blocked Issues
- Bugs Only
- Ready for Review

---

## 15. AUTOMATION RULES

### Recommended Automations:

1. **Auto-assign based on component**
   - When component = "Frontend" → assign to frontend team

2. **Status transition notifications**
   - When status changes to "Code Review" → notify reviewers

3. **SLA reminders**
   - When issue is in "QA Testing" for >2 days → notify QA lead

4. **Sprint hygiene**
   - When sprint ends → move incomplete issues to backlog

5. **Bug escalation**
   - When bug priority = "Critical" → notify project manager

6. **Blocked issue alerts**
   - When issue labeled "blocked" → daily reminder to assignee

---

## 16. REPORTING & DASHBOARDS

### Key Reports for Each Team:

#### Sprint Reports:

- **Burndown Chart:** Track daily progress
- **Velocity Chart:** Historical sprint velocity
- **Sprint Report:** Completed vs incomplete
- **Cumulative Flow Diagram:** Work distribution

#### Release Reports:

- **Epic Burndown:** Epic progress over time
- **Release Burnup:** Scope vs completion
- **Version Report:** Release readiness

#### Team Performance:

- **Control Chart:** Cycle time analysis
- **Throughput:** Issues completed per sprint
- **Work in Progress:** Current load per person

---

## 17. CUSTOM DASHBOARD

### Create Project Dashboard with Widgets:

**Widgets to Include:**

1. Sprint Health (Burndown)
2. Issue Statistics (By Status)
3. Created vs Resolved Chart
4. Filter Results (My Open Issues)
5. Epic Progress
6. Upcoming Deadlines
7. Recently Updated Issues
8. Team Velocity Trend

---

## 18. JIRA FEATURES TO LEVERAGE

### Advanced Features:

1. **Advanced Roadmaps**
   - Cross-project planning
   - Dependency visualization
   - Capacity planning
   - Scenario planning

2. **Automation**
   - Auto-transitions
   - SLA management
   - Notifications
   - Field updates

3. **Dashboards**
   - Real-time project status
   - Executive summaries
   - Team performance metrics

4. **JQL (Jira Query Language)**
   - Complex searches
   - Custom filters
   - Bulk operations

5. **Integrations**
   - Confluence (Documentation)
   - Bitbucket/GitHub (Code repos)
   - Slack (Notifications)
   - Jenkins (CI/CD)

6. **Advanced Permissions**
   - Role-based access
   - Field-level security
   - Project-level permissions

---

## 19. VERSIONING & RELEASES

### Version Naming Convention:

- **Format:** `v[Major].[Minor].[Patch]-[Module]`
- **Example:** `v1.0.0-EDU`, `v1.1.0-HR`

### Release Schedule:

- **Sprint Release:** Every 2 weeks to staging
- **Minor Release:** Monthly to production
- **Major Release:** Quarterly (full feature set)

### Version Mapping:

| Version | Modules                                        | Target Date |
| ------- | ---------------------------------------------- | ----------- |
| v1.0.0  | Education Core (Admissions, Students, SIS)     | Q2 2026     |
| v1.1.0  | Academic Delivery (LMS, Timetable, Attendance) | Q3 2026     |
| v1.2.0  | Assessment (Exams, Grades, Quiz)               | Q3 2026     |
| v2.0.0  | HR & Recruitment                               | Q4 2026     |
| v2.1.0  | Business Operations                            | Q1 2027     |

---

## 20. CROSS-PROJECT DEPENDENCIES

### Managing Dependencies:

1. **Create Dependency Links:**
   - Use "blocks" and "is blocked by" link types
   - Visualize in Advanced Roadmaps

2. **Dependency Board:**
   - Create filter showing all cross-project dependencies
   - Review in weekly sync meetings

3. **Integration Stories:**
   - Create separate stories for system integrations
   - Assign to appropriate teams
   - Tag with `integration` label

**Example Dependencies:**

- ODOO-EDU (Students) depends on ODOO-CORE (Contacts)
- ODOO-HR (Recruitment) depends on ODOO-COMM (Email Marketing)
- ODOO-BUS (Sales) depends on ODOO-BUS (CRM)

---

## 21. QUALITY GATES

### Definition of Ready (DoR):

- [ ] User story follows template
- [ ] Acceptance criteria defined
- [ ] Dependencies identified
- [ ] Story points estimated
- [ ] Priority assigned
- [ ] Mockups/designs available (if UI)

### Definition of Done (DoD):

- [ ] Code complete and committed
- [ ] Peer review completed
- [ ] Unit tests pass (>80% coverage)
- [ ] Integration tests pass
- [ ] QA testing completed
- [ ] Documentation updated
- [ ] UAT approved
- [ ] Deployed to production
- [ ] Release notes updated

---

## 22. RISK MANAGEMENT

### Risk Labels:

- `risk:technical`
- `risk:resource`
- `risk:dependency`
- `risk:compliance`

### Risk Tracking:

- Create separate "Risk" issue type
- Link risks to affected epics/stories
- Review in sprint planning
- Update risk register weekly

---

## 23. STAKEHOLDER COMMUNICATION

### Communication Plan:

| Audience             | Report                   | Frequency | Tool                  |
| -------------------- | ------------------------ | --------- | --------------------- |
| **Executives**       | Project Status Dashboard | Weekly    | Jira Dashboard        |
| **Product Owners**   | Sprint Review            | Bi-weekly | Sprint Review Meeting |
| **Development Team** | Daily Standup Notes      | Daily     | Jira Board            |
| **QA Team**          | Test Progress Report     | Daily     | Jira Filter           |
| **Business Users**   | Release Notes            | Monthly   | Confluence            |

---

## 24. TRAINING & ONBOARDING

### New Team Member Onboarding:

**Week 1: Jira Basics**

- Jira navigation
- Creating/updating issues
- Using boards and filters
- Understanding workflows

**Week 2: Project Specifics**

- Project structure
- Team conventions
- Estimation process
- Sprint ceremonies

**Week 3: Advanced Features**

- JQL queries
- Dashboard creation
- Automation rules
- Reporting

---

## 25. IMPLEMENTATION ROADMAP

### Phase 1: Setup (Weeks 1-2)

- [ ] Create projects in Jira
- [ ] Configure workflows
- [ ] Set up issue types and fields
- [ ] Create initial epics
- [ ] Configure boards
- [ ] Set up automation rules
- [ ] Create dashboards

### Phase 2: Backlog Creation (Weeks 3-4)

- [ ] Break down epics into stories
- [ ] Write acceptance criteria
- [ ] Estimate stories
- [ ] Prioritize backlog
- [ ] Identify dependencies
- [ ] Create initial sprints

### Phase 3: Team Training (Week 5)

- [ ] Conduct Jira training
- [ ] Scrum methodology workshop
- [ ] Tool walk-throughs
- [ ] Practice sprint

### Phase 4: Sprint 0 (Weeks 6-7)

- [ ] Environment setup
- [ ] Architecture decisions
- [ ] Technical spikes
- [ ] Development standards
- [ ] CI/CD pipeline setup

### Phase 5: Active Development (Week 8+)

- [ ] Regular sprints begin
- [ ] Weekly stakeholder demos
- [ ] Continuous backlog refinement
- [ ] Monthly releases

---

## 26. SUCCESS METRICS

### Key Performance Indicators:

1. **Velocity Metrics**
   - Average story points per sprint
   - Velocity trend (increasing/stable)
   - Sprint commitment vs completion rate

2. **Quality Metrics**
   - Bugs per story point
   - Defect escape rate
   - Code review turnaround time

3. **Delivery Metrics**
   - Sprint burndown completion
   - Release predictability
   - Cycle time per issue type

4. **Team Health**
   - Sprint retrospective action items completed
   - Team satisfaction scores
   - Unplanned work percentage

---

## 27. BEST PRACTICES SUMMARY

### Do's:

✅ Keep backlogs groomed and prioritized ✅ Break large stories into smaller ones ✅ Use
consistent naming conventions ✅ Update issues regularly ✅ Link related issues ✅ Add
comments for important decisions ✅ Use components and labels effectively ✅ Automate
repetitive tasks ✅ Review and update workflows regularly ✅ Conduct regular
retrospectives

### Don'ts:

❌ Don't create too many custom fields ❌ Don't skip backlog refinement ❌ Don't
overload sprints ❌ Don't neglect documentation ❌ Don't ignore technical debt ❌ Don't
work on issues outside sprint ❌ Don't bypass workflow steps ❌ Don't create duplicate
issues ❌ Don't forget to update issue status ❌ Don't ignore blocked issues

---

## 28. TROUBLESHOOTING GUIDE

### Common Issues & Solutions:

**Problem:** Velocity is inconsistent

- **Solution:** Review estimation process, check for scope creep, ensure team stability

**Problem:** Too many incomplete sprint items

- **Solution:** Reduce sprint commitment, improve story breakdown, address blockers
  faster

**Problem:** Backlog is overwhelming

- **Solution:** Archive old items, prioritize ruthlessly, groom regularly

**Problem:** Dependencies causing delays

- **Solution:** Identify earlier, create integration team, improve communication

**Problem:** Quality issues in releases

- **Solution:** Strengthen DoD, improve code review, enhance testing

---

## 29. TOOLS & INTEGRATIONS

### Recommended Jira Add-ons:

1. **Advanced Roadmaps** (Portfolio Management)
2. **Tempo Timesheets** (Time Tracking)
3. **ScriptRunner** (Advanced Automation)
4. **Zephyr** (Test Management)
5. **BigPicture** (Program Management)

### External Integrations:

- **Confluence:** Documentation and knowledge base
- **Bitbucket/GitHub:** Code repositories
- **Slack:** Team communication
- **Jenkins/GitLab CI:** Continuous integration
- **Figma:** Design collaboration

---

## 30. CONCLUSION & NEXT STEPS

### Immediate Actions:

1. Review this architecture with stakeholders
2. Gather feedback from development teams
3. Customize to fit organizational needs
4. Create pilot project to test structure
5. Schedule training sessions
6. Set up first sprint
7. Begin implementation

### Success Criteria for Implementation:

- [ ] All 51 modules mapped to projects
- [ ] Teams assigned and trained
- [ ] First 3 sprints planned
- [ ] Automation rules active
- [ ] Dashboards accessible
- [ ] Dependencies documented
- [ ] Stakeholders informed

---

## APPENDIX A: COMPLETE MODULE MAPPING

| Module              | Project   | Epic | Team               | Priority    |
| ------------------- | --------- | ---- | ------------------ | ----------- |
| Admissions          | ODOO-EDU  | E01  | Education Squad    | Must Have   |
| Students            | ODOO-EDU  | E01  | Education Squad    | Must Have   |
| SIS                 | ODOO-EDU  | E01  | Education Squad    | Must Have   |
| LMS                 | ODOO-EDU  | E02  | Education Squad    | Must Have   |
| Time Table          | ODOO-EDU  | E02  | Education Squad    | Should Have |
| Class Attendances   | ODOO-EDU  | E02  | Education Squad    | Must Have   |
| Assignments         | ODOO-EDU  | E02  | Education Squad    | Should Have |
| Exams               | ODOO-EDU  | E03  | Education Squad    | Must Have   |
| Grade Book          | ODOO-EDU  | E03  | Education Squad    | Must Have   |
| Quiz                | ODOO-EDU  | E03  | Education Squad    | Could Have  |
| Thesis              | ODOO-EDU  | E03  | Education Squad    | Could Have  |
| OMR                 | ODOO-EDU  | E03  | Education Squad    | Could Have  |
| Campus              | ODOO-EDU  | E04  | Education Squad    | Should Have |
| Transportation      | ODOO-EDU  | E04  | Education Squad    | Should Have |
| Library             | ODOO-EDU  | E04  | Education Squad    | Should Have |
| Digital Library     | ODOO-EDU  | E04  | Education Squad    | Could Have  |
| Events              | ODOO-EDU  | E04  | Education Squad    | Could Have  |
| Placements          | ODOO-EDU  | E05  | Education Squad    | Should Have |
| Alumni              | ODOO-EDU  | E05  | Education Squad    | Could Have  |
| Fleet               | ODOO-HR   | E01  | HR Squad           | Should Have |
| Recruitment         | ODOO-HR   | E01  | HR Squad           | Must Have   |
| Job                 | ODOO-HR   | E01  | HR Squad           | Must Have   |
| OnBoarding          | ODOO-HR   | E01  | HR Squad           | Should Have |
| Human Resources     | ODOO-HR   | E02  | HR Squad           | Must Have   |
| Time Off            | ODOO-HR   | E02  | HR Squad           | Must Have   |
| Expenses            | ODOO-HR   | E02  | HR Squad           | Should Have |
| Approvals           | ODOO-HR   | E02  | HR Squad           | Should Have |
| Sales               | ODOO-BUS  | E01  | Business Ops Squad | Must Have   |
| CRM                 | ODOO-BUS  | E01  | Business Ops Squad | Must Have   |
| Email Marketing     | ODOO-BUS  | E01  | Business Ops Squad | Should Have |
| Accounting          | ODOO-BUS  | E02  | Business Ops Squad | Must Have   |
| Purchase            | ODOO-BUS  | E02  | Business Ops Squad | Must Have   |
| Inventory           | ODOO-BUS  | E02  | Business Ops Squad | Must Have   |
| Helpdesk            | ODOO-BUS  | E03  | Business Ops Squad | Should Have |
| Live Chat           | ODOO-BUS  | E03  | Business Ops Squad | Could Have  |
| Surveys             | ODOO-BUS  | E03  | Business Ops Squad | Could Have  |
| Website             | ODOO-COMM | E01  | Comm Squad         | Must Have   |
| WhatsApp            | ODOO-COMM | E01  | Comm Squad         | Should Have |
| Automated Marketing | ODOO-COMM | E02  | Comm Squad         | Should Have |
| Discuss             | ODOO-COMM | E03  | Comm Squad         | Must Have   |
| Notice Board        | ODOO-COMM | E03  | Comm Squad         | Should Have |
| Multi Campus        | ODOO-CORE | E01  | Platform Squad     | Must Have   |
| Settings            | ODOO-CORE | E01  | Platform Squad     | Must Have   |
| Apps                | ODOO-CORE | E01  | Platform Squad     | Must Have   |
| Calendar            | ODOO-CORE | E02  | Platform Squad     | Should Have |
| Documents           | ODOO-CORE | E02  | Platform Squad     | Should Have |
| E-sign              | ODOO-CORE | E02  | Platform Squad     | Could Have  |
| Spreadsheets        | ODOO-CORE | E02  | Platform Squad     | Could Have  |
| Dashboards          | ODOO-CORE | E03  | Platform Squad     | Must Have   |
| KPI Dashboard       | ODOO-CORE | E03  | Platform Squad     | Should Have |
| Contacts            | ODOO-CORE | E04  | Platform Squad     | Must Have   |

---

## APPENDIX B: SAMPLE JQL QUERIES

```sql
-- All open issues in current sprint
sprint in openSprints() AND status != Done

-- My issues that are blocked
assignee = currentUser() AND labels = "blocked"

-- High priority bugs in QA
type = Bug AND priority = High AND status = "QA Testing"

-- Stories ready for sprint planning
type = Story AND status = "To Do" AND "Story Points" IS NOT EMPTY

-- Overdue issues
duedate < now() AND status != Done

-- Recent completed work (last 7 days)
status = Done AND resolved >= -7d

-- All epics in Education project
project = "ODOO-EDU" AND type = Epic

-- Cross-project dependencies
issueFunction in linkedIssuesOf("project = ODOO-EDU", "is blocked by") AND project != "ODOO-EDU"

-- Issues without story points
type = Story AND "Story Points" IS EMPTY AND sprint IS NOT EMPTY
```

---

**Document Version:** 1.0 **Last Updated:** March 30, 2026 **Author:** Claude AI
Assistant **Status:** Draft for Review
