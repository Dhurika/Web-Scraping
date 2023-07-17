import scrapy
from scrapy.spiders import CrawlSpider


def generate_start_urls():
    years = ['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    return ["https://edition.cnn.com/sitemaps/article-{}-{}.xml".format(year,month) for year in years for month in months]


class TenyearsarticlesSpider(scrapy.Spider):
    name = "tenyearsarticles"
    allowed_domains = ["cnn.com"]
    start_urls = generate_start_urls()
    #for executing this hide the pipelines setting other it throw an error since we getting only the url
    def parse(self, response):
        return {
            "url":response.url,
            "count":response.text.count('<url>')
        }
