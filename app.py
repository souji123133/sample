import boto3
import os

def lambda_handler(event, context):
    rds_client = boto3.client('rds')

    # Get read replica ID from environment variables or event
    replica_instance_id = os.getenv('READ_REPLICA_ID', 'your-read-replica-id')

    # Promote the read replica to master
    try:
        response = rds_client.promote_read_replica(
            DBInstanceIdentifier=replica_instance_id
        )
        print(f"Promoted read replica: {replica_instance_id}")
        return response
    except Exception as e:
        print(f"Error promoting replica: {e}")
        raise

