# Event Types Currently Supported by the workflow #
The workflow is collecting Mail Tracking Logs which includes:
- accepted_traffic
- blocked_traffic


# Obtaining the Secret Key #
To create an API Key, follow the steps here - <https://docs.trendmicro.com/en-us/documentation/article/trend-micro-email-security-rest-api-online-help-obtaining-the-api-ke>


# QRadar Log Source Configuration #
If you want to ingest data from an endpoint using Universal Rest API Protocol, configure a log source on the QRadar® Console using the Workflow field so that the defined endpoint can communicate with QRadar by using the Universal Rest API protocol.

1. Log in to QRadar.
2. Click the *Admin* tab.
3. To open the app, click the *QRadar Log Source Management* app icon.
4. Click *New Log Source* > Single Log Source.

## 1. Select Log Source Type ##
1. Select *Universal DSM* log source type for now, later on you will have to create a new DSM to parse the events since there is no supported parser. 
2. Click *Select Protocol Type* to go to the next section.

## 2. Select Protocol Type ##
1. Select *Universal Cloud Rest API* protocol type. 
2. Click *Configure Log Source Parameters* to go to the next section.

## 3. Configure Log Source Parameters ##
1. Name is the name of the Log Source and it can be kept anything based on the user's choice.
2. Disable *Coalescing Events* to avoid grouping of the events on the basis of Source and Destination IP. 
3. Except for the above fields everything can be kept as their default values or if needed can be changed by the QRadar admin.
4. Click *Configure Protocol Parameters* to go to the next section.

## 4. Configure Protocol Parameters ##
1.  Add "Log Source Identifier" of user's choice, it must be the same as the *host* parameter.
2.  Copy the content from file TrendMicroEmailSecurity-Workflow.xml in "Workflow".
3.  Modify the content as per user specification in the file TrendMicroEmailSecurity-Workflow-Parameter-Values.xml and add in "Workflow Parameter Values".
4.  Recurrence is the time interval between each execution of the workflow. It can be modified according the user's requirement, default value would be 5 minutes.
5.  Except for the above fields everything can be kept as their default values or if needed can be changed by the QRadar admin.
6.  Click *Test Protocol Parameters* to test the entered workflow files.

## 5. Test Protocol Parameters ##
1.  Click *Start Test* to start the testing of the entered workflows, once it is finished click *Finish*.
2.  Deploy the configuration from admin panel.


# Workflow Parameter Description #
1. *host*: The API Endpoint Hostname to fetch the events from, follow this URL to get your URL - <https://docs.trendmicro.com/en-us/documentation/article/trend-micro-email-security-rest-api-online-help-understanding-the-ur>
2. *secret_key*: The Secret Key obtained from Trend Micro Email Security administrator console, follow this URL to obtain the key - <https://docs.trendmicro.com/en-us/documentation/article/trend-micro-email-security-rest-api-online-help-obtaining-the-api-ke>
3. *nextToken*: Used to retrieve the next set of log items.
4. *startDateTime*: If this is the first workflow run, it will be set to 5 mintues before current time, otherwise, it will be the endDateTime of the last workflow run.
5. *endDateTime*: Current time.


# DSM Parsing Tips #
- *Event Category* Regex Expression: **,"(details)"**
- *Event ID* JSON Expression: **/"reason"**
- *Event ID* JSON Expression: **/"action"**
- Note that there are 2 expressions for the *Event ID* as the payload is different for accepted_traffic & blocked_traffic.


# Endpoint Documentation #
Getting Started with Trend Micro Email Security APIs - <https://docs.trendmicro.com/en-us/documentation/article/trend-micro-email-security-rest-api-online-help-getting-started-with>
