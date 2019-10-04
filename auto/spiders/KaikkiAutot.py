# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import datetime

class AutoHakki(scrapy.Spider):
    name = "Optima"
    allowed_domains = ["nettiauto.com"]
    start_urls = [
            'https://www.nettiauto.com/kia/optima',
            'https://www.nettiauto.com/mitsubishi/outlander',
            'https://www.nettiauto.com/volkswagen/passat',
            'https://www.nettiauto.com/ford/mondeo',
            'https://www.nettiauto.com/skoda/octavia'
    ]

    def parse(self, response):
        autolist_even  = response.xpath('//div[@class="hide_list_ad_animation"]')
        for auto in autolist_even:
                ilmoid = auto.xpath('a[@class="childVifUrl tricky_link"]/@data-id').extract_first()
                merkki = auto.xpath('a[@class="childVifUrl tricky_link"]/@data-make').extract_first()
                malli = auto.xpath('a[@class="childVifUrl tricky_link"]/@data-model').extract_first()
                vuosimalli = auto.xpath('a[@class="childVifUrl tricky_link"]/@data-year').extract_first()
                liike = auto.xpath('a[@class="childVifUrl tricky_link"]/@data-postedby').extract_first()
                hinta = auto.xpath('a[@class="childVifUrl tricky_link"]/@data-price').extract_first()
                kuvaus = auto.xpath('a[@class="childVifUrl tricky_link"]/text()').extract_first()
                kilsat = auto.xpath('a[@class="childVifUrl tricky_link"]/@data-mileage').extract_first()
                kuvaus2 = auto.xpath('div[@class="width_full"]/div[@class="data_box"]/div[@class="clearfix_nett"]/div[@class="info_block"]/div[@class="eng_line_blck engine_modal_info"]/div[@class="checkLnesFlat"]/text()').extract_first()
                dtstamp = datetime.datetime.now()
                kuvaurl = auto.xpath('div[@class="width_full"]/div[@class="img_box listImgBox"]/div[@class="listing_thumb"]//img[@src]/@src').extract_first()
                ilmourl = auto.xpath('a[@class="childVifUrl tricky_link"]/@href').extract_first()
                if str(kilsat) == "":
                        kilsat = 0 
                yield	{
                        'ilmoId':ilmoid,
                        'merkki':merkki,
                        'malli':malli,
                        'vuosimalli':vuosimalli,
                        'liike':liike,
                        'hinta':hinta,
                        'kuvaus':kuvaus,
                        'kilsat':kilsat,
                        'dtstamp':dtstamp,
                        'kuvaus2':kuvaus2.strip(),
                        'kuvaurl':kuvaurl,
                        'ilmourl':ilmourl
                        }
        relative_next_url = str(response.xpath('//a[@class="pageNavigation next_link"]/@href').extract_first())

        if relative_next_url != "":
                absolute_next_url = "https://www.nettiauto.com" + relative_next_url
                yield Request(absolute_next_url, callback=self.parse)