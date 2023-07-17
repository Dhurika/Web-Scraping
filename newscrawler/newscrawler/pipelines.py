# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.exceptions import DropItem
class MissingValue:
    def process_item(self,article, spider):
        if not article["url"] or not article["source"] or not article["title"] or not article["description"] or not article["date"] or not article["author"]:
            raise DropItem("Missing something!")
        return article