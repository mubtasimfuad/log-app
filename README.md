# log-app SAM Project

This is a Serverless Application Model (SAM) project for log management and archiving. The project includes AWS resources and configurations to store logs in DynamoDB and export them to an S3 bucket.

## Prerequisites

Before deploying the log-app SAM project, make sure you have the following:

- AWS CLI installed and configured with appropriate credentials.
- SAM CLI installed on your local machine.

## Deployment

To deploy the log-app SAM project, follow these steps:

1. Clone the repository to your local machine:

```shell
git clone <repository-url>
```

2. Navigate to the project directory:

```shell
cd log-app
```

3. Build the SAM project:

```shell
sam build
```

4. Deploy the SAM project:

```shell
sam deploy --guided
```

5. Follow the prompts to provide the necessary deployment parameters, such as bucket names, table names, and API stage names.

6. After the deployment is complete, the API endpoint URL will be displayed in the terminal output. You can use this URL to access the log-app API.

## Usage

Once the log-app SAM project is deployed, you can perform the following operations:

- **Upload Logs**: Use the API endpoint to upload logs to the log-app. Send a GET request to the API endpoint with the log data to upload it.
- **Export Logs**: Logs stored in the DynamoDB table will be automatically exported to the specified S3 bucket. The export process is triggered by a DynamoDB stream and handled by the log-export Lambda function.

## Clean Up

To remove the log-app SAM project and associated resources from your AWS account, follow these steps:

1. Delete the SAM stack using the AWS CLI:

```shell
aws cloudformation delete-stack --stack-name log-app
```

2. Confirm the deletion when prompted.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and adapt the log-app SAM project to suit your specific requirements. If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.
