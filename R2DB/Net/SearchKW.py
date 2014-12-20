#coding:utf-8
'''
Created on 2014��7��15��

@author: TOM
'''
from Reptile import text
import urllib

class SearchKW(object):
    """docstring for SearchKW"""
    def __init__(self, account, keyword):
        super(SearchKW, self).__init__()
        self.keyword = keyword
        self.account = account
        self.resoure = ''
        self.url = ''
        self.price = ''
        
    def getWebPage(self,headers=None):
        '''打开一个网页'''
        print self.url
        if headers != None:
            from Reptile import Spider
            self.resoure = Spider.urldocument(self.url, headers)
            #self.resoure = html.Browser(self.url, headers)
        else:
            self.resoure = urllib.urlopen(self.url).read()
        
    def getSearchpage(self):
        '''获取搜索结果页面
        return self.resoure
        '''
        self.url = "http://%s.1688.com/page/offerlist.htm?keywords=%s" % (self.account,urllib.quote(self.keyword.encode('gbk')))
        self.getWebPage()


    def getURL(self):
        '''获取第一个宝贝的url
        return self.url
        '''
        wb = text.regex(self.resoure,"http://detail\.1688\.com/offer/\d+.html",'s')
        self.url = wb.group()

#======================上面是基础==========================================

    def regexPrice(self):
        '''打开宝贝URL正则获取价格
        return self.price
        '''
        self.getWebPage()
        price = text.regex(self.resoure,'"price":"(\d+\.\d+)"','s')
        self.price = price.group(1)
        
        
    def regexAnyone(self,reg):
        '''打开宝贝URL正则任意内容'''
        self.getWebPage()
        regresult = text.regex(self.resoure,reg,'s')
        return regresult.group(1)
        