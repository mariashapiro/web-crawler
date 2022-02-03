from collections import Counter
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Maria Shapiro
# CS 4675

# Homework 1: Option 1.2 Write a Web Crawler of your own
# First spider!

"""
References:
"""

""" 
(1) Select a seed URL to initialize your Web crawler, such as cc.gatech.edu, and
you are expected to crawl at least 1000 URLs.
(2) Show the design of your Web archive to store your crawled web pages, the
keywords (subjects) you have extracted.
(3) Plot the crawl speed in terms of the number of keywords you have extracted
and the number of URLs you have extracted and the number of URLs you are
able to crawl.
(4) Discuss your experience and lessons learned. Predict how long your crawler
may need to work in order to crawl 10 millions of pages and 1 billion of pages.

Deliverable:
(a) Source code and executable with readme.
(b) Discuss the design of your crawler: Pros and cons.
(c) ScreenShots of your Web Crawler's Command lines or GUIs
(d) Crawl Statistics (Crawl speed #pages/minute, ratio of #URL crawled / #URL
to be crawled, etc.) in excel plots or tabular format
(e) Discuss your experience and lessons learned.
"""

class SipSpider(CrawlSpider):
    name = 'sip'
    #allowed_domains = ['cc.gatech.edu']
    start_urls = ['https://cc.gatech.edu']
    #c = Counter()

    
    
    rules = (
      #Rule(LinkExtractor(allow='a'), callback='parse', follow=True),
      Rule(LinkExtractor(), follow=True),
      #[Rule(LinkExtractor(allow='gatech', deny='http://iamweb1.iam.gatech.edu'))]
      #Rule(LinkExtractor(deny='http://iamweb1.iam.gatech.edu'))

    )

    #Rule(LinkExtractor(allow="a"), callback='parse', follow=True),
    #Rule(LinkExtractor(allow='b'))
    def parse(self, response):
        count = {}
        sel = scrapy.Selector(response)
        website_text = sel.xpath('//body//text()').extract()
        '''
        for word in website_text.strip().split():
          if word in count:
            count[word] += 1
          else:
            count[word] = 1

        common_words =  sorted(count.items(), key=lambda x: x[1], reverse=True)[:50]
        '''
        
        yield {
          #'body': sel.css('h1.title::text').get()
          #'body': sel.xpath('//*[@id="body"]').extract_first()
          #'body': ''.join(sel.select("//body//text()").extract()).strip()
          
          'body': website_text,
          #'word count': common_words
        }

    