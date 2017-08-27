# Python 3.6

from __future__ import print_function

import boto3
import json
import random
import urllib.request
import urllib.parse

print('Loading function')

s3 = boto3.client('s3')
ip = '173.49.90.96'
port = '8934'
urlbase = 'http://' + ip + ':' + port + '/blink1/fadeToRGB?rgb=%23'
fadetime = '0.1'

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    try:
        blink_request()
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

def blink_request():
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    url = urlbase + color + '&time=' + fadetime
    f = urllib.request.urlopen(url)
    print(f.read().decode('utf-8'))
    return
