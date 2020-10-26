
## SecurityBridge for SAP
The connector works in combination with SecurityBridge addon for SAP.
https://securitybridge.com/siem-integration-for-sap/

#### HTTP over SSL:
(!) We strongly recommend to encrypt data in transfer.
Depending on your SAP system configuration HTTP over SSL may not be configured. In this case please use parameter "ssl_enabled"
with value "false", otherwise set it to "true".

The 'API User' and 'API User password' has to be provided by the SAP User Administrator.

#### Documentation of 
SecurityBridge REST API: https://abap-experts.atlassian.net/servicedesk/customer/portal/1/article/708804780?src=-1705466695
Tutorial Universal REST API with SecurityBridge: https://abap-experts.atlassian.net/wiki/spaces/SB/pages/1840349274/IBM+QRadar+-+Integration+tutorial

```NOTE```:
The SecurityBridge REST API within SAP needs to be enabled before QRadar will be able to acquire
data from SAP. The SAP log APIs will provide only new data to QRadar. We recommend to synchronize the call
frequency with the SecurityBridge Intrusion Detection job frequency which is set in minutes in order to maximize the efficiency.
For this reason, this workflow uses the `minimumRecurrence` and was set to 1 minute.
