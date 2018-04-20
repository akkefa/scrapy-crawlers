"""Bathak posts Spider"""

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PostSpider(CrawlSpider):
    """
    Fetching post data
    """
    name = "posts"
    start_urls = ['http://www.bathak.com/urdu-news']
    allowed_domains = ["www.bathak.com"]

    rules = (
        Rule(LinkExtractor(restrict_css='div.cat-list')),
        Rule(LinkExtractor(restrict_css='div.styleThree'),
             callback="parse_post")
        )

    def parse_post(self, response):
        """
        Parsing bathak Post data
        Args:
            response:

        Returns:

        """
        post = response.css('div.detailNews ::text').extract()

        yield {
            'post': " ".join(post)
            }
