# -*- coding: utf-8 -*-

"""
GET http://mhpic.zymkcdn.com/comic/D%2F%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86%E6%8B%86%E5%88%86%E7%89%88%2F585%E8%AF%9D%2F8.jpg-zymk.middle HTTP/1.1
Host: mhpic.zymkcdn.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
Accept: image/webp,image/apng,image/*,*/*;q=0.8
Referer: http://www.zymk.cn/2/53427.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8

#http://mhpic.zymkcdn.com/comic/D%2F%E6%96%97%E7%A0%B4%E8%8B%8D%E7%A9%B9%E6%8B%86%E5%88%86%E7%89%88%2F1%E8%AF%9D%2F1.jpg-zymk.high
"""
import requests
import sys
import time
header={'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Referer': 'http://www.zymk.cn/' ,'Host': 'mhpic.zymkcdn.com'}
bo=range(90,641)
page= range(1,30)
for i in bo:
	for p in page:
		print 'Book'+str(i)+'page:' +str(p) 
		url='http://mhpic.zymkcdn.com/comic/D%2F%E6%96%97%E7%A0%B4%E8%8B%8D%E7%A9%B9%E6%8B%86%E5%88%86%E7%89%88%2F' +str(i) + '%E8%AF%9D%2F' +str(p)+ '.jpg-zymk.high'
		#print url
		#print '000'+str(i) + str('000'+str(i))[-3:]
		#校园爆笑大王漫画
		#http://mhpic.zymkcdn.com/comic/X%2F%E6%A0%A1%E5%9B%AD%E7%88%86%E7%AC%91%E5%A4%A7%E7%8E%8B%2F001%E8%AF%9D%2F10.jpg-zymk.high
		try:
			resp = requests.get(url,headers=header,timeout=10)
			if resp.status_code == 200 :
				target = open('doupo\\' +str('000'+str(i//10))[-2:]+ '0\\'+str('000'+str(i))[-3:]+ '-'+str('00'+str(p))[-2:]+'.jpg', 'wb')
				target.write(resp.content)
				target.close()
				print 'HTTP 200 done'
			else:
				break
				print 'HTTP 404'
		except requests.exceptions.ConnectionError:
			print ('Req No.',i,'ConnectionError')
		except requests.exceptions.ReadTimeout:
			print ('Req No.',i,'ReadTimeout')
		except requests.exceptions.ConnectTimeout:
			print ('Req No.',i,'ConnectTimeout')
		time.sleep(0.4)
