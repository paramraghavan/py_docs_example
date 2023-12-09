import boto3

def lambda_handler(event, context):
    """
    AWS Lambda function using Boto3.

    :param event: AWS Lambda uses this parameter to pass in event data to the handler.
    :param context: AWS Lambda uses this parameter to provide runtime information to your handler.
    :return: Response object
    """
    # Example: List S3 Buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    return response
