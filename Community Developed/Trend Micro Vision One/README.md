- Input Parameters: 
  - Bearer Token: A token you get from the Vision One Portal or the Trend Micro Support
  - TrendMicro Vision One API Base URL (e.g. api.eu.xdr.trendmicro.com): check here for the corect base URL https://automation.trendmicro.com/xdr/Guides/Regional-Domains

- Log Source setup
  - Setting it up without allowing untrusted certificates did not work for me which is why I set it up to allow untrusted certificates. Importing the certificate chain into the   QRadar trust store did not do the job for me. 

- Log Source tests
  - The SSL connection test is not possible somehow (my guess is the wildcard certificate TrendMicro is using is causing problems in QRadar)
  - I did not test the http through proxy as I did not have the chance to test this with a proxy 

- Events creation
  - This protocol will generate Events which are "unknown" to QRadar as the events include either the EventID 
"NoAlertsReported" which you might want to map to an Event saying "No new alerts found" (or you remove the entire part from the workflow if you do not like to see this event)
OR the EventID which the alert event provides. As this is highly custom based on the alerts defined for each customer of Trend Micro One View, you will need to map all the eventIds before you can really use these events for correlation. If you want a simpler approach, simply use the predefined eventId "AlertFound" to fill the eventI field in a static way so you will always get the same eventId and do not need to worry about new kind of alerts popping up as "unknown"

- Example Event (sanitized with "XXXX" at some points)
  - <191>1 2021-09-28T14:55:41.542Z - - - LEEF:2.0|IBM|Trend Micro Vision One|1.0|Network Discovery|0x7c|cat=Suspicious Activity|devTime=2021-09-28T14:55:41.542Z|devTimeFormat=yyyy-MM-dd'T'HH:mm:ss.SSS'Z'|sev=3|usrName=nt authority\system|url=https://portal.eu.xdr.trendmicro.com/index.html#/workbench?workbenchId=WB-XXXX-20210928-00004&ref=0c12e642cXXXXXXXXXXX|LastPollStartTime=2021-09-27T14:55:41.541Z|LastPollEndTime=2021-09-28T14:55:41.542Z|payload={"info":{"code":3002000,"msg":"Get workbench details successfully."},"data":{"schemaVersion":"1.8","workbenchId":"WB-11237-20210928-00004","workbenchLink":"https://portal.eu.xdr.trendmicro.com/index.html#/workbench?workbenchId=WB-11237-20210928-00004&ref=0c12e642ca5XXXXXXXXXX","alertProvider":"SAE","model":"Network Discovery","description":"Attempts to scan ports were detected on the network.","score":"26","modelSeverity":"low","impactScope":[{"entityValue":"nt authority\\system","entityId":"nt authority\\system","relatedEntities":["1E244F35-85F1-4C5B-87D5-F25871B0C7EA"],"relatedIndicators":[],"entityType":"account"},{"entityValue":{"guid":"1E244F35-85F1-4C5B-87D5-XXXXXXXX","name":"XXXXXXX","ips":["10.XXX.XXX.XXX"]},"entityId":"1E244F35-85F1-4C5B-XXXXXXXXXXXXX","relatedEntities":["nt authority\\system"],"relatedIndicators":[1],"entityType":"host"}],"indicators":[{"id":1,"objectType":"command_line","objectValue":"\"C:\\Program Files (x86)\\BigFix Enterprise\\XXXXXXX\\NMAP\\nmap.exe\" -sV -sS -sU -p T:22,T:23,T:80,T:135,T:139,T:445,T:235,T:61616,U:52311 --exclude \"192.168.XXX.XXX,192.168.XXX.XXX,10.XXX.XXX.XXX\" -O --osscan-guess -T 4 10.XXX.XXX.XXX/24 -oX \"C:\\Windows\\temp\\nmap\\XXXXXXX.xml\" ","relatedEntities":["1E244F35-85F1-4C5B-87D5-XXXXXXX"],"filterId":["f555c40a-8471-4287-a829-XXXXXX"]}],"matchedRules":[{"id":"cb4d06b0-29f8-40ed-9c27-XXXXXXX","name":"Network Discovery - Endpoint","matchedFilters":[{"id":"f555c40a-8471-4287-a829-XXXXXXX","name":"Network Service Scanning Via Nmap","timestamp":"2021-09-28T06:44:49.730Z","mitreTechniques":["T1046","V9.T1046"]}]}],"alertTriggerTimestamp":"2021-09-28T06:46:46.530Z","workbenchCompleteTimestamp":"2021-09-28T06:47:33Z"}}

  - Standard properties or CEPs to adjust or extract:
    - AlertID: regex: workbenchId":"(.*?)",  OR use JSON keypath. Recommended to index offenses on the alertID 
    - Username: LEEFKey: usrName  --> I worked with the assumption that there can only be one username in an alert (not confirmed by TrendMicro at the time of writing this)
    - URL: LEEFKey: url --> analysts found it nice to get the workbench URL extracted. 

- QID Mapping
  - The way I set up the posted events requires a mapping of each possible EventID (pull a list of EventIDs here: https://<YourAPIEndpoint>/v2.0/xdr/dmm/models). If you want a generic mapping and only one QID you will need to change this part "${/get_events_alertDetails/response/body/data/model}" in "<!-- prepare event content and post the event -->" with something generic like "Alert" and then create a mapping for it in QRadar. I like to see immeditately what the alert is about so I choose the precise solution over this one. 

