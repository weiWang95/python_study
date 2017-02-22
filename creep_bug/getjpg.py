#!/usr/bin/python
#coding=utf-8

import re
import urllib
import time

def getHtml(url):
  pageSource = urllib.urlopen(url)
  html = pageSource.read()
  return html

def getImage(html):
  # reg = r' (?:ng-)?src="(https?://.+?\.(?:jpg|png|jpeg))" '
  reg = r'(https?://[\w\./\%]+?\.(?:jpg|png|jpeg|gif){1})'
  imgre = re.compile(reg)
  imglist = re.findall(imgre, html)
  return imglist

def saveImages(images):
  timeStr = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
  x = 1
  for imgurl in images:
    urllib.urlretrieve(imgurl, '../sources/%s_%s%s' % (timeStr, x, imgurl[imgurl.rindex('.'):len(imgurl)]))
    x += 1

winseHtml = getHtml("https://www.zhihu.com/topic/19606792/top-answers")
imageList = getImage(winseHtml)
# if len(imageList) > 20:
#   print(len(imageList))
# else:
#   print(imageList)
print(imageList[0])
print(imageList[1])
print(imageList[2])
# saveImages(imageList)
