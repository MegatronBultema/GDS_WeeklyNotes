'''
This script takes 1 additional arguments and runs like so:
    python new_bucket.py new_bucket_name
'''

from sys import argv

import boto3

def make_bucket(bucket_name):
    s3 = boto3.resource('s3')
    s3.create_bucket(Bucket=bucket_name)


if __name__ == '__main__':
    _, new_bucket_name = argv
    make_bucket(new_bucket_name)
