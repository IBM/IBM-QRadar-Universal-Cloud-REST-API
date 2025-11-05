# Collect authentication info from Vectra XDR #

To integrate with QRadar, you need to add a Vectra XDR connector in QRadar's Universal REST connector. To do so, you'll need to first collect the following authentication information from Vectra XDR:

- Vectra Hostname
- Client ID and Secret Key

# Vectra Hostname #

To find your Vectra Hostname:

1. Log in to Vectra XDR, then take the hostname from the URL.
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
1. Select *Vectra XDR* log source type. 
2. Click *Select Protocol Type* to go to the next section.

## 2. Select Protocol Type ##
1. Select *Universal Cloud Rest API* protocol type. 
2. Click *Configure Log Source Parameters* to go to the next section.
3. If option "Universal Cloud Rest API" is not available in protocol type, then uninstall the Vectra XDR app from extensions management, install the Universal Cloud Rest API Protocol and then install the Vectra XDR app.

## 3. Configure Log Source Parameters ##
1. Name is the name of the Log Source and it can be kept anything based on the user's choice.
2. Select "VectraXDRCustom_ext" Extension. It is used for post processing of events.
3. Disable *Coalescing Events* to avoid grouping of the events on the basis of Source and Destination IP. 
4. Except for the above fields everything can be kept as their default values or if needed can be changed by the QRadar admin.
5. Click *Configure Protocol Parameters* to go to the next section. 

## 4. Configure Protocol Parameters ##
1.  Add "Log Source Identifier" of user's choice.
2.  Copy the content from file VectraXDR-Detection-Workflow.xml in "Workflow".
3.  Modify the content as per user specification in the file VectraXDR-Workflow-Parameter-Values.xml and add in "Workflow Parameter Values".
4.  Create new log sources and repeat **QRadar Log Source Configuration** steps to collect other data and use below files as Workflow.
      - For entity score data collection use VectraXDR-EntityScoring-Workflow.xml
      - For Audit data collection use VectraXDR-Audit-Workflow.xml
      - For Lockdown data collection use VectraXDR-Lockdown-Workflow.xml
      - For Health data collection use VectraXDR-Health-Workflow.xml
5.  Recurrence is the time interval between each execution of the workflow. It can be modified according the user's requirement, default value would be 10 minutes.
6.  Except for the above fields everything can be kept as their default values or if needed can be changed by the QRadar admin.
7.  Click *Test Protocol Parameters* to test the entered workflow files.

## 5. Test Protocol Parameters ##
1.  Click *Start Test* to start the testing of the entered workflows, once it is finished click *Finish*.
2.  Deploy the configuration from admin panel.

# Workflow Parameter Description #
1. clientId: The Client ID obtained from Vectra XDR portal.
2. secretKey: The Secret Key obtained from Vectra XDR portal.
3. vectraHostName: The API Endpoint Hostname to fetch the events from Vectra XDR. If your URL is https://example.com/accounts then enter example.com
4. historical: This flag will be considered only in the first run of the workflow, so that you can configure whether to pull the historical data in the first pull. If set true it will pull the data from past 24 hours else it will pull from the current time.
