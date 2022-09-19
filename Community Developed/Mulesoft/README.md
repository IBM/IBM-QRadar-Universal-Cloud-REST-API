MuleSoft CloudHub API Reference Page:
https://anypoint.mulesoft.com/apiplatform/anypoint-platform/#/portals/organizations/68ef9520-24e9-4cf2-b2f5-620025690913/apis/8617/versions/2321502/pages/107964

CloudHub API Parameter Reference Page:
https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/cloudhub-api/minor/1.0/console/method/%233041/

Necessary Parameters needed to pull logs from the API:
- Host (Customer Endpoint Hostname)
- Domain (This is a domain within the Customer's Endpoint)
- X-ANYPNT-ENV-ID (Environment ID)
- Client ID
- Client Secret

In the Parameter XML file, you'll noticed "grant_type" which will remain "client_credentials" as that allows the use of the Client ID and Secret.  The "orderByDate" is set to "DESC" so it orders the results of the "deployment ID" when it is queried so the most recent one (the active one) is pulled.

In the workflow, the first section "Get Access Token" pulls a token from the customer endpoint using the Client ID and Secret.  It is saved under /access_token.  

In the section "Get Deployment ID" it is connecting to the customer's endpoint API specific to the domain and receives the entire list of the available deployments.  Since new deployment can be spun up, there will likely be one active one and the rest will be down.  Since it is ordered by DESCENDING date, the most recent will be active, thus the /get_deploymnentid/body/data[1]/deploymentId value gets saved under /deploymentId.

If you were to pull all the data from the array of deployments, you will see some with a status of "TERMINATED", while the one you want to pull from should show "STARTED".
