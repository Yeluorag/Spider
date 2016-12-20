#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Crwal Douban Movies and Comments.

Anthor: Yelurag
Version: 1.0
Date: 20xx-xx-xx
Language: Python
Editor: Sublime
"""

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from doubanmovie.items import MovieItem
from doubanmovie.items import CommentItem
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def GetMovieOrUserID(_url):
	ret = ""
	strr = str(_url)
	print "URL TO GET ID: "
	print strr
	index = strr.find('subject/')		# movie: st = 0; user: st = 1
	if index is -1:
		index = strr.find('people/')
		index += 6
	else:
		index += 7

	if index is -1:
		print 'Not find movie or user id...'
		return '-1'

	while index < len(strr):
		index += 1
		if strr[index] is '/':
			break
		ret += strr[index]
	print "ID: " + ret
	return ret

class DoubanSpider(CrawlSpider):

	name = "doubanmovie"
	allowed_domains = ["movie.douban.com"]
	# start_urls = ["http://movie.douban.com/tag/2016?start=0&type=T"]
	# start_urls = ["http://movie.douban.com"]
	start_urls = ["http://movie.douban.com/tag/1994",
				  "http://movie.douban.com/tag/1995",
				  "http://movie.douban.com/tag/1996",
				  "http://movie.douban.com/tag/1997"]

	rules = [
		# All grep rules here
		# Parse Movie Information
		Rule(SgmlLinkExtractor(allow = (r'tag/\d{4}\?start=\d+', ))),
		Rule(SgmlLinkExtractor(allow = (r'https://movie\.douban\.com/subject/\d+/collections\?start=[2468]0$', )), callback = 'parse_comment', follow = True),

		Rule(SgmlLinkExtractor(allow = (r'https://movie\.douban\.com/subject/\d+/$', )), callback = 'parse_page', follow = True),
		# Parse Movie Comments
		Rule(SgmlLinkExtractor(allow = (r'https://movie\.douban\.com/subject/\b\d+\b/collections$', )), callback = 'parse_comment', follow = True)
		]

	def parse_page(self, response):
		sel = Selector(response)
		item = MovieItem()
		# print 'Crawl ' + response.url + ' start...'
		

		item['name'] = sel.xpath('//h1/span[@property="v:itemreviewed"]/text()').extract()
		item['year'] = sel.xpath('//h1/span[@class="year"]/text()').extract()
		item['director'] = sel.xpath('//a[@rel="v:directedBy"]/text()').extract()
		item['date'] = sel.xpath('//span[@property="v:initialReleaseDate"]/text()').extract()
		item['time'] = sel.xpath('//span[@property="v:runtime"]/text()').extract()
		item['description'] = sel.xpath('//span[@property="v:summary"]/text()').extract()
		item['value'] = sel.xpath('//strong[@property="v:average"]/text()').extract()
		item['people'] = sel.xpath('//span[@property="v:votes"]/text()').extract()
		item['image_url'] = sel.xpath('//a[contains(@href, "photos")]/img/@src').extract()
		item['star5'] = sel.xpath('//span[@class="stars5 starstop"]/following-sibling::*[2]/text()').extract()
		item['star4'] = sel.xpath('//span[@class="stars4 starstop"]/following-sibling::*[2]/text()').extract()
		item['star3'] = sel.xpath('//span[@class="stars3 starstop"]/following-sibling::*[2]/text()').extract()
		item['star2'] = sel.xpath('//span[@class="stars2 starstop"]/following-sibling::*[2]/text()').extract()
		item['star1'] = sel.xpath('//span[@class="stars1 starstop"]/following-sibling::*[2]/text()').extract()
		item['movietype'] = sel.xpath('//span[@property="v:genre"]/text()').extract()
		item['actor'] = sel.xpath('//span/span[@class="attrs"]/a[@rel="v:starring"]/text()').extract()
		item['writer'] = sel.xpath(u'//span/span[./text()="编剧"]/following-sibling::*/a/text()').extract()
		item['country'] = sel.xpath(u'//span[./text()="制片国家/地区:"]/following::text()[1]').extract()
		item['language'] = sel.xpath(u'//span[./text()="语言:"]/following::text()[1]').extract()
		item['othername'] = sel.xpath(u'//span[./text()="又名:"]/following::text()[1]').extract()
		item['movie_id'] = GetMovieOrUserID(response.url)
		item['movie_url'] = response.url
#		item['site'] = sel.xpath('//div[@id="info"]/span[contains(@href, "http")]/text()').extract()


		print 'Crawl ' + response.url + ' done...'
		# print item
		return item

	def parse_comment(self, response):
		items = []
		sel = Selector(response)
		print 'Crawl ' + response.url + ' start...'

		comments = sel.xpath('//table[@width="100%"]')
		for comment in comments:
			# print comment
			item = CommentItem()
			
			item['user_img'] = comment.xpath('.//img/@src').extract()
			item['user_name'] = comment.xpath('.//img/@alt').extract()
			item['user_city'] = comment.xpath('.//span[@style="font-size:12px;"]/text()').extract()
			item['user_value'] = comment.xpath('.//p[@class="pl"]/span/@class').extract()
			item['comment'] = comment.xpath('.//p[@class="pl"]/following::*[1]/text()').extract()
			item['comment_date'] = comment.xpath('.//p[@class="pl"]/text()').extract()
			url = comment.xpath('.//td[@width="80"]/a[contains(@href, "people")]/@href').extract()
			print '======================'
			print 'Get This URL ID'
			print url
			print '======================'
			item['user_url'] = url
			item['user_id'] = GetMovieOrUserID(url)
			item['movie_id'] = GetMovieOrUserID(response.url)
			items.append(item)
			print item

		return items

	def parse_try(self, response):
		pass





