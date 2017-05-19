#coding:utf8
from Tkinter import *
from ScrolledText import ScrolledText
import urllib
# import requests
import urllib2
# import pygame
import re
import threading
import time

url_name = []  # 放置地址 名称
a = 1  # 代表页数


def get():
    global a  # 改变全局变量
    hd = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    url = 'http://www.budejie.com/video/' + str(a)
    varl.set('已经获取到第%s的视频' % a)
    opener = urllib2.build_opener()
    request = urllib2.Request(url, None, hd)
    result = opener.open(request).read()
    url_content = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)', re.S)  # re.S匹配换行符
    url_contents = re.findall(url_content, result)
    # for iterm in url_contents:
    #     print iterm
    url_reg = r'data-mp4="(.*?)">'
    for iterm in url_contents:
        url_items = re.findall(url_reg, iterm)
        # print url_items
        if url_items:  # 如果有视频存在，就匹配名字，如果是其他格式，则跳过
            name_reg = re.compile(r'<a .*?>(.*?)</a>', re.S)
            name_items = re.findall(name_reg, iterm)
            # print name_items
            for name, url in zip(name_items, url_items):
                url_name.append([name, url])
                print name, url
    return url_name


id = 1  # 视频个数


def write():
    global id
    while id < 10:
        url_name = get()  # 获取视频和名字
        for iterm in url_name:
            urllib.urlretrieve(iterm[1], '%s.mp4' % (iterm[0].decode('utf-8')))  # 下载
            text.insert(END, str(id) + '.' + iterm[1] + '\n' + iterm[0] + '\n')
            url_name.pop(0)  # 删除第一个元素
            id += 1
    varl.set('抓取完成')


def start():
    th = threading.Thread(target=write)
    th.start()  # 运行线程


root = Tk()
root.title = ('视频下载')
text = ScrolledText(root, font=('微软雅黑', 10))
text.grid()  # 实现布局方法
button = Button(root, text='开始爬取', font=('微软雅黑', 10), command=start)
button.grid()
varl = StringVar()  # 通过tk方法绑定一个变量

label = Label(root, font=('微软雅黑', 10), fg='red', textvariable=varl)
varl.set('熊猫已准备....')
label.grid()
root.mainloop()
