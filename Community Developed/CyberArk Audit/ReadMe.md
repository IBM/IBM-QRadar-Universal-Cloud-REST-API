## Collect Audit Events from CyberArk Audit Service

To integrate with QRadar, you need to add a CyberArk Audit connector in QRadar's Universal REST connector. To do so, you'll need to configure new SIEM integration described here (TBD):
  

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

1. client_id : The OAuth2 Username from Identity Administration.
2. client_secret : The OAuth2 Password from Identity Administration.
3. identity_endpoint : Identity Endpoint that can be retrieved from Audit Service.
4. host : API Base URL that can be retrieved from Audit Service.
5. api_key : API Key that can be retrieved from Audit Service.
6. webapp_id : Application ID of OAuth2 server web app.
