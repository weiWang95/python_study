#coding=utf-8

import re
import urllib
import time
from random import randint
import threading

def _html(url):
  page_source = urllib.urlopen(url)
  return page_source.read()

def analysis(url, reg_str):
  html = _html(url)
  return re.findall(re.compile(reg_str), html)

def save_file(file_url):
  t = threading.currentThread()
  file_url = str(file_url)
  print('--> %s download %s ~~~~' % (t.name, file_url))
  time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
  suffix = file_url[file_url.rindex('.'):len(file_url)]
  random_num = randint(10000, 99999)
  file_name = '/home/optilink/python/sources/%s_%s%s' % (time_str, random_num, suffix)
  # urllib.urlretrieve(file_url, file_name)
  try:
    urllib.urlretrieve(file_url, file_name)
  except Exception:
    print('Error: file -> %s download failed!!!' % (file_name))
    return False
  else:
    print('%s download %s success !!!' % (t.name, file_url))
    return True
