import boto3
from botocore.exceptions import ClientError
import time
import sys
import logging

# Setup logging
logging.basicConfig(filename='Glue_Job_Run.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def start_glue_job(glue_client, job_name):
    try:
        # Attempt to start the Glue job
        response = glue_client.start_job_run(JobName=job_name)
        job_run_id = response['JobRunId']
        logging.info(f"Started Glue job: {job_name} with run ID: {job_run_id}")
        return job_run_id
    except ClientError as e:
        logging.error(f"Failed to start Glue job {job_name}: {e.response['Error']['Message']}")
        return None

def check_job_status(glue_client, job_name, job_run_id):
    while True:
        try:
            # Attempt to check the status of the job run
            response = glue_client.get_job_run(JobName=job_name, RunId=job_run_id)
            status = response['JobRun']['JobRunState']
            logging.info(f"Job run {job_run_id} status: {status}")
            if status in ['SUCCEEDED', 'FAILED', 'STOPPED', 'TIMEOUT']:
                return status
            time.sleep(30)  # Wait before checking the status again
        except ClientError as e:
            logging.error(f"Error checking status of job run {job_run_id}: {e.response['Error']['Message']}")
            return None

if __name__ == "__main__":
    profile_name = sys.argv[1]
    
    if len(sys.argv) < 3:
        logging.error("Usage: python script.py <profile_name> <glue_job_name>")
        sys.exit(1)
        
    profile_name, glue_job_name = sys.argv[1], sys.argv[2]
    session = boto3.Session(profile_name=profile_name)
    glue_client = session.client('glue')

    logging.info(f"Attempting to execute Glue job: {glue_job_name}")
    job_run_id = start_glue_job(glue_client, glue_job_name)

    if job_run_id:
        final_status = check_job_status(glue_client, glue_job_name, job_run_id)
        logging.info(f"Final status of Glue job run {job_run_id}: {final_status}")
    else:
        logging.error("Failed to start Glue job due to insufficient permissions.")
