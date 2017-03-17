#!/usr/bin/python2
#coding=utf-8

import re
import urllib
import urllib2
import time
import os

def save(data_list):
  base_url = '/home/optilink/python/sources/jokes/'
  if not os.path.exists(base_url):
    os.makedirs(base_url)

  file_name = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())) + '.txt'
  file_object = open(base_url + file_name, 'w+')
  try:
    print 'start write'
    file_object.read()
    file_object.writelines(data_list)
    print 'write success'
  finally:
    file_object.close()

def get_data_list(url, reg, headers={}):
  try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    html = re.sub(r'<br/>', '\r\n', html)
    return re.findall(re.compile(reg), html)
  except urllib2.URLError, e:
    if hasattr(e, 'code'):
      print e.code
    if hasattr(e, 'reason'):
      print e.reason
    return []

url = "http://www.qiushibaike.com/text/"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
  'Referer': 'http://www.qiushibaike.com/text/'
}
reg = r'<div class="content">\n{4}<span>(.+?)</span>\n{3}</div>'
data_list = get_data_list(url, reg, headers)
print 'Get Data Success !!! count -> ', len(data_list)

for data in data_list:
  print data

save(data_list)
print 'Save Success !!!'