"""Bathak posts Spider"""

import scrapy
import json
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


class PostUrlSpider(scrapy.Spider):
    """
    Fetching Bathak Post by json urls list
    """

    name = "json_urls"
    allowed_domains = ["www.bathak.com"]

    def start_requests(self):
        """

        Returns:

        """
        urls = json.load(open('urls.json'))
        for item in urls:
            url = 'http://www.bathak.com{}'.format(item['url'])

            post_name = url.split('/')[-1]
            post_id = int(post_name.split('-')[-1])

            if 163458 < post_id:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
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


class CategorySpider(scrapy.Spider):
    """
    Fetching post data
    """
    name = "fetch_posts_url"
    allowed_domains = ["www.bathak.com"]
    custom_settings = {'ITEM_PIPELINES': {}}

    def start_requests(self):
        """

        Returns:

        """
        url = "http://www.bathak.com/ajax/categoryListing"
        categories_id = ['379', '384', '386', '380', '385', '382', '383',
                         '381']

        for cat_id in categories_id:
            for offset in range(1, 10):
                params = {'offset': str(offset), 'id': str(cat_id)}

                yield scrapy.FormRequest(url,
                                         callback=self.parse,
                                         method='POST', formdata=params)

    def parse(self, response):
        """
        Parsing bathak Post data
        Args:
            response:

        Returns:

        """
        post_urls = response.css('div.styleThree a::attr(href)').extract()

        for url in post_urls:
            yield {"url": url}

# scrapy runspider article.py -o articles.csv -t csv
# scrapy runspider article.py -o articles.json -t json
# scrapy runspider article.py -o articles.xml -t xml
