"""Bathak posts Spider"""

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from posts.items import PostItem


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
        post_data = response.css('div.detailNews ::text').extract()

        post_item = PostItem()
        post_item['id'] = response.url
        post_item['category'] = response.url
        post_item['text'] = " ".join(post_data)

        return post_item
