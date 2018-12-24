#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 8:53 AM
# @Author  : Beer
# @Site    : 
# @File    : testscrapy.py
# @Software: PyCharm
# @Discription: 图片按照url地址用urllib爬取，信息由于是由js动态加载，使用python操作chrome爬取

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import ssl
import lxml
import time

if __name__ == '__main__':
	context = ssl._create_unverified_context()
	#信息地址
	#requrl = "https://mall.jd.com/advance_search-403842-1000002370-1000002370-0-0-0-1-1-60.html?keyword=%25E6%25BC%25B1%25E5%258F%25A3%25E6%25B0%25B4"#漱口水
	#requrl = "https://mall.jd.com/view_search-403842-1000002370-1000002370-0-1-0-0-1-1-24.html?keyword=%25E7%2589%2599%25E8%2586%258F&isGlobalSearch=1"#牙膏
	#requrl = "https://mall.jd.com/advance_search-403842-1000002370-1000002370-0-0-0-1-1-60.html?keyword=%25E7%2589%2599%25E5%2588%25B7"#牙刷
	#requrl = "https://mall.jd.com/advance_search-403842-1000002370-1000002370-0-0-0-1-1-60.html?keyword=%25E7%2594%25B5%25E5%258A%25A8" #电动牙刷
	#requrl = "https://mall.jd.com/advance_search-403842-1000002370-1000002370-0-0-0-1-1-60.html?keyword=%25E5%2584%25BF%25E7%25AB%25A5%25E5%258F%25A3%25E8%2585%2594" #儿童口腔
	#requrl = "https://mall.jd.com/advance_search-403842-1000002370-1000002370-0-0-0-1-1-60.html?keyword=%25E8%25BF%259B%25E5%258F%25A3" #进口产品
	#读图片
	imgurl = "https:"
	header = headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
	#reqimg = urllib.request.Request(imgurl, headers=header)
	#resp = urllib.request.urlopen(req, context=context)
	#html = resp.read()
	#html = BeautifulSoup(html, 'html.parser')
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get(requrl)
	time.sleep(10)
	data = driver.page_source
	html = BeautifulSoup(data, "lxml")
	pictures = html.find_all("div", class_="jPic") #获取图片地址
	infos = html.find_all("div", class_="jDesc") #获取信息
	prices = html.find_all("span", class_="jdNum") #获取商品价格
	types = html.find_all("div", class_="jSearchInput") #获取商品类型
	i = 1
	j = 1
	k = 1
	m = 1
	#开爬
	for goodtype in types:
		print('——————————-——————————————————————————————' + '商品类型---' + goodtype.input.attrs['value'] + '——————————-——————————————————————————————')
	#获取文字信息
	print('——————————-————' + str(len(infos)) + '个商品-商品信息' + '——————————-————')
	for info in infos:
		print(str(k) + ':' + str(info.a.get_text()))
		k = k + 1
	#获取商品价格
	print('——————————-————' + str(len(prices)) + '个商品-价格' + '——————————-————')
	for price in prices:
		print(str(j) + ':' + str(price.get_text))
		j = j+1
	#获取图片地址
	print('——————————-————' + str(len(pictures)) + '个商品-图片地址' + '——————————-————')
	for src in pictures:
		print(str(i) + ':' + str(src.a.img.attrs['src']))
		i = i+1
	#爬图片,获取图片地址
	for src in pictures:
		imgurl = imgurl + str(src.a.img.attrs['src'])
		print(imgurl)
		#拼接图片的名字和文字信息对应
		imgname = str(m) + '.jpg'
		#打开图片的url地址
		req = urllib.request.Request(url=imgurl, headers=header)
		response = urllib.request.urlopen(req, context=context)
		data = response.read()
		# 清除并以二进制写入
		f = open('/Users/dongwenqi/Desktop/scrapy/进口产品/' + imgname, 'w+b')
		f.write(data)
		f.close()
		imgurl = "https:"
		m = m + 1

	driver.close()
	driver.quit





