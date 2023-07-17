import scrapy


class CookiesPySpider(scrapy.Spider):
    name = "cookies.py"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/cookies/welcome.php"]
    
    def make_request_from_url(self,url):
        request = super(PythonscrapingSpider,self).make_request_from_url(url)
        request.cookies['username'] = 'Dhurika'
        request.cookies['loggedin'] = 0
        return request

    def parse(self, response):
        return {
            "text" : response.xpath("//body/text()").get()
        }
