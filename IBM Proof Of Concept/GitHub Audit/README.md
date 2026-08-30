# GitHub Audit QRadar Universal Cloud REST API

QRadar Univseral Cloud Rest API log source that ingests GitHub audit logs.

* **Author Name:** Liam Mahoney
* **Maintainer Name:** [lmahoney1](https://github.com/lmahoney1)
* **Version Number:** 1.0.0
* **Endpoint Documentation:**
    * **Choose the appropriate version of GitHub being used in the top left corner of the page**
    * [Enterprise Audit Logs](https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/audit-log?apiVersion=2022-11-28#get-the-audit-log-for-an-enterprise)
    * [Organization Audit Logs](https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/orgs?apiVersion=2022-11-28#get-the-audit-log-for-an-organization)
* **Event Types Supported by Workflow:** All

## Workflow Parameters

| Name | Description | Required | Example |
| ---- | ----------- | -------- | ------- |
| host | GitHub API to connect to | yes | api.github.com |
| app_id | ID of the application installed on the organization. Required if using app authentication to retrieve organization audit logs. | no | 123456 |
| app_private_key | Base64 encoded app private key **PCKS#8 certificate**. Required if using app authentication to retrieve organization audit logs. | no | LS0.... |
| app_installation_id | Installation ID of the application installed on the organization. Required if using app authentication to retrieve organization audit logs. | no | 7891011 |
| personal_access_token | GitHub personal access token that has permission to view audit logs on the organization / enterprise. Required if retrieving enterprise audit logs, or using personal access token authentication to retrieve organization audit logs. | no | xxxxxxx |
| organization | GitHub Organization to gather audit logs from. Required when retrieving organization audit logs. | no | example-org |
| enterprise | GitHub Enterprise to gather audit logs from. Required when retrieving enterprise audit logs. | no | example-enterprise |

## Configuration

This workflow can be configured to pull audit logs from either a GitHub Organization or an Enterprise.

### Configuring For Enterprise

To configure the workflow to pull audit logs for teh whole enterprise you must supply values for the following workflow parameters:
* `host`
* `personal_access_token`
* `enterprise`

#### Generating a Personal Access Token

You must generate a personal access token from a GitHub account that is a Site Owner. See [This page](https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/audit-log?apiVersion=2022-11-28) for more details about the proper roles required for the Personal Access token. **Verify you are looking at the proper verison of GitHub in the top left corner**.

#### Finding Enterprise Name

You need to specify the name of the enterprise to retrieve audit logs from as the value for the workflow paramter `enterprise`. The enterprise name can be found by clicking the top right icon -> 'Your Enterprise' -> copy the end of the URL from the URL bar in your web browser.

### Configuring For Organization

To configure the workflow to pull audit logs from an organization you must supply values for the following workflow parameters:
* `host`
* `organization`

You must also supply values for one of the two authenticatio methods that are supported:
* GitHub App
    * `app_id`
    * `app_private_key`
    * `app_installation_id`
* Personal Access Token
    * `personal_access_token`

#### Finding Organization Name

Navigate to your organization's page. Copy the name of the organization from the web browser URL bar. Provide this as the value for the workflow parameter `organization`.

#### Configuring App Authentication

##### Create GitHub App

You must be an administrator on the organization you wish to install the app on. Navigate to the organization page and click on 'Developer Settings'.

Make sure the 'GitHub Apps' page is selected, and click the 'New GitHub App' button.

Make the following changes:
* name
    * recommend something related to QRadar / QRadar Universal Cloud REST API
* description
    * more detail that this app is for authenticating the QRadar Universal Cloud REST API log source
* homepage URL
    * copy + paste the URL to this README.md file
* webhook
    * unselect the 'active' checkbox
* permissions
    * see [this](https://docs.github.com/en/enterprise-server@3.7/rest/orgs/orgs#get-the-audit-log-for-an-organization) link for more details about the proper permissions to grant the app. **Verify you are looking at the correct version of GitHub in the top left corner of the page**

Determine what you would like for whether or not the app can only be installed by the user account or anyone.

Once the app is created you should be able to see the ID of the app by navigating the the `About` section of the app. Provide this ID as the value for the `app_id` workflow parameter.

##### Get GitHub App Installation ID

Navigate to your organization page (top right icon -> settings -> organization -> 'settings' button on the organization)

In the left tool bar, scroll down to the 'Integrations' section and click on 'GitHub Apps'.

Click on the app, the installation ID should be avaiable in the web browser URL bar. Provide this installation ID as the value for the `app_installation_id` workflow parameter.

##### Generate GitHub App Private Key

Naviagate to the GitHub application you have created. Scroll to the bottom of the page until you see "Private keys".

Generate a private key, note that it downloads the key for you automatically. This key is the in `PKCS#1 RSAPrivateKey` format, and QRadar Universal Cloud REST API requires that the file be in the format `PKCS#8`. Use the following command on linux to convert the key to `PKCS#8` and base64 encode it. Not sure how to do it on other OSes, apologies.

`openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt -in /path/to/key/downloaded/key-name.pem | openssl base64 -A`

Replace `/path/to/key/downloaded/key-name.pem` with the path to the private key you downloaded.

Provide this base64 encoded string as the `app_private_key` workflow parameter value.

#### Configuring Personal Access Token Authentication

Generate a Personal Access Token and specify the token as the value for the `personal_access_token` workflow paramter. See [this](https://docs.github.com/en/enterprise-server@3.7/rest/orgs/orgs#get-the-audit-log-for-an-organization) link for more details about the roles required to be granted to the personal access token. **Validate you are looking at the correct version of GitHub in the top left corner of the page**.