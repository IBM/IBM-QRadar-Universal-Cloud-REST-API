# Rapid& CyberInt Parameters Configuration
Parameter                           | Name | Default Value | Type | Required (True/False) | Description
---                                 | --- | --- | --- |--- |---
hostname                            | Host Name | https://cyberint.com | String | True | IP or URL for the instance.
api_key                             | API Key | False | Authentication | True | 
severity                            | Severity | "very_high" "high", "medium", "low" | String | False | You can specify the alert severity to pull.
status                              | Status | "open", "acknowledged", "closed" | String | False | You can specify the alert status to pull.
