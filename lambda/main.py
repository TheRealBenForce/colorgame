# example url
# http://173.49.90.96:8934/blink1/fadeToRGB?rgb=%230000ff&time=1.0

import urllib.request
#import urllib.parse
import json
import random

ip = '173.49.90.96'
port = '8934'
urlbase = 'http://' + ip + ':' + port + '/blink1/fadeToRGB?rgb=%23'
fadetime = '0.5'

def make_url():
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    return urlbase + color + '&time=' + fadetime

url = make_url()
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))
