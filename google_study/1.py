#!/usr/bin/python2.7
#coding=utf-8

import sys

def hello(name):
  print 'Hello', name

def main():
  hello(sys.argv[1])

if __name__ == '__main__':
   main()