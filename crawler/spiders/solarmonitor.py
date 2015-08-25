# -*- coding: utf-8 -*-
from urlparse import urlparse, parse_qs

import scrapy

from crawler.items import SolarmonitorItem


class SolarmonitorSpider(scrapy.Spider):
    name = "solarmonitor"
    allowed_domains = ["solarmonitor.org"]
    start_urls = (
        'http://www.solarmonitor.org/',
    )

    def parse(self, response):
        for href in response.xpath('//div[@class="tabslider"]//tr/td/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_image_contents)

    def parse_image_contents(self, response):
        item = SolarmonitorItem()
        item['type'] = response.xpath('//title/text()').extract()

        query_string = urlparse(response.url).query
        item['date'] = parse_qs(query_string)['date'][0]

        img_src = response.xpath('/html/body/center/table//td/img/@src').extract()
        item['image_urls'] = [response.urljoin(i) for i in img_src]

        item['number'] = response.xpath('//td[@id="noaa_number"]/a/text()').extract()
        item['location'] = response.xpath('//td[@id="position"]/text()').extract()
        item['hale_class'] = response.xpath('//td[@id="hale"]/text()').extract()
        item['mcintosh_class'] = response.xpath('//td[@id="mcintosh"]/text()').extract()
        item['area'] = response.xpath('//td[@id="area"]/text()').extract()
        item['number_of_spots'] = response.xpath('//td[@id="nspots"]/text()').extract()

        flares = response.xpath('//td[@id="events"]')
        item['flares'] = [','.join(flare.xpath('a/text()').extract()) for flare in flares]
        yield item
