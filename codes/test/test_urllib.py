#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import urllib

import json
from bs4 import BeautifulSoup

'''
#Get
url ='http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013'

request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
result = unicode(response.read())

print result
'''

#Post
url = 'https://shuju.wdzj.com/plat-info-initialize.html'
data = urllib.urlencode({'type1':1,'type2':2,'status':0,'wdzjPlatId':59})
request = urllib2.Request(url)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
response = opener.open(request,data)
result = response.read()
for key in json.loads(result).keys():
    print key
