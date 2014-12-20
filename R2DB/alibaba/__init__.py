# coding:utf-8
'''
处理csv里的价格型号信息段，提取出价格跟型号的值填入配置文件d:/name3.txt
@author: Aey
'''
def addprojectpath():
    import os
    import sys
    sys.path.append(os.path.abspath('../'))

addprojectpath()

from Net.JsonGet import *


def xlsgetjson(obj):
    '''json获取价格及规格'''
    o = json.loads(obj)
    res = []
    for x in xrange(0,len(o)):
        res.append({'name':o[x]['specAttributes']['1234'],'price':o[x]['price']})
    return res


def getnameprice(content):
    '''得到价格名字'''
    # name = text.regex(content, r'{"{1,2}\d+"{1,2}:"{1,2}(.*?)"{1,2}}', 'f', G='re.I')
    # price = text.regex(content, r'"{1,2}price"{1,2}:(\d+.\d+),"{1,2}', 'f', G='re.I')
    loadsobj = xlsgetjson(content)
    # 将名字价格从数据对象中取出
    name = [i['name'] for i in loadsobj]
    price = [str(i['price']) for i in loadsobj]
    ini = []
    print name,price
    ini.append(','.join(name))
    ini.append(','.join(price))
    return ini


def writeini(path, keyvalue, ini):
    '''将处理好的数据存入文件'''
    content = text.fread(path)
    content = content.decode('gb2312')
    for i in content.split('\n'):
        if len(i)>10 and i[0] != '#':
            ls = i.split('=>')
            # print ls[0],keyvalue
            if ls[0] == keyvalue.decode('utf-8'):
                ls[1] = ini[0]
                ls[2] = ini[1]
                break
    res = '=>'.join(ls)
    print i.encode('utf-8'),res.encode('utf-8')
    content = content.replace(i, res)
    text.fwrite(path, content,u=True)


def ini_main():
    import os
    os.system('notepad d:/name.txt')
    content = text.fread('d:/name.txt')
    content = content.decode('gb2312')
    ini = getnameprice(content)
    writeini('d:/name3.txt', '泵', ini)
    os.system('notepad d:/name3.txt')


def main():
    import os
    os.system('notepad d:/name.txt')
    content = text.fread('d:/name.txt')
    content = content.decode('gb2312')
    js = JsonGet(content)
#     js.htmlget()
    js.getnameprice()
    js.writeini('d:/name3.txt', '泵')
    os.system('notepad d:/name3.txt')

# main()
from Reptile.AvgSort import sort_test
sort_test(60)
