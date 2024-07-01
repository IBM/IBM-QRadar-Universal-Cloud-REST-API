- Author Name: Paulo Dantas
- Maintainer Name: @paulofdantas
- Version Number: 0
- Event type: Supported sources are any of the following: Google Operations, Mobile device management, Gmail phishing, Data Loss Prevention, Domain wide takeout, State sponsored attack, Google identity, Apps outage.

# Google Alert Center Configuration

Google Alert Center API

https://developers.google.com/admin-sdk/alertcenter

Use the alert center

https://support.google.com/a/answer/9105276?hl=en

Configuring access to Google Alert Center API:

- Follow the IBM docs for Google G Suite Activity Reports and just change/add the Alert Center API scope at step '5' on Granting API client access to a service account' section.

    IBM G-Suite Activity Reports to use as a reference: https://www.ibm.com/docs/en/dsm?topic=ggsar-configuring-google-g-suite-activity-reports-communicate-qradar
    
    Alert Center API scope to add at step '5': https://www.googleapis.com/auth/apps.alerts
    
- Make sure you saved the JSON file for your service account, this file contain the Private Key required to call Google Alert Center API: https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating
    
IMPORTANT: Copy the entire private key from your service account JSON Key file replacing all the '\n' with line breaks and encode the key using Base64 before paste it in the 'GoogleWorkspaceAlertCenter-Workflow-Parameter-Values.xml' file. Take a look at the following command, it could be very helpful to do that.

    grep -o -e "-----BEGIN PRIVATE KEY-----[^\"]\+" your_service_account_credentials_file.json | awk '{gsub("\\\\n","\n")};1' | base64 -w0

IMPORTANT! Be sure to configure an user that have access to Google Alert Center Admin Console in the 'GoogleWorkspaceAlertCenter-Workflow-Parameter-Values.xml' for use in the 'sub' parameter at the moment of JTW configuration. This user is crucial once it will be impersonated in the API calls.

    <Value name="user_email"    value="an_alert_center_user@your_domain.com" />


# QRadar Log Source Configuration

1. Log in to QRadar.
2. Click the _Admin_ tab.
3. To open the app, click the _QRadar Log Source Management_ app icon.
4. Click _New Log Source_ > Single Log Source.
5. On the Select a Log Source Type page, _Select a Log Source Type (Universal DSM)_ and click _Select Protocol Type (Universal Rest API)_.
6. On the Select a Protocol Type page, select a protocol and click _Configure Log Source Parameters_.
7. On the Configure the Log Source parameters page, configure the log source parameters and click _Configure Protocol
Parameters_.
8. On the Configure the Protocol Parameters page, configure the protocol-specific parameters (Workflow and Workflow
Parameter Values). 
9. In the Test protocol parameters window, click _Start Test_.
10. To fix any errors, click _Configure Protocol Parameters_. Configure the parameters and click Test Protocol Parameters.
11. Click _Finish_
