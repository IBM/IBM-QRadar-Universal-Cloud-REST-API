This Workflow fetches the logs via the Redrock API.  It fetches them in 2 minute increments as the API will timeout with big queries.  
It will begin fetching the logs stored in the API from 24 hours before it first runs, giving a 24 hours backlog.  This is tunable in the Workflow.
It will fetch up to 30 minutes worth of logs per invocation, we suggest shceduling it to run every minute.  This means it will take around an hour 
to get the 24 hours indexed and to start getting current logs.

There is currently no mechanism to filter out the NULL valued fields from the API response but we will do a fix when it becomes possible.

# CyberArk Idaptive Configuration

Please refer to the SIEM integration gudie provided by CyberArk here:
https://docs.cyberark.com/Product-Doc/OnlineHelp/Idaptive/Latest/en/integrations/Idaptive-SIEM-Integration-Guide.pdf

You only need to complete the following section:
"Setting up the SIEM User and the OAuth App on the Tenant"

When you folow the guide you will create a user, role and webapp.

When creating the user, note the following for the Parameters later:
-   Username (include suffix)
-   Password
When Creating the WebApp (OAuth2 Client), note the following for the Parameters later:
-   Application ID
-   Scope
Finally you will need your tenant url, something like "myOrg.my.idaptive.app"


# QRadar Log Source Configuration
Please follow the root ReadMe for configuring within QRadar.
