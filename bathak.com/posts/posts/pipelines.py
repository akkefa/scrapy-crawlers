# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PostsPipeline(object):
    """
    Post Pipeline
    """

    def process_item(self, post, spider):
        """
        Nothing
        Args:
            post:
            spider:

        Returns:

        """
        url = post['id']
        post_name = url.split('/')[-1]
        post_id = post_name.split('-')[-1]
        category_name = url.split('/')[-2]

        post['id'] = str(post_id)
        post['category'] = str(category_name)
        post['text'] = str(post['text']).strip()

        return post
