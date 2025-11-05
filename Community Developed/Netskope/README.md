# Collect authentication info from Netskope #

To integrate with QRadar, you need to add a Netskope connector in QRadar's Universal REST connector. To do so, you'll need to first collect the following authentication information from Netskope:

- Netskope Tenant Hostname
- API Token

# Netskope Tenant Hostname #

To find your Netskope Tenant Hostname:

1. Log in to Netskope portal, then take the hostname from the URL.
2. Copy the Netskope URL and remove “https://” if it is there at the start of URL.

# API Token #

To create an API Token, Follow the steps from the documentation of Netskope - <https://docs.netskope.com/en/rest-api-v2-overview-312207>
Make sure to add required endpoints while creating API Token. Supported Endpoints are listed [here](#supported-events-and-alerts-types)

# QRadar Log Source Configuration #

If you want to ingest data from an endpoint using Universal Rest API Protocol, configure a log source on the QRadar® Console using the Workflow field so that the defined endpoint can communicate with QRadar by using the Universal Rest API protocol.

1. Log in to QRadar.
2. Click the *Admin* tab.
3. To open the app, click the *QRadar Log Source Management* app icon.
4. Click *New Log Source* > Single Log Source.


## 1. Select Log Source Type ##
1. Select *Netskope* log source type. 
2. Click *Select Protocol Type* to go to the next section.

## 2. Select Protocol Type ##
1. Select *Universal Cloud Rest API* protocol type. 
2. Click *Configure Log Source Parameters* to go to the next section.
3. If option "Universal Cloud Rest API" is not available in protocol type, then uninstall the Netskope app from extensions management, install the Universal Cloud Rest API Protocol and then install the Netskope app.

## 3. Configure Log Source Parameters ##
1. Name is the name of the Log Source and it can be kept anything based on the user's choice.
2. Select "NetskopeCustom_ext" Extension. It is used for post processing of events.
3. Disable *Coalescing Events* to avoid grouping of the events on the basis of Source and Destination IP. 
4. Except for the above fields everything can be kept as their default values or if needed can be changed by the QRadar admin.
5. Click *Configure Protocol Parameters* to go to the next section. 

## 4. Configure Protocol Parameters ##
1.  Add "Log Source Identifier" of your choice.
2.  Copy the content of the any workflow file in "Workflow". List of the workflow files can be found [here](#supported-events-and-alerts-types).
3.  Modify the content as per user specification in the file Netskope-Workflow-Parameter-Values.xml and add in "Workflow Parameter Values".
4.  Create new log sources and repeat **QRadar Log Source Configuration** steps to collect other data and use the files as Workflow listed [here](#supported-events-and-alerts-types).
5.  Recurrence is the time interval between each execution of the workflow. It can be modified according the user's requirement, default value would be 10 minutes. Recommended value is 1 minutes.
6.  Except for the above fields everything can be kept as their default values or if needed can be changed by the QRadar admin.
7.  Click *Test Protocol Parameters* to test the entered workflow files.

## 5. Test Protocol Parameters ##
1.  Click *Start Test* to start the testing of the entered workflows, once it is finished click *Finish*.
2.  Deploy the configuration from admin panel.

# Workflow Parameter Description #
1. tenantHostName: The Netskope Tenant Hostname to fetch the events from Netskope. If your URL is https://example.com/accounts then enter example.com
2. apiToken: The API Token obtained from Netskope portal.
3. operationIndex: Enter the value of operationIndex. Accepted values are ["head","tail",epoch timestamp]. **Note**: The parameter ‘operationIndex’ is only used during the initial configuration of the workflow. Once data collection begins, the API will only use the value 'next'.
4. indexParam: A unique identifier. This will be used to create an iterator.

# Supported Events and Alerts Types #

| Workflow Name | Events/Alerts will be collected | API Endpoint |
| --- | --- | --- |
| Netskope-Compromised-Credential-Alert-Workflow.xml | Compromised Credential Alert | /api/v2/events/dataexport/alerts/compromisedcredential |
| Netskope-Content-Alert-Workflow.xml | Content Alert | /api/v2/events/dataexport/alerts/content |
| Netskope-CTEP-Alert-Workflow.xml | CTEP Alert | /api/v2/events/dataexport/alerts/ctep |
| Netskope-Device-Alert-Workflow.xml | Device Alert | /api/v2/events/dataexport/alerts/device |
| Netskope-DLP-Alert-Workflow.xml | DLP Alert | /api/v2/events/dataexport/alerts/dlp |
| Netskope-Malsite-Alert-Workflow.xml | Malsite Alert | /api/v2/events/dataexport/alerts/malsite |
| Netskope-Malware-Alert-Workflow.xml | Malware Alert | /api/v2/events/dataexport/alerts/malware |
| Netskope-Policy-Alert-Workflow.xml | Policy Alert | /api/v2/events/dataexport/alerts/policy |
| Netskope-Quarantine-Alert-Workflow.xml | Quarantine Alert | /api/v2/events/dataexport/alerts/quarantine |
| Netskope-Remediation-Alert-Workflow.xml | Remediation Alert | /api/v2/events/dataexport/alerts/remediation |
| Netskope-Security-Assessment-Alert-Workflow.xml | Security Assessment Alert | /api/v2/events/dataexport/alerts/securityassessment |
| Netskope-UBA-Alert-Workflow.xml | UBA Alert | /api/v2/events/dataexport/alerts/uba |
| Netskope-Watchlist-Alert-Workflow.xml | Watchlist Alert | /api/v2/events/dataexport/alerts/watchlist | 
| Netskope-Alert-Event-Workflow.xml | Alert Event | /api/v2/events/dataexport/events/alert |
| Netskope-Application-Event-Workflow.xml | Application Event | /api/v2/events/dataexport/events/application |
| Netskope-Audit-Event-Workflow.xml | Audit Event | /api/v2/events/dataexport/events/audit |
| Netskope-Connection-Event-Workflow.xml | Connection Event | /api/v2/events/dataexport/alerts/connection | 
| Netskope-Endpoint-Event-Workflow.xml | Endpoint Event | /api/v2/events/dataexport/events/endpoint | 
| Netskope-Incident-Event-Workflow.xml | DLP Incident | /api/v2/events/dataexport/events/incident | 
| Netskope-Infrastructure-Event-Workflow.xml | Infrastructure Event | /api/v2/events/dataexport/events/infrastructure | 
| Netskope-Network-Event-Workflow.xml | Network Event | /api/v2/events/dataexport/events/network |
| Netskope-Page-Event-Workflow.xml | Page Event | /api/v2/events/dataexport/events/page |

Note: Data retrieved through the workflow “Netskope-Incident-Event-Workflow.xml” will be
parsed as a “DLP Incident” in QRadar.