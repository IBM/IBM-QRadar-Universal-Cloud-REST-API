### IBM Spectrum Protect Plus REST API:
* [SPP landing page](https://www.ibm.com/docs/en/spp/10.1.10)
* [SPP REST API Doc](https://www.ibm.com/docs/en/SSNQFQ_10.1.10/pdf/restapi.pdf)

### tested Spectrum Protect Plus versions:
This Workflow has been tested with SPP version 10.1.9 and 10.1.10. 
The SPP REST API in versions 10.1.8 and earlier do not provide the required 
information and functionalities required by this workflow.


### sample API response of an audit log entry

```
{
  "accessTime": 1648475990938,
  "serverTime": 1648475990938,
  "user": "monitorUser",
  "groups": "",
  "operation": "Login",
  "description": "Login failed for user monitorUser.",
  "requesterIp": "AAA.BBB.CCC.100",
  "sppserver": "AAA.BBB.CCC.120"
}
```


### conversion from epoch time to date and vice versa

**Note:** SPP utilizes epoch timestamp in milliseconds -> multiply / devide with 1000 may be required

```
date +%s               # converts local time to epoch time in seconds (not MS)
date -d @1648466798    # convert epoch timestamp in seconds (not MS) to local date
```


### sample test tool execution and debug logs - sanitized

> time /opt/qradar/bin/test-workflow.sh -u -w /tmp/spp/spp-Workflow.xml -wp /tmp/spp/spp-Workflow-Parameter-Values.xml
```
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
2022-03-28 16:30:59 [INFO ][LogAction] [NOT:0000006000][QRadarInstance1/- -] [-/- -]SPP IQUCRA> debug: true
2022-03-28 16:30:59 [INFO ][LogAction] [NOT:0000006000][QRadarInstance1/- -] [-/- -]SPP IQUCRA> bookmark (start): 1648461176749
2022-03-28 16:30:59 [INFO ][LogAction] [NOT:0000006000][QRadarInstance1/- -] [-/- -]SPP IQUCRA> counter (start): 0
2022-03-28 16:30:59 [INFO ][LogAction] [NOT:0000006000][QRadarInstance1/- -] [-/- -]SPP IQUCRA> URL: https://AAA.BBB.CCC.100:443/api/endeavour/log/audit
2022-03-28 16:30:59 [INFO ][UniversalCloudRESTAPITest] Received 1 events from AAA.BBB.CCC.100
2022-03-28 16:30:59 [INFO ][UniversalCloudRESTAPITest] {"accessTime":1648461176749,"serverTime":1648461176749,"user":"restapiuser","groups":"","operation":"Login","description":"Login failed for user restapiuser (request originated from IP address: AAA.BBB.CCC.120).","requesterIp":"AAA.BBB.CCC.120","sppserver":"AAA.BBB.CCC.100"}

...

2022-03-28 16:31:01 [INFO ][LogAction] [NOT:0000006000][QRadarInstance1/- -] [-/- -]SPP IQUCRA> bookmark (queryPage): 1648475895751
2022-03-28 16:31:01 [INFO ][LogAction] [NOT:0000006000][QRadarInstance1/- -] [-/- -]SPP IQUCRA> URL: https://AAA.BBB.CCC.100/api/endeavour/log/audit?sort=%5B%7B%22property%22%3A+%22accessTime%22%2C+%22direction%22%3A+%22ASC%22%7D%5D&filter=%5B%7B%22property%22%3A+%22accessTime%22%2C+%22op%22%3A+%22%3E%3D%22%2C+%22value%22%3A+%221648461176749%22%7D%5D&pageSize=100&pageStartIndex=100

...

2022-03-28 16:31:01 [INFO ][UniversalCloudRESTAPITest] Received 1 events from AAA.BBB.CCC.100
2022-03-28 16:31:01 [INFO ][UniversalCloudRESTAPITest] {"accessTime":1648477857858,"serverTime":1648477857858,"user":"monitorUser","groups":"","operation":"Login","description":"Login successful for user monitorUser.","requesterIp":"QRadarInstance1","sppserver":"AAA.BBB.CCC.100"}
2022-03-28 16:31:01 [INFO ][LogAction] [NOT:0000006000][QRadarInstance1/- -] [-/- -]SPP IQUCRA> bookmark (queryPage): 1648477857858
2022-03-28 16:31:01 [INFO ][LogAction] [NOT:0000006000][QRadarInstance1/- -] [-/- -]SPP IQUCRA> bookmark (final): 1648477857858
2022-03-28 16:31:01 [INFO ][LogAction] [NOT:0000006000][QRadarInstance1/- -] [-/- -]SPP IQUCRA> collected events: 114
```


### sample QRadar log output 

>tail -f /var/log/qradar.log  | grep SPP

```
Mar 28 16:13:19 ::ffff:QRadarInstance1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-7638764] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][QRadarInstance1/- -] [-/- -]SPP IQUCRA> debug: true
Mar 28 16:13:19 ::ffff:QRadarInstance1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-7638764] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][QRadarInstance1/- -] [-/- -]SPP IQUCRA> bookmark (start): 1648461176749
Mar 28 16:13:19 ::ffff:QRadarInstance1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-7638764] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][QRadarInstance1/- -] [-/- -]SPP IQUCRA> counter (start): 0
Mar 28 16:13:19 ::ffff:QRadarInstance1 [ecs-ec-ingress.ecs-ec-ingress] [Thread-7638764] com.q1labs.semsources.sources.universalcloudrestapi.v1.workflow.action.LogAction: [INFO] [NOT:0000006000][QRadarInstance1/- -] [-/- -]SPP IQUCRA> URL: https://AAA.BBB.CCC.100:443/api/endeavour/log/audit
```