import scrapy
from scrapy.http import FormRequest


class PostformspiderSpider(scrapy.Spider):
    name = "postformspider"
    allowed_domains = ["pythonscraping.com"]

    def start_requests(self):
       names = ['jimin','tae','kookie']
       quests = ['to get a Grammy','to meet all the armies in the world','to love everyone']
       return [FormRequest('https://pythonscraping.com/linkedin/formAction2.php',formdata = {'name':name,'quest':quest,'color':'grey'},callback=self.parse) for name in names for quest in quests]
    

    def parse(self, response):
        title = response.xpath("//div[@class='wrapper']/text()").get()
        return {
            "title":title
        }
