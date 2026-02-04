# Collect authentication info from XM Cyber #

To integrate with QRadar, you need to add a XM Cyber log source with QRadar's Universal REST protocol. To do so, you'll need to first collect the following authentication information from XM Cyber:

- XM Cyber Hostname
- XM Cyber API Key

# XM Cyber Hostname #

To find your XM Cyber Hostname:

1. Log in to XM Cyber, then take the hostname from the URL.
2. If XM Cyber URL is https://your-tenant.clients.xmcyber.com/login, enter hostname as **your-tenant.clients.xmcyber.com**

# API Key #

To create an API Key, follow the below steps:
1. Log in to XM Cyber.
2. Go to System Config > Integrations > XM API.
3. Click View/generate API keys. The API keys table appears.
4. Click + Create API key
5. Complete the following fields:
   1. Application name: Enter the name of the key, which is how it will appear in the API keys table.
   2. Description: Describe the purpose or usage of the API key.
   3. Expiration: Select the number of months until the key expires.
6. Click Assign Roles.
7. For each API scope, assign the roles Read.
8. Click Create. The Copy & Save tab appears with your key.
9. Copy and save your key now. Important: Once you close the window, you will not be able to recover the key for security


# QRadar Log Source Configuration #

If you want to ingest data from an endpoint using Universal Rest API Protocol, configure a log source on the QRadar® Console using the Workflow field so that the defined endpoint can communicate with QRadar by using the Universal Rest API protocol.

1. Log in to QRadar.
2. Click the *Admin* tab.
3. To open the app, click the *QRadar Log Source Management* app icon.
4. Click *New Log Source* > Single Log Source.


## 1. Select Log Source Type ##
1. Select *XM Cyber* log source type. 
2. Click *Select Protocol Type* to go to the next section.

## 2. Select Protocol Type ##
1. Select *Universal Cloud Rest API* protocol type. 
2. Click *Configure Log Source Parameters* to go to the next section.
3. If option "Universal Cloud Rest API" is not available in protocol type, then uninstall the XM Cyber app from extensions management, install the Universal Cloud Rest API Protocol and then install the XM Cyber app.

## 3. Configure Log Source Parameters ##
1. Name is the name of the Log Source and it can be kept anything based on the user's choice.
2. Select "XMCyberCustom_ext" Extension. It is used for post processing of events.
3. Disable *Coalescing Events* to avoid grouping of the events on the basis of Source and Destination IP. 
4. Except for the above fields everything can be kept as their default values or if needed can be changed by the QRadar admin.
5. Click *Configure Protocol Parameters* to go to the next section. 

## 4. Configure Protocol Parameters ##
1.  Add "Log Source Identifier" of user's choice.
2.  Copy the content of the any workflow file in "Workflow". List of the workflow files can be found [here](#supported-events-types).
3.  Modify the content as per user specification in the file XM-Cyber-Workflow-Parameter-Values.xml and add in "Workflow Parameter Values".
4.  Create new log sources and repeat **QRadar Log Source Configuration** steps to collect other data and use the files as Workflow listed [here](#supported-events-types).
5.  Recurrence is the time interval between each execution of the workflow. Input the value as 1D, default value would be 10 minutes.
6.  Except for the above fields everything can be kept as their default values or if needed can be changed by the QRadar admin.
7.  Click *Test Protocol Parameters* to test the entered workflow files.

## 5. Test Protocol Parameters ##
1.  Click *Start Test* to start the testing of the entered workflows, once it is finished click *Finish*.
2.  Deploy the configuration from admin panel.

# Workflow Parameter Description #
1. tenantName: The API Endpoint Hostname to fetch the events from XM Cyber. If your URL is https://your-tenant.clients.xmcyber.com/login then enter **your-tenant.clients.xmcyber.com**
2. apiKey: The API Key obtained from XM Cyber portal.
3. auditTrailsStartTime: Required for Audit Trails collection. Defines the start time for collecting Audit Trails data. Provide the Audit Trails start time in the format YYYY-MM-DDTHH:MM:SS.SSSZ 
4. ingestChokepointStats: Required for Entities collection. If set to True, entities chokepoint statistics will also be ingested into QRadar as an event after entity data collection. 
5. ingestScenarios: Required for Security Score collection. If set to True, scenarios data collected during Security Score data collection will also be ingested into QRadar.
6. timeId: Required for Security Score collection. Defines the start time for collecting Security Score data. Must be from [timeAgo_days_7, timeAgo_days_14, timeAgo_days_30, timeAgo_days_365].

# Supported Events Types #

| Workflow Name | Events will be collected | API Endpoint |
| --- | --- | --- |
| XMCyber-AuditTrails-Workflow.xml | Audit Trail | /api/audit-trail/auditRecords |
| XMCyber-Entities-Workflow.xml | Compromised Entity, Entity, Entity Chokepoint | /api/v2/reports/data/scenariosCriticalAssetsReport/entities, /api/entityInventory/entities, /api/v2/reports/data/scenariosChokePointsReport/chokePointsEntities |
| XMCyber-Devices-Workflow.xml | Device | /api/v2/vavm/devices |
| XMCyber-FindingsExposures-Workflow.xml | Finding and Exposure | /api/v2/reports/data/scenariosExposureReport/exposures |
| XMCyber-Products-Workflow.xml | Products | /api/v2/vavm/public/products |
| XMCyber-Scenarios-Workflow.xml | Scenario | /api/scenariosInfo/scenarios |
| XMCyber-SecurityScore-Workflow.xml | Security Score, Security Score Scenario | /api/systemReport/riskScoreV2 |
| XMCyber-Sensors-Workflow.xml | Sensor | /api/sensors |
| XMCyber-Vulnerabilities-Workflow.xml | Vulnerability | /api/v2/vavm/public/vulnerabilities |