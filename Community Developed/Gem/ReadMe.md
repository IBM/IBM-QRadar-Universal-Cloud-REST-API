## Gem Security Workflow

This workflow can be used to get notifications from Gem Security into your QRadar environment using UNIVERSAL CLOUD REST API protocol.


## Collect client id & client secret from Gem 
 
You'll need to collect authentication information from Gem in order to ingest data from Gem to QRadar.
1. Go to <a href="https://app.gem.security/integrations" target="_blank">integrations page</a>
2. On **IBM QRadar** integration, click on set up integration and proceed in the steps till you'll get client id & client secret.
3. Copy the client id & client secret to your clipboard.

## QRadar Configuration

In order to configure new log source in QRadar that will ingest data using Universal Cloud Rest API, you'll need to make sure that you have the protocol installed in your environment.
Official documentation can be found [here](https://www.ibm.com/docs/en/dsm?topic=configuration-universal-cloud-rest-api-protocol).

You'll also need to install "Gem Threats" DSM from the App Exchange.

1. Login to QRadar Console
2. Click the _Admin_ tab.
3. Click the _QRadar Log Source Management_ app icon (if it's not installed, you can find it in [QRadar App Exchange](https://exchange.xforce.ibmcloud.com/hub)).
4. Click _New Log Source_ and then select _Single Log Source_.
5. On the _Select a Log Source Type_ page, select "Gem Threats" (Note that you can also use your own mapping and use "Universal DSM" - we recommend to use Gem Threats DSM).
6. On the _Select a Protocol Type_ page, select "Universal Cloud REST API" and click _Configure Log Source Parameters_.
7. On the _Configure the Log Source parameters_ page, configure the log source parameters and click Configure Protocol Parameters.
**Make sure to turn off the _Coalescing Events_ to avoid grouping on the events based on time and source IP - it can cause missing notifications.**
8. On the Configure the Protocol Parameters page, configure the protocol-specific parameters (Gem-Workflow and Gem-Workflow
Parameter Values). 
"clientId" and "clientSecret" can be found as explained before
9. In the _Test protocol parameters_ window, click _Start Test_.
10. Once all the test have passed, you can Click Finish and get new notification from Gem to your QRadar environment!