# Miro Workflow for Audit Logs

This workflow can be used to configure a new Source Log of type Universal Cloud REST API protocol in order to ingest [Miro audit logs](https://developers.miro.com/reference/get-logs).

## Configure Miro

The workflow parameter values requires an `access_token` which can be obtained by a Miro admin in an Enterprise plan.

1. As an admin go to _Settings_ page.
2. Click on _Enterprise Integrations_ in the navigation menu.
3. Click on _SIEM_ toggle to enable the integration.
4. Click on "Copy" button to copy the access token to the clipboard.
5. Paste the access token in the `access_token` field value within the [Miro-Workflow-Parameter-Values.xml](./Miro-Workflow-Parameter-Values.xml) file.

## Configure QRadar

In order to ingest data using Universal Cloud REST API Protocol, you should first verify that your QRadar instance meets the pre-requisites. You can read more about this in the [official documentation](https://www.ibm.com/docs/en/dsm?topic=configuration-universal-cloud-rest-api-protocol).

It is recommended that you install the "Miro Audit Logs" custom DSM from the [App Exchange](https://exchange.xforce.ibmcloud.com/hub) so the events are parsed and mapped correctly.

1. Log in to QRadar Console.
2. Click the _Admin_ tab.
3. Click the _QRadar Log Source Management_ app icon.
4. Click _New Log Source_ and then select _Single Log Source_.
5. On the _Select a Log Source Type_ page, select "Miro Audit Logs" (or if you want to do your own event mapping use "Universal DSM") and then click _Select Protocol Type_ button.
6. On the _Select a Protocol Type_ page, select "Universal Cloud REST API" and click _Configure Log Source Parameters_.
7. On the _Configure the Log Source parameters_ page, configure the log source parameters and click Configure Protocol Parameters.
8. On the _Configure the protocol parameters_ page, configure the protocol-specific parameters ([Workflow](./Miro-Workflow.xml) and [Workflow Parameter Values](./Miro-Workflow-Parameter-Values.xml)).
9. In the _Test protocol parameters_ window, click _Start Test_.
10. To fix any errors, click _Configure Protocol Parameters_. Configure the parameters and click _Test Protocol Parameters_.
11. Click Finish.
