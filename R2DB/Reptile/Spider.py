#coding:utf-8
'''
Created on 2014Äê7ÔÂ15ÈÕ

@author: TOM
'''
import text
import urllib2

def urldocument(url,headers='',enc=''):
    if headers=='':
        res = urllib2.urlopen(url)
        return res.read()
    req = urllib2.Request(url,None,headers)
    retval = urllib2.urlopen(req)
    if retval.headers.has_key('content-encoding'):
        import StringIO,gzip
        fileobj = StringIO.StringIO()
        fileobj.write(retval.read())
        fileobj.seek(0)
        gzip_file = gzip.GzipFile(fileobj=fileobj)
        res = gzip_file.read()
    else:
        res = retval.read()
    retval.close()
    if enc!='': res = res.decode(enc,'ignore')
    return res

class Spider(object):
    """This is a small spider crawling the site taken
    1.     read(headers='',enc='')
            Read pages feature
    2.     peel(reg,m='f')
            Web content extraction function
    """
    def __init__(self, url=''):
        super(Spider, self).__init__()
        self.url = url
        self.res = ''
        self.restr = ''
        self.soc = ''

    def read(self,headers='',enc=''):
        """read(headers='',enc='')
                Read pages feature"""
        self.res = urldocument(self.url,headers,enc)
        self.soc = self.res

    def geturl(self,reg,m='f'):
        return text.regex(self.res,reg,m)

    def title(self,reg):
        """title(reg)
        return regex title,
        Full text search. """
        return text.regex(self.soc,reg,'s')

    def peel(self,reg,method,m='f'):
        """peel(reg,m='f')
                Web content extraction function
                if m='test' then return htmlstring
                Intercept Text Retrieval"""
        if method=='bs4':
            if '.' in reg[0] or '#' in reg[0]:
                if '.' in reg:
                    clsid = ('class','.')
                elif '#' in reg:
                    clsid = ('id','#')
                attr = reg.split(clsid[1])[0]
                name = reg.split(clsid[1])[1]
                import olib
                sr = olib.bslib(self.res)
                if attr=='': attr='div'
                print '<%s %s="%s">' % (attr,clsid[0],name)
                self.restr = sr.getattr(attr,clsid[0],name)
                if m=='test':
                    return self.res
            else:
                raise ValueError('Input illegal --->    reg: %s' % reg)
        elif method=='re':
            return text.regex(self.res,reg,m)
        return self.restr

    def PicSave(self,path,headers,Host='',m='f'):
        """PicSave(reg,Host,path,headers,m='f')
            Save crawl Web Images
        """
        import os,sys,chardet
        #Regular out of the picture address.
        imgls = text.regex(str(self.restr),'src="(.*?\.\w{3})"',m)
        for url in imgls:
            url = urllib2.quote(url)
            try:
                Host = text.regex(url,r'http://.*?/','s').group(0)
            except Exception:
                pass
            imgname = url.split('/')[-1]
            #Generate save path
            mkdir = url.replace(imgname,'')
            if 'http' in mkdir:
                location = '%s/%s' % (path,mkdir.replace(Host,''))
            else:
                location = '%s/%s' % (path,mkdir)
            if os.path.isdir(location)==False:
                print 'this is new path: '+location
                try:
                    os.makedirs(urllib2.unquote(location))
                except Exception:
                    try:
                        unicode(url)
                    except Exception:
                        coding = chardet.detect(url)
                        url = url.decode(coding['encoding'])
                    f=open('c:/errpath.log','a+')
                    f.write(self.url+'\n\timg-->'+url)
                    f.close()
                    continue
            print Host+url
            imgwb = urldocument(Host+url,headers)
            coding = chardet.detect(imgname)
            imgpath = location+imgname.decode(coding['encoding'])
            if os.path.isfile(imgpath):
                print 'Input illegal --->    Image path already exists\n\t-->%s' % imgpath
            else:
                with open(imgpath, 'wb') as jpg:
                    temp = sys.stdout
                    sys.stdout = jpg
                    print imgwb
                    sys.stdout = temp