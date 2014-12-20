# coding: utf-8
'''
Created on 2014年9月21日

@author: TOM
'''


def xls():
    # 表格过滤
    from Reptile.xlsme import XlsCan
    x = XlsCan()
    x.Open("D:/tmp/faxin.xls")
    sheetdata = x.forsheet('门|阀|0|5')
    x.xlswtAll(sheetdata, '../Config/database/testda.xls')


def picCan():
    from taobao import picCA
    path = 'd:/name.txt'
    dbpath = 'd:/src_ali.db'
    dowpicpath = 'E:/20140905taobao/0909/pic/alibabapic'
    # 将图片下载，并将路径数据存入数据库
    picCA.src2db(dowpicpath, dbpath, path)
    # 得到从图片空间里的获取的图片链接
    # picCA.getpic(dbpath, path)
    # 匹配链接，替换链接
    # picCA.subsrc(dbpath, path)
    # 遍历数据库，获取缺失图片，并下载
    # picCA.iterates_dowpic(dbpath, dowpicpath)


def sort(n):
    '''标题60字重排'''
    from Reptile import AvgSort
    # 按字数计算
    # print AvgSort.sort_test(n)
    # 按列数计算
    print AvgSort.sort_column(n)


def pic_rename(path):
    '''图片乱序命名'''
    from Reptile import text
    import os
    import time
    pals = text.pathls(path, 0, '')
    import string
    n = 0
    for old in pals:
        dic = string.lowercase[n]
        new = dic+str(time.time())
        print '%s/%s' % (path, old), '%s/%s' % (path, new+old)
        os.rename('%s/%s' % (path, old), '%s/%s' % (path, new+old))
        if n < 25:
            n += 1
        else:
            n = 0
