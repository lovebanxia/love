#-*- coding:UTF-8 -*-
import requests,json,os
from urllib.request import urlretrieve
from threading import Thread
urls = []
names = []

#下载图像
def download(url,name):#这里就是下载图像的函数，配合多线程使用，使下载速度加倍
    print ('正在下载：%s' %name)
    if(not os.path.exists('img')):#这里是创建文件夹
        os.makedirs('img')
    #name='/img/'+str(name)+'.png'#这里就是换一个路径，下载到img下
    name='C:/Users/Administrator/Desktop/bilibiliimgtool-master/BiliPicture/img/'+str(name)+'.png'#这里就是换一个路径，下载到img下
    urlretrieve(url,name)#下载图像

def moredown():
    threads = []#这里我们使用多线程，要把这些线程放到列表里
    for i in range(len(urls)):#我们要下多少图片就开多少线程
        t =Thread(target=download(urls[i],names[i]))#把函数加到线程里面
        t.start()#开始线程
        threads.append(t)#把线程都加到列表里面，方便后面判断是否下载完毕
    for t in threads:
        t.join()#这里就是等待线程结束的代码
    print ("下载完成")

if __name__=="__main__":
    target = 'https://api.bilibili.com/x/v2/reply/v2/emojis?callback=emoji&jsonp=jsonp'
    headers = {'Referer': 'https://www.bilibili.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    req = requests.get(url=target, headers=headers)
    js = json.loads(req.text[6:-1])
    for each in js['data']['free'][0]['emojis']:
        urls.append(each['url'])
        names.append(each['id'])
    for each in js['data']['vip']:
        a = each['emojis']
        for i in a:
            urls.append(i['url'])
            names.append(i['id'])
    moredown()