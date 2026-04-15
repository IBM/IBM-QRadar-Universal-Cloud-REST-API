Author Name: bizdevtech@cyberark.com
Maintainer Name: Compostcy
Version Number: 1.0
Version Description: add ISPSS authentication to EPM events retrieval

EPM Configuration
-----------------
Steps to obtain an integration with QRadar:
1). ISPSS authentication configs and EPM API region host these need to be fill into the xml parameter file.
https://api-docs.cyberark.com/create-api-token/docs/create-api-token
<identity_host> - the id of the identity tenant. I.E.: abc9876.id.cyberark.cloud
<api_host> - the EPM host of the region to retrieve the EPM tenant url, api-{region}.epm.cyberark.cloud where region = [na,eu,it,ch,uk,au,ca,in,jp,sg,ae,br] I.E.: api-na.epm.cyberark.cloud

2). There are 3 log source type:
EPM – EPM aggregated events. This fetch 7 days backlog on first run. 
https://docs.cyberark.com/EPM/Latest/en/Content/WebServices/GetAggregatedEvents.htm
Log source identifier must be named:  <identity_host>_Events

EPM-AdminAudit1 – EPM admin audit. This fetch 1 day backlog on first run.
https://docs.cyberark.com/EPM/Latest/en/Content/WebServices/GetAccountAdminAudit.htm
Log source identifier must be named:  <identity_host>_AdminAudits

EPM-Policy – EPM aggregated policy audits. This fetch 7 days backlog on first run.
https://docs.cyberark.com/EPM/Latest/en/Content/WebServices/GetAggregatedPolicyAudits.htm
Log source identifier must be named:  <identity_host>_Policies

QRadar Log Source Configuration
--------------------------------
Please follow the root ReadMe for configuring within QRadar.


Troubleshooting 
-------------------
You can extract the debug run of the workflow from /var/log/qradar.log into a file and share the file with Cyberark support. Each workflow has 
a specific prefix for logging.

For event workflow:
grep “ISPSS-EPM::AggEvent” qradar.log > aggevent.log

For policy workflow:
grep “ISPSS-EPM:AggPolicy” qradar.log > aggpolicy.log

For admin audit workflow:
grep “ISPSS-EPM::AdminAudit” qradar.log > aggaudit.log

You can also grep on the ISPSS-EPM:: prefix to capture logs for all 3 workflows. Example:

[root@host-1 log]# grep “ISPSS-EPM::" qradar.log
Apr  6 17:38:09 ::ffff:10.0.0.1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-1758074] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][10.0.0.1/- -] [-/- -]ISPSS-EPM::AdminAudit - The EPM Bookmark value was 1775331106165 : 2026-04-04T19:31:46.165Z
Apr  6 17:38:11 ::ffff:10.0.0.1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-1758074] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][10.0.0.1/- -] [-/- -]ISPSS-EPM::AdminAudit - 200 : OK
Apr  6 17:38:11 ::ffff:10.0.0.1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-1758074] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][10.0.0.1/- -] [-/- -]ISPSS-EPM::AdminAudit - e41f896a-eb09-485c-9f3d-bebd2ffa0d5e : SaaSCorps Bizdevtech2/bizdevtech@cyberark.(saascorps bizdevtech2)
Apr  6 17:38:11 ::ffff:10.0.0.1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-1758074] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][10.0.0.1/- -] [-/- -]ISPSS-EPM::AdminAudit - offset : 0 : count=0 : datefrom=2026-04-04T19:31:46.165Z : dateto=2026-04-06T21:38:09.137Z
Apr  6 17:38:12 ::ffff:10.0.0.1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-1758074] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][10.0.0.1/- -] [-/- -]ISPSS-EPM::AdminAudit - e41f896a-eb09-485c-9f3d-bebd2ffa0d5e : 200 : OK
Apr  6 17:38:12 ::ffff:10.0.0.1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-1758074] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][10.0.0.1/- -] [-/- -]ISPSS-EPM::AdminAudit - DoWhile #records for setID e41f896a-eb09-485c-9f3d-bebd2ffa0d5e : 59
Apr  6 17:38:12 ::ffff:10.0.0.1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-1758074] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][10.0.0.1/- -] [-/- -]ISPSS-EPM::AdminAudit - offset : 500 : count=59 : datefrom=2026-04-04T19:31:46.165Z : dateto=2026-04-06T21:38:09.137Z
Apr  6 17:38:13 ::ffff:10.0.0.1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-1758074] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][10.0.0.1/- -] [-/- -]ISPSS-EPM::AdminAudit - e41f896a-eb09-485c-9f3d-bebd2ffa0d5e : 200 : OK
Apr  6 17:38:13 ::ffff:10.0.0.1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-1758074] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][10.0.0.1/- -] [-/- -]ISPSS-EPM::AdminAudit - DoWhile #records for setID e41f896a-eb09-485c-9f3d-bebd2ffa0d5e : 118
Apr  6 17:38:13 ::ffff:10.0.0.1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-1758074] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][10.0.0.1/- -] [-/- -]ISPSS-EPM::AdminAudit - offset : 1000 : count=59 : datefrom=2026-04-04T19:31:46.165Z : dateto=2026-04-06T21:38:09.137Z
Apr  6 17:38:14 ::ffff:10.0.0.1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-1758074] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][10.0.0.1/- -] [-/- -]ISPSS-EPM::AdminAudit - e41f896a-eb09-485c-9f3d-bebd2ffa0d5e : 200 : OK


