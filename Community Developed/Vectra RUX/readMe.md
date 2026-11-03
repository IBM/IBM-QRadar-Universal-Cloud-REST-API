# Collect authentication info from Vectra RUX #

To integrate with QRadar, you need to add a Vectra RUX connector in QRadar's Universal REST connector. To do so, you'll need to first collect the following authentication information from Vectra RUX:

- Vectra Hostname
- Client ID and Secret Key

# Vectra Hostname #

To find your Vectra Hostname:

1. Log in to Vectra RUX, then take the hostname from the URL.
2. Copy the Vectra URL and remove “https://” if it is there at the start of URL.

# Client ID and Secret Key #

To create an API client, Follow the steps from the documentation of Vectra API - <https://support.vectra.ai/s/article/KB-VS-1665>


# QRadar Log Source Configuration #

If you want to ingest data from an endpoint using Universal Rest API Protocol, configure a log source on the QRadar® Console using the Workflow field so that the defined endpoint can communicate with QRadar by using the Universal Rest API protocol.

1. Log in to QRadar.
2. Click the *Admin* tab.
3. To open the app, click the *QRadar Log Source Management* app icon.
4. Click *New Log Source* > Single Log Source.


## 1. Select Log Source Type ##
1. Select *Vectra RUX* log source type.
2. Click *Select Protocol Type* to go to the next section.

## 2. Select Protocol Type ##
1. Select *Universal Cloud Rest API* protocol type.
2. Click *Configure Log Source Parameters* to go to the next section.
3. If option "Universal Cloud Rest API" is not available in protocol type, then uninstall the Vectra RUX app from extensions management, install the Universal Cloud Rest API Protocol and then install the Vectra RUX app.

## 3. Configure Log Source Parameters ##
1. Name is the name of the Log Source and it can be kept anything based on the user's choice.
2. Select "VectraRUXCustom_ext" Extension. It is used for post processing of events.
3. Disable *Coalescing Events* to avoid grouping of the events on the basis of Source and Destination IP.
4. Except for the above fields everything can be kept as their default values or if needed can be changed by the QRadar admin.
5. Click *Configure Protocol Parameters* to go to the next section.

## 4. Configure Protocol Parameters ##
1.  Add "Log Source Identifier" of user's choice.
2.  Copy the content from file VectraRUX-Detection-Workflow.xml in "Workflow".
3.  Modify the content as per user specification in the file VectraRUX-Workflow-Parameter-Values.xml and add in "Workflow Parameter Values".
4.  Create new log sources and repeat **QRadar Log Source Configuration** steps to collect other data and use below files as Workflow.
      - For Entity Score data collection use VectraRUX-EntityScoring-Workflow.xml
      - For Audit data collection use VectraRUX-Audit-Workflow.xml
      - For Lockdown data collection use VectraRUX-Lockdown-Workflow.xml
      - For Health data collection use VectraRUX-Health-Workflow.xml
5.  Recurrence is the time interval between each execution of the workflow. It can be modified according the user's requirement, default value would be 10 minutes.
6.  Except for the above fields everything can be kept as their default values or if needed can be changed by the QRadar admin.
7.  Click *Test Protocol Parameters* to test the entered workflow files.

## 5. Test Protocol Parameters ##
1.  Click *Start Test* to start the testing of the entered workflows, once it is finished click *Finish*.
2.  Deploy the configuration from admin panel.

# Workflow Parameter Description #
1. clientId: The Client ID obtained from Vectra RUX portal.
2. secretKey: The Secret Key obtained from Vectra RUX portal.
3. vectraHostName: The API Endpoint Hostname to fetch the events from Vectra RUX. If your URL is https://example.com/accounts then enter example.com
4. historical: This flag will be considered only in the first run of the workflow, so that you can configure whether to pull the historical data in the first pull. If set to 'enable' it will pull the data from past 24 hours else it will pull from the current time. Must be from [enable, disable]. Applicable to Audit and Entity Scoring collections only.
5. from: Optional initial detection event checkpoint. Define id of the detection event to start collecting Detecction from there. Leave empty to start from the lookback window. Applicable to Detection collection only.
6. lookbackHours: Initial lookback window in hours to start collecting Detection from specific time. It will applicable when 'from' is empty. Default is 24 hours. Applicable to Detection collection only.
7. includeInfoCategory: Flag to include detections having an INFO category. If set to 'enable', such detections will also be collected. Must be from [enable, disable]. Applicable to Detection collection only.
8. includeTriaged: Flag to include triaged detections. If set to 'enable', triaged detections will also be collected. Must be from [enable, disable]. Applicable to Detection collection only.
9. collectEdrHealth: Flag to enable EDR health data collection. If set to 'enable', EDR Health summary and details will also be ingested into QRadar. Must be from [enable, disable]. Applicable to Health collection only.
10. collectExternalConnectorsHealth: Flag to enable External Connectors health data collection. If set to 'enable', External Connectors Health summary and details will also be ingested into QRadar. Must be from [enable, disable]. Applicable to Health collection only.