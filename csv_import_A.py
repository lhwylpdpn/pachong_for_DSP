#!/usr/bin/python
# -*- coding: UTF-8 -*- 
#encoding=utf-8


import os
import sys
import time
import csv
import sys
import datetime
import codecs
import os
import shutil
import re

from Config import Config
import time
import pymysql
import csv
import string
reload(sys)

sys.setdefaultencoding('utf-8')
global conn
conn = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])

def delete_csv(tablename,date):
	global conn
	if date!="":
		sql="delete from "+str(tablename)+" where csv_update_time='"+str(date)+"'"
	else:
		sql="delete from "+str(tablename)	
 
	cursor=conn.cursor()
	cursor.execute(sql)
	conn.commit()


def import_csv(file_pwd,filename,table):
	global conn
	test = []
	pwd=file_pwd
	file=filename
	newlist=[]
	statinfo=[]
	tablename=table
	sql=""
	time_tag=str(datetime.datetime.now().strftime('%Y-%m-%d'));

	i=0
	if  os.path.exists(pwd+file):
		print(pwd+file)
		filename=pwd+file
		filenode=codecs.open(filename,'r')

		tag=0
		j=0
		t=0
		for row in filenode:
			print(row)
			print(i)
			i=i+1
			if i>2000:
				sql='insert into '+tablename+'  values '+sql
				sql=sql.strip(',')+';'
				print(len(sql))
				print(sql)
				cursor=conn.cursor()
				cursor.execute(sql)
				conn.commit()

				sql=""
				i=0
			sql+="('"+str(row[0:-1]).replace(' " ',' ').replace(",","','")+"'),"
		print(len(sql),'3')
		#print(sql)
		if len(sql)>0:
			sql='insert into '+tablename+' values '+sql
			sql=sql.strip(',')+';'
			print(sql)
			cursor=conn.cursor()
			cursor.execute(sql)
			conn.commit()
	else:
		print(pwd+file+" not found")






def import_check(file_pwd,filename,table,num):

	test = []
	pwd=file_pwd
	file=filename
	newlist=[]
	statinfo=[]
	tablename=table
	sql=""
	time_tag=str(datetime.datetime.now().strftime('%Y-%m-%d'));

	i=0
	if  os.path.exists(pwd+file):
		print(pwd+file)
		filename=pwd+file
		filenode=codecs.open(filename,'r','utf-8')

		tag=0
		j=0
		for row in filenode:
			i=i+1
			if row.count(',')!=num:
				print(row.count(','))
				print(str(row))
				print(i)



def import_clac():#补充自然量的数据到spend表
	global conn
	sql="INSERT INTO spend SELECT NULL,DATE,game_id,platform,'ziranliang',game_channel,agent,'ziranliang',0,0.1,0,0,0,'-',0,0 FROM `ad_action_v2` WHERE ad_id IN ('10','20') GROUP BY game_id,platform,DATE,game_channel,agent"
	#conn =  pymysql.connect(host='120.26.162.150',user='root',passwd='PkBJ2016@_*#',db='zilong_report',port=3306,charset='utf8')
	cursor=conn.cursor()
	cursor.execute(sql)
	conn.commit()

# def test():
# 	word="""DROP TABLE IF EXISTS `login_detail`;

# 	CREATE TABLE `login_detail` (
#   `ad_id` varchar(45) DEFAULT NULL,
#   `game_id` varchar(45) DEFAULT NULL,
#   `platform` varchar(100) DEFAULT NULL,
#   `date` varchar(40) DEFAULT NULL,
#   `game_channel` varchar(100) DEFAULT NULL,
#   `agent` varchar(100) DEFAULT NULL,
#   `ad_Creative` varchar(100) DEFAULT NULL,"""
# 	# for x in xrange(0,730):
# 	# 	word+='  `money'+str(x)+'` varchar(30) DEFAULT NULL,'
# 	word+=" `accountid` varchar(100) DEFAULT NULL,`login_time` varchar(100) DEFAULT NULL,"
# 	word+="""`csv_update_time` varchar(45) DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
# 	create_txt(word,"test")

# def create_txt(word,name):
# 	file_object = open(os.getcwd()+'/'+name+'.txt','w')
# 	file_object.write(word)
# 	file_object.close()
# 	print("create_json_"+name)

# def import_check(pwd,file):
# 	strlen=[]
# 	if  os.path.exists(pwd+file):
# 		print(pwd+file)
# 		filename=pwd+file
# 		filenode=open(filename)
# 		reader=csv.reader(filenode)
# 		for r in reader:
# 			strlen.append(len(r))
# 		if strlen.count(strlen[0])==len(strlen):
# 			print(file+" file format  ok")
# 		else:
# 			print(file+" file format  error, min is "+str(min(strlen))+"  max is "+str(max(strlen)))
# 	else:
# 		print(pwd+file+" not found")


if __name__ == '__main__':

	import_csv("tempdata/","zhangshuang.csv",'account_info')
