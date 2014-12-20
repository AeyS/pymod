#coding:utf-8
'''
Created on 2014年7月15日

@author: aey

这里封装了对sqlite数据库的常规动作，更方便调用
'''
from Reptile import mydb


class DBcan(object):
    """docstring for Dbcan"""
    def __init__(self, dbpath):
        super(DBcan, self).__init__()
        self.dbpath = dbpath
        self.sql = mydb.Sqlite(dbpath)

    def newtab(self, tabname, sqlcommand):
        '''链接一个列表（没有则新建）
        tabname = 列表名
        sqlcommand = 命令行'''
        return self.sql.createsql(tabname, sqlcommand)

    def execute(self, sqlcommand):
        '''执行sql命令行
        sqlcommand = 命令'''
        self.sql.execute(sqlcommand)
        return self.sql.cur.fetchall()

    def like(self, column, arg):
        '''查找数据
        column = 列名
        arg = 参数'''
        return self.sql.like(column, arg)

    def write(self, sqlarg=()):
        '''写入数据
        sqlarg = 填表数据'''
        return self.sql.insert(sqlarg)

    def update(self, sqlcommand):
        return self.sql.update(sqlcommand)

    def close(self):
        '''关闭链接'''
        return self.sql.close()


def writeDB(dbfile, tabname, tablist, content=[]):
        '''写入sqlite数据库

            dbfile = 数据库文件
            tabname = 列表名
            tablist = 创建列表项
            content[] = 填写列表内容(此处一定为列表，并且按tablist的要求填写)
            '''
        # 链接数据库文件
        db = DBcan(dbfile)
        db.newtab(tabname, tablist)
        db.write(content)


def searchDB(dbfile, tabname, tablist, column, arg):
        '''读取sqlite数据库

            dbfile = 数据库文件
            tabname = 数据表名
            tablist = 创建列表项
            column = 指定数据表列名，用于指定搜索范围
            arg = 指定类似搜索关键词
            '''
        # 判断数据库文件是否存在
        import os
        if os.path.exists(dbfile):
            # 链接数据库文件
            db = DBcan(dbfile)
            db.newtab(tabname, tablist)
            return db.like(column, arg)
        else:
            return False
