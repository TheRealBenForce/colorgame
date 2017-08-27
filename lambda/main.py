# example url
# http://173.49.90.96:8934/blink1/fadeToRGB?rgb=%230000ff&time=1.0

from __future__ import print_function
import urllib.request
#import urllib.parse
import json
import random
import boto3

print('loading function')

s3 = boto3.client('s3')

ip = '173.49.90.96'
port = '8934'
urlbase = 'http://' + ip + ':' + port + '/blink1/fadeToRGB?rgb=%23'
fadetime = '0.5'

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))



def make_url(event, context):
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    return urlbase + color + '&time=' + fadetime

url = make_url()
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))
