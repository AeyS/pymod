# coding: utf-8
'''
Created on 2014.12.17

@author: TOM
'''
from Reptile import text
import json


class JsonGet():
    def __init__(self, obj):
        self.obj = obj
        self.loadsobj = None
        self.ini = []

    def xlsget(self):
        '''获取导出的xls文档内容'''
        try:
            return [{'name':i['specAttributes']['1234'],'price':i['price']} for i in json.loads(self.obj)]
        except:
            return False
    
    def htmlget(self):
        '''获取阿里鼠标copy的名称价格'''
        rom = {'name': [],'price': []}
        c = self.obj.split('\n')
        for i in c:
            r = i.split('\t')
            if len(r)>2:
                rom['name'].append(r[0])
                try:
                    rom['price'].append(text.regex(r[1], '\d+.\d+', 's').group())
                except:
                    return False
        self.loadsobj = rom
    
    def getnameprice(self):
        '''得到价格名字'''
        if self.xlsget()==False:
            if self.htmlget()==False:
                return False
        print '读取数据:', self.loadsobj
        # 将名字价格从数据对象中取出
        name = self.loadsobj['name']
        price = self.loadsobj['price']
        print "长度：",len(name)
        self.ini.append(','.join(name))
        self.ini.append(','.join(price))
    
    def writeini(self, path, keyvalue):
        '''将处理好的数据存入文件'''
        content = text.fread(path)
        content = content.decode('gb2312')
        for i in content.split('\n'):
            if len(i)>10 and i[0] != '#':
                ls = i.split('=>')
                # print ls[0],keyvalue
                if ls[0] == keyvalue.decode('utf-8'):
                    ls[1] = self.ini[0]
                    ls[2] = self.ini[1]
                    break
        res = '=>'.join(ls)
        print i.encode('utf-8'),res.encode('utf-8')
        content = content.replace(i, res)
        text.fwrite(path, content,u=True)
