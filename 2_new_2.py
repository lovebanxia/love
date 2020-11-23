#coding=utf-8
#
#
# import urllib2
# import urllib

"""import random

for i in range(20):
    I_num = random.choice(i)
    print str(I_num)

list = [11,22,33,44,55,66]
randon_num = random.choice(list)

#需要爬取的网页url
url="http://www.baidu.com"

print randon_num"""

# import urllib
#
# word = {"wd":"数据联盟"}
#
# print urllib.urlencode(word)
#
# print urllib.unquote("wd=%E6%95%B0%E6%8D%AE%E8%81%94%E7%9B%9F")

#urllib2_profile:/E:/untitled2/name_file/111.txtxy2.py

# # 私密代理授权的账户
# user = "mr_mao_hacker"
# # 私密代理授权的密码
# passwd = "sffqry9r"
# # 私密代理 IP
# proxyserver = "61.158.163.130:16816"
# 
# 
# str_data = raw_input("数据：")

# import requests
# url = 'https://img.txt80.com/d/file/pic/2020/07/15/tf35l3qtzoa.jpg'
# r = requests.get(url,stream=True)
# with open('123.jpg', 'wb') as fd:
#     for chunk in r.iter_content():
#         fd.write(chunk)

# 作者：写bug的高师傅
# 链接：https://www.zhihu.com/question/63503594/answer/209790574
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# # 1. 构建一个密码管理对象，用来保存需要处理的用户名和密码
# passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# with open("test.txt","a+") as f:
# 	f.write(str_data+"\n")


# # 2. 添加账户信息，第一个参数realm是与远程服务器相关的域信息，一般没人管它都是写None，后面三个参数分别是 代理服务器、用户名、密码
# passwdmgr.add_password(None, proxyserver, user, passwd)

# # 3. 构建一个代理基础用户名/密码验证的ProxyBasicAuthHandler处理器对象，参数是创建的密码管理对象
# #   注意，这里不再使用普通ProxyHandler类了
# proxyauth_handler = urllib2.ProxyBasicAuthHandler(passwdmgr)

# # 4. 通过 build_opener()方法使用这些代理Handler对象，创建自定义opener对象，参数包括构建的 proxy_handler 和 proxyauth_handler
# opener = urllib2.build_opener(proxyauth_handler)

#需要爬取的网页url
# url="http://www.baidu.com"

# # 5. 构造Request 请求
# request = urllib2.Request(url)

# #对服务器发送请求
# response = urllib2.urlopen(request)
# # # 6. 使用自定义opener发送请求
# # response = opener.open(request)

# # 7. 打印响应内容
# print response.read()

import requests
from lxml import etree
import json
import os
# #设置的保存图片的位置
# img_gps = "E://image//"
#LOL部分皮肤
url = "https://lol.52pk.com/pifu/hero/"
#动漫壁纸
url2 = 'http://so.picasso.adesk.com/v1/search/wallpaper/resource/%E4%BA%8C%E6%AC%A1%E5%85%83?limit=300&channel=xiaomi&adult=false&first=1&order=new'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#获取80主页的源码
response = requests.get(url2,headers=headers)
text = json.loads(response.text)['res']['wallpaper']
# html =  response.content
# print html
# xpat_html = etree.HTML(html)
#获取小说的名字
# name_txt = xpat_html.xpath('//div[@class="tclist fl"]//p')

#获取80电子书首页图片的连接
# img_list = xpat_html.xpath('//div[@class="tclist fl"]/ul/li/a/img/@src')
# '//div[@class="imgbox"]//img[@class="main_img img-hover"]/@data-imgurl'
# img_list = xpat_html.xpath('//div/div/ul/li/a/img/@src')
# print "============================================="
# print img_list
# # print response.content
# print name_txt
# str_name = str(name_txt).decode("unicode-escape").encode("utf-8")
# for name in name_txt:
#link_str = str(link_list).decode("unicode-escape").encode("utf-8")
# print str_name

# img_name_list = [
# 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3628689749,205704893&fm=26&gp=0.jpg',
# 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=356173232,458438283&fm=26&gp=0.jpg',
# 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3716722949,1442086837&fm=26&gp=0.jpg',
# 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1323175818,3445142626&fm=26&gp=0.jpg']
# #对图片连接遍历，拿到每个图片
for single_img in text:
    # print single_img
    #再次向服务器发送每张图片
    #伪造报头
    print single_img['img']
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    # response_two = requests.get(single_img,headers=headers)
    # 设置的保存图片的位置
    LOL_doman = "E://LOL_doman//"
    # path = LOL_pifu + single_img.split("=")[-1][-10:]
    path = LOL_doman + single_img['id'] + '.jpg'
    #进行异常判断
    try:
        if not os.path.exists(LOL_doman):
            os.mkdir(LOL_doman)
        if not os.path.exists(path):
            # 再次向服务器发送每张图片
            response_two = requests.get(single_img['img'], headers=headers)
            with open(path,"wb") as f:
                f.write(response_two.content)
                print "图片保存成功".decode("utf-8")

        else:
            print "图片存在".decode("utf-8")
    except:
        print "保存失败".decode("utf-8")
