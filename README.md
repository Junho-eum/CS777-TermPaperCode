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

The repository includes two AWS S3 service policy files tailored to define access levels for Junior Developers and Senior Data Scientists. These policies are designed to align with the principle of least privilege, ensuring that each role has access only to the resources necessary for their tasks.

### AWSS3ServicePolicy-JuniorDev.json

This policy grants Junior Developers read-only access to S3 resources. The permissions include the ability to get and list objects and buckets within S3, as well as the same actions for S3 Object Lambda, providing limited but sufficient access for viewing and analyzing data stored in S3.

**Permissions Granted:**
- `s3:Get*`
- `s3:List*`
- `s3:Describe*`
- `s3-object-lambda:Get*`
- `s3-object-lambda:List*`

**Resource Scope:** All S3 resources (`*`), which should be further restricted in practice to specific buckets as necessary.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:Get*",
        "s3:List*",
        "s3:Describe*",
        "s3-object-lambda:Get*",
        "s3-object-lambda:List*"
      ],
      "Resource": "*"
    }
  ]
}
