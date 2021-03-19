import boto3
from auditlog.writer.writer import kinesis_writer

kinesis_writer.set_client(boto3.client('kinesis', endpoint_url='http://localhost:4566/'))