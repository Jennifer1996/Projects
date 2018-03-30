import socket
import csv
import urllib2
import requests

def IPpool():
    socket.setdefaulttimeout(2)
    reader=csv.reader(open('ips.csv'))
    IPpool=[]
    for row in reader:
        proxy=row[0]+':'+row[1]
        proxy_handler=urllib2.ProxyHandler({"http":proxy})
        opener=urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        try:
            html=urllib2.urlopen('http://www.baidu.com')
            IPpool.append([row[0],row[1]])
        except Exception,e:
            continue
    return IPpool

