#!/usr/bin/env node

const {Version3Client} = require("jira.js");
const readline = require("readline");
const fs = require("fs");

console.log("╔════════════════════════════════════════════════════════════╗");
console.log("║   JIRA ODOO ERP SCRUM ARCHITECTURE SETUP                  ║");
console.log("╚════════════════════════════════════════════════════════════╝\n");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function question(query) {
    return new Promise((resolve) => rl.question(query, resolve));
}

async function verifyCredentials(email, apiToken) {
    const jira = new Version3Client({
        host: "https://abdelhadieddiraa4-1768918580829.atlassian.net",
        authentication: {
            basic: {
                email: email,
                apiToken: apiToken,
            },
        },
    });

    try {
        const user = await jira.myself.getCurrentUser();
        console.log("\n✅ Authentication successful!");
        console.log(`   Name: ${user.displayName}`);
        console.log(`   Email: ${user.emailAddress}`);
        console.log(`   Account ID: ${user.accountId}\n`);
        return {jira, user};
    } catch (error) {
        console.error("\n❌ Authentication failed!");
        console.error(`   Error: ${error.message}\n`);
        return null;
    }
}

async function setupProjects(jira, currentUserId) {
    const projects = [
        {
            key: "ODEDU",
            name: "ODOO-EDU Education Management",
            description:
                "Education Management System - Student lifecycle, academics, assessments, campus operations",
            projectTypeKey: "software",
            projectTemplateKey: "com.pyxis.greenhopper.jira:gh-scrum-template",
            epics: [
                {
                    name: "Student Lifecycle Management",
                    desc: "Admissions, Students, SIS",
                    modules: ["Admissions", "Students", "SIS"],
                },
                {
                    name: "Academic Delivery",
                    desc: "LMS, Time Table, Attendances, Assignments",
                    modules: ["LMS", "Time Table", "Class Attendances", "Assignments"],
                },
                {
                    name: "Assessment & Evaluation",
                    desc: "Exams, Grades, Quiz, Thesis, OMR",
                    modules: ["Exams", "Grade Book", "Quiz", "Thesis", "OMR"],
                },
                {
                    name: "Campus Operations",
                    desc: "Campus, Transport, Library, Events",
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
                    desc: "Placements, Alumni",
                    modules: ["Placements", "Alumni"],
                },
            ],
        },
        {
            key: "ODHR",
            name: "ODOO-HR Human Resources",
            description: "Human Resources & Recruitment",
            projectTypeKey: "software",
            projectTemplateKey: "com.pyxis.greenhopper.jira:gh-scrum-template",
            epics: [
                {
                    name: "Talent Acquisition",
                    desc: "Recruitment, Jobs, Onboarding",
                    modules: ["Fleet", "Recruitment", "Job", "OnBoarding"],
                },
                {
                    name: "Employee Management",
                    desc: "HR Core, Time Off, Expenses",
                    modules: ["Human Resources", "Time Off", "Expenses", "Approvals"],
                },
            ],
        },
        {
            key: "ODBUS",
            name: "ODOO-BUS Business Operations",
            description: "Business Operations - Revenue, finance, customer support",
            projectTypeKey: "software",
            projectTemplateKey: "com.pyxis.greenhopper.jira:gh-scrum-template",
            epics: [
                {
                    name: "Revenue Management",
                    desc: "Sales, CRM, Marketing",
                    modules: ["Sales", "CRM", "Email Marketing"],
                },
                {
                    name: "Financial Operations",
                    desc: "Accounting, Purchase, Inventory",
                    modules: ["Accounting", "Purchase", "Inventory"],
                },
                {
                    name: "Customer Support",
                    desc: "Helpdesk, Chat, Surveys",
                    modules: ["Helpdesk", "Live Chat", "Surveys"],
                },
            ],
        },
        {
            key: "ODCOM",
            name: "ODOO-COMM Communication",
            description: "Communication & Marketing",
            projectTypeKey: "software",
            projectTemplateKey: "com.pyxis.greenhopper.jira:gh-kanban-template",
            epics: [
                {
                    name: "Digital Presence",
                    desc: "Website, WhatsApp, Email",
                    modules: ["Website", "WhatsApp"],
                },
                {
                    name: "Engagement & Automation",
                    desc: "Marketing automation",
                    modules: ["Automated Marketing"],
                },
                {
                    name: "Internal Communication",
                    desc: "Discuss, Notice Board",
                    modules: ["Discuss", "Notice Board"],
                },
            ],
        },
        {
            key: "ODCOR",
            name: "ODOO-CORE Platform",
            description: "Core Infrastructure & Platform",
            projectTypeKey: "software",
            projectTemplateKey: "com.pyxis.greenhopper.jira:gh-scrum-template",
            epics: [
                {
                    name: "Platform Foundation",
                    desc: "Multi Campus, Settings, Apps",
                    modules: ["Multi Campus", "Settings", "Apps"],
                },
                {
                    name: "Collaboration Tools",
                    desc: "Calendar, Documents, E-sign",
                    modules: ["Calendar", "Documents", "E-sign", "Spreadsheets"],
                },
                {
                    name: "Analytics & Reporting",
                    desc: "Dashboards, KPIs",
                    modules: ["Dashboards", "KPI Dashboard"],
                },
                {name: "Master Data", desc: "Contacts", modules: ["Contacts"]},
            ],
        },
    ];

    const components = [
        "Frontend/UI",
        "Backend/API",
        "Database",
        "Integration",
        "Infrastructure",
        "Security",
    ];

    let successCount = 0;
    let failCount = 0;

    for (const projectData of projects) {
        try {
            console.log(`\n${"=".repeat(60)}`);
            console.log(`📦 Creating: ${projectData.name}`);
            console.log("=".repeat(60));

            // Create project
            let project;
            try {
                project = await jira.projects.createProject({
                    key: projectData.key,
                    name: projectData.name,
                    description: projectData.description,
                    projectTypeKey: projectData.projectTypeKey,
                    projectTemplateKey: projectData.projectTemplateKey,
                    leadAccountId: currentUserId,
                });
                console.log(`✓ Project ${projectData.key} created`);
            } catch (error) {
                if (error.response?.status === 400) {
                    console.log(`⚠ Project ${projectData.key} exists, continuing...`);
                    project = await jira.projects.getProject({
                        projectIdOrKey: projectData.key,
                    });
                } else {
                    throw error;
                }
            }

            await new Promise((r) => setTimeout(r, 1500));

            // Create components
            console.log("\n  🔧 Components:");
            for (const comp of components) {
                try {
                    await jira.projectComponents.createComponent({
                        name: comp,
                        project: projectData.key,
                    });
                    console.log(`     ✓ ${comp}`);
                } catch (e) {
                    console.log(`     ⚠ ${comp} (exists)`);
                }
            }

            // Create epics
            console.log("\n  📋 Epics:");
            for (let i = 0; i < projectData.epics.length; i++) {
                const epic = projectData.epics[i];
                try {
                    const issue = await jira.issues.createIssue({
                        fields: {
                            project: {key: projectData.key},
                            summary: epic.name,
                            description: {
                                type: "doc",
                                version: 1,
                                content: [
                                    {
                                        type: "paragraph",
                                        content: [{type: "text", text: epic.desc}],
                                    },
                                ],
                            },
                            issuetype: {name: "Epic"},
                        },
                    });
                    console.log(
                        `     ✓ E${String(i + 1).padStart(2, "0")}: ${epic.name} (${issue.key})`
                    );

                    // Create 1 sample story
                    if (epic.modules.length > 0) {
                        try {
                            const story = await jira.issues.createIssue({
                                fields: {
                                    project: {key: projectData.key},
                                    summary: `Implement ${epic.modules[0]} - Setup`,
                                    description: {
                                        type: "doc",
                                        version: 1,
                                        content: [
                                            {
                                                type: "paragraph",
                                                content: [
                                                    {
                                                        type: "text",
                                                        text: `Setup ${epic.modules[0]} module`,
                                                    },
                                                ],
                                            },
                                        ],
                                    },
                                    issuetype: {name: "Story"},
                                    parent: {key: issue.key},
                                },
                            });
                            console.log(`        → Sample story: ${story.key}`);
                        } catch (e) {
                            console.log(`        ⚠ Story creation skipped`);
                        }
                    }

                    await new Promise((r) => setTimeout(r, 800));
                } catch (error) {
                    console.log(`     ✗ ${epic.name}: ${error.message}`);
                }
            }

            successCount++;
            await new Promise((r) => setTimeout(r, 2000));
        } catch (error) {
            console.error(`✗ Failed: ${projectData.name}`);
            console.error(`  Error: ${error.message}`);
            failCount++;
        }
    }

    return {successCount, failCount, total: projects.length};
}

async function main() {
    try {
        console.log("This script will set up your complete Jira Scrum architecture.\n");
        console.log("What will be created:");
        console.log("  • 5 Jira projects (ODEDU, ODHR, ODBUS, ODCOM, ODCOR)");
        console.log("  • 17 epics across all projects");
        console.log("  • Sample stories for each epic");
        console.log("  • Components and structure\n");

        const email = "abdelhadieddiraa4@gmail.com";
        const apiToken =
            "ATATT3xFfGF0NljpDQUco6gAqyhJsnqdt73wNqYnLkoAwIOI0l5WcZhUA-2CLX5EfPdYI2EoLNjGaPYxNUc7BNROg6CEqXIy5pRgaBnLqXUxVv4eWJc7PrINsg2acrwzj1xUxApIV6h41HziVHdkCOcjf4vDDA0VzSL7oAT7bSaP-yK7DjxiKrc=5F72132C";

        console.log("\n🔐 Verifying credentials...");
        const auth = await verifyCredentials(email, apiToken);

        if (!auth) {
            console.log("Please check your email and try again.");
            rl.close();
            return;
        }

        const proceed = "yes";
        if (proceed.toLowerCase() !== "yes" && proceed.toLowerCase() !== "y") {
            console.log("\nSetup cancelled.");
            rl.close();
            return;
        }

        console.log("\n🚀 Starting setup...\n");
        console.log("This will take 5-10 minutes. Please wait...\n");

        const results = await setupProjects(auth.jira, auth.user.accountId);

        console.log("\n\n" + "=".repeat(60));
        console.log("SETUP COMPLETE");
        console.log("=".repeat(60));
        console.log(
            `\n✅ Successfully created: ${results.successCount}/${results.total} projects`
        );
        if (results.failCount > 0) {
            console.log(`⚠️  Failed: ${results.failCount}/${results.total} projects`);
        }

        console.log("\n📋 Next Steps:");
        console.log(
            "   1. Visit: https://abdelhadieddiraa4-1768918580829.atlassian.net"
        );
        console.log("   2. Review your projects and epics");
        console.log("   3. Configure boards and workflows");
        console.log("   4. Invite team members");
        console.log("   5. Start your first sprint!\n");

        console.log("📚 See odoo_jira_scrum_architecture.md for detailed guidelines\n");

        rl.close();
    } catch (error) {
        console.error("\n❌ Setup failed:", error.message);
        rl.close();
        process.exit(1);
    }
}

main();
