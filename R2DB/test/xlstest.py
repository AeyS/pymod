# coding:utf-8
'''
Created on 2014年8月28日

@author: lfq
'''
def addprojectpath():
    '''添加项目到系统路径'''
    import os
    import sys
    sys.path.append('../')


addprojectpath()
path = '../Config/database/testdata.xls'
# from xlwt import Workbook
# w = Workbook()
# ws = w.add_sheet("this is sheet")
# ws.write(0, 0, 'everyday  --1')
# ws2 = w.add_sheet("this is sheet2")
# ws2.write(0, 0, 'everyday  --2')
# ws3 = w.add_sheet("this is sheet3")
# ws3.write(0, 0, 'everyday  --3')
# w.save(path)


def handledict(data, key):
    '''过滤右边关键词'''
    try:
        if key.index('|') > -1:
            key = key.split('|')
            for i in key:
                if handledict(data, i):
                    return 1
            return 0
    except:
        try:
            n = len(key)
            if data.index(key) >= len(data) - 1 - n:
                return 1
        except:
            return 0

# print handledict('10', '门|阀|0|5')
from Reptile.xlsme import XlsCan
x = XlsCan()
x.Open("E:/20140905taobao/voluenewname.xls")
sheetdata = x.forsheet()
x.xlswtAll(sheetdata, '../Config/database/voluenewname.xls')
print "ok"


# from xlrd import open_workbook
# op = open_workbook(path)
# sh = len(op.sheets())
# shname = op.sheet_names()
# for i in range(0, sh):
#     print shname[i]
