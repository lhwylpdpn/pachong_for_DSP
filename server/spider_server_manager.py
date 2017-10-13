#!/usr/bin/python
# -*- coding: UTF-8 -*- 
#encoding=utf-8


import os
import sys
import time

import sys
import datetime

import re
import urllib2
from Config import Config
import time
import pymysql

reload(sys)
sys.setdefaultencoding('utf-8')
global conn
conn = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])

def spider_contor():
	global conn
	start_code=""
	sql="""
select a.spider_id,a.account_id,b.spider_lang,b.start_code,b.spider_name from `spider_run_contorllar` a ,spider b where status=3 and TIMESTAMPDIFF(SECOND,next_start_time,now()) >0 and a.spider_id=b.id
	"""

	cursor=conn.cursor()
	cursor.execute(sql)
	rs=cursor.fetchall()
	if len(rs)>0:
		for r in rs:
			if r[2]=='nodejs':
				start_code=r[3].replace('[spider_name]',str(r[4])).replace('[account_id]',str(r[1]))
				#start_code='http://127.0.0.1:5200/LP_click3.gif?LPID=118'
				opener = urllib2.build_opener()
				try:
					res = opener.open(start_code,timeout=5)
				except:
					start_code='http://127.0.0.1:1110/update_status?status=1&des=start_error&account_id="'+str(r[1])+'"'
					res = opener.open(start_code)


if __name__ == '__main__':
	while 1:
		spider_contor()
		time.sleep(10)
