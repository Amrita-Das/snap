import scrapy
import math
class SnapSpider(scrapy.Spider):
    name='snap'
    start_urls=['https://www.snapdeal.com/seller/S241f4']
    
    product_titles=[]
    product_price=[]
    product_img=[]
    product_link=[]
    product_discount=[]
    product_rating=[]
    total=0
    
    next_page=0
    
    api_url='https://www.snapdeal.com/seller/S241f4'

#==============================================================================
#     def parse1(self,response):
#         self.total= int(response.xpath('//div[@class="jsNumberFound hidden"]//text()').extract()[0])
#         yield scrapy.Request(url=self.start_urls,callback=self.parse)
#==============================================================================
        
    def parse(self, response):
        self.next_page+=1
        if(response.url==self.api_url.format(self.next_page)):
            self.total= int(response.xpath('//div[@class="jsNumberFound hidden"]//text()').extract()[0])
        self.api_url='https://www.snapdeal.com/omn/getOmnitureCode?eventType=showMoreRevamp&pageNumber={}'
#==============================================================================
#         self.product_titles+=  response.xpath('//p[@class="product-title"]/@title').extract()
#         self.product_titles+=response.xpath('//p[@class="product-title "]/@title').extract()
#         self.product_price+=  response.xpath('//span[@class="lfloat product-price"]/@data-price').extract()
#         self.product_img+=response.xpath('//source[@class="product-image"]/@srcset').extract()
#         self.product_link+=response.xpath('//a[@class="dp-widget-link"]/@href').extract()
#         self.product_discount+=response.xpath('//div[@class="product-discount"]/span//text()').extract()
#         
#==============================================================================
        
        
        while (self.next_page<=math.ceil(self.total/20)):
            
            self.product_titles+=  response.xpath('//p[@class="product-title"]/@title').extract()
            self.product_titles+=response.xpath('//p[@class="product-title "]/@title').extract()
            self.product_price+=  response.xpath('//span[@class="lfloat product-price"]/@data-price').extract()
            self.product_img+=response.xpath('//source[@class="product-image"]/@srcset').extract()
            self.product_link+=response.xpath('//a[@class="dp-widget-link"]/@href').extract()
            self.product_discount+=response.xpath('//div[@class="product-discount"]/span//text()').extract()
            
            yield scrapy.Request(url=self.api_url.format(self.next_page),callback=self.parse,method='POST')
        
        for page_url in self.product_link:
            yield scrapy.Request(url=page_url, callback=self.parse2)
        
        yield {
                'product_titles' : self.product_titles,
                'product_price' : self.product_price,
                'product_img' : self.product_img,
                'product_link' : self.product_link,
                'product_discount':self.product_discount,
                'product_rating':self.product_rating
                }

        
    
    def parse2(self,response):
       # product_rating=response.xpath('//span[@class="avrg-rating"]//text()').extract()
       self.product_rating+=(response.xpath('//span[@class="avrg-rating"]//text()').extract())
       
       
