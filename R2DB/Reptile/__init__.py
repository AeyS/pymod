#coding:utf-8
__version__ = '0.12'
__license__ = 'MIT'

__all__ = ['Spider','html','olib','text']

import Spider
import text
import html,os

def savefile(path,res,name):
    """path is result savefile path,
        s is source file content,
        res is regex or bs4 filter. """
    htmlpath = '%s\\%s.html' % (path,name.replace('/' or '\\' or '*' or '?' or '|' or ':',' '))
    # print '%s\n%s' % (url,htmlpath)
    if os.path.isfile(htmlpath):
        print 'Input illegal --->    Html path already exists\n%s' % htmlpath
    else:
        # Replace Naming Violation
        print htmlpath
        f=open(htmlpath,'w')
        f.write(res.encode('gb2312'))#into is unicode output is windows encode gb2312
        f.close()

def Webpage(url,path,reg,clsid,header,enc='',test=0):
    """Webpage(url,path,reg,clsid,header,enc)

        Web crawling
        url = Web file
        path = location file
        reg = (regex / bs4)get file title
        clsid = (regex / bs4)get file content
        header = Request header"""
    def Detect(url,test):
        if test:
            print 'Now is test model!'
            return 0
        ini = 'c:/url.log'
        if os.path.isfile(ini)==False:
            filels=open(ini,'w')
            filels.close()
        filels=open(ini,'r').read()
        if filels.find(url)==-1:
            f=open(ini,'a+')
            f.write(url+'\n')
            f.close()
        else:
            return 1

    if Detect(url,test):
        print 'Input illegal --->    Url path already exists\n%s-->' % url
        exit(0)
    else:
        s = Spider.Spider(url)
        s.read(header,enc)
        res = s.peel(clsid,'bs4')
        name = text.Transcoding(text.regex(s.soc,reg,'s').group(1))
        if path=='':
            return {'result':res,'name':name}
        else:
            savefile(path,res,name)
            # s.PicSave(path,header)

def Locpage(oldpath,newpath,reg,m='f'):
    """Locpage(oldpath,newpath,reg)

    regex file content """
    return text.fwrite(newpath,text.regex(text.fread(oldpath),reg,m))