#coding:utf-8

def addprojectpath():
    '''添加项目到系统路径'''
    import os
    import sys
    sys.path.append('../')


def test(sourcekey,keyword,nextid):
    keyword = keyword.decode("gb2312")
    sourcekey = sourcekey.decode("gb2312")
    from Net import Net
    net = Net()
    #net.getkeyword("cm79",keyword)
    net.getsource("cm79",keyword)
    print net.result
    exit()
    print "ok"
    net.writeDB(u'../Config/databaselKeyWord.db',
                'august',
                'id INTEGER PRIMARY KEY,keyword text unicode,price text unicode',
                nextid,sourcekey)
def main():
    from Reptile import text
    keyword = file("../Config/inifile/keyword.txt",'r').readlines()
    nextid = 0
    for i in keyword:
        k = i.replace("\n","")
        k = k[0:k.index('\xb3\xa9\xcf\xfa\xc6\xb7\xc5\xc6-')]
        print k.decode("gb2312")
        test(i,k,nextid)
        nextid += 1
        
def productData():
    '''
                将产品数据录入数据库
    '''
    from Location.DBcan import writeDB
    from Reptile import text
    content = (u"通用模板",u"自吸泵页头链接模板",u'''<div style="padding: 3px;margin: auto;">
    <h1>同款其他规格链接</h1>
<table style="box-shadow: 0 0 3px #999;margin: auto;border-radius: 17px;"><tbody>
    <tr><td style="padding: 5px 15px 5px 15px;margin: 0 5px 10px 0;font-size: 13px;border-right: 1px solid #ccc;">型号</td>
        <td style="padding: 10px 18px 10px 18px;margin: 0 5px 10px 0;font-size: 13px;border-right: 1px solid #ccc;"><a href="{0}" target="_blank">G125WZ / G250WZ</a></td>
        <td style="padding: 10px 18px 10px 18px;margin: 0 5px 10px 0;font-size: 13px;border-right: 1px solid #ccc;"><a href="{1}" target="_blank">G300WZ / G370WZ</a></td>
        <td style="padding: 10px 18px 10px 18px;margin: 0 5px 10px 0;font-size: 13px;border-right: 1px solid #ccc;"><a href="{2}" target="_blank">G550WZ / G750WZ</a></td>
        <td style="padding: 10px 18px 10px 18px;margin: 0 5px 10px 0;font-size: 13px;"><a href="{3}" target="_blank">G1100WZ / G1300WZ</a></td>
</tr></tbody></table>
<br>
</div>
''')
    writeDB('../Config/database/home_pump.db', 'info',
                '''"account" TEXT,
                "question" TEXT,
                "result" TEXT''',
                content)


def outtpl():
    from Location.DBcan import searchDB
    from Reptile import text
    """
    result = searchDB('../Config/database/home_pump.db', 'info',
                '''"account" TEXT,
                "question" TEXT,
                "result" TEXT''',
                "result",
                u"padding")"""

    result = searchDB('../Config/database/home_pump.db', 'gwz',
                '''"id" int,
                "model" TEXT,
                "spec" TEXT,
                "price" TEXT,
                "content" TEXT''',
                "spec",
                u"G550WZ")
    print result

addprojectpath()
from taobao import run
run.xls()