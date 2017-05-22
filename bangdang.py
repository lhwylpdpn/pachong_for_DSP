# coding=utf-8
import urllib2
import urllib
import sys
import time
import datetime
import cookielib
import random
import re
import os
import json

# coding=gbk
# url = 'http://toefl.etest.net.cn/cn/TOEFLAPP'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {'username':'4018060','password':'Zing@821004'}
# headers = { 'Cookie' : 'Cookie:BIGipServertoefl_internal_pub=2684397760.20480.0000; WebBrokerSessionID=ketMSePUSTC5r8Ot' }
# data = urllib.parse.urlencode(values).encode(encoding='UTF8')
# req = urllib.request.Request(url, data, headers)
# response = urllib.request.urlopen(req)
# the_page=response.read()
# print(the_page.decode("GBK"))

def spider_toutiao():

	cookie = cookielib.CookieJar()
	handler = urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(handler)
	url="https://ad.toutiao.com/login/"
	token=""
	data=""
	res = opener.open(url)
	for item in cookie:
		if item.name=="csrftoken":
			token=item.value
	print(token)#  确认token 获取成功
	data=urllib.urlencode({"csrfmiddlewaretoken":token,"email":"x","password":"x"})
	headers=[]
	#url="https://ad.toutiao.com/overture/data/advertiser/ad/"
	#url="https://ad.toutiao.com/overture/reporter/creative_stat/?page=1&st=2017-01-10&et=2017-02-23&day=1&inventory_type=0&image_mode=0&sort_stat=stat_cost&sort_order=1&compare=0&pricing=%%5B1%%2C2%%2C4%%2C7%%2C8%%2C9%%2C10%%5D&_=1494313000682"
	# headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3053.3 Safari/537.36',\
	# 'Cookie':'login_flag=673b34113cbd60dfb16ef9459614fc89; sessionid=045478ea44327f38154b5befa2cc9b19; sid_tt=045478ea44327f38154b5befa2cc9b19; sid_guard="045478ea44327f38154b5befa2cc9b19|1494241731|2592000|Wed\\054 07-Jun-2017 11:08:51 GMT"; Hm_lvt_85c76e21c62dcb584da211941caf4e0a=1494241739; csrftoken='+str(token)+'; part=stable; _ga=GA1.2.1764577891.1494240835; _gid=GA1.2.374623132.1494927607; _gat=1',\
	#   'Accept':'*/*',\
	#   'Accept-Encoding':'gzip, deflate',\
	#   'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6' ,\
	#   'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarySpLUemDW8rDnMyRf',\
	#   'Connection': 'keep-alive',\
	#   'Host': 'ad.toutiao.com',\
	#   'Referer':'https://ad.toutiao.com/login/',\
	#   'Upgrade-Insecure-Requests': '1'
	#    }


	# headers = [('User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3053.3 Safari/537.36')\

	#   ('Cookie','login_flag=673b34113cbd60dfb16ef9459614fc89; sessionid=045478ea44327f38154b5befa2cc9b19; sid_tt=045478ea44327f38154b5befa2cc9b19; sid_guard="045478ea44327f38154b5befa2cc9b19|1494241731|2592000|Wed\\054 07-Jun-2017 11:08:51 GMT"; Hm_lvt_85c76e21c62dcb584da211941caf4e0a=1494241739; csrftoken='+str(token)+'; part=stable; _ga=GA1.2.1764577891.1494240835; _gid=GA1.2.374623132.1494927607; _gat=1')\
	#   ('Accept','*/*')\
	#   ('Accept-Encoding','gzip, deflate')\
	#   ('Accept-Language','zh-CN,zh;q=0.8,en;q=0.6' )\
	#   ('Content-Type', 'multipart/form-data; boundary=----WebKitFormBoundarySpLUemDW8rDnMyRf')\
	#   ('Connection', 'keep-alive')\
	#   ('Host', 'ad.toutiao.com')\
	#   ('Referer','https://ad.toutiao.com/login/')\
	#   ('Upgrade-Insecure-Requests', '1')]

	headers.append(('Cookie','login_flag=673b34113cbd60dfb16ef9459614fc89; sessionid=045478ea44327f38154b5befa2cc9b19; sid_tt=045478ea44327f38154b5befa2cc9b19; sid_guard="045478ea44327f38154b5befa2cc9b19|1494241731|2592000|Wed\\054 07-Jun-2017 11:08:51 GMT"; Hm_lvt_85c76e21c62dcb584da211941caf4e0a=1494241739; csrftoken='+str(token)+'; part=stable; _ga=GA1.2.1764577891.1494240835; _gid=GA1.2.374623132.1494927607; _gat=1'))
	headers.append(('Accept','*/*'))
	headers.append(('User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3053.3 Safari/537.36'))
	headers.append(('Accept-Language','zh-CN,zh;q=0.8,en;q=0.6' ))
	headers.append(('Content-Type', 'multipart/form-data; boundary=----WebKitFormBoundarySpLUemDW8rDnMyRf'))
	headers.append(('Connection', 'keep-alive'))
	headers.append(('Host', 'ad.toutiao.com'))
	headers.append(('Referer','https://ad.toutiao.com/login/'))


	handler = urllib2.HTTPCookieProcessor(cookie) 
	opener = urllib2.build_opener(handler)
	opener.addheaders=headers
	res=opener.open(url,data)
	print(res.info())
	save_html(res.read())

	url="https://ad.toutiao.com/overture/reporter/creative_stat/?page=1&st=2017-01-10&et=2017-02-23&day=1&inventory_type=0&image_mode=0&sort_stat=stat_cost&sort_order=1&compare=0&pricing=%%5B1%%2C2%%2C4%%2C7%%2C8%%2C9%%2C10%%5D&_=1494313000682"
	url="https://ad.toutiao.com/overture/data/advertiser/ad/"
	opener.addheaders=headers
	res=opener.open(url)

	return res.read()




def spider_guangdiantong():


	url="http://e.qq.com/ec/api.php?mod=report&act=adlist&g_tk=995262453&d_p=0.7564790954599885&callback=frameElement.callback&script&g_tk=995262453"
	headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3053.3 Safari/537.36',\
	  'Cookie':'atlasdominfo=,loguid=3259173373,aduid=1353608,nickname=%%E5%%A4%%A9%%E6%%B4%%A5%%E7%%B4%%AB%%E9%%BE%%99%%E5%%A5%%87%%E7%%82%%B9%%E4%%BA%%92%%E5%%8A%%A8%%E5%%A8%%B1%%E4%%B9%%90%%E6%%9C%%89%%E9%%99%%90%%E5%%85%%AC%%E5%%8F%%B8,messagenumber=99; atlasdomflag=,newmore,platformlist,newmsg; RK=OI0ykRePeS; tvfe_boss_uuid=8e217558d85d95b6; pgv_pvid=3514642820; o_cookie=58254451; pgv_pvi=6615725056; pgv_si=s1087614976; gdt_refer=e.qq.com; gdt_full_refer=http%%3A%%2F%%2Fe.qq.com%%2F; gdt_original_refer=e.qq.com; gdt_original_full_refer=http%%3A%%2F%%2Fe.qq.com%%2F; tsa_pgv_ssid=tsassid__1494323148411_769062393; pgv_info=ssid=s7345288897; verifysession=h023nwRDTlh-ac9SO1dk3jxjm5fgiRQ9to7vubwqkZnjGxnONE4qNfVpiOiOaZKgwbdGx_U1mmF61Uw4gBIejrz8-eUO8ywo_99; gdt_from=02_bj_PINPAO_txhx; _qpsvr_localtk=0.8549011635540227; atlas_platform=atlas; ptui_loginuin=3259173373; pt2gguin=o3259173373; uin=o3259173373; skey=@DNU89AKxt; ptisp=cnc; ptcz=aa4ec6ebc9f89f0a5313a8ec33b0c231a3d6a5e0e3e4ca8a6aa6b2c395763395; portalversion=400; dm_cookie=version=400&log_type=internal_click&ssid=tsassid__1494323148411_769062393&pvid=3514642820&qq=3259173373&loadtime=11627&url=http%%3A%%2F%%2Fe.qq.com%%2Fads%%2F400&gdt_refer=e.qq.com&gdt_full_refer=http%%3A%%2F%%2Fe.qq.com%%2F&gdt_original_refer=e.qq.com&gdt_original_full_refer=http%%3A%%2F%%2Fe.qq.com%%2F&gdt_from=02_bj_PINPAO_txhx&uid=1353608&hottag=atlas&hottagtype=header;site_type=400;hottag=atlas;hottagtype=header','Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6' ,\
	  'Cache-Control':'max-age=0',\
	  'Connection': 'keep-alive',\
	  'Host': 'ad.toutiao.com',\
	  'Referer':'http://e.qq.com/atlas/1353608/report/order',\
	  'Upgrade-Insecure-Requests': '1',\
	  'Accpet':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
	   } 
	req = urllib2.Request(url,headers=headers) 
	response = urllib2.urlopen(req) 
	save_html(response.read())

	return response.read()

def save_html(data):
    file=open("s.html", "wb")
    file.write(data)
    file.flush()
    file.close()




def json_clac():
	jsons=spider_toutiao()
	jsons=json.loads(jsons)
	jsons=json.dumps(jsons["data"]["creative_data"])
	create_json(jsons,"test")
def create_json(word,name):
	file_object = open(os.getcwd()+'/'+name+'.json','w')
	file_object.write(word)
	file_object.close()
	print("create_json_"+name)


if __name__ == '__main__':
	spider_toutiao()
