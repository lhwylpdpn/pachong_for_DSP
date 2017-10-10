import scrapy
import sys
from uc.items import UC_money
import re
from twisted.internet import reactor, defer
from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings

class ucSpider(scrapy.Spider):
    name = "uc"
    allowed_domains = ["e.uc.cn"]
    start_urls = [
        "https://e.uc.cn/ad/web/init/operator?userId=0&_t=1504005049501"
    ]
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'e.uc.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3053.3 Safari/537.36',
    'Upgrade-Insecure-Requests':1
    }
    cookies2={
    'JSESSIONID':'EDEFCF7422F33714D29ABC516DD7C102',
    'SSO_IDT':'"Bearer eyJhbGciOiJBMTI4S1ciLCJjdHkiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.zTDdWb6_IWgoZ-NpPRnzEivhF_FjpUYkhz16pYdMQsrUZQTuN5Y32g.5YHHNnd39WbmA7fvmw2hcg.nSiE6JxEvC3peLYcZhbifWnzM8-yxP7lAiKT4-EdU37EdZaXlR6KlvC35JhMvd8tqFWmeFLzvFNqRDYjbzlZYLFeMfb8owuQqWDFgvUeAOStLdTXdfic81TGEiXnOJ22UL_DijKsyzOII4VFECit2FTOC3YcflefRdrpjQSuKHqPRERqe88-hdX3rLiVpiux78yUs3TIYKUreev_2YfdlqwVpkhXzrVY6hfIqM9Tm-4HAbZkc3oQ1wiVfJEb48599xIgSuLhBjjR8YXOBlifYdVYinFQedN5BJxDRYydlfW-ArOxTRcT4cm2GAge9WZYe9ZTCrNdKSmBajNEzq9WMp5QbjjFvKMNkWGOLbLQlyA4G4LzDPgZsZepUqdEy9lkO2W73MZ_LW6kMogC31kSLg.rTw04eUxkASdvc8czsW0BQ"',
    '_pk_id.27cfe14ef220.a6b8':'064b7c83-1bf2-4b25-a60b-a961abbff7a4.1503988295.13.1504164252.1504148474.',
    '_pk_ses.27cfe14ef220.a6b8':'*'

    }

    cookies ={   
    'JSESSIONID':'E4D0B7AF6525A0C21BE4915F5B2B055F',
    'SSO_IDT':'"Bearer eyJhbGciOiJBMTI4S1ciLCJjdHkiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.TqLKB4uRFOBZnICQOtQzYgGsqIMISlPvXc1054IOBIxWObzJQGtLmw.d_c86df7G6huA_nXDJwAUg.R1hZjNxEIVTrZAXkjb9hV3VEUkVKgqLdQpR33EDbIrwDgegqfshdy1KhBeoCt2-gnuL0DqNbpkyUjFhH_Z4ZV6fLEQtr6CenLXrvUViaOtPJR1k7mqbmaX26jqdhOWn6w3F-wrxwZ2rOVbQ03duzVCUYQZVJNMiDKLsFa6VjKIrfhGIUmBkUzcJRkF6hHl68x13wJseDymfw_VVEuYAcqJdwYU5TKmwdW0YqU_l_Ph0Llsbcna9xeD70_ZwHWtPKocNz53So8i5l17Z6YhqGpg0X6jCQRXCz5suK11fsiBtcLONTiVMgt1krq7oxcgjDjlpcwB8MUwsMMTEcNc-AL_Q6BmakS0DFjLagdXH0qKu6fD9LjvvrYAga1Ytn-2sJ-0AOxH2u30b_QNn1wNvoKpmtBb7qOc9agzzM0jBHBk0._Khd9SCvQXsNHzE7FLrWbw"',
    '_pk_id.27cfe14ef220.a6b8':'064b7c83-1bf2-4b25-a60b-a961abbff7a4.1503988295.5.1504005050.1503999702.',
    '_pk_ses.27cfe14ef220.a6b8':'*'
    }
    def parse(self, response):
        money = UC_money()
        balance="""["']balance["']:["'][0-9+/.]+["']"""
        totalCost="""["']totalCost["']:["'][0-9+/.]+["']"""
        accountid="""["']id["']:[0-9+/.]+"""
        num_re='[0-9+/.]+'
        print(response.body)
        try:
            money['balance']=re.findall(num_re,re.findall(balance,response.body)[0])[0]
        except:
            money['balance']=""
        try:
            money['totalcost']=re.findall(num_re,re.findall(totalCost,response.body)[0])[0]
        except:
            money['totalcost']=""
        try:
            money['accountid']=re.findall(num_re,re.findall(accountid,response.body)[0])[0]
        except:
            money['accountid']=""
        return money
    def start_requests(self):

        yield scrapy.Request(url=self.start_urls[0],headers=self.headers,callback=self.parse,cookies=self.cookies2)



def save_html(data):
	file=open("C:\Users\Zlongame0156\Documents\GitHub\pachong_for_DSP\uc\uc\spiders\s.html", "wb")
	file.write(data)
	file.flush()
	file.close()


