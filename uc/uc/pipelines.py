# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
import pymysql
import datetime
from uc.items import UC_money
import json
import codecs
class UcPipeline(object):
    def process_item(self, item, spider):
    	line = json.dumps(dict(item)) + "\n"
    	self.file.write(line)
        return item

    def __init__(self):
        self.settings=get_project_settings() #获取settings配置，设置需要的信息

        self.host=self.settings['MYSQL_HOST']
        self.port=self.settings['MYSQL_PORT']
        self.user=self.settings['MYSQL_USER']
        self.passwd=self.settings['MYSQL_PASSWD']
        self.db=self.settings['MYSQL_DBNAME']
        self.file = open('items.jl', 'wb')
    def close_spider(self,spider):
		sql=""
		self.file.close()
		filenode=codecs.open('items.jl','r','utf-8')

		conn=self.connectMysql()
		for row in filenode:
			jsons=json.loads(row)

			sql+='insert into spider_spend values("UC","'+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+'","UC","","'+str(datetime.datetime.now().strftime('%Y-%m-%d'))+'","'+str(jsons['accountid'])+'","'+str(jsons['balance'])+'","'+str(jsons['totalcost'])+'");'
		
		cur=conn.cursor()
		cur.execute(sql)#执行sql语句\
		conn.commit()
		cur.close()
		conn.close()
    def open_spider(self,spider):

    	pass
    	#print(self.UC_money.keys())



    def connectMysql(self):
        conn=pymysql.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             db=self.db,
                             charset='utf8') #要指定编码，否则中文可能乱码
        return conn

