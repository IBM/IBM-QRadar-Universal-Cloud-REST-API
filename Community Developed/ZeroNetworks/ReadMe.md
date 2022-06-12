## Collect audit logs from Zero Networks

To integrate with QRadar, you need to add a Zero Networks connector in QRadar's Universal REST API connector. To do so, you'll need to first collect the following:
* API Token


### API Token
To find your API Token:
1. Log in to the Zero Networks portal at [portal.zeronetwroks.com](https://portal.zeronetworks.com)
2. Click ***Settings***
3. Click ***API***
4. Click ***Add new token***
5. Enter a ***Token name***, set ***Access type*** to ***Read only***, and set ***Expriy*** to ***36 Months***
5. Click ***Add***
6. Copy the API Token

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
1. api_token : The API Token obtained from the portal.
2. host : The portal url
3. historical_days : Number of historical days to fetch data from Zero Networks Audit Log (default value is 30 days) .