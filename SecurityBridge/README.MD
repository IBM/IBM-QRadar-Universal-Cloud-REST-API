## SecurityBridge for SAP
The connector works in combination with the SecurityBridge addon for SAP.
https://securitybridge.com/siem-integration-for-sap/

#### HTTP over SSL:
(!) We strongly recommend encrypting data in transfer.
Depending on your SAP system configuration HTTP over SSL may not be configured. In this case please use the parameter "ssl_enabled"
with value "false", otherwise, set it to "true".

The 'API User' and 'API User password' has to be provided by the SAP User Administrator.

#### Documentation of 
- SecurityBridge REST API: https://abap-experts.atlassian.net/servicedesk/customer/portal/1/article/708804780?src=-1705466695 (Login required)

- Tutorial Universal REST API with SecurityBridge: https://abap-experts.atlassian.net/servicedesk/customer/portal/1/article/1840349274?src=1077970461 (Login required)


```RELEVANT NOTES```:

The SecurityBridge REST API within SAP must be enabled before QRadar can acquire data from SAP. The endpoint can be invoked in two different scenarios. The "Generic mode" will flag all events pulled to QRadar as delivered within SAP. Events that have been flagged as delivered will not be exposed again thus each call receives the delta of new events since the last pull. As a second option, the workflow can be configured to acquire events in delta mode (using a bookmark). Using the "Bookmark mode" will not change the output status of events and can be i.e. used to pull data into reporting solutions.


_Option 1:_ Generic mode

Parameter: 

```bookmark_enabled = False```

The SAP log API's will provide only new data to QRadar. We recommend synchronizing the call frequency with the SecurityBridge Intrusion Detection job frequency which is set in minutes to maximize efficiency.

For this reason, this workflow uses the `minimumRecurrence` and was set to 1 minute.


_Option 2:_ Bookmark mode

Parameter: 

```bookmark_enabled = True```

Is this option active, the workflow will invoke the SAP endpoint with a filter on date and time. Please note, whether or not the data has been pulled, is not visible in SAP, this can only be checked in QRadar. 