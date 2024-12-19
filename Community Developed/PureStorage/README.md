Author Name: PureStorage 
Maintainer Name: eng-solutions-core@purestorage.com
Version Number: 1.0
Endpoint Documentation:
## Pure Storage FlashArray
This workflow can be used to pull alerts/events from PureStorage FlashArray.
The workflow is based on the following PureStorage FlashArray documentation.
https://support.purestorage.com/bundle/m_flasharray_release/page/FlashArray/FlashArray_Release/Purity_FA_REST_API_Release_Notes/topics/concept/c_purityfa_rest_api_2x_release_notes.html

Event Types Currently Supported by the workflow: PureStorage FlashArray Alerts

## Workflow Parameter Values Notes
There are two parameters required for the workflow as parameters which need to be updated in PureStorage-FlashArray-workflow-parameter-values.xml. 
array - IP / hostname of the FlashArray
apitoken - API token to access FlashArray.  

Access https://support.purestorage.com/FlashArray/PurityFA/FlashArray_Admin_and_CLI_Reference_Guides and refer to the section Creating API Tokens for details on how to create an api_token.


## Pure Storage FlashBlade
This workflow can be used to pull alerts/events from PureStorage FlashBlade.
The workflow is based on the following PureStorage FlashBlade documentation.
https://support.purestorage.com/bundle/m_flashblade_release/page/FlashBlade/FlashBlade_Release/Purity_FB_REST_API_Release_Notes/topics/concept/c_purityfb_rest_api_2x_release_notes.html

Event Types Currently Supported by the workflow: PureStorage FlashBlade Alerts

## Workflow Parameter Values Notes
There are two parameters required for the workflow as parameters which need to be updated in PureStorage-FlashBlade-workflow-parameter-values.xml. 
array - IP / hostname of the FlashBlade
apitoken - API token to access FlashBlade

Access https://support.purestorage.com/bundle/m_purityfb_rest_api/page/FlashBlade/Purity_FB/PurityFB_REST_API/Management_REST_API/topics/reference/r_flashblade_management_rest_api_reference.html  and refer to the section Creating API Tokens for details on how to create an api_token.

For example, the "array" value for the workflow is:
 ```
<Value name="array"          value="10.1.1.0" />
```
For example, the "apitoken" value for the workflow is:
```
<Value name="apitoken"     value="xxxxxxxx-xx-xxxx-xxxx-xxxxxxxx" />
```



 
