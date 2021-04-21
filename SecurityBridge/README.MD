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

```slice = 1...9``` (new since v1.4)
Is this option active, the workflow will invoke the SAP endpoint with a filter on date and time. Please note, whether or not the data has been pulled, is not visible in SAP, this can only be checked in QRadar. An initial bookmark is set 1 day in the past in case the service is executed for the first time. 

Timeslices (New since Workflow version 1.4): For systems that record a high log volume IBM QRadar may run into a threshold at 100 MB for a service call. The ```slice``` parameter allows to define the duration in hour(s) of the timeslice that is used to pull data per iteration. Remains the parameter empty a default of 1 hour is set. 


#### HISTORY:
13-APRIL-2021

```v1.4```: 
- New:Bookmark mode enhancement to read event-api in slices of time. 
- Update: Bookmark default is set to 1 day back instead of 3 days. 