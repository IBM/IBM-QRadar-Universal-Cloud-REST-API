Author Name: Cyble Inc

Maintainer Name: developers@cyble.com

Version Number: 1.0

Endpoint Documentation: This workflow can be used to pull Indicators of Compromise (IOCs) from Cyble Vision.

Detailed documentation can be found at: https://cyble.ai/centers/help-center

Event Types Currently Supported by the workflow: Cyble IOCs (Domain, IPv4, URL, Hash, etc.)

## Workflow Parameter Description

For integrating QRadar with Cyble Vision via the workflow, you will need the following information:

| **Parameter Label** | **Parameter** | **Description**                                                                                                                                            |
|---------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hostname            | hostname      | Enter _hostname_ of Cyble Vision (e.g. `api.cyble.ai`). Contact your Customer Success Manager to get this value.                                            |
| Api Key             | api_key       | Enter _api_key_ for authentication and fetching IOCs from Cyble. Contact your Customer Success Manager to get this value.                                   |
| Fetch Since (days)  | fetch_since   | Number of days of history to retrieve on the first run.                                                                                                    |
| IOC Types           | ioc_type      | A **comma-separated** list of IOC types to fetch (no spaces), e.g. `Domain` or `Domain,IPv4,URL`. Use the exact type labels returned by the API (the `ioc_type` field). The API accepts only one type per request, so the workflow runs one paginated pass per type. |
| Risk Rating Gte     | risk_gte      | Lower bound (inclusive) of the IOC `risk_score` filter, e.g. `70`.                                                                                         |
| Risk Rating Lte     | risk_lte      | Upper bound (inclusive) of the IOC `risk_score` filter, e.g. `100`.                                                                                        |
| Regions filter      | regions       | Comma-separated list of regions to filter on, e.g. `Asia & Pacific (APAC)`. Leave **empty** to not filter by region.                      |
| Industries filter   | industries    | Comma-separated list of industries to filter on, e.g. `BFSI,Healthcare`. Leave **empty** to not filter by industry.                       |

> Note: `regions` and `industries` are always sent in the request; an **empty** value is ignored by the API (equivalent to no filter), so they are safe to leave blank.

## Discovering valid filter values

Cyble exposes a filters endpoint that returns the current valid values accepted by the IOC request body. Use it to look up the exact labels to put into `ioc_type`, `regions`, `industries`, and the other filters. It requires the same Bearer token as the workflow:

```bash
curl -X 'GET' \
  'https://api.cyble.ai/engine/api/v2/y/iocs/filters' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <API_KEY>'
```

The response is `{"data": { ... }, "success": true}`, where each key under `data` is a list of `{ "key": ..., "name": ... }` options. Use the **`key`** value in the request body. The categories map to the IOC request body as follows:

| Filters endpoint category | IOC request body field | Notes                                    |
|---------------------------|-------------------------|------------------------------------------|
| `types`                   | `iocType`               | Exposed as the `ioc_type` parameter      |
| `regions`                 | `regions`               | Exposed as the `regions` parameter  |
| `industries`              | `industries`            | Exposed as the `industries` parameter |
| `confidence_ratings`      | `confidentRating`       | Not yet exposed as a parameter           |
| `countries`               | `countryCodes`          | Not yet exposed as a parameter           |
| `sources`                 | `sources`               | Not yet exposed as a parameter           |
| `threat_actors`           | `threatActors`          | Not yet exposed as a parameter           |
| `threat_malwares`         | `malwareFamilies`       | Not yet exposed as a parameter           |
| `behaviour_tags`          | `tags`                  | Not yet exposed as a parameter           |
| `is_whitelisted`          | `isWhitelisted`         | Not yet exposed as a parameter           |

Current values for the smaller enumerations (larger lists such as `countries`, `sources`, `threat_actors`, `threat_malwares`, and `behaviour_tags` should be fetched live from the endpoint):

- **`types`** (use for `ioc_type`): `Domain`, `Email`, `FileHash-MD5`, `FileHash-SHA1`, `FileHash-SHA256`, `IPv4`, `IPv6`, `URL`, `Wallet-Address`
- **`regions`**: `Asia & Pacific (APAC)`, `Australia and New Zealand (ANZ)`, `Europe & UK`, `Middle East & Africa (MEA)`, `North America (NA)`, `South America (SA)`, `Worldwide`
- **`industries`**: `Aerospace & Defense`, `Agriculture & Livestock`, `Automotive`, `BFSI`, `Chemicals`, `Construction`, `Consumer Goods`, `Critical Infrastructure`, `Education`, `Energy & Utilities`, `Food & Beverages`, `Government & LEA`, `Healthcare`, `Hospitality`, `IT & ITES`, `Manufacturing`, `Media & Entertainment`, `Metals Minerals & Mining`, `Multiple`, `Organisation`, `Pharmaceuticals & Biotechnology`, `Professional Services`, `Real Estate`, `Retail`, `Technology`, `Telecommunication`, `Transportation & Logistics`
- **`confidence_ratings`**: `High`, `Medium`, `Low`

## QRadar Log Source Configuration

Cyble IOC Workflow utilizes QRadar's Universal Cloud REST API Protocol to fetch data from Cyble Vision.

The steps to configure a log source on the QRadar® Console using the Workflow field are as follows:

1. Log in to QRadar.
2. Admin Panel > click on the 'QRadar Log Source Management' or 'Log Sources' app icon.
3. Click 'Log Sources' > 'New Log Source' > 'Single Log Source'.
4. On the 'Select Log Source Type' page, select __Universal DSM__ from the list.
5. On the 'Select Protocol Type' page, select __Universal Cloud REST API__, and proceed to next step.
6. On the 'Configure the Log Source parameters' page, configure the log source parameters:
    - __Name__: __Cyble IOC__
    - __Enabled__: __On__
    - __Coalescing Events__: __Off__
    - Keep rest of the settings as default, and proceed to next step.
7. On the Configure the Protocol Parameters page:
    - __Log source identifier__: < same as __hostname__ above >
    - Copy the workflow code from __Cyble-IOC-Workflow.xml__ and paste it into the 'Workflow' field
    - Copy the workflow params from __Cyble-IOC-Workflow-Parameter-Values.xml__, populate the fields and paste into the 'Workflow Parameters Values' field
    - __Untrusted Certificates__: __Allow__
    - Set Recurrence as per your choice. Recommended value is 1D.
    - Keep rest of the settings as default, and proceed to next step.
8. In the Test protocol parameters window, click 'Start Test'. All tests should pass.
9. To fix any errors, click 'Configure Protocol Parameters'. Configure the parameters and click Test Protocol Parameters.
10. Click 'Finish'
11. Navigate to the 'Admin' tab. From the top bar choose 'Deploy Changes'

## Installing the Cyble IOC DSM Parser (optional)

By default the log source uses the **Universal DSM**, so incoming IOC events are stored with their raw JSON payload but are not normalized into QRadar fields. To have the IOC events parsed and mapped into proper QRadar properties, install the Cyble IOC DSM parser:

1. **Request the DSM export** — the parser is distributed as a DSM export archive (e.g. `Cyble-IOC-DSM-Export.zip`). Contact your **Customer Success Manager (Cyble)** to obtain the latest zip.
2. In your QRadar instance, navigate to **Admin Panel > Extensions Management > Add**, select the downloaded zip, and install it.
   - Alternatively, import it from the **DSM Editor** (Admin > DSM Editor > import), if provided in that format.
3. Edit the **Cyble IOC** log source and set its **Log Source Type** to the **Cyble IOC DSM** provided by the parser (instead of Universal DSM).
4. Navigate to the 'Admin' tab and choose **Deploy Changes**.

> Note: QRadar parses events at ingest time. Installing or updating the DSM only affects **new** events received after it is deployed; events already ingested under the Universal DSM are not retroactively re-parsed.
