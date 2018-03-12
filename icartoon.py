# -*- coding: utf-8 -*-

"""

GET http://www.icartoons.cn/webapi/web/serials.json?type=1&content_id=1S201509300200102316&sort=1 HTTP/1.1
Host: www.icartoons.cn
Connection: keep-alive
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
Referer: http://www.icartoons.cn/portal/creader.html?content_id=1S201509300200102316&set_id=1C201509301200198929
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: PHPSESSID=1769b32c25d2d72f82d642be8388ecf1; KEfax_icartoon_guid=8372dc04ee5028c74516be31e4685738; xmidcdm_cookie=77719145; DM_SID=1510491605178605c9b944a678c64f2f; KEfax_portal_type=Mx0O; KEfax_wap_style=Mx0O; Hm_lvt_a6d7644b0ab6b0d59d31d5682b6ed9a3=1510476879; Hm_lpvt_a6d7644b0ab6b0d59d31d5682b6ed9a3=1510491622

GET http://www.icartoons.cn/webapi/web/auth.json?userparam=null&set_id=1C201509301200198929&content_id=1S201509300200102316&phpsessid=null HTTP/1.1
Host: www.icartoons.cn
Connection: keep-alive
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
Referer: http://www.icartoons.cn/portal/creader.html?content_id=1S201509300200102316&set_id=1C201509301200198929
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: PHPSESSID=1769b32c25d2d72f82d642be8388ecf1; KEfax_icartoon_guid=8372dc04ee5028c74516be31e4685738; xmidcdm_cookie=77719145; DM_SID=1510491605178605c9b944a678c64f2f; KEfax_portal_type=Mx0O; KEfax_wap_style=Mx0O; 

Cookie: PHPSESSID=1769b32c25d2d72f82d642be8388ecf1; KEfax_icartoon_guid=8372dc04ee5028c74516be31e4685738; xmidcdm_cookie=77719145; 
DM_SID=1510497838803739d7ca866d1528d2db; KEfax_portal_type=Mx0O; KEfax_wap_style=Mx0O; works=0; userparam=2f1955c8-1fb1-3998-42f8-de6ca78d30d6; userid=109693553; username=%E6%BC%AB%E5%8F%8B17%E5%98%89%E5%98%89; photo=http%3A%2F%2Fimg0.icartoons.cn%2F%2Fgroup5%2FM00%2F82%2F00%2FwKgbXlmvaH2AICODAAA1YRDlhZo957.jpg; Hm_lvt_a6d7644b0ab6b0d59d31d5682b6ed9a3=1510476879; Hm_lpvt_a6d7644b0ab6b0d59d31d5682b6ed9a3=1510498196

Cookie: PHPSESSID=1769b32c25d2d72f82d642be8388ecf1; KEfax_icartoon_guid=8372dc04ee5028c74516be31e4685738; xmidcdm_cookie=77719145; 
DM_SID=1510497838803739d7ca866d1528d2db; KEfax_portal_type=Mx0O; KEfax_wap_style=Mx0O; works=0; userparam=2f1955c8-1fb1-3998-42f8-de6ca78d30d6; userid=109693553; username=%E6%BC%AB%E5%8F%8B17%E5%98%89%E5%98%89; 


"""

import requests
import sys
import time
import simplejson as json
content_idlist='1S201312260200095940'
"""
设定爱动漫网站的动画的编号
"""
def mkdir(path):
    # 引入模块
    import os 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
     # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path) 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)  
        print path+' makedirs success'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' directorys existed'
        return False 
# 定义要创建的目录
#mkpath="d:\\qttc\\web\\"
# 调用函数
#mkdir(mkpath)


userparam='2f1955c8-1fb1-3998-42f8-de6ca78d30d6'
site_cookies='PHPSESSID=1769b32c25d2d72f82d642be8388ecf1; KEfax_icartoon_guid=8372dc04ee5028c74516be31e4685738; xmidcdm_cookie=77719145; DM_SID=1510497838803739d7ca866d1528d2db; KEfax_portal_type=Mx0O; KEfax_wap_style=Mx0O; works=0; userparam='+ str(userparam)+'; userid=109693553; username=%E6%BC%AB%E5%8F%8B17%E5%98%89%E5%98%89; '

start_sortid=30
end_sortid=1000
# 为了保证程序出错后，可以重新开始，设定了开始的话数，即从大于设定的 话数开始，节省时间	
for content_id in content_idlist.split('|'):
	header={'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)','Accept-Encoding': 'deflate','Accept': 'text/html,application/xhtml+xml,appapplication/json, text/javascript, */*; q=0.01lication/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Referer': 'http://www.icartoons.cn/portal/creader.html?content_id=' +str(content_id)+ '&set_id=1C201509301200198929' ,'Host': 'www.icartoons.cn' ,'Cookie' : str(site_cookies)}
	mkdir(content_id)
	curl='http://www.icartoons.cn/webapi/web/serials.json?type=1&content_id=' +str(content_id)+ '&sort=1'
	content_resp = requests.get(curl,headers=header,timeout=10)
	#print str(content_resp.text).decode('utf')
	content_json = json.loads(content_resp.text,encoding="utf-8")
	#print content_json.keys()
	record_count=len(content_json["items"])
	#print record_count	
	for i in range(len(content_json["items"])):	
		set_id=str(content_json["items"][i]["set_id"]).decode('utf')
		sortid=content_json["items"][i]["sortid"]
		print 'set_id:'+str(set_id) +' | record_count:'+str(record_count)+' | sortid:'+str(sortid) +' | start_sortid:'+str(start_sortid)
		mkdir(str(content_id)+'\\'+str('000'+str(sortid//10))[-2:]+ '0')
		if (start_sortid<sortid and sortid<end_sortid):
			purl='http://www.icartoons.cn/webapi/web/auth.json?userparam=' +str(userparam)+'&set_id=' +set_id+'&content_id=' +content_id+'&phpsessid=null'
			pcontent_resp = requests.get(purl,headers=header,timeout=10)
			pcontent_json = json.loads(pcontent_resp.text,encoding="utf-8")
			print len(pcontent_json["items"])
			for p in range(len(pcontent_json["items"])):
				#print str(pcontent_json["items"][p]["url"]).decode('utf')
				picurl=str(pcontent_json["items"][p]["url"]).decode('utf')
				page=str(pcontent_json["items"][p]["page"]).decode('utf')
				try:
					piccontent_resp = requests.get(picurl,headers=header,timeout=10)
					if piccontent_resp.status_code == 200 :
						target = open(str(content_id)+'\\' +str('000'+str(sortid//10))[-2:]+ '0\\'+str('000'+str(sortid))[-3:]+ '-'+str(page)+'.jpg', 'wb')				
						target.write(piccontent_resp.content)
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
				time.sleep(0.1)
		#break	
	print str(content_id) +'Done'
