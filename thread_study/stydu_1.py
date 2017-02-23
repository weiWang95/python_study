#!/usr/bin/python2
#coding=utf-8

import time
# from random import random
# from threading import Thread, Semaphore

# sema = Semaphore(2)

# def randomnum(tid):
#   with sema:
#     print '%s using sema' % (tid)
#     sleeptime = random() * 2
#     time.sleep(sleeptime)
#   print '%s end sema' % (tid)

# threads = []
# for i in range(5):
#   t = Thread(target=randomnum, args=(i,))
#   threads.append(t)
#   t.start()

# for t in threads:
#   t.join()





from threading import Thread, Lock

value = 0
lock = Lock()

def getlock():
  global value
  with lock:
    new = value + 1
    time.sleep(0.001)
    value = new

threads = []

for i in range(100):
  t = Thread(target=getlock)
  t.start()
  threads.append(t)

for t in threads:
  t.join

print value