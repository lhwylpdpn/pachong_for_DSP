import urllib.parse
import urllib.request
import sys
import time
import datetime
import http.cookiejar
import random
import re
import os

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

def test():
	global log_txt
	global log_new
	url_choose="http://www.app12345.com/"
	webCookie = http.cookiejar.LWPCookieJar()  
	openner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(webCookie),urllib.request.HTTPHandler)
	user_agent=[]
	user_agent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50")
	user_agent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50")
	user_agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0")
	user_agent.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)")
	user_agent.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0")
	user_agent.append("Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
	user_agent.append("Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11")
	user_agent.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)")
	user_agent.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)")
	user_agent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")
	random.shuffle(user_agent)
	send_header = {'Host':url_choose,'User-Agent':user_agent[1],'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Connection':'keep-alive'}
	#urlopener.addheaders.append(('Referer', 'http://www.chinabidding.com.cn/zbw/login/login.jsp'))
	#urlopener.addheaders.append(('Accept', 'text/html, application/xhtml+xml, */*'))
	#urlopener.addheaders.append(('Accept-Encoding', 'gzip, deflate'))
	#urlopener.addheaders.append(('Accept-Language', 'zh-CN'))
	#urlopener.addheaders.append(('Host', 'www.chinabidding.com.cn'))i
	#urlopener.addheaders.append(('Connection', 'Keep-Alive'))
	urllib.request.install_opener(openner)
	imgurl="http://www.app12345.com/?area=tw&store=Apple%20Store&device=iPhone&pop_id=27&showdate=2016-1-20&showtime=10"
#获取登录验证码的请求
	#print(imgurl)
	req1 = urllib.request.Request(imgurl)
	response1=urllib.request.urlopen(req1)
	
	save_html(response1.read())

def update_config(name):
	cf=configparser.ConfigParser()
	cf.read("config.ini")
	opts2=cf.options("user/pwd")
	user=re.findall("\w+\s\_\s"+str(name),";".join(opts2))
	print(user[0])
	cf.set("user/pwd",user[0],str(cf.get("user/pwd",user[0]))+" _ [success]")
	cf.write(open("config.ini","w"))


def save_file(data):
    file=open("test_pics/test.jpg", "wb")
    file.write(data)
    file.flush()
    file.close()
def save_html(data):
    file=open("s.html", "wb")
    file.write(data)
    file.flush()
    file.close()

def save_log(data):
    file=open("log.ini", "a")
    file.write(data)
    file.close()
def save_mail(data):
    file=open("mail.ini", "a")
    file.write(data)
    file.close()
def save_successlog(data):
    file=open("successlog.ini", "a")
    file.write(data)
    file.close()
def register_all(page):
	global log_txt
	global log_new
	p=re.findall("\w+\=\"\w+\=\w+\"\>\s+\<\w+\s\w+\=\"\w+\"\s\w+\=\"\w+\"\s\w+\=\"[\u4e00-\u9fa5]+\"\s\w+\=\"\w+.__act.value=\'\w+.\w+.\w+.\w+.\w+.\w+.\w+.\w+.\w+\';\w+\s\w+\(\);\"\>",page)
	q=re.findall("onclick\=[\u4e00-\u9fa5_a-zA-Z0-9()\.\;\"\s\=\']+disabled\=\"\"\>",page)
	if len(q)>0:
		try:
			#print(p[0])
			#print(p[1])
			return str(p[0])
		except Exception as e:
			log_txt=log_txt+"6"
			print(e,"查询位置页面的时候出错了")
		


if __name__ == '__main__':
	test()


