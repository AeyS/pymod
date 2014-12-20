#coding:utf-8
'''
Created on 2014��7��15��

@author: TOM
'''
class bslib(object):
    """docstring for bslib"""
    def __init__(self, string):
        super(bslib, self).__init__()
        import bs4
        self.soup = bs4.BeautifulSoup(string)

    def prettify(self):
        return self.soup.prettify()

    def getattr(self,attr1,attr2,attr3,alls=0):
        '''self.soup.find('div',{'class':attr})
        '''
        if alls: return self.soup.html.body.findAll(attr1,{attr2:attr3})
        else: return self.soup.html.body.find(attr1,{attr2:attr3})

import HTMLParser
class Myparser(HTMLParser.HTMLParser):
    """docstring for Myparser"""
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.res = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for name,value in attrs:
                if name == 'src':
                    print value
                    self.res.append(value)

class Grabstr(object):
    """docstring for Grabstr"""
    def __init__(self, url, ):
        super(Grabstr, self).__init__()
        self.url = url
        import html
        self.source = html.Browser(self.url).read()

    def getregex(self,rege,m='f'):
        import Reptile.text
        print 'html long:%s' % len(self.source)
        return Reptile.text.regex(self.source,rege,m)


def test():
    #bslib
    soup = bslib('<div class="p"></div><div id="o"></div>')
    print soup.getid('o'),soup.getclass('p')

if __name__ == '__main__':
    test()