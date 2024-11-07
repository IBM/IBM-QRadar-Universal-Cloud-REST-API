Author Name: Vishal Tangadkar 
Email: vishal.tangadkar1@ibm.com
Maintainer Name:tangadkarv1990
Version Number:1.0
Endpoint Documentation:
https://www.ibm.com/docs/en/qradar-common?topic=api-endpoint-documentation-supported-versions

Event Types Currently Supported by the workflow: All which got modified between last run time to now.

To pull Offenses from QRadar, you need to add Universal REST connector to QRadar It Self. To do so, you'll need to first collect the following authentication information from QRadar SIEM:
* QRadar Console Host IP 
* Authorized Token 

### QRadar Console Host IP
IP Address of QRadar Console

### Authorized Token
We need Authorized Security Token with Admin Security Profile and Admin User Role. Here, You can know more about Creating an authorized service token for QRadar Operations. https://www.ibm.com/docs/en/qradar-common?topic=app-creating-authorized-service-token-qradar-operations.

## Historical Poll Configuration
It will start polling All the offenses in First Run. 

## Download the DSM storeOffenseInAriel
Download DSM from storeOffenseInAriel-DSM : https://ibm.ent.box.com/folder/292661255515?v=storeOffenseInAriel-DSM
Import it using Extension Management Application.

## QRadar Log Source Configuration

If you want to ingest data from an endpoint using the Universal Rest API Protocol, configure a log source on the QRadar® Console using the Workflow field so that the defined endpoint can communicate with QRadar by using the Universal Rest API protocol.

1. Log in to QRadar.
2. Click the _Admin_ tab.
3. To open the app, click the _QRadar Log Source Management_ app icon.
4. Click _New Log Source_ > Single Log Source.
5. On the Select a Log Source Type page, _Select a Log Source Type storeOffenseInAriel for configuring storeOffenseInAriel and click _Select Protocol Type_.
6. On the Select a Protocol Type page, select a Protocol Type (Universal Cloud Rest API) and click _Configure Log Source Parameters_.
7. On the Configure the Log Source parameters page, configure the log source parameters and click _Configure Protocol
Parameters_.
**Make sure to turn off the _Coalescing Events_ to avoid grouping the events based on Source and Destination IP.**
8. On the Configure the Protocol Parameters page, configure the protocol-specific parameters (Workflow and Workflow
Parameter Values). 
9. In the Test protocol parameters window, click _Start Test_.
10. Click _Finish_


## Workflow Parameter Description
1. host: IP Address of QRadar Console
2. auth_token: Authorized Service Token
