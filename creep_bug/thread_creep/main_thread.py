#coding=utf-8

import time
import sys
from threading import Thread, Semaphore

import html_analysis

MAX_FILE_SIZE = 100
page = int(sys.argv[1])
success_size = 0
failed_size = 0
sema = Semaphore(1)


def download_task(file_url):
  global success_size
  global failed_size
  # html_analysis.save_file(file_url):
  if html_analysis.save_file(file_url):
    success_size += 1
  else:
    failed_size += 1

def task(lists):
  while len(lists) > 0:
    with sema:
      file_url = lists.pop()
    download_task(file_url)

reg_str = r'(https?://[\w\./\%]+?\.(?:jpg|png|jpeg|gif){1})'
web_url = 'https://www.zhihu.com/topic/19606792/top-answers'
# web_url = 'https://www.zhihu.com/question/36851579'
file_list = html_analysis.analysis(web_url, reg_str)

# 去除重复的图片
delete_arr = []
for i in range(len(file_list)):
  if i == 0: continue
  md5 = file_list[i][file_list[i].rindex('/'):file_list[i].rindex('_')]
  if md5 == file_list[i - 1][file_list[i - 1].rindex('/'):file_list[i - 1].rindex('_')]:
    delete_arr.append(file_list[i])

for arg in delete_arr:
  file_list.remove(arg)
img_total = len(file_list)
if img_total > MAX_FILE_SIZE:
  limit = img_total if (page+1)*MAX_FILE_SIZE >= img_total else (page+1)*MAX_FILE_SIZE
  file_list = file_list[page*MAX_FILE_SIZE:limit]

print(file_list)

threads = []

begin = time.time()

for i in range(10):
  t = Thread(target = task, args = (file_list, ))
  t.start()
  threads.append(t)

for t in threads:
  t.join()

use_time = round(time.time()-begin, 2)
print('success -> %s, failed -> %s, use time -> %s (s)' % (success_size, failed_size, str(use_time)))