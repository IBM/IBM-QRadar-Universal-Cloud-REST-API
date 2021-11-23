# Ermes - Intelligent Web Protection Configuration

Steps to obtain an integration with QRadar:

- Log on to the Ermes for Enterprise Panel
- Navigate to "SIEM Integrations"
- Go to "QRadar Integration"
- Generate a new ClientID / ClientSecret credential combo
- Download the Custom DSM (.zip file) and install it
- Download the Workflow XML and the Workflow Params XML (preconfigured with your data)
- Follow the instructions below

# QRadar Log Source Configuration
To ingest data from the Ermes for Enterprise event log using Universal Rest API Protocol, configure a log source on the QRadar® Console using the Workflow provided on the Ermes for Enterprise dashboard.

1. Log in to QRadar.
2. Click the _Admin_ tab.
3. Click on _Extensions Management_
4. Click on _Add_ then select the Custom DSM .zip file you downloaded from Ermes for Enterprise dashboard
5. Accept and install the package.
6. Go back to the admin panel, click on the _QRadar Log Source Management_ app icon.
7. Click _New Log Source_ > Single Log Source.
8. On the _Select Log Source Type_ page, select _Ermes for Enterprise_, and go to Step 2.
9. On the _Select Protocol Type_ page, select _Universal Cloud REST API_, and go to Step 3.
11. On the Configure the Log Source parameters page, configure the log source parameters:
    - Insert a name for this log source (_Ermes For Enterprise Log Source_);
    - For the field _Extension_, select *ErmesForEnterpriseCustom_ext*;
    - Disable _Coalescing Events_ to make sure every event is reported each time;
12. On the Configure the Protocol Parameters page, configure:
    - Insert a log source identifier (*ermes_for_enterprise*);
    - Copy the Workflow XML you downloaded from Ermes for Enterprise panel and paste it into the *Workflow* field;
    - Copy the Workflow Params (make sure your ClientID and ClientSecret are populated) into the *Workflow Parameters Values* field;
    - Enable *Allow Untrusted Certificates*
    - Set *5M* as the Recurrence
13. In the Test protocol parameters window, click _Start Test_. All tests should pass.
14. To fix any errors, click _Configure Protocol Parameters_. Configure the parameters and click Test Protocol Parameters.
15. Click _Finish_
16. Do a full configuration deploy (__Deploy Changes -> Advanced -> Deploy Full Configuration__)
