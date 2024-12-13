## Collect authentication information from Palo Alto Networks Cortex Xpanse

To integrate with QRadar, you need to add a Cortex Xpanse connector in QRadar's Universal REST connector. To do so, you'll need to first collect the following authentication information from the Cortex Xpanse Tenant:
* API Endpoint URL
* API Key and API Key ID

### API endpoint URL
To find your API endpoint URL:
1. Log in to Cortex Xpanse, take the hostname from the URL
2. Copy the Cortex Xpanse URL and remove “https://” if it is there at the start of the URL.

### API Key and API Key ID
To generate a client ID and client secret, please refer the following article to <a href="https://docs-cortex.paloaltonetworks.com/r/Beta/Cortex-XPANSE/Online-Help/Generate-an-API-Key">Generate an API Key</a>

## Historical Poll Configuration
To ingest data historically, please provide the number of days from where the alerts are to be polled. 

**The historical poll configuration is needed only for fetching the Cortex Xpanse Alerts.**

**This value can be kept as blank in the Workflow Parameter file while configuring the Log Source for the Cortex Xpanse Assets.**

## QRadar Log Source Configuration

If you want to ingest data from an endpoint using the Universal Rest API Protocol, configure a log source on the QRadar® Console using the Workflow field so that the defined endpoint can communicate with QRadar by using the Universal Rest API protocol.

1. Log in to QRadar.
2. Click the _Admin_ tab.
3. To open the app, click the _QRadar Log Source Management_ app icon.
4. Click _New Log Source_ > Single Log Source.
5. On the Select a Log Source Type page, _Select a Log Source Type (Xpanse-Qradar)_ for configuring Cortex Xpanse Alerts and click _Select Protocol Type_.
**To configure the Cortex Xpanse Networks Assets, Select the Log Source Type as Xpanse Qradar Assets.**
6. On the Select a Protocol Type page, select a Protocol Type (Universal Cloud Rest API) and click _Configure Log Source Parameters_.
7. On the Configure the Log Source parameters page, configure the log source parameters and click _Configure Protocol
Parameters_.
**Make sure to turn off the _Coalescing Events_ to avoid grouping the events based on Source and Destination IP.**
8. On the Configure the Protocol Parameters page, configure the protocol-specific parameters (Workflow and Workflow
Parameter Values). 
9. In the Test protocol parameters window, click _Start Test_.
10. Click _Finish_


## Workflow Parameter Description

1. api_key: The API Key obtained/copied from the Cortex Xpanse tenant.
2. api_key_id: The API Key ID obtained/copied from the Cortex Xpanse tenant.
3. xpanse_tenant: The API Endpoint URL Domain/FQDN (Fully Qualified Domain Name) to fetch the events from the Cortex Xpanse portal.
4. historical_poll: The value of historical polling in days needs to get Cortex Xpanse Alert Events. 
**This parameter is not needed for fetching the Cortex Xpanse Assets.**
