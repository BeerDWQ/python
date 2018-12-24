#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 4:44 PM
# @Author  : Beer
# @Site    : 
# @File    : imgtest.py
# @Software: PyCharm
# @Discrption: urllib读取url中的图片，使用数据流读取

import urllib.request
import ssl

if __name__ == '__main__':
	#https ssl认证
	context = ssl._create_unverified_context()
	#User-Agent认证
	header = headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
	#图片地址
	imgurl = "https://img12.360buyimg.com/n7/jfs/t26437/312/296063802/380586/dfc5f616/5b8d1336Nb9c397e8.jpg"
	req = urllib.request.Request(url=imgurl, headers=header)
	response = urllib.request.urlopen(req, context=context)
	data = response.read()
	# 清除并以二进制写入
	f = open('/Users/dongwenqi/Desktop/scrapy/' + '1.jpg', 'w+b')
	f.write(data)
	f.close()
