# coding:utf-8
'''
Created on 2014年7月15日

@author: aey
'''


class Sqlite(object):
    """docstring for sqlite"""
    def __init__(self, dbfile):
        super(Sqlite, self).__init__()
        import sqlite3
        if '/' in dbfile:
            print dbfile
            self.conn = sqlite3.connect(dbfile)
            self.cur = self.conn.cursor()
            self.tabname = ''
        else:
            raise IOError('this is no set path,\n\t or "/" don\'t not support \
            writing!\npath: %s' % dbfile)

    def execute(self, sqlcommand, arg=0):
        if 'create' in sqlcommand:
            return self.conn.execute(sqlcommand)
        elif 'insert' in sqlcommand:
            self.conn.execute(sqlcommand, arg)
        else:
            self.conn.execute(sqlcommand)
        self.conn.commit()

    def createsql(self, tabname, sqlcommand):
        self.tabname = tabname
        self.execute('create table if not exists %s (%s)' % (tabname,
                                                             sqlcommand))

    def selectRow(self, arg):
        self.execute('select %s from %s' % (arg, self.tabname))
        return self.cur.fetchall()

    def like(self, column, arg):
        print "select * from %s where %s \
            like" % (self.tabname, column) + " '%" + arg + "%'"
        self.conn.execute("select * from %s where %s \
            like" % (self.tabname, column) + " '%" + arg + "%'")
        return self.cur.fetchall()

    def update(self, sqlcommand):
        # self.cur.execute('update hhss set info="I am rollen" where id=3')
        self.execute('update %s set %s' % (self.tabname, sqlcommand))

    def insert(self, sqlarg):
        '''
        self.execute('insert into %s values (%s)' % (self.tabname,s),sqlarg)
        '''
        s = ('?,'*len(sqlarg))[0:-1]    # ?,?,?  Sqlite placeholder
        self.execute('insert into %s values (%s)' % (self.tabname, s), sqlarg)

    def close(self):
        self.cur.close()
        self.conn.close()


class Mysql(object):
    """docstring for Mysql"""
    def __init__(self, host, user, passwd, port, charset):
        super(Mysql, self).__init__()
        import MySQLdb
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.charset = charset
        self.tablename = ''
        self.cur = ''
        self.conn = ''
        self.n = 0
        try:
            self.conn = MySQLdb.connect(host=self.host, user=self.user,
                                        passwd=self.passwd, port=self.port,
                                        charset=self.charset)
            self.cur = self.conn.cursor()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def create(self, database, tablename, sqlcommand):
        self.database = database
        self.tablename = tablename
        self.cur.execute('create database if not exists %s' % database)
        self.conn.select_db('%s' % database)
        self.cur.execute('create table if not exists \
            %s (%s)' % (tablename, sqlcommand))
        self.n = self.selectRow('max(id)')[0][0]

    def selectRow(self, arg):
        self.cur.execute('select %s from %s' % (arg, self.tablename))
        return self.cur.fetchall()

    def insert(self, sqlarg):
        s = ('?,'*len(sqlarg))[0:-1]    # ?,?,?  Sqlite placeholder
        self.cur.executemany('insert into %s \
            values(%s)' % (self.tablename, s), sqlarg)
        self.conn.commit()

    def update(self, modify_content, conditions):
        # self.cur.execute('update hhss set info="I am rollen" where id=3')
        self.cur.execute('update %s set %s where \
            %s' % (self.tablename, modify_content, conditions))

    def where(self, sqlcommand):
        self.cur.execute("select * from %s where \
            %s" % (self.tablename, sqlcommand))
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    # sql = Sqlite('d:/test.db')
    # '''//>>>>>>>>>>--------------------------v1.0-------------------------->>>>>>>>>>>'''
    # sql.execute('create table if not exists keyprice (id integer primary key,key varchar(35) UNIQUE,price integer)')
    # for t in [(0,u'\u7cd6\u679c',50),(1,u'\u5feb\u4e50',58)]:
    #     sql.execute('insert into keyprice values (?,?,?)', t)
    # sql.execute('select price from keyprice')
    # for i in sql.cur.fetchall():
    #     print i[0]
    # sql.execute("select * from keyprice where key like '%"+u'\u7cd6\u679c'+"%'")
    # for i in sql.cur.fetchall():
    #     print i,i[1]
    # '''//>>>>>>>>>>--------------------------v2.0-------------------------->>>>>>>>>>>'''
    # db = olib.Sqlite('D:/TH/taobao/jibi_content.db')
    # db.createsql('contab','id INTEGER PRIMARY KEY,txt LONGTEXT(60) UNIQUE')
    # db.insert((db.n,r))
    # db.like(column,arg)
    '''//>>>>>>>>>>--------------------------Mysql v0.5-------------------------->>>>>>>>>>>'''
    mq = Mysql('localhost','came','123',3307,'utf8')
    mq.create('test','hhss','id int,info varchar(20)')
    print mq.where('info like \'%\\am%\'')
    mq.update('info="hello yeah"','id=1')
    print mq.where('id=1')
    print mq.where('id=%d' % mq.n)
    mq.insert((mq.n+1,'this is '))
    print mq.where('id=%d' % mq.n)