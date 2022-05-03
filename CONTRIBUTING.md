# Contributing
This is a IBM-owned repository. We have provided a handful of workflows but it is completely open to community submissions. We will gladly post your workflows here for others to consume.

Note that the instructions here describe very basic GitHub usage. It does not cover topics such as creating/managing branches, clone repository remotely, etc. If you have a higher level of proficiency with git, please feel free to make full use of all its facilities.

**NOTE:** This project in its entirety is facilitated by IBM Security, but are not providing support in any manner for these workflows. It is understood that the contributor of the workflow listed under the Maintainer name section of the readme is the community member contact regarding updates, issues, or otherwise altering the currently available workflow. IBM Support channels will not take any cases with relation to community provided workflows and have been directed to close them as unsupported if they arise. While we have a gateway criteria for accepting these workflows into the master project, we cannot confirm that these works have undergone thorough testing, and so any users applying these to their projects do so at their own risk.

# Be consistent
The number one rule for contributing is consistency. Pay attention to the other workflows here. Make sure that your workflow follows the naming pattern, etc. The workflows here can also be very useful as examples to write your own. Take time to understand them.

# Create an GitHub issue
While GitHub does not make issues mandatory, it is a good idea to use them.  It creates a space for discussions, and also provides tracking of all activity surrounding the work.

- Navigate to https://github.com/ibm-security-intelligence/IBM-QRadar-Universal-Cloud-REST-API/issues/new
- Select an appropriate title (e.g. Add a workflow for MyFavoriteVendor).
- Enter a description, if applicable.
- Take note of the issue number, it will be used later.

# Fork this repository
In GitHub, all work is typically done in a "fork". The fork is a private copy of the main repository. All changes will be published to the main repository once they have been reviewed and accepted by a main repository owner.

- Navigate to https://github.com/ibm-security-intelligence/IBM-QRadar-Universal-Cloud-REST-API
- Click on the "Fork" button in the top left area of the page.
- This will create and navigate you to a private copy of this repository (notice the URL is slightly different from the main repository).
- This is where all the work will be done, and reviewed before getting pulled/published to the main repository.

# Upload your workflow
Now that the fork is created, your files can be uploaded. Note that these instructions are meant for working directly in the master branch of your fork. If you prefer to separate your work into issue-specific branches, feel free to do so.

- Navigate to your fork.
- Use the "Add File" button to upload all your files. Note that to create a folder, you simply include a / in the file name to create (e.g. My Favorite Vendor/MyFavoriteVendor-Workflow.xml).
- Upload your workflow. The name should match the following pattern: MyFavoriteVendor-Workflow.xml.
- Upload your workflow parameter values template.  The name should match the following pattern: MyFavoriteVendor-Workflow-Parameter-Values.xml.
- Optionally upload a README.md file to describe important details of this protocol.  Note that GitHub will display this file when navigating to the folder (e.g. see the Duo workflow).

# What to include
In order to have your workflow pulled into the master branch successfully, please ensure the following criteria is met before submitting:

**Ensure your README file fits the following template:**
- **Author Name:**
- **Maintainer Name:** (Github Alias of who any issues should be logged against for consideration)
- **Version Number:**
    - Setting 0 as the major version, (IE: 0.X) indicates under development / needs work.
    - Minor version updates, IE:1.1) Indicate minor bug fixes have been made, such as order of operations or maintainability modifications, extra logging, etc.
    - Providing net new functionality such as pulling down new event types, changing authentication methods or endpoint versions should be set as a new major version.
- **Endpoint Documentation:**
    - Please provide a link to vendor documentation if available on the internet. if this is behind a portal, please provide at minimum a link to the portal it is behind.
- **Event Types Currently Supported by the workflow:**
    - "All" is a valid term if the endpoint is a sink for every event type offered. Otherwise, please state which types are covered. 
- **Any other information pertaining to the workflow that the Author feels is important to convey**

**Ensure your code follows these guidelines:**
- **Ensure that Logging and Debugging messages are present in your code** - These messages are what allow users to verify what may be wrong with their code. As a general outline, we should be logging messages in the workflow at these points (but not limited to, based on the context of your workflow):
    - We combine fields, or translate them (such as taking a timestamp and formatting it)
    - We begin a query
    - We end a query - and how many events were returned
    - Any time we receive messages back from the endpoint we should try and capture non - authentication information into a comment
- Ensure that any complex processing is adequately commented for future maintainers / forkers to follow.
- Please Use camel casing for variable names (IE: newVariable)
- Please use indentation on opening and closing of XML tags to assist in readability, and use tab as the indentation character.
- Please try to name variables such that the names provide information about their usage - IE: "startTime" to identify the variable holding the timestamp the next query should begin at. 
- Ensure that any potentially sensitive user - provided parameters are set to secret.
- Please provide in your submission some obfuscated sample output of your workflow operating. This can be done by utilizing the workflow validation tool (https://www.ibm.com/docs/en/dsm?topic=protocol-command-line-testing-tool - with verbose output turned on).
    - **This information should be obfuscated before upload and have no PII / SPII within it**. We strictly want to see the proper operation of the workflow in the document. 

# Create a Pull request
Once you are happy with the of your work and want to publish it, you will need to create a "Pull request". This is where IBM will have a chance to review the changes before accepting them into the public repository.

- Navigate to your fork.
- Switch to the "Pull requests" tab.
- Click the "New pull request" button.
- Click the "Create pull request" button.
- In the title, reference the issue number, prefixed with a pound sign (e.g. Add MyFavoriteVendor workflow #123).
- Optionally add comments.
- Click the "Create pull request".
- We will receive a notification, do the review and eventually accept the pull request into the main repository.

