import logging
import requests
import json
import ibm_boto3
import gzip

from time import time
from ibm_botocore.client import Config, ClientError



def main(params):
    #validate params
    logging.info("Validating parameters")
    validationResult = validateParams(params)
    if validationResult[0] != True:
        return {'Error': validationResult[1]}
    else:
        validatedParams = validationResult[1]

    #download COS file
    cos = ibm_boto3.client("s3",ibm_api_key_id=params['cos_api_key'],ibm_service_instance_id=params['cos_instance_crn'],config=Config(signature_version="oauth"),endpoint_url=params['cos_endpoint'])
    file = cos.get_object(Bucket=params['bucket'], Key=params['key'])
    data_body = file['Body']
    
    #Unzip and get JSON logs
    with gzip.open(data_body, 'rt') as flow_data:
            for lines in flow_data:
                for flow_entry in (json.loads(lines)["flow_logs"]):                    
                    if flow_entry['start_time']:
                        print(json.dumps(flow_entry))
                        #PUT JSON logs into LogDNA
                        success = sendToLogDna(json.dumps(flow_entry),params)
                        if not success:
                            return {"Error":"Failed sending to LogDNA"}
    return {"Success":"Logs sent to LogDNA"}
                        

def validateParams(params):
    validatedParams = params.copy()
    requiredParams = ['cos_endpoint', 'cos_api_key', 'cos_instance_crn', 'logdna_host', 'logdna_injest_key']
    missingParams = []    

    for requiredParam in requiredParams:
        if requiredParam not in params:
            missingParams.append(requiredParam)

    if len(missingParams) > 0:
        return (False, "You must supply all of the following parameters: {}".format(', '.join(missingParams)))
        
    return (True,"Validated Params")
    
 
def sendToLogDna(flow_entry, params):
    #Build Headers
    time_stamp = str( round(time()*1000))
    url_params = {'hostname':'VPC_FLOW_LOGS','now':time_stamp, 'apikey':params['logdna_injest_key']}
    url = params['logdna_host']
    post_data = {"lines":[
                    {"timestamp": time_stamp, 
                     "line":flow_entry,
                     "app":"vpc_flow_logs"}
                   ]
                  }
    headers = {'Content-Type': 'application/json; charset=UTF-8'}    
    r = requests.post(url, headers=headers, params=url_params, data=post_data)
    print(post_data)
    if (r.status_code == 200):
        return True
    else:
        logging.error("Error Posting to LogDNA: " + r.text)
        return False