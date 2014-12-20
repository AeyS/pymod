#coding:utf-8
class Net(object):
    '''读取网络资源
    
    通常应用于抓取阿里淘宝上面的页面数据
    
    '''
    def __init__(self):
        super(Net,self).__init__()
        self.result = ""
        self.keyword = ""
        self.ns = None
        
        
    def __reset(self,account,keyword):
        '''初始化请求资源页面'''
        if keyword != self.keyword:
            self.keyword = keyword
            from SearchKW import SearchKW
            self.ns = SearchKW(account,keyword)
            self.ns.getSearchpage()
            self.ns.getURL()
        
        
    def getkeyword(self,account,keyword):
        '''搜索关键词，进入首个宝贝链接，并获取宝贝页面的第一个价格'''
        self.__reset(account,keyword)
        self.ns.regexPrice()
        self.result = self.ns.price


    def getsource(self,account,keyword):
        '''搜索关键词，进入首个宝贝链接，并获取宝贝页面的详情页源码'''
        self.__reset(account,keyword)
        self.ns.url = self.ns.regexAnyone('data-tfs-url="(.*?)"')
        header = {'Host': 'dsc.taobaocdn.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
        self.result = self.ns.getWebPage(header)


    def wrtieDB(self,dbfile,tabname,tablist,idnext=0,keyword=0):
        '''写入sqlite数据库
                            如果不指定keyword，将自动使用搜索关键词做keyword'''
        if keyword==0: keyword = self.keyword
        from Location.DBcan import DBcan 
        db = DBcan(dbfile)
        db.newtab(tabname,tablist)
        db.write((idnext,keyword,self.result))