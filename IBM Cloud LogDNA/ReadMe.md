# Getting IBM Cloud LogDNA Hostname

To obtain the 'Host Name':
1. Log on to the IBM Cloud LogDNA
2. Navigate to "Installation Instructions"
3. Click 'REST API'
4. This will give you the URL for the LogDNA service in your region. Example: https://logs.us-south.logging.cloud.ibm.com
5. This URL is for log ingestion, so you will need to modify the URL for event export.
6. In the URL relpace 'logs' with 'api'. Example: https://api.us-south.logging.cloud.ibm.com 

# Getting IBM Cloud LogDNA Service Key

To obtain a 'Service Key':
1. Log on to the IBM Cloud LogDNA
2. Navigate to "Settings"
3. Click "Organization"
4. Click the 'API Keys'
7. Generate or choose and existing 'Service Key'

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
