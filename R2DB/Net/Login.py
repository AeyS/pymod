#coding:utf-8
'''
Created on 2014年7月17日

@author: Aey in 5号机
'''
import urllib2
import cookielib

def log(func):
    print "start"
    func()
    print "end"
    

class login(object):
    '''登陆'''
    def __init__(self,url):
        super(login,self).__init__()
        self.cj = cookielib.CookieJar()
        self.url = url

    def open(self):
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(opener)
        resp = urllib2.urlopen(self.url)
    
    def req(self,post):
        urllib2.Request(self.url,post)

    def echo(self):
        for index,cookie in enumerate(self.cj):
            print "%d=%s" % (index,cookie)
            
if __name__ == '__main__':
    lg = login('http://www.baidu.com')
    lg.req()
    lg.echo() 
    print "end"