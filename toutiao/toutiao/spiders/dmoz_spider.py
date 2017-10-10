import scrapy

class DmozSpider(scrapy.Spider):
    name = "uc"
    allowed_domains = ["e.uc.cn"]
    start_urls = [
        "http://e.uc.cn"
    ]

    def parse(self, response):

        filename = response.url.split("/")[-2]

        with open(filename, 'wb') as f:
            f.write(response.body)
