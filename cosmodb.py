import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey

import os
from dotenv import load_dotenv
load_dotenv()

# ----------------------------------------------------------------------------------------------------------
# Prerequistes -
#
# 1. An Azure Cosmos account -
#    https://docs.microsoft.com/azure/cosmos-db/create-cosmosdb-resources-portal#create-an-azure-cosmos-db-account
#
# 2. Microsoft Azure Cosmos PyPi package -
#    https://pypi.python.org/pypi/azure-cosmos/
# ----------------------------------------------------------------------------------------------------------


HOST = os.environ['ACCOUNT_HOST']
MASTER_KEY = os.environ['ACCOUNT_KEY']
DATABASE_ID = os.environ['COSMOS_DATABASE']
CONTAINER_ID = os.environ['COSMOS_CONTAINER']


def getorcreatecontainer():
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)
    # setup database
    try:
        db = client.create_database(id=DATABASE_ID)
    except exceptions.CosmosResourceExistsError:
        db = client.get_database_client(DATABASE_ID)

    # setup container        
    try:
        container = db.create_container(id=CONTAINER_ID, partition_key=PartitionKey(path='/partitionKey'))
    except exceptions.CosmosResourceExistsError:
        container = db.get_container_client(CONTAINER_ID)

    return container

def create_item(container, sales_order_document ):
    container.create_item(body=sales_order_document)

