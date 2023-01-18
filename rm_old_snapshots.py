import boto3
import datetime 

ec2 = boto3.resource('ec2')

max_age = 180

snaps = ec2.snapshots.filter(OwnerIds=['self'])

for snap in snaps:
    snap_time = snap.start_time.date()
    now = datetime.datetime.now().date()
    snap_age = (now - snap_time).days

    if(snap_age > max_age):
        try:
            snap.delete(snap.id)
            print(snap.id,'created on',snap_time,'has been deleted.')
        except:
            print(snap.id,'will not be deleted. It is most likely in use.')
            continue
