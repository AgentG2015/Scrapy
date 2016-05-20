# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Person(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    thumb = scrapy.Field()
    rating = scrapy.Field()
    roles = scrapy.Field()
    birthday = scrapy.Field()
    birthplace = scrapy.Field()
    real_name = scrapy.Field()
    review = scrapy.Field()
    skinfo = scrapy.Field()
    quote = scrapy.Field()
    
class Movie(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    thumb = scrapy.Field()
    rating = scrapy.Field()
    genre = scrapy.Field()
    aka = scrapy.Field()
    director = scrapy.Field()
    rated = scrapy.Field()
    year = scrapy.Field()
    dvd_year = scrapy.Field()
    country = scrapy.Field()
    review = scrapy.Field()
    skinfo = scrapy.Field()
    quote = scrapy.Field()
    
class PersonMovieRelation(scrapy.Item):
    id = scrapy.Field()
    pid = scrapy.Field()
    mid = scrapy.Field()
    castAs = scrapy.Field()
    nudity = scrapy.Field()
    parts = scrapy.Field()
    
class Video(scrapy.Item):
    id = scrapy.Field()
    pid = scrapy.Field()
    mid = scrapy.Field()
    url = scrapy.Field()
    
class Image(scrapy.Item):
    id = scrapy.Field()
    pid = scrapy.Field()
    mid = scrapy.Field()
    url = scrapy.Field()