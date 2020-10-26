# Contributing
This is a IBM-owned repository. We have provided a handful of workflows but it is completely open to community submissions. We will gladly post your workflows here for others to consume.

Note that the instructions here describe very basic GitHub usage. It does not cover topics such as creating/managing branches, clone repository remotely, etc. If you have a higher level of proficiency with git, please feel free to make full use of all its facilities.

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

