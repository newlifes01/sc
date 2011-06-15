from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class GlaSpider(BaseSpider):
    """A simple spider for gla.ac.uk"""
    name = "gla.ac.uk"
    allowed_domains = ["gla.ac.uk"]
    start_urls = ["http://www.gla.ac.uk"]
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        filename = response.url.split("/")[-2]
        open('temp.txt','wb').write(response.body)
