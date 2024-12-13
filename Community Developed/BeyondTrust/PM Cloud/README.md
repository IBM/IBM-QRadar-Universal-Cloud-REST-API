# BeyondTrust PM Cloud + IBM QRadar Integration

***Written and maintained by:** BeyondTrust Corporation*
***Version:** 24.1.1*

This document describes the installation and configuration of the integration between BeyondTrust Privilege Management Cloud and IBM QRadar.

The integration consists of:
- a pair of workflow definitions that are leveraged by IBM's Universal Cloud REST API Protocol
- corresponding workflow parameters files
- an extension package which provides Log Source Categories, Log Source Extensions, Event Mappings, QID Records, and other components 

---

# Prerequisites

Before proceeding with the installation and configuration of the integration with PM Cloud, it's important to ensure a few things are in place.

### Network Considerations

Your QRadar instance will need the ability to connect to various REST API endpoints provided by your PM Cloud site.  Communication is in the form of **secure HTTP traffic on TCP port 443**  The purpose of this connectivity is to query the PM Cloud site for event information which can be ingested by QRadar.

### Create a PM Cloud API Account

The API account is used from within QRadar to make API calls to PM cloud. This process is covered in the [PM Cloud Admin Guide](https://www.beyondtrust.com/docs/privilege-management/console/pm-cloud/configuration/configure-api-settings.htm).

---

# Installation and Configuration

Once the prerequisites have been satisfied, you can move on to the installation and configuration of the integration.

### Install Extension Package

The extension package is available via the IBM Security App Exchange:
1. Go to the App Exchange at: https://exchange.xforce.ibmcloud.com/hub
2. Search for **BeyondTrust**; select and then download the app for PM Cloud then download
3. Navigate to **Admin > System Configuration > Extensions Management**
4. In the Extensions Management window, click the **Add** button to begin the process of adding a new extension
5. Browse to and select the extension file downloaded from the App Exchange and click **Add** to begin installation
6. Proceed through the subsequent dialogs to complete the installation process

### Download and Configure Workflows

After the extension is installed, the other primary component of the integration is the pair of workflow definitions and parameters.  The two definitions files provide the logic to make the PM Cloud API calls to retrieve event data while the parameters files provide the necessary configuration for those workflows.

These files are all published to IBM's Universal Cloud REST API connector library, available here:  [https://github.com/IBM/IBM-QRadar-Universal-Cloud-REST-API/tree/master/Community%20Developed/BeyondTrust/PM%20Cloud](https://github.com/IBM/IBM-QRadar-Universal-Cloud-REST-API/tree/master/Community%20Developed/BeyondTrust/PM%20Cloud)
1. From the link above, download all 4 XML files.  These should include:
    - BeyondTrust-PMCloud-ActivityAudits-Workflow.xml
    - BeyondTrust-PMCloud-ActivityAudits-Workflow-Parameter-Values.xml
    - BeyondTrust-PMCloud-ClientEvents-Workflow.xml
    - BeyondTrust-PMCloud-ClientEvents-Workflow-Parameter-Values.xml
2. Open each of the parameters files (BeyondTrust-PMCloud-xxxxx-Workflow-Parameter-Values.xml) in a text editor
3. Supply values for each of the following parameters in these two files:
    - **hostname** - PM Cloud Services Hostname - Be sure to include the '-services' portion of the hostname (ex: if you access the web site at 'mysite.example.com' then the value to enter here would be 'mysite-services.example.com')
    - **client_id** - PM Cloud API Account Client ID
    - **client_secret** - PM Cloud API Account Client Secret
4. You may also modify the **page_size** or **batch_size** values if desired.  There are corresponding notes in each file which describe the purpose of these files, their default values, as well as the maximum values for each
5. Save your changes to each parameters file

### Create Log Sources

Once the extension is installed and you have downloaded and configured the workflows, the next step is to create Log Sources for the two event data feeds supported by the integration.

The two basic categories of events that can be consumed by the application are:
1. **Client Events** - These events originate from the individual systems being managed by BeyondTrust Endpoint Privilege Management. The flow back to the PM Cloud site, and are retrievable via the API.  Examples include: user logon, a process started, a process blocked, etc.
2. **Activity Audits** - These events represent activities that occur within the PM Cloud web interface.  Examples include: user role changes, editing or committing a policy draft, assigning a computer to a group, etc.

The following steps describe how to add a Log Source for either of the two data feeds:
1. Authenticate to your QRadar instance as an administrator
2. Navigate to **Admin > Data Sources > Events > Log Sources**
3. In the **Log Source Management** window, click the arrow next to the **+ New Log Source** button to expand additional options
4. From the expanded options, select **+ Quick Log Source**
5. On the **Overview** tab, enter the appropriate values in each of the configuration fields:
    - **Name** - Give the log source a unique name
    - **Log Source Type** - Select one of the two ***BeyondTrust PM Cloud - xxxxx*** types
    - **Protocol Type** - Select ***Universal Cloud REST API***
    - **Extension** - Select the ***BeyondTrustPMCloudxxxxxCustom_ext*** corresponding to the selected Log Source Type
    - *(Supply or modify other fields as needed)*
6. Click the **Protocol** tab to proceed to the next configuration section
7. On the **Protocol** tab, enter the appropriate values in each of the configuration fields:
    - **Log Source Identifier** - It is suggested to initially use a dummy value, then once all configuration is entered and you reach the **Test** step below, the test should return the correct identifier. Use that value to replace the dummy value. 
    - **Workflow** - Copy and paste the contents of the appropriate workflow XML file here
    - **Workflow Parameters** - Copy and paste the contents of the appropriate workflow parameters XML file here
    - *(Supply or modify other fields as needed)*
8. Click the **Test** tab and then **Start Test** to verify your configuration
9. If the test was successful, click **Create** to save the new Log Source
10. Repeat the steps above to add a second Log Source for the other type of events

---

# Troubleshooting and Support

Should you encounter issues with event ingestion, the application does write to the standard QRadar log and error log.  Review these logs first to determine if an issue has occurred.

You can find more information on QRadar logs, including how to access them, here:  [https://www.ibm.com/docs/en/qsip/7.5?topic=problems-qradar-log-files](https://www.ibm.com/docs/en/qsip/7.5?topic=problems-qradar-log-files)

For any issues which require additional assistance, please contact BeyondTrust Support at [mysupport@beyondtrust.com](mailto:mysupport@beyondtrust.com) or through the Customer Support Portal.
