#!/usr/bin/python
#coding=utf-8

file = open("mydata.txt","r+")
while((str = file.next()) != '')
  print("data-> %s" % str)
file.close
