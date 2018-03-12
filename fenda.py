# -*- coding: utf-8 -*-
"""
Created on Fri Jul 08 16:04:06 2016

@author: Administrator
"""

#抓取分答平台的相关数据

'''
#查询原生报文
GET http://fd.zaih.com/api/v1/accounts/rank?page=1&per_page=20 HTTP/1.1
Accept: */*
X-Requested-With: XMLHttpRequest
Referer: http://fd.zaih.com/leaderboard
Accept-Language: zh-CN
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko
Connection: Keep-Alive
Host: fd.zaih.com
Pragma: no-cache
Cookie: _smt_uid=577f354e.320c5a7a; _ga=GA1.2.1554336512.1467954524; _gat=1
'''

import sys
import time
import requests
import json
reload(sys)
sys.setdefaultencoding( "utf-8" )
pages=range(1,6)
#年份
timeStamp = int(time.time())
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y%m%d_%H%M", timeArray)
itemnow=0
target = open('fenda\\fd_rank_'+str(otherStyleTime)+'.txt', 'w')
site_bcur='http://fd.zaih.com/api/v1/accounts/rank?'
site_cookies='_smt_uid=577f354e.320c5a7a; _ga=GA1.2.1554336512.1467954524; _gat=1'
for pg in pages:
    #pgnum=pg[2:13]
    pgnum=pg
    print pgnum
    curl='page='+str(pgnum)+'&per_page=20'
    curl=site_bcur+curl
    print curl
    #---以上为目标URL要获取的URL地址。可以通Fiddler工具抓包获取到
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko','Content-Type': 'application/x-www-form-urlencoded','x-requested-with': 'XMLHttpRequest','Referer': 'http://fd.zaih.com/leaderboard' , 'Cookie' : str(site_cookies),'Host': 'fd.zaih.com'}
    # get 形式
    r=requests.get(curl,headers=header)
    print (u"正在获取数据。。。。。")
    u=r.text 
    #print u
    d = json.loads(u)
    accountid_ls=[]
    accountid_ls=''
    for i in range(11):
        accountid=d[i].get('id')
        accountid_ls=accountid_ls+str(accountid)+'\n'
#删除列表中的重复数据
        accountid_ls=str(accountid_ls).replace('[','')
        accountid_ls=str(accountid_ls).replace(']','')
    print accountid_ls
    itemnow=itemnow+1
    #print(u'获取数据 '+str(pg)+' '+str(itemnow)+'/'+str(len(pages))+'完成')
    #target.write(str(pg)+'@\n'+uflow +'@\n'+uflowtime+'@\n'+'[end]\n')
    target.write(str(accountid_ls))
    time.sleep(1)
target.close()
print(u'生成文件.txt完成')
    #文件写入完毕。关闭文件