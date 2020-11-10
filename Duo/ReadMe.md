# Duo Configuration

Duo Admin API

https://duo.com/docs/adminapi

Duo Admin API access guide
https://duo.com/docs/adminapi#api-details

Duo Admin Panel

https://admin.duosecurity.com/

To obtain an 'Integration Key' and 'Secret Key':
- Log on to the Duo Admin Panel as an 'Owner'
- Navigate to "Applications"
- Click "Protect Application"
- 'Protect' the 'Admin API'
- Give it a friendly name
- Grant the 'Grant read log' permission only
- The "Integration Key", "Secret Key" and "API hostname" should be visible on the application page.
- Click 'Save changes'

# QRadar Log Source Configuration
If you want to ingest data from an endpoint using Universal Rest API Protocol, configure a log source on the QRadar® Console using the Workflow field so that the defined endpoint can communicate with QRadar by using the Universal Rest API protocol.

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
