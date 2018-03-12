#coding=utf-8

import requests
import sys
from bs4 import BeautifulSoup as bs
import re
import time
import json
#import jieba  
#import jieba.analyse
#from urllib import parse as urlparse
from urlparse import *

site_cookies='_gat_autotrack_320917960=1; _gat_autotrack_592498438=1; _gat_autotrack_121864195=1; _ga=GA1.2.651133754.1511839161; _gid=GA1.2.943854026.1511839161; _gat_autotrack_805021092=1'
site_bcur = 'http://www.265.com'
header={'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
'Accept-Encoding': 'deflate','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'http://www.265.com/','Host': 'www.265.com' ,'Cookie' : str(site_cookies)}

"""
def extract_tags(content,topk):  
	content = content.strip()  
	tags=jieba.analyse.extract_tags(content, topK=topk) 
	return ','.join(tags)
"""
def get_keywords(urlstoget):
	r = urlparse(urlstoget)
	#print r.netloc
	header={'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)','Accept-Encoding': 'deflate','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Referer': urlstoget,'Host': r.netloc }
	try:
		resp = requests.get(urlstoget , headers=header , timeout=10 , allow_redirects=False)
		if (resp.status_code == 200 and resp.content[:3000].lower().find('<meta name="keywords"') >=0):
			content = resp.content[:3000].replace('/>','>').lower()
			if content.find('keywords')<>-1:
				soup = bs(content,"html.parser")
				#description = soup.find(attrs={"name":"description"})['content'] 
				keywords = soup.find(attrs={"name":"keywords"})['content']
				if len(keywords) >3 :
					#print keywords
					return keywords.encode('utf8')
	except requests.exceptions.ConnectionError:
		print ('Req ConnectionError')
		return 'None'
	except requests.exceptions.ReadTimeout:
		print ('Req ReadTimeout')
		return 'None'
	except requests.exceptions.ConnectTimeout:
		print ('Req ConnectTimeout')
		return 'None'
	except requests.exceptions.ChunkedEncodingError:
		print ('Req ChunkedEncodingError')
		return 'None'


def get_bad_site(urlstoclean):
	bad_site_list='linktech.cn|yiqifa.com|google.com'
	for i in bad_site_list:
		findresult=urlstoclean.find(i)
		findresultsum=findresultsum+findresult
	return findresultsum
	
#抓取关键词
#startnum=5362
#endnum=5363
#resultcount=0
timeStamp = int(time.time())
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y%m%d%H%M", timeArray)
print (otherStyleTime)
print ('Starting Web Crawler')
#target = codecs.open('265\\site_'+str(otherStyleTime)+'.txt', 'w','utf-8')
#target.write("id|question_time|title|content\n")
#target.write(u"读书有三到\n")
curl='http://www.265.com'
resp = requests.get(curl , headers=header , timeout=10) 
print (u"getting Data。。。。。")
if resp.status_code == 200:
	u=str(resp.content)
	datastart=u.find('<div  class="b-f b-Ab-f">')
	dataend=u.find('<div  class="b-f b-Bb-f">') 
	soup = bs(u[datastart:dataend],"html.parser")
	urls = soup.find_all(name='a',attrs={'href':re.compile(('.'))})
	#print soup.a.attrs
	#print soup.a.string
"""
#urls = soup.find_all('tag', {'id': 'tag id', 'class': 'tag class'})
#urls = soup.find_all('div', {'class': 'b-c-d b-f-i-h'})
#a.sting 可以获取标签内的值 
find_all() 
1. 查找标签 soup.find_all('tag') 
2. 查找文本 soup.find_all(text='text') 
3. 根据id查找 soup.find_all(id='tag id') 
4. 使用正则 soup.find_all(text=re.compile('your re')), soup.find_all(id=re.compile('your re')) 
5. 指定属性查找标签 soup.find_all('tag', {'id': 'tag id', 'class': 'tag class'})
 """

##获取265首页的列表
##------------------------------------
##抓取详细页
target = open('265\\site_'+str(otherStyleTime)+'.txt', 'w')

for i in urls:
    print (i['href'] , i.string)
    catetory=i.string.encode('utf8')
    curl=i['href'].strip()
    curl=site_bcur+curl
    print (curl)
    try:
        resp = requests.get(curl , headers=header , timeout=10)
        if resp.status_code == 200:
	        print (u"getting cateory page...")
	        u=resp.content
	        datastart=u.find('<span id="current-nav"></span>')
	        dataend=u.find('</body>')
	        soup = bs(resp.content[datastart:dataend],"html.parser")
	        urls = soup.find_all(name='a',attrs={'href':re.compile(('.'))})
	        #a.sting 可以获取标签内的值 
	        #print soup.a.attrs 显示标签属性
	        #print soup.a.string
	        for i in urls:
	                content=i['href']
	                print (u"getting site page info...")
	                if (content.find('http')<>-1 and content.find('google.com') ==-1):
	                	site_name=i.string.encode('utf8')
	                	print (i['href'] ,site_name)
	                	keywords_list=get_keywords(i['href'].strip())
	                	print (keywords_list)
	                	target.write(str(catetory)+'\t'+str(site_name)+'\t'+str(i['href'])+'\t'+str(keywords_list)+'\n')
	        #break
    except requests.exceptions.ConnectionError:
        print ('Req ConnectionError')
    except requests.exceptions.ReadTimeout:
        print ('Req ReadTimeout')
    except requests.exceptions.ConnectTimeout:
        print ('Req ConnectTimeout')
    except requests.exceptions.ChunkedEncodingError:
        print ('Req ChunkedEncodingError')
#target.close()
print(u'Writing txt完成')
