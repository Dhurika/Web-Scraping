import scrapy

def generateurls():
    names = ['jimin','tae','kookie']
    quests = ['to get a Grammy','to meet all the armies in the world','to love everyone']
    return ['https://pythonscraping.com/linkedin/formAction.php?name={}&quest={}&color=Black'.format(name,quest) for name in names for quest in quests]

class GetformspiderSpider(scrapy.Spider):
    name = "getformspider"
    allowed_domains = ["pythonscraping.com"]
    start_urls = generateurls()

    def parse(self, response):
        title = response.xpath("//div[@class='wrapper']/text()").get()
        return {
            "title":title
        }
