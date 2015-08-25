# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from crawler.utils import clear_list


class SolarmonitorClearDataPipeline(object):
    def process_item(self, item, spider):

        item['area'] = clear_list(item['area'])
        item['number_of_spots'] = clear_list(item['number_of_spots'])
        item['hale_class'] = clear_list(item['hale_class'])
        item['mcintosh_class'] = clear_list(item['mcintosh_class'])
        item['location'] = clear_list(item['location'])
        item['flares'] = clear_list(item['flares'])

        return item
