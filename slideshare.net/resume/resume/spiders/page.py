"""Resume spider"""

import scrapy
from resume.items import ResumeItem


class SlideShareSpider(scrapy.Spider):
    """
    Fetching data
    """

    name = "slideshare"
    allowed_domains = ["www.slideshare.net"]

    def start_requests(self):
        """

        Returns:

        """

        file_name = "slideshares_urls.txt"
        lines = list(open(file_name, 'r'))

        for line in lines:
            url = line.strip()
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        Parsing Post data
        Args:
            response:

        Returns:

        """

        user_name = response.css('a.j-author-name > span '
                                 '::text').extract_first()
        text = response.css("ol.j-transcripts ::text").extract()

        resume_item = ResumeItem()
        resume_item['url'] = response.url
        resume_item['user_name'] = user_name
        resume_item['text'] = text

        return resume_item
