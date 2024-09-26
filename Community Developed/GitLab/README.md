# Workflow for collecting Audit event logs from Gitlab

Author & Maintainer: Michal Pavlis (@michal0000000)  
Version Number: v1.0.0

## Userful Links:

- [Gitlab Audit Events API](https://docs.gitlab.com/ee/api/audit_events.html#retrieve-all-instance-audit-events)
- [Gitlab API pagination](https://docs.gitlab.com/ee/api/rest/index.html#keyset-based-pagination)
- [Gitlab API authentication](https://docs.gitlab.com/ee/api/rest/index.html#authentication)

## Event Types Currently Supported by the workflow:

- Instance audit events (gitlab.com only)
- All group audit events (gitlab.com and self-hosted)
- All project audit events (gitlab.com and self-hosted)

## Parameters you will need:

- `apiHost` - hostname of your Gitlab instance
- `accessToken` - Personal Access Token with admin privileges
- `logType` - One of the following: `instance`,`groups`,`projects`
- `objectId` - Only used when `log_type` is `groups` or `projects`, represents the ID
