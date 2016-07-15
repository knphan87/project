
'''import tinys3
S3_ACCESS_KEY = raw_input("Access ID key: ")
S3_SECRET_KEY = raw_input("Secret Key: ")
NAME_OF_FILE = raw_input("File: ")
my_bucket = 'ap.navyunix.us'
conn = tinys3.Connection(S3_ACCESS_KEY,S3_SECRET_KEY,tls=True,endpoint='s3-us-west-1.amazonaws.com')
f = open(NAME_OF_FILE,'rb')
conn.upload('ex2.py',f,my_bucket)
'''
import boto
import boto.s3
from boto.s3.connection import OrdinaryCallingFormat
import os.path
import sys

# Fill these in - you get them when you sign up for S3
AWS_ACCESS_KEY_ID = raw_input("Access ID key: ")
AWS_ACCESS_KEY_SECRET = raw_input("Secret Key: ")
sourceDir = raw_input('Enter source directory: ')
# Fill in info on data to upload
# destination bucket name
bucket_name = raw_input('Enter bucket name: ')
# source directory
#sourceDir = 'testdata/'
# destination directory name (on s3)
destDir = ''

#max size in bytes before uploading in parts. between 1 and 5 GB recommended
MAX_SIZE = 20 * 1000 * 1000
#size of parts when uploading in parts
PART_SIZE = 6 * 1000 * 1000

#conn = boto.s3.connect_to_region(region_name='us-east-1',aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_ACCESS_KEY_SECRET,calling_format=boto.s3.connection.OrdinaryCallingFormat())
conn = boto.connect_s3(aws_access_key_id = AWS_ACCESS_KEY_ID, aws_secret_access_key = AWS_ACCESS_KEY_SECRET,calling_format=boto.s3.connection.OrdinaryCallingFormat())
bucket = conn.get_bucket(bucket_name)

uploadFileNames = []
for (sourceDir, dirname, filename) in os.walk(sourceDir):
    uploadFileNames.extend(filename)
    break

def percent_cb(complete, total):
    sys.stdout.write('*')
    sys.stdout.flush()

for filename in uploadFileNames:
    sourcepath = os.path.join(sourceDir + filename)
    destpath = os.path.join(destDir, filename)
    print 'Uploading %s to Amazon S3 bucket %s' % \
           (sourcepath, bucket_name)

    filesize = os.path.getsize(sourcepath)
    if filesize > MAX_SIZE:
        print "multipart upload"
        mp = bucket.initiate_multipart_upload(destpath)
        fp = open(sourcepath,'rb')
        fp_num = 0
        while (fp.tell() < filesize):
            fp_num += 1
            print "uploading part %i" %fp_num
            mp.upload_part_from_file(fp, fp_num, cb=percent_cb, num_cb=10, size=PART_SIZE)

        mp.complete_upload()

    else:
        print "singlepart upload"
        k = boto.s3.key.Key(bucket)
        k.key = destpath
        k.set_contents_from_filename(sourcepath,
                cb=percent_cb, num_cb=10)
