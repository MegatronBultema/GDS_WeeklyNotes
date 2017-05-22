'''
This script takes 1 additional arguments and runs like so:
    python list_files.py bucket_name
'''

from sys import argv

import boto3

def list_files(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    for key in bucket.objects.all():
        print(key.key)


if __name__ == '__main__':
    _, bucket = argv
    list_files(bucket)
