# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import codecs
import json
import os
from collections import OrderedDict
from doubanmovie.items import MovieItem
from doubanmovie.items import CommentItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# class JsonWithEncodingPipeline:
# 	def __init__(self):
# 		self.file = codecs.open('test.json', 'wb', encoding='utf-8')

# 	def process_item(self, item, spider):
# 		line = json.dumps(dict(item)) + '\n'
# 		self.file.write(line.decode('unicode-escape'))
# 		return item
	
# 	def close_spider(self, spider):
# 		print "JsonWithEncodingPipline closed"
# 		self.file.close()

# 	def open_spider(self, spider):
# 		print "JsonWithEncodingPipeline opened"
def mkdir(path):
	path = path.strip()
	path = path.rstrip('\\')
	isExists = os.path.exists(path)

	if not isExists:
		os.makedirs(path)


class DoubanmoviePipeline(object):
	def __init__(self):
		self.xxx = 1

	def process_item(self, item, spider):

		write_addr = ''
		Dir = ''
		if isinstance(item, CommentItem):
			Dir = 'CommentData/' + item['movie_id'].encode('utf-8') + '/'
		elif isinstance(item, MovieItem):
			Dir = 'MovieData/'
		else:
			pass
		print Dir
		mkdir(Dir)
		id_str = ''
		if isinstance(item, CommentItem):
			id_str += item['user_id'].encode('utf-8')
		if isinstance(item, MovieItem):
			id_str += item['movie_id'].encode('utf-8')
		write_addr += Dir + id_str + '.json'
		
		file = codecs.open(write_addr, 'wb', encoding='utf-8')
		line = json.dumps(dict(item)) + '\n'
		file.write(line.decode('unicode-escape'))
		file.close()
		return item

	def open_spider(self, spider):
		print 'Movie Spider Open'

	def close_spider(self, spider):
		print 'Write Movie Done'













