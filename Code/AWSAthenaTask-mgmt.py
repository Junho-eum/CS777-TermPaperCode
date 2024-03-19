import boto3
from botocore.exceptions import ClientError
import sys
import logging

# Setup logging
logging.basicConfig(filename='Athena_Management_Actions.log', filemode='w',
                    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def list_athena_databases(athena_client):
    try:
        # Attempt to list databases in Athena
        response = athena_client.list_databases(CatalogName='AwsDataCatalog')
        logging.info("Successfully listed Athena databases.")
        for db in response['DatabaseList']:
            logging.info(f"Database: {db['Name']}")
    except ClientError as e:
        logging.error(f"Failed to list Athena databases due to an error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Usage: python script.py <profile_name>")
        sys.exit(1)

    profile_name = sys.argv[1]

    # Set the session to use your specified profile
    session = boto3.Session(profile_name=profile_name)

    # Create Athena client with the session
    athena_client = session.client('athena')

    # Attempt to perform management action
    list_athena_databases(athena_client)
