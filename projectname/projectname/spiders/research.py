import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Maria Shapiro
# CS 4675

# Homework 1: Option 1.2 Write a Web Crawler of your own
# Spider #3: Only add links that contain the keywords "AI", "ML", and "research". This spider's name is research


class ResearchSpider(CrawlSpider):
    name = 'research'
    start_urls = ['https://www.gatech.edu']
   
    rules = (
      #Rule(LinkExtractor(allow='a'), callback='parse', follow=True),
      #Rule(LinkExtractor(), follow=True),
      [Rule(LinkExtractor(allow=["AI", "ML", "research"], deny='http://iamweb1.iam.gatech.edu'))]
      #Rule(LinkExtractor(deny='http://iamweb1.iam.gatech.edu'))
    )

def parse(self, response):

        sel = scrapy.Selector(response)
        yield {
          'body': sel.css('h1.title::text').get()
        }