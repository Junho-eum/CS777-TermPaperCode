import boto3
from botocore.exceptions import ClientError
import time
import sys
import logging

# Setup logging
logging.basicConfig(filename='Athena_Query_Run.log', filemode='w',
                    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def execute_athena_query(athena_client, query, database, s3_output):
    try:
        # Start the Athena query
        response = athena_client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={'Database': database},
            ResultConfiguration={'OutputLocation': s3_output, })
        query_execution_id = response['QueryExecutionId']
        logging.info(
            f"Started Athena query with Execution ID: {query_execution_id}")
        return query_execution_id
    except ClientError as e:
        logging.error(f"Failed to execute Athena query due to an error: {e}")
        return None


def check_query_status(athena_client, query_execution_id):
    while True:
        try:
            # Check the status of the query execution
            response = athena_client.get_query_execution(
                QueryExecutionId=query_execution_id)
            status = response['QueryExecution']['Status']['State']
            logging.info(
                f"Query Execution ID {query_execution_id} status: {status}")
            if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
                logging.info(
                    f"Final status of Athena query {query_execution_id}: {status}")
                return status
            time.sleep(5)  # Wait before checking the status again
        except ClientError as e:
            logging.error(
                f"Error checking status of query {query_execution_id}: {e}")
            return None


if __name__ == "__main__":
    if len(sys.argv) < 5:
        logging.error(
            "Usage: python script.py <profile_name> '<query>' <database> <s3_output>")
        sys.exit(1)

    profile_name, query, database, s3_output = sys.argv[1:5]
    session = boto3.Session(profile_name=profile_name)

    # Create Athena client with the session
    athena_client = session.client('athena')

    # Execute the Athena query
    query_execution_id = execute_athena_query(
        athena_client, query, database, s3_output)

    if query_execution_id:
        final_status = check_query_status(athena_client, query_execution_id)

# python3 /Users/junhoeum/Desktop/Fall23/CS777/TermPaper/Code/AWSAthenaTask.py juno "SELECT * FROM your_table LIMIT 10" term_paper_database s3://fall23bu/CS550/
