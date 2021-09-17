1. This protocol will generate Events which are "unknown" to QRadar as the events include either the EventID 
1.1 "NoAlertsReported" which you might want to map to an Event saying "No new alerts found" (or you remove the entire part from the workflow if you do not like to see this event)
1.2 OR the EventID which the alert event provides. As this is highly custom based on the alerts defined for each customer of Trend Micro One View, you will need to map all the eventIds before you can really use these events for correlation. If you want a simpler approach, simply use the predefined eventId "AlertFound" to fill the eventI field in a static way so you will always get the same eventId and do not need to worry about new kind of alerts popping up as "unknown"

