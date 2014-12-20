# coding:utf-8
'''
Created on 2014年8月27日

@author: Aey
'''
import types
import sqlite3


class XlsCan(object):
    """XlsCan是一个综合性的表格操作对象
    
        完全依赖xlrd及xlwt进行操作"""
        
    def __init__(self):
        super(XlsCan, self).__init__()
        self.book = None

    def Open(self, xls_file):
        '''打开表格
            xls_file = 表格文件路径'''
        
        from xlrd import open_workbook
        self.book = open_workbook(xls_file)

    def forsheet(self, key=''):
        '''循环表单内容
            key = 关键词'''
        
        name = self.book.sheet_names()
        i = 0
        bookdata = {}
        for sheet in self.book.sheets():
            # 循环表单
            bookdata[name[i]] = self.xlsrdAll(sheet, key)
            i += 1
        return bookdata

    def xlsrdAll(self, sheet, key=''):
        '''负责将表格数据读取出来
            sheet = 一面表格
            key = 关键词'''
        
        sheetdata = []
        if sheet.nrows > 0 and sheet.ncols > 0:
            for row in range(sheet.nrows):
                row_data = []
                # 循环行
                for col in range(0, sheet.ncols):
                    # 循环列
                    data = sheet.cell(row, col).value
                    if type(data) is types.UnicodeType:
                        data = data.replace('\n', '')
                    elif type(data) is types.FloatType:
                        data = data
                    # 过滤装置
                    if key != '':
                        try:
                            data = str(data)
                        except Exception, e:
                            print e
                        if self.handledict(data, key):
                            row_data.append(data)
                        else:
                            row_data.append('')
                    else:
                        row_data.append(data)
                sheetdata.append(row_data)
            return sheetdata

    def xlswtAll(self, sheetdata, xls_file):
        '''写入全部数据
            sheetdata = 需要写入的表格数据
            xls_file = 表哥文件路径'''
        
        from xlwt import Workbook
        w = Workbook()
        for (sheet, content) in sheetdata.items():
            print sheet
            ws = w.add_sheet(sheet)
            # 循环出列
            for col in range(0, len(content)):
                col_data = content[col]
                for row in range(0, len(col_data)):
                    row_data = col_data[row]
                    ws.write(col, row, row_data)
            ws = None
        w.save(xls_file)

    def xlswtAll2DB(self, dbfile, csql):
        '''写入全部数据到数据库
            data - 读取的表格数据'''
        
        for (sheet, content) in self.sheetdata.items():
            print sheet
            for col in range(0, len(content)):
                col_data = content[col]
                for row in range(0, len(col_data)):
                    row_data = col_data[row]
                    self.insert_sqlite(dbfile, sheet, csql, row_data)

    def handledict(self, data, key):
        '''过滤右边尾部关键词
            data = 检测数据
            key = 包含关键词
            如果不包含key返回假，否则返回真'''
        
        try:
            if key.index('|') > -1:
                key = key.split('|')
                for i in key:
                    if self.handledict(data, i):
                        return 1
                return 0
        except:
            try:
                # n = 关键词处在倒数位置
                n = len(key)
                if data.index(key) >= len(data) - 1 - n:
                    return 1
            except:
                return 0

    def insert_sqlite(self, dbfile, table, csql, row_data):
        '''写入数据库
            dbfile = 数据库文件
            table = 列表
            csql = 数据库阵列
            row_data = 表格数据'''
        
        n = len(row_data)
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        dd = '?,' * n
        dd = dd[0:-1]
        # autoincrement
        try:
            cur.execute("create table if not exists %s(%s)" % \
                        (self.table, self.csql))
            cur.execute("insert into %s values(%s)" % \
                        (self.table, dd), row_data)
            con.commit()
        except sqlite3.Error as e:
            print "An error occurred: %s", e.args[0]
        finally:
            cur.close
            con.close


def XlstoDB(xls_file, dbfile, table, csql, key='', n=0):
    '''负责将表格读取跟填写进数据库
        xls_file = 表格文件路径
        dbfile = 数据文件路径
        key = 关键词
        n   = 关键词处在倒数位置'''
    
    x = XlsCan()
    x.Open(xls_file)
    data = x.forsheet(key, n)
    x.xlswriteAll(data)
    x.xlswtAll2DB(dbfile, csql) 
    print "------ Done ------"


def XlsCopy(xls_file, new_xls_file):
    xd = XlsCan(xls_file)


def test():
    x = XlsCan()
    x.Open("D:/tmp/faxin.xls")
    sheetdata = x.forsheet('门|阀|0|5')
    x.xlswtAll(sheetdata, '../Config/database/testda.xls')
    print "ok"


if __name__ == '__main__':
    '''xls_file = "D:/Galileo_test1.xls"
    dbfile = "d:/Galileo.db"
    table = "lg"
    csql = "id integer primary key,"\
            "model text,flow float,head float,speed float,voltage float,"\
            "price float,priceALL float"
    XlstoDB(xls_file, dbfile, table, csql)
'''