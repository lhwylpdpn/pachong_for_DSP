# This Python file uses the following encoding: utf-8
import sys
from Config import Config
import datetime
import random
import pymysql
class run_contor:


	@staticmethod
	def update_status(status,des,id_):
		try:	
			mysql_r = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])

			if 	status=='0':
				sql="""
				update `spider_run_contorllar` set status='"""+str(status)+"""' , next_start_time=''
				, status_describe=''
				where account_id = '"""+str(id_)+"""'"""
				sql+=';INSERT INTO `run_log` SELECT spider_id,account_id,NOW(),"","" FROM `spider_run_contorllar` WHERE account_id="'+str(id_)+'"'
			if 	status=='1':
				sql="""
				update `spider_run_contorllar` set status='"""+str(status)+"""' , next_start_time=''
				, status_describe='"""+str(des)+"""'
				where account_id= '"""+str(id_)+"""'"""
				sql+=';update  `run_log` set end_time=now() ,end_status=1 where account_id="'+str(id_)+'" and end_time="" and end_status=""'
			if 	status=='2':
				sql="""
				update `spider_run_contorllar` set status='"""+str(status)+"""' , next_start_time=DATE_FORMAT(date_add(now(), interval cycle_second second),'%Y-%m-%d %H:%i:%s')
				, status_describe='' 
				where account_id= '"""+str(id_)+"""';"""
				sql+="""
				UPDATE  `spider_run_contorllar` a ,( SELECT spider_id,account_id FROM `spider_run_contorllar` WHERE STATUS=2  AND LENGTH(next_start_time)>0 GROUP BY spider_id HAVING spider_id IN (SELECT spider_id FROM spider_run_contorllar WHERE account_id='"""+str(id_)+"""')) b 
SET a.status=3 WHERE a.spider_id=b.spider_id AND a.account_id=b.account_id


				"""
				sql+=';update  `run_log` set end_time=now() ,end_status=2 where account_id="'+str(id_)+'" and end_time="" and end_status=""'

			cursor=mysql_r.cursor()
			cursor.execute(sql)
			mysql_r.commit()
			mysql_r.close()
			r="""
			{"status":"200"}
			"""
			return r
		except:
			return {"status":"500"}


	@staticmethod
	def userinfo(id_):
		result=""
		try:	
			mysql_r = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])


			sql="""
				select username,password,media_user_id from `account_info` where accountid='"""+str(id_)+"""'
				"""

			cursor=mysql_r.cursor()
			cursor.execute(sql)
			rs=cursor.fetchall()
			if len(rs)>0:
				for r in rs:
					result='{"status":"200","body":[{"user":"'+str(r[0])+'","pass":"'+str(r[1])+'","media_id":"'+str(r[2])+'"}]}'
			else:
				result='{"status":"500"}'
			mysql_r.close()

			return result
		except:
			return '{"status":"500"}'



	@staticmethod
	def import_spend(id_,balance,today_spend):
		#try:	
			mysql_r = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])

			sql='insert into `data_spend` values("'+str(id_)+'","'+str(balance)+'","'+str(today_spend)+'",now());'
			sql+='insert into `spider_log`  select spider_id,account_id,now() from  `spider_run_contorllar` where account_id="'+str(id_)+'";'
			 
			

			cursor=mysql_r.cursor()
			cursor.execute(sql)
			mysql_r.commit()
			mysql_r.close()
			r="""
			{"status":"200"}
			"""
			return r
		#except:
			#return {"status":"500"}