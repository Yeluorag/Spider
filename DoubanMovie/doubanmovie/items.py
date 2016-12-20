# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MovieItem(scrapy.Item):
    movie_id = scrapy.Field()           # 电影ID - 8位
    name = scrapy.Field()               # 电影名
    director = scrapy.Field()           # 导演
    actor = scrapy.Field()              # 主演
    writer = scrapy.Field()             # 编剧
    year = scrapy.Field()               # 年份
#   site = scrapy.Field()               # 官网
    movietype = scrapy.Field()          # 类型
    country = scrapy.Field()            # 国家地区
    language = scrapy.Field()           # 语言
    date = scrapy.Field()               # 上映日期
    time = scrapy.Field()               # 片长
    people = scrapy.Field()             # 观看评论人数
    proportion = scrapy.Field()         # 评分比例（5分4分3分2分1分）
    value = scrapy.Field()              # 影片评分
    description = scrapy.Field()        # 简介描述
    othername = scrapy.Field()          # 又名
    movie_url = scrapy.Field()          # 豆瓣url
    image_url = scrapy.Field()          # 海报url
    star5 = scrapy.Field()              # 5星评价占比
    star4 = scrapy.Field()              # 4星评价占比
    star3 = scrapy.Field()              # 3星评价占比
    star2 = scrapy.Field()              # 2星评价占比
    star1 = scrapy.Field()              # 1星评价占比

class CommentItem(scrapy.Item):
    movie_id = scrapy.Field()           # 电影ID - 8位
    user_value = scrapy.Field()         # 评分 1-5 分
    user_id = scrapy.Field()            # 评价的用户
    user_url = scrapy.Field()           # 用户地址
    user_name = scrapy.Field()          # 用户昵称
    user_img = scrapy.Field()           # 用户头像
    user_city = scrapy.Field()          # 用户城市
    comment = scrapy.Field()            # 短评
    comment_date = scrapy.Field()       # 评价日期
    
    

    

