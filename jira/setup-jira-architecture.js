#!/usr/bin/env node

const JiraApi = require("jira.js").default;

// Configuration
const config = {
    host: "https://abdelhadieddiraa4-1768918580829.atlassian.net",
    authentication: {
        basic: {
            email: "your-email@example.com", // REPLACE WITH YOUR JIRA EMAIL
            apiToken:
                "ATATT3xFfGF0NljpDQUco6gAqyhJsnqdt73wNqYnLkoAwIOI0l5WcZhUA-2CLX5EfPdYI2EoLNjGaPYxNUc7BNROg6CEqXIy5pRgaBnLqXUxVv4eWJc7PrINsg2acrwzj1xUxApIV6h41HziVHdkCOcjf4vDDA0VzSL7oAT7bSaP-yK7DjxiKrc=5F72132C",
        },
    },
};

const jira = new JiraApi(config);

// Project definitions based on the architecture
const projects = [
    {
        key: "ODEDU",
        name: "ODOO-EDU Education Management",
        description:
            "Education Management System - Student lifecycle, academics, assessments, campus operations",
        projectTypeKey: "software",
        projectTemplateKey: "com.pyxis.greenhopper.jira:gh-scrum-template",
        leadAccountId: null, // Will be set to current user
        epics: [
            {
                name: "Student Lifecycle Management",
                description: "Admissions, Students, SIS (Student Information System)",
                modules: ["Admissions", "Students", "SIS"],
            },
            {
                name: "Academic Delivery",
                description: "LMS, Time Table, Class Attendances, Assignments",
                modules: ["LMS", "Time Table", "Class Attendances", "Assignments"],
            },
            {
                name: "Assessment & Evaluation",
                description: "Exams, Grade Book, Quiz, Thesis, OMR",
                modules: ["Exams", "Grade Book", "Quiz", "Thesis", "OMR"],
            },
            {
                name: "Campus Operations",
                description:
                    "Campus Management, Transportation, Library, Digital Library, Events",
                modules: [
                    "Campus",
                    "Transportation",
                    "Library",
                    "Digital Library",
                    "Events",
                ],
            },
            {
                name: "Career Services",
                description: "Placements and Alumni management",
                modules: ["Placements", "Alumni"],
            },
        ],
    },
    {
        key: "ODHR",
        name: "ODOO-HR Human Resources",
        description:
            "Human Resources & Recruitment - Talent acquisition and employee management",
        projectTypeKey: "software",
        projectTemplateKey: "com.pyxis.greenhopper.jira:gh-scrum-template",
        leadAccountId: null,
        epics: [
            {
                name: "Talent Acquisition",
                description: "Fleet, Recruitment, Job Postings, OnBoarding",
                modules: ["Fleet", "Recruitment", "Job", "OnBoarding"],
            },
            {
                name: "Employee Management",
                description: "Human Resources Core, Time Off, Expenses, Approvals",
                modules: ["Human Resources", "Time Off", "Expenses", "Approvals"],
            },
        ],
    },
    {
        key: "ODBUS",
        name: "ODOO-BUS Business Operations",
        description: "Business Operations - Revenue, finance, and customer support",
        projectTypeKey: "software",
        projectTemplateKey: "com.pyxis.greenhopper.jira:gh-scrum-template",
        leadAccountId: null,
        epics: [
            {
                name: "Revenue Management",
                description: "Sales, CRM, Email Marketing",
                modules: ["Sales", "CRM", "Email Marketing"],
            },
            {
                name: "Financial Operations",
                description: "Accounting, Purchase, Inventory",
                modules: ["Accounting", "Purchase", "Inventory"],
            },
            {
                name: "Customer Support",
                description: "Helpdesk, Live Chat, Surveys",
                modules: ["Helpdesk", "Live Chat", "Surveys"],
            },
        ],
    },
    {
        key: "ODCOM",
        name: "ODOO-COMM Communication & Marketing",
        description: "Communication & Marketing - Digital presence and engagement",
        projectTypeKey: "software",
        projectTemplateKey: "com.pyxis.greenhopper.jira:gh-kanban-template",
        leadAccountId: null,
        epics: [
            {
                name: "Digital Presence",
                description: "Website, Email Marketing, WhatsApp Integration",
                modules: ["Website", "WhatsApp"],
            },
            {
                name: "Engagement & Automation",
                description: "Live Chat, Automated Marketing, Surveys",
                modules: ["Automated Marketing"],
            },
            {
                name: "Internal Communication",
                description: "Discuss, Notice Board",
                modules: ["Discuss", "Notice Board"],
            },
        ],
    },
    {
        key: "ODCOR",
        name: "ODOO-CORE Platform Infrastructure",
        description:
            "Core Infrastructure & Platform - Foundation, collaboration, analytics",
        projectTypeKey: "software",
        projectTemplateKey: "com.pyxis.greenhopper.jira:gh-scrum-template",
        leadAccountId: null,
        epics: [
            {
                name: "Platform Foundation",
                description: "Multi Campus Support, Settings, Apps Marketplace",
                modules: ["Multi Campus", "Settings", "Apps"],
            },
            {
                name: "Collaboration Tools",
                description: "Calendar, Documents, E-sign, Spreadsheets",
                modules: ["Calendar", "Documents", "E-sign", "Spreadsheets"],
            },
            {
                name: "Analytics & Reporting",
                description: "Dashboards, KPI Dashboard",
                modules: ["Dashboards", "KPI Dashboard"],
            },
            {
                name: "Master Data",
                description: "Contacts management",
                modules: ["Contacts"],
            },
        ],
    },
];

// Component definitions
const components = [
    "Frontend/UI",
    "Backend/API",
    "Database",
    "Integration",
    "Infrastructure",
    "Security",
    "Performance",
    "Reporting",
    "Notifications",
    "Workflows",
    "User Management",
    "Permissions",
    "Data Migration",
    "Training/Documentation",
];

// Labels to create
const labels = [
    "critical",
    "high-priority",
    "medium-priority",
    "low-priority",
    "feature",
    "enhancement",
    "bug",
    "technical-debt",
    "documentation",
    "academic",
    "finance",
    "hr",
    "operations",
    "infrastructure",
    "blocked",
    "needs-review",
    "waiting-qa",
    "ready-for-uat",
];

async function getCurrentUser() {
    try {
        const user = await jira.myself.getCurrentUser();
        console.log(`✓ Authenticated as: ${user.displayName} (${user.emailAddress})`);
        return user.accountId;
    } catch (error) {
        console.error("✗ Authentication failed:", error.message);
        throw error;
    }
}

async function createProject(projectData, currentUserId) {
    try {
        console.log(
            `\n📦 Creating project: ${projectData.name} (${projectData.key})...`
        );

        const project = await jira.projects.createProject({
            key: projectData.key,
            name: projectData.name,
            description: projectData.description,
            projectTypeKey: projectData.projectTypeKey,
            projectTemplateKey: projectData.projectTemplateKey,
            leadAccountId: currentUserId,
        });

        console.log(`  ✓ Project ${projectData.key} created successfully`);
        return project;
    } catch (error) {
        if (
            error.response?.status === 400 &&
            error.response?.data?.errors?.projectKey
        ) {
            console.log(`  ⚠ Project ${projectData.key} already exists, skipping...`);
            return await jira.projects.getProject({projectIdOrKey: projectData.key});
        }
        console.error(
            `  ✗ Failed to create project ${projectData.key}:`,
            error.message
        );
        throw error;
    }
}

async function createEpic(projectKey, epicData, epicNumber) {
    try {
        console.log(
            `  📋 Creating Epic E${String(epicNumber).padStart(2, "0")}: ${epicData.name}...`
        );

        const issue = await jira.issues.createIssue({
            fields: {
                project: {key: projectKey},
                summary: epicData.name,
                description: {
                    type: "doc",
                    version: 1,
                    content: [
                        {
                            type: "paragraph",
                            content: [
                                {
                                    type: "text",
                                    text: epicData.description,
                                },
                            ],
                        },
                        {
                            type: "paragraph",
                            content: [
                                {
                                    type: "text",
                                    text: "\nModules included:",
                                },
                            ],
                        },
                        {
                            type: "bulletList",
                            content: epicData.modules.map((module) => ({
                                type: "listItem",
                                content: [
                                    {
                                        type: "paragraph",
                                        content: [
                                            {
                                                type: "text",
                                                text: module,
                                            },
                                        ],
                                    },
                                ],
                            })),
                        },
                    ],
                },
                issuetype: {name: "Epic"},
            },
        });

        console.log(`    ✓ Epic ${issue.key} created`);
        return issue;
    } catch (error) {
        console.error(`    ✗ Failed to create epic:`, error.message);
        // Continue with other epics even if one fails
        return null;
    }
}

async function createSampleStories(projectKey, epicKey, modules) {
    const stories = [];

    for (const module of modules.slice(0, 2)) {
        // Create 2 sample stories per epic
        try {
            console.log(`    📝 Creating sample story for ${module}...`);

            const story = await jira.issues.createIssue({
                fields: {
                    project: {key: projectKey},
                    summary: `Implement ${module} module - Initial setup`,
                    description: {
                        type: "doc",
                        version: 1,
                        content: [
                            {
                                type: "paragraph",
                                content: [
                                    {
                                        type: "text",
                                        text: `As a system administrator, I want to set up the ${module} module so that users can access core functionality.`,
                                    },
                                ],
                            },
                            {
                                type: "heading",
                                attrs: {level: 3},
                                content: [
                                    {
                                        type: "text",
                                        text: "Acceptance Criteria",
                                    },
                                ],
                            },
                            {
                                type: "bulletList",
                                content: [
                                    {
                                        type: "listItem",
                                        content: [
                                            {
                                                type: "paragraph",
                                                content: [
                                                    {
                                                        type: "text",
                                                        text: `${module} module is installed and configured`,
                                                    },
                                                ],
                                            },
                                        ],
                                    },
                                    {
                                        type: "listItem",
                                        content: [
                                            {
                                                type: "paragraph",
                                                content: [
                                                    {
                                                        type: "text",
                                                        text: "Database schema is created",
                                                    },
                                                ],
                                            },
                                        ],
                                    },
                                    {
                                        type: "listItem",
                                        content: [
                                            {
                                                type: "paragraph",
                                                content: [
                                                    {
                                                        type: "text",
                                                        text: "Basic UI is accessible",
                                                    },
                                                ],
                                            },
                                        ],
                                    },
                                    {
                                        type: "listItem",
                                        content: [
                                            {
                                                type: "paragraph",
                                                content: [
                                                    {
                                                        type: "text",
                                                        text: "Unit tests pass",
                                                    },
                                                ],
                                            },
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                    issuetype: {name: "Story"},
                    parent: {key: epicKey},
                    labels: [
                        "feature",
                        `module:${module.toLowerCase().replace(/\s+/g, "-")}`,
                    ],
                },
            });

            console.log(`      ✓ Story ${story.key} created`);
            stories.push(story);
        } catch (error) {
            console.error(
                `      ✗ Failed to create story for ${module}:`,
                error.message
            );
        }
    }

    return stories;
}

async function createComponents(projectKey) {
    console.log(`\n  🔧 Creating components for ${projectKey}...`);

    for (const componentName of components) {
        try {
            await jira.projectComponents.createComponent({
                name: componentName,
                project: projectKey,
                description: `${componentName} related work`,
            });
            console.log(`    ✓ Component: ${componentName}`);
        } catch (error) {
            if (error.response?.status === 400) {
                console.log(`    ⚠ Component ${componentName} already exists`);
            } else {
                console.error(
                    `    ✗ Failed to create component ${componentName}:`,
                    error.message
                );
            }
        }
    }
}

async function createVersion(projectKey, versionName, description, releaseDate) {
    try {
        const version = await jira.projectVersions.createVersion({
            project: projectKey,
            name: versionName,
            description: description,
            releaseDate: releaseDate,
            released: false,
        });
        console.log(`    ✓ Version: ${versionName}`);
        return version;
    } catch (error) {
        if (error.response?.status === 404) {
            console.log(
                `    ⚠ Version ${versionName} already exists or project not found`
            );
        } else {
            console.error(
                `    ✗ Failed to create version ${versionName}:`,
                error.message
            );
        }
        return null;
    }
}

async function createProjectVersions(projectKey, projectName) {
    console.log(`\n  📅 Creating versions for ${projectKey}...`);

    const versions = [
        {
            name: "v1.0.0",
            description: `${projectName} - Initial Release`,
            date: "2026-06-30",
        },
        {
            name: "v1.1.0",
            description: `${projectName} - Feature Enhancement`,
            date: "2026-09-30",
        },
        {
            name: "v2.0.0",
            description: `${projectName} - Major Update`,
            date: "2026-12-31",
        },
    ];

    for (const ver of versions) {
        await createVersion(projectKey, ver.name, ver.description, ver.date);
    }
}

async function setupProject(projectData, currentUserId) {
    try {
        // Create project
        const project = await createProject(projectData, currentUserId);

        // Small delay to ensure project is fully created
        await new Promise((resolve) => setTimeout(resolve, 2000));

        // Create components
        await createComponents(projectData.key);

        // Create versions
        await createProjectVersions(projectData.key, projectData.name);

        // Create epics and sample stories
        console.log(`\n  📋 Creating epics for ${projectData.key}...`);
        let epicNumber = 1;

        for (const epicData of projectData.epics) {
            const epic = await createEpic(projectData.key, epicData, epicNumber);

            if (epic) {
                // Create 2 sample stories per epic
                await createSampleStories(projectData.key, epic.key, epicData.modules);
            }

            epicNumber++;
            // Small delay between epics
            await new Promise((resolve) => setTimeout(resolve, 1000));
        }

        console.log(`\n  ✅ Project ${projectData.key} setup complete!\n`);
        return project;
    } catch (error) {
        console.error(
            `\n  ❌ Failed to setup project ${projectData.key}:`,
            error.message
        );
        return null;
    }
}

async function createBoard(projectKey, projectName, boardType) {
    try {
        console.log(`\n  📊 Creating ${boardType} board for ${projectKey}...`);

        const board = await jira.board.createBoard({
            name: `${projectName} ${boardType === "scrum" ? "Scrum" : "Kanban"} Board`,
            type: boardType,
            filterId: undefined, // Will use default filter for the project
            location: {
                type: "project",
                projectKeyOrId: projectKey,
            },
        });

        console.log(`    ✓ Board created: ${board.name}`);
        return board;
    } catch (error) {
        console.error(`    ✗ Failed to create board:`, error.message);
        return null;
    }
}

async function main() {
    console.log("╔════════════════════════════════════════════════════════════╗");
    console.log("║   JIRA ODOO ERP SCRUM ARCHITECTURE SETUP                  ║");
    console.log("╚════════════════════════════════════════════════════════════╝\n");

    try {
        // Authenticate and get current user
        const currentUserId = await getCurrentUser();

        console.log("\n📋 Setup Plan:");
        console.log("  → 5 Jira Projects");
        console.log("  → 17 Epics across all projects");
        console.log("  → 34+ Sample stories");
        console.log("  → 14 Components per project");
        console.log("  → 3 Versions per project");
        console.log("  → Scrum/Kanban boards\n");

        const readline = require("readline").createInterface({
            input: process.stdin,
            output: process.stdout,
        });

        console.log(
            '⚠️  IMPORTANT: Make sure you have replaced "your-email@example.com" with your actual Jira email in this script!\n'
        );

        await new Promise((resolve) => {
            readline.question("Press Enter to continue with setup...", () => {
                readline.close();
                resolve();
            });
        });

        console.log("\n🚀 Starting setup...\n");

        const createdProjects = [];

        // Setup each project
        for (const projectData of projects) {
            const project = await setupProject(projectData, currentUserId);
            if (project) {
                createdProjects.push({...project, originalData: projectData});
            }

            // Delay between projects
            await new Promise((resolve) => setTimeout(resolve, 2000));
        }

        console.log("\n═══════════════════════════════════════════════════════════");
        console.log("                    SETUP SUMMARY                          ");
        console.log("═══════════════════════════════════════════════════════════\n");

        console.log("✅ Projects Created:\n");
        for (const project of createdProjects) {
            console.log(`   ${project.key} - ${project.name}`);
            console.log(`   └─ ${project.originalData.epics.length} epics`);
        }

        console.log("\n\n🎯 Next Steps:");
        console.log("   1. Log into your Jira instance:");
        console.log(`      ${config.host}`);
        console.log("   2. Review the created projects and epics");
        console.log("   3. Configure board columns and workflows as needed");
        console.log("   4. Set up automation rules (see documentation)");
        console.log("   5. Invite team members to appropriate projects");
        console.log("   6. Start sprint planning!\n");

        console.log("📚 Documentation:");
        console.log("   See odoo_jira_scrum_architecture.md for detailed guidelines\n");

        console.log("✅ Setup Complete!\n");
    } catch (error) {
        console.error("\n❌ Setup failed:", error.message);
        if (error.response?.data) {
            console.error(
                "Error details:",
                JSON.stringify(error.response.data, null, 2)
            );
        }
        process.exit(1);
    }
}

// Run the setup
main();
