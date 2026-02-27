# Atlassian Jira
The Jira workflow collects audit logs from audit API.

## Authentication Set-Up
When setting up the workflow for Atlassian Cloud you will need to use the "Jira User Identifier" and "Jira API Token" fields in the Workflow Parameter Values file. These will allow connection to the [Atlassian Cloud REST API](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/) via [Basic Authentication](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/).

You need to uncheck Coalescing Events option during log source configuration. 
