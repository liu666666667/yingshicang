#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json
import time
import base64
import re

class Spider(Spider):  # 元类 默认的元类 type
	def getName(self):
		return "央视片库"
	def init(self,extend=""):
		print("============{0}============".format(extend))
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		cateManual = {
			
			"动画片": "动画片",
			
			#"特别节目": "特别节目"
		}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name':k,
				'type_id':cateManual[k]
			})
		result['class'] = classes
		if(filter):
			result['filters'] = self.config['filter']
		return result
	def homeVideoContent(self):
		result = {
			'list':[]
		}
		return result
	def categoryContent(self,tid,pg,filter,extend):		
		result = {}
		month = ""
		year = ""
		if 'month' in extend.keys():
			month = extend['month']
		if 'year' in extend.keys():
			year = extend['year']
		if year == '':
			month = ''
		prefix = year + month

		url="https://api.cntv.cn/list/getVideoAlbumList?channelid=CHAL1460955899450127&area=&sc=&fc=%E5%8A%A8%E7%94%BB%E7%89%87&lette