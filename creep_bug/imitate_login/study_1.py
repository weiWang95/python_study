#!/usr/bin/python2
#coding=utf-8

import urllib
import urllib2
import cookielib

cookie_file_name = '/home/optilink/python/sources/cookie/pixiv_cookie.txt'
cookie = cookielib.MozillaCookieJar(cookie_file_name)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

user_info = {'email': '1260859052@qq.com', 'password': 'xxxxxx', '_xsrf': 'fc15e58cf08db1b26e451c889d457883'}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36', 
  'Referer': 'https://www.zhihu.com/',
  'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
  'X-Xsrftoken': 'fc15e58cf08db1b26e451c889d457883'
}
data = urllib.urlencode(user_info)
url = 'https://www.zhihu.com/login/email'
request = urllib2.Request(url, data, headers)
response = opener.open(request)
cookie.save(ignore_discard=True, ignore_expires=True)

# response = urllib2.urlopen(request)
print response.read()

response = opener.open('https://www.zhihu.com')
print response.read()