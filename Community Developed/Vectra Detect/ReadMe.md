# Collect authentication info from Vectra Detect #

To integrate with QRadar, you need to add a Vectra Detect connector in QRadar's Universal REST connector. To do so, you'll need to first collect the following authentication information from Vectra Detect:

- Vectra SaaS Hostname
- Client ID and Secret Key

# Vectra SaaS Hostname #

To find your Vectra SaaS Hostname:

1. Log in to Vectra Detect, then take the hostname from the URL.
2. Copy the Vectra SaaS URL and remove “https://” if it is there at the start of URL.

# Client ID and Secret Key #

To create an API client, log in to your Vectra Detect portal with “Super Admin” role. Documentation of Vectra SaaS API - <https://support.vectra.ai/s/article/KB-VS-1571>

1. Go to Manage > API Clients, then click Add API Client.
2. On the Add API client page:
3. Role – the role maps the API Client to a set of permissions, similar to the way a Detect UI user would be assigned a role. The role must be one of the following:
   1. Read-Only
   2. Restricted Admin
   3. Security Analyst
   4. Settings Admin
4. Creating a new API Client has two optional parameters:
   1. Name – a user-friendly name to identify the client (up to 256 characters)
   2. Description – a brief description to aid in identifying the client (up to 2048 characters)
5. After adding all the above information click on ‘Generate Credentials’ to obtain your client credentials.
6. From the API client created dialog, copy the Client ID and Secret Key to a local file or secret manager for use below. Note: The Client ID and Secret Key are only shown once. Do not close the dialog without copying them to a local file or secret manager.
7. Click Done.

# QRadar Log Source Configuration #

If you want to ingest data from an endpoint using Universal Rest API Protocol, configure a log source on the QRadar® Console using the Workflow field so that the defined endpoint can communicate with QRadar by using the Universal Rest API protocol.

1. Log in to QRadar.
2. Click the *Admin* tab.
3. To open the app, click the *QRadar Log Source Management* app icon.
4. Click *New Log Source* > Single Log Source.


## 1. Select Log Source Type ##
1. Select *Vectra Detect* log source type. 
2. Click *Select Protocol Type* to go to the next section.

## 2. Select Protocol Type ##
1. Select *Universal Cloud Rest API* protocol type. 
2. Click *Configure Log Source Parameters* to go to the next section.
3. If option "Universal Cloud Rest API" is not available in protocol type, then uninstall the Vectra Detect app from extensions management, install the Universal Cloud Rest API Protocol and then install the Vectra Detect app.

## 3. Configure Log Source Parameters ##
1. Name is the name of the Log Source and it can be kept anything based on the user's choice.
2. Select "VectraDetectCustom_ext" Extension. It is used for post processing of events.
3. Disable *Coalescing Events* to avoid grouping of the events on the basis of Source and Destination IP. 
4. Except for the above fields everything can be kept as their default values or if needed can be changed by the QRadar admin.
5. Click *Configure Protocol Parameters* to go to the next section. 

## 4. Configure Protocol Parameters ##
1.  Add "Log Source Identifier" of your choice.
2.  Copy the content from file VectraDetect-AccountDetection-Workflow.xml in "Workflow".
3.  Modify the content as per user specification in the file VectraDetect-Workflow-Parameter-Values.xml and add in "Workflow Parameter Values".
4.  Create a new log source and repeat **QRadar Log Source Configuration** steps to collect account score data and use file VectraDetect-AccountScoring-Workflow.xml as Workflow.
5.  Recurrence is the time interval between each execution of the workflow. It can be modified according the the user's requirement, default value would be 10 minutes.
6.  Except for the above fields everything can be kept as their default values or if needed can be changed by the QRadar admin.
7.  Click *Test Protocol Parameters* to test the entered workflow files.

## 5. Test Protocol Parameters ##
1.  Click *Start Test* to start the testing of the entered workflows, once it is finished click *Finish*.
2.  Deploy the configuration from admin panel.

# Workflow Parameter Description #
1. clientId: The Client ID obtained from Vectra Detect portal.
2. secretKey: The Secret Key obtained from Vectra Detect portal.
3. vectraSaaSHostName: The API Endpoint Hostname to fetch the events from Vectra Detect. If your URL is https://example.com/accounts then enter example.com
4. historical: This flag will be considered only in the first run of the workflow, so that you can configure whether to pull all the historical data in the first pull. If set true it will pull all the historical data.
