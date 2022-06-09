#### Workflow Parameter Values
To configure the _Workflow_ the user has to add the _Workflow Parameter Values_ containing the Vantage `host`, `key_name`, `key_token` and the `org` (organization name).
To generate the `key_name` and the `key_token` follow the Vantage guide.  
The _organization name_ if match more than one organization will return the data of the first one: if does not match anyone will return the data of the default organization.

Every XML special characters that could be contained in the parameter values as to be escaped, examples:

`"` to  `&quot;`

`'` to `&apos;`

`<` to `&lt;`

`>` to `&gt;`

`&` to `&amp;`
