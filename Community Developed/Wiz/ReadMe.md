## Collect authentication info from Wiz

To integrate with QRadar, you need to add a Wiz connector in QRadar's Universal REST connector. To do so, you'll need to first collect the following authentication information from Wiz:
* API Endpoint URL
* Client ID and client secret

### API endpoint URL
To find your API endpoint URL:
1. Log in to Wiz, then open your <a href="https://app.wiz.io/user/profile" target="_blank">user profile</a>
2. Copy the **API Endpoint URL** to a local file for use below.

### Token URL
To find your Token URL:
1. Go to <a href="https://app.wiz.io/settings/service-accounts" target="_blank">Settings > Service Accounts</a>
2. The token URL is near the top of the screen.
3. Copy the token URL to a local file for use below.

### Client ID and client secret
To generate a client ID and client secret:
1. Go to <a href="https://app.wiz.io/settings/service-accounts" target="_blank">Settings > Service Accounts</a>, then click **Add Service Account**.
2. On the New Service Account page:
   1. Give the new service account a meaningful name, e.g. "QRadar integration".
   2. Select the permission **read:issues**.
   3. Click **Add Service Account**.
3. From the secret credential dialog, copy the **Client ID** and **Client Secret** to a local file or secret manager for use below.
**Note: The Client ID and Client Secret are only shown once. Do not close the dialog without copying them to a local file or secret manager.**
4. Click **Finish**.  
  

## QRadar Log Source Configuration

If you want to ingest data from an endpoint using Universal Rest API Protocol, configure a log source on the QRadar® Console using the Workflow field so that the defined endpoint can communicate with QRadar by using the Universal Rest API protocol.

1. Log in to QRadar.
2. Click the _Admin_ tab.
3. To open the app, click the _QRadar Log Source Management_ app icon.
4. Click _New Log Source_ > Single Log Source.
5. On the Select a Log Source Type page, _Select a Log Source Type (Universal DSM)_ and click _Select Protocol Type_.
6. On the Select a Protocol Type page, select a Protocol Type (Universal Cloud Rest API) and click _Configure Log Source Parameters_.
7. On the Configure the Log Source parameters page, configure the log source parameters and click _Configure Protocol
Parameters_.
**Make sure to turn off the _Coalescing Events_ to avoid grouping of the events on the basis of Source and Destination IP.**
8. On the Configure the Protocol Parameters page, configure the protocol-specific parameters (Workflow and Workflow
Parameter Values). 
9. In the Test protocol parameters window, click _Start Test_.
10. Click _Finish_


## Workflow Parameter Description

1. client_id : The Client ID obtained from Wiz portal.
2. client_secret : The Client Secret obtained from Wiz portal.
3. token_url_domain : The Token URL Domain to fetch the JWT Token from Wiz.
4. host : The API Endpoint URL Domain to fetch the events from Wiz.
5. historical_days : Number of historical days to fetch data from Wiz (default value is 10 days) .
6. auth_type : The Authentication type used to fetch JWT Token from Wiz.
7. gql_query : The GraphQL query to be used while fetching the events from Wiz (default GraphQL query already present).
