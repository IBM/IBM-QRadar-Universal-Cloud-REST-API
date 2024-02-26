Author Name: PureStorage 
Maintainer Name: eng-solutions-core@purestorage.com
Version Number: 1.0
Endpoint Documentation: 
This workflow can be used to pull alerts/events from PureStorage FlashArray.
The workflow is based on the following PureStorage FlashArray documentation.
https://support.purestorage.com/FlashArray/FlashArray_Release/Purity%2F%2F%2F%2FFA_REST_API_Release_Notes/Purity%2F%2F%2F%2FFA_REST_API_2.x_Release_Notes

Event Types Currently Supported by the workflow: PureStorage FlashArray Alerts

## Workflow Parameter Values Notes
There are two parameters required for the workflow as parameters which need to be updated in PureStorage-FlashArray-workflow-parameter-values.xml. 
array - IP / hostname of the FlashArray
apitoken - API token to access FlashArray.  

Access https://support.purestorage.com/FlashArray/PurityFA/FlashArray_Admin_and_CLI_Reference_Guides and refer to the section Creating API Tokens for details on how to create an api_token. 


For example, the "array" value for the workflow is:
 ```
<Value name="array"          value="10.1.1.0" />
```
For example, the "apitoken" value for the workflow is:
```
<Value name="apitoken"     value="xxxxxxxx-xx-xxxx-xxxx-xxxxxxxx" />
```


 
