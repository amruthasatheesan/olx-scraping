import scrapy
from scrapy.selector import Selector
# from urllib.parse import parse


class OlxspiderSpider(scrapy.Spider):
    name = "olxspider"
    allowed_domains = ["www.olx.in"]
    start_urls = ["https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723"]

    def parse(self, response):
        # selector = Selector(response)
        # titles = selector.css('span.YBbhy').get()
        # for title in titles:
        #     print(title)
        for products in response.css('._2cbZ2'):
            
            try:  
                
                yield {
                'title': response.css('span.YBbhy::text').getall() ,
                'price': response.css('span._2Ks63::text').getall() ,
                }
            except:
                yield{
                    
                'title': response.css('span.YBbhy::text').getall() ,
                'price': 'sold out',
                }   