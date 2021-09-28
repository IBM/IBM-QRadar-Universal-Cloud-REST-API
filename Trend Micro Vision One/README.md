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
