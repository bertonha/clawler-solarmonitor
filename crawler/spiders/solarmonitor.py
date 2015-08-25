# -*- coding: utf-8 -*-

import datetime
from urlparse import urlparse, parse_qs

import scrapy

from crawler.items import SolarmonitorItem
from crawler.utils import convert_to_datetime


class SolarmonitorSpider(scrapy.Spider):
    name = "solarmonitor"
    allowed_domains = ["solarmonitor.org"]
    start_urls = (
        'http://www.solarmonitor.org/',
    )

    def __init__(self, final_date=None, **kwargs):
        super(SolarmonitorSpider, self).__init__(**kwargs)

        if final_date:
            final_date = convert_to_datetime(final_date)
        else:
            final_date = datetime.datetime.today() - datetime.timedelta(days=5 * 365)

        self.final_date = final_date

    def parse(self, response):
        for href in response.xpath('//div[@class="tabslider"]//tr/td/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_image_contents)

    def parse_image_contents(self, response):
        item = SolarmonitorItem()
        item['type'] = response.xpath('//title/text()').extract()[0]

        query_string = urlparse(response.url).query
        date = parse_qs(query_string)['date'][0]
        item['date'] = date

        img_src = response.xpath('/html/body/center/table//td/img/@src').extract()
        item['image_urls'] = [response.urljoin(i) for i in img_src]

        item['number'] = response.xpath('//td[@id="noaa_number"]/a/text()').extract()

        locations = response.xpath('//td[@id="position"]')
        item['location'] = [' '.join(location.xpath('text()').extract()) for location in locations]
        item['hale_class'] = response.xpath('//td[@id="hale"]/text()').extract()
        item['mcintosh_class'] = response.xpath('//td[@id="mcintosh"]/text()').extract()
        item['area'] = response.xpath('//td[@id="area"]/text()').extract()
        item['number_of_spots'] = response.xpath('//td[@id="nspots"]/text()').extract()

        flares = response.xpath('//td[@id="events"]')
        item['flares'] = [','.join(flare.xpath('a/text()').extract()) for flare in flares]

        yield item

        if convert_to_datetime(date) >= self.final_date:
            href = response.xpath('//a[@title="-1 day"]/@href').extract()
            url = response.urljoin(href[0])
            yield scrapy.Request(url, callback=self.parse_image_contents)
