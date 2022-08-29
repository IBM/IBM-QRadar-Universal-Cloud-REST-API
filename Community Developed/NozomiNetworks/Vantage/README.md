### Workflow for Nozomi Networks Vantage

#### Author Name: Nozomi Networks
#### Maintainer Name: NozomiNetworks
#### Version Number: 1.0.0
#### Event Types Currently Supported by the workflow: Alerts and Assets

#### Workflow Parameter Values
To configure the _Workflow_ the user has to add the _Workflow Parameter Values_ containing the Vantage `host`, `key_name`, `key_token` and the `org` (organization name).
To generate the `key_name` and the `key_token` follow the Vantage guide.  
The _organization name_ if match more than one organization will return the data of the first one: if does not match anyone will return the data of the default organization.


The organization name could contain a special character, every special characters has to be escaped, examples:

`"` to  `&quot;`

`'` to `&apos;`

`<` to `&lt;`

`>` to `&gt;`

`&` to `&amp;`


#### Example

The organization name: 
```Dolce&Gabbana``` 
must be written inside the XML as: 
```Dolce&amp;Gabbana```

#### Workflow
The workflow get all the Assets and Alerts from the host configured.
It could be useful to get the Alerts only from a given time, to do it you can modify the Workflow bookmark initialization; for example if you want to get the Alerts from the last hour you can initialize the bookmark as:

```<Initialize path="/bookmark" value="${time() - 3600000}" />```

### Log Source Identifier

The `Alert` events returned by the app are mapped with the proper `Event MAppings` if the `name` of the Alert in the payload match with the event id.

For example the payload here:
```
{"id":"analertid","type":"alerts","attributes":{"risk":9,"ack":false,**"name":"Malware detection"**,"time":1657774054000,"id_dst":"172.16.0.55","id_src":"172.16.0.253","ip_dst":"172.16.0.55","ip_src":"172.16.0.253","status":"open","mac_dst":"00:0c:BB:BB:BB:BB","mac_src":"00:AA:AA:AA:AA:AA","port_dst":445,"port_src":43221,"protocol":"smb","zone_dst":"Production-11","zone_src":"Production-11","dst_roles":"other","src_roles":"consumer","type_name":"Malware detection", "properties":{"cause":"An user has clicked on untrusted link and a malware is being transferred, or an already existing malware is downloading additional pieces from a local share.","solution":"Perform an investigation and cleanup the victim, and block or cleanup also the attacker."
...
```
match witht the `Nozomi Vantage Event` having name `Malware detection`

The `Asset` events are mapped with the `ASSET-INFO` mapping event if the `type` field of the payload is `assets`.

To see all the Properties and `Event Mappings` in the `Nozomi Netoworks Vantage` app for QRadar go to the `DSM editor` and select the `Nozomi Networks Vantage`  `Log Source Type`.

### Troubbleshooting
To see the logs of the apconnect via `ssh` with your QRadar instance and go to:

```
docker ps #to get the container id 
docker exec -it container_id /bin/bash #to go inside the app docker 
cat opt/app-root/store/log/startup.log #to print the logs
```

or check for errors in the logs here:

```
- /var/log/qradar.log
- /var/log/qradar.error
```

the workflow print some logs starting with `NN Vantage`.

### Support
If you have any issues with the Workflow and/or the `Nozomi Netoworks Vantage` app for QRadar you can ask support to:
`support@nozominetworks.com`
