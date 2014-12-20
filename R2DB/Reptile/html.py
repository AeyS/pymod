# coding:utf-8
'''
Created on 2014��7��15��

@author: TOM
'''
import urllib2
import os
import Reptile.text


def Browser(url, headers=''):
    if headers == '':
        Host = Reptile.text.regex(url, 'http://(\w+\.\w+\.[\w]{2,3}[\.\w]{0,3})\
            ', 's').group(1)
        print Host
        Referer = url.split("//")[1]
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,im\
                age/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Connection': 'keep-alive',
            'Host': Host,
            'Referer:http': Referer,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHT\
                ML, like Gecko) Chrome/33.0.1750.154 Safari/537.36',
        }
    req = urllib2.Request(url, None, headers)
    return urllib2.urlopen(req)


def Savepic(savepath, src=False):
    '''html.Savepic('D:/mv/',src)
            下载web图片，并且能主动过滤已下载图片'''
    if savepath[-1] != '/' and savepath[-1] != '\\':
        savepath = savepath + '/'
    if src is False:
        src = raw_input('src:')
    if src is '':
        return False
    else:
        savepath = '%s%s' % (savepath, src.split('/')[-1])
        if os.path.exists(savepath) is False:
            pic = urllib2.urlopen(src).read()
            f = open(savepath, 'wb')
            f.write(pic)
            f.close()
            print savepath
        else:
            #如果图片存在
            savepath = (savepath, True)
    return savepath


def __pic_link_big(pic_link):
    if len(pic_link.split('.')[-2]) <= 7:
        return pic_link.replace(pic_link.split('.')[-2] + '.', '')
    else:
        return pic_link


def getsrc(text, m='f'):
    '''得到图片链接
    text = 文本
    m = 匹配方式'''
    return Reptile.text.regex(text, 'src=["]{0,2}(.*?)"', m)


def select(obj):
    '''选择器：负责处理类JQuery的选择器语法
    obj = 分析对象'''
    tagname = nameattr = nameval = ''
    tagls = ('div', 'input', 'li', 'ul', 'a')
    if '.' in obj:
        nameattr = ('.', 'class')
    elif '#' in obj:
        nameattr = ('#', 'id')
    nameval = obj.split(nameattr[0])
    return nameval[0], nameattr[1], nameval[-1]


def get_attr(html, name, single=0):
    '''获取class标签
    html = 分析文本
    name = 获取语法
    single = 单个检索'''
    from bs4 import BeautifulSoup
    bs = BeautifulSoup(html)
    tagname, nameattr, nameval = select(name)
    print tagname, nameattr, nameval
    if single == 0:
        return bs.find_all(tagname, attrs={nameattr: nameval})
    else:
        return bs.find(tagname, attrs={nameattr: nameval})

def bsencode(html):
    from bs4 import BeautifulSoup
    bs = BeautifulSoup(html)