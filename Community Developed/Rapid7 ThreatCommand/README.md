# Rapid& ThreatCommand Parameters Configuration
Parameter                           | Name | Default Value | Type | Required (True/False) | Description
---                                 | --- | --- | --- |--- |---
hostname                            | Host Name | https://api.ti.insight.rapid7.com | String | True | IP or URL for the instance.
account_id                          | Account ID | False | Authentication | True | 
api_key                             | API Key | False | Authentication | True | 
severity                            | Severity | "High", "Medium", "Low" | String | False | you can specify the alert severity to pull
is_closed                           | Is Closed | True | Bool | False | Change to folse for ignoring closed alerts