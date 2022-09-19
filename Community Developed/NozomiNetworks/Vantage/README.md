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

It's important that, when you set the "Recurrence" time property of the LogSource, it must be big enough for the Workflow to get all the data before another LogSource job run. If concurrency between parallel LogSource jobs happens some events could be imported twice. 
You have to be mostly aware of this if the `bookmark` initial value it's set to `0`, it means that all the events will be imported in the first run.

