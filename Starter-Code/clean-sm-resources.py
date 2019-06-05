import json
import boto3
import time

def get_endpoint_names(client):
    endpoint_names = []
    endpoints =  client.list_endpoints(MaxResults = 100)["Endpoints"]
    for each in endpoints:
        name = each["EndpointName"]
        endpoint_names.append(name)
    return endpoint_names
    
def get_notebook_names(client, state):
    notebook_names = []
    notebooks = client.list_notebook_instances(MaxResults = 100)["NotebookInstances"]
    for each in notebooks:
        if each['NotebookInstanceStatus'] == state:
            name = each["NotebookInstanceName"]
            notebook_names.append(name)
    return notebook_names
    
def delete_endpoints(client, endpoint_names):
    for name in endpoint_names:
        client.delete_endpoint(EndpointName = name)
    return 0

def stop_notebook_instances(client, notebook_names):
    for name in notebook_names:
        try:
            client.stop_notebook_instance(NotebookInstanceName = name)
        except:
            continue
    return "Stopped notbook instances"

def lambda_handler(event, context):

    client = boto3.client('sagemaker')
    
    endpoint_names = get_endpoint_names(client)
    
    delete_endpoints(client, endpoint_names)

    notebook_names = get_notebook_names(client, 'InService')

    stop_notebook_instances(client, notebook_names)

    return {
        'statusCode': 200,
        'body': json.dumps('Completed lambda function to clean workshop.')
    }
