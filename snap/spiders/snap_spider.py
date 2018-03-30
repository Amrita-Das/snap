import scrapy
import math

class Items(scrapy.Item):
    title=scrapy.Field()
    finprice=scrapy.Field()
    price=scrapy.Field()
    Pimg=scrapy.Field()
    Simg=scrapy.Field()
    link=scrapy.Field()
    rating=scrapy.Field()
    
    
class SnapSpider(scrapy.Spider):
    name='snap'
    start_urls=['https://www.snapdeal.com/seller/S241f4']
    
    product_title=""
    product_finprice=0
    product_price=0
    Pproduct_img=""
    Sproduct_img=""
    product_link=""
    product_rating=0
    total=0
    
    next_page=0
    api_url='https://www.snapdeal.com/acors/json/product/get/search/0/20/20?q=&sort=plrty&brandPageUrl=&keyword=&searchState=k3=true|k4=null|k5=0|k6=0&pincode=&vc=S241f4&webpageName=sellerListing&campaignId=&brandName=&isMC=false&clickSrc=&showAds=&cartId=&page=sp'
    

        
    def parse(self, response):
        
       
        self.total= int(response.xpath('//div[@class="jsNumberFound hidden"]//text()').extract()[0])

        yield scrapy.Request(url=self.start_urls[0],callback=self.getProdInfo)
        while (self.next_page<=math.ceil(self.total/20)):
            
            
            self.next_page+=1
            self.api_url='https://www.snapdeal.com/acors/json/product/get/search/0/'+str(self.next_page*20)+'/20?q=&sort=plrty&brandPageUrl=&keyword=&searchState=k3=true|k4=null|k5=0|k6=0&pincode=&vc=S241f4&webpageName=sellerListing&campaignId=&brandName=&isMC=false&clickSrc=&showAds=&cartId=&page=sp'
            yield scrapy.Request(url=self.api_url,callback=self.getProdInfo)
    
    def getProdInfo(self,response):
        
        print(response.url)
        self.product_link=response.xpath('//a[@class="dp-widget-link noUdLine"]/@href').extract()
        print(self.product_link)
        for page_url in self.product_link:
            try:
                
                yield scrapy.Request(url=page_url, callback=self.getProduct)
            except Exception as e:
                print(e)
       

        
    
    def getProduct(self,response):
        
        item=Items()
        self.product_title=response.xpath('//h1[@class="pdp-e-i-head"]/@title').extract()[0]
        self.product_finprice=response.xpath('//span[@class="payBlkBig"]//text()').extract()[0]
        self.product_finprice=float("".join(e for e in self.product_finprice if str.isdigit(e)==True or e=='.'))
        self.product_price=response.xpath('//s[@class="strike"]/span//text()').extract()[0]
        self.product_price=float("".join(e for e in self.product_price if str.isdigit(e)==True or e=='.'))
        self.product_rating=response.xpath('//span[@class="avrg-rating"]//text()').extract()[0]
        self.product_rating=float("".join(e for e in self.product_rating if str.isdigit(e)==True or e=='.'))
        self.Pproduct_img=response.xpath('//img[@class="cloudzoom"]/@src').extract()
        self.Sproduct_img=response.xpath('//img[@class="cloudzoom"]/@bigsrc').extract()
        
        
        item['title']=self.product_title,
        item['price']=self.product_price,
        item['finprice']=self.product_finprice,
        item['Pimg']=self.Pproduct_img,
        item['Simg']=self.Sproduct_img,
        item['rating']=self.product_rating
             
        yield item
       
       
