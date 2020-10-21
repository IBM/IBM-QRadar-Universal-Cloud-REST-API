# IBM-QRadar-Universal-Cloud-REST-API

IBM Security QRadar is pleased to announce the release of the Universal Cloud Connector, which is designed to enable security teams to more easily ingest data from a wide range of REST API cloud-based applications and services for enhanced visibility. To address this new dynamic, the Universal Cloud Connector includes a new Universal Cloud REST API Protocol that enables you to create log sources for the acquisition of data from REST API compatible data sources that aren’t currently supported. With the Universal Cloud REST API Protocol, you can: 

  - Quickly and easily connect to REST API based cloud applications and services. As organizations and vendors continue their digital transformation to improve and modify their existing services, the ability to quickly adapt to these changes is critical. The Universal Cloud REST API Protocol allows for the integration of cloud based (or traditional on-premise) endpoints that are not currently supported by QRadar. Configuration of these data sources is clear and accessible using the Log Source Management App.


  - Leverage pre-configured workflows for select  data sources or create your own. A Universal Cloud REST API Protocol workflow defines the connection logic – a series of actions that are executed sequentially – for retrieving events. Using pre-configured workflows substantially reduces the time to create new log sources. Creating a new workflow or modifying an existing workflow allows you the flexibility to customize event data for your specific security use cases.


  - Tailor the data for your specific use cases. Events received from log sources created using the Universal Cloud REST API Protocol may initially appear as unknown or stored. The DSM Editor can be used to define normalized properties, classify event data and extract custom event properties, ensuring that your data will provide valuable insight for activity in your network.


  - Augment threat detection abilities. Connecting your data sources with the Universal Cloud REST API Protocol facilitates the applying security use cases and analytics to new environments. The analyst sees threat intelligence, asset information, rule details, risk indicators, and by leveraging QRadar’s Analyst Workflow, they’ll have access to key investigation information in their workspace, minimizing the need to, navigate elsewhere for additional context.

 
# Before you begin

QRadar currently integrates with approximately 450 third-party devices. However, as organizations adapt to new technology, there is an immediate  need to monitor network traffic for new data sources. As an example, I’ll walk you through how to easily ingest data from a third party service, Duo Security.  

Note the following terminology as you configure the Universal Cloud REST API:

   - The Workflow is an XML document that describes the event retrieval process. The Workflow defines one or more parameters, which can be explicitly assigned values in the Workflow XML or can derive values from the Workflow Parameter Values XML document. The Workflow consists of multiple actions that run sequentially. When you run the Workflow, the parameter values are added to the State, and the State can then be accessed and changed by actions as the Workflow runs.


   - Workflow Parameter Values are the input parameters for a workflow instance, and are stored in an XML file. The Workflow Parameter Values are represented by a set of key/value pairs, and the key must match one of the parameters defined in the associated Workflow.


   - The State is a JSON object that represents the data of a running Workflow. Since the State is not strictly defined, data is dynamically stored in the State.

# Contributing

For informationa bout how to contribute your own workflow to this repository, refer to the CONTRIBUTING.md document.


# Configuration Documentation
Universal Cloud REST API configuration documentation and be found here: https://www.ibm.com/support/knowledgecenter/SS42VS_DSM/com.ibm.dsm.doc/c_universal_rest_overview.html?cp=SS42VS_7.4

