### Workflow for the Dragos WorldView Threat Intelligence API
<a href="https://portal.dragos.com/api/v1/doc/index.html" target="_blank">https://portal.dragos.com/api/v1/doc/index.html</a>

- **Version Number:** 1.0
- **Event Types Currently Supported by the workflow:** All threat intelligence indicators


### Dragos API Collect authentication info from Wiz
To integrate with QRadar, a new set of API keys needs to be generated in the <a href="https://portal.dragos.com/" target="_blank">Dragos Customer Portal</a>.<br/>
This can be done under _Account Settings_ > _API_



### QRadar Log Source Configuration

1. Log in to QRadar.
2. Under _Admin_ > _DSM Editor_, create a new DSM for "Dragos WorldView". Save and exit.
3. Under _Admin_ > _QRadar Log Source Management_, create a new single Log Source with the following arttibutes.
- Log Source Type = Dragos WorldView
- Protocol Type = Universal Cloud REST API
- Coalescing Events = No
- Log Source Identifier = dragos
- Workflow = <<< Copy and paste [Dragos-Workflow.xml](Dragos-Workflow.xml) unchanged >>>
- Workflow Parameter Values = <<< Copy and paste [Dragos-Workflow-Parameter-Values.xml](Dragos-Workflow-Parameter-Values.xml), updating access_token/access_key with the API values obtained from the Dragos Customer Portal >>>
- Recurrence = 6H
4. In the Test protocol parameters window, click _Start Test_.
5. Click _Finish_ and deploy the changes.


## Workflow Parameter Description

1. access_token : The Client ID obtained from Wiz portal.
2. access_key : The Client Secret obtained from Wiz portal.
