def main():
    import boto3
    boto3.setup_default_session(profile_name='localstack')
    import auditlog.writer

if __name__ == 'auditlog':
    main()