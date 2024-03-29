
#!/usr/bin/env python
# the script will create snapshots of volumes and delete volumes which are older than 2 weeks

import boto
from boto import ec2
from datetime import datetime
from datetime import timedelta

conn_us = boto.ec2.connect_to_region('us-east-1',aws_access_key_id='AKIAIWM7N2XR34NU6NQQ',aws_secret_access_key='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')

now = datetime.now()

today = now.date()

#first EBS volume description
#vmail_root_vol_description = "mail-root-8G-%s" % today
#second EBS volume decription
#vmail_mail_vol_description = "vmail-50G-%s" % today
#third EBS volume description
#vhosting3_gluster_vol_description = "vhosting3-gluster-30G-%s" % today
#DC-CB-AWS-04 volume description
dc_cb_AWS_04_vol_description = "DC-CB-AWS-04-%s" % today

#Create snapthot for DC-CB-AWS-04
conn_us.create_snapshot ("vol-2545d8c4", description=dc_cb_AWS_04_vol_description)
#create snapshot for first EBS volume
#conn_eu.create_snapshot ("vol-2545d8c4", description=vmail_root_vol_description)
#create snapshot for second EBS volume
#conn_eu.create_snapshot ("vol-XXXXXXXX", description=vmail_mail_vol_description)
#create snapshot for third EBS volume:
#conn_eu.create_snapshot ("vol-XXXXXXXX", description=vhosting3_gluster_vol_description)

# calculate description two weeks from now:
two_weeks_ago = (today - timedelta(days=13))
dc_cb_AWS_04_vol_description_two_weeks_ago = "DC-CB-AWS-04-%s" % two_weeks_ago
#vmail_root_vol_description_two_weeks_ago = "vmail-root-8G-%s" % two_weeks_ago
#vmail_mail_vol_description_two_weeks_ago = "vmail-50G-%s" % two_weeks_ago
#vhosting2_root_vol_description = "vhosting3-gluster-30G-%s" % two_weeks_ago

# grab snapshot for first EBS volume 2 weeks ago, and delete it
two_weeks_ago_vmail_root_snapshot = conn_eu.get_all_snapshots(filters = {"description": vmail_root_vol_description_two_weeks_ago})
#grab snapshot-ID (since result is in list-of-tuples format)
try:
two_weeks_ago_all_snapshots2 = two_weeks_ago_vmail_root_snapshot[0]
two_weeks_ago_all_snapshots3 = two_weeks_ago_vmail_root_snapshot2.id
#delete snapshot
conn_eu.delete_snapshot(two_weeks_ago_all_snapshots3)
except:
print "no snapshot two weeks ago to delete!"

#same for second EBS volume
two_weeks_ago_vmail_mail_snapshot = conn_eu.get_all_snapshots(filters = {"description": vmail_mail_vol_description_two_weeks_ago})
try:
two_weeks_ago_vmail_mail_snapshot2 = two_weeks_ago_vmail_mail_snapshot[0]
two_weeks_ago_vmail_mail_snapshot3 = two_weeks_ago_vmail_mail_snapshot2.id
conn_eu.delete_snapshot(two_weeks_ago_vmail_mail_snapshot3)
except:
print "no snapshot two weeks ago to delete!"

#same for third

two_weeks_ago_vhosting2 = conn_eu.get_all_snapshots(filters = {"description": vhosting2_root_vol_description})
try:
two_weeks_ago_vhosting22 = two_weeks_ago_vhosting2[0]
two_weeks_ago_vhosting23 = two_weeks_ago_vhosting22.id
conn_eu.delete_snapshot(two_weeks_ago_vhosting23)
except:
print "no snapshot two weeks ago to delete!"
