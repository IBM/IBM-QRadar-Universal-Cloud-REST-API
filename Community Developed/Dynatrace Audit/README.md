Dynatrace Audit Configuration
-----------------

1). Steps to obtain an integration with QRadar:

Easily check configuration changes or environment sign ins with the new Audit logs API
https://www.dynatrace.com/news/blog/easily-check-configuration-changes-or-environment-sign-ins-with-the-new-audit-logs-api/

2). There are the following source type:

Audit logs API - GET audit log
https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/audit-logs/get-log


QRadar Log Source Configuration
--------------------------------
Please follow the root ReadMe for configuring within QRadar.


Workflow parameters
--------------------------------

```xml
<WorkflowParameterValues xmlns="http://qradar.ibm.com/UniversalCloudRESTAPI/WorkflowParameterValues/V1">
    <Value name="host" value="dynlocal.company.com/e/XXXXX-XXXXX-XXXXX-XXXX" />
    <Value name="apiToken" value="dt0c01.XXXXXX.XXXXXXXXXXXXXXXXXXXX" />    
    <Value name="fromTime" value="now-1d" />
</WorkflowParameterValues>
```

where:

- `host`: hostname of your Dynatrace instance
- `apiToken`: Access Token with admin privileges
- `fromTime`: The start of the requested timeframe. Default value: `now-2w`, the last 2 weeks.


In `host`, depends on your environment. For:

- SaaS:	{your-environment-id}.live.dynatrace.com/api/v2/auditlogs
- Environment ActiveGateCluster ActiveGate:	{your-activegate-domain}:9999/e/{your-environment-id}

In `fromTime`. You can use multiple formats, but my sugestion is to use Relative timeframe, back from now. Example: `now-5m`, the last 5 minutes.

Supported time units for the relative timeframe are:

- `m`: minutes
- `h`: hours
- `d`: days
- `w`: weeks
- `M`: months
- `y`: years

Troubleshooting 
-------------------
You can extract the debug run of the workflow from /var/log/qradar.log into a file and share the file with Cyberark support. Each workflow has 
a specific prefix for logging.

For Dynatrace Audit Logs workflow:

```bash
grep "Dynatrace::AuditLogs" /var/log/qradar.log  > dynaudit.log
```

You can also grep on the “Dynatrace:: prefix to capture logs workflows. Here is a sample where the password was changed in EPM but not 
reflected in the workflow parameter xml file in Qradar.

```bash
[root@host-1 log]# grep "Dynatrace::" /var/log/qradar.log
```
