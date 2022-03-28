### Workflow basic information:

* Author: Daniel Wendler
* Maintainer: dwendler, dwendler(at)de(dot)ibm(dot)com
* Workflow Version Number: 1.0
* [Endpoint Documentation of Spectrum Protect Plus REST API](https://www.ibm.com/docs/en/SSNQFQ_10.1.10/pdf/restapi.pdf)
* [SPP landing page](https://www.ibm.com/docs/en/spp/10.1.10)
* supported endpoints: Audit Logs via api/endeavour/log/audit


### Workflow parameters

* #host# (required): IP_Address or Hostname, no protocol prefix, e.g. "mySppHost.myCompany.com" will be assebled to https://mySppHost.myCompany.com:443 
* #port# (not required, default is 443): 443
* #username# (required): e.g. monitorUser, this user needs the correct RBAC within SPP to query the SPP audit logs
* #password# (required): password of above user
* #pageSize# (not required, leave default): number of audit log entries to retrieve with a single REST API get operation, the workflow will use pagination until no new events exist in the audit log queue. default = 100 is suggested by the API for this endpoint


### tested REST API of IBM Spectrum Protect Plus versions:
This Workflow has been tested with SPP version 10.1.9 and 10.1.10. 
The SPP REST API in versions 10.1.8 and earlier do not provide the required 
information and functionalities required by this workflow.

### QRadar Log Source Configuration

If you want to ingest data from an endpoint using Universal Rest API Protocol, configure a log source on the QRadar® Console using the Workflow field so that the defined endpoint can communicate with QRadar by using the Universal Rest API protocol.

1. Log in to QRadar.
2. Click the _Admin_ tab.
3. To open the app, click the _Log Sources_ app icon and _launch_ the app to select _Log Sources - Manage Log Sources_ 
4. Click _New Log Source_ > _Single Log Source_.
5. On the _Select a Log Source Type_ page, Select the Log Source Type _Universal DSM_ and click _Select Protocol Type_ >  _Universal Cloud REST API_.
6. *Important:* disable the function _Coalescing Events_, otherwise, similar Audit Logs may be interpreted as a single event. 
7. On the Select a Protocol Type page, select a protocol and click _Configure Log Source Parameters_.
8. On the Configure the Log Source parameters page, configure the log source parameters and click _Configure Protocol
Parameters_.
9. On the Configure the Protocol Parameters page, configure the protocol-specific parameters (Workflow and Workflow
Parameter Values). 
10. In the Test protocol parameters window, click _Start Test_.
11. To fix any errors, click _Configure Protocol Parameters_. Configure the parameters and click Test Protocol Parameters.
12. Click _Finish_

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