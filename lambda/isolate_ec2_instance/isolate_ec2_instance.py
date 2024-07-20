import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instance_id = event['detail']['resource']['instanceDetails']['instanceId']
    response = ec2.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=['sg-0123456789abcdefg']  # Your restricted security group ID
    )
    print(f"Instance {instance_id} isolated: {response}")
