# coding:utf-8
from Reptile.text import regex, wlist


class Hatml():
    '''底层处理

        提供html文档基础操作部分
    '''

    def __init__(self, content):
        self.content = content.lower()
        self.resultarray = []

    def sub(self, reg, substr, content=False):
        # 正则单个替换
        if content: return regex(content, reg, 'r', substr)
        self.content = regex(self.content, reg, 'r', substr)

    def subn(self, subdict, content=False):
        # 正则多个替换
        for i in subdict:
            print '本源：%s\n替换：%s' % (i, subdict[i])
            if content: content = self.sub(i, subdict[i], content)
            else: self.sub(i, subdict[i])
        return content

    def rep(self, r, s, c=False):
        # 单个替换
        if c: return c.replace(r, s)
        self.content = self.content.replace(r,s)
        
    def repn(self, subdict, content=False):
        # 多个替换
        for i in subdict:
            if content: content = self.rep(i, subdict[i], content)
            else: self.rep(i, subdict[i])
        return content

    def add(self, content):
        # 添加内容进入结果队列
        self.resultarray.append(content)


class HanOA(Hatml):
    '''处理html文档的常规对象

        例如：图片，列表
    '''

    def picture(self, style):
        subdict = {'img src=' : 'img style="%s" src=' % style,
                '<br class=img-brk>' : ''}
        self.subn(subdict)
        self.add(self.content)

    def table(self):
        subdict = {'^\s*|\s*$' : '',
                '<table.*?>' : '<table border="1" bordercolor="#ececec" width="100%">',
                '<td style=".*?">' : '<td>'}
        self.subn(subdict)
        content = self.content
        tdls = regex(content,'<table.*?>.*?</table>', G="re.S")
        subdict = {#'<p.*[style=".*?"]{1}.*?>' : '<p>',
                '<div align=center>' : '<p>',
                '<font style="font-size: 12px">' : '',
                '</font>' : '',
                '</div>' : '</p>'}
        for x in xrange(0,len(tdls)-1):
            # 正则修改内容
            cont = self.subn(subdict, tdls[x])
            # 将获取的内容替换为新内容
            self.rep(tdls[x], cont)
            self.rep(tdls[x], ' style="text-align: center"', '')

    def ords(self):
        # 列表倒序
        i=0
        strls = self.content.split('\n')
        while len(strls) > i:
            print strls[len(strls)-i-1]
            self.add(strls[len(strls)-i-1]+'\n')
            i = i+1

    def getresult(self):
        # 获取结果
        return self.resultarray


from HTMLParser import HTMLParser

class Myparser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.result = []
    
    def append(self, arg):
        if arg not in self.result:
            self.result.append(arg)
    
    def handle_starttag(self, tag, attrs):
        if tag=="td":
            for attr in attrs:
                if attr[0]=="style":
                    self.append(attr[1])
                    
    def strsub(self, content):
        for i in self.result:
            print i
            content = content.replace(i, "")
        return content

class HanOparser(HanOA):

    def subtable(self):
        self.table()
        my = Myparser()
        my.feed(self.content)
        self.add(my.strsub(self.content))


class HanOB(HanOparser):
    '''顶层调用

        这里的每个函数都是直接产出结果的
    '''

    def hanPic(self, style=False):
        if style == False: style = "margin: 8px; width: 734px; box-shadow: #e6e6e6 0px 0px \
8px 2px; border-radius: 3px"
        self.picture(style)
        self.add(self.content)

    def hanTable(self):
        self.table()
        self.add(self.content)
        self.add('</div>')

    def hanAd(self):
        def picframe(url, src, name):
            string = '<div style="height: 192px;width: 170px;border: 1px solid #eeeeee;margin: 0 5px \
20px 5px;float: left;padding: 2px;box-shadow:1.0px 1.0px 6.0px #dddddd;"> \
<div style="height: 170px;width: 170px;overflow: hidden;"> \
<a href="%s"><img style="width: 170px;box-shadow: inset 0 -3px 3px #dddddd;" src="%s">\
</a></div><div style="height: 22px;line-height: 22px;text-indent: 5px;backgroun \
d: #fff1e0;"><a href="%s">%s</a></div></div>' % (url,src,url,name)
            return string
        subdict = {'^\s*|\s*$' : '', '\n' : '', '<p>' : '', '<u>' : '', '</u>' : '', '<font.*?>' : '', '</font>' : ''}
        self.subn(subdict)
        res = regex(self.content,'html"><img src="(.*?)"></a><br class=img-brk><a href="(.*?)">(.*?)</a></td>')
        for i in res:
            src = i[0]
            url = i[1]
            name = i[2]
            self.add(picframe(url, src, name))
        self.add('<div style="clear: both;">&nbsp;</div>')

    def hanCont(self):
        def title_bold(res, reg, subtitle=''):
            if subtitle == '':
                subtitle = 'font-weight: bold;background: red;border-radius: 50px;color: white;padding: 6px;'
            brls = regex(res, reg)
            for title in [i for i in brls if len(i) <= 25]:
                print title.decode('gb2312').encode('utf-8')
                res.replace(title, '><span style="%s"%s/span><' % (subtitle, title))
                # res = regex(res,title,'r','><span style="%s"%s/span><' % (subtitle, title))
            return res
        if self.content.find('<div style="font-size: 25px; border-top: #e9e9e9 1px solid; font-family: microsoft yahei; border-right: #dbdbdb 1px dashed; font-weight: bold; color: #4a4a4a; text-align: center; border-left: #dbdbdb 1px dashed; background-color: #efefef; box-shadow: 0 -1px 3px rgba(209, 209, 209,0.5)">')!=-1:
            # res = regex(res,'background-color: #[^#c0c0c0]\S+"|background-color: #[^#c0c0c0]\S+;|background: #[^#c0c0c0]\S+"|background: #[^#c0c0c0]\S+;','r',"background:#FFF1E0")
            subdict = {'<p.*?>' : '<p style="line-height:1.75;">'}
            content = self.subn(subdict)
            self.add(content)
        else:
            self.add('<div style="border-top: #dbdbdb 1px dashed; border-right: #dbdbdb 1px dashed; b \
order-bottom: #dbdbdb 1px dashed; color: #333333; padding-bottom: 10px; padding- \
top: 10px; padding-left: 20px; border-left: #dbdbdb 1px dashed; line-height: 20p \
x; padding-right: 20px;font-size:16px;">')
            subdict = {'style=".*?"' : '',
                    '<p.*?>' : '<p style="line-height:1.75;">',
                    '<td>' : '<td style="background-color: #ffffff">',
                    '<font.*?>' : '',
                    '</font>' : '',
            }
            self.subn(subdict)
#             self.content = title_bold(self.content,'>\d.*?<')
#             self.content = title_bold(self.content.decode('gb2312'),u'>[\u4e00|\u4e8c|\u4e09|\u56db|\u4e94|\u516d|\u4e03|\u516b|\u4e5d|\u5341]\u3001.*?<')
#             self.content = self.content.encode('gb2312')
            self.table()
            self.picture("margin: 8px; width: 734px; box-shadow: #e6e6e6 0px 0px \
8px 2px; border-radius: 3px")
            self.add(self.content)
            self.add('</div>')


def main(path,writepath):
    res=open(path,'r').read()
    print u'1.处理文本表格\n2.处理广告\n3.处理图片\n4.处理表格\n5.排序倒序\nplease:'
    n=int(raw_input())
    h = HanOB(res)
    if n==1: h.hanCont()
    elif n==2: h.hanAd()
    elif n==3: h.hanPic()
    elif n==4: h.hanTable()
    elif n==5: h.ords()
    elif n==6: h.subtable()
    wlist(h.getresult(),writepath)


if __name__ == '__main__':
    import os
    os.system('notepad D:/name.txt')
    main('D:/name.txt','D:/file_handle.txt')
    os.system('notepad D:/file_handle.txt')
