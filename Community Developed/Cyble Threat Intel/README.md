Author Name: Cyble Inc

Maintainer Name: developers@cyble.com

Version Number: 1.1

Endpoint Documentation: This workflow can be used to pull alerts/events from Cyble Vision.

Detailed documentation can be found at: https://cyble.ai/centers/help-center

Event Types Currently Supported by the workflow: Cyble Threat Intel Alerts

## Workflow Parameter Description

For integrating QRadar with Cyble Vision via the workflow, you will need following information:

| **Parameter Label** | **Parameter** | **Description**                                                                                                             |
|---------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------|
| Hostname            | hostname      | Enter _hostname_ of Cyble Vision. Contact your Customer Success Manager to get this value.                                  |
| Api Key             | api_key       | Enter _api_key_ for authentication and fetching events from Cyble. Contact your Customer Success Manager to get this value. |
| Fetch Since         | fetch_since   | Enter _fetch_since_ (number of days) for retrieving previous days' data on the first run.                                   |

## QRadar Log Source Configuration

Cyble Threat Intel Workflow utilizes QRadar's Universal REST API Protocol to fetch data from Cyble Vision.
Cyble has a dedicated DSM to parse the incoming events properly.

The steps to configure a log source on the QRadar® Console using the Workflow field so that the defined endpoint can communicate with QRadar by using the Universal Rest API protocol are as follows:

1. Log in to QRadar.
2. Admin Panel > click on the 'QRadar Log Source Management' or 'Log Sources' app icon. 
3. Click 'Log Sources' > 'New Log Source' > 'Single Log Source'. 
4. On the 'Select Log Source Type' page, select __Cyble Threat Intel DSM__ from the list:
    - If 'Cyble Threat Intel DSM' does not appear in the list, follow the steps to install the DSM as given below.
    - Note that you can also use your own mapping and use 'Universal DSM' - we recommend to use 'Cyble Threat Intel DSM'.
5. On the 'Select Protocol Type' page, select __Universal Cloud REST API__, and proceed to next step. 
6. On the 'Configure the Log Source parameters' page, configure the log source parameters:
    - __Name__: __Cyble Threat Intel__
    - __Enabled__: __On__
    - __Coalescing Events__: __Off__
    - Keep rest of the settings as default, and proceed to next step.
7. On the Configure the Protocol Parameters page:
    - __Log source identifier__: < same as __hostname__ above >
    - Copy the workflow code from __Cyble-Threat-Intel-Workflow.xml__ and paste it into the 'Workflow' field
    - Copy the workflow params from __Cyble-Threat-Intel-Workflow-Parameter-Values.xml__, populate the fields and paste into the 'Workflow Parameters Values' field
    - __Untrusted Certificates__: __Allow__
    - Set Recurrence as per your choice. Recommended value is 30M.
    - Keep rest of the settings as default, and proceed to next step.
8. In the Test protocol parameters window, click 'Start Test'. All tests should pass.
9. To fix any errors, click 'Configure Protocol Parameters'. Configure the parameters and click Test Protocol Parameters. 
10. Click 'Finish'
11. Navigate to the 'Admin' tab. From the top bar choose 'Deploy Changes'


## Installing Cyble Threat Intel DSM

1. Navigate to [IBM App Exchange](https://exchange.xforce.ibmcloud.com/hub) and log in.
2. Search for __Cyble Threat Intel DSM__.
3. Download the file.
4. In your QRadar instance, navigate to Admin Panel > Extension Management > Add > and select the downloaded file.
5. Navigate to the 'Admin' tab. From the top bar choose 'Deploy Changes'