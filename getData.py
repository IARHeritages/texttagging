import scrapy
import settings
from readability import Document

class QuotesSpider(scrapy.Spider):
    name = settings.NAME
    start_urls = settings.START_URLS

    def parse(self, response):
        for href in response.css('div.body>h2>a::attr("href")').extract():
            if (settings.DOMAIN) in href:
                yield scrapy.Request(response.urljoin(href),
                                     callback=self.parse_article)

        next_page = response.css('li.pager-next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_article(self, response):
        main_text = ''
        title = ''
        time = ''
        author = ''

        doc = Document(response.body)

        for t in response.css('header>h1'):
            title = t.css('h1::text').extract_first()
        for p in response.css('div.text-wrapper>p'):
            tmp =  p.css('p').extract_first()
            if tmp:
                main_text += '\n ' + tmp
        for a in response.css('li.author>span>a'):
            author = a.css('a::text').extract_first()
        for t in response.css('time'):
            time = t.css('time::attr("datetime")').extract_first()
        yield {'text': main_text, 'title': title,
               'author': author, 'datetime': time, 'url': response.url,
               'source': settings.SOURCE}
