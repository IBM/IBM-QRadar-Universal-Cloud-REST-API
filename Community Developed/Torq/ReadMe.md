# **Description**

[qRadar's Universal Cloud REST API](https://github.com/IBM/IBM-QRadar-Universal-Cloud-REST-API/tree/master) allows fetch of Torq Logs via Torq API.  
Attached Torq XML to be used in qRadar's Universal DSM log source protocol.  
More info at [qRadar Guide](https://www.ibm.com/docs/en/dsm?topic=configuration-universal-cloud-rest-api-protocol)

# **Details**

### Torq Audit Logs XML for qRadar

This workflow is designed to configure a new Source Log using the Universal Cloud REST API protocol to ingest Torq audit logs.

**Required Information from your Torq workspace:**

*Note: The Torq admin should create an [API key in Torq as a service connector](https://kb.torq.io/en/articles/9145827-create-a-torq-api-key-enable-programmatic-access#h_1b6c02c262) that can fetch logs.*

The workflow requires the following parameters, which can be retrieved by a Torq admin:

1. **client_id**: Your Client ID from Torq platform.
2. **client_secret**: Your Client Secret from Torq platform.
3. **base_url**: The Base URL of your Torq workspace.  
   * `https://api.torq.io/public`  
   * or  
   * `https://api.eu.torq.io/public` for EU region.

Once you have these, you will need to update the **Torq-Workflow-Parameter-Values.xml** file with the following fields:

- **client_id**: Your Torq Client ID.
- **client_secret**: Your Torq Client Secret.
- **base_url**: The API Base URL.
- **log_source_name**: The name of the log source that will be used in qRadar.

**Configure qRadar**

To ingest audit log data from Torq using the Universal Cloud REST API Protocol, follow these steps:

1. Log in to QRadar Console.
2. Click the **Admin** tab.
3. Open the **QRadar Log Source Management** app.
4. Click **New Log Source** and select **Single Log Source**.
5. On the **Select a Log Source Type** page, select **Universal DSM**.
6. Click **Select Protocol Type** and choose **Universal Cloud REST API**.
7. On the **Configure Log Source Parameters** page, configure the general log source parameters and click **Configure Protocol Parameters**.
8. On the **Configure the protocol parameters** page, configure the protocol-specific parameters, Copy the content of the XMLs accordingly:
   - Workflow - from Torq-audit-workflow.xml
   - Workflow Parameter Values - from your Torq-Workflow-Parameter-Values
9. Make sure to **turn off** the Coalescing Events.
10. In the **Test protocol parameters** window, click **Start Test**.
11. Once the test is successful, click **Finish**.

**Workflow Parameter Description (Torq-AuditLogs-Workflow.xml)**

- **client_id**: The Client ID retrieved from Torq.
- **client_secret**: The Client Secret retrieved from Torq.
- **base_url**: The Base URL for Torq’s API.
- **log_source_name**: The name you assign to the log source in QRadar.