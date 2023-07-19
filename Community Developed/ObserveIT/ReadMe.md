# ObserveIT Parameters Configuration
Parameter                           | Name | Default Value | Type | Required (True/False) | Description
---                                 | --- | --- | --- |--- |---
hostname                            | Host Name | myobserveit.com | String | True | IP for the instance.
client_id                           | Organization Key | False | Authentication | True | Can be received through the Developer Portal by selecting Credentials and pressing the Create App button.
client_secret                       | API Secret | False | Authentication | True | Can be received through the Developer Portal by selecting Credentials and pressing the Create App button.
poll_alert                          | Poll Alert | False | Bool | False | Alert Events.
poll_configuration_activity         | Poll Configuration Activity | False | Bool | False | Audit Configuration Activity.
poll_login_activity                 | Poll Login Activity | False | Bool | False | Audit Login Activity.
poll_saved_session_activity         | Poll Saved Session Activity | False | Bool | False | Audit Saved Sessions Activity.
poll_session_playback_activity      | Poll Session Playback Activity | False | Bool | False | Audit Session Playback Activity.
poll_system_event                   | Poll System Event | False | Bool | False | System Events.
poll_command_activity_with_output   | Poll Command Activity with Output | False | Bool | False | UNIX Command Events
poll_command_output_stream          | Poll Command Output Stream | False | Bool | False | UNIX Output Streams
poll_dba_activity                   | Poll Database Activity | False | Bool | False | Database Events
poll_file_activity                  | Poll File Activity | False | Bool | False | File Monitoring Activity Events
poll_interface_activity             | Poll Interface Activity | False | Bool | False | Windows/Mac user interface interaction events
poll_messaging_actions_activity     | Poll Messaging Action Activity | False | Bool | False | Messaging Actions Activity Events
poll_session                        | Poll Session Activity | False | Bool | False | Summary of activities for a completed or in-progress user session
events_per_poll                     | Events Per Poll | 100 | Number | False | Max number of records to return per poll
exclude_pii                         | Exclude Personal Information | False | Bool | False | Exclude Personal Identifiable Information from the reports.The fields to exclude are: `loginName`, `secondaryLoginName`, `endpointName`, `remoteHostName`, `windowTitle`,`accessedUrl`, `domainName`, `secondaryDomainName`, `remoteAddress`,`sqlUserName`, `sessionServerName`, `sessionLoginName`,  `savedSessionName`, `operatorUsername`, `operatorDomainName`, `userName`, `machineName`

# How to Generate Client ID and Client Secret
1. Log on to your ObserveIT instance through: https://\<MyObserveIT>/ObserveIT.

2. At the top right of the screen press the "?" button and then enter the "Developer Portal".

3. In the Developer Portal enter "🔒 Credentials".

4. Press the "+ Create App" button.

5. Enter an "Application Name".

6. Press your application's name.

7. Here you can see your Client ID and Client Secret.


# QRadar Log Source Configuration
If you want to ingest data from an endpoint using Universal Rest API Protocol, configure a log source on the QRadar® Console using the Workflow field so that the defined endpoint can communicate with QRadar by using the Universal Rest API protocol.

1. Log in to QRadar.

2. Click the Admin tab.

3. To open the app, click the QRadar Log Source Management app icon.

4. Click New Log Source > Single Log Source.

5. On the Select a Log Source Type page, Select a Log Source Type (Universal DSM) and click Select Protocol Type (Universal Rest API).

6. On the Select a Protocol Type page, select a protocol and click Configure Log Source Parameters.

7. On the Configure the Log Source parameters page, configure the log source parameters and click Configure Protocol Parameters.

8. On the Configure the Protocol Parameters page, configure the protocol-specific parameters (Workflow and Workflow Parameter Values).

9. In the Test protocol parameters window, click Start Test.

10. To fix any errors, click Configure Protocol Parameters. Configure the parameters and click Test Protocol Parameters.

11. Click Finish