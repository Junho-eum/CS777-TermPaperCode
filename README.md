# CS777-TermPaperCode
## Repository Structure

# Project Repository Structure

This repository contains scripts, log files, and IAM policy files used in the demonstration of AWS service tasks and the application of IAM policies for role-specific access control. The structure and contents of this repository are as follows:

## Code
Scripts used for executing tasks on AWS services and checking configurations.
- `AWSAthenaTask-mgmt.py`: Script for managing Athena resources to test IAM policy restrictions
- `AWSAthenaTask.py`: Script for executing Athena queries
- `AWSGlueTask.py`: Script for managing AWS Glue tasks
- `AWSS3Task-JuniorDev.py`: Demonstrates restricted S3 access for a Junior Developer
- `AWSS3Task-SeniorDS.py`: Demonstrates full S3 access for a Senior Data Scientist
- `CheckConfig.py`: Utility script to check AWS configurations or permissions
- `ForbesRichestAtheletes.csv`: Sample dataset used in demonstrations

## LogFiles
Contains logs generated from the execution of scripts, providing insights into task outcomes and policy enforcement.
- `AthenaTask_JuniorDev.log`: Log for Athena query tasks executed by Junior Developer
- `AthenaTask_SeniorDS.log`: Log for Athena query tasks executed by Senior Data Scientist
- `Athena_Management_Actions_JuniorDev.log`: Log capturing attempts by Junior Developer to manage Athena resources
- `Athena_Management_Actions_SeniorDS.log`: Log for Athena management actions successfully performed by Senior Data Scientist
- `GlueTask_JuniorDev.log`: Log for Glue tasks showing restricted actions by Junior Developer
- `GlueTask_SeniorDS.log`: Log for successful Glue tasks executed by Senior Data Scientist
- `Junior_Dev_s3_access.log`: Log detailing S3 access attempts by Junior Developer
- `SeniorDS_s3_access.log`: Log for unrestricted S3 access by Senior Data Scientist

## Policies
IAM policies designed to specify and restrict access based on role responsibilities.
- `AWSAthenaFullAccess.json`: General full access policy for Athena (not role-specific)
- `AWSAthenaServicePolicy-JuniorDev.json`: Defines Athena access for Junior Developer, focusing on query execution without management actions
- `AWSAthenaServicePolicy-SeniorDS.json`: Athena access policy for Senior Data Scientist, allowing comprehensive service management
- `AWSGlueServicePolicy-JuniorDev.json`: Glue policy restricting Junior Developer access to read-only operations
- `AWSGlueServicePolicy-SeniorDS.json`: Full Glue access policy for Senior Data Scientist
- `AWSS3ServicePolicy-JuniorDev.json`: S3 policy granting read-only access to Junior Developer
- `AWSS3ServicePolicy-SeniorDS.json`: S3 policy providing full access for Senior Data Scientist

## AWS S3 Service Policies

This repository includes two AWS S3 service policy files designed to define and limit access to Amazon S3 resources according to the principles of least privilege. These policies are tailored for two distinct roles within the AWS environment: Junior Developer and Senior Data Scientist. Each policy ensures that the permissions granted are aligned with the responsibilities and data access needs of the respective roles.

### Junior Developer S3 Policy (`AWSS3ServicePolicy-JuniorDev.json`)

The Junior Developer policy grants read-only access to S3 resources, enabling users with this role to list, retrieve, and describe S3 objects and buckets. This policy is crafted to support scenarios where Junior Developers need to access data for analysis or application development without modifying the data or its storage container.

**Policy Actions:**
- `s3:Get*`: Allows retrieving objects and bucket properties.
- `s3:List*`: Permits listing of objects within buckets and the buckets themselves.
- `s3:Describe*`: Enables description calls for S3 resources (if applicable).
- `s3-object-lambda:Get*`: Grants access to retrieve objects through S3 Object Lambda.
- `s3-object-lambda:List*`: Allows listing operations via S3 Object Lambda.

**Resource Scope:**
- Applies to S3 resources in s3 bucket fall23bu for read access to the specified bucket.

### Senior Data Scientist S3 Policy (`AWSS3ServicePolicy-SeniorDS.json`)

The Senior Data Scientist policy provides full access to specific S3 buckets necessary for advanced data analysis, manipulation, and management tasks. This includes the ability to create, modify, and delete S3 objects and buckets as required for their work, demonstrating the role's elevated level of trust and responsibility.

**Policy Actions:**
- `s3:*`: Grants full access to perform any actions on S3 resources.

**Resource Scope:**
- Specifically tailored to the `fall23bu` bucket (`"Resource": ["arn:aws:s3:::fall23bu"]`), ensuring that Senior Data Scientists have extensive permissions only to the resources critical for their data projects.

## AWS Glue Service Policies

In addition to S3 service policies, this repository contains policies for AWS Glue, a fully managed extract, transform, and load (ETL) service that makes it easy for users to prepare and load their data for analytics. These policies arranges access rights for the Senior Data Scientist and Junior Developer roles. 

### Senior Data Scientist Glue Policy (`AWSGlueServicePolicy-SeniorDS.json`)

The Senior Data Scientist Glue policy is designed to grant extensive permissions for AWS Glue service, allowing for full management of Glue resources. This reflects the Senior Data Scientist's need for comprehensive access to perform data processing, analysis, and management tasks within AWS Glue.

**Policy Actions:**
- `s3:*`: Full access to the `fall23bu` S3 bucket, facilitating operations related to data storage and retrieval essential for Glue jobs.
- `glue:*`: Allows all actions on AWS Glue resources, enabling the Senior Data Scientist to create, execute, and manage Glue jobs, databases, and crawlers.

**Resource Scope:**
- S3 access is specifically restricted to the `arn:aws:s3:::fall23bu` bucket.
- Glue permissions apply broadly to all Glue resources (`"Resource": "*"`) to support various data processing and ETL tasks.

### Junior Developer Glue Policy (`AWSGlueServicePolicy-JuniorDev.json`)

The Junior Developer Glue policy provides limited permissions, focusing on allowing read-only access to job definitions and executions. This policy enforces the principle of least privilege by restricting the Junior Developer's ability to start Glue job runs. 

**Policy Actions:**
- `glue:GetJob`, `glue:GetJobRuns`: Grants permission to view Glue job configurations and their execution history.
- Denies the `glue:StartJobRun` action to prevent the Junior Developer from initiating new Glue job executions.

**Resource Scope:**
- Both allowed and denied actions apply to all Glue resources (`"Resource": "*"`) to simplify policy management while ensuring that Junior Developers can only read job information without executing them.

## AWS Athena Service Policy for Senior Data Scientist (`AWSAthenaServicePolicy-SeniorDS.json`)

The AWS Athena Service Policy for Senior Data Scientists grants comprehensive permissions for querying data with Athena, managing related AWS Glue resources, accessing query results in S3, and interacting with other AWS services that integrate with Athena. 

#### Policy Actions:

- **Base Athena Permissions (`BaseAthenaPermissions`)**: Grants full access to Athena (`athena:*`), enabling the execution of queries, management of query execution environments, and configuration of Athena settings.

- **Base Glue Permissions (`BaseGluePermissions`)**: Allows comprehensive management of AWS Glue resources which are often used in conjunction with Athena for data cataloging and ETL operations.

- **Base Query Results Permissions (`BaseQueryResultsPermissions`)**: Facilitates access to S3 buckets used for storing Athena query results, ensuring Senior Data Scientists can store, retrieve, and manage query outputs.

- **Base Athena Examples Permissions (`BaseAthenaExamplesPermissions`)**: Provides access to Athena example resources stored in S3, allowing users to fetch example datasets and queries for learning and experimentation.

- **Base S3 Bucket Permissions (`BaseS3BucketPermissions`)**: Grants permissions to list and access S3 buckets, crucial for managing data files used in Athena queries.

### Implementing Policies

To attach these JSON policy files to IAM roles or users, use the AWS Management Console, AWS CLI, or AWS CloudFormation, ensuring that each role within your AWS environment has the appropriate permissions.

## Demonstrating AWS Athena Policies with `AWSAthenaTask.py`

The `AWSAthenaTask.py` script simulates how Senior Data Scientists can leverage Athena for data querying under the permissions granted by the `AWSAthenaServicePolicy-SeniorDS.json`. 

### Script Functionality

- **Query Execution**: Executes a provided SQL query within Amazon Athena to analyze data as permitted under the comprehensive access granted to Senior Data Scientists.
- **Logging**: Records each step of the Athena query execution process, from initiation to completion, in an `Athena_Query_Run.log` file. 

### Usage

The script can be run from the command line with the following format:

```bash
python3 AWSAthenaTask.py <profile_name> '<query>' <database> <s3_output>
```

## Demonstrating AWS Glue Policies with `AWSGlueTask.py`

The `AWSGlueTask.py` script plays a pivotal role in our exploration of IAM policy enforcement within AWS Glue services. It is specifically designed to test the IAM policies assigned to the Senior Data Scientist and Junior Developer roles by initiating AWS Glue jobs and monitoring their execution status. This practical demonstration highlights the nuances of access control and permissions within AWS Glue.

### Script Functionality

- **Glue Job Execution**: Initiates AWS Glue jobs, showcasing the Senior Data Scientist's ability to leverage Glue for complex ETL tasks, in alignment with the permissions granted by their IAM policy.
- **Status Monitoring**: Continuously checks and logs the execution status of the Glue jobs, providing insights into the operational impact of the IAM policies on Glue job executions.

### Usage

Execute the script from the command line using the following format:

```bash
python AWSGlueTask.py <profile_name> <glue_job_name>
```

### Example Command
```bash
python AWSGlueTask.py SeniorDataScientist sample-glue-job
```

## Demonstrating S3 Policies with `AWSS3Task.py`

This script is tailored to test the S3 policies applied to the Senior Data Scientist and Junior Developer roles, focusing on operations within Amazon S3. By performing actions such as listing objects in a bucket, downloading, and uploading objects, `AWSS3Task.py` concretely demonstrates the effects of IAM policies on S3 access and manipulation.

### Script Functionality

`AWSS3Task.py` encompasses several functions to interact with S3, reflecting different levels of access permissions as defined by IAM policies:

- **List Bucket Objects**: Demonstrates the ability to list objects within a specific S3 bucket directory, showcasing read permissions.
- **Download Object**: Tests the capability to download an object from S3, highlighting the implications of read permissions.
- **Upload Object**: Examines the permission to upload an object to S3, differentiating between roles with read-only access versus those with write permissions.

### Usage

To utilize the script, execute it from the command line with the syntax:

```bash
python AWSS3Task.py <profile_name>
```

### Example Command

```bash
python AWSS3Task.py SeniorDataScientist
```
