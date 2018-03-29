# -*- coding: utf-8 -*-

import scrapy
from novel.items import NovelItem

class NovalSpider(scrapy.Spider):
    name = "novel"
    start_urls = [
        'https://ck101.com/forum.php?gid=1180',
    ]

    DEPTH = 3

    def parse(self, response):
        for novel_type in response.css("div.fl_dl"):
            next_url = novel_type.css("h2 a::attr(href)").extract_first()
            yield response.follow(next_url, callback=self.novelparse)
             
            
    def novelparse(self, response):
        page = response.url.split("page=")
        if len(page) > 1:
            page = int(page[1])
        else:
            page = 1
        
        novel_type = response.css("div.xs2 a::attr(title)").extract_first()
        for novel in response.xpath("//tbody[contains(@id,'normalthread')]"):
            item = NovelItem()
            item['novel_type'] = novel_type
            item['name'] = novel.css("div.blockTitle a::attr(title)").extract_first()
            item['image'] = novel.css("div.l_sPic a img::attr(src)").extract_first()
            item['time'] = novel.css("div.postInfo span span::text").extract_first()
            item['url'] = novel.css("div.l_sPic a::attr(href)").extract_first()
            yield item

        next_page = response.css("a.nxt::attr(href)").extract_first()
        if next_page is not None:
            if page <= NovalSpider.DEPTH:
                yield response.follow(next_page, self.novelparse)
