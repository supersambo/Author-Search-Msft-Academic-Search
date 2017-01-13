#!/usr/bin/env python
# -*- coding: utf-8 -*-


########### Python 2.7 #############
import httplib, urllib, base64, json
import time
import re
import codecs
import sys
import unicodedata
import os
import os.path

reload(sys)  
sys.setdefaultencoding('utf8')

#check if access key is available
if os.path.isfile("access_key"):
    key = re.sub("\n$", "", open('access_key').readlines()[1])
else:
    print "\nThere is no access_key."
    print "Please edit access_key.edit and fill in your key. Then rename it to access_key and run this again.\n"
    exit()

#check if input file is supplied as command line argument
if len(sys.argv)<2:
    print "\nYou must specify the an input file with names of authors as command line argument!\n"
    exit()

#read inputfile
filename = sys.argv[1] #expects path to inputfile as argument
inputfile = codecs.open(filename, 'r','utf-8')
names = inputfile.readlines()

#create output directory if it doesn't alread exist
if not os.path.exists('output'):
        os.makedirs('output')

for name in names:
    name = re.sub('\n$', '', name.decode('utf-8')) #strip line breaks
    qname = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore') #replace special characters
    qname = qname.lower() #transform to lower case
    print 'Searching for ' + name + ' as >' + qname +'<'
    request = "Composite(AA.AuN=="+"'"+qname+"')"

    headers = {# Request headers
        'Ocp-Apim-Subscription-Key': key,
    }
    params = urllib.urlencode({
        # Request parameters
        'expr': request,
        'model': 'latest',
        'count': '1000',
        'offset': '0',
        'attributes': 'Id,AA.AuN,AA.AuId,Y,Ti,CC,ECC,AA.AfN,F.FN,E',
    })
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("GET", "/academic/v1.0/evaluate?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read().decode('utf8')
        outputfile = str(re.sub('\s','_', qname))
        outputfile = str('output/' + outputfile + '.json')
        with codecs.open(outputfile, 'w' ,'utf8') as f:
            f.write(data + '\n' )
            f.close()
        conn.close()
    except Exception as e:
        print e
    time.sleep(1)

###################################
