import os
import sys
import time
import csv
import sys
import datetime
import subprocess
import pyocr
from PIL import Image,ImageDraw,ImageFilter,ImageEnhance
from Config import Config
import pymysql
reload(sys)
import pytesseract

global mysql_r


mysql_r = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],database=Config.mysql_conf['dbName'],password=Config.mysql_conf['password'],charset=Config.mysql_conf['charset'])


def run(name):

	cmd="cd "+str(name)+" && cd "+str(name)+" && scrapy crawl "+str(name)+""
	subprocess.call(cmd, shell=True)
	write_log_mysql(name)


def write_log_mysql(name):
	global mysql_r
	sql='insert into `spider_log` values("'+str(name)+'","'+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+'")'
	cursor=mysql_r.cursor()
	cursor.execute(sql)
	mysql_r.commit()
	cursor.close()


def binarizing(img,threshold): #input: gray image
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img



def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img


def getPixel(image,x,y,G,N):  
    L = image.getpixel((x,y))  
    if L > G:  
        L = True  
    else:  
        L = False  
  
    nearDots = 0  
    if L == (image.getpixel((x - 1,y - 1)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x - 1,y)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x - 1,y + 1)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x,y - 1)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x,y + 1)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x + 1,y - 1)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x + 1,y)) > G):  
        nearDots += 1  
    if L == (image.getpixel((x + 1,y + 1)) > G):  
        nearDots += 1  
  
    if nearDots < N:  
        return image.getpixel((x,y-1))  
    else:  
        return None  
  
 
def clearNoise(image,G,N,Z):  
    draw = ImageDraw.Draw(image)  
  
    for i in xrange(0,Z):  
        for x in xrange(1,image.size[0] - 1):  
            for y in xrange(1,image.size[1] - 1):  
                color = getPixel(image,x,y,G,N)  
                if color != None:  
                    draw.point((x,y),color)  
if __name__ == '__main__':

    run('uc')
