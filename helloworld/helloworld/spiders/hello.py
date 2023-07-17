import scrapy


class HelloSpider(scrapy.Spider):
    name = "hello"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        title = response.css('span.title::text').get()
        return {
            "title":title
        }
