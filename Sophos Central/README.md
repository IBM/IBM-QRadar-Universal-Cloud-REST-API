This workflow can be used to pull events from Sophos Central.
The workflow is based on the following Sophos Central documentation.

https://support.sophos.com/support/s/article/KB-000036372?language=en_US

## Workflow Parameter Values Notes
Sophos documentation detailing API Host values is available here.

https://developer.sophos.com/intro#global-vs-regional-apis

For example, the "api_host" value for the Global API's would be:
 ```
 <Value name="api_host" value="api.central.sophos.com"/>
```
Alternatively, if your Tenant's data region is EU - Ireland, the "api_host" value would be:
```
<Value name="api_host" value="api-eu01.central.sophos.com"/>
```
The client_id, client_secret and tenant_id values are retrieved from Sophos Central with further details in the links already mentioned.

-----------------------------------------------------------------

## Workflow Notes
For the Initial bookmark value, provide a Unix timestamp in UTC within the last 24 hours in the Initialize statement below.
For example, in Linux to get the time 12 hours before the current time in the correct format for the Initialize statement.

echo $(($(date +%s)-(12 * 60 * 60)))

1641881796
```
<Initialize path="/bookmark" value="1641881796" />
```
