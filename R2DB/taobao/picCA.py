# coding: utf-8
'''
Created on 2014年9月9日

@author: Aeys
'''
# 常用链接数据库指令
createsql = 'id int,oldsrc text,locsrc text,newsrc text'


def src2db(savepicpath, dbpath, path):
    '''下载文本内的图片，并将图片html与本地地址路径关联写入到一个数据文件
    savepicpath = 保存图片路径
    dbpath = 数据文件路径'''
    from Reptile import text
    from Location import DBcan
    from Reptile import html
    import os
    os.system('notepad %s' % path)
    oldsrc = html.getsrc(text.fread(path))
    db = DBcan.DBcan(dbpath)
    db.newtab('srcid', createsql)
    # 为了索引id的有序排列故多一个n来计值
    n = 0
    for x in range(0, len(oldsrc)):
        locsrc = html.Savepic(savepicpath, oldsrc[x])
        if type(locsrc) != type(()):
            print n, locsrc
            db.write((n, oldsrc[x], locsrc, ''))
            n += 1
        else:
            print '图片已存在！'


def getpic(dbpath, path):
    '''bs4获取图片地址，文件名'''
    from Reptile import text
    from Reptile import html
    import os
    os.system('notepad %s' % path)
    basemsg_ls = html.get_attr(text.fread(path), 'div.base-msg')
    for basemsg in basemsg_ls:
        basemsg = basemsg.prettify()
        src = html.getsrc(str(html.get_attr(basemsg, 'div.img-container', 1)),
                          's')
        name = text.regex(str(html.get_attr(basemsg, 'div.img-name', 1)),
                          'title="(.*?)"', 's')
        updatesrc2db(dbpath, src.group(1).split('_160x160')[0], name.group(1))


def subsrc_old(dbpath, path):
    '''替换src
    dbpath = 数据文件路径'''
    from Reptile import text
    from Location import DBcan
    import os
    os.system('notepad %s' % path)
    db = DBcan.DBcan(dbpath)
    data = text.fread(path, u=True)
    db.newtab('srcid', createsql)
    n = 54
    for x in range(0, n):
        res = db.execute('select * from srcid where id=%d' % x)
        print res[0][1], res[0][3]
        exit()
        data = data.replace(res[0][1], res[0][3])
    text.fwrite(path, data, u=True)
    os.system('notepad %s' % path)


def subsrc(dbpath, path):
    '''替换src
    dbpath = 数据文件路径'''
    from Reptile import text
    from Location import DBcan
    from Reptile import html
    import os
    os.system('notepad %s' % path)
    db = DBcan.DBcan(dbpath)
    data = text.fread(path, u=True)
    srcls = html.getsrc(data)
    db.newtab('srcid', createsql)
    for i in srcls:
        res = db.execute('select * from srcid where oldsrc like "%'+i+'%"' )
        if len(res[0][3])>2:
            data = data.replace(i, res[0][3])
        else:
            print "newsrc图片链接不存在%s" % i.decode('gb2312').encode('utf-8')
    text.fwrite(path, data, u=True)
    os.system('notepad %s' % path)


def updatesrc2db(dbpath, src, name):
    '''链接数据文件匹配原图位置保存入库
    dbpath = 数据文件路径
    src = 图片地址
    name = 图片名'''
    from Location import DBcan
    db = DBcan.DBcan(dbpath)
    db.newtab('srcid', createsql)
    db.update('newsrc = "%s" where oldsrc like "%s"' %
              (src, '%'+name+'%'))


def iterates_dowpic(dbpath, dowpicpath):
    '''遍历图片src数据库，并下载缺失newsrc图片'''
    from Location import DBcan
    from Reptile import html
    db = DBcan.DBcan(dbpath)
    db.newtab('srcid', createsql)
    res = db.execute("select * from srcid where newsrc=''")
    for i in res:
        if len(i[1]) > 2:
            print i[1]
            html.Savepic(dowpicpath, i[1])
