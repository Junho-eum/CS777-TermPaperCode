# CS777-TermPaperCode
## Repository Structure
```
├── Code
│   ├── AWSAthenaTask.py            # Script for executing Athena queries
│   ├── AWSGlueTask.py              # Script for managing AWS Glue tasks
│   ├── AWSS3Task-JuniorDev.py      # Demonstrates S3 access for a Junior Developer
│   ├── AWSS3Task-SeniorDS.py       # Demonstrates S3 access for a Senior Data Scientist
│   └── ForbesRichestAtheletes.csv  # Sample dataset
├── LogFiles
│   ├── GlueTask_JuniorDev.log      # Log for Glue tasks executed by Junior Developer
│   ├── GlueTask_SeniorDS.log       # Log for Glue tasks executed by Senior Data Scientist
│   ├── Junior_Dev_s3_access.log    # Log for S3 access by Junior Developer
│   └── SeniorDS_s3_access.log      # Log for S3 access by Senior Data Scientist
└── README.md
```

## AWS S3 Service Policies

This repository includes two AWS S3 service policy files designed to define and limit access to Amazon S3 resources according to the principles of least privilege. These policies are tailored for two distinct roles within our AWS environment: Junior Developer and Senior Data Scientist. Each policy ensures that the permissions granted are aligned with the responsibilities and data access needs of the respective roles.

### Junior Developer S3 Policy (`AWSS3ServicePolicy-JuniorDev.json`)

The Junior Developer policy grants read-only access to S3 resources, enabling users with this role to list, retrieve, and describe S3 objects and buckets. This policy is crafted to support scenarios where Junior Developers need to access data for analysis or application development without modifying the data or its storage container.

**Policy Actions:**
- `s3:Get*`: Allows retrieving objects and bucket properties.
- `s3:List*`: Permits listing of objects within buckets and the buckets themselves.
- `s3:Describe*`: Enables description calls for S3 resources (if applicable).
- `s3-object-lambda:Get*`: Grants access to retrieve objects through S3 Object Lambda.
- `s3-object-lambda:List*`: Allows listing operations via S3 Object Lambda.

**Resource Scope:**
- Applies to all S3 resources (`"Resource": "*"`) for broad read access, with the assumption that further access controls are managed at the bucket or account level.

### Senior Data Scientist S3 Policy (`AWSS3ServicePolicy-SeniorDS.json`)

The Senior Data Scientist policy provides full access to specific S3 buckets necessary for advanced data analysis, manipulation, and management tasks. This includes the ability to create, modify, and delete S3 objects and buckets as required for their work, demonstrating the role's elevated level of trust and responsibility.

**Policy Actions:**
- `s3:*`: Grants full access to perform any actions on S3 resources.

**Resource Scope:**
- Specifically tailored to the `fall23bu` bucket (`"Resource": ["arn:aws:s3:::fall23bu"]`), ensuring that Senior Data Scientists have extensive permissions only to the resources critical for their data projects.

## AWS Glue Service Policies

In addition to S3 service policies, this repository contains policies for AWS Glue, a fully managed extract, transform, and load (ETL) service that makes it easy for users to prepare and load their data for analytics. These policies delineate access rights for the Senior Data Scientist and Junior Developer roles, ensuring that permissions are aligned with the responsibilities and requirements of each role.

### Senior Data Scientist Glue Policy (`AWSGlueServicePolicy-SeniorDS.json`)

The Senior Data Scientist Glue policy is designed to grant extensive permissions for AWS Glue service, allowing for full management of Glue resources. This reflects the Senior Data Scientist's need for comprehensive access to perform data processing, analysis, and management tasks within AWS Glue.

**Policy Actions:**
- `s3:*`: Full access to the `fall23bu` S3 bucket, facilitating operations related to data storage and retrieval essential for Glue jobs.
- `glue:*`: Allows all actions on AWS Glue resources, enabling the Senior Data Scientist to create, execute, and manage Glue jobs, databases, and crawlers.

**Resource Scope:**
- S3 access is specifically restricted to the `arn:aws:s3:::fall23bu` bucket.
- Glue permissions apply broadly to all Glue resources (`"Resource": "*"`) to support various data processing and ETL tasks.

### Junior Developer Glue Policy (`AWSGlueServicePolicy-JuniorDev.json`)

The Junior Developer Glue policy provides limited permissions, focusing on allowing read-only access to job definitions and executions. This policy enforces the principle of least privilege by restricting the Junior Developer's ability to start Glue job runs, aligning with a more constrained scope of responsibilities.

**Policy Actions:**
- `glue:GetJob`, `glue:GetJobRuns`: Grants permission to view Glue job configurations and their execution history.
- Denies the `glue:StartJobRun` action to prevent the Junior Developer from initiating new Glue job executions.

**Resource Scope:**
- Both allowed and denied actions apply to all Glue resources (`"Resource": "*"`) to simplify policy management while ensuring that Junior Developers can only read job information without executing them.

### Implementing Policies

To attach these JSON policy files to IAM roles or users, you can use the AWS Management Console, AWS CLI, or AWS CloudFormation, ensuring that each role within your AWS environment has the appropriate permissions for their data tasks in AWS Glue. This setup allows for fine-grained control over data processing and ETL operations, reinforcing security and compliance by adhering to the least privilege principle.


