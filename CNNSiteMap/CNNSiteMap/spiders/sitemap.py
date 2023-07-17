import scrapy
from scrapy.spiders import SitemapSpider
from CNNSiteMap.items import Article
from scrapy.linkextractors import LinkExtractors

class SitemapSpider(SitemapSpider):
    name = "sitemap"
    allowed_domains = ["cnn.com"]
    sitemap_urls = ["https://edition.cnn.com/sitemaps/article-2023-07.xml"]

    def parse(self, response):
        article = Article()
        article["url"] = response.url
        article["source"] = "CNN"
        article["title"] = response.xpath("//title/text()").get()
        article["description"]=response.xpath("//meta[@name='description']/@content").get()
        article["date"]= response.xpath("//meta[@property='article:published_time']/@content").get()
        article["author"]=response.xpath("//meta[@name='author']/@content").get()
        return article

