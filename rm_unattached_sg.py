import boto3
 
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

sgs = list(ec2.security_groups.all())
hosts = list(ec2.instances.all())

all_sgs = set([sg.group_id for sg in sgs])
attached_sgs = set([sg['GroupId'] for host in hosts for sg in host.security_groups])
not_attached_sgs = all_sgs - attached_sgs

for group_id in not_attached_sgs:
  try:  
    client.delete_security_group(GroupId=group_id,DryRun=True)
    print(group_id,'has been deleted.')
  except:
    print(group_id,'will not be deleted. It is most likely in use.')
    continue
