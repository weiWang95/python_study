#!/usr/bin/python
#coding=utf-8

import time

now_time = time.time()
localtime = time.localtime(now_time)
print("now_time -> %f, localtime -> %s" % (now_time, localtime))


print('time -> %s' % (time.strftime("%Y-%m-%d %H:%M:%S", localtime)))
