#coding:utf-8
'''
Created on 2014年8月27日

@author: Aey
'''
from xlrd import open_workbook
import sqlite3
import types
class XlstoDB(object):
    """docstring for XlstoDB"""
    def __init__(self, dbfile, table, csql):
        super(XlstoDB, self).__init__()
        self.dbfile = dbfile
        self.table = table
        self.csql = csql
        
        
    def xls2db(self,sheet,key='',n=0):
        '''负责将表格读取跟填写进数据库
            key = 关键词
            n   = 关键词处在倒数位置'''
        if sheet.nrows > 0 and sheet.ncols > 0:
            for row in range(1, sheet.nrows):
                row_data = []
                for col in range(sheet.ncols):
                    data = sheet.cell(row, col).value
                    if type(data) is types.UnicodeType: data = data.replace('\n','')
                    elif type(data) is types.FloatType: data = data
                    #过滤装置
                    if key!='':
                        if self.handledict(data,key,n): row_data.append(data)
                    else:
                        row_data.append(data)
                self.insert_sqlite(row_data,len(row_data))


    def handledict(self,data,key,n=1):
        '''过滤关键词'''
        try:
            if data.index(key)>=len(data)-n: return 1
        except:
            return 0


    def insert_sqlite(self,row_data,n):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        dd = '?,'*n
        dd = dd[0:-1]
        try:    #autoincrement
            cur.execute("create table if not exists %s(%s)" % (self.table,self.csql))
            cur.execute("insert into %s values(%s)" % (self.table,dd), row_data)
            con.commit()
        except sqlite3.Error as e:
            print "An error occurred: %s", e.args[0]
        finally:
            cur.close
            con.close

        


def main(xls_file,dbfile,table,csql,key='',n=0):
    '''负责将表格读取跟填写进数据库
        key = 关键词
        n   = 关键词处在倒数位置'''
    x2d = XlstoDB(dbfile,table,csql)
    book = open_workbook(xls_file)

    for sheet in book.sheets():
        x2d.xls2db(sheet,key,n)
    print "------ Done ------"




if __name__ == '__main__':
    xls_file = "D:/Galileo_test1.xls"
    dbfile = "d:/Galileo.db"
    table = "lg"
    csql = "id integer primary key,"\
            "model text,flow float,head float,speed float,voltage float,"\
            "price float,priceALL float"
    main(xls_file,dbfile,table,csql)