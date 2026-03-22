#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..')
from base.spider import Spider
import json
import math
import re

class Spider(Spider):
	def getName(self):
		return "企鹅体育"
	def init(self,extend=""):
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		cateManual = {
			"全部": "",
			"足球": "Football",
			"篮球": "Basketball",
			"NBA": "NBA",
			"台球": "Billiards",
			"搏击": "Fight",
			"网排": "Tennis",
			"游戏": "Game",
			"其他": "Others",
			"橄棒冰": "MLB"
		}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name': k,
				'type_id': cateManual[k]
			})

		result['class'] = classes
		if (filter):
			result['filters'] = self.config['filter']
		return result
	def homeVideoContent(self):
		result = {}
		return result

	def categoryContent(self,tid,pg,filter,extend):
		result = {}
		url = 'https://live.qq.com/api/live/vlist?page_size=60&shortName={0}&page={1}'.format(tid, pg)
		rsp = self.fetch(url)
		content = rsp.text
		jo = json.loads(content)
		videos = []
		vodList = jo['data']['result']
		numvL = len(vodList)
		pgc = math.ceil(numvL/15)
		for vod in vodL