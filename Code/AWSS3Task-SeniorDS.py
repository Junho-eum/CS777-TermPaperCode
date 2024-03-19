import boto3
from botocore.exceptions import ClientError
import sys
import logging

# Setup logging
logging.basicConfig(filename='SeniorDS_s3_access.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to list objects in a bucket's directory
def list_bucket_objects(s3_client, bucket_name, prefix):
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        if 'Contents' in response:
            for obj in response['Contents']:
                logging.info(obj['Key'])
        else:
            logging.info("No objects found in the prefix.")
    except ClientError as e:
        logging.error(e.response['Error']['Message'])

# Function to download an object from a bucket
def download_object(s3_client, bucket_name, object_name, file_name):
    try:
        s3_client.download_file(bucket_name, object_name, file_name)
        logging.info(f"{object_name} has been downloaded to {file_name}.")
    except ClientError as e:
        logging.error(e.response['Error']['Message'])


# Function to upload an object to a bucket
def upload_object(s3_client, bucket_name, object_name, file_name):
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        logging.info(f"{file_name} has been uploaded as {object_name}.")
    except ClientError as e:
        logging.error(e.response['Error']['Message'])
    except Exception as e:
        # Catching any exception that wasn't caught by specific handlers above
        logging.error(f"Unexpected error occurred: {str(e)}")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Usage: python script.py <profile_name>")
        sys.exit(1)

    profile_name = sys.argv[1]
    session = boto3.Session(profile_name=profile_name)
    s3_client = session.client('s3')

    bucket_name = 'fall23bu'
    object_name = 'Paper-Demo/ForbesRichestAtheletes.csv'
    file_name = 'ForbesRichestAtheletes.csv'
    file_name_to_upload = '/Users/junhoeum/Desktop/Fall23/CS777/HW2/assignment2-student-data.csv'

    logging.info("Listing bucket objects:")
    list_bucket_objects(s3_client, bucket_name, "Paper-Demo/")

    logging.info("\nDownloading an object:")
    download_object(s3_client, bucket_name, object_name, file_name)

    logging.info("\nUploading an object:")
    upload_object(s3_client, bucket_name, "Paper-Demo/my-upload-test_SeniorDS.csv", file_name_to_upload)
