#!/usr/bin/env node

const JiraApi = require("jira.js").default;

const jira = new JiraApi({
    host: "https://abdelhadieddiraa4-1768918580829.atlassian.net",
    authentication: {
        basic: {
            email: process.argv[2] || "unknown",
            apiToken:
                "ATATT3xFfGF0NljpDQUco6gAqyhJsnqdt73wNqYnLkoAwIOI0l5WcZhUA-2CLX5EfPdYI2EoLNjGaPYxNUc7BNROg6CEqXIy5pRgaBnLqXUxVv4eWJc7PrINsg2acrwzj1xUxApIV6h41HziVHdkCOcjf4vDDA0VzSL7oAT7bSaP-yK7DjxiKrc=5F72132C",
        },
    },
});

async function testConnection(email) {
    try {
        const user = await jira.myself.getCurrentUser();
        console.log("✅ Connection successful!");
        console.log(`Email: ${user.emailAddress}`);
        console.log(`Name: ${user.displayName}`);
        console.log(`Account ID: ${user.accountId}`);
        return user.emailAddress;
    } catch (error) {
        console.error("❌ Connection failed:", error.message);
        process.exit(1);
    }
}

if (!process.argv[2]) {
    console.log("Usage: node get-jira-user.js YOUR_EMAIL@example.com");
    process.exit(1);
}

testConnection(process.argv[2]);
