#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib
import urllib2
import json
from bs4 import BeautifulSoup
import requests  # 导入requests模块用于访问测试自己的ip
import random

pro = ['139.224.135.94:80', '61.135.217.7:80', '122.114.31.177:808']  # 在(http://www.xicidaili.com/wt/)上面收集的ip用于测试
# 没有使用字典的原因是 因为字典中的键是唯一的 http 和https 只能存在一个 所以不建议使用字典


#  你的请求头信息
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
url = 'https://movie.douban.com/j/search_tags?type=movie'  # 你用于测试自己ip的网站
request = requests.get(url, proxies={'http': random.choice(pro)}, headers=head)  # 让问这个网页  随机生成一个ip
# print(request.text)  # 输出返回的内容
result = request.json()
tags = result['tags']

movies = []

for tag in tags:
    # time.sleep(random.random() * 3)
    limit = 0
    while 1:   #把某一个标签下基本定义的所有数据获取成功，并加入列表之中
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag='+ tag + '&page_limit=50&page_start='+str(limit)
        print url
        request = urllib2.Request(url=url)
        response = urllib2.urlopen(request, timeout=20)
        result = json.loads(response.read())

        result = result['subjects']

        if len(result) == 0:
            break

        limit += 20

        for item in result:
            movies.append(item)
        #####
        break

    #####
    break

for x in xrange(0,len(movies)):
    item = movies[x]
    request = urllib2.Request(url=item['url'])
    response = urllib2.urlopen(request, timeout=20)
    result = response.read()
    html = BeautifulSoup(result,"lxml")#解析成结构化信息
    title = html.select('h1')[0]
    title = title.select('span')[0]
    title = title.get_text()

    movies[x]['title'] = title

    fw = open('movies.txt','w')

    for item in movies:
        tmp = ''
        for key,value in item.items():
            tmp += str(value) + ','
        fw.write(tmp[:-1] + '\n')

    fw.close()



