**Collect authentication info from Vectra Detect**

To integrate with QRadar, you need to add a Vectra Detect connector in QRadar's Universal REST connector. To do so, you'll need to first collect the following authentication information from Vectra Detect:

- Vectra SaaS Hostname
- Client ID and Secret Key

**Vectra SaaS Hostname**

To find your Vectra SaaS Hostname:

1. Log in to Vectra Detect, then take the hostname from the URL.
2. Copy the Vectra SaaS URL and remove “https://” if it is there at the start of URL.

**Client ID and Secret Key**

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

**QRadar Log Source Configuration**

If you want to ingest data from an endpoint using Universal Rest API Protocol, configure a log source on the QRadar® Console using the Workflow field so that the defined endpoint can communicate with QRadar by using the Universal Rest API protocol.

1. Log in to QRadar.
2. Click the *Admin* tab.
3. To open the app, click the *QRadar Log Source Management* app icon.
4. Click *New Log Source* > Single Log Source.
5. On the Select a Log Source Type page, *Select a Log Source Type (Vectra Detect)* and click *Select Protocol Type*.
6. On the Select a Protocol Type page, select a Protocol Type (Universal Cloud Rest API) and click *Configure Log Source Parameters*.
7. On the Configure the Log Source parameters page, configure the log source parameters and click *Configure Protocol Parameters*. Make sure to turn off the *Coalescing Events* to avoid grouping of the events on the basis of Source and Destination IP.
8. On the Configure Protocol Parameters page, configure the protocol-specific parameters (Workflow and Workflow Parameter Values).
9. In the Test protocol parameters window, click *Start Test*.
10. Click *Finish.*
11. Deploy the configuration from admin panel.

**Workflow Parameter Description**

1. clientId: The Client ID obtained from Vectra Detect portal.
2. secretKey: The Secret Key obtained from Vectra Detect portal.
3. vectraSaaSHostName: The API Endpoint Hostname to fetch the events from Vectra Detect. If your URL is https://example.com/accounts then enter example.com
4. historical: true or false flag to convey whether to do historical data collection or not, by default value would be false.
